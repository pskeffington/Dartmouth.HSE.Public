#!/usr/bin/env python3
"""Render the curated public companion deterministically; --check never writes."""
import argparse
from pathlib import Path
import gene_companion_content as content
from gene_companion_domains import DOMAINS
import gene_companion_chapters as editorial
from gene_companion_figures import FIGURES, FIGURE_INTRO

ROOT = Path(__file__).resolve().parents[1]
BASE = Path('06_RESOURCES/Genomics')
HEADINGS = (
 'A. Identification', 'B. What this gene normally does',
 'C. Why breast cancer researchers study it', 'D. Molecular subtype context',
 'E. What the measurement means', 'F. Clinical and research relevance',
 'G. What this gene cannot tell us', 'H. Literature and evidence',
 'I. Student learning takeaway')


def domain_anchor(key):
    return DOMAINS[key][0].lower().replace(" ", "-")


def study_link(key):
    item = content.STUDIES[key]
    return f"[{item['title']} ({item['year']})](https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/)"


def subtype_context(gene):
    symbol = gene['symbol']
    if symbol == 'FOXC1':
        finding = 'The reviewed FOXC1 study reports a basal-like association. It does not establish a rule separating luminal A, luminal B and HER2-enriched tumors from one FOXC1 value.'
    elif symbol in ('PIK3CA', 'GATA3'):
        finding = 'TCGA reports enrichment of particular mutations in luminal A disease. This is a DNA finding, not a claim that high RNA separates luminal A from luminal B, HER2-enriched or basal-like disease.'
    elif symbol == 'ERBB2':
        finding = 'TCGA reports HER-family signaling within HER2-enriched tumors. This does not make ERBB2 RNA a classifier separating luminal A, luminal B or basal-like tumors, nor make HER2-enriched identical to clinical HER2-positive.'
    else:
        finding = 'The reviewed evidence does not establish a gene-specific discriminator across luminal A, luminal B, HER2-enriched and basal-like disease. The study context below should not be promoted to a four-subtype claim.'
    return finding + ' PAM50 uses a defined multi-gene expression method; clinical ER, PR and HER2 categories use separate assays. ' + study_link('PAM50') + '.'


def clinical_context(gene):
    symbol = gene['symbol']
    if symbol in ('ESR1', 'PGR', 'ERBB2', 'MKI67'):
        explanation = 'Clinical laboratories measure ER, PR, HER2 and sometimes Ki-67 using defined tissue assays. This gene encodes a relevant product, but the RNA value is not the corresponding pathology result or its clinical threshold.'
    elif symbol in ('BRCA1', 'BRCA2', 'PALB2', 'ATM', 'CHEK2', 'BARD1'):
        explanation = 'Inherited-variant research concerns classified DNA variants, with risk depending on gene, variant and population. Genetic counseling and validated testing are separate from this educational RNA reference.'
    elif symbol in ('AKT1', 'CDK4', 'CDK6', 'MTOR'):
        explanation = 'A randomized pathway-drug trial supplies clinical research evidence in a defined population. It does not by itself establish a current regulatory indication, isolate one gene as the drug mechanism or make transcript abundance a selection test.'
    else:
        explanation = 'The source supplies research context at the stated review extent. This card does not establish a regulatory or guideline-approved application for this gene measurement; exploratory associations require independent validation.'
    return explanation + ' For the established assay distinctions, see [NCI biomarker testing](https://www.cancer.gov/types/breast/diagnosis/breast-cancer-biomarker-tests).'


