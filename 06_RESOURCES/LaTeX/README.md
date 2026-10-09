# Example APA 7 Manuscript

**Header note:** This file is known to compile safely.

[Resource index](../README.md) · [Repository home](../../README.md)

[Editable LaTeX manuscript](Example_APA_7_Manuscript.tex) · [Compiled example PDF](Example_APA_7_Manuscript.pdf) · [Example bibliography](Example_References.bib) · [Full source-type guide](Bibliography_Guide.md) · [Practice entry catalogue](Example_Entry_Types.bib)

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
| Citations | Author–date examples; standalone `natbib` mode or optional `biblatex-apa` mode |
| References | New page; alphabetical entries; double spacing; 0.5-inch hanging indents |
| Tables and figures | Bold numbers, italic titles above, explanatory notes below |
| Abstract | Off by default; enable if the instructor requests it |
| Appendix | Commands after the references; compact code spacing for readability |

The Times-family font is a portable TeX substitute, rather than a bundled proprietary Times New Roman font. Use your institution's required font if it specifies one. The title page has no running head by default. No table of contents is included.

## Personalize and compile

1. Copy the canonical `.tex` file into your own working folder or upload it to Overleaf. Copy `Example_References.bib` alongside it if you plan to use bibliography-file mode.
2. Edit the metadata block near the top: title, student name, department/program, course, instructor and due date.
3. Replace the instructional paragraphs with your study's question, design, methods and verified results. Remove unused tables, figures and appendix material.
4. Replace both example citations and reference entries with the works you actually use. Each retained reference must be cited in the text. Choose one bibliography mode below.
5. Follow that mode's compile sequence and inspect the PDF before submission.

### Option 1: Standalone compilation

Leave `\usebibfilefalse` in the manuscript. References are supplied manually in `thebibliography`; the `.bib` file is not read in this mode. Compile from this folder:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
```

This mode uses common TeX packages and compiles without an `apa7` class or a BibTeX/Biber run. The source configures student-paper layout using `article`. `natbib` formats citations but does not automatically correct manually typed reference entries.

### Option 2: APA 7 bibliography-file compilation

Use a TeX installation containing `biblatex`, `biblatex-apa`, `csquotes` and `babel`, plus the **Biber** executable. The [APA citation package](https://ctan.org/pkg/biblatex-apa) uses Biber for this workflow. Package installation depends on your TeX distribution; use its package manager to install missing packages and keep Biber compatible with `biblatex`.

In the source, change the active line:

```latex
\usebibfilefalse
```

to:

```latex
\usebibfiletrue
```

The template then loads these settings automatically:

```latex
\usepackage[american]{babel}
\usepackage{csquotes}
\usepackage[backend=biber,style=apa]{biblatex}
\DeclareLanguageMapping{american}{american-apa}
\addbibresource{Example_References.bib}
```

**Do not paste a second copy of this block into the supplied template.** It is shown to explain the connection. The template loads `natbib` only in standalone mode and `biblatex` only in bibliography-file mode. Keep those systems separate when adapting other manuscripts.

Run all four commands from the directory containing the `.tex` and `.bib` files:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
biber Example_APA_7_Manuscript
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
```

The first pass creates the `.bcf` control file. Biber reads that file and the `.bib` entries, then writes bibliography data to `.bbl`. The final LaTeX passes resolve citations, references and cross-references. Give Biber the document basename **without `.tex`**. Run Biber again after changing the bibliography or which works you cite.

On Overleaf, upload the `.tex` and `.bib` together, set the manuscript as the main document, enable `\usebibfiletrue` and recompile using pdfLaTeX. Its build system normally runs the bibliography backend selected in the source. Inspect the compilation log if references do not appear.

## Create and connect your own bibliography

Create a plain UTF-8 text file named `references.bib` beside your manuscript. Each entry begins with an entry type and a unique citation key, followed by named fields. The included [example file](Example_References.bib) contains real Dr. Seuss books. The [source-type guide](Bibliography_Guide.md) maps APA reference categories to a separate catalogue of 52 fictional practice records, including journals, books, reports, theses, data, software, media, webpages and legal materials.

For example, this is a real reference already included in the example file:

