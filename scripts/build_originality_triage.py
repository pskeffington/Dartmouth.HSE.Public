#!/usr/bin/env python3
"""Turn heuristic originality findings into an evidence-focused review queue."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

def review_action(reason: str) -> str:
    reason = reason.lower()
    if "binary" in reason or "media" in reason:
        return "Check origin, embedded assets, license, and reproducible build lineage."
    if "tracked data" in reason or "redistribution" in reason:
        return "Verify data origin, privacy obligations, permission, and release terms."
    if "course" in reason or "instructor" in reason or "lecture" in reason:
        return "Compare privately with authorized course files; verify authorship and permission."
    if "distribution warning" in reason or "rights restriction" in reason:
        return "Determine whether the wording is original cautionary prose or a third-party rights notice."
    if "missing" in reason:
        return "Restore tracked file or remove it through a reviewed commit."
    return "Determine provenance, rights, and disposition through documented human review."

def render(report: dict) -> str:
    if report.get("status") not in {"BLOCK", "REVIEW", "SCREEN_CLEAR"}:
        raise ValueError("Unrecognized originality report status")
    findings = report.get("findings")
    if not isinstance(findings, list):
        raise ValueError("Missing findings array")
    rows = []
    for finding in findings:
        if not all(isinstance(finding.get(k), str) for k in ("path", "level", "reason")):
            raise ValueError("Incomplete finding")
        if finding["level"] not in ("block", "review"):
            raise ValueError("Unrecognized finding level")
        rows.append(finding)
    counts = Counter(x["level"] for x in rows)
    out = [
        "# Current public-release review queue", "",
        f"**Scanner state:** {report['status']}  ",
        f"**Tracked files:** {report.get('tracked_files', 'unknown')}  ",
        f"**Unresolved indicators:** {len(rows)} ({counts['block']} block, {counts['review']} review)", "",
        "The queue is generated from a heuristic scan. It is neither a rights determination "
        "nor a record of clearance. Never copy restricted instructional content into this report.", "",
    ]
    if not rows:
        out += ["No configured indicators were found. Manual provenance and historical "
                "review are still required before publication.", ""]
    else:
        out += ["## File-specific review", ""]
        for finding in sorted(rows, key=lambda x: (x["path"], x["level"], x["reason"])):
            out += [
                f"### \`{finding['path']}\`",
                f"- Indicator: **{finding['level'].upper()}** — {finding['reason']}",
                f"- Required action: {review_action(finding['reason'])}",
                "- Human reviewer / date: **PENDING**",
                "- Permission or original-authorship evidence: **PENDING**",
                "- File-version confirmation: **PENDING**",
                "- Disposition: **HOLD**", "",
            ]
    out += ["## Closure conditions", "",
            "Resolve each indication with documented file-level evidence and authorized "
            "source comparison. Update provenance records and historical exposure decisions. "
            "Do not remove warnings merely to pass CI; do not mark the repository cleared "
            "on the strength of hashes or absent regex matches.", ""]
    return "\n".join(out)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Input originality-report.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    args.output.write_text(render(report), encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
