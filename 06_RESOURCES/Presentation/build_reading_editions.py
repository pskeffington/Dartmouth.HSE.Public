#!/usr/bin/env python3
"""Build public reading companions without executing their source code."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LECTURES = ROOT / '02_Lecture_Notes'
GROUP_WORK = ROOT / '03_Group_Work'

# Explicit baseline prevents missing files being masked by unrelated new sources.
# Adding a new reading edition is a reviewed source-manifest change.
REQUIRED_SOURCES = (
    "02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.Rmd",
    "02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.Rmd",
    "02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.Rmd",
    "02_Lecture_Notes/Week_4_Introduction_to_Bash_Lecture_Notes.Rmd",
    "03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.Rmd",
    "03_Group_Work/Week_2_Group_Work_Narrative_Walkthrough.Rmd",
    "03_Group_Work/Week_3_Group_Work_Narrative_Walkthrough.Rmd",
)

def verify_required_sources(root: Path, sources: list[Path]) -> list[str]:
    available = {p.relative_to(root).as_posix() for p in sources}
    return sorted(set(REQUIRED_SOURCES) - available)



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
    notice = ('Code is displayed, not executed by this converter. '
              'The weekly teaching guides provide synthetic inputs and expected results; '
              'see each source for dependencies and execution checks.')
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
    missing = verify_required_sources(ROOT, sources)
    if missing:
        print("ERROR: required public reading sources are missing:")
        for name in missing:
            print(f"  - {name}")
        return 2
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
