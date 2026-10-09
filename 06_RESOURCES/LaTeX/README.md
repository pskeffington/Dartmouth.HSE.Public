# APA 7 student manuscript template

[Resource index](../README.md) · [Repository home](../../README.md)

[Editable LaTeX manuscript](APA_7_Student_Manuscript_Template.tex) · [Compiled example PDF](APA_7_Student_Manuscript_Template.pdf)

This template turns the Week 4 metadata exercise into a student manuscript example. It provides a title page, an introductory section under the repeated paper title, Method, Results, Discussion, References and a command appendix. Bracketed text explains what to replace. Tables and figures contain explicit placeholders; no numerical findings are supplied.

## Formatting included

| Element | Template setting |
| --- | --- |
| Page and margins | US Letter; 1-inch margins |
| Font | 12-point Times-family serif, using PDFLaTeX's `mathptmx` |
| Body paragraphs | Double-spaced; left aligned; 0.5-inch first-line indent; no extra paragraph spacing |
| Header | Page number at the upper right, beginning with 1 on the title page |
| Student title page | Bold centered title, student, affiliation, course, instructor and due date |
| Headings | Unnumbered APA-style levels 1–3; no separate “Introduction” heading |
| Citations | Author–date narrative and parenthetical examples with `natbib` |
| References | New page; alphabetical entries; double spacing; 0.5-inch hanging indents |
| Tables and figures | Bold numbers, italic titles above, explanatory notes below |
| Abstract | Off by default; enable if the instructor requests it |
| Appendix | Commands after the references; compact code spacing for readability |

The Times-family font is a portable TeX substitute, rather than a bundled proprietary Times New Roman font. Use your institution's required font if it specifies one. The title page has no running head by default. No table of contents is included.

## Personalize and compile

1. Copy the canonical `.tex` file into your own working folder or upload it to Overleaf.
2. Edit the metadata block near the top: title, student name, department/program, course, instructor and due date.
3. Replace the instructional paragraphs with your study's question, design, methods and verified results. Remove unused tables, figures and appendix material.
4. Replace both example citations and reference entries with the works you actually use. Each retained reference must be cited in the text.
5. Compile twice and inspect the PDF before submission.

From this folder:

```bash
pdflatex -interaction=nonstopmode -halt-on-error APA_7_Student_Manuscript_Template.tex
pdflatex -interaction=nonstopmode -halt-on-error APA_7_Student_Manuscript_Template.tex
```

The source uses common TeX packages and compiles without an `apa7` class or a BibTeX/Biber run. It explicitly configures student-paper layout using `article`. References are editable entries in `thebibliography`; `natbib` formats the in-text examples, but does not automatically validate or convert the reference text. For a larger bibliography, consider the [APA 7 citation package](https://ctan.org/pkg/biblatex-apa) and its Biber workflow.

For an assigned abstract, change `\includeabstractfalse` to `\includeabstracttrue`. The abstract appears on its own page as an unindented paragraph. Professional journal submissions can require a running head, author note, separate figure files or a journal class; follow that venue's requirements.

## APA guidance and course example

Use APA's [student paper setup guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf), [title-page guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page) and [heading guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/headings), together with the instructor's instructions.

The manuscript example uses the lab's actual six-field schema: `sex` is field 5 with `F`/`M` codes. The source input is held locally in the ignored `data/` folder. See the [Week 4 reading walkthrough](../../03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.md) and [runnable lab](../../03_Group_Work/Week_4_Bash_Lab/README.md) for the procedure and its limitations.

The previous [Week 4 filename](Week_4_Bash_LaTeX_Template.tex) remains as a compatibility entry point. To use that entry point, keep both `.tex` files together and compile from this directory. Edit the canonical manuscript source to update either entry point.
