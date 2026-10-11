# Publishing original work

[Paul's Notes](README.md) · [Publication rules](AGENTS.md)

Original learning guides, scientific code, research documentation and synthetic
examples can use the `ORIGINAL_WORK` pathway regardless of academic topic or
folder name. Document the authoring process once, refresh the automated manifest
for edited files, and run the usual guarded publication workflow. A separate
human rights approval is needed for uncertain origin or reuse, not every routine
revision of original text.

## Record the authoring evidence

Keep a JSON authoring record outside public Git, for example in your local
temporary workspace. Describe the actual method and inputs; do not include
protected passages, fingerprints or comparison reports. This example applies
only if it accurately describes your work:

```json
{
  "method": "I developed this counting explanation from my own invented specimen example, checked the arithmetic independently, and wrote the interpretation in my own words.",
  "inputs": [
    {
      "kind": "own-work",
      "reference": "My invented specimen-count example and independently checked calculation",
      "use": "independently-written"
    }
  ]
}
```

Supported input pairs are `own-work` / `independently-written`,
`public-concept-reference` / `concepts-only` (identify a public URL), and
`synthetic-generation` / `simulated-data` (identify the actual generator).
`synthetic-example` requires a generator input. Copied external expression needs
verified license/permission evidence in the existing rights-review workflow.
Do not label restricted inputs as own work or use this sample as a declaration
when the facts differ. The manifest does not prove authorship or copyright clearance.

With the existing executable guard and authorized private inventory installed,
record a batch of public paths from the checkout root:

```bash
python3 scripts/record_original_work.py \
  --category documentation \
  --evidence /tmp/my-authoring-evidence.json \
  path/to/my-guide.md path/to/my-other-guide.md
```

Categories are `documentation`, `research-software`, and `synthetic-example`.
The command computes content hashes and records available evidence and contributor
identity in `.git/original-work-manifest.json`. It requires the configured live
protected inventory and refuses unsafe paths, unsupported categories, copying,
uncertain licensing, contradictory review records and unresolved similarity.
It saves no batch changes if any candidate fails. The pre-push hook separately
checks committed bytes and newly introduced history, including subsequently
deleted files. Keep earlier manifest versions for commits that have not yet been
published. After a revision or rename, rerun the batch command with the appropriate
evidence; no new manual approval is required for eligible original work.

## Run the normal gates and publish

Update each changed file's observed digest in `PROVENANCE_RECORDS.json`, preserving
all other metadata and the register's intentional null self-digest. These observations
confirm public content identity; they do not approve rights.

```bash
python3 -m unittest discover -s tests -v
python3 06_RESOURCES/Presentation/build_reading_editions.py --check
python3 06_RESOURCES/Presentation/check_navigation.py
python3 -m py_compile scripts/*.py 06_RESOURCES/Presentation/*.py
python3 scripts/build_provenance_inventory.py --check --output /tmp/provenance-inventory.json
python3 scripts/check_originality_change.py --base origin/main --output /tmp/originality-change.json
git diff --check
```

Run the configured private-source comparison and any relevant executable-example
validators as described in [AGENTS.md](AGENTS.md). Then inspect and commit only
the intended public files, push normally, and open a PR. Merge after the required
checks and reviews pass. Never publish the private inventory, manifest, source
inputs or detailed comparisons, and never bypass or replace hooks to obtain a pass.

Exact and substantive normalized copying remain blocked even with an authoring
manifest. Similarity, unsupported provenance, unverified media, uncertain licenses
or conflicting origin evidence require review. Standalone datasets/media can also
trigger existing public originality checks, which this pathway does not remove.
An unavailable protected inventory is not evidence of independence. Existing
byte-identical remote reviews may remain unresolved during an unrelated change;
technical success never certifies full repository or historical copyright clearance.
