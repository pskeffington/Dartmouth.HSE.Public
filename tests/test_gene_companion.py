"""Synthetic failure cases for public teaching content and evidence boundaries."""
import copy
import shutil
import re
from urllib.parse import urlsplit
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
        shutil.copytree(ROOT/builder.BASE, root/builder.BASE)
        for filename in ('README.md','06_RESOURCES/README.md'):
            path = root/filename; path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/filename,path)
        for name in validator.EDITORIAL_SOURCE_SEALS:
            path = root/'scripts'/name; path.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/'scripts'/name,path)
        for source in (ROOT/builder.BASE).rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',source.read_text()):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                original = (source.parent/url.path).resolve()
                if original.is_dir():
                    original = original/'README.md'
                if original.is_file() and original.is_relative_to(ROOT):
                    destination = root/original.relative_to(ROOT)
                    destination.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(original,destination)
        for relative, text in builder.render_outputs().items():
            path = root/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text)

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

    def test_complete_synthetic_tree_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);self.make_tree(root)
            self.assertEqual(validator.validate_tree(root),[])

    def mutate_guide(self, old, new):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/validator.editorial.CANONICAL
            self.assertIn(old,path.read_text())
            path.write_text(path.read_text().replace(old,new,1))
            return validator.validate_guide(root)

    def test_twelve_chapters_in_order(self):
        self.assertTrue(any('instructional order' in e for e in self.mutate_guide(
            '## Chapter 1: The People Behind the Numbers','## Chapter 99: Changed')))

    def test_changed_gene_anchor(self):
        self.assertTrue(any('anchor' in e for e in self.mutate_guide('#### ESR1','#### RenamedESR1')))

    def test_duplicate_integrated_gene(self):
        self.assertTrue(any('60 distinct' in e for e in self.mutate_guide('#### ESR1','#### PGR')))

    def test_missing_alphabetical_link(self):
        self.assertTrue(any('gene jump' in e for e in self.mutate_guide('| [ESR1](#esr1) |','| ESR1 |')))

    def test_short_profile_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/validator.editorial.CANONICAL
            path.write_text(re.sub(r'(#### ESR1\n\n).*?(?=\n###)',r'\1Short.\n',path.read_text(),flags=re.S))
            self.assertTrue(any('Substantive profile' in e for e in validator.validate_guide(root)))

    def test_adjacent_chapter_failure(self):
        self.assertTrue(any('adjacent' in e for e in self.mutate_guide(
            '[Next chapter](#chapter-2-understanding-the-breast-cancer-dataset)',
            '[Next chapter](#chapter-3-how-researchers-measure-genes)')))

    def test_route_failure(self):
        self.assertTrue(any('Learning route' in e for e in self.mutate_guide('**Beginner:**','**Unspecified:**')))

    def test_nested_figure_link_failure(self):
        self.assertTrue(any('Broken supporting' in e for e in self.mutate_guide(
            '](FIGURES/gene_companion_heatmap.R)','](gene_companion_heatmap.R)')))

    def test_missing_or_renamed_card(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/builder.BASE/'GENE_CARDS/ESR1.md'
            path.rename(path.with_name('RENAMED.md'))
            errors = validator.validate_tree(root)
            self.assertTrue(any('filenames' in e for e in errors))
            self.assertTrue(any('Broken supporting' in e for e in errors))

    def test_root_has_only_one_canonical_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/'README.md';path.write_text(path.read_text()+
                '\n[Another start](06_RESOURCES/Genomics/COMMON_BREAST_CANCER_GENE_DESCRIPTORS.md)\n')
            self.assertTrue(any('Competing root' in e for e in validator.validate_guide(root)))

    def test_resource_canonical_link_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/'06_RESOURCES/README.md';path.write_text('# Resources\n')
            self.assertTrue(any('one labeled' in e for e in validator.validate_guide(root)))

    def test_supporting_backlink_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/builder.BASE/'REFERENCES/ANNOTATION_SOURCE_REGISTER.md'
            path.write_text(path.read_text().replace('BREAST_CANCER_60_GENE_COMPANION.md','REMOVED.md'))
            self.assertTrue(any('backlink' in e for e in validator.validate_guide(root)))

    def test_editorial_seal_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.make_tree(root)
            path = root/'scripts/gene_companion_chapters.py';path.write_text(path.read_text()+'\n# altered\n')
            self.assertTrue(any('seal differs' in e for e in validator.validate_guide(root)))

    def test_editorial_version_failure(self):
        from unittest.mock import patch
        with patch.object(validator.editorial,'EDITORIAL_VERSION','UNAPPROVED'):
            self.assertTrue(any('version not accepted' in e for e in validator.validate_guide(ROOT)))

    def test_deterministic_and_read_only_check(self):
        import subprocess
        import hashlib
        before = {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in builder.render_outputs()}
        self.assertEqual(builder.render_outputs(),builder.render_outputs())
        subprocess.run([sys.executable,str(ROOT/'scripts/build_gene_companion.py'),'--check'],check=True,capture_output=True)
        after = {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in builder.render_outputs()}
        self.assertEqual(before,after)

    def test_stale_generated_guide_detected(self):
        self.assertTrue(any('nonreproducible' in e for e in self.mutate_generated_guide()))

    def mutate_generated_guide(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);self.make_tree(root)
            path=root/validator.editorial.CANONICAL;path.write_text(path.read_text()+'\nChanged prose.\n')
            return validator.validate_tree(root)


if __name__ == '__main__':
    unittest.main()
