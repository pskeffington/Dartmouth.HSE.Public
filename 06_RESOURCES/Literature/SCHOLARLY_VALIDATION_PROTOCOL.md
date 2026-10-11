# Scholarly evidence verification protocol

[Repository home](../../README.md) · [Literature matrix](README.md) · [60-gene source register](../Genomics/REFERENCES/ANNOTATION_SOURCE_REGISTER.md)

## Evidence boundary

A citation inventory is **not** a scholarly fact check. A resolvable DOI does not demonstrate that a source supports the adjacent assertion. Annotation identity checks do not validate clinical associations. A reproducible script does not independently validate its research design.

## Review stages

| Gate | Evidence required | Acceptable status |
|---|---|---|
| S0 Inventory | All Markdown paths, DOI and PMID strings, review labels, structural gaps | INVENTORIED |
| S1 Bibliography | Resolve DOI via Crossref/DataCite or publisher, PMID via PubMed; compare title, authors, year, journal, errata/retractions and publication type | METADATA_VERIFIED |
| S2 Claim mapping | Locate exact claim, source, supporting section/table, design, population, endpoint, effect and limits | CLAIM_SUPPORTED / QUALIFY / UNSUPPORTED |
| S3 Methodology | Confirm assay, cohort, n, units, missingness, bias, statistics, multiplicity and independent data provenance | METHODS_REVIEWED |
| S4 Reproduction | Pin dependencies and inputs; execute independent fixture and match documented numerical tolerances | REPRODUCED |
| S5 Release | Peer/editorial review, protected-source guard, navigation and code CI all pass | RELEASED |

## Source hierarchy

Use authoritative identifiers (HGNC, NCBI Gene, Ensembl) for gene identity; original studies and systematic evidence for biological/clinical claims; methodological papers and reporting standards for analytical recommendations; version-specific primary manuals for software behavior. Do not conflate peer review with software documentation. Flag retractions, corrections and conflicting high-quality evidence.

## Reviewer record

Record publicly shareable fields only: `path`, `section_or_claim_id`, `claim_excerpt` (short, independently authored), `doi_or_pmid`, `source_type`, `verification_stage`, `supporting_location`, `population_and_assay`, `limitations`, `reviewer`, `reviewed_utc`, `decision`, `correction_pr`. Never publish protected lectures, private comparison traces, PHI or restricted datasets.

## Local check

```bash
python3 scripts/audit_scholarly_references.py --output scholarly-reference-inventory.json
python3 scripts/audit_scholarly_references.py --strict --output scholarly-reference-inventory.json
```

The first command inventories Markdown citations and review labels; the second blocks structurally incomplete gene-card bibliography records. Neither command calls external services or verifies the accuracy of scientific claims. Review flags for unlinked DOI strings are **not** proof of bad citations, because references may use a publisher or PubMed URL instead.

**Publication policy:** Do not label the entire repository scientifically validated until S1–S5 evidence covers each substantive claim in the intended release scope. Existing `ABSTRACT_ONLY` materials remain abstract-only until a separate full-text review is recorded.
