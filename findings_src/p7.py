from common import F,save
SYS="Human iPSC-derived astrocytes, APOE2 / APOE3 / APOE4 homozygous isogenic sets from two backgrounds (KOLF2.1J and line 325), oleic-acid loaded."
fs=[
F("Lipid droplets resist degradation in APOE4 astrocytes: BODIPY-C12 fatty acid persists longer in lipid droplets after a 24 h chase than in APOE2 astrocytes.",
  "C12 fatty acids within lipid droplets persisted longer in APOE4 than in APOE2 astrocytes following a 24 h chase period under baseline conditions (Fig. 5D, E and Supplementary Fig.",
  "(APOE2 -> APOE4) -> (slower lipid droplet turnover)",0.6,SYS+" BODIPY-C12 pulse-chase live imaging. Comparison is APOE4 vs APOE2, not vs APOE3.","Fig 5D-E","N/A","not_found_in_source","0.0059","printed_in_text","4","printed_in_text",3,3),
F("Lipophagy marker: the autophagy receptor p62 on lipid droplets is higher in APOE4 than in APOE3 or APOE2 astrocytes, consistent with droplets stalled in an autophagic route.",
  "We observed by immunofluorescence that the levels of co-localized SQSTM1/p62 with lipid droplets were indeed higher in APOE4 than APOE2 astrocytes (Fig. 5B, C and Supplementary Fig.",
  "(APOE3 -> APOE4) -> (more p62 on lipid droplets -> stalled lipophagy)",0.6,SYS+" p62 and LipidSpot confocal colocalization, about 700 droplets per replicate.","Fig 5C","N/A","not_found_in_source","0.000038","printed_in_text","4-5","printed_in_text",3,3),
F("Proteome: autophagosome assembly proteins are enriched on APOE4 lipid droplets relative to APOE2, the molecular basis for the stalled lipophagy.",
  "In contrast, proteins present on APOE4 lipid droplets but not found in APOE2 showed functional enrichment in protein secretion and autophagosome assembly pathways (Fig. 3B and Supplementary Data 12, 13)",
  "(APOE2 -> APOE4) -> (autophagosome assembly proteins on lipid droplets)",0.45,SYS+" Buoyant-fraction lipid droplet proteomics.","Fig 3B","N/A","not_found_in_source","N/A","not_found_in_source","4","printed_in_text",4,4),
F("Lipid arm, with a caveat for the hypothesis: APOE4, APOE2 and APOE-knockout astrocytes all accumulate more lipid droplets than APOE3, so droplet number alone does not single out APOE4.",
  "We recapitulate this finding and observe that APOE4, APOE2, and APOE-KO iPSC-derived astrocytes also accumulate lipid droplets relative to APOE3 (Supplementary Fig. S1C, D)",
  "(APOE3 -> APOE4) -> (more lipid droplets), but APOE2 and KO do the same",0.55,SYS+" Lipid droplet staining and counting.","Fig S1C-D","N/A","supplement_only","N/A","supplement_only","N/A","supplement_only",5,4),
]
save("p7","10.1038/s41467-026-76565-6","42749735","PubMed published",fs)
