# Paul's Notes · Week 2: Participant Data, Reshaping, and Graphs

[Section index](README.md) · [Editable R Markdown](Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose and dependencies](#purpose-and-dependencies)
- [Simulation parameters and scientific limits](#simulation-parameters-and-scientific-limits)
- [Missingness, derived fields, and factors](#missingness-derived-fields-and-factors)
- [Wide and long are layouts, not new participants](#wide-and-long-are-layouts-not-new-participants)
- [Choosing and reading a graph](#choosing-and-reading-a-graph)
- [Misconceptions and self-check](#misconceptions-and-self-check)

## Purpose and dependencies

Use this reference with the [complete Week 2 lesson](../03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md). **Study time:** 30–40 minutes. **Prerequisites:** Week 1; R and tidyr for the examples below. The full lesson also uses dplyr and ggplot2. Explain the participant key, measurement units, and repeated-observation structure.

## Simulation parameters and scientific limits

A pseudorandom seed controls a compatible generator's starting state. Sample size determines the number of draws; distribution parameters describe a mechanism, not exact sample moments. A normal generator is unbounded. Clipping creates boundary piles; rejection samples within a bound and changes the resulting distribution. None of these choices validates a clinical model.

```r
set.seed(77201)
reference_WBC <- runif(8, min = 4.8, max = 9.6)
set.seed(77201)
stopifnot(identical(reference_WBC, runif(8, 4.8, 9.6)))
stopifnot(length(reference_WBC) == 8L, all(reference_WBC >= 4.8 & reference_WBC <= 9.6))
print(round(reference_WBC, 2))
```

**Expected:** eight repeatable invented WBC values in 10^9 cells/L. Uniform limits are chosen for practice and are not a laboratory reference interval. RBC is commonly expressed in 10^12 cells/L; do not combine the two fields into one unqualified numeric axis.

## Missingness, derived fields, and factors

Participant identifiers remain stable across visits. Factors encode categories with declared levels. A derived category must follow the source measurement's creation and missingness decision; an unknown value must stay unknown. A simulation-centre split is not a diagnostic cutoff.

```r
reference_WBC[3] <- NA_real_
reference_status <- factor(ifelse(is.na(reference_WBC), "Missing", "Observed"),
                           levels = c("Observed", "Missing"))
print(table(reference_status))
stopifnot(sum(reference_status == "Observed") == 7L)
```

**Expected:** seven observed, one missing of eight. Available-case means need this denominator. A separate reason field, if known, provides information that NA alone cannot.

## Wide and long are layouts, not new participants

```r
if (!requireNamespace("tidyr", quietly = TRUE)) stop("Install tidyr in your own R library")
reference_wide <- data.frame(Participant_ID = c("Q01", "Q02", "Q03"),
                             WBC_Baseline = c(6.1, 7.2, 5.9), WBC_FollowUp = c(6.4, NA, 6.0))
reference_long <- tidyr::pivot_longer(reference_wide, tidyr::starts_with("WBC_"),
  names_to = "Visit", names_prefix = "WBC_", values_to = "WBC_Count")
stopifnot(nrow(reference_long) == 6L, !anyDuplicated(reference_long[c("Participant_ID", "Visit")]))
reference_recovered <- tidyr::pivot_wider(reference_long, names_from = Visit,
  names_prefix = "WBC_", values_from = WBC_Count)
stopifnot(isTRUE(all.equal(as.data.frame(reference_recovered), reference_wide, check.attributes = FALSE)))
print(reference_long)
```

**Expected:** six participant–visit rows for three people; one missing measurement; unchanged values after recovery. The compound key is Participant_ID plus Visit. Visit-specific fields belong to measurements, not participant-level identifiers. Duplicate keys can produce list-columns in `pivot_wider()`.

## Choosing and reading a graph

| Graph | Reading rule and limitation |
| --- | --- |
| Histogram | Bars count measured observations in bins; bin choice changes appearance |
| Density | A smoothed distribution with approximately unit area; height is not probability at a point |
| Scatter | Each point pairs two fields on one observation unit; association is not causation |
| Box with points | Shows center/spread and individual observations; tiny groups give unstable summaries |
| Repeated-visit display | Link the same participant across visits; rows remain dependent |

In ggplot2, data define observations, `aes()` maps fields to visual properties, and a geometry specifies marks. Label axes with the precise field and unit. Summaries need total, measured, and missing counts. Repeated visits are paired because of participant identity, not because rows happen to be adjacent. Complete-pair changes and available-case visit means can use different subsets.

## Misconceptions and self-check

Reproduce a seeded sample, explain its bounds, preserve missingness in a derived variable, and reverse a pivot without changing values. Explain why six long rows above are not six people, and why a density curve or a visually separated group does not establish clinical significance. The full lesson supplies labeled graphs, paired changes, debugging, and independent exercises.

[Previous topic](Week_1_Introduction_to_R_Lecture_Notes.md) · [Next topic](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) · [Topic index](README.md) · [tidyr pivots](https://tidyr.tidyverse.org/reference/pivot_longer.html)
