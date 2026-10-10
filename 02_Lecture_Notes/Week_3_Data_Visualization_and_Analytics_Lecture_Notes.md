# Paul's Notes · Week 3: Health-Data Joins and Exploratory Models

[Section index](README.md) · [Editable R Markdown](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose and dependencies](#purpose-and-dependencies)
- [Dictionaries and keys before joins](#dictionaries-and-keys-before-joins)
- [Codes and analysis-specific inclusion](#codes-and-analysis-specific-inclusion)
- [Exploratory linear models](#exploratory-linear-models)
- [Figures, functions, and panels](#figures-functions-and-panels)
- [Misconceptions and self-check](#misconceptions-and-self-check)

## Purpose and dependencies

Use this reference with the [complete Week 3 lesson](../03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md). **Study time:** 30–40 minutes. **Prerequisites:** Weeks 1–2; R and dplyr >= 1.1.0. The full lesson additionally uses ggplot2. Explain joining populations, analytic inclusion, and exploratory model limits.

## Dictionaries and keys before joins

A dictionary states field meaning, types, units, codes, and missing conventions. Serum albumin (g/dL) and creatinine (mg/dL) are biomarker concentrations; age is years; a kidney-health response is self-reported information. A self-report is not a diagnosis. Character identifiers preserve formatting; row position is not a stable key.

```r
if (!requireNamespace("dplyr", quietly = TRUE) || utils::packageVersion("dplyr") < "1.1.0") {
  stop("Need dplyr >= 1.1.0")
}
reference_profile <- data.frame(Subject_ID = c("T01", "T02", "T03"), Age = c(29, 48, 65))
reference_lab <- data.frame(Subject_ID = c("T01", "T03", "T04"), Creatinine = c(0.8, 1.2, 0.9))
stopifnot(!anyDuplicated(reference_profile$Subject_ID), !anyDuplicated(reference_lab$Subject_ID))
reference_inner <- dplyr::inner_join(reference_profile, reference_lab, by = "Subject_ID", relationship = "one-to-one")
reference_left <- dplyr::left_join(reference_profile, reference_lab, by = "Subject_ID", relationship = "one-to-one")
stopifnot(nrow(reference_inner) == 2L, nrow(reference_left) == 3L)
print(dplyr::anti_join(reference_lab, reference_profile, by = "Subject_ID"))
```

**Expected:** two inner matches, three left rows, and T04 in the unmatched-laboratory audit. An inner join restricts to matched keys; a left join retains its left population; a full join retains the union. Cardinality declares permitted matching multiplicity. A duplicate can multiply records; declare and check the intended relationship rather than silently deduplicating conflicting values.

## Codes and analysis-specific inclusion

```r
reference_codes <- c(1L, 2L, 7L, 9L, NA_integer_)
stopifnot(all(reference_codes[!is.na(reference_codes)] %in% c(1L, 2L, 7L, 9L)))
reference_response <- factor(reference_codes, levels = c(1L, 2L, 7L, 9L),
  labels = c("Reported yes", "Reported no", "Refused", "Unsure"))
print(table(reference_response, useNA = "ifany"))
```

**Expected:** one of each toy response and one missing field. These codes apply only to the invented example. Refusal, uncertainty, a missing field, and an absent joined record carry different information. Audit dictionary codes before factor conversion or an unknown code may silently become NA.

Define inclusion for the specific analysis. An age–creatinine model needs those two finite fields, not complete information in every unrelated column. Report total, included, and excluded counts; complete cases alone do not solve informative missingness.

## Exploratory linear models

```r
reference_model_data <- data.frame(Age = c(25, 35, 45, 55, 65, 75),
  Creatinine = c(0.75, 0.92, 0.89, 1.11, 1.09, 1.28))
reference_fit <- lm(Creatinine ~ Age, data = reference_model_data, na.action = na.fail)
print(coef(reference_fit))
stopifnot(nobs(reference_fit) == 6L, coef(reference_fit)["Age"] > 0)
```

**Expected:** six modeled observations and a positive fitted slope, computed from these invented values. Its unit is mg/dL per year. The intercept predicts age zero outside the observed range. A mean-response confidence band differs from an individual prediction interval. R-squared is sample fit, not causal strength or predictive validation.

Residual-versus-fitted plots can flag curvature and changing spread. Normal Q-Q plots compare residual shape to a normal reference. Neither establishes independent sampling, eliminates confounding, or diagnoses disease. A repeated-visit design needs methods that account for dependence.

## Figures, functions, and panels

Histograms show bins, densities smooth shape, and ECDFs give the proportion at or below a value. Violin width represents a density scaling choice; it is not automatically a count. Boxes summarize middle values under a plotting convention; they do not define clinical boundaries. Scatter plots preserve the pair of measurements on each subject.

A plotting function should validate requested numeric fields, finite values, and unit labels, and return measured/excluded counts. Name imported file lists so outputs can be traced back to inputs. A multi-panel figure needs a scientific question and separate denominator for every panel. The full lesson demonstrates a 58-measurement distribution beside a 57-pair association; its caption explains the difference.

## Misconceptions and self-check

Predict join sizes before running them, detect a duplicate key, decode the toy responses, and state the fields defining your model sample. Explain slope units, residual axes, and why a pleasing violin or fitted line is not biological evidence. Use the full tutorial for CSV import, complete audits, diagnostics, functions, multi-panel construction, and practice.

[Previous topic](Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) · [Next topic](Week_4_Introduction_to_Bash_Lecture_Notes.md) · [Topic index](README.md) · [dplyr joins](https://dplyr.tidyverse.org/reference/mutate-joins.html) · [R linear models](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html)
