# HSE 711 | Public plotting and statistics helpers
# Copyright (c) 2026. Educational examples; not clinical software.
#
# DESIGN
# - Source this file to define functions; sourcing never loads datasets or draws figures.
# - Base R handles data checks/statistics; ggplot2 is needed ONLY when plotting.
# - Column names are passed as strings to keep calls simple for beginners.
# - Functions return values or ggplot objects; saving is a separate, explicit step.
# - Never substitute CPM for raw counts in edgeR differential-expression models.

# Validate an input data.frame and a list of column names before plotting.
hse_check_cols <- function(data, cols) {
  if (!is.data.frame(data)) stop("data must be a data.frame.", call. = FALSE)
  missing <- setdiff(cols, names(data))
  if (length(missing)) {
    stop("Missing columns: ", paste(missing, collapse = ", "), call. = FALSE)
  }
  invisible(TRUE)
}

# Validate numeric observations; missing values are permitted but are removed
# explicitly by summary/test functions. Infinite values are not permitted.
hse_numeric <- function(x, label = "x") {
  if (!is.numeric(x)) stop(label, " must be numeric.", call. = FALSE)
  if (any(is.infinite(x))) stop(label, " contains infinite values.", call. = FALSE)
  invisible(TRUE)
}

# Count nonmissing observations and report robust descriptive statistics.
# Use a data frame rather than a formatted string so results are exportable.
hse_describe <- function(data, value, group = NULL) {
  cols <- c(value, group)
  hse_check_cols(data, cols)
  hse_numeric(data[[value]], value)
  g <- if (is.null(group)) factor(rep("All", nrow(data))) else
    factor(as.character(data[[group]]), exclude = NULL)
  parts <- split(data[[value]], g, drop = TRUE)
  out <- lapply(names(parts), function(nm) {
    x <- parts[[nm]]
    x <- x[!is.na(x)]
    data.frame(group = nm, n = length(x),
               mean = if (length(x)) mean(x) else NA_real_,
               sd = if (length(x) > 1L) stats::sd(x) else NA_real_,
               median = if (length(x)) stats::median(x) else NA_real_,
               q1 = if (length(x)) as.numeric(stats::quantile(x, .25)) else NA_real_,
               q3 = if (length(x)) as.numeric(stats::quantile(x, .75)) else NA_real_,
               min = if (length(x)) min(x) else NA_real_,
               max = if (length(x)) max(x) else NA_real_)
  })
  if (!length(out)) return(data.frame(group = character(), n = integer(),
                                    mean = numeric(), sd = numeric(),
                                    median = numeric(), q1 = numeric(),
                                    q3 = numeric(), min = numeric(), max = numeric()))
  do.call(rbind, out)
}

# Two-group Wilcoxon rank-sum test for independent samples.
# It tests the distributions, not universally a difference of medians.
# Do not use it for matched samples; use hse_wilcox_paired instead.
hse_wilcox_independent <- function(data, value, group, conf_int = FALSE) {
  hse_check_cols(data, c(value, group))
  hse_numeric(data[[value]], value)
  ok <- !is.na(data[[value]]) & !is.na(data[[group]])
  d <- data[ok, , drop = FALSE]
  groups <- unique(as.character(d[[group]]))
  if (length(groups) != 2L) stop("Exactly two nonmissing groups required.")
  if (any(table(as.character(d[[group]])) < 1L)) stop("Each group needs observations.")
  d[[group]] <- factor(d[[group]], levels = sort(groups))
  stats::wilcox.test(stats::reformulate(group, response = value),
                     data = d, paired = FALSE, exact = FALSE,
                     conf.int = conf_int)
}

# Paired Wilcoxon signed-rank test. Requires an explicit subject ID.
# Only complete pairs are used; duplicate subject-by-group IDs are rejected.
hse_wilcox_paired <- function(data, value, group, id) {
  hse_check_cols(data, c(value, group, id))
  hse_numeric(data[[value]], value)
  d <- data[stats::complete.cases(data[c(value, group, id)]), , drop = FALSE]
  groups <- sort(unique(as.character(d[[group]])))
  if (length(groups) != 2L) stop("Exactly two groups required.")
  key <- paste(d[[id]], d[[group]], sep = "\r")
  if (anyDuplicated(key)) stop("Duplicate subject/group pair.")
  a <- d[d[[group]] == groups[1], c(id, value), drop = FALSE]
  b <- d[d[[group]] == groups[2], c(id, value), drop = FALSE]
  idx <- match(as.character(a[[id]]), as.character(b[[id]]))
  ok <- !is.na(idx)
  if (!any(ok)) stop("No complete matched subjects.")
  stats::wilcox.test(a[[value]][ok], b[[value]][idx[ok]],
                     paired = TRUE, exact = FALSE)
}

