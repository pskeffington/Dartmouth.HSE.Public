# Synthetic-only smoke tests. Execute from repo root with Rscript.
args <- commandArgs(FALSE)
f <- grep("^--file=", args, value=TRUE)
if (!length(f)) stop("Run via Rscript --vanilla")
here <- dirname(normalizePath(sub("^--file=","",f[1])))
source(file.path(here,"..","R","hse_stats_plots.R"))
source(file.path(here,"..","R","hse_one_call_plots.R"))
source(file.path(here,"..","R","hse_biostat_panels.R"))
if (!requireNamespace("ggplot2",quietly=TRUE)) {
  cat("SKIP: ggplot2 not installed\n")
} else {
  set.seed(711)
  d <- data.frame(id=rep(1:40,each=3),
                  time=rep(1:3,40),
                  group=rep(c("A","B"),each=60),
                  value=rnorm(120))
  d$facet <- rep(rep(c("x","y"),each=20),each=3)
  p <- hse_plot_panel_box(d,"value","group","facet")
  stopifnot(inherits(p,"ggplot"))
  # Distinct independent groups inside each facet.
  b <- data.frame(value=rnorm(80), group=rep(rep(c("A","B"),each=20),2),
                  facet=rep(c("x","y"),each=40))
  p <- hse_plot_panel_wilcox(b,"value","group","facet")
  stopifnot(inherits(p,"ggplot"), nrow(attr(p,"hse_tests"))==2L,
            all(is.finite(attr(p,"hse_tests")$p_adjusted)))
  stopifnot(inherits(hse_plot_trajectory(d,"id","time","value"),"ggplot"))
  stopifnot(inherits(hse_plot_mean_ci(d,"time","value","group"),"ggplot"))
  e <- data.frame(term=c("A","B"),est=c(.2,-.3),
                  low=c(.1,-.5), high=c(.4,-.1))
  stopifnot(inherits(hse_plot_forest(e,"term","est","low","high"),"ggplot"))
  fit <- stats::lm(mpg ~ wt, data=mtcars)
  stopifnot(inherits(hse_plot_lm_diagnostics(fit),"ggplot"))
  if (requireNamespace("pROC",quietly=TRUE)) {
    roc <- data.frame(outcome=rep(c("Control","Case"),each=25),
                      score=c(runif(25,0,.5),runif(25,.5,1)))
    stopifnot(inherits(hse_plot_roc(roc,"outcome","score","Case"),"ggplot"))
  }
  if (requireNamespace("survival",quietly=TRUE)) {
    s <- data.frame(time=seq_len(40),event=rep(c(1,0),20),
                    group=rep(c("A","B"),each=20))
    stopifnot(inherits(hse_plot_survival(s,"time","event","group"),"ggplot"))
  }
  cat("PASS: biostatistics panel smoke tests (installed optional modules)\n")
}
