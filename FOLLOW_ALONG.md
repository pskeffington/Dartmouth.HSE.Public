# Follow along with Paul's Notes

[Paul's Notes](README.md) · [Weekly lessons](03_Group_Work/README.md) · [Topic companions](02_Lecture_Notes/README.md)

These public lessons use independently constructed examples and synthetic inputs. You can read them on GitHub without installing R. For Weeks 1–3, use an R session; Week 4 uses a Bash shell and launches Rscript.

## Set up once

| Week | Required environment | Check before starting |
| --- | --- | --- |
| 1 | Base R | Run `R.version.string` in R |
| 2 | R, tidyr, dplyr, ggplot2 | Run the lesson's package check; install missing packages in your own R library |
| 3 | R, dplyr >= 1.1.0 | Run `packageVersion("dplyr")` in R |
| 4 | Bash 3.2+, standard shell utilities, base Rscript | Run `bash --version` and `command -v Rscript` in Bash |

RStudio is an optional editor. You can run a saved R script with `Rscript --vanilla path/to/script.R` in a terminal. Windows readers need a Bash environment for shell examples; PowerShell commands use a different language. Read each lesson's exact package requirements before running a topic companion.

To install the Week 2 packages, run this in R, once, using your own writable library:

```r
install.packages(c("tidyr", "dplyr", "ggplot2"))
```

Successful installation is followed by the lesson's dependency check. A firewall, package-library permission problem, or incompatible version must be resolved before a missing function can run. Installing packages is separate from running the exercises.

## Prepare a study session

1. Open a lesson's Markdown reading edition and skim its objectives and prerequisites.
2. Open the linked `.Rmd` source. Start a fresh R session for Weeks 1–3 or Bash session for Week 4; check the listed dependencies first.
3. Work through code blocks in order. Compare objects, dimensions, missing counts, and printed results with the explanations. A silent `stopifnot()` means its check passed.
4. For each graph, name the axes, units, and denominator before interpreting its shape. Separate descriptive patterns from statistical or causal claims.
5. Complete the independent exercises, explain the teach-back questions aloud, and use the next-lesson link.

The reading-edition builder displays code without running it. A GitHub page does not itself establish execution success. The lesson-validation tool extracts and parses every R block and executes the examples in separate clean sessions, saving logs and plot files outside the repository:

```bash
python3 scripts/validate_weekly_r.py --output-dir /tmp/pauls-notes-r-checks
python3 scripts/validate_weekly_bash.py --output-dir /tmp/pauls-notes-bash-checks
```

## Choose your next lesson

| Stage | Lesson | Related reference |
| --- | --- | --- |
| 1 | [R foundations](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) | [R objects and syntax](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) |
| 2 | [Wrangling and visualization](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) | [Wrangling topic companion](02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) |
| 3 | [Visualization and analytics](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) | [Analytics topic companion](02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) |
| 4 | [Bash and reproducible workflows](03_Group_Work/Week_4_Bash_and_Reproducible_Workflows_Study_Guide.md) | [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) |

## When something differs

Check spelling and object availability first, then inspect `str()`, `names()`, and `dim()`. A missing package is a dependency problem, not a data result. Seeded examples still require a compatible R and package environment; printed rounding may differ. Keep raw inputs unchanged and record exclusions rather than deleting rows without explanation.

For short reminders, use the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md), [plot-reading guide](06_RESOURCES/READING_PLOTS.md), and [APA 7 LaTeX guide](06_RESOURCES/LaTeX/README.md).

## Finish with evidence

| Week | Keep from your practice | Explain before moving on |
| --- | --- | --- |
| 1 | R script, checked import/export, available/missing counts, labeled histogram | Object structure, selection, function inputs, units, and denominator |
| 2 | Simulation seed, wide/long round trip, group summaries, plots | Observation key, missingness, categories, and paired versus independent design |
| 3 | Join audits, codebook check, model record, diagnostics, reusable function | Retained/unmatched rows, slope units, exclusions, and limits of inference |
| 4 | Filter and R scripts, known input, selected tables, summary, run log | Quoting, arguments, statuses, validation failures, and measured versus total counts |

Use the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) to narrate a figure and the [APA manuscript example](06_RESOURCES/LaTeX/README.md) to organize a methods note. Do not invent results to fill a template: calculate them from the objects produced by your run.
