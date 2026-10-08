# Week 4 Bash Group Work — Deployment package

**Verified source layout:** `"","sampleID","condition","age","sex","batch"`. In the uploaded classroom example, there are 10 data records plus 1 header, and `sex` in field 5 uses `F` and `M` (not `Female` and `Male`). Quoted field contents are simple and contain no embedded commas in the provided sample.

## Run from the repository root

Copy the course-supplied `pseudo_metadata.csv` to your local machine. Do not upload confidential or real patient records.

```sh
bash "Group Work/Week_4_Bash_Lab/run_week4.sh" /path/to/pseudo_metadata.csv ./week4_practice
```

The script implements all five questions and leaves `only_female.txt` and `females_metadata.csv` in the practice workspace. The nested `new_dir` is created, populated, inspected, and deleted in the fifth exercise. Run with a **new, disposable workspace**; the script refuses to remove a preexisting `new_dir`.

## Observed results from the supplied synthetic file

- `wc -l`: **11** (header plus ten participants).
- Female-coded records (`sex = F`): **6**; male-coded (`M`): **4**.
- Extracted source columns 3 and 4: **condition** and **age**.
- Filename clarification: `only_female.txt` is the Question 2 output and `females_metadata.csv` is an explicit copied alias to satisfy Question 3.

## Verify scripts

```sh
bash -n "Group Work/Week_4_Bash_Lab/run_week4.sh"
bash "Group Work/Week_4_Bash_Lab/test_week4.sh"
```

The shell exercise assumes fixed, simple six-column CSV records, consistent with the supplied synthetic file. For general quoted CSV containing embedded commas/newlines, use a CSV-aware parser. This is a learning script, not a production ETL system.

See [scholarly walkthrough](../Week_4_Bash_Group_Work_Narrative_Walkthrough.Rmd) and the [LaTeX report template](../../RESOURCES/LaTeX/Week_4_Bash_LaTeX_Template.tex).
