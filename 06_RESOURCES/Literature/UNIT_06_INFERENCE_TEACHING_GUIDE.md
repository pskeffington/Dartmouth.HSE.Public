# Unit 6 — Estimation, uncertainty, and biomedical interpretation

> **Paul's Notes | independent study companion.** Not an institutional lesson, course requirement, or clinical analysis. All example patient data are synthetic. Last research scan: 2026-10-10. Code execution in an independent R environment remains pending.

## Learning objectives and prerequisites

After this unit, learners can: (1) define observational unit, target population, outcome, exposure and estimand; (2) explain mean, SD, SE and a 95% confidence interval; (3) contrast absolute group differences and standardized effects; (4) justify a Welch two-sample t-test and its assumptions; (5) distinguish statistical evidence from clinical importance; (6) explain why an observational or simulated comparison does not prove causality; (7) independently run and test an analysis with explicit measurement units; and (8) write a report giving the estimate, interval, p-value, limitations and clinically meaningful threshold.

**Prerequisites:** R vectors and data frames, indexing, missing values, basic plots and a shell capable of running `Rscript`.

## 1. Research question before code

**Illustrative question:** in a synthetic study of 80 participants, how does the mean biomarker concentration differ between two labeled groups? The **unit of analysis** is one participant; outcome `biomarker_mg_l` is continuous and measured in mg/L. The **estimand** is mean(intervention) minus mean(control), in mg/L. The simulation labels are not a real randomized trial and no clinical effect is established. The assignment mechanism and clinical importance threshold would require justification in actual research.

Predefine: eligibility, one row per participant, grouping definitions, measurement units, handling of missing/outlying observations, testing strategy and sensitivity analysis. For repeated observations, the independent-samples t-test below would be inappropriate without accounting for within-patient correlation.

## 2. Evidence-to-method matrix (public research scan)

