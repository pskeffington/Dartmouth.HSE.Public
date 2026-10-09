# Dartmouth Health Data Science — Public Learning Repository

**Teaching notes · Group exercises · Reusable statistical computing resources**

A public companion to graduate-level health data science coursework. Materials emphasize reproducible analysis, readable scientific explanations, and practical code examples. This is an independent educational repository, **not an official Dartmouth course website**.

## Start here

Open the **reading editions** below directly in GitHub. Each has links to its editable source. For a guided session, use the [follow-along guide](FOLLOW_ALONG.md); for short examples, keep the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md) and [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) open.

Current coverage: Weeks 1–4 lecture companions, Week 1–3 group work, and reusable resources. Capstone, final-project and assignment sections are reserved; no deliverables are posted there yet.

| I want to… | Go to |
| --- | --- |
| Follow a weekly lecture | [Lecture Notes](02_Lecture_Notes/) |
| Work through a classroom exercise | [Group Work](03_Group_Work/) |
| Generate descriptive statistics or annotated plots in R | [R Resources](06_RESOURCES/#r-statistics-and-visualization) |
| Study Bash, scripting, and data processing | [Bash Resources](06_RESOURCES/#bash-programming) |
| Prepare an APA 7 student manuscript | [LaTeX Template](06_RESOURCES/LaTeX/) |

## How I learned Bash

My introduction to Bash came through playing [Terminus](https://terminus-global.vercel.app/), a command-line adventure game. Exploring its world by typing commands made the terminal approachable and helped me learn through experimentation. That early experience grew into using Bash for file navigation, scripting, and reproducible data workflows.

### How I learned SSH and networking concepts

For an approachable introduction to remote systems and networking, I also recommend [Hacknet](https://store.steampowered.com/app/365450/Hacknet/), a terminal-driven simulation game. Its missions turn ideas such as remote connections, host discovery, ports, and navigating unfamiliar systems into interactive problems rather than vocabulary to memorize. I found this game-based approach a useful companion to learning command-line tools.

Hacknet uses a **fictional, simplified command environment**: it teaches concepts and curiosity, not the exact syntax or security practices of real SSH or network administration. To move from the game into a legitimate practice environment, start with your own computer or a lab machine you have permission to administer:

| Goal | Real-world command | What it does |
| --- | --- | --- |
| Connect to an authorized remote host | `ssh user@host.example` | Opens an encrypted remote shell |
| Copy a file securely | `scp report.csv user@host.example:~/` | Transfers a file over SSH |
| Confirm the host is reachable | `ping host.example` | Sends diagnostic echo requests (when permitted by the network) |
| Look up a hostname | `nslookup host.example` | Queries DNS |
| Inspect local network interfaces | `ip addr` (Linux) or `ifconfig` (macOS) | Displays local addressing information |
| Check a service you operate | `curl -I https://host.example` | Retrieves HTTP response headers |

**Learning path:** Play Terminus for terminal navigation, explore Hacknet for networking intuition, then practice SSH and diagnostics against your own local virtual machine or an explicitly authorized training host. Use SSH keys, verify host fingerprints, and never attempt access to systems without permission.

## Course materials

Each group walkthrough opens with session checkpoints. Use them to pause, check output and explain the method to a partner. For figures, keep the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) beside the code.

| Week | Lecture | Group work |
| --- | --- | --- |
| 1 | [Introduction to R lecture notes](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) | [Data types, indexing, and functions](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) |
| 2 | [Learning objective notes](02_Lecture_Notes/Week_2_Learning_Objective_Notes.md) | [Data wrangling and visualization](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) |
| 3 | [Learning objective notes](02_Lecture_Notes/Week_3_Learning_Objective_Notes.md) | [Simulation and reusable functions](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) |
| 4 | [Introduction to Bash](02_Lecture_Notes/Week_4_Introduction_to_Bash_Narrative_Walkthrough.md) | Execution materials maintained privately |

## Repository organization

| Section | Contents |
| --- | --- |
| [Capstone](01_Capstone/) | Planning and synthesis, reserved for future public materials |
| [Lecture Notes](02_Lecture_Notes/) | Explanatory lecture companions and learning objectives |
| [Group Work](03_Group_Work/) | Narrative exercises and runnable lab files |
| [Final Project](04_Final_Project/) | Public-facing final-project materials when approved for release |
| [Assignments](05_Assignments/) | Assignment-related teaching materials when appropriate to share |
| [RESOURCES](06_RESOURCES/) | R functions, statistical plots, Bash utilities, LaTeX templates and literature |

## Private execution boundary

Continued analysis, lab execution scripts, local datasets and generated outputs are maintained exclusively in the private repository.

## Scientific and academic-use notes

The examples distinguish exploratory visualization from statistical inference. Statistical interpretation requires documented sample sizes, missingness, measurement units, study design and tested assumptions. Gene-expression log-CPM displays do not substitute for count-based differential-expression models.

Some lectures and exercises require files distributed separately through the course. Their absence is noted; unexecuted or unavailable results are not presented as verified findings. Respect course collaboration, attribution, sharing and AI-use policies.

See [RESOURCES](06_RESOURCES/) for references, tests, installation requirements and reproducibility guidance. [License](LICENSE).
