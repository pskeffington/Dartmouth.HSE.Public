# Original synthetic paired arithmetic: no real genes, participants or count model.
# Chosen values demonstrate sensitivity; they do not supply sampling inference.
companion_pairs <- function() {
  data.frame(pair = paste0("DemoPair", seq_len(6L)),
             comparator = rep(10, 6L), tumor = c(20, 40, 10, 5, 20, 10))
}

paired_teaching_summary <- function(pairs = companion_pairs()) {
  stopifnot(is.data.frame(pairs), nrow(pairs) >= 2L,
            !anyDuplicated(pairs$pair),
            all(is.finite(pairs$comparator)), all(pairs$comparator > 0),
            all(is.finite(pairs$tumor)), all(pairs$tumor > 0))
  contrasts <- log2(pairs$tumor / pairs$comparator)
  leave_one_pair_means <- vapply(seq_along(contrasts), function(index) {
    mean(contrasts[-index])
  }, numeric(1))
  list(contrasts = contrasts, mean = mean(contrasts), range = range(contrasts),
       sensitivity_range = range(leave_one_pair_means),
       interpretation = "Chosen-value sensitivity; not a confidence interval")
}

if (sys.nframe() == 0L) print(paired_teaching_summary())
