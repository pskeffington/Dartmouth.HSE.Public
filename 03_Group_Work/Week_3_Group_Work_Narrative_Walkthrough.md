# HSE.711 Week 3: Group Work Narrative Walkthrough

[Section index](README.md) · [Editable R Markdown](Week_3_Group_Work_Narrative_Walkthrough.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed for study and has not been executed to generate this page. Run the source chunks in order to produce and check outputs; data-dependent examples need separately supplied course files.

## On this page

- [Session checkpoints](#session-checkpoints)
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)
- [Question 4](#question-4)
- [Question 5](#question-5)
- [Scholarly reporting and reproducibility](#scholarly-reporting-and-reproducibility)
- [Continue learning](#continue-learning)

## Session checkpoints

**Goal:** simulate cohorts, reuse functions and combine files. Questions 1–4 create their own data. Question 5 needs course CSVs in `data/In-Class-Exercises`; the source skips that question when no files are found.

| Stop after | Check | Explain to a partner |
| --- | --- | --- |
| Question 1 | Bounds, rounding, units and plot labels | Which simulation choices determine the plotted values? |
| Question 2 | Named list and summaries across twenty cohorts | Why do repeated random samples give different summaries? |
| Questions 3–4 | Function inputs, returned summary and histogram bins | What can change through an argument without editing the function? |
| Question 5 | File list, combined rows, category labels and group sizes | How do you know that every intended CSV was included? |

The five question prompts below are preserved from the supplied exercise. Each walkthrough connects the task to the attached Week 3 lecture. Chunk numbers count every R chunk in source order, including setup (21 chunks total). Prior Lecture 1 and 2 references are omitted because those source files were not supplied.

Run the chunks in order. Questions 1–4 generate simulated data; Question 5 requires the actual CSVs. Set the working directory to the folder containing `data/`. The setup parameter skips Question 5 when those files are absent, so the simulation notes can still knit. This does not reproduce Question 5 results.

```r
knitr::opts_chunk$set(echo = TRUE, message = FALSE)
data_path <- "data/In-Class-Exercises"
filenames <- list.files(path = data_path, pattern = "\\.csv$", full.names = TRUE)
csv_ready <- length(filenames) > 0L
```

## Question 1

**Before you plot.** Check the simulation rules, bounds, rounding and units before reading the box plots. Sex categories demonstrate grouping here. The simulated differences do not establish biological differences.

Create a data frame of random data containing the following columns:

- Sex: Sex should have two levels: "Male" and "Female".
- Age: Age should be normally distributed with a minimum of 18 and maximum of 85 with a mean of 50 and a standard deviation of 10. 
- Platelet_Count: Platelet count should be bound between 1.35 and 3.71 (this is in billion/L). Make sure you round the resulting values to two decimal places! Check out the function `runif()` to help you generate these values. 

Once you have created this data frame, generate a box plot of platelet count values by sex. Make sure you label the x and y axes appropriately and add a title to the plot. 

We begin with one reproducible simulated cohort. `set.seed(123)` makes the random draws repeatable; `n` controls the number of rows. `Sex` is a factor with explicit levels, `Age` is drawn from a normal distribution then rounded and clipped to the required bounds, and `Platelet_Count` is drawn uniformly and rounded to two decimals. Clipping satisfies the bounds but creates a bounded approximation rather than an exact normal distribution. The realized mean and standard deviation will vary around the generating values. The platelet units follow the supplied question.

We inspect `random_data` before plotting. The `box_plot` maps sex to both the x-axis and fill, following Lecture 3, chunk 17. Named colors keep Male and Female colors stable. This is simulated data, so a difference between the boxes would not establish a biological difference.

```r
# Lecture 3, chunks 1 and 17: packages and box plots by sex.

library(ggplot2)

set.seed(123)
n <- 100

# round(..., 2) rounds the values to two decimal places.

random_data <- data.frame(
  Sex = factor(
    sample(c("Male", "Female"), n, replace = TRUE),
    levels = c("Male", "Female")
  ),
  Age = pmax(18, pmin(85, round(rnorm(n, mean = 50, sd = 10)))),
  Platelet_Count = round(runif(n, min = 1.35, max = 3.71), 2)
)

head(random_data)

str(random_data)

# Build the labeled box plot. 

box_plot <- ggplot(
  random_data,
  aes(x = Sex, y = Platelet_Count, fill = Sex)
) +
  geom_boxplot(
    alpha = 0.7,
    color = "black",
    outlier.color = "red",
    outlier.shape = 16,
    width = 0.5
  ) +
  scale_fill_manual(
    values = c("Male" = "goldenrod1", "Female" = "darkgray")
  ) +
  labs(
    title = "Platelet Count Distribution by Sex",
    x = "Sex",
    y = "Platelet Count (billion/L)"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    axis.title = element_text(face = "bold"),
    legend.position = "none",
    panel.grid.minor = element_blank()
  )

print(box_plot)
```

## Question 2

**Why replicate a simulated cohort?** Twenty simulated cohorts show how summaries vary between random draws. `lapply()` applies the same operation to every data frame, so you can compare results without maintaining twenty separate code blocks.

Use the code above to generate 20 data frames with the same specifications, then summarize `Age` in each. (Hint: `lapply()`.)

Next we retain 20 simulated cohorts in `data_list`, instead of overwriting one data frame each time. `lapply()` runs the same generator once per index and returns a list; this is an exercise extension of the iteration taught in Lecture 3, chunks 14–15. We set the seed once before the iteration so that successive cohorts use successive random draws. Setting it inside the function would repeat the same cohort.

The second `lapply()` selects `Age` from each cohort and returns its summary in `age_summary`. This follows the `summary()` operation in Lecture 3, chunk 15. Each summary contains the minimum, quartiles, median, mean, and maximum.

```r
# Lecture 3, chunks 14–15: iteration and summaries; lapply() is an exercise extension.

set.seed(123)
n <- 100

data_list <- lapply(1:20, function(i) {

  # Reuse the Question 1 generator; seed stays outside the function.

  # Assignment extension: runif() and rounding platelet counts.
  random_data <- data.frame(
    Sex = factor(
      sample(c("Male", "Female"), n, replace = TRUE),
      levels = c("Male", "Female")
    ),
    Age = pmax(18, pmin(85, round(rnorm(n, mean = 50, sd = 10)))),
    Platelet_Count = round(runif(n, min = 1.35, max = 3.71), 2)
  )

  return(random_data)
})

names(data_list) <- sprintf("cohort_%02d", seq_along(data_list))

age_summary <- lapply(data_list, function(random_data) {
  summary(random_data$Age)
})

print(age_summary)

```

## Question 3

**Reuse the method.** A function gives the same input the same treatment across datasets. State what it accepts and what it returns. For a fuller report, use the summary resources to inspect sample size, missingness, center and spread.

A reusable summary function: Using the code you generated above, generate a function that takes a continuous covariate as input and applies it to the function you used above to summarize the spread of the age variable. Apply it to `Platelet_Count`.

We now separate the summary operation from the particular variable. `summary_cov(cov)` accepts a numeric vector and returns `summary(cov)`. This follows the reusable-function pattern in Lecture 3, chunk 10, with the summary operation from chunk 15. Passing `random_data$Platelet_Count` applies the same logic to a new continuous covariate without rewriting the function.

`platelet_summary` stores one summary per cohort. A summary describes the data; it does not by itself test a difference between groups.

```r
# Lecture 3, chunks 10 and 15: reusable functions and summaries.

summary_cov <- function(cov) {
  return(summary(cov))
}

platelet_summary <- lapply(data_list, function(random_data) {
  summary_cov(random_data$Platelet_Count)
})

print(platelet_summary)

```

## Question 4

**Read the histogram.** A histogram counts observations within intervals. Compare plots using consistent bin choices, label the units and identify simulated data. A smooth-looking histogram alone does not establish normality.

Add histograms, saved to separate files: Extend the function so it also draws a histogram of the chosen covariate for each data frame and saves each plot to its own file.

We extend `summary_cov` with a file path and a readable label. The function computes the summary, opens a PNG graphics device, draws a histogram, and returns the summary. `on.exit(dev.off(), add = TRUE)` closes the device even if plotting fails. This function-and-iteration structure follows Lecture 3, chunks 10 and 16; saving with a PNG device is an exercise extension.

The output folder is created before plotting. `seq_along(data_list)` supplies a unique index for each output path, producing 20 separate PNGs. Running this chunk again replaces files with the same names. `platelet_summary` still contains the numerical results, so saving a plot does not discard the summaries.

```r
# Lecture 3, chunks 10 and 16: functions and repeated histograms.

dir.create("figures", recursive = TRUE, showWarnings = FALSE)

summary_cov <- function(cov, file, label) {

  cov_summary <- summary(cov)

  png(filename = file, width = 1800, height = 1200, res = 200)

  on.exit(dev.off(), add = TRUE)

  hist(
    cov,
    breaks = 10,
    main = paste("Distribution of", label),
    xlab = label,
    ylab = "Frequency",
    col = "lightblue",
    border = "white"
  )

  return(cov_summary)
}

platelet_summary <- lapply(seq_along(data_list), function(i) {
  summary_cov(
    cov = data_list[[i]]$Platelet_Count,
    file = file.path("figures", paste0("platelet_hist_", i, ".png")),
    label = "Platelet Count (billion/L)"
  )
})

print(platelet_summary)

```

## Question 5

**Check the inputs.** This question needs the supplied CSVs. After running it, report the imported row count, missing values, group sizes and units, then describe the figures. The public reading edition contains no computed findings for these files.

Suppose your working directory contains a folder called data/In-Class-Exercises/ with several CSV files. Each file has the same columns:
- Participant_ID: Unique patient identifier
- Sex: 2 levels - Male and Female
- Age: Normally distributed and bound between 18 and 85
- Socioeconomic_Status: 3 levels - Low, Medium, and High
- Disease_Status: 2 levels - Case and Control
- CReactive_Protein: Continuous variable  

Write an R script that does the following:

a) Use list.files() with pattern="\\.csv$" to find all CSV files in data/, read them into a named list of data frames, and then row‐bind them into one big data frame.

b) Create a box plot with Disease_Status on the x-axis and C-Reactive Protein levels on the y-axis. Add jitter to the box plots for the individual points. Make sure to color the box plots! Add appropriate titles and labels. 

c) Create a scatter plot of Age and C-Reactive_Protein. Make the "Male" points triangles and the Female points circles. Color the Cases red and the Controls blue. Make sure to add appropriate labels and titles to your graph!

Finally we replace simulated cohorts with the supplied CSV files. The question describes `data/In-Class-Exercises/`, so discovery is scoped to that folder. The exact `\.csv$` pattern selects CSV endings, and `full.names = TRUE` returns paths that `read.csv()` can use directly (Lecture 3, chunks 12 and 14). `data_list` is named by file, and `do.call(rbind, data_list)` stacks observations; row binding is an exercise extension. It differs from the participant-key joins in Lecture 3, chunks 3 and 19.

Before binding, we check for the required columns and consistent column sets. We report duplicate participant IDs for review rather than silently removing rows. Categorical levels are checked before converting to factors so unexpected spellings do not silently become missing values.

The box plot follows Lecture 3, chunk 17, with jitter added for individual observations. `outlier.shape = NA` prevents duplicate drawing of flagged observations because jitter already shows them. The scatter plot follows chunk 8 and adds separate mappings: `shape = Sex` and `color = Disease_Status`. Manual scales assign Male triangles (17), Female circles (16), Case red, and Control blue. No CRP unit is invented because the question does not specify one.

```r
# Lecture 3, chunks 12, 14, 17, and 8: discover, read, box plots, scatter plots.

# Setup ---------------------------------------------------------------
library(ggplot2)

# a) Find, read, and combine CSV files ---------------------------------
filenames <- list.files(
  path = data_path,
  pattern = "\\.csv$",
  full.names = TRUE
)

if (length(filenames) == 0) {
  stop("No CSV files found in data/In-Class-Exercises/.")
}

data_list <- lapply(filenames, function(file) {
  read.csv(file, stringsAsFactors = FALSE)
})

# Name each list element using its input path.
names(data_list) <- filenames

required_cols <- c("Participant_ID", "Sex", "Age", "Socioeconomic_Status",
                   "Disease_Status", "CReactive_Protein")
for (file in names(data_list)) {
  the_file <- data_list[[file]]
  if (!all(required_cols %in% names(the_file))) {
    stop("Missing required columns in: ", file)
  }
  if (!setequal(names(the_file), names(data_list[[1]]))) {
    stop("Inconsistent column sets in: ", file)
  }
}

data_df <- do.call(rbind, data_list)
rownames(data_df) <- NULL

# Validate category spellings before factor conversion.
for (variable in c("Sex", "Socioeconomic_Status", "Disease_Status")) {
  levels_expected <- switch(variable,
    Sex = c("Male", "Female"),
    Socioeconomic_Status = c("Low", "Medium", "High"),
    Disease_Status = c("Case", "Control")
  )
  if (any(!is.na(data_df[[variable]]) &
          !data_df[[variable]] %in% levels_expected)) {
    stop("Unexpected category in: ", variable)
  }
}
if (!is.numeric(data_df$Age) || !is.numeric(data_df$CReactive_Protein)) {
  stop("Age and CReactive_Protein must be numeric.")
}
cat("Repeated participant IDs:", sum(duplicated(data_df$Participant_ID)), "\n")

data_df$Sex <- factor(
  data_df$Sex,
  levels = c("Male", "Female")
)

data_df$Socioeconomic_Status <- factor(
  data_df$Socioeconomic_Status,
  levels = c("Low", "Medium", "High")
)

data_df$Disease_Status <- factor(
  data_df$Disease_Status,
  levels = c("Case", "Control")
)

str(data_df)

# b) Colored box plots with individual points -------------------------
box_plot <- ggplot(
  data_df,
  aes(
    x = Disease_Status,
    y = CReactive_Protein,
    fill = Disease_Status
  )
) +
  geom_boxplot(outlier.shape = NA, alpha = 0.7, width = 0.5) +
  geom_jitter(
    width = 0.15,
    height = 0,
    size = 1.5,
    alpha = 0.5
  ) +
  scale_fill_manual(values = c("Case" = "red", "Control" = "blue")) +
  labs(
    title = "C-Reactive Protein by Disease Status",
    x = "Disease Status",
    y = "C-Reactive Protein"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

print(box_plot)

# c) Scatter plot with sex shapes and disease colors ------------------
scatter_plot <- ggplot(
  data_df,
  aes(           
    x = Age,
    y = CReactive_Protein,
    shape = Sex,
    color = Disease_Status
  )
) +
  geom_point(size = 2, alpha = 0.7) +
  scale_shape_manual(values = c("Male" = 17, "Female" = 16)) +
  scale_color_manual(values = c("Case" = "red", "Control" = "blue")) +
  labs(
    title = "Age and C-Reactive Protein by Sex and Disease Status",
    x = "Age (years)",
    y = "C-Reactive Protein",
    shape = "Sex",
    color = "Disease Status"
  ) +
  theme_minimal()                          

print(scatter_plot)

```

If Question 5 is skipped, add the assignment CSVs to `data/In-Class-Exercises/` and knit again. Questions 1–4 do not require those CSVs.

For review, explain why named lists retain all cohorts, why row binding differs from joining, how a function parameter selects the measurement being summarized, and how mapped aesthetics differ from a fixed color outside `aes()`. Do not claim observed results for the CSV task until the data have been run.

## Scholarly reporting and reproducibility

A useful teaching narrative connects the **question**, the **analytic decision**, the **observed or simulated output**, and the **limits of interpretation**. When discussing a quantitative variable, use mean with standard deviation and median with Q1, Q3 and interquartile range (IQR); specify the number of nonmissing observations and the amount of missing data. The shared [descriptive statistics guide](../06_RESOURCES/SUMMARY_STATISTICS.md) provides a reusable R function and reader-facing narrative for this purpose. Figure annotations should state the variable, its units, the comparison groups, and the analytic method when applicable.

The original exercise commands remain in place for instructional comparison. Code comments explain *how* a command works; surrounding prose explains *why* the operation is appropriate, what a result would mean, and which conclusions the exercise cannot establish. All numerical interpretations require actual execution against the stated input data.

## Continue learning

[Group index](README.md) · [Plot-reading guide](../06_RESOURCES/READING_PLOTS.md) · [Previous week](Week_2_Group_Work_Narrative_Walkthrough.md) · [Next week](Week_4_Bash_Group_Work_Narrative_Walkthrough.md)
