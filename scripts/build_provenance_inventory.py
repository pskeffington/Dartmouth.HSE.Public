#!/usr/bin/env python3
"""Create a reproducible, non-certifying inventory of Git-tracked public files."""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import subprocess
from pathlib import Path

CATEGORIES = {
    "02_Lecture_Notes/": "lecture-companion",
    "03_Group_Work/": "group-study",
    "05_Assignments/": "assignment-boundary",
    "06_RESOURCES/": "independent-resource",
    "scripts/": "maintenance-script",
    ".github/": "automation",
}

def inventory(root: Path) -> dict:
    register_path = root / "PROVENANCE_RECORDS.json"
    records = {}
    if register_path.is_file():
        for record in json.loads(register_path.read_text(encoding="utf-8"))["entries"]:
            path = record["path"]
            if path in records:
                raise ValueError(f"Duplicate provenance path: {path}")
            records[path] = record
    tracked = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True,
        stdout=subprocess.PIPE
    ).stdout
    entries = []
    for raw in tracked.split(b"\0"):
        if not raw:
            continue
        rel = raw.decode("utf-8", errors="surrogateescape")
        p = root / rel
        if not p.is_file():
            entries.append({"path": rel, "status": "missing", "review": "required"})
            continue
        data = p.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        record = records.get(rel)
        evidence = "unrecorded"
        if record:
            evidence = ("pending" if not record["observed_sha256"] else
                        "current" if record["observed_sha256"] == digest else "stale")
        category = next((v for prefix, v in CATEGORIES.items()
                         if rel.startswith(prefix)), "other")
        entries.append({
            "path": rel,
            "category": category,
            "bytes": len(data),
            "sha256": digest,
            "review": "unverified",
            "provenance_record": record,
            "snapshot_evidence": evidence,
        })
    return {
        "schema": "public-provenance-inventory-v2",
        "tracked_files": len(entries),
        "entries": entries,
        "record_coverage": {
            "recorded": sum(e.get("provenance_record") is not None for e in entries),
            "unrecorded_paths": [e["path"] for e in entries
                                 if not e.get("provenance_record")],
            "obsolete_record_paths": sorted(set(records) - {e["path"] for e in entries}),
            "snapshot_evidence": dict(collections.Counter(
                e.get("snapshot_evidence", "missing") for e in entries)),
        },
        "rights_status": "UNVERIFIED",
        "warning": (
            "A digest confirms content identity, not authorship, permissions, "
            "copyright clearance, or similarity to institutional sources."
        ),
    }

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()
    result = inventory(args.root.resolve())
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
