# Gene plots: source hse_stats_plots.R first.
# Plot log2 CPM for exploration; keep raw counts for statistical models.

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
  sample_index <- match(colnames(expr), as.character(metadata[[sample_col]]))
  if (anyNA(sample_index)) stop("Metadata missing expression sample(s).")
  metadata[sample_index, , drop = FALSE]
}

# Stable top-variable feature choice for plots; uses row variance directly.
# Only use finite log-scale expression. Explicit gene lists take precedence.
hse_gene_top_var <- function(expr, n = 50L) {
  hse_gene_validate(expr)
  if (length(n) != 1L || !is.finite(n) || n < 1 || n != as.integer(n))
    stop("n must be a positive integer.")
  if (ncol(expr) < 2L) stop("Variance needs at least two samples.")
  gene_variance <- if (requireNamespace("matrixStats", quietly = TRUE))
    matrixStats::rowVars(expr) else apply(expr, 1L, stats::var)
  rownames(expr)[head(order(-gene_variance, rownames(expr)), min(n, nrow(expr)))]
}

# Heatmap: select genes FIRST (avoids materializing a full long table).
# center_rows=TRUE highlights within-gene sample differences. Z-scores
# are not absolute gene abundance and should be labeled accordingly.
hse_gene_heatmap <- function(expr, genes, center_rows = TRUE,
                             title = "Selected gene expression heatmap", fill_scale = NULL) {
  hse_gene_validate(expr, genes)
  hse_require_plot()
  expression_matrix <- expr[genes, , drop = FALSE]
  if (center_rows) {
    gene_mean <- rowMeans(expression_matrix)
    sd <- if (requireNamespace("matrixStats", quietly = TRUE))
      matrixStats::rowSds(expression_matrix) else apply(expression_matrix, 1L, stats::sd)
    sd[!is.finite(sd) | sd == 0] <- 1
    expression_matrix <- sweep(sweep(expression_matrix, 1L, gene_mean), 1L, sd, "/")
  }
  plot_data <- data.frame(Gene = factor(rep(rownames(expression_matrix), times = ncol(expression_matrix)),
                                 levels = rev(rownames(expression_matrix))),
                  Sample = factor(rep(colnames(expression_matrix), each = nrow(expression_matrix)),
                                  levels = colnames(expression_matrix)),
                  Value = as.vector(expression_matrix))
  ggplot2::ggplot(plot_data, ggplot2::aes(x = .data$Sample, y = .data$Gene,
                                  fill = .data$Value)) +
    ggplot2::geom_raster() +
    (if (!is.null(fill_scale)) fill_scale else if (center_rows)
      ggplot2::scale_fill_gradient2(low = "#2166AC", mid = "#F7F7F7",
                                  high = "#B2182B", midpoint = 0,
                                  na.value = "#808080", name = "Row z-score") else
      ggplot2::scale_fill_viridis_c(na.value = "#808080", name = "log2 CPM")) +
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
  aligned_metadata <- hse_gene_meta(expr, metadata, sample_col)
  genes <- hse_gene_top_var(expr, n_genes)
  expression_matrix <- t(expr[genes, , drop = FALSE])
  variable_genes <- apply(expression_matrix, 2L, stats::sd) > 0
  expression_matrix <- expression_matrix[, variable_genes, drop = FALSE]
  if (nrow(expression_matrix) < 3L || ncol(expression_matrix) < 2L)
    stop("PCA requires at least three samples and two variable genes.")
  pca_fit <- stats::prcomp(expression_matrix, center = TRUE, scale. = FALSE, rank. = 2)
  plot_data <- data.frame(PC1 = pca_fit$x[, 1], PC2 = pca_fit$x[, 2],
                  Group = as.factor(aligned_metadata[[group]]))
  explained_variance_pct <- 100 * pca_fit$sdev^2 / sum(pca_fit$sdev^2)
  ggplot2::ggplot(plot_data, ggplot2::aes(x = .data$PC1, y = .data$PC2,
                                  color = .data$Group)) +
    ggplot2::geom_point(size = 2, alpha = .8) +
    ggplot2::labs(title = "Gene expression PCA",
                  x = sprintf("PC1 (%.1f%%)", explained_variance_pct[1]),
                  y = sprintf("PC2 (%.1f%%)", explained_variance_pct[2]), color = group) +
    hse_theme()
}

