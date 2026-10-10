# Next units: evidence-to-code teaching guides

**Status:** independent draft; curriculum mapping not verified. **Literature freshness:** foundational sources listed below; a 2024–2026 primary-paper search and DOI verification are required before calling this a refreshed corpus. No paper execution has been independently reproduced here.

## Common unit contract
Each unit includes (1) independently phrased measurable learning objectives, (2) research question and evidence matrix with DOI, date, study type and limitations, (3) methods reconstruction distinguishing reported from inferred steps, (4) synthetic runnable example, (5) annotated rationale for every transformation and model, (6) expected outputs and failure modes, (7) checks for leakage, missingness, units and uncertainty, (8) exercises and rubric, (9) reproducibility manifest and (10) rights/provenance review.

## Unit 6 — Inference, estimation and uncertainty

**Full teaching edition:** [Unit 6 — Estimation, uncertainty and biomedical interpretation](UNIT_06_INFERENCE_TEACHING_GUIDE.md) · [Base R executable example](../R/examples/unit_06_inference.R). **Status:** authored; independent runtime verification pending.
**Objectives:** identify estimand and sampling unit; distinguish SD, SE and confidence interval; compare parametric and nonparametric procedures; report effect sizes and assumptions; interpret uncertainty without treating a p-value as probability of the null.

**Methods:** define cohort, denominator, outcome, grouping variable, missingness rule, estimand, confidence interval and sensitivity analysis before testing.

**Original R demonstration (synthetic):**
```r
set.seed(711)
patient_id <- sprintf("S%03d", seq_len(80))
treatment_group <- rep(c("control", "intervention"), each = 40)
biomarker_mg_l <- rnorm(80, mean = ifelse(treatment_group == "control", 10, 12), sd = 3)
study_data <- data.frame(patient_id, treatment_group, biomarker_mg_l)
stopifnot(!anyDuplicated(study_data$patient_id), all(is.finite(study_data$biomarker_mg_l)))
group_summary <- aggregate(biomarker_mg_l ~ treatment_group, study_data,
                           function(x) c(n = length(x), mean = mean(x), sd = sd(x)))
print(group_summary)
print(t.test(biomarker_mg_l ~ treatment_group, data = study_data))
```
**Reasoning:** fixed seed supports repeatability, explicit units prevent ambiguity, unique identifiers establish observation grain, and Welch's t-test does not require equal group variances. Synthetic group differences do not constitute evidence of a treatment effect.

**Mastery:** reproduce summary, explain CI, assess independence and plausible distribution assumptions, and describe why causal interpretation is unwarranted.

## Unit 7 — Regression and diagnostics
**Objectives:** specify outcome and predictors; distinguish linear and logistic links; interpret coefficient units; diagnose collinearity, influential observations and misspecification; avoid causal claims from association.

**Methods:** define a synthetic cohort with age, treatment and outcome; fit `lm()` and `glm(family = binomial())`; inspect residuals, separation and confidence intervals; compare prespecified alternatives. Split at patient level before any learned preprocessing.

**Mastery:** interpret a coefficient on its correct scale, demonstrate residual checks, and identify a deliberately invalid model.

## Unit 8 — Biomedical classification and evaluation
**Objectives:** define target and index time; prevent temporal and patient leakage; use stratified patient-level splits; distinguish discrimination from calibration; evaluate prevalence dependence and subgroup performance.

**Methods:** create synthetic longitudinal records; freeze holdout patient IDs; fit baseline logistic regression; evaluate sensitivity, specificity, predictive values, Brier score and calibration on untouched holdout; state threshold selection procedure.

**Mastery:** detect a leaked future variable, explain why accuracy alone is insufficient, and provide an auditable evaluation table.

## Unit 9 — Reproducible evidence and reporting
**Objectives:** produce data dictionary, environment manifest and deterministic scripts; separate exploratory from confirmatory analysis; document missingness and exclusions; map a study to a reporting checklist.

**Methods:** save synthetic source-generation script, input schema, environment information, tests and rendered report; use a clean session and verify figures and links.

**Mastery:** independently rerun analysis and identify unsupported claims.

## Unit 10 — Responsible biomedical AI
**Objectives:** document intended use and population; distinguish bias, drift and dataset shift; identify privacy and clinical deployment risks; construct human oversight and monitoring criteria.

**Methods:** build a model card and risk register for the Unit 8 synthetic classifier; test subgroup sample sizes and performance; specify escalation and rollback thresholds without claiming clinical validation.

**Mastery:** articulate when a model must not be deployed.

## Literature corpus: initial methodological anchors
These are **not** claimed to be newly discovered 2026 papers. Verify DOI and publication metadata before indexing.
- Collins GS et al. (2015), TRIPOD statement, *Annals of Internal Medicine*, DOI: 10.7326/M14-0697 — transparent prediction-model reporting.
- Wolff RF et al. (2019), PROBAST, *Annals of Internal Medicine*, DOI: 10.7326/M18-1376 — prediction-model risk of bias.
- Wilkinson MD et al. (2016), FAIR guiding principles, *Scientific Data*, DOI: 10.1038/sdata.2016.18 — findability, accessibility, interoperability, reuse.
- Johnson AEW et al. (2023), MIMIC-IV, *Scientific Data*, DOI: 10.1038/s41597-022-01899-x — clinical dataset provenance and longitudinal data structures.
- Collins GS et al. (2024), TRIPOD+AI, *BMJ*, DOI: 10.1136/bmj-2023-078378 — prediction model reporting including machine learning.

## Evidence matrix requirements for 2024–2026 refresh
For each candidate: citation; DOI/PMID; verified date; study design; population; data license; target/estimand; preprocessing; software/version; split unit; model and assumptions; uncertainty/calibration; reported limitations; code availability; reproduction status (NOT_RUN / PASS / FAIL); instructional mapping; independent interpretation. Prefer primary methodological papers and official documentation. Never present a reported method as independently reproduced without execution evidence.

## Publication gates
P0 public independent scope; P1 original objectives; P2 verified sources and fresh literature; P3 full original notes; P4 runnable examples; P5 clean-session tests; P6 scientific/accessibility review; P7 provenance/rights; P8 PR and navigation; P9 refresh. A newly created draft satisfies none of the later gates by itself. Protected source files remain excluded; original documentation may proceed through the standard originality checks.
