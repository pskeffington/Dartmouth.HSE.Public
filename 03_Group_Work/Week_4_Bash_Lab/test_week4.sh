#!/usr/bin/env bash
# Week 4 Bash lab: synthetic regression / smoke test.
# Run: bash "03_Group_Work/Week_4_Bash_Lab/test_week4.sh"
# Creates a temporary 3-record CSV; no course data required.
set -euo pipefail

# Locate this script and create an automatically cleaned test workspace.
here=$(cd "$(dirname "$0")" && pwd -P)
tmp=$(mktemp -d)
trap 'rm -r "$tmp"' EXIT

# Fixture: two female-coded participants, one male-coded participant.
cat > "$tmp/pseudo_metadata.csv" <<'CSV'
"","sampleID","condition","age","sex","batch"
"Disease_1","Disease_1","Disease",56,"F","Batch1"
"Disease_2","Disease_2","Disease",44,"M","Batch1"
"Control_1","Control_1","Control",43,"F","Batch1"
CSV

# Run the complete five-question exercise against the synthetic fixture.
bash "$here/run_week4.sh" "$tmp/pseudo_metadata.csv" "$tmp/practice"

# Confirm outputs were retained, temporary directory removed,
# and both female-coded records survived filtering.
[[ -f "$tmp/practice/only_female.txt" ]]
[[ -f "$tmp/practice/females_metadata.csv" ]]
[[ ! -e "$tmp/practice/new_dir" ]]
[[ $(wc -l < "$tmp/practice/only_female.txt") -eq 3 ]]

# Extracted third and fourth columns must be condition and age.
grep -Fq '"condition","age"' <(head -n 1 "$tmp/practice/only_female.txt" | cut -d ',' -f 3,4)
printf 'PASS: Week 4 staging smoke test\n'
