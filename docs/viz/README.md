# APOE4 knowledge graph (H5 findings)

`docs/index.html` is an interactive knowledge graph of every finding in the H5 submission. It links APOE4 (and lipid interventions) to the concepts each finding measures. The graph is laid under a draft six-step H5 mechanism drawn in MecCog's SSP/MM notation. Link width shows the number of supporting (blue) and contradicting (red) findings. A solid link has at least one class 1 or 2 finding; a dashed link has only class 3 or 4 findings.

Rebuild after the workbook changes:

    python3 docs/viz/build.py path/to/h5_submission.xlsx path/to/meta.json <commit-sha>

`meta.json` is optional; it only supplies paper titles. The concept tags, link directions, cell-type groups and the six-step chain are assigned by hand in `build.py` for this view. They are not columns of the submission. When a finding is added, give it a line in the edge table in `build.py`, or the build stops with the missing ID.
