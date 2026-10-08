# HSE 711 | Genomic visualization helpers (educational)
# Load AFTER hse_stats_plots.R. All functions return ggplot objects.
# Inputs: expression matrix (genes x samples), with unique dimnames.
# For RNA-seq figures use log2 CPM from hse_cpm(), never CPM as edgeR model input.
# Performance: subset rows before reshape; use matrixStats only if installed;
# PCA transposes the selected matrix, not an entire count collection.

hse_gene_validate <- function(expr, genes = NULL) {
  if (!is.matrix(expr) || !is.numeric(expr) || any(!is.finite(expr)))
    stop("expr must be a finite numeric genes-by-samples matrix.")
  if (is.null(rownames(expr)) || is.null(colnames(expr)) ||
      anyDuplicated(rownames(expr)) || anyDuplicated(colnames(expr)))
    stop("Gene and sample names must exist and be unique.")
  if (!is.null(genes) && (!length(genes) || anyDuplicated(genes) ||
                           !all(genes %in% rownames(expr))))
    stop("genes must be unique nonempty names present in expr.")
  invisible(TRUE)
}

# Align metadata by sample ID; never assume that row order matches expression.
hse_gene_meta <- function(expr, metadata, sample_col = "Sample") {
  hse_check_cols(metadata, sample_col)
  if (anyNA(metadata[[sample_col]]) ||
      anyDuplicated(as.character(metadata[[sample_col]])))
    stop("Metadata sample identifiers must be unique and nonmissing.")
  idx <- match(colnames(expr), as.character(metadata[[sample_col]]))
  if (anyNA(idx)) stop("Metadata missing expression sample(s).")
  metadata[idx, , drop = FALSE]
}

# Stable top-variable feature choice for plots; uses row variance directly.
# Only use finite log-scale expression. Explicit gene lists take precedence.
hse_gene_top_var <- function(expr, n = 50L) {
  hse_gene_validate(expr)
  if (length(n) != 1L || !is.finite(n) || n < 1 || n != as.integer(n))
    stop("n must be a positive integer.")
  if (ncol(expr) < 2L) stop("Variance needs at least two samples.")
  v <- if (requireNamespace("matrixStats", quietly = TRUE))
    matrixStats::rowVars(expr) else apply(expr, 1L, stats::var)
  rownames(expr)[head(order(-v, rownames(expr)), min(n, nrow(expr)))]
}

# Heatmap: select genes FIRST (avoids materializing a full long table).
# center_rows=TRUE highlights within-gene sample differences. Z-scores
# are not absolute gene abundance and should be labeled accordingly.
hse_gene_heatmap <- function(expr, genes, center_rows = TRUE,
                             title = "Selected gene expression heatmap") {
  hse_gene_validate(expr, genes)
  hse_require_plot()
  m <- expr[genes, , drop = FALSE]
  if (center_rows) {
    mu <- rowMeans(m)
    sd <- if (requireNamespace("matrixStats", quietly = TRUE))
      matrixStats::rowSds(m) else apply(m, 1L, stats::sd)
    sd[!is.finite(sd) | sd == 0] <- 1
    m <- sweep(sweep(m, 1L, mu), 1L, sd, "/")
  }
  d <- data.frame(Gene = factor(rep(rownames(m), times = ncol(m)),
                                 levels = rev(rownames(m))),
                  Sample = factor(rep(colnames(m), each = nrow(m)),
                                  levels = colnames(m)),
                  Value = as.vector(m))
  ggplot2::ggplot(d, ggplot2::aes(x = .data$Sample, y = .data$Gene,
                                  fill = .data$Value)) +
    ggplot2::geom_raster() +
    ggplot2::scale_fill_gradient2(low = "#2166AC", mid = "white",
                                  high = "#B2182B", midpoint = 0,
                                  name = if (center_rows) "Row z-score" else "log2 CPM") +
    ggplot2::labs(title = title, x = "Sample", y = "Gene") +
    hse_theme() + ggplot2::theme(axis.text.x =
                                  ggplot2::element_text(angle = 90, hjust = 1, vjust = .5))
}

