# APOE4 knowledge graph (H5 findings)

`docs/index.html` (copied to `index.html` at the repo root, which GitHub Pages serves) is an interactive map of every finding in the H5 submission, drawn as a MecCog mechanism schema: steps (SSPs) joined by mechanism modules (ovals). Each step opens into narrow branches, and every finding sits in exactly one branch. Class 2 findings (a lipid changed, the lysosome measured) form the module between the lipid step and the lysosome step. SSP1, SSP2 and the outcome are copied from MecCog's mechanism example; SSP3 and SSP4 use the words of the H5 statement; SSP5 and the branch names are ours.

Rebuild after the workbook changes:

    python3 docs/viz/build.py path/to/h5_submission.xlsx path/to/meta.json <commit-sha>

`meta.json` is optional; it only supplies paper titles. The concept tags, link directions, cell-type groups and the six-step chain are assigned by hand in `build.py` for this view. They are not columns of the submission. When a finding is added, give it a line in the edge table in `build.py`, or the build stops with the missing ID.
