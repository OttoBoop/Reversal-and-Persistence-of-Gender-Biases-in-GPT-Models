#!/usr/bin/env python3
"""
JAIR build helper.

1. Convert the DELIVERABLE main_jair.tex citations from natbib -> theapa (in place):
   \citet -> \citeA, \citep -> \cite, \citealp/\citealt -> \cite/\citeA.
   (Sections inserted for the JAIR build already use \citeA/\cite, so they are untouched.)
2. Generate a LOCAL-CHECK file _localcheck.tex that compiles WITHOUT jair.sty/theapa
   (which are not available in this environment): swap the JAIR preamble back to
   article+natbib+apalike and down-convert theapa cite commands to natbib so the
   shared body compiles to a real verification PDF.

Run from anywhere; paths are relative to this script's directory.
"""
import re, pathlib

HERE = pathlib.Path(__file__).resolve().parent          # .../paper/latex/jair/analysis
JAIR = HERE.parent                                       # .../paper/latex/jair
MAIN = JAIR / "main_jair.tex"
LOCAL = JAIR / "_localcheck.tex"

src = MAIN.read_text(encoding="utf-8")

# ---- 1. Deliverable: natbib -> theapa (only the original commands) ----
def to_theapa(s):
    s = re.sub(r'\\citet(?=[\[{])', r'\\citeA', s)
    s = re.sub(r'\\citealt(?=[\[{])', r'\\citeA', s)
    s = re.sub(r'\\citep(?=[\[{])', r'\\cite', s)
    s = re.sub(r'\\citealp(?=[\[{])', r'\\cite', s)
    return s

src = to_theapa(src)
MAIN.write_text(src, encoding="utf-8")

# ---- 2. Local-check: theapa preamble -> article+natbib, theapa cites -> natbib ----
local = src
local = local.replace(
    r"\documentclass[jair,11pt,letterpaper]{article}",
    r"\documentclass[12pt,a4paper]{article}")
local = local.replace(
    "\\usepackage{jair}\n\\usepackage{theapa}\n\\bibliographystyle{theapa}",
    "\\usepackage{natbib}\n\\bibliographystyle{apalike}")
local = local.replace(
    "% \\usepackage[margin=2.5cm]{geometry}\n% \\usepackage{setspace}\n% \\onehalfspacing",
    "\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{setspace}\n\\onehalfspacing")
# down-convert theapa cite commands to natbib equivalents
local = re.sub(r'\\citeA(?=[\[{])', r'\\citet', local)
local = re.sub(r'\\cite(?![A-Za-z])', r'\\citep', local)   # \cite{ / \cite[ -> \citep ; leaves \citeauthor/\citeyear
local = local.replace("%%METRICS_SUBSECTION%%", "")        # placeholder removed for the local build if unfilled

LOCAL.write_text(local, encoding="utf-8")

# quick sanity report (avoid backslashes inside f-string expressions for older Python)
n_left = len(re.findall(r'\\cite[tp]\b', src)) + len(re.findall(r'\\citealp\b', src))
n_citeA = len(re.findall(r'\\citeA', src))
n_cite = len(re.findall(r'\\cite[{\[]', src))
print("deliverable remaining natbib citet/citep/citealp =", n_left)
print("deliverable theapa citeA =", n_citeA, " cite-paren =", n_cite)
print("wrote", LOCAL)
