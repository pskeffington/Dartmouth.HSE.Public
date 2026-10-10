"""Synthetic failure cases for public teaching content and evidence boundaries."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import gene_companion_content as content
import build_gene_companion as builder
import validate_gene_companion as validator


class ContentContracts(unittest.TestCase):
    def errors(self, genes=None, studies=None):
        return validator.validate_content(genes if genes is not None else content.GENES,
            studies if studies is not None else content.STUDIES)

    def test_current_catalog(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(validator.validate_tree(ROOT), [])

    def test_missing_original_gene(self):
        genes = [g for g in content.GENES if g['symbol'] != 'ESR1']
        self.assertTrue(any('Original 21' in x for x in self.errors(genes)))

    def test_duplicate_identity(self):
        genes = copy.deepcopy(content.GENES)
        genes[1]['entrez_id'] = genes[0]['entrez_id']
        self.assertTrue(any('duplicate primary' in x for x in self.errors(genes)))

    def test_changed_but_well_formed_identity(self):
        genes = copy.deepcopy(content.GENES); genes[0]['hgnc_id'] = 'HGNC:999999'
        self.assertTrue(any('snapshot differs' in x for x in self.errors(genes)))

    def test_withdrawn_symbol_and_alias_cannot_replace_identity(self):
        genes = copy.deepcopy(content.GENES)
        genes[0]['status'] = 'Withdrawn'; genes[0]['symbol'] = 'PKB'
        self.assertTrue(any('not verified/approved' in x for x in self.errors(genes)))
        self.assertTrue(any('snapshot differs' in x for x in self.errors(genes)))

    def test_unsupported_evidence_promotion(self):
        studies = copy.deepcopy(content.STUDIES)
        studies[content.GENES[0]['study']]['status'] = 'PRIMARY_EVIDENCE_VERIFIED'
        self.assertTrue(any('exceeds this edition' in x for x in self.errors(studies=studies)))

    def test_shared_reference_cannot_be_promoted(self):
        studies = copy.deepcopy(content.STUDIES)
        studies["WU"]["status"] = "PRIMARY_EVIDENCE_VERIFIED"
        self.assertTrue(any("shared reference review" in x for x in self.errors(studies=studies)))

    def test_incomplete_reference_or_domain(self):
        genes = copy.deepcopy(content.GENES); genes[0]['domains'] = ['imaginary']
        genes[1]['study'] = 'missing'
        self.assertTrue(any('unknown domain' in x for x in self.errors(genes)))
        self.assertTrue(any('reference missing' in x for x in self.errors(genes)))

    def make_tree(self, root):
        for relative, text in builder.render_outputs().items():
            path = root/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text)
        figure = root/builder.BASE/'FIGURES'/'README.md'
        figure.parent.mkdir(parents=True)
        figure.write_text((ROOT/builder.BASE/'FIGURES'/'README.md').read_text())

    def test_incomplete_card_and_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            (root/builder.BASE/'GENE_CARDS'/'ESR1.md').write_text('# ESR1\n')
            (root/builder.BASE/'GENE_ATLAS_INDEX.md').write_text('# Index\n')
            errors = validator.validate_tree(root)
            self.assertTrue(any('required A–I' in x for x in errors))
            self.assertTrue(any('GENE_ATLAS_INDEX' in x for x in errors))

    def test_unexpected_card_and_unlabeled_figure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            (root/builder.BASE/'GENE_CARDS'/'PKB.md').write_text('# PKB\n')
            figure = root/builder.BASE/'FIGURES'/'README.md'
            figure.write_text(figure.read_text().replace('**Inputs:**','Inputs:').replace('zero-centered','uncentered'))
            errors = validator.validate_tree(root)
            self.assertTrue(any('filenames' in x for x in errors))
            self.assertTrue(any('caption, inputs' in x for x in errors))
            self.assertTrue(any('zero-centered' in x for x in errors))

    def test_participant_like_label_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/builder.BASE/'GENE_CARDS'/'ESR1.md'
            path.write_text(path.read_text() + '\nTCGA-ZZ-0000\n')
            self.assertTrue(any('participant-like' in x for x in validator.validate_tree(root)))


if __name__ == '__main__':
    unittest.main()
