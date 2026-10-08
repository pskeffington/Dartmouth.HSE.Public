# Annotation smoke tests; synthetic data only.
args <- commandArgs(FALSE); f <- grep("^--file=",args,value=TRUE)
if (!length(f)) stop("Run with Rscript --vanilla")
here <- dirname(normalizePath(sub("^--file=","",f[1])))
for (nm in c("hse_stats_plots.R","hse_one_call_plots.R",
             "hse_biostat_panels.R","hse_plot_annotations.R"))
  source(file.path(here,"..","R",nm))
if (!requireNamespace("ggplot2",quietly=TRUE)) {
  cat("SKIP: ggplot2 unavailable\n")
} else {
  set.seed(711)
  d <- data.frame(x=seq_len(40),y=rnorm(40)+seq_len(40)/10,
                  group=rep(c("A","B"),each=20),
                  facet=rep(rep(c("first","second"),each=10),2))
  p <- hse_plot_test(d,"x","y")
  stopifnot(hse_plot_audit(p)$pass, inherits(attr(p,"hse_test"),"htest"),
            is.numeric(hse_plot_annotation(p)$p))
  w <- hse_plot_wilcox(d,"y","group")
  stopifnot(hse_plot_audit(w)$pass, inherits(attr(w,"hse_test"),"htest"))
  q <- hse_plot_multigroup(d,"y","group")
  stopifnot(hse_plot_audit(q)$pass,
            inherits(attr(q,"hse_posthoc"),"pairwise.htest"))
  pw <- hse_plot_panel_wilcox(d,"y","group","facet")
  stopifnot(hse_plot_audit(pw)$pass, nrow(attr(pw,"hse_tests"))==2L)
  fw <- hse_plot_forest(data.frame(term=c("G1","G2"),est=c(.1,.2),
    lo=c(0,.1),hi=c(.3,.4)), "term","est","lo","hi")
  stopifnot(hse_plot_audit(fw)$pass)
  gene <- transform(d, Gene="ESR1", Expression=y, Subtype=group)
  gw <- hse_plot_gene_wilcox(gene,"ESR1","Subtype")
  stopifnot(hse_plot_audit(gw)$pass)
  bad <- ggplot2::ggplot(data.frame(x=1,y=1),ggplot2::aes(x=x,y=y))+
         ggplot2::geom_point()
  stopifnot(!hse_plot_audit(bad)$pass)
  annotated <- hse_annotation(bad,title="Demo",x="X units",y="Y units",
                              source="synthetic fixture",note="No inference")
  stopifnot(hse_plot_audit(annotated, require_source=TRUE)$pass)
  outfile <- tempfile(fileext=".pdf")
  saved <- hse_save_annotated(annotated,outfile,require_source=TRUE)
  stopifnot(file.exists(saved$figure),file.exists(saved$manifest))
  unlink(c(saved$figure,saved$manifest))
  cat("PASS: annotation, metadata retention, audit and export smoke tests\n")
}
