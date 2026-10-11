# Paul's Notes · Week 4: Bash and Reproducible Workflows

[Section index](README.md) · [Editable R Markdown](Week_4_Bash_and_Reproducible_Workflows_Study_Guide.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

Use Bash to organize files, inspect a small table, validate and filter records, automate repeated work, and pass explicit arguments to R. The invented data describe adult participant blood-sample metadata and synthetic creatinine measurements in mg/dL. Every input needed for this lesson is created below.

**Study time:** 90–120 minutes. **Prerequisites:** Weeks 1–3 data checks and summaries. Use a Bash shell, not a PowerShell prompt. The examples work with Bash 3.2 or newer and standard `awk`, `grep`, `head`, `tail`, `wc`, `sort`, `uniq`, `mktemp`, and file utilities. The final bridge needs `Rscript` with base R; no add-on R packages are required. Python is needed only for the optional automated lesson check.

Copy the blocks into one Bash session in order, or save them in a script. The `.Rmd` is the editable lesson; read its Markdown edition directly on GitHub. The named Bash chunks are for the validation tool and are not instructions to knit shell commands in RStudio.

[Previous: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md) · [Weekly index](README.md) · [Topic companion](../02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) · [Paul's Notes](../README.md)

## On this page

- [Scientific motivation](#scientific-motivation)
- [Learning objectives](#learning-objectives)
- [1. Check tools and create a practice workspace](#1-check-tools-and-create-a-practice-workspace)
- [2. Create and inspect known data](#2-create-and-inspect-known-data)
- [3. Make a reusable filter with validation](#3-make-a-reusable-filter-with-validation)
- [4. Check an expected failure](#4-check-an-expected-failure)
- [5. Automate two filters and verify record counts](#5-automate-two-filters-and-verify-record-counts)
- [6. Write an R script with a clear argument contract](#6-write-an-r-script-with-a-clear-argument-contract)
- [7. Run the bridge, record logs, and check results](#7-run-the-bridge-record-logs-and-check-results)
- [8. What to keep and how to rerun](#8-what-to-keep-and-how-to-rerun)
- [Common mistakes and debugging](#common-mistakes-and-debugging)
- [Independent practice](#independent-practice)
- [Ready to move on](#ready-to-move-on)
- [Next steps and references](#next-steps-and-references)
- [Weekly Learning Objectives & Mastery Assessment](#weekly-learning-objectives--mastery-assessment)

## Scientific motivation

Research workflows connect a specimen identifier to its metadata, transformation commands, and numerical output. File operations can break that connection by changing headers, losing records, or replacing inputs. Validate the row unit and schema before computing summaries. The age bounds and category vocabulary here are a toy adult-data contract, not eligibility rules for a real study.

## Learning objectives

By the end, you should be able to explain relative paths and quoting, distinguish line counts from record counts, validate a simple delimiter-separated table, write a script with positional arguments and clear errors, handle expected no-match results, loop over files safely, and separate shell orchestration from R calculations.

## 1. Check tools and create a practice workspace

A shell interprets commands; a directory determines how relative paths resolve. Work in a new temporary directory so these examples do not replace existing files. Keep the printed path if you want to inspect the results later.

```bash
set -euo pipefail
for tool in awk grep head tail wc sort uniq mktemp cp mv rm ls Rscript; do
  command -v "$tool" >/dev/null 2>&1 || {
    printf 'Required command unavailable: %s\n' "$tool" >&2
    exit 1
  }
done
practice_dir=$(mktemp -d "${TMPDIR:-/tmp}/pauls-week4.XXXXXX")
cd "$practice_dir"
mkdir -p input output scripts logs
printf 'Practice workspace: %s\n' "$PWD"
```

**Expected:** one new workspace with four empty subdirectories. `$(...)` captures command output. Quoting preserves paths containing spaces. `set -euo pipefail` helps detect unset variables and failed commands, but it does not validate a dataset or make every failure case equivalent. The later `if` statements handle expected failures deliberately.

On Windows, use a Bash environment and ensure Rscript is visible within that environment. If `command -v Rscript` prints nothing, fix its installation or PATH before continuing. Do not confuse the R console prompt with a shell prompt.

### Location awareness and disposable file operations

An absolute path begins at the filesystem root; a relative path starts at the current directory. Inspect both before copying, moving, or deleting. Only the tiny note created in this block is removed; inputs and results remain available.

```bash
pwd
ls -lh
absolute_input_dir="$PWD/input"
[[ -d "$absolute_input_dir" ]]
printf 'Disposable practice note\n' > logs/practice_note.tmp
cp -- logs/practice_note.tmp logs/note_copy.tmp
mv -- logs/note_copy.tmp logs/note_renamed.tmp
[[ -f logs/note_renamed.tmp ]]
rm -- logs/practice_note.tmp logs/note_renamed.tmp
[[ ! -e logs/note_renamed.tmp ]]
```

**Expected:** the absolute workspace and its directories are printed; the two disposable notes are absent afterward. `cp` copies, `mv` moves or renames, and `rm` removes. Deletion is immediate; inspect exact paths first, keep raw data, and avoid broad recursive patterns. `--` ends option parsing for these utilities on the supported macOS/Linux environments.

## 2. Create and inspect known data

The row unit is one blood specimen from one invented participant; this example has only one specimen per participant. `Participant_ID` is its unique key. `Sex` is a simplified fictional recorded Female/Male category; `Age` is integer years; `Sample_Type` is Plasma or Serum; `Measurement` is synthetic creatinine in mg/dL or literal `NA`. Plasma and serum name specimen types, not treatment groups. Repeated specimens would need a participant-plus-specimen key. This lesson uses simple comma-delimited records with no quoted commas or embedded newlines. General CSV needs a CSV-aware parser such as R's `read.csv()`.

```bash
cat > "input/sample metadata.csv" <<'CSV'
Participant_ID,Sex,Age,Sample_Type,Measurement
M01,Female,41,Plasma,0.8
M02,Male,52,Serum,1.1
M03,Female,36,Plasma,NA
M04,Male,64,Serum,1.3
M05,Female,47,Plasma,1.2
CSV
head -n 3 "input/sample metadata.csv"
tail -n 1 "input/sample metadata.csv"
wc -l < "input/sample metadata.csv"
awk 'END {print (NR > 0 ? NR - 1 : 0)}' < "input/sample metadata.csv"
```

**Expected:** the header and first two sample records, followed by the final M05 record; then `6` lines and `5` data records. `wc -l` counts newline characters, including the header here. A missing final newline can affect it. The quoted heredoc delimiter (`'CSV'`) keeps its contents literal rather than expanding shell variables.

Select participant identifiers and measurements by field position into a new file, keeping a new explicit header:

```bash
awk -F ',' 'BEGIN {print "Participant_ID,Measurement"}
            NR > 1 {print $1 "," $5}' < "input/sample metadata.csv" > output/measurements_only.csv
head -n 3 output/measurements_only.csv
[[ $(awk 'END {print NR}' < output/measurements_only.csv) -eq 6 ]]
```

**Expected:** the two-column header, M01/0.8 and M02/1.1, and six physical records including the header. Field 5 is Measurement; verify the schema before extracting. The unavailable value stays NA. This projection is for inspection, not the five-column input expected by the checked filter below.

Before calculating a mean, count unavailable values:

```bash
awk -F ',' 'NR > 1 && $5 == "NA" {missing++}
            END {print "Missing measurements:", missing + 0}' < "input/sample metadata.csv"
if grep -Fq 'unknown-marker' "input/sample metadata.csv"; then
  printf 'Marker found\n'
else
  search_status=$?
  if [[ "$search_status" -ne 1 ]]; then
    printf 'Search failed with status %s\n' "$search_status" >&2
    exit "$search_status"
  fi
  printf 'Marker absent\n'
fi
```

**Expected:** one missing measurement and `Marker absent`. Grep status `1` means no match; a larger status indicates an error. A no-match result is useful evidence, whereas an unreadable file is a failure to inspect it. Text search is not the same as selecting rows by a specific field.

A pipeline connects standard output from one command to standard input of the next. Count specimens per type by extracting field 4, sorting labels, and counting adjacent repetitions:

```bash
awk -F ',' 'NR > 1 {print $4}' < "input/sample metadata.csv" | sort | uniq -c
```

**Expected:** three Plasma labels and two Serum labels. `uniq` counts adjacent repeats, so sorting first matters. `pipefail` makes a pipeline report a failed earlier command instead of relying only on its last command. This is still a text-format calculation, not a general CSV parser.

## 3. Make a reusable filter with validation

A script receives arguments through `$1`, `$2`, and `$3`. Validate the argument count before reading those variables when `set -u` is enabled. The script below takes an input file, an output file, and one specimen-type label. It validates every row, including rows that are not selected.

```bash
cat > scripts/filter_samples.sh <<'BASH'
#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then
  printf 'Usage: filter_samples.sh input.csv output.csv Plasma|Serum\n' >&2
  exit 2
fi
input_file=$1
output_file=$2
sample_type=$3
[[ -r "$input_file" && -f "$input_file" ]] || {
  printf 'Unreadable input: %s\n' "$input_file" >&2
  exit 1
}
[[ "$sample_type" == Plasma || "$sample_type" == Serum ]] || {
  printf 'Sample type must be Plasma or Serum\n' >&2
  exit 2
}
if [[ "$input_file" == "$output_file" || "$input_file" -ef "$output_file" ]]; then
  printf 'Input and output must differ\n' >&2
  exit 2
fi
# Build a temporary output beside its destination; publish only after validation.
temp_file=$(mktemp "${output_file}.XXXXXX")
trap 'rm -f -- "$temp_file"' EXIT
awk -F ',' -v wanted="$sample_type" '
  NR == 1 {
    if ($0 != "Participant_ID,Sex,Age,Sample_Type,Measurement") exit 1
    print
    next
  }
  $0 ~ /"/ || NF != 5 || $1 == "" || seen[$1]++ {exit 1}
  $2 != "Female" && $2 != "Male" {exit 1}
  $3 !~ /^[0-9]+$/ || $3 < 18 || $3 > 100 {exit 1}
  $4 != "Plasma" && $4 != "Serum" {exit 1}
  $5 != "NA" && $5 !~ /^[0-9]+([.][0-9]+)?$/ {exit 1}
  $4 == wanted {print}
  END {if (NR == 0) exit 1}
' < "$input_file" > "$temp_file" || {
  printf 'Invalid input: check header, fields, unique IDs, recorded sex, adult age, type, and measurement\n' >&2
  exit 1
}
mv -- "$temp_file" "$output_file"
BASH
bash -n scripts/filter_samples.sh
bash scripts/filter_samples.sh "input/sample metadata.csv" output/selected_plasma.csv Plasma
cat output/selected_plasma.csv
```

**Expected:** a header plus `M01,Female,41,Plasma,0.8`, `M03,Female,36,Plasma,NA`, and `M05,Female,47,Plasma,1.2`. The missing row is retained so the denominator remains visible. `bash -n` checks syntax without running the script. Explicit `bash script` does not require execute permission; a shebang plus `chmod +x` allows direct execution if desired.

The awk record checks reject duplicate IDs, missing fields, unknown specimen types, negative values, quoted fields, and undocumented measurement strings. They do not establish scientific validity. This deliberately small format excludes full CSV quoting and CRLF line endings; use R's CSV parser for other formats rather than weakening checks blindly. Temporary output prevents a failed validation from replacing an existing result. Reusing the output path in a successful call replaces that output intentionally.

## 4. Check an expected failure

A robust workflow demonstrates its failure behavior, not only its successful path. Duplicate the first data row in a separate practice file and confirm that no final output is created.

```bash
cp -- "input/sample metadata.csv" input/duplicate.csv
printf 'M01,Female,41,Plasma,0.8\n' >> input/duplicate.csv
if bash scripts/filter_samples.sh input/duplicate.csv output/rejected.csv Plasma; then
  printf 'Unexpected success for duplicate IDs\n' >&2
  exit 1
else
  filter_status=$?
  [[ "$filter_status" -eq 1 ]] || exit "$filter_status"
  printf 'Duplicate input rejected as expected\n'
fi
[[ ! -e output/rejected.csv ]]
```

**Expected:** an input-validation error followed by `Duplicate input rejected as expected`. The original input is unchanged. If a failure produces a partial final CSV, a downstream reader might mistake incomplete data for a valid result; that is why the script writes to a temporary path first.

## 5. Automate two filters and verify record counts

A loop applies one checked operation to several explicit values. A function performs one reusable calculation. Here the count excludes exactly one header; it is for the simple line-delimited format defined above.

```bash
count_data_records() {
  [[ $# -eq 1 ]] || { printf 'Usage: count_data_records file\n' >&2; return 2; }
  [[ -r "$1" && -f "$1" ]] || { printf 'Unreadable: %s\n' "$1" >&2; return 1; }
  awk 'END {print (NR > 0 ? NR - 1 : 0)}' < "$1"
}
for sample_type in Plasma Serum; do
  bash scripts/filter_samples.sh "input/sample metadata.csv" "output/type_${sample_type}.csv" "$sample_type"
  printf 'Sample type %s: %s records\n' "$sample_type" "$(count_data_records "output/type_${sample_type}.csv")"
done
[[ $(count_data_records output/type_Plasma.csv) -eq 3 ]]
[[ $(count_data_records output/type_Serum.csv) -eq 2 ]]
```

**Expected:** Plasma has three specimens, Serum has two. Filtering does not imply dropping missing measurements. The loop writes two clearly named outputs; a filename alone is not proof that the record count is correct.

To process discovered files, use a quoted glob loop rather than splitting `ls` output:

```bash
for file in output/type_*.csv; do
  [[ -f "$file" ]] || continue
  printf 'Inspecting %s\n' "$file"
  head -n 2 "$file"
done
```

**Expected:** the two `type_Plasma.csv` and `type_Serum.csv` files are inspected separately. The explicit file test handles a pattern with no matches. All paths inside the loop remain quoted.

## 6. Write an R script with a clear argument contract

Bash should manage paths and execution; R should parse CSV and calculate numerical summaries. This script takes an input CSV, an output CSV, and the minimum observed count needed to report a descriptive mean. This is a practice reporting rule, not a study-design calculation. It keeps total, measured, and missing counts separate.

```bash
cat > scripts/summarize_samples.R <<'RSCRIPT'
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3L) stop("Provide input.csv output.csv minimum_count")
minimum_count <- suppressWarnings(as.numeric(args[3]))
if (is.na(minimum_count) || !is.finite(minimum_count) ||
    minimum_count < 1 || minimum_count != floor(minimum_count)) {
  stop("minimum_count must be a positive integer")
}
if (!file.exists(args[1])) stop("Input file is missing")
if (normalizePath(args[1]) == normalizePath(args[2], mustWork = FALSE)) {
  stop("Input and output must differ")
}
sample_data <- read.csv(args[1], na.strings = "NA", stringsAsFactors = FALSE,
  colClasses = c(Participant_ID = "character", Sex = "character", Sample_Type = "character"))
if (!identical(names(sample_data), c("Participant_ID", "Sex", "Age", "Sample_Type", "Measurement"))) {
  stop("Expected Participant_ID, Sex, Age, Sample_Type, Measurement columns")
}
if (nrow(sample_data) == 0L || anyNA(sample_data$Participant_ID) ||
    any(sample_data$Participant_ID == "") || anyDuplicated(sample_data$Participant_ID)) {
  stop("Need nonempty, unique participant IDs")
}
if (anyNA(sample_data$Sample_Type) || !all(sample_data$Sample_Type %in% c("Plasma", "Serum"))) {
  stop("Sample type must be Plasma or Serum")
}
if (anyNA(sample_data$Sex) || !all(sample_data$Sex %in% c("Female", "Male"))) stop("Unknown recorded sex label")
if (!is.numeric(sample_data$Age) || anyNA(sample_data$Age) ||
    any(!is.finite(sample_data$Age)) || any(sample_data$Age != floor(sample_data$Age)) ||
    any(sample_data$Age < 18 | sample_data$Age > 100)) stop("Age must be integer years from 18 to 100")
# CSV may infer an entirely missing column as logical; retain numeric NA.
if (is.logical(sample_data$Measurement) && all(is.na(sample_data$Measurement))) {
  sample_data$Measurement <- as.numeric(sample_data$Measurement)
}
if (!is.numeric(sample_data$Measurement) || any(is.nan(sample_data$Measurement)) ||
    any(!is.finite(sample_data$Measurement[!is.na(sample_data$Measurement)])) ||
    any(sample_data$Measurement < 0, na.rm = TRUE)) {
  stop("Measurement must be finite nonnegative mg/dL or NA")
}
summary_rows <- lapply(sort(unique(sample_data$Sample_Type)), function(type_name) {
  values <- sample_data$Measurement[sample_data$Sample_Type == type_name]
  n_measured <- sum(!is.na(values))
  data.frame(
    Sample_Type = type_name, n_total = length(values), n_measured = n_measured,
    n_missing = sum(is.na(values)), eligible = n_measured >= minimum_count,
    mean_mg_dL = if (n_measured >= minimum_count) mean(values, na.rm = TRUE) else NA_real_
  )
})
sample_summary <- do.call(rbind, summary_rows)
write.csv(sample_summary, args[2], row.names = FALSE, na = "NA")
print(sample_summary)
RSCRIPT
```

**Expected:** the script file exists; writing it does not run R. The quoted heredoc preserves `$` in R column references. Identifier and categorical columns are explicitly imported as character, preserving leading zeros. A base-R script does not require RStudio. Values such as `two`, zero, a negative number, or `2.5` are invalid minimum-count arguments.

## 7. Run the bridge, record logs, and check results

```bash
Rscript --vanilla scripts/summarize_samples.R "input/sample metadata.csv" output/summary.csv 2 \
  > logs/summary.log 2>&1
cat logs/summary.log
cat output/summary.csv
```

**Expected:** Plasma has total `3`, measured `2`, missing `1`, and mean `1.0` mg/dL. Serum has total `2`, measured `2`, missing `0`, and mean `1.2` mg/dL. Both meet the minimum of two measured values. `2>&1` sends standard error to the same log destination as standard output; check the exit status as well as the log.

With a minimum of three measurements, both means should be withheld rather than presented as zero:

```bash
Rscript --vanilla scripts/summarize_samples.R "input/sample metadata.csv" output/minimum_three.csv 3
```

**Expected:** both `eligible` values are FALSE and both means are `NA`; record counts are unchanged. A threshold is a reporting rule, not a substitute for study design, uncertainty, or a clinically justified sample size. These invented values do not establish clinical status, specimen equivalence, or a population difference. Real assay comparisons need method validation and a suitable design.

## 8. What to keep and how to rerun

Keep the input definition, the two scripts, the output summaries, the run log, and a short explanation of missingness and denominators. Record your tool versions (`bash --version`, `Rscript --version`). To repeat the workflow, rerun the lesson in a fresh temporary workspace; avoid depending on objects or files left from an earlier attempt.

The optional automated checker parses every Bash chunk before executing the lesson in a separate process and checks its output files. Run it from the repository root:

```text
python3 scripts/validate_weekly_bash.py --output-dir /tmp/pauls-week4-checks
```

It requires the same tools as the lesson, including Rscript, and writes logs outside the repository. Keep the practice directory to inspect it; delete it later only after confirming its path and that it contains your disposable practice files.

## Common mistakes and debugging

| Symptom | Check and repair |
| --- | --- |
| `command not found` | Confirm the shell, installation, and PATH; use `command -v` for the named tool |
| `No such file` | Run `pwd`; compare relative paths with the current directory; keep spaces quoted |
| `$1` is unbound | Validate argument count before accessing positional arguments |
| Search exits with 1 | Distinguish an expected no-match from an error; handle the status in an `if` |
| Filter rejects input | Check the exact header, five-field layout, unique IDs, recorded categories, integer ages, and numeric/NA convention |
| R sees text measurements | Inspect the imported column and undocumented values; do not convert bad text to zero |
| Output count seems too large | Account for the header and any duplicate records; compare selected and original counts |
| Mean differs | Check the minimum measured count, missingness, units, and actual input file |

## Independent practice

1. Add Plasma specimens from new participants, one observed and one unavailable. Predict total, measured, missing, and the new mean before executing.
2. Supply an invalid specimen type, a duplicate ID, a negative measurement, and an input/output collision. Show that each fails without replacing a valid output.
3. Rename the input with spaces and rerun both scripts without changing their calculations.
4. Adapt the output loop to a third specimen type. Identify every schema check and argument contract that must change together.
5. Explain the difference between matching text with grep, selecting a field with awk, and parsing general CSV with R.

## Ready to move on

| Evidence | Completion check |
| --- | --- |
| Workspace | Four deliberate subdirectories; explain every relative path and quoted argument |
| Inputs and filter | Five known specimens; three Plasma and two Serum; one missing measurement; duplicate input rejected |
| Scripts and control flow | Trace positional arguments, one conditional, one loop, one function, and a nonzero status |
| R bridge | Report Plasma = 1.0 mg/dL and Serum = 1.2 mg/dL with measured counts of two; explain the withheld means at minimum three |
| Reproducibility | Rerun from a fresh workspace and compare structures and counts; keep a methods note and log |

Explain which commands create, inspect, transform, or replace files. Why must a missing measurement stay in the total count? What evidence shows the script failed safely rather than merely printed an error?

## Next steps and references

[Previous: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md) · [Weekly lessons](README.md) · [Bash topic companion](../02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) · [Command sheet](../06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) · [Operation sheet](../06_RESOURCES/Bash/BASH_OPERATION_SHEET.md) · [Paul's Notes](../README.md)

References: [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html), [GNU awk manual](https://www.gnu.org/software/gawk/manual/gawk.html), and [Rscript documentation](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rscript.html). Consult the manuals for your installed versions when options differ.

## Weekly Learning Objectives & Mastery Assessment

Work in a disposable practice directory with new invented specimen records. These criteria assess this independent guide and do not reproduce institutional taskings.

| Measurable objective | Evidence of competency | Independent mastery criterion |
| --- | --- | --- |
| Navigate and quote paths deliberately | Directory map, relative-path explanation, and successful run with spaces in a filename | Explain the working directory and every argument boundary; keep outputs inside the intended practice workspace |
| Validate input before transformation | Schema, unique-ID, category, numeric-value, and input/output collision trials | Each invalid case exits nonzero and leaves the previously valid output intact |
| Trace a reusable shell program | Documented arguments, conditional, loop, function, and captured status | Predict each branch and distinguish an expected no-match from an execution error |
| Connect Bash filtering to R summaries | Filtered records, total/measured/missing counts, unitful summaries, and minimum-count trials | Counts reconcile with the original records; missing values stay in totals and inadequate measured counts withhold the summary as specified |
| Reproduce and explain the workflow | Fresh-workspace rerun, logs, data dictionary, and short methods note | Recover the expected structures and counts, identify which commands can replace files, and demonstrate safe failure with a recorded status |

**Mastery decision:** satisfy every row on fresh invented inputs, including the failure trials, before calling the workflow reproducible. Keep commands, outputs, status checks, and your explanation; revise and rerun any unmet criterion. Never substitute private coursework or protected data for these public synthetic exercises.


### Fresh TSV checkpoint

Predict the number and identifiers of accepted rows before running this separate synthetic fixture. The directory and records are created only for this exercise; no course or research data are used.

```bash
mastery_dir=$(mktemp -d)
printf 'id\tquality\nS01\tpass\nS02\tfail\nS03\tpass\n' > "$mastery_dir/fresh records.tsv"
mastery_ids=$(awk -F '\t' 'NR > 1 && $2 == "pass" { print $1 }' "$mastery_dir/fresh records.tsv")
mastery_count=$(printf '%s\n' "$mastery_ids" | awk 'NF { count++ } END { print count+0 }')
printf '%s\n' "$mastery_ids"
printf 'Accepted rows: %s\n' "$mastery_count"
test "$mastery_count" -eq 2
rm "$mastery_dir/fresh records.tsv"
rmdir "$mastery_dir"
```

**Expected checkpoint:** identifiers `S01` and `S03`, followed by `Accepted rows: 2`. Explain why the header is not an observation and why the path with a space needs quoting. Diagnose an incorrectly chosen field separator and inspect its exit status before trusting its output. Invent a new fixture with zero accepted rows and verify that an empty selection is reported deliberately. Review [the Bash topic guide](../02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md).
