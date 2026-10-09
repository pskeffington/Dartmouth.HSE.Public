# Link and navigation audit

[Presentation guide](README.md) · [Resource index](../README.md) · [Repository home](../../README.md)

Checked October 8, 2026 (America/New_York). Repository navigation is checked against the local files and heading fragments. External destinations are checked separately; a timeout, access gate or retrieval failure does not establish that a link is broken for a human reader.

## Repeat the repository checks

```bash
python3 06_RESOURCES/Presentation/build_reading_editions.py --check
python3 06_RESOURCES/Presentation/check_navigation.py
```

The navigation checker covers Markdown and R Markdown paths, directory landing pages, same-page and cross-page fragments, code-fence closure and HTML stylesheet paths. It does not run R, knit HTML or verify external hosts.

## External reference access

Of 24 original external URLs, 10 returned page content and 14 could not be confirmed through the retrieval service. A verified PubMed alternate was added for the Week 1 article, bringing the checked inventory to 25 destinations. Original citations are retained; external references with unresolved access should be checked in a browser before use.

| Destination | Access result | Detail |
| --- | --- | --- |
| [https://bioconductor.org/packages/release/workflows/vignettes/rnaseqGene/inst/doc/rnaseqGene.html](https://bioconductor.org/packages/release/workflows/vignettes/rnaseqGene/inst/doc/rnaseqGene.html) | Retrieved | Page content retrieved. |
| [https://cran.r-project.org/package=survival](https://cran.r-project.org/package=survival) | Retrieved | Page content retrieved. |
| [https://doi.org/10.1093/nar/gkaf018](https://doi.org/10.1093/nar/gkaf018) | Not confirmed | Retrieval failed or an access gate prevented content verification. |
| [https://ggplot2.tidyverse.org/reference/facet_grid.html](https://ggplot2.tidyverse.org/reference/facet_grid.html) | Retrieved | Page content retrieved. |
| [https://ggplot2.tidyverse.org/reference/facet_wrap.html](https://ggplot2.tidyverse.org/reference/facet_wrap.html) | Retrieved | Page content retrieved. |
| [https://google.github.io/styleguide/shellguide.html](https://google.github.io/styleguide/shellguide.html) | Retrieved | Page content retrieved. |
| [https://link.springer.com/article/10.1186/s13058-025-02061-2](https://link.springer.com/article/10.1186/s13058-025-02061-2) | Retrieved | Page content retrieved. |
| [https://pmc.ncbi.nlm.nih.gov/articles/PMC13259627/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13259627/) | Not confirmed | CAPTCHA page returned; article content not verified. |
| [https://pubs.opengroup.org/onlinepubs/9799919799/](https://pubs.opengroup.org/onlinepubs/9799919799/) | Not confirmed | Retrieval failed or an access gate prevented content verification. |
| [https://swcarpentry.github.io/shell-novice/](https://swcarpentry.github.io/shell-novice/) | Retrieved | Page content retrieved. |
| [https://www.bmj.com/content/385/bmj-2023-078378](https://www.bmj.com/content/385/bmj-2023-078378) | Not confirmed | Retrieval failed or an access gate prevented content verification. |
| [https://www.bmj.com/content/388/bmj-2024-082505](https://www.bmj.com/content/388/bmj-2024-082505) | Not confirmed | Retrieval failed or an access gate prevented content verification. |
| [https://www.gnu.org/software/bash/manual/bash.html](https://www.gnu.org/software/bash/manual/bash.html) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.gnu.org/software/coreutils/manual/](https://www.gnu.org/software/coreutils/manual/) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.gnu.org/software/gawk/manual/](https://www.gnu.org/software/gawk/manual/) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.gnu.org/software/grep/manual/](https://www.gnu.org/software/grep/manual/) | Not confirmed | GNU host timed out during retrieval. |
| [https://www.medrxiv.org/content/10.64898/2026.06.23.26355479v1.full](https://www.medrxiv.org/content/10.64898/2026.06.23.26355479v1.full) | Not confirmed | HTTP 403 returned. |
| [https://www.nature.com/articles/s41523-026-01022-y](https://www.nature.com/articles/s41523-026-01022-y) | Not confirmed | Publisher authentication redirect blocked retrieval. |
| [https://www.nature.com/articles/s43018-024-00773-6](https://www.nature.com/articles/s43018-024-00773-6) | Retrieved | Page content retrieved. |
| [https://www.science.org/doi/10.1126/sciadv.abd2688](https://www.science.org/doi/10.1126/sciadv.abd2688) | Not confirmed | Retrieval failed or an access gate prevented content verification. |
| [https://www.shellcheck.net/](https://www.shellcheck.net/) | Retrieved | Page content retrieved. |
| [https://xrobin.github.io/pROC/](https://xrobin.github.io/pROC/) | Retrieved | Page content retrieved. |
| [PubMed alternate for the Week 1 source](https://pubmed.ncbi.nlm.nih.gov/33115748/) | Retrieved | Alternate record verified for DOI 10.1126/sciadv.abd2688. |
