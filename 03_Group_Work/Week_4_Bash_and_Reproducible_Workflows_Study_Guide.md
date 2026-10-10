# Paul's Notes · Week 4: Bash and Reproducible Workflows

[Section index](README.md) · [Editable R Markdown](Week_4_Bash_and_Reproducible_Workflows_Study_Guide.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

Use Bash to organize files, inspect a small table, validate and filter records, automate repeated work, and pass explicit arguments to R. The invented data describe workshop assembly runs in minutes. Every input needed for this lesson is created below.

**Study time:** 90–120 minutes. **Prerequisites:** Weeks 1–3 data checks and summaries. Use a Bash shell, not a PowerShell prompt. The examples work with Bash 3.2 or newer and standard `awk`, `grep`, `head`, `wc`, `mktemp`, and file utilities. The final bridge needs `Rscript` with base R; no add-on R packages are required. Python is needed only for the optional automated lesson check.

Copy the blocks into one Bash session in order, or save them in a script. The `.Rmd` is the editable lesson; read its Markdown edition directly on GitHub. The named Bash chunks are for the validation tool and are not instructions to knit shell commands in RStudio.

## On this page

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

## Learning objectives

By the end, you should be able to explain relative paths and quoting, distinguish line counts from record counts, validate a simple delimiter-separated table, write a script with positional arguments and clear errors, handle expected no-match results, loop over files safely, and separate shell orchestration from R calculations.

## 1. Check tools and create a practice workspace

A shell interprets commands; a directory determines how relative paths resolve. Work in a new temporary directory so these examples do not replace existing files. Keep the printed path if you want to inspect the results later.

```bash
set -euo pipefail
for tool in awk grep head wc sort uniq mktemp Rscript; do
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

## 2. Create and inspect known data

The row unit is one assembly run. `run_id` is its unique key; `bench` is A or B; `minutes` is a nonnegative number or the literal `NA`. This lesson uses simple comma-delimited records with no quoted commas or embedded newlines. General CSV needs a CSV-aware parser such as R's `read.csv()`.

```bash
cat > "input/run times.csv" <<'CSV'
run_id,bench,minutes
b01,A,8
b02,B,15
b03,A,NA
b04,B,21
b05,A,12
CSV
head -n 3 "input/run times.csv"
wc -l < "input/run times.csv"
awk 'END {print (NR > 0 ? NR - 1 : 0)}' < "input/run times.csv"
```

**Expected:** the header and first two runs; then `6` lines and `5` data records. `wc -l` counts newline characters, including the header here. A missing final newline can affect it. The quoted heredoc delimiter (`'CSV'`) keeps its contents literal rather than expanding shell variables.

Before calculating a mean, count unavailable values:

```bash
awk -F ',' 'NR > 1 && $3 == "NA" {missing++}
            END {print "Missing measurements:", missing + 0}' < "input/run times.csv"
if grep -Fq 'unknown-marker' "input/run times.csv"; then
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

A pipeline connects standard output from one command to standard input of the next. Count runs per bench by extracting field 2, sorting labels, and counting adjacent repetitions:

```bash
awk -F ',' 'NR > 1 {print $2}' < "input/run times.csv" | sort | uniq -c
```

**Expected:** three A labels and two B labels. `uniq` counts adjacent repeats, so sorting first matters. `pipefail` makes a pipeline report a failed earlier command instead of relying only on its last command. This is still a text-format calculation, not a general CSV parser.

## 3. Make a reusable filter with validation

A script receives arguments through `$1`, `$2`, and `$3`. Validate the argument count before reading those variables when `set -u` is enabled. The script below takes an input file, an output file, and one bench label. It validates every row, including rows that are not selected.

```bash
cat > scripts/filter_runs.sh <<'BASH'
#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 3 ]]; then
  printf 'Usage: filter_runs.sh input.csv output.csv A|B\n' >&2
  exit 2
fi
input_file=$1
output_file=$2
bench=$3
[[ -r "$input_file" && -f "$input_file" ]] || {
  printf 'Unreadable input: %s\n' "$input_file" >&2
  exit 1
}
[[ "$bench" == A || "$bench" == B ]] || {
  printf 'Bench must be A or B\n' >&2
  exit 2
}
if [[ "$input_file" == "$output_file" || "$input_file" -ef "$output_file" ]]; then
  printf 'Input and output must differ\n' >&2
  exit 2
fi
# Build a temporary output beside its destination; publish only after validation.
temp_file=$(mktemp "${output_file}.XXXXXX")
trap 'rm -f -- "$temp_file"' EXIT
awk -F ',' -v wanted="$bench" '
  NR == 1 {
    if ($0 != "run_id,bench,minutes") exit 1
    print
    next
  }
  $0 ~ /"/ || NF != 3 || $1 == "" || seen[$1]++ || ($2 != "A" && $2 != "B") {exit 1}
  $3 != "NA" && $3 !~ /^[0-9]+([.][0-9]+)?$/ {exit 1}
  $2 == wanted {print}
  END {if (NR == 0) exit 1}
' < "$input_file" > "$temp_file" || {
  printf 'Invalid input: check header, fields, unique IDs, bench, and minutes\n' >&2
  exit 1
}
mv -- "$temp_file" "$output_file"
BASH
bash -n scripts/filter_runs.sh
bash scripts/filter_runs.sh "input/run times.csv" output/selected_a.csv A
cat output/selected_a.csv
```

**Expected:** a header plus `b01,A,8`, `b03,A,NA`, and `b05,A,12`. The missing row is retained so the denominator remains visible. `bash -n` checks syntax without running the script. Explicit `bash script` does not require execute permission; a shebang plus `chmod +x` allows direct execution if desired.

The awk record checks reject duplicate IDs, missing fields, unknown benches, negative values, quoted fields, and undocumented measurement strings. They do not establish scientific validity. This deliberately small format excludes full CSV quoting and CRLF line endings; use R's CSV parser for other formats rather than weakening checks blindly. Temporary output prevents a failed validation from replacing an existing result. Reusing the output path in a successful call replaces that output intentionally.

## 4. Check an expected failure

A robust workflow demonstrates its failure behavior, not only its successful path. Duplicate the first data row in a separate practice file and confirm that no final output is created.

```bash
cp -- "input/run times.csv" input/duplicate.csv
printf 'b01,A,8\n' >> input/duplicate.csv
if bash scripts/filter_runs.sh input/duplicate.csv output/rejected.csv A; then
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
for bench in A B; do
  bash scripts/filter_runs.sh "input/run times.csv" "output/bench_${bench}.csv" "$bench"
  printf 'Bench %s: %s records\n' "$bench" "$(count_data_records "output/bench_${bench}.csv")"
done
[[ $(count_data_records output/bench_A.csv) -eq 3 ]]
[[ $(count_data_records output/bench_B.csv) -eq 2 ]]
```

**Expected:** A has three runs, B has two. Filtering does not imply dropping missing measurements. The loop writes two clearly named outputs; a filename alone is not proof that the record count is correct.

To process discovered files, use a quoted glob loop rather than splitting `ls` output:

```bash
for file in output/bench_*.csv; do
  [[ -f "$file" ]] || continue
  printf 'Inspecting %s\n' "$file"
  head -n 2 "$file"
done
```

**Expected:** the two `bench_A.csv` and `bench_B.csv` files are inspected separately. The explicit file test handles a pattern with no matches. All paths inside the loop remain quoted.

## 6. Write an R script with a clear argument contract

Bash should manage paths and execution; R should parse CSV and calculate numerical summaries. This script takes an input CSV, an output CSV, and the minimum measured count needed to report a mean. It keeps total, measured, and missing counts separate.

```bash
cat > scripts/summarize_runs.R <<'RSCRIPT'
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
run_data <- read.csv(args[1], na.strings = "NA", stringsAsFactors = FALSE)
if (!identical(names(run_data), c("run_id", "bench", "minutes"))) {
  stop("Expected run_id, bench, minutes columns")
}
if (nrow(run_data) == 0L || anyNA(run_data$run_id) ||
    any(run_data$run_id == "") || anyDuplicated(run_data$run_id)) {
  stop("Need nonempty, unique run IDs")
}
if (anyNA(run_data$bench) || !all(run_data$bench %in% c("A", "B"))) {
  stop("Bench must be A or B")
}
# CSV may infer an entirely missing column as logical; retain numeric NA.
if (is.logical(run_data$minutes) && all(is.na(run_data$minutes))) {
  run_data$minutes <- as.numeric(run_data$minutes)
}
if (!is.numeric(run_data$minutes) ||
    any(!is.finite(run_data$minutes[!is.na(run_data$minutes)])) ||
    any(run_data$minutes < 0, na.rm = TRUE)) {
  stop("Minutes must be finite nonnegative numbers or NA")
}
summary_rows <- lapply(sort(unique(run_data$bench)), function(bench_name) {
  values <- run_data$minutes[run_data$bench == bench_name]
  n_measured <- sum(!is.na(values))
  data.frame(
    bench = bench_name, n_total = length(values), n_measured = n_measured,
    n_missing = sum(is.na(values)), eligible = n_measured >= minimum_count,
    mean_minutes = if (n_measured >= minimum_count) mean(values, na.rm = TRUE) else NA_real_
  )
})
bench_summary <- do.call(rbind, summary_rows)
write.csv(bench_summary, args[2], row.names = FALSE, na = "NA")
print(bench_summary)
RSCRIPT
```

**Expected:** the script file exists; writing it does not run R. The quoted heredoc preserves `$` in R column references. A base-R script does not require RStudio. Values such as `two`, zero, a negative number, or `2.5` are invalid minimum-count arguments.

## 7. Run the bridge, record logs, and check results

```bash
Rscript --vanilla scripts/summarize_runs.R "input/run times.csv" output/summary.csv 2 \
  > logs/summary.log 2>&1
cat logs/summary.log
cat output/summary.csv
```

**Expected:** A has total `3`, measured `2`, missing `1`, and mean `10` minutes. B has total `2`, measured `2`, missing `0`, and mean `18` minutes. Both meet the minimum of two measured values. `2>&1` sends standard error to the same log destination as standard output; check the exit status as well as the log.

With a minimum of three measurements, both means should be withheld rather than presented as zero:

```bash
Rscript --vanilla scripts/summarize_runs.R "input/run times.csv" output/minimum_three.csv 3
```

**Expected:** both `eligible` values are FALSE and both means are `NA`; record counts are unchanged. A threshold is a reporting rule, not a substitute for study design, uncertainty, or a clinically justified sample size. These summaries describe invented runs and do not support a population claim.

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
| Filter rejects input | Check the exact header, three-field layout, unique IDs, bench labels, and numeric/NA convention |
| R sees text minutes | Inspect the imported column and undocumented values; do not convert bad text to zero |
| Output count seems too large | Account for the header and any duplicate records; compare selected and original counts |
| Mean differs | Check the minimum measured count, missingness, units, and actual input file |

## Independent practice

1. Add bench A runs with one observed value and one unavailable value. Predict total, measured, missing, and the new mean before executing.
2. Supply an invalid bench, a duplicate ID, a negative duration, and an input/output collision. Show that each fails without replacing a valid output.
3. Rename the input with spaces and rerun both scripts without changing their calculations.
4. Adapt the output loop to a third bench. Identify every schema check and argument contract that must change together.
5. Explain the difference between matching text with grep, selecting a field with awk, and parsing general CSV with R.

## Ready to move on

| Evidence | Completion check |
| --- | --- |
| Workspace | Four deliberate subdirectories; explain every relative path and quoted argument |
| Inputs and filter | Five known runs; three A and two B; one missing measurement; duplicate input rejected |
| Scripts and control flow | Trace positional arguments, one conditional, one loop, one function, and a nonzero status |
| R bridge | Report A = 10 min and B = 18 min with measured counts of two; explain the withheld means at minimum three |
| Reproducibility | Rerun from a fresh workspace and compare structures and counts; keep a methods note and log |

Explain which commands create, inspect, transform, or replace files. Why must a missing measurement stay in the total count? What evidence shows the script failed safely rather than merely printed an error?

## Next steps and references

[Previous: Week 3](Week_3_Group_Work_Narrative_Walkthrough.md) · [Weekly lessons](README.md) · [Bash topic companion](../02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) · [Command sheet](../06_RESOURCES/Bash/EASY_COMMAND_SHEET.md) · [Operation sheet](../06_RESOURCES/Bash/BASH_OPERATION_SHEET.md) · [Paul's Notes](../README.md)

References: [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html), [GNU awk manual](https://www.gnu.org/software/gawk/manual/gawk.html), and [Rscript documentation](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rscript.html). Consult the manuals for your installed versions when options differ.
