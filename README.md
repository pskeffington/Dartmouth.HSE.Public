# Dartmouth Health Data Science — Public Learning Repository

**Teaching notes · Group exercises · Reusable statistical computing resources**

A public companion to graduate-level health data science coursework. Materials emphasize reproducible analysis, readable scientific explanations, and practical code examples. This is an independent educational repository, **not an official Dartmouth course website**.

## Start here

Open the **reading editions** below directly in GitHub. Each has links to its editable source. For a guided session, use the [follow-along guide](FOLLOW_ALONG.md); for short examples, keep the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md) and [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) open.

Current coverage: Week 1 group work, Weeks 2–4 notes and group work, and reusable resources. Capstone, final-project and assignment sections are reserved; no deliverables are posted there yet.

| I want to… | Go to |
| --- | --- |
| Follow a weekly lecture | [Lecture Notes](02_Lecture_Notes/) |
| Work through a classroom exercise | [Group Work](03_Group_Work/) |
| Run the Week 4 Bash metadata lab | [Week 4 Lab](03_Group_Work/Week_4_Bash_Lab/) |
| Generate descriptive statistics or annotated plots in R | [R Resources](06_RESOURCES/#r-statistics-and-visualization) |
| Study Bash, scripting, and data processing | [Bash Resources](06_RESOURCES/#bash-programming) |
| Prepare a formatted Week 4 report | [LaTeX Template](06_RESOURCES/LaTeX/) |

## Course materials

Each group walkthrough opens with session checkpoints. Use them to pause, check output and explain the method to a partner. For figures, keep the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) beside the code.

| Week | Lecture | Group work |
| --- | --- | --- |
| 1 | Lecture companion not posted | [Data types, indexing, and functions](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) |
| 2 | [Learning objective notes](02_Lecture_Notes/Week_2_Learning_Objective_Notes.md) | [Data wrangling and visualization](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) |
| 3 | [Learning objective notes](02_Lecture_Notes/Week_3_Learning_Objective_Notes.md) | [Simulation and reusable functions](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) |
| 4 | [Introduction to Bash](02_Lecture_Notes/Week_4_Introduction_to_Bash_Narrative_Walkthrough.md) | [Bash metadata walkthrough](03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.md) · [Run the lab](03_Group_Work/Week_4_Bash_Lab/) |

## Repository organization

| Section | Contents |
| --- | --- |
| [Capstone](01_Capstone/) | Planning and synthesis, reserved for future public materials |
| [Lecture Notes](02_Lecture_Notes/) | Explanatory lecture companions and learning objectives |
| [Group Work](03_Group_Work/) | Narrative exercises and runnable lab files |
| [Final Project](04_Final_Project/) | Public-facing final-project materials when approved for release |
| [Assignments](05_Assignments/) | Assignment-related teaching materials when appropriate to share |
| [RESOURCES](06_RESOURCES/) | R functions, statistical plots, Bash utilities, LaTeX templates and literature |

## Quick start: Week 4 Bash

Use your **local** copy of the supplied classroom data:

```bash
# In an existing clone, open a terminal at the repository root.
pwd
mkdir -p data
# Place pseudo_metadata.csv inside ./data/ before continuing.
bash "03_Group_Work/Week_4_Bash_Lab/test_week4.sh"
bash "03_Group_Work/Week_4_Bash_Lab/run_week4.sh" \
  data/pseudo_metadata.csv ./week4_practice
```

The repository ignores the root-level `data/` folder and the generated `week4_practice/` output. Never force-add source data or confidential records to this public repository.

## Scientific and academic-use notes

The examples distinguish exploratory visualization from statistical inference. Statistical interpretation requires documented sample sizes, missingness, measurement units, study design and tested assumptions. Gene-expression log-CPM displays do not substitute for count-based differential-expression models.

Some lectures and exercises require files distributed separately through the course. Their absence is noted; unexecuted or unavailable results are not presented as verified findings. Respect course collaboration, attribution, sharing and AI-use policies.

See [RESOURCES](06_RESOURCES/) for references, tests, installation requirements and reproducibility guidance. [License](LICENSE).
