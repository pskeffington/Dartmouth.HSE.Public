# Unit 8 — Biomedical classification, calibration and safe evaluation

**Paul's Notes — original educational guide (2026-10-10).** No protected course source, real patient records, or published clinical model is reproduced. All observations are synthetic; results are illustrative only.

## Required learning objectives

Upon completing this module, independently:
1. Define patient, index time, binary outcome, look-ahead window and clinical *intended use*.
2. Split train/evaluation populations by independent patient IDs before model fitting or learned preprocessing.
3. Explain event prevalence, class imbalance, thresholded confusion matrices and why predictive values depend on prevalence.
4. Compute sensitivity, specificity, PPV, NPV, AUROC and Brier score and distinguish discrimination from calibration.
5. Describe proper holdout evaluation and why threshold tuning on a test set is leakage.
6. Produce probability-bin calibration data with counts, axes and scientific descriptions; identify uncertain low-count bins.
7. Identify conditions requiring temporal/geographic external validation and clinical impact assessment.
8. Discuss subgroup evaluation, applicability, patient safety, code/data provenance and reporting limits.

**Prerequisites:** Units 6–7; R data frames, probabilistic regression, confidence intervals, identifiers and splits.

## Research-to-execution evidence matrix

| Source and source type | Reported methods | Our independent teaching adaptation | Limitation |
| --- | --- | --- | --- |
| [Collins et al., 2024, TRIPOD+AI, DOI:10.1136/bmj-2023-078378](https://doi.org/10.1136/bmj-2023-078378) — consensus reporting guidance | A harmonized 27-item reporting checklist for regression and machine-learning clinical prediction studies | Record the cohort, outcome, predictors, missingness, performance and subgroup assessments before reporting | Reporting checklist is **not** a risk-of-bias tool or algorithm |
| [Sounderajah et al., 2025, STARD-AI, DOI:10.1038/s41591-025-03953-8](https://doi.org/10.1038/s41591-025-03953-8) — diagnostic-accuracy reporting consensus | Literature/scoping work, patient/public engagement and modified Delphi with >240 stakeholders; adds 18 new/modified AI reporting items | Compare diagnostic test/reference-standard evaluation with our prognostic-style risk prediction example | Article has an author correction dated 2026-07-13: read corrected publisher version. Diagnostic accuracy differs from risk forecasting |
| [Ben Hmido et al., 2025, DOI:10.1016/j.ejso.2025.110367](https://doi.org/10.1016/j.ejso.2025.110367) — systematic review | Searched MEDLINE, Embase, Web of Science and Cochrane for externally validated anastomotic-leakage models; extracted CHARMS, evaluated PROBAST and TRIPOD+AI; included 10 studies | Recreate the transparency appraisal headings, not the clinical model; teach why small event counts, missing-data gaps and validation limitations weaken results | Specialized surgical population; does not validate synthetic model |
| [Arshi et al., 2025, DOI:10.1016/j.jclinepi.2025.111902](https://doi.org/10.1016/j.jclinepi.2025.111902) — follow-up methodological cohort | Followed 109 regression-model development papers using forward citations; estimated external-validation and impact-assessment timing and surveyed authors | Distinguish internal evaluation, external validation and clinical impact in the model reporting worksheet | Study follows published models, not patients in our simulation |

## Execution and reasoning

1. **Set the question and observation grain.** Each row is one synthetic person. All predictive inputs are baseline age, biomarker (mg/L) and history flag; the outcome is a simulated future binary event. The specific clinical setting and time window are undefined, so the example cannot support clinical claims.
2. **Simulate transparently.** `set.seed` fixes deterministic generation; logistic `plogis` converts a constructed log-odds equation to simulated probability, then `rbinom` samples event outcomes. These assumptions deliberately simplify reality.
3. **Protect independent evaluation.** Split by patient ID prior to fitting. All modeling uses training records, and the holdout remains unseen until evaluation. Real repeated-visit datasets require grouping all rows from a patient together, not random row splitting.
4. **Use interpretable baseline.** Logistic regression is a transparent baseline model for probabilities, not a universal optimal method. `predict(type="response")` returns risk in [0,1].
5. **Discrimination:** AUROC is the proportion of positive-negative pairs ranked correctly (ties count one-half). It measures ranking, not calibrated risk. With no positives or no negatives AUC is undefined.
6. **Probability accuracy:** Brier score averages squared differences between observed binary events and predicted probabilities; it blends several performance dimensions and is prevalence-sensitive.
7. **Threshold consequences:** at fixed illustrative threshold 0.30 calculate TP/TN/FP/FN, sensitivity, specificity and predictive values. Changing the threshold changes errors and tradeoffs; do not select it on this holdout.
8. **Calibration summary:** fixed bins display mean predicted probability, observed event fraction and sample size. Small bins have unstable observed rates. A visualization must label risk scale, counts and synthetic origin; calibration intercept/slope and uncertainty are separate advanced tasks.
9. **Interpretation:** never label a holdout from the same simulated population 'external validation'; no bias/fairness audit or prospective impact study is performed.

## Run

```bash
Rscript 06_RESOURCES/R/examples/unit_08_classification.R
```

**Dependencies:** base R only. **Expected structure:** 450 train observations, 150 holdout; finite AUC and Brier; confusion-matrix totals sum to 150; summary table of nonempty probability bins, including bin n, mean risk and event fraction; R session information. Exact scores should be captured only after a successful clean R execution.

## Practice / error-driven learning

- Reproduce AUC with a small hand-built case (one positive and one negative); explain a tied pair.
- Compare thresholds 0.20, 0.30 and 0.50 **as prespecified instructional scenarios**, not retrospective test optimization.
- Add a future-only measurement and explain why it must be excluded from baseline models.
- Construct two observations per patient; demonstrate why row-level random splitting can leak patient information.
- Change prevalence in a separate simulation and compare predictive values; maintain explicit denominators.
- Sketch a probability-calibration graph: x=predicted risk, y=observed rate; annotate bins with counts, diagonal reference and limitations.

## Mastery evidence

A learner passes when they reproduce a patient-disjoint split, identify outcome timing and data types, distinguish discrimination/calibration, calculate metrics with explicit denominators, interpret clinical threshold tradeoffs, and state that internal synthetic holdout performance is **not** clinical validity. Incomplete if probabilities are treated as diagnoses, labels/future data leak into predictors, or metrics omit population and event counts.

## Quality gates

- Independently authored original prose/code: **DRAFT**
- Primary publisher/PubMed literature identity: **PARTIALLY VERIFIED**
- Method extraction: **ABSTRACT/PUBLISHER-LEVEL**, no published experiment reproduced
- Clean-session R execution: **NOT_RUN**
- Figures, testing and accessibility: **PENDING**
- Scientific review, originality guard and release: **PENDING**
