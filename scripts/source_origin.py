#!/usr/bin/env python3
"""Content-origin decisions for a local guard; no legal-clearance inference.

Review evidence is local, bound to public candidate bytes and path, and cannot
cancel exact or substantive overlap with any configured rights holder's corpus.
"""
import hashlib
import re
from pathlib import Path

INDEPENDENT = 'INDEPENDENT_ORIGINAL'
PROTECTED = 'PROTECTED_SOURCE'
REVIEW = 'REVIEW_REQUIRED'
MEDIA = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.zip', '.ppt', '.pptx',
         '.key', '.pages', '.doc', '.docx', '.xlsx', '.xls', '.rds', '.rdata', '.xpt'}
STOP = set('a an the and or to of in on for from with by is are was were be been this that these those as at it its not can may must should will your you we our then than into using use'.split())


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


def classify(data, path, corpus, windows, text, reviews):
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
