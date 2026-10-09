# HSE 711 · Week 2 learning notes

[Lecture index](README.md) · [Commented source](Week_2_Learning_Objective_Notes.R) · [Repository home](../README.md)

> **Reading edition.** Original lecture references are retained for study. The commented source runs no analysis. Code below is reference material; check paths, packages, inputs and prerequisites before using it.

HSE 711: Foundations in Data Science

Week 2 Learning Objective Notes — Data Wrangling and Visualization

Source: Lecture_2_Data_Wrangling(2).Rmd (2026-08)

Prepared: September 25, 2026

Every line is commented: sourcing this file performs no analysis.

Chunk numbers count the 44 R code fences in source order, including unlabeled fences.

These are original study notes, not a copy of the lecture or a runnable analysis.

Read the exercise walkthrough for a complete applied example.

## On this page

- [01. SETUP AND PACKAGES (source line 31)](#01-setup-and-packages-source-line-31)
- [02. NORMAL DRAWS (source line 46)](#02-normal-draws-source-line-46)
- [03. BINOMIAL DRAWS (source line 53)](#03-binomial-draws-source-line-53)
- [04. SEED FOR NORMAL SIMULATION (source line 62)](#04-seed-for-normal-simulation-source-line-62)
- [05. SEED FOR BINOMIAL SIMULATION (source line 69)](#05-seed-for-binomial-simulation-source-line-69)
- [06. BASE DATA FRAME SIMULATION (source line 76)](#06-base-data-frame-simulation-source-line-76)
- [07. TIBBLE AND PIPE (source line 124)](#07-tibble-and-pipe-source-line-124)
- [08. BIND A COLUMN (source line 145)](#08-bind-a-column-source-line-145)
- [09. BIND A ROW (source line 160)](#09-bind-a-row-source-line-160)
- [10. TIDY BINDING (source line 172)](#10-tidy-binding-source-line-172)
- [11. REMOVE COLUMNS (source line 198)](#11-remove-columns-source-line-198)
- [12. REMOVE ROWS (source line 214)](#12-remove-rows-source-line-214)
- [13. BASE FILTERING AND GROUPING (source line 247)](#13-base-filtering-and-grouping-source-line-247)
- [14. TIDY FILTERING AND GROUPING (source line 257)](#14-tidy-filtering-and-grouping-source-line-257)
- [15. GROUPED SUMMARIES (source line 270)](#15-grouped-summaries-source-line-270)
- [16. REPLACE TEXT (source line 318)](#16-replace-text-source-line-318)
- [17. CAPTURE PART OF A STRING (source line 328)](#17-capture-part-of-a-string-source-line-328)
- [18. WIDE TO LONG (source line 342)](#18-wide-to-long-source-line-342)
- [19. LONG TO WIDE (source line 352)](#19-long-to-wide-source-line-352)
- [20. FIRST HISTOGRAM (source line 366)](#20-first-histogram-source-line-366)
- [21. HISTOGRAM LABELS (source line 372)](#21-histogram-labels-source-line-372)
- [22. HISTOGRAM BREAKS: 10 (source line 379)](#22-histogram-breaks-10-source-line-379)
- [23. HISTOGRAM BREAKS: 30 (source line 385)](#23-histogram-breaks-30-source-line-385)
- [24. HISTOGRAM BREAKS: 50 (source line 391)](#24-histogram-breaks-50-source-line-391)
- [25. SCATTER PLOT (source line 401)](#25-scatter-plot-source-line-401)
- [26. SAVE A BASE GRAPHICS PANEL (source line 410)](#26-save-a-base-graphics-panel-source-line-410)
- [27. ANSCOMBE DATA (source line 442)](#27-anscombe-data-source-line-442)
- [28. ANSCOMBE CALCULATIONS (source line 447)](#28-anscombe-calculations-source-line-447)
- [29. ANSCOMBE SUMMARY TABLE (source line 481)](#29-anscombe-summary-table-source-line-481)
- [30. PLOT ANSCOMBE QUARTETS (source line 504)](#30-plot-anscombe-quartets-source-line-504)
- [31. GROUPED GGPLOT BOX PLOT (source line 535)](#31-grouped-ggplot-box-plot-source-line-535)
- [32. JITTERED BOX PLOT (source line 547)](#32-jittered-box-plot-source-line-547)
- [33. HALF-EYE PLOT (source line 563)](#33-half-eye-plot-source-line-563)
- [34. QUASIRANDOM PLOT (source line 584)](#34-quasirandom-plot-source-line-584)
- [35. READ PUBLIC COUNT DATA (source line 600)](#35-read-public-count-data-source-line-600)
- [36. CHECK COUNT DIMENSIONS (source line 616)](#36-check-count-dimensions-source-line-616)
- [37. READ METADATA (source line 621)](#37-read-metadata-source-line-621)
- [38. JOIN GENE MEASURES TO METADATA (source line 631)](#38-join-gene-measures-to-metadata-source-line-631)
- [39. PLOT A SELECTED GENE (source line 653)](#39-plot-a-selected-gene-source-line-653)
- [40. ADD RANK-SUM TEST (source line 675)](#40-add-rank-sum-test-source-line-675)
- [41. CREATE A PANEL (source line 692)](#41-create-a-panel-source-line-692)
- [42. SAVE PANEL WITH PNG (source line 760)](#42-save-panel-with-png-source-line-760)
- [43. SAVE PLOT WITH GGSAVE (source line 776)](#43-save-plot-with-ggsave-source-line-776)
- [44. SUMMARY STATISTICS (source line 783)](#44-summary-statistics-source-line-783)

## 01. SETUP AND PACKAGES (source line 31)

**Learn:** Load tidyverse and gridExtra in a setup chunk; install packages separately in the Console.

**Apply:** Establish reproducible dependencies before wrangling or plotting.

## 02. NORMAL DRAWS (source line 46)

**Learn:** rnorm(n, mean, sd) draws continuous values from a normal distribution.

**Apply:** Prototype measurement variables and understand mean/spread.

## 03. BINOMIAL DRAWS (source line 53)

**Learn:** rbinom(n, size, prob) draws successes over fixed trials.

**Apply:** Model binary labels with size = 1 or counts with larger size.

## 04. SEED FOR NORMAL SIMULATION (source line 62)

**Learn:** set.seed(246) fixes the pseudorandom sequence before rnorm().

**Apply:** Make a demonstration reproducible under compatible R settings.

## 05. SEED FOR BINOMIAL SIMULATION (source line 69)

**Learn:** Set the seed before rbinom(); repeating a seed restarts the stream.

**Apply:** Compare classmates' draws and separate examples deliberately.

## 06. BASE DATA FRAME SIMULATION (source line 76)

**Learn:** Build random_data with Subject_ID, Age, Sex, Disease_Status, Heart_Rate.

**Apply:** Check n, bounds and types before treating generated rows as observations.

## 07. TIBBLE AND PIPE (source line 124)

**Learn:** Create random_data_tbl with tibble(); pass it through %>% to slice_head().

**Apply:** Keep tabular workflows readable; note it is a distinct simulated object.

## 08. BIND A COLUMN (source line 145)

**Learn:** Create Alcohol_Consumption of matching length and cbind() to random_data.

**Apply:** Add a variable only after checking row order and length.

## 09. BIND A ROW (source line 160)

**Learn:** Add participant_101 using rbind() with values aligned to existing columns.

**Apply:** Extend the example without silently permuting fields; verify types afterward.

## 10. TIDY BINDING (source line 172)

**Learn:** Use bind_cols() and bind_rows() with named tibble fields.

**Apply:** Add rows/columns while retaining explicit field names.

## 11. REMOVE COLUMNS (source line 198)

**Learn:** Use positional/base selection or select(-Sex) on a copy.

**Apply:** Exclude unnecessary fields while preserving the original.

## 12. REMOVE ROWS (source line 214)

**Learn:** Filter by row number or Subject_ID; dplyr offers slice() and filter().

**Apply:** Prefer an ID predicate when row order may change.

## 13. BASE FILTERING AND GROUPING (source line 247)

**Learn:** Subset adults >= 30, retain Subject_ID/Age/Sex, then cut() Age_Group.

**Apply:** Define a reproducible study cohort and age categories.

## 14. TIDY FILTERING AND GROUPING (source line 257)

**Learn:** Pipe filter() -> select() -> mutate(case_when()).

**Apply:** Express the same cohort logic with verbs and explicit boundary rules.

## 15. GROUPED SUMMARIES (source line 270)

**Learn:** Use tapply() or group_by() + summarize() for means, medians, counts.

**Apply:** Describe differences by Sex; use na.rm = TRUE where appropriate.

## 16. REPLACE TEXT (source line 318)

**Learn:** gsub() substitutes all matches in Subject_ID.

**Apply:** Normalize identifiers; check that replacement does not alter unintended text.

## 17. CAPTURE PART OF A STRING (source line 328)

**Learn:** sub() with a pattern retains the prefix before later underscores.

**Apply:** Extract a structured label from a delimited string; test the pattern.

## 18. WIDE TO LONG (source line 342)

**Learn:** pivot_longer() stacks Age and Heart_Rate into name/value rows.

**Apply:** Prepare tidy input for grouped plotting; keep measurement units separate.

## 19. LONG TO WIDE (source line 352)

**Learn:** pivot_wider() expands a measurement column back into fields.

**Apply:** Recover one row per subject, checking key uniqueness first.

## 20. FIRST HISTOGRAM (source line 366)

**Learn:** hist(random_data$Heart_Rate) displays a numerical distribution.

**Apply:** Inspect shape, tails and possible implausible simulated values.

## 21. HISTOGRAM LABELS (source line 372)

**Learn:** Set main, xlab and ylab on hist().

**Apply:** Make a figure interpretable outside the code.

## 22. HISTOGRAM BREAKS: 10 (source line 379)

**Learn:** Set breaks = 10 to coarsen the heart-rate bins.

**Apply:** See broad distribution features.

## 23. HISTOGRAM BREAKS: 30 (source line 385)

**Learn:** Set breaks = 30 for finer bins.

**Apply:** Compare visual sensitivity to bin count.

## 24. HISTOGRAM BREAKS: 50 (source line 391)

**Learn:** Set breaks = 50 for still finer bins.

**Apply:** Avoid treating an apparent pattern as independent of binning.

## 25. SCATTER PLOT (source line 401)

**Learn:** plot(Age, Heart_Rate) with labels compares two numeric variables.

**Apply:** Explore association without claiming a causal relation.

## 26. SAVE A BASE GRAPHICS PANEL (source line 410)

**Learn:** Create the figures folder, open png(), draw a panel, call dev.off().

**Apply:** Export a figure; ensure p1/p2/p3 exist before running this example.

## 27. ANSCOMBE DATA (source line 442)

**Learn:** Inspect built-in anscombe before summarizing.

**Apply:** Recognize that identical statistics can hide distinct patterns.

## 28. ANSCOMBE CALCULATIONS (source line 447)

**Learn:** Use apply() and cor() on the four paired data sets.

**Apply:** Compare means/correlations before looking at plots.

## 29. ANSCOMBE SUMMARY TABLE (source line 481)

**Learn:** Build anscombe_summary with means, variances and correlations.

**Apply:** Put comparable statistics side by side.

## 30. PLOT ANSCOMBE QUARTETS (source line 504)

**Learn:** Inspect each x/y pair as a scatter plot.

**Apply:** Let graphical diagnostics challenge summary-only conclusions.

## 31. GROUPED GGPLOT BOX PLOT (source line 535)

**Learn:** Map Sex to x, Heart_Rate to y and Disease_Status to fill.

**Apply:** Compare distributions by two categories.

## 32. JITTERED BOX PLOT (source line 547)

**Learn:** Add geom_jitter() with aligned dodge and suppress duplicate outlier symbols.

**Apply:** Show observations and summaries together.

## 33. HALF-EYE PLOT (source line 563)

**Learn:** ggdist::stat_halfeye() adds distribution shape to the grouping.

**Apply:** Use an optional package only if installed and needed.

## 34. QUASIRANDOM PLOT (source line 584)

**Learn:** ggbeeswarm::geom_quasirandom() spreads overlapping points.

**Apply:** Display dense groups without implying new observations.

## 35. READ PUBLIC COUNT DATA (source line 600)

**Learn:** Use file_path and read.delim() to import ra_df with gene IDs as row names.

**Apply:** Inspect actual file location and schema before analysis.

## 36. CHECK COUNT DIMENSIONS (source line 616)

**Learn:** dim(ra_df) reports genes by sample columns.

**Apply:** Confirm orientation and expected record counts.

## 37. READ METADATA (source line 621)

**Learn:** read.csv(..., row.names = 1) imports metadata.

**Apply:** Check sample identifiers and column types before joining.

## 38. JOIN GENE MEASURES TO METADATA (source line 631)

**Learn:** Select CXCL13/STAT3/ACTA2, transpose, then merge on sample IDs.

**Apply:** Check unmatched samples after an all = TRUE merge; the comment about IL6 is stale.

## 39. PLOT A SELECTED GENE (source line 653)

**Learn:** Set timepoint level order, then ggplot() + geom_boxplot().

**Apply:** Display CXCL13 pre/post distributions with clear labels.

## 40. ADD RANK-SUM TEST (source line 675)

**Learn:** ggpubr::stat_compare_means(method = 'wilcox') annotates a two-group plot.

**Apply:** Check exactly two nonempty groups and missing/tied values before interpreting.

## 41. CREATE A PANEL (source line 692)

**Learn:** Build p1/p2/p3 for genes and arrange with gridExtra.

**Apply:** Keep variables defined in execution order and use a consistent visual scale.

## 42. SAVE PANEL WITH PNG (source line 760)

**Learn:** Open png(), draw grid.arrange(), then dev.off().

**Apply:** Export high-resolution output; create its folder first.

## 43. SAVE PLOT WITH GGSAVE (source line 776)

**Learn:** ggsave() writes the existing myplot object.

**Apply:** Use explicit dimensions and verify the plot object exists.

## 44. SUMMARY STATISTICS (source line 783)

**Learn:** summary(), min/max/mean/median/sd(), and summarize()/pull() describe AGE.

**Apply:** Choose complete-case handling and report units and sample size.

Cross-cutting checks: preserve stable IDs, inspect class/NA before pivoting or testing,

use a seed for simulated data, verify join cardinality, and label units on figures.

