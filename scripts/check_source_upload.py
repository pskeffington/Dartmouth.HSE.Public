#!/usr/bin/env python3
"""Fail closed before Git push when proposed content overlaps local sources.

This is a local guard, not a server rule or copyright certification. Corpus
configuration and source fingerprints remain in the untracked Git directory.
"""
from collections import defaultdict
import importlib.util
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

SPEC = importlib.util.spec_from_file_location('private_compare', Path(__file__).with_name('compare_private_sources.py'))
comparison = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparison)
ZERO = '0' * 40


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root)


def load_corpus(root, directories):
    hashes = set()
    names = set()
    index = set()
    for directory in directories:
        directory = Path(directory).resolve()
        if not directory.is_dir() or directory.is_relative_to(root):
            raise ValueError('Every protected source folder must be available outside the public repo')
        files = [p for p in directory.rglob('*') if p.is_file()]
        if not files:
            raise ValueError('A protected source folder is empty')
        for path in files:
            if path.resolve().is_relative_to(root):
                raise ValueError('Protected source symlink resolves into the public repo')
            names.add(path.name.casefold())
            hashes.add(comparison.digest(path))
            if path.suffix.lower() in comparison.TEXT_EXT | {'.pdf'} and path.stat().st_size <= 2_000_000:
                index.update(comparison.windows(comparison.extract(path)))
    return hashes, names, index


def check_push(root, directories, updates, remote_name):
    root = root.resolve()
    hashes, names, index = load_corpus(root, directories)
    findings = []
    blobs = defaultdict(set)
    commits = set()
    for line in updates:
        fields = line.split()
        if len(fields) != 4:
            raise ValueError('Malformed Git pre-push update')
        _, local_sha, _, remote_sha = fields
        if local_sha == ZERO:  # deletion sends no new file content
            continue
        target = git(root, 'rev-parse', f'{local_sha}^{{commit}}').decode().strip()
        # Always inspect the proposed final tree, even if the working tree is clean.
        commits.add(target)
        if remote_sha != ZERO:
            base = git(root, 'rev-parse', f'{remote_sha}^{{commit}}').decode().strip()
            args = [target, '^' + base]
        else:
            # Existing remote ancestry is already uploaded; inspect all newly
            # introduced commits plus the final tree. An unknown remote forces
            # a full history inspection rather than trusting unrelated refs.
            known = git(root, 'for-each-ref', '--format=%(objectname)', f'refs/remotes/{remote_name}/').decode().splitlines()
            args = [target, *('^' + sha for sha in known)]
        commits.update(git(root, 'rev-list', *args).decode().splitlines())
    for commit in commits:
        for record in git(root, 'ls-tree', '-rz', commit).split(b'\0'):
            if not record:
                continue
            header, raw_path = record.split(b'\t', 1)
            mode, kind, sha = header.decode().split()
            path = raw_path.decode('utf-8', 'surrogateescape')
            if kind != 'blob' or mode == '120000':
                findings.append({'path': path, 'reason': 'unreviewed submodule or symlink'})
                continue
            blobs[sha].add(path)
    for sha, paths in blobs.items():
        data = git(root, 'cat-file', 'blob', sha)
        if hashlib.sha256(data).hexdigest() in hashes:
            findings.extend({'path': p, 'reason': 'identical protected source bytes'} for p in sorted(paths))
        for p in sorted(paths):
            if Path(p).name.casefold() in names:
                findings.append({'path': p, 'reason': 'protected source filename'})
        if len(data) <= 2_000_000:
            if data.startswith(b'%PDF-'):
                with tempfile.TemporaryDirectory() as folder:
                    pdf = Path(folder) / 'candidate.pdf'
                    pdf.write_bytes(data)
                    text = comparison.extract(pdf)
            elif b'\0' not in data[:8192]:
                text = data.decode('utf-8', 'replace')
            else:
                continue
            if comparison.windows(text) & index:
                findings.extend({'path': p, 'reason': 'shared protected-source token sequence'} for p in sorted(paths))
    return sorted({(f['path'], f['reason']) for f in findings})


def main():
    try:
        root = Path(git(Path.cwd(), 'rev-parse', '--show-toplevel').decode().strip()).resolve()
        git_dir = Path(git(root, 'rev-parse', '--absolute-git-dir').decode().strip())
        config = json.loads((git_dir / 'private-source-guard.json').read_text())
        result = check_push(root, config['source_dirs'], sys.stdin.read().splitlines(), sys.argv[1])
    except Exception:
        print('UPLOAD BLOCKED: private-source checks unavailable or invalid. Restore the local corpus/configuration; no source details emitted.', file=sys.stderr)
        return 2
    if result:
        print(f'UPLOAD BLOCKED: {len(result)} protected-source indicators in proposed commits.', file=sys.stderr)
        for path, reason in result[:25]:
            print(f'  {path}: {reason}', file=sys.stderr)
        return 1
    print('Private-source upload guard: proposed commits pass bounded checks.', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
