# HSE 711 | Week 3 | Reusable summary and graph functions
# Load once: source("06_RESOURCES/R/Week_3_Reusable_Functions.R")
# Requires ggplot2. Loading this file defines functions; it reads no data.
# Keep data_df, random_data, and data_list as in the lecture/exercises.
# Pass column names as strings: plt_hist(data_df, "Age").
# .data[[variable]] selects the column named by a string inside aes().
# This is an exercise extension of Lecture 3, chunk 10's !!sym(variable).

# Lecture 3, chunks 10 and 15: functions and numerical summaries.
summary_cov <- function(cov) {
  if (!is.numeric(cov)) stop("cov must be a numeric vector.")
  summary(cov)
}

# Lecture 3, chunks 4 and 16: histograms.
plt_hist <- function(data, variable, bins = 10, fill_color = "darkgreen",
                     label = variable, title = paste("Distribution of", label)) {
  ggplot2::ggplot(data, ggplot2::aes(x = .data[[variable]])) +
    ggplot2::geom_histogram(bins = bins, fill = fill_color,
                           color = "white", alpha = 0.7) +
    ggplot2::labs(title = title, x = label, y = "Frequency") +
    ggplot2::theme_minimal()
}

# Lecture 3, chunk 17: box plots; jitter is the Question 5 extension.
plt_box <- function(data, group, variable, fill_colors = NULL,
                    jitter = TRUE, label = variable,
                    title = paste(label, "by", group)) {
  box_plot <- ggplot2::ggplot(
    data, ggplot2::aes(x = .data[[group]], y = .data[[variable]],
                      fill = .data[[group]])
  ) +
    ggplot2::geom_boxplot(width = 0.5, alpha = 0.7,
                         outlier.shape = if (jitter) NA else 16) +
    ggplot2::labs(title = title, x = group, y = label, fill = group) +
    ggplot2::theme_minimal()
  if (jitter) {
    box_plot <- box_plot + ggplot2::geom_jitter(
      width = 0.15, height = 0, size = 1.5, alpha = 0.5
    )
  }
  if (!is.null(fill_colors)) {
    box_plot <- box_plot + ggplot2::scale_fill_manual(values = fill_colors)
  }
  box_plot
}

# Lecture 3, chunks 8–9: scatter plots and optional linear fit.
# Question 5 extension: optional categorical color and shape mappings.
plt_scatter <- function(data, x_var, y_var, color_var = NULL,
                        shape_var = NULL, color_values = NULL,
                        shape_values = NULL, fit = FALSE,
                        x_label = x_var, y_label = y_var,
                        title = paste(y_label, "vs", x_label)) {
  scatter_plot <- ggplot2::ggplot(
    data, ggplot2::aes(x = .data[[x_var]], y = .data[[y_var]])
  )
  if (!is.null(color_var)) {
    scatter_plot <- scatter_plot + ggplot2::aes(color = .data[[color_var]])
  }
  if (!is.null(shape_var)) {
    scatter_plot <- scatter_plot + ggplot2::aes(shape = .data[[shape_var]])
  }
  scatter_plot <- scatter_plot + ggplot2::geom_point(alpha = 0.5, size = 2)
  if (!is.null(color_values)) {
    scatter_plot <- scatter_plot + ggplot2::scale_color_manual(values = color_values)
  }
  if (!is.null(shape_values)) {
    scatter_plot <- scatter_plot + ggplot2::scale_shape_manual(values = shape_values)
  }
  if (fit) {
    # Explicit mappings keep one pooled line, even when points have groups.
    scatter_plot <- scatter_plot + ggplot2::geom_smooth(
      data = data,
      mapping = ggplot2::aes(x = .data[[x_var]], y = .data[[y_var]]),
      inherit.aes = FALSE, method = "lm", formula = y ~ x,
      se = TRUE, color = "black"
    )
  }
  scatter_plot +
    ggplot2::labs(title = title, x = x_label, y = y_label,
                  color = color_var, shape = shape_var) +
    ggplot2::theme_minimal()
}
