# Originality and public-release roadmap

**Status:** Source-boundary revisions committed; clearance pending source comparison, workflow execution, and history review.  
**Updated:** 2026-10-09  
**Scope:** All tracked files in Dartmouth.HSE.Public, generated reading editions, research tools, and Git history.

## Publication standard

The public repository may explain general methods using independently written commentary and original generic tools. It must not reproduce Geisel source lectures, course-only prompts, rubrics, datasets, answer keys, assessed solutions, or substantial instructor code. Actual Geisel tasks require the official authorized files. Public general-purpose R, Bash, and LaTeX materials may remain functional; deliberate obfuscation is not a copyright safeguard.

## Gate progression

| Gate | Review and acceptance test | Status |
| --- | --- | --- |
| O1: Group-work source boundary | Replace copied prompts, task-by-task solutions, and course-bound results in Weeks 1–3 .Rmd and .md | Remediated; manual similarity check remains |
| O2: Lecture-reference boundary | Remove source-code transcriptions, chunk-number mapping, and regenerated lecture excerpts in Weeks 2–3 | Remediated; verify against restricted originals |
| O3: Lecture companions | Remove assignment-to-method matrices and lecture chunk mappings in Weeks 1–4; keep independent instruction | Remediated; source comparison pending |
| O4: Repository navigation | Explain which content is independent and where official files are required | Updated |
| O5: CI originality screen | Screen tracked files for course-package indicators and accidental lecture/assignment mappings | Full independent diagnostic checks; tracked dataset and missing-input guards added; CI results unverified |
| O6: Public resources | Inspect R, Bash, LaTeX, supporting scripts, images, and examples for course-derived code or data | Public resource and TeX files now receive course-content heuristic review; manual audit and media approvals pending |
| O7: Generated editions | Build with the updated script; run --check and link validation; inspect every generated page for old text | Exact seven-file source manifest enforced; omission/substitution regression tests committed; execution unverified |
| O8: Provenance ledger | Record origin, license, reviewer, and release decision for every nontrivial public artifact | CI per-file SHA256 inventory configured; rights provenance and individual human approvals pending |
| O9: Git history exposure | Inspect historical commits/branches/releases for previously published instructor or assessed material | Historical exposure confirmed in commit 3132a04; targeted report written; exhaustive history and remediation decision pending |
| O10: Official comparison | Authorized reviewer compares public materials to actual Geisel lecture, prompt, and starter files | Requires privately held authoritative files |
| O11: Release gate | No BLOCK indicators; review findings adjudicated; checks green; manual approvals documented | Not cleared |

## Pass 4 — resource and publication tooling review (2026-10-09)

- Removed lecture-chunk references and assignment extension language from `06_RESOURCES/R/Week_3_Reusable_Functions.R`; function behavior remains intact.
- Replaced the coursework-specific metadata filtering example in `06_RESOURCES/Bash/BASH_OPERATION_SHEET.md` with a generic categorical-filter demonstration.
- Inspected seven R Markdown and Markdown reading-edition pairs. Four lecture companions had mismatched generated headers; all four were refreshed to match their current generator output. The other three pairs already matched.
- Removed the obsolete `commented_lecture` converter, eliminating a legacy path that could regenerate copied lecture-code sections.
- Added publishing freshness, internal navigation, and Python syntax checks to the GitHub Actions originality workflow.
- No local Git checkout was available in this environment. The source comparisons were performed through the connected GitHub repository; runtime validation and CI outcomes have **not** been independently confirmed.

**Next pass:** Inspect remaining Bash and R resource examples, LaTeX bibliographies, images/media, and any historical commits that contained original course material. Verify the Actions run and reconcile failures before raising the release gate.

## Pass 5 — historical exposure and provenance (2026-10-09)

- Created [provisional provenance register](PROVENANCE_REGISTER.md) covering lecture notes, group work, R/Bash/LaTeX resources, publishing utilities, binary assets, and governance scripts. All entries remain subject to human verification.
- Confirmed that historical commit `3132a041436fa4d82baa919fe524b3bda69b5082` included numbered Week 3 group-work questions/worked code and 21 Week 3 lecture-reference code sections. These were subsequently replaced in the present tree, but remain part of the historic snapshot.
- Added [history exposure review](HISTORY_EXPOSURE_REVIEW.md) with read-only inventory commands, a private source-comparison protocol, and explicit **no automatic history rewrite** safeguards.
- Spot-checked APA 7 manuscript and practice bibliography materials. Removed the manuscript README's Week 4 coursework characterization and replaced the manuscript appendix's old Week 4 lab invocations with generic examples. The bibliography catalogue contains fictional illustrative records; author/source verification and compilation tests remain pending.
- This was a targeted connector audit, **not** a complete Git-object, binary-media, authorship, or third-party-license audit. No copyright clearance, source-originality certification, or historical remediation approval is claimed.

**Next gates:** finish individual provenance records, enumerate all reachable historic objects, inspect media and bibliography rights, execute CI and document checks, and compare against authorized Geisel files before granting release clearance.

