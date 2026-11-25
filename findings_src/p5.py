from common import F,save
N2A="Neuro-2a mouse neuroblastoma cells stably expressing human APOE3 or APOE4 (not human cells); isogenic apart from the APOE transgene."
IPS="Isogenic APOE3 vs APOE4 human iPSC-derived mixed neuronal cultures including GABAergic interneurons."
fs=[
F("Lysosomes are alkalinized in APOE4-expressing neuronal cells: ratiometric dextran pH 5.86 versus 4.30 for APOE3.",
  "We found that HsAPOE4-expressing cells exhibit dramatic lysosomal alkalinization (pH = 5.86) compared to HsAPOE3 (pH = 4.30) cells (Figure 1C-E), reminiscent of previous results in APOE4-expressing astrocyte lysosomes (pH = 5.20, compared to pH = 4.08 in APOE3 astrocytes) [26]",
  "(APOE3 -> APOE4) -> (higher lysosomal pH -> impaired lysosomal function)",0.75,N2A+" OregonGreen-dextran ratiometric lysosomal pH.","Fig 1C-E","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",1,2),
F("Lysosomal proteolysis is reduced in APOE4 cells: Magic Red cathepsin B cleavage is lower, in line with the higher lysosomal pH.",
  "We found that the HsAPOE4-expressing cells exhibited significantly decreased MR-CTSB proteolysis compared to HsAPOE3-expressing cells, in line with their decreased lysosomal acidity (Figure 1F,G)",
  "(APOE3 -> APOE4) -> (less cathepsin B proteolysis)",0.75,N2A+" Magic Red cathepsin B live imaging.","Fig 1F-G","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",1,2),
F("LysoTracker signal is reduced in APOE4 cells while LAMP1 lysosomal density is not, so the loss of acidic signal reflects alkalinization rather than fewer lysosomes.",
  "We found that the LysoTracker intensity was significantly reduced in HsAPOE4-expressing cells (Figure 1A,B), suggesting either endolysosomal alkalinization or a reduction in endolysosomal density",
  "(APOE3 -> APOE4) -> (less LysoTracker signal, lysosomes less acidic)",0.65,N2A+" LysoTracker Deep Red imaging.","Fig 1A-B","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",3,2),
F("Lipid-related mechanism: LysoIP proteomics finds lipid and glycan regulators, including the long-chain fatty acid ligase ACSL4 and the phosphoinositide phosphatase SACM1L, accumulating in APOE4 lysosomes alongside APOE itself.",
  "we found that HsAPOE4-expressing lysosomes accumulated APOE itself, AD-associated secretase proteins (PSEN2, CD63, TSPAN3), trafficking receptors (AP1S1, AP1G1, BET1L, LAMTOR1, LAMTOR2, TMED5), and lipid/glycan-regulators (ACSL4, ACBD3, GALNT2, MAN2B1, NEU1, PIP4P1, SACM1L, PIP4P1/TMEM55B, UXS1) (Figure 3B,C, Figure S3C)",
  "(APOE3 -> APOE4) -> (remodeled lysosomal proteome including lipid-handling proteins)",0.6,N2A+" LysoIP (TMEM192-3xHA) lysosomal proteomics.","Fig 3B","N/A","not_found_in_source","N/A","not_found_in_source","N/A","not_found_in_source",4,4),
F("Causal test of the driver: knocking down TMED5 re-acidifies lysosomes in APOE4 cells without changing lysosomal density.",
  "We confirmed by lysosomal Oregon-green pH measurements that knockdown of TMED5 significantly enhanced lysosomal acidification in HsAPOE4 Neuro-2a cells, while not impacting the lysosomal density (Figure 5C-E)",
  "(APOE4 + TMED5 knockdown) -> (lysosomal pH restored)",0.55,N2A+" siRNA knockdown, Oregon-green lysosomal pH.","Fig 5C-E","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",2,3),
F("Replication in human cells: APOE4 iPSC-derived neurons carry less lysosomal LGALS3BP and more lysosomal TMED5 than isogenic APOE3 neurons.",
  "we found that APOE4 iPSC-derived neurons harbored less lysosomal LGALS3BP and more lysosomal TMED5 compared to their APOE3 counterparts (Figure 6B,C)",
  "(APOE3 -> APOE4) -> (altered lysosomal protein composition in human neurons)",0.7,IPS+" Lysosomal proximity ligation assay against LAMP1.","Fig 6B-C","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",3,3),
]
save("p5","10.1080/15548627.2025.2576613","41103078","PubMed published",fs)
