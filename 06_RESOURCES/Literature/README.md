# Coding practices and methods — public literature matrix

[Resource index](../README.md) · [R reference](../R/README.md) · [Bash review](../Bash/BASH_LITERATURE_REVIEW.md) · [Repository home](../../README.md)

This curated matrix connects openly available programming documentation, research-software guidance, and reproducibility resources to independently authored health-data science exercises. It is a **narrative teaching bibliography**, not a systematic literature review or validation of a clinical model. All descriptions below are original summaries of general public guidance. Consult the linked primary sources for exact syntax and version-specific behavior.

## Biomedical research computing

For survey methodology, Bioconductor, count-based RNA-seq methods, and observational-research reporting, use the [biomedical research computing matrix](BIOMEDICAL_CODING_METHODS.md). For naming conventions, scientific data dictionaries, longitudinal identifier rules, research-code testing, and future-course quality gates, use the [biomedical coding standards framework](BIOMEDICAL_CODING_STANDARDS.md). These documents are original public-reference syntheses. For an actionable evidence-to-code review and quality-gate matrix covering NIH, FDA, CDISC, R testing and reproducibility, see the [research code quality matrix](RESEARCH_CODE_QUALITY_MATRIX.md). To plan a new course or research project, consult the [project intake, schema and reproducibility contracts](RESEARCH_PROJECT_INTAKE.md).

For laboratory-unit semantics, clinical terminology, FHIR/OMOP mapping, gene identifiers and reproducible research packaging, consult the [biomedical interoperability and metadata standards matrix](INTEROPERABILITY_METADATA_STANDARDS.md).

## Program-wide companion roadmap

The [gated program study-companion roadmap](PROGRAM_COMPANION_ROADMAP.md) indexes existing teaching resources, preliminary future-domain tracks, prerequisite dependencies, publication gates and acceptance evidence. It does not reproduce any protected syllabus or claim an official course sequence.

## Provisional biostatistics reference inventory

The [biostatistics P0–P2 evidence matrix](BIOSTATISTICS_REFERENCE_MATRIX.md) inventories independent public statistical references, candidate prerequisites and scientific limitations for future work. It is **not** a course teaching guide or a verified HSE 712 syllabus alignment; later source-dependent instructional changes require the separate local publishing guard.

## Evidence and usage key

- **Specification/manual:** authoritative source for documented behavior, but not necessarily a recommendation for every project.
- **Engineering guide:** recommended style or workflow; context-specific, not a language requirement.
- **Peer-reviewed methods:** scholarly guidance; implementation still requires independent validation.
- **Community teaching resource:** beginner-oriented explanation, not a substitute for primary documentation.

## Curated coding best-practices matrix

