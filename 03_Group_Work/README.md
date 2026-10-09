# Group Work

**Narrative walkthroughs and reproducible classroom labs — HSE 711**

These materials connect a research question to implementation, expected output, interpretation and limitations. Original exercises remain recognizable, with additional scholarly explanation and verification guidance.

## Exercise library

| Week | Topic | Walkthrough | Ready-to-run materials |
| --- | --- | --- | --- |
| 1 | Introductory R, data types, indexing and functions | [Week 1 (.Rmd)](Week_1_Group_Work_Narrative_Walkthrough.Rmd) | Embedded R examples |
| 2 | Data preparation, visualizations and Wilcoxon comparisons | [Week 2 (.Rmd)](Week_2_Group_Work_Narrative_Walkthrough.Rmd) | Requires separate arsenic CSV |
| 3 | Simulation, reusable functions and multiple CSV files | [Week 3 (.Rmd)](Week_3_Group_Work_Narrative_Walkthrough.Rmd) | Simulations and separate course CSVs |
| 4 | Bash metadata manipulation | [Week 4 (.Rmd)](Week_4_Bash_Group_Work_Narrative_Walkthrough.Rmd) | [Bash lab scripts and tests](Week_4_Bash_Lab/) |

## Week 4: run the lab

From the repository root, with `pseudo_metadata.csv` already in the ignored `data/` directory:

```bash
bash "03_Group_Work/Week_4_Bash_Lab/test_week4.sh"
bash "03_Group_Work/Week_4_Bash_Lab/run_week4.sh" \
  data/pseudo_metadata.csv ./week4_practice
```

The script deliberately removes the temporary `new_dir` created in Question 3, but retains `only_female.txt` and `females_metadata.csv` in `week4_practice/`. The source exercise uses both names; the lab documents that distinction.

## How to read a worked example

A good learning narrative identifies the **question**, **input**, **method**, **observed output**, and **limits of interpretation**. Means and SDs describe magnitude and variability; medians and IQRs describe central tendency and spread with less sensitivity to extreme observations. A plot or a difference in sample means is not, by itself, evidence of causation or statistical significance.

Use the [complete summary statistics](../06_06_RESOURCES/SUMMARY_STATISTICS.md), [annotated plot functions](../06_06_RESOURCES/PLOT_ANNOTATIONS.md), and [student LaTeX report template](../06_06_RESOURCES/LaTeX/) where appropriate.

**Source boundary:** The Week 2 and part of the Week 3 work depend on course files not published here. Week 4 uses synthetic classroom metadata. Do not assert empirical results unless the relevant analysis has been run and checked.
