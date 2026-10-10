# Biomedical research computing — public methods and coding reference matrix

[General coding practices](README.md) · [Resources](../README.md) · [R resources](../R/README.md) · [Bash resources](../Bash/README.md)

**Reviewed:** 2026-10-10. This is an independently written, selective guide to public documentation and reporting standards. It is **not** a systematic review, a clinical practice guideline, a claim of copyright clearance, or a validation of any particular analysis. No private classroom materials or original protected research files were consulted for this document.

## Research-computing reference matrix

| ID | Primary resource | Type | Coding practice or analytical safeguard | Best educational application | Boundary / common failure |
| --- | --- | --- | --- | --- | --- |
| BIO-01 | [CDC NHANES datasets and documentation](https://wwwn.cdc.gov/nchs/nhanes/tutorials/datasets.aspx) | Federal technical guidance | Match variables to cycle-specific codebooks, component eligibility, file structure and documented missing-value conventions; verify joins and record counts | Participant-level data ingestion, metadata audit, joins | Variable meaning and availability can change by cycle; do not guess from column names |
| BIO-02 | [CDC NHANES sample design](https://wwwn.cdc.gov/nchs/nhanes/tutorials/SampleDesign.aspx) | Federal survey methodology | Specify strata, primary sampling units and weights for population inference | Survey design before modeling | Treating a complex sample as an unweighted simple random sample can distort precision and estimates |
| BIO-03 | [CDC NHANES weighting](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx) | Federal survey methodology | Select weights according to the smallest analytic subsample and the relevant collection component; handle combined cycles explicitly | Survey-weighted descriptive analysis | Interview weights are not interchangeable with exam or laboratory subsample weights |
| BIO-04 | [R survey package documentation](https://cran.r-project.org/package=survey) | Statistical software reference | Represent complex designs explicitly, then use survey-aware estimators rather than ordinary unweighted standard errors | Weighted population estimates | Inspect current version and variance-design assumptions; this does not validate questionnaire coding |
| BIO-05 | [Bioconductor SummarizedExperiment](https://bioconductor.org/packages/release/bioc/html/SummarizedExperiment.html) | Primary software documentation | Keep assays, sample metadata and feature metadata aligned by stable identifiers | Gene-by-sample matrices and sample annotations | Assay rows are usually features and columns samples; metadata reordering can silently corrupt interpretations |
| BIO-06 | [Bioconductor edgeR](https://bioconductor.org/packages/release/bioc/html/edgeR.html) | Primary statistical software documentation | For supported sequencing count data, verify library sizes, design, normalization, dispersion and test selection | Count-based differential-expression reasoning | Counts, CPM and log-CPM are not interchangeable model inputs; fit/test choice depends on design |
| BIO-07 | [Bioconductor DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) | Primary statistical software documentation | Document sample design and use appropriate negative-binomial count models | Independent explanation of count-based expression inference | Do not submit normalized expression as if it were unmodified integer read counts |
| BIO-08 | [Bioconductor limma](https://bioconductor.org/packages/release/bioc/html/limma.html) | Primary statistical software documentation | Make the design matrix, contrasts, preprocessing and multiplicity correction explicit | Regression-style gene expression analysis | A contrast coefficient is not inherently a validated biological effect; confirm scale and design |
| BIO-09 | [Bioconductor workflows](https://www.bioconductor.org/help/workflows/) | Official workflow index | Compare input and output contracts across assay preprocessing, quality checks and models | Reproducible computational genomics workflow | Example workflows are starting points, not validation of unrelated data |
| BIO-10 | [STROBE statement](https://www.strobe-statement.org/) | Observational-study reporting guideline | State study design, participant selection, variables, bias, statistical methods and limitations | Writing transparent epidemiologic methods and results | Reporting completeness does not establish causal validity |
| BIO-11 | [RECORD statement (EQUATOR)](https://www.equator-network.org/reporting-guidelines/record/) | Routinely collected health-data reporting guideline | Document data provenance, codes/algorithms, linkage, selection and availability | Administrative and clinical observational data | RECORD is a reporting extension, not a substitute for legal/ethical permissions |
| BIO-12 | [TRIPOD reporting guideline (EQUATOR)](https://www.equator-network.org/reporting-guidelines/tripod-statement/) | Prediction-model reporting guideline | State predictor selection, missingness, performance, uncertainty and validation design | Model-reporting literacy | Prediction performance is not causal evidence or clinical deployment authorization |
| BIO-13 | [The Turing Way: Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research/) | Open research handbook | Preserve software/environment details, inputs, transformations and output provenance | Re-run scripts and document reproducible pipelines | Reproducibility does not establish external validity or consent to redistribute inputs |
| BIO-14 | [FAIR Guiding Principles (Wilkinson et al., 2016)](https://doi.org/10.1038/sdata.2016.18) | Peer-reviewed data-stewardship principles | Use stable identifiers and meaningful metadata for findability/interoperability | Dataset dictionary and provenance exercises | FAIR does not require publishing confidential person-level records |

## Practical resource selection

| Research task | Start here | Record before analysis | Minimum evidence to retain |
| --- | --- | --- | --- |
| Read public-health survey data | BIO-01–04 | Cycle, file/component, participant key, skip codes, appropriate weight, strata/PSU | Codebook version, join audit, missingness, specified survey design |
| Work with expression assays | BIO-05, BIO-09 | Sample-feature orientation, count/normalized scale, group mapping, feature IDs | Matrix dimensions, sample order checks, metadata join checks |
| Fit differential-expression models | BIO-06–08 | Input count scale, design, contrasts, normalization, dispersion or weighting method | Model specification, fitting diagnostics, multiple-testing method, reproducible environment |
| Report observational research | BIO-10, BIO-11 | Design, sample restrictions, measurement sources, missingness, selection | Transparent methods, documented assumptions, disclosure of limitations |
| Study prediction-model reporting | BIO-12 | Intended population, target outcome, leakage controls, train/validation boundaries | Evaluation design and uncertainty, avoiding claims beyond observed performance |
| Publish a reproducible student example | BIO-13, BIO-14 | Synthetic/license status, software version, input schema, seed | Re-run instructions, independent source links, output checks |

## Reusable evidence checklist

1. **Source:** Identify whether the input is simulated, public, restricted, or licensed. Do not assume public availability means unrestricted redistribution.
2. **Schema:** Record the observation unit, identifier, measurement unit, assay or survey design, and acceptable missingness.
3. **Joining:** Validate uniqueness and cardinality before linking health records; report unmatched counts without fabricating absent responses.
4. **Modeling:** Distinguish descriptive visualization from model fitting, and distinguish weighted survey estimates from unweighted classroom demonstrations.
5. **Inference:** Preserve the scale of estimates, uncertainty, comparison definition and multiplicity corrections.
6. **Reproducibility:** Record package/software versions, input provenance and deterministic operations; separate protected data from public code.
7. **Reporting:** Apply a relevant reporting guideline when appropriate, without treating checklist completion as proof of scientific validity.

## Maintenance boundary

This page summarizes generally available public sources. It does not encode protected classroom learning objectives, privately observed code, a project-specific genomic model, or any patient-level information. Use the upstream manuals and their release-specific guides for exact software contracts. Review external URLs periodically; inaccessible links must be noted, not silently replaced with unrelated sites.
