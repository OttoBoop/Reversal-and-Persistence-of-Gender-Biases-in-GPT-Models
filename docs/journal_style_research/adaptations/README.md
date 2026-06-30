# Manuscript adaptation packages

Ready-to-paste packages for converting *"Reversal and Persistence of Gender Biases in GPT
Models"* to the house style of **each** candidate journal. One package per journal — the
same treatment for all four, not just the top pick.

> **The canonical paper is not modified.** These are drop-in packages: each contains a
> journal-compliant rewritten abstract, ready-to-paste LaTeX for the new sections the journal
> expects (theory/framing, Discussion + Implications, declarations), template + citation
> conversion notes, and an apply-checklist mapping each snippet to an anchor in a *copy* of
> `paper/latex/main_english.tex`. Apply them to a copy, not to the canonical file.

| Package | Journal | Adaptation effort |
|---|---|---|
| [`ai_society.md`](ai_society.md) | AI & Society (Springer) | **Medium** |
| [`journal_of_business_ethics.md`](journal_of_business_ethics.md) | Journal of Business Ethics (Springer) | **High** |
| [`pacmhci.md`](pacmhci.md) | Proceedings of the ACM on HCI (PACMHCI) | **High** |
| [`jair.md`](jair.md) | Journal of Artificial Intelligence Research (JAIR) | **High** |

Each package has the same seven sections: (1) conversion checklist, (2) rewritten abstract,
(3) new/restructured sections (LaTeX), (4) declarations, (5) template & citation conversion,
(6) apply checklist with `main_english.tex` anchors, (7) honest notes / open items.

## How to use

1. `cp paper/latex/main_english.tex paper/latex/main_<journal>.tex` (work on a copy).
2. Apply the package's section 2 (abstract), section 3 (new sections), and section 4
   (declarations) at the anchors listed in section 6.
3. Follow section 5 for the template/citation switch (Overleaf is easiest for `sn-jnl`,
   `acmart`, or the JAIR class).
4. Compile locally and resolve citations (no LaTeX toolchain was available in the
   environment that generated these packages, so nothing here has been compiled).

> ⚠️ The new theory/framing and Discussion sections are **DRAFTS** flagged for co-author/
> advisor (Valdemar) validation, per the project's cooperative-process rule — read and revise
> before submission. `[TODO]` markers in the declarations are author-specific values to fill.

## Rationale

Why each journal (precedent papers + norms with links) and the overall ranking are in the
sibling files: the per-journal dossiers [`01`–`04`](..), the matrix
[`05_comparison_matrix_and_recommendation.md`](../05_comparison_matrix_and_recommendation.md),
and the referenced decision guide
[`06_why_choose_each_journal.md`](../06_why_choose_each_journal.md). Recommended target:
**AI & Society** (best topical fit, lowest adaptation cost).
