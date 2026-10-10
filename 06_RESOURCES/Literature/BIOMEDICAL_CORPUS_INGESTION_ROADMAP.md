# Biomedical evidence corpus — targeted ingestion roadmap

**Date:** 2026-10-10. **Scope:** public, independently authored evidence for Paul's Notes, Units 6–10 and future biomedical health-sciences study. **Not** a mirror of institutional lectures, an unrestricted full-text archive, or a claim that source code from the papers was reproduced.

## Selection principle

Ingest papers because they support a **specific learning objective and runnable method**. Prefer directly applicable primary methods and empirical validation evidence, then consensus reporting standards, then systematic reviews, then tutorials/editorials for orientation. Flag study type; never treat checklists as trials.

## Search lanes and reusable queries

| Lane | Example PubMed search | Required implementation trace | Target |
| --- | --- | --- | --- |
| Statistical estimation | `("confidence intervals"[Title/Abstract] OR "clinical importance"[Title/Abstract]) AND (biomedical OR clinical) AND 2024:2026[dp]` | estimand; distribution; uncertainty; sensitivity | 6 |
| Regression and diagnostics | `("clinical prediction"[Title/Abstract] OR regression[Title/Abstract]) AND (validation OR calibration OR assumptions) AND 2024:2026[dp]` | predictor timing; formulas; missingness; diagnostics | 7 |
| Classifier validation | `("clinical prediction model"[Title/Abstract]) AND (external validation OR calibration OR data leakage) AND 2024:2026[dp]` | train/holdout unit; prevalence; AUROC/AUPRC; Brier; calibration | 8 |
| Reproducibility | `("medical research"[Title/Abstract]) AND (reproducibility OR code sharing OR provenance) AND 2024:2026[dp]` | software versions; seed; test; data/code availability | 9 |
| Responsible AI / drift | `("machine learning" AND healthcare) AND (dataset shift OR fairness OR monitoring) AND 2024:2026[dp]` | cohort shift; subgroup evaluation; intended use; oversight | 10 |

Search **PubMed**, then cross-check **Crossref DOI metadata**, publisher article pages, and open full text at **PMC** when available. Add other domain indexes only when a specific question calls for them. Preserve literal query, search date, databases, page/count and inclusion/exclusion decisions.

## Evidence scoring (0–100)

- **Direct fit to a measurable objective (0–25):** 25 for method and exercise match, 15 for conceptual relevance, 5 for background only.
- **Methodological transparency (0–20):** access to design, sampling, exclusions, variables, validation and uncertainty.
- **Execution reproducibility (0–20):** accessible runnable code/environment and licensed data, or completely specified method for faithful independent illustration.
- **Evidence strength / applicability (0–15):** appropriate design, comparison, bias limitations, relevant patient/data context.
- **Freshness (0–10):** 2026=10, 2025=8, 2024=6, older=0–5 depending on foundational status.
- **Rights and metadata completeness (0–10):** resolvable DOI, verified authors/year, permissible quotation and link/access status.

**Tiers:** A >=80; B 65–79; C 50–64; hold below 50. A paper with an unresolved DOI, substantial corrections, retraction concerns, unclear source rights or undisclosed methods is **REVIEW_REQUIRED** irrespective of numeric score. Retain valuable older foundational papers as separately marked `FOUNDATIONAL`, rather than forcing them to compete solely on recency.

## Evidence record contract

A machine-readable row must contain `paper_id,doi,year,title,study_type,primary_url,unit,objective_ids,method_summary,execution_steps,reason_for_method,code_availability,data_access,reproduction_status,verification_status,score,relevance_note`. Optional next-pass fields: `pmid,license,search_query,search_date,cohort,setting,n_samples,missingness,estimand,leakage_control,validation_design,calibration,limitations,correction_status`.

