# Adaptation package: Journal of Artificial Intelligence Research (JAIR)

> JAIR is a diamond/platinum open-access core-AI journal (AI Access Foundation; CC BY, no APC) that publishes long, comprehensive, technically self-contained articles — refereed research, surveys, and technical notes — for an AI-researcher audience. Its load-bearing house features are: its own LaTeX class (`\documentclass[jair,11pt,letterpaper]{article}` + `jair.sty` + `theapa`), author-date APA citation via `theapa` (NOT numeric), a single-paragraph narrative abstract, BOTH figure AND table captions BELOW the artwork, lettered appendices after Acknowledgments, online appendices for data/code, a CC BY copyright notice, and an AI-use statement. There is no IMRaD mandate, so the paper's Test 1/2/3 layout, equation-in-text methodology, missing Discussion, and absent hypotheses are all tolerated. The single biggest lift is conceptual: an economist's product-audit has essentially zero precedent at JAIR, so the paper must be reframed as a reproducible multi-model measurement/methodology for gender-association drift, leaning on the Fairness & Bias in AI Special Track, with "overcorrection" demoted to a demonstration. The snippets below are ready to paste into a COPY of `paper/latex/main_english.tex` — the canonical file is not modified. **Adaptation-effort rating from the dossier: HIGH** (surface edits are Low; the reframing/repositioning dominates).

## 1. Conversion checklist (must-adopt, with where each is documented)

| Item | Status | What to do | Source |
|---|---|---|---|
| **Template / class** | MUST ADOPT | Switch from generic `article` (12pt/a4) to `\documentclass[jair,11pt,letterpaper]{article}` + `\usepackage{jair}` + `\usepackage{theapa}`; start from the Author Kit / Overleaf template. | https://www.jair.org/index.php/jair/formatting ; Overleaf: https://www.overleaf.com/read/hycbzkdksrzz ; jair.sty: https://www.cs.cmu.edu/afs/cs/project/jair/pub/information/format/latex/jair.sty |
| **Citation style** | MUST ADOPT (mechanical) | Already author-date. Replace natbib `apalike` + `\citet`/`\citep` with `\bibliographystyle{theapa}` + `\citeA`/`\cite`/`\citeyear`. | https://www.cs.cmu.edu/afs/cs/project/jair/pub/information/format/latex/theapa.txt |
| **Abstract** | MUST ADOPT | Collapse the current ~229-word, 2-paragraph, 8-citation abstract into ONE narrative paragraph, no in-text citations, ~150–200 words. (Structured Objective/Methods/Findings is encouraged, not required.) | https://www.jair.org/index.php/jair/about/submissions ; https://www.jair.org/index.php/jair/authorinstrs |
| **Structure (IMRaD/hypotheses/Discussion)** | ALREADY SATISFIED (tolerated) | No IMRaD mandate; Test 1/2/3, equation-in-text, no Discussion, no H1/H2 are all fine. (Adding a measurement-framing block and a Discussion is recommended for fit/length, not required.) | https://www.jair.org/index.php/jair/authorinstrs ; dossier §2 "Structure expectations" |
| **Heading conventions** | MUST ADOPT | Capitalize section/subsection titles; never open a section with a subsection (lead with body text); capitalize "Figure N"/"Table N" cross-references. | https://www.jair.org/index.php/jair/authorinstrs |
| **Figures** | ALREADY SATISFIED | Captions already BELOW; keep all in-artwork text ≥9pt. | https://www.jair.org/index.php/jair/authorinstrs |
| **Tables** | MUST ADOPT | Move table captions from ABOVE to BELOW the table (place `\caption{}` after `tabular`). | https://www.jair.org/index.php/jair/authorinstrs |
| **Appendices** | MUST ADOPT | Make appendices lettered (Appendix A/B…) and place them AFTER Acknowledgments; route notebook/CSVs/896 audit checks into JAIR online appendices. | https://www.jair.org/index.php/jair/about/submissions |
| **Keywords** | ALREADY SATISFIED (count UNCONFIRMED) | Keywords requested for indexing; current 5 are reasonable. Exact count/format UNCONFIRMED. | https://www.jair.org/index.php/jair/about/submissions |
| **Length** | MUST ADOPT (expand) | ~5,500-word main text is short; JAIR norm is 29–40+ pp. Expand toward a comprehensive treatment (measurement framing + Discussion help). No hard limit (UNCONFIRMED). | dossier §2 "Length norms" |
| **Declarations (CC BY + AI-use)** | MUST ADOPT | Add a CC BY copyright notice (required in every paper) and an AI-use statement (core contributions by authors; AI not an author). | https://www.jair.org/index.php/jair/about/submissions |
| **Anonymization** | ALREADY SATISFIED | Single-blind track; author anonymization NOT required. | https://www.jair.org/index.php/jair/about/submissions |

