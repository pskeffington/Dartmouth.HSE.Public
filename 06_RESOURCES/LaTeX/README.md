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
| Citations | Author–date examples; `biblatex-apa` and Biber; example `.bib` already connected |
| References | New page; alphabetical entries; double spacing; 0.5-inch hanging indents |
| Tables and figures | Bold numbers, italic titles above, explanatory notes below |
| Abstract | Off by default; enable if the instructor requests it |
| Appendix | Commands after the references; compact code spacing for readability |

The Times-family font is a portable TeX substitute, rather than a bundled proprietary Times New Roman font. Use your institution's required font if it specifies one. The title page has no running head by default. No table of contents is included.

## Personalize and compile

1. Copy `Example_APA_7_Manuscript.tex` and `Example_References.bib` together into your working folder or Overleaf project. The template already loads this bibliography. Copy `compile_manuscript.sh` too if you want the local one-command build.
2. Edit the metadata block near the top: title, student name, department/program, course, instructor and due date.
3. Replace the instructional paragraphs with your study's question, design, methods and verified results. Remove unused tables, figures and appendix material.
4. Replace both example citations and reference entries with the works you actually use. Each retained reference must be cited in the text. Keep the bibliography filename or update the existing resource line if you rename it.
5. Follow the compile sequence and inspect the PDF before submission.

### Ready-linked APA 7 build

The supplied template is ready to use: it loads `Example_References.bib`, cites two real Dr. Seuss books and prints the cited records under References. No mode switch, package block or manual reference list needs to be added.

Use a TeX installation containing `biblatex`, `biblatex-apa`, `csquotes` and `babel`, plus the **Biber** executable. The [APA citation package](https://ctan.org/pkg/biblatex-apa) uses Biber. Use your TeX distribution's package manager to install missing packages and keep Biber compatible with `biblatex`.

With the three files together, run from this folder:

```bash
bash compile_manuscript.sh
```

The [build script](compile_manuscript.sh) checks the bibliography dependencies and runs the four passes below. It also works when called by path from another working directory.

The template already contains these settings:

```latex
\usepackage[american]{babel}
\usepackage{csquotes}
\usepackage[backend=biber,style=apa]{biblatex}
\DeclareLanguageMapping{american}{american-apa}
\addbibresource{Example_References.bib}
```

**Do not paste a second copy of this block into the supplied template.** It is shown to explain the existing connection. This template uses `biblatex`; do not add `natbib` or a manual `thebibliography` list.

Run all four commands from the directory containing the `.tex` and `.bib` files:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
biber Example_APA_7_Manuscript
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error Example_APA_7_Manuscript.tex
```

The first pass creates the `.bcf` control file. Biber reads that file and the `.bib` entries, then writes bibliography data to `.bbl`. The final LaTeX passes resolve citations, references and cross-references. Give Biber the document basename **without `.tex`**. Run Biber again after changing the bibliography or which works you cite.

On Overleaf, upload the `.tex` and `.bib` together, set the manuscript as the main document, recompile using pdfLaTeX. Its build system normally runs the bibliography backend selected in the source. Inspect the compilation log if references do not appear.

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

If you rename the bibliography, update the existing connection in the preamble:

```latex
\addbibresource{references.bib}
```

Citation keys connect the manuscript to entries; they are not printed author names. Use the exact key inside the citation command:

```latex
\textcite{seuss1957cat} is an example of a narrative citation.
This demonstrates a parenthetical citation \parencite{seuss1957cat}.
```

Both commands are provided by `biblatex`. The keys must match records in the connected `.bib`; no manual `\bibitem` entries are needed.

For a page-specific citation:

```latex
\parencite[p. 3]{seuss1957cat}
```

Use that form only when page 3 actually supports your statement. A bibliography record does not verify the claim being cited.

The References section is already wired to print cited entries:

```latex
\section*{References}
\printbibliography[heading=none]
```

The uncited `seuss1960eggs` book in the example `.bib` is excluded until you cite it. To inspect every entry during editing, temporarily add `\nocite{*}` before printing the bibliography; this includes every entry in every loaded bibliography file. Remove it for a reference list that should contain only cited works.

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
| New `.bib` entries do not affect the PDF | Check the resource filename, cite the new key and run the full build again. |
| Old manual-mode auxiliary files cause errors | Use a clean build, then run the full four-command sequence. |

The ready-linked manuscript has been built successfully with PDFLaTeX, Biber 2.21, `biblatex` 3.21 and `biblatex-apa` 9.20. The final build resolves the citation keys and prints the references from `Example_References.bib`; its PDF has been visually checked. The header's compilation note applies to this connected configuration. See the package's [official documentation](https://ctan.org/pkg/biblatex-apa) for automatic APA 7 reference formatting.

For the complete fictional practice catalogue, run:

```bash
bash compile_manuscript.sh --catalogue
```

This builds [Example_APA_7_Reference_Catalogue.tex](Example_APA_7_Reference_Catalogue.tex), which is already connected to `Example_Entry_Types.bib`. Its [compiled PDF](Example_APA_7_Reference_Catalogue.pdf) prints all 52 practice records. The catalogue stays separate from the manuscript's real reference file.

For an assigned abstract, change `\includeabstractfalse` to `\includeabstracttrue`. The abstract appears on its own page as an unindented paragraph. Professional journal submissions can require a running head, author note, separate figure files or a journal class; follow that venue's requirements.

## APA guidance and course example

Use APA's [student paper setup guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf), [title-page guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/title-page) and [heading guidance](https://apastyle.apa.org/style-grammar-guidelines/paper-format/headings), together with the instructor's instructions.

The manuscript example uses the lab's actual six-field schema: `sex` is field 5 with `F`/`M` codes. The source input is held locally in the ignored `data/` folder. See the [Week 4 reading walkthrough](../../03_Group_Work/Week_4_Bash_Group_Work_Narrative_Walkthrough.md) and [runnable lab](../../03_Group_Work/Week_4_Bash_Lab/README.md) for the procedure and its limitations.
