#!/usr/bin/env python3
"""Fail closed on catalog, identity, evidence or generated-document inconsistency.

Offline verification checks the reviewed public access snapshot, not fresh online
annotation or legal clearance. Protected-source and publication gates stay separate.
"""
import hashlib
import json
from pathlib import Path
import re
import gene_companion_content as content
from gene_companion_domains import DOMAINS
import build_gene_companion as builder
import gene_companion_chapters as editorial
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
# Sealed only over public approved identity facts; refresh after a new source audit.
EDITORIAL_SOURCE_SEALS = {'gene_companion_chapters.py': '50fa88682a12f4e4f8f2f8840d03567179e10da2b1d9a54c12bab22675e78981', 'gene_companion_figures.py': '667aa150657fb7d886d2c42ed9f6d22204e994c6fdee1b4fca7804edb49d9e81'}

IDENTITY_SNAPSHOT_SHA256 = '74bf65f70d34dafa55dc2994222c960b7ee644dcc860c3e406e076f4d4b9f6b0'


def identity_digest(genes):
    fields = ('symbol', 'name', 'hgnc_id', 'entrez_id', 'ensembl_gene_id', 'status')
    rows = [{key: gene[key] for key in fields} for gene in genes]
    return hashlib.sha256(json.dumps(sorted(rows, key=lambda row: row['symbol']),
        sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def validate_content(genes, studies):
    errors = []
    if len(genes) != 60:
        errors.append('Exactly 60 genes required')
    for field in ('symbol', 'hgnc_id', 'entrez_id', 'ensembl_gene_id'):
        values = [g.get(field) for g in genes]
        if None in values or len(set(values)) != len(values):
            errors.append('Missing or duplicate primary identity: ' + field)
    if not set(content.ORIGINAL_GENES).issubset({g.get('symbol') for g in genes}):
        errors.append('Original 21-gene coverage incomplete')
    try:
        if identity_digest(genes) != IDENTITY_SNAPSHOT_SHA256:
            errors.append('Approved identity snapshot differs; repeat source verification')
    except KeyError:
        errors.append('Incomplete identity snapshot')
    for g in genes:
        symbol = g.get('symbol', '<missing>')
        for field in ('name','normal','research','measurement','limitation','question',
                      'design','model','finding','claim_limit','product','annotation_crosscheck'):
            if not isinstance(g.get(field), str) or not g[field].strip():
                errors.append(f'{symbol}: missing {field}')
        for field, pattern in (('symbol',r'[A-Z][A-Z0-9]*'),('hgnc_id',r'HGNC:[1-9][0-9]*'),
                               ('entrez_id',r'[1-9][0-9]*'),('ensembl_gene_id',r'ENSG[0-9]{11}')):
            if not re.fullmatch(pattern, g.get(field, '')):
                errors.append(f'{symbol}: invalid {field}')
        if g.get('status') != 'Approved' or g.get('verification') != 'ANNOTATION_VERIFIED':
            errors.append(f'{symbol}: annotation not verified/approved')
        if g.get('access_date') != content.ACCESS_DATE:
            errors.append(f'{symbol}: annotation access date differs')
        if not g.get('domains') or not set(g['domains']).issubset(DOMAINS):
            errors.append(f'{symbol}: missing or unknown domain')
        study = studies.get(g.get('study'))
        if not study:
            errors.append(f'{symbol}: primary reference missing'); continue
        for field in ('title', 'doi', 'pmid', 'year', 'status', 'review_extent', 'access_date'):
            if not isinstance(study.get(field), str) or not study[field].strip():
                errors.append(f'{symbol}: missing reference field {field}')
        if study.get('status') != 'ABSTRACT_ONLY':
            errors.append(f'{symbol}: literature review state exceeds this edition audit')
        if not re.fullmatch(r'[1-9][0-9]*', study.get('pmid','')) or not re.fullmatch(r'10\.[0-9]{4,9}/\S+', study.get('doi','')):
            errors.append(f'{symbol}: invalid PMID/DOI')
        if study.get('access_date') != content.ACCESS_DATE or not re.fullmatch(r'(19|20)[0-9]{2}', study.get('year','')):
            errors.append(f'{symbol}: invalid reference date')
        if 'full methods' not in study.get('review_extent',''):
            errors.append(f'{symbol}: literature review extent missing')
    for key, study in studies.items():
        if study.get('status') != 'ABSTRACT_ONLY' or study.get('access_date') != content.ACCESS_DATE:
            errors.append(f'{key}: shared reference review state/date exceeds this edition audit')
    if not all(any(key in g.get('domains', []) for g in genes) for key in DOMAINS):
        errors.append('Not all 12 domains represented')
    return errors



def heading_anchors(text):
    """Match GitHub headings, including suffixes for duplicate headings."""
    counts = {}; anchors = set(); fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r'^#{1,6}\s+(.+)$', line)
        if match:
            label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match[1])
            slug = re.sub(r'[^\w\- ]', '', label.lower()).replace(' ', '-')
            count = counts.get(slug,0); counts[slug] = count+1
            anchors.add(slug + (f'-{count}' if count else ''))
    return anchors


