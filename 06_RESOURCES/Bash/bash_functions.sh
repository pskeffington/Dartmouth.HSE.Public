#!/usr/bin/env bash
# Sourceable Bash helpers; compatible with Bash 3.2+.
# Sourcing defines functions only: no files are modified.

# Print consistent errors to stderr and return failure to the caller.
hse_error() {
  printf 'ERROR: %s\n' "$*" >&2
  return 1
}

# Validate a required executable before launching a research stage.
hse_require_command() {
  [[ $# -eq 1 ]] || { hse_error 'usage: hse_require_command executable'; return 2; }
  command -v "$1" >/dev/null 2>&1 || hse_error "command not found: $1"
}

# Validate that an input exists, is an ordinary file and is readable.
hse_require_file() {
  [[ $# -eq 1 ]] || { hse_error 'usage: hse_require_file path'; return 2; }
  [[ -f "$1" && -r "$1" ]] || hse_error "missing or unreadable file: $1"
}

# Count tabular data records excluding one header line.
# Intended for well-formed line-delimited TSV files (not multiline quoted CSV).
hse_tsv_records() {
  [[ $# -eq 1 ]] || { hse_error 'usage: hse_tsv_records file.tsv'; return 2; }
  hse_require_file "$1" || return
  awk 'END {print NR > 0 ? NR - 1 : 0}' "$1"
}

# Print TSV field names with 1-based positions for safe column selection.
hse_tsv_columns() {
  [[ $# -eq 1 ]] || { hse_error 'usage: hse_tsv_columns file.tsv'; return 2; }
  hse_require_file "$1" || return
  awk -F '\t' 'NR == 1 {for(i=1;i<=NF;i++) printf "%d\t%s\n", i, $i; exit}' "$1"
}

# Produce a SHA-256 fingerprint using common GNU or macOS utilities.
hse_sha256() {
  [[ $# -eq 1 ]] || { hse_error 'usage: hse_sha256 path'; return 2; }
  hse_require_file "$1" || return
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1"
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1"
  else
    hse_error 'Neither sha256sum nor shasum is installed'
  fi
}

# Run an R analysis using its explicit path; forward all additional arguments.
# The R script itself must validate its scientific input and output contract.
hse_run_r() {
  [[ $# -ge 1 ]] || { hse_error 'usage: hse_run_r script.R [args...]'; return 2; }
  hse_require_command Rscript || return
  local script_path=$1
  shift
  hse_require_file "$script_path" || return
  Rscript --vanilla "$script_path" "$@"
}

# To try these operations:
# source 06_RESOURCES/Bash/bash_functions.sh
# hse_require_command awk
# hse_tsv_columns simple_metadata.tsv
# hse_tsv_records simple_metadata.tsv
# hse_sha256 simple_metadata.tsv
