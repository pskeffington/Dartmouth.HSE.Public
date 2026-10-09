#!/usr/bin/env python3
"""Compare local restricted sources without copying source text into reports.

Inputs and reports must remain outside the repository. This detects identical
bytes and long normalized token sequences, not plagiarism or legal clearance.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

TEXT_EXT = {'.rmd', '.r', '.md', '.txt', '.tex', '.html', '.py', '.sh', '.bib', '.css', '.yml', '.yaml', '.json'}
WINDOW = 20


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def extract(path):
    if path.suffix.lower() == '.pdf':
        if not shutil.which('pdftotext'):
            raise RuntimeError('pdftotext is required to compare PDF content')
        return subprocess.run(['pdftotext', str(path), '-'], check=True,
                              capture_output=True).stdout.decode('utf-8', 'replace')
    return path.read_text(encoding='utf-8', errors='replace')


def windows(text):
    tokens = re.findall(r'[a-z0-9_]+', text.lower())
    return {tuple(tokens[i:i + WINDOW]) for i in range(len(tokens) - WINDOW + 1)}


def compare(root, source_dirs, history=False):
    root = root.resolve()
    if any(directory.resolve().is_relative_to(root) for directory in source_dirs):
        raise ValueError("Restricted source directories must be outside the public repository")
    sources = sorted({p.resolve() for directory in source_dirs
                      for p in directory.rglob('*') if p.is_file()})
    if not sources:
        raise ValueError('No local comparison sources were found')
    if any(p.is_relative_to(root) for p in sources):
        raise ValueError('Restricted sources must be outside the public repository')
    hashes = defaultdict(list)
    index = defaultdict(set)
    text_sources = 0
    skipped_text = []
    for n, path in enumerate(sources, 1):
        label = f'S{n:03d}'
        hashes[digest(path)].append(label)
        # Large datasets get byte comparison only, not token normalization.
        if path.suffix.lower() in TEXT_EXT | {'.pdf'} and path.stat().st_size <= 2_000_000:
            for window in windows(extract(path)):
                index[window].add(label)
            text_sources += 1
        else:
            skipped_text.append(label)
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).split(b'\0')
    findings = []
    for raw in tracked:
        if not raw:
            continue
        rel = raw.decode('utf-8', 'surrogateescape')
        path = root / rel
        if not path.is_file():
            findings.append({'public_path': rel, 'kind': 'missing_tracked_path'})
            continue
        exact = hashes.get(digest(path), [])
        if exact:
            findings.append({'public_path': rel, 'kind': 'identical_bytes', 'source_ids': exact})
        if path.suffix.lower() in TEXT_EXT | {'.pdf'} and path.stat().st_size <= 2_000_000:
            matches = defaultdict(int)
            for window in windows(extract(path)):
                for label in index.get(window, ()):
                    matches[label] += 1
            if matches:
                findings.append({'public_path': rel, 'kind': 'shared_20_token_windows',
                                 'matches': dict(sorted(matches.items()))})
    historic = []
    history_text = []
    objects_scanned = 0
    if history:
        objects = subprocess.check_output(['git', 'rev-list', '--objects', '--all'], cwd=root).splitlines()
        ids = [line.split(b' ', 1)[0] for line in objects]
        types = subprocess.run(['git', 'cat-file', '--batch-check=%(objectname) %(objecttype)'],
                               cwd=root, input=b'\n'.join(ids) + b'\n', capture_output=True, check=True).stdout
        names = {line.split(b' ', 1)[0].decode(): line.split(b' ', 1)[1].decode('utf-8', 'replace')
                 for line in objects if b' ' in line}
        for line in types.splitlines():
            sha, kind = line.decode().split()
            if kind != 'blob':
                continue
            data = subprocess.check_output(['git', 'cat-file', 'blob', sha], cwd=root)
            objects_scanned += 1
            exact = hashes.get(hashlib.sha256(data).hexdigest(), [])
            if exact:
                historic.append({'blob': sha, 'representative_path': names.get(sha),
                                 'kind': 'identical_bytes', 'source_ids': exact})
            name = names.get(sha, '')
            if Path(name).suffix.lower() in TEXT_EXT and len(data) <= 2_000_000 and b'\0' not in data[:8192]:
                matches = defaultdict(int)
                for window in windows(data.decode('utf-8', 'replace')):
                    for label in index.get(window, ()):
                        matches[label] += 1
                if matches:
                    history_text.append({'blob': sha, 'representative_path': name,
                                         'kind': 'shared_20_token_windows',
                                         'matches': dict(sorted(matches.items()))})
    return {'schema': 'local-restricted-comparison-v1', 'source_files': len(sources),
            'text_sources': text_sources, 'byte_only_source_ids': skipped_text,
            'tracked_files': len([p for p in tracked if p]), 'token_window': WINDOW,
            'current_findings': findings, 'history_blobs_scanned': objects_scanned,
            'history_exact_matches': historic, 'history_text_matches': history_text,
            'limitations': 'No source text or filesystem paths emitted. Source IDs are local run identifiers. Token matches require adjudication; generic syntax may match. Paraphrases, partial datasets, transformed images, and PDF images may evade detection. History mode compares bytes and text blobs across locally reachable refs, not all GitHub caches or forks.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--private-source-dir', type=Path, action='append', required=True)
    parser.add_argument('--history', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if output.is_relative_to(root):
        parser.error('Comparison reports must be outside the public repository')
    if any(not p.is_dir() for p in args.private_source_dir):
        parser.error('Every private source directory must exist')
    try:
        report = compare(root, args.private_source_dir, args.history)
        output.write_text(json.dumps(report, indent=2) + '\n')
    except (ValueError, RuntimeError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Comparison failed: {exc}', file=sys.stderr)
        return 2
    print(f"Compared {report['tracked_files']} public files against {report['source_files']} local sources; "
          f"{len(report['current_findings'])} current findings; "
          f"{len(report['history_exact_matches'])} historical byte matches; "
          f"{len(report['history_text_matches'])} historical text matches.")
    return 1 if report['current_findings'] or report['history_exact_matches'] or report['history_text_matches'] else 0


if __name__ == '__main__':
    sys.exit(main())
