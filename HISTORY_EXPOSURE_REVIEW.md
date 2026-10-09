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

## Local enumeration follow-up — 2026-10-09

At baseline public main `4f91edfea8b76d9ec7632eea948ba609c2630de0`, after fetching origin, `git rev-list --objects --all` and `git cat-file --batch-check` enumerated 257 commits, 729 trees, and 497 blobs across local branches and remote-tracking refs. No tags were present. GitHub API confirmed four remote heads and no releases. The counts cover objects reachable from these local refs; they do not establish absence of other PR refs, caches, attachments, forks, or external copies. No exhaustive similarity or rights adjudication is claimed. O9 remains open.

## Restricted-source comparison — 2026-10-09

A local-only comparison against 108 authorized Week 1–3 source files found no identical source files or shared 20-token windows in the current public tree. Comparing 508 locally reachable historical blobs found 30 text-overlap blobs in earlier group-work guides and Week 3 lecture references. No whole-file byte matches were found. This confirms historical source-text overlap rather than a conclusion of infringement; details and originals remain outside Git.

A current-tree merge cannot close O9. Proposed next action: preserve a private recovery snapshot, prepare cleaned replacements for every affected published branch, obtain explicit history-rewrite authorization, update affected refs with verified leases, and request GitHub review of retained PR refs/caches. Confirm the affected ref/object set immediately before any rewrite. Do not force-push automatically. External copies and platform retention require separate handling.
