#!/usr/bin/env python3
"""Conservative public-release screening; NOT a plagiarism or copyright certification."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

RESTRICTED_EXT = {".ppt", ".pptx", ".key", ".pages", ".doc", ".docx"}
REVIEW_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".zip"}
DATA_EXT = {".csv", ".tsv", ".xlsx", ".xls", ".xpt", ".rds", ".rdata",
            ".parquet", ".feather", ".sav", ".dta"}
RESTRICTED_NAME = re.compile(r"(?:^|[/_. -])(syllabus|instructor[_. -]?(?:copy|notes|solution|slides)|answer[_. -]?key|solution[_. -]?key|course[_. -]?(?:handout|packet)|lecture[_. -]?slides)(?:$|[/_. -])", re.I)
RESTRICTED_TEXT = [
    ("explicit rights restriction", re.compile(r"all rights reserved|(?:this (?:file|document|material|work) is )?for (?:enrolled )?students only|not for (?:public )?distribution", re.I)),
    ("course-platform export", re.compile(r"canvas\.dartmouth\.edu/courses/|blackboard\.dartmouth\.edu/", re.I)),
]
REVIEW_TEXT = [
    # Positive disclosure of source reuse. Rules forbidding republication are
    # policy language, not evidence that source content was republished.
    ("instructor source included", re.compile(
        r"\b(?:included|embedded|copied|reproduced|transcribed|uploaded)\b"
        r"[^.\n]{0,65}\b(?:instructor|professor|course)\b"
        r"[^.\n]{0,35}\b(?:code|material|handout|slides?|solution|prompt)\b",
        re.I)),
    ("verbatim instructor material", re.compile(
        r"\b(?:instructor|professor)[- ]provided\b"
        r"[^.\n]{0,50}\b(?:reproduced|copied|included|embedded|transcribed)\b",
        re.I)),
]
# Heuristic signals confined to public instructional publications. These warrant
# review, not a conclusive claim that material was copied.
COURSE_SPECIFIC = [
    ("lecture chunk mapping", re.compile(r"\b(?:lecture\s+\d+[,.:]?\s*)?chunks?\s*\d+(?:\s*[-–]\s*\d+)?", re.I)),
    ("verbatim-prompt indicator", re.compile(r"(?:prompts?\s+(?:below\s+)?(?:are|is)\s+preserved|copied\s+(?:from|verbatim)|original\s+(?:assignment|exercise)\s+questions?)", re.I)),
    ("assignment item mapping", re.compile(r"\bassignment\s+(?:task|item|question)\s*[|:#-]", re.I)),
]
COURSE_PUBLIC = ("02_Lecture_Notes/", "03_Group_Work/", "05_Assignments/", "06_RESOURCES/")
MAX_TEXT_BYTES = 1_000_000
SKIP = {".git", "__pycache__", ".venv", "node_modules"}
# These exact files contain quoted heuristic patterns and artificial violation
# examples. Continue checking their tracked presence, filename, and binary type,
# but do not treat their intentional test strings as published teaching content.
RULE_DOCUMENTS = {
    "scripts/check_public_originality.py",
    "ORIGINALITY_POLICY.md",
    "ORIGINALITY_ROADMAP.md",
    "PROVENANCE_REGISTER.md",
    "HISTORY_EXPOSURE_REVIEW.md",
    "tests/test_originality_screen.py",
    "tests/test_originality_scan_integration.py",
}

def tracked_files(root: Path) -> list[Path]:
    try:
        proc = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError("Run inside a Git checkout with Git available") from exc
    return [root / p.decode("utf-8", errors="surrogateescape") for p in proc.stdout.split(b"\0") if p]

def scan(root: Path) -> dict:
    findings = []
    paths = tracked_files(root)
    for path in paths:
        rel = path.relative_to(root).as_posix()
        if any(part in SKIP for part in path.parts):
            continue
        if not path.is_file():
            findings.append({"path": rel, "level": "review", "reason": "tracked path not present in working tree"})
            continue
        suffix = path.suffix.lower()
        if suffix in RESTRICTED_EXT or RESTRICTED_NAME.search(rel):
            findings.append({"path": rel, "level": "block", "reason": "restricted-format or instructor/course-material filename; manual clearance required"})
        elif suffix in REVIEW_EXT:
            findings.append({"path": rel, "level": "review", "reason": "binary/media file requires provenance and rights review"})
        elif suffix in DATA_EXT:
            findings.append({"path": rel, "level": "review", "reason": "tracked data requires source, privacy, and redistribution review"})
        data = path.read_bytes()[:MAX_TEXT_BYTES + 1]
        if b"\0" in data[:8192]:
            if suffix not in RESTRICTED_EXT | REVIEW_EXT | DATA_EXT:
                findings.append({"path": rel, "level": "review", "reason": "other binary format requires provenance review"})
            continue
        if len(data) > MAX_TEXT_BYTES:
            findings.append({"path": rel, "level": "review", "reason": "text file exceeded scan limit"})
        text = data[:MAX_TEXT_BYTES].decode("utf-8", errors="replace")
        # Treat the checker and policy documentation as rules, not evidence of violations.
        if rel in RULE_DOCUMENTS:
            continue
        for reason, pattern in RESTRICTED_TEXT:
            if pattern.search(text):
                findings.append({"path": rel, "level": "block", "reason": reason})
        if rel.startswith(COURSE_PUBLIC) and suffix in {".md", ".rmd", ".r", ".py", ".sh", ".tex"}:
            for reason, pattern in COURSE_SPECIFIC:
                if pattern.search(text):
                    findings.append({"path": rel, "level": "review", "reason": reason})
        for reason, pattern in REVIEW_TEXT:
            if pattern.search(text):
                findings.append({"path": rel, "level": "review", "reason": reason})
    findings.sort(key=lambda f: (f["path"], f["level"], f["reason"]))
    return {"status": "BLOCK" if any(f["level"] == "block" for f in findings) else ("REVIEW" if findings else "SCREEN_CLEAR"),
            "tracked_files": len(paths), "findings": findings,
            "limitations": "Heuristic screening only: scans at most the first 1 MB of each file; cannot establish originality, permission, similarity, public-domain status, or clean Git history."}

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--json", action="store_true", help="Emit machine-readable results")
    ap.add_argument("--fail-on-review", action="store_true",
                    help="Fail the gate when manual review remains unresolved")
    args = ap.parse_args()
    try:
        report = scan(args.root.resolve())
    except (RuntimeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['status']}: {report['tracked_files']} tracked files, {len(report['findings'])} findings")
        for finding in report["findings"]:
            print(f"  {finding['level'].upper()}: {finding['path']}: {finding['reason']}")
        print(report["limitations"])
    return 1 if report["status"] == "BLOCK" or (args.fail_on_review and report["status"] == "REVIEW") else 0

if __name__ == "__main__":
    sys.exit(main())
