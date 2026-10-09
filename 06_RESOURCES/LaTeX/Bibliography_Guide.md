# Dr. Seuss-themed APA 7 bibliography guide

[LaTeX instructions](README.md) · [Resource index](../README.md) · [Repository home](../../README.md)

Use this guide alongside APA's [reference examples](https://apastyle.apa.org/style-grammar-guidelines/references/examples). It covers the major source families in APA 7 Chapter 10 and the legal-reference family in Chapter 11. APA categories describe sources; `.bib` entry types describe structured metadata. Several source categories share an entry type. This is a teaching companion, not a reproduction of the APA manual or an exhaustive list of every possible variation.

## Two files, two purposes

| File | Contents | How to use it |
| --- | --- | --- |
| [Example_References.bib](Example_References.bib) | Three real Dr. Seuss books: *The cat in the hat*, *Green eggs and ham*, and *The Lorax* | Loaded when the manuscript's bibliography-file mode is enabled. Two books are cited; the third demonstrates an uncited record. |
| [Example_Entry_Types.bib](Example_Entry_Types.bib) | 52 fictional, Dr. Seuss-themed practice records across 29 entry types | Browse and copy a suitable structure. Replace all metadata before using it in your research. Not loaded by the manuscript. |

**All `practice-` records are invented.** Their authors, journals, dates, page numbers, organizations, legal citations and `example.org` links are placeholders. They are not publications by Dr. Seuss or claims about his work. The theme appears in titles and classroom topics; it does not imply that Dr. Seuss authored a dataset, journal article or legal document. No text from his books is reproduced.

