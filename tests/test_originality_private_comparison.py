"""Synthetic fixtures only; never embed actual course sources in tests."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('private_comparison', Path(__file__).resolve().parents[1] / 'scripts/compare_private_sources.py')
compare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compare)


class PrivateComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base / 'public'
        self.sources = base / 'private'
        self.root.mkdir()
        self.sources.mkdir()
        subprocess.run(['git', 'init', '-q'], cwd=self.root, check=True)
        self.text = ' '.join(f'synthetic_word_{n}' for n in range(35))
        (self.sources / 'private_original.rmd').write_text(self.text)

    def tracked(self, text):
        (self.root / 'notes.md').write_text(text)
        subprocess.run(['git', 'add', 'notes.md'], cwd=self.root, check=True)

    def test_identical_source_bytes_and_no_source_text_in_report(self):
        self.tracked(self.text)
        report = compare.compare(self.root, [self.sources])
        self.assertTrue(any(x['kind'] == 'identical_bytes' for x in report['current_findings']))
        rendered = json.dumps(report)
        self.assertNotIn(self.text, rendered)
        self.assertNotIn(str(self.sources), rendered)
        self.assertNotIn('private_original', rendered)

    def test_normalized_overlap_detected_without_exact_copy(self):
        self.tracked('Preface. ' + self.text.upper() + ' Footer.')
        report = compare.compare(self.root, [self.sources])
        self.assertTrue(any(x['kind'] == 'shared_20_token_windows' for x in report['current_findings']))
        self.assertFalse(any(x['kind'] == 'identical_bytes' for x in report['current_findings']))

    def test_independent_content_passes(self):
        self.tracked('Completely different independent example.')
        self.assertEqual(compare.compare(self.root, [self.sources])['current_findings'], [])

    def test_source_inside_public_repository_rejected(self):
        self.tracked(self.text)
        with self.assertRaises(ValueError):
            compare.compare(self.root, [self.root])

    def test_removed_content_remains_visible_in_history(self):
        self.tracked(self.text)
        subprocess.run(['git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                        'commit', '-qm', 'synthetic fixture'], cwd=self.root, check=True)
        self.tracked('Replacement independent content.')
        report = compare.compare(self.root, [self.sources], history=True)
        self.assertEqual(report['current_findings'], [])
        self.assertEqual(len(report['history_exact_matches']), 1)
        self.assertEqual(len(report['history_text_matches']), 1)

    def test_empty_source_set_is_not_a_pass(self):
        (self.sources / 'private_original.rmd').unlink()
        with self.assertRaises(ValueError):
            compare.compare(self.root, [self.sources])


if __name__ == '__main__':
    unittest.main()
