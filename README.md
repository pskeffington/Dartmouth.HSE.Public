# Paul's Notes

**A free, public study guide for health data science, research methods, and practical computing.** Independently maintained by Paul, this project covers R, Bash, reproducible research, and academic writing; **it is not an official Dartmouth or Geisel site.**

For students beginning biomedical data science, the complete lessons connect programming to synthetic expression, participant measurements, epidemiologic tables, and scientific sample metadata. Each week includes its inputs, expected results, interpretation, debugging, practice, and mastery checks.

[60-Gene Breast Cancer Research Companion](06_RESOURCES/Genomics/BREAST_CANCER_60_GENE_COMPANION.md) — complete gene cards, three learning routes, evidence register and seven original visual explanations.

## Start here

| What you want to study | Where to start |
| --- | --- |
| Scientific figure styles and worked examples | [Visualization gallery](06_RESOURCES/VISUALIZATION_GALLERY.md) |
| Breast cancer datasets and common gene biology | [Genomics companion](06_RESOURCES/Genomics/README.md), [dataset narrative](06_RESOURCES/Genomics/BREAST_CANCER_TCGA_BRCA_NARRATIVE.md) and [21-gene guide](06_RESOURCES/Genomics/COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md) |
| Concepts and topic notes | [Study guides](02_Lecture_Notes/README.md) |
| Introduction to Data Science (Weeks 1–5) | [Course learning hub](03_Group_Work/README.md) |
| R functions, summaries, and plots | [R resources](06_RESOURCES/R/README.md) and [function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md) |
| Bash, files, and scripting | [Bash resources](06_RESOURCES/Bash/README.md) and [command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) |
| APA 7 manuscripts and references | [LaTeX examples](06_RESOURCES/LaTeX/README.md) |
| Reading and explaining figures | [Plot-reading guide](06_RESOURCES/READING_PLOTS.md) |
| A guided study session | [Follow-along guide](FOLLOW_ALONG.md) |

Read the Markdown editions directly in GitHub. Their linked `.Rmd` files are editable sources. The [resource index](06_RESOURCES/README.md) includes tools, references, installation requirements, and reproducibility guidance.

## Introduction to Data Science — Weeks 1–5

Week numbers organize the topics. The teaching guides include runnable synthetic examples, expected results, practice, and self-assessment.

| Week | Concept/topic guide | Complete teaching lesson |
| --- | --- | --- |
| 1 | [R objects, data types, and indexing](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) | [R foundations with synthetic expression](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) |
| 2 | [Data wrangling and visualization](02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) | [Participant blood-cell data and repeated visits](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) |
| 3 | [Visualization and analytical reasoning](02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) | [Health-data joins, models, and figure panels](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) |
| 4 | [Bash and shell workflows](02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) | [Scientific metadata and Bash-to-R workflow](03_Group_Work/Week_4_Bash_and_Reproducible_Workflows_Study_Guide.md) |
| 5 | [Machine learning literature and method foundations](06_RESOURCES/Literature/WEEK_5_MACHINE_LEARNING_LITERATURE_REVIEW.md) | Complete Week 5 guide pending originality review and publication |

## Technical prerequisites

Weeks 1–3 use R; Week 2 needs tidyr, dplyr, and ggplot2, while Week 3 needs dplyr >= 1.1.0 and ggplot2. Week 4 needs Bash 3.2+, standard shell utilities, and Rscript. RStudio is optional. Start with the [installation and session guide](FOLLOW_ALONG.md#set-up-once); no classroom dataset is required.

## How I learned through games

My introduction to Bash came through [Terminus](https://terminus-global.vercel.app/): exploring a command-line adventure made the terminal approachable and encouraged experimentation. [Hack RUN](https://store.steampowered.com/app/378110/Hack_RUN/) gave me repeated practice with command-prompt navigation and file inspection, while [Hacknet](https://store.steampowered.com/app/365450/Hacknet/) helped me explore networking ideas in a simulation.

Those fictional environments sparked curiosity. I then practiced real commands for navigation, scripting, and reproducible workflows on my own computer and authorized systems. The games' simplified commands are not a substitute for real SSH syntax or security practices.

## Research and academic use

Use the examples to learn methods, not to establish health findings. Statistical interpretation depends on study design, sample size, missingness, measurement units, and assumptions. Distinguish exploratory plots from statistical inference, and follow the attribution and collaboration rules that apply to your work.

The [research-planning](01_Capstone/README.md), [reporting](04_Final_Project/README.md), and [practice](05_Assignments/README.md) sections connect these skills to a complete study workflow.

## License and feedback

See the [MIT license](LICENSE) for material distributed under this repository’s license. Linked third-party resources retain their own ownership and terms; this license does not grant rights to institutional instructional material. The guide supplies independent practice, not official lectures, restricted datasets, or assessed solutions.

To report an error or suggest an improvement, [open an issue](https://github.com/pskeffington/Dartmouth.HSE.Public/issues/new) with relevant public file paths and a brief description. Do not reproduce protected instructional material or personal data in a report.
