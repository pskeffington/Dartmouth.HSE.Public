# Core R statistics and plotting helpers. Source once; no work runs on load.
# Inputs use column names as strings. Keep raw counts for edgeR inference.

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

# Comprehensive numerical summary. One row per group, including explicit
# missingness and robust quantiles. SD and variance are *sample* statistics.
# IQR is Q3 - Q1 using the same type=7 quantile convention as base R.
# CV and skewness are intentionally omitted: they require additional
# assumptions and can mislead on values near zero or signed scales.
hse_describe <- function(data, value, group = NULL, digits = 3L) {
  hse_check_cols(data, c(value, group))
  hse_numeric(data[[value]], value)
  if (length(digits) != 1L || is.na(digits) || digits < 0 ||
      digits != as.integer(digits)) stop("digits must be a nonnegative integer")
  if (!is.null(group) && identical(group, value))
    stop("group and value must be different columns")
  # Missing grouping labels remain visible as their own category.
  groups <- if (is.null(group)) rep("All", nrow(data)) else {
    g <- as.character(data[[group]])
    g[is.na(g)] <- "(Missing group)"
    g
  }
  levels <- unique(groups)
  # Return stable column types even for completely empty data.
  schema <- data.frame(group=character(), n_total=integer(), n=integer(),
    n_missing=integer(), pct_missing=numeric(), mean=numeric(),
    sd=numeric(), variance=numeric(), se=numeric(),
    median=numeric(), q1=numeric(), q3=numeric(), iqr=numeric(),
    min=numeric(), max=numeric(), range=numeric(),
    p05=numeric(), p95=numeric(), stringsAsFactors=FALSE)
  if (!length(levels)) return(schema)
  output <- lapply(levels, function(level) {
    raw <- data[[value]][groups == level]
    x <- raw[!is.na(raw)]
    n <- length(x); total <- length(raw)
    quant <- function(prob) if (n) as.numeric(stats::quantile(
      x, probs=prob, names=FALSE, type=7)) else NA_real_
    mu <- if (n) mean(x) else NA_real_
    sd <- if (n > 1L) stats::sd(x) else NA_real_
    q1 <- quant(.25); q3 <- quant(.75)
    data.frame(group=level, n_total=total, n=n, n_missing=total-n,
      pct_missing=if (total) 100*(total-n)/total else NA_real_,
      mean=mu, sd=sd, variance=if(n>1L) sd^2 else NA_real_,
      se=if(n>1L) sd/sqrt(n) else NA_real_,
      median=if(n) stats::median(x) else NA_real_,
      q1=q1, q3=q3, iqr=q3-q1,
      min=if(n) min(x) else NA_real_,
      max=if(n) max(x) else NA_real_,
      range=if(n) diff(range(x)) else NA_real_,
      p05=quant(.05), p95=quant(.95),
      stringsAsFactors=FALSE)
  })
  out <- do.call(rbind, output)
  rownames(out) <- NULL
  # Keep exact counts; round display-level measurements only.
  metric <- setdiff(names(out), c("group", "n_total", "n", "n_missing"))
  out[metric] <- lapply(out[metric], round, digits=digits)
  out
}

# Plain-language statistical summary for a reader. Describes the observed
# sample only; does not invent a statistical test or imply causation.
hse_describe_narrative <- function(summary, value, unit = NULL, digits = 2L) {
  needed <- c("group","n_total","n","n_missing","mean","sd",
              "median","q1","q3","iqr","min","max")
  hse_check_cols(summary, needed)
  if (!is.character(value) || length(value)!=1L || !nzchar(value))
    stop("value must identify the measured variable")
  fmt <- function(x) if(is.na(x)) "unavailable" else
    format(round(x,digits), trim=TRUE, scientific=FALSE)
  unit_label <- if (is.null(unit)) "" else paste0(" ",unit)
  vapply(seq_len(nrow(summary)), function(i) {
    s <- summary[i,,drop=FALSE]
    prefix <- paste0(value, " [", s$group, "]: ")
    if (s$n == 0L) return(paste0(prefix,"no observed measurements (",
      s$n_missing," of ",s$n_total," missing)."))
    spread <- paste0("Median ",fmt(s$median),unit_label,
      " (Q1 ",fmt(s$q1),", Q3 ",fmt(s$q3),
      "; IQR ",fmt(s$iqr),unit_label,"). ")
    average <- if (s$n > 1L) paste0("Mean ",fmt(s$mean),unit_label,
      " (SD ",fmt(s$sd),unit_label,"). ") else
      paste0("Mean ",fmt(s$mean),unit_label,"; SD unavailable (n=1). ")
    paste0(prefix,s$n," observed of ",s$n_total," (",
      s$n_missing," missing). ",average,spread,
      "Observed range ",fmt(s$min),"–",fmt(s$max),unit_label,
      ". Descriptive statistics only.")
  }, character(1))
}

# Single-call reader-facing report with numeric table + generated narrative.
# Return a list to preserve programmatic access to the exact summary.
hse_summary_report <- function(data, value, group = NULL, unit = NULL,
                               digits = 3L) {
  tab <- hse_describe(data,value,group,digits=digits)
  narrative <- hse_describe_narrative(tab,value,unit)
  list(statistics=tab, narrative=narrative)
}

# Print a report in a compact form suitable for an exploratory report.
hse_print_summary <- function(report) {
  if (!is.list(report) || is.null(report$statistics) ||
      is.null(report$narrative)) stop("Expected hse_summary_report output")
  print(report$statistics, row.names=FALSE)
  cat("\nReader summary:\n",paste(report$narrative,collapse="\n"),"\n",sep="")
  invisible(report)
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
                     data = d, exact = FALSE,
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

# Pearson or Spearman association; assumptions depend on method and design.
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
