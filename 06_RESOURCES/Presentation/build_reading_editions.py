#!/usr/bin/env python3
"""Build public reading companions without executing their source code."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LECTURES = ROOT / '02_Lecture_Notes'
GROUP_WORK = ROOT / '03_Group_Work'


def anchor(title: str) -> str:
    """Create the same simple heading anchors used by the reading editions."""
    return re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')


def contents(text: str) -> str:
    """Insert an index before the first level-two heading."""
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
    first = text.find('\n## ')
    if first < 0:
        return text
    return text[:first] + '\n## On this page\n\n' + '\n'.join(headings) + '\n' + text[first:]


def rmarkdown(source: Path) -> str:
    """Convert an R Markdown lesson to a nonexecuting Markdown reading copy."""
    parts = source.read_text(encoding='utf-8').split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'{source.relative_to(ROOT)}: expected YAML front matter')
    _, metadata, body = parts
    match = re.search(r'^title:\s*(.+?)\s*$', metadata, re.M)
    if not match:
        raise ValueError(f'{source.relative_to(ROOT)}: missing title in YAML front matter')
    title = match.group(1).strip().strip('"').strip("'")
    body = re.sub(r'^```\{(r|bash|sh)[^}]*\}', r'```\1', body, flags=re.M)
    body = re.sub(r'^```\{[^}]*\}', '```text', body, flags=re.M)
    body = re.sub(r'`r [^`]+`', '[computed when rendered]', body)
    course_keyed = source.parent == GROUP_WORK
    notice = ('**Course-file dependency.** This independent guide is not a substitute for official Geisel prompts and course inputs. Obtain these separately and perform assessed work privately.' if course_keyed else 'Code is displayed for independent study and has not been executed to generate this page. Check source permissions and locally supplied inputs before running examples.')
    header = (
        f'# {title}\n\n'
        f'[Section index](README.md) · [Editable R Markdown]({source.name}) · '
        '[Repository home](../README.md)\n\n'
        f'> **Reading edition.** {notice}\n\n'
    )
    return contents(header + body.lstrip())



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report stale editions without writing.')
    args = parser.parse_args()
    # Publish student-authored R Markdown only. Standalone conceptual .R
    # references have manually maintained .md companions; never generate
    # public instructor-code transcripts from R scripts.
    sources = sorted(LECTURES.glob('Week*.Rmd'))
    sources += sorted(GROUP_WORK.glob('Week*.Rmd'))
    stale = []
    for source in sources:
        output = rmarkdown(source)
        target = source.with_suffix('.md')
        if not target.exists() or target.read_text(encoding='utf-8') != output:
            stale.append(str(target.relative_to(ROOT)))
            if not args.check:
                target.write_text(output, encoding='utf-8')
    if args.check and stale:
        print('Stale reading editions:\n' + '\n'.join(stale))
        return 1
    print(f'{"Checked" if args.check else "Built"} {len(sources)} reading editions; '
          f'{len(stale)} {"stale" if args.check else "updated"}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
