# HSE 711: Reusable R statistics and plotting library

Source: [hse_stats_plots.R](hse_stats_plots.R). **Educational utilities, not clinical software.** Source the file in an R session to define the functions. Nothing runs automatically.

## Getting started

From the repository root:

```r
source("HSE_711/library/hse_stats_plots.R")
# Only graphing needs ggplot2: install.packages("ggplot2")
# Only RNA-seq CPM needs edgeR:
# if (!requireNamespace("BiocManager", quietly=TRUE)) install.packages("BiocManager")
# BiocManager::install("edgeR")
data(mtcars)
mtcars$cyl <- factor(mtcars$cyl)
hse_describe(mtcars, "mpg", "cyl")
p <- hse_box(mtcars, "mpg", "cyl", y_label = "Miles per gallon")
print(p)
hse_save_plot(p, "figures/cyl_mpg.pdf")
```

## Function index

| Function | What it returns | Notes |
|---|---|---|
| `hse_check_cols(data, cols)` | invisible TRUE or clear error | Explicit column validation |
| `hse_describe(data, value, group)` | Data frame of n, mean, SD, median, quartiles and range | Omit group for whole sample |
| `hse_wilcox_independent(data, value, group)` | `htest` | Independent two-group rank-sum test |
| `hse_wilcox_paired(data, value, group, id)` | `htest` | Matches observations by subject ID |
| `hse_cor(data, x, y, method)` | list of n and `htest` | Pearson, Spearman or Kendall |
| `hse_hist(data, value)` | ggplot | Histogram with controlled bins |
| `hse_box(data, value, group)` | ggplot | Box + reproducible jitter |
| `hse_scatter(data, x, y, group, fit)` | ggplot | Optional pooled linear fit |
| `hse_theme()` | ggplot theme | Consistent styling |
| `hse_cpm(counts, log, prior_count)` | expression matrix | TMM-adjusted CPM/logCPM for EDA |
| `hse_gene_long(expr, genes, metadata)` | tidy data frame | Identifier-checked gene panel |
| `hse_gene_panel(data, group, scale)` | faceted ggplot | Explicit CPM/logCPM label |
| `hse_save_plot(plot, file)` | invisible saved path | PDF, PNG, SVG |

## Gene review with actual counts

```r
# counts: integer gene x sample matrix with rownames and colnames
# metadata: data.frame with Sample (unique) and Subtype
source("HSE_711/library/hse_stats_plots.R")
logcpm <- hse_cpm(counts, log = TRUE, prior_count = 1)
genes <- intersect(c("ESR1", "PGR", "ERBB2", "MKI67"), rownames(logcpm))
stopifnot(length(genes) > 0L)
selected <- hse_gene_long(logcpm, genes, metadata, sample_col = "Sample")
fig <- hse_gene_panel(selected, group = "Subtype", scale = "log2 CPM")
hse_save_plot(fig, "figures/gene_panel.pdf", width = 9, height = 5)
```

**Important:** `hse_cpm` is for descriptive analysis, not for fitting a negative-binomial regression. Retain the raw counts, design matrix, offsets, patient pairing and metadata for `edgeR::glmQLFit` / `glmQLFTest`. The helpers make no confidence-interval or differential-expression claims.

## Testing and responsible reporting

```sh
Rscript --vanilla HSE_711/library/tests/test_hse_stats_plots.R
```

Tests exercise group statistics, independent and paired nonparametric tests, missing columns, and sample-order alignment, using built-in or synthetic data. Plot tests are conditional on having ggplot2 installed; CPM tests are conditional on edgeR. For publication, report group sample sizes, tests used, effects and uncertainty justified by the statistical design. Do not interpret a visual difference or correlation as causal.

## Useful references

- Chen, Lun & Smyth (2016), [edgeR RNA-seq workflow](https://doi.org/10.12688/f1000research.8987.2).
- Robinson & Oshlack (2010), [TMM normalization](https://doi.org/10.1186/gb-2010-11-3-r25).
- Wickham, [ggplot2: Elegant Graphics for Data Analysis](https://ggplot2-book.org/).
- Wickham, [Advanced R](https://adv-r.hadley.nz/).
- Wilke, [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/).
