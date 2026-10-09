#!/usr/bin/env python3
"""Check repository Markdown links, fragments and navigation using local files."""

import collections
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]


def prose(path):
    output = []
    fence = None
    for line in path.read_text().splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            if fence is None:
                fence = match[1]
            elif match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
        elif fence is None:
            output.append(line)
    if fence is not None:
        raise ValueError(f'{path.relative_to(ROOT)}: unclosed code fence')
    return '\n'.join(output)


def fragments(path):
    ids = set()
    counts = collections.Counter()
    for line in prose(path).splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match[1])
        label = re.sub(r'<[^>]+>', '', label)
        slug = re.sub(r'[^\w\- ]', '', label.lower()).replace(' ', '-')
        count = counts[slug]
        counts[slug] += 1
        ids.add(slug + (f'-{count}' if count else ''))
    return ids


def main():
    errors = []
    checked = 0
    externals = set()
    documents = sorted(ROOT.rglob('*.md')) + sorted(ROOT.rglob('*.Rmd'))
    for source in documents:
        for target in re.findall(r'\]\(([^)]+)\)', prose(source)):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                if url.scheme in ('http', 'https'):
                    externals.add(target)
                continue
            checked += 1
            destination = (source.parent / unquote(url.path)).resolve() if url.path else source
            if not destination.is_relative_to(ROOT):
                errors.append(f'{source.relative_to(ROOT)}: target outside repository: {target}')
                continue
            if destination.is_dir():
                destination = destination / 'README.md'
            if not destination.is_file():
                errors.append(f'{source.relative_to(ROOT)}: missing target: {target}')
            elif url.fragment and destination.suffix in ('.md', '.Rmd'):
                if unquote(url.fragment) not in fragments(destination):
                    errors.append(f'{source.relative_to(ROOT)}: missing fragment: {target}')
        if source.suffix == '.Rmd':
            match = re.search(r'^\s+css:\s*(.+)$', source.read_text().split('---', 2)[1], re.M)
            if match and not (source.parent / match[1].strip()).is_file():
                errors.append(f'{source.relative_to(ROOT)}: missing HTML stylesheet')
    print(f'Checked {checked} local links across {len(documents)} documents.')
    print(f'Found {len(externals)} distinct external Markdown destinations; network access is not checked here.')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: local paths, directory landing pages, fragments and HTML stylesheet paths.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
