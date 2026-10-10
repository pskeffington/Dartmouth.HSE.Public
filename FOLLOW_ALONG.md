# Follow along with Paul's Notes

[Paul's Notes](README.md) · [Weekly lessons](03_Group_Work/README.md) · [Topic companions](02_Lecture_Notes/README.md)

These public lessons use independently constructed examples and synthetic inputs. You can read them on GitHub without installing R. To run the examples, use your own R session; no official Dartmouth or Geisel materials are required.

## Prepare a study session

1. Open a lesson's Markdown reading edition and skim its objectives and prerequisites.
2. If executing examples, open its linked `.Rmd` source and start a fresh R session. Check the dependencies at the beginning.
3. Work through code blocks in order. Compare objects, dimensions, missing counts, and printed results with the explanations. A silent `stopifnot()` means its check passed.
4. For each graph, name the axes, units, and denominator before interpreting its shape. Separate descriptive patterns from statistical or causal claims.
5. Complete the independent exercises, explain the teach-back questions aloud, and use the next-lesson link.

The reading-edition builder displays code without running it. A GitHub page does not itself establish execution success. The lesson-validation tool extracts and parses every R block and executes the examples in separate clean sessions, saving logs and plot files outside the repository:

```bash
python3 scripts/validate_weekly_r.py --output-dir /tmp/pauls-notes-r-checks
```

## Choose your next lesson

| Stage | Lesson | Related reference |
| --- | --- | --- |
| 1 | [R foundations](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) | [R objects and syntax](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) |
| 2 | [Wrangling and visualization](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) | [Wrangling topic companion](02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) |
| 3 | [Visualization and analytics](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) | [Analytics topic companion](02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) |
| 4 | [Bash topic guide](02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) | [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) |

## When something differs

Check spelling and object availability first, then inspect `str()`, `names()`, and `dim()`. A missing package is a dependency problem, not a data result. Seeded examples still require a compatible R and package environment; printed rounding may differ. Keep raw inputs unchanged and record exclusions rather than deleting rows without explanation.

For short reminders, use the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md), [plot-reading guide](06_RESOURCES/READING_PLOTS.md), and [APA 7 LaTeX guide](06_RESOURCES/LaTeX/README.md).

## Public source boundary

Official instructional files, private datasets, and assessed work stay in authorized private workspaces. The [source policy](ORIGINALITY_POLICY.md), [provenance register](PROVENANCE_REGISTER.md), and [history review](HISTORY_EXPOSURE_REVIEW.md) describe publication controls and remaining reviews. Technical validation is not a copyright certificate.
