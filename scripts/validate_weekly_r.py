#!/usr/bin/env python3
"""Parse and execute the three public teaching lessons in clean R sessions.

Writes logs and plots only to an explicitly selected directory outside Git.
Lesson stopifnot checks verify expected structures, counts, values, and errors.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

COMPANIONS = (
    "02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.Rmd",
    "02_Lecture_Notes/Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.Rmd",
    "02_Lecture_Notes/Week_3_Data_Visualization_and_Analytics_Lecture_Notes.Rmd",
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = tuple(f'03_Group_Work/Week_{week}_Group_Work_Narrative_Walkthrough.Rmd' for week in (1, 2, 3))


def chunks(text: str) -> list[tuple[str, str]]:
    result = []
    active = None
    body = []
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            if fenced:
                if line != "```":
                    raise ValueError("Expected closing code fence")
                if active is not None:
                    result.append((active, '\n'.join(body)))
                active, body, fenced = None, [], False
            else:
                fenced = True
                match = re.fullmatch(r'```\{r(?:\s+([A-Za-z0-9_-]+))?\}', line)
                if line.startswith('```{r') and not match:
                    raise ValueError('Unsupported R chunk options; explicit validation is required')
                active = (match.group(1) or f'block-{len(result)+1}') if match else None
        elif active is not None:
            body.append(line)
    if fenced:
        raise ValueError('Unclosed code fence')
    if not result or any(not code.strip() for _, code in result):
        raise ValueError('Missing or empty executable R blocks')
    names = [name for name, _ in result]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate R block labels')
    return result


def driver(blocks: list[tuple[str, str]]) -> str:
    # Parse ALL blocks before execution so an early runtime error cannot conceal
    # a later syntax error. Each process starts with --vanilla and warns as errors.
    lines = ['options(warn = 2)', 'pdf("plots.pdf", width = 7, height = 5)']
    for index, (name, code) in enumerate(blocks):
        lines += [f'parsed_{index} <- parse(text = {json.dumps(code)})']
    for index, (name, code) in enumerate(blocks):
        lines += [f'cat({json.dumps("CHECK " + name + chr(10))})',
                  f'eval(parsed_{index}, envir = .GlobalEnv)']
    lines += ['dev.off()', f'cat("PASS: {len(blocks)} blocks\\n")']
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument("--include-companions", action="store_true", help="Also execute the three R topic companions")
    args = parser.parse_args()
    destination = args.output_dir.resolve()
    if destination.is_relative_to(ROOT):
        parser.exit(2, 'Validation outputs must be outside the repository\n')
    rscript = shutil.which('Rscript')
    if not rscript:
        parser.exit(2, 'Rscript unavailable: runtime checks have NOT passed\n')
    destination.mkdir(parents=True, exist_ok=True)
    results = []
    try:
        for index, name in enumerate(SOURCES + (COMPANIONS if args.include_companions else ()), 1):
            week = (index - 1) % 3 + 1
            label = ("companion-" if index > 3 else "") + f"week-{week}"
            blocks = chunks((ROOT / name).read_text())
            folder = destination / label
            folder.mkdir(exist_ok=True)
            (folder / 'validate.R').write_text(driver(blocks))
            run = subprocess.run([rscript, '--vanilla', 'validate.R'], cwd=folder,
                                 capture_output=True, text=True, timeout=120)
            (folder / 'execution.log').write_text(run.stdout + run.stderr)
            result = {'source': name, 'blocks': len(blocks), 'status': 'PASS' if run.returncode == 0 else 'FAIL'}
            results.append(result)
            print(f"{label}: {len(blocks)} blocks — {result['status']}")
            if run.returncode:
                print((run.stdout + run.stderr)[-3000:])
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        parser.exit(2, f'Lesson validation incomplete: {exc}\n')
    (destination / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    return 0 if all(item['status'] == 'PASS' for item in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
