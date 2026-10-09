# Synthetic, deterministic descriptive-statistics checks.
args <- commandArgs(FALSE)
f <- grep("^--file=", args, value=TRUE)
if (!length(f)) stop("Run with Rscript --vanilla")
here <- dirname(normalizePath(sub("^--file=", "", f[1])))
source(file.path(here, "..", "R", "hse_stats_plots.R"))
d <- data.frame(group=c("A","A","A","A","A","B","B"),
                score=c(1,2,3,4,NA,8,NA))
a <- hse_describe(d, "score", group="group")
stopifnot(nrow(a)==2L, all(c("iqr","se","variance","n_missing",
                              "p05","p95") %in% names(a)))
stopifnot(a$n[a$group=="A"]==4L, a$n_missing[a$group=="A"]==1L)
stopifnot(a$iqr[a$group=="A"]==1.5)
stopifnot(a$median[a$group=="A"]==2.5)
stopifnot(a$pct_missing[a$group=="A"]==20)
stopifnot(is.na(a$sd[a$group=="B"]), is.na(a$se[a$group=="B"]))
r <- hse_summary_report(d, "score", group="group", unit="points")
stopifnot(length(r$narrative)==2L, grepl("IQR",r$narrative[1],fixed=TRUE))
stopifnot(grepl("missing",r$narrative[1],fixed=TRUE))
stopifnot(inherits(try(hse_describe(data.frame(score="x"),"score"),
                      silent=TRUE),"try-error"))
empty <- hse_describe(data.frame(score=numeric()), "score")
stopifnot(nrow(empty)==0L)
all_missing <- hse_summary_report(data.frame(score=c(NA_real_,NA_real_)),"score")
stopifnot(all_missing$statistics$n==0L,
          grepl("no observed",all_missing$narrative[1]))
hse_print_summary(r)
cat("PASS: descriptive statistics, IQR, and narrative report tests\n")