## 2. Rewritten abstract (ready to paste)

```latex
\begin{abstract}
The rapid deployment of Large Language Models (LLMs) has renewed concern that
generative systems may encode and amplify gender bias, yet how such bias
changes across successive model generations remains poorly measured. We present
a reproducible, multi-model measurement methodology for quantifying gender-
association drift in story-generation tasks, applied to more than fourteen
models of the GPT family released since 2020 and over sixty-two thousand
generated narratives. The framework combines three prompt-based elicitation
designs---varying employer-valued character traits, the valence of supervisor
feedback, and occupational power cues---with a linear-probability estimator
that reports the gender association of each manipulated attribute as a
percentage-point effect, together with an audit harness of nearly nine hundred
automated checks. Using this instrument we document a sharp behavioural shift:
alignment-tuned ``chat'' models from GPT-3.5 onward associate positively
valued attributes with non-male characters, a reversal absent in the near-
neutral ``completion'' GPT-3 baseline, while occupational stereotypes persist
across all generations. We interpret this pattern as overcorrection rather than
resolution, and we release the data, code, and audit checks so the measurement
can be re-run on future models.
\end{abstract}
```

**Word count: 184 words.** (Single paragraph, no in-text citations; within the ~150–200-word de-facto norm. Note: the no-citations-in-abstract rule for JAIR specifically is UNCONFIRMED, but is observed in all three dossier exemplars.)

## 3. New / restructured sections (ready-to-paste LaTeX skeletons)

> Both blocks are **DRAFTS requiring advisor (Valdemar) validation.** They use only citation keys confirmed present in `referencias.bib`.

**3a. Measurement-methodology framing section** (insert before `\section{Methodology}`; plays the JAIR "Preliminaries/Background" role and carries the core reframing):

```latex
% DRAFT -- requires advisor (Valdemar) validation.
\section{A Measurement Framework for Gender-Association Drift}
\label{sec:framework}

Work on bias in natural language processing increasingly distinguishes the
\emph{measurement} of bias from any single audit of a deployed system: what is
measured, whether the measure is valid, and whether it remains stable across
models are questions logically prior to reporting a bias value. We adopt this
stance and treat the present study as a measurement contribution. Rather than
asking only whether a given GPT model is biased, we specify a reusable
instrument---prompt designs, an estimator, and an automated audit harness---for
quantifying how the association between gender and valued attributes
\emph{drifts} as model generations succeed one another.

Early audits established that completion-style GPT models reproduce
human gender stereotypes in generated text \citeA{lucy2021}, and that
alignment interventions reshape, rather than simply remove, such associations
\citeA{liu2025}. Convergent evidence reports residual or redirected gender
effects in instruction-tuned models \citeA{wang2024,mirza2024,karvonen2025},
while \citeA{joshi2024} cautions that corrections need not generalise across
domains. These findings motivate a measurement that is (i) \emph{longitudinal}
across model generations, (ii) \emph{multi-attribute} rather than tied to a
single stereotype, and (iii) \emph{reproducible}, in the sense that an
identical protocol can be re-run on models released after publication.

Our instrument has three components. First, three prompt-based elicitation
designs manipulate, respectively, an employer-valued character trait, the
valence of supervisor feedback, and occupational power cues. Second, a
linear-probability estimator maps each manipulation onto the probability that
the generated character is male, reporting effects in percentage points; this
estimator is deliberately treated as one calibrated instrument within the
framework, not as a stand-alone econometric claim. Third, an audit harness of
roughly nine hundred automated checks validates parsing, gender assignment, and
prompt fidelity. The remainder of the paper details each component
(Section~\ref{sec:methodology}) and reports the drift it measures across the
GPT family (Section~\ref{sec:results}).
```

