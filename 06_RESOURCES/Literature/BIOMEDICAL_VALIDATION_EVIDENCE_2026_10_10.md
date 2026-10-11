# Biomedical companion — validation evidence (2026-10-10)

**Run:** [GitHub Actions 38033351968](https://github.com/pskeffington/Dartmouth.HSE.Public/actions/runs/38033351968) — **SUCCESS**. Commit under test: `e58710f6434483673c63d00f40408332ef8ef915`. Platform: Ubuntu 24.04.5, R 4.6.1, x86_64. These are *synthetic educational examples*, not clinical findings and not independent reproductions of any source papers.

## What actually passed

- Corpus CSV structural validator: **8 records, 0 schema errors, 8 review notices**. All remain `DISCOVERED`; this test does **not** verify DOI resolution or article method claims.
- Unit 6 script: **PASS**; in-script cohort/data-contract and manual-vs-built-in Welch calculations passed.
- Unit 7 script: **PASS**; patient-disjoint train/holdout, finite predictions, model and diagnostic sanity assertions passed.
- Unit 8 script: **PASS**; patient-disjoint split, finite bounded probabilities, observed class presence and confusion-matrix checks passed.
- Diagnostic logs were uploaded. Exact results below are **illustrative** and arise from fixed-seed data-generation code.

## Captured outputs

| Metric | Synthetic result | Interpretation guard |
| --- | ---: | --- |
| Unit 6: mean intervention-control | 1.8917 mg/L | Simulated group difference, not a clinical treatment effect |
| Unit 6: 95% Welch interval | [0.5529, 3.2304] mg/L | Conditional on simulated model/sampling assumptions |
| Unit 6: Welch p-value | 0.00622 | Does not establish clinical importance or causal effect |
| Unit 7: train / holdout | 210 / 90 | Zero overlapping IDs reported |
| Unit 7: holdout MAE | 1.8851 mg/L | In-population synthetic prediction error |
| Unit 7: holdout RMSE | 2.2659 mg/L | Not external validation |
| Unit 7: holdout Brier | 0.1830 | Model mean predicted 0.1783 vs observed event fraction 0.2778; investigate calibration |
| Unit 8: train / holdout | 450 / 150 | Zero overlapping IDs |
| Unit 8: AUROC | 0.7326 | Discrimination ranking only |
| Unit 8: Brier | 0.1688 | Probability scoring; does not prove calibration or clinical utility |
| Unit 8: sensitivity / specificity | 0.421 / 0.821 | At prespecified educational threshold 0.30 |
| Unit 8: PPV / NPV | 0.444 / 0.807 | Depend on prevalence and target population |

### Unit 8 calibration limitations

| Predicted-risk bin | Mean predicted | Event fraction | n |
| --- | ---: | ---: | ---: |
| [0,0.2] | 0.1186 | 0.1379 | 87 |
| (0.2,0.4] | 0.2876 | 0.3864 | 44 |
| (0.4,0.6] | 0.4627 | 0.4444 | 18 |
| (0.6,0.8] | 0.6249 | 1.0000 | **1** |

The last bin contains only one observation. Its empirical event fraction is effectively uninformative as a calibration estimate; graphs must annotate denominators and avoid implying stable high-risk calibration. Calibration uncertainty and subgroup/external validation remain open scientific tasks.

## Independent release gate findings

**Public originality run:** [38033351932](https://github.com/pskeffington/Dartmouth.HSE.Public/actions/runs/38033351932) — **FAILURE**. Log verified: 99 tests passed (one skipped); 8 reading editions current; 495 local links passed. Enforced release failed due to `SCREEN` and `INVENTORY` outcomes.

**Provenance reason:** tracked changes require records in `PROVENANCE_RECORDS.json`; the inventory script fails closed when paths are unrecorded, hashes stale or records obsolete. Never bypass this to publish original work. Resolve by recording correct origin/rights evidence and regenerating accurate content hashes according to repository policy. No institutional source upload is authorized.

**Originality-screen reason:** scanner/review outcome requires inspection of artifact `originality-screening-report`; the existence of review findings is **not** proof that the new original documents infringe. Conversely, passing script tests is not copyright clearance. A human rights review and available private-source comparison are still needed where required.

## Gate decisions

| Gate | Decision |
| --- | --- |
| Executable synthetic examples / basic numerical contracts | PASS |
| Corpus structure, uniqueness and required fields | PASS |
| External DOI check of all eight papers | NOT_VERIFIED |
| Complete paper methods extraction / actual study reproduction | NOT_VERIFIED |
| Scientific validation of models and small-bin calibration | REVIEW_REQUIRED |
| Provenance inventory | FAIL |
| Public originality release screen | FAIL |
| Draft PR publication | BLOCKED |

This report describes outcomes from GitHub logs, not separate local execution. Do not merge PR #30 based solely on the biomedical job success.

## Local follow-up — 2026-10-11

The historical CI failures above remain a record of that earlier commit. After merging current `main`, `python3 scripts/build_provenance_inventory.py --check --output /tmp/pr30-provenance.json` passed. This establishes consistent inventory metadata, not rights clearance.

These commands each exited 0 in separate clean base-R sessions on R 4.4.3, macOS arm64:

```bash
Rscript --vanilla 06_RESOURCES/R/examples/unit_06_inference.R
Rscript --vanilla 06_RESOURCES/R/examples/unit_07_regression.R
Rscript --vanilla 06_RESOURCES/R/examples/unit_08_classification.R
python3 06_RESOURCES/tests/validate_biomedical_corpus.py
```

The rounded numerical outputs match the captured values above: Unit 6 difference 1.8917 mg/L and interval [0.5529, 3.2304]; Unit 7 MAE 1.8851 mg/L, RMSE 2.2659 mg/L and Brier 0.1830; Unit 8 AUC 0.7326 and Brier 0.1688. The calibration bin with one observation remains unsuitable for stable inference. The corpus validator reported 8 records, 0 schema errors and 8 review notices. No source paper was reproduced.

Dated source checks against public primary metadata:

| Candidate | Identity observation on 2026-10-11 | Remaining limitation |
| --- | --- | --- |
| TRIPODAI2024 | [BMJ article](https://www.bmj.com/content/385/bmj-2023-078378), Collins and colleagues, 2024 | Reporting guidance does not certify model validity |
| TRIPODLLM2025 | [Nature Medicine](https://www.nature.com/articles/s41591-024-03425-5), Gallifant and colleagues, published 2025-01-08 | Guidance is versioned; full methods appraisal pending |
| STARD2025 | [Nature Medicine](https://doi.org/10.1038/s41591-025-03953-8), 2025; [author correction](https://doi.org/10.1038/s41591-026-04570-9) | Corrected text must be assessed before detailed use |
| STREIBER2025 | [PubMed 41043836](https://pubmed.ncbi.nlm.nih.gov/41043836/), Streiber and colleagues, 2025-10-02; DOI matches | Article/code licensing and full extraction pending |
| SHIFT2025 | [PubMed 40876698](https://pubmed.ncbi.nlm.nih.gov/40876698/) and Crossref agree on DOI, authors, journal and 2025 identity | Abstract-level observation; no methods reproduction |
| EVIDENCE2026 | Publisher destination returned HTTP 403 during this check | REVIEW_REQUIRED; do not rely on an inaccessible primary record |
| EXTERNAL2025 | [PubMed 40845608](https://pubmed.ncbi.nlm.nih.gov/40845608/) and Crossref agree on DOI, authors, journal and 2025 identity | Full text and applicability review pending |
| TRIPODTOOL2026 | [Springer Nature](https://link.springer.com/article/10.1186/s12911-026-03866-7), Musa, published 2026-09-23 | Publisher labels an early citable version subject to replacement; no independent validation |

The CSV remains `DISCOVERED`; identity observations do not clear rights, support every teaching claim, or establish reproduction. Required release work: content-bound human rights review for the new standalone CSV, scientific/educational appraisal of Units 6–8, and green required CI on the final candidate.
