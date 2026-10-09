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
| O5: CI originality screen | Screen tracked files for course-package indicators and accidental lecture/assignment mappings | Rule updated; CI result unverified |
| O6: Public resources | Inspect R, Bash, LaTeX, supporting scripts, images, and examples for course-derived code or data | Pending file-by-file audit |
| O7: Generated editions | Build with the updated script; run --check and link validation; inspect every generated page for old text | Pending execution |
| O8: Provenance ledger | Record origin, license, reviewer, and release decision for every nontrivial public artifact | Pending |
| O9: Git history exposure | Inspect historical commits/branches/releases for previously published instructor or assessed material | Pending; current-branch removal is insufficient |
| O10: Official comparison | Authorized reviewer compares public materials to actual Geisel lecture, prompt, and starter files | Requires privately held authoritative files |
| O11: Release gate | No BLOCK indicators; review findings adjudicated; checks green; manual approvals documented | Not cleared |

## Required acceptance commands

Run in the local checkout after syncing main:

```bash
python3 scripts/check_public_originality.py --json
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