def card(gene):
    symbol = gene['symbol']; source = content.STUDIES[gene['study']]
    domains = ', '.join(f"[{DOMAINS[d][0]}](../GENE_BIOLOGY_LEARNING_GUIDE.md#{domain_anchor(d)})" for d in gene['domains'])
    aliases = ', '.join(gene['alias_symbol'].split('|')) or 'None recorded in the accessed HGNC record.'
    former = ', '.join(gene['prev_symbol'].split('|')) or 'None recorded.'
    sections = [
      f"- Approved symbol: **{symbol}**; full name: **{gene['name']}**.\n"
      f"- HGNC: [{gene['hgnc_id']}](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/{gene['hgnc_id']}).\n"
      f"- NCBI Gene: [{gene['entrez_id']}](https://www.ncbi.nlm.nih.gov/gene/{gene['entrez_id']}); human (taxid 9606).\n"
      f"- Ensembl: [{gene['ensembl_gene_id']}](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={gene['ensembl_gene_id']}).\n"
      f"- HGNC alias symbols (historical search aids): {aliases}\n- Previous symbols: {former}\n"
      f"- Product: {gene['product']}; locus type: {gene['locus_type']}.\n"
      f"- Annotation state: `ANNOTATION_VERIFIED`; HGNC status: `Approved`; access: {gene['access_date']}.\n"
      f"- Identity check: {gene['annotation_crosscheck']} Aliases are not additional genes or join keys.\n- Teaching domains: {domains}.",
      gene['normal'] + ' This molecular-function explanation is independently written and checked against the linked NCBI Gene record; it is separate from the cancer-study interpretation.',
      gene['research'] + '\n\n' + gene['finding'] + ' This finding is confined to the study design and model described in section H.',
      subtype_context(gene),
      gene['measurement'] + '\n\nDNA mutation changes sequence; copy number changes genomic dosage; RNA measures transcripts; total protein measures abundance; phosphorylation or another activity assay addresses regulation. A clinical laboratory result also depends on specimen, assay and validated criteria. None of these is a substitute for the others. See the [measurement guide](../GENE_EXPRESSION_INTERPRETATION.md).',
      clinical_context(gene),
      gene['limitation'] + ' ' + gene['claim_limit'],
      f"**Primary study:** {study_link(gene['study'])}. DOI: [{source['doi']}](https://doi.org/{source['doi']}).\n\n"
      f"**Design:** {gene['design']}. **Population/model:** {gene['model']}.\n\n"
      f"**Narrow supported claim:** {gene['finding']}\n\n**Important limit:** {gene['claim_limit']}\n\n"
      f"**Verification:** `{source['status']}`; {source['review_extent']} Accessed {source['access_date']}. This is an abstract-supported account, not independent replication or full-text method validation. Annotation verification does not upgrade literature evidence.\n\n"
      'Normal function and stable identity use the authoritative records in section A. [Evidence matrix](../REFERENCES/GENE_EVIDENCE_MATRIX.md) · [Annotation register](../REFERENCES/ANNOTATION_SOURCE_REGISTER.md).',
      f"1. **Function:** {gene['normal'].split('. ')[0]}.\n"
      f"2. **Measurement:** {gene['measurement']}\n3. **Inference:** {gene['limitation']}\n\n"
      f"**Scientific question:** {gene['question']}\n\n**Common mistake:** Treating the study's association or experimental endpoint as a validated individual diagnosis, subtype or treatment prediction.\n\n"
      f"**Exercise:** Read the linked primary abstract and record its assay, model, comparison and endpoint. Propose one additional assay that would address this card's limitation, and explain what it would still leave uncertain. Compare with the [{DOMAINS[gene['domains'][0]][0]} mastery check](../GENE_BIOLOGY_LEARNING_GUIDE.md#{domain_anchor(gene['domains'][0])})."
    ]
    if symbol == 'MALAT1':
        sections[7] += '\n\n**Contradictory context:** ' + study_link('MALAT1_2016') + ' reports reduced metastasis after loss or knockdown, whereas the 2018 add-back study reports suppression by MALAT1. ' + study_link('MALAT1_2024') + ' investigates metastatic reactivation and immune evasion. All three are `ABSTRACT_ONLY` here. Compare perturbation, neighboring genes, host immunity and disease stage before choosing a universal direction of effect.'
    return f"# {symbol} — {gene['name']}\n\n[Companion](../BREAST_CANCER_60_GENE_COMPANION.md) · [Alphabetical index](../GENE_ATLAS_INDEX.md) · [Glossary](../GENE_EXPRESSION_INTERPRETATION.md#glossary)\n\n" + '\n\n'.join(f'## {h}\n\n{body}' for h, body in zip(HEADINGS, sections)) + '\n'



def chapter_anchor(number):
    import re
    title = f"Chapter {number}: {editorial.CHAPTERS[number-1][0]}"
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def figure_at(number):
    """Rebase the shared figure's relative links for its in-guide presentation."""
    import re
    title, body = FIGURES[number-1]
    def rebase(match):
        target = match[1]
        if target.startswith('../'):
            target = target[3:]
        elif not target.startswith(('http:', 'https:', '#')):
            target = 'FIGURES/' + target
        return '](' + target + ')'
    body = re.sub(r'\]\(([^)]+)\)', rebase, body)
    return f"#### Figure {number}: {title}\n\n{body}"