| ID | Source | Evidence type | Actionable practice | Relevant lessons | Scope / caution |
| --- | --- | --- | --- | --- | --- |
| CP-01 | [R Language Definition](https://cran.r-project.org/doc/manuals/r-release/R-lang.html) | Primary manual | Check vector types, indexing, evaluation, and missing-value behavior before interpreting results | 1–3 | Documents language semantics, not scientific validity |
| CP-02 | [R Data Import/Export manual](https://cran.r-project.org/doc/manuals/r-release/R-data.html) | Primary manual | Specify data layout and encoding, inspect types, and verify imported row counts | 1–3 | Check version and file-specific parsing behavior |
| CP-03 | [Advanced R](https://adv-r.hadley.nz/) | Technical textbook | Prefer small functions, explicit arguments, and deliberate object/condition handling | 1–3 | Explanations may assume prior R knowledge |
| CP-04 | [tidyverse Style Guide](https://style.tidyverse.org/) | Engineering guide | Use consistent object names, whitespace, function layout, and readable pipelines | 1–3 | Style conventions are recommendations, not R requirements |
| CP-05 | [dplyr Mutating Joins](https://dplyr.tidyverse.org/reference/mutate-joins.html) | Package reference | Define key relationships, audit unmatched rows and duplicates, make many-to-many behavior explicit | 3 | Joins may multiply observations; never infer valid linkage from a successful call |
| CP-06 | [tidyr pivot_longer](https://tidyr.tidyverse.org/reference/pivot_longer.html) / [pivot_wider](https://tidyr.tidyverse.org/reference/pivot_wider.html) | Package reference | Define observation keys and check wide/long transformation round trips | 2–3 | Nonunique keys can create list columns or duplicate mappings |
| CP-07 | [ggplot2 reference](https://ggplot2.tidyverse.org/reference/) | Package reference | Map variables to aesthetics deliberately; label axes, units, scales, and groups | 2–3 | Plot appearance alone cannot establish inference or causality |
| CP-08 | [testthat](https://testthat.r-lib.org/) | Testing framework | Test functions on expected cases, missingness, invalid inputs, and edge cases | 1–3 | Passing tests covers chosen contracts, not all inputs |
| CP-09 | [renv project environments](https://rstudio.github.io/renv/) | Dependency-management tool | Record package dependencies and use a project lockfile where appropriate | 2–4 | Locked packages do not by themselves freeze the OS or external datasets |
| CP-10 | [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | Primary manual | Explain quoting, expansion, conditionals, redirection, and exit status | 4 | macOS system Bash is often older than current GNU Bash |
| CP-11 | [GNU awk Manual](https://www.gnu.org/software/gawk/manual/) | Primary utility manual | Validate record/field separators before simple scientific metadata filtering | 4 | Plain `-F,` does not correctly parse quoted RFC-style CSV |
| CP-12 | [ShellCheck](https://www.shellcheck.net/) | Static analysis project | Review shell scripts for unsafe expansions and common mistakes | 4 | Static linting is not runtime verification |
| CP-13 | [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) | Engineering guide | Quote variables, use clear functions, document errors, and prefer small scripts | 4 | Organization-specific guidance; not universal POSIX law |
| CP-14 | [Software Carpentry — The Unix Shell](https://swcarpentry.github.io/shell-novice/) | Community teaching resource | Introduce command pipelines through small observable file transformations | 4 | Write independent exercises rather than copying curriculum examples |
| CP-15 | [The Turing Way — Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research/) | Community research handbook | Preserve provenance, document environments, track analysis steps and verification | 1–4 | Reproducibility is distinct from clinical or causal correctness |
| CP-16 | [The Turing Way — Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv/) | Community research handbook | Record software versions and define how to reconstruct computational environments | 1–4 | Environment capture does not establish access rights to input data |
| CP-17 | [Git documentation](https://git-scm.com/doc) | Primary manual | Separate source changes into reviewable commits; record changes and rollback paths | 1–4 | Never commit private reference files, credentials or patient data |
| CP-18 | [FAIR Guiding Principles (Wilkinson et al., 2016)](https://doi.org/10.1038/sdata.2016.18) | Peer-reviewed principles | Improve data identifiers, metadata and machine-readable provenance | 2–3 | FAIR does not require making confidential individual-level data public |
| CP-19 | [Ten Simple Rules for Reproducible Computational Research (Sandve et al., 2013)](https://doi.org/10.1371/journal.pcbi.1003285) | Peer-reviewed guidance | Track intermediate decisions, settings, outputs and analysis provenance | 1–4 | Rules guide practice; they do not certify a result reproducible |
| CP-20 | [Software Carpentry — Programming with R](https://swcarpentry.github.io/r-novice-inflammation/) | Community teaching resource | Reinforce variables, functions, loops, input checks and plotting in scientific contexts | 1–3 | Use original biological examples and exercises |

## Suggested learning path

| Starting need | Read first | Practice in an original health-data exercise |
| --- | --- | --- |
| R objects and inspection | CP-01, CP-02, CP-03 | Check types, dimensions, missingness, and units before a summary |
| Clean and reviewable R code | CP-04, CP-08 | Wrap a small summary function and test valid/invalid inputs |
| Repeated clinical measurements | CP-06, CP-07 | Reshape synthetic participant visits and verify observation keys |
| Merged epidemiology records | CP-05, CP-18 | Validate subject identifiers and report unmatched rows |
| Shell processing | CP-10, CP-11, CP-12 | Filter a synthetic TSV and verify retained record counts |
| Research pipeline handoff | CP-09, CP-15, CP-16, CP-17, CP-19 | Record R/package versions, scripts, and input provenance |

## Minimum review checklist for public examples

1. **Input contract:** identify the observation unit, schema, key columns, units and permissible missingness.
2. **Data transformation:** check row counts and unique keys before and after reshaping or joining.
3. **Result contract:** validate outputs and record exclusions, error conditions and software versions.
4. **Interpretation:** distinguish descriptive patterns, uncertainty, associations and causal/clinical claims.
5. **Publication:** use synthetic or appropriately licensed source data and follow the separate classroom-source publication guard where applicable.

## Maintenance and limitations

This matrix is intended as a navigational learning resource. Source links and package interfaces can change; check upstream release notes before adopting examples in production. The citations establish sources for general coding and research practices only. They are not evidence that any particular biomedical analysis, dataset, course objective or public lesson has been scientifically validated. No protected classroom source material or private comparison reports are included.

Project-specific research literature matrices and protected teaching-source comparisons remain private.
