#!/usr/bin/env python3
"""Batch-record original-work evidence locally, with live protected comparisons.

This records authoring inputs, not legal clearance or a human rights approval.
The installed pre-push guard independently checks committed bytes and history.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

import check_source_upload as guard


def record(root, paths, category, evidence):
    root = root.resolve()
    if not guard.origin.authoring_evidence_valid(evidence, category):
        raise ValueError('Document the authoring method and supported inputs; declarations alone are insufficient')
    git_dir = Path(guard.git(root, 'rev-parse', '--absolute-git-dir').decode().strip())
    target = git_dir / 'original-work-manifest.json'
    if target.is_symlink():
        raise ValueError('Unsafe original-work manifest')
    payload = json.loads(target.read_text()) if target.exists() else {'schema': 'original-work-v1', 'entries': {}}
    if payload.get('schema') != 'original-work-v1' or not isinstance(payload.get('entries'), dict):
        raise ValueError('Invalid existing original-work manifest; preserve it for diagnosis')
    config = json.loads((git_dir / 'private-source-guard.json').read_text())
    # Recording needs the live inventory; no absence-of-source inference.
    corpus = guard.load_corpus(root, config['source_dirs'])
    review_file = git_dir / 'source-rights-reviews.json'
    if review_file.is_symlink():
        raise ValueError('Unsafe rights review register')
    reviews = json.loads(review_file.read_text()).get('entries', {}) if review_file.exists() else {}
    author = guard.git(root, 'config', 'user.name').decode().strip()
    if not author:
        raise ValueError('Configure a contributor identity before recording authoring evidence')
    recorded = []
    for path in paths:
        relative = Path(path)
        candidate = root / relative
        if (relative.is_absolute() or '..' in relative.parts or '.git' in relative.parts
                or candidate.is_symlink() or not candidate.resolve().is_relative_to(root)
                or not candidate.is_file()):
            raise ValueError('Only regular public files inside this checkout can be recorded')
        name = relative.as_posix()
        data = candidate.read_bytes()
        if len(data) > 2_000_000 or b'\0' in data:
            raise ValueError('Binary or oversized material requires the rights-review workflow')
        text = data.decode('utf-8')
        entry = {'path': name, 'sha256': hashlib.sha256(data).hexdigest(),
                 'source_category': category, 'author': author,
                 'recorded_on': datetime.now(timezone.utc).isoformat(),
                 'authoring_evidence': evidence,
                 'evidence_sha256': hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()}
        if not guard.origin.verified_original_work(data, name, {'schema': 'original-work-v1', 'entries': {name: [entry]}}):
            raise ValueError('Category or candidate evidence does not qualify for original work')
        versions = payload['entries'].setdefault(name, [])
        if not isinstance(versions, list):
            raise ValueError('Invalid existing entry; preserve it for diagnosis')
        versions.append(entry)
        decision, reason = guard.origin.classify(data, name, corpus, guard.comparison.windows, text, reviews, payload)
        if decision != guard.origin.ORIGINAL_WORK:
            raise ValueError(f'{name}: {decision}: {reason}; no manifest changes saved')
        recorded.append(name)
    # Preserve previous byte-bound evidence for newly introduced intermediate commits.
    target.write_text(json.dumps(payload, indent=2) + '\n')
    target.chmod(0o600)
    return recorded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--category', choices=sorted(guard.origin.ORIGINAL_CATEGORIES), required=True)
    parser.add_argument('--evidence', type=Path, required=True, help='Local JSON containing method and inputs; keep outside public Git')
    parser.add_argument('paths', nargs='+', help='Public paths relative to this checkout; one invocation can record multiple files')
    args = parser.parse_args()
    try:
        root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
        names = record(root, args.paths, args.category, json.loads(args.evidence.read_text()))
    except (OSError, ValueError, UnicodeError, KeyError, subprocess.CalledProcessError):
        parser.exit(1, 'Original-work recording stopped: invalid evidence, uncertain origin, or unavailable protected inputs. No new manifest saved.\n')
    print(f'ORIGINAL_WORK: recorded {len(names)} content-bound entries locally; normal checks and guarded push remain required.')


if __name__ == '__main__':
    main()
