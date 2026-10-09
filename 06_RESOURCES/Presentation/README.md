# Reading editions and presentation styling

[Resource index](../README.md) · [Repository home](../../README.md)

The weekly Markdown editions are the default browser-reading format. Their editable `.Rmd` and comment-only `.R` sources remain beside them. To change a lesson, edit its source first and update the reading editions with:

```bash
python3 06_RESOURCES/Presentation/build_reading_editions.py
python3 06_RESOURCES/Presentation/build_reading_editions.py --check
```

The builder uses only Python's standard library. It formats prose and code fences, adds contents and source links, and labels inline computed output as available when rendered. It does not run R or create scientific results. `--check` reports stale editions without writing files.

For a locally knitted HTML companion, open a weekly `.Rmd` in RStudio and choose **Knit to HTML**. Its output settings provide a floating contents menu, collapsible code and the shared [reading stylesheet](reading.css). Install required packages and provide course inputs first. PDF output, where offered, uses the TeX installation and its own defaults; the CSS applies to HTML only.

For Week 3, run the following in the R Console **from the repository root** so its `data/In-Class-Exercises` path resolves correctly. The Knit button's default working directory is the source file's folder, which can cause Question 5 to skip even when the data exists at the repository root.

```r
rmarkdown::render(
  "03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.Rmd",
  output_format = "html_document",
  knit_root_dir = normalizePath(".")
)
```

Review the [follow-along guide](../../FOLLOW_ALONG.md) for input locations and the [plot-reading guide](../READING_PLOTS.md) for explanations of figures. A formatted reading edition does not verify the underlying analysis.
