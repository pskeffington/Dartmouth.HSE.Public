# Biostatistics and faceted ggplot2 helpers.
# Source hse_stats_plots.R and hse_one_call_plots.R first.
# Optional packages: pROC and survival.

hse_panel <- function(plot, facet, column = NULL, ncol = 3L,
                      scales = c("fixed", "free_y", "free_x", "free")) {
  hse_require_plot()
  if (!inherits(plot, "ggplot")) stop("plot must be a ggplot object")
  scales <- match.arg(scales)
  if (!is.character(facet) || length(facet) != 1L || !nzchar(facet))
    stop("facet must be a single column name")
  # ggplot2 stores the source data in plot$data; validate both facet keys.
  hse_check_cols(plot$data, c(facet, column))
  if (is.null(column)) {
    if (!is.numeric(ncol) || length(ncol) != 1L ||
        !is.finite(ncol) || ncol < 1 || ncol != as.integer(ncol))
      stop("ncol must be a positive integer")
    return(plot + ggplot2::facet_wrap(ggplot2::vars(.data[[facet]]),
                                     ncol = ncol, scales = scales))
  }
  plot + ggplot2::facet_grid(rows = ggplot2::vars(.data[[facet]]),
                             cols = ggplot2::vars(.data[[column]]),
                             scales = scales)
}

# Single call: a boxplot with patient or subgroup facets.
# Statistics belong to the underlying comparison; no pooled p-value is
# recycled across panels. Use hse_plot_panel_wilcox for panelwise p-values.
hse_plot_panel_box <- function(data, value, group, facet,
                               scales = "fixed", ncol = 3L) {
  hse_check_cols(data, c(value, group, facet))
  hse_numeric(data[[value]], value)
  hse_require_plot()
  d <- data.frame(Value = data[[value]],
                  Group = factor(data[[group]]),
                  Panel = factor(data[[facet]]))
  p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$Group, y = .data$Value)) +
    ggplot2::geom_boxplot(width = 0.6, outlier.shape = NA, na.rm = TRUE) +
    ggplot2::geom_point(position = ggplot2::position_jitter(
      width = .12, height = 0, seed = 711), alpha = .32, size = 1,
      na.rm = TRUE) + ggplot2::labs(x = group, y = value,
                                   title = paste(value, "by", group)) + hse_theme()
  hse_panel(p, "Panel", ncol = ncol, scales = scales)
}

# Faceted pairwise Wilcoxon panels. Each facet is tested separately and
# requires exactly two observed groups and >=1 valid sample in each.
# P-values are BH-adjusted across all facet tests, not independently.
hse_plot_panel_wilcox <- function(data, value, group, facet,
                                  p_adjust = "BH", ncol = 3L) {
  hse_check_cols(data, c(value, group, facet))
  hse_numeric(data[[value]], value)
  hse_require_plot()
  p_adjust <- match.arg(p_adjust, stats::p.adjust.methods)
  d <- data[stats::complete.cases(data[c(value, group, facet)]), , drop = FALSE]
  keys <- unique(as.character(d[[facet]]))
  if (!length(keys)) stop("No complete facet groups")
  result <- lapply(keys, function(k) {
    z <- d[as.character(d[[facet]]) == k, , drop = FALSE]
    groups <- unique(as.character(z[[group]]))
    if (length(groups) != 2L)
      stop("Each facet must contain two observed groups: ", k)
    tst <- hse_wilcox_independent(z, value, group)
    data.frame(Panel = k, n = nrow(z), p = tst$p.value)
  })
  tab <- do.call(rbind, result)
  tab$p_adjusted <- stats::p.adjust(tab$p, method = p_adjust)
  tab$PanelLabel <- sprintf("%s | n=%d | adj p=%.3g",
                            tab$Panel, tab$n, tab$p_adjusted)
  label_map <- stats::setNames(tab$PanelLabel, tab$Panel)
  d$PanelLabel <- factor(label_map[as.character(d[[facet]])],
                         levels = tab$PanelLabel)
  p <- ggplot2::ggplot(d, ggplot2::aes(x = .data[[group]], y = .data[[value]])) +
    ggplot2::geom_boxplot(outlier.shape = NA, na.rm = TRUE) +
    ggplot2::geom_point(position = ggplot2::position_jitter(
      width = .12, height = 0, seed = 711), alpha = .35, size = 1,
      na.rm = TRUE) +
    ggplot2::facet_wrap(ggplot2::vars(.data$PanelLabel), ncol = ncol) +
    ggplot2::labs(x = group, y = value,
                  title = "Facet-wise Wilcoxon comparisons",
                  subtitle = paste("P adjustment across facets:", p_adjust)) + hse_theme()
  attr(p, "hse_tests") <- tab
  p
}

