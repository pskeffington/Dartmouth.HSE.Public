#!/usr/bin/env python3
"""Offline scholarly citation inventory. This is NOT scientific claim verification.

Produces stable, machine-readable findings without network requests, PHI access,
or copying institutional source material. External metadata verification and
claim-level appraisal remain distinct human/research review gates.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOI = re.compile(r"(?<![\w/])10\.\d{4,9}/[^\s<>\]\)\}\"']+", re.I)
PMID_URL = re.compile(r"https?://(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/", re.I)
DOI_URL = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s<>\]\)\}\"']+)", re.I)
STATUS = ("ABSTRACT_ONLY", "FULL_TEXT_REVIEWED", "REVIEWED", "CANDIDATE",
          "LICENSE_REVIEWED", "REPRODUCED", "RELEASED", "PENDING",
          "ANNOTATION_VERIFIED", "DESCRIPTIVE_EFFECTS_ONLY")

def markdown_files(root):
    for folder in ("01_Capstone", "02_Lecture_Notes", "03_Group_Work",
                   "04_Final_Project", "05_Assignments", "06_RESOURCES"):
        path = root / folder
        if path.is_dir():
            yield from sorted(path.rglob("*.md"))
    for name in ("README.md", "FOLLOW_ALONG.md"):
        if (root / name).exists():
            yield root / name

def audit(root):
    records = []
    findings = []
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        txt = path.read_text(encoding="utf-8")
        dois = sorted(set(m.rstrip(".,;:`") for m in DOI.findall(txt)))
        pmids = sorted(set(PMID_URL.findall(txt)))
        linked_dois = sorted(set(m.rstrip(".,;:`") for m in DOI_URL.findall(txt)))
        publisher_dois = set(re.findall(r"https?://[^\\s)\\]]+/doi/(10\\.\\d{4,9}/[^\\s)\\]]+)", txt, re.I))
        statuses = [s for s in STATUS if s in txt]
        records.append({"path": rel, "doi_count": len(dois), "pmid_count": len(pmids),
                        "dois": dois, "pmids": pmids,
                        "review_labels": statuses, "linked_dois": linked_dois})
        for doi in dois:
            if doi not in linked_dois and doi not in publisher_dois:
                findings.append({"path": rel, "severity": "review",
                                 "rule": "DOI_NOT_LINKED",
                                 "detail": doi + " has no matching doi.org link in this file"})
        if rel.startswith("06_RESOURCES/Genomics/GENE_CARDS/") and path.name != "README.md":
            if not dois or not pmids:
                findings.append({"path": rel, "severity": "error",
                                 "rule": "GENE_CARD_REFERENCE_MISSING",
                                 "detail": "Expected at least one DOI and PubMed URL"})
            if "ABSTRACT_ONLY" not in statuses and "FULL_TEXT_REVIEWED" not in statuses:
                findings.append({"path": rel, "severity": "error",
                                 "rule": "GENE_CARD_REVIEW_STATE_MISSING",
                                 "detail": "No explicit literature review extent"})
    return {"schema": "scholarly-audit-v1",
            "scope": "Offline structural reference inventory only",
            "limitations": ["DOI/PMID existence not checked online",
                            "publication metadata not compared to registries",
                            "claims not checked against methods or full text",
                            "source rights and numerical reproduction not evaluated"],
            "documents": records, "findings": findings,
            "counts": {"documents": len(records),
                       "documents_with_doi": sum(bool(r["dois"]) for r in records),
                       "unique_dois": len(set(d for r in records for d in r["dois"])),
                       "errors": sum(f["severity"] == "error" for f in findings),
                       "review": sum(f["severity"] == "review" for f in findings)}}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="-", help="JSON output path; default stdout")
    parser.add_argument("--strict", action="store_true",
                        help="Fail for missing gene-card references or review states")
    args = parser.parse_args()
    result = audit(ROOT)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output == "-":
        print(payload, end="")
    else:
        dest = Path(args.output)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(payload, encoding="utf-8")
    for finding in result["findings"]:
        print("{}: {}: {}: {}".format(finding["severity"].upper(), finding["path"], finding["rule"], finding["detail"]), file=sys.stderr)
    print("Scholarly inventory: {documents} documents, {unique_dois} unique DOI strings; "
          "{errors} structural errors; {review} manual review flags".format(**result["counts"]),
          file=sys.stderr)
    return 1 if args.strict and result["counts"]["errors"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
