# RESOURCES — R functions, genomic graphics, and literature

This is the entry point for students and collaborators. All examples are **educational**, not diagnostic or clinical software.

## Files

### Bash programming

- [Bash literature review](Bash/BASH_LITERATURE_REVIEW.md) — annotated sources on Bash syntax, shell safety, text processing, portability and bioinformatics workflows.
- [Bash operation sheet](Bash/BASH_OPERATION_SHEET.md) — beginner-to-intermediate command reference and worked metadata exercises.
- [Reusable Bash functions](Bash/bash_functions.sh) — sourceable helpers for file validation, TSV inspection, SHA-256 and Rscript orchestration.

### R programming

- [Complete summary statistics + narrative](SUMMARY_STATISTICS.md) — IQR, quartiles, spread, sample sizes, missingness, and automatically generated reader summaries.
- [Summary statistics tests](tests/test_hse_summary_report.R) — small deterministic example and boundary checks.

- [Automatic figure annotations](PLOT_ANNOTATIONS.md) — method, sample counts, p-values, units, statistical cautions, provenance, figure audits and export manifests.
- [Annotation functions](R/hse_plot_annotations.R) — source after other plotting modules to annotate downstream one-call plots.
- [Annotation tests](tests/test_hse_plot_annotations.R) — synthetic regression, Wilcoxon, panels and export audits.

- [Biostatistics plot panels](BIOSTAT_PLOT_PANELS.md) — one-call ggplot facets, Wilcoxon panels, longitudinal and confidence-interval plots, forest, ROC, survival and model diagnostics.
- [Biostatistics panel R functions](R/hse_biostat_panels.R) — thoroughly commented source code.
- [Biostatistics plot tests](tests/test_hse_biostat_panels.R) — synthetic examples and optional-dependency checks.

- [One-call statistical graphics](ONE_CALL_PLOTS.md) — ready-made regression, Pearson/Spearman, Wilcoxon, Kruskal-Wallis and gene-expression plots, with annotated p-values.
- [One-call plotting functions](R/hse_one_call_plots.R) — reusable implementation and test-result attributes.
- [Statistical plotting smoke tests](tests/test_hse_one_call_plots.R) — synthetic-data validation script.

- [R/hse_stats_plots.R](R/hse_stats_plots.R) — descriptive statistics, Wilcoxon tests, correlation, basic plots, CPM and gene-panel preparation.
- [R/hse_gene_visuals.R](R/hse_gene_visuals.R) — selected-gene heatmaps, PCA, mean–variance plots, and model-derived volcano plots.
- [R/Week_3_Reusable_Functions.R](R/Week_3_Reusable_Functions.R) — original annotated Week 3 classroom functions.
- [tests/test_hse_stats_plots.R](tests/test_hse_stats_plots.R) and [tests/test_hse_gene_visuals.R](tests/test_hse_gene_visuals.R) — synthetic-data smoke tests.
- [Literature/literature_matrix.csv](Literature/literature_matrix.csv) — machine-readable evidence matrix.
- [Literature/LITERATURE_MATRIX.md](Literature/LITERATURE_MATRIX.md) — explanatory literature evidence and limitations.

## Quick start

From the repository root:

```r
source("RESOURCES/R/hse_stats_plots.R")
source("RESOURCES/R/hse_gene_visuals.R")
data(mtcars)
mtcars$cyl <- factor(mtcars$cyl)
hse_describe(mtcars, "mpg", "cyl")
p <- hse_box(mtcars, "mpg", "cyl")
print(p)
hse_save_plot(p, "figures/mtcars_mpg.pdf")
```

To explore real RNA-seq data, supply a named integer gene-by-sample count matrix and sample metadata. Use `hse_cpm(counts)` for **TMM-adjusted logCPM displays**; preserve raw counts and edgeR offsets for differential-expression inference.

```r
# Only after defining counts and metadata:
# logcpm <- hse_cpm(counts)
# genes <- hse_gene_top_var(logcpm, 40)
# p <- hse_gene_heatmap(logcpm, genes)
# print(p)
```

## Install optional packages

```r
install.packages("ggplot2")
# Optional faster row-wise matrix statistics:
install.packages("matrixStats")
# Bioconductor edgeR is needed for the CPM helper:
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
BiocManager::install("edgeR")
```

## Tests

```sh
Rscript --vanilla RESOURCES/tests/test_hse_stats_plots.R
Rscript --vanilla RESOURCES/tests/test_hse_gene_visuals.R
```

The tests were authored as smoke tests and must be executed in an environment with R installed before describing them as passed. Plotting checks are conditional on ggplot2; CPM checks are conditional on edgeR.

## Literature and publication standards

The literature matrix was transferred from the research literature compilation as a **bibliographic/methods resource**, not as release of private project data. Some entries discuss unpublished or internal evidence; these are annotated and **must not be presented as independently verified public results**. Always distinguish primary evidence, background sources, exploratory comparisons, and provenance exclusions.

Publication figures should have explicit assay scale, sample counts, consistent labels, reproducible code, and traceable software versions. Heatmap row z-scores are not CPM magnitudes. Volcano plots require independent model-derived logFC and adjusted p-values.

## Layout migration

Earlier paths under `HSE_711/library/` and `HSE_711/notes/` moved to `RESOURCES/R/`, `Lecture Notes/` and `Group Work/`. Source code demonstrations and file references should use the paths above.