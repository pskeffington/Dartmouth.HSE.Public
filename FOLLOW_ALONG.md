# HSE 711 · Follow-along guide

[Repository home](README.md) · [Lecture notes](02_Lecture_Notes/README.md) · [Group work](03_Group_Work/README.md) · [Resources](06_RESOURCES/README.md)

Use this guide to read independently or lead a small group through the public materials. These are student-prepared study companions. Consult the course materials for the authoritative prompts and requirements.

## Prepare your workspace

For reading, open the Markdown editions on GitHub. No software or data download is needed. For R practice, open a local repository copy in RStudio and set the working directory to the repository root. Run `getwd()` to check it. Install only the packages required by the selected example, once, in the Console; then load them in the script. For Bash practice, use a Bash terminal on macOS, Linux or Windows with WSL.

Keep course-supplied inputs in the ignored `data/` folder. Some original lecture reference snippets use `../data/`; adjust these to your actual working directory. Reading editions show code and explanation, without computed output. They do not require knitting. Editable `.Rmd` sources require R Markdown, their packages and any specified inputs to generate results.

## Choose a week

| Session | Read first | Practice | Pause and explain |
| --- | --- | --- | --- |
| Week 1 · R foundations | [Group walkthrough](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) | Types, lists, indexing, missing values and functions | What does the object contain, and which indexing rule selects it? |
| Week 2 · Data wrangling | [Lecture notes](02_Lecture_Notes/Week_2_Learning_Objective_Notes.md) | [Group walkthrough](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md); data-dependent tasks need the separate arsenic CSV | Which rows and columns remain? What does each row represent after reshaping? |
| Week 3 · Visualization | [Lecture notes](02_Lecture_Notes/Week_3_Learning_Objective_Notes.md) | [Group walkthrough](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md); Questions 1–4 simulate data, Question 5 needs course CSVs | What do the plot's axes, groups and marks mean? Are these simulated or observed measurements? |
| Week 4 · Bash | [Lecture walkthrough](02_Lecture_Notes/Week_4_Introduction_to_Bash_Narrative_Walkthrough.md) | [Group walkthrough](03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.md) and [runnable lab](03_Group_Work/Week_4_Bash_Lab/README.md) | Does the count include a header? Which field encodes sex, and which files remain after cleanup? |

The group walkthroughs provide a checkpoint table and previous/next-week links. Use the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) when preparing a short explanation of a figure.

## Work through one question

1. State the task in one sentence and identify the input columns or objects.
2. Read the explanation, then run one complete code chunk in the editable source. Earlier chunks may define objects used later.
3. Inspect the result with `head()`, `str()`, `dim()` or the relevant file preview. Check category labels, units and missing values.
4. Describe what the result shows. For a figure, describe axes and visible patterns before discussing a statistical test.
5. Change one parameter and explain what changes. Record your observation before continuing.

## Keep these sheets beside your work

[Easy R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md) covers inspection, summaries and common graphs. [Easy Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) covers location, file inspection, simple filtering and script checks. The resource index links to longer statistical and methodological guides.

## When something stops working

| Symptom | Check |
| --- | --- |
| File not found | Check `getwd()` or `pwd`, the filename and the local `data/` location. |
| R function not found | Load the package or `source()` the helper named in the example. |
| R object not found | Run the earlier chunk that creates it; check spelling and capitalization. |
| Plot appears in the Console but not a script run | Explicitly call `print(plot_object)`. |
| No CSVs discovered | Inspect `list.files()` and the path; Week 3 Question 5 skips when course files are absent. |
| Bash subset is empty | Inspect the header and category codes. The Week 4 file uses `F` and `M` in field 5. |

## Before sharing a result

Include the question, input source, method, sample size and measurement units. Explain missingness and limitations. Simulation illustrates a procedure; it does not establish a biological finding. An exploratory association does not establish causation. Keep classroom input files and participant records out of public commits.
