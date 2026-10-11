# Scholarly source verification register — initial reviewed batch

[Scholarly validation protocol](SCHOLARLY_VALIDATION_PROTOCOL.md) · [Week 5 machine-learning review](WEEK_5_MACHINE_LEARNING_LITERATURE_REVIEW.md) · [Gene companion](../Genomics/BREAST_CANCER_60_GENE_COMPANION.md)

**Review date:** 2026-10-10 (America/New_York). **Scope:** Three publication-level checks against publicly accessible publisher and PubMed/PMC records. **Important:** These checks do not establish repository-wide or full-text methods verification, retraction-free status at future dates, or independent numerical replication.

| Evidence ID | DOI | Primary source | Publication facts checked | Narrow claim checked | Status | Remaining work |
| --- | --- | --- | --- | --- | --- | --- |
| SOURCE-001 | [10.1136/bmj-2023-078378](https://doi.org/10.1136/bmj-2023-078378) | Collins et al., *BMJ* (2024), TRIPOD+AI statement | Publisher title, DOI, year and reporting-guideline context | TRIPOD+AI is an updated reporting guideline for clinical prediction modeling using regression or machine learning and includes a 27-item checklist | PUBLISHER_RECORD_CHECKED | Map individual lesson recommendations to checklist items; appraise explanation and elaboration |
| SOURCE-002 | [10.1136/bmj-2024-082505](https://doi.org/10.1136/bmj-2024-082505) | Moons et al., *BMJ* (2025), PROBAST+AI | Publisher title, DOI and year; PubMed bibliographic record | The tool separates development quality/applicability assessment from evaluation risk-of-bias/applicability assessment | PUBLISHER_AND_PUBMED_CHECKED | Review signaling questions against specific worked examples |
| SOURCE-003 | [10.1056/NEJMoa2005936](https://doi.org/10.1056/NEJMoa2005936) | Hu et al., *New England Journal of Medicine* (2021), population-based breast cancer study | Publisher title, DOI, year; accessible PMC manuscript | Case-control sample 32,247 cases and 32,544 controls; pathogenic germline ATM variants were associated with increased breast cancer risk, including ER-positive disease | PUBLISHER_AND_PMC_RECORD_CHECKED | Independently verify study tables, model specification, stratified estimates and confounding/bias; do not apply variant risk results to RNA expression |

## Release interpretation

- **PUBLISHER_RECORD_CHECKED** confirms identification and narrow claims visible in the publisher's accessible record, not full review or independent replication.
- **PUBLISHER_AND_PUBMED_CHECKED** adds corroboration of a PubMed record; it is not evidence of independent scientific validation.
- **PUBLISHER_AND_PMC_RECORD_CHECKED** confirms that a manuscript is publicly accessible; it does not imply methods or supplements were systematically appraised.
- Existing gene-card `ABSTRACT_ONLY` labeling remains unchanged. Do not automatically upgrade individual cards based on this bibliography review.

## Priority queue

1. Resolve DOI/PMID metadata for all distinct referenced research publications; separate example identifiers, software URLs and publisher-domain links from scholarly citations.
2. For each gene card, trace the cited primary article to a specific outcome and population, and record the assay, effect size and limitations.
3. Evaluate software guidance against its exact version and cited documentation.
4. Record corrections with claim identifiers, source locations and reviewer decisions; do not silently rewrite substantive research findings.

Protected lectures, institutional assignment contents, private data and private similarity reports must remain excluded from public records.