# Basic assumption-free Pearson or Spearman association.
# Report correlation alongside sample size and avoid causal interpretation.
hse_cor <- function(data, x, y, method = "spearman") {
  hse_check_cols(data, c(x, y))
  hse_numeric(data[[x]], x)
  hse_numeric(data[[y]], y)
  method <- match.arg(method, c("spearman", "pearson", "kendall"))
  ok <- stats::complete.cases(data[c(x, y)])
  if (sum(ok) < 3L) stop("At least three complete observations required.")
  result <- stats::cor.test(data[[x]][ok], data[[y]][ok],
                            method = method, exact = FALSE)
  list(n = sum(ok), test = result)
}

# Plotting dependency is evaluated only when a figure is requested.
hse_require_plot <- function() {
  if (!requireNamespace("ggplot2", quietly = TRUE))
    stop("Install ggplot2 first: install.packages('ggplot2')")
  invisible(TRUE)
}

# A consistent minimal publication-oriented theme. The returned theme may be
# composed with any ggplot; no global graphics settings are changed.
hse_theme <- function(base_size = 12) {
  hse_require_plot()
  ggplot2::theme_bw(base_size = base_size) +
    ggplot2::theme(panel.grid.minor = ggplot2::element_blank(),
                   plot.title.position = "plot",
                   legend.position = "bottom",
                   strip.background = ggplot2::element_rect(fill = "grey95"))
}

# Histogram of a continuous variable. The number of bins is explicit,
# making comparisons more reproducible between runs.
hse_hist <- function(data, value, bins = 30L, title = NULL) {
  hse_check_cols(data, value)
  hse_numeric(data[[value]], value)
  hse_require_plot()
  if (length(bins) != 1L || is.na(bins) || bins < 1 || bins != as.integer(bins))
    stop("bins must be a positive integer.")
  d <- data.frame(x = data[[value]])
  ggplot2::ggplot(d, ggplot2::aes(x = .data$x)) +
    ggplot2::geom_histogram(bins = bins, fill = "#3179A8", color = "white",
                            na.rm = TRUE) +
    ggplot2::labs(title = title %||% paste("Distribution of", value),
                  x = value, y = "Number of observations") + hse_theme()
}

# Boxplots with transparent points reveal sample distributions and outliers.
# A fixed seed controls jitter reproducibility where the installed ggplot2
# supports position_jitter(seed=...). Jitter is display-only.
hse_box <- function(data, value, group, y_label = value,
                    title = NULL, show_points = TRUE) {
  hse_check_cols(data, c(value, group))
  hse_numeric(data[[value]], value)
  hse_require_plot()
  d <- data.frame(value = data[[value]], group = as.factor(data[[group]]))
  p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$group, y = .data$value)) +
    ggplot2::geom_boxplot(width = .55, outlier.shape = if (show_points) NA else 19,
                          na.rm = TRUE)
  if (show_points) p <- p + ggplot2::geom_point(
    position = ggplot2::position_jitter(width = .12, height = 0, seed = 711),
    alpha = .32, size = 1)
  p + ggplot2::labs(title = title %||% paste(value, "by", group),
                    x = group, y = y_label) + hse_theme()
}

# Scatter plot with optional least-squares regression line. A fitted line
# describes association and is not evidence of causality.
hse_scatter <- function(data, x, y, group = NULL, fit = FALSE) {
  hse_check_cols(data, c(x, y, group))
  hse_numeric(data[[x]], x)
  hse_numeric(data[[y]], y)
  hse_require_plot()
  d <- data.frame(x = data[[x]], y = data[[y]])
  if (is.null(group)) {
    p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$x, y = .data$y))
  } else {
    d$group <- as.factor(data[[group]])
    p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$x, y = .data$y,
                                         color = .data$group))
  }
  p <- p + ggplot2::geom_point(alpha = .55, na.rm = TRUE)
  if (fit) p <- p + ggplot2::geom_smooth(
    data = d, mapping = ggplot2::aes(x = .data$x, y = .data$y),
    inherit.aes = FALSE, method = "lm", formula = y ~ x,
    se = TRUE, color = "black", na.rm = TRUE)
  p + ggplot2::labs(x = x, y = y, color = group) + hse_theme()
}

