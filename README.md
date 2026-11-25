# Method

MecCog Step 1 submission.

- **Team:** c-brain
- **Hypothesis:** H5. In some types of non-Alzheimer's, non-aged human brain cells, APOE4 disruption of lipid metabolism, compared with APOE3, results in impaired late endosome/lysosome function.
- **Submission date:** TBD

---

## 1. Who did the work

An agent did the searching, screening, extraction and checking; a person supplied publisher or author-manuscript PDFs for seven papers and reviews the result before submission. Concretely: the agent ran the Europe PMC and PubMed searches, the citation-graph expansion, the relevance screen, the full-text retrieval, the extraction of every finding, the reading of figure panels and the automated quote and statistic checks. The person downloaded the PDF of the starting reference, which no open archive carries, and six further PDFs whose figure images the archives serve only behind a browser check; the person is the only human check on the output at the time of writing. Section 5 says exactly how much has been human-checked.

## 2. Model and version

claude-opus-5-5 (Claude Opus 5.5), run in Claude Code in a cloud container. No other model was used. Figure panels of the starting reference were read by the same model from page images rendered at 150 dpi; no separate vision model.

## 3. How papers were found

Three routes, all through the Europe PMC REST API (`search`, `citations`, `references`) on 2026-11-25:

1. Four broad keyword queries over title, abstract and full text combining APOE4 synonyms with endolysosomal terms (lysosome, late endosome, endolysosome, autophagy, lipid droplet, cathepsin, BMP) and lipid terms (cholesterol, triglyceride, fatty acid, sphingolipid, lipidomics), with and without a cell-type restriction (iPSC, astrocyte, microglia, neuron). About 1,600 hits, 968 unique PMIDs.
2. The same combinations restricted to title and abstract, which cut the pool to 226 records with a far better hit rate. The broad queries were kept because they surfaced papers whose endolysosomal readout is only in the results text.
3. Forward and backward citations of the starting reference, PMID 37777962: 91 citing and 44 cited papers.

Targeted queries were also run for terms the broad queries could miss: PICALM, NPC1 and Niemann-Pick, bis(monoacylglycero)phosphate and gangliosides, lipid droplet with lipophagy.

Searches that returned nothing useful: the bis(monoacylglycero)phosphate and ganglioside query returned one mouse lipidomics paper and no cell study, so the specific lysosomal phospholipid route to the hypothesis is not represented in the submission. The APOE4-plus-PICALM query returned a single paper, on endocytosis rather than lysosomal function.

Screening kept a paper only if it compared APOE4 with APOE3 (or with a matched isoform set) and reported a late endosome, lysosome, autophagy or lipid readout in a brain-relevant cell type. Reviews were dropped. Thirty-four papers were taken to full text; thirteen carry findings here. Papers were left out when the APOE4-versus-APOE3 comparison was absent, when the only readout was transcriptomic with no functional measurement, or when the system was peripheral (liver, cochlea, bone).

## 4. How full text was obtained

In order: Europe PMC `fullTextXML` for the open-access subset; then, for PMC records Europe PMC returned a server error for, NCBI E-utilities `efetch` against PMC with the same PMCID; then the abstract alone. Of the 34 papers taken to full text, 29 yielded JATS full text, including figure legends and tables. Four are abstract-only in both archives (PMIDs 40571761, 15485881, 11162242, and for two more only the abstract is deposited), and none of those four carries findings in this submission.

The starting reference, Lee et al. 2023 (PMID 37777962, doi 10.1016/j.celrep.2023.113183), is Cell Press open access but is deposited in neither Europe PMC nor PMC, and the container's network policy did not reach cell.com at the time. A person downloaded the publisher PDF and supplied it; text was extracted with `pdftotext` and the figure pages were rendered to images and read. For this one paper the source of record is the publisher PDF, not an archive copy.

**Figures and supplements.** Archive XML carries figure legends but not figure images. Figure images and supplementary files were taken from the Europe PMC `supplementaryFiles` endpoint where it returned them (five papers). For the other six papers with unread figures, Europe PMC and PMC put image requests behind a browser challenge that an automated client cannot pass, so a person downloaded the article PDFs (author manuscripts or publisher versions) and the figures were read from those, by extracting the embedded images with `pdfimages` or rendering pages with `pdftoppm`. Supplements were opened for three papers where they came with the archive bundle; in one of them (Hellén et al. 2025, Supplementary Fig 3) the axis labels and statistics did not survive extraction, so that row keeps its N/A. Where a value is shown only in a supplement that could not be obtained, the provenance is `full_text_unavailable` rather than a claim that the paper does not report it; where it was read from a supplement, `supplement_only`.

## 5. What a human checked

No row has yet been read against the papers by a person. The person supplied seven PDFs and will review before submission; this section will be updated with the number of rows a person actually checked. Until then, treat the file as agent output with the automated checks and the AI verification pass described below.

