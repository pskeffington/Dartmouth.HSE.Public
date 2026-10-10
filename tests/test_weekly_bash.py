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
        self.input.write_text('Participant_ID,Sex,Age,Sample_Type,Measurement\nx1,Male,40,Serum,0.9\nx2,Female,52,Plasma,NA\nx3,Female,61,Plasma,1.4\n')
        self.output = self.root / 'output' / 'selection.csv'

    def filter(self, *args):
        return subprocess.run(['bash', str(self.root / 'scripts/filter_samples.sh'),
                               *map(str, args)], capture_output=True, text=True)

    def test_actual_lesson_syntax(self):
        lesson.check_syntax(list(BLOCKS.items()))

    def test_selection_retains_missingness_and_accepts_space_paths(self):
        run = self.filter(self.input, self.output, 'Plasma')
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(self.output.read_text(), 'Participant_ID,Sex,Age,Sample_Type,Measurement\nx2,Female,52,Plasma,NA\nx3,Female,61,Plasma,1.4\n')

    def test_bad_records_do_not_replace_existing_output(self):
        cases = [
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,1.4\nx,Male,42,Serum,1.5\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,-1\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,NaN\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\n"x",Female,40,Plasma,1.4\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Male,40,Saliva,1.5\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\n,Female,40,Plasma,1.4\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma\n',
            'Wrong_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,1.4\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,17,Plasma,1.4\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40.5,Plasma,1.4\n',
            'Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Unknown,40,Plasma,1.4\n',
            '',
        ]
        for contents in cases:
            with self.subTest(contents=contents):
                self.input.write_text(contents)
                self.output.write_text('preserved output\n')
                run = self.filter(self.input, self.output, 'Plasma')
                self.assertEqual(run.returncode, 1)
                self.assertEqual(self.output.read_text(), 'preserved output\n')
                self.assertEqual(list(self.output.parent.glob('selection.csv.*')), [])

    def test_bad_arguments_and_aliases_do_not_replace_input(self):
        original = self.input.read_bytes()
        alias = self.root / 'same-input.csv'
        alias.symlink_to(self.input)
        for args in ((self.input, self.output), (self.input, self.output, 'Saliva'),
                     (self.input, self.input, 'Plasma'), (self.input, alias, 'Plasma')):
            self.assertEqual(self.filter(*args).returncode, 2)
            self.assertEqual(self.input.read_bytes(), original)
        self.assertFalse(self.output.exists())

    def test_zero_selected_rows_preserve_header(self):
        self.input.write_text('Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Male,40,Serum,1.4\n')
        self.assertEqual(self.filter(self.input, self.output, 'Plasma').returncode, 0)
        self.assertEqual(self.output.read_text(), 'Participant_ID,Sex,Age,Sample_Type,Measurement\n')

    @unittest.skipUnless(shutil.which('Rscript'), 'Rscript required for bridge behavior')
    def test_r_bridge_missing_measurements_and_argument_validation(self):
        self.input.write_text('Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,NA\ny,Male,42,Serum,NA\n')
        script = str(self.root / 'scripts/summarize_samples.R')
        run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), '2'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn('"Plasma",1,0,1,FALSE,NA', self.output.read_text())
        self.assertIn('"Serum",1,0,1,FALSE,NA', self.output.read_text())
        self.input.write_text('Participant_ID,Sex,Age,Sample_Type,Measurement\n01,Female,40,Plasma,1.1\n1,Male,42,Serum,1.2\n')
        run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), '1'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)  # Distinct character IDs must not collapse.
        for cutoff in ('two', '0', '-1', '2.5', 'Inf'):
            run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), cutoff], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('positive integer', run.stderr)
        self.input.write_text('Participant_ID,Sex,Age,Sample_Type,Measurement\nx,Female,40,Plasma,bad\n')
        run = subprocess.run(['Rscript', '--vanilla', script, str(self.input), str(self.output), '2'], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('Measurement must be', run.stderr)

    def test_unclosed_duplicate_or_unsupported_chunks_fail(self):
        for text in ('```{bash first}\necho ok',
                     '```{bash first, eval=FALSE}\necho ok\n```',
                     '```{bash first}\necho ok\n```\n```{bash first}\necho ok\n```'):
            with self.assertRaises(ValueError):
                lesson.chunks(text)


if __name__ == '__main__':
    unittest.main()
