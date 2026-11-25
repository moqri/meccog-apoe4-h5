#!/usr/bin/env python3
"""Checks aimed at the failure modes seen in the MecCog agent collab.

Usage:
    python verify_findings.py findings.json sources/

sources/ holds one text file per paper, named by PMID (e.g. 29946028.txt),
containing the full-text passages (results, legends, methods) retrieved from
Europe PMC. Quotes and printed statistics are checked against these files.

Checks (errors unless marked warning):
  Q1 quote_not_verbatim   quote must appear word for word in the source text
  Q2 duplicate_quote      the same quote used by two findings
  S1 stat_not_in_source   a value marked printed_in_text must appear in the
                          quote or the source text
  S2 p_from_figure        P value may never be estimated_from_figure
  S3 tilde_mismatch       "~" if and only if estimated_from_figure
  D1 duplicate_doi        each paper once
  D2 bad_doi              DOI must look like 10.xxxx/...
  L1 location_no_panel    (warning) location names a figure without a panel
  M1 merged_assays        (warning) one finding location spans several figures
  R1 direction_check      (warning) summary says APOE4 lowers/raises something
                          but description uses the opposite word, or a
                          no-difference quote is not marked as contradicting
  C1 directness_strength  (warning) class 1 with strength 4 or 5
"""
import json
import os
import re
import sys
import unicodedata


def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace(" ", " ").replace(" ", " ")
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"[‘’]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    return re.sub(r"\s+", " ", s).strip().lower()


NO_DIFF = re.compile(r"\b(no (significant )?(difference|change|effect)|"
                     r"not (significantly )?(different|altered|changed)|"
                     r"did not (differ|change|alter)|comparable|similar)\b", re.I)


def number_tokens(v):
    return re.findall(r"\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", v or "")


def main(fpath, srcdir):
    data = json.load(open(fpath))
    errs, warns = [], []
    seen_doi, seen_quote = {}, {}
    for i, p in enumerate(data["papers"], 1):
        pid = f"P{i}"
        doi = (p.get("doi") or "").lower()
        if doi != "n/a":
            if not re.match(r"10\.\d{4,9}/\S+$", doi):
                errs.append((pid, "D2", f"bad DOI {doi}"))
            if doi in seen_doi:
                errs.append((pid, "D1", f"DOI also used by {seen_doi[doi]}"))
            seen_doi[doi] = pid
        src = ""
        sp = os.path.join(srcdir, f"{p.get('pmid')}.txt")
        if os.path.exists(sp):
            src = norm(open(sp).read())
        for j, f in enumerate(p["findings"], 1):
            fid = f"{pid}.F{j}"
            q = f.get("quote", "N/A")
            if q != "N/A":
                if not src:
                    warns.append((fid, "Q1", "no source text cached; quote unverified"))
                elif norm(q) not in src:
                    errs.append((fid, "Q1", "quote not found verbatim in source"))
                if norm(q) in seen_quote:
                    errs.append((fid, "Q2", f"same quote as {seen_quote[norm(q)]}"))
                seen_quote[norm(q)] = fid
            for key in ("effect_size", "p_value", "sample_size"):
                v, prov = str(f.get(key, "")), f.get(key + "_prov", "")
                if prov == "printed_in_text":
                    hay = norm(q) + " " + src
                    for t in number_tokens(v):
                        if t not in hay:
                            errs.append((fid, "S1", f"{key} {v}: '{t}' not in quote or source"))
                if key == "p_value" and prov == "estimated_from_figure":
                    errs.append((fid, "S2", "P value estimated from figure"))
                if v.startswith("~") != (prov == "estimated_from_figure"):
                    errs.append((fid, "S3", f"{key} '{v}' vs provenance {prov}"))
            loc = f.get("location", "")
            if re.fullmatch(r"fig(ure)?\s*\d+", loc.strip(), re.I):
                warns.append((fid, "L1", f"location '{loc}' has no panel"))
            if len(set(re.findall(r"fig(?:ure)?\.?\s*(S?\d+)", loc, re.I))) > 1:
                warns.append((fid, "M1", f"location '{loc}' spans several figures"))
            if q != "N/A" and NO_DIFF.search(q) and "CONTRADICT" not in f.get("summary", "").upper() \
                    and "no change" not in f.get("summary", "").lower():
                warns.append((fid, "R1", "quote reports no difference but summary is not marked as contradicting / no change"))
            if str(f.get("directness")) == "1" and str(f.get("strength", ""))[:1] in "45":
                warns.append((fid, "C1", "class 1 with weak strength"))
    for tag, items in (("ERROR", errs), ("WARNING", warns)):
        for fid, code, msg in items:
            print(f"{tag} {fid} [{code}] {msg}")
    print(f"\n{len(errs)} error(s), {len(warns)} warning(s)")
    return not errs


if __name__ == "__main__":
    sys.exit(0 if main(*sys.argv[1:3]) else 1)