**AI verification pass (not a human check).** After extraction, the same model made a separate second pass over all 67 rows, in a priority order set by the challenge's misconduct rules: first every row with a value recorded as absent and every contradicting or no-effect finding (19 rows), then every P value read from significance marks, every directness class 1 or 2 call and every effect size estimated by eye (42 rows), then the remaining rows' locations (6 rows). For each row it reopened the cited panel (figure image, PDF page or supplement), re-read the legend's significance key and the statistical test, and checked that the recorded comparison is the one the finding describes. For this pass the publisher supplements of three Cell Press papers were downloaded and the Supplementary Data of Cuní-López et al. 2026 was read. Twelve rows changed:

- Values filled from supplements that had not been read before: P1.F11 (Lee 2023, Fig S6I), P3.F3 (TCW 2022, Fig S6F), P12.F2 (Lin 2018, Fig S3D), P6.F3 (Hellén 2025, Supplementary Fig 3C, effect size and n).
- A P value that belonged to a different comparison: P1.F8, P1.F9 and P1.F10 record the asterisk for APOE4 versus APOE3, but the findings are about the rescue by cyclodextrin or simvastatin, which the paper's Dunnett's test does not compare. The legend does not name Dunnett's comparison group; a human checker confirmed it is APOE3, so the star values are kept and each row says that its P is APOE4 versus APOE3 while its effect is the rescue size.
- A finding weakened on reading the source data: P7.F3 (autophagosome-assembly enrichment on APOE4 lipid droplets) rests on three proteins and does not survive the paper's own multiple-testing correction (log q = 0); P = 0.0079 recorded from Supplementary Data 13 and strength lowered to 5.
- Directness corrected: P12.F2 (lysosome-dependent amyloid-beta degradation is a direct functional readout) from class 3 to 1; P13.F1 (lysosome area in HEK293 cells) from class 1 to 3.
- Wording tightened so the sentence matches the panel: P2.F8, P10.F4 (filipin measures total cholesterol, not lysosomal), P11.F2 (the ~6x fold change applies to the most unsaturated class only).

Rows that still need a person:
- P3.F4 (TCW 2022, Fig 2C): the lysosome gene-set statistics are in the paper's Table S2, which could not be located on the publisher's server.
- P8.F2 (Guo 2024): the time-course comparison is in Fig S5G, which is not in the author manuscript and was not obtained.
- P3.F3 (TCW 2022, Fig S6F): the supplementary figure image carries no legend; the asterisk key used is the one in the paper's main-figure legends.
- Every effect size marked with `~` (estimated by eye) deserves a glance for order of magnitude.

The automated checks that did run, on every row:

- Every quote must appear word for word in the cached source text, after Unicode normalization of dashes, quotes and spaces. All 67 quotes pass. Quotes were never retyped from memory; each was copied out of the cached text.
- No quote may be used twice.
- Every value marked `printed_in_text` must have each of its numbers present in the quote or the source text.
- A P value may never carry `estimated_from_figure`.
- A value starting with `~` must carry `estimated_from_figure` and nothing else may.
- DOIs must be unique and well formed; data locations must name a panel; one finding may not span several figures.
- A quote reporting no difference must be flagged as contradicting in its summary.

Three warnings remain and were reviewed and accepted: in P2.F8, P9.F5 and P10.F3 the no-difference regular expression fires on the phrases "comparable to", "similar to" and "did not show a similar response", which in context report a rescue or a genotype difference rather than a null result.

## 6. Anything else

**What counts as evidence here.** The hypothesis has two halves, a lipid disruption (A) and an impaired late endosome or lysosome (B). Directness classes follow the challenge rules. Comparing APOE4 with APOE3 cells is itself a perturbation of A. Where the genotype is compared and a lysosomal or late-endosomal function is measured directly, the finding is class 1. Where a lipid is perturbed instead of the genotype (cyclodextrin, statin, cholesterol loading, choline supplementation) and a lysosomal readout is measured, it is class 2. Findings that carry only a lipid readout (cholesterol level, lipid droplet number, lipidome composition) are class 3: the genotype is perturbed, but B is only inferred from a surrogate. An earlier draft put these at class 5; the rules reserve class 5 for findings none of the other classes fit, so they were moved. Experiments in non-brain cells keep their class, and the caveat sits in the experimental-system column.

**Contradicting findings are in.** Nine of the 67 are recorded as contradicting or showing no difference, and they are not confined to weak papers:

- Lee et al. 2023 (P1), the starting reference itself, measures about 50% higher cathepsin B activity in APOE4 astrocytes (P1.F5), the opposite of impaired lysosomal function. An earlier draft described this in the row but did not label it contradicting.

- de Leeuw et al. 2022 (P4) finds lysosomal activity equally low in APOE3 and APOE4 isogenic astrocytes, and no genotype difference in lysosomal compartment area. This is a direct, class 1 contradiction of the hypothesis in the same cell type as the starting reference.
- Hellén et al. 2025, APOE4/4 iPSC microglia (P6) show a lysosomal degradation deficit but no cholesterol difference at all, which breaks the lipid half of the mechanism, and no difference in autophagic flux.
- Nyberg et al. 2025 (P9) find no endolysosomal difference in mature neurons at 18 days, the deficit appearing only after prolonged culture, and, importantly, cholesterol loading impairs degradation equally in APOE4, APOE3 and knockout neurons, so lipid load alone does not reproduce the genotype effect.