## Pass 6 — residual course-data details and scanner reliability (2026-10-09)

- Removed the remaining classroom metadata schema, sex-field selection rules, and course-specific narrative from `06_RESOURCES/LaTeX/Example_APA_7_Manuscript.tex`; made course name a neutral placeholder.
- Generalized the quick Bash demonstration and helper examples in `06_RESOURCES/Bash/EASY_COMMAND_SHEET.md`, replacing classroom-specific metadata naming with independent categorical records.
- Clarified `06_RESOURCES/Presentation/README.md` so its instructions refer to original public study notes rather than executable Geisel lab work.
- Corrected incorrectly double-escaped regular expressions in `scripts/check_public_originality.py` that had prevented intended lecture-chunk and prompt indicators from matching.
- Added `tests/test_originality_screen.py` and configured GitHub Actions to run its regression checks. The tests verify detection logic; they do **not** establish originality.
- Attempted a fresh local clone for validation; the runtime could not resolve `github.com`. Consequently the test suite, source freshness checker, navigation scan, and GitHub Actions outcome are **not verified by execution here**.

**Priority next:** run CI and inspect results; expand provenance checks to all remaining resources/binaries; inspect full reachable Git history with an authorized clone; conduct the private Geisel-source comparison.

## Pass 7 — reliability and release-gate hardening (2026-10-09)

- Inspected the originality scanner, regression tests, reading-edition builder, and GitHub Actions configuration via connected GitHub.
- Corrected the detector to recognize `Lecture 3 chunks 10-15`, `chunk 17`, and numbered ranges. Independently checked the regular expression against positive and negative examples in a Python runtime; this did **not** execute the repository's full tests.
- Distinguished explicit restriction notices from general author-written distribution cautions, which are now review indicators instead of definitive blocks. This is classification logic, not a legal determination.
- Added `--fail-on-review`: the informational CLI still emits REVIEW with exit 0, while GitHub Actions now exits nonzero for unresolved reviews. Regression tests cover both modes.
- Attempted to inspect the public Actions page; its status could not be fetched. A GitHub checkout from this runtime also failed DNS resolution, so CI health and complete test execution remain **unverified**.
- No Git history rewrite or copyright-clearance declaration was made.

**Next:** execute the strict gate and tests in the connected repository's Actions environment, triage file-specific REVIEW findings, and continue private provenance/history comparisons before marking O5 or O11 complete.

## Pass 8 — complete diagnostics and provenance inventory (2026-10-09)

- Changed the CI originality-screening step to `continue-on-error` while retaining its reported outcome. A final unconditional step fails the job when screening did not succeed. The release gate remains fail-closed, but later diagnostic checks may still run.
- Added six Git-fixture integration scenarios in `tests/test_originality_scan_integration.py` for lecture mapping, generic independent notes, restricted filenames, missing tracked files, binary assets, and non-course resource scope.
- CI now discovers both `test_originality_screen.py` and `test_originality_scan_integration.py`.
- Added `scripts/build_provenance_inventory.py` to report tracked paths, content sizes, SHA256 digests, and review categories. The workflow saves `provenance-inventory.json` alongside `originality-report.json` as a 30-day artifact.
- **No hashes establish intellectual-property rights.** Every inventory entry defaults to unverified; the register is not a clearance list.
- GitHub checkout remains inaccessible from this runtime due DNS resolution. Connected-repository commits succeeded, but CI run results, integration-test results, and actual generated inventory are not independently verified.

**Next gate:** inspect Actions reports, triage any false-positive findings without automatically suppressing legitimate violations, and complete manual file-by-file rights review and historical exposure decisions.

## Pass 9 — self-matching audit fixture remediation (2026-10-09)

- Audited the scanner and both committed regression-test files. Found a deterministic false-positive: `tests/test_originality_screen.py` contains the literal `All rights reserved` as a positive test case, which the strict scanner would classify as BLOCK when scanning its own repository.
- Added an **exact-path** rule-document list to omit heuristic *text* matching for the two named synthetic fixture/test scripts and existing policy/evidence files. All files still receive tracked-existence, restricted filename, binary type, and size checks.
- Added two integration scenarios: the named fixture with a synthetic rights string is not a release blocker; an arbitrary unlisted `tests/test_unreviewed.py` containing the same string remains BLOCK. This avoids a blanket `tests/` exemption.
- Confirmed checkout DNS failure again in this environment. The connected GitHub commits completed, but a full source checkout and GitHub Actions result were unavailable. **The eight regression scenarios are configured, not verified as passing.**
- Historical course exposure and actual institutional permissions remain unreviewed; no change to the O9–O11 clearance decisions.

**Next:** read CI run logs/artifacts from a reachable environment; separate legitimate restricted content from synthetic fixture strings; complete remaining media/provenance source checks.

## Pass 10 — validator completeness and CI result isolation (2026-10-09)

