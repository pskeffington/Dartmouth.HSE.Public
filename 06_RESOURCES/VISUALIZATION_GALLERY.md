# Scientific Visualization Gallery — Paul's Notes

[Home](../README.md) · [R functions](R/README.md) · [Figure interpretation](READING_PLOTS.md)

Six runnable examples use independently constructed synthetic observations. They illustrate graphics and statistical descriptions, not clinical evidence or institutional course solutions. Run the blocks in order from the repository root in a fresh R session with `ggplot2` installed. `matrixStats` is optional; the gene helpers have a base-R fallback.

## Choose a visual encoding

| Quantity | Encoding | Interpretation |
| --- | --- | --- |
| Categories | Okabe–Ito colors, labels and position or shape | Categories have no numeric ordering |
| Continuous magnitude | Viridis fill and a labeled colorbar | Color represents the supplied measurement scale |
| Signed deviation | Blue–neutral–red centered at an explicit midpoint | Zero must have a scientific meaning |
| Missing value | Neutral gray for mapped missing colors; explicit exclusions for absent coordinates | Missing is never zero |
| Statistical threshold categories | Labeled categorical color plus shape | Cutoffs describe supplied model results, not biological truth |

`hse_group_colors()` sorts character groups deterministically. Pass the same `levels` vector to every subset/panel, or retain the full factor levels, to keep a category's color stable when another category is absent. More than eight categories require facets or additional encodings. Accessibility also depends on size, contrast, labels and the reader's display.

## Prepare known inputs

```r
source("06_RESOURCES/R/hse_teaching_data.R")
source("06_RESOURCES/R/hse_stats_plots.R")
source("06_RESOURCES/R/hse_gene_visuals.R")
source("06_RESOURCES/R/hse_plot_annotations.R")
source("06_RESOURCES/R/hse_scientific_palette.R")
cohort <- make_teaching_cohort(n = 48L, seed = 260410L)
cohort$Creatinine[c(3, 42)] <- NA_real_
cohort$Age[7] <- NA_real_
site_levels <- levels(cohort$Site)
box_data <- cohort[is.finite(cohort$Creatinine), ]
association <- cohort[is.finite(cohort$Age) & is.finite(cohort$Creatinine), ]
stopifnot(nrow(box_data) == 46L, nrow(association) == 45L)
```

One row is one invented adult. Age is in years and serum creatinine in mg/dL. We intentionally remove two creatinine values and one separate age value to make each figure's denominator visible. No site effect was programmed. Helper sourcing installs no packages and reads no external data.

## 1. Distribution — creatinine by site

Boxes show medians and quartiles; whiskers extend to the most extreme observations within 1.5 interquartile ranges. Jittered points show measured participants. These whiskers are not confidence intervals. X-position and text identify groups even without color.

```r
p_box <- hse_box(box_data, value = "Creatinine", group = "Site",
  y_label = hse_axis_label("Serum creatinine", "mg/dL"),
  title = "Creatinine across simulated sites",
  fill_scale = hse_scale_group_fill(box_data$Site, site_levels, "Enrollment site")) +
  hse_theme_scientific() +
  ggplot2::labs(x = "Synthetic enrollment site (category)",
    subtitle = "46 of 48 measured; median and quartiles",
    caption = "Two missing creatinine values excluded. Synthetic descriptive comparison.")
print(p_box)
table(box_data$Site) # Per-site measured denominators, not just total n.
```

## 2. Association — age and creatinine

A pooled least-squares line summarizes association among 45 complete pairs. Its shaded band is a pointwise 95% confidence interval for the mean response, not a prediction interval. Colors and shapes redundantly identify sites; the model does not adjust for site.

