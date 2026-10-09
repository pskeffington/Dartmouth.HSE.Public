# Total repository originality status

**Date:** 2026-10-09
**Repository:** `pskeffington/Dartmouth.HSE.Public` only
**Decision:** REVIEW REQUIRED — originality and rights clearance remain unverified.

This report continues the [originality roadmap](ORIGINALITY_ROADMAP.md). It distinguishes execution evidence from authorship, permissions, source comparison, and historical remediation. It does not assign an originality percentage: the available evidence cannot support one.

## Verified baseline

The starting public main commit was `4f91edfea8b76d9ec7632eea948ba609c2630de0`, containing 77 tracked files. This batch adds this report, a [per-file record](PROVENANCE_RECORDS.json), and provenance regression tests. All 83 paths have an intake record; none is individually rights-cleared. The records identify file versions and remaining evidence, rather than asserting authorship from a Git commit.

| Check | Executed result |
| --- | --- |
| Strict originality scanner | REVIEW; 12 findings across 12 paths; zero BLOCK findings; expected exit 1 |
| Originality regression suite | 32 tests pass, including missing records, duplicate records, obsolete records, and changed-content detection |
| Reading-edition freshness | All seven generated editions current |
| Local navigation | Pass; external destinations are not verified by this check |
| Python compilation | Validation and publishing scripts compile |
| Independent Bash practice block | Header plus R01 and R03; selected-record count 2 |
| Manuscript PDF | Rebuilt from current TeX/BibLaTeX sources; six pages visually inspected; former course schema and lab commands absent from extracted text |

