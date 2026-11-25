from common import F,save
PRI="Primary mouse brain cultures (neurons with astrocytes) from human APOE knock-in mice: APOE knockout, APOE3 and APOE4. Mouse cells, not human."
fs=[
F("CONTRADICTING at maturity: at 18 days in vitro, lysosomal degradation of DQ-BSA and endosome appearance do not differ between ApoE4, ApoE3 and ApoE knockout neurons.",
  "When we compared our ApoE groups at 18 DIV there were no differences in the total intensities of DQ BSA in dendrites or cell bodies between ApoE KO, ApoE3, and ApoE4 neurons after 8 h (Fig. 2, G and H)",
  "CONTRADICTS at 18 DIV: (ApoE3 -> ApoE4) -> (no change in lysosomal degradation)",0.75,PRI+" DQ-BSA 8 h, 18 DIV.","Fig 2G-H","N/A","not_found_in_source","N/A","not_found_in_source","4","printed_in_text",1,1),
F("With longer time in culture the deficit appears: at 25-26 DIV, DQ-BSA degradation in ApoE4 neuronal cell bodies is 21.9 percent lower than ApoE3.",
  "remarkably the degradation of DQ BSA after 8 h was reduced with ApoE4, consistent with a significant reduction in DQ BSA integrated intensity in the cell bodies compared to ApoE3 (Fig. 4, F and G, 21.9%, p = 0.0495)",
  "(ApoE3 -> ApoE4, aged culture) -> (less lysosomal degradation)",0.8,PRI+" DQ-BSA 8 h, 25-26 DIV.","Fig 4F-G","21.9%","printed_in_text","0.0495","printed_in_text","4","printed_in_text",1,1),
F("Fewer active acidic compartments in aged ApoE4 neurons: 19.8 percent fewer LysoTracker-positive vesicles and 35.6 percent lower LysoTracker intensity per cell body than ApoE3.",
  "we detected a 19.8% lower number of LysoTracker positive vesicles (p = 0.011) and a 35.6% lower total LysoTracker intensity per neuronal cell body (p = 0.0059) in ApoE4 compared to ApoE3 neurons (Fig. 4, I-K)",
  "(ApoE3 -> ApoE4, aged culture) -> (fewer active degradative compartments)",0.75,PRI+" Live LysoTracker high-content imaging, 25-26 DIV.","Fig 4I-K","19.8%","printed_in_text","0.011","printed_in_text","4","printed_in_text",1,1),
F("CONTRADICTING on lysosome number and size: LAMP1-positive vesicle number and size do not differ between genotypes even at 25-26 DIV, so the deficit is functional rather than structural.",
  "Although we did not detect significant differences in LAMP1+ vesicle number and size (Fig. 4, A-E) or trafficking of EGF to the cell body (Fig. S3W) between the ApoE isoforms at 25 to 26 DIV",
  "CONTRADICTS: (ApoE3 -> ApoE4) -> (no change in lysosome number or size)",0.6,PRI+" LAMP1 immunofluorescence, 25-26 DIV.","Fig 4A-E","N/A","not_found_in_source","N/A","not_found_in_source","4","printed_in_text",3,2),
F("Lipid arm, directly tested: when aged cultures are given cholesterol, ApoE4 neurons that accumulate it reach much higher endolysosomal (LAMP1-positive) cholesterol than ApoE3 or knockout, though only in about half the cultures.",
  "Half of the time, similar to ApoE3 neurons, ApoE4 neurons accumulated very low amounts of cholesterol in endolysosomes (LAMP1+). Remarkably, however, when cholesterol did accumulate in ApoE4 neurons, it reached a considerably higher level than either ApoE KO or ApoE3 (Figs. 6, F, I, J and S4A)",
  "(ApoE3 -> ApoE4, cholesterol load) -> (more cholesterol in late endosomes/lysosomes), variable",0.7,PRI+" Filipin puncta inside LAMP1 vesicles after 12.5 ug/ml cholesterol for 3 d, 25 DIV.","Fig 6J","N/A","not_found_in_source","N/A","visual_only","5","printed_in_text",1,2),
F("CONTRADICTING on the lipid-to-lysosome step: cholesterol loading impairs DQ-BSA degradation and enlarges LAMP1 vesicles equally in all three genotypes, so lipid load alone does not produce the APOE4-specific deficit.",
  "Even though cholesterol seemed to have an impact on endosomes, including a lower number of early endosomes (Fig. 6K), larger LAMP1+ vesicles (Fig. 6L) without altering the number (Fig. S4E), and reduced degradation of DQ-BSA after 8 h (Fig. 6M), we detected similar changes between ApoE KO, ApoE3, and ApoE4",
  "CONTRADICTS the mediation step: (cholesterol load) -> (lysosomal impairment) in every genotype alike",0.7,PRI+" DQ-BSA and LAMP1 after cholesterol supplementation, 25 DIV.","Fig 6K-M","N/A","not_found_in_source","N/A","not_found_in_source","5","printed_in_text",2,2),
]
save("p9","10.1016/j.jbc.2025.110479","40675218","PubMed published",fs)
