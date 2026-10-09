# Easy Bash command sheet

[Resource index](../README.md) · [Follow-along guide](../../FOLLOW_ALONG.md) · [Full operation sheet](BASH_OPERATION_SHEET.md) · [Helper source](bash_functions.sh)

Use a Bash terminal. Examples that reference course files assume you are at the repository root. Quoted paths preserve spaces. Read a command before running it; `>` creates or overwrites a destination file.

## Find your place and inspect a file

| Goal | Command | Check / meaning |
| --- | --- | --- |
| Show current location | `pwd` | Relative paths start here |
| List visible files | `ls -lh` | Names, sizes and modification times |
| Move up one folder | `cd ..` | Changes the working directory |
| Preview a file | `head -n 5 data/pseudo_metadata.csv` | Header and first four records |
| Inspect the end | `tail -n 5 data/pseudo_metadata.csv` | Last five lines |
| Count lines | `wc -l data/pseudo_metadata.csv` | Includes the header; counts newline characters |
| Inspect interactively | `less data/pseudo_metadata.csv` | Press `q` to leave |
| Search literal text | `grep -n 'sample' data/pseudo_metadata.csv` | Matching lines with line numbers; text search, not a field filter |
| Check Bash syntax | `bash -n 03_Group_Work/Week_4_Bash_Lab/run_week4.sh` | No output on success; does not run the lab |

## Practice without course files

Run this complete block. It creates a temporary directory, prints its location, and leaves the two practice files there for inspection.

```bash
practice_dir=$(mktemp -d)
printf 'Practice files: %s\n' "$practice_dir"
printf 'sampleID,sex,age\nS01,F,35\nS02,M,42\nS03,F,51\n' \
  > "$practice_dir/metadata.csv"

# Retain the header and select F-coded records from field 2.
awk -F ',' 'NR == 1 || $2 == "F"' "$practice_dir/metadata.csv" \
  > "$practice_dir/only_female.txt"
cat "$practice_dir/only_female.txt"

# Count selected records after excluding the header.
awk 'END { print (NR > 0 ? NR - 1 : 0) }' "$practice_dir/only_female.txt"
```

**Expected:** the header, S01 and S03, followed by a record count of `2`. This practice file has three simple fields and no quoted commas or multiline values.

## Apply the course schema correctly

The Week 4 file has six fields: an unnamed first field, `sampleID`, `condition`, `age`, `sex`, `batch`. Sex is field **5**, encoded as `F` / `M`. The lab validates that layout and handles the simple quoted values in the supplied classroom format. Use the [runnable lab](../../03_Group_Work/Week_4_Bash_Lab/README.md) for that file; the three-column practice filter above has a different schema.

```bash
# Run the synthetic fixture test first; it needs no course file.
bash "03_Group_Work/Week_4_Bash_Lab/test_week4.sh"

# After placing the course input in data/, run in a disposable workspace.
bash "03_Group_Work/Week_4_Bash_Lab/run_week4.sh" \
  data/pseudo_metadata.csv ./week4_practice
```

**Check:** the lab retains `only_female.txt` and `females_metadata.csv`. Its temporary `new_dir` is removed during the cleanup exercise. A general CSV with embedded commas or newlines requires a CSV-aware parser.

## Load reusable helpers

```bash
source "06_RESOURCES/Bash/bash_functions.sh"
hse_require_command awk
hse_require_file "data/pseudo_metadata.csv"
hse_sha256 "data/pseudo_metadata.csv"
```

The first two helper calls return success silently when their checks pass. The checksum identifies file contents; it does not establish their scientific validity. `hse_tsv_columns` and `hse_tsv_records` are for simple **tab-delimited** files. Use the [full operation sheet](BASH_OPERATION_SHEET.md) for loops, pipelines, arguments and additional examples.
