#!/usr/bin/env bash
# HSE 711 Week 4: reproducible five-question metadata lab.
# Usage: bash "Group Work/Week_4_Bash_Lab/run_week4.sh" path/to/pseudo_metadata.csv [workspace]
# Safety: only creates/deletes a nested "new_dir" inside the named workspace.
set -euo pipefail
if [[ $# -lt 1 || $# -gt 2 ]]; then
  printf 'Usage: %s pseudo_metadata.csv [workspace]\n' "$0" >&2; exit 2
fi
input=$1
workspace=${2:-week4_practice}
[[ -f "$input" && -r "$input" ]] || { echo "Missing input: $input" >&2; exit 1; }
mkdir -p "$workspace"
workspace=$(cd "$workspace" && pwd -P)
input=$(cd "$(dirname "$input")" && pwd -P)/$(basename "$input")
# Establish a fixed throwaway workspace and reject symlinks and preexisting subdirs.
[[ "$workspace" != "/" && "$workspace" != "$HOME" ]] || exit 1
[[ ! -e "$workspace/new_dir" && ! -L "$workspace/new_dir" ]] ||
 { echo "Refusing to overwrite existing new_dir" >&2; exit 1; }
printf 'Question 1: file line count\n'
wc -l < "$input"
# The supplied CSV has a quoted header and F/M values.
# Validate header position and simple comma-separated records before AWK.
awk -F ',' '
NR==1 {
 for (i=1;i<=NF;i++) { h=$i; gsub(/["\r]/,"",h); if(h=="sex") sex=i }
 if(!sex) {print "Missing sex header" > "/dev/stderr"; exit 2}
 if(sex!=5) {print "Unexpected sex column position" > "/dev/stderr"; exit 2}
 next
}
NF!=6 {print "Unexpected field count in record " NR > "/dev/stderr"; exit 2}
' "$input"
printf 'Question 2: female (F) subset\n'
awk -F ',' '
NR==1 {print; next}
{
 sex=$5; gsub(/["\r]/,"",sex)
 if (sex=="F") print
 else if (sex!="M") {print "Unexpected sex label on row " NR > "/dev/stderr"; exit 2}
}' "$input" > "$workspace/only_female.txt"
female_n=$(awk 'END {print NR-1}' "$workspace/only_female.txt")
printf 'Female participant rows: %s\n' "$female_n"
printf 'Question 3: create documented practice folder\n'
cp "$workspace/only_female.txt" "$workspace/females_metadata.csv"
mkdir "$workspace/new_dir"
cp "$workspace/females_metadata.csv" "$workspace/new_dir/"
cat > "$workspace/new_dir/notes.txt" <<EOF
Synthetic HSE 711 Week 4 metadata subset.
Input header: unnamed index, sampleID, condition, age, sex, batch.
Eligibility: sex code F; observed female rows: $female_n.
Outputs are examples, not clinical data.
EOF
printf 'Question 4: extract original columns 3 and 4\n'
(cd "$workspace/new_dir" &&
  cut -d ',' -f 3,4 females_metadata.csv > females_metadata_sub.csv &&
  head -n 3 females_metadata_sub.csv)
printf 'Question 5: list, inspect and remove disposable new_dir\n'
ls -lah "$workspace/new_dir"
# This path is constructed from a validated workspace. Guard again before deletion.
[[ -d "$workspace/new_dir" && ! -L "$workspace/new_dir" ]] || exit 1
rm -r "$workspace/new_dir"
printf 'Complete. Preserved files: %s/only_female.txt and females_metadata.csv\n' "$workspace"
