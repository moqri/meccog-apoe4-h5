from common import F,save
SYS="Human iPSC-derived astrocytes from APOE4 and APOE3 carriers (fibroblast-derived, population lines), plus yeast expressing human APOE isoforms."
fs=[
F("APOE4 astrocytes accumulate more lipid droplets than APOE3 astrocytes, with more of the droplet protein perilipin-2.",
  "After 2 weeks in culture, we observed that APOE4 astrocytes accumulated a greater number of lipid droplets than did their APOE3 counterparts (Fig. 1E), which was accompanied by accumulation of a lipid droplet-resident protein, Perilipin-2 (Fig. 1F) (32)",
  "(APOE3 -> APOE4) -> (more lipid droplets)",0.6,SYS+" BODIPY lipid droplet staining and perilipin-2 western blot, 2 weeks in culture.","Fig 1E","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",5,3),
F("The triacylglycerols stored in APOE4 astrocytes are far more unsaturated than in APOE3, the lipid-composition change that makes them prone to peroxidation.",
  "We also observed that the degree of unsaturation of the fatty acids attached to triacylglycerides in APOE4 astrocytes was far higher than that in APOE3 astrocytes (Fig. 1D)",
  "(APOE3 -> APOE4) -> (more unsaturated stored triacylglycerol)",0.55,SYS+" LC-MS whole-cell lipidomics.","Fig 1D","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",5,4),
F("The lipid disruption is reversible by a phospholipid precursor: choline supplementation restores the APOE4 astrocyte lipidome, showing the defect is metabolic rather than fixed.",
  "APOE4-expressing astrocytes treated with CDP-choline showed a decrease in lipid droplet number to that found in APOE3-expressing astrocytes (Fig. 4D)",
  "(APOE4 + CDP-choline) -> (lipid droplets back to APOE3 level)",0.5,SYS+" CDP-choline supplementation then lipid droplet imaging and lipidomics.","Fig 4D","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",5,4),
]
save("p11","10.1126/scitranslmed.aaz4564","33658354","PubMed published",fs)
