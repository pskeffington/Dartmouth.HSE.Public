#!/usr/bin/env bash
# HSE 711 Week 4: reproducible five-question metadata lab.
# Usage: bash "Group Work/Week_4_Bash_Lab/run_week4.sh" path/to/pseudo_metadata.csv [workspace]
# Safety: only creates/deletes a nested "new_dir" inside the named workspace.
set -euo pipefail

# Setup: validate inputs and prepare a temporary workspace.
if [[ $# -lt 1 || $# -gt 2 ]]; then
  printf 'Usage: %s pseudo_metadata.csv [workspace]\n' "$0" >&2
  exit 2
fi
# The first argument is the source CSV; the optional second is the output folder.
input=$1
workspace=${2:-week4_practice}
if [[ ! -f "$input" || ! -r "$input" ]]; then
  printf 'Missing or unreadable input: %s\n' "$input" >&2
  exit 1
fi
# Resolve the workspace and input to absolute paths before changing directories.
mkdir -p "$workspace"
workspace=$(cd "$workspace" && pwd -P)
input=$(cd "$(dirname "$input")" && pwd -P)/$(basename "$input")
# Establish a fixed throwaway workspace and reject symlinks and preexisting subdirs.
[[ "$workspace" != "/" && "$workspace" != "$HOME" ]] || exit 1
[[ ! -e "$workspace/new_dir" && ! -L "$workspace/new_dir" ]] ||
 { echo "Refusing to overwrite existing new_dir" >&2; exit 1; }
# Question 1: count newline-terminated lines
# A header is a line too; line count need not equal participant count.
printf '\nQuestion 1: file line count\n'
wc -l < "$input"
# Verify the six-column classroom CSV (sex is column 5; F/M codes).
awk -F ',' '
NR == 1 {
  for (i = 1; i <= NF; i++) {
    header = $i
    gsub(/["\r]/, "", header)
    if (header == "sex") sex_col = i
  }
  if (!sex_col) { print "Missing sex header" > "/dev/stderr"; exit 2 }
  if (sex_col != 5) { print "Unexpected sex column position" > "/dev/stderr"; exit 2 }
  next
}
NF != 6 { print "Unexpected field count at row " NR > "/dev/stderr"; exit 2 }
' "$input"
# Question 2: filter female-coded (F) records
# Retain the header so selected columns remain identifiable.
printf '\nQuestion 2: female (F) subset\n'
awk -F ',' '
NR == 1 { print; next }
{
  sex = $5
  gsub(/["\r]/, "", sex)
  if (sex == "F") print
  else if (sex != "M") {
    print "Unexpected sex label on row " NR > "/dev/stderr"
    exit 2
  }
}' "$input" > "$workspace/only_female.txt"
# The female subset includes a header: subtract one for participant rows.
female_n=$(awk 'END {print NR-1}' "$workspace/only_female.txt")
printf 'Female participant rows: %s\n' "$female_n"
# Question 3: create, copy, and document
# The prompt alternates between only_female.txt and females_metadata.csv;
# copy explicitly rather than silently changing the requested filename.
printf '\nQuestion 3: create documented practice folder\n'
cp "$workspace/only_female.txt" "$workspace/females_metadata.csv"
mkdir "$workspace/new_dir"
cp "$workspace/females_metadata.csv" "$workspace/new_dir/"
# Here-document writes notes; $female_n is substituted by Bash.
cat > "$workspace/new_dir/notes.txt" <<EOF
Synthetic HSE 711 Week 4 metadata subset.
Input header: unnamed index, sampleID, condition, age, sex, batch.
Eligibility: sex code F; observed female rows: $female_n.
Outputs are examples, not clinical data.
EOF
# Question 4: select source columns 3 and 4
# In the classroom file, these columns are condition and age.
printf '\nQuestion 4: extract original columns 3 and 4\n'
(
  cd "$workspace/new_dir"
  cut -d ',' -f 3,4 females_metadata.csv > females_metadata_sub.csv
  head -n 3 females_metadata_sub.csv
)
# Question 5: inspect and safely clean up
# Only the explicitly created new_dir is deleted; the subset files remain.
printf '\nQuestion 5: list, inspect and remove disposable new_dir\n'
ls -lah "$workspace/new_dir"
# This path is constructed from a validated workspace. Guard again before deletion.
[[ -d "$workspace/new_dir" && ! -L "$workspace/new_dir" ]] || exit 1
rm -r "$workspace/new_dir"
printf 'Complete. Preserved files: %s/only_female.txt and females_metadata.csv\n' "$workspace"
