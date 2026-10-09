# HSE 711 · Week 2 learning notes

[Lecture index](README.md) · [Commented source](Week_2_Learning_Objective_Notes.R) · [Repository home](../README.md)

> **Reading edition.** Original lecture references are retained for study. The commented source runs no analysis. Code below is reference material; check paths, packages, inputs and prerequisites before using it.

HSE 711: Foundations in Data Science Week 2 Learning Objective Notes — Data Wrangling and Visualization Source: Lecture_2_Data_Wrangling(2).Rmd (2026-08) Prepared: September 25, 2026 Every line is commented: sourcing this file performs no analysis. Chunk numbers count the 44 R code fences in source order, including unlabeled fences. These are original study notes, not a copy of the lecture or a runnable analysis. Read the exercise walkthrough for a complete applied example.

## On this page

- [01. Setup and packages](#01-setup-and-packages)
- [02. Normal draws](#02-normal-draws)
- [03. Binomial draws](#03-binomial-draws)
- [04. Seed for normal simulation](#04-seed-for-normal-simulation)
- [05. Seed for binomial simulation](#05-seed-for-binomial-simulation)
- [06. Base data frame simulation](#06-base-data-frame-simulation)
- [07. Tibble and pipe](#07-tibble-and-pipe)
- [08. Bind a column](#08-bind-a-column)
- [09. Bind a row](#09-bind-a-row)
- [10. Tidy binding](#10-tidy-binding)
- [11. Remove columns](#11-remove-columns)
- [12. Remove rows](#12-remove-rows)
- [13. Base filtering and grouping](#13-base-filtering-and-grouping)
- [14. Tidy filtering and grouping](#14-tidy-filtering-and-grouping)
- [15. Grouped summaries](#15-grouped-summaries)
- [16. Replace text](#16-replace-text)
- [17. Capture part of a string](#17-capture-part-of-a-string)
- [18. Wide to long](#18-wide-to-long)
- [19. Long to wide](#19-long-to-wide)
- [20. First histogram](#20-first-histogram)
- [21. Histogram labels](#21-histogram-labels)
- [22. Histogram breaks: 10](#22-histogram-breaks-10)
- [23. Histogram breaks: 30](#23-histogram-breaks-30)
- [24. Histogram breaks: 50](#24-histogram-breaks-50)
- [25. Scatter plot](#25-scatter-plot)
- [26. Save a base graphics panel](#26-save-a-base-graphics-panel)
- [27. Anscombe data](#27-anscombe-data)
- [28. Anscombe calculations](#28-anscombe-calculations)
- [29. Anscombe summary table](#29-anscombe-summary-table)
- [30. Plot anscombe quartets](#30-plot-anscombe-quartets)
- [31. Grouped ggplot box plot](#31-grouped-ggplot-box-plot)
- [32. Jittered box plot](#32-jittered-box-plot)
- [33. Half-eye plot](#33-half-eye-plot)
- [34. Quasirandom plot](#34-quasirandom-plot)
- [35. Read public count data](#35-read-public-count-data)
- [36. Check count dimensions](#36-check-count-dimensions)
- [37. Read metadata](#37-read-metadata)
- [38. Join gene measures to metadata](#38-join-gene-measures-to-metadata)
- [39. Plot a selected gene](#39-plot-a-selected-gene)
- [40. Add rank-sum test](#40-add-rank-sum-test)
- [41. Create a panel](#41-create-a-panel)
- [42. Save panel with png](#42-save-panel-with-png)
- [43. Save plot with ggsave](#43-save-plot-with-ggsave)
- [44. Summary statistics](#44-summary-statistics)

## 01. Setup and packages

**Learn:** Load tidyverse and gridExtra in a setup chunk; install packages separately in the Console.

**Apply:** Establish reproducible dependencies before wrangling or plotting.

## 02. Normal draws

**Learn:** rnorm(n, mean, sd) draws continuous values from a normal distribution.

**Apply:** Prototype measurement variables and understand mean/spread.

## 03. Binomial draws

**Learn:** rbinom(n, size, prob) draws successes over fixed trials.

**Apply:** Model binary labels with size = 1 or counts with larger size.

## 04. Seed for normal simulation

**Learn:** set.seed(246) fixes the pseudorandom sequence before rnorm().

**Apply:** Make a demonstration reproducible under compatible R settings.

## 05. Seed for binomial simulation

**Learn:** Set the seed before rbinom(); repeating a seed restarts the stream.

**Apply:** Compare classmates' draws and separate examples deliberately.

## 06. Base data frame simulation

**Learn:** Build random_data with Subject_ID, Age, Sex, Disease_Status, Heart_Rate.

**Apply:** Check n, bounds and types before treating generated rows as observations.

## 07. Tibble and pipe

**Learn:** Create random_data_tbl with tibble(); pass it through %>% to slice_head().

**Apply:** Keep tabular workflows readable; note it is a distinct simulated object.

## 08. Bind a column

**Learn:** Create Alcohol_Consumption of matching length and cbind() to random_data.

**Apply:** Add a variable only after checking row order and length.

## 09. Bind a row

**Learn:** Add participant_101 using rbind() with values aligned to existing columns.

**Apply:** Extend the example without silently permuting fields; verify types afterward.

## 10. Tidy binding

**Learn:** Use bind_cols() and bind_rows() with named tibble fields.

**Apply:** Add rows/columns while retaining explicit field names.

## 11. Remove columns

**Learn:** Use positional/base selection or select(-Sex) on a copy.

**Apply:** Exclude unnecessary fields while preserving the original.

## 12. Remove rows

**Learn:** Filter by row number or Subject_ID; dplyr offers slice() and filter().

**Apply:** Prefer an ID predicate when row order may change.

## 13. Base filtering and grouping

**Learn:** Subset adults >= 30, retain Subject_ID/Age/Sex, then cut() Age_Group.

**Apply:** Define a reproducible study cohort and age categories.

## 14. Tidy filtering and grouping

**Learn:** Pipe filter() -> select() -> mutate(case_when()).

**Apply:** Express the same cohort logic with verbs and explicit boundary rules.

## 15. Grouped summaries

**Learn:** Use tapply() or group_by() + summarize() for means, medians, counts.

**Apply:** Describe differences by Sex; use na.rm = TRUE where appropriate.

## 16. Replace text

**Learn:** gsub() substitutes all matches in Subject_ID.

**Apply:** Normalize identifiers; check that replacement does not alter unintended text.

## 17. Capture part of a string

**Learn:** sub() with a pattern retains the prefix before later underscores.

**Apply:** Extract a structured label from a delimited string; test the pattern.

## 18. Wide to long

**Learn:** pivot_longer() stacks Age and Heart_Rate into name/value rows.

**Apply:** Prepare tidy input for grouped plotting; keep measurement units separate.

## 19. Long to wide

**Learn:** pivot_wider() expands a measurement column back into fields.

**Apply:** Recover one row per subject, checking key uniqueness first.

## 20. First histogram

**Learn:** hist(random_data$Heart_Rate) displays a numerical distribution.

**Apply:** Inspect shape, tails and possible implausible simulated values.

## 21. Histogram labels

**Learn:** Set main, xlab and ylab on hist().

**Apply:** Make a figure interpretable outside the code.

## 22. Histogram breaks: 10

**Learn:** Set breaks = 10 to coarsen the heart-rate bins.

**Apply:** See broad distribution features.

## 23. Histogram breaks: 30

**Learn:** Set breaks = 30 for finer bins.

**Apply:** Compare visual sensitivity to bin count.

## 24. Histogram breaks: 50

**Learn:** Set breaks = 50 for still finer bins.

**Apply:** Avoid treating an apparent pattern as independent of binning.

## 25. Scatter plot

**Learn:** plot(Age, Heart_Rate) with labels compares two numeric variables.

**Apply:** Explore association without claiming a causal relation.

## 26. Save a base graphics panel

**Learn:** Create the figures folder, open png(), draw a panel, call dev.off().

**Apply:** Export a figure; ensure p1/p2/p3 exist before running this example.

## 27. Anscombe data

**Learn:** Inspect built-in anscombe before summarizing.

**Apply:** Recognize that identical statistics can hide distinct patterns.

## 28. Anscombe calculations

**Learn:** Use apply() and cor() on the four paired data sets.

**Apply:** Compare means/correlations before looking at plots.

## 29. Anscombe summary table

**Learn:** Build anscombe_summary with means, variances and correlations.

**Apply:** Put comparable statistics side by side.

## 30. Plot anscombe quartets

**Learn:** Inspect each x/y pair as a scatter plot.

**Apply:** Let graphical diagnostics challenge summary-only conclusions.

## 31. Grouped ggplot box plot

**Learn:** Map Sex to x, Heart_Rate to y and Disease_Status to fill.

**Apply:** Compare distributions by two categories.

## 32. Jittered box plot

**Learn:** Add geom_jitter() with aligned dodge and suppress duplicate outlier symbols.

**Apply:** Show observations and summaries together.

## 33. Half-eye plot

**Learn:** ggdist::stat_halfeye() adds distribution shape to the grouping.

**Apply:** Use an optional package only if installed and needed.

## 34. Quasirandom plot

**Learn:** ggbeeswarm::geom_quasirandom() spreads overlapping points.

**Apply:** Display dense groups without implying new observations.

## 35. Read public count data

**Learn:** Use file_path and read.delim() to import ra_df with gene IDs as row names.

**Apply:** Inspect actual file location and schema before analysis.

## 36. Check count dimensions

**Learn:** dim(ra_df) reports genes by sample columns.

**Apply:** Confirm orientation and expected record counts.

## 37. Read metadata

**Learn:** read.csv(..., row.names = 1) imports metadata.

**Apply:** Check sample identifiers and column types before joining.

## 38. Join gene measures to metadata

**Learn:** Select CXCL13/STAT3/ACTA2, transpose, then merge on sample IDs.

**Apply:** Check unmatched samples after an all = TRUE merge; the comment about IL6 is stale.

## 39. Plot a selected gene

**Learn:** Set timepoint level order, then ggplot() + geom_boxplot().

**Apply:** Display CXCL13 pre/post distributions with clear labels.

## 40. Add rank-sum test

**Learn:** ggpubr::stat_compare_means(method = 'wilcox') annotates a two-group plot.

**Apply:** Check exactly two nonempty groups and missing/tied values before interpreting.

## 41. Create a panel

**Learn:** Build p1/p2/p3 for genes and arrange with gridExtra.

**Apply:** Keep variables defined in execution order and use a consistent visual scale.

## 42. Save panel with png

**Learn:** Open png(), draw grid.arrange(), then dev.off().

**Apply:** Export high-resolution output; create its folder first.

## 43. Save plot with ggsave

**Learn:** ggsave() writes the existing myplot object.

**Apply:** Use explicit dimensions and verify the plot object exists.

## 44. Summary statistics

**Learn:** summary(), min/max/mean/median/sd(), and summarize()/pull() describe AGE.

**Apply:** Choose complete-case handling and report units and sample size.

Cross-cutting checks: preserve stable IDs, inspect class/NA before pivoting or testing,

use a seed for simulated data, verify join cardinality, and label units on figures.

