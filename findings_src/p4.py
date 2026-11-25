from common import F,save
SYS="Isogenic APOE2/E3/E4/knockout iPSC-derived astrocytes (EBiSC lines from one donor), quiescent, serum-free protocol."
fs=[
F("CONTRADICTING: lysosomal activity is equally low in APOE3 and APOE4 iAstrocytes (both below APOE2 and APOE-knockout), so no APOE4-specific impairment relative to APOE3 in this assay.",
  "Lysosomal activity in APOE3 and APOE4 was significantly lower than in APOE2 and APOE-KO cells (KO = E2 > E3 = E4) (Figure 4F)",
  "CONTRADICTS: (APOE3 -> APOE4) -> (no change in lysosomal activity)",0.85,SYS+" Lysosomal activity assay normalized to APOE3.","Fig 4F","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",1,1),
F("CONTRADICTING: lysosome and endosome compartment area show no genotype difference by LAMP2 or dextran imaging; RAB5 endosomes are also unchanged.",
  "Immunofluorescent detection of lysosomes by LAMP2 (Figure 4C) or Dextran-Alexa 555 (Figure S3) showed no difference between genotypes",
  "CONTRADICTS: (APOE3 -> APOE4) -> (no change in lysosomal compartment area)",0.65,SYS+" LAMP2 immunostaining, percent of cell area.","Fig 4C","N/A","not_found_in_source","N/A","not_found_in_source","3","printed_in_text",3,3),
F("LAMP2 protein by western blot is lower in APOE4 than APOE3, but APOE2 and the knockout are equally low, so the effect is not specific to APOE4.",
  "However, protein levels of LAMP2 detected by western blot were significantly higher in APOE3 compared with APOE2, APOE4, and APOE-KO (E3 > E2 = E4 = KO) (Figures 4D and 4E)",
  "(APOE3 -> APOE4) -> (less LAMP2 protein), not APOE4-specific",0.65,SYS+" Western blot normalized to beta-actin.","Fig 4E","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",3,3),
F("Lipid arm: non-membrane-bound free cholesterol is increased in APOE4 iAstrocytes above all other genotypes.",
  "We found that non-membrane-bound cholesterol was increased in APOE4 iAstrocytes (E4 > E3 = E2 = KO) (Figure 3F)",
  "(APOE3 -> APOE4) -> (more intracellular free cholesterol)",0.7,SYS+" MbetaCD wash then filipin III. Lipid readout only.","Fig 3F","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",5,3),
F("Lysosomal cholesterol is highest in APOE4, but the reported significance is only against APOE2 (E4 > E2), not against APOE3.",
  "Further colocalization of Filipin III with Dextran-Alexa 555 was highest in APOE4 iAstrocytes, indicating higher cholesterol levels in lysosomes of APOE4 iAstrocytes (E4 > E2) (Figure 3G)",
  "(APOE3 -> APOE4) -> (trend to more lysosomal cholesterol, significant only vs APOE2)",0.7,SYS+" Filipin III and Dextran-Alexa 555 colocalization.","Fig 3G","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",3,3),
F("Lipid arm: cellular triacylglycerol, the main lipid droplet component, rises with APOE genotype in the order E4 > E3 > E2 = knockout.",
  "TAGs show a genotype-dependent increase both at baseline and after activation, with lowest cellular TAG levels in APOE-KO and highest in APOE4 iAstrocytes (Figures S2A and S5A)",
  "(APOE3 -> APOE4) -> (more triacylglycerol / lipid droplets)",0.55,SYS+" HPTLC lipid profiling of cell pellets. Lipid readout only.","Fig S2A","N/A","supplement_only","N/A","supplement_only","N/A","supplement_only",5,4),
]
save("p4","10.1016/j.stemcr.2021.11.007","34919811","PubMed published",fs)