- Audited the live `main` workflow, scanner, test files, and reading-edition builder using the GitHub connector.
- The workflow now records the individual outcomes of screening, regression tests, edition freshness, navigation, Python compilation, and provenance-inventory generation. All checks are diagnostic even after one check fails; the final step blocks on **any** unsuccessful required outcome.
- Extended `scripts/check_public_originality.py` to flag tracked structured data files (including CSV, TSV, XLSX, SAS transport, R data, and columnar data formats) for privacy, source, and redistribution review. These files are not automatically presumed infringing; unresolved reviews still fail the strict release gate.
- Added integration-test cases for CSV provenance flags and suppression of duplicate binary warnings.
- The reading-edition builder now fails if it discovers fewer than the seven expected R Markdown source files; formerly a missing source tree could result in a false-green zero-source validation.
- A fresh repository clone again failed with DNS resolution of `github.com`. The connector endpoint for commit workflow runs searches pull-request-triggered runs only and returned no runs for the inspected commit. **This is not evidence that push-triggered CI passed or failed.**
- No definitive finding of copyright infringement, clean Git history, or institutional approval has been made.

**Next:** obtain actual push-run Actions logs and artifacts, adjudicate flagged datasets/media and course-like files with original permissions, and perform the private source-to-public comparison. The final clearance gate remains open.

## Pass 11 — exact publication source manifest (2026-10-09)

- Verified the existence of the seven expected Week 1–4 lecture and Week 1–3 group-work R Markdown sources through connected GitHub.
- Replaced the previous `len(sources) < 7` gate with explicit required-path validation in `06_RESOURCES/Presentation/build_reading_editions.py`. A missing expected source now fails even if an unrelated `Week*.Rmd` file makes the count seven.
- Added `tests/test_reading_source_manifest.py` to check for manifest duplicates, presence in the current checkout, missing-but-substituted sources, and zero-source failure.
- Updated GitHub Actions to run those source-manifest tests alongside the originality regression tests.
- The expected-source manifest is intentionally maintained in code and must be updated through review when the official scope of published student-authored companions changes.
- No CI execution outcome or institutional source-comparison evidence was available through the connector. These commits update controls; they do **not** close O7 or certify originality.

**Next:** inspect the actual push-triggered Actions artifact and run logs; adjudicate media/data source provenance; conduct authorized source similarity and historic exposure review. Do not rewrite repository history without a documented authorization decision.

## Pass 12 — cross-directory instructional-source screening (2026-10-09)

- Reviewed the public scanner and identified a detection gap: lecture-chunk, verbatim-prompt, and assignment-item heuristics applied only to `02_Lecture_Notes/`, `03_Group_Work/`, and `05_Assignments/`. Course-derived passages could therefore evade this specific check if moved to the public `06_RESOURCES/` examples.
- Expanded course-content heuristic screening to `06_RESOURCES/` and to `.tex` files. This **flags** suspected reuse for manual review; it does not automatically assert infringement. Generic resources without indicators remain eligible for `SCREEN_CLEAR` in this heuristic category.
- Updated the Git-fixture integration tests to expect a resource lecture mapping to trigger `REVIEW`, to flag copied-prompt indicators in LaTeX, and to retain a negative test for generic independent resources.
- Clarified the scanner report's first-megabyte inspection limitation. Oversized text already generates a review finding and therefore cannot silently clear under the strict gate.
- Commits were made through the connected GitHub repository; actual CI execution and comparison with authorized Geisel instructional files remain unverified. Historical Git exposures remain unresolved.

**Next:** inspect current Actions artifacts, review the resulting resource-level flags against legitimate examples, then finish binary provenance and private institutional-source comparison. Do not use broad suppressions to turn CI green.

## Required acceptance commands

Run in the local checkout after syncing main:

```bash
python3 scripts/check_public_originality.py --json --fail-on-review
python3 -m unittest discover -s tests -p 'test_originality*.py' -v
python3 -m unittest discover -s tests -p 'test_reading_source_manifest.py' -v
python3 scripts/build_provenance_inventory.py --output provenance-inventory.json
python3 06_RESOURCES/Presentation/build_reading_editions.py --check
python3 06_RESOURCES/Presentation/check_navigation.py
python3 -m py_compile scripts/check_public_originality.py 06_RESOURCES/Presentation/*.py
git status --short
```

If generated editions are stale, rebuild them and inspect diffs before committing. Do not publish a page merely because a generator succeeds. CI output is an indicator screen, not a certificate of originality.

## Human review checklist

- Compare course-adjacent code, prose, plots, and examples with the restricted source in a private environment.
- Identify exact copied text, substantial paraphrase, and distinctive instructor example structure.
- Confirm that publicly posted materials are neither assessed solutions nor near-equivalent substitutes.
- Verify attribution and licensing for all third-party code and media.
- Inspect Markdown output separately from its R Markdown or R source.
- Review exposed historical material and take appropriate platform-level remediation if necessary.
- Respect the current Geisel academic-integrity, AI-use, sharing, and collaboration policy.

**Decision rule:** Do not mark the repo copyright-cleared until O6–O11 are satisfied and human review confirms provenance and permissions.
