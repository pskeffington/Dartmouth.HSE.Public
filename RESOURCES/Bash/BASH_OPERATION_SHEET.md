# Bash Functions and Operations — Practical Reference

Companion to [Bash literature review](BASH_LITERATURE_REVIEW.md). Commands assume Bash and a disposable practice directory. **Review file paths before running commands with destructive effects.**

## 1. Environment and navigation

| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print working directory | `pwd` |
| `ls -lah` | List files, including hidden | `ls -lah` |
| `cd` | Change directory | `cd "$HOME"` |
| `mkdir -p` | Create directories | `mkdir -p output/tables` |
| `touch` | Create/update an empty file | `touch notes.txt` |
| `command -v` | Find an executable | `command -v Rscript` |
| `bash --version` | Check shell version | `bash --version` |
| `man` or `--help` | View command documentation | `man awk` |

## 2. Reading, searching and composing data

| Command | Purpose | Example |
|---|---|---|
| `head -n 5` | First five lines | `head -n 5 genes.tsv` |
| `tail -n 5` | Last five lines | `tail -n 5 genes.tsv` |
| `wc -l` | Count lines | `wc -l genes.tsv` |
| `grep -F` | Match literal strings | `grep -F 'ESR1' genes.tsv` |
| `cut -f` | Select TAB-separated columns | `cut -f 1,3 genes.tsv` |
| `sort` | Sort lines | `sort gene_ids.txt` |
| `uniq -c` | Count adjacent repeats | `sort gene_ids.txt | uniq -c` |
| `awk` | Process fields/records | `awk -F '\t' 'NR>1 {print $1}' genes.tsv` |
| `sed -n` | Print selected lines | `sed -n '1,10p' genes.tsv` |

**Important:** `uniq` counts only adjacent identical lines; sort first. Counting a file with `wc -l` includes its header and depends on line endings.

## 3. Variables, tests and status

```bash
#!/usr/bin/env bash
set -euo pipefail

input="metadata.tsv"
if [[ ! -f "$input" ]]; then
  printf 'Missing file: %s\n' "$input" >&2
  exit 1
fi

# "$@" preserves argument boundaries; "$input" preserves spaces.
printf 'Input file: %s\n' "$input"

# A failed grep can mean zero matching records; handle deliberately.
if grep -Fq 'ESR1' "$input"; then
  printf 'Gene found\n'
else
  printf 'Gene absent (or grep failed)\n'
fi
```

For critical error distinctions, capture a command status explicitly rather than treating every nonzero status as a successful no-match case.

## 4. Loops and reusable functions

```bash
# Prints file names safely, including names with spaces.
for file in ./*.tsv; do
  [[ -e "$file" ]] || continue
  printf 'File: %s\n' "$file"
done

# One function, one purpose; arguments are positional.
count_rows() {
  local input=$1
  [[ -f "$input" ]] || { printf 'Missing: %s\n' "$input" >&2; return 1; }
  awk 'END {print NR}' "$input"
}
count_rows "metadata.tsv"
```

```bash
# Reading TSV rows: IFS prevents tab-delimited fields from being split on spaces.
# NOTE: read can collapse adjacent empty tab fields. Use a TSV parser if
# preserving empty fields is scientifically important.
while IFS=$'\t' read -r sample subtype; do
  printf '%s -> %s\n' "$sample" "$subtype"
done < simple_two_column.tsv
```

## 5. Research operations: genomics metadata

For a **simple** comma-delimited table with no quoted commas, this demonstrates the earlier course exercise:

```bash
awk -F ',' '
  NR == 1 { print; next }
  tolower($2) == "female" { print }
' pseudo_metadata.csv > only_female.csv
```

**Verify the column number first.** The above assumes participant sex is exactly column 2 and no values contain quoted commas. If either assumption is false, use R's `read.csv()` or a CSV-aware tool instead. To exclude a malformed row, audit the file rather than silently guessing its meaning.

```bash
# Efficient exploratory summary for a simple TSV with gene in column 1.
awk -F '\t' 'NR > 1 {n[$1]++} END {for (g in n) print g, n[g]}' genes.tsv |
  sort -k1,1
```

## 6. Safe file operations and pipelines

```bash
cp -- source.tsv backup.tsv    # GNU syntax: -- stops flag parsing
mv -- backup.tsv archive.tsv   # GNU syntax; consult macOS BSD behavior
# rm -i obsolete.tsv           # interactive removal, deliberately commented

# Save a command's output, and error stream separately.
awk -F '\t' 'NR > 1 {print $1}' genes.tsv > gene_ids.txt 2> errors.log

# Streaming processing reduces unnecessary intermediate files:
cut -f 1 genes.tsv | sort -u > unique_ids.txt
```

Use `mktemp` for temporary files and `trap` for cleanup. Avoid `eval`, unquoted argument expansion, and broad `rm -rf` patterns.

## 7. Running and checking scripts

```bash
bash -n my_script.sh                # Parse/syntax check
shellcheck my_script.sh             # Optional static lint, if installed
bash my_script.sh                   # Explicit interpreter
Rscript --vanilla analysis.R        # R analysis invoked from Bash
```

Portable checksum command names vary: `shasum -a 256 file` is common on macOS, `sha256sum file` on GNU/Linux.

## 8. Script template

The companion [bash_functions.sh](bash_functions.sh) supplies checked operations: required command check, file validation, safe TSV inspection, checksum, and invocation of R scripts. It can be sourced without running a workload; see its example comments.

## 9. Review checklist

- Are interpreter requirements and file formats documented?
- Do quoted arguments preserve whitespace, empty values and paths?
- Are expected no-match results separated from unexpected command errors?
- Are headers, delimiters and sample identity validated before data transformation?
- Are destructive actions reviewed, and outputs written to an intended directory?
- Do syntax checks, static checks and sample-file tests pass?
- Are inputs and results traceable through checksums and logs?
