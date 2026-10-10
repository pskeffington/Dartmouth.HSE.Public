# Historical exposure review — Paul's Notes

This review separates ordinary Git branches from GitHub-managed retention and external copies. Current-tree checks do not establish that every historical copy has disappeared.

## Ordinary branch remediation

The authorized R5 operation completed the prior history rewrite for six ordinary published branches. Its targeted inventory contained 30 historical text-overlap blobs; verification found none of those targets reachable from the six rewritten branch heads. Recovery evidence and detailed comparisons remain private. R8 performs no further history rewrite.

## Retained pull-request references

GitHub-managed references remained separately exposed at the R5 verification: closed PR #2 retained 27 targeted blobs, and closed PRs #3–5 retained 30 each. Open PR #1's inspected head and merge references had none of the 30 targets. This is a bounded observation of the target inventory, not an exhaustive clearance of every object.

Closing a PR or cleaning ordinary branches does not guarantee removal of retained refs, caches, forks, or external clones. Platform-level retention review remains open; no GitHub deletion or disappearance is claimed. Unrelated branches and PRs are not removed during R8.

## Remaining review

Keep protected excerpts and detailed source evidence outside public reports. Any further platform remediation requires a documented decision and verification of the affected references. Authorship, permission, and third-party rights review remain separate from technical reachability checks.

**O9:** ordinary-branch remediation complete; GitHub retention and external-copy review open. **O11:** rights clearance remains on hold.

[Paul's Notes](README.md) · [Current status](ORIGINALITY_STATUS.md) · [Provenance register](PROVENANCE_REGISTER.md)
