#!/usr/bin/env python3
"""Validate independent biomedical bibliography metadata without claiming scientific reproduction."""
import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

COLUMNS = (
    "paper_id doi year title study_type primary_url unit objective_ids "
    "method_summary execution_steps reason_for_method code_availability "
    "data_access reproduction_status verification_status score relevance_note"
).split()
VALID_STATES = {"DISCOVERED", "METADATA_VERIFIED", "METHOD_EXTRACTED",
                "EXECUTION_SPECIFIED", "REPRODUCED", "SYNTHETIC_DEMO_ONLY", "REVIEW_REQUIRED"}
LEGACY_REPRO = {"NOT_RUN", "PASS", "FAIL"}
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
OBJECTIVE_PATTERN = re.compile(r"^U(6|7|8|9|10)-[1-9]\d*$")

def validate(path: Path) -> tuple[list[str], list[str], int]:
    errors, warnings = [], []
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            return ["empty file"], [], 0
        if reader.fieldnames != COLUMNS:
            errors.append("schema mismatch: expected exact ordered headers: " + ",".join(COLUMNS))
        seen_ids, seen_dois = set(), set()
        n_rows = 0
        for lineno, row in enumerate(reader, 2):
            n_rows += 1
            if None in row:
                errors.append(f"line {lineno}: extra CSV columns")
            if any(v is None for v in row.values()):
                errors.append(f"line {lineno}: missing CSV cells")
            get = lambda key: (row.get(key) or "").strip()
            key, doi = get("paper_id"), get("doi").lower()
            if not key or key in seen_ids:
                errors.append(f"line {lineno}: empty/duplicate paper_id {key!r}")
            seen_ids.add(key)
            if not DOI_PATTERN.fullmatch(doi) or doi in seen_dois:
                errors.append(f"line {lineno}: invalid/duplicate DOI {doi!r}")
            seen_dois.add(doi)
            try:
                year = int(get("year"))
                if year < 1900 or year > 2026:
                    errors.append(f"line {lineno}: implausible year {year}")
            except ValueError:
                errors.append(f"line {lineno}: year must be integer")
            for col in ("title", "study_type", "method_summary", "execution_steps",
                        "reason_for_method", "relevance_note", "code_availability", "data_access"):
                if not get(col):
                    errors.append(f"line {lineno}: missing {col}")
            url = urlparse(get("primary_url"))
            if url.scheme != "https" or not url.netloc:
                errors.append(f"line {lineno}: source URL must be HTTPS")
            objectives = get("objective_ids").split(";")
            if not all(OBJECTIVE_PATTERN.fullmatch(obj) for obj in objectives):
                errors.append(f"line {lineno}: malformed objective identifier(s)")
            if not re.fullmatch(r"(?:[6-9]|10)(?:-(?:[6-9]|10))?", get("unit")):
                errors.append(f"line {lineno}: malformed unit range")
            verification, reproduction = get("verification_status"), get("reproduction_status")
            if verification not in VALID_STATES:
                errors.append(f"line {lineno}: unrecognized verification_status {verification!r}")
            if reproduction not in LEGACY_REPRO | VALID_STATES:
                errors.append(f"line {lineno}: unrecognized reproduction_status {reproduction!r}")
            if reproduction in {"REPRODUCED", "PASS"}:
                errors.append(f"line {lineno}: reproduction claim requires external run-log and artifact audit")
            raw_score = get("score")
            if raw_score:
                try:
                    score = float(raw_score)
                    if not 0 <= score <= 100:
                        errors.append(f"line {lineno}: score outside 0..100")
                except ValueError:
                    errors.append(f"line {lineno}: score is not numeric")
            elif verification not in {"DISCOVERED", "REVIEW_REQUIRED"}:
                warnings.append(f"line {lineno}: progressed candidate has no scored relevance")
            if verification == "DISCOVERED":
                warnings.append(f"line {lineno}: candidate not independently metadata-verified")
        if not n_rows:
            errors.append("no bibliography records")
    return errors, warnings, n_rows

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path,
                        default=Path("06_RESOURCES/Literature/BIOMEDICAL_CORPUS_2026_CANDIDATES.csv"))
    args = parser.parse_args()
    errors, warnings, count = validate(args.path)
    for msg in errors:
        print("FAIL:", msg)
    for msg in warnings:
        print("REVIEW:", msg)
    print(f"Checked {count} corpus rows; errors={len(errors)}; review_notices={len(warnings)}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
