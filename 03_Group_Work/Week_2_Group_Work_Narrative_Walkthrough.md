# Paul's Notes · Week 2: Data Wrangling and Visualization

[Section index](README.md) · [Editable R Markdown](Week_2_Group_Work_Narrative_Walkthrough.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The weekly teaching guides provide synthetic inputs and expected results; see each source for dependencies and execution checks.

A public study guide with independent synthetic examples, not an official Dartmouth or Geisel lesson. We simulate packing-station timings in seconds. They are invented values for learning, not empirical or clinical findings; no course datasets are required.

**Study time:** 90–120 minutes. **Prerequisites:** Week 1 vectors, data frames, factors, and missingness. **Dependencies:** R plus `tidyr`, `dplyr`, and `ggplot2`. Run blocks in order in a clean session. The reading edition includes expected results but does not execute R.

## On this page

- [Learning objectives and setup](#learning-objectives-and-setup)
- [1. A reproducible simulated population of observations](#1-a-reproducible-simulated-population-of-observations)
- [2. Clipping is not truncated sampling](#2-clipping-is-not-truncated-sampling)
- [3. Derived categories and missing-value summaries](#3-derived-categories-and-missing-value-summaries)
- [4. Wide and long tables describe the same repeated readings](#4-wide-and-long-tables-describe-the-same-repeated-readings)
- [5. Grouped summaries need explicit denominators](#5-grouped-summaries-need-explicit-denominators)
- [6. Three plots answer different questions](#6-three-plots-answer-different-questions)
- [7. Paired and independent comparisons](#7-paired-and-independent-comparisons)
- [Common mistakes and debugging](#common-mistakes-and-debugging)
- [Independent practice](#independent-practice)
- [Teach-back and summary](#teach-back-and-summary)
- [Next steps and references](#next-steps-and-references)

## Learning objectives and setup

You will explain reproducible random draws, derive ordered categories, reshape repeated observations without losing identifiers, summarize denominators, create three kinds of graph, and distinguish paired comparisons from independent-group inference.

```r
needed_packages <- c("tidyr", "dplyr", "ggplot2")
unavailable <- needed_packages[!vapply(needed_packages, requireNamespace, logical(1), quietly = TRUE)]
if (length(unavailable)) stop(paste("Install these packages in your own R library:", paste(unavailable, collapse = ", ")))
```

**Expected:** no output if the three packages are available. If not, use `install.packages(c("tidyr", "dplyr", "ggplot2"))` in your own R environment, then rerun this check. The lesson never installs packages automatically. Namespaced calls such as `tidyr::pivot_longer()` show which package supplies a function.

## 1. A reproducible simulated population of observations

A random-number seed fixes the generator's starting state. It makes a specified sequence reproducible in a compatible R environment; it does not make simulated values real. Changing the number or order of random draws changes later values, even if the seed stays the same.

```r
set.seed(8216)
station_seconds <- rnorm(48, mean = 85, sd = 9)
set.seed(8216)
repeat_seconds <- rnorm(48, mean = 85, sd = 9)
stopifnot(identical(station_seconds, repeat_seconds), length(station_seconds) == 48L)
station_sample <- data.frame(
  station = sprintf("p%02d", seq_along(station_seconds)),
  lane = factor(rep(c("north", "south"), each = 24), levels = c("north", "south")),
  seconds = station_seconds
)
print(round(c(sample_mean = mean(station_seconds), sample_sd = sd(station_seconds)), 2))
```

**Observable behavior:** 48 numeric draws, two lanes of 24 unique station identifiers, and identical repeated draws. The sample mean and sample standard deviation are near the generating values `85` and `9`, not guaranteed equal to them. Normal-distribution parameters describe the generator; sample size controls how many observations are drawn. Normal draws have unbounded support, so they are not automatically suitable for quantities that must be positive.

Increasing sample size usually stabilizes estimates of the generating distribution; it does not repair a badly chosen distribution or an incorrect design. The lane labels here were assigned without a simulated lane effect. Any lane difference is random variation in this construction.

## 2. Clipping is not truncated sampling

Clipping replaces values below a boundary with the boundary. It creates a pile of identical values at that boundary. A truncated distribution instead samples conditional on being inside the allowed range: out-of-range draws are rejected and replaced.

```r
illustrative_draws <- c(-2, -0.5, 0.4, 1.8)
clipped_draws <- pmax(illustrative_draws, 0)
print(clipped_draws)
set.seed(9123)
positive_draws <- numeric(0)
while (length(positive_draws) < 48L) {
  batch <- rnorm(80, mean = 1, sd = 1)
  positive_draws <- c(positive_draws, batch[batch > 0])
}
positive_draws <- positive_draws[seq_len(48L)]
stopifnot(identical(clipped_draws, c(0, 0, 0.4, 1.8)))
stopifnot(length(positive_draws) == 48L, all(positive_draws > 0))
```

**Expected:** clipping produces `0, 0, 0.4, 1.8`; rejection yields 48 strictly positive draws and no replacement zeros. Rejecting negative draws changes the distribution's mean and spread: the parameters of the untruncated normal are not the resulting truncated sample's moments. This simple loop is reasonable for this acceptance rate; specialized sampling is preferable for extreme truncation.

## 3. Derived categories and missing-value summaries

A threshold translates a numeric measurement into a category. Choose and document it before interpreting differences; do not optimize a cutoff after seeing an attractive plot. Categorization loses within-category information.

```r
station_sample$pace <- factor(
  ifelse(station_sample$seconds < 85, "under target", "at or over target"),
  levels = c("under target", "at or over target")
)
station_sample$seconds[c(5, 32)] <- NA_real_
# Derive categories again after deliberately marking two measurements missing.
station_sample$pace <- factor(
  ifelse(station_sample$seconds < 85, "under target", "at or over target"),
  levels = c("under target", "at or over target")
)
print(table(station_sample$pace, useNA = "ifany"))
stopifnot(sum(is.na(station_sample$seconds)) == 2L)
stopifnot(sum(is.na(station_sample$pace)) == 2L)
stopifnot(identical(levels(station_sample$pace), c("under target", "at or over target")))
```

**Expected:** category counts total 46 known timings plus two unknown categories. An unknown timing must not become an ordinary "slow" or "fast" category. Factor levels set the display order and remain present even if a category has no observations.

## 4. Wide and long tables describe the same repeated readings

Wide data have separate columns for repeated measurements. Long data put the measurement label in one column and the value in another. Neither representation is universally best. A reshape should change layout, not identifiers, values, or the meaning of one observation.

```r
packing_wide <- data.frame(
  station = c("p01", "p02", "p03", "p04", "p05", "p06"),
  lane = factor(c("north", "north", "north", "south", "south", "south")),
  before_s = c(84, 91, 88, 95, 87, 90),
  after_s = c(80, 86, NA, 92, 82, 89)
)
stopifnot(!anyDuplicated(packing_wide$station))
packing_long <- tidyr::pivot_longer(
  packing_wide, cols = c(before_s, after_s),
  names_to = "occasion", values_to = "seconds"
)
packing_long$occasion <- factor(packing_long$occasion, levels = c("before_s", "after_s"))
print(packing_long)
stopifnot(nrow(packing_long) == 12L, sum(is.na(packing_long$seconds)) == 1L)
stopifnot(!anyDuplicated(packing_long[c("station", "occasion")]))
```

**Expected:** twelve rows: one per station and occasion. `p03` has `88` before and `NA` after. The row key is now the combination of station and occasion; station alone appropriately repeats. `values_drop_na` is not used: keeping the missing row preserves the intended observation structure.

```r
packing_again <- tidyr::pivot_wider(
  packing_long, id_cols = c(station, lane),
  names_from = occasion, values_from = seconds
)
stopifnot(nrow(packing_again) == 6L)
stopifnot(identical(packing_again$station, packing_wide$station))
stopifnot(isTRUE(all.equal(packing_again$before_s, packing_wide$before_s)))
stopifnot(isTRUE(all.equal(packing_again$after_s, packing_wide$after_s)))
```

**Expected:** six rows with the original before/after values and missingness. If widening produces list columns, check for duplicate station–occasion keys. Do not silently average duplicates: first determine whether they are legitimate repeated observations or a data error.

## 5. Grouped summaries need explicit denominators

A mean without an available count can conceal missing observations. Summarize total, available, and unavailable counts alongside mean and standard deviation. A group's standard deviation needs at least two measured values.

```r
lane_summary <- dplyr::summarise(
  dplyr::group_by(packing_long, lane, occasion),
  rows = dplyr::n(),
  measured = sum(!is.na(seconds)),
  missing = sum(is.na(seconds)),
  mean_s = mean(seconds, na.rm = TRUE),
  sd_s = sd(seconds, na.rm = TRUE),
  .groups = "drop"
)
print(lane_summary)
stopifnot(nrow(lane_summary) == 4L, sum(lane_summary$measured) == 11L)
stopifnot(isTRUE(all.equal(lane_summary$mean_s, c(263/3, 83, 272/3, 263/3))))
```

**Expected:** four lane–occasion groups. North before has mean `87.67` from three readings, north after `83` from two; south before `90.67` and after `87.67`, each from three. `.groups = "drop"` avoids accidentally carrying grouping into later operations. These descriptive differences are not evidence of an intervention effect.

## 6. Three plots answer different questions

All plotted timings below are synthetic. The code explicitly excludes missing values so the denominator is clear.

```r
known_timings <- station_sample[!is.na(station_sample$seconds), ]
timing_histogram <- ggplot2::ggplot(known_timings, ggplot2::aes(x = seconds)) +
  ggplot2::geom_histogram(binwidth = 5, boundary = 0, colour = "white", fill = "steelblue") +
  ggplot2::labs(title = "46 simulated station timings", x = "Packing time (s)", y = "Stations")
print(timing_histogram)
paired_timings <- packing_wide[complete.cases(packing_wide[c("before_s", "after_s")]), ]
paired_scatter <- ggplot2::ggplot(paired_timings, ggplot2::aes(x = before_s, y = after_s, colour = lane)) +
  ggplot2::geom_point(size = 3) +
  ggplot2::geom_abline(slope = 1, intercept = 0, linetype = "dashed") +
  ggplot2::coord_equal() +
  ggplot2::labs(x = "Before timing (s)", y = "After timing (s)", colour = "Lane")
print(paired_scatter)
stopifnot(nrow(known_timings) == 46L, nrow(paired_timings) == 5L)
```

**Histogram:** the horizontal axis is time in seconds; the vertical axis counts stations in five-second bins. It shows simulated spread and concentration, not a clinical distribution. Changing bin width changes apparent smoothness.

**Scatter plot:** each point is one of five stations with both readings. The horizontal axis is before time and the vertical axis is after time. The dashed equality line marks no change; all five points are below it, showing lower after times in this invented set. Colour identifies lane through a legend. Equal coordinate scaling makes distance from equality interpretable, but the plot alone does not establish a cause.

```r
known_repeats <- packing_long[!is.na(packing_long$seconds), ]
repeat_boxplot <- ggplot2::ggplot(known_repeats, ggplot2::aes(x = occasion, y = seconds, fill = occasion)) +
  ggplot2::geom_boxplot(outlier.shape = NA, width = 0.45) +
  ggplot2::geom_jitter(width = 0.06, height = 0, size = 2) +
  ggplot2::labs(x = "Measurement occasion", y = "Packing time (s)", fill = "Occasion")
print(repeat_boxplot)
stopifnot(nrow(known_repeats) == 11L)
```

**Box plot:** the horizontal axis identifies occasion; the vertical axis is seconds. Boxes summarize medians and quartiles, while jitter exposes the small number of readings. Horizontal jitter separates overlaps and is not another measurement. The groups have six before and five after readings; their boxes do not display pairing or a matched comparison. Colour or fill belongs inside `aes()` when it maps data to a legend; a fixed style belongs outside `aes()`.

## 7. Paired and independent comparisons

Paired readings come from the same station. Analyze within-station differences, not twelve supposedly independent rows. An independent-group comparison instead requires distinct independent observational units in each group. This distinction follows the design, not the appearance of the table.

```r
change_s <- paired_timings$after_s - paired_timings$before_s
print(change_s)
print(mean(change_s))
paired_check <- t.test(paired_timings$after_s, paired_timings$before_s, paired = TRUE)
print(paired_check$estimate)
stopifnot(identical(change_s, c(-4, -5, -3, -5, -1)))
stopifnot(isTRUE(all.equal(mean(change_s), -3.6)))
```

**Expected:** five differences `-4, -5, -3, -5, -1` seconds, averaging `-3.6` seconds. The paired test uses those five complete pairs. Its estimated mean difference is after minus before; the sign must match the question being asked.

This test is a mechanics demonstration. A paired t procedure assumes independent pairs and, for exact small-sample inference, normally distributed differences. Check design, outliers, measurement consistency, missingness, and whether the sampling process supports inference. A normality test with five values cannot establish that assumptions hold. Independent-group t procedures require independent units; the default Welch version does not assume equal variances. Repeated trials within one station may need a hierarchical model. Neither a p-value nor a lower mean establishes causality, especially in an invented example.

## Common mistakes and debugging

- **A seed appears ineffective:** reset it immediately before the same random calls; check R version and RNG settings.
- **Clipped values called truncated:** inspect exact boundary counts and explain the generating mechanism.
- **Widening creates list columns:** inspect duplicate compound keys before aggregating.
- **Missing values disappear:** report intended rows and measured rows separately; avoid implicit dropping during reshaping.
- **Categories reorder:** declare levels explicitly rather than relying on alphabetical defaults.
- **A plot has a mysterious legend:** distinguish mapped aesthetics from fixed colours and label axes with units.
- **Paired data analyzed as independent:** recover the identifier and compute matched differences first.

## Independent practice

1. Generate 80 invented positive timings using a documented mechanism. Explain whether you rejected, clipped, or used a positive-support distribution.
2. Add a third occasion to the six-station table, introduce two missing readings, and verify an eighteen-row long representation with a unique compound key.
3. Report counts, mean, and standard deviation for each occasion. Explain when a mean would be undefined.
4. Compare two histogram bin widths. Describe what changes and what stays fixed.
5. Draw connecting lines for station pairs, using `group = station`. Explain what those lines add beyond two box plots.

## Teach-back and summary

Why is a seed not a guarantee of valid simulation? What defines a table's row key before and after pivoting? Why does the denominator differ for a paired analysis and an available-case group summary? What can a descriptive graph say without claiming an effect?

The working sequence is **define the observation → simulate transparently → verify keys → reshape → count missingness → summarize → plot → choose inference from the design**.

## Next steps and references

[Previous: Week 1](Week_1_Group_Work_Narrative_Walkthrough.md) · [Next: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md) · [Weekly lessons](README.md) · [Wrangling topic companion](../02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) · [Plot-reading guide](../06_RESOURCES/READING_PLOTS.md) · [Paul's Notes](../README.md)

References: [tidyr pivot documentation](https://tidyr.tidyverse.org/reference/pivot_longer.html), [ggplot2 reference](https://ggplot2.tidyverse.org/reference/), and installed R help `?rnorm` and `?t.test`. [Source policy](../ORIGINALITY_POLICY.md).
