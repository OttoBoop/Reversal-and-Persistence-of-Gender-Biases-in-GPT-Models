# Baseline — Your Paper's Current Style

This document is the **reference baseline**. Every journal dossier in this folder
(`01`–`04`) and the synthesis (`05`) measures the four target journals *against this
profile*. It was distilled from the paper's LaTeX source, appendix, data/analysis
layout, and the project's planning notes.

**Paper:** *Reversal and Persistence of Gender Biases in GPT Models*
**Authors:** Otávio Oliveira Bopp, Valdemar Pinho Neto (advisor & co-author)
**Current target & template:** **Public Choice** (Springer), styled after
**Motoki et al. (2024), "More human than human", Public Choice 198:3–23** — the
deliberately conservative *"arroz com feijão"* template (when in doubt, choose the
conventional option).

---

## Disciplinary flavor

- **Applied labor economics** (the Bertrand–Mullainathan résumé-audit tradition) fused
  with **algorithmic fairness**; a **secondary** NLP/ML framing.
- An **economist's voice** — *not* computer science, *not* humanities/social theory.
- Gender bias is operationalized as an **outcome variable estimated by regression**, not
  as a fairness metric to be optimized nor as a socially-constructed theoretical object.

## Template & format

- Generic LaTeX `\documentclass[12pt,a4paper]{article}` — **no journal template**.
- `natbib` + `apalike`; **author-date Chicago/APA** in-text citations (`\citet`/`\citep`).
- **No numeric citations.** ~80–100 references in `referencias.bib`.
- Figure captions **below** figures; table captions **above** tables.

## Abstract

- ~240 words, **two paragraphs**, narrative + quantitative.
- **No structured headings**, **no formal hypotheses**.

## Section structure

`Introduction → Literature Review (4 subsec) → Methodology (8 subsec) → Results
(by Test 1 / Test 2 / Test 3) → Conclusion.`

- Methodology is long and detailed, with **econometric specifications shown in-text** as
  equations.
- **No separate Discussion section**, **no numbered hypotheses (H1/H2)**, **no dedicated
  theory-building section**.

## Empirical weight (~80% empirical)

- 62,000+ generated stories; 14+ GPT models (GPT-3 legacy → GPT-5 / o-series); three
  prompt-based experiments.
- **OLS linear-probability model** with robust (heteroskedasticity-consistent) standard
  errors, p-values, R². Coefficients read as **percentage points** (e.g. β₁ = −0.61 →
  −61 pp on P(male character)).
- 4 main + 2 detailed regression tables; 10 bar/distribution figures; a large appendix
  (20+ regressions, 5 profession cross-tabs).
- **Key finding — "overcorrection":** newer aligned chat models (GPT-3.5+) swing to a
  pro-female association (β ≈ −0.61) while older completion GPT-3 models were near-neutral
  (β ≈ −0.03); occupational stereotypes persist (all receptionists female, 98 % blue-collar
  male).

## Tone & apparatus

- Formal, first-person plural ("we/our"), hedged, policy-aware, conservative.
- **Reproducibility-heavy**: Jupyter notebook, canonical CSVs, 896 numeric audit checks.

## Keywords (5)

Bias in artificial intelligence · gender bias · Large Language Models · natural language
processing · algorithmic fairness.

## Length

~15 pages main text + an extensive appendix.

---

### Why this baseline matters for the comparison

The paper is, stylistically, an **empirical-econometrics economics article**. The four
journals it is being compared against sit at very different points: an interdisciplinary
AI-and-society venue (AI & Society), a technical CS/AI venue (JAIR), an HCI venue with
strong qualitative/mixed-methods norms (PACMHCI), and a management/ethics venue that
expects theory and hypotheses (Journal of Business Ethics). The dossiers therefore focus
on the gap between *"empirical economics paper"* and each journal's house expectations.
