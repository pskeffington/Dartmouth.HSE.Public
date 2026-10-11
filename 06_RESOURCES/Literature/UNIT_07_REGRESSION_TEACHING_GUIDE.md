# Unit 7 — Biomedical regression, diagnostics, and model interpretation

**Paul's Notes | independently authored educational resource | 2026-10-10.** This is a self-study topic companion, not an institutional course syllabus or clinical model. The data are generated synthetically. The linked literature supports methodological choices, not estimates derived from this demonstration.

## Required learning objectives

By the end of this unit, the learner will be able to:
1. Identify observational unit, target population, outcome type, predictors, estimand and analysis purpose (explanation versus prediction).
2. Write and interpret linear and logistic regression equations, including coefficient units, odds ratios and baseline/reference category.
3. Explain outcome-appropriate link functions and the difference between fitted conditional means and event probabilities.
4. Detect nonlinearity, unequal residual variance, collinearity, influential observations, separation and data leakage.
5. Explain confounding, effect modification and why adjusting for a collider or post-outcome variable can introduce bias.
6. Enforce patient-level data splitting and evaluate out-of-sample errors and probability calibration.
7. Produce an auditable model report: sample size, missingness, seed, assumptions, coefficients, intervals, diagnostics and limitations.

**Prerequisites:** Units 1–6: R objects, data frames, plotting, independent sampling, uncertainty and confidence intervals.

## Method reconstruction: evidence before syntax

| Evidence | Reported method / scope | What the learner implements | Caution |
| --- | --- | --- | --- |
| [Collins et al., TRIPOD+AI, BMJ 2024, DOI:10.1136/bmj-2023-078378](https://doi.org/10.1136/bmj-2023-078378) | Consensus-based updated 27-item reporting guidance for regression or ML clinical prediction models | Declare model purpose, population, predictors, outcomes, missingness, performance and uncertainty | Reporting guidance is not a validation of this synthetic model |
| [Cohen & Bossuyt, BMJ 2024, DOI:10.1136/bmj.q824](https://doi.org/10.1136/bmj.q824) | Editorial analysis of the TRIPOD+AI reporting update | Explain why transparency is a prerequisite for appraisal | Editorial, not an empirical model comparison |
| [Wolff et al., PROBAST, Ann Intern Med 2019, DOI:10.7326/M18-1376](https://doi.org/10.7326/M18-1376) | Structured risk-of-bias and applicability assessment of prediction-model studies | Complete a design/data/analysis limitations checklist | Foundational older standard; check current revisions |
| [R Core Team, stats::lm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html) and [stats::glm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html) | Software reference and mathematical conventions | Explicit formula, family, link and prediction scale | Documentation does not prove clinical correctness |

**Corpus refresh rule:** for each 2024–2026 empirical candidate extract DOI/PMID, exact date, target population, outcome, sample size, preprocessing, predictors, model, calibration, internal/external evaluation, uncertainty, access/licensing, code availability and limitations. Mark `REPORTED_ONLY` until the published implementation is separately reproduced. Do not mislabel an editorial or guideline a new experiment.

## Statistical and biomedical reasoning

### Linear regression

The working model is `E(Y | X) = beta0 + beta1 X1 + beta2 X2 + ...`. In the synthetic example, `Y` is biomarker concentration **mg/L**. An age coefficient is an expected mg/L difference per **year** at fixed other included predictors, under the fitted linear model. Inspect residual-versus-fitted and normal QQ plots; departures may imply incorrect functional form, unusual observations or uncertainty estimates requiring revision. Normal residuals matter to small-sample classical intervals, not the arithmetic ability of `lm` to fit a line. Residual heteroscedasticity can invalidate default SEs.

### Logistic regression

For a binary event `D`, `logit(P(D=1 | X)) = beta0 + beta1 X1 + ...`. The exponential of an age coefficient is an **odds ratio per year**. It is *not* the risk ratio and not an absolute probability increase. Predicted probabilities require `predict(..., type="response")`. The model is a synthetic prediction illustration, not an approved diagnosis.

### Critical analysis decisions

One row per participant and a declared index time are enforced here. No future information appears in predictors. A fixed 70/30 patient-level split is created **before** modeling, with an untouched test set. Only the training data estimate coefficients. Holdout MAE/RMSE and Brier score are descriptive, not a claim of external validation. Demonstrate collinearity with a correlation check and fit diagnostics with leverage and Cook's distance. Do not remove influential observations automatically: first investigate whether records are errors or legitimate extremes.

## Run the example

```bash
Rscript 06_RESOURCES/R/examples/unit_07_regression.R
```

**Script walkthrough:**
1. Generate stable participant IDs and observed-at-baseline age, group and binary history.
2. Generate a continuous biomarker in mg/L and simulated event from a known logistic data-generating model.
3. Assert schema, one row per participant, finite values and legal event levels.
4. Split participants deterministically; check zero overlap before fitting.
5. Fit `lm` and `glm(family=binomial)` on training records only.
6. Orient every prediction onto its correct scale: mg/L for `lm`, probability for `glm`.
7. On held-out observations compute MAE, RMSE, Brier score and overall observed event rate.
8. Check `hatvalues`, `cooks.distance` and finite coefficients. Inspect residual plots and predictor correlation as additional exercises; the script does not produce those plots.
9. Print session information for reproduction.

**Scientific interpretation:** regression coefficients are conditional associations; a formula and a train/test split cannot establish causal identifiability, fairness, generalizability or safe use. Synthetic events and biomarker values are not evidence about patients.

## Independent laboratory exercises

1. **Predictor coding:** change group reference level, refit, and explain why predictions stay equivalent despite a coefficient sign change.
2. **Nonlinearity:** generate a quadratic age response and compare linear residual patterns to a prespecified `I(age_years^2)` fit; do not interpret this as data-mining proof.
3. **Collinearity:** create `age_decades = age_years / 10` alongside `age_years`; observe aliased predictors and explain rank deficiency.
4. **Leakage:** append a mock `future_diagnosis` column; demonstrate that including it as a baseline predictor violates index-time constraints (do not fit it).
5. **Calibration:** bin held-out probabilities into predeclared intervals, compare predicted versus observed event rates and explain sampling uncertainty in small bins.
6. **Robustness:** introduce heteroscedastic residuals and justify alternative uncertainty approaches, including what base `lm` SEs assume.

## Competency check

A satisfactory submission identifies outcome scales, units, population and observational grain; labels an odds ratio correctly; interprets residual and influence diagnostics; reports at least two holdout metrics; documents missingness and leakage review; supplies fully reproducible code; and states limitations. **Fail/revise** if event probability and odds are confused, holdout data leak into fitting, observations are treated as independent when repeated, or clinical effectiveness is claimed.

## Gate ledger

| Gate | Status | Remaining evidence |
| --- | --- | --- |
| P0–P1 independent scope and measurable objectives | DRAFT | Review against public-domain competencies |
| P2 literature | PARTIAL | Verify more current empirical studies and extracted execution details |
| P3–P4 guide and working example | DRAFT | Synthetic output captured; human educational review pending |
| P5 execution and numerical verification | PASS (synthetic contracts) | Local clean-session R 4.4.3 run on 2026-10-11; broader scientific review pending |
| P6 scientific/accessibility | REVIEW_REQUIRED | Statistical and human review |
| P7 originality/provenance | REVIEW_REQUIRED | Private-source guard remains for source-derived work |
| P8 publishing/navigation | DRAFT_PR | Merge only after approvals |
| P9 literature/software refresh | PLANNED | Future maintenance |
