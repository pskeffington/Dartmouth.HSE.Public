# Automatic downstream plot annotations

Source **after** the core R plotting modules:

```r
source("RESOURCES/R/hse_stats_plots.R")
source("RESOURCES/R/hse_one_call_plots.R")
source("RESOURCES/R/hse_biostat_panels.R")
source("RESOURCES/R/hse_plot_annotations.R")
```

The annotation module decorates the existing plotting functions so a normal **one-call** statistical plot includes clear figure title, x/y axes, statistical method, sample size, p-value if applicable, multiple-testing details, and an appropriate limitations caption. Original statistical test objects remain available in `attr(plot, "hse_test")` or the existing function-specific attributes.

## One-call examples

```r
p <- hse_plot_test(mtcars, "wt", "mpg", method="pearson", fit=TRUE)
print(p)
hse_plot_annotation(p)              # machine-readable annotation fields
hse_plot_audit(p)                   # missing-label and caption check

# Add figure-specific publication provenance without changing the test:
p <- hse_annotation(
  p,
  title="Vehicle weight and fuel efficiency",
  x="Weight (1000 lb)", y="Miles per gallon",
  source="R datasets::mtcars",
  note="Exploratory association; not causal"
)
hse_save_annotated(p, "figures/weight_mpg.pdf", require_source=TRUE)
```

`hse_save_annotated()` creates the figure and a neighboring `.annotations.R` manifest containing annotation fields, units, and export size. The manifest is a base-R `dput` file readable with `dget`.

## Scope and statistical integrity

- **Correlation and regression:** the p-value is for Pearson/Spearman correlation; a regression trendline with mean-response CI is distinct, and the confidence band must not be presented as the correlation confidence interval.
- **Wilcoxon:** explicit independent versus paired design; the graph's p-value belongs to that test. For paired inference, subject identifiers are required.
- **Faceted Wilcoxon:** BH or selected adjustment is across the set of facet-level tests, and panel labels show the adjusted p-value with n per panel.
- **Multigroup:** show the Kruskal–Wallis global p and store adjusted post-hoc Wilcoxon results as a separate table, not as invented glyphs.
- **Forest:** intervals are provided by the caller; the module does not fabricate them.
- **ROC:** AUC annotation identifies apparent discrimination unless the input is held out.
- **Survival:** annotate censoring and method; no hazard ratio or log-rank p is generated without an appropriate additional statistical analysis.
- **Means by time:** descriptive pointwise t-intervals must not be relabeled as fitted repeated-measures confidence intervals.
- **Genomics:** log-CPM is a plotting scale, not an edgeR QL count-model substitute.

## Publication gate

```r
audit <- hse_plot_audit(p, require_source=TRUE)
stopifnot(audit$pass)
```

This checks annotation presence, **not** correctness of the statistical model or provenance claims. Supply meaningful source and assay labels from the actual dataset.

To validate the implementation:

```sh
Rscript --vanilla RESOURCES/tests/test_hse_plot_annotations.R
```