def integrated_profile(gene):
    """One audited claim source supplies both the short profile and detailed card."""
    symbol = gene['symbol']
    paragraphs = [f"**{gene['name']}**. The encoded product is {gene['product']}. {gene['normal']}",
        'Research focus: ' + gene['research'] + f" Study context: {gene['model']}. " + gene['finding'],
        gene['measurement'] + ' ' + gene['limitation'] + ' ' + gene['claim_limit']]
    if symbol == 'MALAT1':
        paragraphs.append('Opposing model findings remain visible: ' + study_link('MALAT1_2016') +
            ' reports reduced metastasis after loss or knockdown, whereas the 2018 add-back study reports suppression by MALAT1. ' +
            study_link('MALAT1_2024') + ' examines metastatic reactivation and immune evasion. Compare interventions and disease stage before assigning a universal effect.')
    paragraphs.append(f"**Evidence:** {study_link(gene['study'])}; `ABSTRACT_ONLY`. "
        f"[Normal-function record](https://www.ncbi.nlm.nih.gov/gene/{gene['entrez_id']}). "
        f"[Complete {symbol} card](GENE_CARDS/{symbol}.md) records identity, design and review scope.")
    return f"#### {symbol}\n\n" + '\n\n'.join(paragraphs)


def render_atlas():
    table = '| Gene | Biological role |\n|---|---|\n'
    for gene in content.GENES:
        table += f"| [{gene['symbol']}](#{gene['symbol'].lower()}) | {gene['product']} |\n"
    # First domain assigns a single presentation location, not exclusive biological membership.
    for key, domain in DOMAINS.items():
        genes = [gene for gene in content.GENES if gene['domains'][0] == key]
        if genes:
            table += f"\n### Atlas: {domain[0]}\n\n"
            table += '\n\n'.join(integrated_profile(gene) for gene in genes) + '\n'
    return table


def render_canonical():
    text = f"# {editorial.LABEL}\n\n[Paul's Notes](../../README.md) · [Resources](../README.md) · [Focused references](README.md)\n\n"
    text += f"Original educational guide · Editorial version `{editorial.EDITORIAL_VERSION}` · Annotation and literature snapshot 2026-10-10.\n\n"
    text += 'Read continuously below, or choose a route into this same guide. Every numerical example is invented; conceptual diagrams carry no patient measurements.\n\n## Contents\n\n'
    text += '\n'.join(f"{n}. [{title}](#{chapter_anchor(n)})" for n,(title,_) in enumerate(editorial.CHAPTERS,1))
    text += '\n\n## Guided learning routes\n\n'
    for label, numbers in [('Beginner',[1,2,3,5,11]),('Biology-focused reader',[4,5,6,7,10]),('Research-focused reader',[2,3,8,9,10,12])]:
        text += f"- **{label}:** " + ' → '.join(f"[{editorial.CHAPTERS[n-1][0]}](#{chapter_anchor(n)})" for n in numbers) + '.\n'
    biology = '\n\n'.join(f"### {name}\n\n{prose}\n\nStarting profiles: " + ' · '.join(f'[{symbol}](#{symbol.lower()})' for symbol in symbols.split()) + '.' for name,symbols,prose in editorial.BIOLOGY_LESSONS)
    for number,(title,prose) in enumerate(editorial.CHAPTERS,1):
        prose = prose.replace('{{BIOLOGY}}',biology).replace('{{ATLAS}}',render_atlas())
        for figure in range(1,8):
            prose = prose.replace('{{FIGURE_'+str(figure)+'}}',figure_at(figure))
        text += f'\n## Chapter {number}: {title}\n\n{prose}\n\n'
        navigation = ['[Return to contents](#contents)']
        if number > 1:
            navigation.insert(0,f'[Previous chapter](#{chapter_anchor(number-1)})')
        if number < 12:
            navigation.append(f'[Next chapter](#{chapter_anchor(number+1)})')
        text += ' · '.join(navigation) + '\n'
    return text


