#!/usr/bin/env python3
"""Parse and execute the complete Week 4 lesson; keep outputs outside Git."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "03_Group_Work/Week_4_Bash_and_Reproducible_Workflows_Study_Guide.Rmd"


def chunks(text: str) -> list[tuple[str, str]]:
    """Extract named Bash chunks, rejecting unsupported options and bad fences."""
    result = []
    active = None
    fenced = False
    body = []
    for line in text.splitlines():
        if line.startswith('```'):
            if fenced:
                if line != '```':
                    raise ValueError('Expected closing code fence')
                if active is not None:
                    result.append((active, '\n'.join(body)))
                active, body, fenced = None, [], False
            else:
                fenced = True
                match = re.fullmatch(r'```\{bash ([a-z0-9_-]+)\}', line)
                if line.startswith('```{bash') and not match:
                    raise ValueError('Unsupported Bash chunk declaration')
                active = match.group(1) if match else None
        elif active is not None:
            body.append(line)
    if fenced or not result or any(not code.strip() for _, code in result):
        raise ValueError('Incomplete or empty Bash lesson')
    if len({name for name, _ in result}) != len(result):
        raise ValueError('Duplicate Bash block labels')
    return result


def check_syntax(blocks: list[tuple[str, str]]) -> None:
    for name, code in blocks:
        run = subprocess.run(['bash', '-n'], input=code, text=True, capture_output=True)
        if run.returncode:
            raise ValueError(f'{name}: {run.stderr.strip()}')


def verify_outputs(workspace: Path) -> None:
    """Verify the data contract, rather than accepting a zero process status alone."""
    expected_input = 'run_id,bench,minutes\nb01,A,8\nb02,B,15\nb03,A,NA\nb04,B,21\nb05,A,12\n'
    if (workspace / 'input/run times.csv').read_text() != expected_input:
        raise ValueError('Original input changed')
    for bench, expected in [('A', ['b01', 'b03', 'b05']), ('B', ['b02', 'b04'])]:
        with (workspace / f'output/bench_{bench}.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        if [row.get('run_id') for row in rows] != expected:
            raise ValueError(f'Wrong selection for bench {bench}')
    if (workspace / 'output/rejected.csv').exists():
        raise ValueError('Failed filter published an output')
    for filename, eligible, means in [('summary.csv', 'TRUE', ['10', '18']),
                                      ('minimum_three.csv', 'FALSE', ['NA', 'NA'])]:
        with (workspace / 'output' / filename).open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        actual = [(row.get('bench'), row.get('n_total'), row.get('n_measured'), row.get('n_missing'),
                   row.get('eligible'), row.get('mean_minutes')) for row in rows]
        expected = [('A', '3', '2', '1', eligible, means[0]),
                    ('B', '2', '2', '0', eligible, means[1])]
        if actual != expected:
            raise ValueError(f'Unexpected summary: {filename}: {actual}')


def run_lesson(destination: Path) -> dict:
    destination = destination.resolve()
    if destination.is_relative_to(ROOT):
        raise ValueError('Validation outputs must be outside the repository')
    for command in ('bash', 'awk', 'grep', 'head', 'wc', 'sort', 'uniq', 'mktemp', 'Rscript'):
        if not shutil.which(command):
            raise ValueError(f'Required command unavailable: {command}')
    blocks = chunks((ROOT / SOURCE).read_text())
    check_syntax(blocks)
    destination.mkdir(parents=True, exist_ok=True)
    # All chunks share one shell; each run gets its own retained practice parent.
    parent = Path(tempfile.mkdtemp(prefix='practice-', dir=destination))
    script = '\n'.join(f"printf '%s\\n' 'CHECK {name}'\n{code}" for name, code in blocks)
    script += '\nprintf "WORKSPACE=%s\\n" "$practice_dir"\n'
    driver = parent / 'validate.sh'
    driver.write_text(script)
    run = subprocess.run(['bash', str(driver)], cwd=parent, capture_output=True,
                         text=True, timeout=120)
    (parent / 'execution.log').write_text(run.stdout + run.stderr)
    if run.returncode:
        raise ValueError(f'Lesson failed; see {parent / "execution.log"}')
    matches = re.findall(r'^WORKSPACE=(.+)$', run.stdout, re.M)
    if len(matches) != 1:
        raise ValueError('Missing lesson workspace result')
    workspace = Path(matches[0]).resolve()
    # The setup chunk creates only a new temporary practice directory.
    if workspace.is_relative_to(ROOT):
        raise ValueError('Lesson workspace unexpectedly inside repository')
    verify_outputs(workspace)
    result = {'source': SOURCE, 'blocks': len(blocks), 'status': 'PASS',
              'workspace': str(workspace), 'log': str(parent / 'execution.log')}
    (destination / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run_lesson(args.output_dir)
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        parser.exit(2, f'Bash lesson validation incomplete: {exc}\n')
    print(f"Week 4: {result['blocks']} Bash blocks — PASS; results: {result['workspace']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
