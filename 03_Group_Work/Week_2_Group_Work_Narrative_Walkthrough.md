# Paul's Notes · Week 2: Participant Measurements and Visualization

[Section index](README.md) · [Editable R Markdown](Week_2_Group_Work_Narrative_Walkthrough.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

Simulate an adult participant table with red and white blood-cell measurements, then reshape repeated visits and interpret graphs. All people, values, and sampling mechanisms are invented. The simulation teaches data structure; it is not a clinical reference population or a diagnostic model.

**Study time:** 100–140 minutes. **Prerequisites:** Week 1 objects, indexing, factors, and missingness. **Dependencies:** R, tidyr, dplyr, ggplot2. Run blocks in order in a fresh session.

[Previous: Week 1](Week_1_Group_Work_Narrative_Walkthrough.md) · [Weekly index](README.md) · [Topic companion](../02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) · [Next: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md)

## On this page

- [Learning objectives](#learning-objectives)
- [Scientific motivation and data dictionary](#scientific-motivation-and-data-dictionary)
- [1. Check dependencies and define a bounded generator](#1-check-dependencies-and-define-a-bounded-generator)
- [2. Construct reproducible participant observations](#2-construct-reproducible-participant-observations)
- [3. Missing measurements and derived categories](#3-missing-measurements-and-derived-categories)
- [4. Wide and long repeated visits](#4-wide-and-long-repeated-visits)
- [5. Group summaries and denominators](#5-group-summaries-and-denominators)
- [6. Histogram, density, and scatter plots](#6-histogram-density-and-scatter-plots)
- [7. Paired observations and interpretation](#7-paired-observations-and-interpretation)
- [Common mistakes and debugging](#common-mistakes-and-debugging)
- [Independent practice](#independent-practice)
- [Ready to move on](#ready-to-move-on)
- [Further learning](#further-learning)
- [Weekly Learning Objectives & Mastery Assessment](#weekly-learning-objectives--mastery-assessment)

## Learning objectives

Simulate reproducible participant measurements; validate IDs, types, ranges, and factors; derive categories without erasing missingness; pivot wide/long tables and recover values; summarize denominators; draw histograms, densities, scatter and grouped plots; distinguish repeated observations from independent participants.

## Scientific motivation and data dictionary

A participant may provide multiple specimens or attend several visits. A study's row count depends on its layout. A valid summary therefore needs both the measurement units and the number of contributing participants.

| Field | Meaning in this simulation |
| --- | --- |
| Participant_ID | Unique invented adult participant; one row per baseline participant |
| Age | Integer years, sampled uniformly from 20–75 |
| Sex | Fictional recorded female/male category, sampled independently; this simplified field is not a model of sex or gender diversity |
| RBC_Count | Red blood cells, in 10^12 cells/L (equivalent to millions/µL) |
| WBC_Count | White blood cells, in 10^9 cells/L (equivalent to thousands/µL) |
| Visit | Baseline or FollowUp in the repeated-measurement example |
| Measurement_Status | Observed or Missing for the selected measurement |

Cell-count units follow standard laboratory reporting conventions; see [MedlinePlus RBC](https://medlineplus.gov/ency/article/003644.htm) and [WBC](https://medlineplus.gov/ency/article/003643.htm) background. The simulation bounds below are chosen for plausible-scale practice, **not diagnostic thresholds or reference intervals**. Laboratory interpretation depends on the population, specimen, method, and clinical context.

## 1. Check dependencies and define a bounded generator

```r
needed_packages <- c("tidyr", "dplyr", "ggplot2")
unavailable <- needed_packages[!vapply(needed_packages, requireNamespace, logical(1), quietly = TRUE)]
if (length(unavailable)) stop("Install in your own R library: ", paste(unavailable, collapse = ", "))
bounded_normal <- function(n, centre, spread, lower, upper) {
  if (length(n) != 1L || !is.finite(n) || n < 1 || n != floor(n)) stop("n must be a positive integer")
  if (!all(is.finite(c(centre, spread, lower, upper))) || spread <= 0 || lower >= upper) {
    stop("Need finite parameters, positive spread, and ordered bounds")
  }
  values <- numeric(0)
  for (attempt in seq_len(1000L)) {
    batch <- rnorm(max(20L, n), mean = centre, sd = spread)
    values <- c(values, batch[batch >= lower & batch <= upper])
    if (length(values) >= n) return(values[seq_len(n)])
  }
  stop("Bounds rejected too many draws; reconsider the generator")
}
```

**Expected:** no output when dependencies are available. Install them separately with `install.packages(c("tidyr", "dplyr", "ggplot2"))`. The function rejects draws outside bounds rather than changing them into boundary values. Its attempt limit avoids an endless loop for impractical parameters.

Clipping with `pmax(lower, pmin(upper, x))` creates piles at boundaries; rejection samples conditionally inside the interval. Neither method creates empirical biological validity. The centre/spread describe the original normal generator; truncation changes its resulting moments.

## 2. Construct reproducible participant observations

```r
simulate_cohort <- function(seed) {
  set.seed(seed)
  n <- 36L
  data.frame(
    Participant_ID = sprintf("B%03d", seq_len(n)),
    Age = sample(20:75, n, replace = TRUE),
    Sex = factor(sample(c("Female", "Male"), n, replace = TRUE), levels = c("Female", "Male")),
    RBC_Count = bounded_normal(n, 4.8, 0.4, 3.6, 6.2),
    WBC_Count = bounded_normal(n, 7, 1.5, 3.5, 12)
  )
}
participants <- simulate_cohort(68104L)
stopifnot(identical(participants, simulate_cohort(68104L)))
stopifnot(nrow(participants) == 36L, !anyDuplicated(participants$Participant_ID))
stopifnot(all(participants$Age >= 20 & participants$Age <= 75))
stopifnot(all(participants$RBC_Count >= 3.6 & participants$RBC_Count <= 6.2))
stopifnot(all(participants$WBC_Count >= 3.5 & participants$WBC_Count <= 12))
print(head(participants))
print(round(c(RBC_mean = mean(participants$RBC_Count), WBC_mean = mean(participants$WBC_Count)), 3))
```

**Expected:** 36 unique participants, documented numeric ranges, two declared Sex levels, and identical repeated generation with the same seed. Printed means are computed by your run; they need not equal 4.8 and 7. The generator has no age or sex effects and samples the two counts independently. An apparent correlation or category difference is random variation here, not biological evidence.

A pseudorandom seed fixes a starting state for a compatible generator. Changing the number or order of random draws changes subsequent values. Larger samples stabilize a specified mechanism; they do not repair an unrealistic mechanism or sampling bias.

## 3. Missing measurements and derived categories

```r
participants$RBC_Count[c(4, 27)] <- NA_real_
participants$Measurement_Status <- factor(
  ifelse(is.na(participants$RBC_Count), "Missing", "Observed"),
  levels = c("Observed", "Missing")
)
participants$RBC_Band <- factor(
  ifelse(is.na(participants$RBC_Count), NA_character_,
         ifelse(participants$RBC_Count < 4.8, "Below simulation centre", "At/above simulation centre")),
  levels = c("Below simulation centre", "At/above simulation centre")
)
print(table(participants$Measurement_Status))
print(table(participants$RBC_Band, useNA = "ifany"))
stopifnot(sum(is.na(participants$RBC_Count)) == 2L, sum(is.na(participants$RBC_Band)) == 2L)
```

**Expected:** 34 observed and two missing RBC values; band counts total 34 known plus two unknown. The 4.8 split describes a chosen simulation centre, not low/high clinical status. Derive categories after their source values exist and missingness has been assigned. A missing value must not be classified as an ordinary category. In real data, record the reason for missingness when known instead of inferring it from NA.

## 4. Wide and long repeated visits

Use a separate small deterministic table to see every value. One wide row is a participant with two visits; one long row is a participant–visit measurement.

```r
visits_wide <- data.frame(
  Participant_ID = sprintf("V%02d", 1:6),
  Sex = factor(c("Female", "Male", "Female", "Male", "Female", "Male")),
  RBC_Baseline = c(4.4, 5.1, 4.8, 5.5, 4.7, 5.0),
  RBC_FollowUp = c(4.5, 5.0, NA, 5.2, 4.8, 5.1)
)
stopifnot(!anyDuplicated(visits_wide$Participant_ID))
visits_long <- tidyr::pivot_longer(visits_wide, cols = c(RBC_Baseline, RBC_FollowUp),
                                  names_to = "Visit", names_prefix = "RBC_", values_to = "RBC_Count")
visits_long$Visit <- factor(visits_long$Visit, levels = c("Baseline", "FollowUp"))
visits_long$Measurement_Status <- ifelse(is.na(visits_long$RBC_Count), "Missing", "Observed")
print(visits_long)
stopifnot(nrow(visits_long) == 12L, sum(is.na(visits_long$RBC_Count)) == 1L)
stopifnot(!anyDuplicated(visits_long[c("Participant_ID", "Visit")]))
```

**Expected:** 12 rows, six unique participants, and one unavailable follow-up. The key is Participant_ID plus Visit. Repeating an identifier is appropriate in long form; repeating that compound key would require investigation.

```r
recovered <- tidyr::pivot_wider(visits_long[c("Participant_ID", "Sex", "Visit", "RBC_Count")],
                                names_from = Visit, names_prefix = "RBC_", values_from = RBC_Count)
recovered <- recovered[match(visits_wide$Participant_ID, recovered$Participant_ID), names(visits_wide)]
stopifnot(nrow(recovered) == 6L)
stopifnot(isTRUE(all.equal(as.data.frame(recovered), visits_wide, check.attributes = FALSE)))
```

**Expected:** the original six participants and values, including NA, are recovered. Exclude the visit-specific status field from the participant identifier set when widening; otherwise it can split one participant into several rows. Verify values and keys, not only row count. Duplicate combinations can create list-columns instead of a single numeric value.

## 5. Group summaries and denominators

```r
visit_summary <- dplyr::summarise(dplyr::group_by(visits_long, Visit),
  n_total = dplyr::n(), n_measured = sum(!is.na(RBC_Count)), n_missing = sum(is.na(RBC_Count)),
  mean_RBC = if (all(is.na(RBC_Count))) NA_real_ else mean(RBC_Count, na.rm = TRUE), .groups = "drop")
print(visit_summary)
stopifnot(identical(visit_summary$n_total, c(6L, 6L)))
stopifnot(identical(visit_summary$n_measured, c(6L, 5L)))
stopifnot(isTRUE(all.equal(visit_summary$mean_RBC, c(29.5/6, 4.92))))
```

**Expected:** baseline uses six measurements, mean about 4.917; follow-up uses five, mean 4.92, in 10^12 cells/L. These available-case means compare different contributing sets. Report total, measured, and missing counts; an entirely unavailable group should return NA, not a misleading zero.

## 6. Histogram, density, and scatter plots

Exclude unavailable values explicitly and preserve the exclusion count. A histogram summarizes bins; density estimates smooth shape; scatter compares two numeric fields from the same participant.

```r
observed_RBC <- participants[!is.na(participants$RBC_Count), ]
stopifnot(nrow(observed_RBC) == 34L)
print(ggplot2::ggplot(observed_RBC, ggplot2::aes(RBC_Count)) +
  ggplot2::geom_histogram(binwidth = 0.2, boundary = 0, fill = "steelblue", colour = "white") +
  ggplot2::labs(title = "Synthetic baseline RBC: 34 measured of 36 participants",
                x = "RBC count (10^12 cells/L)", y = "Measured participants") + ggplot2::theme_minimal())
```

**Histogram check:** 34 measured participants, with bin width 0.2 in the stated RBC units.

```r
print(ggplot2::ggplot(observed_RBC, ggplot2::aes(RBC_Count)) +
  ggplot2::geom_density(fill = "lightblue", alpha = 0.5) +
  ggplot2::labs(x = "RBC count (10^12 cells/L)", y = "Density (per 10^12 cells/L)",
                title = "Smoothed synthetic RBC distribution") + ggplot2::theme_minimal())
print(ggplot2::ggplot(observed_RBC, ggplot2::aes(Age, RBC_Count, colour = Sex)) +
  ggplot2::geom_point() + ggplot2::labs(x = "Age (years)", y = "RBC count (10^12 cells/L)",
    title = "No age or sex effect was built into this simulation") + ggplot2::theme_minimal())
```

**Expected:** three figures based on 34 observed participants. Histogram bars count participants within intervals. A density curve has approximately unit area; its height is not a point probability, and bandwidth changes smoothness. It may extend beyond generator bounds. Each scatter point pairs one participant's age with RBC count; colors show recorded categories, not causal groups.

```r
observed_visits <- visits_long[!is.na(visits_long$RBC_Count), ]
print(ggplot2::ggplot(observed_visits, ggplot2::aes(Visit, RBC_Count)) +
  ggplot2::geom_boxplot(width = 0.4, outlier.shape = NA) +
  ggplot2::geom_line(ggplot2::aes(group = Participant_ID), alpha = 0.4) +
  ggplot2::geom_point() + ggplot2::labs(x = "Visit", y = "RBC count (10^12 cells/L)",
    title = "Six invented participants; 11 observed participant-visits") + ggplot2::theme_minimal())
```

**Expected:** six baseline and five follow-up points. Lines link repeated observations from the same participant; the participant with no follow-up has one point. With tiny samples, boxes are unstable; inspect individual values. The display does not establish an intervention effect.

## 7. Paired observations and interpretation

```r
complete_pairs <- complete.cases(visits_wide[c("RBC_Baseline", "RBC_FollowUp")])
paired_changes <- with(visits_wide[complete_pairs, ], RBC_FollowUp - RBC_Baseline)
print(paired_changes)
print(mean(paired_changes))
stopifnot(sum(complete_pairs) == 5L)
stopifnot(isTRUE(all.equal(paired_changes, c(0.1, -0.1, -0.3, 0.1, 0.1))))
stopifnot(isTRUE(all.equal(mean(paired_changes), -0.02)))
```

**Expected:** five paired changes, average −0.02 in 10^12 cells/L. This compares within-person changes among complete pairs. Treating their ten measurements as independent ignores pairing. A paired test would assess participant differences under its assumptions; independent-group tests require independently sampled groups. Neither test makes missing follow-up ignorable. This small fixed exercise is descriptive and does not demonstrate clinical improvement or harm.

## Common mistakes and debugging

| Symptom | Check and repair |
| --- | --- |
| Function unavailable | Run dependency checks; use the correct package namespace |
| Many boundary values | Determine whether values were clipped instead of rejection-sampled |
| Missing value assigned a band | Define missingness before categories and test NA explicitly |
| Pivot creates list-columns | Audit the participant–visit key before widening |
| Too many wide rows | Remove visit-specific fields from identifier columns |
| Plot drops rows silently | Select observed values explicitly and report exclusions |
| 12 rows called 12 people | Count unique participant identifiers as well as measurements |

## Independent practice

1. Simulate 50 adults with a new seed and document units, bounds, IDs, and the absence or presence of programmed associations.
2. Add three unavailable WBC values and derive a clearly labeled nonclinical simulation category. Count unknown values separately.
3. Add a third visit to the deterministic table. Predict long rows, validate the compound key, and recover wide values.
4. Vary histogram bins and density bandwidth. Explain which features are stable and which are display-dependent.
5. Remove a follow-up deliberately and compare available-case visit means with complete-pair changes. Explain their denominators.

## Ready to move on

| Evidence | Mastery check |
| --- | --- |
| Simulation | Reproduce 36 unique participants; explain parameters, bounds, units, and synthetic limitations |
| Missingness | Account for 34 measured RBC values and two unavailable values |
| Reshaping | Recover six participants from 12 participant–visit rows without changing values |
| Figures | Explain histogram, density, scatter, and paired display axes and denominators |
| Design | Identify five complete pairs and interpret −0.02 as a descriptive within-pair mean change |

Keep the seed, data dictionary, script, summaries, labeled figures, and an explanation of selection. Rerun in a clean session.

## Further learning

[Previous: Week 1](Week_1_Group_Work_Narrative_Walkthrough.md) · [Next: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md) · [Plot reading](../06_RESOURCES/READING_PLOTS.md) · [Paul's Notes](../README.md)

References: [tidyr pivots](https://tidyr.tidyverse.org/reference/pivot_longer.html), [ggplot2 density](https://ggplot2.tidyverse.org/reference/geom_density.html), and installed R help `?rnorm`, `?set.seed`, `?t.test`.

## Weekly Learning Objectives & Mastery Assessment

Use a new seed and an independently invented participant/visit table. These criteria assess the public study guide, not an official assignment.

| Measurable objective | Evidence of competency | Independent mastery criterion |
| --- | --- | --- |
| Generate reproducible synthetic measurements | Generator settings, seed, dictionary, unique IDs, and range checks | A fresh session recreates identical values; explain the bounds and why they are not clinical reference intervals |
| Preserve unknown measurements during transformation | A derived simulation category and a table of total, measured, and missing counts | All rows reconcile; missing measurements remain unknown rather than becoming a clinical classification |
| Reshape repeated observations reversibly | Wide and long tables with participant–visit key checks | Recover original values and participants without list-columns or duplicate key multiplication |
| Choose and interpret visual encodings | Histogram, density, scatter, and repeated-visit plot with units and denominators | Explain each row unit, every exclusion, and how bins or smoothing influence the display |
| Separate paired changes from independent observations | A complete-pair table, difference calculation, and missing-follow-up explanation | Reconcile the pair count, compute changes within participants, and explain why repeated rows are not additional independent people |

**Mastery decision:** meet every criterion on fresh synthetic inputs, rerun in a clean session, and explain results without relying on the lesson's fixed numeric answers. Retain the seed, dictionary, code, checks, figures, and a brief limitations note. Rework any unmet criterion before advancing.


### Fresh paired-observation checkpoint

Predict how many complete pairs remain in this newly invented participant table and the mean within-participant change. Values are synthetic assay units and do not establish a treatment effect.

```r
mastery_visits <- data.frame(id = c("fresh01", "fresh02", "fresh03"),
                            before = c(4, 7, NA_real_), after = c(5, 9, 8))
stopifnot(!anyDuplicated(mastery_visits$id))
mastery_pairs <- mastery_visits[complete.cases(mastery_visits), ]
mastery_change <- mastery_pairs$after - mastery_pairs$before
print(c(pairs = nrow(mastery_pairs), mean_change = mean(mastery_change)))
stopifnot(nrow(mastery_pairs) == 2, identical(mastery_change, c(1, 2)),
          mean(mastery_change) == 1.5)
```

**Expected checkpoint:** 2 complete pairs; changes 1 and 2 assay units; mean change 1.5 units. Explain why subtracting two means computed on different participant sets gives a different answer. Diagnose a duplicated participant identifier before reshaping and show how a unique-key check detects it. Make a new table with a different missing visit, predict which pairs remain, and repeat the reasoning. Review [the repeated-measurement topic guide](../02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md).
