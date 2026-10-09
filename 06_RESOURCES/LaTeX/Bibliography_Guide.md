# Dr. Seuss-themed APA 7 bibliography guide

[LaTeX instructions](README.md) · [Resource index](../README.md) · [Repository home](../../README.md)

Use this guide alongside APA's [reference examples](https://apastyle.apa.org/style-grammar-guidelines/references/examples). It covers the major source families in APA 7 Chapter 10 and the legal-reference family in Chapter 11. APA categories describe sources; `.bib` entry types describe structured metadata. Several source categories share an entry type. Consult APA guidance for additional source-specific variations.

## Two files, two purposes

| File | Contents | How to use it |
| --- | --- | --- |
| [Example_References.bib](Example_References.bib) | Three real Dr. Seuss books: *The cat in the hat*, *Green eggs and ham*, and *The Lorax* | Already connected to the supplied manuscript. Two books are cited; the third demonstrates an uncited record. |
| [Example_Entry_Types.bib](Example_Entry_Types.bib) | 52 fictional, Dr. Seuss-themed practice records across 29 entry types | Browse and copy a suitable structure. Replace all metadata before using it in your research. Not loaded by the manuscript. |

**The `practice-` records are fictional teaching examples.** Their metadata and `example.org` links illustrate entry structure. Replace them with verified details before using a record in a manuscript. Dr. Seuss provides the classroom theme; each record identifies its own example creator.

