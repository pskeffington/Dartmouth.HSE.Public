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


## Genomics visualization module

Source both files, in this order:

```r
source("HSE_711/library/hse_stats_plots.R")
source("HSE_711/library/hse_gene_visuals.R")
# logcpm <- hse_cpm(counts)  # counts: integer genes x samples
# meta <- data.frame(Sample=colnames(logcpm), Subtype=...)
genes <- hse_gene_top_var(logcpm, n = 40)
p1 <- hse_gene_heatmap(logcpm, genes)           # selected genes only
p2 <- hse_gene_pca(logcpm, meta, "Subtype")     # top-500 variable genes
p3 <- hse_gene_mean_variance(logcpm)            # all genes, no long pivot
# DE model results only (not CPM):
# p4 <- hse_gene_volcano(de_table, logfc="logFC", fdr="FDR")
hse_save_plot(p1, "figures/gene_heatmap.pdf", width = 12, height = 8)
```

| Function | Purpose | Optimization |
|---|---|---|
| `hse_gene_validate` | Check matrix names/values | Lightweight sanity check |
| `hse_gene_meta` | Align sample metadata | One ID match |
| `hse_gene_top_var` | Top variable genes | Direct row variance, optional matrixStats |
| `hse_gene_heatmap` | Selected gene heatmap | Subset before reshaping; optional row z-score |
| `hse_gene_pca` | Sample PCA by metadata group | PCA over chosen top-variable genes |
| `hse_gene_mean_variance` | Mean versus variance | Row-wise summaries, no pivot |
| `hse_gene_volcano` | Model-derived differential expression | No fitting; finite display floor for adjusted p-values |

Heatmaps with `center_rows=TRUE` display within-gene *z-scores*, not abundance. Uncentered heatmaps assume the supplied matrix is **log2 CPM**. PCA is unsupervised descriptive analysis; its first two components are not inferential tests. Volcano plots require independently estimated model log-fold changes and adjusted p-values. Gene selection and plot parameters must be documented for any manuscript figure.

Performance guidance: benchmark representative samples, avoid dense conversions of sparse matrices, prefer selected panels for heatmaps, and keep model inference separate from display. `ggplot2` is required for visualization; `matrixStats` is optional for faster gene-wise variance calculations.

Run the additional tests with `Rscript --vanilla HSE_711/library/tests/test_hse_gene_visuals.R`.