**3b. Discussion and Implications section** (insert before `\section{Conclusion}`):

```latex
% DRAFT -- requires advisor (Valdemar) validation.
\section{Discussion and Implications}
\label{sec:discussion}

\subsection{What the Measurement Reveals}
Applied across the GPT family, the instrument detects a discontinuity rather
than a gradient. The near-neutral association in completion-type GPT-3 gives
way, from GPT-3.5 onward, to a pronounced pro-female association on positively
valued attributes, while gender--occupation stereotypes persist across every
generation tested. We read this as \emph{overcorrection}: alignment shifts the
sign of the association on some axes without resolving it on others. This is
consistent with \citeA{liu2025} and with the residual or redirected effects
reported by \citeA{wang2024}, \citeA{mirza2024}, and \citeA{karvonen2025}, and
it concretises the cross-domain incompleteness anticipated by
\citeA{joshi2024}.

\subsection{Implications for Bias Measurement}
The result argues against single-snapshot, single-attribute audits. Because the
direction of bias is not stable across generations, a measure calibrated on one
model class can mislead when applied to the next; longitudinal, multi-attribute
instruments such as the one proposed here are needed to track drift rather than
to certify a fixed state. The persistence of occupational stereotypes alongside
attribute-level overcorrection further shows that an aggregate ``less biased''
verdict can mask heterogeneous, partially reversed effects.

\subsection{Broader Implications}
For practitioners, the findings caution that alignment is not monotone debiasing
and may introduce new asymmetries; downstream effects of biased model outputs
have well-documented real-world stakes \citeA{obermeyer2019}, and vendor
mitigation efforts are described only at a high level in artefacts such as the
GPT-4 System Card \citeA{openai2023}. We therefore release the prompts,
generations, estimator, and audit checks as online appendices so the
measurement can be reproduced and extended to models released after this paper.
```

## 4. Declarations / required statements (ready to paste)

> Insert before `\bibliography{referencias}`. Mark `[TODO]` values for the authors.

```latex
\section*{Copyright Notice}
\textcopyright~[TODO: year] The Authors. This article is published under a
Creative Commons Attribution 4.0 International License (CC BY 4.0), which
permits use, distribution, and reproduction in any medium, provided the
original work is properly cited.

\section*{Use of AI Tools}
The core contributions of this paper---its research questions, measurement
design, analysis, and conclusions---are the work of the authors. Large language
models were the \emph{object of study}; in addition, [TODO: state any
assistive use, e.g. "AI tools were used to refine language and check code" or
"no generative AI tools were used in the preparation of this manuscript"].
No AI system is listed as an author, consistent with COPE guidance.

\section*{Conflict of Interest}
The authors declare no competing interests. % [TODO: confirm]

\section*{Funding}
[TODO: state funding sources, or "This research received no specific grant
from any funding agency."]

\section*{Data and Code Availability}
% JAIR's reproducibility mechanism is online appendices; a formal statement is
% not explicitly mandated (UNCONFIRMED) but recommended for this paper.
The generated stories, analysis notebook, CSV datasets, and the automated audit
checks are provided as online appendices accompanying this article.
[TODO: repository URL / DOI]
```

## 5. Template & citation conversion notes

