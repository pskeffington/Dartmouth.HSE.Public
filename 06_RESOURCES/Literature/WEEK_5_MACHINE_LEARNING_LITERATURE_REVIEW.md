# Week 5 machine learning — independent biomedical literature review

[Public literature index](README.md) · [Validated-code corpus protocol](VALIDATED_CODE_CORPUS.md) · [Biomedical conventions](BIOMEDICAL_CODING_STANDARDS.md)

**Review type:** focused, narrative scoping bibliography; **initiated:** 2026-10-10. This is not a systematic review, an institutional lecture derivative, an official Week 5 syllabus, or proof that any linked example was executed. The maintainer identifies Week 5 as machine learning; detailed classroom learning objectives remain unverified. All text below is independently authored from public references.

## Guiding question

Which primary software manuals and peer-reviewed methods should govern a reproducible introductory biomedical machine-learning workflow, from a defined prediction target through leakage-safe evaluation and scientifically honest communication?

## Evidence matrix

| ID | Primary source | Source type | Core principle | Review/application |
| --- | --- | --- | --- | --- |
| ML-01 | [scikit-learn: supervised learning](https://scikit-learn.org/stable/supervised_learning.html) | Primary software manual | Distinguish regression and classification and start with interpretable baselines | Compare linear/logistic models to trees or ensembles only under matching splits and metrics |
| ML-02 | [scikit-learn: cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) | Primary software manual | Estimate performance on samples not used for fitted parameters | Stratify if appropriate, but split by participant/site/time where dependence demands it |
| ML-03 | [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Primary software manual | Avoid inconsistent preprocessing and information leakage | Fit preprocessing *inside* each training fold; never fit a scaler or imputer on holdout data |
| ML-04 | [scikit-learn: probability calibration](https://scikit-learn.org/stable/modules/calibration.html) | Primary software manual | Calibration and discrimination answer distinct questions | Examine reliability curves and Brier score alongside AUROC and recall |
| ML-05 | [scikit-learn: model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | Primary software manual | Select metrics based on target prevalence and cost of errors | Report confusion matrix denominators; do not rely on accuracy alone for imbalanced outcomes |
| ML-06 | [scikit-learn: pipelines](https://scikit-learn.org/stable/modules/compose.html#pipeline-chaining-estimators) | Primary software manual | Package transforms and estimators into one fitted workflow | Confirm identical preprocessing for validation and inference |
| ML-07 | [tidymodels: resampling](https://rsample.tidymodels.org/) | Primary software manual | Separate resampling specifications from fitting recipes | Demonstrate R-compatible resampling without sharing holdout information |
| ML-08 | [tidymodels: recipes](https://recipes.tidymodels.org/) | Primary software manual | Declare feature preparation as explicit, estimable steps | Verify predictor selection, missingness and fold-specific preprocessing |
| ML-09 | [TRIPOD+AI — Collins et al., BMJ 2024](https://doi.org/10.1136/bmj-2023-078378) | Peer-reviewed reporting guideline | Transparent reporting for prediction models developed or evaluated with regression or ML | Map objectives, design, participants, outcome, validation, performance and limitations to the updated 27-item checklist |
| ML-10 | [PROBAST+AI — Moons et al., BMJ 2025](https://doi.org/10.1136/bmj-2024-082505) | Peer-reviewed appraisal tool | Evaluate model-development quality and evaluation risk of bias/applicability | Review participant selection, predictors, outcome and analysis separately |
| ML-11 | [Steyerberg et al., Epidemiology 2010](https://doi.org/10.1097/EDE.0b013e3181c30fb2) | Peer-reviewed methods | Clinical prediction performance is multidimensional | Contrast discrimination, calibration and clinical usefulness |
| ML-12 | [Vickers and Elkin, Medical Decision Making 2006](https://doi.org/10.1177/0272989X06295361) | Peer-reviewed methods | Decision-curve analysis contextualizes threshold-dependent utility | Explain net benefit only when a defined decision and threshold make it meaningful |
| ML-13 | [Wolpert and Macready, IEEE TEC 1997](https://doi.org/10.1109/4235.585893) | Foundational methods | No universally optimal learning algorithm exists across all problems | Motivate baselines and explicit inductive assumptions; avoid 'best model' claims |
| ML-14 | [JMLR: scikit-learn — Pedregosa et al. 2011](https://jmlr.org/papers/v12/pedregosa11a.html) | Peer-reviewed software article | Reusable ML implementation and documented estimator interfaces | Cite software and capture exact package version in the environment manifest |

**Evidence status:** sources identified and linked; per-source full-text appraisal, license determination, versions and local execution tests are **PENDING**. The methods papers support methodological decisions, not a guarantee of clinical efficacy.

## Learning sequence (independent proposal)

1. Translate a biomedical question into outcome, index time, prediction horizon and eligible predictors. Distinguish prediction from causal inference.
2. Inspect source schema and units; resolve patient, encounter, specimen and site identifiers. Preserve source fields before any internal renaming.
3. Distinguish supervised learning (regression/classification) from unsupervised learning (clustering and dimensionality reduction). State what labels mean.
4. Fit a transparent baseline. Explain intercept, coefficients or model output on the correct scale.
5. Split by the actual independent unit; participant groups, time-order, institutions and repeated measurements can invalidate a random row split.
6. Keep imputation, scaling, encoding, feature selection, sampling and hyperparameter tuning within training folds.
7. Evaluate on untouched test data: sensitivity, specificity, PPV, NPV, ROC/PR curves where applicable; calibration intercept/slope and Brier score for probabilities; uncertainty intervals where justified.
8. Examine prevalence shift, missingness, unequal performance across meaningful groups, transportability and decision consequences.
9. Present an auditable visual report with labeled axes, units where relevant, outcome definition, denominators and interpretation.
10. Record seed, runtime, locked dependencies, algorithm configuration, splits, data provenance and limits of intended use.

## Model comparison checklist

| Question | Evidence needed |
| --- | --- |
| Does the target exist at the intended decision time? | Document target time and prediction horizon |
| Is the same person's data in both train and test? | Participant-group overlap test, zero shared IDs |
| Can preprocessing see test statistics? | Pipeline boundaries inspected and tested |
| Were hyperparameters tuned on the final holdout? | Untouched holdout plus cross-validation log |
| Are class counts and prevalence reported? | Numerators, denominators and class definitions |
| Does AUROC conceal poor calibration or PPV? | Calibration results and precision-recall metrics |
| Is the study reproducible? | Pinned environment, fixed seeds, source manifest and automated tests |
| Can results be called clinically validated? | Independent clinical review, external evaluation and appropriate intended-use evidence; otherwise state not validated |

## Example figure specifications

- **Class balance:** count plot with outcome labels, sample size and denominator.
- **Confusion matrix:** actual-versus-predicted label definitions and raw counts; optional normalized view separately labeled.
- **ROC and precision–recall:** labeled axes, baseline prevalence for PR where relevant, AUC annotation and split provenance.
- **Calibration:** predicted risk against observed frequency, binning method, reference diagonal, sample size and Brier score.
- **Feature effects:** coefficient or importance units/scale and uncertainty/limitations; predictive association must not be interpreted as causation.
- **Data partition:** participant/site/time overlap report instead of a merely decorative split chart.

Use accessible, documented semantic mappings rather than asserting there is one mandated biomedical color palette.

## Proposed reproducibility gates

- **ML-G0 bibliography:** stable source identifiers, evidence types and research question — draft recorded here.
- **ML-G1 appraisal:** inspect source methods, usage terms, applicability and contradictions — pending.
- **ML-G2 executable fixtures:** original synthetic binary classification and continuous outcome examples in R and Python — pending.
- **ML-G3 leakage tests:** deliberately invalid example produces failed guard; clean grouped split produces zero participant overlap — pending.
- **ML-G4 metrics:** fixture-checked confusion matrix, sensitivity/specificity and probability calibration — pending.
- **ML-G5 publication:** originality/source-boundary review, correct licenses, accessible figures, tests and navigation — pending.

**Safety and scope:** do not upload classroom assets, protected examples, identifiable health data, patient-derived row samples or clinical decision-support claims. This bibliography alone does not certify any code.
