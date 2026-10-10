# Paul's Notes · Week 3: Data Visualization and Analytics

[Section index](README.md) · [Editable R Markdown](Week_3_Group_Work_Narrative_Walkthrough.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

This study guide connects invented workshop records, interprets coded feedback, and models simulated production times.

**Study time:** 90–120 minutes. **Prerequisites:** Weeks 1–2 object checks, missingness, reshaping, and plot axes. **Dependencies:** base R and `dplyr` (version 1.1.0 or newer for explicit join relationships). Run blocks in order in a clean session.

## On this page

- [Learning objectives and setup](#learning-objectives-and-setup)
- [1. Relational tables and unique identifiers](#1-relational-tables-and-unique-identifiers)
- [2. Inner and left joins, cardinality, and missingness](#2-inner-and-left-joins-cardinality-and-missingness)
- [3. Coded feedback and nonresponse](#3-coded-feedback-and-nonresponse)
- [4. Simulate a relationship transparently](#4-simulate-a-relationship-transparently)
- [5. Frequency, density, and cumulative views](#5-frequency-density-and-cumulative-views)
- [6. Regression, units, and legitimate conclusions](#6-regression-units-and-legitimate-conclusions)
- [7. Assumptions and diagnostic views](#7-assumptions-and-diagnostic-views)
- [8. Reusable functions and iteration](#8-reusable-functions-and-iteration)
- [9. Reproducible reporting](#9-reproducible-reporting)
- [Common mistakes and debugging](#common-mistakes-and-debugging)
- [Independent practice](#independent-practice)
- [Teach-back and summary](#teach-back-and-summary)
- [Ready to move on](#ready-to-move-on)
- [Next steps and references](#next-steps-and-references)

## Learning objectives and setup

You will define row units and keys, choose joins intentionally, detect row multiplication, separate nonresponse from valid categories, read cumulative distributions, interpret a linear model cautiously, and validate reusable plotting functions.

```r
if (!requireNamespace("dplyr", quietly = TRUE)) stop("Install dplyr in your own R library")
if (utils::packageVersion("dplyr") < "1.1.0") stop("This lesson needs dplyr >= 1.1.0")
```

**Expected:** no output in a compatible environment. Check `packageVersion("dplyr")` if `relationship` is reported as unused. The lesson does not install or update shared packages automatically.

## 1. Relational tables and unique identifiers

Each table must have a clear row meaning. One table records a workshop visitor; a second records at most one feedback response per visitor. A key identifies that row. Matching row positions is unsafe because rows may be reordered or absent.

```r
visitors <- data.frame(
  visitor = c("vA", "vB", "vC", "vD", "vE", "vF"),
  bench = c("oak", "elm", "oak", "elm", "oak", "elm"),
  sessions = c(1L, 2L, 1L, 3L, 2L, 4L)
)
feedback <- data.frame(
  visitor = c("vA", "vB", "vD", "vF", "vZ"),
  clarity_code = c(1L, 2L, 9L, 3L, 2L)
)
stopifnot(!anyNA(visitors$visitor), !anyDuplicated(visitors$visitor))
stopifnot(!anyNA(feedback$visitor), !anyDuplicated(feedback$visitor))
print(dim(visitors))
print(dim(feedback))
```

**Expected:** visitors has six rows and three columns; feedback has five rows and two columns. `vZ` has feedback but no visitor record. Missing keys and duplicate keys need resolution before claiming a one-to-one join.

## 2. Inner and left joins, cardinality, and missingness

An inner join keeps matched keys only. A left join keeps every row of its left input and adds matching fields from the right. It may introduce missing fields when there is no match. Cardinality describes how many rows may match on each side: one-to-one, one-to-many, or many-to-many.

```r
matched_feedback <- dplyr::inner_join(visitors, feedback, by = "visitor", relationship = "one-to-one")
all_visitors <- dplyr::left_join(visitors, feedback, by = "visitor", relationship = "one-to-one")
print(all_visitors)
stopifnot(nrow(matched_feedback) == 4L, nrow(all_visitors) == 6L)
stopifnot(sum(is.na(all_visitors$clarity_code)) == 2L)
stopifnot(identical(all_visitors$visitor[is.na(all_visitors$clarity_code)], c("vC", "vE")))
stopifnot(identical(dplyr::anti_join(feedback, visitors, by = "visitor")$visitor, "vZ"))
```

**Expected:** four matched visitors. The left join keeps all six, with missing feedback fields for `vC` and `vE`. `vZ` appears in the unmatched-right audit, not in the left result. Before removing missing rows, distinguish unavailable feedback from an import error or a failed key match.

Duplicate keys can multiply rows rather than merely fill a column. Explicit relationship checks turn unintended duplication into an error. Multiple feedback events may be valid, but then the row unit and aggregation plan must change.

```r
feedback_repeated <- rbind(feedback, feedback[1, ])
relationship_error <- tryCatch(
  dplyr::left_join(visitors, feedback_repeated, by = "visitor", relationship = "one-to-one"),
  error = function(e) conditionMessage(e)
)
stopifnot(is.character(relationship_error), length(relationship_error) == 1L)
expanded_visitors <- dplyr::left_join(visitors, feedback_repeated, by = "visitor", relationship = "one-to-many")
stopifnot(nrow(expanded_visitors) == 7L)
```

**Observable behavior:** the one-to-one declaration rejects the repeated key; allowing one-to-many produces seven rows because `vA` now has two matches. Do not apply `distinct()` indiscriminately: conflicting responses require a documented decision, not arbitrary deletion. For joins with missing keys, decide whether missing-to-missing matches are sensible; dplyr's `na_matches = "never"` can prevent them.

## 3. Coded feedback and nonresponse

Codes need a codebook. Here `1`, `2`, and `3` mean low, medium, and high clarity. Code `9` means declined to answer. Missing after the join means no matching response. Neither nonresponse condition is a numerical rating of nine or zero.

```r
known_codes <- c(1L, 2L, 3L, 9L)
observed_codes <- all_visitors$clarity_code[!is.na(all_visitors$clarity_code)]
stopifnot(all(observed_codes %in% known_codes))
all_visitors$response_state <- ifelse(
  is.na(all_visitors$clarity_code), "no matched response",
  ifelse(all_visitors$clarity_code == 9L, "declined", "rated")
)
all_visitors$clarity <- factor(
  all_visitors$clarity_code, levels = c(1L, 2L, 3L),
  labels = c("low", "medium", "high"), ordered = TRUE
)
print(table(all_visitors$response_state))
clarity_frequency <- table(all_visitors$clarity)
print(clarity_frequency)
print(cumsum(clarity_frequency))
stopifnot(sum(all_visitors$response_state == "rated") == 3L)
stopifnot(sum(is.na(all_visitors$clarity)) == 3L)
stopifnot(identical(as.integer(clarity_frequency), c(1L, 1L, 1L)))
```

**Expected:** three rated responses, one declined, and two unmatched. Low, medium, and high each have count one; cumulative counts are `1, 2, 3`. The rated-response denominator is three, while the visitor denominator is six. Report both when describing response coverage. Ordered factors support ordered displays, but do not imply equally spaced numerical scores. Averaging raw category codes is not automatically meaningful.

## 4. Simulate a relationship transparently

A simulation specifies a mechanism before drawing values. This one makes time increase with the number of items, plus independent normal noise. The seed reproduces the example, and the generating slope is known because we chose it.

```r
set.seed(4308)
item_count <- rep(seq(4, 22, by = 2), each = 3)
assembly_runs <- data.frame(
  run = sprintf("a%02d", seq_along(item_count)),
  items = item_count,
  minutes = 6 + 1.4 * item_count + rnorm(length(item_count), mean = 0, sd = 2)
)
stopifnot(nrow(assembly_runs) == 30L, !anyDuplicated(assembly_runs$run))
stopifnot(is.numeric(assembly_runs$minutes), !anyNA(assembly_runs))
print(range(assembly_runs$items))
```

**Expected:** 30 unique runs, numeric times with no missing values, and item counts from `4` to `22`. The intercept is six minutes and the generating slope is 1.4 minutes per item. The fitted estimates below need not equal those generating values because the sample has noise. This is not observed evidence about a real production line.

## 5. Frequency, density, and cumulative views

A histogram counts observations within intervals. A density estimate smooths the distribution and has area approximately one; density height is not the probability at an exact point. An empirical cumulative distribution function (ECDF) instead reports the fraction of observations at or below a threshold.

```r
assembly_hist <- hist(assembly_runs$minutes, breaks = 6, probability = TRUE,
                      main = "30 simulated assembly runs", xlab = "Assembly time (min)",
                      ylab = "Density (per min)", col = "grey85")
lines(density(assembly_runs$minutes), col = "navy", lwd = 2)
stopifnot(sum(assembly_hist$counts) == 30L)
assembly_ecdf <- ecdf(assembly_runs$minutes)
plot(assembly_ecdf, main = "Cumulative assembly times", xlab = "Assembly time (min)",
     ylab = "Fraction of runs at or below time", verticals = TRUE)
print(assembly_ecdf(30))
stopifnot(assembly_ecdf(30) == mean(assembly_runs$minutes <= 30))
```

**Histogram and density:** the horizontal axis is minutes and the vertical axis is density per minute. With unequal-width bins, compare areas rather than heights; this density-scaled histogram supports a density overlay. Kernel bandwidth changes smoothing, and smooth tails may extend beyond the observed range. Thirty simulated runs are insufficient to establish a real-world distribution.

**ECDF:** the horizontal axis is minutes; the vertical axis ranges from zero to one. At 30 minutes it gives exactly the observed fraction of runs with times at most 30. Steps represent accumulated observations, not abrupt changes in an underlying population probability. This view avoids selecting histogram bins.

## 6. Regression, units, and legitimate conclusions

Linear regression summarizes a conditional mean relationship. In this simple model, the outcome is minutes and the predictor is item count. The fitted slope has units of minutes per additional item.

```r
assembly_model <- lm(minutes ~ items, data = assembly_runs)
print(round(coef(assembly_model), 3))
print(summary(assembly_model)$r.squared)
plot(assembly_runs$items, assembly_runs$minutes,
     xlab = "Items in run (count)", ylab = "Assembly time (min)",
     main = "Synthetic item count and assembly time", pch = 19)
abline(assembly_model, col = "firebrick", lwd = 2)
stopifnot(nobs(assembly_model) == 30L)
stopifnot(identical(names(coef(assembly_model)), c("(Intercept)", "items")))
stopifnot(abs(coef(assembly_model)["items"] - 1.4) < 0.3)
```

**Expected behavior:** 30 observations used and a fitted slope near the generating value 1.4, within 0.3 in this seeded example. The intercept predicts time at zero items, outside the simulated range; do not claim it was observed. R-squared describes the share of sample outcome variation explained by this fitted linear relationship, not causal strength or external accuracy.

**Scatter plot:** the horizontal axis counts items and the vertical axis measures minutes. The line shows the fitted mean trend, not each run's exact duration. The association was built into the simulation. An association in observational data could arise from confounding, selection, measurement error, or reverse causation; regression alone does not establish causality. Extrapolation beyond 4–22 items needs additional justification.

## 7. Assumptions and diagnostic views

Check the study design before reading diagnostics. Ordinary least squares interpretation relies on an appropriate mean relationship; familiar standard errors additionally assume independent errors with constant variance. Normal errors support exact small-sample tests and intervals. A fitted line or a large R-squared does not verify those conditions.

```r
plot(fitted(assembly_model), resid(assembly_model),
     xlab = "Fitted assembly time (min)", ylab = "Residual (min)",
     main = "Residuals versus fitted values", pch = 19)
abline(h = 0, lty = 2)
qqnorm(resid(assembly_model), main = "Normal Q-Q view of residuals")
qqline(resid(assembly_model), col = "firebrick")
stopifnot(length(resid(assembly_model)) == 30L)
```

**Residual plot:** horizontal values are model-fitted minutes; vertical values are observed minus fitted minutes. Look for curvature, a widening spread, or unusual points. A structure-free cloud would be compatible with the simple specification, not proof of correctness or independence.

**Q-Q plot:** the horizontal axis contains theoretical normal quantiles; the vertical axis contains ordered residuals in minutes. Departures from the reference line flag shape or tail differences. With 30 runs it is a limited diagnostic. Neither plot can reveal unrecorded dependence or fix a flawed sampling design; influential points and repeated measurements need their own checks.

## 8. Reusable functions and iteration

A plotting function should state required columns, reject malformed inputs, count usable rows, and label units. This function returns a small reporting record as well as drawing the plot, so later code can use the checks rather than scraping printed output.

```r
plot_run_table <- function(tbl, label) {
  if (!is.character(label) || length(label) != 1L ||
      is.na(label) || !nzchar(label)) stop("label must be one nonempty string")
  if (!is.data.frame(tbl) || !all(c("items", "minutes") %in% names(tbl))) {
    stop("table needs items and minutes columns")
  }
  if (!is.numeric(tbl$items) || !is.numeric(tbl$minutes)) stop("plot columns must be numeric")
  valid <- is.finite(tbl$items) & is.finite(tbl$minutes)
  if (sum(valid) < 3L) stop("need at least three finite pairs")
  observed <- tbl[valid, c("items", "minutes"), drop = FALSE]
  plot(observed$items, observed$minutes, main = label,
       xlab = "Items in run (count)", ylab = "Assembly time (min)", pch = 19)
  return(list(label = label, measured = nrow(observed), excluded = sum(!valid)))
}
run_tables <- list(first_half = assembly_runs[1:15, ], second_half = assembly_runs[16:30, ])
plot_records <- lapply(names(run_tables), function(nm) plot_run_table(run_tables[[nm]], nm))
print(vapply(plot_records, function(record) record$measured, integer(1)))
invalid_table_error <- tryCatch(plot_run_table(data.frame(items = 1:4), "bad table"),
                               error = function(e) conditionMessage(e))
stopifnot(identical(vapply(plot_records, function(record) record$measured, integer(1)), c(15L, 15L)))
stopifnot(identical(invalid_table_error, "table needs items and minutes columns"))
with_gap <- assembly_runs
with_gap$minutes[1] <- NA_real_
gap_record <- plot_run_table(with_gap, "One unavailable timing")
stopifnot(gap_record$measured == 29L, gap_record$excluded == 1L)
```

**Expected:** two returned measured counts of `15`; malformed input yields the caught validation message; the missing-value example reports 29 usable pairs and one exclusion. Each generated plot uses item count horizontally and minutes vertically. Splitting a table for demonstration does not create independent replications or evidence of different mechanisms. `lapply()` returns one result per table; `vapply()` checks the requested return type while collecting counts.

## 9. Reproducible reporting

A useful report includes the simulation mechanism, seed, input row unit, join decisions, exclusions, plot definitions, model formula, units, and software versions. Compute numeric results directly from the analysis objects so the report describes its actual run.

```r
analysis_record <- list(
  observations = nobs(assembly_model),
  slope_minutes_per_item = unname(coef(assembly_model)["items"]),
  seed = 4308L,
  r_version = R.version.string,
  dplyr_version = as.character(utils::packageVersion("dplyr"))
)
print(analysis_record)
stopifnot(analysis_record$observations == 30L)
```

**Expected:** a 30-observation record with the fitted slope and your installed software versions. Different environments may change presentation; check structure and tolerances rather than assuming all printed digits are portable. No lesson output needs to be committed as a dataset.

## Common mistakes and debugging

- **A join unexpectedly adds rows:** inspect duplicate keys and the declared relationship on both sides.
- **Many fields become missing:** check key formatting and unmatched keys before assuming nonresponse.
- **A response code is treated as a measurement:** consult the codebook and separate valid categories from declined and unmatched cases.
- **Density height called probability:** probability corresponds to area over an interval, not a point's height.
- **A slope has no units:** identify outcome units per predictor unit and state the observed range.
- **An association called causal:** discuss the design and alternative explanations.
- **A function silently drops values:** return usable and excluded counts, and reject invalid schemas early.

## Independent practice

1. Add a seventh visitor without feedback and a feedback record with no matching visitor. Predict inner/left sizes and audit unmatched keys before running joins.
2. Change one code to an undocumented value. Add a validation rule that rejects unknown codes rather than silently treating them as normal nonresponse.
3. Generate a second time dataset with noise that increases with item count. Describe the expected residual-plot pattern before fitting it.
4. Add a minimum distinct-item requirement to `plot_run_table()`. Test constant predictors, text columns, and all-missing pairs.
5. Compare histogram and ECDF statements about the same threshold. Identify which statement depends on bin choices.

## Teach-back and summary

What defines join cardinality? How do unmatched rows differ from a declined response? Why can a density exceed one? What does a slope mean when both axes have units? Which regression assumptions cannot be checked from residual plots alone?

The sequence is **define keys → audit joins → decode missingness → simulate explicitly → read distributions → fit and diagnose → report with validated functions**. Every graph needs units, a denominator, and a conclusion that stays within the design.

## Ready to move on

Prepare a reproducible script and short methods note covering input keys, join type, unmatched records, codebook, exclusions, distribution views, model formula, units, and diagnostic limits. Keep validation results alongside the plots.

| Evidence | Completion check |
| --- | --- |
| Relational data | Demonstrate the 4-row inner and 6-row left joins; detect the repeated key before accepting row multiplication |
| Codebook and missingness | Separate 3 ratings, 1 declined response, and 2 unmatched records; reject undocumented codes |
| Model and graphics | Use 30 simulated runs; interpret minutes per item, observed range, residuals, and Q-Q axes |
| Reuse and reporting | Return measured/excluded counts from a checked function; handle bad inputs and report software versions |

## Next steps and references

[Previous: Week 2](Week_2_Group_Work_Narrative_Walkthrough.md) · [Weekly lessons](README.md) · [Analytics topic companion](../02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) · [Next: Week 4](Week_4_Bash_and_Reproducible_Workflows_Study_Guide.md) · [R function sheet](../06_RESOURCES/R/EASY_FUNCTION_SHEET.md) · [Paul's Notes](../README.md)

References: [dplyr join documentation](https://dplyr.tidyverse.org/reference/mutate-joins.html) and [R linear-model documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html). See installed help `?ecdf` and `?density`.
