# Week 4 LaTeX — guided learning and lab report

[Open the editable LaTeX template](Week_4_Bash_LaTeX_Template.tex)

This public teaching template follows the supplied HSE 711 Week 4 Bash lecture and all five group-work exercises. It is a fill-in study handout and reproducible lab report, **not a completed assignment**. It includes a command map, code blocks, conceptual explanations, results table, scholarly narrative scaffold, provenance and safety checks, and bibliography.

## Use

1. Copy `Week_4_Bash_LaTeX_Template.tex` to your own working folder.
2. Open it in Overleaf, TeXShop, or another LaTeX editor.
3. Replace `[Student name]`, `[Submission date]`, and each `[Insert ...]` placeholder.
4. Run the commands with the actual course `pseudo_metadata.csv` and record what happened. The file supplied for this assignment contains synthetic metadata, so do not frame the results as population findings.
5. Review the output PDF, especially tables and code blocks, before submitting.

Compile locally with:

```sh
pdflatex -interaction=nonstopmode Week_4_Bash_LaTeX_Template.tex
pdflatex -interaction=nonstopmode Week_4_Bash_LaTeX_Template.tex
```

Required LaTeX packages: `geometry`, `fontenc`, `inputenc`, `lmodern`, `microtype`, `amsmath`, `amssymb`, `booktabs`, `longtable`, `array`, `xcolor`, `hyperref`, `fancyvrb`, `listings`, `graphicx`, and `enumitem`. Most full TeX installations include them.

## Learning outcomes

The template explains shell navigation, file inspection, scripting, AWK selection, CUT extraction, safe deletion, and Rscript handoff. It intentionally separates *expected behavior* from *observed result* and highlights the mismatch between `only_female.txt` and `females_metadata.csv` in the exercise instructions.

**CSV caveat:** The classroom AWK/CUT examples assume a simple comma-delimited file with a `Sex` header and no embedded quoted commas. Check the actual file schema before using them; use a CSV-aware parser where necessary.

## Related teaching materials

- [Week 4 Lecture Narrative](../../02_Lecture_Notes/Week_4_Introduction_to_Bash_Narrative_Walkthrough.Rmd)
- [Week 4 Group Work Walkthrough](../../03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.Rmd)
- [Bash Operations Sheet](../Bash/BASH_OPERATION_SHEET.md)

No PDF compilation is claimed until a LaTeX compiler is run.
