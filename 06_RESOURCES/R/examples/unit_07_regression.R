# Unit 7: synthetic patient-level regression and diagnostics, base R only.
# All labels are invented; never use as a clinical prediction instrument.
set.seed(712)
n <- 300L
patient_id <- sprintf("P%04d", seq_len(n))
age_years <- round(runif(n, 25, 85))
study_group <- factor(sample(c("control", "intervention"), n, replace=TRUE),
                      levels=c("control", "intervention"))
history_flag <- rbinom(n, 1, 0.35)
biomarker_mg_l <- 5 + 0.12 * age_years + 1.6 * (study_group == "intervention") +
  1.4 * history_flag + rnorm(n, sd=2.5)
event_probability <- plogis(-5 + 0.055 * age_years +
                             0.5 * (study_group == "intervention") + 0.8 * history_flag)
event_flag <- rbinom(n, 1, event_probability)
patient_data <- data.frame(patient_id, age_years, study_group, history_flag,
                           biomarker_mg_l, event_flag)
stopifnot(nrow(patient_data)==n, !anyDuplicated(patient_data$patient_id),
          !anyNA(patient_data), all(is.finite(patient_data$biomarker_mg_l)),
          all(patient_data$event_flag %in% c(0,1)),
          all(patient_data$age_years >= 0))
# Split by person before estimating models; reproducible base R sampling.
set.seed(713)
training_index <- sample.int(n, size=floor(0.7*n), replace=FALSE)
training_data <- patient_data[training_index, , drop=FALSE]
test_data <- patient_data[-training_index, , drop=FALSE]
stopifnot(length(intersect(training_data$patient_id, test_data$patient_id))==0L,
          nrow(training_data)+nrow(test_data)==n)
linear_fit <- lm(biomarker_mg_l ~ age_years + study_group + history_flag,
                 data=training_data)
logistic_fit <- glm(event_flag ~ age_years + study_group + history_flag,
                    data=training_data, family=binomial(link="logit"))
linear_prediction <- predict(linear_fit, newdata=test_data)
risk_prediction <- predict(logistic_fit, newdata=test_data, type="response")
stopifnot(all(is.finite(linear_prediction)), all(is.finite(risk_prediction)),
          all(risk_prediction >= 0 & risk_prediction <= 1),
          all(is.finite(coef(linear_fit))), all(is.finite(coef(logistic_fit))))
mae_mg_l <- mean(abs(test_data$biomarker_mg_l-linear_prediction))
rmse_mg_l <- sqrt(mean((test_data$biomarker_mg_l-linear_prediction)^2))
brier_score <- mean((test_data$event_flag-risk_prediction)^2)
max_cooks_distance <- max(cooks.distance(linear_fit))
max_leverage <- max(hatvalues(linear_fit))
stopifnot(is.finite(mae_mg_l), is.finite(rmse_mg_l), is.finite(brier_score),
          brier_score>=0 && brier_score<=1, is.finite(max_cooks_distance),
          is.finite(max_leverage))
cat(sprintf("Train n=%d; test n=%d; overlap=0\n",nrow(training_data),nrow(test_data)))
cat(sprintf("Linear holdout MAE=%.4f mg/L, RMSE=%.4f mg/L\n",mae_mg_l,rmse_mg_l))
cat(sprintf("Logistic holdout Brier=%.4f; event rate=%.4f; mean predicted=%.4f\n",
            brier_score,mean(test_data$event_flag),mean(risk_prediction)))
cat(sprintf("Linear max Cook distance=%.5f, max leverage=%.5f\n",
            max_cooks_distance,max_leverage))
print(summary(linear_fit)$coefficients)
print(summary(logistic_fit)$coefficients)
print(sessionInfo())
