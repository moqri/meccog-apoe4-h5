from common import F,save
SYS="Isogenic human iPSC-derived astrocytes: APOE4/4 line CRISPR-edited from the APOE3/3 iPSCs of an unaffected donor."
fs=[
F("Cellular cholesterol by filipin III is higher in APOE4 than isogenic APOE3 astrocytes, quantified per cell by flow cytometry.",
  "We next used flow cytometry analysis to better quantify the filipin III signal in individual cells, finding higher average fluorescent intensity in APOE4 compared to APOE3 astrocytes (Figure 3F)",
  "(APOE3 -> APOE4) -> (more cellular cholesterol)",0.65,SYS+" Filipin III flow cytometry. Lipid readout only in this panel.","Fig 3F","N/A","not_found_in_source","N/A","visual_only","6","printed_in_text",5,3),
F("Lysosome-dependent degradation of amyloid-beta is reduced in APOE4 astrocytes: blocking lysosomes raises intracellular Abeta42 in APOE3 but much less in APOE4, implying APOE4 lysosomes were degrading less to begin with.",
  "We observed increased Aβ42 accumulation following lysosome inhibition in APOE3 astrocytes compared to APOE4 astrocytes, suggesting reduced lysosome-dependent Aβ42 degradation in APOE4 astrocytes (Figure S3D)",
  "(APOE3 -> APOE4) -> (less lysosome-dependent degradation of cargo)",0.7,SYS+" Abeta42 uptake with lysosomal inhibition, then intracellular Abeta42 measurement.","Fig S3D","N/A","supplement_only","N/A","supplement_only","N/A","supplement_only",3,2),
]
save("p12","10.1016/j.neuron.2018.05.008","29861287","PubMed published",fs)
