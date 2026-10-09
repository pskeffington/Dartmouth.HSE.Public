# Synthetic-only smoke checks. Execute with Rscript --vanilla.
args <- commandArgs(trailingOnly = FALSE)
f <- grep("^--file=", args, value = TRUE)
if (!length(f)) stop("Run with Rscript --vanilla")
dir <- dirname(normalizePath(sub("^--file=", "", f[1])))
source(file.path(dir, "..", "R", "hse_stats_plots.R"))
source(file.path(dir, "..", "R", "hse_gene_visuals.R"))
set.seed(711)
m <- matrix(rnorm(240), nrow = 20,
            dimnames = list(paste0("gene", 1:20), paste0("sample", 1:12)))
meta <- data.frame(Sample = rev(colnames(m)),
                   Subtype = rep(c("A", "B"), each=6))
stopifnot(length(hse_gene_top_var(m, 5)) == 5L)
stopifnot(identical(as.character(hse_gene_meta(m, meta)$Sample), colnames(m)))
stopifnot(inherits(try(hse_gene_validate(m, "missing"), silent=TRUE), "try-error"))
if (requireNamespace("ggplot2", quietly = TRUE)) {
  stopifnot(inherits(hse_gene_heatmap(m, rownames(m)[1:5]), "ggplot"))
  stopifnot(inherits(hse_gene_pca(m, meta, "Subtype", n_genes=10), "ggplot"))
  stopifnot(inherits(hse_gene_mean_variance(m), "ggplot"))
  de <- data.frame(logFC = rnorm(20), FDR = seq(.001, 1, length.out=20))
  stopifnot(inherits(hse_gene_volcano(de), "ggplot"))
}
cat("PASS: synthetic genomics visualizations and validation smoke tests\n")
