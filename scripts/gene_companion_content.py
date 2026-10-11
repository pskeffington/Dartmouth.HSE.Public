"""Independently curated public teaching content, version 1 (2026-10-10).

Gene identity facts: HGNC (CC0), independently cross-checked against NCBI and
Ensembl public records. Explanations and narrow literature interpretations are
original. No source abstracts, private research tables or classifier weights
are reproduced. Review extent is a claim-level boundary, not paper approval.
"""

ACCESS_DATE = '2026-10-10'
ORIGINAL_GENES = ['ESR1', 'PGR', 'GATA3', 'FOXA1', 'KRT8', 'KRT18', 'ERBB2', 'EGFR', 'MKI67', 'PIK3CA', 'TP53', 'BRCA1', 'BRCA2', 'FOXC1', 'KRT5', 'KRT14', 'KRT17', 'CDH1', 'VIM', 'MMP9', 'CD274']
STUDIES = {'TCGA': {'pmid': '23000897',
          'doi': '10.1038/nature11412',
          'title': 'Comprehensive molecular portraits of human breast tumours.',
          'year': '2012',
          'status': 'ABSTRACT_ONLY',
          'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                           'and results not independently audited.',
          'access_date': '2026-10-10'},
 'PAM50': {'pmid': '19204204',
           'doi': '10.1200/jco.2008.18.1370',
           'title': 'Supervised risk predictor of breast cancer based on intrinsic subtypes.',
           'year': '2009',
           'status': 'ABSTRACT_ONLY',
           'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                            'and results not independently audited.',
           'access_date': '2026-10-10'},
 'RISK': {'pmid': '33471974',
          'doi': '10.1056/nejmoa2005936',
          'title': 'A Population-Based Study of Genes Previously Implicated in Breast Cancer.',
          'year': '2021',
          'status': 'ABSTRACT_ONLY',
          'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                           'and results not independently audited.',
          'access_date': '2026-10-10'},
 'FOXA1': {'pmid': '21151129',
           'doi': '10.1038/ng.730',
           'title': 'FOXA1 is a key determinant of estrogen receptor function and endocrine '
                    'response.',
           'year': '2011',
           'status': 'ABSTRACT_ONLY',
           'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                            'and results not independently audited.',
           'access_date': '2026-10-10'},
 'FOXC1': {'pmid': '20406990',
           'doi': '10.1158/0008-5472.can-09-4120',
           'title': 'FOXC1 is a potential prognostic biomarker with functional significance in '
                    'basal-like breast cancer.',
           'year': '2010',
           'status': 'ABSTRACT_ONLY',
           'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                            'and results not independently audited.',
           'access_date': '2026-10-10'},
 'XBP1': {'pmid': '24670641',
          'doi': '10.1038/nature13119',
          'title': 'XBP1 promotes triple-negative breast cancer by controlling the HIF1α pathway.',
          'year': '2014',
          'status': 'ABSTRACT_ONLY',
          'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                           'and results not independently audited.',
          'access_date': '2026-10-10'},
 'MALAT1_2016': {'pmid': '26701265',
                 'doi': '10.1101/gad.270959.115',
                 'title': 'Differentiation of mammary tumors and reduction in metastasis upon '
                          'Malat1 lncRNA loss.',
                 'year': '2016',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'MALAT1_2018': {'pmid': '30349115',
                 'doi': '10.1038/s41588-018-0252-3',
                 'title': 'Long noncoding RNA MALAT1 suppresses breast cancer metastasis.',
                 'year': '2018',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'MALAT1_2024': {'pmid': '38195932',
                 'doi': '10.1038/s43018-023-00695-9',
                 'title': 'LncRNA Malat1 suppresses pyroptosis and T cell-mediated killing of '
                          'incipient metastatic cells.',
                 'year': '2024',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'AKT_TRIAL': {'pmid': '37256976',
               'doi': '10.1056/nejmoa2214131',
               'title': 'Capivasertib in Hormone Receptor-Positive Advanced Breast Cancer.',
               'year': '2023',
               'status': 'ABSTRACT_ONLY',
               'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                'supplements and results not independently audited.',
               'access_date': '2026-10-10'},
 'CDK_TRIAL': {'pmid': '38507751',
               'doi': '10.1056/nejmoa2305488',
               'title': 'Ribociclib plus Endocrine Therapy in Early Breast Cancer.',
               'year': '2024',
               'status': 'ABSTRACT_ONLY',
               'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                'supplements and results not independently audited.',
               'access_date': '2026-10-10'},
 'MTOR_TRIAL': {'pmid': '22149876',
                'doi': '10.1056/nejmoa1109653',
                'title': 'Everolimus in postmenopausal hormone-receptor-positive advanced breast '
                         'cancer.',
                'year': '2012',
                'status': 'ABSTRACT_ONLY',
                'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                 'supplements and results not independently audited.',
                'access_date': '2026-10-10'},
 'NORMAL': {'pmid': '38548988',
            'doi': '10.1038/s41588-024-01688-9',
            'title': 'A single-cell atlas enables mapping of homeostatic cellular shifts in the '
                     'adult human breast.',
            'year': '2024',
            'status': 'ABSTRACT_ONLY',
            'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                             'supplements and results not independently audited.',
            'access_date': '2026-10-10'},
 'WU': {'pmid': '34493872',
        'doi': '10.1038/s41588-021-00911-1',
        'title': 'A single-cell and spatially resolved atlas of human breast cancers.',
        'year': '2021',
        'status': 'ABSTRACT_ONLY',
        'review_extent': 'Bibliographic record and abstract reviewed; full methods, supplements '
                         'and results not independently audited.',
        'access_date': '2026-10-10'},
 'RECENT_AURKA': {'pmid': '42289849',
                  'doi': '10.1042/bsr20253828',
                  'title': 'A peripheral blood-based approach involving vimentin along with AURKA '
                           'enabled efficient tracking of elusive Oct4/Sox2-expressing '
                           'disseminated breast cancer stem cells.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_BAX': {'pmid': '42384357',
                'doi': '10.1007/s10528-026-11423-0',
                'title': 'VALD-3 Induces GSDME-Dependent Pyroptosis via ROS/JNK/Bax Pathway in '
                         'Triple-Negative Breast Cancer Cells.',
                'year': '2026',
                'status': 'ABSTRACT_ONLY',
                'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                 'supplements and results not independently audited.',
                'access_date': '2026-10-10'},
 'RECENT_BCL2': {'pmid': '42320114',
                 'doi': '10.1016/j.bioorg.2026.110112',
                 'title': 'Discovery of new thiazolyl hydrazone derivatives as anti-breast cancer '
                          'agents: Synthesis, biological evaluation and in silico studies.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_CCNB1': {'pmid': '42515730',
                  'doi': '10.3390/ph19071048',
                  'title': 'An Integrated Cellular Computational Pipeline Decodes Luteolin to '
                           'Design Possible Allosteric CDK1/CYCLIN B1 Inhibitors That Overcome '
                           'Breast Cancer Stemness.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_CCND1': {'pmid': '42811741',
                  'doi': '10.1002/cam4.72331',
                  'title': 'Optimizing the ER Cutoff in HER2-Positive Breast Cancer: ER\u2009'
                           '≥\u200950% Predicts Low pCR Rates and Resistance to Antibody-Drug '
                           'Conjugates in the Neoadjuvant Setting.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_CCNE1': {'pmid': '42517982',
                  'doi': '10.1007/s12094-026-04477-4',
                  'title': 'Assessing the significance of CCNE1 overexpression in triple negative '
                           'breast cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_CD274': {'pmid': '41549178',
                  'doi': '10.1007/s00210-026-04978-7',
                  'title': 'Integrative transcriptomic and structural modeling reveal CASP1, TLR3, '
                           'PYCARD, and CD274 as immune-modulatory drivers in breast cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_CD3D': {'pmid': '42065189',
                 'doi': '10.1097/md.0000000000048367',
                 'title': 'Exploration of CD2 and CD3D as potential immune-related biomarkers for '
                          'IORT in breast cancer treatment.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_CD68': {'pmid': '42615360',
                 'doi': '10.1369/00221554261474562',
                 'title': 'Detection of Human Cytomegalovirus <i>lncRNA4.9</i> in Breast Tumor '
                          'Tissue Using RNA In Situ Hybridization.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_CD8A': {'pmid': '42794881',
                 'doi': '10.3390/cancers18182913',
                 'title': 'HSP90AA1 Knockdown Enhances Doxorubicin Sensitivity by Promoting '
                          'Immunogenic Cell Death-Related Signaling and Immune-Related Tumor '
                          'Microenvironment Remodeling in Breast Cancer.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_CDC20': {'pmid': '42620215',
                  'doi': '10.3389/fonc.2026.1899923',
                  'title': 'LncTRDMT1-5 promotes chromosomal instability through MSRB3-mediated '
                           'cell cycle and DNA damage in breast cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_CDH1': {'pmid': '42641685',
                 'doi': '10.1016/j.modpat.2026.101072',
                 'title': 'A Transcriptional ILCness Score Reveals Lobular-like Biology and '
                          'Clinical Behavior Beyond CDH1 Mutation Status.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_CDKN1A': {'pmid': '42065068',
                   'doi': '10.32604/or.2026.074965',
                   'title': 'CDKN1A/p21 Influences the Survival and Expansion of Breast Cancer '
                            'Stem Cells after Oxidative Damage.',
                   'year': '2026',
                   'status': 'ABSTRACT_ONLY',
                   'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                    'supplements and results not independently audited.',
                   'access_date': '2026-10-10'},
 'RECENT_COL1A1': {'pmid': '42464413',
                   'doi': '10.1186/s13062-026-00869-2',
                   'title': 'SERPINH1 expression represents a reliable biomarker of human breast '
                            'cancer aggressiveness.',
                   'year': '2026',
                   'status': 'ABSTRACT_ONLY',
                   'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                    'supplements and results not independently audited.',
                   'access_date': '2026-10-10'},
 'RECENT_CXCL12': {'pmid': '41902967',
                   'doi': '10.1007/s10238-026-02126-2',
                   'title': 'CXCL12-mediated T cell infiltration drives breast cancer metastasis.',
                   'year': '2026',
                   'status': 'ABSTRACT_ONLY',
                   'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                    'supplements and results not independently audited.',
                   'access_date': '2026-10-10'},
 'RECENT_EGFR': {'pmid': '42469310',
                 'doi': '10.1038/s41598-026-62101-5',
                 'title': "Inhibitory effects of 2'-nitroflavone and apigenin on EGFR signaling in "
                          'breast cancer cells.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_EPCAM': {'pmid': '42708763',
                  'doi': '10.1021/acs.analchem.6c01556',
                  'title': 'Single-Exosome EpCAM Heterogeneity Profiling for Breast Cancer '
                           'Diagnosis and Progression Monitoring.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_ERBB3': {'pmid': '42648410',
                  'doi': '10.1016/j.jep.2026.122321',
                  'title': 'Anti-breast cancer effects of the Xingxiao Pill are associated with '
                           'inhibition of the ErbB3/PI3K/AKT/mTOR pathway, modulation of amino '
                           'acid metabolism, and promotion of apoptosis.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_ERBB4': {'pmid': '41716632',
                  'doi': '10.1016/j.gendis.2025.101691',
                  'title': 'NRG4 suppresses breast cancer metastasis via ERBB4-YAP1-mediated '
                           'down-regulation of MMPs.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_FGFR1': {'pmid': '42617046',
                  'doi': '10.1158/2767-9764.crc-25-0821',
                  'title': 'FGFR1 Suppresses STING-Mediated Interferon Response in Endocrine '
                           'Therapy-Resistant Breast Cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_FN1': {'pmid': '42085441',
                'doi': '10.1371/journal.pone.0348500',
                'title': "Plasma small-extracellular vesicles' proteomic signature in neoadjuvant "
                         'chemotherapy-naïve breast cancer patients.',
                'year': '2026',
                'status': 'ABSTRACT_ONLY',
                'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                 'supplements and results not independently audited.',
                'access_date': '2026-10-10'},
 'RECENT_HIF1A': {'pmid': '42480772',
                  'doi': '10.1016/j.bbadis.2026.168379',
                  'title': 'HNRNPF-driven retention of exon 14 in HIF1A pre-mRNA promotes breast '
                           'cancer metastasis.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_ITGA6': {'pmid': '41735581',
                  'doi': '10.1038/s41416-026-03347-8',
                  'title': 'ASH2L induces tamoxifen resistance via H3K4me3 dependent ITGA6/ERK '
                           'signaling in ER-positive breast cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_KRT14': {'pmid': '42031621',
                  'doi': '10.1016/j.ebiom.2026.106241',
                  'title': 'MechanoAge, a machine learning platform to identify individuals '
                           'susceptible to breast cancer based on mechanical properties of single '
                           'cells.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_KRT17': {'pmid': '41888575',
                  'doi': '10.1038/s42003-026-09897-0',
                  'title': 'KRT17 promotes triple negative breast cancer through activation of Wnt '
                           'signaling and γδ T-cells recruitment.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_KRT18': {'pmid': '42256294',
                  'doi': '10.1016/j.isci.2026.116155',
                  'title': 'Single-cell transcriptomics profiling elucidates RBP-driven metastatic '
                           'signaling pathways in ER<sup>+</sup> breast cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_KRT19': {'pmid': '40806403',
                  'doi': '10.3390/ijms26157269',
                  'title': 'Impact of Copper Nanoparticles on Keratin 19 (KRT19) Gene Expression '
                           'in Breast Cancer Subtypes: Integrating Experimental and Bioinformatics '
                           'Approaches.',
                  'year': '2025',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_KRT5': {'pmid': '42539924',
                 'doi': '10.37349/etat.2026.1002388',
                 'title': 'Distinct transcriptomic features of tumor and stromal cells in direct '
                          'contact in luminal and triple-negative breast cancers.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_KRT8': {'pmid': '38915368',
                 'doi': '10.3389/fonc.2024.1411295',
                 'title': 'Investigating phenotypic plasticity due to toxicants with exposure '
                          'disparities in primary human breast cells <i>in vitro</i>.',
                 'year': '2024',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_MKI67': {'pmid': '41963560',
                  'doi': '10.1245/s10434-026-19620-2',
                  'title': 'Ki67 Gene Expression is Associated with Immune Cell Infiltration and '
                           'Neoadjuvant Chemotherapy Response in ER+/HER2- Breast Cancer.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_MMP9': {'pmid': '42579698',
                 'doi': '10.1371/journal.pone.0355672',
                 'title': 'Mechanistic insights into daidzin from Glycine max against breast '
                          'cancer via network pharmacology and multi-level molecular modeling.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_PDCD1': {'pmid': '41322014',
                  'doi': '10.1177/11795549251399383',
                  'title': 'Machine Learning-Based Enhanced MRI Radiomics for PDCD1 '
                           'Prognostication and Expression Prediction in Breast Cancer.',
                  'year': '2025',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_PTEN': {'pmid': '42795427',
                 'doi': '10.3390/life16091563',
                 'title': 'Distinct Associations of PTEN and TMPRSS4 Expression with Clinical '
                          'Outcomes and Fudan Immunohistochemistry-Based Subtypes in '
                          'Triple-Negative Breast Cancer.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_PTPRC': {'pmid': '40627035',
                  'doi': '10.1007/s10142-025-01654-6',
                  'title': 'Immune-based molecular subtyping of triple-negative breast cancer via '
                           'SNF-CC and functional validation of key immune-associated genes.',
                  'year': '2025',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_RAD51': {'pmid': '42236675',
                  'doi': '10.1038/s41419-026-08912-w',
                  'title': 'MND1 reduces breast cancer chemosensitivity by promoting '
                           'RAD51-mediated homologous recombination repair.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_RB1': {'pmid': '42651837',
                'doi': '10.3390/cimb48080839',
                'title': 'Inorganic Phosphate Is Associated with RB1-E2F-Related Transcriptional '
                         'and DNA Repair-Associated Changes Under Cisplatin Exposure in MDA-MB-231 '
                         'Cells.',
                'year': '2026',
                'status': 'ABSTRACT_ONLY',
                'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                 'supplements and results not independently audited.',
                'access_date': '2026-10-10'},
 'RECENT_SLC2A1': {'pmid': '42456828',
                   'doi': '10.1016/j.bcp.2026.118260',
                   'title': 'EFO2 promotes triple-negative breast cancer progression and reduces '
                            'CD8<sup>+</sup> T cell-mediated killing by acetylating USF1 to '
                            'enhance SLC2A1-mediated glycolysis.',
                   'year': '2026',
                   'status': 'ABSTRACT_ONLY',
                   'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                    'supplements and results not independently audited.',
                   'access_date': '2026-10-10'},
 'RECENT_STAT1': {'pmid': '41974939',
                  'doi': '10.1038/s44318-026-00766-4',
                  'title': 'Chromosomal instability promotes cell migration and invasion via '
                           'EFEMP1 secretion into extracellular vesicles.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_TOP2A': {'pmid': '41851614',
                  'doi': '10.1186/s11658-026-00902-2',
                  'title': 'STUB1 downregulates TOP2A through a dual mechanism of ubiquitination '
                           'and FOXM1-mediated transcription repression, suppressing breast cancer '
                           'growth and enhancing sensitivity to chemotherapy.',
                  'year': '2026',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'},
 'RECENT_TP53': {'pmid': '42607633',
                 'doi': '10.1016/j.canep.2026.103204',
                 'title': 'TP53 mutations predict poor breast cancer-specific survival in '
                          'ER-positive breast cancer patients.',
                 'year': '2026',
                 'status': 'ABSTRACT_ONLY',
                 'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                  'supplements and results not independently audited.',
                 'access_date': '2026-10-10'},
 'RECENT_VIM': {'pmid': '42058674',
                'doi': '10.1155/humu/8880918',
                'title': 'Targeting the Vim-PGI<sub>2</sub> Pathway Enhances CD8<sup>+</sup> T '
                         'Cell-Mediated Antitumor Immunity in Breast Cancer.',
                'year': '2026',
                'status': 'ABSTRACT_ONLY',
                'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                 'supplements and results not independently audited.',
                'access_date': '2026-10-10'},
 'PGR_FUNCTION': {'pmid': '26153859',
                  'doi': '10.1038/nature14583',
                  'title': 'Progesterone receptor modulates ERα action in breast cancer.',
                  'year': '2015',
                  'status': 'ABSTRACT_ONLY',
                  'review_extent': 'Bibliographic record and abstract reviewed; full methods, '
                                   'supplements and results not independently audited.',
                  'access_date': '2026-10-10'}}

GENES = [{'symbol': 'AKT1',
  'name': 'AKT serine/threonine kinase 1',
  'hgnc_id': 'HGNC:391',
  'entrez_id': '207',
  'ensembl_gene_id': 'ENSG00000142208',
  'alias_symbol': 'RAC|PKB|PRKBA|AKT|RAC-alpha',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth', 'metabolism'],
  'product': 'signaling kinase',
  'normal': 'AKT1 carries growth and survival messages inside cells. Its activity changes when '
            'upstream signals recruit and phosphorylate the protein.',
  'research': 'Separate a changed signaling state from a changed number of AKT1 transcripts.',
  'measurement': 'Compare total AKT1 protein with phosphorylated AKT1 after a controlled stimulus.',
  'limitation': 'RNA abundance does not reveal an activating AKT1 variant or kinase activity.',
  'question': 'Can two specimens with similar AKT1 RNA have different signaling activity?',
  'study': 'AKT_TRIAL',
  'design': 'Randomized phase 3 trial',
  'model': 'Hormone-receptor-positive, HER2-negative advanced breast cancer after '
           'aromatase-inhibitor treatment',
  'finding': 'Adding capivasertib to fulvestrant improved progression-free survival in the studied '
             'population, including an alteration-defined subgroup.',
  'claim_limit': 'An AKT-pathway intervention is relevant to this signaling gene; a drug trial '
                 'does not make AKT1 RNA a treatment-selection test.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ATM',
  'name': 'ATM serine/threonine kinase',
  'hgnc_id': 'HGNC:795',
  'entrez_id': '472',
  'ensembl_gene_id': 'ENSG00000149311',
  'alias_symbol': 'TEL1|TELO1',
  'prev_symbol': 'ATA|ATDC|ATC|ATD',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'DNA-damage sensor kinase',
  'normal': 'ATM helps cells recognize DNA damage and coordinate repair or a pause in division. It '
            'is a signaling controller rather than a repair enzyme that directly replaces damaged '
            'bases.',
  'research': 'Learn why inherited variant studies and tumor stress responses answer different '
              'questions.',
  'measurement': 'A DNA variant assay asks about sequence; phosphorylation assays ask about a '
                 'damage response.',
  'limitation': 'An ATM variant of uncertain significance is not equivalent to a pathogenic '
                'inherited variant.',
  'question': 'What evidence distinguishes an inherited risk association from a transient repair '
              'response?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic germline ATM variants were associated with breast cancer risk, '
             'particularly ER-positive disease.',
  'claim_limit': 'Risk pertains to classified DNA variants and population ascertainment, not high '
                 'or low ATM expression.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'AURKA',
  'name': 'aurora kinase A',
  'hgnc_id': 'HGNC:11393',
  'entrez_id': '6790',
  'ensembl_gene_id': 'ENSG00000087586',
  'alias_symbol': 'BTAK|AurA|STK7|ARK1|PPP1R47|AIK',
  'prev_symbol': 'STK15|STK6',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation'],
  'product': 'mitotic kinase',
  'normal': 'AURKA helps organize the machinery that separates duplicated chromosomes. Timing and '
            'location of its activity matter for orderly cell division.',
  'research': 'Use a mitotic regulator to ask whether a proliferation signal reflects more '
              'dividing cells or altered control within those cells.',
  'measurement': 'Protein location and phosphorylation add information beyond a bulk RNA count.',
  'limitation': 'AURKA RNA is not a direct measure of spindle accuracy or response to an '
                'inhibitor.',
  'question': 'Would the association remain after comparing cells at the same cell-cycle stage?',
  'study': 'RECENT_AURKA',
  'design': 'Exploratory circulating-cell marker study',
  'model': 'Blood-associated breast cancer cells and experimental cell models',
  'finding': 'The investigators evaluated AURKA with vimentin in identifying heterogeneous '
             'Oct4/Sox2-expressing cells.',
  'claim_limit': 'The multi-marker approach is exploratory; blood RNA or one marker does not '
                 'establish a validated screening assay.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'BARD1',
  'name': 'BRCA1 associated RING domain 1',
  'hgnc_id': 'HGNC:952',
  'entrez_id': '580',
  'ensembl_gene_id': 'ENSG00000138376',
  'alias_symbol': '',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'DNA-repair partner',
  'normal': 'BARD1 partners with BRCA1 in responses to damaged DNA. Cooperation between the '
            'proteins helps protect chromosome integrity.',
  'research': 'Connect a repair complex to inherited-variant research without confusing a variant '
              'with low expression.',
  'measurement': 'Sequence testing, loss of the remaining functional allele and repair assays '
                 'examine different steps.',
  'limitation': 'Not every BARD1 variant disrupts repair or carries the same risk.',
  'question': 'How would a functional assay help classify a rare variant?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic BARD1 variants showed associations with ER-negative and triple-negative '
             'disease.',
  'claim_limit': 'Inherited variant risk is distinct from RNA abundance, and clinical '
                 'triple-negative categories are not PAM50 labels.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'BAX',
  'name': 'BCL2 associated X, apoptosis regulator',
  'hgnc_id': 'HGNC:959',
  'entrez_id': '581',
  'ensembl_gene_id': 'ENSG00000087088',
  'alias_symbol': 'BCL2L4',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression'],
  'product': 'cell-death regulator',
  'normal': 'BAX participates in the mitochondrial route to programmed cell death. Activation and '
            'movement of the protein help control whether a stressed cell proceeds toward death.',
  'research': 'Investigate why a cell can contain BAX RNA yet remain alive after a stressor.',
  'measurement': 'Localization, protein conformation and downstream cell-death assays are more '
                 'informative about activation than RNA alone.',
  'limitation': 'A larger BAX transcript count does not prove that apoptosis has occurred.',
  'question': 'What measurements distinguish a prepared death pathway from an activated one?',
  'study': 'RECENT_BAX',
  'design': 'Compound perturbation study',
  'model': 'Triple-negative breast cancer cell models',
  'finding': 'VALD-3 experiments implicated ROS/JNK/Bax signaling in GSDME-dependent cell death.',
  'claim_limit': 'The compound, cell model and death pathway matter; no patient benefit or '
                 'BAX-based drug eligibility was established.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'BCL2',
  'name': 'BCL2 apoptosis regulator',
  'hgnc_id': 'HGNC:990',
  'entrez_id': '596',
  'ensembl_gene_id': 'ENSG00000171791',
  'alias_symbol': 'Bcl-2|PPP1R50',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression'],
  'product': 'cell-survival regulator',
  'normal': 'BCL2 can restrain mitochondrial cell-death signaling. Normal cells use such controls '
            'to avoid unnecessary loss while balancing survival against damage.',
  'research': 'Study the balance between survival signals and cell death rather than treating '
              'every survival protein as the same type of cancer marker.',
  'measurement': 'Compare BCL2 protein, interacting partners and a cell-death endpoint.',
  'limitation': 'BCL2 expression cannot independently establish a treatment response or an '
                "individual's prognosis.",
  'question': 'How could high survival-protein abundance coexist with sensitivity to a different '
              'stress?',
  'study': 'RECENT_BCL2',
  'design': 'Compound synthesis and cell experiments with modeling',
  'model': 'Human breast cancer cell models and computational docking',
  'finding': 'Thiazolyl hydrazone experiments investigated cell death alongside modeled protein '
             'interactions.',
  'claim_limit': 'Docking and expression shifts do not establish direct BCL2 binding or clinical '
                 'efficacy.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'BRCA1',
  'name': 'BRCA1 DNA repair associated',
  'hgnc_id': 'HGNC:1100',
  'entrez_id': '672',
  'ensembl_gene_id': 'ENSG00000012048',
  'alias_symbol': 'RNF53|BRCC1|PPP1R53|FANCS',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'DNA-repair coordinator',
  'normal': 'BRCA1 helps coordinate responses to DNA breaks and supports accurate repair using a '
            'matching DNA template. Its functions involve protein partners and cell-cycle context.',
  'research': 'Learn the distinction between inherited predisposition and repair behavior in a '
              'tumor.',
  'measurement': 'Germline DNA, tumor DNA, RNA and repair-function assays have different '
                 'denominators and meanings.',
  'limitation': 'BRCA1 RNA cannot diagnose an inherited pathogenic variant or establish repair '
                'deficiency.',
  'question': 'Which additional evidence would connect a sequence change to impaired repair?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic germline BRCA1 variants were associated with breast cancer risk.',
  'claim_limit': 'A classified inherited variant is not interchangeable with tumor expression, '
                 'somatic mutation or family history alone.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'BRCA2',
  'name': 'BRCA2 DNA repair associated',
  'hgnc_id': 'HGNC:1101',
  'entrez_id': '675',
  'ensembl_gene_id': 'ENSG00000139618',
  'alias_symbol': 'FAD|FAD1|BRCC2|XRCC11',
  'prev_symbol': 'FANCD1|FACD|FANCD',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'DNA-repair coordinator',
  'normal': 'BRCA2 helps position RAD51 for template-guided repair of broken DNA. It supports a '
            'repair process whose success depends on multiple proteins.',
  'research': 'Follow the path from a DNA variant to a functional repair experiment and then to a '
              'population association.',
  'measurement': 'Sequence a defined tissue or germline sample and distinguish the result from RNA '
                 'expression.',
  'limitation': 'An uncertain BRCA2 variant is not automatically harmful; normal RNA does not '
                'prove normal protein function.',
  'question': 'How would functional and family evidence complement each other?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic germline BRCA2 variants were associated with breast cancer risk.',
  'claim_limit': 'Risk estimates refer to pathogenic variants, not every DNA change or reduced '
                 'transcript abundance.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CCNB1',
  'name': 'cyclin B1',
  'hgnc_id': 'HGNC:1579',
  'entrez_id': '891',
  'ensembl_gene_id': 'ENSG00000134057',
  'alias_symbol': '',
  'prev_symbol': 'CCNB',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation'],
  'product': 'cell-cycle cyclin',
  'normal': 'Cyclin B1 helps control entry into mitosis through its kinase partners. Its '
            'concentration changes over the cell cycle and is regulated by protein destruction as '
            'well as production.',
  'research': 'Ask whether elevated cell-cycle RNA reflects cell-cycle timing or a larger '
              'proliferating population.',
  'measurement': 'Time-resolved protein and cell-cycle measurements can explain differences hidden '
                 'by one bulk RNA value.',
  'limitation': 'CCNB1 alone cannot identify a molecular subtype or demonstrate uncontrolled '
                'division.',
  'question': 'Would synchronized cells change the interpretation of the same RNA difference?',
  'study': 'RECENT_CCNB1',
  'design': 'Computational screening with cellular follow-up',
  'model': 'Normal and breast cancer cell lines plus engineered HEK293T cells',
  'finding': 'The investigators examined luteolin and CCNB1-related proliferation signals with '
             'engineered-cell experiments.',
  'claim_limit': 'A non-breast engineered cell model and computational selection do not establish '
                 'CCNB1-dependent benefit in patients.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CCND1',
  'name': 'cyclin D1',
  'hgnc_id': 'HGNC:1582',
  'entrez_id': '595',
  'ensembl_gene_id': 'ENSG00000110092',
  'alias_symbol': 'U21B31',
  'prev_symbol': 'BCL1|D11S287E|PRAD1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation', 'growth'],
  'product': 'cell-cycle cyclin',
  'normal': 'Cyclin D1 links growth signals to the decision to enter the DNA-replication cycle. It '
            'works with cyclin-dependent kinases rather than acting as a DNA-copying enzyme.',
  'research': 'Connect growth signaling to cell-cycle control and compare RNA expression with gene '
              'copy number.',
  'measurement': 'DNA copy number, cyclin D1 protein and downstream RB phosphorylation are '
                 'distinct measurements.',
  'limitation': 'High CCND1 RNA is not proof of amplification or sensitivity to a cell-cycle drug.',
  'question': 'Can increased copy number and a changed cellular mixture produce similar bulk RNA '
              'values?',
  'study': 'RECENT_CCND1',
  'design': 'Retrospective cohort with public-data comparisons',
  'model': '741 HER2-positive cases and TCGA/SCAN-B datasets',
  'finding': 'Exploratory ER-expression groups differed in prognosis and CCND1-related biological '
             'context.',
  'claim_limit': 'Research cutoffs and retrospective associations are not a new approved ER '
                 'threshold or a CCND1 clinical assay.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CCNE1',
  'name': 'cyclin E1',
  'hgnc_id': 'HGNC:1589',
  'entrez_id': '898',
  'ensembl_gene_id': 'ENSG00000105173',
  'alias_symbol': '',
  'prev_symbol': 'CCNE',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation'],
  'product': 'cell-cycle cyclin',
  'normal': 'Cyclin E1 helps regulate the transition toward DNA replication with kinase partners. '
            'Normal control depends on when the protein is made and removed.',
  'research': 'Examine proliferation-related heterogeneity without assuming that every rapidly '
              'dividing tumor has the same mechanism.',
  'measurement': 'Measure copy number and protein alongside RNA and cell-cycle fraction.',
  'limitation': 'RNA overexpression alone cannot show that a particular kinase complex drives a '
                'tumor.',
  'question': 'How would you distinguish more cycling cells from greater expression per cycling '
              'cell?',
  'study': 'RECENT_CCNE1',
  'design': 'Cohort analysis with cell perturbation',
  'model': 'Public breast cancer expression cohorts and triple-negative cell models',
  'finding': 'CCNE1 associations were examined with experiments linking cell-cycle effects to mTOR '
             'signaling.',
  'claim_limit': 'Cohort RNA correlations and cell perturbations answer different questions; '
                 'neither alone supplies a clinical cutoff.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CD274',
  'name': 'CD274 molecule',
  'hgnc_id': 'HGNC:17635',
  'entrez_id': '29126',
  'ensembl_gene_id': 'ENSG00000120217',
  'alias_symbol': 'B7-H|B7H1|PD-L1|PDL1|B7-H1',
  'prev_symbol': 'PDCD1LG1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'immune-regulatory ligand',
  'normal': 'CD274 encodes PD-L1, a surface ligand that participates in signals restraining immune '
            'responses. Several cell types can carry the protein.',
  'research': 'Use checkpoint biology to separate the source of an immune signal from a clinical '
              'pathology score.',
  'measurement': 'A validated PD-L1 protein assay has a defined specimen, scoring system and '
                 'clinical use; RNA is a different assay.',
  'limitation': 'Bulk CD274 RNA cannot replace a PD-L1 score or determine immunotherapy '
                'eligibility.',
  'question': 'Which cell populations contribute to the signal and how would spatial measurements '
              'distinguish them?',
  'study': 'RECENT_CD274',
  'design': 'Computational expression, survival and structural modeling',
  'model': 'Public breast cancer expression cohorts and protein models',
  'finding': 'The researchers examined CD274 within immune-associated expression and modeled '
             'variant effects.',
  'claim_limit': 'Expression and structural predictions do not establish a variant mechanism '
                 'experimentally or validate checkpoint-treatment benefit.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CD3D',
  'name': 'CD3 delta subunit of T-cell receptor complex',
  'hgnc_id': 'HGNC:1673',
  'entrez_id': '915',
  'ensembl_gene_id': 'ENSG00000167286',
  'alias_symbol': 'CD3DELTA|CD3-DELTA',
  'prev_symbol': 'T3D',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'T-cell receptor complex component',
  'normal': 'CD3D contributes to the receptor complex through which T cells communicate antigen '
            'recognition to the inside of the cell. It helps coordinate signaling rather than '
            'specifying the antigen by itself.',
  'research': 'Interpret T-cell-associated RNA in a tumor as a possible composition signal.',
  'measurement': 'Cell counting and spatial localization help distinguish more T cells from '
                 'altered expression within T cells.',
  'limitation': 'CD3D abundance does not establish an effective antitumor response.',
  'question': 'Would the signal change after adjusting for the proportion of T cells?',
  'study': 'RECENT_CD3D',
  'design': 'Exploratory transcriptomic comparison',
  'model': '21 intraoperative-radiotherapy and 16 comparison samples',
  'finding': 'CD3D appeared in immune-related transcriptomic analyses of the studied radiotherapy '
             'groups.',
  'claim_limit': 'Small observational groups and immune composition prevent a causal '
                 'treatment-effect interpretation.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CD68',
  'name': 'CD68 molecule',
  'hgnc_id': 'HGNC:1693',
  'entrez_id': '968',
  'ensembl_gene_id': 'ENSG00000129226',
  'alias_symbol': 'SCARD1|GP110|DKFZp686M18236|LAMP4',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'lysosome-associated glycoprotein',
  'normal': 'CD68 is associated with intracellular membrane compartments and is commonly used to '
            "study macrophage-rich populations. A marker's usefulness does not make it exclusive "
            'to one cell state.',
  'research': 'Explore myeloid-cell presence and the limits of broad macrophage markers.',
  'measurement': 'Histology can locate CD68-positive cells; bulk RNA averages their contribution '
                 'with other cells.',
  'limitation': 'CD68 alone cannot classify macrophages into a beneficial or harmful functional '
                'state.',
  'question': "What additional markers and functional observations would identify the cells' "
              'behavior?',
  'study': 'RECENT_CD68',
  'design': 'Tissue in situ and immunohistochemistry study',
  'model': 'Breast cancer tissue samples classified by clinical markers',
  'finding': 'The investigators used CD68 staining while examining virus-associated tissue '
             'signals.',
  'claim_limit': 'Macrophage localization is relevant; co-occurring signals do not prove viral '
                 'causation of breast cancer.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CD8A',
  'name': 'CD8 subunit alpha',
  'hgnc_id': 'HGNC:1706',
  'entrez_id': '925',
  'ensembl_gene_id': 'ENSG00000153563',
  'alias_symbol': 'p32|CD8alpha',
  'prev_symbol': 'CD8',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'immune-cell coreceptor',
  'normal': 'CD8A contributes to a coreceptor involved in immune recognition. It is often useful '
            'for identifying CD8-bearing immune-cell populations.',
  'research': 'Separate immune-cell abundance from immune-cell killing capacity.',
  'measurement': 'Protein localization and functional assays provide information beyond a '
                 'tissue-average transcript.',
  'limitation': 'CD8A RNA alone cannot prove that immune cells recognize or kill tumor cells.',
  'question': 'How would you measure activation and tumor recognition separately from cell number?',
  'study': 'RECENT_CD8A',
  'design': 'Cell and mouse perturbation study',
  'model': 'Breast cancer cells and 4T1 mouse tumors under treatment',
  'finding': 'HSP90AA1 perturbation with doxorubicin was associated with altered CD8A-related '
             'immune signals.',
  'claim_limit': 'Mouse infiltration and marker expression cannot establish individual patient '
                 'treatment response.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CDC20',
  'name': 'cell division cycle 20',
  'hgnc_id': 'HGNC:1723',
  'entrez_id': '991',
  'ensembl_gene_id': 'ENSG00000117399',
  'alias_symbol': 'p55CDC|CDC20A',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation'],
  'product': 'protein-degradation regulator',
  'normal': 'CDC20 helps activate a complex that marks selected proteins for destruction during '
            'cell division. Controlled destruction permits chromosomes to progress through '
            'mitosis.',
  'research': 'Learn that cell-cycle control includes removing proteins, not just producing them.',
  'measurement': 'A mitotic fraction and degradation-pathway assay complement expression '
                 'measurements.',
  'limitation': 'CDC20 RNA does not establish that the chromosome-separation checkpoint is '
                'functioning correctly.',
  'question': 'What happens if a division-associated transcript rises but its checkpoint remains '
              'intact?',
  'study': 'RECENT_CDC20',
  'design': 'Noncoding-RNA perturbation study',
  'model': 'Breast cancer cell models including MDA-MB-231',
  'finding': 'Lnc-TRDMT1-5 experiments implicated an MSRB3/CDC20-related cell-cycle pathway.',
  'claim_limit': 'A model-specific regulatory result does not prove that elevated CDC20 RNA causes '
                 'all breast cancers.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CDH1',
  'name': 'cadherin 1',
  'hgnc_id': 'HGNC:1748',
  'entrez_id': '999',
  'ensembl_gene_id': 'ENSG00000039068',
  'alias_symbol': 'uvomorulin|CD324',
  'prev_symbol': 'UVO',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['adhesion', 'suppression'],
  'product': 'cell-adhesion protein',
  'normal': 'CDH1 encodes E-cadherin, which helps neighboring epithelial cells attach and organize '
            'tissue. Membrane placement and protein partners affect the resulting adhesion.',
  'research': 'Relate epithelial architecture to lobular pathology while keeping histology, '
              'sequence and RNA distinct.',
  'measurement': 'Protein localization, tissue morphology and DNA alterations answer different '
                 'questions.',
  'limitation': 'A CDH1 RNA value alone cannot diagnose invasive lobular carcinoma or prove '
                'E-cadherin loss.',
  'question': 'How could similar transcript levels accompany different membrane-localized protein '
              'patterns?',
  'study': 'RECENT_CDH1',
  'design': 'Expression and histopathology study',
  'model': 'Invasive lobular and non-lobular breast tumors',
  'finding': 'An expression-defined lobular-like continuum was examined in relation to histology '
             'and CDH1 alterations.',
  'claim_limit': 'Expression patterns, histologic diagnosis and CDH1 mutation status were related '
                 'but not identical classifications.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CDK4',
  'name': 'cyclin dependent kinase 4',
  'hgnc_id': 'HGNC:1773',
  'entrez_id': '1019',
  'ensembl_gene_id': 'ENSG00000135446',
  'alias_symbol': 'PSK-J3',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation', 'growth'],
  'product': 'cell-cycle kinase',
  'normal': "CDK4 works with cyclin D proteins to regulate a cell's progression toward DNA "
            'replication. Its effects depend on downstream control proteins, including RB.',
  'research': 'Explore how a defined drug target can be relevant without its RNA being a '
              'drug-selection test.',
  'measurement': 'Kinase inhibition, RB phosphorylation and growth endpoints examine pathway '
                 'function.',
  'limitation': 'CDK4 RNA cannot determine treatment eligibility, response or the integrity of '
                'downstream RB control.',
  'question': 'How could a tumor bypass a blocked cell-cycle step?',
  'study': 'CDK_TRIAL',
  'design': 'Randomized phase 3 trial',
  'model': 'HR-positive, HER2-negative stage II or III early breast cancer',
  'finding': 'Ribociclib plus endocrine therapy improved invasive disease-free survival in the '
             'studied setting.',
  'claim_limit': 'Ribociclib targets CDK4/6 activity; CDK4 transcript abundance was not '
                 'established as an independent selection assay.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CDK6',
  'name': 'cyclin dependent kinase 6',
  'hgnc_id': 'HGNC:1777',
  'entrez_id': '1021',
  'ensembl_gene_id': 'ENSG00000105810',
  'alias_symbol': 'PLSTIRE',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation', 'growth'],
  'product': 'cell-cycle kinase',
  'normal': 'CDK6 participates in cell-cycle control and can also influence '
            'differentiation-related programs. Its kinase role overlaps with, but is not identical '
            'to, that of CDK4.',
  'research': 'Compare related proteins without assuming that similar names imply interchangeable '
              'biology.',
  'measurement': 'Measure protein abundance, kinase activity and cell-cycle outcomes separately.',
  'limitation': 'CDK6 expression alone cannot establish dependency on CDK4/6 signaling.',
  'question': 'What experiment would separate a kinase-dependent effect from another CDK6 '
              'function?',
  'study': 'CDK_TRIAL',
  'design': 'Randomized phase 3 trial',
  'model': 'HR-positive, HER2-negative stage II or III early breast cancer',
  'finding': 'Ribociclib plus endocrine therapy improved invasive disease-free survival in the '
             'studied setting.',
  'claim_limit': 'A dual-kinase drug result does not isolate the causal contribution of CDK6 or '
                 'validate its RNA as a biomarker.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CDKN1A',
  'name': 'cyclin dependent kinase inhibitor 1A',
  'hgnc_id': 'HGNC:1784',
  'entrez_id': '1026',
  'ensembl_gene_id': 'ENSG00000124762',
  'alias_symbol': 'P21|CIP1|WAF1|SDI1|CAP20|p21CIP1|p21Cip1/Waf1|p21',
  'prev_symbol': 'CDKN1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression', 'proliferation'],
  'product': 'cell-cycle inhibitor',
  'normal': 'CDKN1A encodes p21, which can slow cell-cycle progression by restraining kinase '
            'complexes. Its consequences depend on stress, cell state and cellular location.',
  'research': 'Learn why a checkpoint-associated signal can accompany either growth arrest or '
              'survival in a particular experiment.',
  'measurement': 'Compare p21 protein location with a direct measure of DNA synthesis or '
                 'cell-cycle distribution.',
  'limitation': 'More p21 RNA does not guarantee permanent growth arrest or a uniformly protective '
                'effect.',
  'question': 'When might a transient pause allow a stressed cell to survive?',
  'study': 'RECENT_CDKN1A',
  'design': 'Oxidative-damage cell experiments',
  'model': 'Three-dimensional breast cancer stem-cell models',
  'finding': 'p21 was investigated in survival and expansion after oxidative injury.',
  'claim_limit': 'Checkpoint proteins can have context-dependent survival roles; a transcript rise '
                 'need not mean permanent growth arrest.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CHEK2',
  'name': 'checkpoint kinase 2',
  'hgnc_id': 'HGNC:16627',
  'entrez_id': '11200',
  'ensembl_gene_id': 'ENSG00000183765',
  'alias_symbol': 'CDS1|CHK2|HuCds1|PP1425|bA444G7',
  'prev_symbol': 'RAD53',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'checkpoint kinase',
  'normal': 'CHEK2 helps relay DNA-damage signals to proteins controlling repair and cell-cycle '
            'decisions. This response connects sensing damage with deciding how to proceed.',
  'research': 'Distinguish inherited-variant associations from tumor expression and uncertain '
              'sequence findings.',
  'measurement': 'Defined DNA variants and damage-induced phosphorylation require different '
                 'assays.',
  'limitation': 'A CHEK2 transcript value is not a hereditary-risk result; variants differ in '
                'consequence.',
  'question': 'How do population and functional evidence help interpret a specific variant?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic CHEK2 variants were associated with breast cancer risk, particularly '
             'ER-positive disease.',
  'claim_limit': 'Variant classification, ancestry and ascertainment matter; RNA cannot supply '
                 'inherited-risk interpretation.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'COL1A1',
  'name': 'collagen type I alpha 1 chain',
  'hgnc_id': 'HGNC:2197',
  'entrez_id': '1277',
  'ensembl_gene_id': 'ENSG00000108821',
  'alias_symbol': 'OI4',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['matrix'],
  'product': 'extracellular matrix protein',
  'normal': 'COL1A1 produces one chain of type I collagen, an important component of tissue '
            'scaffolding. Collagen is assembled, secreted and remodeled outside cells.',
  'research': 'Recognize a stromal signal that may change when fibroblast abundance changes.',
  'measurement': 'RNA, collagen protein and the physical organization of matrix are different '
                 'quantities.',
  'limitation': 'Bulk COL1A1 expression cannot identify which cells made collagen or measure '
                'tissue stiffness.',
  'question': 'Could a larger fibroblast fraction explain a matrix-associated expression '
              'difference?',
  'study': 'RECENT_COL1A1',
  'design': 'Multimodal tissue association study',
  'model': '21 breast carcinomas with molecular and spatial measurements',
  'finding': 'SERPINH1-related analyses included COL1A1 and collagen-rich tissue context.',
  'claim_limit': 'The observed co-expression is not a COL1A1 perturbation experiment, and stromal '
                 'abundance can drive the signal.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'CXCL12',
  'name': 'C-X-C motif chemokine ligand 12',
  'hgnc_id': 'HGNC:10672',
  'entrez_id': '6387',
  'ensembl_gene_id': 'ENSG00000107562',
  'alias_symbol': 'SCYB12|SDF-1a|SDF-1b|PBSF|TLSF-a|TLSF-b|TPAR1',
  'prev_symbol': 'SDF1A|SDF1B|SDF1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['matrix', 'immune'],
  'product': 'secreted chemokine',
  'normal': 'CXCL12 helps guide cell movement and positioning through chemokine signaling. Its '
            'effects depend on producing cells, responding cells and spatial gradients.',
  'research': 'Investigate communication between stromal, immune and epithelial compartments.',
  'measurement': 'Spatial protein gradients and receptor-bearing cells matter beyond a '
                 'tissue-average RNA value.',
  'limitation': 'CXCL12 expression does not by itself establish migration direction or a '
                'metastatic mechanism.',
  'question': 'How would you distinguish a chemokine gradient from a uniform increase in '
              'abundance?',
  'study': 'RECENT_CXCL12',
  'design': 'Tissue profiling and knockdown experiments',
  'model': 'Breast tumor tissue and experimental cell models',
  'finding': 'CXCL12-associated immune context and migration were examined with tissue and cell '
             'assays.',
  'claim_limit': 'Chemokine source cells and receptor availability matter; bulk RNA alone cannot '
                 'demonstrate recruitment or metastasis.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'EGFR',
  'name': 'epidermal growth factor receptor',
  'hgnc_id': 'HGNC:3236',
  'entrez_id': '1956',
  'ensembl_gene_id': 'ENSG00000146648',
  'alias_symbol': 'ERBB1|ERRP',
  'prev_symbol': 'ERBB',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth', 'basal'],
  'product': 'growth-factor receptor',
  'normal': 'EGFR receives extracellular growth-factor messages and transmits them through its '
            'intracellular kinase activity. Receptor abundance and receptor activation are '
            'separable.',
  'research': 'Connect epithelial signaling to basal-associated research without defining a tumor '
              'by one receptor.',
  'measurement': 'Compare total receptor protein, phosphorylation and DNA alterations.',
  'limitation': 'EGFR RNA cannot prove active signaling or justify a therapy used in another '
                'cancer type.',
  'question': 'Can a receptor be plentiful but weakly activated?',
  'study': 'RECENT_EGFR',
  'design': 'Compound and cell-line experiments',
  'model': 'MCF-7 and MDA-MB-231 cells studied with flavones and gefitinib',
  'finding': 'The researchers examined growth-signaling responses in distinct breast cancer cell '
             'models.',
  'claim_limit': 'Cell-line drug combinations do not validate EGFR RNA as a clinical response '
                 'test.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'EPCAM',
  'name': 'epithelial cell adhesion molecule',
  'hgnc_id': 'HGNC:11529',
  'entrez_id': '4072',
  'ensembl_gene_id': 'ENSG00000119888',
  'alias_symbol': 'Ly74|TROP1|GA733-2|EGP34|EGP40|EGP-2|KSA|CD326|Ep-CAM|HEA125|KS1/4|MK-1|MH99|MOC31|MOC-31|323/A3|17-1A|TACST-1|CO-17A|ESA|BerEp4|Ber-Ep4',
  'prev_symbol': 'M4S1|MIC18|TACSTD1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['adhesion'],
  'product': 'epithelial surface protein',
  'normal': 'EPCAM is an epithelial surface protein involved in cell interactions and tissue '
            'organization. It is useful for studying epithelial populations but is not present at '
            'the same level in all epithelial states.',
  'research': 'Examine how selecting EpCAM-positive cells can change the cell populations captured '
              'by an assay.',
  'measurement': 'A surface-protein capture assay and bulk RNA sequencing have different selection '
                 'properties.',
  'limitation': 'EPCAM alone cannot establish malignancy, and low capture does not prove absence '
                'of tumor cells.',
  'question': 'Which epithelial states might a capture strategy underrepresent?',
  'study': 'RECENT_EPCAM',
  'design': 'Exploratory extracellular-vesicle assay development',
  'model': 'MCF-7 and HeLa cell-derived material and serum assays',
  'finding': 'An electrochemical assay used EpCAM-associated exosomes as a detection target.',
  'claim_limit': 'Analytical detection is not a demonstrated population screening benefit; '
                 'non-breast controls and vesicle origin matter.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ERBB2',
  'name': 'erb-b2 receptor tyrosine kinase 2',
  'hgnc_id': 'HGNC:3430',
  'entrez_id': '2064',
  'ensembl_gene_id': 'ENSG00000141736',
  'alias_symbol': 'NEU|HER-2|CD340|HER2|c-ERB2|c-ERB-2|MLN-19|p185(erbB2)',
  'prev_symbol': 'NGL',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth'],
  'product': 'growth-signaling receptor',
  'normal': 'ERBB2 encodes HER2, a receptor that helps transmit growth signals through receptor '
            'partnerships. Receptor quantity, gene copy number and phosphorylation are different '
            'layers of biology.',
  'research': 'Understand why clinical HER2 assessment and an RNA-defined HER2-enriched label are '
              'related but distinct.',
  'measurement': 'Clinical HER2 protein and amplification testing follow defined assay and scoring '
                 'standards.',
  'limitation': 'ERBB2 RNA alone cannot establish HER2 status, subtype or treatment eligibility.',
  'question': 'Which assay is needed to answer a question about amplification rather than '
              'expression?',
  'study': 'TCGA',
  'design': 'Multi-platform molecular profiling',
  'model': 'Primary breast tumors analyzed across DNA, RNA and protein platforms',
  'finding': 'HER2-enriched tumors showed a characteristic molecular context including HER-family '
             'signaling.',
  'claim_limit': 'Expression-defined HER2-enriched status does not equal pathology-defined HER2 '
                 'positivity; clinical assays require their own criteria.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ERBB3',
  'name': 'erb-b2 receptor tyrosine kinase 3',
  'hgnc_id': 'HGNC:3431',
  'entrez_id': '2065',
  'ensembl_gene_id': 'ENSG00000065361',
  'alias_symbol': 'HER3',
  'prev_symbol': 'LCCS2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth'],
  'product': 'receptor signaling partner',
  'normal': 'ERBB3 helps receive growth-factor messages and works with other ERBB receptors. Its '
            'limited intrinsic kinase activity makes receptor partnerships especially important.',
  'research': 'Ask how signaling depends on partners rather than a single receptor transcript.',
  'measurement': 'Measure receptor partners and downstream phosphorylation, not only ERBB3 RNA.',
  'limitation': 'More ERBB3 RNA is not proof that a specific receptor pair is active.',
  'question': "Would removing a partner receptor change the same ligand's effect?",
  'study': 'RECENT_ERBB3',
  'design': 'Compound perturbation and biochemical study',
  'model': 'Eight breast cancer cell lines and 4T1 mouse tumors',
  'finding': 'Xingxiao Pill experiments examined ErbB3/PI3K/AKT/mTOR signaling, including protein '
             'phosphorylation.',
  'claim_limit': 'A complex compound experiment is not a recommendation, and total protein and '
                 'activated protein are different measurements.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ERBB4',
  'name': 'erb-b2 receptor tyrosine kinase 4',
  'hgnc_id': 'HGNC:3432',
  'entrez_id': '2066',
  'ensembl_gene_id': 'ENSG00000178568',
  'alias_symbol': 'ALS19|HER4',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth'],
  'product': 'growth-factor receptor',
  'normal': 'ERBB4 transmits growth-factor signals and has isoforms and processing states that can '
            'affect its behavior. Different molecular forms need not have identical consequences.',
  'research': 'Use a receptor to investigate context-dependent effects instead of labeling all '
              'growth signaling uniformly harmful.',
  'measurement': 'Isoform-sensitive RNA assays and protein-fragment measurements reveal different '
                 'information.',
  'limitation': 'One gene-level RNA total cannot identify the relevant ERBB4 isoform or processed '
                'fragment.',
  'question': 'How could receptor processing change a signaling response?',
  'study': 'RECENT_ERBB4',
  'design': 'Receptor perturbation study',
  'model': 'Mouse and organoid breast cancer models',
  'finding': 'NRG4-ERBB4 signaling was investigated in restraint of metastatic behavior through '
             'YAP-related effects.',
  'claim_limit': 'A growth-factor receptor can have context-dependent effects; receptor expression '
                 'alone does not determine metastatic risk.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ESR1',
  'name': 'estrogen receptor 1',
  'hgnc_id': 'HGNC:3467',
  'entrez_id': '2099',
  'ensembl_gene_id': 'ENSG00000091831',
  'alias_symbol': 'ER|NR3A1|Era|ER-alpha',
  'prev_symbol': 'ESR',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'transcription'],
  'product': 'hormone-responsive transcription factor',
  'normal': 'ESR1 encodes estrogen receptor alpha, which helps regulate gene transcription in '
            'response to hormonal and cellular context. Access to DNA and cooperating proteins '
            'influence which targets respond.',
  'research': 'Relate luminal transcription to receptor biology while separating clinical protein '
              'status from RNA.',
  'measurement': 'ER immunohistochemistry, ESR1 sequencing and RNA expression measure different '
                 'properties.',
  'limitation': 'RNA abundance cannot establish an ESR1 mutation, clinical ER status or endocrine '
                'response.',
  'question': 'How could the same receptor abundance produce different transcriptional responses?',
  'study': 'TCGA',
  'design': 'Multi-platform molecular profiling',
  'model': 'Primary breast tumors across intrinsic molecular subtypes',
  'finding': 'Luminal tumors shared hormone-related biology but differed in other molecular '
             'features.',
  'claim_limit': 'A broad luminal association is not a single-gene classifier or evidence that '
                 'ESR1 RNA determines endocrine eligibility.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'FGFR1',
  'name': 'fibroblast growth factor receptor 1',
  'hgnc_id': 'HGNC:3688',
  'entrez_id': '2260',
  'ensembl_gene_id': 'ENSG00000077782',
  'alias_symbol': 'H2|H3|H4|H5|CEK|FLG|BFGFR|N-SAM|CD331',
  'prev_symbol': 'FLT2|KAL2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth'],
  'product': 'growth-factor receptor',
  'normal': 'FGFR1 receives fibroblast growth-factor signals and activates intracellular '
            'communication pathways. Signal output depends on ligands, receptor forms and cellular '
            'context.',
  'research': 'Compare amplification-associated research with receptor abundance and '
              'endocrine-resistant model systems.',
  'measurement': 'Copy-number assays and activated receptor protein are distinct from normalized '
                 'RNA.',
  'limitation': 'High FGFR1 RNA does not prove amplification or sensitivity to receptor '
                'inhibition.',
  'question': 'Would a copy-number change predict signaling equally well in different cell types?',
  'study': 'RECENT_FGFR1',
  'design': 'Resistance-model perturbation with cohort context',
  'model': 'ER-positive resistant models, FGFR1-amplified xenografts and public cohorts',
  'finding': 'FGFR1-related experiments examined interferon and STING responses in endocrine '
             'resistance.',
  'claim_limit': 'Amplification, pathway activity and RNA differ; a model-specific resistance '
                 'mechanism is not a universal selection rule.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'FN1',
  'name': 'fibronectin 1',
  'hgnc_id': 'HGNC:3778',
  'entrez_id': '2335',
  'ensembl_gene_id': 'ENSG00000115414',
  'alias_symbol': 'MSF|CIG|LETS|GFND2|FINC|lnc-ABCA12-8',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['matrix', 'adhesion'],
  'product': 'extracellular matrix glycoprotein',
  'normal': 'FN1 encodes fibronectin, an extracellular protein that helps cells attach to and '
            'organize their surroundings. Its forms and assembly influence the matrix environment.',
  'research': 'Interpret tissue-remodeling signals that can come from stromal as well as '
              'epithelial cells.',
  'measurement': 'Protein deposition and matrix organization complement RNA measurements.',
  'limitation': 'A bulk FN1 increase does not prove that tumor cells acquired a migratory state.',
  'question': 'Which producing cells account for the extracellular protein in a section?',
  'study': 'RECENT_FN1',
  'design': 'Extracellular-vesicle proteomics and cell assays',
  'model': '76 breast cancer cases and 36 obese controls',
  'finding': 'Plasma-vesicle protein analyses included fibronectin alongside cellular follow-up.',
  'claim_limit': 'Protein cargo and control selection limit transport to tumor RNA or population '
                 'screening.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'FOXA1',
  'name': 'forkhead box A1',
  'hgnc_id': 'HGNC:5021',
  'entrez_id': '3169',
  'ensembl_gene_id': 'ENSG00000129514',
  'alias_symbol': '',
  'prev_symbol': 'HNF3A',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'transcription'],
  'product': 'pioneer transcription factor',
  'normal': 'FOXA1 helps make selected DNA regions accessible to regulatory proteins. This access '
            'can shape which hormone-responsive transcriptional programs a cell can use.',
  'research': 'Study the relationship between cell identity, chromatin accessibility and '
              'estrogen-receptor function.',
  'measurement': 'Chromatin accessibility and DNA binding test properties not measured by FOXA1 '
                 'RNA.',
  'limitation': 'One transcript does not describe the entire accessible chromatin landscape.',
  'question': 'Can the same hormone signal have different effects when accessible DNA regions '
              'differ?',
  'study': 'FOXA1',
  'design': 'Genome-binding and functional perturbation study',
  'model': 'Estrogen-receptor breast cancer cell models and tumor-expression context',
  'finding': 'FOXA1 was examined as a determinant of estrogen-receptor genomic binding and '
             'endocrine response.',
  'claim_limit': 'A regulatory requirement in tested models does not mean FOXA1 RNA alone predicts '
                 'every endocrine response.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'FOXC1',
  'name': 'forkhead box C1',
  'hgnc_id': 'HGNC:3800',
  'entrez_id': '2296',
  'ensembl_gene_id': 'ENSG00000054598',
  'alias_symbol': 'FREAC3|ARA|IGDA|IHG1',
  'prev_symbol': 'FKHL7|IRID1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['basal', 'transcription'],
  'product': 'transcription factor',
  'normal': 'FOXC1 regulates transcription in developmental and cell-identity programs. Its effect '
            'depends on the genes accessible in a particular cellular state.',
  'research': 'Understand a basal-associated research marker without turning it into a single-gene '
              'subtype classifier.',
  'measurement': 'Protein expression and target-gene experiments add context to RNA abundance.',
  'limitation': 'FOXC1 alone cannot establish Basal-like or triple-negative disease.',
  'question': 'Which multigene and pathology measurements would test a proposed basal association?',
  'study': 'FOXC1',
  'design': 'Expression association with functional experiments',
  'model': 'Basal-like breast cancer tissues and cell models',
  'finding': 'FOXC1 was investigated as a basal-like-associated regulator and potential prognostic '
             'marker.',
  'claim_limit': 'Basal-like classification and clinical triple-negative status overlap '
                 'incompletely; an association is not a standalone classifier.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'GATA3',
  'name': 'GATA binding protein 3',
  'hgnc_id': 'HGNC:4172',
  'entrez_id': '2625',
  'ensembl_gene_id': 'ENSG00000107485',
  'alias_symbol': 'HDR',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'transcription'],
  'product': 'lineage-regulating transcription factor',
  'normal': 'GATA3 participates in differentiation and helps organize gene-expression programs in '
            'several cell lineages. In breast epithelium it is useful for exploring luminal '
            'identity.',
  'research': 'Separate lineage-associated RNA from the consequences of a particular tumor DNA '
              'mutation.',
  'measurement': 'DNA sequencing, protein staining and transcript measurement answer different '
                 'questions.',
  'limitation': "GATA3 expression cannot establish mutation status or a person's clinical outcome.",
  'question': 'How might a mutation alter a lineage program without eliminating the transcript?',
  'study': 'TCGA',
  'design': 'Multi-platform molecular profiling',
  'model': 'Primary breast tumors across molecular subtypes',
  'finding': 'GATA3 was among recurrently mutated genes, with luminal differentiation context.',
  'claim_limit': 'Mutation status and a lineage-associated RNA signal provide different '
                 'information.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'HIF1A',
  'name': 'hypoxia inducible factor 1 subunit alpha',
  'hgnc_id': 'HGNC:4910',
  'entrez_id': '3091',
  'ensembl_gene_id': 'ENSG00000100644',
  'alias_symbol': 'MOP1|HIF-1alpha|PASD8|HIF1|bHLHe78',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['metabolism', 'transcription'],
  'product': 'oxygen-response transcription factor',
  'normal': 'HIF1A encodes an oxygen-responsive transcriptional regulator whose protein is '
            'strongly controlled by stabilization and degradation. Cells use the response to adapt '
            'to oxygen availability.',
  'research': 'Explore why stress-pathway activity can change without a large RNA change.',
  'measurement': 'Protein stabilization and target-gene responses are not equivalent to HIF1A RNA.',
  'limitation': 'A transcript count is not a tissue oxygen measurement. Protein stabilization and '
                'isoform composition need separate observations.',
  'question': 'Which observations distinguish low oxygen from another cause of HIF-related '
              'activity?',
  'study': 'RECENT_HIF1A',
  'design': 'Isoform and splicing experiments',
  'model': 'Breast cancer experimental models',
  'finding': 'Long and short HIF1A isoforms were investigated for differing regulatory effects.',
  'claim_limit': 'A gene-level RNA total can obscure isoform-specific and protein-stability '
                 'differences.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'ITGA6',
  'name': 'integrin subunit alpha 6',
  'hgnc_id': 'HGNC:6142',
  'entrez_id': '3655',
  'ensembl_gene_id': 'ENSG00000091409',
  'alias_symbol': 'CD49f|VLA-6|ITGA6A|ITGA6B',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['adhesion', 'basal'],
  'product': 'cell-matrix receptor subunit',
  'normal': 'ITGA6 contributes to integrin receptors that connect cells to extracellular matrix. '
            "The partner subunit and matrix context determine the receptor's behavior.",
  'research': 'Study basal epithelial attachment while remembering that a surface marker can span '
              'several cell states.',
  'measurement': 'Surface protein and receptor-partner measurements complement RNA.',
  'limitation': 'ITGA6 alone cannot establish a stem-cell population or a malignant phenotype.',
  'question': 'How would the matrix and integrin partner change the result of an attachment assay?',
  'study': 'RECENT_ITGA6',
  'design': 'Regulatory perturbation study',
  'model': 'Tamoxifen-resistance and breast cancer stem-like cell models',
  'finding': 'ASH2L-related experiments linked ITGA6 and ERK signaling to model-specific '
             'resistance.',
  'claim_limit': 'ITGA6 abundance alone does not identify a cancer stem cell or establish clinical '
                 'resistance.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT14',
  'name': 'keratin 14',
  'hgnc_id': 'HGNC:6416',
  'entrez_id': '3861',
  'ensembl_gene_id': 'ENSG00000186847',
  'alias_symbol': '',
  'prev_symbol': 'EBS3|EBS4',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['basal'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 14 contributes to epithelial intermediate filaments, often with keratin 5. '
            'The network helps cells withstand mechanical stress.',
  'research': 'Recognize basal epithelial structure and distinguish cell identity from malignancy.',
  'measurement': 'Protein localization identifies cells that a bulk transcript measurement '
                 'averages together.',
  'limitation': 'KRT14 is not a standalone cancer or aggressiveness test.',
  'question': 'Would a higher signal reflect more basal cells or a different state within those '
              'cells?',
  'study': 'RECENT_KRT14',
  'design': 'Exploratory mechanics and epithelial-cell study',
  'model': 'Healthy mammary epithelial cells from small donor groups with different risk contexts',
  'finding': 'Cell mechanics and keratin-associated epithelial states were examined together.',
  'claim_limit': 'Small selected donor groups and in vitro phenotypes do not validate a population '
                 'risk-screening test.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT17',
  'name': 'keratin 17',
  'hgnc_id': 'HGNC:6427',
  'entrez_id': '3872',
  'ensembl_gene_id': 'ENSG00000128422',
  'alias_symbol': '',
  'prev_symbol': 'PCHC1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['basal'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 17 contributes to epithelial structural networks and can appear in altered '
            'differentiation or stress-related contexts. Its presence is not exclusive to one '
            'breast tumor group.',
  'research': 'Study differentiation-related heterogeneity without assuming a universal direction '
              'of change.',
  'measurement': 'Spatial protein or single-cell RNA helps locate the source of a bulk signal.',
  'limitation': 'KRT17 alone cannot identify a molecular subtype, malignancy or causal pathway.',
  'question': 'How would the interpretation differ between tumor-only and tumor-adjacent-normal '
              'comparisons?',
  'study': 'RECENT_KRT17',
  'design': 'Immune and signaling model study',
  'model': 'Triple-negative tumors and experimental Wnt-related mouse models',
  'finding': 'The study examined Wnt-associated keratin and gamma-delta T-cell contexts.',
  'claim_limit': 'Reported group associations do not establish ancestry causation, and one keratin '
                 'cannot assign an intrinsic subtype.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT18',
  'name': 'keratin 18',
  'hgnc_id': 'HGNC:6430',
  'entrez_id': '3875',
  'ensembl_gene_id': 'ENSG00000111057',
  'alias_symbol': '',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'adhesion'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 18 forms intermediate filaments with keratin 8 in many simple epithelia. This '
            'partnership supports mechanical integrity and cellular organization.',
  'research': 'Use an epithelial marker to ask whether tissue composition affects a measured '
              'expression difference.',
  'measurement': 'Protein staining can locate an epithelial network that bulk RNA does not '
                 'resolve.',
  'limitation': 'KRT18 RNA cannot identify which epithelial cells produced it.',
  'question': 'Would the signal persist after comparing similar epithelial populations?',
  'study': 'RECENT_KRT18',
  'design': 'Single-cell computational association study',
  'model': '198,286 cells from 39 breast cancer samples',
  'finding': 'An RNA-binding-protein analysis included KRT18-associated epithelial expression '
             'patterns.',
  'claim_limit': 'A computational co-expression pattern does not demonstrate a direct KRT18 '
                 'regulatory mechanism.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT19',
  'name': 'keratin 19',
  'hgnc_id': 'HGNC:6436',
  'entrez_id': '3880',
  'ensembl_gene_id': 'ENSG00000171345',
  'alias_symbol': 'K19|CK19|K1CS|MGC15366',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['adhesion'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 19 contributes to epithelial intermediate-filament networks. Its distribution '
            'depends on epithelial lineage and cell state.',
  'research': 'Explore epithelial capture and circulating-cell research while distinguishing '
              'detection from proof of tumor origin.',
  'measurement': 'A transcript-detection assay and intact-cell protein staining have different '
                 'specificity limits.',
  'limitation': 'KRT19 positivity alone does not establish that a detected cell is malignant.',
  'question': 'What additional evidence would establish the origin of a keratin-positive cell?',
  'study': 'RECENT_KRT19',
  'design': 'Compound-exposure cell study',
  'model': 'Four breast cancer cell lines',
  'finding': 'Copper-based nanoparticle experiments included KRT19 RNA responses.',
  'claim_limit': 'An exposure-associated marker change does not establish a treatment '
                 'recommendation or a tumor-specific marker.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT5',
  'name': 'keratin 5',
  'hgnc_id': 'HGNC:6442',
  'entrez_id': '3852',
  'ensembl_gene_id': 'ENSG00000186081',
  'alias_symbol': 'KRT5A|CK-5',
  'prev_symbol': 'EBS2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['basal'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 5 helps build intermediate filaments in basal epithelial cells, commonly with '
            'keratin 14. Such structures are part of healthy tissue organization.',
  'research': 'Learn why a basal marker may reflect normal basal cells as well as a '
              'tumor-associated differentiation program.',
  'measurement': 'Spatial staining or cell-resolved RNA can separate contributions from different '
                 'compartments.',
  'limitation': 'KRT5 RNA alone cannot establish Basal-like disease or tumor-cell identity.',
  'question': 'Where in a tissue section would you expect a basal structural marker?',
  'study': 'RECENT_KRT5',
  'design': 'Spatial expression study',
  'model': '19 tumors: 10 luminal and 9 triple-negative',
  'finding': 'KRT5-associated signals were observed at particular tumor-normal interfaces, '
             'including luminal contexts.',
  'claim_limit': 'Mixed spatial spots and interface cell types mean KRT5 is not exclusive to '
                 'basal-like tumors.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'KRT8',
  'name': 'keratin 8',
  'hgnc_id': 'HGNC:6446',
  'entrez_id': '3856',
  'ensembl_gene_id': 'ENSG00000170421',
  'alias_symbol': 'CARD2|K8|CK8|CK-8|CYK8|K2C8|KO',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'adhesion'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Keratin 8 supports intermediate filaments in simple epithelia, commonly with keratin '
            '18. Its structural role is different from that of a growth receptor.',
  'research': 'Study epithelial identity and tissue mixtures without assuming every epithelial '
              'signal is hormone driven.',
  'measurement': 'Compare localization and epithelial-cell fraction with the bulk RNA measurement.',
  'limitation': 'KRT8 abundance does not establish a clinical luminal subtype.',
  'question': 'Can an epithelial marker remain abundant when hormone-receptor status changes?',
  'study': 'RECENT_KRT8',
  'design': 'Exposure and epithelial-state study',
  'model': 'Healthy mammary epithelial cell lines from six donors',
  'finding': 'Chemical-exposure experiments investigated mixed KRT8/KRT14 epithelial phenotypes.',
  'claim_limit': 'Plasticity in cell models does not supply an individual cancer-risk estimate.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'MALAT1',
  'name': 'metastasis associated lung adenocarcinoma transcript 1',
  'hgnc_id': 'HGNC:29665',
  'entrez_id': '378938',
  'ensembl_gene_id': 'ENSG00000251562',
  'alias_symbol': 'miPEP-52|PRO1073|MALAT-1|NCRNA00047|HCN|NEAT2|LINC00047|mascRNA',
  'prev_symbol': '',
  'locus_type': 'RNA, long non-coding',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['emerging', 'transcription'],
  'product': 'long noncoding RNA',
  'normal': 'MALAT1 is a nuclear long noncoding RNA studied in RNA processing and gene regulation. '
            'A noncoding transcript can have biological roles without producing a conventional '
            'protein.',
  'research': 'Investigate conflicting results across perturbation methods, models and metastatic '
              'stages.',
  'measurement': 'Transcript amount, RNA localization and a carefully controlled perturbation are '
                 'separate observations.',
  'limitation': 'Its historical name does not prove that MALAT1 universally promotes metastasis.',
  'question': 'Could a deletion affect neighboring regulation differently from an RNA-targeting '
              'perturbation?',
  'study': 'MALAT1_2018',
  'design': 'Genetic perturbation and add-back study',
  'model': 'Transgenic mouse tumors and human breast cancer model systems',
  'finding': 'The investigators reported metastasis suppression by MALAT1 in their tested models.',
  'claim_limit': 'This conflicts in direction with other perturbation studies; model, intervention '
                 'and metastatic stage must be considered.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'MKI67',
  'name': 'marker of proliferation Ki-67',
  'hgnc_id': 'HGNC:7107',
  'entrez_id': '4288',
  'ensembl_gene_id': 'ENSG00000148773',
  'alias_symbol': 'MIB-1|PPP1R105|Ki-67',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation'],
  'product': 'chromosome-associated proliferation protein',
  'normal': 'Ki-67 is associated with cycling cells and helps organize chromosomes during '
            'division. Its cellular distribution changes with cell-cycle stage.',
  'research': 'Separate a proliferation theme from a pathology labeling percentage or direct '
              'growth rate.',
  'measurement': 'An IHC percentage counts stained nuclei under a defined protocol; RNA is a '
                 'different quantity.',
  'limitation': 'MKI67 RNA is not a Ki-67 labeling index or a complete prognosis model.',
  'question': 'How would tumor-cell counting change an apparent bulk proliferation signal?',
  'study': 'RECENT_MKI67',
  'design': 'Multi-cohort observational RNA study',
  'model': '5,036 patients across 11 public cohorts',
  'finding': 'MKI67 RNA was examined for prognostic associations with an exploratory cutoff.',
  'claim_limit': 'RNA thresholds are not Ki-67 immunohistochemistry percentages, and associations '
                 'varied between cohorts.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'MMP9',
  'name': 'matrix metallopeptidase 9',
  'hgnc_id': 'HGNC:7176',
  'entrez_id': '4318',
  'ensembl_gene_id': 'ENSG00000100985',
  'alias_symbol': '',
  'prev_symbol': 'CLG4B',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['matrix', 'immune'],
  'product': 'matrix-remodeling enzyme',
  'normal': 'MMP9 can cleave extracellular proteins and contributes to tissue remodeling and cell '
            'movement. It is made by more than one cell population and requires activation.',
  'research': 'Investigate protease biology while distinguishing the source of the protein from '
              'its activity.',
  'measurement': 'Protein abundance, protease activation and substrate cleavage require different '
                 'assays.',
  'limitation': 'Bulk MMP9 RNA cannot demonstrate active matrix degradation or predict metastasis.',
  'question': 'Which producing cells and activity assays would test a remodeling hypothesis?',
  'study': 'RECENT_MMP9',
  'design': 'Network modeling and docking',
  'model': 'Public molecular data and computational protein models',
  'finding': 'MMP9 appeared among predicted targets in a daidzin network analysis.',
  'claim_limit': 'Predicted binding does not establish enzyme inhibition, invasion causality or '
                 'patient benefit.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'MTOR',
  'name': 'mechanistic target of rapamycin kinase',
  'hgnc_id': 'HGNC:3942',
  'entrez_id': '2475',
  'ensembl_gene_id': 'ENSG00000198793',
  'alias_symbol': 'mTOR|RAFT1|RAPT1|FLJ44809',
  'prev_symbol': 'FRAP|FRAP2|FRAP1',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth', 'metabolism'],
  'product': 'nutrient-responsive kinase',
  'normal': 'MTOR participates in distinct protein complexes that coordinate growth, metabolism '
            'and stress responses. Activity depends on complex membership and upstream signals.',
  'research': 'Connect nutrient sensing to clinical research without using expression as a '
              'treatment-selection shortcut.',
  'measurement': 'Downstream phosphorylation and complex-specific responses provide evidence '
                 'beyond MTOR RNA.',
  'limitation': 'One transcript total cannot distinguish mTOR complex activities or establish drug '
                'response.',
  'question': 'Can a nutrient change alter signaling before transcription changes?',
  'study': 'MTOR_TRIAL',
  'design': 'Randomized phase 3 trial',
  'model': 'Postmenopausal HR-positive advanced breast cancer after endocrine treatment',
  'finding': 'Everolimus plus exemestane improved progression-free survival in the studied '
             'population.',
  'claim_limit': 'A pathway-drug trial does not validate MTOR RNA as an eligibility test or '
                 'measure kinase activation.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PALB2',
  'name': 'partner and localizer of BRCA2',
  'hgnc_id': 'HGNC:26144',
  'entrez_id': '79728',
  'ensembl_gene_id': 'ENSG00000083093',
  'alias_symbol': 'FLJ21816|FANCN',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair', 'suppression'],
  'product': 'DNA-repair scaffold',
  'normal': 'PALB2 helps recruit and organize BRCA2 and RAD51 at damaged DNA. Its coordinating '
            'role supports template-guided repair.',
  'research': 'Explain how repair partners connect inherited variant evidence with functional '
              'experiments.',
  'measurement': 'A pathogenic DNA variant and an RNA expression difference are not the same '
                 'observation.',
  'limitation': 'PALB2 expression cannot diagnose hereditary risk or classify an uncertain '
                'variant.',
  'question': 'Which experiment would test whether a variant disrupts partner recruitment?',
  'study': 'RISK',
  'design': 'Population-based case-control sequencing',
  'model': '32,247 breast cancer cases and 32,544 controls',
  'finding': 'Pathogenic PALB2 variants were associated with breast cancer risk.',
  'claim_limit': 'Do not generalize from all variants or infer inherited risk from tumor '
                 'transcript abundance.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PDCD1',
  'name': 'programmed cell death 1',
  'hgnc_id': 'HGNC:8760',
  'entrez_id': '5133',
  'ensembl_gene_id': 'ENSG00000188389',
  'alias_symbol': 'CD279|PD1|hSLE1|PD-1',
  'prev_symbol': 'SLEB2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'immune-inhibitory receptor',
  'normal': 'PDCD1 encodes PD-1, a receptor that can restrain immune-cell signaling. Its effects '
            'depend on ligands, cell state and location.',
  'research': 'Distinguish a receptor on responding immune cells from the PD-L1 ligand encoded by '
              'CD274.',
  'measurement': 'Cell-specific receptor staining and immune-function measurements complement RNA.',
  'limitation': 'PDCD1 RNA cannot prove immune exhaustion or identify treatment eligibility.',
  'question': 'Where are the receptor-bearing cells relative to ligand-bearing cells?',
  'study': 'RECENT_PDCD1',
  'design': 'Retrospective radiomics and expression modeling',
  'model': '108 imaging cases from TCIA and 1,082 TCGA expression cases',
  'finding': 'The investigators modeled relationships between imaging features, PDCD1 expression '
             'and outcomes.',
  'claim_limit': 'Prediction of expression is not validation of checkpoint-inhibitor benefit or a '
                 'new clinical assay.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PGR',
  'name': 'progesterone receptor',
  'hgnc_id': 'HGNC:8910',
  'entrez_id': '5241',
  'ensembl_gene_id': 'ENSG00000082175',
  'alias_symbol': 'PR|NR3C3',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['hormone', 'transcription'],
  'product': 'hormone-responsive transcription factor',
  'normal': 'PGR encodes the progesterone receptor, which helps regulate transcription in '
            'hormone-responsive cells. Receptor forms and other regulatory proteins affect the '
            'response.',
  'research': 'Connect progesterone response with luminal programs while retaining the distinction '
              'from a clinical PR assay.',
  'measurement': 'PR IHC, receptor isoforms and PGR RNA provide different information.',
  'limitation': 'RNA cannot replace a PR test or establish treatment sensitivity.',
  'question': 'Could two cells with similar PGR RNA respond differently to a hormone stimulus?',
  'study': 'PGR_FUNCTION',
  'design': 'Receptor binding and functional experiments',
  'model': 'ER-positive breast cancer cells, xenografts and primary tumor explants',
  'finding': 'PR was investigated as a regulator of estrogen-receptor chromatin binding; '
             'progesterone altered growth responses in the tested models.',
  'claim_limit': 'Model-specific ligand and receptor effects do not validate PGR RNA as a '
                 'treatment-selection test or recommend hormone administration.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PIK3CA',
  'name': 'phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha',
  'hgnc_id': 'HGNC:8975',
  'entrez_id': '5290',
  'ensembl_gene_id': 'ENSG00000121879',
  'alias_symbol': 'PI3K',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['growth', 'metabolism'],
  'product': 'lipid-signaling enzyme',
  'normal': 'PIK3CA encodes a catalytic component of PI3K signaling. The enzyme changes membrane '
            'lipids that help recruit downstream signaling proteins.',
  'research': 'Follow a growth-signaling pathway across DNA variants, protein activity and '
              'clinical research.',
  'measurement': 'A defined mutation assay is distinct from expression, copy number and downstream '
                 'phosphorylation.',
  'limitation': 'PIK3CA RNA cannot establish a hotspot mutation or treatment eligibility.',
  'question': 'How would a variant-associated signaling change differ from greater enzyme '
              'abundance?',
  'study': 'TCGA',
  'design': 'Multi-platform molecular profiling',
  'model': 'Primary breast tumors across DNA, RNA and protein platforms',
  'finding': 'PIK3CA was among recurrently mutated genes in breast tumors.',
  'claim_limit': 'Mutation frequency and pathway alterations cannot be inferred from an RNA '
                 'heatmap.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PTEN',
  'name': 'phosphatase and tensin homolog',
  'hgnc_id': 'HGNC:9588',
  'entrez_id': '5728',
  'ensembl_gene_id': 'ENSG00000171862',
  'alias_symbol': 'MMAC1|TEP1|PTEN1',
  'prev_symbol': 'BZS|MHAM',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression', 'growth'],
  'product': 'lipid-signaling phosphatase',
  'normal': 'PTEN can remove a lipid signal that recruits growth-pathway proteins, opposing part '
            'of PI3K signaling. Localization and intact enzymatic function matter.',
  'research': 'Investigate pathway restraint without assuming that transcript quantity measures '
              'tumor-suppressor function.',
  'measurement': 'Sequence, deletion, protein loss and phosphatase function require different '
                 'assays.',
  'limitation': 'Normal PTEN RNA cannot rule out protein loss or a damaging DNA alteration.',
  'question': 'What could explain intact RNA alongside reduced pathway restraint?',
  'study': 'RECENT_PTEN',
  'design': 'Retrospective protein and outcome association',
  'model': '145 tumors assessed by immunohistochemistry, with 59 complete survival records',
  'finding': 'PTEN protein associations were explored in clinical triple-negative subgroups and '
             'compared with public RNA datasets.',
  'claim_limit': 'Few events and disagreement between protein and RNA findings prevent a validated '
                 'individual prognostic rule.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'PTPRC',
  'name': 'protein tyrosine phosphatase receptor type C',
  'hgnc_id': 'HGNC:9666',
  'entrez_id': '5788',
  'ensembl_gene_id': 'ENSG00000081237',
  'alias_symbol': 'LCA|T200|GP180|LY5|B220|CD45R',
  'prev_symbol': 'CD45',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune'],
  'product': 'immune signaling phosphatase',
  'normal': 'PTPRC encodes CD45, which helps regulate signaling in many immune cells. It is a '
            'broad leukocyte-associated marker rather than a label for one immune response.',
  'research': 'Recognize how changing leukocyte abundance can shift a bulk tissue profile.',
  'measurement': 'Cell counts and spatial markers distinguish population abundance from activity.',
  'limitation': 'PTPRC alone cannot specify the immune-cell type, activation state or tumor origin '
                'of a signal.',
  'question': 'How would you distinguish lymphocyte and myeloid contributions to a CD45-rich '
              'sample?',
  'study': 'RECENT_PTPRC',
  'design': 'Computational immune subtyping with cell experiments',
  'model': 'Public triple-negative cohorts and selected experimental models',
  'finding': 'The study examined PTPRC within immune-associated clustering and follow-up '
             'perturbations.',
  'claim_limit': 'A leukocyte-associated bulk signal does not identify a single immune lineage or '
                 'reproduce PAM50 classification.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'RAD51',
  'name': 'RAD51 recombinase',
  'hgnc_id': 'HGNC:9817',
  'entrez_id': '5888',
  'ensembl_gene_id': 'ENSG00000051180',
  'alias_symbol': 'HsRad51|HsT16930|BRCC5|FANCR',
  'prev_symbol': 'RAD51A|RECA',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['repair'],
  'product': 'DNA recombinase',
  'normal': 'RAD51 helps search for a matching DNA template and exchange DNA strands during '
            'homologous recombination. Recruitment depends on other repair proteins.',
  'research': 'Study repair competence with a functional endpoint rather than an isolated '
              'expression value.',
  'measurement': 'Damage-induced RAD51 foci and their cellular context differ from RNA abundance.',
  'limitation': 'High RAD51 RNA does not prove that accurate repair occurred.',
  'question': 'Why should a repair-foci assay consider the cell-cycle stage?',
  'study': 'RECENT_RAD51',
  'design': 'Repair-pathway perturbation study',
  'model': 'Breast cancer cell and mouse models',
  'finding': 'MND1/USP5-related experiments investigated RAD51 protein regulation and homologous '
             'recombination.',
  'claim_limit': 'A repair-pathway mechanism in models does not mean RAD51 RNA measures repair '
                 'capacity or drug benefit.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'RB1',
  'name': 'RB transcriptional corepressor 1',
  'hgnc_id': 'HGNC:9884',
  'entrez_id': '5925',
  'ensembl_gene_id': 'ENSG00000139687',
  'alias_symbol': 'RB|PPP1R130',
  'prev_symbol': 'OSRC',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression', 'proliferation'],
  'product': 'transcriptional cell-cycle gatekeeper',
  'normal': 'RB1 restrains transcriptional programs that help cells enter DNA replication. '
            'Phosphorylation and protein integrity affect whether that restraint remains in place.',
  'research': 'Explore how a downstream gate can alter responses to upstream cell-cycle '
              'inhibition.',
  'measurement': 'DNA sequence, total RB protein and phosphorylation are different measurements.',
  'limitation': 'RB1 RNA cannot establish a functional checkpoint or predict inhibitor response.',
  'question': 'What happens when an upstream kinase is inhibited but the downstream gate is '
              'missing?',
  'study': 'RECENT_RB1',
  'design': 'Exposure and transcriptional study',
  'model': 'MDA-MB-231 cells under cisplatin and a serum-phosphate cohort',
  'finding': 'Phosphate experiments examined RB1-E2F-related transcription and repair responses.',
  'claim_limit': 'Expression changes under exposure and serum associations do not demonstrate '
                 'intact RB1 protein function.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'SLC2A1',
  'name': 'solute carrier family 2 member 1',
  'hgnc_id': 'HGNC:11005',
  'entrez_id': '6513',
  'ensembl_gene_id': 'ENSG00000117394',
  'alias_symbol': 'DYT18|DYT9|GLUT-1',
  'prev_symbol': 'GLUT1|GLUT|HTLVR|CSE',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['metabolism'],
  'product': 'glucose transporter',
  'normal': 'SLC2A1 encodes GLUT1, which helps glucose cross cell membranes. Transport depends on '
            'protein placement and concentration gradients as well as transcript production.',
  'research': 'Distinguish a metabolic expression program from actual nutrient uptake.',
  'measurement': 'Surface transporter abundance, glucose uptake and metabolic flux are separate '
                 'measurements.',
  'limitation': 'SLC2A1 RNA cannot measure glycolytic flux or tissue oxygen availability.',
  'question': 'Would more transporter RNA always produce greater glucose uptake?',
  'study': 'RECENT_SLC2A1',
  'design': 'Metabolic perturbation and immune co-culture study',
  'model': 'Triple-negative breast cancer models with CD8-positive T-cell assays',
  'finding': 'EFO2/USF1 experiments investigated SLC2A1-related glycolysis and altered immune-cell '
             'killing.',
  'claim_limit': 'Transcript abundance cannot replace measured glucose flux; co-culture findings '
                 'are not clinical treatment evidence.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'STAT1',
  'name': 'signal transducer and activator of transcription 1',
  'hgnc_id': 'HGNC:11362',
  'entrez_id': '6772',
  'ensembl_gene_id': 'ENSG00000115415',
  'alias_symbol': 'STAT91|ISGF-3',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['immune', 'transcription'],
  'product': 'signal-responsive transcription factor',
  'normal': 'STAT1 helps cells convert interferon-related signals into transcriptional responses. '
            'Activation involves phosphorylation and movement within the cell.',
  'research': 'Explore immune signaling in both malignant and nonmalignant cell populations.',
  'measurement': 'Phosphorylation and cell-resolved target expression provide context for a bulk '
                 'transcript.',
  'limitation': 'STAT1 RNA alone cannot distinguish an antitumor response from another '
                'inflammatory state.',
  'question': 'Which cells are responding, and how does timing change the observed signal?',
  'study': 'RECENT_STAT1',
  'design': 'Chromosomal-instability and extracellular-vesicle perturbation study',
  'model': 'Triple-negative breast cancer cell lines and zebrafish embryo xenografts',
  'finding': 'STAT1-dependent EFEMP1 expression was investigated in vesicle-mediated migration, '
             'including a rescue experiment in STAT1-deficient cells.',
  'claim_limit': 'Cell migration and embryo models do not establish clinical metastasis '
                 'prevention; STAT1 abundance alone cannot specify the producing cell or '
                 'regulatory effect.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'TOP2A',
  'name': 'DNA topoisomerase II alpha',
  'hgnc_id': 'HGNC:11989',
  'entrez_id': '7153',
  'ensembl_gene_id': 'ENSG00000131747',
  'alias_symbol': 'TOP2alpha|TOPIIA',
  'prev_symbol': 'TOP2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['proliferation', 'repair'],
  'product': 'DNA topology enzyme',
  'normal': 'TOP2A helps untangle and manage DNA during replication and chromosome separation. Its '
            'activity includes controlled DNA cutting and rejoining.',
  'research': 'Learn how an enzyme can be a proliferation-associated signal and a pharmacological '
              'target without RNA being a response test.',
  'measurement': 'Copy number, protein abundance, enzyme activity and drug effects are distinct '
                 'observations.',
  'limitation': 'TOP2A RNA alone cannot establish drug sensitivity or identify DNA amplification.',
  'question': 'Can a larger cycling-cell fraction explain a higher enzyme transcript level?',
  'study': 'RECENT_TOP2A',
  'design': 'Protein-regulation perturbation with tissue associations',
  'model': 'Breast cancer cells, xenografts and chemotherapy-associated tissue analyses',
  'finding': 'STUB1-related experiments examined TOP2A ubiquitination and FOXM1-dependent '
             'transcription.',
  'claim_limit': 'Protein degradation, RNA and treatment response are distinct; retrospective '
                 'tissue associations are not a standalone clinical test.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'TP53',
  'name': 'tumor protein p53',
  'hgnc_id': 'HGNC:11998',
  'entrez_id': '7157',
  'ensembl_gene_id': 'ENSG00000141510',
  'alias_symbol': 'p53|LFS1',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['suppression', 'repair', 'transcription'],
  'product': 'stress-response transcription factor',
  'normal': 'TP53 encodes p53, which helps coordinate responses to cellular stress, including '
            'arrest, repair and cell death. The outcome depends on stress and cellular context.',
  'research': "Distinguish a tumor's DNA variant from RNA abundance and a functional stress "
              'response.',
  'measurement': 'Sequencing, protein staining and target-gene response are complementary assays.',
  'limitation': 'TP53 RNA cannot establish mutation status or whether p53 is functioning normally.',
  'question': 'Why might an altered p53 protein be abundant while its normal response is impaired?',
  'study': 'RECENT_TP53',
  'design': 'Retrospective mutation and survival study',
  'model': '1,201 Icelandic breast cancer cases diagnosed during 1970-2003',
  'finding': 'TP53 mutations were examined for breast-cancer-specific survival associations, '
             'including ER-positive disease.',
  'claim_limit': 'Historical ascertainment and treatment context limit transport; p53 RNA does not '
                 'specify mutation or functional status.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'VIM',
  'name': 'vimentin',
  'hgnc_id': 'HGNC:12692',
  'entrez_id': '7431',
  'ensembl_gene_id': 'ENSG00000026025',
  'alias_symbol': '',
  'prev_symbol': '',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['matrix', 'adhesion'],
  'product': 'structural intermediate-filament protein',
  'normal': 'Vimentin supports the internal structure of many mesenchymal cells. It is also found '
            'in several other cellular contexts and can change with cell state.',
  'research': 'Interpret a mesenchymal-associated signal while considering stromal cells and '
              'tissue composition.',
  'measurement': 'Spatial protein and cell-resolved RNA can identify the contributing populations.',
  'limitation': 'High bulk VIM is not proof that tumor cells underwent epithelial-to-mesenchymal '
                'transition.',
  'question': 'Could a changed stromal fraction mimic a tumor-cell state change?',
  'study': 'RECENT_VIM',
  'design': 'Immune-pathway perturbation study',
  'model': 'Breast cancer experimental and mouse models',
  'finding': 'Vimentin-related PGI2 signaling was investigated in CD8-positive antitumor immunity.',
  'claim_limit': 'A model-specific immune mechanism does not mean bulk VIM expression proves '
                 'epithelial transition or metastatic spread.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'},
 {'symbol': 'XBP1',
  'name': 'X-box binding protein 1',
  'hgnc_id': 'HGNC:12801',
  'entrez_id': '7494',
  'ensembl_gene_id': 'ENSG00000100219',
  'alias_symbol': '',
  'prev_symbol': 'XBP2',
  'locus_type': 'gene with protein product',
  'status': 'Approved',
  'verification': 'ANNOTATION_VERIFIED',
  'access_date': '2026-10-10',
  'domains': ['metabolism', 'transcription'],
  'product': 'stress-response transcription factor',
  'normal': 'XBP1 helps regulate responses to stress in the endoplasmic reticulum. RNA processing '
            'can produce an active form, so transcript processing matters alongside abundance.',
  'research': 'Connect protein-folding stress with experimental breast-cancer biology and '
              'oxygen-response programs.',
  'measurement': 'An assay distinguishing spliced XBP1 from total transcript answers a different '
                 'question.',
  'limitation': 'Total XBP1 RNA cannot identify the active spliced form or prove a uniform stress '
                'mechanism.',
  'question': 'How would you separate altered RNA processing from an increase in transcript '
              'production?',
  'study': 'XBP1',
  'design': 'Stress-pathway functional study',
  'model': 'Triple-negative breast cancer models and patient-expression associations',
  'finding': 'XBP1 was investigated in hypoxia-related transcription with HIF1-alpha.',
  'claim_limit': 'Splicing and model context matter; a signature association does not make XBP1 '
                 'RNA a clinical treatment rule.',
  'annotation_crosscheck': 'HGNC approved record; NCBI human taxid 9606 and symbol; Ensembl human '
                           'stable ID and display name agree.'}]
