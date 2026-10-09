# Dartmouth Health Data Science — Public Learning Repository

**Original method notes · Course-dependent study references · Independent computing resources**

A public companion to graduate-level health data science coursework. Materials emphasize reproducible analysis, readable scientific explanations, and practical code examples. This is an independent educational repository, **not an official Dartmouth course website**. The lecture and group-work sections do **not** provide the original Geisel lectures, questions, data, or assessed solutions; an authorized reader must obtain those separately to complete coursework.

## Start here

Open the **reading editions** below directly in GitHub. Each has links to its editable source. For a guided session, use the [follow-along guide](FOLLOW_ALONG.md); for short examples, keep the [R function sheet](06_RESOURCES/R/EASY_FUNCTION_SHEET.md) and [Bash command sheet](06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) open.

Current coverage: Weeks 1–4 independently authored conceptual notes, Week 1–3 course-dependent methodology references, and general-purpose resources. Capstone, final-project and assignment sections are reserved; no deliverables are posted there yet.

| I want to… | Go to |
| --- | --- |
| Follow a weekly lecture | [Lecture Notes](02_Lecture_Notes/) |
| Review methods before using the official exercise | [Group Work](03_Group_Work/) |
| Generate descriptive statistics or annotated plots in R | [R Resources](06_RESOURCES/#r-statistics-and-visualization) |
| Study Bash, scripting, and data processing | [Bash Resources](06_RESOURCES/#bash-programming) |
| Prepare an APA 7 student manuscript | [LaTeX Template](06_RESOURCES/LaTeX/) |

## How I learned Bash

My introduction to Bash came through playing [Terminus](https://terminus-global.vercel.app/), a command-line adventure game. Exploring its world by typing commands made the terminal approachable and helped me learn through experimentation. That early experience grew into using Bash for file navigation, scripting, and reproducible data workflows.

### How I learned SSH and networking concepts

For an approachable introduction to remote systems and networking, I also recommend [Hacknet](https://store.steampowered.com/app/365450/Hacknet/), a terminal-driven simulation game. Its missions turn ideas such as remote connections, host discovery, ports, and navigating unfamiliar systems into interactive problems rather than vocabulary to memorize. I found this game-based approach a useful companion to learning command-line tools.

Another useful option is [Hack RUN](https://store.steampowered.com/app/378110/Hack_RUN/), a command-prompt adventure that uses simulated DOS- and UNIX-style environments. It makes navigating directories, reading files, and recognizing basic command patterns part of solving the game's puzzles. Rather than memorizing a printed command list, players repeatedly retrieve and apply commands to make progress. That task-driven repetition can support familiarity and recall of basic computational operations; transferring the skill to a real terminal still requires practice with actual commands.

Hacknet and Hack RUN use **fictional, simplified command environments**: it teaches concepts and curiosity, not the exact syntax or security practices of real SSH or network administration. To move from the game into a legitimate practice environment, start with your own computer or a lab machine you have permission to administer:

| Goal | Real-world command | What it does |
| --- | --- | --- |
| Connect to an authorized remote host | `ssh user@host.example` | Opens an encrypted remote shell |
| Copy a file securely | `scp report.csv user@host.example:~/` | Transfers a file over SSH |
| Confirm the host is reachable | `ping host.example` | Sends diagnostic echo requests (when permitted by the network) |
| Look up a hostname | `nslookup host.example` | Queries DNS |
| Inspect local network interfaces | `ip addr` (Linux) or `ifconfig` (macOS) | Displays local addressing information |
| Check a service you operate | `curl -I https://host.example` | Retrieves HTTP response headers |

**Learning path:** Play Terminus for terminal navigation, use Hack RUN for repeated command-prompt navigation and file inspection, explore Hacknet for networking intuition, then practice SSH and diagnostics against your own local virtual machine or an explicitly authorized training host. Use SSH keys, verify host fingerprints, and never attempt access to systems without permission.

## Course materials

The public group-work files now contain original method-level checkpoints, not assigned questions or runnable solutions. Consult authorized Geisel course files for the actual exercise, source schema, and grading requirements. For figures, keep the [plot-reading guide](06_RESOURCES/READING_PLOTS.md) beside the code.

| Week | Lecture | Group work |
| --- | --- | --- |
| 1 | [Introduction to R lecture notes](02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) | [Data types, indexing, and functions](03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) |
| 2 | [Lecture methods + mastery](02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) | [Data wrangling and visualization](03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md) |
| 3 | [Lecture methods + mastery](02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) | [Simulation and reusable functions](03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md) |
| 4 | [Introduction to Bash](02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) | Execution materials maintained privately |

## Repository organization

| Section | Contents |
| --- | --- |
| [Capstone](01_Capstone/) | Planning and synthesis, reserved for future public materials |
| [Lecture Notes](02_Lecture_Notes/) | Explanatory lecture companions and learning objectives |
| [Group Work](03_Group_Work/) | Non-executable conceptual notes; official prompts and local inputs required |
| [Final Project](04_Final_Project/) | Public-facing final-project materials when approved for release |
| [Assignments](05_Assignments/) | Public-sharing policy only; no assignments, prompts, or solutions |
| [RESOURCES](06_RESOURCES/) | R functions, statistical plots, Bash utilities, LaTeX templates and literature |

## Originality and public-release screening

Follow the [gated originality roadmap](ORIGINALITY_ROADMAP.md), [provisional provenance register](PROVENANCE_REGISTER.md), and [historical exposure review](HISTORY_EXPOSURE_REVIEW.md) for completed remediation, remaining manual comparisons, generated-edition checks, and historical repository review. The repository is not certified copyright-cleared.

This repository is an **independent student-authored learning resource**, not an official Dartmouth publication. The intent is to publish original explanations, original example code, and appropriately credited references—not to redistribute restricted instructional materials.

A [scheduled GitHub Actions originality check](.github/workflows/originality-screen.yml) runs on every push to `main`, every pull request, every Monday, and through manual workflow dispatch. [View run results](https://github.com/pskeffington/Dartmouth.HSE.Public/actions/workflows/originality-screen.yml). A reproducible, standard-library-only [originality screening tool](scripts/check_public_originality.py) checks Git-tracked files for potentially restricted document formats, course-material filename patterns, publication-restriction language, course-platform exports, and binary/media assets requiring manual rights review.

```bash
python3 scripts/check_public_originality.py
python3 scripts/check_public_originality.py --json
python3 scripts/check_public_originality.py --json --fail-on-review  # strict CI-style gate
```

| Result | Interpretation | Action |
| --- | --- | --- |
| `SCREEN_CLEAR` | No configured indicators were detected | Still verify authorship, licensing, and source attribution |
| `REVIEW` | File(s) need a provenance/permissions check | Inspect each flagged file before public release; CI fails closed |
| `BLOCK` | Potentially restricted material detected | Remove, replace, or document redistribution authorization |

The same workflow also publishes a **per-file SHA256 provenance inventory** as a short-lived Actions artifact. Run `python3 scripts/build_provenance_inventory.py --output provenance-inventory.json` in a local checkout to reproduce it. All inventory records are marked unverified; hashes demonstrate file identity only, not originality or permission. Review the register and historical exposure report before release.

**This validator is a screening gate, not proof of originality or legal clearance.** It does not compare text with Dartmouth source materials, inspect historical Git commits or untracked files, or verify third-party permissions. Flagged content must be reviewed by a person. See the [originality and rights policy](ORIGINALITY_POLICY.md) for the publication standard and manual review requirements.

## Private execution boundary

Course instructions, instructor source code, official datasets, assessed solutions, lab execution scripts, local results, and submissions must remain in an authorized private workspace. The public materials do not reconstruct course assignments. The independent general-purpose R, Bash, and LaTeX resources are educational tools, not Geisel course substitutes.

## Scientific and academic-use notes

The examples distinguish exploratory visualization from statistical inference. Statistical interpretation requires documented sample sizes, missingness, measurement units, study design and tested assumptions. Gene-expression log-CPM displays do not substitute for count-based differential-expression models.

Course-specific exercises and verification require original files distributed separately through the course. Their absence is noted; unexecuted or unavailable results are not presented as verified findings. Respect course collaboration, attribution, sharing and AI-use policies.

See [RESOURCES](06_RESOURCES/) for references, tests, installation requirements and reproducibility guidance. [License](LICENSE).

## Repository originality status

See the [total repository status](ORIGINALITY_STATUS.md), [completion roadmap](ORIGINALITY_ROADMAP.md), and [provenance register](PROVENANCE_REGISTER.md). Current status is **REVIEW REQUIRED**; passing technical checks does not establish authorship or redistribution permission.
