# Scholarly evidence verification protocol

[Repository home](../../README.md) · [Literature matrix](README.md) · [60-gene source register](../Genomics/REFERENCES/ANNOTATION_SOURCE_REGISTER.md)

## Evidence boundary

A citation inventory is **not** a scholarly fact check. A resolvable DOI does not demonstrate that a source supports the adjacent assertion. Annotation identity checks do not validate clinical associations. A reproducible script does not independently validate its research design.

## Review stages

| Gate | Evidence required | Acceptable status |
|---|---|---|
| S0 Inventory | All Markdown paths, DOI and PMID strings, review labels, structural gaps | INVENTORIED |
| S1a Identity | Match a DOI or PMID to a dated authoritative registry response | IDENTIFIER_VERIFIED |
| S1b Bibliography | Inspect registry title, authors, year and journal; compare the intended citation and check dated correction/retraction notices | METADATA_VERIFIED |
| S2 Claim mapping | Independently appraise the exact claim, source, supporting section/table, design, population, endpoint, effect and limits | CLAIM_SUPPORT_REVIEWED, with a separate support/qualify/unsupported decision |
| S3 Methodology | Confirm assay, cohort, n, units, missingness, bias, statistics, multiplicity and independent data provenance | METHODS_REVIEWED |
| S4 Reproduction | Pin dependencies and authorized study inputs; execute the stated methods and match documented numerical tolerances | METHODS_REPRODUCED |
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

The optional `--metadata-file /tmp/registry-evidence.json` consumes a local object keyed by `doi:<normalized-doi>` or `pmid:<number>`. Each entry records `authority` (Crossref, DataCite or PubMed), HTTPS `source_url`, `retrieved_utc`, `lookup_status`, returned `identifier`, and bibliographic `title`, `authors`, `year`, `venue`. Record dated `publication_notices` separately, including corrections or retractions when returned. Failed or unavailable lookups remain `REVIEW_REQUIRED`. A matched registry identifier is `IDENTIFIER_VERIFIED`; complete returned bibliography is `METADATA_VERIFIED` only for that record. Citation matching and claim support still require appraisal. No notices returned is not proof that no notice exists.

Inventory v2 keeps identity, metadata, claim support and reproduction statuses separate. It never automatically assigns `CLAIM_SUPPORT_REVIEWED` or `METHODS_REPRODUCED`, even when registry metadata is complete. Existing source-register observations remain dated, limited observations; they are not upgraded by this inventory. Keep raw retrieval evidence local, and publish only independently written review decisions with source links. Synthetic test fixtures cover duplicate/case/encoded identifiers, balanced parentheses, malformed strings, unavailable records, corrections and retractions.

**Publication policy:** Do not label the entire repository scientifically validated until S1–S5 evidence covers each substantive claim in the intended release scope. Existing `ABSTRACT_ONLY` materials remain abstract-only until a separate full-text review is recorded.
