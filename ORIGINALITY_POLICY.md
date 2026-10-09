# Public originality and rights policy

This is an independent, student-authored educational repository, not an official Dartmouth publication. The repository license applies only to material its contributor has the rights to license; citations to external sources do not transfer those rights.

## Admission rules
1. Include your own explanations, original code, original graphics, and independently prepared examples.
2. Cite factual claims and adapted ideas using authoritative sources; document licenses and permission for any third-party files, figures, datasets, or substantial excerpts.
3. Do not publish instructor slides, prompts copied from assignments, solutions distributed by instructors, LMS downloads, syllabi, course-only datasets, or other restricted materials without explicit redistribution permission.
4. Paraphrasing an assignment prompt or reproducing a protected figure is not automatically permitted; when in doubt, replace it with a genuinely independent example and point readers to the authorized original.
5. Review all images, PDFs, binary assets, and generated artifacts before release.
6. Conduct human review of code and commentary for unattributed copying, including outputs from automated tools.

## Course-file dependency and public boundary

Public lecture and group-work pages may summarize general computational methods, but **must not supply enough course-specific detail to reconstruct assessed Geisel assignments**. Keep authoritative prompts, scoring rubrics, instructor examples, starter scripts, tables, reference results, and graded responses in an authorized private workspace.

Every course-related publication must be reviewed for: (a) copied or closely paraphrased prompt language; (b) reproduced lecture code and figures; (c) ready-to-submit answers; (d) embedded source data or schema exports; (e) generated Markdown or HTML that republishes content removed from its source; and (f) disclosures in prior commits. Cite public research sources where relevant. Course-file dependency is a separation of materials, **not** a legal defense against copying or an assertion that general-purpose computing resources must be inoperable.

New material requires human approval of source provenance and permission. Automated gates should flag likely problems but must not certify originality.

## Validator

Run `python3 scripts/check_public_originality.py` from the repository root, or `python3 scripts/check_public_originality.py --json` for a structured report. GitHub Actions uses `--json --fail-on-review`, so pending reviews deliberately fail the release gate. Do not treat this as a certification even when checks pass.

**BLOCK** (exit 1) indicates restrictive markers requiring removal or documented clearance. **REVIEW** (exit 0 in informational mode, exit 1 with `--fail-on-review`) requires manual verification before claiming the repository is publication-ready. **SCREEN_CLEAR** (exit 0) means no configured signatures were detected, **not** that originality or copyright clearance is established.

The script inspects tracked files in the working tree; it does not inspect untracked files, Git history, external source repositories, or similarity with Dartmouth course content. A separate reviewer must compare suspect materials with the actual teaching sources, check licensing and authorship, and inspect historical commits. Do not present its output as an institutional certification.

## Manual review record

For each public contribution, document: source/author; whether wholly original, adapted, or third-party; applicable license or permission; URLs/citations; reviewer/date; disposition (retain, replace, remove, or restrict). Store the record outside the public repository when it contains nonpublic academic materials.
