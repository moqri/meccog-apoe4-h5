#!/usr/bin/env python3
"""Build a MecCog Step 1 submission workbook from a curated findings JSON.

Usage:
    python build_submission.py findings.json method.json out.xlsx

findings.json:
{
  "hypothesis": "<verbatim statement>",
  "papers": [
    {"doi": "10.x/..", "source_type": "PubMed published", "pmid": "123",
     "findings": [
       {"description": "...", "quote": "...", "summary": "(APOE3 -> APOE4) -> (...)",
        "relevance": 0.9, "system": "...", "location": "Fig 2C",
        "effect_size": "40%", "effect_size_prov": "printed_in_text",
        "p_value": "<0.01", "p_value_prov": "printed_in_text",
        "sample_size": "3", "sample_size_prov": "printed_in_text",
        "directness": 1, "strength": "1 very strong"}
     ]}
  ]
}
method.json: {"Team":..., "Team leader":..., "Team leader email":..., "Method URL":...,
              "Commit SHA":..., "Who did the work":..., "Model and version":...}
"""
import json
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font

COLUMNS = [
    "Hypothesis", "DOI", "Paper/source type", "PubMed ID", "Paper/Finding ID",
    "Finding description", "Finding quote", "Finding summary",
    "Finding relevance", "Experimental system", "Data location",
    "Effect size", "Effect size provenance", "P value", "P value provenance",
    "Sample size", "Sample size provenance", "Directness class",
    "Directness strength",
]
METHOD_FIELDS = ["Team", "Team leader", "Team leader email", "Method URL",
                 "Commit SHA", "Who did the work", "Model and version"]
FINDING_KEYS = ["description", "quote", "summary", "relevance", "system",
                "location", "effect_size", "effect_size_prov", "p_value",
                "p_value_prov", "sample_size", "sample_size_prov",
                "directness", "strength"]


def build(findings, method, out):
    wb = Workbook()
    ws = wb.active
    ws.title = "Submission"
    ws.append(COLUMNS)
    for c in ws[1]:
        c.font = Font(bold=True)
    ws.append([findings["hypothesis"]] + [None] * (len(COLUMNS) - 1))
    for i, p in enumerate(findings["papers"], 1):
        pid = f"P{i}"
        ws.append([None, p["doi"], p["source_type"], p.get("pmid", "N/A"), pid]
                  + [None] * 14)
        for j, f in enumerate(p["findings"], 1):
            vals = [f[k] for k in FINDING_KEYS]
            ws.append([None, None, None, None, f"{pid}.F{j}"] + vals)
    widths = {"A": 30, "B": 26, "C": 16, "D": 11, "E": 9, "F": 60, "G": 60,
              "H": 40, "J": 50, "K": 14}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")

    ms = wb.create_sheet("Method")
    for k in METHOD_FIELDS:
        ms.append([k, method[k]])
    ms.column_dimensions["A"].width = 22
    ms.column_dimensions["B"].width = 70
    wb.save(out)


if __name__ == "__main__":
    f, m, o = sys.argv[1:4]
    build(json.load(open(f)), json.load(open(m)), o)
    print("wrote", o)
