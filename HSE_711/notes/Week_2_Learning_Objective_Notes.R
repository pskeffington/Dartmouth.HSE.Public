# HSE 711: Foundations in Data Science
# Week 2 Learning Objective Notes — Data Wrangling and Visualization
# Source: Lecture_2_Data_Wrangling(2).Rmd (2026-08)
# Prepared: September 25, 2026
#
# Every line is commented: sourcing this file performs no analysis.
# Chunk numbers count the 44 R code fences in source order, including unlabeled fences.
# These are original study notes, not a copy of the lecture or a runnable analysis.
# Read the exercise walkthrough for a complete applied example.
#
# CHUNK 01 — SETUP AND PACKAGES (source line 31)
# Objective/how: Load tidyverse and gridExtra in a setup chunk; install packages separately in the Console.
# Apply: Establish reproducible dependencies before wrangling or plotting.
#
# CHUNK 02 — NORMAL DRAWS (source line 46)
# Objective/how: rnorm(n, mean, sd) draws continuous values from a normal distribution.
# Apply: Prototype measurement variables and understand mean/spread.
#
# CHUNK 03 — BINOMIAL DRAWS (source line 53)
# Objective/how: rbinom(n, size, prob) draws successes over fixed trials.
# Apply: Model binary labels with size = 1 or counts with larger size.
#
# CHUNK 04 — SEED FOR NORMAL SIMULATION (source line 62)
# Objective/how: set.seed(246) fixes the pseudorandom sequence before rnorm().
# Apply: Make a demonstration reproducible under compatible R settings.
#
# CHUNK 05 — SEED FOR BINOMIAL SIMULATION (source line 69)
# Objective/how: Set the seed before rbinom(); repeating a seed restarts the stream.
# Apply: Compare classmates' draws and separate examples deliberately.
#
# CHUNK 06 — BASE DATA FRAME SIMULATION (source line 76)
# Objective/how: Build random_data with Subject_ID, Age, Sex, Disease_Status, Heart_Rate.
# Apply: Check n, bounds and types before treating generated rows as observations.
#
# CHUNK 07 — TIBBLE AND PIPE (source line 124)
# Objective/how: Create random_data_tbl with tibble(); pass it through %>% to slice_head().
# Apply: Keep tabular workflows readable; note it is a distinct simulated object.
#
# CHUNK 08 — BIND A COLUMN (source line 145)
# Objective/how: Create Alcohol_Consumption of matching length and cbind() to random_data.
# Apply: Add a variable only after checking row order and length.
#
# CHUNK 09 — BIND A ROW (source line 160)
# Objective/how: Add participant_101 using rbind() with values aligned to existing columns.
# Apply: Extend the example without silently permuting fields; verify types afterward.
#
# CHUNK 10 — TIDY BINDING (source line 172)
# Objective/how: Use bind_cols() and bind_rows() with named tibble fields.
# Apply: Add rows/columns while retaining explicit field names.
#
# CHUNK 11 — REMOVE COLUMNS (source line 198)
# Objective/how: Use positional/base selection or select(-Sex) on a copy.
# Apply: Exclude unnecessary fields while preserving the original.
#
# CHUNK 12 — REMOVE ROWS (source line 214)
# Objective/how: Filter by row number or Subject_ID; dplyr offers slice() and filter().
# Apply: Prefer an ID predicate when row order may change.
#
# CHUNK 13 — BASE FILTERING AND GROUPING (source line 247)
# Objective/how: Subset adults >= 30, retain Subject_ID/Age/Sex, then cut() Age_Group.
# Apply: Define a reproducible study cohort and age categories.
#
# CHUNK 14 — TIDY FILTERING AND GROUPING (source line 257)
# Objective/how: Pipe filter() -> select() -> mutate(case_when()).
# Apply: Express the same cohort logic with verbs and explicit boundary rules.
#
# CHUNK 15 — GROUPED SUMMARIES (source line 270)
# Objective/how: Use tapply() or group_by() + summarize() for means, medians, counts.
# Apply: Describe differences by Sex; use na.rm = TRUE where appropriate.
#
# CHUNK 16 — REPLACE TEXT (source line 318)
# Objective/how: gsub() substitutes all matches in Subject_ID.
# Apply: Normalize identifiers; check that replacement does not alter unintended text.
#
# CHUNK 17 — CAPTURE PART OF A STRING (source line 328)
# Objective/how: sub() with a pattern retains the prefix before later underscores.
# Apply: Extract a structured label from a delimited string; test the pattern.
#
# CHUNK 18 — WIDE TO LONG (source line 342)
# Objective/how: pivot_longer() stacks Age and Heart_Rate into name/value rows.
# Apply: Prepare tidy input for grouped plotting; keep measurement units separate.
#
# CHUNK 19 — LONG TO WIDE (source line 352)
# Objective/how: pivot_wider() expands a measurement column back into fields.
# Apply: Recover one row per subject, checking key uniqueness first.
#
# CHUNK 20 — FIRST HISTOGRAM (source line 366)
# Objective/how: hist(random_data$Heart_Rate) displays a numerical distribution.
# Apply: Inspect shape, tails and possible implausible simulated values.
#
# CHUNK 21 — HISTOGRAM LABELS (source line 372)
# Objective/how: Set main, xlab and ylab on hist().
# Apply: Make a figure interpretable outside the code.
#
# CHUNK 22 — HISTOGRAM BREAKS: 10 (source line 379)
# Objective/how: Set breaks = 10 to coarsen the heart-rate bins.
# Apply: See broad distribution features.
#
# CHUNK 23 — HISTOGRAM BREAKS: 30 (source line 385)
# Objective/how: Set breaks = 30 for finer bins.
# Apply: Compare visual sensitivity to bin count.
#
# CHUNK 24 — HISTOGRAM BREAKS: 50 (source line 391)
# Objective/how: Set breaks = 50 for still finer bins.
# Apply: Avoid treating an apparent pattern as independent of binning.
#
# CHUNK 25 — SCATTER PLOT (source line 401)
# Objective/how: plot(Age, Heart_Rate) with labels compares two numeric variables.
# Apply: Explore association without claiming a causal relation.
#
# CHUNK 26 — SAVE A BASE GRAPHICS PANEL (source line 410)
# Objective/how: Create the figures folder, open png(), draw a panel, call dev.off().
# Apply: Export a figure; ensure p1/p2/p3 exist before running this example.
#
# CHUNK 27 — ANSCOMBE DATA (source line 442)
# Objective/how: Inspect built-in anscombe before summarizing.
# Apply: Recognize that identical statistics can hide distinct patterns.
#
# CHUNK 28 — ANSCOMBE CALCULATIONS (source line 447)
# Objective/how: Use apply() and cor() on the four paired data sets.
# Apply: Compare means/correlations before looking at plots.
#
# CHUNK 29 — ANSCOMBE SUMMARY TABLE (source line 481)
# Objective/how: Build anscombe_summary with means, variances and correlations.
# Apply: Put comparable statistics side by side.
#
# CHUNK 30 — PLOT ANSCOMBE QUARTETS (source line 504)
# Objective/how: Inspect each x/y pair as a scatter plot.
# Apply: Let graphical diagnostics challenge summary-only conclusions.
#
# CHUNK 31 — GROUPED GGPLOT BOX PLOT (source line 535)
# Objective/how: Map Sex to x, Heart_Rate to y and Disease_Status to fill.
# Apply: Compare distributions by two categories.
#
# CHUNK 32 — JITTERED BOX PLOT (source line 547)
# Objective/how: Add geom_jitter() with aligned dodge and suppress duplicate outlier symbols.
# Apply: Show observations and summaries together.
#
# CHUNK 33 — HALF-EYE PLOT (source line 563)
# Objective/how: ggdist::stat_halfeye() adds distribution shape to the grouping.
# Apply: Use an optional package only if installed and needed.
#
# CHUNK 34 — QUASIRANDOM PLOT (source line 584)
# Objective/how: ggbeeswarm::geom_quasirandom() spreads overlapping points.
# Apply: Display dense groups without implying new observations.
#
# CHUNK 35 — READ PUBLIC COUNT DATA (source line 600)
# Objective/how: Use file_path and read.delim() to import ra_df with gene IDs as row names.
# Apply: Inspect actual file location and schema before analysis.
#
# CHUNK 36 — CHECK COUNT DIMENSIONS (source line 616)
# Objective/how: dim(ra_df) reports genes by sample columns.
# Apply: Confirm orientation and expected record counts.
#
# CHUNK 37 — READ METADATA (source line 621)
# Objective/how: read.csv(..., row.names = 1) imports metadata.
# Apply: Check sample identifiers and column types before joining.
#
# CHUNK 38 — JOIN GENE MEASURES TO METADATA (source line 631)
# Objective/how: Select CXCL13/STAT3/ACTA2, transpose, then merge on sample IDs.
# Apply: Check unmatched samples after an all = TRUE merge; the comment about IL6 is stale.
#
# CHUNK 39 — PLOT A SELECTED GENE (source line 653)
# Objective/how: Set timepoint level order, then ggplot() + geom_boxplot().
# Apply: Display CXCL13 pre/post distributions with clear labels.
#
# CHUNK 40 — ADD RANK-SUM TEST (source line 675)
# Objective/how: ggpubr::stat_compare_means(method = 'wilcox') annotates a two-group plot.
# Apply: Check exactly two nonempty groups and missing/tied values before interpreting.
#
# CHUNK 41 — CREATE A PANEL (source line 692)
# Objective/how: Build p1/p2/p3 for genes and arrange with gridExtra.
# Apply: Keep variables defined in execution order and use a consistent visual scale.
#
# CHUNK 42 — SAVE PANEL WITH PNG (source line 760)
# Objective/how: Open png(), draw grid.arrange(), then dev.off().
# Apply: Export high-resolution output; create its folder first.
#
# CHUNK 43 — SAVE PLOT WITH GGSAVE (source line 776)
# Objective/how: ggsave() writes the existing myplot object.
# Apply: Use explicit dimensions and verify the plot object exists.
#
# CHUNK 44 — SUMMARY STATISTICS (source line 783)
# Objective/how: summary(), min/max/mean/median/sd(), and summarize()/pull() describe AGE.
# Apply: Choose complete-case handling and report units and sample size.
#
# Cross-cutting checks: preserve stable IDs, inspect class/NA before pivoting or testing,
# use a seed for simulated data, verify join cardinality, and label units on figures.
