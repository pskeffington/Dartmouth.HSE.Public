# Before the Heatmap: The People Behind Breast Cancer Data

[Paul's Notes](../../README.md) · [Genomics companion](README.md) · [Common gene descriptors](COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md)

*An independently written, public learning narrative | Reviewed 10 October 2026 | Population figures refer to 2024 estimates.*

Continue from people and specimens to biological questions in the [60-Gene Breast Cancer Research Companion](BREAST_CANCER_60_GENE_COMPANION.md).

## Why begin with people rather than a spreadsheet?

A breast cancer diagnosis begins long before a row appears in a research table. Someone may notice a change, receive a screening result, wait for imaging or a biopsy, and face decisions about surgery, medicines, work, family, and daily life. The experience varies enormously. No one person's course should be assumed from a tumor's molecular measurements.

Researchers often speak about *cases*, *samples*, and *gene counts*. Those are necessary scientific terms, but a **case is a person**, a *sample* is material obtained during care or research, and a gene-expression measurement is one narrow observation from that material. The person is much more than the measurement.

The reason for analyzing breast cancer data is not to discover an impressive-looking heatmap. It is to learn why tumors that share an anatomical diagnosis can behave differently, how their molecular patterns may inform future questions, and which findings could eventually support more equitable and effective care. A research result is only one step on that path; it is not a diagnosis or a treatment recommendation.

## The worldwide scale — and what the numbers mean

The most recent IARC GLOBOCAN global burden release available when this guide was reviewed estimated the following for **2024**:

| Measure | Global estimate | What is being counted |
| --- | ---: | --- |
| New breast cancer diagnoses among women | **About 2.4 million** (2,434,087) | *Incidence*: new diagnoses during 2024, not everyone living with a past diagnosis |
| Deaths attributed to breast cancer among women | **About 694,000** (693,660) | *Mortality*: deaths during 2024; not the number of people who were diagnosed that year and then died |
| Five-year prevalence of breast cancer, both sexes | **About 8.16 million** (8,162,335) | People alive in 2024 who had been diagnosed within approximately the preceding five years; not an all-time count of everyone living after breast cancer |

Sources (accessed 10 October 2026): [IARC female breast incidence table](https://gco.iarc.who.int/today/en/dataviz/tables?cancers=20&mode=population&sexes=2&types=0), [IARC female breast mortality table](https://gco.iarc.who.int/today/en/dataviz/tables?cancers=20&mode=population&sexes=2&types=1), [IARC/ACS GLOBOCAN 2024](https://www.iarc.who.int/news-events/global-cancer-statistics-2024-globocan-estimates-of-incidence-and-mortality-worldwide-for-34-cancers-in-186-countries), [2024 global statistics paper](https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/caac.70090), and [IARC Cancer Today five-year prevalence table](https://gco.iarc.who.int/today/en/dataviz/tables-prevalence?cancers=20&mode=population&types=2). These are modeled population estimates, not a live register of known individuals. The incidence and death counts above describe women; the prevalence table describes both sexes, so their denominators are not identical. The WHO notes that breast cancer also occurs in men, who account for a small minority of cases. [WHO fact sheet, July 2026](https://www.who.int/news-room/fact-sheets/detail/breast-cancer).

**How many people worldwide are living with breast cancer?** The estimated **8.16 million five-year prevalent cases** offer a meaningful, consistently defined measure. They do **not** include everyone diagnosed more than five years earlier who remains alive, so this figure must not be presented as the total number of all breast cancer survivors worldwide. Nor should the annual new-diagnosis count be presented as that total.

Breast cancer occurs across countries and communities, but the likelihood of early detection, access to diagnostic services, timely treatment, and survival is not evenly distributed. Population figures are a reminder that the need for understandable evidence is global; a genomic cohort from selected treatment institutions cannot stand in for every affected community. [WHO breast cancer overview](https://www.who.int/news-room/fact-sheets/detail/breast-cancer); [WHO global breast cancer survival overview](https://www.who.int/data/gho/data/themes/breast-cancer-survival/).

## From one person's tissue to a research dataset

A simplified path from care to analysis looks like this:

1. **A person receives clinical care.** A tissue specimen may be obtained through biopsy or surgery. Consent, ethical oversight, and data-access conditions determine whether and how material can be used for research.
2. **A laboratory characterizes a specimen.** Researchers can measure RNA molecules, DNA changes, proteins, or other biological features. Different assays answer different questions.
3. **A specimen receives research identifiers.** A case, a tissue sample, and an individual sequencing file are not interchangeable units. One case can contribute multiple samples, and one sample can have multiple files.
4. **A data table is assembled.** Columns may correspond to samples; rows may correspond to genes; entries are assay-dependent measurements. A separate metadata table records relevant, permitted descriptors.
5. **Researchers check whether comparisons are valid.** Tissue origin, subject identity, assay scale, quality control, missingness, and biological grouping determine what may responsibly be compared.
6. **Only then do statistical models and visualizations begin.** The final scientific claim must be narrower than or equal to what the study design and evidence support.

The Cancer Genome Atlas (TCGA) was a large research effort that characterized thousands of tumors with multiple technologies. Its breast invasive carcinoma project is commonly called **TCGA-BRCA**. The [NCI Genomic Data Commons TCGA-BRCA project page](https://portal.gdc.cancer.gov/projects/TCGA-BRCA) listed **1,098 cases** in the live project API snapshot accessed **10 October 2026** ([GDC project summary API](https://api.gdc.cancer.gov/projects/TCGA-BRCA?expand=summary)). That is a **project-level case count**, not 1,098 matched tumor–normal pairs, 1,098 RNA-expression values, or a representative census of everyone with breast cancer. GDC counts and available files can change as its holdings are updated. See [NCI: using TCGA data](https://www.cancer.gov/ccg/research/genome-sequencing/tcga/using-tcga-data).

**Important source boundary:** This page discusses public dataset concepts and published project-level figures. It does not distribute any patient-level TCGA records, classroom-source datasets, private research sample tables, or unreviewed results. Some GDC data require controlled authorization.

## What does an RNA-expression measurement actually tell us?

DNA contains genes; cells use selected genes to produce RNA, and many RNAs are involved in making proteins. **RNA sequencing (RNA-seq)** estimates the abundance of RNA transcripts in a specimen. This tells us something about the biological activity of a mixed tissue at a particular collection time.

But **more RNA is not automatically more protein**, and neither is automatically greater biological activity. A tumor sample may contain cancer cells alongside immune cells, stromal cells, blood vessels, and residual normal tissue. A change in a measured gene can reflect tumor-cell activity, differences in cellular composition, or both.

A useful beginner's data dictionary:

| Term | Working meaning | Common mistake to avoid |
| --- | --- | --- |
| Case / participant | A person represented in the study | Treating multiple files from one person as independent people |
| Tumor specimen | Tissue containing tumor obtained from a particular person | Assuming every tumor sample has the same cell composition |
| Solid tissue normal | A non-tumor tissue sample, often adjacent to the tumor | Calling it a healthy, cancer-free person's breast tissue |
| Matched tumor–normal pair | Two appropriate specimens linked to the same person | Pairing tissues by row order, similar filenames, or unrelated individuals |
| Gene identifier | A stable reference to a gene, such as an Ensembl ID | Assuming a familiar gene symbol is a permanent, unique join key |
| RNA-seq counts | Sequencing-derived measurements subject to library-size and other considerations | Feeding TPM or log-transformed expression into a raw-count model |
| log2 fold change | An estimated expression difference on a log2 scale | Treating it as the observed experience or prognosis of an individual patient |
| PAM50 / intrinsic subtype | A molecular classification based on an expression pattern and a defined classifier | Treating a subtype name as the same thing as a single receptor test |

### Why compare tissue from the same person?

A paired tumor-versus-normal analysis asks whether measured expression tends to differ **within individuals**, rather than simply comparing unrelated groups of people. Matching can account for some person-level differences, but the analysis still depends on correct sample linkage, specimen quality, appropriate modeling, and sufficiently informative cases.

**Adjacent normal tissue is a comparator, not a perfect control.** Histologically nonmalignant tissue close to a tumor may still reflect local inflammation, tissue composition, hormonal context, or a field effect. Comparing it with tumor tissue does not automatically identify a cancer-cell-specific molecular mechanism.

The public TCGA-BRCA resource contains more cases than any particular restricted analysis subset. Actual usable pair counts depend on exact sample identifiers, assay availability, inclusion criteria, and the research question. The public teaching narrative does not publish or imply the private study's patient-level pair map.

## Why are there several breast cancer subtypes?

Breast cancer is not one uniform molecular condition. A seminal TCGA study showed substantial differences among expression-defined biological groups and across molecular platforms. [TCGA Network, *Comprehensive molecular portraits of human breast tumours* (2012)](https://www.nature.com/articles/nature11412).

| Molecular group | Broad introductory interpretation | Caution |
| --- | --- | --- |
| **Luminal A** | Commonly reflects a hormone-receptor-associated, luminal epithelial expression program | Do not infer stage, outcome, or treatment from an RNA label alone |
| **Luminal B** | Often retains luminal features alongside stronger proliferative signals | A luminal label does not supply a person's individual prognosis |
| **HER2-enriched** | Represents an expression pattern often associated with ERBB2/HER2-related signaling | Expression-defined HER2-enriched is **not identical** to clinically measured HER2-positive status |
| **Basal-like** | Often includes basal epithelial programs and overlaps with many triple-negative cancers | Basal-like and triple-negative are overlapping, **not interchangeable**, classifications |

Clinical tests often examine **estrogen receptor (ER), progesterone receptor (PR), HER2 protein, and Ki-67**. Those clinical biomarker measurements should not be substituted for molecular subtype calls. [NCI breast cancer biomarker guide](https://www.cancer.gov/types/breast/diagnosis/breast-cancer-biomarker-tests).

## Common gene names: the vocabulary behind the patterns

Genes in breast cancer research are not interchangeable labels. A few examples illustrate different biological questions:

- **ESR1 and PGR:** Can suggest hormone-receptor-related expression programs, but RNA abundance is not a clinical receptor assay.
- **ERBB2:** Encodes HER2, a receptor involved in growth signaling; RNA abundance is not proof of HER2 protein overexpression or gene amplification.
- **MKI67:** Tracks a proliferation-associated transcript; an RNA value is not a pathology Ki-67 percentage.
- **GATA3 and FOXA1:** Help organize luminal epithelial and hormone-responsive gene programs.
- **FOXC1 and KRT5:** Can inform investigation of basal-like differentiation, without individually classifying a tumor.
- **BRCA1, BRCA2, TP53, and PIK3CA:** Are commonly discussed in DNA repair, cell-cycle control, or signaling. Their RNA measurements do not establish an inherited variant or a particular somatic mutation.

Read the [full common-gene descriptor guide](COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md) before assigning meaning to a heatmap row. These examples are a teaching glossary, **not a clinical test panel or an independently validated disease signature**.

## Reading a heatmap without losing sight of the person

Imagine a heatmap cell shaded to indicate that a gene's RNA measurement is higher in a tumor specimen than in an appropriate comparator. The color may summarize a carefully processed measurement or a model estimate; it does **not** display pain, uncertainty, family responsibilities, ability to access treatment, or what happened after the sample was collected. Two people with visually similar molecular measurements may have very different diagnoses, treatment options, outcomes, and circumstances. Conversely, two tumors diagnosed under the same clinical name can have quite different molecular patterns.

A good caption therefore begins with *who and what was actually measured*, makes the tissue comparator and units explicit, and states the limits of interpretation. Respect for participants shows up in technical choices too: correct pairing, controlled access, privacy protection, honest missing-data reporting, and refusing to exaggerate a statistical result.

## The questions our analysis is trying to teach us to ask

Instead of starting with "Which gene is significant?", a thoughtful analysis starts with more careful questions:

- **Who was measured?** How many distinct participants are represented, and how were specimens obtained?
- **What was measured?** RNA counts, transformed abundance, DNA alterations, protein status, or something else?
- **Compared with what?** Another specimen from the same person, tumor tissue from someone else, or a separate reference cohort?
- **Does a result differ by subtype?** If so, are the subtype definitions, sample sizes, and statistical contrasts defensible?
- **How certain are we?** What do the variance method, sample size, multiple testing, and potential selection effects allow us to say?
- **What could explain the pattern?** A tumor-cell program, tissue composition, collection practices, or several influences at once?
- **Will this finding matter outside this dataset?** Independent replication, clinical measurement and patient outcomes require separate evidence.

The ethical conclusion is as important as the statistical one: **a plot represents measurements from people who contributed to research, not a substitute for their stories or a prediction about their lives**.

## A practical reading sequence

1. Learn the distinctions among people, cases, tissue samples, and gene measurements.
2. Open the [common gene descriptor guide](COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md).
3. Review [public gene-expression visualization examples](../VISUALIZATION_GALLERY.md), which use independently simulated data, not identifiable patient records.
4. For every real analysis, locate its dataset provenance, inclusion criteria, model definition, and permissions before interpreting a figure.
5. Write a results paragraph that says what was measured, among whom, and what the data **cannot** establish.

## Sources and attribution

- [WHO, Breast cancer fact sheet](https://www.who.int/news-room/fact-sheets/detail/breast-cancer) (3 July 2026): burden, clinical overview and access-to-care context.
- [IARC, GLOBOCAN 2024 international release](https://www.iarc.who.int/news-events/global-cancer-statistics-2024-globocan-estimates-of-incidence-and-mortality-worldwide-for-34-cancers-in-186-countries) (8 July 2026): 2024 modeled incidence and mortality.
- [Sung et al., Global cancer statistics 2024](https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/caac.70090) (2026): primary statistical report.
- [IARC Cancer Today, 2024 five-year prevalence](https://gco.iarc.who.int/today/en/dataviz/tables-prevalence?cancers=20&mode=population&types=2): 8,162,335 prevalent cases, both sexes, five-year duration.
- [WHO Global Health Observatory, breast cancer survival](https://www.who.int/data/gho/data/themes/breast-cancer-survival/): global equity and five-year survival context.
- [NCI Genomic Data Commons, TCGA-BRCA](https://portal.gdc.cancer.gov/projects/TCGA-BRCA): live project-level case/data categories and access restrictions.
- [NCI, Using TCGA data](https://www.cancer.gov/ccg/research/genome-sequencing/tcga/using-tcga-data): specimen and clinical-data workflow.
- [TCGA Network, Comprehensive molecular portraits](https://www.nature.com/articles/nature11412) (2012): molecular heterogeneity and subtype foundations.
- [NCI, Breast cancer biomarkers](https://www.cancer.gov/types/breast/diagnosis/breast-cancer-biomarker-tests): clinical ER, PR, HER2 and Ki-67 distinctions.

This independent educational commentary cites external concepts and project-level statistics; no source language, original study tables, restricted patient records, or institutional materials are reproduced. It is not medical advice or a description of any specific patient's treatment.