def validate_guide(root):
    errors = []
    if editorial.EDITORIAL_VERSION != 'UNIFIED_GUIDE_V1':
        errors.append('Editorial source version not accepted')
    for name, seal in EDITORIAL_SOURCE_SEALS.items():
        path = root/'scripts'/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != seal:
            errors.append('Editorial source seal differs: ' + name)
    canonical = root/editorial.CANONICAL
    if not canonical.is_file():
        return errors + ['Canonical guide missing']
    text = canonical.read_text()
    expected_chapters = [f'Chapter {n}: {title}' for n,(title,_) in enumerate(editorial.CHAPTERS,1)]
    chapters = re.findall(r'^## (Chapter .+)$',text,re.M)
    if len(expected_chapters) != 12 or chapters != expected_chapters:
        errors.append('Twelve chapters absent or out of instructional order')
    symbols = re.findall(r'^#### ([A-Z][A-Z0-9]*)$',text,re.M)
    expected = [g['symbol'] for g in content.GENES]
    if len(symbols) != 60 or sorted(symbols) != sorted(expected):
        errors.append('Integrated atlas must contain exactly 60 distinct genes')
    for symbol in expected:
        if f'| [{symbol}](#{symbol.lower()}) |' not in text:
            errors.append('Alphabetical gene jump missing: ' + symbol)
        if f'[Complete {symbol} card](GENE_CARDS/{symbol}.md)' not in text:
            errors.append('Orphaned complete card: ' + symbol)
        section = text.split('#### '+symbol+'\n\n',1)[-1].split('\n###',1)[0]
        if len(section.split()) < 100 or '`ABSTRACT_ONLY`' not in section:
            errors.append('Substantive profile or review state missing: ' + symbol)
    table = text.split('### Alphabetical gene lookup',1)[-1].split('\n### Atlas:',1)[0]
    lookup = re.findall(r'^\| \[([A-Z][A-Z0-9]*)\]',table,re.M)
    if lookup != sorted(expected):
        errors.append('Alphabetical lookup missing, duplicated or reordered')
    if text.count('```mermaid\n') != 7 or text.count('[Return to contents](#contents)') != 12:
        errors.append('Integrated figures or chapter return navigation incomplete')
    for label in ('Beginner','Biology-focused reader','Research-focused reader'):
        if f'**{label}:**' not in text:
            errors.append('Learning route missing: ' + label)
    for n in range(1,13):
        chapter = text.split('## '+expected_chapters[n-1]+'\n',1)[-1].split('\n## Chapter ',1)[0]
        for label, adjacent in [('Previous chapter',n-1),('Next chapter',n+1)]:
            if 1 <= adjacent <= 12 and f'[{label}](#{builder.chapter_anchor(adjacent)})' not in chapter:
                errors.append('Broken adjacent chapter navigation: ' + str(n))
    for filename,prefix in [('README.md','06_RESOURCES/Genomics/'),('06_RESOURCES/README.md','Genomics/')]:
        path = root/filename
        if not path.is_file():
            errors.append('Canonical entrypoint missing: ' + filename); continue
        document = path.read_text()
        entry = f'[{editorial.LABEL}]({prefix}BREAST_CANCER_60_GENE_COMPANION.md)'
        if document.count(entry) != 1:
            errors.append('Exactly one labeled canonical entry required: ' + filename)
        if filename == 'README.md' and re.search(r'\]\([^)]*Genomics/(?:README|BREAST_CANCER_TCGA_BRCA_NARRATIVE|COMMON_BREAST_CANCER_GENE_DESCRIPTORS)\.md',document):
            errors.append('Competing root genomics entrypoint')
    # Validate focused backlinks and every local link, including rebased figure paths.
    for source in (root/builder.BASE).rglob('*.md'):
        document = source.read_text()
        if source != canonical and 'BREAST_CANCER_60_GENE_COMPANION.md' not in document:
            errors.append('Supporting page lacks canonical backlink: ' + str(source.relative_to(root)))
        for target in re.findall(r'\]\(([^)]+)\)',document):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = (source.parent/unquote(url.path)).resolve() if url.path else source.resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append('Supporting link escapes repository: ' + target); continue
            if destination.is_dir():
                destination = destination/'README.md'
            if not destination.is_file():
                errors.append('Broken supporting link: ' + target)
            elif url.fragment and destination.suffix in ('.md','.Rmd') and unquote(url.fragment) not in heading_anchors(destination.read_text()):
                errors.append('Broken chapter/supporting anchor: ' + target)
    return errors


