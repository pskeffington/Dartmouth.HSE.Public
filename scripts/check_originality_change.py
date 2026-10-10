#!/usr/bin/env python3
"""Check an ordinary change while retaining unchanged baseline REVIEW findings.

The full strict scanner remains separate and authoritative for whole-repository
clearance. This gate never declares existing reviews cleared, tolerates BLOCK,
or accepts a changed file with a retained review. No private inputs enter CI.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import tarfile
import tempfile
from pathlib import Path

import check_public_originality as screen


def decision(before: dict, after: dict, unchanged: set[str]) -> dict:
    for report in (before, after):
        if report.get('status') not in {'BLOCK', 'REVIEW', 'SCREEN_CLEAR'}:
            raise ValueError('Invalid or unavailable originality report')
        if not isinstance(report.get('findings'), list):
            raise ValueError('Missing finding list')
    baseline = {(f['path'], f['level'], f['reason']) for f in before['findings']}
    retained, unresolved = [], []
    for finding in after['findings']:
        signature = (finding['path'], finding['level'], finding['reason'])
        if finding['level'] == 'review' and signature in baseline and finding['path'] in unchanged:
            retained.append(finding)
        else:
            unresolved.append(finding)
    return {'change_status': 'FAIL' if unresolved else 'PASS',
            'full_repository_status': after['status'],
            'retained_unresolved_reviews': retained,
            'new_or_changed_findings': unresolved,
            'limitation': 'Unchanged reviews remain unresolved. This is not copyright clearance.'}


def inspect(root: Path, base: str) -> dict:
    resolved = subprocess.check_output(['git', 'rev-parse', '--verify', base + '^{commit}'], cwd=root, text=True).strip()
    raw = subprocess.check_output(['git', 'ls-tree', '-r', '-z', resolved], cwd=root)
    tree = {}
    for entry in raw.split(b'\0'):
        if not entry:
            continue
        metadata, name = entry.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        if mode not in {'100644', '100755'} or kind != 'blob':
            raise ValueError('Unsupported baseline tree entry; manual review needed')
        tree[name.decode()] = oid
    if not tree:
        raise ValueError('Empty baseline cannot establish prior reviews')
    # Materialize only the public baseline. A temporary index lets the unchanged
    # scanner inspect exactly its tracked paths, with no private corpus in CI.
    with tempfile.TemporaryDirectory(prefix='pauls-originality-baseline-') as temp:
        dest = Path(temp)
        archive = dest / 'baseline.tar'
        subprocess.run(['git', 'archive', '--format=tar', '-o', str(archive), resolved], cwd=root, check=True)
        baseline_root = dest / 'tree'
        baseline_root.mkdir()
        with tarfile.open(archive) as stream:
            stream.extractall(baseline_root, filter='data')
        subprocess.run(['git', 'init', '-q', str(baseline_root)], check=True)
        subprocess.run(['git', 'add', '-f', '--all'], cwd=baseline_root, check=True)
        before = screen.scan(baseline_root)
    after = screen.scan(root)
    unchanged = set()
    for path, oid in tree.items():
        candidate = root / path
        if candidate.is_file() and not candidate.is_symlink():
            current_oid = subprocess.check_output(['git', 'hash-object', '--', path], cwd=root, text=True).strip()
            if current_oid == oid:
                unchanged.add(path)
    result = decision(before, after, unchanged)
    result['baseline_commit'] = resolved
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, help='Trusted public base commit for this change')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        result = inspect(args.root.resolve(), args.base)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, tarfile.TarError) as exc:
        parser.exit(2, f'Change comparison unavailable: {exc}\n')
    rendered = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end='')
    return 1 if result['change_status'] != 'PASS' else 0


if __name__ == '__main__':
    raise SystemExit(main())
