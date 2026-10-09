#!/usr/bin/env python3
"""Exercise the public-release scanner on temporary Git-tracked fixtures."""
from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "public_originality", ROOT / "scripts" / "check_public_originality.py"
)
assert SPEC and SPEC.loader
screen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(screen)


class ScanIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def tracked(self, name: str, content: str) -> None:
        file = self.root / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
        subprocess.run(["git", "add", "--", name], cwd=self.root, check=True)

    def test_course_mapping_requires_review(self) -> None:
        self.tracked("02_Lecture_Notes/practice.md", "Lecture 3 chunks 10-15")
        report = screen.scan(self.root)
        self.assertEqual(report["status"], "REVIEW")
        self.assertTrue(any("lecture chunk mapping" in x["reason"]
                            for x in report["findings"]))

    def test_generic_original_notes_can_screen_clear(self) -> None:
        self.tracked("03_Group_Work/concepts.md", "Understand numeric columns.")
        self.assertEqual(screen.scan(self.root)["status"], "SCREEN_CLEAR")

    def test_restricted_named_file_blocks(self) -> None:
        self.tracked("05_Assignments/instructor_slides.pptx", "placeholder")
        self.assertEqual(screen.scan(self.root)["status"], "BLOCK")

    def test_missing_tracked_file_requires_review(self) -> None:
        self.tracked("notes.md", "original commentary")
        (self.root / "notes.md").unlink()
        self.assertEqual(screen.scan(self.root)["status"], "REVIEW")

    def test_binary_requires_manual_review(self) -> None:
        self.tracked("illustration.png", "PNG placeholder")
        self.assertEqual(screen.scan(self.root)["status"], "REVIEW")

    def test_test_fixture_literals_do_not_block_ci(self) -> None:
        self.tracked("tests/test_originality_screen.py",
                     'self.assertIn("All rights reserved", example)')
        self.assertEqual(screen.scan(self.root)["status"], "SCREEN_CLEAR")

    def test_unlisted_test_file_still_scanned(self) -> None:
        self.tracked("tests/test_unreviewed.py", "All rights reserved")
        self.assertEqual(screen.scan(self.root)["status"], "BLOCK")

    def test_tracked_csv_needs_provenance_review(self) -> None:
        self.tracked("06_RESOURCES/example.csv", "id,value\\n1,4\\n")
        report = screen.scan(self.root)
        self.assertEqual(report["status"], "REVIEW")
        self.assertTrue(any("redistribution review" in item["reason"]
                            for item in report["findings"]))

    def test_data_binary_report_is_not_duplicated(self) -> None:
        self.tracked("06_RESOURCES/example.rds", "placeholder")
        report = screen.scan(self.root)
        matches = [item for item in report["findings"]
                   if item["path"] == "06_RESOURCES/example.rds"]
        self.assertEqual(len(matches), 1)

    def test_resource_lecture_mapping_requires_review(self) -> None:
        self.tracked("06_RESOURCES/methods.md", "Lecture 3 chunks 10-15")
        self.assertEqual(screen.scan(self.root)["status"], "REVIEW")

    def test_tex_prompt_reproduction_requires_review(self) -> None:
        self.tracked("06_RESOURCES/LaTeX/example.tex",
                     "The prompts below are preserved")
        self.assertEqual(screen.scan(self.root)["status"], "REVIEW")

    def test_generic_resource_remains_clear(self) -> None:
        self.tracked("06_RESOURCES/methods.md", "A generic histogram example")
        self.assertEqual(screen.scan(self.root)["status"], "SCREEN_CLEAR")


if __name__ == "__main__":
    unittest.main()
