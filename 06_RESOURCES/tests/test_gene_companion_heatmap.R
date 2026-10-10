# Numerical and display contracts: invented values, orientation and caption units.
source("06_RESOURCES/Genomics/FIGURES/gene_companion_heatmap.R")
values <- companion_matrix()
stopifnot(identical(dim(values), c(6L, 4L)), all(is.finite(values)),
          range(values) == c(-2, 2), values["TeachA", "C1"] == 2,
          values["TeachE", "C1"] == -2, values["TeachD", "C4"] == 2,
          all(2^values > 0), 2^values["TeachA", "C1"] == 4)
text <- paste(readLines("06_RESOURCES/Genomics/FIGURES/README.md"), collapse = "\n")
for (column in seq_len(ncol(values))) {
  for (row in seq_len(nrow(values))) {
    value <- values[row, column]
    shown <- if (value > 0) paste0("+", value) else as.character(value)
    label <- paste0("C", column, LETTERS[row], "[\"Teach", LETTERS[row], ": ", shown, "\"]")
    stopifnot(grepl(label, text, fixed = TRUE))
  }
}
stopifnot(grepl("log2 fold change, not row z-score", text, fixed = TRUE))
if (requireNamespace("ggplot2", quietly = TRUE)) {
  plot <- companion_heatmap()
  built <- ggplot2::ggplot_build(plot)
  stopifnot(nrow(built$data[[1]]) == 24L,
            identical(plot$scales$get_scales("fill")$limits, c(-2, 2)),
            plot$labels$x == "Simulated comparison (C1-C4)")
}
cat("Synthetic companion heatmap numerical and display contracts passed.\n")
