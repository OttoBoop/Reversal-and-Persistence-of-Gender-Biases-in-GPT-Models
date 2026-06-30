# JAIR build — notes

`main_jair.tex` is the **JAIR-targeted rebuild** of the paper, derived from
`../main_english.tex` (**the canonical paper is unchanged**). Per the agreed scope this is a
**reframe + convert (no length padding)** build that adds **new measurement reliability/validity
analyses computed from the existing data**. Rationale/norms: see
`../../docs/journal_style_research/02_jair.md` and `.../adaptations/jair.md`.

## What was applied
- **Reframing:** repositioned as a *reproducible measurement methodology for gender-association
  drift*; "overcorrection" is demoted to a demonstration.
  - New `\section{A Measurement Framework for Gender-Association Drift}` (before Methodology).
  - New `\subsection{Measurement reliability and validity}` (the new analyses, see below).
  - New `\section{Discussion and Implications}` (before Conclusion).
- **Mechanical conversion to JAIR house style:**
  - Abstract → single paragraph, **no in-text citations** (~184 words).
  - Citations → **theapa** (`\citet`→`\citeA`, `\citep`/`\citealp`→`\cite`); `\bibliographystyle{theapa}`.
  - Preamble → `\documentclass[jair,11pt,letterpaper]{article}` + `\usepackage{jair,theapa}`;
    `geometry`/`setspace` disabled (the class controls layout); `\graphicspath{{../figuras_final/}}`.
  - **Table captions moved below** the tables (6 tables); figure captions were already below.
  - Section labels added so cross-references resolve.
  - **Declarations** block added (CC BY notice, AI-use, COI, funding, data/code).
- **Appendix merged (single self-contained file):** `../appendix.tex` is folded into
  `main_jair.tex` as lettered appendices — **Appendix A: Definition of Bias** (the formal bias
  construct) and **Appendix B: Full Regressions** (the 20+ per-model regression tables). The
  standalone `\maketitle`/wrapper section was dropped, headings promoted, the `heymann2020`
  citation key corrected to `heymann2021` (the key present in the bib), and cross-references
  added from the Framework section (`\ref{app:bias}`, `\ref{app:fullreg}`). The appendix
  regression tables use bold run-in headers rather than `\caption{}`, so the
  "captions below" rule is not triggered there (optional polish: convert them to captioned
  tables). The canonical `../appendix.tex` is unchanged.

## New analyses (computed from the data — flagged for advisor validation)
`analysis/measurement_validity.py` (re-runnable, offline) → `analysis/measurement_validity.md`:
- **Split-half reliability** of P(male) per condition: Pearson **0.941 / 0.915 / 0.909**
  (Tests 1/2/3), Spearman–Brown **0.970 / 0.956 / 0.952**.
- **Classifier validity:** pooled **Unknown = 2.42%** (unresolved 2.53%); 0–4.8% across families.
- **Convergent validity** (model-level P(male) across tests): Pearson **0.46–0.82**
  (strongest T2↔T3 = 0.822).
- ⚠️ **Quant substance — to be validated by the advisor (Valdemar Pinho Neto).** Note the
  validity corpus is reported as N≈32,613 stories (resolved-gender subset); reconcile with the
  paper's 62k total before submission.

## Compilation
**This environment has no `jair.sty`/`theapa`** (jair.org/CTAN, crates.io, and the tectonic
bundle host are all blocked by the network policy), so the JAIR-class file cannot be compiled
here directly. We therefore verify with a **local fallback build**:

- `analysis/build_local.py` regenerates `_localcheck.tex` by swapping the JAIR preamble for
  `article`+`natbib`+`apalike` and down-converting the theapa cite commands, then:
  - `latexmk -pdf -bibtex -cd _localcheck.tex` → **`main_jair_localcheck.pdf` (52 pages,
    incl. merged Appendices A–B), 0 undefined citations, 0 undefined references, no errors.**
- The canonical `../main_english.tex` also compiles here (34 pages) — toolchain sanity check.

**Reproduce the local PDF:**
```
python3 analysis/build_local.py
latexmk -pdf -bibtex -interaction=nonstopmode -cd _localcheck.tex
cp _localcheck.pdf main_jair_localcheck.pdf
```

**Final production build (real JAIR class) — on Overleaf:**
1. Open the JAIR Author Kit / Overleaf template (https://www.overleaf.com/read/hycbzkdksrzz → copy).
2. Add `main_jair.tex`, `referencias.bib`, and the `figuras_final/` images (or point
   `\graphicspath` at them).
3. Ensure `jair.sty`, `theapa.sty`, `theapa.bst` are present (they ship with the Author Kit);
   compile with pdfLaTeX + BibTeX. `main_jair.tex` already targets that class/style.

## Remaining TODOs before submission
- Advisor (Valdemar) validation of the **Framework**, **Discussion**, and **validity analyses**.
- Fill the `[TODO]` placeholders in the Declarations (year, funding, data DOI, AI-use wording).
- The analytic appendix is now **merged in-paper** (Appendix A/B); the **raw data, code, and
  notebook** still go to **JAIR online appendices** (the data-availability statement points
  there). Optional polish: convert the appendix regression blocks to `\caption{}`-ed tables.
- Confirm the `UNCONFIRMED` JAIR guideline points listed in `.../adaptations/jair.md`
  (abstract word limit, keyword count, etc.).
- Candor: JAIR has ~no precedent for this audit genre even after reframing — see the dossier's
  fit caveat.
