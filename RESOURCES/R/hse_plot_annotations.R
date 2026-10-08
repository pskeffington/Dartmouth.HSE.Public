# HSE Public: downstream figure annotations and export provenance
# Source after hse_stats_plots.R, hse_one_call_plots.R and hse_biostat_panels.R.
# No datasets are read, no plots are generated, and no globals are changed.
#
# Every plot carries readable title/subtitle/caption, accurate axis labels,
# and an inspectable annotation record. Missing inferential values stay absent.
# Do not infer p-values from graphics, or relabel descriptive CI as model CI.

hse_annotation <- function(plot, title = NULL, subtitle = NULL,
                           x = NULL, y = NULL, method = NULL,
                           n = NULL, p = NULL, adjustment = NULL,
                           scale = NULL, design = NULL, source = NULL,
                           note = NULL) {
  hse_require_plot()
  if (!inherits(plot, "ggplot")) stop("plot must be ggplot")
  if (!is.null(n) && (length(n) != 1L || !is.finite(n) || n < 0))
    stop("n must be a nonnegative scalar")
  if (!is.null(p) && (length(p) != 1L || !is.finite(p) ||
                     p < 0 || p > 1)) stop("p must lie in [0,1]")
  fmt <- function(x) if (is.null(x)) NULL else as.character(x)
  details <- c(if (!is.null(method)) paste("Method:", method),
               if (!is.null(n)) paste("n =", n),
               if (!is.null(p)) paste("p =", format.pval(p, digits = 3,
                                                        eps = .Machine$double.eps)),
               if (!is.null(adjustment)) paste("p adjustment:", adjustment))
  # Preserve existing labels when no override is supplied.
  prior <- plot$labels
  existing_subtitle <- if (!is.null(prior$subtitle)) prior$subtitle else NULL
  annotation_subtitle <- if (!is.null(subtitle)) subtitle else
    if (length(details)) paste(details, collapse = " | ") else existing_subtitle
  # Caption stores information helpful once the figure leaves its R session.
  caption <- paste(c(if (!is.null(scale)) paste("Scale:", scale),
                     if (!is.null(design)) paste("Design:", design),
                     if (!is.null(source)) paste("Source:", source),
                     if (!is.null(note)) note), collapse = " | ")
  plot <- plot + ggplot2::labs(title = title, subtitle = annotation_subtitle,
             x = x, y = y, caption = if (nzchar(caption)) caption else NULL)
  attr(plot, "hse_annotation") <- list(title = title, subtitle = annotation_subtitle,
       x = x, y = y, method = method, n = n, p = p,
       adjustment = adjustment, scale = scale,
       design = design, source = source, note = note)
  plot
}

# Inspect the metadata rather than manually copying labels from an image.
hse_plot_annotation <- function(plot) {
  if (!inherits(plot, "ggplot")) stop("plot must be ggplot")
  attr(plot, "hse_annotation")
}

# Ensure all required labels are actually present before publication.
hse_plot_audit <- function(plot, require_source = FALSE) {
  if (!inherits(plot, "ggplot")) stop("plot must be ggplot")
  labels <- plot$labels
  get_label <- function(key) {
    val <- labels[[key]]
    if (is.null(val) || !is.character(val) || !length(val)) "" else val[1]
  }
  required <- c("title", "x", "y", "caption")
  missing <- required[!vapply(required, function(k) nzchar(trimws(get_label(k))),
                               logical(1))]
  a <- hse_plot_annotation(plot)
  if (require_source && (is.null(a$source) || !nzchar(a$source)))
    missing <- unique(c(missing, "source"))
  data.frame(field = required, valid = !(required %in% missing),
             stringsAsFactors = FALSE) -> audit
  list(pass = !length(missing), missing = missing, fields = audit)
}

# One-call export enforces annotation checks and writes a companion
# manifest so that published figures retain method and provenance.
hse_save_annotated <- function(plot, file, width = 8, height = 5,
                               dpi = 300, require_source = FALSE) {
  check <- hse_plot_audit(plot, require_source)
  if (!check$pass)
    stop("Missing figure annotations: ", paste(check$missing, collapse = ", "))
  hse_save_plot(plot, file, width = width, height = height, dpi = dpi)
  a <- hse_plot_annotation(plot)
  # Base R dput avoids requiring JSON packages for educational users.
  manifest <- paste0(file, ".annotations.R")
  dput(list(annotation = a, labels = plot$labels,
            width_in = width, height_in = height, dpi = dpi),
       file = manifest)
  invisible(list(figure = file, manifest = manifest))
}

# Auto-decorate the existing one-call statistical plot functions.
# Keep the original htest attributes, and embed methods/p in the figure.
# The wrappers are installed only once by this file, after all base modules.
if (exists("hse_plot_test", mode = "function") &&
    !exists(".hse_original_plot_test", inherits = FALSE)) {
  .hse_original_plot_test <- hse_plot_test
  hse_plot_test <- function(data, x, y,
                            method = c("pearson", "spearman"), fit = TRUE,
                            conf_level = .95) {
    method <- match.arg(method)
    p <- .hse_original_plot_test(data,x,y,method,fit,conf_level)
    result <- attr(p,"hse_test")
    n <- sum(stats::complete.cases(data[c(x,y)]))
    p <- hse_annotation(p, title = "Association and fitted trend",
                       x=x, y=y, method=paste(method,"correlation"), n=n,
                       p=result$p.value, design="cross-sectional",
                       note=if (fit) "Line: least squares; band: mean-response CI" else
                         "Correlation only; no fitted line")
    attr(p,"hse_test") <- result
    p
  }
}

if (exists("hse_plot_wilcox", mode = "function") &&
    !exists(".hse_original_plot_wilcox", inherits = FALSE)) {
  .hse_original_plot_wilcox <- hse_plot_wilcox
  hse_plot_wilcox <- function(data, value, group, paired=FALSE, id=NULL,
                              adjust="none", title=NULL) {
    p <- .hse_original_plot_wilcox(data,value,group,paired,id,adjust,title)
    result <- attr(p,"hse_test")
    # n corresponds to complete observations (unpaired) or matched IDs.
    if (paired) {
      d <- data[stats::complete.cases(data[c(value,group,id)]),,drop=FALSE]
      gg <- sort(unique(as.character(d[[group]])))
      a <- unique(as.character(d[[id]][as.character(d[[group]])==gg[1]]))
      b <- unique(as.character(d[[id]][as.character(d[[group]])==gg[2]]))
      n <- length(intersect(a,b))
    } else {
      n <- sum(stats::complete.cases(data[c(value,group)]))
    }
    p <- hse_annotation(p, title=title %||% "Group comparison",
      x=group,y=value,method=if(paired) "Wilcoxon signed rank" else "Wilcoxon rank sum",
      n=n,p=result$p.value,adjustment=if(adjust!="none") adjust else NULL,
      design=if(paired) "matched pairs" else "independent groups",
      note=if(paired) "n counts complete matched pairs" else
        "n counts complete independent observations")
    attr(p,"hse_test") <- result
    p
  }
}
