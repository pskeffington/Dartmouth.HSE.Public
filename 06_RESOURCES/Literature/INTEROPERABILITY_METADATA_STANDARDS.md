# Biomedical interoperability and metadata — coding reference matrix

[Research intake](RESEARCH_PROJECT_INTAKE.md) · [Coding conventions](BIOMEDICAL_CODING_STANDARDS.md) · [Quality gates](RESEARCH_CODE_QUALITY_MATRIX.md) · [Literature index](README.md)

**Reference review:** October 10, 2026. This is an independently authored reference to public standards and specifications, not a claim of compliance, a substitute for the primary specifications, or a clinical terminology mapping product. No institution-owned classroom sources or patient records were used.

## Evidence matrix

| ID | Authoritative reference | Type | Implementation guidance | Required qualification |
| --- | --- | --- | --- | --- |
| INT-01 | [UCUM specification](https://ucum.org/ucum) | Units coding standard | Store an explicit coded unit alongside its quantitative value; validate dimensional compatibility before conversion | Machine-readable units require correct source interpretation and UCUM grammar, not string matching |
| INT-02 | [LOINC overview](https://loinc.org/get-started/what-loinc-is/) | Observation terminology | Separate laboratory/clinical observation identity from numeric result and unit | Selecting a LOINC code requires meaning, specimen, property, time and method context as relevant |
| INT-03 | [FHIR R4 Observation](https://hl7.org/fhir/R4/observation.html) | Versioned interoperability resource | Distinguish Observation.code, subject, effective time, status, value and unit in an interface | R4 is not interchangeable with later FHIR releases or jurisdiction-specific profiles |
| INT-04 | [FHIR R4 Patient](https://hl7.org/fhir/R4/patient.html) | Versioned interoperability resource | Preserve patient identity boundaries and references rather than substituting event IDs | Pseudonymized IDs still require privacy evaluation |
| INT-05 | [FHIR R4 Specimen](https://hl7.org/fhir/R4/specimen.html) | Versioned interoperability resource | Model specimen identity, collection, subject and sample relationships independently | Specimens are not one-to-one with encounters or subjects by default |
| INT-06 | [OHDSI OMOP data model conventions](https://ohdsi.github.io/CommonDataModel/dataModelConventions.html) | Common data model conventions | Keep person, visit, measurement, concept IDs and source vocabulary distinct | Require the exact deployed CDM version and ETL contract |
| INT-07 | [OHDSI Athena vocabularies](https://athena.ohdsi.org/) | Vocabulary distribution | Record the vocabulary and concept release used in each standardization | Mapping availability does not prove clinical equivalence or licensing for redistribution |
| INT-08 | [SNOMED CT overview](https://www.snomed.org/what-is-snomed-ct) | Clinical terminology | Use clinical concepts with explicit version and terminology scope | Licensing and jurisdictional access conditions may apply |
| INT-09 | [HGNC guidelines](https://www.genenames.org/about/guidelines/) | Gene nomenclature authority | Preserve approved symbols and stable identifiers; record alias resolution | Symbols can change and aliases can be ambiguous |
| INT-10 | [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) | Reference database | Record taxon, accession or gene ID, and mapping provenance | Do not treat displayed symbols as globally unique identifiers |
| INT-11 | [GA4GH Phenopackets](https://phenopacket-schema.readthedocs.io/en/latest/) | Phenotype data exchange schema | Represent individual, phenotypic features, disease, biosamples and time context explicitly | Use a specified schema version and controlled ontology references |
| INT-12 | [RO-Crate specification](https://www.researchobject.org/ro-crate/specification) | Research packaging specification | Attach machine-readable metadata for datasets, files, authors, software and licenses | Current release/version must be recorded; metadata cannot grant absent rights |
| INT-13 | [W3C PROV-O](https://www.w3.org/TR/prov-o/) | Provenance ontology | Track entities, activities and agents behind transformations and outputs | Provenance records explain lineage, not scientific validity |
| INT-14 | [DataCite Metadata Schema](https://schema.datacite.org/) | Citation and metadata standard | Record creators, titles, dates, identifiers, versions and related resources | A DOI or citation does not authorize data redistribution |

## Data-model boundary rules

**Identifier roles:** Never silently equate `person_id`, encounter ID, specimen ID, biosample ID, measurement event ID or gene accession. Document a primary key and explicit foreign-key relationships, including expected one-to-many cardinality. Preserve native identifiers in a protected source layer; avoid putting direct identifiers in public examples.

**Observation identity:** A laboratory result is not identified adequately by a number and free-text label. Record the analyte or coded concept, specimen or matrix, method where applicable, unit, reference context, collection/effective time and status. Use independently generated examples in public teaching.

**Units:** Store original value and unit; construct converted measurements in separate fields with a documented, dimensionally valid formula. Require a conversion audit for `mg/dL` versus `mg/L` and distinguish dimensionless ratios from percentages. UCUM supports machine representation; a code cannot repair an incorrectly labeled source measurement.

**Terminology mapping:** Maintain `source_code`, `source_vocabulary`, `standard_code`, `standard_vocabulary_version`, `mapping_method`, and `mapping_review_status`. A syntactically valid mapped code can still be clinically wrong. Never fabricate code mappings to make a join pass.

**Genomics:** Separate approved gene symbols, stable accessions, transcript identifiers, genome assembly and taxonomy. Gene names are not stable join keys on their own; preserve reference release and any one-to-many mapping ambiguity.

**Provenance and citation:** Dataset history should identify input versions, transformation script versions, parameter sets, generated artifacts, authorship and applicable permissions. Use public-facing manifests that reveal only distributable information. Research package standards do not supersede data use agreements.

## Minimum validation matrix

| Test | Valid scenario | Must detect |
| --- | --- | --- |
| Unit contract | Same unit or documented compatible conversion | Incompatible dimensions or conversion with unknown source unit |
| Observation semantics | Same concept, time context and specimen definition | Same name representing different analytes or specimen contexts |
| Key integrity | Unique entity keys and declared one-to-many joins | Multiple source records multiplying a person-level denominator |
| Temporal integrity | Explicit collection/effective time and zone where relevant | Comparing collection date with result publication time as if identical |
| Vocabulary lineage | Known terminology release and reviewed mapping | Unversioned mappings or ambiguous aliases treated as exact matches |
| Expression identity | Stable feature IDs tied to organism and annotation release | Colliding gene symbols or unmatched feature/sample metadata |
| Provenance | Input, script, parameter and artifact lineage recorded | Output with no attributable source or execution version |
| Rights | Metadata and artifacts allowed by license/permission | Confidential identifiers or restricted datasets in a public release |

## Adoption progression

| Stage | Recommended course integration | Acceptance |
| --- | --- | --- |
| Introductory data science | Explain identifier and unit distinctions | Data dictionary and valid/invalid synthetic examples |
| Biostatistics | Align measurements, denominators and observation units | Join and unit audits before inference |
| Epidemiology / surveys | Introduce coding and observation windows | Explicit sample design and case definitions |
| Clinical informatics | Introduce FHIR, OMOP and terminology versioning | Versioned source-to-target mapping review |
| Genomics | Introduce stable accessions and annotation releases | Reproducible feature/sample identity checks |
| AI/ML | Add provenance, leakage prevention and target/label definitions | Model evaluation contracts, dataset lineage and rights review |

This document is a public reference matrix; implement executable validators in a separately reviewed code change. Source-dependent lessons or course-specific comparisons remain subject to the repository's local source-publication guard.

## Review limitations

These references vary in license, scope and release schedule. Validate official links and version applicability at the time of implementation. A matrix entry is not a verified local adapter, an approved terminology map, or proof of regulatory compliance.
