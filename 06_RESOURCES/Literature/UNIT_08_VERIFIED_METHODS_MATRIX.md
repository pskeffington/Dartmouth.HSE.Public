# Verified methods-to-objectives ingestion slice — October 10, 2026

**Scope:** Unit 8 and overlap with Units 7, 9, 10. **Evidence identity:** publisher and/or PubMed reviewed, as indicated. **Execution state:** NO PAPER REPRODUCED. All study descriptions below summarize public article pages/abstracts, not independent full-paper replication. This file supplements the candidate inventory; it does not replace an audit log.

| Paper | Identity checked | Research execution as reported | Instructional adaptation | Objective | Gate and limits |
| --- | --- | --- | --- | --- | --- |
| [Collins et al., TRIPOD+AI (2024)](https://doi.org/10.1136/bmj-2023-078378) | BMJ original article, DOI, publication 2024-04-16 | Reporting-guidance development; 27-item checklist for development and evaluation of regression and ML prediction models | Write transparent model/specification sheet, report subgroup evaluation, missingness and open science | U7-1, U8-1, U8-7 | METADATA_VERIFIED / METHOD_EXTRACTED (publisher narrative); guidance **not** clinical model evaluation; supersedes original TRIPOD 2015 |
| [Sounderajah et al., STARD-AI (2025)](https://doi.org/10.1038/s41591-025-03953-8) | Nature Medicine published 2025-09-15; correction dated 2026-07-13 | Scoping review/survey, patient-public engagement, modified Delphi with >240 stakeholders; 18 new/modified reporting items | Compare AI diagnostic index test/reference standard reporting against our *different* risk-prediction example | U8-7, U10-1 | METADATA_VERIFIED / METHOD_EXTRACTED (publisher narrative); read corrected version; rights reserved |
| [Ben Hmido et al. (2025)](https://doi.org/10.1016/j.ejso.2025.110367) | PubMed PMID 40845608; online 2025-08-14 | PRISMA systematic review, searched MEDLINE/Embase/Web of Science/Cochrane, identified 10 studies; extracted CHARMS, assessed PROBAST and TRIPOD+AI | Compare systematic-review extraction, sample size, events, missingness, validation, applicability | U7-7, U8-7 | METADATA_VERIFIED / METHOD_EXTRACTED (PubMed abstract); full text extraction and study-level reproduction pending |
| [Arshi et al. (2025)](https://doi.org/10.1016/j.jclinepi.2025.111902) | PubMed PMID 40675230; online 2025-07-16 | Prospective research follow-up of random 109 CPM articles using forward citation searching, time-to-validation Kaplan-Meier analyses and author survey | Separate internal holdout, external validation, impact study and real-world utilization | U8-7, U10-4 | METADATA_VERIFIED / METHOD_EXTRACTED (PubMed abstract); author follow-up data not reproduced |

## Scoring audit (provisional)

Scores are editorial assessments (NOT scientific evidence quality certificates). Each component has the maximum defined in the corpus roadmap: fit 25, methods 20, reproducibility 20, applicability 15, recency 10, metadata/rights 10. Reproducibility reflects *availability of an independently teachable approach*, not successful replication.

| Record | Fit | Methods | Reproducibility | Applicability | Freshness | Metadata | Total | Treatment |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TRIPODAI2024 | 25 | 18 | 12 | 12 | 6 | 10 | 83 | A, reporting reference |
| STARD2025 | 15 | 18 | 10 | 11 | 8 | 7 | 69 | B, diagnostic contrast; correction tracked |
| EXTERNAL2025 | 25 | 17 | 8 | 14 | 8 | 9 | 81 | A, empirical methodological review |
| VALIDATION2025 | 24 | 18 | 8 | 14 | 8 | 9 | 81 | A, follow-up empirical study |

Review scores if code/data access or correction handling changes. Record source classification; ranking must not imply a reporting guideline is an original diagnostic accuracy experiment.

## Unresolved checks

- Direct article supplementary materials and complete methods not yet extracted; avoid claims about methods not visible in indexed material.
- Full bibliographic author lists, correction details, licensing and machine-checkable DOI resolving remain to be audited in a reproducible metadata pipeline.
- No retraction audit, primary dataset access, study reproduction or Unit 8 runtime test has passed.
- Candidate inventory still contains DISCOVERED entries; reconcile these four statuses only after review of links and schema/record consistency.

## Why these papers matter to our code

**Method:** reproduce *structure* rather than protected expression: define patient-level split, index-time predictors and binary outcomes. **Reasoning:** information leakage, weak reporting and unexamined calibration make superficially strong models unreliable. **Implementation:** [synthetic classifier source](../R/examples/unit_08_classification.R) models baseline probabilities and reports AUC, Brier score, fixed-threshold confusion metrics and bin-level calibration. **Objectives:** [Unit 8 teaching guide](UNIT_08_CLASSIFICATION_TEACHING_GUIDE.md) requires learners to distinguish ranking from probabilistic accuracy and internal evaluation from clinical validation.

The synthetic script uses none of the real studies' data and does not reproduce the literature's empirical findings.
