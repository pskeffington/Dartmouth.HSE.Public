# Group Work — Scholarly teaching walkthroughs

This collection presents the public HSE 711 exercises as readable academic teaching narratives. Each walkthrough connects the question under study to its R implementation, the meaning of the resulting output, and the limitations of the evidence. These independent teaching notes are not official Dartmouth course instructions.

## Week 4 update

[Week 4 — Bash metadata exercise](Week_4_Bash_Group_Work_Narrative_Walkthrough.Rmd) covers all five provided tasks with annotated command examples, a filename mismatch note, source-data limitations, and safe cleanup instructions.

## Reading sequence

| Week | Teaching focus | Scholarly emphasis |
|---|---|---|
| [Week 1: Introduction to R](Week_1_Group_Work_Narrative_Walkthrough.Rmd) | Data types, missing values, matrices, functions, iteration | How data representation and identifier integrity affect analytical validity |
| [Week 2: Data wrangling and visualization](Week_2_Group_Work_Narrative_Walkthrough.Rmd) | Source checking, categorical recoding, plots, Wilcoxon testing, reshaping | How eligibility, units, visualization choices, and sampling limit inference |
| [Week 3: Reusable analysis](Week_3_Group_Work_Narrative_Walkthrough.Rmd) | Simulations, functions, histograms, multi-file data processing | Reproducibility, sampling variability, unit-aware interpretation, and source-data boundaries |

## Reading a scientific exercise

For each exercise, identify its **research question**, **data-generating process or source**, **transformation**, **method**, **observable outcome**, and **interpretive limitations**. The code shows implementation; the prose provides the rationale for choosing the operation and the limits on what it demonstrates.

The [summary-statistics guide](../RESOURCES/SUMMARY_STATISTICS.md) supplies groupwise means, standard deviations, quartiles, IQR, sample sizes, missingness and an automatically generated descriptive narrative. The [statistical plotting modules](../RESOURCES/ONE_CALL_PLOTS.md) offer reusable, annotated displays. Those tools supplement the course exercises rather than replace their original function calls.

## Evidence and execution boundaries

Week 1 examples use illustrative values. Week 2's arsenic exercise requires the original course CSV, which is not distributed in this repository. Week 3 Questions 1–4 use simulated observations, while Question 5 requires external course files. No unexecuted result is reported as an observed empirical finding. Numerical interpretation should follow execution with the relevant source data, record units, show the denominator and missingness, and distinguish descriptive patterns from hypothesis tests.

## Reproduction

```sh
# From the public repository root; install R, rmarkdown and required
# packages first. CSV-dependent chunks need the original course files.
Rscript -e 'rmarkdown::render("Group Work/Week_1_Group_Work_Narrative_Walkthrough.Rmd")'
```

Other walkthroughs can be rendered by changing the file name, after supplying their documented data dependencies. Rendering is not claimed as completed in this documentation.

## Week 4 formal write-up

Use the [student LaTeX lab-report template](../RESOURCES/LaTeX/Week_4_Bash_LaTeX_Template.tex) to document the five Bash metadata exercises, preserving observed outputs and a reproducibility checklist.
