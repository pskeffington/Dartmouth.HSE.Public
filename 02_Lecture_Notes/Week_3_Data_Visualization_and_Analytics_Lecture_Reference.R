# Dartmouth | HSE.711 | Week 3 learning-objective notes
# Source: Lecture_3_Data_Visualization_and_Analytics(2).Rmd
# Chunk references count all 21 R chunks in source order, including setup.
# Entire file is commented for study; sourcing it runs no analysis.
# Objectives: inspect and join data; assess distributions and missingness;
# fit an exploratory linear model; build reusable functions; iterate files;
# keep named data lists; interpret annotated heatmaps.
# No instructor-provided source code is reproduced in this public edition.
# Data files were not attached; numeric lecture results are not reproduced.

# ===== Lecture 3, chunk 01: Prepare the session =====
# Learn: Load packages before using their functions. tidyverse supplies wrangling and plotting; haven reads SAS transport files; ggpubr arranges panels.
# Apply: Use at the start of an analysis. harrypotter is optional styling; gridExtra is not essential to the examples shown. Install packages separately from analysis scripts.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 02: Read SAS transport files =====
# Learn: read_xpt() creates blood_pressure_df and demographics_df from the examination and demographic files.
# Apply: Use for .xpt input. Relative paths depend on the working directory. Confirm actual filenames: BPXO uses the letter O, not zero.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 03: Inspect and join records =====
# Learn: glimpse() checks types and variables; inner_join(..., by = "SEQN") creates data_df using matched participant identifiers.
# Apply: Use to connect participant tables. Check duplicate keys first: repeated SEQN values can multiply rows. Inner joins discard unmatched participants.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 04: Explore distributions in three views =====
# Learn: p1 through p6 compare histograms, violin densities, and empirical cumulative distributions; ggarrange() combines plots.
# Apply: Use histograms for frequencies, violins for density shape, and ECDFs for the fraction at or below a threshold. Read axis units and inspect missingness before interpreting.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 05: Count missing age values =====
# Learn: sum(is.na(data_df$RIDAGEYR)) counts missing ages.
# Apply: Use before eligibility filtering. A zero count is a dataset result, not a guarantee for future files.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 06: Count missing blood pressure values =====
# Learn: sum(is.na(data_df$BPXOSY1)) counts unavailable first systolic measurements.
# Apply: Use to report missingness with its denominator. The lecture reports 284, but recalculate from actual files. There is no universal missingness percentage that determines whether imputation is appropriate.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 07: Define the analytic sample =====
# Learn: filter(RIDAGEYR >= 18) and drop_na(BPXOSY1) create data_df_sub; prop_removed describes total exclusions.
# Apply: Use to align data with adult eligibility and available outcomes. prop_removed combines age and missingness exclusions; report them separately when documenting sample flow.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 08: Inspect a continuous relationship =====
# Learn: scatterp1 maps RIDAGEYR to x and BPXOSY1 to y; transparency reduces overplotting.
# Apply: Use before fitting a model to inspect shape, spread, and unusual values. Axes should read Age (years) and Systolic blood pressure (mmHg).
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 09: Fit and display a linear model =====
# Learn: lm(BPXOSY1 ~ RIDAGEYR, data = data_df_sub) creates model; coef() supplies intercept and slope for eq_label.
# Apply: Use for a simple linear association. Slope units are mmHg per year. geom_smooth(se = TRUE) shows uncertainty around the fitted mean, not a prediction interval for individuals. Recompute the slope; the lecture example is about 0.4. This model does not adjust for confounding or establish causation.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 10: Write a reusable plotting function =====
# Learn: create_distribution_plots(data, variable, fill_color) creates p1, p2, p3 and returns plots.
# Apply: Use when the same plot structure repeats. sym(variable) converts a string to a symbol; !! injects that symbol into aes(). It does not itself convert the string. bins controls histogram bins, not breaks. Local p1 objects stay inside the function.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 11: Apply the function to other variables =====
# Learn: Reuse create_distribution_plots() for BPXODI1 and BPXOPLS1 without copying the plotting code.
# Apply: Use to compare diastolic pressure and pulse distributions. Check that the requested columns exist and are numeric in every input.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 12: Discover CSV files =====
# Learn: list.files() returns filenames matching a regular expression.
# Apply: Use pattern = "\\.csv$" in R to match a literal .csv suffix; full.names = TRUE returns usable paths. The lecture pattern ".csv" is broader than an exact extension match.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 13: Select a filename family =====
# Learn: A pattern of "sample" selects the lecture sample files.
# Apply: Use a more specific pattern when a folder contains unrelated CSVs. Assignment columns such as Age are capitalized; lecture sample columns such as age are lowercase. R distinguishes them.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 14: Read each file in a loop =====
# Learn: for (file in filenames) reads the_file and prints head(the_file).
# Apply: Use to inspect each input. head() returns six rows by default. file.path(data_path, file) avoids relying on a trailing slash. The loop overwrites the_file; use a named list when all inputs must remain available.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 15: Summarize each input =====
# Learn: summary(the_file$age) describes each sample file.
# Apply: Use to compare minima, quartiles, median, mean, maxima, and missing values. The lecture prose omits mean from its list; numeric summary() includes it.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 16: Repeat histograms across inputs =====
# Learn: histogram is regenerated inside the loop and printed for each file.
# Apply: Use for repeated distribution checks. aes(x = age) directly refers to the data column; the lecture age_var approach is less convenient when reusing plots with other data.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 17: Compare distributions by sex =====
# Learn: box_plot maps sex to x, age to y, and sex to fill.
# Apply: Use for a continuous measurement grouped by category. The box spans the middle 50%; whiskers and flagged points do not define clinical abnormality. Use named palette entries to keep group colors stable.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 18: Style plots by race =====
# Learn: The same box plot pattern maps race to fill and applies scale_fill_hp_d().
# Apply: Use discrete palettes for categories. This remains a box plot despite the lecture prose calling it a bar plot. Avoid treating visual differences as evidence of a causal effect.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 19: Pair files across cycles =====
# Learn: xpt_files are separated into bpxo_dfs and demo_dfs; corresponding files are joined into merged_dfs.
# Apply: Use named lists and exact matching filenames; require exactly one counterpart. Do not assume three inputs or manually assign cycle names by list order. Confirm each cycle has the expected BP variables and measurement protocol before combining.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 20: Combine loops with functions =====
# Learn: for (df in merged_dfs) calls create_distribution_plots() for each cycle.
# Apply: Use to repeat a consistent visualization across studies. Loop over names(merged_dfs) when titles need cycle identifiers. Classroom plots are unweighted exploration; population inference needs the relevant survey design and weights.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.
# ===== Lecture 3, chunk 21: Draw an annotated heatmap =====
# Learn: counts_subset keeps ten genes; column_ha maps Disease_Status and Sex; Heatmap() clusters gene and sample patterns.
# Apply: Use for multivariable expression patterns. Match metadata row names to counts column names before annotation. Verify numeric counts and sample identity. Raw counts reflect library size as well as expression; normalization, transformation, and row scaling answer different questions. The first ten rows are a teaching selection, not a biological ranking.
# Independent practice prompt: recreate the described technique using self-authored code and permitted data.