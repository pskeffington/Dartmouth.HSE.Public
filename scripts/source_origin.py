#!/usr/bin/env python3
"""Content-origin decisions for a local guard; no legal-clearance inference.

Review evidence is local, bound to public candidate bytes and path, and cannot
cancel exact or substantive overlap with any configured rights holder's corpus.
"""
import hashlib
import json
import re
from pathlib import Path

INDEPENDENT = 'INDEPENDENT_ORIGINAL'
ORIGINAL_WORK = 'ORIGINAL_WORK'
PROTECTED = 'PROTECTED_SOURCE'
REVIEW = 'REVIEW_REQUIRED'
MEDIA = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.zip', '.ppt', '.pptx',
         '.key', '.pages', '.doc', '.docx', '.xlsx', '.xls', '.rds', '.rdata', '.xpt'}
STOP = set('a an the and or to of in on for from with by is are was were be been this that these those as at it its not can may must should will your you we our then than into using use'.split())
ORIGINAL_CATEGORIES = {
    'documentation': {'.md', '.rmd', '.txt', '.rst', '.tex'},
    'research-software': {'.py', '.r', '.sh', '.bash', '.js', '.ts', '.c', '.cpp', '.h', '.jl', '.json', '.yml', '.yaml'},
    'synthetic-example': {'.md', '.rmd', '.py', '.r', '.sh', '.csv', '.tsv', '.json'},
}
INPUT_USES = {'own-work': 'independently-written',
              'public-concept-reference': 'concepts-only',
              'synthetic-generation': 'simulated-data'}
# Content indicators are independent of names, academic subject, and folder.
# A routine authoring record cannot adjudicate explicit restrictions or licensing.
UNCERTAIN_RIGHTS = re.compile(
    r'all\s+rights\s+reserved|not\s+for\s+(?:public\s+)?distribution|'
    r'for\s+(?:enrolled\s+)?students\s+only|'
    r'\b(?:license|permission|rights)\s*[:=]\s*(?:unknown|pending|restricted|unverified)|'
    r'canvas\.dartmouth\.edu/courses/|blackboard\.dartmouth\.edu/', re.I)


def authoring_evidence_valid(evidence, category):
    """Structured authoring inputs, not an original=true or ALLOW declaration."""
    if not isinstance(evidence, dict) or set(evidence) != {'method', 'inputs'}:
        return False
    method = evidence['method']
    inputs = evidence['inputs']
    if not isinstance(method, str) or len(method.strip()) < 40 or not isinstance(inputs, list) or not inputs:
        return False
    for item in inputs:
        if not isinstance(item, dict) or set(item) != {'kind', 'reference', 'use'}:
            return False
        if not isinstance(item['kind'], str) or item['kind'] not in INPUT_USES or item['use'] != INPUT_USES[item['kind']]:
            return False
        if not isinstance(item['reference'], str) or not item['reference'].strip():
            return False
        if item['kind'] == 'public-concept-reference' and not re.match(r'https?://[^/\s]+', item['reference']):
            return False
    return category != 'synthetic-example' or any(i['kind'] == 'synthetic-generation' for i in inputs)


def verified_original_work(data, path, manifest):
    if not isinstance(manifest, dict) or manifest.get('schema') != 'original-work-v1':
        return None
    records = manifest.get('entries')
    if not isinstance(records, dict):
        return None
    entries = records.get(path, [])
    if not isinstance(entries, list):
        return None
    for entry in entries:
        if (not isinstance(entry, dict) or set(entry) != {'path', 'sha256', 'source_category', 'author',
                'recorded_on', 'authoring_evidence', 'evidence_sha256'}
                or entry.get('path') != path or entry.get('sha256') != hashlib.sha256(data).hexdigest()):
            continue
        category = entry.get('source_category')
        if not isinstance(category, str) or category not in ORIGINAL_CATEGORIES or Path(path).suffix.lower() not in ORIGINAL_CATEGORIES[category]:
            continue
        if (not isinstance(entry.get('author'), str) or not entry['author'].strip()
                or not isinstance(entry.get('recorded_on'), str) or not entry['recorded_on'].strip()):
            continue
        evidence = entry.get('authoring_evidence')
        if not authoring_evidence_valid(evidence, category):
            continue
        expected = hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()
        if entry.get('evidence_sha256') == expected:
            return entry
    return None


def original_work_conflict(entry, corpus):
    if UNCERTAIN_RIGHTS.search(json.dumps(entry['authoring_evidence'])):
        return 'contradictory or uncertain authoring inputs'
    for item in entry['authoring_evidence']['inputs']:
        reference = Path(item['reference'])
        if (reference.is_absolute() or '..' in reference.parts) and any(
                reference.resolve().is_relative_to(Path(d).resolve()) for d in corpus.get('source_dirs', [])):
            return 'protected authoring input cannot use original-work pathway'
    return None


def tokens(text):
    return re.findall(r'[a-z0-9_]+', text.lower())


