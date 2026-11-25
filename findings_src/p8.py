from common import F,save
NEU="Human iPSC-derived NGN2 neurons treated with recombinant ApoE isoforms lipidated with POPC and the polyunsaturated cholesteryl ester CE(20:4); exogenous ApoE, not genotype."
fs=[
F("Lipid cargo drives a lysosomal pathology in an isoform series: ApoE4 carrying polyunsaturated cholesteryl ester induces more neuronal lipofuscin than ApoE3 or ApoE2.",
  "In human neurons, the addition of ApoE carrying polyunsaturated fatty acids (PUFAs)-CE revealed an allelic series (ApoE4 > ApoE3 > ApoE2) associated with lipofuscinosis, an age-related lysosomal pathology resulting from lipid peroxidation",
  "(ApoE3 -> ApoE4, same lipid cargo) -> (more lysosomal lipofuscin)",0.7,NEU+" Longitudinal autofluorescence imaging at 7, 14 and 21 d.","Fig 5A-B","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",2,2),
F("The APOE4-ApoE3 gap in lipofuscin widens with incubation time, matching the age-dependence built into the hypothesis.",
  "After longer incubation (14 d and 21 d), a progressively larger difference between ApoE4 and ApoE3 emerged (Figure S5G, Figure 5B)",
  "(ApoE3 -> ApoE4) -> (lysosomal lipofuscin, growing with time)",0.6,NEU+" Autofluorescence time course.","Fig 5B","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",2,3),
F("The lipofuscin is lysosomal: it localizes to LAMP1-positive vesicles by super-resolution imaging.",
  "Lipofuscin appeared mostly perikaryal and localized in LAMP1-positive lysosomes shown by super-resolution imaging (Figure 5C)",
  "(ApoE4 + PUFA-CE) -> (lysosomal lipid deposit)",0.6,NEU+" Super-resolution confocal with LAMP1.","Fig 5C","N/A","not_found_in_source","N/A","not_found_in_source","N/A","not_found_in_source",3,3),
F("The effect needs the lipid: replacing the polyunsaturated cholesteryl ester with a monounsaturated one abolishes lipofuscin induction by ApoE4.",
  "Replacing CE(20:4) with CE(18:1) in the POPC-ApoE4 lipoproteins abolished lipofuscin induction (Figure 5J-K), denoting a PUFA requirement",
  "(ApoE4 with saturated cargo) -> (no lysosomal lipofuscin) -> lipid-dependent",0.65,"H4 neuroglioma cells treated with CE(20:4) or CE(18:1) lipidated ApoE4. Caveat: cell line, not neurons.","Fig 5J-K","N/A","not_found_in_source","N/A","visual_only","N/A","not_found_in_source",2,2),
F("Functional consequence: neurons loaded with the lipid-laden ApoE4 accumulate more internalized tau fibrils in endolysosomes, with the isoform order ApoE4 > ApoE3 > ApoE2.",
  "total pHrodo signals from tau pffs that were internalized and accumulated in the endolysosomes demonstrated a trend of ApoE4 > ApoE3 > ApoE2 > K146E ApoE4, with the isoform-dependent difference being more pronounced among lipofuscin-positive neurons (Figure 6H-I)",
  "(ApoE3 -> ApoE4, lipid cargo) -> (more undegraded tau in endolysosomes)",0.55,NEU+" pHrodo-labeled tau preformed fibrils, 13-14 d after 14 d ApoE treatment.","Fig 6H-I","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",3,3),
]
save("p8","10.1016/j.cell.2024.10.027","39532095","PubMed published",fs)