# Longitudinal patient trajectories: separate within-ID lines, never connect
# observations from different subjects. Repeated time per ID is rejected.
hse_plot_trajectory <- function(data, id, time, value, group = NULL) {
  hse_check_cols(data, c(id, time, value, group))
  hse_numeric(data[[value]], value)
  hse_require_plot()
  d <- data[stats::complete.cases(data[c(id, time, value, group)]), , drop = FALSE]
  if (anyDuplicated(paste(d[[id]], d[[time]], sep = "\r")))
    stop("Duplicate subject/time observations")
  d$.hse_id <- factor(d[[id]])
  d$.hse_time <- d[[time]]
  d$.hse_value <- d[[value]]
  p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$.hse_time,
    y = .data$.hse_value, group = .data$.hse_id)) +
    ggplot2::geom_line(alpha = .3) + ggplot2::geom_point(alpha = .5, size = .9) +
    ggplot2::labs(x = time, y = value, title = "Individual longitudinal trajectories") +
    hse_theme()
  if (!is.null(group)) {
    d$.hse_group <- factor(d[[group]])
    p <- ggplot2::ggplot(d, ggplot2::aes(x = .data$.hse_time,
      y = .data$.hse_value, group = .data$.hse_id, color = .data$.hse_group)) +
      ggplot2::geom_line(alpha = .3) + ggplot2::geom_point(alpha = .55, size = .9) +
      ggplot2::labs(x = time, y = value, color = group,
                    title = "Individual longitudinal trajectories") + hse_theme()
  }
  p
}

# Group mean with a classical t-based 95% confidence interval at each time.
# These are descriptive cross-sectional CIs, NOT repeated-measures model CIs.
hse_plot_mean_ci <- function(data, time, value, group = NULL,
                             conf_level = .95) {
  hse_check_cols(data, c(time, value, group))
  hse_numeric(data[[value]], value)
  hse_require_plot()
  if (!is.numeric(conf_level) || length(conf_level) != 1L ||
      !is.finite(conf_level) || conf_level <= 0 || conf_level >= 1)
    stop("conf_level must be between 0 and 1")
  d <- data[stats::complete.cases(data[c(time, value, group)]), , drop = FALSE]
  d$hse_group <- if (is.null(group)) "All" else as.character(d[[group]])
  key <- interaction(d[[time]], d$hse_group, drop = TRUE)
  idx <- split(seq_len(nrow(d)), key)
  tab <- do.call(rbind, lapply(idx, function(ii) {
    x <- d[[value]][ii]
    n <- length(x)
    if (n < 2L) stop("Each time-by-group cell needs at least two observations")
    m <- mean(x); se <- stats::sd(x) / sqrt(n)
    half <- stats::qt((1 + conf_level)/2, df = n - 1) * se
    data.frame(time = d[[time]][ii[1]], group = d$hse_group[ii[1]],
               n = n, mean = m, low = m-half, high = m+half)
  }))
  p <- ggplot2::ggplot(tab, ggplot2::aes(x = .data$time, y = .data$mean,
    color = .data$group, group = .data$group)) +
    ggplot2::geom_line() + ggplot2::geom_point() +
    ggplot2::geom_errorbar(ggplot2::aes(ymin = .data$low, ymax = .data$high),
                            width = .1) +
    ggplot2::labs(x = time, y = paste("Mean", value),
                  title = sprintf("Group means with %.0f%% t confidence intervals",
                                  100*conf_level), color = group) + hse_theme()
  attr(p, "hse_summary") <- tab
  p
}

# Forest plot for *already estimated* effects and compatible confidence limits.
# A zero reference is used for additive/log effects; a one reference for ratios.
hse_plot_forest <- function(data, label, estimate, lower, upper,
                            reference = 0, x_label = "Estimated effect") {
  hse_check_cols(data, c(label, estimate, lower, upper))
  for (nm in c(estimate, lower, upper)) hse_numeric(data[[nm]], nm)
  hse_require_plot()
  d <- data.frame(term = as.character(data[[label]]),
                  estimate = data[[estimate]], low = data[[lower]],
                  high = data[[upper]])
  if (anyNA(d) || any(d$low > d$estimate | d$high < d$estimate))
    stop("Complete intervals must include their point estimates")
  if (anyDuplicated(d$term)) stop("Forest plot labels must be unique")
  d$term <- factor(d$term, levels = rev(d$term))
  ggplot2::ggplot(d, ggplot2::aes(x = .data$estimate, y = .data$term)) +
    ggplot2::geom_vline(xintercept = reference, linetype = "dashed",
                        color = "grey55") +
    ggplot2::geom_errorbar(ggplot2::aes(xmin = .data$low,
                                      xmax = .data$high), width = .18, orientation = "y") +
    ggplot2::geom_point(size = 2.1) +
    ggplot2::labs(x = x_label, y = NULL, title = "Effect estimates and intervals") +
    hse_theme()
}

