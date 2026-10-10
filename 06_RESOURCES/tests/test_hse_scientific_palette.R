# Numerical and graphical contracts, synthetic data only; no silent skips.
args <- commandArgs(trailingOnly = FALSE)
f <- grep("^--file=", args, value = TRUE)
dir <- dirname(normalizePath(sub("^--file=", "", f[1])))
for (name in c("hse_stats_plots.R", "hse_gene_visuals.R", "hse_plot_annotations.R", "hse_scientific_palette.R"))
  source(file.path(dir, "..", "R", name))
if (!requireNamespace("ggplot2", quietly=TRUE)) stop("ggplot2 required")
options(warn=2)
expected <- c(orange="#E69F00", sky_blue="#56B4E9", bluish_green="#009E73", yellow="#F0E442",
              blue="#0072B2", vermillion="#D55E00", reddish_purple="#CC79A7", black="#000000")
stopifnot(identical(hse_okabe_ito(), expected))
levels <- c("A", "B", "C")
stopifnot(identical(hse_group_colors(c("B", "A")), hse_group_colors(c("A", "B", "A"))))
stopifnot(identical(hse_group_colors("B", levels), hse_group_colors(c("A", "B", "C"), levels)))
stopifnot(identical(hse_group_colors(factor("B", levels=levels)), hse_group_colors("B", levels)))
for (x in list(NA_character_, "", "  "))
  stopifnot(inherits(try(hse_axis_label(x, "mg/dL"), silent=TRUE), "try-error"))
stopifnot(inherits(try(hse_group_colors(letters[1:9]), silent=TRUE), "try-error"))
stopifnot(identical(hse_axis_label("Creatinine", "mg/dL"), "Creatinine (mg/dL)"))
stopifnot(identical(hse_scale_group_fill("A")$na.value, "#808080"),
          identical(hse_scale_sequential_fill()$na.value, "#808080"))
# Actual mapped NA cell and exact sequential scale behavior.
d <- data.frame(x=1:3, y=1, value=c(0, 1, NA_real_))
p <- ggplot2::ggplot(d, ggplot2::aes(x, y, fill=value)) + ggplot2::geom_tile() + hse_scale_sequential_fill("Biomarker", "mg/dL")
b <- ggplot2::ggplot_build(p)
stopifnot(tail(b$data[[1]]$fill,1)=="#808080",
          identical(b$data[[1]]$fill[1:2], ggplot2::scale_fill_viridis_c()$palette(c(0,1))))
scale <- hse_scale_diverging_fill(midpoint=0)
rescaled <- scale$rescaler(c(-2,0,2), to=c(0,1), from=c(-2,2))
stopifnot(all.equal(rescaled,c(0,.5,1)), identical(scale$palette(.5), "#F7F7F7"))
# Row transformation and constant row handling are checked independently.
m <- matrix(c(1,2,4, 7,7,7, 3,5,8), nrow=3, byrow=TRUE,
            dimnames=list(c("variable", "constant", "other"), c("s1","s2","s3")))
p <- hse_gene_heatmap(m, rownames(m), TRUE, fill_scale=hse_scale_diverging_fill())
expected_z <- (m[1,]-mean(m[1,]))/stats::sd(m[1,])
stopifnot(all.equal(p$data$Value[as.character(p$data$Gene)=="variable"], unname(expected_z)),
          all(p$data$Value[as.character(p$data$Gene)=="constant"]==0))
invisible(ggplot2::ggplot_build(p))
# PCA labels must use all-component denominator, independently calculated.
set.seed(43); m <- matrix(rnorm(6*10),6,dimnames=list(paste0("g",1:6),paste0("s",1:10)))
meta <- data.frame(Sample=rev(colnames(m)), Group=rep(c("A","B"),5))
p <- hse_gene_pca(m,meta,"Group",6)
fit <- stats::prcomp(t(m),center=TRUE,scale.=FALSE)
pct <- 100*fit$sdev^2/sum(fit$sdev^2)
stopifnot(p$labels$x==sprintf("PC1 (%.1f%%)",pct[1]),p$labels$y==sprintf("PC2 (%.1f%%)",pct[2]))
# Volcano coordinates and threshold flags are not recomputed by palette changes.
de <- data.frame(logFC=c(-2,0,2,NA),FDR=c(.01,.7,0,.2))
p <- hse_gene_volcano(de)
stopifnot(all.equal(p$data$score[1:3],-log10(pmax(de$FDR[1:3],.Machine$double.xmin))),
          identical(p$data$status,c(TRUE,FALSE,TRUE,FALSE)),
          p$labels$x=="Model log2 fold change",p$labels$y=="-log10(adjusted p-value)")
# Export reuses annotation audit and produces raster/vector and sidecar files.
p <- ggplot2::ggplot(data.frame(x=1:3,y=c(1,4,2)),ggplot2::aes(x,y)) + ggplot2::geom_point() +
  ggplot2::labs(title="Synthetic export",x="Age (years)",y="Creatinine (mg/dL)",caption="Three invented observations")
stem <- file.path(tempdir(),"palette-contract")
paths <- hse_save_figure(p,stem)
stopifnot(all(file.exists(paths)),all(file.info(paths)$size>1000),file.exists(paste0(paths[1],".annotations.R")))
bad <- p;bad$labels$y <- ""
stopifnot(inherits(try(hse_save_figure(bad,file.path(tempdir(),"invalid-export")),silent=TRUE),"try-error"))
cat("PASS: palette, scale, numerical, annotation and export contracts\n")
