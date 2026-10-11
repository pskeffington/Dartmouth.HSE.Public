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
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOI = re.compile(r"(?<!\w)10\.[^\s<>\[\]\"']+", re.I)
DOI_VALID = re.compile(r"10\.\d{4,9}/\S+", re.I)
PMID_URL = re.compile(r"https?://(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/([1-9]\d*)(?=[/?#\s)\]]|$)", re.I)
PMID_LABEL = re.compile(r"\bPMID\s*:?\s*([1-9]\d*)\b", re.I)
URL = re.compile(r"https?://[^\s<>\[\]\"']+", re.I)
STAGES = ("IDENTIFIER_VERIFIED", "METADATA_VERIFIED", "CLAIM_SUPPORT_REVIEWED",
          "METHODS_REPRODUCED", "REVIEW_REQUIRED")
STATUS = ("ABSTRACT_ONLY", "FULL_TEXT_REVIEWED", "REVIEWED", "CANDIDATE",
          "LICENSE_REVIEWED", "REPRODUCED", "RELEASED", "PENDING",
          "ANNOTATION_VERIFIED", "DESCRIPTIVE_EFFECTS_ONLY")

def normalize_doi(value):
    """Keep balanced DOI parentheses; remove surrounding prose delimiters."""
    value = unquote(value).strip().rstrip(".,;:`}")
    while value.endswith(")") and value.count(")") > value.count("("):
        value = value[:-1]
    return value.casefold()

def identifiers(text):
    linked, malformed = set(), set()
    url_spans = []
    for match in URL.finditer(text):
        url_spans.append(match.span())
        raw = match.group()
        url = urlsplit(normalize_doi(raw))
        match = re.search(r"10\.\d{4,9}/.+", url.path)
        if match:
            value = normalize_doi(match.group())
            if url.hostname and url.hostname.endswith("frontiersin.org"):
                value = re.sub(r"/(full|abstract)$", "", value)
            if url.hostname in {"www.medrxiv.org", "www.biorxiv.org", "medrxiv.org", "biorxiv.org"}:
                value = re.sub(r"\.(full|abstract)$", "", value)
            linked.add(value)
    dois = set(linked)
    for match in DOI.finditer(text):
        if any(start <= match.start() < end for start, end in url_spans):
            continue
        raw = match.group()
        value = normalize_doi(raw.split("?", 1)[0].split("#", 1)[0])
        if "/" not in value and not re.fullmatch(r"10\.\d{4,9}", value):
            continue  # Date/filename fragments such as 2026-10-10.md are not citations.
        if DOI_VALID.fullmatch(value):
            dois.add(value)
        else:
            malformed.add(value)
    pmids = set(PMID_URL.findall(text)) | set(PMID_LABEL.findall(text))
    return sorted(dois), sorted(pmids), sorted(linked), sorted(malformed)

def reference_state(kind, value, evidence):
    """Registry identity and metadata never imply claim support or reproduction."""
    item = evidence.get(f"{kind}:{value}")
    state = {"kind": kind, "identifier": value, "identifier_status": "REVIEW_REQUIRED",
             "metadata_status": "REVIEW_REQUIRED", "claim_support_status": "REVIEW_REQUIRED",
             "methods_status": "REVIEW_REQUIRED", "publication_notices": "NOT_CHECKED"}
    if not isinstance(item, dict):
        return state
    authority = {"doi": {"Crossref", "DataCite", "PubMed"}, "pmid": {"PubMed"}}[kind]
    allowed_hosts = {"Crossref": "api.crossref.org", "DataCite": "api.datacite.org",
                     "PubMed": "eutils.ncbi.nlm.nih.gov"}
    provider = item.get("authority")
    source = urlsplit(item.get("source_url", ""))
    if (provider not in authority or source.scheme != "https"
            or source.hostname != allowed_hosts.get(provider) or not item.get("retrieved_utc")):
        state["evidence_problem"] = "Authoritative retrieval record missing or invalid"
        return state
    state.update({"authority": provider, "source_url": item["source_url"],
                  "retrieved_utc": item["retrieved_utc"], "lookup_status": item.get("lookup_status")})
    actual = item.get("identifier", "")
    actual = normalize_doi(actual) if kind == "doi" else str(actual)
    if item.get("lookup_status") != "FOUND" or actual != value:
        state["evidence_problem"] = "Unavailable or mismatched registry identifier"
        return state
    state["identifier_status"] = "IDENTIFIER_VERIFIED"
    if all(item.get(k) for k in ("title", "authors", "year", "venue")):
        state["metadata_status"] = "METADATA_VERIFIED"
        state["metadata"] = {k: item[k] for k in ("title", "authors", "year", "venue")}
    state["publication_notices"] = item.get("publication_notices", "NOT_CHECKED")
    # An empty registry notice list is a dated observation, not retraction clearance.
    return state

def markdown_files(root):
    for folder in ("01_Capstone", "02_Lecture_Notes", "03_Group_Work",
                   "04_Final_Project", "05_Assignments", "06_RESOURCES"):
        path = root / folder
        if path.is_dir():
            yield from sorted(path.rglob("*.md"))
    for name in ("README.md", "FOLLOW_ALONG.md"):
        if (root / name).exists():
            yield root / name

def audit(root, evidence=None):
    evidence = {} if evidence is None else evidence
    records = []
    findings = []
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        txt = path.read_text(encoding="utf-8")
        dois, pmids, linked_dois, malformed = identifiers(txt)
        statuses = [s for s in STATUS + STAGES if re.search(r"\b" + s + r"\b", txt)]
        records.append({"path": rel, "doi_count": len(dois), "pmid_count": len(pmids),
                        "dois": dois, "pmids": pmids,
                        "review_labels": statuses, "linked_dois": linked_dois,
                        "references": [reference_state(k, v, evidence)
                                       for k, values in (("doi", dois), ("pmid", pmids)) for v in values]})
        for value in malformed:
            findings.append({"path": rel, "severity": "review", "rule": "MALFORMED_DOI",
                             "detail": value})
        for doi in dois:
            if doi not in linked_dois:
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
    return {"schema": "scholarly-audit-v2",
            "scope": "Offline structural reference inventory only",
            "limitations": ["Offline extraction alone never verifies DOI/PMID existence",
                            "Optional registry evidence verifies record identity, not citation-to-claim matching",
                            "Publication notices are dated registry observations, not absence-of-retraction proof",
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
    parser.add_argument("--metadata-file", type=Path,
                        help="Optional local JSON mapping doi:/pmid: keys to dated authoritative registry records")
    parser.add_argument("--strict", action="store_true",
                        help="Fail for missing gene-card references or review states")
    args = parser.parse_args()
    evidence = json.loads(args.metadata_file.read_text(encoding="utf-8")) if args.metadata_file else {}
    if not isinstance(evidence, dict):
        parser.error("Metadata file must contain an object keyed by doi:/pmid: identifiers")
    result = audit(ROOT, evidence)
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
