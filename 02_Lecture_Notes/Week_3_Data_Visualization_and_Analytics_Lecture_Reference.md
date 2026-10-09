# HSE 711 · Week 3 learning notes

[Lecture index](README.md) · [Commented source](Week_3_Data_Visualization_and_Analytics_Lecture_Reference.R) · [Repository home](../README.md)

> **Reading edition.** Original lecture references are retained for study. The commented source runs no analysis. Code below is reference material; check paths, packages, inputs and prerequisites before using it.

Dartmouth | HSE.711 | Week 3 learning-objective notes Source: Lecture_3_Data_Visualization_and_Analytics(2).Rmd Chunk references count all 21 R chunks in source order, including setup. Entire file is commented for study; sourcing it runs no analysis. Objectives: inspect and join data; assess distributions and missingness; fit an exploratory linear model; build reusable functions; iterate files; keep named data lists; interpret annotated heatmaps. Original lecture code below is reference material, not a corrected pipeline. Data files were not attached; numeric lecture results are not reproduced.

## On this page

- [01. Prepare the session](#01-prepare-the-session)
- [02. Read SAS transport files](#02-read-sas-transport-files)
- [03. Inspect and join records](#03-inspect-and-join-records)
- [04. Explore distributions in three views](#04-explore-distributions-in-three-views)
- [05. Count missing age values](#05-count-missing-age-values)
- [06. Count missing blood pressure values](#06-count-missing-blood-pressure-values)
- [07. Define the analytic sample](#07-define-the-analytic-sample)
- [08. Inspect a continuous relationship](#08-inspect-a-continuous-relationship)
- [09. Fit and display a linear model](#09-fit-and-display-a-linear-model)
- [10. Write a reusable plotting function](#10-write-a-reusable-plotting-function)
- [11. Apply the function to other variables](#11-apply-the-function-to-other-variables)
- [12. Discover CSV files](#12-discover-csv-files)
- [13. Select a filename family](#13-select-a-filename-family)
- [14. Read each file in a loop](#14-read-each-file-in-a-loop)
- [15. Summarize each input](#15-summarize-each-input)
- [16. Repeat histograms across inputs](#16-repeat-histograms-across-inputs)
- [17. Compare distributions by sex](#17-compare-distributions-by-sex)
- [18. Style plots by race](#18-style-plots-by-race)
- [19. Pair files across cycles](#19-pair-files-across-cycles)
- [20. Combine loops with functions](#20-combine-loops-with-functions)
- [21. Draw an annotated heatmap](#21-draw-an-annotated-heatmap)

## 01. Prepare the session

**Learn:** Load packages before using their functions. tidyverse supplies wrangling and plotting; haven reads SAS transport files; ggpubr arranges panels.

**Apply:** Use at the start of an analysis. harrypotter is optional styling; gridExtra is not essential to the examples shown. Install packages separately from analysis scripts.

**Lecture reference code**

```r
## Set data path
#knitr::opts_knit$set(root.dir = "yourpath/data")

## Read in packages
library(tidyverse)   # dplyr, ggplot2, readr, tidyr, etc.
library(haven)       # read_xpt()
library(gridExtra)   # organizing plots
library(ggpubr)      # plot labels
library(harrypotter) # fun color palettes (optional)

```

## 02. Read SAS transport files

**Learn:** read_xpt() creates blood_pressure_df and demographics_df from the examination and demographic files.

**Apply:** Use for .xpt input. Relative paths depend on the working directory. Confirm actual filenames: BPXO uses the letter O, not zero.

**Lecture reference code**

```r
## Read in files
blood_pressure_df <- read_xpt("../data/BPXO_2021-2023.xpt")
demographics_df <- read_xpt("../data/DEMO_2021-2023.xpt")

```

## 03. Inspect and join records

**Learn:** glimpse() checks types and variables; inner_join(..., by = "SEQN") creates data_df using matched participant identifiers.

**Apply:** Use to connect participant tables. Check duplicate keys first: repeated SEQN values can multiply rows. Inner joins discard unmatched participants.

**Lecture reference code**

```r
## Take a look at the data
# head(blood_pressure_df) # or
blood_pressure_df %>% glimpse()
# head(demographics_df) #or
demographics_df %>% glimpse()

## Combine data frames on the SEQN (participant identifier) column, see ?merge
# data_df <- merge(demographics_df, blood_pressure_df, by = "SEQN") # Base R

# or tidy way using dplyr:
# An inner_join() only keeps observations from x that have a matching key in y.
# See ?inner_join
data_df <- demographics_df %>%
  inner_join(blood_pressure_df, by = "SEQN") 

```

## 04. Explore distributions in three views

**Learn:** p1 through p6 compare histograms, violin densities, and empirical cumulative distributions; ggarrange() combines plots.

**Apply:** Use histograms for frequencies, violins for density shape, and ECDFs for the fraction at or below a threshold. Read axis units and inspect missingness before interpreting.

**Lecture reference code**

```r
# Histogram for Age
p1 <- ggplot(data_df, aes(x = RIDAGEYR)) +
  geom_histogram(bins = 30, fill = "blue", alpha = 0.7) +
  labs(title = "Histogram of Age", 
       x = "Age", 
       y = "Frequency")

# Violin plot for Age
p2 <- ggplot(data_df, aes(x = "", y = RIDAGEYR)) +
  geom_violin(fill = "blue", alpha = 0.7) +
  labs(title = "Violin Plot of Age", 
       x = "", 
       y = "Age")

# Cumulative Distribution Function for Age
p3 <- ggplot(data_df, aes(x = RIDAGEYR)) +
  stat_ecdf(geom = "step", color = "blue") +
  labs(title = "CDF of Age", 
       x = "Age", 
       y = "Cumulative Probability")

# Arrange Age plots
ridageyr_plots <- ggarrange(p1, p2, p3, 
                            ncol = 2, 
                            nrow = 2)

# Histogram for Systolic Blood Pressure
p4 <- ggplot(data_df, aes(x = BPXOSY1)) +
  geom_histogram(bins = 30, fill = "red", alpha = 0.7) +
  labs(title = "Histogram of Systolic Blood Pressure", 
       x = "Systolic Blood Pressure", 
       y = "Frequency")

# Violin plot for Systolic Blood Pressure
p5 <- ggplot(data_df, aes(x = "", y = BPXOSY1)) +
  geom_violin(fill = "red", alpha = 0.7) +
  labs(title = "Violin Plot of Systolic Blood Pressure", 
       x = "", 
       y = "Systolic Blood Pressure")

# Cumulative Distribution Function for Systolic Blood Pressure
p6 <- ggplot(data_df, aes(x = BPXOSY1)) +
  stat_ecdf(geom = "step", color = "red") +
  labs(title = "CDF of Systolic Blood Pressure", 
       x = "Systolic Blood Pressure", 
       y = "Cumulative Probability")

# Arrange Systolic Blood Pressure plots
BPXOSY1_plots <- ggarrange(p4, p5, p6, 
                           ncol = 2, 
                           nrow = 2)

# Display plots
print(ridageyr_plots)
print(BPXOSY1_plots)

```

## 05. Count missing age values

**Learn:** sum(is.na(data_df$RIDAGEYR)) counts missing ages.

**Apply:** Use before eligibility filtering. A zero count is a dataset result, not a guarantee for future files.

**Lecture reference code**

```r
## Check how many NAs there are in the age variable
sum(is.na(data_df$RIDAGEYR))

```

## 06. Count missing blood pressure values

**Learn:** sum(is.na(data_df$BPXOSY1)) counts unavailable first systolic measurements.

**Apply:** Use to report missingness with its denominator. The lecture reports 284, but recalculate from actual files. There is no universal missingness percentage that determines whether imputation is appropriate.

**Lecture reference code**

```r
## Check for NAs in the BP variable
sum(is.na(data_df$BPXOSY1))

```

## 07. Define the analytic sample

**Learn:** filter(RIDAGEYR >= 18) and drop_na(BPXOSY1) create data_df_sub; prop_removed describes total exclusions.

**Apply:** Use to align data with adult eligibility and available outcomes. prop_removed combines age and missingness exclusions; report them separately when documenting sample flow.

**Lecture reference code**

```r
## Subset the data to remove under 18
# data_df_sub <- data_df[data_df$RIDAGEYR >= 18,]
#or
data_df_sub <- data_df %>%
  filter(RIDAGEYR >= 18)

## Subset the data to remove participants with NA values
# data_df_sub <- data_df_sub[(is.na(data_df_sub$BPXOSY1) == FALSE),]
#or
# data_df_sub <- data_df_sub %>%
#  filter(!is.na(BPXOSY1))
#or
data_df_sub <- data_df_sub %>%
  drop_na(BPXOSY1)

## Number of participants after subsetting to adults
dim(data_df_sub)
#or
data_df_sub %>% dim()

# Or more efficient and tidy, all in one step:
data_df_sub <- data_df %>% 
  filter(RIDAGEYR >= 18) %>%                     # keep adults only
  drop_na(BPXOSY1)                               # drop missing SBP
# And see proportion removed
prop_removed <- (nrow(data_df) - nrow(data_df_sub)) / nrow(data_df)

```

## 08. Inspect a continuous relationship

**Learn:** scatterp1 maps RIDAGEYR to x and BPXOSY1 to y; transparency reduces overplotting.

**Apply:** Use before fitting a model to inspect shape, spread, and unusual values. Axes should read Age (years) and Systolic blood pressure (mmHg).

**Lecture reference code**

```r
# Basic scatter plot of Systolic Blood Pressure vs Age
scatterp1 <- ggplot(data_df_sub, aes(x = RIDAGEYR, y = BPXOSY1)) +
  geom_point(alpha = 0.4, color = "blue") +  # scatterplot w/ transparency
  labs(title = "Scatter plot of Systolic Blood Pressure vs Age",
       x = "Age",
       y = "Systolic Blood Pressure") +
  theme_minimal()    
scatterp1

```

## 09. Fit and display a linear model

**Learn:** lm(BPXOSY1 ~ RIDAGEYR, data = data_df_sub) creates model; coef() supplies intercept and slope for eq_label.

**Apply:** Use for a simple linear association. Slope units are mmHg per year. geom_smooth(se = TRUE) shows uncertainty around the fitted mean, not a prediction interval for individuals. Recompute the slope; the lecture example is about 0.4. This model does not adjust for confounding or establish causation.

**Lecture reference code**

```r
# Fit linear model
model <- lm(BPXOSY1 ~ RIDAGEYR, data = data_df_sub)
# or 
# model <- data_df_sub %>%
#  lm(BPXOSY1 ~ RIDAGEYR, data = .)

# Extract coefficients
coefficients <- coef(model)
intercept <- coefficients[1]
slope <- coefficients[2]

# Create equation label text
eq_label <- paste0("y = ",
                   round(slope, 2), "x + ",
                   round(intercept, 2))

# Generate scatter plot with regression line and equation annotation
ggplot(data_df_sub, aes(x = RIDAGEYR, y = BPXOSY1)) +
  geom_point(alpha = 0.4, color = "blue") +                
  geom_smooth(method = "lm", formula = y ~ x, se = TRUE, color = "red") +   
  #, level = 0.99
  labs(title = "Systolic Blood Pressure vs Age \nwith Regression Line and Equation",
       x = "Age",
       y = "Systolic Blood Pressure") +
  annotate("text", x = Inf, y = -Inf, label = eq_label,
           hjust = 1.2, vjust = -0.2, size = 5, color = "red") +   
  theme_minimal()

```

## 10. Write a reusable plotting function

**Learn:** create_distribution_plots(data, variable, fill_color) creates p1, p2, p3 and returns plots.

**Apply:** Use when the same plot structure repeats. sym(variable) converts a string to a symbol; !! injects that symbol into aes(). It does not itself convert the string. bins controls histogram bins, not breaks. Local p1 objects stay inside the function.

**Lecture reference code**

```r
create_distribution_plots <- function(data, variable, fill_color = "blue") {
  # Histogram
  p1 <- ggplot(data, aes(x = !!sym(variable))) +
    geom_histogram(bins = 30, fill = fill_color, alpha = 0.7) +
    labs(title = paste("Histogram of", variable),
         x = variable,
         y = "Frequency")
  
  # Violin plot
  p2 <- ggplot(data, aes(x = "", y = !!sym(variable))) +
    geom_violin(fill = fill_color, alpha = 0.7) +
    labs(title = paste("Violin Plot of", variable),
         x = "",
         y = variable)
  
  # Cumulative Distribution Function
  p3 <- ggplot(data, aes(x = !!sym(variable))) +
    stat_ecdf(geom = "step", color = fill_color) +
    labs(title = paste("CDF of", variable),
         x = variable,
         y = "Cumulative Probability")
  
  # Arrange plots
  plots <- ggarrange(p1, p2, p3,
                     ncol = 2,
                     nrow = 2)
  
  return(plots)
}

# Usage example:
# For Age
ridageyr_plots <- create_distribution_plots(data_df, "RIDAGEYR", "blue")

# For Systolic Blood Pressure
BPXOSY1_plots <- create_distribution_plots(data_df, "BPXOSY1", "red")

# Display plots
print(ridageyr_plots)
print(BPXOSY1_plots)

```

## 11. Apply the function to other variables

**Learn:** Reuse create_distribution_plots() for BPXODI1 and BPXOPLS1 without copying the plotting code.

**Apply:** Use to compare diastolic pressure and pulse distributions. Check that the requested columns exist and are numeric in every input.

**Lecture reference code**

```r
## Run for diastolic blood pressure
diastolic_bp_plots <- create_distribution_plots(data_df, "BPXODI1", "orange")

## Run for heart rate
heart_rate_plots <- create_distribution_plots(data_df, "BPXOPLS1", "darkgreen")

## Print out results
print(diastolic_bp_plots)
print(heart_rate_plots)

```

## 12. Discover CSV files

**Learn:** list.files() returns filenames matching a regular expression.

**Apply:** Use pattern = "\\.csv$" in R to match a literal .csv suffix; full.names = TRUE returns usable paths. The lecture pattern ".csv" is broader than an exact extension match.

**Lecture reference code**

```r
## Using .csv as the pattern search
filenames <- list.files(path = "../data", pattern = ".csv")
print(filenames)

```

## 13. Select a filename family

**Learn:** A pattern of "sample" selects the lecture sample files.

**Apply:** Use a more specific pattern when a folder contains unrelated CSVs. Assignment columns such as Age are capitalized; lecture sample columns such as age are lowercase. R distinguishes them.

**Lecture reference code**

```r
## Using sample as the pattern search
filenames <- list.files(path = "../data", pattern = "sample")
print(filenames)

```

## 14. Read each file in a loop

**Learn:** for (file in filenames) reads the_file and prints head(the_file).

**Apply:** Use to inspect each input. head() returns six rows by default. file.path(data_path, file) avoids relying on a trailing slash. The loop overwrites the_file; use a named list when all inputs must remain available.

**Lecture reference code**

```r
data_path="../data/"
for (file in filenames){
  the_file <- read.csv(paste0(data_path,file))
  print(head(the_file))
}

```

## 15. Summarize each input

**Learn:** summary(the_file$age) describes each sample file.

**Apply:** Use to compare minima, quartiles, median, mean, maxima, and missing values. The lecture prose omits mean from its list; numeric summary() includes it.

**Lecture reference code**

```r
for (file in filenames){
  the_file <- read.csv(paste0(data_path,file))
  print(summary(the_file$age))
}

```

## 16. Repeat histograms across inputs

**Learn:** histogram is regenerated inside the loop and printed for each file.

**Apply:** Use for repeated distribution checks. aes(x = age) directly refers to the data column; the lecture age_var approach is less convenient when reusing plots with other data.

**Lecture reference code**

```r
for (file in filenames){
  the_file <- read.csv(paste0(data_path,file))
  age_var <- the_file$age
  histogram <- ggplot(the_file, aes(x = age_var)) + 
    geom_histogram(bins = 10, 
                   fill = "darkgreen", 
                   color = "black", 
                   alpha = 0.7) +
    labs(title = paste("Age Distribution -", file),
         x = "Age (years)", 
         y = "Frequency") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"),
          axis.title = element_text(face = "bold"),
          panel.grid.minor = element_blank())
  plot(histogram)
}

```

## 17. Compare distributions by sex

**Learn:** box_plot maps sex to x, age to y, and sex to fill.

**Apply:** Use for a continuous measurement grouped by category. The box spans the middle 50%; whiskers and flagged points do not define clinical abnormality. Use named palette entries to keep group colors stable.

**Lecture reference code**

```r
for (file in filenames){
  the_file <- read.csv(paste0(data_path,file))
  age_var <- the_file$age
  box_plot <- ggplot(the_file, aes(x = sex, y = age, fill = sex)) +
    geom_boxplot(alpha = 0.7, 
                 color = "black", 
                 outlier.color = "red", 
                 outlier.shape = 16,
                 width = 0.5) +
    scale_fill_manual(values = c("goldenrod1", "darkgray")) +
    labs(title = paste("Age Distribution by Sex -", file),
         x = "Sex",
         y = "Age (years)") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"),
          axis.title = element_text(face = "bold"),
          legend.position = "none", # No legend
          panel.grid.minor = element_blank())
  plot(box_plot)
}

```

## 18. Style plots by race

**Learn:** The same box plot pattern maps race to fill and applies scale_fill_hp_d().

**Apply:** Use discrete palettes for categories. This remains a box plot despite the lecture prose calling it a bar plot. Avoid treating visual differences as evidence of a causal effect.

**Lecture reference code**

```r
library(harrypotter) # for special color palettes

for (file in filenames){
  the_file <- read.csv(paste0(data_path,file))
  age_var <- the_file$age
  box_plot <- ggplot(the_file, aes(x = race, y = age, fill = race)) +
    geom_boxplot(alpha = 0.7, 
                 color = "black", 
                 outlier.color = "red", 
                 outlier.shape = 16,
                 width = 0.5) +
    scale_fill_hp_d(option = "ronweasley") +
    labs(title = paste("Age Distribution by Race -", file),
         x = "Race", 
         y = "Age (years)") +
    theme_minimal() +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"),
          axis.title = element_text(face = "bold"),
          legend.position = "none",
          panel.grid.minor = element_blank(),
          axis.text.x = element_text(angle = 45, hjust = 1))
  plot(box_plot)
}

```

## 19. Pair files across cycles

**Learn:** xpt_files are separated into bpxo_dfs and demo_dfs; corresponding files are joined into merged_dfs.

**Apply:** Use named lists and exact matching filenames; require exactly one counterpart. Do not assume three inputs or manually assign cycle names by list order. Confirm each cycle has the expected BP variables and measurement protocol before combining.

**Lecture reference code**

```r
# Set the path to the data files
data_path <- "../data"

# List all .xpt files in the directory
xpt_files <- list.files(path = data_path, pattern = ".xpt")
xpt_files
# Create empty lists to store BPXO and DEMO dataframes
bpxo_dfs <- list()
demo_dfs <- list()

# Read in BPXO and DEMO files
for (file in xpt_files) {
  # Read the file
  df <- read_xpt(file.path(data_path, file))
  
  # Separate BPXO and DEMO files
  if (grepl("BPXO", file)) {
    bpxo_dfs[[file]] <- df
  } else if (grepl("DEMO", file)) {
    demo_dfs[[file]] <- df
  }
}

# Merge corresponding BPXO and DEMO data frames
merged_dfs <- list()

for (bpxo_name in names(bpxo_dfs)) {
  # Find the corresponding DEMO file by matching years
  matching_demo <- grep(gsub("BPXO", "DEMO", bpxo_name), names(demo_dfs), value = TRUE)

  merged_dfs[[bpxo_name]] <- merge(bpxo_dfs[[bpxo_name]], 
                                          demo_dfs[[matching_demo]], 
                                          by = "SEQN")
}

names(merged_dfs) <- c("years2015-2016", "years2017-2018", "years2021-2023")

```

## 20. Combine loops with functions

**Learn:** for (df in merged_dfs) calls create_distribution_plots() for each cycle.

**Apply:** Use to repeat a consistent visualization across studies. Loop over names(merged_dfs) when titles need cycle identifiers. Classroom plots are unweighted exploration; population inference needs the relevant survey design and weights.

**Lecture reference code**

```r
## Loop through the data frames in the merged set
for (df in merged_dfs){
  print(create_distribution_plots(df, "RIDAGEYR", "#81555a"))
}

```

## 21. Draw an annotated heatmap

**Learn:** counts_subset keeps ten genes; column_ha maps Disease_Status and Sex; Heatmap() clusters gene and sample patterns.

**Apply:** Use for multivariable expression patterns. Match metadata row names to counts column names before annotation. Verify numeric counts and sample identity. Raw counts reflect library size as well as expression; normalization, transformation, and row scaling answer different questions. The first ten rows are a teaching selection, not a biological ranking.

**Lecture reference code**

```r
# load heatmap libraries
library(ComplexHeatmap)
library(circlize)

##Read in count matrix and corresponding meta data
counts <- read.csv("../data/heatmap_counts.csv", row.names = 1)
metadata <- read.csv("../data/heatmap_metadata.csv", row.names = 1)

## Selecting 10 genes
genes_to_plot <- rownames(counts)[1:10]

## Keep only the 10 genes we want
counts_subset <- counts[genes_to_plot, ]

## Heatmap annotations
column_ha <- HeatmapAnnotation(
  Disease_Status = metadata$Disease_Status,
  Sex = metadata$Sex,
  col = list(
    Disease_Status = c(Case = "red", Control = "blue"),
    Sex = c(Male = "green", Female = "purple")
  )
)

# Create heatmap
Heatmap(
  as.matrix(counts_subset),
  name = "Counts",
  top_annotation = column_ha,
  show_row_names = TRUE,
  show_column_names = TRUE,
  cluster_columns = TRUE,
  cluster_rows = TRUE,
  column_title = "Samples",
  row_title = "Genes",
  heatmap_legend_param = list(title = "Count")
)
```
