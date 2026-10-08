#!/usr/bin/env bash
# Self-contained smoke test from repository root.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd -P)
tmp=$(mktemp -d)
trap 'rm -r "$tmp"' EXIT
cat > "$tmp/pseudo_metadata.csv" <<'CSV'
"","sampleID","condition","age","sex","batch"
"Disease_1","Disease_1","Disease",56,"F","Batch1"
"Disease_2","Disease_2","Disease",44,"M","Batch1"
"Control_1","Control_1","Control",43,"F","Batch1"
CSV
bash "$here/run_week4.sh" "$tmp/pseudo_metadata.csv" "$tmp/practice"
[[ -f "$tmp/practice/only_female.txt" ]]
[[ -f "$tmp/practice/females_metadata.csv" ]]
[[ ! -e "$tmp/practice/new_dir" ]]
[[ $(wc -l < "$tmp/practice/only_female.txt") -eq 3 ]]
grep -Fq '"condition","age"' <(head -n 1 "$tmp/practice/only_female.txt" | cut -d ',' -f 3,4)
printf 'PASS: Week 4 staging smoke test\n'
