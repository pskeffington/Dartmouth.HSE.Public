# Paul's Notes — Week 4: Introduction to Bash

[Section index](README.md) · [Editable R Markdown](Week_4_Introduction_to_Bash_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The weekly teaching guides provide synthetic inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose: the shell as a reproducible research interface](#purpose-the-shell-as-a-reproducible-research-interface)
- [1. Shells, Bash, and computational research](#1-shells-bash-and-computational-research)
- [2. Navigating and organizing a filesystem](#2-navigating-and-organizing-a-filesystem)
- [3. Inspecting research files without loading everything](#3-inspecting-research-files-without-loading-everything)
- [4. Scripts, shebangs, and reproducibility](#4-scripts-shebangs-and-reproducibility)
- [5. Pipes, redirection, and columns](#5-pipes-redirection-and-columns)
- [6. Conditionals and loops](#6-conditionals-and-loops)
- [7. Bash and R: division of responsibility](#7-bash-and-r-division-of-responsibility)
- [Scholarly synthesis](#scholarly-synthesis)
- [8. General-purpose shell workflow and verification](#8-general-purpose-shell-workflow-and-verification)
- [9. Final self-check: what Week 4 mastery requires](#9-final-self-check-what-week-4-mastery-requires)

## Purpose: the shell as a reproducible research interface

Learn Bash navigation, scripts, pipelines, and responsible file handling. This independent public study guide is not an official Dartmouth or Geisel publication.

These public examples require no official instructional files. Course-specific requirements belong to authorized course channels.

## 1. Shells, Bash, and computational research

A shell interprets instructions typed at a command line. Bash (Bourne Again SHell) can also run saved sequences of instructions, converting an interactive procedure into a repeatable workflow. Bash belongs to the family of Unix command interpreters.

For data science, shell operations are especially useful when dozens of study files need the same organization or when scripts must launch an R analysis on a cluster. Schedulers such as SLURM manage jobs on computing clusters. Bash coordinates tasks and paths; the scientific model remains the responsibility of the analysis language and its validated inputs.

## 2. Navigating and organizing a filesystem

The central idea is *location awareness*: every relative path is interpreted against a working directory. This explains why a command may run correctly from one directory but fail elsewhere.

```bash
pwd                          # Print the current directory
current_dir=$(pwd)            # Store command output in a variable
printf 'Working in %s\n' "$current_dir"
ls -lah                       # Include hidden files and human-readable sizes
cd "$HOME"                    # Return home
cd ..                         # Move to parent directory
mkdir -p my_project/data      # Create nested directories
```

`cp` duplicates files, `mv` relocates or renames them, `cat` displays complete text, and `rm` deletes entries. These operations are important for source provenance: a renamed or overwritten file can break the connection between analysis and input. **Practice check:** work inside a disposable exercise directory and check the target before any recursive deletion.

**Optional game-based reinforcement:** [Terminus](https://terminus-global.vercel.app/) introduces terminal navigation through a command-line adventure; [Hack RUN](https://store.steampowered.com/app/378110/Hack_RUN/) uses simulated DOS/UNIX-style command prompts to make inspecting files and moving through a system part of solving puzzles; [Hacknet](https://store.steampowered.com/app/365450/Hacknet/) introduces simulated remote-system exploration. Requiring a player to recall and apply navigation commands repeatedly can encourage retrieval practice and make basic operations more familiar than passive reading alone. These games use simplified interfaces, so they supplement rather than replace practice in a real, authorized terminal.

**Mastery transfer:** Without following a game walkthrough, open a local terminal and demonstrate `pwd`, `ls`, `cd`, and `head` on a disposable exercise directory. Explain the working directory and relative path at each step.

## 3. Inspecting research files without loading everything

A hypothetical gene-by-sample table, `data.csv`, illustrates `head`, `tail`, `less`, and `wc`. In this example, rows are genes and columns are samples; displaying a header is therefore a preliminary schema check, not a statistical analysis.

```bash
head -n 5 data.csv            # Preview the header and first observations
tail -n 5 data.csv            # Inspect the end of the file
wc -l data.csv                # Count newline-terminated lines
less data.csv                 # Search interactively; press q to exit
```

The printed line count usually includes a header. A file without a final newline may require additional care when interpreting `wc -l`. The commands reveal file shape and superficial structure; they do not establish whether sample IDs, gene identifiers, or counts are valid.

## 4. Scripts, shebangs, and reproducibility

A saved Bash script converts a list of manual commands into repeatable instructions. The shebang identifies the interpreter, while execute permissions allow direct invocation.

```bash
#!/usr/bin/env bash
set -euo pipefail

# Paths are relative to the directory from which this script is executed.
input="data.csv"
[[ -f "$input" ]] || { printf 'Missing: %s\n' "$input" >&2; exit 1; }
mkdir -p my_project/data
cp "$input" my_project/data/rnaseq_dat.csv
touch my_project/notes.txt
ls -l my_project/data
```

```bash
bash -n my_first_bash_script.sh  # Check syntax
bash my_first_bash_script.sh     # Run explicitly
# chmod +x my_first_bash_script.sh  # Optional direct-execution setup
```

**Practice check:** quoting variables, checking files, and using `set -euo pipefail` improve reliability but do not guarantee correctness. Treat script outputs as evidence only after validating inputs and confirming the intended transformations.

## 5. Pipes, redirection, and columns

A pipe connects one program's output to the next program's input. Redirection writes output to a file: `>` replaces an existing file, whereas `>>` appends. Use `grep`, `awk`, and `cut` for small inspection and extraction tasks.

```bash
grep -F 'ESR1' gene_list.txt          # Literal search
awk -F ',' 'NR == 1 {print $2}' data.csv
cut -d ',' -f 1,3 data.csv
```

**Practice check:** the `awk -F ','` and `cut -d ','` examples assume simple delimiter-separated records. They do not correctly parse arbitrary quoted CSV, particularly cells containing commas or newlines. Use a CSV-aware parser in R or Python for such data. For listing CSV files, globbing (`*.csv`) is generally safer than parsing `ls` output.

## 6. Conditionals and loops

Conditional statements let a script branch according to a test; loops repeat the same operation across files or records. The `if ... then ... else ... fi`, `for`, and `while` examples demonstrate decision-making and iteration.

```bash
if [[ -f "data.csv" ]]; then
  printf 'data.csv exists\n'
else
  printf 'data.csv is missing\n'
fi

for file in ./*.csv; do
  [[ -f "$file" ]] || continue
  printf 'Previewing %s\n' "$file"
  head -n 5 "$file"
done

count=5
while [[ "$count" -gt 0 ]]; do
  printf '%s\n' "$count"
  count=$((count - 1))
done
```

The loop body is one analytical rule applied repeatedly; changing that rule changes every processed file. That is why one validated function is generally preferable to many manually edited commands.

## 7. Bash and R: division of responsibility

Bash can launch R scripts and pass arguments. This is a useful research pattern because data locations and job scheduling can be managed without embedding them throughout an R model.

```bash
Rscript --vanilla analysis.R input.csv output.csv 10
```

```r
args <- commandArgs(trailingOnly = TRUE)
stopifnot(length(args) == 3L)
input_file <- args[1]
output_file <- args[2]
n <- as.numeric(args[3])
if (is.na(n)) stop("n must be numeric")
# read, validate, analyze and write within a deliberate R workflow
```

Bash can pass arguments and redirect console output, but it cannot establish biological validity or inferential confidence. The [Bash operation sheet](../06_RESOURCES/Bash/BASH_OPERATION_SHEET.md) and [function library](../06_RESOURCES/Bash/bash_functions.sh) provide further practice.

## Scholarly synthesis

The methodological progression is from *where the data reside*, to *what the data contain*, to *how operations are repeated and documented*. Students should be able to explain which commands inspect data, which transform it, and which may permanently alter it. They should also be able to show that the shell's orchestration logic is distinct from substantive R statistical analysis.

**Execution boundary:** Commands using external paths are illustrative templates requiring your own inputs. Section 8 supplies a self-contained practice session with known text output.

## 8. General-purpose shell workflow and verification

The workflow moves from finding files to inspecting content, automating repeated operations, and invoking R. Practise that complete sequence in a disposable folder before applying it to coursework. The following is a **self-contained practice example**, not an assignment solution.

```bash
# Run within a disposable directory created for this exercise.
mkdir -p week4_practice
cd week4_practice
printf 'sample,value\na,4\nb,9\n' > measurements.csv

pwd
head -n 3 measurements.csv
wc -l measurements.csv

# Check for a valid input before processing it.
if [[ -f measurements.csv ]]; then
  printf 'Input exists\n'
fi
```

**Why it works:** `mkdir` establishes an explicit working location; `printf` writes known practice content; `head` and `wc` inspect text without loading R; `[[ -f ... ]]` confirms a file is present. The count includes the header. The practice command uses `>`, which overwrites the file if it already exists: run it only in a disposable location.

**Mastery checkpoint:** Describe which lines create files, which inspect them, and which conditionally branch. Identify the exact working directory that determines where `measurements.csv` is found.

## 9. Final self-check: what Week 4 mastery requires

Mark an objective only when you can demonstrate it in a clean practice directory and explain its effect.

- [ ] **Shell model:** Distinguish an interactive shell, a script, and the R process it launches.
- [ ] **Navigation:** Use `pwd`, `ls`, and `cd` to resolve relative versus absolute paths and recover from a wrong directory.
- [ ] **File inspection:** Use `head`, `tail`, `wc`, and `less` to inspect a text dataset without confusing line counts with data-record counts.
- [ ] **Safe file operations:** Demonstrate `mkdir`, `cp`, and `mv` in a disposable directory; explain overwrites and why `rm` requires explicit care.
- [ ] **Reproducible scripts:** Create a shebang-based Bash script, quote variable expansions, check syntax with `bash -n`, and run it.
- [ ] **Pipes and columns:** Explain standard input/output, `|`, `>`, and `>>`; demonstrate a safe text extraction and identify cases where naive CSV splitting is invalid.
- [ ] **Control flow:** Write an `if` condition and a file loop that do not fail when optional inputs are absent.
- [ ] **Bash-to-R bridge:** Explain and demonstrate how `Rscript` receives positional arguments through `commandArgs(trailingOnly = TRUE)`.
- [ ] **Reproducibility boundary:** Record inputs, commands, validation evidence, and outputs; distinguish a script that completes from a scientifically valid result.

**Mastery standard:** All nine objectives demonstrated in an authorized practice workspace. A peer can follow your script from a clean directory, identify each file operation and argument, and reproduce the expected text output without guessing hidden paths.

**Related:** [Bash operation sheet](../06_RESOURCES/Bash/BASH_OPERATION_SHEET.md) · [Bash utility examples](../06_RESOURCES/Bash/bash_functions.sh) · [Topic index](README.md)

[Previous topic](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) · [Paul's Notes](../README.md)
