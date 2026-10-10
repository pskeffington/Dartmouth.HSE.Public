# Resources
The examples use 48 independently simulated adult participants from `make_teaching_cohort()`. Age is years; creatinine is mg/dL; albumin is g/dL. Recorded sex and site are fictional categories, and the programmed age association is not clinical evidence. Run blocks in order from the repository root. Optional file exports create or replace the named output; choose a deliberate destination.


Reusable methods, functions, teaching references and templates for health data science. All code is educational, **not clinical decision software**.

## Start with the short sheets

- [Easy R functions](R/EASY_FUNCTION_SHEET.md): inspect data, summarize values and reuse three common graphs.
- [Easy Bash commands](Bash/EASY_COMMAND_SHEET.md): navigate, inspect, select fields and check a script.
- [Read and explain a plot](READING_PLOTS.md): axes, distributions, groups and statistical annotations.
- [Weekly lessons](../03_Group_Work/README.md): complete independent R and Bash lessons with synthetic examples and exercises.
- [Follow-along guide](../FOLLOW_ALONG.md): prepare a session and review each week.

## Choose a resource

| Need | Guide | Code |
| --- | --- | --- |
| Complete descriptive statistics, IQR and narrative | [Summary statistics](SUMMARY_STATISTICS.md) | [R statistics](R/hse_stats_plots.R) |
| One-call regression and Wilcoxon plots | [Statistical graphics](ONE_CALL_PLOTS.md) | [R plot functions](R/hse_one_call_plots.R) |
| Faceted panels and clinical biostatistics figures | [Biostatistics panels](BIOSTAT_PLOT_PANELS.md) | [R panel functions](R/hse_biostat_panels.R) |
| Consistent figure titles, sample sizes and annotations | [Plot annotations](PLOT_ANNOTATIONS.md) | [R annotation functions](R/hse_plot_annotations.R) |
| Gene-expression heatmaps, PCA and volcano plots | [Gene graphics](R/hse_gene_visuals.R) | [R source](R/hse_gene_visuals.R) |
| Bash syntax, operations and safe scripting | [Bash operation sheet](Bash/BASH_OPERATION_SHEET.md) | [Bash helpers](Bash/bash_functions.sh) |
| APA 7 student manuscript example | [LaTeX guide](LaTeX/) | [Editable TeX](LaTeX/Example_APA_7_Manuscript.tex) |
| Coding practices and reproducibility literature | [Best-practices reference matrix](Literature/README.md) | [Bash literature](Bash/BASH_LITERATURE_REVIEW.md) |
| Biomedical research computing and reporting | [Biomedical methods matrix](Literature/BIOMEDICAL_CODING_METHODS.md) | [R resources](R/README.md) |
| Naming, biomedical coding standards and quality gates | [Extensible coding standards](Literature/BIOMEDICAL_CODING_STANDARDS.md) | [General coding references](Literature/README.md) |
| Biomedical code review and evidence gates | [Research code quality matrix](Literature/RESEARCH_CODE_QUALITY_MATRIX.md) | [Biomedical methods matrix](Literature/BIOMEDICAL_CODING_METHODS.md) |
| Future-course research project intake and data contracts | [Project intake reference](Literature/RESEARCH_PROJECT_INTAKE.md) | [Biomedical coding conventions](Literature/BIOMEDICAL_CODING_STANDARDS.md) |
| Clinical terminology, units and research metadata | [Interoperability matrix](Literature/INTEROPERABILITY_METADATA_STANDARDS.md) | [Research code quality](Literature/RESEARCH_CODE_QUALITY_MATRIX.md) |

## R statistics and visualization

Load modules in dependency order:

```r
source("06_RESOURCES/R/hse_teaching_data.R")
health_data <- make_teaching_cohort()
source("06_RESOURCES/R/hse_stats_plots.R")
source("06_RESOURCES/R/hse_gene_visuals.R")
source("06_RESOURCES/R/hse_one_call_plots.R")
source("06_RESOURCES/R/hse_biostat_panels.R")
source("06_RESOURCES/R/hse_plot_annotations.R")
```

**Descriptive report:**

```r
report <- hse_summary_report(health_data, "Creatinine", unit = "mg/dL")
hse_print_summary(report)
```

**Annotated visualization:**

```r
plot <- hse_plot_test(health_data, "Age", "Creatinine")
plot <- plot + ggplot2::labs(x = "Age (years)", y = "Creatinine (mg/dL)")
hse_plot_audit(plot)
print(plot)
```

For additional basic reusable functions, see [Week 3 reusable functions](R/Week_3_Reusable_Functions.R).

## Bash programming

Start with the [operation reference](Bash/BASH_OPERATION_SHEET.md), then the [annotated literature review](Bash/BASH_LITERATURE_REVIEW.md). The [sourceable utility functions](Bash/bash_functions.sh) provide file checking, TSV inspection, checksum utilities and Rscript orchestration.


## LaTeX learning and reports

The [APA 7 student manuscript template](LaTeX/) contains a student title page, manuscript sections, author–date citations, references, table/figure placeholders and a reproducibility appendix. TeX compilation requires a separate LaTeX installation.

## Publishing and navigation checks

The [document publishing tools](Presentation/README.md) produce browser-friendly reading editions from editable study-guide sources. After changing headings, links, or source content, verify the generated editions and local navigation from the repository root:

```bash
python3 06_RESOURCES/Presentation/build_reading_editions.py --check
python3 06_RESOURCES/Presentation/check_navigation.py
```

The [dated link audit](Presentation/LINK_AUDIT.md) distinguishes retrieved external references from destinations that could not be verified; an unavailable response is not automatically a broken link.

## Tests and scientific boundaries

Smoke tests are in [tests](tests/), including descriptive statistics, gene plots, regression, panels, annotations and summary narratives. These tests require R and appropriate packages and are **not a substitute for independent scientific validation**. Run the relevant test before relying on a figure or statistical result.

Report sample sizes, missingness, measures, units and statistical assumptions. Distinguish descriptive log-CPM analysis from count-based models for RNA-seq inference. The literature matrix is methodological background, not confirmation of project-specific clinical results.

## Reading and output formats

Editable study-guide sources live in the lecture and group-work folders. Weekly Markdown reading editions are generated from those sources; HTML knitting uses a shared stylesheet. See the [publishing guide](Presentation/README.md) for build and rendering instructions. This tooling does not run analyses or validate scientific conclusions.

## Local-only inputs

`/data/` and `/week4_practice/` are excluded by `.gitignore`. Do not use `git add -f` to publish them. Avoid committing sensitive data or identifiable patient records.
