#!/usr/bin/env bash
# Build the ready-linked APA 7 example and its bibliography.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

for cmd in pdflatex biber kpsewhich; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    printf 'Missing tool: %s. Install a TeX distribution with Biber.\n' "$cmd" >&2
    exit 1
  fi
done
for pkg in biblatex.sty apa.bbx csquotes.sty babel.sty; do
  if ! kpsewhich "$pkg" >/dev/null; then
    printf 'Missing TeX package file: %s. See README.md for dependencies.\n' "$pkg" >&2
    exit 1
  fi
done

case "${1:-}" in
  "") name=Example_APA_7_Manuscript; bib=Example_References.bib ;;
  --catalogue) name=Example_APA_7_Reference_Catalogue; bib=Example_Entry_Types.bib ;;
  *) printf 'Usage: bash compile_manuscript.sh [--catalogue]\n' >&2; exit 2 ;;
esac
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
biber "$name"
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
printf '\nBuilt %s.pdf with %s.\n' "$name" "$bib"
