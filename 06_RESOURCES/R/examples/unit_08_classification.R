# Unit 8: original synthetic biomedical binary classification.
# Base R only. Not clinical data and not a validated medical device.
set.seed(814)
n_patients <- 600L
patient_id <- sprintf("P%04d", seq_len(n_patients))
age_years <- sample(30:85, n_patients, replace = TRUE)
biomarker_mg_l <- pmax(0.1, rnorm(n_patients, 9 + 0.06 * age_years, 3))
history_flag <- rbinom(n_patients, 1, 0.4)
log_odds <- -5.5 + 0.038 * age_years + 0.14 * biomarker_mg_l + 0.7 * history_flag
event_flag <- rbinom(n_patients, 1, plogis(log_odds))
study_data <- data.frame(patient_id, age_years, biomarker_mg_l,
                         history_flag, event_flag)
stopifnot(!anyDuplicated(study_data$patient_id),
          !anyNA(study_data), all(is.finite(study_data$biomarker_mg_l)),
          all(study_data$event_flag %in% 0:1))
# Split patients once; no row can occur in both partitions.
set.seed(815)
train_rows <- sample.int(n_patients, floor(0.75 * n_patients))
train <- study_data[train_rows, , drop = FALSE]
test <- study_data[-train_rows, , drop = FALSE]
stopifnot(length(intersect(train$patient_id, test$patient_id)) == 0,
          all(c(0, 1) %in% train$event_flag),
          all(c(0, 1) %in% test$event_flag))
fit <- glm(event_flag ~ age_years + biomarker_mg_l + history_flag,
           data = train, family = binomial(link = "logit"))
risk <- as.numeric(predict(fit, newdata = test, type = "response"))
observed <- test$event_flag
stopifnot(length(risk) == nrow(test), all(is.finite(risk)),
          all(risk >= 0 & risk <= 1))
# Pairwise AUC calculates P(score_positive > score_negative) plus half ties.
pos <- risk[observed == 1]
neg <- risk[observed == 0]
auc <- mean(outer(pos, neg, FUN = function(a, b) as.numeric(a > b) +
                    0.5 * as.numeric(a == b)))
brier <- mean((observed - risk)^2)
# Threshold predeclared as an educational choice, not optimized on test.
threshold <- 0.30
predicted <- as.integer(risk >= threshold)
tp <- sum(predicted == 1 & observed == 1)
tn <- sum(predicted == 0 & observed == 0)
fp <- sum(predicted == 1 & observed == 0)
fn <- sum(predicted == 0 & observed == 1)
sensitivity <- if (tp + fn) tp / (tp + fn) else NA_real_
specificity <- if (tn + fp) tn / (tn + fp) else NA_real_
ppv <- if (tp + fp) tp / (tp + fp) else NA_real_
npv <- if (tn + fn) tn / (tn + fn) else NA_real_
stopifnot(tp + tn + fp + fn == nrow(test), is.finite(auc), is.finite(brier))
# Equal-width bins: no fitting or recalibration performed using holdout labels.
breaks <- seq(0, 1, by = 0.2)
bin <- cut(risk, breaks = breaks, include.lowest = TRUE)
calibration <- aggregate(cbind(predicted_risk = risk, observed_event = observed),
                         by = list(probability_bin = bin), FUN = mean)
calibration$n <- as.integer(table(bin)[as.character(calibration$probability_bin)])
stopifnot(sum(calibration$n) == nrow(test))
cat(sprintf("Train n=%d; holdout n=%d; train prevalence=%.3f; holdout prevalence=%.3f\n",
            nrow(train), nrow(test), mean(train$event_flag), mean(observed)))
cat(sprintf("AUC=%.4f; Brier=%.4f; threshold=%.2f\n", auc, brier, threshold))
cat(sprintf("Sensitivity=%.3f; specificity=%.3f; PPV=%.3f; NPV=%.3f\n",
            sensitivity, specificity, ppv, npv))
print(calibration)
cat("Clinical utility, external validation and deployment authorization: NOT ASSESSED.\n")
print(sessionInfo())
