# Reading editions and document publishing

[Resources](../README.md) · [Repository home](../../README.md)

## Purpose

This directory contains **publishing utilities** for independently authored public study notes. It is not a repository of slide decks, presentation submissions, or research results. Topic companions and weekly guides remain in their respective study directories.

| File | Responsibility |
| --- | --- |
| [`build_reading_editions.py`](build_reading_editions.py) | Generate browser-friendly Markdown reading editions from the student-authored R Markdown sources |
| [`check_navigation.py`](check_navigation.py) | Check local document links, headings, code fences, and stylesheet paths |
| [`reading.css`](reading.css) | Consistent formatting for locally knitted R Markdown HTML |
| [`LINK_AUDIT.md`](LINK_AUDIT.md) | Dated evidence of navigation and external-link checks; a historical report, not a list of confirmed broken links |

## Editing workflow

1. Edit the independent `.Rmd` teaching material in `02_Lecture_Notes/` or `03_Group_Work/`, not the generated Markdown.
2. From the repository root, regenerate reading editions:

   ```bash
   python3 06_RESOURCES/Presentation/build_reading_editions.py
   ```

3. Verify generated pages and local navigation without changing files:

   ```bash
   python3 06_RESOURCES/Presentation/build_reading_editions.py --check
   python3 06_RESOURCES/Presentation/check_navigation.py
   ```

4. Review the changed Markdown before committing. When links or outside sources change, document the results in the [link audit](LINK_AUDIT.md), distinguishing inaccessible sites from proven broken URLs.

The builder uses the Python standard library. It does **not** execute R, validate statistical findings, or regenerate experimental results. A passing navigation check establishes local document consistency, not scientific reproducibility.

## HTML and PDF

For an HTML version, open the corresponding `.Rmd` in RStudio and knit to HTML. The [shared stylesheet](reading.css) affects HTML only; it has no effect on PDF output. Install required R packages. Keep any authorized course inputs out of public source control; public method guides do not require instructor files.

The publishing tool creates Markdown, not HTML. A separate R Markdown renderer creates HTML. Rendering is optional and must not introduce restricted course prompts, outputs, or datasets.

For interpreting figures, use the [plot-reading guide](../READING_PLOTS.md). For guided exercises, see the [follow-along guide](../../FOLLOW_ALONG.md).

## Maintenance boundary

Keep source lessons in study folders, reusable formatting/build tooling here, and scientific analyses or private datasets outside the public publishing workflow. The `Presentation/` path is retained for compatibility with existing `.Rmd` CSS references and automation; moving or renaming it requires an atomic update of every caller.
