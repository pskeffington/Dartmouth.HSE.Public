# Biomedical computing conventions — extensible coding standard

[Biomedical literature matrix](BIOMEDICAL_CODING_METHODS.md) · [General coding references](README.md) · [Resources](../README.md)

**Scope:** independently authored, public-reference guidance for research computing, biostatistics, biomedical data engineering and future course projects. This is a **recommended project convention**, not a universal standard, clinical software qualification, institutional policy, or claim of copyright clearance. Adapt to a published schema (e.g., OMOP), course requirements or existing interoperable data contracts rather than silently renaming external interfaces.

## A. Decision hierarchy

1. **Respect the data source contract.** Preserve original field names, labels, codes, units and identifiers in a raw or source-schema layer.
2. **Use documented standards where applicable.** For OMOP-based projects, follow the selected CDM release; for Bioconductor, preserve assay dimensions and identifier semantics; for NHANES, obey the cycle-specific documentation and sampling design.
3. **Define a normalized internal analysis schema.** Prefer readable, unambiguous snake_case names for newly authored R objects, functions and internal table columns. Maintain a tested source-to-analysis mapping.
4. **Require scientific meaning.** One field = one documented concept with a unit, temporal meaning, missing-value rule and provenance.
5. **Make tests evidence-based.** A successful script exit is insufficient without schema, counts, join, unit, model and output checks.
6. **Version decisions.** A changed transformation, exclusion or model definition must be recorded and reviewed.

## B. Naming conventions

| Object | Recommended style | Illustrative name | Required semantic check |
| --- | --- | --- | --- |
| Internal analysis variable | `snake_case`, descriptive noun | `urine_albumin_mg_l` | Unit must be explicit in dictionary; unit suffix when stable and useful |
| Identifier | `<entity>_id` | `participant_id`, `specimen_id` | Do not use row index as identity or expose direct personal identifiers |
| Timestamp/date | `*_at` for timestamp, `*_date` for date | `collected_at`, `visit_date` | Timezone and sampling/recording event defined |
| Boolean | `is_*`, `has_*`, `*_flag` | `has_measurement`, `is_missing` | Distinguish TRUE/FALSE/unknown |
| Factor/category | descriptive noun | `sample_type`, `visit_group` | Enumerate allowed levels and reference category |
| Count | `n_*` or `*_count` | `n_participants`, `read_count` | Specify denominator and whether zero is observed vs missing |
| Rate/ratio | `*_rate`, `*_ratio` | `response_rate`, `albumin_creatinine_ratio` | Record numerator, denominator and units; don't invent clinical thresholds |
| R function | verb + object in `snake_case` | `validate_join_keys()`, `summarize_measurements()` | Return type, side effects and error behavior documented |
| R data frame | domain + stage suffix | `participants_raw`, `measurements_clean` | Raw, normalized, analysis-ready stages distinct |
| Statistical estimate | estimand + scale | `log2_fold_change`, `risk_ratio` | Distinguish natural log, log2, odds/risk, raw/adjusted |
| R script | lower-case descriptive file name | `02_validate_metadata.R` | Order only when pipeline stage order matters |
| Bash script | lower-case `kebab-case` or `snake_case` consistently | `validate-inputs.sh` | Include interpreter, quoted arguments and exit checks |
| Configuration | explicit machine-readable format | `analysis-config.yaml` | Validate schema; never commit secrets |
| Artifact | stage + subject + version/date if useful | `03_join_audit.csv` | Immutable provenance, controlled output directory |

**Examples are conventions, not automatic rename instructions.** Existing externally specified fields such as `SEQN`, `person_id`, `measurement_concept_id`, official accession IDs, sample barcodes and exported interface keys must be preserved unless a lossless, documented mapping is created. Do not conflate `sex`, sex assigned at birth, and gender identity; retain the source variable's stated meaning.

## C. Biomedical data dictionary contract

For each analysis field, record:

| Field | Purpose |
| --- | --- |
| `analysis_name` | Internal field name |
| `source_name` and `source_system` | Exact origin and cycle/version |
| `definition` | Plain-language concept, not a guess from the name |
| `data_type` and `allowed_values` | Type and code/level constraints |
| `unit` and `measurement_scale` | Unit, count/CPM/log scale, temporal meaning |
| `observation_unit` | Participant, specimen, encounter, gene, visit or event |
| `key_relationship` | Primary/foreign key or repeated-observation structure |
| `missing_codes` | Explicit unknown/refused/not measured/not applicable distinctions |
| `transformation` | Source-to-analysis rule and parameter references |
| `provenance` | Original file/version, extraction time and permission status |
| `quality_check` | Non-null, domain, uniqueness, range or compatibility contract |

A data dictionary should distinguish a column's *measurement units* from its *statistical interpretation* and should not invent clinical reference ranges.

## D. Identifier and join integrity

