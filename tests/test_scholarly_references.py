"""Synthetic bibliography fixtures; no external publications or source passages."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("scholarly", Path(__file__).parents[1] / "scripts/audit_scholarly_references.py")
scholarly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scholarly)


class ScholarlyReferenceTests(unittest.TestCase):
    def test_case_encoding_balanced_parentheses_and_duplicate_links(self):
        text = "[study](https://doi.org/10.1234/ABC%28x%29). DOI: 10.1234/abc(x); "
        text += "https://publisher.example/doi/10.1234/ABC(x)?tracking=1 "
        dois, _, linked, malformed = scholarly.identifiers(text)
        self.assertEqual(dois, ["10.1234/abc(x)"])
        self.assertEqual(linked, dois)
        self.assertEqual(malformed, [])

    def test_unicode_suffix_and_malformed_citation_are_not_silently_lost(self):
        dois, _, _, malformed = scholarly.identifiers("10.1234/café. 10.nope/x 10.1234/")
        self.assertEqual(dois, ["10.1234/café"])
        self.assertEqual(malformed, ["10.1234/", "10.nope/x"])
        self.assertEqual(scholarly.identifiers("REVIEW_2026-10-10.md")[3], [])

    def test_pubmed_without_trailing_slash_labels_and_duplicates(self):
        text = "https://pubmed.ncbi.nlm.nih.gov/12345678 PMID: 12345678; "
        text += "https://pubmed.ncbi.nlm.nih.gov/12345678/?view=1 PMID 87654321"
        self.assertEqual(scholarly.identifiers(text)[1], ["12345678", "87654321"])

    def test_publisher_full_text_routes_are_not_doi_suffixes(self):
        text = "https://www.frontiersin.org/articles/10.1234/fixture/full "
        text += "https://www.medrxiv.org/content/10.1234/draftv1.full"
        self.assertEqual(scholarly.identifiers(text)[0], ["10.1234/draftv1", "10.1234/fixture"])

    def test_missing_and_unavailable_evidence_remains_review_required(self):
        missing = scholarly.reference_state("doi", "10.1234/fixture", {})
        self.assertEqual(missing["identifier_status"], "REVIEW_REQUIRED")
        evidence = self.evidence(lookup_status="UNAVAILABLE")
        state = scholarly.reference_state("doi", "10.1234/fixture", evidence)
        self.assertEqual(state["metadata_status"], "REVIEW_REQUIRED")
        self.assertEqual(state["lookup_status"], "UNAVAILABLE")

    @staticmethod
    def evidence(**changes):
        item = {"identifier": "10.1234/fixture", "authority": "Crossref",
                "source_url": "https://api.crossref.org/works/10.1234%2Ffixture",
                "retrieved_utc": "2026-10-11T00:00:00+00:00", "lookup_status": "FOUND",
                "title": "Invented fixture title", "authors": ["Synthetic Author"],
                "year": 2020, "venue": "Invented Fixture Journal",
                "publication_notices": [{"type": "correction", "identifier": "10.1234/notice"}]}
        item.update(changes)
        return {"doi:10.1234/fixture": item}

    def test_metadata_cannot_promote_claim_support_or_methods(self):
        state = scholarly.reference_state("doi", "10.1234/fixture", self.evidence())
        self.assertEqual(state["identifier_status"], "IDENTIFIER_VERIFIED")
        self.assertEqual(state["metadata_status"], "METADATA_VERIFIED")
        self.assertEqual(state["claim_support_status"], "REVIEW_REQUIRED")
        self.assertEqual(state["methods_status"], "REVIEW_REQUIRED")
        self.assertEqual(state["publication_notices"][0]["type"], "correction")
        retraction = self.evidence(publication_notices=[{"type": "retraction"}])
        self.assertEqual(scholarly.reference_state("doi", "10.1234/fixture", retraction)["publication_notices"], [{"type": "retraction"}])

    def test_wrong_identifier_or_authority_and_incomplete_metadata(self):
        for changes in ({"identifier": "10.1234/other"}, {"authority": "Unknown"},
                        {"source_url": "https://untrusted.example/record"}):
            state = scholarly.reference_state("doi", "10.1234/fixture", self.evidence(**changes))
            self.assertEqual(state["identifier_status"], "REVIEW_REQUIRED")
        state = scholarly.reference_state("doi", "10.1234/fixture", self.evidence(authors=[]))
        self.assertEqual(state["identifier_status"], "IDENTIFIER_VERIFIED")
        self.assertEqual(state["metadata_status"], "REVIEW_REQUIRED")

    def test_structural_gene_card_checks_and_labels_remain_independent(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            card = root / "06_RESOURCES/Genomics/GENE_CARDS/fixture.md"
            card.parent.mkdir(parents=True)
            card.write_text("NOT_FULL_TEXT_REVIEWED 10.nope/x", encoding="utf-8")
            report = scholarly.audit(root)
            self.assertEqual(report["counts"]["errors"], 2)
            self.assertTrue(any(f["rule"] == "MALFORMED_DOI" for f in report["findings"]))
            card.write_text("ABSTRACT_ONLY https://doi.org/10.1234/fixture PMID: 12345678", encoding="utf-8")
            report = scholarly.audit(root)
            self.assertEqual(report["counts"]["errors"], 0)
            self.assertEqual(report["documents"][0]["references"][0]["claim_support_status"], "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
