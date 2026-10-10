"""Exercise actual local pushes with synthetic sources; no course text embedded."""
import importlib.util
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


guard = load('check_source_upload')
installer = load('install_source_upload_guard')


class UploadGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base / 'public'
        self.sources = base / 'private'
        self.remote = base / 'remote.git'
        self.root.mkdir(); self.sources.mkdir()
        self.text = ' '.join(f'guard_synthetic_{n}' for n in range(35))
        (self.sources / 'protected.rmd').write_text(self.text)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        subprocess.run(['git', 'init', '--bare', '-q', str(self.remote)], check=True)
        self.git('remote', 'add', 'origin', str(self.remote))
        installer.install(self.root, [self.sources])

    def git(self, *args, check=True):
        return subprocess.run(['git', *args], cwd=self.root, capture_output=True,
                              text=True, check=check)

    def commit(self, text, name='notes.md'):
        (self.root / name).write_text(text)
        self.git('add', name)
        self.git('commit', '-qm', 'synthetic fixture')
        return self.git('rev-parse', 'HEAD').stdout.strip()

    def push(self):
        return self.git('push', 'origin', 'HEAD:refs/heads/main', check=False)

    def review(self, name, origin='independent', **extra):
        p = self.root / '.git/source-rights-reviews.json'
        records = json.loads(p.read_text()) if p.exists() else {'entries': {}}
        records['entries'][name] = {'sha256': hashlib.sha256((self.root / name).read_bytes()).hexdigest(),
            'origin': origin, 'decision': 'ALLOW', 'reviewer': 'Fixture author',
            'reviewed_on': '2026-10-10', 'evidence': 'Constructed in this synthetic test',
            'input_scope': 'Synthetic fixtures only', **extra}
        p.write_text(json.dumps(records))

    def evidence(self):
        return {'method': 'Authored the explanation independently from an invented example and verified its counts with a fresh script.',
                'inputs': [{'kind': 'own-work', 'reference': 'New invented specimen example composed in this test',
                            'use': 'independently-written'}]}

    def record_original(self, *names, evidence=None, category='documentation'):
        path = Path(self.tmp.name) / 'authoring-evidence.json'
        path.write_text(json.dumps(self.evidence() if evidence is None else evidence))
        return subprocess.run(['python3', str(SCRIPTS / 'record_original_work.py'), '--category', category,
                               '--evidence', str(path), *names], cwd=self.root, capture_output=True, text=True)

    def manifest(self, name, evidence=None, category='documentation'):
        evidence = self.evidence() if evidence is None else evidence
        entry = {'path': name, 'sha256': hashlib.sha256((self.root / name).read_bytes()).hexdigest(),
                 'source_category': category, 'author': 'Fixture contributor', 'recorded_on': '2026-10-10',
                 'authoring_evidence': evidence,
                 'evidence_sha256': hashlib.sha256(json.dumps(evidence, sort_keys=True).encode()).hexdigest()}
        (self.root / '.git/original-work-manifest.json').write_text(json.dumps(
            {'schema': 'original-work-v1', 'entries': {name: [entry]}}))

    def test_original_markdown_publishes_without_manual_rights_record(self):
        self.commit('# Specimen counting\nReport observed and absent measurements separately.')
        result = self.record_original('notes.md')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.root / '.git/source-rights-reviews.json').exists())
        payload = json.loads((self.root / '.git/original-work-manifest.json').read_text())
        entry = payload['entries']['notes.md'][0]
        self.assertEqual(entry['source_category'], 'documentation')
        self.assertEqual(entry['path'], 'notes.md')
        self.assertEqual(guard.origin.verified_original_work((self.root/'notes.md').read_bytes(), 'notes.md', payload), entry)
        self.assertEqual(self.push().returncode, 0)

    def test_original_revision_refreshes_automatically_without_human_approval(self):
        self.commit('New explanation about plotting observed specimen counts.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.assertEqual(self.push().returncode, 0)
        self.commit('Revised explanation about units and observed specimen counts.')
        self.assertNotEqual(self.push().returncode, 0)  # stale digest is not inherited
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.assertEqual(self.push().returncode, 0)

    def test_original_manifest_retains_new_intermediate_versions(self):
        self.commit('Original draft of a unitful synthetic summary.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.commit('Revised original draft of a unitful synthetic summary.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.assertEqual(self.push().returncode, 0)

    def test_original_academic_folder_and_source_name_are_not_conclusive(self):
        name = '02_Lecture_Notes/protected.rmd'
        (self.root / name).parent.mkdir()
        self.commit('An independent explanation of invented participant summaries.', name)
        self.assertEqual(self.record_original(name).returncode, 0)
        self.assertEqual(self.push().returncode, 0)

    def test_original_rename_needs_automated_path_binding_not_human_review(self):
        self.commit('An original specimen-counting explanation.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.assertEqual(self.push().returncode, 0)
        self.git('mv', 'notes.md', 'new.md'); self.git('commit', '-qm', 'rename')
        self.assertNotEqual(self.push().returncode, 0)
        self.assertEqual(self.record_original('new.md').returncode, 0)
        self.assertEqual(self.push().returncode, 0)

    def test_declaration_only_is_not_authoring_evidence(self):
        self.commit('Unattributed original-looking words.')
        self.assertNotEqual(self.record_original('notes.md', evidence={'original': True}).returncode, 0)
        self.manifest('notes.md', evidence={'original': True})
        self.assertNotEqual(self.push().returncode, 0)

    def test_original_manifest_never_overrides_exact_or_embedded_copy(self):
        for content in (self.text, 'An invented introduction. ' + self.text.upper().replace(' ', ', ') + ' Ending.'):
            with self.subTest(content=content[:20]):
                self.commit(content)
                self.manifest('notes.md')
                self.assertNotEqual(self.record_original('notes.md').returncode, 0)
                self.assertNotEqual(self.push().returncode, 0)

    def test_original_similarity_still_requires_review(self):
        words = [f'distinctive{i}' for i in range(60)]
        (self.sources / 'instruction.txt').write_text(' '.join(words))
        self.commit(' '.join(word for i in range(0, 60, 4) for word in reversed(words[i:i+4])))
        self.manifest('notes.md')
        self.assertNotEqual(self.record_original('notes.md').returncode, 0)
        self.assertNotEqual(self.push().returncode, 0)

    def test_original_pathway_rejects_license_uncertainty_and_restrictions(self):
        for content in ('License' + ': unknown', 'All rights ' + 'reserved'):
            with self.subTest(content=content):
                self.commit(content)
                self.manifest('notes.md')
                self.assertNotEqual(self.record_original('notes.md').returncode, 0)
                self.assertNotEqual(self.push().returncode, 0)

    def test_contradictory_license_or_review_record_cannot_be_relabelled_original(self):
        self.commit('An external explanation of unrelated concepts.')
        self.manifest('notes.md')
        self.review('notes.md', origin='licensed')  # license missing
        self.assertNotEqual(self.push().returncode, 0)
        self.review('notes.md', decision='REVIEW')
        self.assertNotEqual(self.push().returncode, 0)

    def test_protected_or_reused_authoring_inputs_need_review(self):
        self.commit('Independent-looking summary.')
        evidence = self.evidence()
        evidence['inputs'][0]['reference'] = str(self.sources / 'protected.rmd')
        self.manifest('notes.md', evidence)
        self.assertNotEqual(self.record_original('notes.md', evidence=evidence).returncode, 0)
        self.assertNotEqual(self.push().returncode, 0)
        evidence['inputs'][0] = {'kind': 'public-concept-reference', 'reference': 'https://example.invalid', 'use': 'reproduced'}
        self.assertNotEqual(self.record_original('notes.md', evidence=evidence).returncode, 0)

    def test_original_missing_live_corpus_is_not_a_proof_of_independence(self):
        self.commit('Original explanation with documented inputs.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        (self.sources / 'protected.rmd').unlink(); self.sources.rmdir()
        self.assertNotEqual(self.push().returncode, 0)
        (self.root / '.git/source-protection-inventory.json').unlink()
        self.assertNotEqual(self.push().returncode, 0)

    def test_original_metadata_does_not_hide_protected_intermediate_commit(self):
        self.commit(self.text)
        self.commit('New independent replacement with an authoring record.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        self.assertNotEqual(self.push().returncode, 0)

    def test_original_media_and_symlink_manifest_remain_blocked(self):
        self.commit('<svg>unverified external figure</svg>', 'figure.svg')
        self.manifest('figure.svg')
        self.assertNotEqual(self.push().returncode, 0)
        self.assertNotEqual(self.record_original('figure.svg').returncode, 0)
        p = self.root / '.git/original-work-manifest.json'
        p.unlink(); p.symlink_to(Path(self.tmp.name)/'untrusted.json')
        self.assertNotEqual(self.push().returncode, 0)

    def test_batch_recording_is_atomic_and_preserves_existing_manifest(self):
        self.commit('Original baseline document.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        p = self.root / '.git/original-work-manifest.json'
        before = p.read_bytes()
        self.commit('Another independently composed explanation.', 'safe.md')
        self.commit(self.text, 'copy.md')
        self.assertNotEqual(self.record_original('safe.md', 'copy.md').returncode, 0)
        self.assertEqual(p.read_bytes(), before)

    def test_original_software_and_documented_synthetic_example(self):
        self.commit('hse_count <- function(x) sum(!is.na(x))', 'count.R')
        self.assertEqual(self.record_original('count.R', category='research-software').returncode, 0)
        self.commit('Specimen,Value\nInvented01,2.5\n', 'synthetic.csv')
        self.assertNotEqual(self.record_original('synthetic.csv', category='synthetic-example').returncode, 0)
        evidence = self.evidence()
        evidence['inputs'].append({'kind': 'synthetic-generation', 'reference': 'Invented01 and 2.5 constructed directly for this test', 'use': 'simulated-data'})
        self.assertEqual(self.record_original('synthetic.csv', evidence=evidence, category='synthetic-example').returncode, 0)
        self.assertEqual(self.push().returncode, 0)

    def test_previous_manifest_record_cannot_mask_contradictory_evidence(self):
        self.commit('An independent explanation with an authoring record.')
        self.assertEqual(self.record_original('notes.md').returncode, 0)
        p = self.root / '.git/original-work-manifest.json'
        payload = json.loads(p.read_text())
        conflict = self.evidence()
        conflict['inputs'][0]['reference'] = str(self.sources / 'protected.rmd')
        self.assertNotEqual(self.record_original('notes.md', evidence=conflict).returncode, 0)
        second = dict(payload['entries']['notes.md'][0])
        second['authoring_evidence'] = conflict
        second['evidence_sha256'] = hashlib.sha256(json.dumps(conflict, sort_keys=True).encode()).hexdigest()
        payload['entries']['notes.md'].append(second)
        p.write_text(json.dumps(payload))
        self.assertNotEqual(self.push().returncode, 0)

    def test_tampered_evidence_digest_and_non_utf8_cannot_use_original_path(self):
        self.commit('A new original explanation.')
        self.manifest('notes.md')
        p = self.root / '.git/original-work-manifest.json'
        payload = json.loads(p.read_text())
        payload['entries']['notes.md'][0]['evidence_sha256'] = '0' * 64
        p.write_text(json.dumps(payload))
        self.assertNotEqual(self.push().returncode, 0)
        (self.root / 'notes.md').write_bytes(b'opaque invalid text \xff')
        self.git('add', 'notes.md'); self.git('commit', '-qm', 'invalid encoding')
        self.manifest('notes.md')
        self.assertNotEqual(self.push().returncode, 0)

    def test_human_verified_independent_work_uses_private_signatures_without_live_corpus(self):
        self.commit('Human-reviewed original utility with no classroom source input.')
        self.review('notes.md', reviewer_kind='human', corpus_independent_review=True)
        (self.sources / 'protected.rmd').unlink(); self.sources.rmdir()
        self.assertEqual(self.push().returncode, 0)

    def test_changed_inventory_scope_is_not_exempt(self):
        self.commit('Human-reviewed original explanation.')
        self.review('notes.md', reviewer_kind='human', corpus_independent_review=True)
        saved = self.root / '.git/source-protection-inventory.json'
        data = json.loads(saved.read_text()); data['source_dirs'] = ['/unrelated/private']
        saved.write_text(json.dumps(data))
        (self.sources / 'protected.rmd').unlink(); self.sources.rmdir()
        self.assertNotEqual(self.push().returncode, 0)

    def test_missing_signature_inventory_is_not_exempt(self):
        self.commit('Human-reviewed original explanation.')
        self.review('notes.md', reviewer_kind='human', corpus_independent_review=True)
        (self.sources / 'protected.rmd').unlink(); self.sources.rmdir()
        (self.root / '.git/source-protection-inventory.json').unlink()
        self.assertNotEqual(self.push().returncode, 0)

    def test_independent_exception_does_not_override_cached_source_match(self):
        self.commit(self.text)
        self.review('notes.md', reviewer_kind='human', corpus_independent_review=True)
        (self.sources / 'protected.rmd').unlink(); self.sources.rmdir()
        self.assertNotEqual(self.push().returncode, 0)

    def test_already_uploaded_ancestry_is_not_reintroduced_on_another_branch(self):
        self.commit('Original baseline A.'); self.review('notes.md')
        self.assertEqual(self.push().returncode, 0)
        self.assertEqual(self.git('push', 'origin', 'HEAD:refs/heads/feature', check=False).returncode, 0)
        self.commit('Original intermediate C.'); self.review('notes.md')
        self.assertEqual(self.push().returncode, 0)
        self.commit('Original current B.'); self.review('notes.md')
        self.assertEqual(self.push().returncode, 0)
        # The path-bound register now contains B only. C is known remote history,
        # not a newly exposed blob; final B remains checked on the feature push.
        self.assertEqual(self.git('push', 'origin', 'HEAD:refs/heads/feature', check=False).returncode, 0)

    def test_unknown_provenance_fails_closed(self):
        self.commit('Unattributed independent-looking text.')
        self.assertNotEqual(self.push().returncode, 0)

    def test_original_flag_cannot_override_detected_copy(self):
        self.commit(self.text)
        self.review('notes.md', original=True)
        self.assertNotEqual(self.push().returncode, 0)

    def test_rewritten_modified_file_invalidates_review(self):
        self.commit('Initial reviewed original function.')
        self.review('notes.md'); self.assertEqual(self.push().returncode, 0)
        self.commit('Changed original function needing a new origin review.')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('notes.md'); self.assertEqual(self.push().returncode, 0)

    def test_renamed_file_needs_path_bound_review(self):
        self.commit('Reviewed original explanation.')
        self.review('notes.md'); self.assertEqual(self.push().returncode, 0)
        self.git('mv', 'notes.md', 'renamed.md'); self.git('commit', '-qm', 'rename')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('renamed.md'); self.assertEqual(self.push().returncode, 0)

    def test_licensed_external_text_needs_license_evidence(self):
        self.commit('A small synthetic external example with permission.')
        self.review('notes.md', origin='licensed')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('notes.md', origin='licensed', license='MIT',
                    license_reference='https://example.invalid/LICENSE', permission_scope='Redistribution with attribution')
        self.assertEqual(self.push().returncode, 0)

    def test_unverified_figure_requires_human_rights_review(self):
        self.commit('<svg>synthetic figure</svg>', 'figure.svg')
        self.review('figure.svg')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('figure.svg', rights_review=True, reviewer_kind='human')
        self.assertEqual(self.push().returncode, 0)

    def test_embedded_normalized_source_passage_is_blocked(self):
        self.commit('Original prefix. ' + self.text.upper().replace(' ', ', ') + ' Original ending.')
        self.review('notes.md'); self.assertNotEqual(self.push().returncode, 0)

    def test_independent_biomedical_code_and_synthetic_data_are_allowed(self):
        for name, content in [('02_Lecture_Notes/original.R', 'hse_mean <- function(x) mean(x, na.rm = TRUE)'),
                              ('synthetic.csv', 'Participant,Measurement\nToy01,1.2\n'),
                              ('explanation.md', 'Report the number of measured participants alongside a mean.')]:
            (self.root / name).parent.mkdir(parents=True, exist_ok=True)
            self.commit(content, name); self.review(name)
        self.assertEqual(self.push().returncode, 0)

    def test_close_reworded_overlap_requires_human_review(self):
        words = [f'distinctive{i}' for i in range(60)]
        (self.sources / 'instruction.txt').write_text(' '.join(words))
        # Reorder short clauses: no contiguous 20-token sequence survives.
        changed = [word for i in range(0, 60, 4) for word in reversed(words[i:i+4])]
        self.commit(' '.join(changed)); self.review('notes.md')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('notes.md', rights_review=True, reviewer_kind='human',
                    evidence='Synthetic adjudication of permitted wording overlap')
        self.assertEqual(self.push().returncode, 0)

    def test_safe_commit_pushes_with_local_hook(self):
        sha = self.commit('Independent example with different wording.')
        self.review('notes.md')
        self.assertEqual(self.push().returncode, 0)
        remote_sha = subprocess.check_output(['git', '--git-dir', str(self.remote), 'rev-parse', 'main'], text=True).strip()
        self.assertEqual(remote_sha, sha)

    def test_renamed_source_copy_is_blocked(self):
        self.commit(self.text, 'renamed.md')
        result = self.push()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('UPLOAD BLOCKED', result.stderr)
        self.assertNotIn(self.text, result.stderr)

    def test_source_filename_requires_review_not_conclusive_block(self):
        self.commit('Distinct unrelated content.', 'protected.rmd')
        self.assertNotEqual(self.push().returncode, 0)
        self.review('protected.rmd')
        self.assertEqual(self.push().returncode, 0)

    def test_committed_source_is_blocked_despite_clean_working_copy(self):
        self.commit(self.text)
        (self.root / 'notes.md').write_text('Uncommitted independent replacement.')
        self.assertNotEqual(self.push().returncode, 0)

    def test_deleted_intermediate_source_is_still_blocked(self):
        self.commit(self.text)
        self.commit('Independent replacement.')
        self.assertNotEqual(self.push().returncode, 0)

    def test_missing_corpus_blocks_push(self):
        self.commit('Independent content.')
        (self.sources / 'protected.rmd').unlink()
        self.sources.rmdir()
        result = self.push()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('UPLOAD BLOCKED', result.stderr)

    def test_custom_hook_is_not_overwritten(self):
        hook = self.root / '.git/hooks/pre-push'
        hook.write_text('# existing custom hook\n')
        with self.assertRaises(ValueError):
            installer.install(self.root, [self.sources])
        self.assertEqual(hook.read_text(), '# existing custom hook\n')

    def test_missing_one_of_multiple_source_folders_is_not_ignored(self):
        with self.assertRaises(ValueError):
            guard.load_corpus(self.root.resolve(), [self.sources, self.sources / 'absent'])


if __name__ == '__main__':
    unittest.main()
