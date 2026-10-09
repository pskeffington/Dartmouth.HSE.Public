"""Verify provenance coverage and stale-evidence detection using Git fixtures."""
import json
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "inventory", Path(__file__).resolve().parents[1] / "scripts/build_provenance_inventory.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        (self.root / "notes.md").write_text("independent example\n")
        subprocess.run(["git", "add", "notes.md"], cwd=self.root, check=True)

    def register(self, rows):
        (self.root / "PROVENANCE_RECORDS.json").write_text(json.dumps({"entries": rows}))

    def test_missing_records_remain_visible(self):
        report = module.inventory(self.root)
        self.assertEqual(report["record_coverage"]["unrecorded_paths"], ["notes.md"])
        self.assertEqual(report["rights_status"], "UNVERIFIED")

    def test_content_change_invalidates_review_evidence(self):
        digest = hashlib.sha256((self.root / "notes.md").read_bytes()).hexdigest()
        self.register([{"path": "notes.md", "observed_sha256": digest}])
        self.assertEqual(module.inventory(self.root)["entries"][0]["snapshot_evidence"], "current")
        (self.root / "notes.md").write_text("changed example\n")
        report = module.inventory(self.root)
        self.assertEqual(report["entries"][0]["snapshot_evidence"], "stale")
        self.assertEqual(report["rights_status"], "UNVERIFIED")

    def test_duplicate_records_are_rejected(self):
        row = {"path": "notes.md", "observed_sha256": ""}
        self.register([row, row])
        with self.assertRaises(ValueError):
            module.inventory(self.root)

    def test_pending_and_obsolete_records_are_reported(self):
        self.register([{"path": "notes.md", "observed_sha256": ""},
                       {"path": "removed.md", "observed_sha256": ""}])
        report = module.inventory(self.root)
        self.assertEqual(report["entries"][0]["snapshot_evidence"], "pending")
        self.assertEqual(report["record_coverage"]["obsolete_record_paths"], ["removed.md"])


if __name__ == "__main__":
    unittest.main()
