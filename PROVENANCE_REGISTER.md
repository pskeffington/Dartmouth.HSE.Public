# Public-source provenance and review register

**Established:** 2026-10-09  
**State:** Provisional; this file is an intake register, not a certification of authorship, rights, or university approval.

The register tracks current public artifacts and the evidence needed to decide whether they may remain public. Entries based on repository naming or existing self-descriptions are **unverified claims**, not adjudicated provenance. Nonpublic teaching documents and protected excerpts must **not** be committed here.

| Artifact / family | Claimed origin | Possible dependency | Rights evidence | Human review | Disposition |
| --- | --- | --- | --- | --- | --- |
| `02_Lecture_Notes/Week_1_*Lecture_Notes.{Rmd,md}` | Student-authored explanatory companion | R and general computing methods; no official files required | Not independently verified | Pending original-source comparison | Hold clearance |
| `02_Lecture_Notes/Week_2_*Lecture_Notes.{Rmd,md}` | Student-authored explanatory companion | R packages and synthetic practice inputs | Not independently verified | Pending | Hold clearance |
| `02_Lecture_Notes/Week_3_*Lecture_Notes.{Rmd,md}` | Student-authored explanatory companion | R packages and synthetic practice inputs | Not independently verified | Pending | Hold clearance |
| `02_Lecture_Notes/Week_4_*Lecture_Notes.{Rmd,md}` | Student-authored explanatory companion | Shell utilities and independent practice inputs | Not independently verified | Pending | Hold clearance |
| `02_Lecture_Notes/Week_2_*Lecture_Reference.md` | Compatibility study reference | Linked complete topic and weekly guides | Prior transcript-style references require review | Pending | Hold clearance |
| `02_Lecture_Notes/Week_3_*Lecture_Reference.md` | Compatibility study reference | Linked complete topic and weekly guides | Historical lecture-code blocks found | Pending | Hold clearance; history exposure |
| `03_Group_Work/Week_1_*Walkthrough.{Rmd,md}` | Independent synthetic-data study guide | R and self-contained synthetic inputs | Originality not independently verified | Pending | Hold clearance |
| `03_Group_Work/Week_2_*Walkthrough.{Rmd,md}` | Independent synthetic-data study guide | R packages and self-contained synthetic inputs | Originality not independently verified | Pending | Hold clearance |
| `03_Group_Work/Week_3_*Walkthrough.{Rmd,md}` | Independent synthetic-data study guide | R packages and self-contained synthetic inputs | Prior historical exposure; current guide replaced independently in R7 | Pending | Hold clearance; history exposure |
| `06_RESOURCES/R/` | Repository contributor's reusable statistical functions | Public R packages; optional local user data | File-by-file authorship/license review required | Partial targeted review | Hold clearance |
| `06_RESOURCES/Bash/` | Repository contributor's shell examples/helpers | Shell utilities; optional local user data | One course-specific example replaced | Partial targeted review | Hold clearance |
| `06_RESOURCES/LaTeX/` | Example manuscript and bibliography | TeX packages, bibliographic entries, third-party works | Verify license, quotation scope, attribution, and example metadata | Pending | Hold clearance |
| `06_RESOURCES/Presentation/` | Publishing scripts and styling | Local source Markdown/R Markdown | Verify script origin, stylesheet rights, and rendered output | Partial source review | Hold clearance |
| Images/PDFs and any other binary assets | Unknown until inspected | Potential licensed third-party inputs | Individual rights/permission record needed | Pending inventory | Hold clearance |
| `scripts/`, CI workflows, policy files | Repository maintenance material | GitHub Actions/public Python tooling | Verify copied snippets, licenses, contributor provenance | Pending | Hold clearance |

## Required record for each reviewed item

Document **path or glob; commit SHA; author or source; wholly original/adapted/third-party category; external source URL if public; license or permission; private source comparison performed (yes/no); reviewed by; review date; disposition; reason and remediation commit**.

Update a family-level entry only after its individual files have been inspected. Keep restricted teaching files and substantive matched excerpts in a controlled private record, not this public register.

## Release rule

No `Hold clearance` entry may be represented as cleared without human review and evidence. A clear automated screen does not close a provenance item. Review Git history separately from the current tree.

## Per-file baseline — 2026-10-09

[PROVENANCE_RECORDS.json](PROVENANCE_RECORDS.json) records every tracked path individually, with observed version, source relationship where known, and unresolved rights action. [Total repository status](ORIGINALITY_STATUS.md) records executed checks and remaining gates. These are automated intake observations; all human review decisions remain pending. Contributor declarations are not substituted for file-level human rights decisions.

The inventory joins entries by exact path, rejects duplicates, and reports changed bytes, missing paths, and obsolete entries. An observed digest is not an authorship or permission attestation. The record file's own digest is omitted to avoid recursion.

[Paul's Notes](README.md) · [History review](HISTORY_EXPOSURE_REVIEW.md)
