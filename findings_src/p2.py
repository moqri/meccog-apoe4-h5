from common import F,save
SYS="Isogenic iPSC-derived astrocytes from two donors (APOE3/3 lines CRISPR-edited to APOE4/4), astrocyte monoculture."
fs=[
F("Lysosomal proteolysis (DQ-BSA cleavage by flow cytometry) is reduced in APOE4/4 versus isogenic APOE3/3 astrocytes in both donor pairs.",
  "APOE4/4 astrocytes showed significantly reduced lysosomal DQ-BSA signal compared to isogenic control APOE3/3 astrocytes across two isogenic donor pairs (Donor #1: p= 0.0032; Donor #2: p < 0.0001, Figure 4d), indicating decreased lysosomal proteolytic activity",
  "(APOE3 -> APOE4) -> (less lysosomal proteolysis)",0.95,SYS+" DQ-BSA Green, 24 h.","Fig 4D","N/A","not_found_in_source","0.0032","printed_in_text","3-4","printed_in_text",1,1),
F("After normalizing DQ-BSA to co-internalized dextran, APOE4/4 astrocytes still show lower proteolysis, so the deficit is per lysosome and not only fewer lysosomes.",
  "Even after dextran normalization, APOE4/4 astrocytes retained significantly lower proteolytic activity (p = 0.0098; Figure S4e), indicating functional impairment rather than solely reduced lysosome abundance",
  "(APOE3 -> APOE4) -> (less proteolysis per lysosome)",0.95,SYS+" DQ-BSA normalized to dextran.","Fig S4E","N/A","not_found_in_source","0.0098","printed_in_text","N/A","supplement_only",1,1),
F("LAMP1 immunoreactivity (lysosomal mass) is reduced in APOE4/4 astrocytes in both donor pairs.",
  "Consistent with this, immunoreactivity for the lysosomal membrane protein LAMP1 was also significantly reduced in APOE4/4 astrocytes compared to isogenic APOE3/3 astrocytes (Donor #1: p = 0.0002 and Donor #2: p = 0.0001, Figure S4d)",
  "(APOE3 -> APOE4) -> (less LAMP1, lower lysosomal mass)",0.8,SYS+" LAMP1 immunostaining.","Fig S4D","N/A","not_found_in_source","0.0002","printed_in_text","N/A","supplement_only",3,3),
F("Lipid arm: BODIPY-cholesterol accumulates more in APOE4/4 than APOE3/3 astrocytes from two donors.",
  "Consistent with altered lipid metabolism, APOE4/4 astrocytes showed significantly increased BODIPY-cholesterol accumulation compared to isogenic APOE3/3 astrocytes generated from two different individuals (Donor #1: p = 0.001; Donor #2: p = 0.002, Figure 5a)",
  "(APOE3 -> APOE4) -> (more cellular cholesterol)",0.7,SYS+" BODIPY-cholesterol live imaging. Lipid readout only in this panel, no lysosomal readout.","Fig 5A","N/A","not_found_in_source","0.001","printed_in_text","3","printed_in_text",5,3),
F("Lipid-to-lysosome link: cyclodextrins raise lysosomal proteolysis in APOE4/4 astrocytes, while atorvastatin, efavirenz and two LXR agonists do not, so not every cholesterol-lowering route helps.",
  "Treatment with 2-hydroxypropyl-β-cyclodextrin (2HβCD) and methyl-β-cyclodextrin (MβCD) significantly increased lysosomal proteolysis (2HβCD: p = 0.0002; MβCD: p = 0.019) (Figure 5b), whereas the other interventions had neutral or negative effects on APOE4/4 lysosomal proteolytic activity (Figure 5b)",
  "(APOE4 + cholesterol extraction) -> (lysosomal proteolysis increased); statin and LXR agonists -> no gain",0.9,SYS+" DQ-BSA Red over 24 h, small-molecule panel.","Fig 5B","N/A","not_found_in_source","0.0002","printed_in_text","4","printed_in_text",2,2),
F("The cyclodextrin gain in lysosomal proteolysis replicates in astrocytes from the second donor.",
  "Increased lysosomal proteolytic activity with MβCD was replicated in astrocytes from a second donor (p = 0.0045; Figure S5c)",
  "(APOE4 + MbetaCD) -> (lysosomal proteolysis increased), second donor",0.85,SYS+" Donor 2, DQ-BSA.","Fig S5C","N/A","not_found_in_source","0.0045","printed_in_text","N/A","supplement_only",2,2),
F("Cyclodextrin increases LysoTracker-positive signal in APOE4/4 astrocytes. Note the baseline direction here is opposite to Lee 2023, where APOE4 raised LysoTracker signal.",
  "Consistent with improved lysosomal capacity, MβCD increased LysoTracker-positive lysosomal signal in APOE4/4 astrocytes (p = 0.044; Figure 5d)",
  "(APOE4 + MbetaCD) -> (more LysoTracker-positive lysosomes)",0.75,SYS+" LysoTracker imaging.","Fig 5D","N/A","not_found_in_source","0.044","printed_in_text","5-6","printed_in_text",2,3),
F("Free cholesterol by filipin is higher in APOE4/4 astrocytes and is lowered by cyclodextrin to APOE3/3 levels.",
  "Filipin staining revealed a significant increase in endogenous free cholesterol in APOE4/4 astrocytes compared to APOE3/3 astrocytes, which was significantly reduced following MβCD treatment (p = 0.0167) to levels comparable to APOE3/3 astrocytes (Figure S5b)",
  "(APOE3 -> APOE4) -> (more free cholesterol), reversed by MbetaCD",0.7,SYS+" Filipin staining.","Fig S5B","N/A","not_found_in_source","0.0167","printed_in_text","N/A","supplement_only",5,3),
]
save("p2","10.1016/j.stem.2026.08.001","42636814","PubMed published",fs)
