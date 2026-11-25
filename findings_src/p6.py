from common import F,save
SYS="Human iPSC-derived microglia-like cells from eight APOE3/3 and six APOE4/4 donor lines (population lines, not isogenic)."
fs=[
F("Lysosomal degradation activity is lower in APOE4/4 than APOE3/3 human iPSC-derived microglia at baseline.",
  "we further analyzed lysosomal activity in iMGs using flow cytometry with an Abcam’s proprietary self-quenched substrate and found that E4/E4 iMGs exhibited significantly lower lysosomal degradation activity compared to E3/E3 cells (Fig. 1G-H)",
  "(APOE3 -> APOE4) -> (less lysosomal degradation in microglia)",0.85,SYS+" Flow cytometry with a self-quenched lysosomal substrate, 1 h.","Fig 1G-H","N/A","not_found_in_source","N/A","visual_only","6-8","printed_in_text",1,1),
F("Lysosomal membrane permeabilization after amyloid-beta exposure is greater in APOE4/4 microglia (more galectin puncta), i.e. leakier lysosomes.",
  "the formation of galectin puncta, detected with galectin (LGALS)-1-specific antibody, was significantly higher in E4/E4 iMGs than in E3/E3 iMGs after Aβ42 exposure, indicating increased lysosomal leakage in E4/E4 iMGs",
  "(APOE3 -> APOE4, with Abeta42) -> (more lysosomal membrane permeabilization)",0.7,SYS+" LGALS1 puncta imaging after Abeta42, 48 h.","Fig 4F-H","N/A","not_found_in_source","N/A","visual_only","6-8","printed_in_text",1,2),
F("CONTRADICTING on the lipid arm: total cholesterol does not differ by APOE genotype in these microglia, measured two ways, so the lysosomal deficit here is not explained by a cholesterol difference.",
  "There was no significant APOE genotype effect on cholesterol levels, and this was confirmed using Amplex Red assay kit in a separate differentiation batch (Supplementary Fig. 3C)",
  "CONTRADICTS the lipid arm: (APOE3 -> APOE4) -> (no change in cellular cholesterol)",0.75,SYS+" Metabolomics plus Amplex Red cholesterol assay.","Fig S3C","N/A","supplement_only","N/A","supplement_only","N/A","supplement_only",5,2),
F("CONTRADICTING on autophagy: basal LC3-II is lower in APOE4/4 microglia but autophagic flux with rapamycin and bafilomycin does not differ by genotype.",
  "E4/E4 iMGs exhibit reduced basal levels of LC3-II but no significant differences in basal or rapamycin-induced autophagic flux, indicating that autophagy is not affected by the APOE genotype",
  "CONTRADICTS: (APOE3 -> APOE4) -> (no change in autophagic flux)",0.7,SYS+" LC3-II/LC3-I western blot with rapamycin and bafilomycin.","Fig 1D-E","N/A","not_found_in_source","N/A","visual_only","6-8","printed_in_text",3,2),
F("Lysosomal protein content trends lower in APOE4/4 microglia: LAMP-2 is reduced, and the lysosomal transporters MFSD1 and GLMP are downregulated in proteomics at baseline.",
  "Since proteomic analysis comparing two (isogenic to each other) E4/E4 lines to E3/E3 lines revealed a downregulation of two other lysosomal proteins MFSD1 and GLMP in E4/E4 iMGs at basal conditions (Fig. 3B, Table S4), the overall lysosomal protein content may be reduced by E4/E4 genotype",
  "(APOE3 -> APOE4) -> (less lysosomal protein content)",0.55,SYS+" Proteomics on an isogenic subset plus LAMP-2 western blot.","Fig 3B","N/A","not_found_in_source","N/A","not_found_in_source","2","printed_in_text",3,4),
]
save("p6","10.1186/s12974-025-03470-y","40457456","PubMed published",fs)
