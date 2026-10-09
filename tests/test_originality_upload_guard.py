"""Exercise actual local pushes with synthetic sources; no course text embedded."""
import importlib.util
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

    def test_safe_commit_pushes_with_local_hook(self):
        sha = self.commit('Independent example with different wording.')
        self.assertEqual(self.push().returncode, 0)
        remote_sha = subprocess.check_output(['git', '--git-dir', str(self.remote), 'rev-parse', 'main'], text=True).strip()
        self.assertEqual(remote_sha, sha)

    def test_renamed_source_copy_is_blocked(self):
        self.commit(self.text, 'renamed.md')
        result = self.push()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('UPLOAD BLOCKED', result.stderr)
        self.assertNotIn(self.text, result.stderr)

    def test_source_filename_is_blocked_even_after_rewriting(self):
        self.commit('Distinct unrelated content.', 'protected.rmd')
        self.assertNotEqual(self.push().returncode, 0)

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
        self.assertIn('checks unavailable', result.stderr)

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