# PCA: select top-variable genes, then center gene columns across samples.
# Constant genes are discarded to avoid singular/undefined scaling.
# PCA is descriptive; biological group differences are not hypothesis tests.
hse_gene_pca <- function(expr, metadata, group, n_genes = 500L,
                         sample_col = "Sample") {
  hse_gene_validate(expr)
  hse_check_cols(metadata, c(sample_col, group))
  hse_require_plot()
  md <- hse_gene_meta(expr, metadata, sample_col)
  genes <- hse_gene_top_var(expr, n_genes)
  m <- t(expr[genes, , drop = FALSE])
  ok <- apply(m, 2L, stats::sd) > 0
  m <- m[, ok, drop = FALSE]
  if (nrow(m) < 3L || ncol(m) < 2L)
    stop("PCA requires at least three samples and two variable genes.")
  fit <- stats::prcomp(m, center = TRUE, scale. = FALSE, rank. = 2)
  d <- data.frame(PC1 = fit$x[, 1], PC2 = fit$x[, 2],
                  Group = as.factor(md[[group]]))
  pct <- 100 * fit$sdev^2 / sum(fit$sdev^2)
  ggplot2::ggplot(d, ggplot2::aes(x = .data$PC1, y = .data$PC2,
                                  color = .data$Group)) +
    ggplot2::geom_point(size = 2, alpha = .8) +
    ggplot2::labs(title = "Gene expression PCA",
                  x = sprintf("PC1 (%.1f%%)", pct[1]),
                  y = sprintf("PC2 (%.1f%%)", pct[2]), color = group) +
    hse_theme()
}

# Mean-variance diagnostic: vectorized rowMeans and optional matrixStats.
# Interpret on the supplied scale (recommended: log2 CPM).
hse_gene_mean_variance <- function(expr) {
  hse_gene_validate(expr)
  if (ncol(expr) < 2L) stop("At least two samples required.")
  hse_require_plot()
  d <- data.frame(mean = rowMeans(expr),
                  variance = if (requireNamespace("matrixStats", quietly = TRUE))
                    matrixStats::rowVars(expr) else apply(expr, 1L, stats::var))
  ggplot2::ggplot(d, ggplot2::aes(x = .data$mean, y = .data$variance)) +
    ggplot2::geom_point(alpha = .2, size = .8) +
    ggplot2::labs(title = "Gene-level mean-variance diagnostic",
                  x = "Mean log2 CPM", y = "Variance of log2 CPM") + hse_theme()
}

# Volcano plot: input MUST contain model-derived logFC and adjusted p-values.
# This never fits a model and does not infer significance from CPM values.
# p=0 can arise from numeric underflow; floor only for display.
hse_gene_volcano <- function(results, logfc = "logFC", fdr = "FDR",
                             gene = NULL, fdr_cutoff = .05,
                             effect_cutoff = 1) {
  hse_check_cols(results, c(logfc, fdr, gene))
  hse_numeric(results[[logfc]], logfc)
  hse_numeric(results[[fdr]], fdr)
  hse_require_plot()
  if (!is.finite(fdr_cutoff) || fdr_cutoff <= 0 || fdr_cutoff >= 1 ||
      !is.finite(effect_cutoff) || effect_cutoff < 0)
    stop("Invalid FDR or effect-size cutoff.")
  if (any(results[[fdr]] < 0 | results[[fdr]] > 1, na.rm = TRUE))
    stop("Adjusted p-values must be between 0 and 1.")
  d <- data.frame(logFC = results[[logfc]],
                  FDR = results[[fdr]])
  d$score <- -log10(pmax(d$FDR, .Machine$double.xmin))
  d$status <- !is.na(d$FDR) & !is.na(d$logFC) &
    d$FDR < fdr_cutoff & abs(d$logFC) >= effect_cutoff
  ggplot2::ggplot(d, ggplot2::aes(x = .data$logFC, y = .data$score,
                                  color = .data$status)) +
    ggplot2::geom_point(alpha = .55, size = 1.1, na.rm = TRUE) +
    ggplot2::geom_vline(xintercept = c(-effect_cutoff, effect_cutoff),
                        linetype = "dashed", color = "grey60") +
    ggplot2::geom_hline(yintercept = -log10(fdr_cutoff),
                        linetype = "dashed", color = "grey60") +
    ggplot2::scale_color_manual(values = c("FALSE" = "grey70",
                                           "TRUE" = "#2166AC"),
                                labels = c("FALSE" = "Other", "TRUE" = "Meets cutoffs"),
                                name = NULL) +
    ggplot2::labs(title = "Differential-expression volcano",
                  x = "Model log2 fold change", y = "-log10(adjusted p-value)") +
    hse_theme()
}
