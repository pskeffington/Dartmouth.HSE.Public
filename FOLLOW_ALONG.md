# Follow along with Paul's Notes

[Breast Cancer Research Guide — People, Data, Biology and 60 Genes](06_RESOURCES/Genomics/BREAST_CANCER_60_GENE_COMPANION.md) connects these methods to synthetic genomics interpretation. Continue to [the research walkthrough](06_RESOURCES/Genomics/BREAST_CANCER_60_GENE_COMPANION.md#chapter-11-working-through-a-research-question).

[Paul's Notes](README.md) · [Weekly lessons](03_Group_Work/README.md) · [Topic companions](02_Lecture_Notes/README.md)

These public lessons use independently constructed examples and synthetic inputs. You can read them on GitHub without installing R. For Weeks 1–3, use an R session; Week 4 uses a Bash shell and launches Rscript.

## Set up once

| Week | Required environment | Check before starting |
| --- | --- | --- |
| 1 | Base R | Run `R.version.string` in R |
| 2 | R, tidyr, dplyr, ggplot2 | Run the lesson's package check; install missing packages in your own R library |
| 3 | R, dplyr >= 1.1.0, ggplot2 | Run `packageVersion("dplyr")` in R |
| 4 | Bash 3.2+, standard shell utilities, base Rscript | Run `bash --version` and `command -v Rscript` in Bash |

1. Install R for your operating system from [CRAN](https://cran.r-project.org/). Open R and run `R.version.string`; the lesson runtime checks were validated with R 4.4.3.
2. Optionally install RStudio using [Posit's installation links](https://docs.posit.co/ide/user/#install-links). RStudio is an editor and interface; it still requires R.
3. Download or clone this public repository into a folder you can read and write. In RStudio, open a project in that folder; in another editor, check `getwd()` before using repository-relative `source()` paths.
4. For Week 4 on macOS/Linux, open a terminal and run `bash` to select the documented shell. On Windows, one option is [WSL](https://learn.microsoft.com/en-us/windows/wsl/install): install R inside that Linux environment as well, so `Rscript` and Bash are available together. Installing Windows R alone does not put Linux Rscript inside WSL.

RStudio is an optional editor. You can run a saved R script with `Rscript --vanilla path/to/script.R` in a terminal. Windows readers need a Bash environment for shell examples; PowerShell commands use a different language. Read each lesson's exact package requirements before running a topic companion.

To install the Week 2–3 packages, run this in R, once, using your own writable library:

```r
install.packages(c("tidyr", "dplyr", "ggplot2"))
```

Successful installation is followed by the lesson's dependency check. A firewall, package-library permission problem, or incompatible version must be resolved before a missing function can run. Installing packages is separate from running the exercises.

## Prepare a study session

1. Open a lesson's Markdown reading edition and skim its objectives and prerequisites.
2. Open the linked `.Rmd` source. Start a fresh R session for Weeks 1–3 or Bash session for Week 4; check the listed dependencies first. In RStudio, run named R chunks in order. In a plain editor, copy their contents into a saved `.R` script, omitting Markdown fences. For Week 4, copy Bash block contents into one Bash session or saved `.sh` file; do not run them in the R console.
3. Work through code blocks in order. Compare objects, dimensions, missing counts, and printed results with the explanations. A silent `stopifnot()` means its check passed.
4. For each graph, name the axes, units, and denominator before interpreting its shape. Separate descriptive patterns from statistical or causal claims.
5. Complete the independent exercises, explain the teach-back questions aloud, and use the next-lesson link.

The reading-edition builder displays code without running it. A GitHub page does not itself establish execution success. The lesson-validation tool extracts and parses every R block and executes the examples in separate clean sessions, saving logs and plot files outside the repository:

```bash
python3 scripts/validate_weekly_r.py --include-companions --output-dir /tmp/pauls-notes-r-checks
python3 scripts/validate_weekly_bash.py --include-companion --output-dir /tmp/pauls-notes-bash-checks
```

These optional checks require Python 3.10+ in addition to the documented R/Bash tools. They write logs and figures outside Git; no patient or classroom inputs are needed. You can complete the lessons manually without Python.

## Choose your next lesson

| Stage | Lesson | Related reference |
| --- | --- | --- |
| 1 | [Synthetic expression foundations](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) | [R objects and syntax](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) |
| 2 | [Participant measurements and visits](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) | [Wrangling topic companion](02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) |
| 3 | [Epidemiologic joins and models](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) | [Analytics topic companion](02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) |
| 4 | [Scientific metadata and Bash workflows](03_Group_Work/Week_4_Bash_and_Reproducible_Workflows_Study_Guide.md) | [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) |

## Readiness is an explanation, not just a successful run

Each full lesson ends with **Ready to move on**. Save your script, input dictionary, output checks, and a short methods note. Ask a peer to identify the row unit, measured denominator, and units from your figure labels alone. Rerun in a clean session before beginning the next week. The exercises use invented observations and do not supply assessed classroom solutions.

## When something differs

Check spelling and object availability first, then inspect `str()`, `names()`, and `dim()`. A missing package is a dependency problem, not a data result. Seeded examples still require a compatible R and package environment; printed rounding may differ. Keep raw inputs unchanged and record exclusions rather than deleting rows without explanation.

For short reminders, use the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md), [plot-reading guide](06_RESOURCES/READING_PLOTS.md), and [APA 7 LaTeX guide](06_RESOURCES/LaTeX/README.md).

## Finish with evidence

| Week | Keep from your practice | Explain before moving on |
| --- | --- | --- |
| 1 | R script, checked import/export, available/missing counts, labeled histogram | Gene/sample row units, object structure, selection, function inputs, and observed denominator |
| 2 | Participant simulation seed, visit round trip, group summaries, plots | Observation key, missingness, categories, and paired versus independent design |
| 3 | Typed health imports, join/code audits, inclusion rule, model record, diagnostics, panels | Biomarkers versus self-reports, retained/unmatched rows, slope units, exclusions, and inference limits |
| 4 | Filter and R scripts, known input, selected tables, summary, run log | Quoting, arguments, statuses, validation failures, and measured versus total counts |

Use the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) to narrate a figure and the [APA manuscript example](06_RESOURCES/LaTeX/README.md) to organize a methods note. Do not invent results to fill a template: calculate them from the objects produced by your run.
