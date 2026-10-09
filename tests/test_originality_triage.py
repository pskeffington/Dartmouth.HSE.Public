#!/usr/bin/env python3
"""Validate that originality findings become a neutral, unresolved review queue."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "originality_triage", ROOT / "scripts" / "build_originality_triage.py"
)
assert SPEC and SPEC.loader
triage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(triage)

class TriageTests(unittest.TestCase):
    def test_open_review_is_never_marked_cleared(self):
        report = {
            "status": "REVIEW", "tracked_files": 2,
            "findings": [{"path": "notes.md", "level": "review",
                          "reason": "source verification"}],
        }
        page = triage.render(report)
        self.assertIn("notes.md", page)
        self.assertIn("Disposition: **HOLD**", page)
        self.assertIn("Human reviewer / date: **PENDING**", page)
        self.assertNotIn("Disposition: **CLEARED**", page)

    def test_blocked_findings_are_counted(self):
        report = {
            "status": "BLOCK", "tracked_files": 1,
            "findings": [{"path": "restricted.txt", "level": "block",
                          "reason": "explicit rights restriction"}],
        }
        self.assertIn("(1 block, 0 review)", triage.render(report))

    def test_empty_screen_is_not_a_rights_certification(self):
        page = triage.render({"status": "SCREEN_CLEAR", "tracked_files": 0,
                              "findings": []})
        self.assertIn("Manual provenance", page)
        self.assertNotIn("Disposition: **CLEARED**", page)

    def test_invalid_input_fails_closed(self):
        with self.assertRaises(ValueError):
            triage.render({"status": "APPROVED", "findings": []})
        with self.assertRaises(ValueError):
            triage.render({"status": "REVIEW", "findings": [{}]})

if __name__ == "__main__":
    unittest.main()