Allowed states:
- `DISCOVERED`: linked metadata, not independently checked;
- `METADATA_VERIFIED`: title, authors/year, DOI and article type checked against primary indexing;
- `METHOD_EXTRACTED`: study design and methods summarized from accessible source;
- `EXECUTION_SPECIFIED`: own workflow implementation and required data contract written;
- `REPRODUCED`: original reported results independently recreated with artifacts and versioned code;
- `SYNTHETIC_DEMO_ONLY`: independently written illustration, not a published experiment's replication;
- `REVIEW_REQUIRED`: rights, scientific, identity or methodological issues unresolved.

Do **not** use `REPRODUCED` after merely running a synthetic exercise.

## Acquisition and extraction workflow

**C0 — Intake:** query scholarly databases; deduplicate by DOI then PMID; collect title, publication year, journal, design and landing page. Preserve provenance and retrieval timestamp. Do not download/paywall-scrape copyrighted PDFs.

**C1 — Identity and integrity:** resolve DOI, confirm publication and correction/retraction status from publisher/PubMed, reconcile discrepancies. Stop if material fields disagree.

**C2 — Question mapping:** record unit(s), specific learning objective IDs, relevant inputs and expected output. Reject papers with no actionable teaching link, even when heavily cited.

**C3 — Methods reading:** extract *reported* design, cohort/setting, observational unit, input dimensions and units, missingness, time zero, split unit, tests/models, uncertainty, comparison and limitations. Quote minimally; paraphrase independently with attribution.

**C4 — Coding rationale:** write why each model, link function, threshold, diagnostic, preprocessing decision and uncertainty method was selected; distinguish paper-author justification from our own teaching interpretation.

**C5 — Execution:** where data/code are openly licensed and safe to use, reproduce only with a documented environment and artifact hashes. Otherwise write a clean synthetic example tagged `SYNTHETIC_DEMO_ONLY`. Never imply results were replicated by synthetic code.

**C6 — Verification:** run offline tests, scientific sanity checks, link/DOI validators, numerical regression tests and independent review. Capture exact versions, seeds, run commands and expected outputs. Fail closed on ambiguity.

**C7 — Teaching integration:** place an annotated method capsule beside lesson sections, attach learning objectives, exercises, failure modes and mastery checks. Explicitly separate consensus checklists, reviews, primary experiments and clinical trials.

**C8 — Publication:** add navigable markdown and reference rows under `06_RESOURCES/Literature/` without copying institutional documents. Original works may enter PRs through ordinary repo safeguards; source-dependent changes retain private rights comparison. Merge only after verified sources and runtime checks.

## Sprint priority and exit gates

| Priority | Deliverable | Ready when |
| --- | --- | --- |
| 1 | Unit 8: leakage, discrimination, calibration and held-out evaluation | 3 scored, verified clinical prediction/validation papers; one runnable synthetic demo; diagnostics |
| 2 | Unit 7: diagnostics and predictor timing | 2 empirical/methods studies with extracted design and model checks; updated exercises |
| 3 | Unit 9: reproducibility and provenance | 2 practical studies + clean-run manifest/checklist |
| 4 | Unit 10: drift, diagnostic AI, responsible deployment | 3 sources spanning AI reporting, external shift, oversight |
| 5 | Unit 6: estimation and clinical importance | 2 empirical methodology sources beyond established foundational guidance |

**Exit for each unit:** >=3 fit-justified sources (including >=1 original methodological/empirical study when applicable), DOI verification, full reported-methods table, original coding rationale, reproducible example with independent tests, objective-to-evidence matrix, accessible navigation and provenance review. The thresholds are editorial goals, not evidence of curriculum requirements.

## Current evidence queue

Use [candidate inventory](BIOMEDICAL_CORPUS_2026_CANDIDATES.csv) for seeded references. All are `DISCOVERED` pending structured extraction and reproduction, even when publication metadata has been checked online. Initial candidates include TRIPOD+AI (2024), TRIPOD-LLM (2025), STARD-AI (2025), a 2025 medical-code reproducibility recommendations paper, a 2025 systematic review of dataset shift and a 2026 methodological paper on dataset-structured model evidence synthesis. No full paper's original results have been reproduced in this intake.

**Quality principle:** at each publication pass, automatically reject unsupported claims such as “reproduced” when no run log and verified comparison artifact exists.
