# Iterative self-check log (AI, 2026-11-25)

Not a human check. Each entry: row, why suspected, what the source shows, change.

| # | Row | Suspicion | Finding | Change |
|---|---|---|---|---|
| 1 | P4.F4 (de Leeuw Fig 3F) | effect and n N/A on a readable bar chart | E3 ~1.0, E4 ~1.8, **** E3 vs E4; legend: 3 experiments, 7-10 images/line/experiment | effect ~80% [estimated], n 3 [printed] |
| 2 | P2.F1, F4, F5, F7 (Mesentier-Louro Fig 4D, 5A, 5B, 5D) | effect N/A on clean bar charts; images first obtained tonight | bars read: 100 vs 72; 1.0 vs 1.8; AUC 4.9 vs 9.3e6; 0.68 vs 0.94 | effects ~28%, ~80%, ~1.9x, ~38% [estimated] |
| 3 | P2.F2, F3, F6, F8 (Mesentier-Louro Fig S4E, S4D, S5C, S5B) | effect N/A on supplement bar charts | AUC 22.5 vs 15.3 (**); LAMP1 donor 1 1.0 vs 0.3 (***); AUC 4.0 vs 5.5e7 with MbCD (**); filipin 1.57 vs 1.0 after MbCD (*). Printed P values agree with the stars | effects ~32%, ~70%, ~38%, ~36% [estimated] |
| 4 | P1.F6 (Lee Fig 3J-K) | effect N/A on bar charts | p62 51 vs 11 (*), LC3 38 vs 12 (**) | effect ~4.6x [estimated] for p62 (matches the recorded <0.05); LC3 in description |
| 4b | P1.F4 (Lee Fig 3E) | effect and n N/A | log-scale violin of individual lysosomes; the dashed lines are not defined in the legend and no n is given for E-G | left N/A (reading a mean off unlabeled lines on a log axis would be a guess) |
| 5 | P4.F3 (de Leeuw Fig 4E) | effect N/A | LAMP2/actin E3 1.0 vs E4 0.57 (**) | effect ~43% [estimated] |
| 6 | P5.F5, P5.F6 (Krogsaeter Fig 5D, 6B) | effect N/A | OG alkaline:acidic 1.0 to 0.63 with siTmed5 (****); LGALS3BP PLA 95 vs 55, TMED5 65 vs 110 (****) | effects ~37%, ~42% [estimated] |
| 7 | P8.F4 (Guo Fig 5K) | effect N/A | CE(20:4)-E4 2.7 vs CE(18:1)-E4 0.1 (****) | effect ~96% [estimated] |
| 8 | P7.F2 (Fig 5C) | effect N/A; which pair is the P? | legend: APOE3-APOE4 p = 0.000038 (matches); bars 3.35 vs 5.8 | effect ~73% [estimated], description names the pair |
| 9 | P7.F1 (Fig 5D) | P might not be the comparison described | P 0.0059 is the within-APOE2 18-24 h decline; APOE4 is ns | effect "qualitative"; description now says what the P tests |
| 10 | P8.F5 (Guo Fig 6I) | effect N/A; which sub-panel carries the P? | all neurons: E3 vs E4 unmarked; LF-positive neurons: E3 1.12 vs E4 1.38 (**) | effect ~23% [estimated]; description says the difference is only in LF-positive neurons |
| 11 | P10.F1-F3 (PNAS Nexus Fig 1C, 4B, 5B) | P <0.05 although the panels show ** to ****; effects N/A | legends define no star key, only "significant differences (P < 0.05) indicated", so <0.05 is the correct recorded value; bars readable | P unchanged; effects ~3x, ~2.1x, ~37% [estimated] |
| 12 | P1.F8-F10 (Lee Fig 4F, 4I, 5B) | P N/A rests on reading Dunnett's control as APOE3 | legends say only "ANOVA followed by Dunnett's post hoc"; the control group is not named. Stars sit over APOE4 only, consistent with control = APOE3, but not proven | P left N/A (needs a human judgment); effects ~26%, ~75%, ~25% [estimated] added |
| 13 | P1.F8-F10 (Lee Fig 4F, 4I, 5B) | follow-up to 12 | human checker confirmed Dunnett comparison group = APOE3 | P <0.001, <0.0001, <0.05 [visual_only]; description says the P is APOE4 vs APOE3 and the effect is the rescue size |
| 14 | P1.F5 (Lee Fig 3H) | direction label: APOE4 raises cathepsin B activity, which runs against "impaired lysosome function", yet the row was not labelled contradicting | description already said it does not support the hypothesis, but the summary lacked CONTRADICTS, so the sheet counted it as supporting; README said 8 contradicting | summary and description now CONTRADICTS; README count 8 -> 9; README also corrected where it still said P1.F8-F10 P = N/A |
| 15 | P4.F5 (de Leeuw Fig 3G) | labelled as supporting, but is APOE4 vs APOE3 significant? | only E2 vs E4 carries a star; E3 ~1.0 vs E4 ~1.25 unmarked: a null for the hypothesis's own comparison | summary CONTRADICTS (no significant change vs APOE3); description rewritten |
| 16 | de Leeuw Fig 3D (missing) | a contradicting panel left out of the sheet? | total cholesterol by HPTLC is lower in APOE4 than APOE3 (~3.2 vs 6.2, *; text: "E2 = E3 > E4 = KO") | new row P4.F7, CONTRADICTS the accumulation direction; README now 68 findings, 11 contradicting |
| 17 | P4.F7 (de Leeuw Fig 3D) | contradicting, or lipid disruption that fits H5? | H5 wording is "disrupted lipid metabolism" (no direction); authors: "dysregulated cholesterol/lipid homeostasis" with "subcellular localization of cholesterol in lysosomes ... elevated" | relabelled as lipid disruption (not CONTRADICTS); README: 10 contradicting, direction disagreement noted; verifier R1 warning on this row is a false positive ("similar levels to APOE-KO") |
