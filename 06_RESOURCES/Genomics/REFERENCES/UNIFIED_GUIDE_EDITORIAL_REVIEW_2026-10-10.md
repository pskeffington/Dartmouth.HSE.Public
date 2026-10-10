# Unified guide editorial validation — 10 October 2026

[Breast Cancer Research Guide — People, Data, Biology and 60 Genes](../BREAST_CANCER_60_GENE_COMPANION.md) · [Evidence matrix](GENE_EVIDENCE_MATRIX.md)

## Scope and architecture

The existing companion URL is the sole continuous guide: 12 ordered chapters, ten connected biology lessons, 60 substantive integrated profiles and seven inline original diagrams. All 60 standalone cards remain available; their scientific content and the 21 foundational identities are unchanged. Twelve original domain categories remain in the structured index. The alphabetical table, three learning routes, chapter navigation and historical guide fragments resolve locally.

Original chapter prose resides in `scripts/gene_companion_chapters.py` (`UNIFIED_GUIDE_V1`). Both figure views use `scripts/gene_companion_figures.py` (`UNIFIED_FIGURES_V1`). The shared curated gene catalog supplies normal functions, model-specific findings, measurement limits and source states. The validator binds editorial sources to public content seals and the builder checks exact deterministic output without writing in check mode.

## Local validation

- 127 Python regression tests passed, including 28 companion contracts. Failure cases cover reordered chapters, changed anchors, missing or renamed cards, duplicate entries, broken nested links, removed routes, stale outputs and altered editorial source versions/seals.
- All 19 resource R sources parsed. All nine R resource contract scripts passed, including the six-pair walkthrough and both heatmap presentations.
- Eight reading editions are current. Navigation checked 1,775 local links across 128 documents before this review page was added; the final whole-repository navigation check includes this page.
- Eight gallery R blocks produced 12 expected figures outside the checkout. Forty weekly/companion R blocks and 14 Bash blocks passed.
- Public provenance observations and content-bound original-work authoring records were refreshed. The live protected-source comparison passed for the proposed current public tree; private inventories and detailed reports remain outside Git. Normal guarded push separately checks newly introduced history.

The six-pair example has mean log2 ratio 0.5, observed range −1 to +2 and leave-one-pair mean range 0.2–0.8. It explicitly labels sensitivity as **not a confidence interval**. There are no participant records, private analyses or clinical findings in these invented values.

## Publication and scientific boundaries

Local checks do not substitute for GitHub-rendered review, required CI or merge checks; their final results are recorded in the associated PR. No literature evidence was upgraded: all accounts remain `ABSTRACT_ONLY`, with annotation verification kept separate. MALAT1 opposing experiments and PTEN protein/RNA disagreements remain explicit. Epidemiology retains the 2024 year and distinct sex denominators; the GDC case count remains a dated project snapshot.

The two unchanged legacy LaTeX PDF rights-review findings remain unresolved. The ordinary-change originality gate passes without declaring whole-repository or historical rights clearance. Protected history is not rewritten, and no institutional sources, private comparisons, datasets, signatures or model objects are distributed by this change.