- Inspect key uniqueness **before** merging. A participant-to-measurement join is usually one-to-many, while participant-to-demographics should be one-to-one for a defined period.
- Report `n_before`, `n_after`, duplicate keys, unmatched records and exclusions.
- Never make row position the identifier after sorting, filtering or importing data.
- Repeated participant visits require an explicit composite key such as `(participant_id, visit_id)`.
- Keep clinical events distinct from participants and specimens; one participant may have many encounters, samples or laboratory measurements.
- Confirm source IDs and source concept codes are not silently substituted for standardized terminology identifiers.
- For longitudinal models, define baseline, outcome window, follow-up, censoring and timezone rules before transformations.

## E. Units, scales and missingness

- Define numerator/denominator for percentages and rates. Always specify whether an estimate is per participant, specimen, encounter or event.
- Use original physical units where available; document conversions and dimensional validation. An arbitrary code such as `0` is not necessarily a measured zero.
- Distinguish RNA sequencing raw counts, normalized counts, CPM, log-CPM and transformed values. Never route one into a method expecting another without documented validation.
- Do not convert `refused`, `unknown`, `not asked` or `below detection` into the same observed numerical zero.
- Validate category levels and ordering before visualization; label axes and clinical units explicitly.
- Distinguish missing-at-random assumptions, missingness descriptions and formal missing-data models.

## F. Layered research software quality gates

| Gate | Question | Evidence to retain |
| --- | --- | --- |
| G0 Source rights | May these inputs be used, analyzed and distributed? | License/permission classification; no public PHI |
| G1 Intake | Is the retrieved file the intended version and schema? | Source manifest, checksum, codebook/cycle, row and column counts |
| G2 Identity | Do records and metadata align? | Unique/composite key checks, join relationships, unmatched and duplicated IDs |
| G3 Semantics | Are type, units, codes, dates, labels and missingness correct? | Dictionary validation and transformations with auditable mapping |
| G4 Analysis | Are the design, population, exclusions and estimands coherent? | Frozen analytical dataset specification and model design |
| G5 Statistical validation | Are numerical results appropriate and reproducible? | Seed, environment lock, diagnostics, uncertainty and sensitivity results |
| G6 Presentation | Does output correctly communicate observations? | Units, n, denominator, model scale, assumptions and captions |
| G7 Publication | Are distribution rights, privacy, provenance and versioning acceptable? | Reviewed diff, source guard where applicable, regenerated outputs |

A **failed gate stays failed**; do not substitute a green CI status, a successful download or a plausible figure.

## G. Testing pyramid for scientific code

1. **Unit tests:** function behavior with correct, missing, out-of-range and wrong-type inputs.
2. **Property/invariant tests:** sorting rows doesn't alter a properly keyed join; wide-to-long roundtrip preserves the stated key; excluded records do not silently reappear.
3. **Schema/contract tests:** column names, source versions, allowed factor levels, timezones, and units match declared contracts.
4. **Numerical verification:** compare known synthetic results or independent implementations within justified tolerances; don't hardcode arbitrary tolerance bands without scaling.
5. **Integration tests:** source import → clean → join → model → report with synthetic fixtures and output assertions.
6. **Regression tests:** keep minimal fixtures for resolved defects and verify no unexpected change in scientific interpretation.
7. **Reproducibility tests:** clean-session or clean-environment run with recorded package versions, seeds and artifact hashes.
8. **Privacy/security checks:** synthetic fixtures in public CI; no real identifiers, credentials, sensitive metadata, or restricted source attachments.

Never assert a statistical effect is *true* merely because a test reproduces the same code result.

## H. Future-course profiles

| Course theme | Adopt this baseline | Additional discipline-specific requirements |
| --- | --- | --- |
| Introductory R/data science | Names, types, missingness, imports, descriptive graphics, tests | Base R semantics, tidyverse syntax when taught |
| Biostatistics | Data dictionary, analysis population, estimand, diagnostics | Sampling, confidence intervals, multiplicity, model assumptions |
| Epidemiology and public health | Participant/visit identifiers, survey and observational design | Survey weights, strata, PSU, confounding, eligibility, selection |
| Clinical informatics / longitudinal EHR | Event timestamps, person/visit/measurement relationships | OMOP schema version, concepts, unit mapping, encounter linkage |
| Genomics and bioinformatics | Feature/sample orientation, assay scale, experimental design | Bioconductor classes, normalization, count-model assumptions |
| AI/ML ethics and clinical AI | Reproducibility, privacy, subgroup reporting and provenance | Leakage checks, dataset shift, bias evaluation, intended-use limits, monitoring |
| Manuscript and research methods | Reproducible report, transparent exclusions and provenance | STROBE/RECORD/TRIPOD where appropriate, journal-specific reporting |

Course-specific requirements must be obtained from authorized sources before a profile is called course-complete. This document does not claim to represent any school's official rubric.

## I. Public evidence matrix: naming, data standards and quality

