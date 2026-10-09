# Biostatistics plotting panels — one-call guide

**Source order:**

```r
source("06_RESOURCES/R/hse_stats_plots.R")
source("06_RESOURCES/R/hse_one_call_plots.R")
source("06_RESOURCES/R/hse_biostat_panels.R")
```

The module uses native `ggplot2::facet_wrap` and `ggplot2::facet_grid`, often called **ggplot panels** or small multiples. The exact `ggpanel` terminology is not the name of a dependency in this library.

## API catalog

| Function | One-call result | Statistical meaning |
|---|---|---|
| `hse_panel(plot,facet,column=NULL)` | Facet any compatible ggplot | Presentation only |
| `hse_plot_panel_box(data,value,group,facet)` | Box/jitter panels | Descriptive |
| `hse_plot_panel_wilcox(data,value,group,facet)` | One Wilcoxon p-value per facet | BH adjustment across facet tests |
| `hse_plot_trajectory(data,id,time,value)` | Individual patient trajectories | Descriptive; preserves subject identity |
| `hse_plot_mean_ci(data,time,value,group)` | Group mean and t confidence intervals | Pointwise descriptive CIs; NOT longitudinal model inference |
| `hse_plot_forest(data,label,estimate,lower,upper)` | Effect/interval forest plot | Uses supplied validated estimates; no fitting |
| `hse_plot_lm_diagnostics(model)` | Residual/fitted and normal Q-Q panels | Existing lm model diagnostics |
| `hse_plot_roc(data,outcome,score,positive)` | ROC plus AUC | pROC; higher score means positive |
| `hse_plot_survival(data,time,event,group)` | Kaplan–Meier steps/censoring marks | survival::survfit; event=1 |

## Single-call examples

```r
data(mtcars)
mtcars$am <- factor(mtcars$am)
mtcars$cyl <- factor(mtcars$cyl)
# Ready-made faceted boxplots:
p <- hse_plot_panel_box(mtcars, "mpg", "am", "cyl")
print(p)

# Distinct tests in each panel with BH-adjusted p-values:
p <- hse_plot_panel_wilcox(mtcars, "mpg", "am", "cyl")
print(p)
attr(p, "hse_tests")

# Model diagnostics without refitting:
p <- hse_plot_lm_diagnostics(lm(mpg ~ wt + hp, data=mtcars))
print(p)

# Means and pointwise CIs in groups:
p <- hse_plot_mean_ci(mtcars, "cyl", "mpg", "am")
print(p)
attr(p, "hse_summary")

# Forest plot uses existing estimates (example only):
effects <- data.frame(term=c("A","B"), effect=c(.3,-.1),
                      low=c(.1,-.3), high=c(.5,.1))
p <- hse_plot_forest(effects,"term","effect","low","high")
print(p)

# ROC needs pROC and an explicit positive class:
# p <- hse_plot_roc(holdout,"outcome","predicted_risk", positive="Case")
# AUC should be evaluated on independent/held-out data.

# Survival needs survival package; event=1 for observed events:
# p <- hse_plot_survival(clinical, "follow_up_days", "event", "treatment")

# Publication export, with consistent size:
hse_save_plot(p,"figures/biostat_panel.pdf",width=8,height=5)
```

## Statistical safeguards

- A faceted Wilcoxon figure makes independent tests within each facet and adjusts the family of facet p-values with the chosen `p_adjust` method. It does not infer matching; paired comparisons require explicit patient IDs and a suitable paired model.
- Confidence intervals calculated with `hse_plot_mean_ci` are *pointwise* t intervals computed separately at each time/group, and should not be described as model-based repeated-measures inference.
- Forest plots require actual estimates and limits from a statistical model. Reference 0 is appropriate for additive/log effects, while ratio-scale odds/hazard/risk ratios require reference 1 and appropriately transformed axes.
- ROC estimates/AUC require an appropriate binary outcome, explicit positive class and proper independent validation to support generalization.
- Kaplan–Meier uses event indicators and censoring, not raw prevalence. No log-rank p-value or hazard ratio is invented.
- Gene-expression charts can use log2-CPM, but edgeR count-model inference still requires counts/offsets and an approved modeling design.
- `free_y` faceting improves within-panel legibility but obstructs direct magnitude comparisons; use fixed scales by default.

## Testing

```sh
Rscript --vanilla 06_RESOURCES/tests/test_hse_biostat_panels.R
```

Optional dependencies: `ggplot2` for all plots, `pROC` for ROC, and `survival` for Kaplan–Meier. R and optional packages may not be available on all learner machines; smoke tests skip their corresponding optional sections.

References: [ggplot2 facets](https://ggplot2.tidyverse.org/reference/facet_wrap.html), [facet_grid](https://ggplot2.tidyverse.org/reference/facet_grid.html), [pROC](https://xrobin.github.io/pROC/), [survival](https://cran.r-project.org/package=survival).
