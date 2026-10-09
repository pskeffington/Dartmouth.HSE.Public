#!/usr/bin/env python3
"""Regression checks for heuristic originality-screening rules."""
from __future__ import annotations

import importlib.util
import pathlib
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "originality_screen", ROOT / "scripts" / "check_public_originality.py"
)
assert SPEC is not None and SPEC.loader is not None
screen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(screen)


class CourseSignalTests(unittest.TestCase):
    def patterns(self, text: str) -> set[str]:
        return {name for name, pattern in screen.COURSE_SPECIFIC
                if pattern.search(text)}

    def test_detects_lecture_chunk_mapping(self) -> None:
        self.assertIn("lecture chunk mapping", self.patterns("Lecture 3 chunks 10-15"))
        self.assertIn("lecture chunk mapping", self.patterns("Chunks 20–34: plots"))
        self.assertIn("lecture chunk mapping", self.patterns("chunk 17: use plotting"))
        self.assertNotIn("lecture chunk mapping",
                         self.patterns("The code processes data in chunks."))

    def test_detects_assessed_prompt_reproduction(self) -> None:
        self.assertIn("verbatim-prompt indicator",
                      self.patterns("The prompts below are preserved from class"))
        self.assertIn("verbatim-prompt indicator",
                      self.patterns("original assignment questions"))

    def test_detects_assignment_item_mapping(self) -> None:
        self.assertIn("assignment item mapping",
                      self.patterns("Assignment task | Lecture technique"))
        self.assertNotIn("assignment item mapping",
                         self.patterns("General statistics and visualization"))

    def test_rights_notice_severity(self) -> None:
        restriction = dict(screen.RESTRICTED_TEXT)
        review = dict(screen.REVIEW_TEXT)
        self.assertIsNotNone(restriction["explicit rights restriction"].search(
            "All rights reserved"))
        self.assertIsNone(restriction["explicit rights restriction"].search(
            "Please do not share these notes"))
        self.assertFalse(any(p.search("Do not reproduce the source handout")
                             for p in review.values()))
        self.assertFalse(any(p.search(
            "Obtain the instructor-provided code from the authorized course channel")
                             for p in review.values()))
        self.assertTrue(any(p.search(
            "We copied the instructor handout code into this repository")
                            for p in review.values()))
        self.assertTrue(any(p.search(
            "Instructor-provided code was included in the public guide")
                            for p in review.values()))

    def test_release_gate_fails_on_unresolved_review(self) -> None:
        report = {"status": "REVIEW", "tracked_files": 1,
                  "findings": [], "limitations": "manual approval required"}
        with mock.patch.object(screen, "scan", return_value=report):
            with mock.patch("sys.argv", ["check_public_originality.py",
                                         "--json", "--fail-on-review"]):
                with mock.patch("builtins.print"):
                    self.assertEqual(screen.main(), 1)
            with mock.patch("sys.argv", ["check_public_originality.py",
                                         "--json"]):
                with mock.patch("builtins.print"):
                    self.assertEqual(screen.main(), 0)

    def test_policy_paths_outside_course_scope(self) -> None:
        self.assertFalse("PROVENANCE_REGISTER.md".startswith(screen.COURSE_PUBLIC))
        self.assertTrue("02_Lecture_Notes/Week_1.Rmd".startswith(screen.COURSE_PUBLIC))


if __name__ == "__main__":
    unittest.main()