# Mean-variance diagnostic: vectorized rowMeans and optional matrixStats.
# Interpret on the supplied scale (recommended: log2 CPM).
hse_gene_mean_variance <- function(expr) {
  hse_gene_validate(expr)
  if (ncol(expr) < 2L) stop("At least two samples required.")
  hse_require_plot()
  plot_data <- data.frame(mean = rowMeans(expr),
                  variance = if (requireNamespace("matrixStats", quietly = TRUE))
                    matrixStats::rowVars(expr) else apply(expr, 1L, stats::var))
  ggplot2::ggplot(plot_data, ggplot2::aes(x = .data$mean, y = .data$variance)) +
    ggplot2::geom_point(alpha = .2, size = .8) +
    ggplot2::labs(title = "Gene-level mean-variance diagnostic",
                  x = "Mean log2 CPM", y = "Variance of log2 CPM") + hse_theme()
}

# Volcano plot: input MUST contain model-derived logFC and adjusted p-values.
# This never fits a model and does not infer significance from CPM values.
# p=0 can arise from numeric underflow; floor only for display.
hse_gene_volcano <- function(results, logfc = "logFC", fdr = "FDR",
                             gene = NULL, fdr_cutoff = .05,
                             effect_cutoff = 1, color_scale = NULL) {
  hse_check_cols(results, c(logfc, fdr, gene))
  hse_numeric(results[[logfc]], logfc)
  hse_numeric(results[[fdr]], fdr)
  hse_require_plot()
  if (!is.finite(fdr_cutoff) || fdr_cutoff <= 0 || fdr_cutoff >= 1 ||
      !is.finite(effect_cutoff) || effect_cutoff < 0)
    stop("Invalid FDR or effect-size cutoff.")
  if (any(results[[fdr]] < 0 | results[[fdr]] > 1, na.rm = TRUE))
    stop("Adjusted p-values must be between 0 and 1.")
  plot_data <- data.frame(logFC = results[[logfc]],
                  FDR = results[[fdr]])
  plot_data$score <- -log10(pmax(plot_data$FDR, .Machine$double.xmin))
  plot_data$status <- !is.na(plot_data$FDR) & !is.na(plot_data$logFC) &
    plot_data$FDR < fdr_cutoff & abs(plot_data$logFC) >= effect_cutoff
  ggplot2::ggplot(plot_data, ggplot2::aes(x = .data$logFC, y = .data$score,
                                  color = .data$status, shape = .data$status)) +
    ggplot2::geom_point(alpha = .55, size = 1.1, na.rm = TRUE) +
    ggplot2::geom_vline(xintercept = c(-effect_cutoff, effect_cutoff),
                        linetype = "dashed", color = "grey60") +
    ggplot2::geom_hline(yintercept = -log10(fdr_cutoff),
                        linetype = "dashed", color = "grey60") +
    (if (!is.null(color_scale)) color_scale else
      ggplot2::scale_color_manual(values = c("FALSE" = "grey70",
                                           "TRUE" = "#2166AC"),
                                labels = c("FALSE" = "Other", "TRUE" = "Meets cutoffs"),
                                name = "Threshold status")) +
    ggplot2::scale_shape_manual(values = c("FALSE" = 16, "TRUE" = 17),
      labels = c("FALSE" = "Other", "TRUE" = "Meets cutoffs"), name = "Threshold status") +
    ggplot2::labs(title = "Differential-expression volcano",
                  x = "Model log2 fold change", y = "-log10(adjusted p-value)") +
    hse_theme()
}