# CPM helper: counts are genes x samples and must be nonnegative integers.
# Normalization factors come from edgeR's TMM method; returned values are
# appropriate for EXPLORATION, not direct substitutes for NB model counts.
hse_cpm <- function(counts, log = TRUE, prior_count = 1) {
  if (!requireNamespace("edgeR", quietly = TRUE))
    stop("Install edgeR through BiocManager before using hse_cpm().")
  if (!is.matrix(counts) || !is.numeric(counts) ||
      anyNA(counts) || any(!is.finite(counts)) ||
      any(counts < 0) || any(counts != floor(counts)))
    stop("counts must be a finite nonnegative integer-valued numeric matrix.")
  if (!nrow(counts) || !ncol(counts) || any(colSums(counts) == 0))
    stop("counts require positive library sizes and nonempty dimensions.")
  if (!is.numeric(prior_count) || length(prior_count) != 1L ||
      !is.finite(prior_count) || prior_count < 0)
    stop("prior_count must be a finite nonnegative scalar.")
  dge <- edgeR::calcNormFactors(edgeR::DGEList(counts = counts))
  edgeR::cpm(dge, log = log, prior.count = prior_count,
             normalized.lib.sizes = TRUE)
}

# Turn a gene-by-sample expression matrix into a compact plotting table.
# Alignment is keyed by sample IDs rather than relying on row ordering.
# Supply a small selected gene panel to avoid unnecessary full-matrix pivots.
hse_gene_long <- function(expr, genes, metadata, sample_col = "Sample") {
  if (!is.matrix(expr) || !is.numeric(expr)) stop("expr must be a numeric matrix.")
  hse_check_cols(metadata, sample_col)
  if (is.null(rownames(expr)) || is.null(colnames(expr)))
    stop("expr must have gene and sample dimnames.")
  if (anyDuplicated(rownames(expr)) || anyDuplicated(colnames(expr)) ||
      anyDuplicated(as.character(metadata[[sample_col]])))
    stop("Gene and sample identifiers must be unique.")
  if (!all(genes %in% rownames(expr)))
    stop("Missing genes: ", paste(setdiff(genes, rownames(expr)), collapse = ", "))
  idx <- match(colnames(expr), as.character(metadata[[sample_col]]))
  if (anyNA(idx)) stop("Some expression samples are absent from metadata.")
  sub <- expr[genes, , drop = FALSE]
  # One data-frame row per (gene,sample), with matching sample metadata.
  out <- data.frame(Gene = rep(rownames(sub), times = ncol(sub)),
                    Sample = rep(colnames(sub), each = nrow(sub)),
                    Expression = as.vector(sub), stringsAsFactors = FALSE)
  extras <- metadata[idx[match(out$Sample, colnames(expr))], ,
                     drop = FALSE]
  extras[[sample_col]] <- NULL
  cbind(out, extras)
}

# Gene panel plot. Explicit scale labels avoid mixing raw CPM and logCPM.
hse_gene_panel <- function(long_data, group, scale = c("log2 CPM", "CPM")) {
  scale <- match.arg(scale)
  hse_check_cols(long_data, c("Gene", "Expression", group))
  hse_numeric(long_data$Expression, "Expression")
  p <- hse_box(long_data, "Expression", group, y_label = scale,
               title = "Gene expression by group")
  p + ggplot2::facet_wrap(~ Gene, scales = "free_y")
}

# Export a plot without modifying the current working directory or graphics
# device. Use PDF for vectors and PNG (>=300 dpi) for manuscript figures.
hse_save_plot <- function(plot, file, width = 7, height = 5, dpi = 300) {
  hse_require_plot()
  if (!inherits(plot, "ggplot")) stop("plot must be a ggplot object.")
  if (!grepl("\\.(pdf|png|svg)$", tolower(file)))
    stop("file extension must be .pdf, .png or .svg")
  if (any(!is.finite(c(width, height, dpi))) ||
      any(c(width, height, dpi) <= 0))
    stop("width, height and dpi must be positive.")
  dir.create(dirname(file), recursive = TRUE, showWarnings = FALSE)
  ggplot2::ggsave(filename = file, plot = plot, width = width,
                  height = height, units = "in", dpi = dpi)
  invisible(normalizePath(file))
}

# Replace NULL values without importing another package.
`%||%` <- function(x, y) if (is.null(x)) y else x
