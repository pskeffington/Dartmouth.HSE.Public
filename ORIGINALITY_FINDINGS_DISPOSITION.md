# Originality findings — baseline disposition and remaining evidence

**Review date:** 2026-10-09  
**Baseline:** Executed strict scan recorded in [ORIGINALITY_STATUS.md](ORIGINALITY_STATUS.md): 12 REVIEW indicators across 12 paths, zero BLOCK indicators.  
**Scope:** Current-tree heuristic triage, not a determination of intellectual-property ownership or permission.

## Ten policy-text indicators

The following original public-course-boundary statements were reviewed by inspection. Their prior heuristic flags were triggered by admonitions **not to reproduce** restricted material or by guidance to obtain starter code privately. Such guidance does not itself assert that protected material was copied. The scanner's two broad regexes have been replaced by narrower affirmative-reuse indicators; corresponding tests cover both cautionary text and explicit declarations of copied instructor content.

| File | Prior indicator | Triage | Rights/provenance state |
| --- | --- | --- | --- |
| `02_Lecture_Notes/README.md` | Instructor/course-source reference in a prohibition | Protective policy wording; retain | UNVERIFIED |
| `02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.Rmd` | No-reproduction caution | Protective authorship boundary; retain | UNVERIFIED |
| `02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md` | Same generated notice | Protective boundary; retain; verify source correspondence | UNVERIFIED |
| `03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.Rmd` | Authorized source-location guidance | Source dependency notice; retain | UNVERIFIED |
| `03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md` | Same generated guidance | Retain; verify source correspondence | UNVERIFIED |
| `03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.Rmd` | Authorized source-location guidance | Source dependency notice; retain | UNVERIFIED |
| `03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.md` | Same generated guidance | Retain; verify source correspondence | UNVERIFIED |
| `03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.Rmd` | Authorized source-location guidance | Source dependency notice; retain | UNVERIFIED |
| `03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.md` | Same generated guidance | Retain; verify source correspondence | UNVERIFIED |
| `05_Assignments/README.md` | Prohibition on copied prompts | Protective policy wording; retain | UNVERIFIED |

**Result:** Scanner-classification defects addressed in code. This is *not* approval of those ten files for publication. The bounded Week 1–3 comparison recorded in the status report, contributor authorship, and applicable course sharing policy require separate consideration. Current-source assertions are not institutional permission.

## Contributor-declared custom-template classification — 2026-10-09

The contributor identifies both APA 7 assets as independently developed, general-purpose examples, **not adaptations of a Dartmouth/Geisel template**. This is a recorded contributor declaration, not an independent institutional similarity determination. Applying a widely used manuscript format is not itself evidence that a file reproduces protected Dartmouth expression.

The user's local PDF audit verified the exact recorded SHA-256 for both compiled files, with no missing inspection tools:

| Custom example | Observed PDF SHA-256 | Confirmed evidence | Open evidence |
| --- | --- | --- | --- |
| `06_RESOURCES/LaTeX/Example_APA_7_Manuscript.pdf` | `18ab38b366fd2fa13e9b1636d4b2881896fa9fd3b11633ced3447bb0c9e13273` | Matches intake; six letter-sized pages; TeX and bibliography inputs identified | Fresh isolated TeX/Biber build and page comparison; third-party/font rights; reviewer/date |
| `06_RESOURCES/LaTeX/Example_APA_7_Reference_Catalogue.pdf` | `612d0876e69b9ca55770a5c158c787ad53797fffc4166963e45f93e7d56ece4d` | Matches intake; five letter-sized pages; TeX and practice bibliography inputs identified | Fresh isolated TeX/Biber build and page comparison; third-party/font rights; reviewer/date |

**Classification:** `CONTRIBUTOR_DECLARED_INDEPENDENT_TEMPLATE` for Dartmouth-origin classification only. **Rights state:** `UNVERIFIED`; **release decision:** `HOLD`. The heuristic scanner's generic PDF/media review findings are still valid as provenance reminders. Do not suppress them based on the contributor statement or byte-identical intake snapshots.

## Two PDF provenance reviews still open

| File | Known evidence | Required closure | State |
| --- | --- | --- | --- |
| `06_RESOURCES/LaTeX/Example_APA_7_Manuscript.pdf` | Current manuscript was locally rebuilt from sanitized TeX and checked visually in the recorded prior audit | Associate exact binary SHA256 with exact TeX/Bib input versions, preserve compiler/toolchain evidence, confirm contributor rights and fonts/assets, record human reviewer/date | HOLD |
| `06_RESOURCES/LaTeX/Example_APA_7_Reference_Catalogue.pdf` | Prior audit inspected extracted text of 52 fictional bibliography entries; full visual and rebuilt-source comparison pending | Rebuild and visually inspect, verify bibliography inputs, third-party licensing and font/package handling, record exact binary hash and reviewer/date | HOLD |

The scanner intentionally continues to flag PDF binaries until provenance is actually adjudicated. **Do not add a global PDF exception**, and do not treat a previously successful build as rights clearance.

## Historical finding outside the 12-file current-tree queue

The private-source comparator documented **30 overlapping historical blobs** in old coursework-guides and lecture references; current files had no 20-token overlaps in the bounded 108-file corpus. Historical overlap may still be accessible on Git refs. [Historical review](HISTORY_EXPOSURE_REVIEW.md) and the authorized rights decision remain open. No history rewrite was performed.

## Evidence required before O11

1. Execute the updated suite and scanner in the current checkout; attach the resulting report without restricted excerpts.
2. Verify both PDF source-to-binary lineages and applicable author/third-party rights.
3. Resolve all file-level provenance records against current content hashes and actual reviewer evidence.
4. Complete the institutional course-policy and historical exposure decision.

**Status: HOLD CLEARANCE.** Reduced heuristic noise is not evidence of original authorship or permission.
