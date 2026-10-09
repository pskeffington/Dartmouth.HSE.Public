# Dartmouth Health Data Science — Public Learning Repository

**Teaching notes · Group exercises · Reusable statistical computing resources**

A public companion to graduate-level health data science coursework. Materials emphasize reproducible analysis, readable scientific explanations, and practical code examples. This is an independent educational repository, **not an official Dartmouth course website**.

## Start here

| I want to… | Go to |
| --- | --- |
| Follow a weekly lecture | [Lecture Notes](Lecture%20Notes/) |
| Work through a classroom exercise | [Group Work](Group%20Work/) |
| Run the Week 4 Bash metadata lab | [Week 4 Lab](Group%20Work/Week_4_Bash_Lab/) |
| Generate descriptive statistics or annotated plots in R | [R Resources](RESOURCES/#r-statistics-and-visualization) |
| Study Bash, scripting, and data processing | [Bash Resources](RESOURCES/#bash-programming) |
| Prepare a formatted Week 4 report | [LaTeX Template](RESOURCES/LaTeX/) |

## Course materials

| Week | Lecture | Group work |
| --- | --- | --- |
| 1 | Introduction to R | [Data types, indexing, and functions](Group%20Work/Week_1_Group_Work_Narrative_Walkthrough.Rmd) |
| 2 | [Learning objective notes](Lecture%20Notes/Week_2_Learning_Objective_Notes.R) | [Data wrangling and visualization](Group%20Work/Week_2_Group_Work_Narrative_Walkthrough.Rmd) |
| 3 | [Learning objective notes](Lecture%20Notes/Week_3_Learning_Objective_Notes.R) | [Simulation and reusable functions](Group%20Work/Week_3_Group_Work_Narrative_Walkthrough.Rmd) |
| 4 | [Introduction to Bash](Lecture%20Notes/Week_4_Introduction_to_Bash_Narrative_Walkthrough.Rmd) | [Bash metadata walkthrough](Group%20Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.Rmd) · [Run the lab](Group%20Work/Week_4_Bash_Lab/) |

## Repository organization

| Section | Contents |
| --- | --- |
| [Capstone](Capstone/) | Planning and synthesis, reserved for future public materials |
| [Lecture Notes](Lecture%20Notes/) | Explanatory lecture companions and learning objectives |
| [Group Work](Group%20Work/) | Narrative exercises and runnable lab files |
| [Final Project](Final%20Project/) | Public-facing final-project materials when approved for release |
| [Assignments](Assignments/) | Assignment-related teaching materials when appropriate to share |
| [RESOURCES](RESOURCES/) | R functions, statistical plots, Bash utilities, LaTeX templates and literature |

## Quick start: Week 4 Bash

Use your **local** copy of the supplied classroom data:

```bash
git pull origin main
mkdir -p data
# Place pseudo_metadata.csv inside ./data/ before continuing.
bash "Group Work/Week_4_Bash_Lab/test_week4.sh"
bash "Group Work/Week_4_Bash_Lab/run_week4.sh" \
  data/pseudo_metadata.csv ./week4_practice
```

The repository ignores the root-level `data/` folder and the generated `week4_practice/` output. Never force-add source data or confidential records to this public repository.

## Scientific and academic-use notes

The examples distinguish exploratory visualization from statistical inference. Statistical interpretation requires documented sample sizes, missingness, measurement units, study design and tested assumptions. Gene-expression log-CPM displays do not substitute for count-based differential-expression models.

Some lectures and exercises require files distributed separately through the course. Their absence is noted; unexecuted or unavailable results are not presented as verified findings. Respect course collaboration, attribution, sharing and AI-use policies.

See [RESOURCES](RESOURCES/) for references, tests, installation requirements and reproducibility guidance. [License](LICENSE).