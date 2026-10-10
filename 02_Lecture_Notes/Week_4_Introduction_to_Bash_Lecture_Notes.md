# Paul's Notes · Week 4: Bash and Scientific Metadata

[Section index](README.md) · [Editable R Markdown](Week_4_Introduction_to_Bash_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose and dependencies](#purpose-and-dependencies)
- [Terminal, shell, and location](#terminal-shell-and-location)
- [Small scientific metadata illustration](#small-scientific-metadata-illustration)
- [Search, fields, and failure status](#search-fields-and-failure-status)
- [Automation and the R bridge](#automation-and-the-r-bridge)
- [Misconceptions and self-check](#misconceptions-and-self-check)

## Purpose and dependencies

Use this conceptual reference with the [complete Week 4 lesson](../03_Group_Work/Week_4_Bash_and_Reproducible_Workflows_Study_Guide.md). **Study time:** 25–35 minutes. **Prerequisites:** file paths and Week 1 data checks. **Dependencies:** Bash 3.2+ and standard utilities; the full workflow also needs base Rscript. PowerShell is a different command language.

## Terminal, shell, and location

A terminal is an interface; a shell interprets commands. Bash executes interactive commands or saved scripts. Rscript launches a separate R process. A working directory gives meaning to relative paths; an absolute path begins at the filesystem root. Do not paste R console prompts into Bash or Bash prompts into R.

| Command | Research use |
| --- | --- |
| `pwd`, `cd`, `ls` | Inspect/change location and list files |
| `mkdir -p` | Create deliberate input/output directories |
| `head`, `tail`, `cat` | Inspect the beginning, end, or complete text |
| `wc -l` | Count newline characters, usually including a header |
| `cp`, `mv` | Copy or relocate; inspect destinations for overwrite risk |
| `rm` | Remove an exact disposable file after checking its path |

Quoting `"$path"` preserves spaces and argument boundaries. `>` creates/replaces output, `>>` appends, and `|` connects standard output to standard input. `2>&1` sends errors to the same destination as output when ordered appropriately.

## Small scientific metadata illustration

This block creates a fresh temporary directory with a two-participant, one-specimen-per-person CSV. Measurements are invented creatinine values in mg/dL; the labels describe specimen type, not treatment.

```bash
reference_dir=$(mktemp -d "${TMPDIR:-/tmp}/pauls-bash-reference.XXXXXX")
printf 'Participant_ID,Sample_Type,Measurement
Z01,Serum,0.9
Z02,Plasma,1.1
' > "$reference_dir/samples.csv"
head -n 3 "$reference_dir/samples.csv"
awk -F ',' 'NR == 1 || $2 == "Serum"' < "$reference_dir/samples.csv" > "$reference_dir/serum.csv"
awk 'END {print (NR > 0 ? NR - 1 : 0)}' < "$reference_dir/serum.csv"
printf 'Practice directory: %s
' "$reference_dir"
```

**Expected:** the header and two input records, then selected record count `1`. The header stays in the output. This is a simple delimiter-separated format; quoted commas, embedded newlines, or a different separator need a real parser. The full lesson validates schema, keys, categories, ages, and measurement strings before publishing a filtered file.

## Search, fields, and failure status

`grep -F` finds literal text anywhere in a line; `awk -F ','` addresses fields in this simple format. Text search does not establish which field matched. Pipelines report the last command's status by default; `set -o pipefail` also exposes earlier failures. Grep status 1 is an expected no-match, whereas an error means inspection failed. Handle known failure cases in `if` rather than assuming every nonzero status means absent data.

`set -euo pipefail` helps expose command failures and unset variables but does not validate scientific data. A script should check argument count before `$1`, validate readable input and distinct output, build a temporary result, and move it into place only after success. A trap cleans temporary output on exit. Retain raw inputs and verify selected record counts.

## Automation and the R bridge

A `for` loop applies one operation to known labels or quoted file paths. A glob with no matches needs an explicit file test. Avoid parsing `ls` output to build a file list. `$@` preserves positional argument boundaries when quoted; functions should return meaningful exit status.

The following is an invocation pattern, requiring a saved script and valid paths rather than an additional runnable example:

```text
Rscript --vanilla summarize_samples.R input.csv output.csv 2 > run.log 2>&1
```

The R script reads `commandArgs(trailingOnly = TRUE)`, checks its argument contract, parses CSV, validates fields, and computes summaries. Bash manages paths and logging; R manages numerical analysis. The full lesson supplies both scripts and checks their actual outputs, including withheld means when observed counts are insufficient.

## Misconceptions and self-check

Explain relative paths, quoting, headers, and the difference between physical lines and data records. Predict what a missing file, wrong delimiter, invalid category, or duplicate identifier should do. Distinguish a printed error from a failed process and a partial output from a validated result. Demonstrate filesystem operations only in a disposable workspace; never apply broad deletion patterns to study inputs.

[Previous topic](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) · [Topic index](README.md) · [Command sheet](../06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) · [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
