#!/usr/bin/env python3
"""Ensure the reading-edition publication baseline is fail-closed."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "06_RESOURCES" / "Presentation" / "build_reading_editions.py"
SPEC = importlib.util.spec_from_file_location("reading_editions", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class ReadingSourceManifestTests(unittest.TestCase):
    def test_manifest_has_no_duplicates(self):
        self.assertEqual(len(builder.REQUIRED_SOURCES),
                         len(set(builder.REQUIRED_SOURCES)))

    def test_current_checkout_has_required_files(self):
        actual = ([*builder.LECTURES.glob("Week*.Rmd")] +
                  [*builder.GROUP_WORK.glob("Week*.Rmd")])
        self.assertEqual(builder.verify_required_sources(ROOT, actual), [])

    def test_missing_expected_file_cannot_be_hidden_by_an_extra(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            paths = [root / name for name in builder.REQUIRED_SOURCES[1:]]
            paths.append(root / "03_Group_Work/Week_99_Extra.Rmd")
            missing = builder.verify_required_sources(root, paths)
            self.assertEqual(missing, [builder.REQUIRED_SOURCES[0]])

    def test_no_sources_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(
                builder.verify_required_sources(Path(folder), []),
                sorted(builder.REQUIRED_SOURCES),
            )


if __name__ == "__main__":
    unittest.main()
