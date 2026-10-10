# Common Breast Cancer Genes: A Reader's Descriptor Guide

[Paul's Notes](../../README.md) · [Genomics companion](README.md) · [Why the dataset matters](BREAST_CANCER_TCGA_BRCA_NARRATIVE.md)

*Independent teaching glossary | Reviewed 10 October 2026 | Gene functions are introductory summaries, not a diagnostic classifier.*

## Before reading a gene name

A gene is a region of DNA. **Gene expression** generally describes the amount of RNA attributed to that gene by a given assay and workflow. A change in measured RNA is different from a DNA mutation, gene amplification, protein activity, inherited cancer risk, or clinical test result.

The following are **commonly discussed genes and molecular markers** that help students read breast cancer genomics literature. **This is not a list of genes selected by a particular private analysis**, a complete PAM50 assay, a clinically validated panel, or an assessment of any individual's cancer. Functions and associations depend on context and should be interpreted with primary evidence and verified annotation.

## Hormone response and luminal epithelial identity

| Gene | In plain language | Why it may appear in a breast cancer analysis | What it cannot establish by itself |
| --- | --- | --- | --- |
| **ESR1** | Encodes estrogen receptor alpha, a regulator of hormone-responsive gene transcription. | Helps investigate hormone-associated and luminal programs. | An ESR1 RNA count does not replace an ER immunohistochemistry (IHC) test or prove endocrine-treatment response. |
| **PGR** | Encodes the progesterone receptor, whose expression often relates to estrogen-receptor signaling. | Helps describe a hormone-regulated cell program. | RNA is not the same measurement as a clinical PR test. |
| **GATA3** | Encodes a transcription factor important in luminal epithelial differentiation. | Can help describe luminal lineage and tumor heterogeneity. | Expression does not tell us whether GATA3 has a DNA mutation or whether a tumor is clinically low-risk. |
| **FOXA1** | Encodes a pioneer transcription factor involved in the accessibility of hormone-responsive DNA regions. | Provides context for endocrine-related transcriptional networks. | One gene does not measure the complete estrogen-signaling state. |
| **KRT8** | Encodes keratin 8, a structural protein often associated with simple/luminal epithelia. | Adds context about the epithelial composition of a specimen. | Keratin transcripts do not reveal which exact cells produced the RNA. |
| **KRT18** | Encodes keratin 18, which often functions with keratin 8. | Helps interpret epithelial identity, differentiation and tissue composition. | A single structural transcript is not a tumor classifier. |

## Growth signaling, cell division, and genomic stability

| Gene | In plain language | Why it may appear in a breast cancer analysis | What it cannot establish by itself |
| --- | --- | --- | --- |
| **ERBB2 (HER2)** | Encodes a cell-surface growth-signaling receptor. | Strongly relevant to some breast cancers and HER2-related biological programs. | ERBB2 RNA expression alone is not proof of clinical HER2 positivity, amplification or drug sensitivity. |
| **EGFR** | Encodes a receptor involved in growth-factor signaling. | Supports investigation of epithelial signaling and some basal-associated programs. | RNA abundance does not demonstrate that the signaling pathway is active. |
| **MKI67** | Encodes Ki-67, a protein associated with actively cycling cells. | Commonly used to discuss proliferation-related states. | RNA does not equal the pathology Ki-67 labeling percentage. |
| **PIK3CA** | Encodes a catalytic component of PI3K signaling. | Alterations in this pathway can affect growth and survival signaling. | High/low expression does not establish a specific PIK3CA DNA mutation. |
| **TP53** | Encodes a major stress-response and tumor-suppressor protein involved in genomic integrity. | Frequently studied in breast tumor molecular profiles. | TP53 expression does not identify mutation status or functional loss. |
| **BRCA1** | Encodes a protein involved in repair of damaged DNA, including homologous recombination. | Provides context for DNA-repair biology and inherited predisposition research. | A tumor's BRCA1 RNA value is not a germline test and cannot diagnose an inherited BRCA1 variant. |
| **BRCA2** | Encodes a DNA-repair protein central to homologous recombination. | Helps explain DNA repair as a biological and therapeutic research topic. | Expression alone cannot determine hereditary risk or a tumor's homologous-recombination deficiency. |

## Basal differentiation and epithelial structure

| Gene | In plain language | Why it may appear in a breast cancer analysis | What it cannot establish by itself |
| --- | --- | --- | --- |
| **FOXC1** | Encodes a transcription factor linked in research to basal-like programs. | An example of a gene whose expression may vary among molecular groups. | FOXC1 cannot by itself identify basal-like or triple-negative breast cancer. |
| **KRT5** | Encodes keratin 5, a basal epithelial structural protein. | Often used to investigate basal cell differentiation. | One marker does not prove the identity of the tumor cells within a bulk tissue sample. |
| **KRT14** | Encodes keratin 14, another basal epithelial cytoskeletal component. | Offers context for cellular differentiation and tissue mixtures. | It cannot independently establish cancer aggressiveness or subtype. |
| **KRT17** | Encodes keratin 17, an epithelial structural component found in several biological contexts. | Sometimes informative in basal-associated or altered differentiation patterns. | Expression is not unique to one subtype or to malignant cells. |

## Adhesion, tissue context, and immune interactions

| Gene | In plain language | Why it may appear in a breast cancer analysis | What it cannot establish by itself |
| --- | --- | --- | --- |
| **CDH1** | Encodes E-cadherin, important for adhesion between epithelial cells. | Relevant to the biology and pathology of some lobular breast cancers. | RNA alone does not establish E-cadherin protein loss or a particular histologic diagnosis. |
| **VIM** | Encodes vimentin, a structural protein often expressed by mesenchymal and stromal cells. | May reflect tissue composition or cellular differentiation programs. | High bulk-tissue RNA is not proof that tumor cells underwent epithelial-to-mesenchymal transition. |
| **MMP9** | Encodes a matrix-remodeling enzyme with multiple possible cellular sources. | Helps discuss extracellular matrix and microenvironment processes. | Bulk expression cannot isolate a tumor-cell mechanism or prove metastatic potential. |
| **CD274 (PD-L1)** | Encodes an immune-regulatory ligand involved in the PD-1/PD-L1 pathway. | Helps frame immune-microenvironment questions. | RNA abundance is not a clinical PD-L1 protein score or a treatment eligibility decision. |

## How to interpret a gene-expression figure

Suppose a scientific figure shows **ESR1** expression higher in one subtype than another. A careful statement is: *the samples analyzed showed a difference in ESR1 RNA abundance under the stated measurement and statistical procedure.* The figure does not automatically prove that every tumor in that subtype is ER-positive, that a person's tumor will respond to endocrine therapy, or that the gene caused the observed difference.

Questions to ask for **every** gene:

1. Is the plotted value a raw count, normalized abundance, log-transformed measurement, estimated log2 fold change, or protein assay?
2. What constitutes one independent observation: person, tumor, tissue specimen, or technical file?
3. Was the comparison made within matched patients or across unrelated groups?
4. Are the gene symbol and stable identifier correctly matched for the annotation release?
5. Could differences in immune, epithelial, stromal or other cells explain part of the measurement?
6. What does the original testing family support, and what remains exploratory or post-selection?
7. Is a primary literature source being used to describe the **general gene function**, not falsely presented as replication of this particular analysis?

### A useful three-layer interpretation

**Layer 1 — Measurement:** What was actually measured, in which specimens and on which scale?

**Layer 2 — Biological context:** What is independently known about the gene's function and cellular sources?

**Layer 3 — Research hypothesis:** What might explain this pattern and what different experiment would be required to test that explanation?

Only layer 1 is a direct statement about the given data. Layer 2 relies on literature. Layer 3 is a proposal, not a validated mechanism.

## Molecular versus clinical classifications

Expression-derived subtypes such as Luminal A, Luminal B, HER2-enriched and Basal-like are based on multigene patterns and a particular classifier. Clinicians may use ER, PR, HER2 and Ki-67 tests to characterize disease, but **a multigene subtype label and a clinical biomarker category are not identical measurements**.

Similarly, a comparison of a tumor to *adjacent normal* tissue is not the same as comparing a patient to a cancer-free control group. Both the definition of the comparator and the mix of cells within each specimen affect interpretation.

## Annotation reference records

All 21 symbols below were confirmed as approved in HGNC on **10 October 2026**. The NCBI records link to gene-specific biology and literature; annotation is a reference snapshot, not validation of a result in an individual specimen. HER2 and PD-L1 are common protein names; the approved gene symbols are ERBB2 and CD274.

| Symbol | HGNC record | NCBI Gene |
| --- | --- | --- |
| ESR1 | [HGNC:3467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3467) | [2099](https://www.ncbi.nlm.nih.gov/gene/2099) |
| PGR | [HGNC:8910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8910) | [5241](https://www.ncbi.nlm.nih.gov/gene/5241) |
| GATA3 | [HGNC:4172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4172) | [2625](https://www.ncbi.nlm.nih.gov/gene/2625) |
| FOXA1 | [HGNC:5021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5021) | [3169](https://www.ncbi.nlm.nih.gov/gene/3169) |
| KRT8 | [HGNC:6446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6446) | [3856](https://www.ncbi.nlm.nih.gov/gene/3856) |
| KRT18 | [HGNC:6430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6430) | [3875](https://www.ncbi.nlm.nih.gov/gene/3875) |
| ERBB2 | [HGNC:3430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3430) | [2064](https://www.ncbi.nlm.nih.gov/gene/2064) |
| EGFR | [HGNC:3236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3236) | [1956](https://www.ncbi.nlm.nih.gov/gene/1956) |
| MKI67 | [HGNC:7107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7107) | [4288](https://www.ncbi.nlm.nih.gov/gene/4288) |
| PIK3CA | [HGNC:8975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8975) | [5290](https://www.ncbi.nlm.nih.gov/gene/5290) |
| TP53 | [HGNC:11998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11998) | [7157](https://www.ncbi.nlm.nih.gov/gene/7157) |
| BRCA1 | [HGNC:1100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1100) | [672](https://www.ncbi.nlm.nih.gov/gene/672) |
| BRCA2 | [HGNC:1101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1101) | [675](https://www.ncbi.nlm.nih.gov/gene/675) |
| FOXC1 | [HGNC:3800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3800) | [2296](https://www.ncbi.nlm.nih.gov/gene/2296) |
| KRT5 | [HGNC:6442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6442) | [3852](https://www.ncbi.nlm.nih.gov/gene/3852) |
| KRT14 | [HGNC:6416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6416) | [3861](https://www.ncbi.nlm.nih.gov/gene/3861) |
| KRT17 | [HGNC:6427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6427) | [3872](https://www.ncbi.nlm.nih.gov/gene/3872) |
| CDH1 | [HGNC:1748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1748) | [999](https://www.ncbi.nlm.nih.gov/gene/999) |
| VIM | [HGNC:12692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12692) | [7431](https://www.ncbi.nlm.nih.gov/gene/7431) |
| MMP9 | [HGNC:7176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7176) | [4318](https://www.ncbi.nlm.nih.gov/gene/4318) |
| CD274 | [HGNC:17635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17635) | [29126](https://www.ncbi.nlm.nih.gov/gene/29126) |

## Primary learning references

- [Hurtado et al. (2011), FOXA1 and estrogen-receptor function](https://www.nature.com/articles/ng.730) — experimental context for chromatin accessibility and hormone-responsive transcription.
- [Ray et al. (2010), FOXC1 in basal-like breast cancer](https://pubmed.ncbi.nlm.nih.gov/20406990/) — research association and functional experiments, not a single-gene clinical classifier.

- [NCI: Breast cancer biomarker tests](https://www.cancer.gov/types/breast/diagnosis/breast-cancer-biomarker-tests) — ER, PR, HER2 and Ki-67 measurements and clinical context.
- [TCGA Network (2012), Comprehensive molecular portraits of human breast tumours](https://www.nature.com/articles/nature11412) — molecular heterogeneity, PIK3CA, TP53, GATA3 and subtype programs.
- [NCI Genomic Data Commons: TCGA-BRCA](https://portal.gdc.cancer.gov/projects/TCGA-BRCA) — specimen-level research context and data access.
- [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) — primary gene-specific identifiers, official descriptions and linked references; confirm current records before adopting annotation changes.
- [HGNC](https://www.genenames.org/) — approved human gene symbols and naming changes.
- [Ensembl](https://www.ensembl.org/) — stable gene annotations and reference-release tracking.
- [Reactome](https://reactome.org/) — curated pathway descriptions; pathway membership is not causal proof.

This glossary is an original educational synthesis of general gene biology. It does not reproduce protected teaching content or original patient-level data. For the broader human and methodological context, continue with [Before the Heatmap](BREAST_CANCER_TCGA_BRCA_NARRATIVE.md).