```bibtex
@book{seuss1957cat,
  author    = {Seuss, Dr.},
  date      = {1957},
  title     = {The cat in the hat},
  publisher = {Random House}
}
```

If you rename the bibliography, update the existing connection inside the `\ifusebibfile` block:

```latex
\addbibresource{references.bib}
```

Citation keys connect the manuscript to entries; they are not printed author names. Use the exact key inside the citation command:

```latex
\textcite{seuss1957cat} is an example of a narrative citation.
This demonstrates a parenthetical citation \parencite{seuss1957cat}.
```

The supplied template supports these two commands in **both** modes. In bibliography-file mode, `\textcite` and `\parencite` are provided by `biblatex`; in standalone mode, the template maps them to `natbib` commands. Keys used in standalone mode must have corresponding manual `\bibitem` entries.

For a page-specific citation in bibliography-file mode:

```latex
\parencite[p. 3]{seuss1957cat}
```

Use that form only when page 3 actually supports your statement. A bibliography record does not verify the claim being cited.

The References section is already wired to print cited entries:

```latex
\section*{References}
\printbibliography[heading=none]
```

The surrounding conditional prints this in bibliography-file mode and the manual list otherwise. The uncited `seuss1960eggs` book in the example `.bib` is excluded until you cite it. To inspect every entry during editing, temporarily add `\nocite{*}` before printing the bibliography; this includes every entry in every loaded bibliography file. Remove it for a reference list that should contain only cited works.

### Bibliography fields to check

| Field | How to write it |
| --- | --- |
| Citation key | Unique and case-sensitive, such as `seuss1957cat` |
| Personal authors | `Family, Given and Family, Given`; use `and` between people |
| Organization author | Double braces, such as `{{American Psychological Association}}`, to preserve the complete name |
| Date | A known year or ISO date; omit an unknown date rather than inventing one |
| Title | Sentence case; protect necessary capitalization, such as `{edgeR}` or `{DNA}` |
| Journal details | Journal title, volume, issue and page range or article identifier |
| DOI | Identifier only, such as `10.1093/nar/gkaf018`; the APA style formats its link |
| URL | Full source URL; check that it identifies the cited work |

Verify exported metadata against the original work. Different entry types require different fields. Preserve commas between fields and matching braces. The package formats supplied metadata; it cannot correct a wrong author, year, DOI or title.

## Troubleshooting and verified scope

| Symptom | Check |
| --- | --- |
| `biblatex.sty`, `apa.bbx` or `csquotes.sty` missing | Install the corresponding TeX packages. |
| `biber: command not found` | Install Biber and confirm it is on your executable path. |
| Biber cannot find `.bcf` | Run the first LaTeX pass successfully; use the document basename and correct working directory. |
| Bibliography file not found | Match `\addbibresource` to the exact filename and location, including capitalization. |
| Citation key undefined | Check that the cited key exists; run the full four-command sequence. |
| New `.bib` entries do not affect the PDF | Confirm `\usebibfiletrue`; standalone mode does not read `.bib` files. |
| References change after switching modes | Clear that document's generated auxiliary files or use a clean build, then run the chosen mode's full sequence. |

The standalone manuscript has been compiled twice and its PDF visually checked. Biber and `biblatex-apa` are unavailable in the editing environment, so the optional automatic-bibliography build has **not** been executed here. The header's compilation note refers to the verified standalone configuration. See the package's [official documentation](https://ctan.org/pkg/biblatex-apa) for automatic APA 7 reference formatting.

For an assigned abstract, change `\includeabstractfalse` to `\includeabstracttrue`. The abstract appears on its own page as an unindented paragraph. Professional journal submissions can require a running head, author note, separate figure files or a journal class; follow that venue's requirements.

## APA guidance and course example

Use APA's [student paper setup guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf), [title-page guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page) and [heading guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/headings), together with the instructor's instructions.

The manuscript example uses the lab's actual six-field schema: `sex` is field 5 with `F`/`M` codes. The source input is held locally in the ignored `data/` folder. See the [Week 4 reading walkthrough](../../03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.md) and [runnable lab](../../03_Group_Work/Week_4_Bash_Lab/README.md) for the procedure and its limitations.
