# Bash Programming and Basic Operations — Literature Review

Updated: 2026-10-08. Scope: foundational Bash operations, reliable research scripting, and command-line genomics preprocessing. This is an educational synthesis, not a systematic review.

## Evidence matrix

| ID | Reference | Type | Direct contribution | Application | Caution |
|---|---|---|---|---|---|
| BASH-001 | [GNU Bash Reference Manual, v5.3](https://www.gnu.org/software/bash/manual/bash.html) | Primary language specification | Shell syntax, functions, expansion, loops, builtins, redirections, exit status | Authoritative basis for operation examples | macOS system Bash may be 3.2; check `bash --version` |
| BASH-002 | [GNU Bash: Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) | Primary language specification | Order of parameter expansion, word splitting, globbing and quoting | Protect filenames and arguments against unexpected splitting | Unquoted expansions can silently change argument counts |
| BASH-003 | [GNU Bash: The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) | Primary language specification | `errexit`, `nounset`, `pipefail` semantics and exceptions | Defensive script defaults and explicit error handling | `set -e` has conditional/function exceptions; it is not a replacement for checking statuses |
| BASH-004 | [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) | Engineering style guide | Consistent functions, quoting, tests, naming and ShellCheck use | Readable, reviewable shell helper functions | Organization-specific conventions are not universal language requirements |
| BASH-005 | [ShellCheck](https://www.shellcheck.net/) | Static analysis project | Flags common shell scripting errors and suspect expansions | Pre-commit linting for Bash scripts | Static analysis does not prove runtime correctness |
| BASH-006 | [Software Carpentry: The Unix Shell](https://swcarpentry.github.io/shell-novice/) | Teaching curriculum | Navigation, pipes, filters, loops and scripts | Beginner exercises using small data files | Introductory curriculum, not a performance benchmark |
| BASH-007 | [GNU awk Manual](https://www.gnu.org/software/gawk/manual/) | Primary utility documentation | Records, fields, patterns, actions and processing structured text | Select rows from phenotype/metadata TSV files | CSV with quoting/embedded delimiters needs a CSV-aware parser, not plain `-F,` |
| BASH-008 | [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/) | Primary utility documentation | File, text, checksum, sorting and counting utilities | Reproducible file inventories and checksums | BSD/macOS options differ from GNU options |
| BASH-009 | [GNU grep Manual](https://www.gnu.org/software/grep/manual/) | Primary utility documentation | Pattern matching, fixed strings and recursive searches | Search logs, gene lists and text metadata | Use `-F` for literal terms and understand exit code 1 = no matches |
| BASH-010 | [The Open Group POSIX Shell and Utilities](https://pubs.opengroup.org/onlinepubs/9799919799/) | Portability standard | Portable shell and command behavior | Identify features shared across Unix environments | Bash arrays and `[[ ... ]]` are not portable POSIX `sh` |

## Findings and recommendations

1. **Choose Bash for orchestration**, file management and simple row/field operations. Use R/Bioconductor for statistical inference and assay-aware genomics analysis rather than reproducing models in shell.
2. **Quote expansions:** `"$file"`, `"$@"` and `"$(command)"`. Handle arbitrary filenames with NUL delimiters when invoking `find` and `xargs` where supported.
3. **Specify shell and version:** start scripts with `#!/usr/bin/env bash`, document Bash requirements and avoid Bash 4+ features if the target includes the macOS Bash 3.2 default.
4. **Treat failures as data:** explicitly check expected `grep` no-match outcomes, read/loop exit codes and command availability; `set -euo pipefail` helps but has documented exceptions.
5. **Keep data schema explicit:** `awk -F '\t'` is reasonable for simple TSV. For quoted CSV or complex genomics metadata, use a parser designed for CSV and validate headers.
6. **Favor transparent pipelines:** version input files, log commands, record checksums, and use temporary outputs followed by atomic moves when practical.
7. **Validate before scale:** run `bash -n`, ShellCheck, and fixture-based tests; avoid timing comparisons that change statistical content or row interpretation.

## Gene-analysis boundary

Shell utilities can inspect count-table headers, verify sample IDs, list files, compute SHA-256 manifests, subset simple TSV metadata and launch `Rscript --vanilla`. Bash must not be used to infer that counts, CPM, log-CPM, FDR or biological contrasts are interchangeable. Gene-level inference remains in validated R/Bioconductor workflows.

## Citation policy

These sources provide language definitions, training, coding guidance or tooling; they do not independently confirm findings from TCGA-BRCA. References are cross-linked to the companion [Bash operation sheet](BASH_OPERATION_SHEET.md).
