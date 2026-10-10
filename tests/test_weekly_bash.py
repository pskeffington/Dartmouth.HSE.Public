"""Exercise the Week 4 script contracts with small local fixtures."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('bash_lesson', ROOT / 'scripts/validate_weekly_bash.py')
lesson = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lesson)
BLOCKS = dict(lesson.chunks((ROOT / lesson.SOURCE).read_text()))


class BashLessonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        (self.root / 'output').mkdir()
        for label in ('write-filter-script', 'write-r-script'):
            code = BLOCKS[label].split('\nbash -n')[0]
            run = subprocess.run(['bash', '-eu', '-c', code], cwd=self.root,
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
        self.input = self.root / 'input with spaces.csv'
        self.input.write_text('run_id,bench,minutes\nx1,B,9\nx2,A,NA\nx3,A,4\n')
        self.output = self.root / 'output' / 'selection.csv'

    def filter(self, *args):
        return subprocess.run(['bash', str(self.root / 'scripts/filter_runs.sh'),
                               *map(str, args)], capture_output=True, text=True)

    def test_actual_lesson_syntax(self):
        lesson.check_syntax(list(BLOCKS.items()))

    def test_selection_retains_missingness_and_accepts_space_paths(self):
        run = self.filter(self.input, self.output, 'A')
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(self.output.read_text(), 'run_id,bench,minutes\nx2,A,NA\nx3,A,4\n')

    def test_bad_records_do_not_replace_existing_output(self):
        cases = [
            'run_id,bench,minutes\nx,A,4\nx,B,5\n',
            'run_id,bench,minutes\nx,A,-1\n',
            'run_id,bench,minutes\nx,A,NaN\n',
            'run_id,bench,minutes\n"x",A,4\n',
            'run_id,bench,minutes\nx,C,5\n',
            'run_id,bench,minutes\n,A,4\n',
            'run_id,bench,minutes\nx,A\n',
            'wrong,bench,minutes\nx,A,4\n',
            '',
        ]
        for contents in cases:
            with self.subTest(contents=contents):
                self.input.write_text(contents)
                self.output.write_text('preserved output\n')
                run = self.filter(self.input, self.output, 'A')
                self.assertEqual(run.returncode, 1)
                self.assertEqual(self.output.read_text(), 'preserved output\n')
                self.assertEqual(list(self.output.parent.glob('selection.csv.*')), [])

    def test_bad_arguments_and_aliases_do_not_replace_input(self):
        original = self.input.read_bytes()
        alias = self.root / 'same-input.csv'
        alias.symlink_to(self.input)
        for args in ((self.input, self.output), (self.input, self.output, 'C'),
                     (self.input, self.input, 'A'), (self.input, alias, 'A')):
            self.assertEqual(self.filter(*args).returncode, 2)
            self.assertEqual(self.input.read_bytes(), original)
        self.assertFalse(self.output.exists())

    def test_zero_selected_rows_preserve_header(self):
        self.input.write_text('run_id,bench,minutes\nx,B,4\n')
        self.assertEqual(self.filter(self.input, self.output, 'A').returncode, 0)
        self.assertEqual(self.output.read_text(), 'run_id,bench,minutes\n')

    @unittest.skipUnless(shutil.which('Rscript'), 'Rscript required for bridge behavior')
    def test_r_bridge_missing_measurements_and_argument_validation(self):
        self.input.write_text('run_id,bench,minutes\nx,A,NA\ny,B,NA\n')
        script = str(self.root / 'scripts/summarize_runs.R')
        run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), '2'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn('"A",1,0,1,FALSE,NA', self.output.read_text())
        self.assertIn('"B",1,0,1,FALSE,NA', self.output.read_text())
        for cutoff in ('two', '0', '-1', '2.5', 'Inf'):
            run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), cutoff], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('positive integer', run.stderr)
        self.input.write_text('run_id,bench,minutes\nx,A,bad\n')
        run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), '2'], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('Minutes must be', run.stderr)

    def test_unclosed_duplicate_or_unsupported_chunks_fail(self):
        for text in ('```{bash first}\necho ok',
                     '```{bash first, eval=FALSE}\necho ok\n```',
                     '```{bash first}\necho ok\n```\n```{bash first}\necho ok\n```'):
            with self.assertRaises(ValueError):
                lesson.chunks(text)


if __name__ == '__main__':
    unittest.main()