# Diagnostic residual-versus-fitted plot and normal Q-Q panel from an
# existing lm object. No refitting or inference is performed.
hse_plot_lm_diagnostics <- function(model) {
  if (!inherits(model, "lm")) stop("model must be an lm object")
  hse_require_plot()
  d <- data.frame(Fitted = stats::fitted(model), Residual = stats::residuals(model))
  q <- stats::qqnorm(d$Residual, plot.it = FALSE)
  d2 <- rbind(data.frame(X = d$Fitted, Y = d$Residual, Panel = "Residual vs fitted"),
              data.frame(X = q$x, Y = q$y, Panel = "Normal Q-Q"))
  ggplot2::ggplot(d2, ggplot2::aes(x = .data$X, y = .data$Y)) +
    ggplot2::geom_point(alpha = .55, size = 1.2) +
    ggplot2::facet_wrap(ggplot2::vars(.data$Panel), scales = "free") +
    ggplot2::labs(title = "Linear model diagnostics",
                  x = "Fitted value or theoretical quantile",
                  y = "Residual or sample quantile") + hse_theme()
}

# ROC curve from a binary observed outcome and numeric prediction score.
# Specify the positive class explicitly; a higher score must mean
# higher predicted probability/risk for the positive class.
hse_plot_roc <- function(data, outcome, score, positive) {
  hse_check_cols(data, c(outcome, score))
  hse_numeric(data[[score]], score)
  hse_require_plot()
  if (!requireNamespace("pROC", quietly = TRUE))
    stop("Install pROC before requesting an ROC plot")
  d <- data[stats::complete.cases(data[c(outcome, score)]), , drop = FALSE]
  lev <- unique(as.character(d[[outcome]]))
  if (length(lev) != 2L || length(positive) != 1L ||
      !positive %in% lev) stop("Supply positive class from binary outcome")
  response <- as.integer(as.character(d[[outcome]]) == positive)
  roc <- pROC::roc(response, d[[score]], levels = c(0, 1),
                   direction = "<", quiet = TRUE)
  xy <- pROC::coords(roc, "all", ret = c("specificity", "sensitivity"),
                     transpose = FALSE)
  xy <- as.data.frame(xy)
  xy$fpr <- 1 - xy$specificity
  auc <- as.numeric(pROC::auc(roc))
  p <- ggplot2::ggplot(xy, ggplot2::aes(x = .data$fpr,
                                       y = .data$sensitivity)) +
    ggplot2::geom_line(color = "#2166AC") +
    ggplot2::geom_abline(slope = 1, intercept = 0, linetype = "dashed",
                         color = "grey60") +
    ggplot2::coord_equal(xlim = c(0, 1), ylim = c(0, 1)) +
    ggplot2::labs(x = "1 - specificity", y = "Sensitivity",
                  title = sprintf("ROC curve | AUC %.3f", auc)) + hse_theme()
  attr(p, "hse_roc") <- roc
  p
}

# Kaplan-Meier plot using a real survival fit and censoring marks.
# Time and event are explicit columns; event must be 0/1 (1=event).
hse_plot_survival <- function(data, time, event, group) {
  hse_check_cols(data, c(time, event, group))
  hse_numeric(data[[time]], time)
  hse_numeric(data[[event]], event)
  hse_require_plot()
  if (!requireNamespace("survival", quietly = TRUE))
    stop("Install survival to plot Kaplan-Meier curves")
  d <- data[stats::complete.cases(data[c(time,event,group)]), , drop = FALSE]
  if (any(d[[time]] < 0) || !all(d[[event]] %in% c(0, 1)))
    stop("Nonnegative time and 0/1 event indicator required")
  d$.time <- d[[time]]
  d$.event <- d[[event]]
  d$.group <- factor(d[[group]])
  if (nlevels(d$.group) < 1L) stop("At least one group required")
  fit <- survival::survfit(survival::Surv(.time, .event) ~ .group, data = d)
  sm <- summary(fit)
  curve <- data.frame(time = sm$time, surv = sm$surv,
                      n_risk = sm$n.risk,
                      stratum = as.character(sm$strata),
                      censored = sm$n.censor > 0)
  p <- ggplot2::ggplot(curve, ggplot2::aes(x = .data$time,
                y = .data$surv, color = .data$stratum,
                group = .data$stratum)) +
    ggplot2::geom_step() +
    ggplot2::geom_point(data = curve[curve$censored,,drop=FALSE],
                        shape = 3, size = 1.5) +
    ggplot2::coord_cartesian(ylim = c(0, 1)) +
    ggplot2::labs(x = time, y = "Estimated survival probability",
                  color = group, title = "Kaplan-Meier survival estimate") +
    hse_theme()
  attr(p, "hse_fit") <- fit
  p
}
