# Research project intake — scaffold and evidence contracts

[Code quality matrix](RESEARCH_CODE_QUALITY_MATRIX.md) · [Biomedical coding standards](BIOMEDICAL_CODING_STANDARDS.md) · [Biomedical methods](BIOMEDICAL_CODING_METHODS.md) · [Literature index](README.md)

**Reference edition:** October 10, 2026. This is an independently authored **planning reference**, not executable teaching code, an assessed assignment template, or a university policy. Select the rules appropriate to the actual project; retain original external data schemas and use the guarded publication workflow when source-dependent lessons or code are changed.

## 1. Design the scientific contract before building a repository

| Decision | Record in project documentation | Failure prevented |
| --- | --- | --- |
| Research question | Population, unit of analysis, exposure/predictors, outcome, time horizon and scientific aim | Changing the question after viewing results |
| Data access | Source, permission, sensitivity classification, expected format and public-release status | Uploading restricted records or assuming redistribution rights |
| Primary unit | Person, encounter, visit, biospecimen, measurement or feature | Invalid joins and pseudoreplication |
| Key scheme | Native source IDs and explicitly mapped internal aliases | Silent row-based identity or ambiguous composite keys |
| Observation window | Event date/timestamp, time zone, baseline, follow-up and censoring conventions | Time leakage and incorrect longitudinal comparisons |
| Measurement | Units, admissible codes, missing-value reasons, reference levels, transformed scales | Mixing counts, concentrations, ratios or transformed features |
| Analysis objective | Estimand or prediction target, sampling strategy, model assumptions, uncertainty measure | Unsupported clinical or population inference |
| Validation | Independent fixtures, expected failures, invariants, domain review | Treating a successful script as scientific evidence |
| Reporting | Figures/tables, n and denominators, exclusions, confidence intervals where applicable | Uninterpretable results |
| Reproduction | Runtime/package versions, seeds, deterministic settings, data manifest, run command | Analysis cannot be reconstructed |

## 2. Suggested project layout and file responsibilities

This is a **reference layout**, not a directive to rename an existing project.

| Logical area | Contents | Policy |
| --- | --- | --- |
| `README.md` | Aim, prerequisites, authorized setup, safe reproduction steps | No personal identifiers or private credentials |
| `docs/` | Methods, schema/dictionary, decisions, interpretation limits, review notes | Keep restricted comparison material in private storage |
| `config/` | Nonsecret analysis settings, versioned parameter sets | No API tokens or private access keys |
| `data/raw/` | Source-original datasets when legally held locally | Typically excluded from public Git; immutable inputs |
| `data/derived/` | Normalized, validated intermediate data | Never assume derivatives are automatically redistributable |
| `src/` or `R/` | Functions with explicit contracts and limited side effects | Consistent names; no reading mutable globals without documentation |
| `scripts/` | Ordered workflow entry points, import/validate/model/report | Fail with informative messages on invalid inputs |
| `tests/` | Synthetic fixtures and checks for valid and invalid cases | No PHI or classroom restricted samples in public CI |
| `reports/` | Figures, tables and machine-readable summaries | Distinguish derived artifacts from source observations |
| `manifest/` | Input versions, checksums, output provenance and release disposition | Avoid publishing private filenames or sensitive inventories |

## 3. Naming and internal conventions

| Concept | Preferred internal pattern | Important exception |
| --- | --- | --- |
| An analysis table | `participant_visits_clean`, `assay_metadata_validated` | Preserve native provider field names in source layer |
| Identifiers | `participant_id`, `visit_id`, `specimen_id` | Do not expose directly identifying native IDs in public outputs |
| Dates and instants | `visit_date`, `collected_at` | Document time zone, date granularity and event semantics |
| Counts and denominators | `n_participants`, `n_specimens` | Clearly distinguish subject counts from measurement counts |
| Concentrations | `albumin_mg_l`, with dictionary definition | Follow standardized terminology and versioned source units |
| Statistical estimates | `mean_difference`, `log2_fold_change` | Name the contrast, scale and adjustment explicitly |
| Flags | `has_follow_up`, `is_missing` | Missing/unknown must not become false by default |
| Functions | `validate_keys()`, `build_design_matrix()` | Names should promise one measurable action |
| File stages | `01_ingest_*`, `02_validate_*`, `03_analyze_*` | Stage numbers optional; no renaming externally referenced interfaces |

