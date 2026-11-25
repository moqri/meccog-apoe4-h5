# Method

MecCog Step 1 submission.

- **Team:** c-brain
- **Hypothesis:** H5. In some types of non-Alzheimer's, non-aged human brain cells, APOE4 disruption of lipid metabolism, compared with APOE3, results in impaired late endosome/lysosome function.
- **Submission date:** TBD

---

## 1. Who did the work

An agent did the searching, screening, extraction and checking; a person supplied one paper's full text and reviews the result before submission. Concretely: the agent ran the Europe PMC and PubMed searches, the citation-graph expansion, the relevance screen, the full-text retrieval, the extraction of every finding and the automated quote and statistic checks. The person obtained the publisher PDF of the starting reference, which no open archive carries, and is the only human check on the output at the time of writing. Section 5 says exactly how much has been human-checked.

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

The starting reference, Lee et al. 2023 (PMID 37777962, doi 10.1016/j.celrep.2023.113183), is Cell Press open access but is deposited in neither Europe PMC nor PMC, and the container's network policy did not reach cell.com at the time. A person downloaded the publisher PDF and supplied it; text was extracted with `pdftotext` and the six figure pages were rendered to images and read. So for this one paper the source of record is the publisher PDF, not an archive copy. Supplementary files were not retrieved for any paper: where a value lives only in a supplement, the provenance says `full_text_unavailable` rather than claiming the paper does not report it.

## 5. What a human checked

At the time of writing, nothing in the spreadsheet has been read against the papers by a person. The person supplied one PDF and will review before submission; this README will be updated with the proportion actually checked. Treat the current file as agent output with automated checks only.

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

**Contradicting findings are in.** Eight of the 67 are recorded as contradicting or showing no difference, and they are not confined to weak papers:

- de Leeuw et al. 2022 (P4) finds lysosomal activity equally low in APOE3 and APOE4 isogenic astrocytes, and no genotype difference in lysosomal compartment area. This is a direct, class 1 contradiction of the hypothesis in the same cell type as the starting reference.
- Hellén et al. 2025, APOE4/4 iPSC microglia (P6) show a lysosomal degradation deficit but no cholesterol difference at all, which breaks the lipid half of the mechanism, and no difference in autophagic flux.
- Nyberg et al. 2025 (P9) find no endolysosomal difference in mature neurons at 18 days, the deficit appearing only after prolonged culture, and, importantly, cholesterol loading impairs degradation equally in APOE4, APOE3 and knockout neurons, so lipid load alone does not reproduce the genotype effect.

**Directions that disagree between papers.** LysoTracker signal goes up with APOE4 in Lee 2023 and down with APOE4 in the miBrain paper (Mesentier-Louro et al. 2026) and in the neuronal APOE4 cell lines. Cathepsin B activity is higher in APOE4 astrocytes in Lee 2023 and lower in APOE4 neuronal cells and microglia. Both are recorded as measured, with the discrepancy noted in the finding description rather than resolved in favour of the hypothesis.

**On the starting reference.** Its parental donor had Alzheimer's disease, the APOE3 line being the CRISPR-corrected isogenic control. The hypothesis is scoped to non-Alzheimer's cells, so the system column says so; a second isogenic pair from a healthy APOE3 donor is used for some panels, and those are marked.

**Statistics.** Where the starting reference reports significance only as asterisks, the inequality recorded is the one its own figure legend assigns to that number of asterisks, with provenance `visual_only`, never a number estimated off a bar. Effect sizes marked with a leading `~` were measured off a panel of that paper by eye and are deliberately coarse. For the other twelve papers, figure images were not read: where the text and legends print no number, the provenance says so rather than guessing.

**Known weaknesses.** No human has verified the extraction yet. Supplementary materials were not retrieved. Only one of the thirteen papers was read from a publisher PDF, the rest from archive XML, so a value present only in a typeset table could have been missed. Three papers in the set are not human brain cells (primary mouse neurons, mouse and human cell lines) and are marked in the experimental system column with a caveat; they are included because they carry the most direct causal tests of the lipid-to-lysosome step, not because they meet the hypothesis scope.

---

## Code and prompts

- `retrieval/search.py`, `retrieval/search2.py`: Europe PMC searches and citation-graph expansion.
- `retrieval/fetch.py`, `retrieval/fetch2.py`: full-text retrieval (Europe PMC, then NCBI E-utilities) and passage extraction to `sources/{PMID}.txt`.
- `findings_src/p1.py` ... `p13.py`: one script per paper holding its curated findings, each quote copied from the cached source; `common.py` is the shared record helper. Running them writes the per-paper JSON that is merged into `findings.json`.
- `findings.json`: the curated findings, the input to both scripts below.
- `pipeline/verify_findings.py findings.json sources/`: the automated checks described in section 5.
- `pipeline/build_submission.py findings.json method.json out.xlsx`: builds the 19-column workbook and the Method sheet.

The cached full texts in `sources/` are not published here because several are under publisher copyright; `retrieval/fetch2.py` regenerates the archive ones, and the starting reference comes from its publisher PDF as described in section 4.