The [baseline GitHub Actions run](https://github.com/pskeffington/Dartmouth.HSE.Public/actions/runs/37985520307) completed with failure. Job logs confirm SCREEN failed while tests, editions, navigation, compilation, and inventory succeeded. The workflow's final enforcement step preserved the closed release gate. A failed strict screen is an unresolved review decision, not proof of infringement or a broken test suite.

## Findings requiring a decision

| Paths | Evidence | Required closure |
| --- | --- | --- |
| `02_Lecture_Notes/README.md` | Reference to instructor-supplied materials | Compare current wording with authorized sources; document the boundary |
| Week 3 lecture notes, `.Rmd` and `.md` | Distribution caution triggers the heuristic | Confirm caution is original policy prose and complete source comparison; retain cautions as appropriate |
| Weeks 1–3 group-work guides, `.Rmd` and `.md` | Reference to instructor-supplied materials | Record authorized comparison and disposition for each source and generated counterpart |
| `05_Assignments/README.md` | Reference to official source materials | Verify boundary wording and original authorship |
| Both LaTeX PDFs | Binary assets require individual provenance | Document source/build lineage, font/package rights, third-party inputs, and reviewer disposition |

The source boundary notices remain intact. This batch does not suppress any finding or change the scanner's release decision.

## Resource and binary review

The previous manuscript PDF still exposed the course-specific six-field metadata schema and Week 4 lab invocations after its TeX source had been generalized. This batch replaces it with a fresh build of the current neutral source. The title page now uses institution/course placeholders; the appendix contains only generic inspection commands. Its retained bibliography cites books rather than reproducing their contents. This establishes current content and build lineage, not ownership of all embedded assets.

The independent Bash example wrote `category_a.txt` but attempted to read an obsolete filename. Both reads now match the written file and the entire practice block was executed. The R quick sheet's remaining course-specific variable list has been replaced with general advice to use authorized inputs and their documentation.

The reference catalogue's extracted text identifies 52 fictional practice records with placeholder URLs. Its existing PDF was inspected through text extraction, but has not been rebuilt or fully visually reviewed in this batch. The bibliographic examples are not verified empirical references. Individual contributor provenance, any adapted snippets, and TeX font/package redistribution terms remain open for both PDFs and source templates.

## History coverage

After fetching origin, local refs enumerate 257 reachable commits, 729 trees, and 497 blobs; no tags were present. GitHub's heads endpoint confirmed four remote branches at the baseline. Its releases endpoint returned no releases. These are enumeration results, not an exhaustive rights review of each object. The [historical exposure report](HISTORY_EXPOSURE_REVIEW.md) remains open. PR refs, cached objects, Actions artifacts, forks, and external copies require separate review. No history was rewritten.

## Completion roadmap

| Order | Deliverable | Completion evidence |
| --- | --- | --- |
| 1 | Import the existing review record once its location is supplied | Identify reviewer, date, exact artifact versions, scope, permission basis, and gaps; keep restricted originals outside this public repo |
| 2 | Reconcile every per-file provenance record | Original/adapted/third-party disposition, actual author/source, license or permission, and human sign-off tied to current bytes |
| 3 | Close course-source comparisons | Authorized comparisons for O1–O3 and O10, including generated editions; replacements or permission evidence for any overlap |
| 4 | Complete resource/media review | Inspect all remaining R/Bash/LaTeX/tooling assets and catalogue pages; verify third-party licenses and PDF source/build correspondence |
| 5 | Adjudicate historical exposure | Review enumerated objects and platform surfaces; document remediation decision and obtain explicit authorization before a history rewrite |
| 6 | Close O11 | No unresolved BLOCK/REVIEW indicators, current provenance evidence, recorded human decisions, verified CI, and closed history decision |
| 7 | Close each work batch on main | Validate, commit, create a reviewable PR, merge into main, and synchronize the local checkout |

The user supplied local Week 1–3 comparison sources. These were read locally and not uploaded. They establish a comparison corpus, not an authorship or permission attestation. The active goal remains open through the unresolved gates.

## Evidence model and sources

Run `python3 scripts/build_provenance_inventory.py --output /tmp/hse-public-provenance.json` for current file digests, record coverage, obsolete paths, and changed snapshots. `current` means bytes match an observed baseline; it never means rights-cleared. The record file's own digest is deliberately omitted to avoid self-reference. Newly edited records must be tied to a new observation; do not carry forward a stale content claim.

Original expression, methodological novelty, and reuse permission are separate questions. Copyright protects qualifying expression rather than methods or facts; a root MIT notice cannot establish rights in contributed third-party material. See the [U.S. Copyright Office overview](https://www.copyright.gov/what-is-copyright/) and [MIT license text](https://opensource.org/license/mit). Where automated generation was used, human authorship must be assessed from the actual contribution; prompts or Git authorship alone do not establish it. See the [Copyright Office AI copyrightability report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf), especially its conclusions. This report makes no registration or institutional-approval claim.

## Local restricted-source comparison — follow-up

Compared the public tracked tree against 108 local files from the user-designated Week 1–3 folders. All 108 received streamed SHA256 comparison; 50 eligible text/PDF files received normalized 20-token-window comparison. Larger datasets and nontext assets received byte comparison only. Zero current byte matches or shared 20-token windows were found. This is a bounded comparison result, not proof of independent authorship: paraphrases, shorter copied fragments, partial datasets, and transformed figures can evade detection.

History enumeration compared 508 reachable blobs by bytes and eligible text blobs by normalized tokens. Zero whole-file byte matches were found, but 30 historical blobs had shared token windows, including old Week 1–3 group-work guides and Week 3 lecture references. Some had hundreds of matched windows. No restricted excerpts, filesystem locations, source files, or source hashes are included in this public report. Detailed findings remain outside the repository.

The current tree passes this source comparison; **historical source-text exposure remains unresolved**. Current-tree cleanup and a regular main merge cannot remove old blobs. A history remediation decision must cover all affected branches, PR refs, retained Actions artifacts, and GitHub caches; external clones cannot be erased by Git operations. Full-history clearance is not claimed.

### Run the source comparison locally

Use [compare_private_sources.py](scripts/compare_private_sources.py) with one or more `--private-source-dir` arguments pointing to authorized local directories, `--history` when required, and `--output` pointing outside this repository. Reports contain public paths, opaque source IDs, and match counts, never matched source text. The scanner rejects source folders and output paths inside the public repository. It fails on empty source corpora and returns nonzero when current or historical matches are found. CI uses synthetic fixtures; restricted originals must never be supplied to public Actions jobs.

Six additional tests cover byte copies, normalized overlap, independent text, source-directory containment, deleted historic content, and empty source sets. The originality suite has 26 passing tests; the integrated reading-source manifest adds four, with two further resource-screening tests, for 32 total. No source corpus or private comparison report is committed.
