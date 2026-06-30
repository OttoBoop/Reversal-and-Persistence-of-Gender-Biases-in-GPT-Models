# AI & Society variant — adaptation notes

`main_aisociety.tex` is an **AI & Society**-targeted version of the paper, derived from
`main_english.tex`. **The canonical Public Choice version (`main_english.tex`) is untouched.**
Rationale and evidence for targeting AI & Society are in
[`../../docs/journal_style_research/06_why_choose_each_journal.md`](../../docs/journal_style_research/06_why_choose_each_journal.md)
and [`01_ai_and_society.md`](../../docs/journal_style_research/01_ai_and_society.md).

## Applied in this variant (done)

- **Abstract** → single unstructured paragraph, **no in-text citations**, **236 words**
  (AI & Society allows 150–250, up to 450). The original two-paragraph, 8-citation abstract
  is preserved in `main_english.tex`.
- **New `\section{Theoretical Framing: Alignment, Overcorrection, and Gendered Language}`**
  (after the Literature Review) — gives the theory/values grounding the journal expects and
  frames the regressions as evidence in a values-first argument. Uses citation keys already
  in `referencias.bib`.
- **New `\section{Discussion and Implications}`** (before the Conclusion) — interpretation,
  societal implications, design/governance implications, limitations/future work. The
  Public Choice version jumps Results → Conclusion.
- **`\section*{Statements and Declarations}`** (before the bibliography) — competing
  interests, funding, author contributions, data/code availability, AI-use, ethics.

> ⚠️ The two new sections are **DRAFTS marked for co-author/advisor (Valdemar) validation**,
> per the project's cooperative-process rule (substance is validated by the advisor). Read
> and revise them before submission — they are a scaffold, not final scholarly prose.

## Still TODO before submission

- **Validate the new sections** (Theory, Discussion) with the advisor; refine wording/claims.
- **Complete the `[TODO]` placeholders** in the Statements and Declarations block.
- **Citation restyle**: `apalike` → Springer "Basic" author-date `(Author Year)` (no comma;
  initials no periods; `Volume:pages`; DOIs as URLs). Easiest via the Springer Nature LaTeX
  template (`sn-jnl.cls`, `sn-basic`) on Overleaf.
- **Template**: move to `sn-jnl.cls` for production (currently generic `article`).
- **Double-blind anonymization** (hard gate): strip author names/affiliations/identifying
  info from the manuscript and all files; provide a separate Title Page. Anonymize the
  reproducibility repo/notebook references for review.
- **Length / supplementary material**: move the densest of the 20+ appendix regressions into
  anonymized Supplementary Information; main text has headroom toward ~10,000 words.
- **Compile check**: no LaTeX toolchain was available in the environment that produced this
  variant, so it has **not been compiled**. Build locally (`pdflatex`/`latexmk` + `bibtex`)
  and confirm the two new sections render and all citations resolve before submitting.
- Optional but recommended: **co-bill a named contribution** (the prompt-based audit
  pipeline / 896-check reproducibility protocol as a reusable framework), as the closest
  AI & Society analogue (Sivakaminathan & Musi 2026) does.
