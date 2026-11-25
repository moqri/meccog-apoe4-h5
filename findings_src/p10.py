from common import F,save
SYS="Human iPSC-derived neuron and astrocyte cocultures: CRISPR-edited APOE3, APOE4 or APOE-knockout human astrocytes plated with APOE3 or APOE4 neurons; lipid load induced with the NPC1 inhibitor U18666A."
fs=[
F("With the lysosomal cholesterol exporter NPC1 blocked, APOE3 astrocytes clear neutral lipid out of neurons but APOE4 astrocytes do not.",
  "In contrast, APOE4 hAs failed to mitigate neutral lipid accumulation (Fig. 1C and D)",
  "(APOE3 -> APOE4 astrocytes) -> (no clearance of lipid load imposed through the lysosome)",0.7,SYS+" Nile Red staining of neuronal somas.","Fig 1C-D","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",2,2),
F("The same split for the downstream damage: APOE3 astrocytes reduce the neurite swellings caused by the lysosomal lipid load, APOE4 astrocytes do not, whatever the neuron genotype.",
  "However, regardless of neuronal APOE genotype, APOE3 hAs significantly reduced the number of GFP+ puncta induced by lipid stress, whereas APOE4 hAs did not (Fig. 4B)",
  "(APOE3 -> APOE4 astrocytes) -> (lipid-induced neurite damage not rescued)",0.6,SYS+" GFP+ neurite puncta, live imaging.","Fig 4B","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",4,4),
F("Candidate lipid mechanism: HDL-like particles secreted into APOE3 cocultures are larger and more lipidated than in APOE4 cocultures.",
  "This difference became more pronounced under lipid challenge, as APOE3 astrocyte cocultures significantly increased large extracellular particle levels in response to NPC1 inhibition, while APOE4 cocultures did not show a similar response (Fig. 5A and B)",
  "(APOE3 -> APOE4) -> (no increase in large, lipidated ApoE particles under lipid load)",0.5,SYS+" Sizing of extracellular HDL-like particles in coculture media.","Fig 5A-B","N/A","not_found_in_source","N/A","visual_only","3","printed_in_text",4,4),
F("CONTRADICTING for neuron-intrinsic APOE: in neurons alone, the lysosomal cholesterol load produced by NPC1 inhibition is the same in APOE3 and APOE4 neurons.",
  "In iN alone, NPC1 inhibition significantly increased both the percentage of filipin+ neurons and the number of filipin+ particles per soma in APOE3 and APOE4 iNs compared with Veh, with no significant difference between APOE genotypes (Fig. 2A-C)",
  "CONTRADICTS in neurons alone: (APOE3 -> APOE4) -> (no change in lysosomal cholesterol load)",0.6,"Human iPSC-derived APOE3 or APOE4 neurons without astrocytes; filipin imaging after NPC1 inhibition.","Fig 2A-C","N/A","not_found_in_source","N/A","not_found_in_source","3","printed_in_text",2,2),
]
save("p10","10.1093/pnasnexus/pgag053","41867897","PubMed published",fs)
