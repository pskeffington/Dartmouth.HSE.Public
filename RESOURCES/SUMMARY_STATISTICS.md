# Descriptive statistics, IQR and narrative reporting

The public library provides a one-call descriptive report that is suitable for lecture notes, assignment write-ups and gene-expression exploratory analysis.

## Load and run

```r
source("RESOURCES/R/hse_stats_plots.R")
data(mtcars)

# One call generates both the complete table and a written interpretation.
report <- hse_summary_report(mtcars, value="mpg", unit="miles per gallon")
hse_print_summary(report)

# Optional groupwise summary:
mtcars$cyl <- factor(mtcars$cyl)
by_cyl <- hse_summary_report(mtcars, "mpg", group="cyl", unit="mpg")
hse_print_summary(by_cyl)

# Reuse the quantitative results directly in charts and documents:
table <- by_cyl$statistics
paragraphs <- by_cyl$narrative
write.csv(table, "summary_statistics.csv", row.names=FALSE)
```

## Metric dictionary

| Field | Meaning |
|---|---|
| `n_total` | Records in the group before excluding missing measurements |
| `n` | Nonmissing measurements used for numerical statistics |
| `n_missing`, `pct_missing` | Count and percentage of missing measured values |
| `mean` | Arithmetic average |
| `sd` | Sample standard deviation; unavailable when n < 2 |
| `variance` | Sample variance, SD squared |
| `se` | Standard error of the sample mean, SD / sqrt(n); not a confidence interval |
| `median` | 50th percentile |
| `q1`, `q3` | 25th and 75th percentiles |
| `iqr` | **Q3 - Q1**; middle-half spread |
| `min`, `max`, `range` | Observed limits and maximum-minus-minimum |
| `p05`, `p95` | 5th and 95th percentiles |

Quartiles use the base-R `quantile(type=7)` convention. Small sample sizes, highly skewed results and extreme values deserve explicit discussion. Differences in medians or means do not, by themselves, demonstrate statistically significant group differences.

## Example narrative style

For each available group, the generator describes the observed number of records, missingness, arithmetic mean with SD (when available), median with Q1/Q3 and IQR, and observed range. The final sentence identifies the output as descriptive statistics rather than hypothesis testing. These sentences are calculated from input data, not handwritten or invented.

## Genomics

Use the report with previously validated log2 CPM from `hse_cpm()`, including only selected genes when creating a long-format expression table. State the gene, sample grouping, biological assay and transformation in manuscript text. Avoid substituting logCPM summaries for raw-count edgeR inference.

## Quality checks

```sh
Rscript --vanilla RESOURCES/tests/test_hse_summary_report.R
```

Synthetic tests cover missingness, quartiles, IQR, single-observation SD, empty groups, narratives and by-group summaries. Runtime validation is distinct from committed source code.
