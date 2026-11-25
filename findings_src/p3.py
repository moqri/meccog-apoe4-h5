from common import F,save
SYS="Isogenic hiPSC-derived astrocytes (CRISPR-edited APOE3/APOE4 pairs, Indiv1 and Indiv2, same APOE haplotype)."
fs=[
F("Lysosomal free cholesterol (filipin colocalized with endocytosed TRITC-dextran) is 3-fold higher in APOE4 than APOE3 isogenic astrocytes.",
  "Filipin and TRITC-Dextran co-localization (yellow puncta), a measure of lysosomal cholesterol (Majumdar et al., 2007), was significantly increased (3-fold, p<0.001) in APOE4 compared to APOE3 astrocytes, indicating that intracellular free cholesterol accumulates in lysosomes (Figure 6H)",
  "(APOE3 -> APOE4) -> (lysosomal cholesterol sequestration)",0.9,SYS+" Filipin plus endocytosed TRITC-dextran imaging.","Fig 6H","3x","printed_in_text","<0.001","printed_in_text","4","printed_in_text",3,2),
F("Lipid arm: total cholesterol is 20 percent higher in APOE4 astrocytes, from the free cholesterol pool rather than cholesteryl esters.",
  "Isogenic APOE4 astrocytes showed 20% increased total cholesterol, derived from a free cholesterol pool but not cholesteryl esters (CE) compared to APOE3 as measured by Gas Chromatography-Mass Spectrometry (GC-MS) (Muller et al., 2019) (Figure 6A)",
  "(APOE3 -> APOE4) -> (more free cholesterol)",0.7,SYS+" GC-MS sterol quantification. Lipid readout only in this panel.","Fig 6A","20%","printed_in_text","N/A","visual_only","6","printed_in_text",5,3),
F("LAMP1 and LAMP2, which act in the NPC2-to-NPC1 route that exports cholesterol out of the lysosome, are lower in APOE4 astrocytes and microglia, a candidate mechanism for the lysosomal cholesterol trapping.",
  "Levels of LAMP1/2, which are involved in NPC2 to NPC1 cholesterol export pathway from lysosome were decreased in APOE4 astrocytes and microglia (Figures S6E and S6F)",
  "(APOE3 -> APOE4) -> (less LAMP1/2 -> impaired lysosomal cholesterol export)",0.75,"Isogenic hiPSC-derived astrocytes and microglia; LAMP1/LAMP2 protein levels.","Fig S6E-F","N/A","supplement_only","N/A","supplement_only","N/A","supplement_only",3,3),
F("Transcriptome: the Lysosome gene set is negatively enriched in APOE4 versus APOE3 population hiPSC microglia, with lysosomal cholesterol-handling genes among the downregulated ones.",
  "Downregulated DEGs in Lysosome (e.g., LAMP1/2, NPC1/2, SMPD1 and LIPA) predicts enhanced cholesterol accumulation, decreased lipid clearance and catabolism",
  "(APOE3 -> APOE4) -> (lower lysosomal gene expression -> predicted cholesterol accumulation)",0.5,"Population (non-isogenic) hiPSC-derived microglia from APOE4 vs APOE3 carriers; RNA-seq with fGSEA and causal network analysis. Transcript surrogate only.","Fig 2C","N/A","not_found_in_source","N/A","not_found_in_source","N/A","not_found_in_source",4,4),
F("Functional consequence of the lysosomal trapping: cholesterol efflux to methyl-beta-cyclodextrin is reduced in APOE4 astrocytes.",
  "APOE4 astrocytes also exhibited reduced cholesterol efflux in the presence of 2% HDL and the cholesterol chelator methyl-β-cyclodextrin (MBCD), a measure of the total available cholesterol in the plasma membrane using fluorescently-labeled cholesterol (Figure 6L)",
  "(APOE3 -> APOE4) -> (less cholesterol efflux)",0.6,SYS+" Fluorescent cholesterol efflux assay, 6 h. Lipid readout only.","Fig 6L","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",5,4),
]
save("p3","10.1016/j.cell.2022.05.017","35750033","PubMed published",fs)
