# Gene biology learning guide

[Companion](BREAST_CANCER_60_GENE_COMPANION.md) · [Index](GENE_ATLAS_INDEX.md) · [Measurement and glossary](GENE_EXPRESSION_INTERPRETATION.md)

## Choose a route

- **Beginner:** Read [the people behind the data](BREAST_CANCER_TCGA_BRCA_NARRATIVE.md), then [DNA to protein](FIGURES/README.md#dna-to-protein), the [measurement guide](GENE_EXPRESSION_INTERPRETATION.md), and the ESR1, KRT8 and CD8A cards. Finish with the synthetic heatmap. Goal: explain what was measured before interpreting a value.
- **Biological:** Work through hormone, growth, proliferation, repair, basal and immune domains below. Use the [pathway overview](GENE_PATHWAY_OVERVIEW.md) to connect processes. Goal: distinguish normal function, altered regulation and cell composition.
- **Research:** Start with the [annotation register](REFERENCES/ANNOTATION_SOURCE_REGISTER.md) and [selection rubric](REFERENCES/SELECTION_RUBRIC.md), then measurement, study design, multiple testing and the [evidence matrix](REFERENCES/GENE_EVIDENCE_MATRIX.md). Compare MALAT1 and PTEN evidence. Goal: formulate a narrow claim and identify the experiment needed to test it.

All worked examples are conceptual or invented. They describe no real participant. The biological framework uses the linked genes’ authoritative normal-function records; specific cancer findings retain the review boundaries on each card.

<a id="hormone"></a>

## Hormone signaling

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Hormones coordinate tissue responses by binding receptors and changing transcription. ESR1 and PGR encode receptors; FOXA1 helps determine which chromatin regions a receptor can access.

**Cancer and measurement:** A tumor may retain hormone-responsive differentiation while acquiring additional growth or resistance mechanisms. Receptor presence does not guarantee every downstream response. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [ESR1](GENE_CARDS/ESR1.md) · [FOXA1](GENE_CARDS/FOXA1.md) · [GATA3](GENE_CARDS/GATA3.md) · [KRT18](GENE_CARDS/KRT18.md) · [KRT8](GENE_CARDS/KRT8.md) · [PGR](GENE_CARDS/PGR.md)

**Worked conceptual example:** Imagine two invented epithelial cultures with equal ESR1 RNA but different receptor binding after hormone exposure. Binding and transcription assays distinguish a functional response from receptor abundance.

**Interpretation questions / mastery check:** Would equal receptor RNA imply equal receptor activity? What information does a pathology protein assay add?

<details>
<summary>Check your reasoning</summary>

No: ligand, chromatin, variants and other regulators matter. Protein testing adds a different measurement with its own validated interpretation.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="growth"></a>

## Growth-factor signaling

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Membrane receptors transmit information about the environment through intracellular enzymes. HER-family receptors and PI3K/AKT/mTOR signaling help coordinate growth and nutrient responses.

**Cancer and measurement:** Amplification, activating variants, inhibitory-protein loss or altered partners can change signaling. These alternatives cannot be identified from one RNA value. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [AKT1](GENE_CARDS/AKT1.md) · [CCND1](GENE_CARDS/CCND1.md) · [CDK4](GENE_CARDS/CDK4.md) · [CDK6](GENE_CARDS/CDK6.md) · [EGFR](GENE_CARDS/EGFR.md) · [ERBB2](GENE_CARDS/ERBB2.md) · [ERBB3](GENE_CARDS/ERBB3.md) · [ERBB4](GENE_CARDS/ERBB4.md) · [FGFR1](GENE_CARDS/FGFR1.md) · [MTOR](GENE_CARDS/MTOR.md) · [PIK3CA](GENE_CARDS/PIK3CA.md) · [PTEN](GENE_CARDS/PTEN.md)

**Worked conceptual example:** Imagine equal ERBB2 transcript abundance in two cultures, but increased phosphorylated receptor in one. Compare total protein with phosphoprotein after a controlled ligand pulse.

**Interpretation questions / mastery check:** Which measurement addresses abundance, and which addresses activation? Does a shared pathway imply a direct physical interaction?

<details>
<summary>Check your reasoning</summary>

Total protein addresses abundance; phosphorylation provides activation-related information in context. Pathway membership alone is not a binding experiment.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="proliferation"></a>

## Proliferation

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Cells duplicate DNA and separate chromosomes through ordered cell-cycle phases. Cyclins, kinases and mitotic regulators control timing; MKI67 is associated with cycling cells.

**Cancer and measurement:** A tissue can have more cycling cells or a different distribution of cell-cycle stages. Both change bulk proliferation-associated RNA without identifying a single initiating defect. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [AURKA](GENE_CARDS/AURKA.md) · [CCNB1](GENE_CARDS/CCNB1.md) · [CCND1](GENE_CARDS/CCND1.md) · [CCNE1](GENE_CARDS/CCNE1.md) · [CDC20](GENE_CARDS/CDC20.md) · [CDK4](GENE_CARDS/CDK4.md) · [CDK6](GENE_CARDS/CDK6.md) · [CDKN1A](GENE_CARDS/CDKN1A.md) · [MKI67](GENE_CARDS/MKI67.md) · [RB1](GENE_CARDS/RB1.md) · [TOP2A](GENE_CARDS/TOP2A.md)

**Worked conceptual example:** Invent a sample containing 10 cycling cells among 100 and another containing 30 among 100. Higher cycling-cell marker RNA could arise without any change within a cycling cell.

**Interpretation questions / mastery check:** Does a threefold marker increase prove each cell divides three times faster? How could microscopy help?

<details>
<summary>Check your reasoning</summary>

No. Cell counts, labeling and stage-specific assays help separate cell fraction from cell behavior.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="repair"></a>

## DNA repair

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Cells detect damage and repair DNA to preserve information across divisions. ATM and CHEK2 participate in damage responses; BRCA1, BRCA2, PALB2 and RAD51 contribute to homologous-recombination biology.

**Cancer and measurement:** A pathogenic variant or impaired protein regulation can alter repair. A transcript can remain abundant while the encoded protein is defective. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [ATM](GENE_CARDS/ATM.md) · [BARD1](GENE_CARDS/BARD1.md) · [BRCA1](GENE_CARDS/BRCA1.md) · [BRCA2](GENE_CARDS/BRCA2.md) · [CHEK2](GENE_CARDS/CHEK2.md) · [PALB2](GENE_CARDS/PALB2.md) · [RAD51](GENE_CARDS/RAD51.md) · [TOP2A](GENE_CARDS/TOP2A.md) · [TP53](GENE_CARDS/TP53.md)

**Worked conceptual example:** Imagine a repair gene with unchanged RNA but a damaging DNA variant. Sequence analysis addresses the variant; a suitable functional assay addresses repair performance.

**Interpretation questions / mastery check:** Can RNA exclude a germline variant? Is a variant of uncertain significance equivalent to a pathogenic variant?

<details>
<summary>Check your reasoning</summary>

No to both. Inherited-variant classification requires dedicated evidence and interpretation; tumor RNA is a different assay.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="suppression"></a>

## Tumor suppression

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Checkpoints, signaling brakes and controlled cell death restrain inappropriate expansion. TP53, RB1 and PTEN affect different control systems; BAX and BCL2 influence survival decisions.

**Cancer and measurement:** Control can fail through DNA changes, protein loss or altered regulation. A stress-induced checkpoint transcript can also accompany cell survival rather than permanent arrest. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [ATM](GENE_CARDS/ATM.md) · [BARD1](GENE_CARDS/BARD1.md) · [BAX](GENE_CARDS/BAX.md) · [BCL2](GENE_CARDS/BCL2.md) · [BRCA1](GENE_CARDS/BRCA1.md) · [BRCA2](GENE_CARDS/BRCA2.md) · [CDH1](GENE_CARDS/CDH1.md) · [CDKN1A](GENE_CARDS/CDKN1A.md) · [CHEK2](GENE_CARDS/CHEK2.md) · [PALB2](GENE_CARDS/PALB2.md) · [PTEN](GENE_CARDS/PTEN.md) · [RB1](GENE_CARDS/RB1.md) · [TP53](GENE_CARDS/TP53.md)

**Worked conceptual example:** Imagine high CDKN1A RNA after oxidative injury. Follow recovery, protein abundance and cell-cycle state before concluding that growth stopped irreversibly.

**Interpretation questions / mastery check:** Does expression of a suppressor prove its protein works? Can a survival phenotype depend on exposure and timing?

<details>
<summary>Check your reasoning</summary>

Expression does not prove function. Exposure, timing and cell state can change the interpretation of the same gene.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="basal"></a>

## Basal epithelial biology

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Epithelial layers use keratin networks and differentiation programs to maintain structure. Basal-associated and luminal-associated keratins describe cell states rather than exclusive identities.

**Cancer and measurement:** Tumors and experimental epithelial cultures can mix differentiation states. Basal-like is a molecular expression classification; basal cells are a tissue compartment. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [EGFR](GENE_CARDS/EGFR.md) · [FOXC1](GENE_CARDS/FOXC1.md) · [ITGA6](GENE_CARDS/ITGA6.md) · [KRT14](GENE_CARDS/KRT14.md) · [KRT17](GENE_CARDS/KRT17.md) · [KRT5](GENE_CARDS/KRT5.md)

**Worked conceptual example:** Imagine a spatial spot containing basal cells beside luminal tumor cells. KRT5 and KRT8 signals can coexist because the measurement combines cells.

**Interpretation questions / mastery check:** Does KRT5 alone assign basal-like disease? Is basal-like identical to triple-negative?

<details>
<summary>Check your reasoning</summary>

No. Multi-gene classification and clinical protein categories overlap incompletely, and spatial composition adds another source of variation.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="adhesion"></a>

## Cell adhesion

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Cells attach to neighboring cells and extracellular surroundings to organize tissues. CDH1 supports epithelial junctions, EPCAM participates in epithelial organization and ITGA6 contributes to matrix attachment.

**Cancer and measurement:** Altered adhesion can change architecture or migration, but expression differences can also reflect the number of epithelial cells sampled. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [CDH1](GENE_CARDS/CDH1.md) · [EPCAM](GENE_CARDS/EPCAM.md) · [FN1](GENE_CARDS/FN1.md) · [ITGA6](GENE_CARDS/ITGA6.md) · [KRT18](GENE_CARDS/KRT18.md) · [KRT19](GENE_CARDS/KRT19.md) · [KRT8](GENE_CARDS/KRT8.md) · [VIM](GENE_CARDS/VIM.md)

**Worked conceptual example:** Imagine lower CDH1 RNA in a sample with fewer epithelial cells but intact junctions in the remaining cells. Compare cell localization and protein staining before inferring junction loss.

**Interpretation questions / mastery check:** Does low bulk RNA diagnose lobular histology? What does membrane localization add?

<details>
<summary>Check your reasoning</summary>

No. Histopathology and localization address tissue architecture and functional placement that an RNA total cannot resolve.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="matrix"></a>

## Invasion and extracellular matrix

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Collagen, fibronectin and remodeling enzymes help tissues maintain and reshape their surroundings. Fibroblasts and other stromal cells contribute much of this extracellular framework.

**Cancer and measurement:** Matrix remodeling can accompany invasion, wound repair or changing stromal content. MMP9 protein must be appropriately activated to act as an enzyme. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [COL1A1](GENE_CARDS/COL1A1.md) · [CXCL12](GENE_CARDS/CXCL12.md) · [FN1](GENE_CARDS/FN1.md) · [MMP9](GENE_CARDS/MMP9.md) · [VIM](GENE_CARDS/VIM.md)

**Worked conceptual example:** Imagine equal collagen production per fibroblast but twice as many fibroblasts in one specimen. Bulk COL1A1 RNA increases without a per-cell regulatory change.

**Interpretation questions / mastery check:** Can collagen RNA identify the producing cell? Does MMP9 RNA establish active proteolysis?

<details>
<summary>Check your reasoning</summary>

No. Spatial or cell-resolved assays help identify sources; protein processing and activity assays address proteolysis.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="immune"></a>

## Immune microenvironment

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Immune cells recognize signals, communicate through cytokines and regulate responses. CD3D, CD8A, CD68 and PTPRC help characterize immune populations; PDCD1 and CD274 participate in checkpoint biology.

**Cancer and measurement:** A tumor can change immune-cell abundance, location or state. A bulk checkpoint signal may come from immune cells, tumor cells or both. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [CD274](GENE_CARDS/CD274.md) · [CD3D](GENE_CARDS/CD3D.md) · [CD68](GENE_CARDS/CD68.md) · [CD8A](GENE_CARDS/CD8A.md) · [CXCL12](GENE_CARDS/CXCL12.md) · [MMP9](GENE_CARDS/MMP9.md) · [PDCD1](GENE_CARDS/PDCD1.md) · [PTPRC](GENE_CARDS/PTPRC.md) · [STAT1](GENE_CARDS/STAT1.md)

**Worked conceptual example:** Imagine increased CD8A RNA with unchanged RNA per T cell. More T cells alone could explain the result; their location and functional state still require measurement.

**Interpretation questions / mastery check:** Does a marker prove effective killing? Does PDCD1 RNA establish eligibility for a checkpoint drug?

<details>
<summary>Check your reasoning</summary>

No. Marker abundance, functional evidence and clinically validated selection criteria address different questions.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="metabolism"></a>

## Metabolism and stress

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Cells regulate nutrient uptake, energy use and responses to low oxygen or protein-folding stress. SLC2A1 transports glucose; HIF1A and XBP1 connect stress sensing to transcription.

**Cancer and measurement:** Cancer cells may adapt to environmental stress, but nonmalignant cells in the same tissue also respond. Protein stability and RNA splicing can change activity without a corresponding gene-level RNA change. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [AKT1](GENE_CARDS/AKT1.md) · [HIF1A](GENE_CARDS/HIF1A.md) · [MTOR](GENE_CARDS/MTOR.md) · [PIK3CA](GENE_CARDS/PIK3CA.md) · [SLC2A1](GENE_CARDS/SLC2A1.md) · [XBP1](GENE_CARDS/XBP1.md)

**Worked conceptual example:** Imagine unchanged total XBP1 RNA with a changed fraction of the spliced transcript. An isoform assay reveals a difference hidden by the gene total.

**Interpretation questions / mastery check:** Does transporter RNA measure glucose flux? Does HIF1A RNA directly measure oxygen tension?

<details>
<summary>Check your reasoning</summary>

No. Flux, oxygen measurements, protein regulation and isoforms provide complementary information.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="transcription"></a>

## Transcriptional regulation

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Transcription factors and chromatin context coordinate when genes are read. GATA3, FOXA1, FOXC1, STAT1 and stress-responsive regulators influence different programs.

**Cancer and measurement:** A regulatory network may change through binding, accessibility or cofactors. Correlated RNA values are a useful hypothesis but do not demonstrate a direct regulatory edge. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [ESR1](GENE_CARDS/ESR1.md) · [FOXA1](GENE_CARDS/FOXA1.md) · [FOXC1](GENE_CARDS/FOXC1.md) · [GATA3](GENE_CARDS/GATA3.md) · [HIF1A](GENE_CARDS/HIF1A.md) · [MALAT1](GENE_CARDS/MALAT1.md) · [PGR](GENE_CARDS/PGR.md) · [STAT1](GENE_CARDS/STAT1.md) · [TP53](GENE_CARDS/TP53.md) · [XBP1](GENE_CARDS/XBP1.md)

**Worked conceptual example:** Imagine FOXA1 and ESR1 RNA rising together. Perturb one regulator and measure binding plus transcription to distinguish shared cell identity from direct dependence.

**Interpretation questions / mastery check:** Does correlation prove binding? What controls would strengthen a perturbation experiment?

<details>
<summary>Check your reasoning</summary>

No. Appropriate controls, dose, timing, rescue and orthogonal binding assays help distinguish direct and indirect effects.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.

<a id="emerging"></a>

## Other emerging biology

**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.

**Normal function:** Noncoding transcripts and context-dependent regulators can affect cellular organization without encoding a protein. MALAT1 is a long noncoding RNA with model-dependent research findings.

**Cancer and measurement:** Different interventions, neighboring-gene effects and disease stages can produce apparently contradictory outcomes. A useful teaching catalog keeps disagreement visible. Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.

**Selected genes:** [MALAT1](GENE_CARDS/MALAT1.md)

**Worked conceptual example:** Compare the 2016, 2018 and 2024 MALAT1 studies. Make separate columns for intervention, model, metastatic stage and direction of effect before drawing a conclusion.

**Interpretation questions / mastery check:** Must one contrary study be wrong? Would more RNA alone reveal the mechanism?

<details>
<summary>Check your reasoning</summary>

Neither follows. Contradictions can reflect design differences, and mechanism requires evidence beyond abundance.

</details>

**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.