def window_fingerprints(text, windows):
    return {hashlib.sha256(' '.join(window).encode()).hexdigest() for window in windows(text)}


def segments(text):
    # Short paragraphs and bounded overlapping spans avoid an entire-document
    # denominator hiding a protected passage embedded in a longer original file.
    words = tokens(text)
    return [set(hashlib.sha256(w.encode()).hexdigest() for w in words[i:i+80] if w not in STOP)
            for i in range(0, max(1, len(words)-39), 40)
            if len(words[i:i+80]) >= 40]


def similar(text, corpus):
    for candidate in segments(text):
        if len(candidate) < 20:
            continue
        for source in corpus['segments']:
            overlap = len(candidate & source)
            if overlap >= 20 and overlap / min(len(candidate), len(source)) >= .70:
                return True
    return False


def verified_review(data, path, reviews):
    r = reviews.get(path)
    if isinstance(r, list):
        for entry in r:
            result = verified_review(data, path, {path: entry})
            if result:
                return result
        return None
    if not isinstance(r, dict) or r.get('sha256') != hashlib.sha256(data).hexdigest():
        return None
    if r.get('decision') != 'ALLOW' or r.get('origin') not in {'independent', 'licensed'}:
        return None
    if not all(isinstance(r.get(k), str) and r[k].strip()
               for k in ('reviewer', 'reviewed_on', 'evidence', 'input_scope')):
        return None
    if r['origin'] == 'licensed' and not all(isinstance(r.get(k), str) and r[k].strip()
                                           for k in ('license', 'license_reference', 'permission_scope')):
        return None
    # Mixed/uncertain files require an actual rights-holder or human adjudication.
    if r.get('rights_review') and r.get('reviewer_kind') != 'human':
        return None
    return r


def classify(data, path, corpus, windows, text, reviews, original_work=None):
    if hashlib.sha256(data).hexdigest() in corpus['hashes']:
        return PROTECTED, 'identical protected source bytes'
    if window_fingerprints(text, windows) & corpus['windows']:
        return PROTECTED, 'shared protected-source token sequence'
    if len(data) > 2_000_000:
        return REVIEW, 'candidate exceeds normalized comparison limit'
    r = verified_review(data, path, reviews)
    if similar(text, corpus):
        # Neither "original=true" nor a declared independent origin adjudicates
        # overlap. A separate human rights review can document a false positive
        # or permitted licensed reuse; it still cannot override exact/window hits.
        if not (r and r.get('rights_review') and r.get('reviewer_kind') == 'human'):
            return REVIEW, 'substantive similarity requires human adjudication'
    original = verified_original_work(data, path, original_work)
    if original:
        # A prior positive record cannot hide contradictory evidence for the
        # same candidate bytes in a subsequent authoring record.
        for entry in original_work['entries'][path]:
            if isinstance(entry, dict) and entry.get('sha256') == hashlib.sha256(data).hexdigest():
                single = {'schema': 'original-work-v1', 'entries': {path: [entry]}}
                if not verified_original_work(data, path, single):
                    return REVIEW, 'incomplete or contradictory original-work records'
                reason = original_work_conflict(entry, corpus)
                if reason:
                    return REVIEW, reason
        existing = reviews.get(path, [])
        if isinstance(existing, dict):
            existing = [existing]
        for record in existing:
            if isinstance(record, dict) and record.get('sha256') == hashlib.sha256(data).hexdigest():
                if record.get('decision') != 'ALLOW':
                    return REVIEW, 'contradictory existing rights decision'
                if record.get('origin') != 'independent':
                    # Reuse needs the licensed workflow, not an original-work label.
                    original = None
        if original is None and not r:
            return REVIEW, 'non-independent origin requires verified license or rights evidence'
    if original:
        # Risk assessment still applies to every revision and historical blob.
        if UNCERTAIN_RIGHTS.search(text):
            return REVIEW, 'content restrictions or uncertain license require rights review'
        try:
            data.decode('utf-8')
        except UnicodeDecodeError:
            return REVIEW, 'original-work pathway requires verifiable UTF-8 text'
        if Path(path).suffix.lower() in MEDIA or b'\0' in data:
            return REVIEW, 'binary rights require documented human review'
        return ORIGINAL_WORK, 'content-bound automated authoring manifest; protected comparisons passed'
    if not r:
        reason = 'unknown or stale provenance'
        if Path(path).name.casefold() in corpus['names']:
            reason = 'source-name indicator; origin review required'
        elif Path(path).suffix.lower() in MEDIA or b'\0' in data[:8192]:
            reason = 'unverified third-party or binary rights'
        return REVIEW, reason
    if (Path(path).suffix.lower() in MEDIA or b'\0' in data[:8192]) and not (
            r.get('rights_review') and r.get('reviewer_kind') == 'human'):
        return REVIEW, 'binary rights require documented human review'
    return INDEPENDENT, 'content-bound independent or licensed origin review'
