"""Regression checks for reading conversion and executable lesson extraction."""
import importlib.util
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_weekly_r as validator
import check_originality_change as change
spec = importlib.util.spec_from_file_location('editions', ROOT / '06_RESOURCES/Presentation/build_reading_editions.py')
editions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editions)


class PresentationTests(unittest.TestCase):
    def test_source_text_preserved_in_reading_edition(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'lesson.Rmd'
            source.write_text('---\ntitle: "Paul\'s Notes"\n---\n\n## Read the axes\n\n| Axis | Unit |\n| --- | --- |\n| Time | s |\n\n```{r check}\nx <- 4\n```\n\n**Expected:** 4.\n')
            reading = editions.rmarkdown(source)
            self.assertIn('# Paul\'s Notes', reading)
            self.assertIn('[Read the axes](#read-the-axes)', reading)
            self.assertIn('```r\nx <- 4\n```', reading)
            self.assertIn('| Time | s |', reading)
            self.assertIn('**Expected:** 4.', reading)
            self.assertNotIn('Course-file dependency', reading)

    def test_extractor_preserves_order_and_ignores_output_fence(self):
        source = '```{r first}\nx <- 3\n```\n```text\nnot R\n```\n```{r second}\nstopifnot(x == 3)\n```\n'
        self.assertEqual(validator.chunks(source), [('first', 'x <- 3'), ('second', 'stopifnot(x == 3)')])

    def test_incomplete_or_unsupported_blocks_fail_closed(self):
        for source in ('no executable blocks', '```{r first}\nx <- 2', '```{r first, eval=FALSE}\nx <- 2\n```', '```{r first}\nx <- 2\n```text'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                validator.chunks(source)

    def test_every_required_lesson_has_runnable_blocks(self):
        for source in validator.SOURCES:
            with self.subTest(source=source):
                self.assertGreaterEqual(len(validator.chunks((ROOT / source).read_text())), 10)


class ChangeGateTests(unittest.TestCase):
    def finding(self, level='review', path='existing.pdf'):
        return {'path': path, 'level': level, 'reason': 'manual review'}

    def report(self, findings):
        return {'status': 'BLOCK' if any(f['level'] == 'block' for f in findings) else 'REVIEW' if findings else 'SCREEN_CLEAR', 'findings': findings}

    def test_unchanged_review_remains_visible(self):
        report = self.report([self.finding()])
        result = change.decision(report, report, {'existing.pdf'})
        self.assertEqual(result['change_status'], 'PASS')
        self.assertEqual(result['full_repository_status'], 'REVIEW')
        self.assertEqual(len(result['retained_unresolved_reviews']), 1)

    def test_changed_review_and_new_review_fail(self):
        report = self.report([self.finding()])
        self.assertEqual(change.decision(report, report, set())['change_status'], 'FAIL')
        extra = self.report([self.finding(), self.finding(path='new.pdf')])
        self.assertEqual(change.decision(report, extra, {'existing.pdf'})['change_status'], 'FAIL')

    def test_existing_block_is_never_exempt(self):
        report = self.report([self.finding(level='block')])
        self.assertEqual(change.decision(report, report, {'existing.pdf'})['change_status'], 'FAIL')

    def test_real_baseline_detects_modified_flagged_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            asset = root / 'existing.pdf'
            asset.write_bytes(b'synthetic baseline fixture')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            subprocess.run(['git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                            'commit', '-qm', 'baseline'], cwd=root, check=True)
            self.assertEqual(change.inspect(root, 'HEAD')['change_status'], 'PASS')
            asset.write_bytes(b'changed synthetic fixture')
            self.assertEqual(change.inspect(root, 'HEAD')['change_status'], 'FAIL')

    def test_invalid_report_is_not_a_pass(self):
        with self.assertRaises(ValueError):
            change.decision({}, self.report([]), set())


if __name__ == '__main__':
    unittest.main()
