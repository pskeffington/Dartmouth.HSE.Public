#!/usr/bin/env python3
"""Build public reading companions without executing their source code."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def anchor(title):
    return re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')


def contents(text):
    headings = []
    in_code = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_code = not in_code
        elif not in_code and line.startswith('## '):
            title = line[3:]
            headings.append(f'- [{title}](#{anchor(title)})')
    if not headings:
        return text
    first = text.index('\n## ')
    return text[:first] + '\n## On this page\n\n' + '\n'.join(headings) + '\n' + text[first:]


def rmarkdown(source):
    _, metadata, body = source.read_text().split('---', 2)
    title = re.search(r'^title:\s*"(.*)"$', metadata, re.M).group(1)
    body = re.sub(r'^```\{(r|bash|sh)[^}]*\}', r'```\1', body, flags=re.M)
    body = re.sub(r'^```\{[^}]*\}', '```text', body, flags=re.M)
    body = re.sub(r'`r [^`]+`', '[computed when rendered]', body)
    header = (
        f'# {title}\n\n'
        f'[Section index](README.md) · [Editable R Markdown]({source.name}) · '
        '[Repository home](../README.md)\n\n'
        '> **Reading edition.** Code is displayed for study and has not been executed '
        'to generate this page. Run the source chunks in order to produce and check '
        'outputs; data-dependent examples need separately supplied course files.\n\n'
    )
    return contents(header + body.lstrip())


def commented_lecture(source):
    lines = [re.sub(r'^# ?', '', line) for line in source.read_text().splitlines()]
    week = source.name.split('_')[1]
    first_heading = next(i for i, line in enumerate(lines) if re.match(r'CHUNK |===== Lecture', line))
    # Fold line-wrapped introductory comments into a readable paragraph.
    intro = ' '.join(line for line in lines[:first_heading] if line)
    out = [
        f'# HSE 711 · Week {week} learning notes', '',
        f'[Lecture index](README.md) · [Commented source]({source.name}) · [Repository home](../README.md)', '',
        '> **Reading edition.** Original lecture references are retained for study. '
        'The commented source runs no analysis. Code below is reference material; '
        'check paths, packages, inputs and prerequisites before using it.', '', intro, '',
    ]
    in_code = False
    for line in lines[first_heading:]:
        heading = re.match(r'(?:CHUNK (\d+) — (.*)|===== Lecture 3, chunk (\d+): (.*?) =====)', line)
        if heading:
            if in_code:
                out.extend(['```', ''])
                in_code = False
            number = heading.group(1) or heading.group(3)
            title = heading.group(2) or heading.group(4)
            title = re.sub(r' \(source line \d+\)$', '', title)
            if title.isupper():
                title = title.capitalize()
            out.extend([f'## {number}. {title}', ''])
        elif line == 'Lecture reference code:':
            out.extend(['', '**Lecture reference code**', '', '```r'])
            in_code = True
        elif in_code:
            out.append(line)
        else:
            line = re.sub(r'^(Objective/how|Learn): ', '**Learn:** ', line)
            line = re.sub(r'^Apply: ', '**Apply:** ', line)
            out.extend([line, ''] if line else [''])
    if in_code:
        out.append('```')
    return contents(re.sub(r'\n{3,}', '\n\n', '\n'.join(out)) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report stale editions without writing.')
    args = parser.parse_args()
    sources = sorted((ROOT / '02_Lecture_Notes').glob('Week*.R'))
    sources += sorted((ROOT / '02_Lecture_Notes').glob('Week*.Rmd'))
    sources += sorted((ROOT / '03_Group_Work').glob('Week*.Rmd'))
    stale = []
    for source in sources:
        output = rmarkdown(source) if source.suffix == '.Rmd' else commented_lecture(source)
        target = source.with_suffix('.md')
        if not target.exists() or target.read_text() != output:
            stale.append(str(target.relative_to(ROOT)))
            if not args.check:
                target.write_text(output)
    if args.check and stale:
        print('Stale reading editions:\n' + '\n'.join(stale))
        return 1
    print(f'{"Checked" if args.check else "Built"} {len(sources)} reading editions; '
          f'{len(stale)} {"stale" if args.check else "updated"}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
