#!/usr/bin/env python3
"""Execute every gallery R block in a clean session; outputs stay outside Git."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def extract(text):
    blocks, current = [], None
    for line in text.splitlines():
        if line.startswith('```'):
            if current is None:
                if line != '```r':
                    raise ValueError('Unsupported gallery fence')
                current = []
            else:
                if line != '```':
                    raise ValueError('Malformed gallery fence')
                blocks.append('\n'.join(current)); current = None
        elif current is not None:
            current.append(line)
    if current is not None or not blocks:
        raise ValueError('Missing or unclosed gallery R blocks')
    return blocks


def validate(output):
    output = output.resolve()
    if output.is_relative_to(ROOT) or output == ROOT:
        raise ValueError('Choose an output directory outside Git')
    if not shutil.which('Rscript'):
        raise ValueError('Rscript is required; no skipped execution')
    output.mkdir(parents=True, exist_ok=True)
    blocks = extract((ROOT / '06_RESOURCES/VISUALIZATION_GALLERY.md').read_text())
    inputs = output / 'gallery-input.R'
    inputs.write_text('\n\n'.join(blocks)+'\n')
    driver = output / 'gallery-driver.R'
    driver.write_text('options(warn=2)\ncode <- parse('+json.dumps(str(inputs))+')\n' +
                      'grDevices::pdf('+json.dumps(str(output/'gallery-pages.pdf'))+', width=7, height=5)\n' +
                      'for (i in seq_along(code)) eval(code[[i]], envir=.GlobalEnv)\n' +
                      'grDevices::dev.off()\n' +
                      'stopifnot(length(figures)==6L)\n' +
                      'writeLines(capture.output(sessionInfo()), '+json.dumps(str(output/'session-info.txt'))+')\n')
    env = dict(os.environ, PAULS_FIGURE_DIR=str(output / 'figures'))
    with (output / 'execution.log').open('w') as log:
        run = subprocess.run(['Rscript', '--vanilla', str(driver)], cwd=ROOT,
                             env=env, stdout=log, stderr=subprocess.STDOUT)
    paths = [output/'figures'/f'{name}.{ext}' for name in
             ('distribution', 'association', 'expression', 'row_deviation', 'pca', 'volcano')
             for ext in ('png', 'pdf')]
    status = run.returncode == 0 and all(p.is_file() and p.stat().st_size > 1000 for p in paths)
    report = {'status': 'PASS' if status else 'FAIL', 'r_blocks': len(blocks),
              'exit_code': run.returncode, 'figures': [str(p) for p in paths],
              'log': str(output/'execution.log')}
    (output/'results.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    try:
        r = validate(args.output_dir)
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc)+'\n')
    print(f"Gallery: {r['status']}; {r['r_blocks']} R blocks, 12 figure files")
    return r['status'] != 'PASS'


if __name__ == '__main__':
    raise SystemExit(main())
