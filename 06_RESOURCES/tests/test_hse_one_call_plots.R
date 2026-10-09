# Synthetic regression and nonparametric plot smoke tests.
args <- commandArgs(FALSE)
f <- grep("^--file=",args,value=TRUE)
if (!length(f)) stop("Run with Rscript --vanilla")
here <- dirname(normalizePath(sub("^--file=","",f[1])))
source(file.path(here,"..","R","hse_stats_plots.R"))
source(file.path(here,"..","R","hse_one_call_plots.R"))
if (!requireNamespace("ggplot2",quietly=TRUE)) {
  cat("SKIP: ggplot2 not installed\n")
} else {
  set.seed(711)
  d <- data.frame(x=1:24,y=1:24+rnorm(24),
    group=rep(c("Control","Case"),each=12))
  p <- hse_plot_test(d,"x","y")
  stopifnot(inherits(p,"ggplot"),inherits(attr(p,"hse_test"),"htest"))
  q <- hse_plot_wilcox(d,"y","group")
  stopifnot(inherits(q,"ggplot"),inherits(attr(q,"hse_test"),"htest"))
  paired <- data.frame(id=rep(1:12,each=2),
    arm=rep(c("Before","After"),12),value=rnorm(24))
  z <- hse_plot_wilcox(paired,"value","arm",paired=TRUE,id="id")
  stopifnot(inherits(z,"ggplot"))
  m <- hse_plot_multigroup(transform(d,group=rep(letters[1:3],each=8)),
                             "y","group")
  stopifnot(inherits(attr(m,"hse_posthoc"),"pairwise.htest"))
  g <- data.frame(Gene=rep("ESR1",nrow(d)),Subtype=d$group,Expression=d$y)
  stopifnot(inherits(hse_plot_gene_wilcox(g,"ESR1","Subtype"),"ggplot"))
  stopifnot(inherits(try(hse_plot_wilcox(d,"y","group",paired=TRUE),
                        silent=TRUE),"try-error"))
  cat("PASS: one-call plotting smoke checks\n")
}
