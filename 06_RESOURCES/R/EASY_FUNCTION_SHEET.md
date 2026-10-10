# Easy R function sheet

[Resource index](../README.md) · [Follow-along guide](../../FOLLOW_ALONG.md) · [Reusable source](Week_3_Reusable_Functions.R)

Run these examples in R or RStudio from the **repository root**. Column names are case-sensitive. The [synthetic cohort generator](hse_teaching_data.R) supplies every input using base R. Its 48 invented adult participants demonstrate biomedical methods; they are not patient data. Age is years, creatinine mg/dL, albumin g/dL, RBC count 10^12 cells/L, and WBC count 10^9 cells/L. Sex and collection site are fictional categories. No sex or site effect is programmed; the age–creatinine association is a chosen simulation rule.

## Inspect before analyzing

```r
source("06_RESOURCES/R/hse_teaching_data.R")
health_data <- make_teaching_cohort()
head(health_data)
str(health_data)
dim(health_data)
names(health_data)
```

**Check:** `dim(health_data)` should report 48 rows and 8 columns. `str()` shows the type of each column.

| Goal | Command | What it tells you |
| --- | --- | --- |
| Preview records | `head(health_data)` | First six rows; not the full dataset |
| Check column types | `str(health_data)` | Structure and storage types |
| Count rows / columns | `dim(health_data)` | Dataset dimensions |
| Find missing values | `sum(is.na(health_data$Creatinine))` | Number missing in one column |
| Count categories | `table(health_data$Sex, useNA = "ifany")` | Records per category, including missing values |
| Summarize a numeric column | `summary(health_data$Creatinine)` | Range, quartiles, median and mean |
| Mean / spread | `mean(health_data$Creatinine, na.rm = TRUE)` / `sd(health_data$Creatinine, na.rm = TRUE)` | Average and standard deviation |
| Keep selected rows | `subset(health_data, Sex == "Female")` | Participants in a recorded category |
| Save a table | `write.csv(health_data, tempfile(fileext = ".csv"), row.names = FALSE)` | Writes to a fresh temporary CSV; record its path if you need it later |

## Load the reusable functions once

Install `ggplot2` once with `install.packages("ggplot2")` in the Console if needed. Then:

```r
source("06_RESOURCES/R/Week_3_Reusable_Functions.R")
summary_cov(health_data$Creatinine)
```

`source()` defines the four helpers below. Pass column names as quoted strings. `summary_cov()` takes the numeric vector itself.

| Function | Minimal call | Purpose |
| --- | --- | --- |
| `summary_cov()` | `summary_cov(health_data$Creatinine)` | Numerical summary of one vector |
| `plt_hist()` | `plt_hist(health_data, "Creatinine")` | Frequencies across numeric bins |
| `plt_box()` | `plt_box(health_data, "Sex", "Creatinine")` | Group medians, spread and individual points |
| `plt_scatter()` | `plt_scatter(health_data, "Age", "Creatinine")` | Relationship between two numeric measurements |

## Three graphs you can explain

```r
hist_plot <- plt_hist(
  health_data, "Creatinine", bins = 10,
  label = "Creatinine (mg/dL)",
  title = "Synthetic creatinine distribution"
)
print(hist_plot)

box_plot <- plt_box(
  health_data, "Sex", "Creatinine",
  label = "Creatinine (mg/dL)",
  title = "Synthetic creatinine by recorded sex category"
)
print(box_plot)

scatter_plot <- plt_scatter(
  health_data, "Age", "Creatinine", color_var = "Sex", fit = FALSE,
  x_label = "Age (years)",
  y_label = "Creatinine (mg/dL)",
  title = "Synthetic age and creatinine"
)
print(scatter_plot)
```

**Histogram:** each bar counts observations in an interval. Changing `bins` changes the visual detail; compare several settings before describing shape.

**Box plot:** the middle line is the median; the box spans the middle half of values. The helper overlays points and hides duplicate outlier symbols. Compare centers, spread and overlap; the graph does not itself test a difference.

**Scatter plot:** each point is one invented participant. Read age horizontally and creatinine vertically. Color identifies the recorded sex category. Setting `fit = TRUE` adds one pooled linear regression line with a confidence band, even when points have groups. That line is an exploratory association.

## Use the same calls with your own data

Replace `health_data` and the quoted columns with your actual data frame and field names. Check `names(your_data)` first. Use independently prepared or authorized inputs and document their provenance. Choose fields and units from your dataset's dictionary. The practice generator's ranges are not diagnostic boundaries.

For longer reports, see [summary statistics](../SUMMARY_STATISTICS.md), [one-call statistical plots](../ONE_CALL_PLOTS.md) and [plot annotations](../PLOT_ANNOTATIONS.md). Report units, sample sizes and missingness alongside every shared graph.