Follow [tidyverse style](https://style.tidyverse.org/) for locally authored R, but accept a different style when project or interoperability requirements justify it. Follow the external schema definition for [OMOP CDM](https://ohdsi.github.io/CommonDataModel/) and documented [Bioconductor assay structures](https://bioconductor.org/packages/release/bioc/html/SummarizedExperiment.html).

## 4. Required machine-readable contracts

### Dataset contract

| Field | Description |
| --- | --- |
| `dataset_id` | Stable internal dataset identifier |
| `source_uri` and `source_version` | Original reference and edition/cycle, without restricted access tokens |
| `permission_class` | Public, permitted-restricted, synthetic or prohibited-for-release |
| `observation_unit` | Person, visit, event, specimen, gene or another explicit entity |
| `primary_keys` | Defined unique keys, possibly composite |
| `columns` | Source name, internal name, type, unit, allowed values and missingness |
| `row_count_expectation` | Grounded range or fixed count where applicable |
| `joins_allowed` | Approved relationships and cardinalities |
| `release_disposition` | Whether metadata, code, aggregate output or data may be shared |

### Analysis contract

| Field | Description |
| --- | --- |
| `analysis_id` | Stable name for the scientific question or analysis |
| `population` | Eligibility, exclusions, denominator and time window |
| `outcome` / `predictors` | Variable IDs linked to the dictionary |
| `method` | Descriptive, complex survey, linear model, count model, prediction, etc. |
| `design` | Strata/PSU/weights, repeated-measure structure or assay contrasts, as relevant |
| `scale` | Original, ratio, count, CPM, natural log, log2 or other explicit scale |
| `uncertainty` | Standard error, confidence interval, multiplicity approach or justified omission |
| `software_environment` | R/OS/package versions and lockfile/manifest |
| `validation_status` | Evidence-supported state; never silently default to pass |

## 5. Stage gates and concrete failure scenarios

| Stage | Valid evidence | Intentionally invalid case to catch |
| --- | --- | --- |
| Intake | File/version manifest, documented parser and schema checks | Wrong cycle or missing essential header |
| Cleaning | Original-to-internal field map; coded missingness preserved | `not measured` converted into zero |
| Linkage | One-to-one or one-to-many key validation with unmatched counts | Duplicate demographics record multiplies visits |
| Derived measures | Units and formula documented, sensible domain bounds | mg/dL silently combined with mg/L |
| Statistical design | Frozen population, model specification and dependencies | Participant visits treated as independent participants |
| Computation | Numerical checks and justified tolerance | NaN/Inf or reversed contrast passes unnoticed |
| Reporting | Labels, units, denominators, uncertainty and caveats | Plot reports visits as unique patients |
| Release | Data and rights review, provenance, source-guard compliance | Synthetic fixture replaced by restricted records |

## 6. Research-specific adoption profiles

| Next project domain | Essential add-ons | Good starting references |
| --- | --- | --- |
| Biostatistics | Estimands, assumptions, design matrix, inference, missingness, multiplicity | [R survey package](https://cran.r-project.org/package=survey), [STROBE](https://www.strobe-statement.org/) |
| Public-health survey | Sampling frame, interview/examination weights, strata, PSU, component eligibility | [CDC NHANES weighting](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx) |
| Longitudinal clinical data | Patient-event cardinality, timestamps, coding systems, incident outcomes | [OMOP CDM](https://ohdsi.github.io/CommonDataModel/), [RECORD](https://www.equator-network.org/reporting-guidelines/record/) |
| Sequencing assays | Feature-by-sample orientation, library sizes, count models, normalization, contrasts | [SummarizedExperiment](https://bioconductor.org/packages/release/bioc/html/SummarizedExperiment.html), [edgeR](https://bioconductor.org/packages/release/bioc/html/edgeR.html) |
| Clinical prediction and AI | Leakage controls, split strategy, calibration, performance by group, intended use | [TRIPOD](https://www.equator-network.org/reporting-guidelines/tripod-statement/), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| Manuscript/reporting | Research question, design transparency, traceability, limitations and reference management | [The Turing Way](https://book.the-turing-way.org/reproducible-research/reproducible-research/), [FAIR principles](https://doi.org/10.1038/sdata.2016.18) |

## 7. Project review record

A future project should identify the reviewer, date, actual input version, acceptance evidence, limitations and status for each gate. Use `NOT_ASSESSED`, `BLOCKED`, `FAIL`, `PASS` or `NOT_APPLICABLE` with a reason. Require scientific review for substantive inference and human authorization for protected-source release.

No blanket instruction to apply these profiles can replace an actual syllabus, data use agreement, required analytic method or course-specific policy. This page itself contains only independent public-reference guidance.