```r
p_scatter <- ggplot2::ggplot(association,
  ggplot2::aes(x = Age, y = Creatinine, color = Site, shape = Site)) +
  ggplot2::geom_point(size = 2.2, alpha = 0.8) +
  ggplot2::geom_smooth(method = "lm", formula = y ~ x, se = TRUE,
    inherit.aes = FALSE, ggplot2::aes(x = Age, y = Creatinine), color = "#000000") +
  hse_scale_group_color(association$Site, site_levels, "Enrollment site") +
  ggplot2::scale_shape_manual(values = stats::setNames(c(16, 17, 15), site_levels),
    name = "Enrollment site") + hse_theme_scientific() +
  ggplot2::labs(title = "Age and serum creatinine",
    subtitle = "45 of 48 complete pairs; pooled linear trend",
    x = hse_axis_label("Age", "years"), y = hse_axis_label("Serum creatinine", "mg/dL"),
    caption = "Three incomplete pairs excluded. Band: 95% mean CI; no causal inference.")
print(p_scatter)
```

## 3. Continuous heatmap — expression magnitude

The 12-by-16 matrix contains finite simulated log2 CPM-like values, not observed sequencing counts or fitted differential-expression estimates. The sequential colorbar represents magnitude. Gene and sample identifiers are categorical axes, so they have no physical unit. There are no missing cells; the helper rejects nonfinite matrices.

```r
set.seed(711)
expr <- matrix(stats::rnorm(12 * 16, mean = 6, sd = 1.3), nrow = 12,
  dimnames = list(paste0("Gene_", seq_len(12)), paste0("Sample_", seq_len(16))))
p_heat <- hse_gene_heatmap(expr, genes = rownames(expr), center_rows = FALSE,
  title = "Simulated expression magnitude",
  fill_scale = hse_scale_sequential_fill("Expression", "log2 CPM-like")) +
  hse_theme_scientific() +
  ggplot2::theme(axis.text.x = ggplot2::element_text(angle = 90, hjust = 1, vjust = 0.5)) +
  ggplot2::labs(subtitle = "12 genes x 16 samples; 192 finite cells",
    x = "Synthetic sample identifier", y = "Synthetic gene identifier",
    caption = "Simulated log scale; no missing cells. Color is magnitude, not significance.")
print(p_heat)
```

## 4. Diverging heatmap — within-gene deviation

Each row is centered and divided by its sample standard deviation. Zero marks that gene's mean; the colorbar shows unitless row z-scores. This transformation changes the displayed quantity, so use it intentionally. It does not change the original matrix. Constant rows are centered to zero using divisor one; PCA separately discards constant features.

```r
p_z <- hse_gene_heatmap(expr, genes = rownames(expr), center_rows = TRUE,
  title = "Within-gene expression deviations",
  fill_scale = hse_scale_diverging_fill("Row z-score (unitless)", midpoint = 0)) +
  hse_theme_scientific() +
  ggplot2::theme(axis.text.x = ggplot2::element_text(angle = 90, hjust = 1, vjust = 0.5)) +
  ggplot2::labs(subtitle = "12 genes x 16 samples; within-row z-scores",
    x = "Synthetic sample identifier", y = "Synthetic gene identifier",
    caption = "No missing cells. Compare within-row patterns, not absolute abundances.")
print(p_z)
```

## 5. PCA — sample-level structure

The helper aligns metadata by unique sample identifiers, centers gene columns and runs unscaled PCA. Labels report each component's percentage of total variance over all components. Scores have the supplied log-scale coordinate units; percentages are dimensionless. No group effect was programmed, and separation is not a hypothesis test.

```r
metadata <- data.frame(Sample = colnames(expr),
  Group = factor(rep(c("Reference", "Comparison"), each = 8),
    levels = c("Reference", "Comparison")))
p_pca <- hse_gene_pca(expr, metadata, group = "Group", n_genes = 12L) +
  ggplot2::aes(shape = Group) +
  hse_scale_group_color(metadata$Group, name = "Synthetic group") +
  ggplot2::scale_shape_manual(values = c(Reference = 16, Comparison = 17),
    name = "Synthetic group") + hse_theme_scientific() +
  ggplot2::labs(subtitle = "16 samples, 12 features; centered, unscaled PCA",
    caption = "No missing cells. Scores on input log scale; descriptive structure only.")
print(p_pca)
```

