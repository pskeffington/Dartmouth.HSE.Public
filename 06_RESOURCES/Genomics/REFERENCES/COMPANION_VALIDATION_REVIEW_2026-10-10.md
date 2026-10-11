# Companion validation review — 10 October 2026

Focused supporting reference for the [Breast Cancer Research Guide — People, Data, Biology and 60 Genes](../BREAST_CANCER_60_GENE_COMPANION.md).

[Companion](../BREAST_CANCER_60_GENE_COMPANION.md) · [Selection rubric](SELECTION_RUBRIC.md) · [Evidence matrix](GENE_EVIDENCE_MATRIX.md)

## Scientific scope reviewed

Exactly 60 unique approved human genes are represented: all 21 published foundation genes plus 39 independently selected additions. HGNC identities were cross-checked against NCBI human records and Ensembl stable IDs on the access date. No ambiguous or withdrawn primary identity was admitted. Aliases are recorded as search aids and are not used to join records.

The catalog covers all 12 teaching domains, with multiple membership allowed. Every card contains the nine required sections, distinct function and study explanations, three learning concepts, a question, an interpretation mistake and an exercise. The three routes, glossary, domain examples and mastery checks distinguish tissue composition, measurement and inference.

The register contains 56 unique primary publications. Bibliographic records and abstracts were reviewed; **all literature accounts remain `ABSTRACT_ONLY`**. Annotation acceptance does not upgrade literature review. Specific clinical or subtype claims are constrained to the referenced design and assay. MALAT1's opposing model results and PTEN's protein/RNA differences are explicitly retained. The edition does not establish a clinical signature, fitted cancer result, replication claim or individual patient recommendation.

## Local validation evidence

| Gate | Observed result |
|---|---|
| Catalog validator and deterministic builder check | PASS: 60 identities, retained 21, 12 domains, complete cards and generated registers |
| Python regression suite | PASS: 110 tests, including 11 companion contracts and failure cases |
| Python syntax compilation | PASS for scripts and presentation tools |
| Public reading editions | PASS: 8 checked, none stale |
| Internal navigation | PASS: 1,506 local links across 128 documents, including this review |
| R resource contracts | PASS, including the new synthetic heatmap numerical/display contract |
| Existing executable teaching examples | PASS: gallery, weekly R companions and Bash companion |
| Synthetic heatmap export | PASS: local PNG/PDF exports outside Git; labels, signed units, orientation and zero-centered palette visually reviewed |
| Whitespace/diff checks | PASS |

The seven original visual resources are Mermaid source embedded in Markdown: six conceptual schematics and one invented signed-expression heatmap. Captions identify inputs, conceptual/synthetic state and public sources. Numeric labels and a plain table provide color-independent access. The R contract compares all 24 displayed heatmap values with the invented matrix. No media binaries or external figure artwork enter the change.

## Publication and provenance boundary

Current-tree protected-source comparison found no matches. A separate full-history audit retains earlier text matches; those have not been certified as resolved or rewritten. Detailed comparisons and protected inventory stay local. The installed pre-push guard independently evaluates the final tree and all newly introduced commits, using content-bound original-work evidence.

The ordinary public change scanner found no new or changed originality findings. The two byte-identical existing PDF reviews remain unresolved. Provenance observations preserve the registry's null self-digest, existing rights-review flags and unverified whole-repository disposition. These are observations and guarded change checks, not a blanket copyright certificate.

CI runs the builder check, catalog validator, complete regression suite, navigation, reading-edition and provenance gates, plus R numerical contracts and heatmap export. Actual PR and merged-main outcomes belong to GitHub check records; this local review does not predeclare their acceptance.

## Reproduction

Run the commands in the [companion](../BREAST_CANCER_60_GENE_COMPANION.md#reproduce-and-validate) and the normal [contributor publication checks](../../../CONTRIBUTING.md). Original text and generator methods are retained in tracked source. Protected comparison inputs and authoring records are checkout-local, not public reproducibility datasets. Updating identities or evidence review extent requires a new source audit and normal guarded publication.
