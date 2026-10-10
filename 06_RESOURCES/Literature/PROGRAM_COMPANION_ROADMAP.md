# Program-wide study companion — gated roadmap

[Paul's Notes](../../README.md) · [Follow-along](../../FOLLOW_ALONG.md) · [Weekly lesson index](../../03_Group_Work/README.md) · [Research project intake](RESEARCH_PROJECT_INTAKE.md) · [Quality gates](RESEARCH_CODE_QUALITY_MATRIX.md)

**Planning baseline:** October 10, 2026. An **independently authored, student-maintained roadmap** for expanding Paul's Notes from introductory computing through quantitative health-science methods, research ethics, advanced analyses and a culminating research portfolio. It is **not an official curriculum, enrollment plan, syllabus, academic-credit checklist, or institution-endorsed course sequence**. Course offerings, assessments, calendars and learning outcomes must be confirmed from authorized sources; do not fill unverified details by inference.

## Goal and coverage boundaries

The public companion should eventually help a student navigate an entire health-science research education: prepare prerequisites, learn concepts independently, run original synthetic examples, critique statistical assumptions, apply reproducibility standards, and create professionally communicated research outputs. It does **not** publish protected classroom exercises, notes copied from lectures, answer keys, source-derived similarity reports or restricted datasets.

**Status meanings:** `DELIVERED` = the public resource exists (not necessarily pedagogically or scientifically approved); `REVIEW_REQUIRED` = existing content needs scope/originality/scientific review; `PLANNED` = no complete guide; `BLOCKED` = cannot proceed without permissions, approved source access or other external dependency; `NOT_VERIFIED` = curriculum fact or alignment has not been established. Never call a course `COMPLETE` solely because a page or CI run exists.

## Program map — confirmed public resources versus planned themes

| Track | Course or domain | Public coverage today | Next independent companion | Status |
| --- | --- | --- | --- | --- |
| Foundations | HSE 711 — foundations in data science (course title supplied by maintainer; not verified against a current institutional catalogue here) | [Weeks 1–4](../../03_Group_Work/README.md) and [topic companions](../../02_Lecture_Notes/README.md) | Finish a source-guarded biomedical-context revision; map *verified* remaining competencies only after authorized review | `REVIEW_REQUIRED` |
| Quantitative methods | HSE 712 — biostatistics (maintainer-supplied course title; current syllabus unverified) | [R summary and plot resources](../README.md), [research software quality](RESEARCH_CODE_QUALITY_MATRIX.md) | Independent modules on design, uncertainty, model assumptions, multiple testing and interpretation | `PLANNED` |
| Responsible computing | HSE 713 — ethics of AI (maintainer-supplied course title; current syllabus unverified) | [AI governance reference anchors](BIOMEDICAL_CODING_STANDARDS.md) | Independent modules on intended use, harm, privacy, fairness, leakage, shift and human oversight | `PLANNED` |
| Evidence interpretation | Epidemiology and observational study methods — **domain placeholder, not a confirmed course** | [Biomedical research methods](BIOMEDICAL_CODING_METHODS.md) | Study design, sampling, confounding, measurement, missingness and reporting | `PLANNED` |
| Health information | Clinical informatics / longitudinal patient data — **domain placeholder** | [Interoperability and metadata standards](INTEROPERABILITY_METADATA_STANDARDS.md) | Standards-aware person/visit/specimen/time data handling and terminology mapping | `PLANNED` |
| Translational methods | Genomics and reproducible bioinformatics — **domain placeholder** | [Biomedical coding standards](BIOMEDICAL_CODING_STANDARDS.md), [biomedical methods](BIOMEDICAL_CODING_METHODS.md) | Assay identity, feature annotation, counts, normalization and defensible modeling | `PLANNED` |
| Applied synthesis | Research design, manuscripts, capstone / portfolio — **program stage, not a confirmed course label** | [Research planning](../../01_Capstone/README.md), [APA manuscript resources](../LaTeX/README.md) | Independent question-to-results workflow, reporting, reproducibility, limitations and portfolio narrative | `PLANNED` |

**Scope rule:** Do not invent HSE course numbers, required credits, assessment rubrics, schedules, degree milestones or a prescribed course order. Replace placeholders only after independently confirming current public catalogue information and, for private source-based alignment, completing authorized local review.

## Gates: from subject discovery to a trustworthy public companion

| Gate | Completion evidence | Required disposition |
| --- | --- | --- |
| P0 — Authorized scope | Course title/period and permitted public general competencies identified; protected-source rights reviewed privately when applicable | `PASS`, `BLOCKED` or `NOT_VERIFIED` |
| P1 — Competency design | Public original list of measurable concepts, prerequisite graph, scope exclusions, scientific vocabulary and intended audience | Do not copy protected lecture outcome phrasing |
| P2 — Evidence baseline | Primary manuals, current domain guidance and critical limitations linked in a versioned literature matrix | Distinguish authority, community advice and local conventions |
| P3 — Independent authoring | Concept companion and full teaching guide created with original explanations and synthetic/openly licensed inputs | Same scientific context, independent expressive design |
| P4 — Practical learning | Runnable examples, defined units and objects, expected outputs, independent exercises and error recovery | Demonstrates usable learning, not only a file's existence |
| P5 — Technical verification | Parse and run in clean environment; check data contracts, dimensions, joins, units, numerical diagnostics and rendered docs | Passing CI does not prove scientific validity |
| P6 — Scientific and accessibility review | Domain checks, sample-size/denominator/uncertainty interpretation, readable headings, navigation and beginner teach-back | Unknowns and limitations visible |
| P7 — Originality, rights and provenance | Required checkout-local private-source comparison for **lesson/source-dependent changes**; appropriate licenses and provenance | No GitHub-API or hook bypass for protected-source changes |
| P8 — Public release and support | Guarded PR merged, links functional, published edition consistent with source, issue route and update ownership defined | Release SHA and date recorded |
| P9 — Retention and refresh | New-term compatibility and upstream software/reference updates reviewed; broken examples repaired | Not automatically green after an earlier term |

A gate passes only with recorded evidence. If a course-specific rights gate is blocked, continue building **independent public reference literature** where permitted, but do not publish source-dependent lessons.

## Repeatable 10-week companion pacing template

This is a **planning cadence**, not a claim that every course has ten identical teaching weeks or these precise topics.

| Course phase | Independently authored companion work | Evidence required |
| --- | --- | --- |
| Weeks 1–2 | Verify public scope; publish a glossary, prerequisite audit and methods literature baseline | Traceable public references and declared unknowns |
| Weeks 3–4 | Build and independently review the first practical concepts | Valid source-free examples and beginner walkthrough |
| Weeks 5–6 | Add intermediate applications, data contracts and deliberately invalid test cases | Execution records and scientific interpretation review |
| Weeks 7–8 | Add integration/synthesis exercises, reusable functions and reproducibility checks | Clean-session reproduction and navigation acceptance |
| Weeks 9–10 | Deliver a consolidation guide, troubleshooting map and mastery checklist | Independent teach-back, completeness review and authorized publication |

For asynchronous, shorter or longer courses, scale by **phase** rather than inventing calendar dates. Avoid publicizing private assignment due dates or detailed protected lecture sequences.

## Cross-program prerequisites

| Competency | Needed before | Canonical independent reference |
| --- | --- | --- |
| Basic R objects, indexing and missingness | Wrangling, analysis and modeling | [R fundamentals](../../02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) |
| Identifiers, reshaping and visualization | Longitudinal data, survey analysis and repeated measures | [Week 2 companion](../../02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) |
| Joins, model scales and interpretation | Biostatistics, epidemiology and clinical informatics | [Week 3 companion](../../02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) |
| Shell, reproducibility and logging | Repeated research pipelines | [Bash companion](../../02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.md) |
| Data dictionaries, provenance and gate decisions | All advanced research courses | [Project intake](RESEARCH_PROJECT_INTAKE.md), [quality matrix](RESEARCH_CODE_QUALITY_MATRIX.md) |
| Responsible inference and reporting | Manuscripts, AI, capstone or portfolio | [Biomedical methods](BIOMEDICAL_CODING_METHODS.md), [interoperability](INTEROPERABILITY_METADATA_STANDARDS.md) |

## Acceptance contract for each future course landing page

Create a publicly usable landing page only when the course/domain scope is genuinely supported. Each page should include: independent course-domain description; the verified-versus-provisional coverage distinction; prerequisites; public objectives in original wording; module/weekly navigation; software and scientific data contracts; authoritative reference matrix; complete original examples; exercises with feedback criteria rather than classroom answers; accessibility and readability checks; provenance and rights notes; status/gate evidence; and an update log.

A public landing page should not imply that the companion is a substitute for enrollment or the institution's materials. A domain page can exist without claiming any particular course equivalence.

## Active backlog (dependency ordered)

| Priority | Task | Entry condition | Exit evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Audit HSE 711 Weeks 1–4 for misleading nonbiomedical metaphors and objective coverage | Authorized private comparison environment for classroom alignment | Independently rewritten biomedical examples, guarded push and verified reading editions | `BLOCKED` for source-derived publication in this GitHub-only workflow |
| 2 | Complete the public methods resource taxonomy and standard naming rules for future course reuse | Public primary references | Versioned source/evidence matrix and stable navigation | `DELIVERED` for existing reference slices; further improvement open |
| 3 | Start a standalone biostatistics concept-and-evidence outline | Verify publicly available scope; do not rely on private syllabus | Independent reference set and objectives explicitly labeled preliminary | `PLANNED` |
| 4 | Start a standalone responsible-clinical-AI concept-and-evidence outline | Verify public guidance and domain scope | Independent responsible-AI literacy resource without claims about course syllabus | `PLANNED` |
| 5 | Build cross-course reproducible project scaffold and data-dictionary examples | Separate executable-code rights and publishing review | Original fixtures, contracts, test evidence and guarded release if source-dependent | `PLANNED` |
| 6 | Establish final program-level research synthesis and portfolio index | Prior methods and reporting resources available | Question-to-method-to-output reproducible narrative with clear limitations | `PLANNED` |
| 7 | Review all companion links, freshness, accessibility and provenance at each term boundary | Completed/released modules | Dated revalidation records, reviewed source version changes | `PLANNED` |

## Governance, honesty and ownership

This roadmap measures an **independent public companion**, not academic progress toward a credential. It must never imply coverage of undisclosed course requirements, certify that code or plots are medically valid, or claim that a repository scanner provides copyright clearance. For each future course intake, record public evidence, decision owner, implementation status, blockers and the next gate. Do not mark placeholders as confirmed courses. The public project is independently maintained and not institutionally endorsed.