| Source | Design and what its investigators did | Transferable computational method | Teaching relevance / limitation |
| --- | --- | --- | --- |
| [Rovetta, Piretta & Mansournia (2025), Lancet Regional Health — Southeast Asia](https://doi.org/10.1016/j.lansea.2025.100534) | Methodological commentary reinterpreting clinical research findings in terms of compatibility rather than a binary significance rule | Report point estimate and interval; investigate all values compatible with data/model, not only p < 0.05 | Commentary, not a new clinical trial; pedagogical interpretation rather than effect replication |
| [Disparity between statistical significance and clinical importance (2025), BMJ Open](https://doi.org/10.1136/bmjopen-2025-100411) | Methodological study of 500 published RCTs; distinguished statistical-significance status from clinical-importance status using trial-specified differences; analyzed discordance | Define meaningful difference before looking at p-values; compare effect/CI to threshold | Literature audit, not evidence for the synthetic biomarker |
| [Zhang et al. (2026), Statistics in Medicine](https://doi.org/10.1002/sim.70643) | Methodological comparison of bootstrap and asymptotic confidence interval methods in small-sample propensity-score analyses | Teach why resampling procedure and estimated nuisance parameters influence coverage | Propensity-score setting differs from the independent Welch example; do not transfer its numerical results |
| [A New Look at P Values for Randomized Clinical Trials (2024), NEJM Evidence](https://doi.org/10.1056/EVIDoa2300003) | Analyses of primary results from 23,551 trials extracted from systematic reviews; examined power and effect exaggeration | Distinguish observed effect, uncertainty and replication risks | Trial-level meta-research; do not present as an individual clinical estimate |
| [AHA/ASA statistical recommendations](https://www.ahajournals.org/statistical-recommendations) | Journal reporting guidance | Present estimate, confidence interval, then exact p-value; specify model and prespecification | Journal guidance, not an experimental evaluation |

The table records **reported methods only**. No original study's supplementary code or raw clinical data have been executed here. For formal literature extraction record PMID/DOI, design, samples, inclusion criteria, version and licensing, statistical model, code availability, limitations and independent reproduction status.

## 3. Concepts and calculation

For group `g`, report `n_g`, mean `xbar_g` and sample SD `s_g`. The sample standard error of a group mean is `s_g / sqrt(n_g)`. SD describes variation in individuals; SE describes sampling variability of the estimated group mean. The Welch estimate is `delta = xbar_intervention - xbar_control` and its estimated standard error is `sqrt(s_i^2/n_i + s_c^2/n_c)`. Welch's degrees of freedom account for potentially unequal variances.

A frequentist 95% confidence-interval procedure has approximately 95% long-run coverage under its model and sampling assumptions. It is not a 95% posterior probability assigned to this particular fixed parameter. A p-value is a probability of data at least as incompatible with the specified null as those observed, conditional on its assumptions; it is neither the probability the null is true nor a measure of clinical importance.

## 4. Run the original worked example

From repository root:

```bash
Rscript 06_RESOURCES/R/examples/unit_06_inference.R
```

This file uses **base R only**, prints a data-contract summary and group estimates, then computes both manually and with `t.test` a two-sided Welch mean difference and its 95% interval. The output is deterministic because the seed is fixed. The code deliberately stops on duplicate patient IDs, invalid units, missing values, unexpected groups and numerical disagreement.

**Why each step matters:**
1. `set.seed(711)` makes synthetic generation reproducible, not intrinsically realistic.
2. `sprintf` creates stable participant identifiers, allowing uniqueness checks.
3. `rnorm` simulates a transparent normal-data assumption and group shifts; it does not reproduce a published trial.
4. `stopifnot` enforces analysis grain, finite measurements, legal categories and data size.
5. `mean`, `sd` and `length` keep SD and SE conceptually separate.
6. `t.test(..., var.equal = FALSE)` uses Welch inference rather than quietly imposing equal variances.
7. The manual and built-in calculations are checked against each other; a mismatch fails the script.
8. `sessionInfo()` records an R environment snapshot for later reproduction.

## 5. Interpretation worksheet

In your own words fill out: observational unit; sample size; group means and SDs; signed mean difference with mg/L; 95% CI; two-sided p-value; assumptions; minimum clinically important difference (if defensibly sourced); why the result is **not** causal or clinically validated.

Avoid these errors: "95% probability the true value lies in this interval"; "p=0.04 means 96% probability the intervention works"; "not significant means no difference"; "statistically significant means clinically important".

## 6. Independent practice (not assessed course solutions)

- **A. Precision:** Increase sample size to 200 per group without changing the SD; record how SE and CI widths typically change across seeds.
- **B. Variance sensitivity:** Increase variance only in one group; compare Welch and pooled-variance assumptions and explain the choice.
- **C. Missingness:** Introduce missing biomarker values; explicitly state missingness assumptions and implement a defensible complete-case description without silently deleting rows.
- **D. Repeated measures:** Duplicate visit rows per participant and show why the unit-of-analysis check rejects them. Explain clustered or longitudinal alternatives before implementing them.
- **E. Clinical relevance:** Propose a separately justified importance threshold and classify whether the interval is compatible with clinically meaningful and negligible values.

## 7. Mastery rubric

**Ready:** correct outputs and data contract; confidence interval described accurately; effect and units reported; all assumptions visible; statistical versus clinical interpretation distinguished; synthetic data and lack of causal inference explicitly disclosed. **Revision needed:** numerical result with no uncertainty, hidden exclusions, unlabeled units, false causal claims, or treating p-value thresholds as proof.

## 8. Gate and publishing record

- P0 independently authored public subject: PASS.
- P1 measurable original objectives: DRAFT.
- P2 recent citation discovery: PARTIAL (2024–2026 sources found, no complete appraisal).
- P3 independent prose and example code: DRAFT.
- P4 execution and expected outputs: NOT_RUN.
- P5 clean-session testing: NOT_RUN.
- P6 scientific/accessibility review: REVIEW_REQUIRED.
- P7 rights/provenance: REVIEW_REQUIRED.
- P8 publication/navigation: PENDING (draft PR).
- P9 refresh: PENDING.

Last edited 2026-10-10. Never equate a committed file with a scientifically approved lesson.
