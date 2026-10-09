# Week 4 Bash Group Work — Runnable lab

**Verified source layout:** `"","sampleID","condition","age","sex","batch"`. In the uploaded classroom example, there are 10 data records plus 1 header, and `sex` in field 5 uses `F` and `M` (not `Female` and `Male`). Quoted field contents are simple and contain no embedded commas in the provided sample.

## Run from the repository root

Clone the repository locally, create the **root-level `data/` folder**, and place the course-supplied `pseudo_metadata.csv` inside it. `/data/` and `/week4_practice/` are Git-ignored; do not force-add them or upload confidential records.

```sh
bash "03_Group_Work/Week_4_Bash_Lab/run_week4.sh" ./data/pseudo_metadata.csv ./week4_practice
```

The script implements all five questions and leaves `only_female.txt` and `females_metadata.csv` in the practice workspace. The nested `new_dir` is created, populated, inspected, and deleted in the fifth exercise. Run with a **new, disposable workspace**; the script refuses to remove a preexisting `new_dir`.

## Observed results from the supplied synthetic file

- `wc -l`: **11** (header plus ten participants).
- Female-coded records (`sex = F`): **6**; male-coded (`M`): **4**.
- Extracted source columns 3 and 4: **condition** and **age**.
- Filename clarification: `only_female.txt` is the Question 2 output and `females_metadata.csv` is an explicit copied alias to satisfy Question 3.

## Verify scripts

```sh
bash -n "03_Group_Work/Week_4_Bash_Lab/run_week4.sh"
bash "03_Group_Work/Week_4_Bash_Lab/test_week4.sh"
```

The shell exercise assumes fixed, simple six-column CSV records, consistent with the supplied synthetic file. For general quoted CSV containing embedded commas/newlines, use a CSV-aware parser. This is a learning script, not a production ETL system.

See [scholarly walkthrough](../Week_4_Bash_Group_Work_Narrative_Walkthrough.md) and the [LaTeX report template](../../06_RESOURCES/LaTeX/Week_4_Bash_LaTeX_Template.tex).