| ID | Reference | Category | Framework contribution | Limits |
| --- | --- | --- | --- | --- |
| STD-01 | [tidyverse Style Guide — Syntax](https://style.tidyverse.org/syntax.html) | Engineering style | Snake_case object names, readable functions, meaningful names | Opinionated style, not a formal R requirement |
| STD-02 | [tidyverse Style Guide — Files](https://style.tidyverse.org/files.html) | Engineering style | Machine-readable file naming, sortable dates/stages | Stage prefixes are a local adaptation |
| STD-03 | [R Language Definition](https://cran.r-project.org/doc/manuals/r-release/R-lang.html) | Primary manual | Type/indexing/NA semantics and evaluation | Does not validate a research design |
| STD-04 | [Bioconductor package guidelines](https://contributions.bioconductor.org/) | Developer guidance | Package architecture, documentation, reproducibility, checks | Applies especially to Bioconductor submissions |
| STD-05 | [BiocCheck package](https://bioconductor.org/packages/release/bioc/html/BiocCheck.html) | Tool | Bioconductor-style code/package assessment | Static checks are not scientific validation |
| STD-06 | [OMOP CDM data model conventions](https://ohdsi.github.io/CommonDataModel/dataModelConventions.html) | Interoperability standard | Distinguish IDs, concept IDs, source values and record types | Require version-specific mapping; do not collapse sex and gender concepts |
| STD-07 | [OMOP CDM 5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html) | Versioned schema | Person, visit, measurement, concepts and field rules | Other deployed CDM versions can differ |
| STD-08 | [CDC NHANES analytic guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx) | Survey methodology | Weight/strata/PSU selection and component-specific samples | Survey weighting depends on analysis and cycle |
| STD-09 | [FHIR R4 resource types](https://hl7.org/fhir/R4/resourcelist.html) | Interoperability specification | Separate observations, patients, encounters, codes, effective times | FHIR profile/version semantics vary; sensitive clinical records stay protected |
| STD-10 | [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) | Peer-reviewed methods | Rich metadata, identifiers and interoperable provenance | FAIR does not compel disclosure of confidential data |
| STD-11 | [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285) | Peer-reviewed methods | Record parameter, software, data and decision provenance | Reproduction is not external validity |
| STD-12 | [The Turing Way — Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research/) | Open methodology | Rerunnable pipelines, documentation and collaboration | Practices require local adaptation |
| STD-13 | [testthat](https://testthat.r-lib.org/) | Testing framework | Assert scientific-code function contracts | Does not prove model correctness |
| STD-14 | [renv](https://rstudio.github.io/renv/) | Dependency framework | Lock R packages and reconstruct project environments | OS and upstream data can still vary |
| STD-15 | [STROBE Statement](https://www.strobe-statement.org/) | Reporting guideline | Record selection, bias, variables and analysis decisions | Reporting quality is not causal validity |
| STD-16 | [RECORD reporting guideline](https://www.equator-network.org/reporting-guidelines/record/) | Reporting guideline | Transparent codes, linkage and routinely collected health data | Not a substitute for permission or privacy review |
| STD-17 | [TRIPOD reporting guideline](https://www.equator-network.org/reporting-guidelines/tripod-statement/) | Prediction reporting guideline | Document predictors, modeling, validation and performance | Select the applicable reporting extension/version |
| STD-18 | [FDA Good Machine Learning Practice](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/good-machine-learning-practice-medical-device-development-guiding-principles) | Regulatory guidance | Intended use, representative datasets, human-AI team, monitoring | Medical-device context; not blanket regulation of student code |
| STD-19 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary risk framework | Document AI risk, testing, monitoring, transparency and governance | Not a substitute for domain-specific clinical validation |
| STD-20 | [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | Primary manual | Quote variables, use explicit failures and safe file operations | Bash version/platform portability differs |

## J. Default pre-project template

When starting a new course, document:

- **Dataset and rights:** source, permission class, schema version, observation unit.
- **Problem:** objective, population, explanatory variables, outcomes and limits.
- **Data dictionary:** names, types, units, missing codes and key relationships.
- **Pipeline:** immutable raw layer → validated normalized layer → analysis-ready layer → report.
- **Analysis contract:** model specification, estimand, seed, software, diagnostics.
- **Verification:** synthetic-fixture checks, domain checks, integration checks and human scientific review.
- **Output:** labeled figures/tables, provenance, limitations and replication instructions.
- **Change record:** documented deviations from the framework and why they are appropriate.

**Change control:** this is a baseline to refine as courses progress; do not bulk-rename existing datasets, overwrite assessed course artifacts, or claim that adopting the convention retroactively validates research.

## Evidence/rights disclaimer

References are linked as public sources of general methods. The matrix is a selective narrative synthesis, not exhaustive research or a substitute for discipline-specific professional judgment. All examples and conventions here are independent; no protected classroom material is embedded.