def validate_tree(root):
    errors = validate_content(content.GENES, content.STUDIES) + validate_guide(root)
    base = root/builder.BASE
    paths = {p.stem for p in (base/'GENE_CARDS').glob('*.md') if p.name != 'README.md'}
    expected = {g['symbol'] for g in content.GENES}
    if paths != expected:
        errors.append('Card filenames do not match exactly 60 approved symbols')
    for relative, rendered in builder.render_outputs().items():
        path = root/relative
        if not path.is_file() or path.read_text() != rendered:
            errors.append('Missing or nonreproducible artifact: ' + str(relative))
    for g in content.GENES:
        path = base/'GENE_CARDS'/f"{g['symbol']}.md"
        if not path.is_file():
            continue
        text = path.read_text()
        headings = re.findall(r'^## (.+)$', text, re.M)
        if headings != list(builder.HEADINGS):
            errors.append(f"{g['symbol']}: required A–I headings absent or reordered")
        for heading in builder.HEADINGS:
            marker = '## ' + heading + '\n\n'
            body = text.split(marker, 1)[-1].split('\n\n## ', 1)[0]
            if marker not in text or len(body.split()) < 20:
                errors.append(f"{g['symbol']}: incomplete section {heading}")
        if '`ABSTRACT_ONLY`' not in text or '`PRIMARY_EVIDENCE_VERIFIED`' in text:
            errors.append(f"{g['symbol']}: unsupported evidence promotion")
    figures = base/'FIGURES'/'README.md'
    if not figures.is_file():
        errors.append('Figure source missing')
    else:
        text = figures.read_text()
        if text.count('```mermaid\n') != 7:
            errors.append('Exactly seven original diagrams required')
        for number in range(1, 8):
            marker = f'**Figure {number} caption.**'
            body = text.split(marker, 1)[-1].split('\n## ', 1)[0]
            if marker not in text or '**Inputs:**' not in body or '**Sources:**' not in body:
                errors.append(f'Figure {number}: caption, inputs or sources incomplete')
            if not re.search(r'conceptual|synthetic', body, re.I):
                errors.append(f'Figure {number}: conceptual/synthetic state missing')
        for label in ('zero-centered', 'log2 fold change', 'TeachA', 'C1 simulated contrast', '#2166AC', '#F7F7F7', '#B2182B'):
            if label not in text:
                errors.append('Synthetic figure labeling incomplete: ' + label)
    # Narrow safety lint is supplementary: live protected-source comparisons and
    # authoring evidence, not a keyword test, determine publication admission.
    for relative in builder.render_outputs():
        path = root/relative
        if path.is_file() and re.search(r'\bST09\b|TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', path.read_text()):
            errors.append('Unexpected private-signature or participant-like label: ' + str(relative))
    return errors


def main():
    errors = validate_tree(ROOT)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: 60 verified snapshot identities; original 21 retained; 12 domains; '
          'A–I cards; abstract-only evidence; reproducible documents; 7 labeled diagrams.')
    print('Fresh online verification, scientific method review and rights clearance are separate gates.')


if __name__ == '__main__':
    main()
