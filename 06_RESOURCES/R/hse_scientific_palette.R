# Independently authored, opt-in scientific plotting palette.
# Source after hse_stats_plots.R. No package installation or file I/O on load.
# Okabe-Ito categorical colors; viridis continuous scale via ggplot2.

hse_okabe_ito <- function() {
  c(orange = "#E69F00", sky_blue = "#56B4E9", bluish_green = "#009E73",
    yellow = "#F0E442", blue = "#0072B2", vermillion = "#D55E00",
    reddish_purple = "#CC79A7", black = "#000000")
}

hse_group_colors <- function(groups, levels = NULL) {
  if (is.null(levels)) levels <- if (is.factor(groups)) base::levels(groups) else
    sort(unique(as.character(groups[!is.na(groups)])), method = "radix")
  if (!is.character(levels) || anyNA(levels) || anyDuplicated(levels) ||
      any(!nzchar(trimws(levels))) || !all(as.character(groups[!is.na(groups)]) %in% levels))
    stop("levels must uniquely cover the nonmissing groups.", call. = FALSE)
  colors <- unname(hse_okabe_ito()[c("blue", "vermillion", "bluish_green",
    "reddish_purple", "orange", "sky_blue", "black", "yellow")])
  if (length(levels) > length(colors))
    stop("More than eight categories; use additional encodings or facets.", call. = FALSE)
  stats::setNames(colors[seq_along(levels)], levels)
}

hse_theme_scientific <- function(base_size = 12) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) stop("ggplot2 required")
  ggplot2::theme_classic(base_size = base_size) +
    ggplot2::theme(plot.title = ggplot2::element_text(face = "bold"),
      plot.subtitle = ggplot2::element_text(colour = "#424242", hjust = 0, size = base_size * 0.9),
      plot.caption = ggplot2::element_text(colour = "#555555", hjust = 0),
      plot.title.position = "plot", plot.caption.position = "plot",
      legend.position = "bottom", axis.title = ggplot2::element_text(face = "plain"),
      plot.margin = ggplot2::margin(12, 14, 12, 12))
}

hse_scale_group_color <- function(groups, levels = NULL, name = "Group") {
  ggplot2::scale_color_manual(values = hse_group_colors(groups, levels),
    name = name, na.value = "#808080", drop = FALSE)
}

hse_scale_group_fill <- function(groups, levels = NULL, name = "Group") {
  ggplot2::scale_fill_manual(values = hse_group_colors(groups, levels),
    name = name, na.value = "#808080", drop = FALSE)
}

hse_scale_sequential_fill <- function(name = "Value", unit = NULL) {
  legend <- if (is.null(unit)) name else sprintf("%s (%s)", name, unit)
  ggplot2::scale_fill_viridis_c(name = legend, na.value = "#808080")
}

hse_scale_diverging_fill <- function(name = "Row z-score", midpoint = 0) {
  if (!is.numeric(midpoint) || length(midpoint) != 1L || !is.finite(midpoint))
    stop("midpoint must be one finite number.")
  ggplot2::scale_fill_gradient2(name = name, low = "#2166AC", mid = "#F7F7F7",
    high = "#B2182B", midpoint = midpoint, na.value = "#808080")
}

# Explicit units: no guessing or concealed units.
hse_axis_label <- function(name, unit) {
  if (length(name) != 1L || !is.character(name) || is.na(name) || !nzchar(trimws(name)) ||
      length(unit) != 1L || !is.character(unit) || is.na(unit) || !nzchar(trimws(unit))) {
    stop("Supply a nonempty variable name and unit ('unitless' where appropriate).")
  }
  sprintf("%s (%s)", name, unit)
}

hse_save_figure <- function(plot, stem, width = 7, height = 5, dpi = 300) {
  if (!inherits(plot, "ggplot")) stop("plot must be a ggplot object")
  if (!is.character(stem) || length(stem) != 1L || is.na(stem) || !nzchar(trimws(stem)))
    stop("stem must be a nonempty path without extension")
  if (!exists("hse_save_annotated", mode = "function"))
    stop("Source hse_plot_annotations.R before exporting.")
  # Reuse the existing audited exporter and its annotation manifest.
  hse_save_annotated(plot, paste0(stem, ".png"), width, height, dpi)
  hse_save_annotated(plot, paste0(stem, ".pdf"), width, height, dpi)
  invisible(c(paste0(stem, ".png"), paste0(stem, ".pdf")))
}