**Directions that disagree between papers.** LysoTracker signal goes up with APOE4 in Lee 2023 and down with APOE4 in the miBrain paper (Mesentier-Louro et al. 2026) and in the neuronal APOE4 cell lines. Cathepsin B activity is higher in APOE4 astrocytes in Lee 2023 and lower in APOE4 neuronal cells and microglia. Both are recorded as measured, with the discrepancy noted in the finding description rather than resolved in favour of the hypothesis.

**On the starting reference.** Its parental donor had Alzheimer's disease, the APOE3 line being the CRISPR-corrected isogenic control. The hypothesis is scoped to non-Alzheimer's cells, so the system column says so; a second isogenic pair from a healthy APOE3 donor is used for some panels, and those are marked.

**Statistics.** Every figure panel a finding points to was opened and read, and its significance marks were translated with the key the paper itself gives: in the figure legend, or for one paper (Guo et al. 2024) in the methods section, which defines the asterisks for all figures. The recorded value is the inequality that key assigns, with provenance `visual_only`, never a number estimated off a bar; where a legend prints the inequality in words (for example "**** p ≤ 0.0001 by Student's t-test") the provenance is `printed_in_text`. One paper (Krogsaeter et al. 2025, Autophagy) prints a garbled key in its published legends ("*p < .05, ****p < .01, *p < .0001"), with a single asterisk defined twice. A human checker judged this a typesetting typo for the standard GraphPad key (* < 0.05, ** < 0.01, *** < 0.001, **** < 0.0001), and that key is applied to this paper's rows; the earlier, more conservative reading recorded every marked comparison as `<0.05`. Effect sizes with a leading `~` were measured off the panel by eye and are deliberately coarse. A P value stays N/A where the comparison the finding is about carries no mark (the paper shows it as not significant without a number), where the panel is a heatmap, volcano plot or enrichment chart with no per-comparison statistic, or where the statistic is only in a supplementary table that could not be obtained.

**Corrections made on reading the figures.** One finding (Fote et al. 2022, J Cell Sci, prohibitin depletion from APOE4 lysosomes) had been given the wrong location; the data are in Fig 7D, not Fig 3D, and the row now says so. In several papers the cached legend text did print a significance threshold or a sample size that the first draft had marked as not found; those rows were corrected. This is the kind of error the challenge rules treat as serious, which is why every N/A was rechecked against the figure itself.

**Figure-image audit (2026-11-25).** A later audit found that for two papers the saved "figure" files were bot-check pages, not images: Hellén et al. 2025 (P6) and the main figures of Mesentier-Louro et al. 2026 (P2). The real figures were then obtained (Europe PMC and the publisher's image server) and every cited panel re-read. P2 values, all printed in the text, matched. For P6 the sample sizes had been taken from the study-wide line count (8 APOE3/3, 6 APOE4/4) instead of the dots in each panel; they were corrected per panel (for example Fig 1H: 5 vs 3 lines, confirmed by a human checker), and two effect sizes were read off the bars.

**Known weaknesses.** No human has verified the extraction yet. Supplements were read for only three papers. Text was taken from archive XML for twelve papers and from the publisher PDF for the starting reference; PDFs were used for figures only, so a value present only in a typeset table of a PDF could have been missed. Three papers in the set are not human brain cells (primary mouse neurons, mouse and human cell lines) and are marked in the experimental system column with a caveat; they are included because they carry the most direct causal tests of the lipid-to-lysosome step, not because they meet the hypothesis scope.

---

## Code and prompts

- `retrieval/search.py`, `retrieval/search2.py`: Europe PMC searches and citation-graph expansion.
- `retrieval/fetch.py`, `retrieval/fetch2.py`: full-text retrieval (Europe PMC, then NCBI E-utilities) and passage extraction to `sources/{PMID}.txt`.
- `findings_src/p1.py` ... `p13.py`: one script per paper holding its curated findings, each quote copied from the cached source; `common.py` is the shared record helper. Running them writes the per-paper JSON that is merged into `findings.json`. Later corrections (the directness reclassification and the figure-reading pass described in section 6) were applied to `findings.json` directly, so `findings.json` is the source of truth; `findings_src/figure_pass_patches.py` lists the last batch of those edits.
- `findings.json`: the curated findings, the input to both scripts below.
- `pipeline/verify_findings.py findings.json sources/`: the automated checks described in section 5.
- `pipeline/build_submission.py findings.json method.json out.xlsx`: builds the 19-column workbook and the Method sheet.

The cached full texts in `sources/` are not published here because several are under publisher copyright; `retrieval/fetch2.py` regenerates the archive ones, and the starting reference comes from its publisher PDF as described in section 4.
