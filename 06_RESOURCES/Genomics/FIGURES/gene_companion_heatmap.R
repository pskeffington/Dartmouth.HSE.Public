# Original synthetic teaching matrix. No downloaded or patient-level input.
# Source from the repository root; optional output directory must be outside Git.
companion_matrix <- function() {
  values <- matrix(c(2, 1, 0, -1, -2, 0,
                     1, 0, -1, -2, 0, 2,
                     0, -1, -2, 0, 2, 1,
                     -1, -2, 0, 2, 1, 0), nrow = 6L)
  dimnames(values) <- list(paste0("Teach", LETTERS[1:6]), paste0("C", 1:4))
  values
}

companion_heatmap <- function() {
  if (!requireNamespace("ggplot2", quietly = TRUE)) stop("ggplot2 required")
  source("06_RESOURCES/R/hse_scientific_palette.R", local = TRUE)
  values <- companion_matrix()
  table <- expand.grid(label = rownames(values), contrast = colnames(values),
                       stringsAsFactors = FALSE)
  table$change <- as.vector(values)
  table$label <- factor(table$label, levels = rev(rownames(values)))
  table$contrast <- factor(table$contrast, levels = colnames(values))
  table$text <- sprintf("%+d", as.integer(table$change))
  ggplot2::ggplot(table, ggplot2::aes(contrast, label, fill = change)) +
    ggplot2::geom_tile(colour = "#333333", linewidth = 0.4) +
    ggplot2::geom_text(ggplot2::aes(label = text,
      colour = abs(change) == 2), size = 4.5, show.legend = FALSE) +
    ggplot2::scale_colour_manual(values = c("FALSE" = "#111111", "TRUE" = "#FFFFFF")) +
    ggplot2::scale_fill_gradient2(low = "#2166AC", mid = "#F7F7F7",
      high = "#B2182B", midpoint = 0, limits = c(-2, 2), breaks = -2:2,
      name = "Signed log2 fold change\nTumor / adjacent-normal (simulated)") +
    ggplot2::coord_fixed() + hse_theme_scientific(12) +
    ggplot2::labs(title = "Synthetic expression demonstration",
      subtitle = "Invented labels and contrasts; no patient data or fitted estimates",
      x = "Simulated comparison (C1-C4)", y = "Invented teaching label (TeachA-TeachF)",
      caption = "Chosen demonstration values; zero-centered scale; not row z-scores.\nSource: companion_matrix(), independently authored.")
}

export_companion_heatmap <- function(output_dir) {
  if (!file.exists("06_RESOURCES/Genomics/FIGURES/gene_companion_heatmap.R"))
    stop("Run the exporter from the repository root")
  root <- normalizePath(".", mustWork = TRUE)
  output <- normalizePath(output_dir, mustWork = TRUE)
  if (identical(root, output) || startsWith(output, paste0(root, .Platform$file.sep)))
    stop("Export directory must be outside the repository")
  plot <- companion_heatmap()
  for (extension in c("png", "pdf")) {
    ggplot2::ggsave(file.path(output, paste0("synthetic-companion-heatmap.", extension)),
      plot, width = 8, height = 6, dpi = 300, bg = "white")
  }
  writeLines(capture.output(sessionInfo()), file.path(output, "session-info.txt"))
  invisible(output)
}

if (sys.nframe() == 0L) {
  args <- commandArgs(trailingOnly = TRUE)
  if (length(args) != 1L) stop("Usage: Rscript gene_companion_heatmap.R OUTSIDE_GIT_DIR")
  export_companion_heatmap(args[[1L]])
}
