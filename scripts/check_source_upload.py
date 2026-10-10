#!/usr/bin/env python3
"""Fail closed before Git push when proposed content overlaps local sources.

This is a local guard, not a server rule or copyright certification. Corpus
configuration and source fingerprints remain in the untracked Git directory.
"""
from collections import defaultdict
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

SPEC = importlib.util.spec_from_file_location('private_compare', Path(__file__).with_name('compare_private_sources.py'))
comparison = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparison)
ORIGIN_SPEC = importlib.util.spec_from_file_location('source_origin', Path(__file__).with_name('source_origin.py'))
origin = importlib.util.module_from_spec(ORIGIN_SPEC)
ORIGIN_SPEC.loader.exec_module(origin)
ZERO = '0' * 40


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root)


def load_corpus(root, directories):
    hashes = set()
    names = set()
    index = set()
    spans = []
    if not directories:
        raise ValueError("A protected-source inventory is required")
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
                text = comparison.extract(path)
                index.update(origin.window_fingerprints(text, comparison.windows))
                spans.extend(origin.segments(text))
    return {"hashes": hashes, "names": names, "windows": index, "segments": spans}


def check_push(root, directories, updates, remote_name, reviews=None):
    root = root.resolve()
    if reviews is None:
        git_dir = Path(git(root, 'rev-parse', '--absolute-git-dir').decode().strip())
        review_file = git_dir / 'source-rights-reviews.json'
        if review_file.is_symlink():
            raise ValueError('Unsafe local review register')
        reviews = json.loads(review_file.read_text()).get('entries', {}) if review_file.exists() else {}
    if not isinstance(reviews, dict):
        raise ValueError('Invalid local review register')
    cached_only = False
    try:
        corpus = load_corpus(root, directories)
    except ValueError:
        if not directories or not any(not Path(p).is_dir() for p in directories):
            raise
        if any(Path(p).resolve().is_relative_to(root) for p in directories):
            raise
        # The live source comparison exemption requires a separate human origin
        # review AND the previously installed private signature inventory. A
        # missing inventory is never evidence of independence.
        git_dir = Path(git(root, 'rev-parse', '--absolute-git-dir').decode().strip())
        inventory_file = git_dir / 'source-protection-inventory.json'
        if inventory_file.is_symlink():
            raise ValueError('Unsafe private signature inventory')
        saved = json.loads(inventory_file.read_text())
        if (saved.get('schema') != 'protected-signatures-v1' or not saved.get('hashes')
                or saved.get('source_dirs') != [str(Path(p).resolve()) for p in directories]):
            raise ValueError('No validated protected signature inventory')
        corpus = {k: set(saved[k]) for k in ('hashes', 'names', 'windows')}
        corpus['segments'] = [set(span) for span in saved['segments']]
        cached_only = True
    # Already-uploaded byte-identical paths may retain unresolved reviews. This
    # does not clear them, and cannot exempt substantive protected-source hits.
    known = git(root, 'for-each-ref', '--format=%(objectname)', f'refs/remotes/{remote_name}/').decode().splitlines()
    inherited = set()
    for sha in set(known):
        for record in git(root, 'ls-tree', '-rz', sha).split(b'\0'):
            if record:
                header, name = record.split(b'\t', 1)
                mode, kind, oid = header.decode().split()
                if mode in {'100644', '100755'} and kind == 'blob':
                    inherited.add((oid, name.decode('utf-8', 'surrogateescape')))
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
        # Inspect only history newly introduced to this remote, not ancestors
        # already uploaded on another branch. The final tree is always checked
        # above, so protected bytes cannot inherit a baseline exemption.
        args = [target, *('^' + sha for sha in known)]
        if remote_sha != ZERO:
            base = git(root, 'rev-parse', f'{remote_sha}^{{commit}}').decode().strip()
            args.append('^' + base)
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
        text = ''
        if len(data) <= 2_000_000:
            if data.startswith(b'%PDF-'):
                with tempfile.TemporaryDirectory() as folder:
                    pdf = Path(folder) / 'candidate.pdf'
                    pdf.write_bytes(data)
                    text = comparison.extract(pdf)
            elif b'\0' not in data[:8192]:
                text = data.decode('utf-8', 'replace')
        for path in sorted(paths):
            classification, reason = origin.classify(data, path, corpus, comparison.windows, text, reviews)
            if cached_only and (sha, path) not in inherited and classification != origin.PROTECTED:
                r = origin.verified_review(data, path, reviews)
                if not (r and r['origin'] == 'independent' and r.get('reviewer_kind') == 'human'
                        and r.get('corpus_independent_review') is True):
                    classification, reason = origin.REVIEW, 'live source comparison required for this origin'
            if classification == origin.PROTECTED or (classification == origin.REVIEW and
                                                       (sha, path) not in inherited):
                findings.append({'path': path, 'reason': classification + ': ' + reason})
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
    print('Private-source upload guard: proposed commits pass content-origin checks; inherited reviews remain unresolved.', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
