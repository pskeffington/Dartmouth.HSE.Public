# Unit 6: independently authored synthetic biomarker inference example
# Base R only; no clinical data, no institutional course material.
set.seed(711)
n_per_group <- 40L
participant_id <- sprintf("S%03d", seq_len(2L * n_per_group))
study_group <- rep(c("control", "intervention"), each = n_per_group)
biomarker_mg_l <- rnorm(length(participant_id),
                        mean = ifelse(study_group == "control", 10, 12), sd = 3)
data <- data.frame(participant_id, study_group, biomarker_mg_l)
stopifnot(nrow(data) == 80L, !anyDuplicated(data$participant_id),
          all(is.finite(data$biomarker_mg_l)),
          identical(sort(unique(data$study_group)), c("control", "intervention")),
          !anyNA(data))
summary_one <- function(group_name) {
  x <- data$biomarker_mg_l[data$study_group == group_name]
  c(n = length(x), mean_mg_l = mean(x), sd_mg_l = sd(x), se_mg_l = sd(x)/sqrt(length(x)))
}
control <- summary_one("control")
intervention <- summary_one("intervention")
stopifnot(control[["n"]] == 40, intervention[["n"]] == 40)
effect_mg_l <- intervention[["mean_mg_l"]] - control[["mean_mg_l"]]
se_effect <- sqrt(intervention[["sd_mg_l"]]^2 / intervention[["n"]] +
                  control[["sd_mg_l"]]^2 / control[["n"]])
a <- intervention[["sd_mg_l"]]^2 / intervention[["n"]]
b <- control[["sd_mg_l"]]^2 / control[["n"]]
df_welch <- (a+b)^2 / (a^2/(intervention[["n"]]-1) + b^2/(control[["n"]]-1))
manual_ci <- effect_mg_l + c(-1, 1) * qt(0.975, df=df_welch) * se_effect
test <- t.test(biomarker_mg_l ~ study_group, data = data,
               var.equal = FALSE, conf.level = 0.95)
# R's formula order uses control - intervention, unlike our planned estimand.
test_effect_reoriented <- -unname(test$estimate[[1]] - test$estimate[[2]])
test_ci_reoriented <- rev(-unname(test$conf.int))
stopifnot(isTRUE(all.equal(effect_mg_l, test_effect_reoriented, tolerance = 1e-10)),
          isTRUE(all.equal(manual_ci, test_ci_reoriented, tolerance = 1e-10)),
          is.finite(test$p.value))
print(rbind(control = control, intervention = intervention))
cat(sprintf("Intervention - control: %.4f mg/L; 95%% CI [%.4f, %.4f] mg/L; p = %.5f\n",
            effect_mg_l, manual_ci[1], manual_ci[2], test$p.value))
cat("Simulated educational observations only; no clinical or causal inference.\n")
print(sessionInfo())
