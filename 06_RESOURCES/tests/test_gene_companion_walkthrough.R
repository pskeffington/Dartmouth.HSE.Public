source("06_RESOURCES/Genomics/FIGURES/gene_companion_walkthrough.R")
summary <- paired_teaching_summary()
stopifnot(identical(summary$contrasts, c(1, 2, 0, -1, 1, 0)),
          summary$mean == 0.5,
          identical(summary$range, c(-1, 2)),
          isTRUE(all.equal(summary$sensitivity_range, c(0.2, 0.8))),
          grepl("not a confidence interval", summary$interpretation, fixed = TRUE))
invalid <- companion_pairs(); invalid$tumor[1] <- 0
stopifnot(inherits(try(paired_teaching_summary(invalid), silent = TRUE), "try-error"))
invalid <- companion_pairs(); invalid$pair[2] <- invalid$pair[1]
stopifnot(inherits(try(paired_teaching_summary(invalid), silent = TRUE), "try-error"))
text <- paste(readLines("06_RESOURCES/Genomics/BREAST_CANCER_60_GENE_COMPANION.md"), collapse = "\n")
stopifnot(grepl("mean is 0.5", text, fixed = TRUE),
          grepl("0.2 to 0.8", text, fixed = TRUE),
          grepl("Five values are nonnegative", text, fixed = TRUE))
cat("Synthetic walkthrough arithmetic, sensitivity and failure contracts passed.\n")