**Template (jair class).**
1. Copy the JAIR Overleaf Author Kit (https://www.overleaf.com/read/hycbzkdksrzz → Menu → Copy Project), or download `jair.sty`, `theapa.sty`, `theapa.bst` from the Author Kit / CMU mirror (https://www.cs.cmu.edu/afs/cs/project/jair/pub/information/format/latex/jair.sty).
2. Replace the preamble line with `\documentclass[jair,11pt,letterpaper]{article}` and add `\usepackage{jair}` and `\usepackage{theapa}`. Remove the generic `article` 12pt/a4 options and any conflicting geometry/style packages the class already provides.
3. Body is single-column (high confidence; exact directive UNCONFIRMED) — let `jair.sty` control layout; do not force two-column.
4. Move every table's `\caption{}` to AFTER the `tabular` environment so the caption renders below; verify all in-artwork text is ≥9pt; ensure cross-references read "Figure N"/"Table N" (capitalized).
5. Relabel appendices to lettered form and place them after Acknowledgments; move bulky data/code to online appendices.

**Citation switch (natbib `apalike` → theapa).** Both styles are author-date, so this is mechanical:
- `\bibliographystyle{apalike}` → `\bibliographystyle{theapa}` (or `newtheapa` if you want DOI/URL rendering: https://github.com/eladden/JAIR_theapa_bst_with_doi_url).
- Drop `\usepackage{natbib}`; `theapa` provides the cite commands.
- Command map: `\citep{key}` → `\cite{key}` (parenthetical); `\citet{key}` → `\citeA{key}` (narrative, author in-sentence); `\citeyear{key}` stays `\citeyear{key}`; author-only → `\citeauthor{key}`. Force short/full forms with `\shortcite`/`\fullcite` if needed.
- `theapa` does automatic et-al. switching (first cite lists all authors, later cites collapse to "et al."), so remove any manual et-al. handling.
- Reference list stays alphabetical by surname (APA), which `theapa.bst` produces automatically.

Source for the command set and rendering: https://www.cs.cmu.edu/afs/cs/project/jair/pub/information/format/latex/theapa.txt

## 6. Apply checklist (anchors in `main_english.tex`)

| Snippet | Where (in a COPY of `main_english.tex`) |
|---|---|
| Preamble: `\documentclass[jair,11pt,letterpaper]` + `\usepackage{jair,theapa}` | Replace the existing `\documentclass`/package preamble (top of file, before line 90). |
| `\bibliographystyle{theapa}` + cite-command swaps | Replace `apalike`/natbib setup in preamble; apply `\citet`→`\citeA`, `\citep`→`\cite` throughout body. |
| **Rewritten abstract (§2)** | Replace lines ~97–104 (the `\textbf{ABSTRACT}` block and its two `\noindent` paragraphs) with the single `abstract` environment. Keep the Keywords line (~108). |
| **Measurement-framing section (§3a)** | Insert immediately before `\section{Methodology}`. |
| **Discussion and Implications (§3b)** | Insert immediately before `\section{Conclusion}`. |
| **Declarations (§4)** | Insert before `\bibliography{referencias}` (near end of file), after Acknowledgments. |
| Table captions below | At each `table`/`tabular` block: move `\caption{}` to after `tabular`. |
| Lettered appendices after Acknowledgments | Wrap appendix material in `\appendix`; place after the Acknowledgments section; move data/code to online appendices. |

## 7. Honest notes / open items

- **Adaptation effort: HIGH.** The surface edits (citation swap, abstract trim, table captions, template, declarations) are each Low-effort, but the dominant cost is the conceptual reframing and the recommended expansion toward JAIR's comprehensive length norm.
- **Single biggest reframing:** stop presenting the paper as an empirical *audit that measures a quantity of bias*, and present it as a **reproducible multi-model measurement/methodology for gender-association drift**, with the OLS recast as one calibrated instrument within the framework and "overcorrection" demoted from headline to demonstration. Lean explicitly on the Fairness & Bias in AI Special Track at submission.
- **Scope candor (genre mismatch):** JAIR has essentially **zero published precedent** for GPT/ChatGPT gender-bias product-audits; that genre lives in *AI & Society*, *Humanities and Social Sciences Communications*, *PNAS Nexus*, and arXiv. The topic is in scope via the Special Track, and the large reproducibility appendix (notebook, CSVs, 896 audit checks) aligns unusually well with JAIR's online-appendix culture — but the econometric, percentage-point method idiom is foreign to JAIR's AI-researcher reviewers. Absent the measurement reframing, the candid recommendation is that the paper's method/contribution type is largely out of scope, and another venue (or the current Public Choice target) may be a better home.
- **UNCONFIRMED guideline points:** exact abstract word limit; the no-citations-in-abstract rule for JAIR specifically; exact keyword count/format; figure resolution/DPI rules; hard page/word limit; whether formal COI/funding/data-availability statements are mandated (only CC BY notice + AI-use statement are CONFIRMED required); the precise `jair.sty` single-vs-two-column directive (single-column is high-confidence from published PDFs); author anonymization (single-blind track strongly implies it is not required).