def render_outputs():
    outputs = {BASE/'GENE_CARDS'/f"{g['symbol']}.md":card(g) for g in content.GENES}
    outputs[Path(editorial.CANONICAL)] = render_canonical()
    outputs[BASE/'FIGURES'/'README.md'] = FIGURE_INTRO + '\n\n' + '\n\n'.join('## '+title+'\n\n'+body for title,body in FIGURES)
    index = '# Gene atlas index\n\n[Companion](BREAST_CANCER_60_GENE_COMPANION.md) · [Learning routes](GENE_BIOLOGY_LEARNING_GUIDE.md)\n\nExactly 60 approved human genes; 21 retained foundation entries and 39 additions. This alphabetical catalog is not a ranked signature. Use your browser’s find command to search symbols or domains. Aliases are search aids, not join keys.\n\n## Alphabetical\n\n'
    index += '\n'.join(f"- [{g['symbol']} — {g['name']}](GENE_CARDS/{g['symbol']}.md)" for g in content.GENES)
    index += '\n\n## By biological domain\n\n'
    for key, data in DOMAINS.items():
        index += f"### {data[0]}\n\n" + ' · '.join(f"[{g['symbol']}](GENE_CARDS/{g['symbol']}.md)" for g in content.GENES if key in g['domains']) + '\n\n'
    outputs[BASE/'GENE_ATLAS_INDEX.md'] = index
    outputs[BASE/'GENE_CARDS'/'README.md'] = '# Gene research cards\n\nEach of the [60 cards](../GENE_ATLAS_INDEX.md) separates identity, function, evidence, subtype context, measurement and limitations. Begin with the [companion](../BREAST_CANCER_60_GENE_COMPANION.md) and choose a learning route.\n\nCards are generated from independently authored, curated [content](../../../scripts/gene_companion_content.py); they retain explicit review-extent labels.\n'
    matrix = '# Gene evidence matrix\n\n[Companion](../BREAST_CANCER_60_GENE_COMPANION.md) · [Annotation register](ANNOTATION_SOURCE_REGISTER.md)\n\n## Evidence states and scope\n\n`ANNOTATION_VERIFIED` means the three public identity records agreed at access. `ABSTRACT_ONLY` means bibliographic information and the abstract were reviewed; full methods, supplements and results were not independently audited. `PRIMARY_EVIDENCE_VERIFIED` would require a documented full-text claim audit; no study is assigned that state in this edition. `INSUFFICIENT_EVIDENCE` denotes an unsupported proposed inference; `REVIEW_REQUIRED` denotes an unresolved source or mapping problem. A paper being primary research does not itself establish its reliability, reproducibility or clinical validity.\n\n56 unique primary publications support 60 card-level accounts or clearly labeled contextual readings. Recent studies were searched within 2021–2026-10-10; useful foundational classification, receptor, stress and trial studies were retained. Publication titles and identifiers were checked against Europe PMC/PubMed records. No complete reference texts or raw database dumps are distributed. Gene-specific mechanism and subtype claims remain limited to the findings described below.\n\n'
    for g in content.GENES:
        s = content.STUDIES[g['study']]
        matrix += f"## {g['symbol']}\n\n[Card](../GENE_CARDS/{g['symbol']}.md) · {study_link(g['study'])}\n\n- DOI: [{s['doi']}](https://doi.org/{s['doi']}); PMID: {s['pmid']}; year: {s['year']}.\n- Design: {g['design']}.\n- Population/model: {g['model']}.\n- Finding and narrow claim: {g['finding']}\n- Limit: {g['claim_limit']}\n- State: `{s['status']}`. {s['review_extent']} Access: {s['access_date']}.\n\n"
    matrix += '## Additional shared and conflicting primary readings\n\n'
    for key in ['PAM50','WU','NORMAL','MALAT1_2016','MALAT1_2024']:
        s = content.STUDIES[key]
        matrix += f"- {study_link(key)} — DOI [{s['doi']}](https://doi.org/{s['doi']}); PMID {s['pmid']}; `ABSTRACT_ONLY`; accessed {s['access_date']}. "
        matrix += {'PAM50':'Multi-gene classifier development and testing; does not justify single-gene subtype rules.','WU':'Single-cell and spatial tumor atlas; supports cell-composition context, not a classifier for this catalog.','NORMAL':'Single-cell atlas from 55 adult breast tissue donors; reduction/risk-reduction tissue is not tumor-adjacent tissue.','MALAT1_2016':'Mouse loss/knockdown and organoid experiments; metastasis direction differs from the 2018 account.','MALAT1_2024':'Metastatic initiation/reactivation and immune-evasion models; stage and intervention limit transport.'}[key]+'\n'
    outputs[BASE/'REFERENCES'/'GENE_EVIDENCE_MATRIX.md'] = matrix
    register = '# Annotation source register\n\n[Complete guide](../BREAST_CANCER_60_GENE_COMPANION.md) · [Selection rubric](SELECTION_RUBRIC.md) · [Evidence matrix](GENE_EVIDENCE_MATRIX.md)\n\n## Method and release boundary\n\nAccess date: **2026-10-10**. HGNC complete-set records were restricted to approved human symbols, then cross-checked by stable ID against NCBI Gene (human taxid 9606; approved symbol) and Ensembl human gene records (same stable ID and display name). All 60 mappings agreed; no withdrawn or ambiguous primary symbol was accepted. No ambiguous alias was used to join records. This is a dated access snapshot, not a claim of a named immutable Ensembl release. Recheck identities before combining with a future assay annotation.\n\nSources: [HGNC complete set](https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt), [HGNC license (CC0)](https://www.genenames.org/about/license/), [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/), [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/), [Ensembl REST](https://rest.ensembl.org/). Only selected public identity facts are retained in the documented Python content source. Descriptions and study interpretations are independently written. Aliases and former symbols appear on each card and can denote older nomenclature or overlapping searches; stable primary IDs govern identity.\n\n## Verified identities\n\n| Symbol | HGNC | NCBI Gene | Ensembl | State |\n|---|---|---|---|---|\n'
    for g in content.GENES:
        register += f"| [{g['symbol']}](../GENE_CARDS/{g['symbol']}.md) | {g['hgnc_id']} | [{g['entrez_id']}](https://www.ncbi.nlm.nih.gov/gene/{g['entrez_id']}) | [{g['ensembl_gene_id']}](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={g['ensembl_gene_id']}) | ANNOTATION_VERIFIED |\n"
    register += '\n## Reproduction and future updates\n\nThe content source records the selected facts, access date, aliases, cross-check extent and original prose. Run `python3 scripts/build_gene_companion.py --check` to compare every generated artifact with that source; run `python3 scripts/validate_gene_companion.py` for identity, completeness and evidence-boundary checks. These offline checks establish consistency with the reviewed snapshot, not fresh online verification. A future annotation update must explicitly repeat the three-source cross-check and refresh the date, facts, evidence and publication checks.\n'
    outputs[BASE/'REFERENCES'/'ANNOTATION_SOURCE_REGISTER.md'] = register
    guide = '# Focused biological-domain lessons\n\n[Breast Cancer Research Guide — People, Data, Biology and 60 Genes](BREAST_CANCER_60_GENE_COMPANION.md) · [Index](GENE_ATLAS_INDEX.md)\n\nThese 12 category exercises supplement the continuous guide; begin with its [three learning routes](BREAST_CANCER_60_GENE_COMPANION.md#guided-learning-routes) and [connected biology chapter](BREAST_CANCER_60_GENE_COMPANION.md#chapter-5-the-biology-behind-the-60-genes). Categories overlap and do not establish direct interactions. All examples below are conceptual or invented.\n\n'
    for key, (name, normal, altered, example, questions, answer) in DOMAINS.items():
        links = ' · '.join(f"[{g['symbol']}](GENE_CARDS/{g['symbol']}.md)" for g in content.GENES if key in g['domains'])
        guide += f'<a id="{key}"></a>\n\n## {name}\n\n**Learning objectives:** Explain the normal process; distinguish an abundance measurement from a functional assay; identify an alternative explanation for a tissue-level signal.\n\n**Normal function:** {normal}\n\n**Cancer and measurement:** {altered} Read the linked cards for RNA, protein and activity distinctions. Measurements can combine different cell types and mechanisms, so each inference needs a specified specimen and assay.\n\n**Selected genes:** {links}\n\n**Worked conceptual example:** {example}\n\n**Interpretation questions / mastery check:** {questions}\n\n<details>\n<summary>Check your reasoning</summary>\n\n{answer}\n\n</details>\n\n**Evidence boundary:** Normal molecular functions are distinct from model-specific cancer findings. Shared membership is a teaching relationship, not proof of binding, causality, individual prognosis or treatment benefit. Use the evidence matrix to identify what remains a hypothesis.\n\n'
    outputs[BASE/'GENE_BIOLOGY_LEARNING_GUIDE.md'] = guide
    return {path: text.rstrip() + "\n" for path, text in outputs.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args(); stale = []
    for relative, text in render_outputs().items():
        path = ROOT/relative
        if args.check:
            if not path.is_file() or path.read_text() != text:
                stale.append(str(relative))
        else:
            path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text)
    if stale:
        parser.exit(1, 'Generated content differs: ' + ', '.join(stale) + '\n')
    print(f"{'Checked' if args.check else 'Rendered'} {len(render_outputs())} companion documents.")


if __name__ == '__main__':
    main()