## 6. Volcano — supplied exploratory model results

For each simulated feature, fit a two-group linear model on the log2-like scale. Its group coefficient is a model log2 fold-change-like difference; adjust the 12 coefficient p-values using Benjamini–Hochberg. This illustration is not a count-data model and does not substitute for an RNA-seq analysis. Labels and shapes distinguish whether both chosen thresholds are met. Missing coordinates are excluded explicitly rather than plotted at zero.

```r
results <- do.call(rbind, lapply(seq_len(nrow(expr)), function(i) {
  fit <- stats::lm(as.numeric(expr[i, ]) ~ metadata$Group)
  coefficient <- summary(fit)$coefficients[2, ]
  data.frame(Gene = rownames(expr)[i], logFC = unname(coefficient[1]),
    p = unname(coefficient[4]))
}))
results$FDR <- stats::p.adjust(results$p, method = "BH")
stopifnot(nrow(results) == 12L, all(is.finite(results$FDR)))
p_volcano <- hse_gene_volcano(results, gene = "Gene",
  color_scale = ggplot2::scale_color_manual(
    values = c("FALSE" = hse_okabe_ito()[["black"]], "TRUE" = hse_okabe_ito()[["vermillion"]]),
    labels = c("FALSE" = "Other", "TRUE" = "Meets cutoffs"), name = "Threshold status")) +
  hse_theme_scientific() +
  ggplot2::labs(title = "Exploratory synthetic feature contrasts",
    subtitle = "12 models; BH p < 0.05, |log2 difference| >= 1",
    x = "Model log2 fold-change-like difference (unitless)",
    y = "-log10(BH adjusted p-value) (unitless)",
    caption = "12 complete results; no exclusions. Illustration, not count-based RNA-seq inference.")
print(p_volcano)
```

Adjusted p-values equal to zero are floored only for display by the existing helper. A category may be empty with these null simulations; thresholds never guarantee discoveries.

## Export and inspect

This intentionally writes six PNG/PDF pairs and annotation manifests. Choose a writable output folder outside Git; inspect labels, legends, clipping and font rendering before sharing. PNGs use 300 dpi (7 × 5 inches gives 2100 × 1500 pixels); PDFs retain vector geometry through R's standard PDF device. Journal requirements vary. No export happens on helper load.

```r
figure_dir <- Sys.getenv("PAULS_FIGURE_DIR", unset = file.path(tempdir(), "pauls-gallery"))
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)
figures <- list(distribution = p_box, association = p_scatter,
  expression = p_heat, row_deviation = p_z, pca = p_pca, volcano = p_volcano)
for (name in names(figures)) {
  stopifnot(hse_plot_audit(figures[[name]])$pass)
  hse_save_figure(figures[[name]], file.path(figure_dir, name))
}
cat("Figure previews:", normalizePath(figure_dir), "\n")
```

Run the clean-session gallery validator with `python3 scripts/validate_visualization_gallery.py --output-dir /tmp/pauls-gallery-check`. The [palette regression test](tests/test_hse_scientific_palette.R) checks exact colors, fixed-level mapping, missing colors, heatmap transforms, PCA variance and volcano coordinates against independent expected calculations. [Resource checks](tests/README.md) cover the existing library.

## Primary references

- [Okabe and Ito: color universal design and redundant encodings](https://jfly.uni-koeln.de/color/)
- [ggplot2 viridis scales](https://ggplot2.tidyverse.org/reference/scale_viridis.html)
- [ggplot2 centered gradient scales](https://ggplot2.tidyverse.org/reference/scale_gradient.html)
- [Nature figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/)
- [Nature figure panels and export](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/)

These links provide conventions and technical references. No protected source figures are reproduced. Passing checks establishes technical behavior, not copyright clearance or validity of an underlying research design.
