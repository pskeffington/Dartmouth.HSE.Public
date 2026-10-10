# Biostatistics: independent public-reference and evidence matrix

[Paul's Notes](../../README.md) · [Program roadmap](PROGRAM_COMPANION_ROADMAP.md) · [Literature index](README.md)

**P0–P2 planning artifact | October 10, 2026 | Status: PRELIMINARY / REVIEW REQUIRED**

This document is an independently assembled index of public statistical guidance, not a course teaching guide, syllabus, assignment sequence or claim of equivalence to HSE 712. The HSE 712 course label is provided by the maintainer; current institutional objectives and requirements have not been verified. The references below support independent subject research only. This document includes no private-source comparison, lecture-derived objective, restricted data or classroom exercise.

## Evidence boundaries

- **P0 — Scope:** Introductory biostatistics is the proposed domain. Confirm any official course-specific scope separately using authorized sources. Until then, all themes here are **provisional** and organized by statistical dependency, not classroom order.
- **P1 — Candidate competencies:** Define estimands, observational units and sampling; distinguish populations from samples; summarize categorical and continuous measurements with meaningful units; describe uncertainty and confidence-interval interpretation; assess hypothesis-testing assumptions; explain regression coefficients on their modeled scale; distinguish association from causation; plan for missingness, multiple comparisons and transparent reporting. These are general, independently formulated methodological topics, not verified course learning objectives.
- **P2 — Evidence:** The reference matrix below identifies primary guidance, a concrete question to investigate, and an important limitation. Link checks, scientific review and version revalidation remain pending.
- **P3 onward — Not authorized by this artifact:** No published course-specific teaching sequence, examples, assignments, or answer keys. Any companion lesson is separately subject to the publication boundary in [AGENTS.md](../../AGENTS.md).

## Public primary-source reference matrix

| ID | Domain / source | Evidence role | Practical reference question | Scope or limitation |
| --- | --- | --- | --- | --- |
| BS-01 | [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) | Public statistical methods handbook | How should distribution shape, variability, estimation, and diagnostics affect analysis choices? | Many examples are industrial; translate only general statistical principles into biomedical work |
| BS-02 | [R: Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html) | Primary software documentation | Which base R functions and objects can represent summaries and simple fitted models? | Computational implementation is not proof of scientific validity |
| BS-03 | [R: stats package reference](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/00Index.html) | Primary software documentation | What do common statistical functions accept, compute, and return? | Development reference may differ from installed R; record versions |
| BS-04 | [STROBE statement](https://www.strobe-statement.org/) | Observational-study reporting guidance | What study-design, participants, missing-data and results details should be reported? | Reporting guidance is not an analytical recipe or risk-of-bias certification |
| BS-05 | [CONSORT statement](https://www.consort-statement.org/) | Randomized-trial reporting guidance | How are trial flow, interventions, outcomes and precision made explicit? | Applies to randomized trials; do not apply trial assumptions to observational evidence |
| BS-06 | [SAMPL guidelines](https://www.equator-network.org/reporting-guidelines/sampl/) | Statistical reporting guidance | How should statistical methods, uncertainty, effect sizes and numeric precision be communicated? | Consult full guidance and its applicability before using as a checklist |
| BS-07 | [ASA Statement on Statistical Significance and P-Values](https://doi.org/10.1080/00031305.2016.1154108) | Professional interpretive guidance | What can and cannot be inferred from a p-value? | A p-value does not quantify effect size or the probability a hypothesis is true |
| BS-08 | [ICH E9 Statistical Principles for Clinical Trials](https://www.ema.europa.eu/en/ich-e9-statistical-principles-clinical-trials-scientific-guideline) | Regulatory statistical principles | How do clinical trial objectives, analysis populations and planned methods connect? | Trial-focused and not a blanket requirement for coursework |
| BS-09 | [ICH E9(R1) estimands addendum](https://www.ema.europa.eu/en/ich-e9-r1-addendum-estimands-sensitivity-analysis-clinical-trials-scientific-guideline) | Regulatory estimand framework | Which treatment effect is being estimated and how are intercurrent events handled? | Specialized trial context; basic estimand concepts may still be useful |
| BS-10 | [CDC NHANES analytic guidelines](https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx) | Public survey-methods guidance | When do survey weights, clusters and strata change estimation? | NHANES guidance is cycle- and design-dependent; do not assume simple random sampling |
| BS-11 | [R survey package documentation](https://cran.r-project.org/package=survey) | Statistical software reference | How are complex survey designs represented in R? | Requires correct design variables and weight interpretation |
| BS-12 | [Cochrane Handbook](https://training.cochrane.org/handbook) | Evidence synthesis methodology | How do heterogeneity, effect measures and bias affect synthesis? | Evidence synthesis is a distinct later-stage activity |

## Dependency-based independent study map

| Theme | Required prior knowledge | Evidence to consult | Later verification target |
| --- | --- | --- | --- |
| Statistical units and sampling | Identifiers, rows vs. observations, variable types | BS-01, BS-04, BS-10 | Identify unit, target population, recruitment/selection and denominator |
| Descriptive summaries | Missingness, numerical vs. categorical variables, measurement units | BS-01, BS-02, BS-03 | Verify denominators, group sizes and summary statistics |
| Estimation and uncertainty | Distributions, sampling variability and standard errors | BS-01, BS-06, BS-07 | Explain interval coverage without treating one realized interval as a posterior probability |
| Testing and multiplicity | Explicit null, statistic, assumptions and planned contrasts | BS-01, BS-06, BS-07 | Separate practical importance from statistical significance |
| Regression and effect interpretation | Link functions, confounders, interactions, missingness | BS-03, BS-04, BS-06 | Interpret coefficients on correct scale; state design limitations |
| Trial methods and estimands | Outcomes, eligibility, intercurrent events, randomization | BS-05, BS-08, BS-09 | Identify estimand and distinguish ITT-style objectives from complete-case analysis |
| Survey methods | Sampling frame, clustering and weighting | BS-10, BS-11 | Avoid unweighted population claims from complex survey data |
| Research reporting and synthesis | Provenance, sensitivity analyses, limitations | BS-04, BS-05, BS-06, BS-12 | Reproducible method description and defensible interpretation |

## Explicit blockers and review record

| Gate | Status | Missing evidence / next action |
| --- | --- | --- |
| P0 scope | NOT_VERIFIED for HSE 712 alignment | Current authorized public course description and rights assessment |
| P1 provisional competencies | DRAFT | Independent reviewer confirms level, prerequisite order and scientific vocabulary |
| P2 reference inventory | DRAFT | Check live destinations, effective versions, and authoritative scope |
| P3–P6 teaching and technical validation | NOT_STARTED | Original authoring, executable validation and scientific review require a separate, appropriately guarded workflow |
| P7 rights/provenance | NOT_STARTED for any teaching material | Local private-source comparison and guard where changes are source-dependent |
| P8 release | NOT_STARTED for course companion | Review all applicable CI, provenance and navigation checks before publication |

**Maintenance:** Review these sources before each term; preserve links and note revisions. A successful originality check, link test or software test does not confer copyright clearance, scientific validity or official course alignment.
