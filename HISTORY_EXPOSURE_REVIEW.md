# Historical Git exposure review — Dartmouth.HSE.Public

**Review date:** 2026-10-09  
**State:** Confirmed *historical availability of previously removed coursework-related content*; infringement and permissions unresolved. This is a targeted review, not an exhaustive scan of every reachable object, branch, tag, fork, or cache.

## Confirmed findings

Historical commit [3132a041436fa4d82baa919fe524b3bda69b5082](https://github.com/pskeffington/Dartmouth.HSE.Public/commit/3132a041436fa4d82baa919fe524b3bda69b5082) was inspected through GitHub's file-by-commit interface.

| Historical path | Observed at historical commit | Current-tree remediation | Determination |
| --- | --- | --- | --- |
| `03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.Rmd` | Included numbered exercise statements and worked R code; describes preserving supplied prompts | Converted to independent method notes in prior passes | Historical exposure confirmed; authorship/permissions review required |
| `02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Reference.md` | Included 21 labeled lecture reference-code sections | Reference converted to conceptual commentary in prior passes | Historical exposure confirmed; source comparison required |

Do not reproduce the historical course content in new public reports or issues. A historical commit containing reproduced instructional material may still be accessible even after the current branch is cleaned. A path's presence in history is **not**, by itself, a finding of infringement.

## Review and remediation protocol

1. **Preserve evidence privately.** Record historical commit IDs, paths, suspected origin, institution permission terms, and authorization decisions in a restricted review log. Do not copy the problematic passages into a public issue or evidence attachment.
2. **Compare to authorized source files privately.** Determine whether each item is independently authored, allowable quotation, permitted reproduction, or restricted material. Seek Geisel clarification where necessary.
3. **Inventory all reachable objects.** On an authorized local clone, inspect branches/tags, added/deleted filenames, large binaries, and the history of course directories. Review GitHub releases, attachments, actions artifacts, open PRs, forks, and externally indexed mirrors separately.
4. **Agree on remediation with collaborators.** If unauthorized material is verified, decide whether to request targeted removal or a full history rewrite, taking account of GitHub retention/caching and cloned copies. Do **not** force-push or change public history automatically.
5. **After authorized remediation**, coordinate re-cloning/reset instructions; invalidate outdated references or artifacts as appropriate; verify reachability on public refs and record checks. Old SHA links and cached copies may persist.

### Local audit commands (read-only)

```bash
git fetch --all --tags --prune
git log --all --name-status -- 02_Lecture_Notes 03_Group_Work 05_Assignments
git log --all --diff-filter=D --name-only -- 02_Lecture_Notes 03_Group_Work 05_Assignments
git branch -a
git tag -l
git rev-list --objects --all > /tmp/dartmouth-public-git-objects.txt
```

Object inventory paths and logs should remain private until reviewed. `git rev-list --objects --all` lists reachable objects; it does not verify their rights, compare source text, or cover every external clone/cache.

## Release decision

**O9 remains OPEN.** Current-tree changes do not resolve the two confirmed historic source exposures. Authoritative comparison, a complete reachable-object inventory, and a documented remediation decision are required before closing O9.
