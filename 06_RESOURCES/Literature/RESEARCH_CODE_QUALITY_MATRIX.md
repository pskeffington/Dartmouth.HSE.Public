# Research code quality — evidence-to-implementation matrix

[Biomedical coding conventions](BIOMEDICAL_CODING_STANDARDS.md) · [Biomedical methods](BIOMEDICAL_CODING_METHODS.md) · [General reference matrix](README.md) · [Resource index](../README.md)

**Reviewed:** 2026-10-10. This is an independently written, selective synthesis of publicly available research-computing standards and technical guidance. The quality gates below are recommended for student projects and future courses; they do not confer clinical, regulatory, or institutional compliance. No private course source files or protected comparisons inform this document.

## Source quality and decision policy

Prefer versioned primary manuals or domain-specific specifications for exact machine behavior, official method guidance for a defined study design, and peer-reviewed research guidance for broad reproducibility principles. A style guide is not a language specification. An organizational reporting or submission rule only applies within its stated scope. Before adopting a source, record its version, audience, and fit to the actual dataset and intended use.

## Evidence-to-practice matrix

| ID | Public source | Evidence class | Practice to adopt | Observable acceptance | Caution |
| --- | --- | --- | --- | --- | --- |
| QA-01 | [NIH Data Management](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/data-management) | Federal research guidance | Inventory data sources, types, permitted use, transformations, storage and future access | Written manifest and input/output provenance | Data availability does not imply redistributable person-level records |
| QA-02 | [NIH DMS Plan guidance](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/writing-dms-plan) | Federal policy implementation | Describe data management, appropriate access and preservation before release | Plan names data categories, constraints, preservation and sharing strategy | Apply the current plan format only when the project is in policy scope |
| QA-03 | [NIH Notice NOT-OD-26-046](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html) | Dated NIH policy notice | Use currently effective requirements rather than copied older DMS templates | Document the effective notice/date used for an applicable grant | The new format has a defined applicability date; not a universal student-project requirement |
| QA-04 | [NCBI GEO high-throughput submissions](https://www.ncbi.nlm.nih.gov/geo/info/seq.html) | Federal repository instructions | Retain biological sample, protocol and processed-data metadata; use safe, uniquely identified filenames | Unique sample and file inventory, protocol descriptions, identity checks | Requirements apply to GEO sequencing submissions, not every dataset |
| QA-05 | [FDA Study Data Technical Conformance Guide (June 2026)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/study-data-technical-conformance-guide-technical-specifications-document) | Regulatory technical guidance | Preserve analysis-data traceability, datasets, controlled terms and reviewer documentation | Trace a reported result to its originating dataset, derivation and analysis | Nonbinding guidance focused on covered submissions; do not imply all student work must use CDISC |
| QA-06 | [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm) | Domain exchange standard | Keep source observations distinct from standardized clinical trial tabulations | Explicit source-to-target mapping and schema version when SDTM applies | Never impose SDTM on unrelated public-health exploratory datasets |
| QA-07 | [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam) | Analysis data standard | Document derivations and traceability from source to analysis datasets | Dataset spec distinguishes analysis variables and derivations | Applies to compatible clinical study analysis workflows |
| QA-08 | [R packages manual](https://cran.r-project.org/doc/manuals/r-release/R-exts.html) | Primary development manual | Document functions, input contracts and dependencies in reusable R software | Rebuild or check the package in an isolated supported session | Package-check success is not statistical truth |
| QA-09 | [testthat reference](https://testthat.r-lib.org/) | Testing framework | Test valid, missing, duplicate, and invalid-input cases; state what is asserted | A failure fixture rejects an invalid join or wrong unit | Assertions reproduce specified contracts only |
| QA-10 | [renv](https://rstudio.github.io/renv/) | Dependency-management documentation | Snapshot package versions and document restoration | Clean environment can restore declared package dependencies | Lockfiles do not freeze external APIs, OS or source data |
| QA-11 | [Bioconductor developer contributions](https://contributions.bioconductor.org/) | Research-software engineering guidance | Define assay/sample structures and maintain code/documentation quality | Sample IDs align with assay columns and metadata rows | Package-submission guidance is not automatically required for a course script |
| QA-12 | [FAIR principles (Wilkinson et al., 2016)](https://doi.org/10.1038/sdata.2016.18) | Peer-reviewed data stewardship | Give datasets stable identifiers, useful dictionaries and provenance | Analysis can identify variable origin, units and version | FAIR does not override participant privacy or licensing |
| QA-13 | [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285) | Peer-reviewed methodological guidance | Preserve input versions, parameters, code and intermediate decisions | Independent rerun with documented inputs yields comparable outputs | Reproducibility is distinct from causal validity |
| QA-14 | [STROBE Statement](https://www.strobe-statement.org/) | Observational reporting framework | Document design, eligibility, exclusion, missingness, assumptions and limitations | Transparent methods and analysis population summary | Reporting checklist completion does not validate inference |
| QA-15 | [RECORD guideline](https://www.equator-network.org/reporting-guidelines/record/) | Routinely collected health-data reporting guideline | Explain variable coding, linkage and source-data provenance | Data lineage and linkage logic disclosed when permissible | Access restrictions and privacy remain independent gates |
| QA-16 | [FDA Good Machine Learning Practice principles](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/good-machine-learning-practice-medical-device-development-guiding-principles) | Medical-device AI guidance | Define intended use, representative evaluation and postdeployment considerations | Intended-use statement, leakage checks, evaluation plan | Medical-device context; not blanket approval of student ML |

## Recommended gate acceptance for new biomedical coding work

| Gate | Question and review action | Minimum deliverable | Fails if |
| --- | --- | --- | --- |
| Q0 Authority/rights | Which source, license, protocol and submission rules actually apply? | Scope note and permission classification | Restricted inputs are exposed or assumed freely shareable |
| Q1 Source intake | Were expected files, headers and versions received intact? | Input manifest with schema and file-version evidence | File missing, schema mismatch or unsupported format |
| Q2 Naming/data dictionary | Can every analytical field be interpreted and mapped back? | Source-to-analysis mapping with types, units, controlled values and missing codes | Ambiguous names or lossy unreviewed renaming |
| Q3 Identity and joins | Do keys and relationship multiplicities match study design? | Join audit: before/after, duplicate, unmatched and exclusion counts | Unexplained row multiplication, missing IDs or false unique claims |
| Q4 Measurement validity | Are denominators, units, transforms, time windows and censoring defined? | Validation summary with explicit out-of-range and missingness rules | Silent zero-fill, wrong unit conversion or mixed count/log scales |
| Q5 Statistical design | Is an estimand, analysis population and design specified? | Frozen design/model summary and diagnostic plan | Design assumptions unspecified or survey/longitudinal dependence ignored |
| Q6 Numerical confidence | Do checks challenge mistakes instead of merely repeating results? | Synthetic expected-case and deliberate invalid-case tests | Tests only confirm that a function returned something |
| Q7 Reproduction | Can another authorized analyst reconstruct the workflow? | Dependencies, execution order, seed where relevant, source/version manifest | Missing dependencies or nonreconstructible input lineage |
| Q8 Communication | Can a reader distinguish observed data from inference? | Labeled plots/tables with units, n, exclusions and limitations | Unlabeled figures or causal/clinical overclaims |
| Q9 Release | Is the intended artifact appropriate to distribute? | Privacy, rights, provenance and source-guard disposition | Protected content, identifiers or unpublished restricted data included |

**Gate status vocabulary:** `PASS` (evidenced), `FAIL` (contradicted), `BLOCKED` (dependency unavailable), `NOT_APPLICABLE` (scoped out with reason), and `NOT_ASSESSED` (not yet reviewed). A completed software build is not a substitute for Q2–Q9 evidence.

## Naming and review patterns

Use lower-case `snake_case` for new internal R functions and normalized analysis fields unless a documented public schema requires another form. Prefer names that indicate the entity, state and units (for example, `participant_id`, `sample_collected_at`, `creatinine_mg_dl`, `n_participants`, `model_design`). Keep native source fields untouched in the intake layer. Every alias needs a mapping record and a check that no fields are silently lost.

For biomedical measurements, the quantity, sampling context and units matter more than superficial style. Never silently equate `participant_id` with an encounter or specimen identifier, or a model output in natural-log units with `log2_fold_change`.

## Expandable future-course evidence record

Use this lightweight schema when evaluating a newly introduced technique:

| Field | Required explanation |
| --- | --- |
| `domain` | Biostatistics, epidemiology, genomics, clinical informatics, AI or research computing |
| `source_reference` | Stable public manual/guideline URL plus version or date |
| `method_contract` | Valid input type, observation unit, important assumptions |
| `recommended_convention` | Proposed name, metadata and workflow practice |
| `testable_acceptance` | An observable check, including at least one invalid case |
| `limits` | Cases where the method or source should not be applied |
| `review_status` | One of the five gate states with evidence reference |
| `next_review` | Review trigger: new course, software version or source update |

The objective is to preserve a portable quality system while making course-specific addenda only when justified. A later course's academic objectives, assessed exercise structure or protected slides must not be copied into this public reference document.

## Scope and provenance

This document is a public-reference synthesis, not a clinical SOP. Citation links point to publishers' own documentation; the summaries and checklists are independently authored. Require human scientific judgment for any high-stakes research interpretation. When appropriate, follow the repository's private-source publication requirements for subsequent lesson or teaching-source changes.
