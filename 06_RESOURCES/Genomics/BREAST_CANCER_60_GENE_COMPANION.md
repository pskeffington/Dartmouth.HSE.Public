# 60-Gene Breast Cancer Research Companion

[Genomics resources](README.md) · [The people behind the data](BREAST_CANCER_TCGA_BRCA_NARRATIVE.md) · [Original 21-gene guide](COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md)

A gene name is the beginning of a question. What does its product normally do? Which cells produced the measured signal? What experiment could distinguish a plausible mechanism from an association? This companion connects 60 independently selected human genes to those questions through normal biology, breast cancer research and careful interpretation.

The people who contribute specimens make this research possible. A tumor-normal value represents sampled tissue at a particular time, with limits on what it can reveal about a person's disease. Our examples use invented numbers and conceptual diagrams; they do not reconstruct anyone's clinical history.

This is an **educational catalog**, not a diagnostic signature, a ranked discovery list, a PAM50 replacement or a treatment-selection tool. It retains all 21 genes in the published foundation guide and adds 39 distinct genes using a [public, source-backed selection rubric](REFERENCES/SELECTION_RUBRIC.md). Overlapping domains reflect overlapping biology rather than exclusive subtype identities.

## Contents

- [Start learning](#start-learning)
- [Explore the catalog](#explore-the-catalog)
- [Read evidence with its limits](#read-evidence-with-its-limits)
- [Seven visual explanations](FIGURES/README.md)
- [Reproduce and validate](#reproduce-and-validate)

## Start learning

Choose a [self-guided route](GENE_BIOLOGY_LEARNING_GUIDE.md#choose-a-route):

- **Beginner:** DNA, RNA and proteins → measurements → an invented paired comparison → three contrasting gene cards.
- **Biological:** Hormone and growth signaling → proliferation and repair → epithelial identity → immune and stromal context.
- **Research:** Stable annotation → study design → differential expression and multiple testing → evidence limits and conflicting findings.

The [measurement guide and glossary](GENE_EXPRESSION_INTERPRETATION.md) explain fold changes, bulk RNA-seq, somatic and germline variants, adjacent-normal tissue, false discovery rate and clinical versus statistical significance. The [domain learning guide](GENE_BIOLOGY_LEARNING_GUIDE.md) provides objectives, worked conceptual examples, questions and answer checks for all 12 domains.

## Explore the catalog

The [alphabetical and domain index](GENE_ATLAS_INDEX.md) links every card. Each card includes nine sections: identity; normal function; breast research; subtype context; measurement; clinical and research relevance; limitations; literature; and student takeaways.

Try a comparison rather than memorizing names:

- [ESR1](GENE_CARDS/ESR1.md) versus [FOXA1](GENE_CARDS/FOXA1.md): receptor abundance and the chromatin context for receptor activity.
- [BRCA2](GENE_CARDS/BRCA2.md) versus [RAD51](GENE_CARDS/RAD51.md): inherited variant evidence and a model-specific repair mechanism.
- [KRT8](GENE_CARDS/KRT8.md) versus [CD8A](GENE_CARDS/CD8A.md): epithelial identity and immune composition in the same bulk specimen.
- [MALAT1](GENE_CARDS/MALAT1.md): why opposing model results should remain visible.
- [PTEN](GENE_CARDS/PTEN.md): why protein and RNA associations need not agree.

The [pathway overview](GENE_PATHWAY_OVERVIEW.md) connects the domains without asserting that all listed genes bind each other.

## Read evidence with its limits

All 60 approved symbols have unique HGNC, NCBI Gene and Ensembl identities cross-checked on **2026-10-10**, with aliases retained for historical searches. The [annotation register](REFERENCES/ANNOTATION_SOURCE_REGISTER.md) documents the access snapshot and update procedure.

The [evidence matrix](REFERENCES/GENE_EVIDENCE_MATRIX.md) identifies primary publications, designs, models, narrow claims, limitations and review extent. This edition reviews bibliographic records and abstracts: **all 56 unique primary publications are `ABSTRACT_ONLY` here**, including foundational readings. None is labeled a completed independent full-text method audit. Most card sources are from 2021–October 2026; older sources are retained where they establish classification, receptor regulation, stress biology or trial context.

Some primary readings supply composition or pathway context rather than direct perturbation evidence for the card's gene. That distinction is explicit. An abstract's authors may describe a proposed biomarker or target more strongly than these cards do. A statistical association, an experimental intervention, a prognostic result and a validated clinical test answer different questions. A primary citation does not make those claims interchangeable.

## Reproduce and validate

From the repository root:

```bash
python3 scripts/build_gene_companion.py --check
python3 scripts/validate_gene_companion.py
python3 -m unittest discover -s tests -v
python3 06_RESOURCES/Presentation/check_navigation.py
Rscript --vanilla 06_RESOURCES/tests/test_gene_companion_heatmap.R
```

The [curated source](../../scripts/gene_companion_content.py) contains selected public identity facts and original explanations; [domain source](../../scripts/gene_companion_domains.py) contains the original teaching sequences. [The builder](../../scripts/build_gene_companion.py) reproduces cards, indices, domain guide and registers. Static editorial pages and diagram source remain directly editable Markdown, reviewed by the validator and documentation checks.

[The synthetic heatmap script](FIGURES/gene_companion_heatmap.R) uses invented labels and signed log2 changes, with the repository's centered blue–neutral–red scale. Optional PNG/PDF exports stay outside the checkout. No private source text, private signature, participant-level measurements or model objects are inputs to this companion.

[Validation review and publication boundaries](REFERENCES/COMPANION_VALIDATION_REVIEW_2026-10-10.md).
