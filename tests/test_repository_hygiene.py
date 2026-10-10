"""Behavior and safety checks for public maintenance utilities."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositoryHygieneTests(unittest.TestCase):
    def test_symlink_is_blocked_without_reading_external_content(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            repo = base / 'repo'
            repo.mkdir()
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            external = base / 'private.txt'
            external.write_text('Private fixture content')
            (repo / 'linked.txt').symlink_to(external)
            subprocess.run(['git', 'add', 'linked.txt'], cwd=repo, check=True)
            screen = load('check_public_originality').scan(repo)
            self.assertEqual(screen['status'], 'BLOCK')
            self.assertIn('symlink', screen['findings'][0]['reason'])
            entry = load('build_provenance_inventory').inventory(repo)['entries'][0]
            self.assertEqual(entry['status'], 'unsafe')
            self.assertNotIn('sha256', entry)
            self.assertNotIn('bytes', entry)

    def test_inventory_check_accepts_only_current_records_and_self_omission(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            (repo / 'README.md').write_text('# Practice\n')
            records = {'entries': [
                {'path': 'README.md', 'observed_sha256': hashlib.sha256((repo / 'README.md').read_bytes()).hexdigest()},
                {'path': 'PROVENANCE_RECORDS.json', 'observed_sha256': None},
            ]}
            register = repo / 'PROVENANCE_RECORDS.json'
            register.write_text(json.dumps(records))
            subprocess.run(['git', 'add', '.'], cwd=repo, check=True)
            command = ['python3', str(ROOT / 'scripts/build_provenance_inventory.py'), '--root', str(repo), '--check']
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            (repo / 'README.md').write_text('# Changed\n')
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            records['entries'][0]['observed_sha256'] = None
            register.write_text(json.dumps(records))
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            records['entries'].append({'path': 'obsolete.txt', 'observed_sha256': None})
            register.write_text(json.dumps(records))
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)

    def test_bash_helpers_handle_option_assignment_and_space_paths(self):
        helper = ROOT / '06_RESOURCES/Bash/bash_functions.sh'
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            data = b'name\tvalue\nu\t4\nv\t9\n'
            for name in ('-records.tsv', 'values=records.tsv', 'two words.tsv'):
                (repo / name).write_bytes(data)
                script = 'source "$1"; hse_tsv_records "$2"; hse_tsv_columns "$2"; hse_sha256 "$2"'
                run = subprocess.run(['bash', '-c', script, 'test', str(helper), name], cwd=repo, capture_output=True, text=True)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertTrue(run.stdout.startswith('2\n1\tname\n2\tvalue\n'))
                self.assertIn(hashlib.sha256(data).hexdigest(), run.stdout)
            missing = subprocess.run(['bash', '-c', 'source "$1"; hse_tsv_records missing.tsv', 'test', str(helper)], cwd=repo, capture_output=True, text=True)
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn('missing or unreadable', missing.stderr)

    def test_r_launcher_preserves_arguments_and_exit_status(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            executable = repo / 'Rscript'
            executable.write_text('#!/usr/bin/env bash\nprintf "%s\\n" "$@"\nexit 7\n')
            executable.chmod(0o755)
            (repo / '-practice.R').write_text('invisible(NULL)\n')
            run = subprocess.run(['bash', '-c', 'source "$1"; hse_run_r -practice.R "two words"', 'test', str(ROOT / '06_RESOURCES/Bash/bash_functions.sh')], cwd=repo, env={**os.environ, 'PATH': str(repo) + os.pathsep + os.environ['PATH']}, capture_output=True, text=True)
            self.assertEqual(run.returncode, 7)
            self.assertEqual(run.stdout.splitlines(), ['--vanilla', './-practice.R', 'two words'])

    def test_tex_invalid_arguments_fail_before_build(self):
        compiler = ROOT / '06_RESOURCES/LaTeX/compile_manuscript.sh'
        for args in (['--unknown'], ['--output-dir'], ['--catalogue', 'unexpected']):
            run = subprocess.run(['bash', str(compiler), *args], capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertNotIn('Missing tool', run.stderr)


if __name__ == '__main__':
    unittest.main()
