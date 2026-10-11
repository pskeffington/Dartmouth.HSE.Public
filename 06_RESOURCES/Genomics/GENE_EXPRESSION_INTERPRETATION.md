# Gene expression: measurement before interpretation

Focused supporting reference for the [Breast Cancer Research Guide — People, Data, Biology and 60 Genes](BREAST_CANCER_60_GENE_COMPANION.md).

[Companion](BREAST_CANCER_60_GENE_COMPANION.md) · [Learning routes](GENE_BIOLOGY_LEARNING_GUIDE.md) · [Figures](FIGURES/README.md)

## What was measured?

A DNA assay can detect sequence variants or copy number. RNA sequencing counts fragments assigned to annotated transcripts or genes. Immunohistochemistry localizes a protein in tissue; other protein assays quantify abundance or phosphorylation. These are complementary observations, with different inputs, errors and units. Higher RNA is not proof of an activating mutation, more protein, protein activation or treatment eligibility.

Before a comparison, write down specimen type, assay, units, cell composition, annotation and experimental design. A clinical ER or HER2 category is an assay-defined classification. PAM50 is a specified expression-based multi-gene classifier. Neither is assigned by selecting a familiar gene from this teaching catalog. [Parker et al. (2009)](https://pubmed.ncbi.nlm.nih.gov/19204204/) provides classifier-development context; [NCI](https://www.cancer.gov/types/breast/diagnosis/breast-cancer-biomarker-tests) explains clinical biomarker testing.

## A worked invented pair

Suppose normalized expression is 20 arbitrary units in an invented tumor specimen and 10 in its paired adjacent-normal specimen. The ratio is 2 and log2(2) is +1. Reversing the comparison gives a ratio of 0.5 and log2(0.5) of −1. This arithmetic has no patient interpretation, uncertainty estimate or statistical test attached.

Pairing reduces some between-person differences but does not make the specimens identical mixtures. Tumor, epithelial, immune, fibroblast and other fractions can differ. Imagine a second pair whose apparent immune increase comes entirely from more T cells: the bulk comparison cannot distinguish that explanation from increased transcription within T cells. The [paired-specimen figure](FIGURES/README.md#paired-specimens) illustrates the distinction.

Zero counts require an explicit statistical approach; casually adding a pseudocount can change small-count ratios. TPM and log-transformed TPM are not raw count matrices. Count-based differential-expression methods need their appropriate inputs and normalization, not substituted units. Learn the method before selecting a plot.

## Design and multiple testing

First define the question and experimental unit. For paired specimens, the person supplies the pairing structure; the specimens are not independent people. A study with two specimens from each of 10 participants has 20 specimens and 10 participants. Technical files are not additional participants.

A differential-expression model estimates a specified contrast while accounting for its design. Confounding, quality, batch, annotation and filtering affect interpretation. Multiple testing is relevant because thousands of genes may be examined: false discovery rate describes an expected fraction of false discoveries under a procedure's assumptions, not the probability that each reported gene is false. Report effect size, uncertainty, model and multiplicity together. This companion supplies no fitted cancer results, SEs or confidence intervals.

A small p-value does not establish a large effect, a causal mechanism, useful diagnostic discrimination or patient benefit. Clinical utility needs a suitable decision context and independent validation. A heatmap can display patterns but cannot perform that validation.

## Glossary

- **Gene expression:** Production and abundance of RNA from a gene, defined by the assay and units. It is not synonymous with protein activity.
- **Fold change:** Ratio of a measurement in a stated numerator condition to a denominator condition. Normalization and zero handling must be explicit.
- **Log2 fold change:** Base-2 logarithm of that ratio. +1 means twofold higher; −1 means half as high; 0 means equal in the stated comparison. It is not a z-score.
- **Somatic mutation:** A DNA change acquired in a subset of cells; a tumor finding need not be inherited.
- **Germline mutation:** An inherited or constitutionally present DNA variant. Pathogenicity is a separate classification; not every variant increases risk.
- **Adjacent-normal tissue:** Non-tumor tissue sampled near a tumor. It is not necessarily equivalent to tissue from an unaffected donor and may have different composition or field effects.
- **Molecular subtype:** A category assigned by a specified molecular method. Luminal A, luminal B, HER2-enriched and basal-like expression classes overlap incompletely with clinical hormone/HER2 categories.
- **Biological pathway:** A connected functional process supported by particular evidence. Sharing a category does not prove a direct physical interaction.
- **False discovery rate:** Expected fraction of false discoveries among selected findings under the chosen statistical procedure and assumptions. It is not a per-gene posterior probability.
- **Statistical significance:** Evidence against a specified null under a model and testing rule. Its practical meaning depends on effect size, design and uncertainty.
- **Clinical significance:** Relevance to a patient-facing outcome or decision, supported by appropriate clinical evidence. It cannot be read from a p-value alone.
- **Bulk RNA sequencing:** RNA measurement from a mixture of cells. Changes can reflect cell abundance, cell state or both.
- **Tumor microenvironment:** Nonmalignant and malignant cells, matrix and signals surrounding and interacting within a tumor. Sampling can alter which components are measured.
- **Amplification:** Increased genomic copy number. Transcript abundance may respond, but an RNA increase is not a copy-number assay.
- **Protein activation:** A function-related state, such as appropriate phosphorylation, localization or complex formation. More total protein does not necessarily mean greater activation.

## Mastery check

A hypothetical sample has higher PDCD1 RNA and a lower p-value than another. Can you infer the immune source cell, active killing or benefit from a checkpoint drug?

<details>
<summary>Check your answer</summary>

No. Cell localization, functional assays and clinical validation address those separate questions. The association can help formulate a study; it cannot substitute for the evidence needed to answer it.

</details>

Source context: [TCGA multi-platform profiling](https://pubmed.ncbi.nlm.nih.gov/23000897/), [Wu tumor atlas](https://pubmed.ncbi.nlm.nih.gov/34493872/) and [normal breast atlas](https://pubmed.ncbi.nlm.nih.gov/38548988/). The [evidence matrix](REFERENCES/GENE_EVIDENCE_MATRIX.md) records the abstract-only review extent for these primary readings.
