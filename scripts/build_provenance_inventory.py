#!/usr/bin/env python3
"""Create a reproducible, non-certifying inventory of Git-tracked public files."""
from __future__ import annotations

import argparse
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
        category = next((v for prefix, v in CATEGORIES.items()
                         if rel.startswith(prefix)), "other")
        entries.append({
            "path": rel,
            "category": category,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "review": "unverified",
        })
    return {
        "schema": "public-provenance-inventory-v1",
        "tracked_files": len(entries),
        "entries": entries,
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
