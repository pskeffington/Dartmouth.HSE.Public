# HSE 711 — Week 3: Data Visualization and Analytics Lecture Notes

[Section index](README.md) · [Editable R Markdown](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed for study and has not been executed to generate this page. Run the source chunks in order to produce and check outputs; data-dependent examples need separately supplied course files.

## On this page

- [Purpose and learning objectives](#purpose-and-learning-objectives)
- [1. Identify the join key before combining tables](#1-identify-the-join-key-before-combining-tables)
- [2. Understand missingness and survey codes](#2-understand-missingness-and-survey-codes)
- [3. Explore distributions before fitting models](#3-explore-distributions-before-fitting-models)
- [4. Read a scatter plot and fit a linear model](#4-read-a-scatter-plot-and-fit-a-linear-model)
- [5. Package repeated plots into one function](#5-package-repeated-plots-into-one-function)
- [6. Import multiple files without losing track of them](#6-import-multiple-files-without-losing-track-of-them)
- [7. Build a publication-readable figure panel](#7-build-a-publication-readable-figure-panel)
- [8. Final self-check: what Week 3 mastery requires](#8-final-self-check-what-week-3-mastery-requires)

## Purpose and learning objectives

Week 3 moves from plot creation to combining independently supplied tables, examining missing observations, fitting simple descriptive models, using repeated plotting functions, and automating file-by-file review. The assignment applies those tools to multiple survey tables and publication-style figures. This guide uses independent toy data instead of the assignment submission or source datasets. Consult the existing [21-chunk lecture reference](Week_3_Data_Visualization_and_Analytics_Lecture_Reference.md) for the original lecture sequence.

| Assignment skill | Lecture topic | Mastery evidence |
| --- | --- | --- |
| Import and inspect survey tables | Chunks 1–3: `read_xpt()`, `head()`, `glimpse()` | Columns, IDs, and type checks documented |
| Select and join fields | Chunk 3: `inner_join()` | Join key uniqueness and retention verified |
| Recode survey response categories | Chunks 5–7: missingness and filtering | Distinguish recorded "unknown" responses from `NA` |
| Construct and explain plot panels | Chunks 4, 8–11: histogram, violin, ECDF, scatter, linear fit | Each plot answers a stated question |
| Generalize workflows | Chunks 10–21: plotting functions, loops, file lists, heatmaps | Reusable code and input checks |

## 1. Identify the join key before combining tables

The lecture uses `haven::read_xpt()` to read SAS transport files. For this standalone demonstration, create two small tables directly in R and join them by a stable participant ID.

```r
library(dplyr)

measure_df <- data.frame(
  participant_id = c(101L, 102L, 103L),
  measurement = c(5.2, 6.8, NA_real_)
)
profile_df <- data.frame(
  participant_id = c(101L, 102L, 104L),
  age = c(38, 51, 44)
)

stopifnot(!anyDuplicated(measure_df$participant_id))
stopifnot(!anyDuplicated(profile_df$participant_id))

matched_df <- inner_join(measure_df, profile_df, by = "participant_id")
retained_df <- left_join(measure_df, profile_df, by = "participant_id")

nrow(matched_df)
nrow(retained_df)
```

**Why it works:** An inner join keeps IDs found in both tables; a left join retains all rows of the left table and inserts `NA` when a partner is absent. When a join key repeats, the output can multiply rows. Join type is an analytical choice, not only a syntax choice.

**Mastery checkpoint:** Identify the unmatched IDs and explain why the two joins have different row counts.

## 2. Understand missingness and survey codes

`NA` means no value is present in the data field. A coded response such as "Don't Know" is an **observed category**, not the same thing as `NA`. Do not drop rows simply because one variable has a missing value; define the exclusion separately for each intended analysis.

```r
survey_df <- data.frame(
  participant_id = 1:5,
  response = c(1, 2, 9, NA, 7)
)

survey_df$response_label <- factor(
  survey_df$response,
  levels = c(1, 2, 7, 9),
  labels = c("Yes", "No", "Refused", "Don't Know")
)

table(survey_df$response_label, useNA = "always")
sum(is.na(survey_df$response_label))
```

**Why it works:** `factor()` maps source codes to readable labels while preserving missing values. The reason for an `NA` cannot be inferred from the value alone.

**Mastery checkpoint:** Distinguish an explicit refusal, an explicit unknown response, and a missing field; state which should be retained for a frequency table.

## 3. Explore distributions before fitting models

The lecture compares histograms, violin plots, and empirical cumulative distribution functions. Each represents the same numeric variable differently: frequency by interval, smoothed distribution shape, and cumulative proportion at or below a value.

```r
library(ggplot2)

set.seed(31)
toy_df <- data.frame(
  age = seq(25, 65, length.out = 25),
  measurement = 12 + seq(25, 65, length.out = 25) * 0.3 +
    rnorm(25, sd = 3)
)

ggplot(toy_df, aes(x = measurement)) +
  geom_histogram(bins = 8) +
  labs(x = "Measurement (illustrative units)", y = "Frequency") +
  theme_minimal()

ggplot(toy_df, aes(x = measurement)) +
  stat_ecdf(geom = "step") +
  labs(x = "Measurement (illustrative units)", y = "Cumulative proportion") +
  theme_minimal()
```

**Mastery checkpoint:** Explain how to read an ECDF at a given threshold and why changing histogram bins changes the display.

## 4. Read a scatter plot and fit a linear model

The lecture uses `lm()` and `geom_smooth(method = "lm")` to illustrate linear association. A linear slope has units of **outcome units per predictor unit**. A confidence band around a fitted mean is not an individual prediction interval.

```r
fit <- lm(measurement ~ age, data = toy_df)
coef(fit)

ggplot(toy_df, aes(x = age, y = measurement)) +
  geom_point(alpha = 0.7) +
  geom_smooth(method = "lm", formula = y ~ x, se = TRUE) +
  labs(
    x = "Age (years)",
    y = "Measurement (illustrative units)",
    title = "Illustrative linear relationship"
  ) +
  theme_minimal()
```

**Mastery checkpoint:** Identify the intercept and slope, state the slope's units, and name one reason an apparent trend may not be causal.

## 5. Package repeated plots into one function

A function reduces repeated editing across variables. It must accept the dataset and requested column, and should fail clearly when the column does not exist or cannot be plotted.

```r
plot_distribution <- function(data, variable) {
  stopifnot(is.character(variable), length(variable) == 1L)
  if (!variable %in% names(data)) {
    stop("Missing column: ", variable)
  }
  if (!is.numeric(data[[variable]])) {
    stop("Column must be numeric: ", variable)
  }

  ggplot(data, aes(x = .data[[variable]])) +
    geom_histogram(bins = 8) +
    labs(x = variable, y = "Frequency") +
    theme_minimal()
}

plot_distribution(toy_df, "measurement")
```

**Why it works:** `.data[[variable]]` selects a column named by a character parameter in the plotting mapping. Reusing a function is safer than copying and changing multiple nearly identical blocks.

**Mastery checkpoint:** Run the function with a valid column and predict the error with an invalid column.

## 6. Import multiple files without losing track of them

The lecture's `list.files()` and `for` loop examples generalize to reading multiple records. Use a strict CSV extension pattern, explicit paths, and a named list to avoid overwriting previous imports.

```r
data_path <- "data/authorized_practice_files"
file_paths <- list.files(
  data_path,
  pattern = "\\.csv$",
  full.names = TRUE
)
stopifnot(length(file_paths) > 0L)

tables <- lapply(file_paths, read.csv)
names(tables) <- basename(file_paths)
lapply(tables, dim)
```

**Why it works:** `lapply()` returns one object per file; naming the list helps match later output to its input. The chunk is not executed because its input folder must be supplied separately.

**Mastery checkpoint:** Verify that every loaded table has the expected columns before combining or graphing it.

## 7. Build a publication-readable figure panel

For each figure, define the scientific question first. A violin summarizes a distribution, a scatter plot shows a paired numeric relationship, and a density curve estimates its shape. The lecture's `ggpubr::ggarrange()` can combine independently built `ggplot` objects. Units, sample sizes, category labels, and missingness must be evaluated separately for each panel.

```r
p_hist <- plot_distribution(toy_df, "measurement")
p_scatter <- ggplot(toy_df, aes(age, measurement)) +
  geom_point() +
  labs(x = "Age (years)", y = "Illustrative units") +
  theme_minimal()

if (requireNamespace("ggpubr", quietly = TRUE)) {
  ggpubr::ggarrange(p_hist, p_scatter, ncol = 2)
} else {
  print(p_hist)
  print(p_scatter)
}
```

**Mastery checkpoint:** Describe what each panel reveals, why the two plots answer different questions, and whether any analyses are inferential.

## 8. Final self-check: what Week 3 mastery requires

- [ ] **Data provenance:** Read or simulate two tables and document file paths, key columns, row counts, data types, and missingness.
- [ ] **Join logic:** Demonstrate inner versus left joins, inspect duplicate keys, and account for retained or excluded records.
- [ ] **Categorical data:** Recode numeric survey responses correctly without treating refusal, "Don't Know", and `NA` as identical.
- [ ] **Visual analysis:** Produce clearly labeled frequency, cumulative, grouped distribution, and paired scatter views as appropriate.
- [ ] **Regression:** Fit and annotate a linear model; explain slope, intercept, uncertainty, and causal limitations.
- [ ] **Reusable analysis:** Write a plotting function, handle invalid inputs, and process multiple named files without accidental overwrites.
- [ ] **Publication quality:** Build a coherent multi-panel display with labels and units; account for the sample used in each plot.
- [ ] **Reproducibility:** Re-run the full workflow in order; inspect errors and verify output rather than accepting an attractive plot uncritically.

**Mastery standard:** All eight objectives demonstrated on a new dataset with correctly checked join cardinality and missing-value handling. The student can defend every plot's purpose and limitations and repeat the code without untracked manual steps.

**Related:** [Week 3 lecture chunk reference](Week_3_Data_Visualization_and_Analytics_Lecture_Reference.md) · [Week 3 group work](../03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) · [Lecture index](README.md)
