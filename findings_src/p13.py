from common import F,save
SYS="HEK293 and HepG2 cell lines stably expressing mCherry-tagged APOE3 or APOE4, plus mouse brain tissue. Not human brain cells: included because it tests the lysosomal handling of APOE itself."
fs=[
F("APOE4 accumulates in enlarged lysosomes and late endosomes and changes autophagic flux, lysosomal protein content and lipid droplets.",
  "We found, by examining cells stably expressing each APOE isoform, that APOE4 increases lysosomal trafficking, accumulates in enlarged lysosomes and late endosomes, alters autophagic flux and the abundance of autophagy proteins and lipid droplets, and alters the proteomic contents of lysosomes following internalization",
  "(APOE3 -> APOE4) -> (enlarged late endosomes/lysosomes, altered autophagic flux and lipid droplets)",0.5,SYS+" Confocal imaging of APOE-mCherry with LAMP1-GFP (Fig 3A); the quote is the abstract summary and also covers autophagy and proteomic panels elsewhere in the paper.","Fig 3A","N/A","not_found_in_source","N/A","not_found_in_source","N/A","not_found_in_source",5,4),
F("Lysosomes exposed to APOE4 lose mitochondrial proteins such as prohibitin from their contents, linking the lysosomal change to mitochondrial turnover.",
  "Proteins reduced in APOE4 lysosomes that were not reduced in mCh-treated cells included mitochondrial proteins such as prohibitin",
  "(APOE3 -> APOE4) -> (altered lysosomal proteome, less mitochondrial cargo)",0.4,"HepG2 cells treated 24 h with APOE3 or APOE4 conditioned medium; lysosome immunoprecipitation and mass spectrometry. Caveat: hepatic cell line.","Fig 3D","N/A","not_found_in_source","N/A","not_found_in_source","N/A","not_found_in_source",5,5),
]
save("p13","10.1242/jcs.258687","34982109","PubMed published",fs)
