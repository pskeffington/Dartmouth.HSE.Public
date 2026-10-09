# Resources

Reusable methods, functions, teaching references and templates for health data science. All code is educational, **not clinical decision software**.

## Start with the short sheets

- [Easy R functions](R/EASY_FUNCTION_SHEET.md): inspect data, summarize values and reuse three common graphs.
- [Easy Bash commands](Bash/EASY_COMMAND_SHEET.md): navigate, inspect, select fields and check a script.
- [Read and explain a plot](READING_PLOTS.md): axes, distributions, groups and statistical annotations.
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
| Week 4 formatted learning document | [LaTeX guide](LaTeX/) | [Editable TeX](LaTeX/Week_4_Bash_LaTeX_Template.tex) |
| Research and coding references | [Bash literature](Bash/BASH_LITERATURE_REVIEW.md) · [Literature matrix](Literature/LITERATURE_MATRIX.md) | [Matrix CSV](Literature/literature_matrix.csv) |

## R statistics and visualization

Load modules in dependency order:

```r
source("06_RESOURCES/R/hse_stats_plots.R")
source("06_RESOURCES/R/hse_gene_visuals.R")
source("06_RESOURCES/R/hse_one_call_plots.R")
source("06_RESOURCES/R/hse_biostat_panels.R")
source("06_RESOURCES/R/hse_plot_annotations.R")
```

**Descriptive report:**

```r
data(mtcars)
report <- hse_summary_report(mtcars, "mpg", unit = "miles per gallon")
hse_print_summary(report)
```

**Annotated visualization:**

```r
plot <- hse_plot_test(mtcars, "wt", "mpg")
hse_plot_audit(plot)
print(plot)
```

For additional historical classroom functions, see [Week 3 reusable functions](R/Week_3_Reusable_Functions.R).

## Bash programming

Start with the [operation reference](Bash/BASH_OPERATION_SHEET.md), then the [annotated literature review](Bash/BASH_LITERATURE_REVIEW.md). The [sourceable utility functions](Bash/bash_functions.sh) provide file checking, TSV inspection, checksum utilities and Rscript orchestration.

The [Week 4 runnable exercise](../03_Group_Work/Week_4_Bash_Lab/) expects local synthetic data in `data/`, which Git ignores.

## LaTeX learning and reports

The [Week 4 LaTeX template](LaTeX/) contains learning objectives, command examples, report sections, observation placeholders and reproducibility checks. TeX compilation requires a separate LaTeX installation.

## Navigation checks

Run the [navigation checker](Presentation/check_navigation.py) after changing paths or headings. The [link audit](Presentation/LINK_AUDIT.md) records the external destinations that could and could not be retrieved.

## Tests and scientific boundaries

Smoke tests are in [tests](tests/), including descriptive statistics, gene plots, regression, panels, annotations and summary narratives. These tests require R and appropriate packages and are **not a substitute for independent scientific validation**. Run the relevant test before relying on a figure or statistical result.

Report sample sizes, missingness, measures, units and statistical assumptions. Distinguish descriptive log-CPM analysis from count-based models for RNA-seq inference. The literature matrix is methodological background, not confirmation of project-specific clinical results.

## Presentation formats

Weekly reading editions are generated from their editable sources. See [reading editions and HTML styling](Presentation/README.md) for updating the pages and knitting a readable companion.

## Local-only inputs

`/data/` and `/week4_practice/` are excluded by `.gitignore`. Do not use `git add -f` to publish them. Avoid committing sensitive data, restricted classroom files or identifiable patient records.
