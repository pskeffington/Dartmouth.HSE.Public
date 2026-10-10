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
