# Easy R function sheet

[Resource index](../README.md) · [Follow-along guide](../../FOLLOW_ALONG.md) · [Reusable source](Week_3_Reusable_Functions.R)

Run these examples in RStudio from the **repository root**. Column names are case-sensitive. The example uses R's built-in `mtcars`, so it needs no course files. It is a practice dataset of cars; its patterns are not health findings.

## Inspect before analyzing

```r
data(mtcars)
car_data <- mtcars
head(car_data)
str(car_data)
dim(car_data)
names(car_data)
```

**Check:** `dim(car_data)` should report 32 rows and 11 columns. `str()` shows the type of each column.

| Goal | Command | What it tells you |
| --- | --- | --- |
| Preview records | `head(car_data)` | First six rows; not the full dataset |
| Check column types | `str(car_data)` | Structure and storage types |
| Count rows / columns | `dim(car_data)` | Dataset dimensions |
| Find missing values | `sum(is.na(car_data$mpg))` | Number missing in one column |
| Count categories | `table(car_data$cyl, useNA = "ifany")` | Records per category, including missing values |
| Summarize a numeric column | `summary(car_data$mpg)` | Range, quartiles, median and mean |
| Mean / spread | `mean(car_data$mpg, na.rm = TRUE)` / `sd(car_data$mpg, na.rm = TRUE)` | Average and standard deviation |
| Keep selected rows | `subset(car_data, cyl == 4)` | Cars meeting the condition |
| Save a table | `write.csv(car_data, "cars_practice.csv", row.names = FALSE)` | Writes a CSV in the working directory; overwrites that filename if present |

## Load the reusable functions once

Install `ggplot2` once with `install.packages("ggplot2")` in the Console if needed. Then:

```r
source("06_RESOURCES/R/Week_3_Reusable_Functions.R")
car_data$cyl_group <- factor(car_data$cyl)
summary_cov(car_data$mpg)
```

`source()` defines the four helpers below. Pass column names as quoted strings. `summary_cov()` takes the numeric vector itself.

| Function | Minimal call | Purpose |
| --- | --- | --- |
| `summary_cov()` | `summary_cov(car_data$mpg)` | Numerical summary of one vector |
| `plt_hist()` | `plt_hist(car_data, "mpg")` | Frequencies across numeric bins |
| `plt_box()` | `plt_box(car_data, "cyl_group", "mpg")` | Group medians, spread and individual points |
| `plt_scatter()` | `plt_scatter(car_data, "wt", "mpg")` | Relationship between two numeric measurements |

## Three graphs you can explain

```r
hist_plot <- plt_hist(
  car_data, "mpg", bins = 10,
  label = "Fuel economy (miles per gallon)",
  title = "Distribution of fuel economy"
)
print(hist_plot)

box_plot <- plt_box(
  car_data, "cyl_group", "mpg",
  label = "Fuel economy (miles per gallon)",
  title = "Fuel economy by cylinder count"
)
print(box_plot)

scatter_plot <- plt_scatter(
  car_data, "wt", "mpg", color_var = "cyl_group", fit = FALSE,
  x_label = "Vehicle weight (1,000 lb)",
  y_label = "Fuel economy (miles per gallon)",
  title = "Vehicle weight and fuel economy"
)
print(scatter_plot)
```

**Histogram:** each bar counts observations in an interval. Changing `bins` changes the visual detail; compare several settings before describing shape.

**Box plot:** the middle line is the median; the box spans the middle half of values. The helper overlays points and hides duplicate outlier symbols. Compare centers, spread and overlap; the graph does not itself test a difference.

**Scatter plot:** each point is one car. Read weight horizontally and fuel economy vertically. Color identifies cylinder count. Setting `fit = TRUE` adds one pooled linear regression line with a confidence band, even when points have groups. That line is an exploratory association.

## Use the same calls with your own data

Replace `car_data` and the quoted columns with your actual data frame and field names. Check `names(your_data)` first. Use independently prepared or authorized inputs and document their provenance. Columns from another dataset will differ from those in `mtcars`; choose them from that dataset's documentation.

For longer reports, see [summary statistics](../SUMMARY_STATISTICS.md), [one-call statistical plots](../ONE_CALL_PLOTS.md) and [plot annotations](../PLOT_ANNOTATIONS.md). Report units, sample sizes and missingness alongside every shared graph.
