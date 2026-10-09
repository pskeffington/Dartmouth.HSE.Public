# One-call statistical plots. Source hse_stats_plots.R first.
# P-values are exploratory; these functions do not fit edgeR models.

hse_plot_test <- function(data, x, y, method = c("pearson","spearman"),
                          fit = TRUE, conf_level = .95) {
  # Scatterplot, optional least-squares best-fit line, and correlation p-value.
  # A linear fit and Pearson association answer related but distinct questions.
  method <- match.arg(method)
  hse_check_cols(data, c(x,y)); hse_numeric(data[[x]],x); hse_numeric(data[[y]],y)
  hse_require_plot()
  if (!is.finite(conf_level) || conf_level <= 0 || conf_level >= 1)
    stop("conf_level must be between zero and one.")
  d <- data.frame(x=data[[x]], y=data[[y]])
  d <- d[stats::complete.cases(d) & is.finite(d$x) & is.finite(d$y),,drop=FALSE]
  if (nrow(d)<3L || length(unique(d$x))<2L || length(unique(d$y))<2L)
    stop("At least three complete observations and variation in both axes required.")
  result <- suppressWarnings(stats::cor.test(d$x,d$y,method=method,
                                              exact=FALSE,conf.level=conf_level))
  lab <- sprintf("%s r = %.3f | p = %.3g | n = %d",method,
                 unname(result$estimate),result$p.value,nrow(d))
  p <- ggplot2::ggplot(d,ggplot2::aes(x=.data$x,y=.data$y)) +
       ggplot2::geom_point(alpha=.65) +
       ggplot2::labs(x=x,y=y,subtitle=lab,title="Association and fitted trend") + hse_theme()
  if (fit) p <- p + ggplot2::geom_smooth(method="lm",formula=y~x,se=TRUE,
                                         level=conf_level,color="#2166AC")
  attr(p,"hse_test") <- result
  p
}

hse_plot_wilcox <- function(data, value, group, paired = FALSE, id = NULL,
                            adjust = "none", title = NULL) {
  # Single-call group boxplot, displayed observations and Wilcoxon p-value.
  # paired=TRUE requires subject ID; pairing is NEVER inferred from row order.
  # adjust is supported for consistency with multiple-comparison workflows;
  # for a single test the correction has no effect.
  hse_check_cols(data,c(value,group,id));hse_numeric(data[[value]],value)
  hse_require_plot()
  adjust <- match.arg(adjust,stats::p.adjust.methods)
  if (paired && is.null(id)) stop("Paired testing requires id.")
  if (!paired && !is.null(id)) stop("Set paired=TRUE to use id.")
  if (paired) {
    d <- data[stats::complete.cases(data[c(value,group,id)]),,drop=FALSE]
    result <- hse_wilcox_paired(d,value,group,id)
    # Only paired subjects contribute to the displayed test.
    ids1 <- d[[id]][as.character(d[[group]])==sort(unique(as.character(d[[group]])))[1]]
    ids2 <- d[[id]][as.character(d[[group]])==sort(unique(as.character(d[[group]])))[2]]
    d <- d[d[[id]] %in% intersect(ids1,ids2),,drop=FALSE]
  } else {
    d <- data[stats::complete.cases(data[c(value,group)]),,drop=FALSE]
    result <- hse_wilcox_independent(d,value,group)
  }
  if (length(unique(as.character(d[[group]])))!=2L) stop("Exactly two groups needed.")
  p_adj <- stats::p.adjust(result$p.value,method=adjust)
  label <- sprintf("Wilcoxon %s | p = %.3g | n = %d%s",
                   if(paired) "paired" else "rank-sum",p_adj,
                   if(paired) length(unique(d[[id]])) else nrow(d),
                   if(adjust!="none") paste0(" | adjustment: ",adjust) else "")
  p <- hse_box(d,value,group,y_label=value,title=title %||% "Group comparison") +
       ggplot2::labs(subtitle=label)
  attr(p,"hse_test") <- result
  p
}

hse_plot_multigroup <- function(data,value,group,
                                p_adjust="BH",pairwise=TRUE) {
  # Kruskal-Wallis global test; optional pairwise Wilcoxon post-hoc tests.
  # Returns plot annotated with global p and metadata attr "hse_posthoc".
  hse_check_cols(data,c(value,group));hse_numeric(data[[value]],value)
  hse_require_plot()
  p_adjust <- match.arg(p_adjust,stats::p.adjust.methods)
  d <- data[stats::complete.cases(data[c(value,group)]),,drop=FALSE]
  d[[group]] <- as.factor(d[[group]])
  if (nlevels(d[[group]])<2L) stop("At least two groups required.")
  global <- stats::kruskal.test(stats::reformulate(group,response=value),data=d)
  p <- hse_box(d,value,group) +
    ggplot2::labs(subtitle=sprintf("Kruskal-Wallis p = %.3g | n = %d",
                                   global$p.value,nrow(d)))
  attr(p,"hse_test") <- global
  if (pairwise) attr(p,"hse_posthoc") <- stats::pairwise.wilcox.test(
    x=d[[value]],g=d[[group]],p.adjust.method=p_adjust,exact=FALSE)
  p
}

hse_plot_gene_wilcox <- function(long_data, gene, group,
                                 value="Expression", paired=FALSE,
                                 id=NULL, scale="log2 CPM") {
  # Single-gene wrapper for matrices prepared with hse_gene_long().
  # Intentionally refuses >2 groups: use hse_plot_multigroup for that case.
  hse_check_cols(long_data,c("Gene",group,value,id))
  d <- long_data[!is.na(long_data$Gene) & as.character(long_data$Gene)==gene,,drop=FALSE]
  if (!nrow(d)) stop("Gene not found: ",gene)
  p <- hse_plot_wilcox(d,value,group,paired=paired,id=id,
                       title=paste("Expression:",gene))
  p <- p + ggplot2::labs(y=scale)
  p
}
