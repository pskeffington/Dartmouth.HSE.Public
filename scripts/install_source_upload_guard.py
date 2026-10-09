#!/usr/bin/env python3
"""Install a checkout-local pre-push source guard; never persist sources in Git."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def install(root, directories):
    root = root.resolve()
    base = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('upload_guard', base / 'check_source_upload.py')
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    # Validate all inputs before changing configuration.
    guard.load_corpus(root, directories)
    existing = subprocess.run(['git', 'config', '--get', 'core.hooksPath'], cwd=root, capture_output=True, text=True)
    if existing.returncode == 0:
        raise ValueError('Custom hooksPath exists; integrate the guard without replacing it')
    git_dir = Path(subprocess.check_output(['git', 'rev-parse', '--absolute-git-dir'], cwd=root, text=True).strip())
    hooks = git_dir / 'hooks'
    hook = hooks / 'pre-push'
    marker = '# private-source-upload-guard-v1'
    if hook.exists() and marker not in hook.read_text():
        raise ValueError('An existing pre-push hook must be integrated, not overwritten')
    target = git_dir / 'private-source-guard'
    target.mkdir(exist_ok=True)
    hooks.mkdir(exist_ok=True)
    for name in ('check_source_upload.py', 'compare_private_sources.py'):
        shutil.copyfile(base / name, target / name)
    config = git_dir / 'private-source-guard.json'
    config.write_text(json.dumps({'source_dirs': [str(Path(p).resolve()) for p in directories]}, indent=2) + '\n')
    config.chmod(0o600)
    # Python launcher avoids shell escaping of the interpreter and private paths.
    hook.write_text('#!/usr/bin/env python3\n' + marker + '\nimport os\nimport sys\nos.execv(' + repr(sys.executable) + ', [' + repr(sys.executable) + ', ' + repr(str(target / 'check_source_upload.py')) + '] + sys.argv[1:])\n')
    hook.chmod(0o700)
    return hook


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--private-source-dir', type=Path, action='append', required=True)
    args = parser.parse_args()
    root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
    try:
        install(root, args.private_source_dir)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Guard installation failed: {exc}\n')
    print('Installed checkout-local pre-push guard. Corpus configuration remains outside tracked files.')


if __name__ == '__main__':
    main()
