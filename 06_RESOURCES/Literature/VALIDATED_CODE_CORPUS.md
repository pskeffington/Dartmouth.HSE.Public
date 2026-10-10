# Validated biomedical code corpus — acquisition and acceptance protocol

[Library index](README.md) · [Coding standards](BIOMEDICAL_CODING_STANDARDS.md) · [Program roadmap](PROGRAM_COMPANION_ROADMAP.md)

**Status: candidate-source registry; no downloaded implementation is represented as tested.** This document defines an independent, reproducible collection workflow. Documentation and software licenses must be verified at the exact version/commit before redistribution. Prefer links and dependency manifests over copying upstream code.

## Candidate primary sources

| Domain | Upstream authority | Reproducible exercise | Validation requirement |
| --- | --- | --- | --- |
| Numerical methods | [NumPy](https://numpy.org/doc/stable/), [SciPy](https://docs.scipy.org/doc/scipy/) | deterministic array statistics and hypothesis tests | analytic fixtures, shape, missingness and tolerance checks |
| Data science pipelines | [scikit-learn](https://scikit-learn.org/stable/) | preprocessing inside cross-validation | demonstrate absence of train/test leakage, seeded splits, calibration |
| R biostatistics | [R manuals](https://cran.r-project.org/manuals.html) | generalized linear models | known coefficient fixture, convergence and confidence interval tests |
| RNA sequencing | [edgeR](https://bioconductor.org/packages/edgeR/), [DESeq2](https://bioconductor.org/packages/DESeq2/) | synthetic count matrix, design matrix and differential expression | library sizes, contrasts, FDR and version-locked output |
| Biomedical imaging | [SimpleITK](https://simpleitk.org/), [MONAI](https://monai.io/) | synthetic volume and segmentation | spacing, orientation, voxel shape, mask alignment |
| Physiologic signals | [PhysioNet](https://physionet.org/), [WFDB](https://wfdb.readthedocs.io/) | synthetic ECG with known event locations | sample rate, units, detection sensitivity and false positives |
| Interoperability | [FHIR](https://hl7.org/fhir/), [OMOP CDM](https://ohdsi.github.io/CommonDataModel/) | synthetic observation mapping | schema version, terminology, units, temporal and patient-key constraints |
| Reproducibility | [FAIR](https://www.go-fair.org/fair-principles/), [RO-Crate](https://www.researchobject.org/ro-crate/) | manifest and artifact provenance | environment lock, checksums, seed and machine-readable provenance |

## Corpus record contract

Each candidate has: `id`, `domain`, `source_url`, `source_type`, `citation`, `upstream_version_or_commit`, `retrieved_utc`, `license_identifier`, `license_evidence_url`, `reuse_decision`, `local_example_path`, `runtime`, `dependency_lock`, `fixture_path`, `test_command`, `expected_output`, `test_result`, `test_timestamp_utc`, `reviewer`, and `limitations`.

Use these evidence labels only:
- **CANDIDATE:** source identified; license and behavior not yet verified.
- **LICENSE_REVIEWED:** exact source/version and permitted use checked.
- **REPRODUCED:** independent fixture passes in a pinned environment with captured logs.
- **REVIEWED:** scientific assumptions, leakage, units, identifiers and edge cases checked.
- **RELEASED:** CI reproduces the example; manifest, citations and license evidence are complete.

Never mark a source REPRODUCED from a successful installation, copied screenshot, publication claim or an unexecuted example.

## Ingestion workflow

1. Register the canonical upstream URL, publication DOI where relevant, version/commit, and access date.
2. Inspect exact code and data licenses separately; keep copyrighted institutional lecture files excluded. No assumption that open access means permissive reuse.
3. Store bibliographic metadata and links first. Vendor only explicitly permitted, necessary source snippets with attribution; prefer original implementation of public algorithms.
4. Create a minimal synthetic or openly licensed fixture, with documented units, dimensions, identifiers and expected output.
5. Pin R/Python and dependencies; run deterministic tests in an isolated environment.
6. Compare numerical results against an independent analytic calculation or second trusted implementation; record tolerances.
7. Test missingness, zero counts, class imbalance, invalid units, duplicate IDs, data leakage and malformed inputs as applicable.
8. Capture command, runtime, environment digest, logs, artifacts, checksums and reviewer decision.
9. Run CI and originality/source-file guard on every proposed change; guard should reject protected source artifacts, not independently authored work.
10. Publish only after review; failed candidates remain visible as candidates, never as validated code.

## Initial acceptance gates

- G0: 8 domain entries have source and licensing metadata.
- G1: 2 independently authored, runnable synthetic examples per domain.
- G2: tests include expected numerical results and negative controls.
- G3: automated matrix for supported runtime versions, lint, unit/schema checks and reproducibility manifest.
- G4: documentation includes scientific purpose, assumptions, input/output schema, plotting labels, units, interpretation and limitations.

**Biomedical plotting:** explicitly label axes, measurement units, sample size and statistical estimator. Select domain-appropriate, color-vision-accessible palettes and document mappings; no single color palette is universally standardized across biomedical disciplines.

**Safety:** examples are educational research software, not clinical decision support or validated medical devices. Do not ingest identifiable patient data into the public corpus.