The real book records describe original print editions. Cite the edition you actually consulted. Check author, date and publisher against its title/copyright pages; modern reprints, translated editions and audiobooks may differ. Publisher listings: [The cat in the hat](https://www.penguinrandomhouse.com/books/43141/the-cat-in-the-hat-by-dr-seuss/), [Green eggs and ham](https://www.penguinrandomhouseretail.com/book/?isbn=9780394800165) and [The Lorax](https://www.penguinrandomhouse.com/books/43157/the-lorax-by-dr-seuss/9780394823379/). In the examples, `author = {Seuss, Dr.}` retains the credited pseudonym. Use the author name shown on the source.

## Find the right example

Open the practice catalogue and search for a citation key from this table. Each record has a source-category comment immediately above it.

| APA source family | Practice keys | Entry types and details to verify |
| --- | --- | --- |
| Periodicals | `practice-journal`, `practice-article-id`, `practice-magazine`, `practice-newspaper`, `practice-inpress` | `@article`: author, date, article title, journal/newspaper, volume, issue, pages or `eid`. Use `pubstate = {inpress}` for an accepted work in press. |
| Books and reference works | `practice-edition`, `practice-edited`, `practice-translation`, `practice-ebook`, `practice-chapter`, `practice-referencebook`, `practice-dictionary`, `practice-updating` | `@book`, `@collection`, `@incollection`, `@reference`, `@inreference`: author/editor, date, title, edition, publisher; chapter author, editor, book title and pages for a chapter; translator/original date when applicable. |
| Reports and gray literature | `practice-report`, `practice-government`, `practice-brief`, `practice-standard` | `@report`, `@manual`: issuing organization, date, title, report/standard number, institution or organization, URL. A PDF's file format does not determine its reference type. |
| Conferences | `practice-talk`, `practice-poster`, `practice-proceedings-paper`, `practice-proceedings` | `@presentation`, `@inproceedings`, `@proceedings`: presentation type, event name/date/location, or the published proceedings' editor, publisher and pages. A proceedings article in a journal uses `@article`. |
| Dissertations and theses | `practice-dissertation`, `practice-thesis` | `@phdthesis`, `@mastersthesis`: degree institution, publication status, repository/database and URL when applicable. Use an explicit unpublished-thesis descriptor in `type` for this example. |
| Reviews | `practice-review` | `@article` with `titleaddon`: review author and date, review title, description of the reviewed work, journal details. The reviewer is the author of the review. |
| Unpublished and informally published works | `practice-manuscript`, `practice-preprint` | `@unpublished`, `@online`: manuscript status/institution or preprint archive and URL. Identify the preprint archive and publication status. |
| Data | `practice-data` | `@dataset`: creator, date, title, version, repository/publisher, DOI or URL, and data-set descriptor. Record the exact version used. |
| Software and apparatus | `practice-software`, `practice-app`, `practice-apparatus` | `@software`, `@hardware`: developer, date, title, version, publisher, software/app/apparatus descriptor and URL. |
| Tests and measurement instruments | `practice-test` | `@misc`: creator, date, title, instrument description and source. Cite a published manual as a book/manual and a published validation article as an article. |
| Audiovisual works | `practice-film`, `practice-tv`, `practice-stream`, `practice-podcast`, `practice-album`, `practice-song`, `practice-audiobook`, `practice-image` | `@video`, `@audio`, `@image`: correct creator roles, date, title, format descriptor, parent series/album for a part, production/distribution source and URL when applicable. |
| Online media | `practice-web`, `practice-blog`, `practice-social`, `practice-forum`, `practice-slides` | `@online`: person or organization, full date when known, title/text, site/platform, descriptor and stable URL. Social posts can include a username. |
| Archival material | `practice-archive` | `@misc`: creator, date, title or description, collection, box/folder and archive. Unrecoverable private correspondence is normally personal communication instead. |
| Legal materials | `practice-case`, `practice-statute`, `practice-hearing`, `practice-regulation`, `practice-patent`, `practice-constitution`, `practice-treaty` | `@jurisdiction`, `@legislation`, `@legmaterial`, `@legadminmaterial`, `@patent`, `@constitution`, `@legal`: jurisdiction-specific citation, source and provision details. |

The catalogue uses types and fields supported by [biblatex-apa](https://ctan.org/pkg/biblatex-apa), including its extensions. Use `style=apa` with Biber to format these records. For specialized roles, legal materials and edge cases, compare the formatted output with the package's [official example records](https://github.com/plk/biblatex-apa/blob/master/bibtex/bib/biblatex-apa-test-references.bib) and APA guidance. Use the reference requirements for the source's jurisdiction when adapting legal entries.

## Connect, cite and print

1. Follow the [README's ready-linked build](README.md#ready-linked-apa-7-build). The source already connects the example bibliography.
2. Keep the real reference file connected through the existing `\addbibresource{Example_References.bib}` line. Add verified sources to that file or rename it and update the connection.
3. Use the entry key, not the filename, in your citation:

```latex
\textcite{seuss1957cat} is a narrative citation example.
This is a parenthetical citation example \parencite{seuss1971lorax}.
% Page locator: use the page from your edition.
\parencite[p. 12]{seuss1957cat}
% Multiple sources in one parenthetical citation:
\parencite{seuss1957cat,seuss1971lorax}
```

The first example displays an author in the sentence with a parenthesized year; the second places author and year in parentheses. Replace the example page locator with the location of the passage you cite.

The template already contains `\printbibliography[heading=none]` under its References heading. Cite every retained reference. The ready-linked template uses automatic sorting, date-letter disambiguation and metadata formatting from `biblatex-apa`.

## Ready-built practice catalogue

The separate [catalogue source](Example_APA_7_Reference_Catalogue.tex) already loads `Example_Entry_Types.bib` and uses `\nocite{*}` to print all 52 records. Its [compiled PDF](Example_APA_7_Reference_Catalogue.pdf) is included. Build it from this folder:

```bash
bash compile_manuscript.sh --catalogue
```

The same script runs PDFLaTeX/Biber/PDFLaTeX/PDFLaTeX for either document. The manuscript loads only its real Dr. Seuss book file; the catalogue loads its fictional practice file. If you borrow a record for research, replace its metadata and put the verified record into your manuscript's bibliography.

The fictional constitution example uses a custom localization key defined in the catalogue source. Replace it with the supported key for the actual jurisdiction when adapting the record; the `source` field uses a localization key.

## Fields students commonly need

| Situation | What to enter |
| --- | --- |
| Multiple authors | `author = {Reader, Riley and Scholar, Morgan}`; enter all authors in the record and let the style abbreviate citations. Let the style produce `et al.` where required. |
| Organization author | `author = {{Example Seuss Reading Group}}`; the inner braces preserve a literal name. |
| Editor instead of author | Use `editor` for an edited book. For a chapter, use the chapter's `author` and the book's `editor`. |
| Known date | `date = {2025}` or `date = {2025-03-02}`. Use a full date only where appropriate to the source type. |
| Unknown date | Omit `date`; the style supplies the no-date form. Leave the field absent when the date is unknown. |
| No named author | Omit `author` and supply the title; use “Anonymous” only for a work signed Anonymous. |
| No title | Supply a concise bracketed description using the appropriate source-type guidance; inspect the output so brackets are not duplicated by a descriptor. |
| Title capitalization | Use sentence case; protect proper names, e.g., `{Dr. Seuss}`, `{The Lorax}` or `{DNA}`, with braces. |
| Edition and version | `edition = {2}` for a book edition; `version = {1.2}` for software/data. Use the source's edition or version statement. |
| Page range or article ID | `pages = {10--24}` or `eid = {e0042}`; choose the field matching the source. |
| DOI | Use the bare verified identifier in `doi`, without `https://doi.org/`. The style formats the link. |
| URL | Use a persistent URL for the exact work. Use the DOI when APA calls for it rather than a database search-session link. |
| Retrieval date | Use `urldate = {2026-10-09}` when the content changes over time and is not archived, such as a living reference entry. Use retrieval dates for sources that require them. Replace the example date with your actual access date. |
| Reprinted or translated work | Verify `origdate`, current `date`, translator, edition and publisher; cite the version consulted and inspect the two-date output. |
| Media role | APA-style fields such as `author+an:role = {1=director}` assign a role to the first listed creator. Check the role against the credits. |
| Username | `author+an:username = {1="@readingexample"}` attaches the handle to the first author; use the actual account details. |
| Special characters | Escape prose `&` as `\&` and `%` as `\%` in LaTeX-valued fields; keep URL/DOI fields as actual identifiers. |

## Cases that do not become ordinary reference entries

Personal communications that readers cannot recover usually receive an in-text citation only, for example `(A. Reader, personal communication, March 2, 2025)` after replacing the fictional details. They do not belong in the reference list. A publicly retrievable interview, recording or archived letter uses the relevant retrievable source type instead.

When quoting a source without page numbers, use a meaningful paragraph, section or timestamp locator rather than inventing pages. For a secondary citation, cite the work you actually read and follow APA's “as cited in” guidance; do not add an unread original to the reference list. Cite a specific webpage rather than an entire website when a particular claim comes from that page.

## Before submitting

Check each record against the source, read the rendered reference list and confirm that author, date, title, source, punctuation, italics and links fit that source category. Check that every in-text key resolves and every listed reference is cited. Remove all fictional entries and unused instructional prose. Confirm that each source supports the statement it accompanies.
