# Synthetic biomedical practice data; no real participants or clinical inference.
# Source from the repository root, then call make_teaching_cohort().
# Requires base R only. Sex and Site are fictional recorded categories.
# Units: Age years, Albumin g/dL, Creatinine mg/dL,
# RBC_Count 10^12 cells/L, WBC_Count 10^9 cells/L.
make_teaching_cohort <- function(n = 48L, seed = 260410L) {
  if (!is.numeric(n) || length(n) != 1L || !is.finite(n) ||
      n < 12 || n != floor(n)) stop("n must be an integer of at least 12")
  if (!is.numeric(seed) || length(seed) != 1L || !is.finite(seed) ||
      seed < 0 || seed > .Machine$integer.max || seed != floor(seed)) {
    stop("seed must be a nonnegative R integer")
  }
  # This teaching function resets the random-number state intentionally.
  set.seed(seed)
  age <- sample(25:70, n, replace = TRUE)
  data.frame(
    Subject_ID = sprintf("D%03d", seq_len(n)),
    Age = age,
    Sex = factor(rep(c("Female", "Male"), length.out = n)),
    Site = factor(rep(c("Site_1", "Site_2", "Site_3"), length.out = n)),
    Albumin = runif(n, 3.8, 4.9),
    Creatinine = 0.75 + 0.004 * (age - 25) + runif(n, 0, 0.2),
    RBC_Count = runif(n, 4.0, 5.8),
    WBC_Count = runif(n, 4.5, 10.5)
  )
}
