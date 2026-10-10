#!/usr/bin/env bash
# Build APA examples in an isolated directory; publish only a successful PDF.
set -euo pipefail
source_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
output_dir=$source_dir
name=Example_APA_7_Manuscript
bib=Example_References.bib
while [[ $# -gt 0 ]]; do
  case "$1" in
    --catalogue) name=Example_APA_7_Reference_Catalogue; bib=Example_Entry_Types.bib; shift ;;
    --output-dir) [[ $# -ge 2 ]] || { printf 'Missing output directory\n' >&2; exit 2; }; output_dir=$2; shift 2 ;;
    *) printf 'Usage: bash compile_manuscript.sh [--catalogue] [--output-dir directory]\n' >&2; exit 2 ;;
  esac
done
for cmd in pdflatex biber kpsewhich; do
  command -v "$cmd" >/dev/null 2>&1 || { printf 'Missing tool: %s\n' "$cmd" >&2; exit 1; }
done
for pkg in biblatex.sty apa.bbx csquotes.sty babel.sty mathptmx.sty; do
  [[ -n $(kpsewhich "$pkg") ]] || { printf 'Missing TeX package: %s\n' "$pkg" >&2; exit 1; }
done
mkdir -p -- "$output_dir"
output_dir=$(cd -- "$output_dir" && pwd)
apa_build_dir=$(mktemp -d "${TMPDIR:-/tmp}/hse-apa-build.XXXXXX")
trap 'rm -rf -- "$apa_build_dir"' EXIT
cp -- "$source_dir/$name.tex" "$source_dir/$bib" "$apa_build_dir/"
cd -- "$apa_build_dir"
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
mkdir -p "$apa_build_dir/biber-runtime"
PAR_GLOBAL_TEMP="$apa_build_dir/biber-runtime" biber --validate-datamodel "$name"
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
pdflatex -interaction=nonstopmode -halt-on-error "$name.tex"
if grep -E 'Citation .* undefined|There were undefined references|Please \(re\)run Biber' "$name.log"; then
  printf 'Unresolved bibliography or references\n' >&2
  exit 1
fi
cp -- "$name.pdf" "$output_dir/$name.pdf"
printf 'Built %s.pdf from %s in an isolated directory.\n' "$name" "$bib"
