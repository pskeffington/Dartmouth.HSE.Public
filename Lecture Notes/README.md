# Lecture Notes

Annotated course lecture notes organized by week. These are independent study materials rather than official course handouts.

## Using the descriptive-statistics library

The notes remain organized chronologically by teaching week. For clearer numerical reporting, use the [complete summary-statistics guide](../RESOURCES/SUMMARY_STATISTICS.md) and `hse_summary_report()`. It returns a table with IQR, quartiles, missingness and a short reader-facing narrative. These utilities supplement, rather than retroactively alter, original classroom examples.

```r
source("RESOURCES/R/hse_stats_plots.R")
data(mtcars)
hse_print_summary(hse_summary_report(mtcars, "mpg", unit="miles per gallon"))
```
