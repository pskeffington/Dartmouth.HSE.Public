#!/usr/bin/env python3
"""Regression checks for heuristic originality-screening rules."""
from __future__ import annotations

import importlib.util
import pathlib
import unittest

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

    def test_policy_paths_outside_course_scope(self) -> None:
        self.assertFalse("PROVENANCE_REGISTER.md".startswith(screen.COURSE_PUBLIC))
        self.assertTrue("02_Lecture_Notes/Week_1.Rmd".startswith(screen.COURSE_PUBLIC))


if __name__ == "__main__":
    unittest.main()