The real book records describe original print editions. Cite the edition you actually consulted. Check author, date and publisher against its title/copyright pages; modern reprints, translated editions and audiobooks may differ. Verification starting points: publisher listings for [The cat in the hat](https://www.penguinrandomhouse.com/books/43141/the-cat-in-the-hat-by-dr-seuss/), [Green eggs and ham](https://www.penguinrandomhouseretail.com/book/?isbn=9780394800165) and [The Lorax](https://www.penguinrandomhouse.com/books/43157/the-lorax-by-dr-seuss/9780394823379/). In the examples, `author = {Seuss, Dr.}` retains the credited pseudonym; do not substitute a legal name without checking the source and citation guidance.

## Find the right example

Open the practice catalogue and search for a citation key from this table. Each record has a source-category comment immediately above it.

| APA source family | Practice keys | Entry types and details to verify |
| --- | --- | --- |
| Periodicals | `practice-journal`, `practice-article-id`, `practice-magazine`, `practice-newspaper`, `practice-inpress` | `@article`: author, date, article title, journal/newspaper, volume, issue, pages or `eid`. Use `pubstate = {inpress}` for an accepted work genuinely in press. |
| Books and reference works | `practice-edition`, `practice-edited`, `practice-translation`, `practice-ebook`, `practice-chapter`, `practice-referencebook`, `practice-dictionary`, `practice-updating` | `@book`, `@collection`, `@incollection`, `@reference`, `@inreference`: author/editor, date, title, edition, publisher; chapter author, editor, book title and pages for a chapter; translator/original date when applicable. |
| Reports and gray literature | `practice-report`, `practice-government`, `practice-brief`, `practice-standard` | `@report`, `@manual`: issuing organization, date, title, report/standard number, institution or organization, URL. A PDF's file format does not determine its reference type. |
| Conferences | `practice-talk`, `practice-poster`, `practice-proceedings-paper`, `practice-proceedings` | `@presentation`, `@inproceedings`, `@proceedings`: presentation type, event name/date/location, or the published proceedings' editor, publisher and pages. A proceedings article in a journal uses `@article`. |
| Dissertations and theses | `practice-dissertation`, `practice-thesis` | `@phdthesis`, `@mastersthesis`: degree institution, publication status, repository/database and URL when applicable. Use `howpublished = {unpublished}` for an unpublished thesis. |
| Reviews | `practice-review` | `@article` with `titleaddon`: review author and date, review title, description of the reviewed work, journal details. The reviewer is the author of the review. |
| Unpublished and informally published works | `practice-manuscript`, `practice-preprint` | `@unpublished`, `@online`: manuscript status/institution or preprint archive and URL. Do not label a preprint as a published journal article. |
| Data | `practice-data` | `@dataset`: creator, date, title, version, repository/publisher, DOI or URL, and data-set descriptor. Record the exact version used. |
| Software and apparatus | `practice-software`, `practice-app`, `practice-apparatus` | `@software`, `@hardware`: developer, date, title, version, publisher, software/app/apparatus descriptor and URL. |
| Tests and measurement instruments | `practice-test` | `@misc`: creator, date, title, instrument description and source. Cite a published manual as a book/manual and a published validation article as an article. |
| Audiovisual works | `practice-film`, `practice-tv`, `practice-stream`, `practice-podcast`, `practice-album`, `practice-song`, `practice-audiobook`, `practice-image` | `@video`, `@audio`, `@image`: correct creator roles, date, title, format descriptor, parent series/album for a part, production/distribution source and URL when applicable. |
| Online media | `practice-web`, `practice-blog`, `practice-social`, `practice-forum`, `practice-slides` | `@online`: person or organization, full date when known, title/text, site/platform, descriptor and stable URL. Social posts can include a username. |
| Archival material | `practice-archive` | `@misc`: creator, date, title or description, collection, box/folder and archive. Unrecoverable private correspondence is normally personal communication instead. |
| Legal materials | `practice-case`, `practice-statute`, `practice-hearing`, `practice-regulation`, `practice-patent`, `practice-constitution`, `practice-treaty` | `@jurisdiction`, `@legislation`, `@legmaterial`, `@legadminmaterial`, `@patent`, `@constitution`, `@legal`: jurisdiction-specific legal metadata, not ordinary author–date book fields. Practice citations are fictional. |

The catalogue uses types and fields supported by [biblatex-apa](https://ctan.org/pkg/biblatex-apa), including its extensions. It is intended for `style=apa` with Biber, not for traditional BibTeX `.bst` styles. For specialized roles, legal materials and edge cases, compare the formatted output with the package's [official example records](https://github.com/plk/biblatex-apa/blob/master/bibtex/bib/biblatex-apa-test-references.bib) and APA guidance. Legal rules vary by jurisdiction; these fictional records teach metadata structure only.

## Connect, cite and print

1. Follow the [README's bibliography-file setup and four-command build](README.md#option-2-apa-7-bibliography-file-compilation). Enable `\usebibfiletrue`.
2. Keep the real reference file connected through the existing `\addbibresource{Example_References.bib}` line. Add verified sources to that file or rename it and update the connection.
3. Use the entry key, not the filename, in your citation:

```latex
\textcite{seuss1957cat} is a narrative citation example.
This is a parenthetical citation example \parencite{seuss1971lorax}.
% A locator must correspond to the edition and passage you actually consulted.
\parencite[p. 12]{seuss1957cat}
% Multiple sources in one parenthetical citation (biblatex mode):
\parencite{seuss1957cat,seuss1971lorax}
```

The first example displays an author in the sentence with a parenthesized year; the second places author and year in parentheses. These sentences demonstrate syntax, not literary findings. Page 12 is a locator example only. Do not reuse it as evidence without reading that page in your edition.

The template already contains `\printbibliography[heading=none]` under its References heading. Cite every retained reference. In standalone mode, `.bib` records are ignored: keys must match manual `\bibitem` entries instead. Automatic sorting, date-letter disambiguation and metadata formatting belong to bibliography-file mode.

For a **separate practice preview**, copy the manuscript into a disposable practice folder, enable bibliography-file mode, change its existing resource line to the following, and place both `.bib` files alongside it:

```latex
\addbibresource{Example_References.bib}
\addbibresource{Example_Entry_Types.bib}
```

Temporarily add `\nocite{*}` just before `\printbibliography[heading=none]`, then run the full PDFLaTeX/Biber/PDFLaTeX/PDFLaTeX sequence. This prints all loaded records, including the fictional practice entries. Label that PDF as a practice catalogue. Remove the practice resource and `\nocite{*}` before preparing a research submission. Never treat successful compilation as confirmation that an entry is a real source.

## Fields students commonly need

| Situation | What to enter |
| --- | --- |
| Multiple authors | `author = {Reader, Riley and Scholar, Morgan}`; enter all authors in the record and let the style abbreviate citations. Do not type `et al.` as an author. |
| Organization author | `author = {{Example Seuss Reading Group}}`; the inner braces preserve a literal name. |
| Editor instead of author | Use `editor` for an edited book. For a chapter, use the chapter's `author` and the book's `editor`. |
| Known date | `date = {2025}` or `date = {2025-03-02}`. Use a full date only where appropriate to the source type. |
| Unknown date | Omit `date`; the style supplies the no-date form. Do not use a guessed year or a literal `n.d.` date value. |
| No named author | Omit `author` and supply the title; do not invent “Anonymous” unless the work is actually signed Anonymous. |
| No title | Supply a concise bracketed description using the appropriate source-type guidance; inspect the output so brackets are not duplicated by a descriptor. |
| Title capitalization | Use sentence case; protect proper names, e.g., `{Dr. Seuss}`, `{The Lorax}` or `{DNA}`, with braces. |
| Edition and version | `edition = {2}` for a book edition; `version = {1.2}` for software/data. Do not confuse an edition with a printing. |
| Page range or article ID | `pages = {10--24}` or `eid = {e0042}`; do not invent a range for an article number. |
| DOI | Use the bare verified identifier in `doi`, without `https://doi.org/`. The style formats the link. No fictional DOI is supplied in the catalogue. |
| URL | Use a persistent URL for the exact work. Do not add a database/search-session link for an ordinary journal article when APA calls for its DOI. |
| Retrieval date | Use `urldate = {2026-10-09}` when the content changes over time and is not archived, such as a living reference entry. Do not add retrieval dates to every webpage. Replace the example date with your actual access date. |
| Reprinted or translated work | Verify `origdate`, current `date`, translator, edition and publisher; cite the version consulted and inspect the two-date output. |
| Media role | APA-style fields such as `author+an:role = {1=director}` assign a role to the first listed creator. Check the role against the credits. |
| Username | `author+an:username = {1=readingexample}` attaches the handle to the first author; use the actual account details. |
| Special characters | Escape prose `&` as `\&` and `%` as `\%` in LaTeX-valued fields; keep URL/DOI fields as actual identifiers. |

## Cases that do not become ordinary reference entries

Personal communications that readers cannot recover usually receive an in-text citation only, for example `(A. Reader, personal communication, March 2, 2025)` after replacing the fictional details. They do not belong in the reference list. A publicly retrievable interview, recording or archived letter uses the relevant retrievable source type instead.

When quoting a source without page numbers, use a meaningful paragraph, section or timestamp locator rather than inventing pages. For a secondary citation, cite the work you actually read and follow APA's “as cited in” guidance; do not add an unread original to the reference list. Cite a specific webpage rather than an entire website when a particular claim comes from that page.

## Before submitting

Check each record against the source, read the rendered reference list and confirm that author, date, title, source, punctuation, italics and links fit that source category. Check that every in-text key resolves and every listed reference is cited. Remove all fictional entries and unused instructional prose. Automatic formatting cannot verify metadata or establish that a source supports your claim.

The standalone manuscript PDF has been compiled and visually checked. The editing environment lacks Biber and `biblatex-apa`, so the optional automatic build and practice-catalogue rendering have not been run here. Inspect those outputs after compiling with the required tools.
