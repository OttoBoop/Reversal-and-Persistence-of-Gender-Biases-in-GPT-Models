# Adaptation package: Journal of Business Ethics (Springer)

> **At a glance.** The *Journal of Business Ethics* (Springer, journal 10551) is a management/business-ethics/moral-philosophy venue — not CS, HCI, or economics. It will accept an empirical LLM-bias audit (there is now direct precedent: Cao, Li, Xu & Zhu 2025, DOI 10.1007/s10551-025-06216-1), but only if the paper "explains the ethics" of the phenomenon and carries a genuine theory section plus a Discussion with **theoretical AND managerial implications**. Mechanics are easy (already author-date; abstract close to length); the substance is a re-genre-ing, not a reformat. The snippets below are ready to paste into a **copy** of `paper/latex/main_english.tex` — the canonical file is left untouched. **Adaptation-effort rating from the dossier: HIGH** (mechanical conversions trivial; new theory section, full Discussion + Implications, ethics re-framing, and method/voice re-register amount to a near-rewrite of the framing and roughly a third of the prose).

## 1. Conversion checklist (must-adopt, with where each is documented)

| Item | Status | Action | Source |
|---|---|---|---|
| **Template / format** | MUST ADOPT | Switch from generic `article` to `sn-jnl` (`sn-basic` or `sn-apa` option), OR submit Word .docx. Single-column, double-spaced, continuous line numbers for review. Editable source mandatory (no PDF-only). | dossier §2; https://link.springer.com/journal/10551/submission-guidelines ; https://www.overleaf.com/latex/templates/springer-nature-latex-template/myxmhdsbzkyd |
| **Citation style** | ALREADY SATISFIED (minor) | Already author-date. Switch `apalike` → `sn-basic`/`spbasic`; render in-text as `(Author, Year)` comma form; alphabetical; **add DOIs** to all journal refs. | dossier §2; https://citationsy.com/styles/springer-basic-author-date |
| **Abstract rules** | MUST ADOPT | Merge the 2-paragraph / 8-citation abstract into ONE unstructured paragraph, **≤250 words**, **NO in-text citations**. | dossier §2; submission-guidelines |
| **Structure** | MUST ADOPT (large) | Add **Theory/Hypothesis Development**, **Discussion**, and **Implications (theoretical + managerial)**, **Limitations**. Current paper has only Intro → Lit Review → Methodology → Results → Conclusion. | dossier §2, §4 |
| **Hypotheses** | SHOULD ADOPT | Numbered H1/H2/H3 are a strong convention for quantitative empirical work (not a hard rule). | dossier §2 (UNCONFIRMED as formal requirement) |
| **"Explain the ethics"** | MUST ADOPT | Foreground the moral argument; demote regression to evidence. Off-mission without it. | dossier §1, §5; https://link.springer.com/article/10.1007/s10551-024-05896-5 |
| **Figures/tables** | MUST ADOPT | Arabic numerals; **table titles above**; captions in the manuscript text file (not embedded in figure files); Springer artwork specs. **NO AI-generated images** (critical for an LLM paper — confirm all figures are plotted from data, not model-generated). | dossier §2; https://www.springer.com/gp/editorial-policies/artificial-intelligence--ai-/25428500 |
| **Keywords** | ALREADY SATISFIED | 5 keywords present; JBE wants **4–6**. OK; consider adding "business ethics" / "responsible AI". | dossier §2 |
| **Length** | MUST ADOPT | Target **8,000–10,000 words including references**; move the 20+-regression appendix to electronic **Supplementary Information**. | dossier §2, §4 |
| **Declarations** | MUST ADOPT | Add a **Declarations** block before references (Funding, Competing interests [3-yr window], Ethics approval, Consent, Data/Materials/**Code availability — required**, Author contributions). | dossier §2 |
| **LLM-use statement** | MUST ADOPT | Document LLM use in **Methods** (LLMs are the *object of study* here; also declare any LLM authoring assistance). LLM not an author. | Springer AI policy (above) |
| **Anonymization** | MUST ADOPT | Double-anonymous: separate title page (authors + **acknowledgements** there), self-cite in third person, anonymize data authorship. | dossier §2 |
| **Section choice** | MUST ADOPT | Self-identify as "Original Paper (empirical)" and pick one of 30+ Sections — best fit: **"Corporate Responsibility: Quantitative Issues."** | dossier §1; https://link.springer.com/journal/10551/updates/17211284 |

## 2. Rewritten abstract (ready to paste)

```latex
\noindent The rapid organizational adoption of large language models (LLMs) makes the
fairness of their outputs an ethical and managerial concern: when firms embed these systems
in hiring, marketing, and communication workflows, the models' implicit gender associations
become organizational conduct. We audit how gender bias has evolved across fourteen models
of the GPT family released since 2020, analyzing more than sixty-two thousand model-generated
workplace narratives produced under three prompt-based experiments that vary desirable worker
characteristics, the valence of supervisor feedback, and occupational power cues. Using a
linear-probability framework with robust standard errors, we document a sharp moral and
behavioral discontinuity. Early completion-type models (GPT-3) associate positively valued
characteristics with character gender in a near-neutral way, whereas alignment-trained
chat-type models (GPT-3.5 and later) swing strongly toward female characters, attaching
positive traits disproportionately to non-male characters by roughly sixty-one percentage
points. We interpret this pattern as ethical overcorrection: alignment interventions intended
to remove discrimination have replaced one directional bias with another rather than achieving
neutrality. At the same time, occupational stereotypes persist even in the newest models, with
receptionists rendered uniformly female and blue-collar roles overwhelmingly male. We argue
that both overcorrection and residual stereotyping are moral failures of fairness with concrete
managerial consequences for organizations that deploy these systems, and we develop the
theoretical and practical implications of governing LLM gender behavior as a matter of business
ethics rather than of engineering alone.
```

**Word count: 238 words** (within the ≤250 limit; no in-text citations).

## 3. New / restructured sections (ready-to-paste LaTeX skeletons)

> **All sections below are DRAFTS requiring advisor (Valdemar) validation** — the ethics framing, hypothesis wording, and managerial claims are first-pass scaffolding, not vetted argument.

### 3a. Theory & Hypothesis Development (insert after Introduction, before Methodology)

```latex
\section{Theory and Hypothesis Development}
\label{sec:theory}

% DRAFT -- requires advisor (Valdemar) validation.

\subsection{Algorithmic gender bias as a business-ethics problem}
When organizations embed large language models in hiring, marketing, performance
feedback, and customer-facing communication, the gender associations these models encode
cease to be technical artifacts and become organizational conduct with moral weight. We
frame LLM gender behavior as a fairness problem in the business-ethics tradition: a system
that systematically links valued workplace traits to one gender enacts distributive and
representational unfairness at the scale of every deployment \citep{obermeyer2019}. The
ethical question is therefore not merely whether a model is "accurate" but whether the
moral content of its outputs treats persons as equals.

\subsection{From bias to overcorrection}
Prior audits establish that early models reproduced human gender stereotypes learned from
training data \citep{lucy2021}. Alignment interventions were introduced to mitigate this
\citep{openai2023}. A distinct ethical risk follows: an intervention calibrated to remove
one directional bias may install the opposite one, substituting reverse discrimination for
neutrality rather than achieving it \citep{liu2025, mirza2024, wang2024, karvonen2025}.
We term this \emph{ethical overcorrection} and treat genuine fairness as an absence of
directional association in either direction, not as a swing of the sign.

\subsection{Persistence of occupational stereotypes}
Overcorrection on diffuse trait--gender associations may coexist with the persistence of
concrete occupational stereotypes, because the two are governed by different parts of the
training and alignment process \citep{joshi2024}. Residual occupation--gender coupling is
ethically salient precisely where LLMs are most likely to be deployed in HR and recruiting.

\subsection{Hypotheses}
% Numbered hypotheses are a strong JBE convention for quantitative work (optional).
\begin{description}
  \item[H1.] Completion-type GPT models exhibit a near-neutral association between
  positively valued workplace characteristics and character gender.
  \item[H2.] Alignment-trained chat-type models (GPT-3.5 and later) exhibit a significant
  association favoring non-male characters, consistent with ethical overcorrection rather
  than neutrality.
  \item[H3.] Stereotypical occupation--gender associations persist across model generations,
  including the most recent models, even where trait-level overcorrection is observed.
\end{description}
```

### 3b. Discussion + Implications + Limitations (insert after Results, before Conclusion)

```latex
\section{Discussion}
\label{sec:discussion}

% DRAFT -- requires advisor (Valdemar) validation.

Our results document a moral discontinuity in the GPT family: near-neutral completion models
give way to chat models that overcorrect strongly toward female characters (H1, H2), while
occupational stereotypes persist even in the newest models (H3). Read through a fairness lens,
neither state is ethically acceptable. Overcorrection is not the cure for bias; it is bias with
the sign reversed \citep{liu2025, mirza2024}. The co-existence of trait-level overcorrection
with occupation-level stereotyping \citep{joshi2024} shows that alignment has redistributed
unfairness rather than eliminated it -- a pattern with clear parallels to documented harms from
optimizing a proxy objective rather than the morally relevant target \citep{obermeyer2019}.

\section{Implications}
\label{sec:implications}

\subsection{Theoretical implications}
We contribute the construct of \emph{ethical overcorrection} to the business-ethics literature
on algorithmic fairness: a directional reversal that satisfies a naive non-discrimination test
while violating the underlying moral commitment to equal treatment. This reframes alignment as
a governance problem rather than a purely technical one and shows that fairness audits must test
for bias in \emph{both} directions and at multiple granularities (trait vs.\ occupation).

\subsection{Practical and managerial implications}
Organizations deploying LLMs in hiring, performance feedback, and marketing inherit both the
overcorrection and the residual occupational stereotypes documented here. Managers should (i)
audit vendor models for directional bias in both directions before deployment, (ii) treat
"de-biased" or aligned models as unverified rather than safe, (iii) monitor occupation-level
outputs in HR and recruiting workflows specifically, and (iv) document model provenance and
alignment version as part of responsible-AI governance. Procurement and compliance functions,
not only engineering teams, bear ethical responsibility for these outputs.

\section{Limitations and Future Research}
\label{sec:limitations}
Our audit measures model outputs, not downstream human or organizational decisions; linking
the documented biases to realized hiring or evaluation outcomes is left to future work, ideally
pairing the computational audit with a human-perception study. We study the GPT family in two
languages (English and Portuguese); generalization to other model families and languages is
open. The linear-probability specification is transparent but does not model higher-order
interactions exhaustively.
```

## 4. Declarations / required statements (ready to paste)

```latex
% Insert immediately BEFORE \bibliography{referencias} (currently line 1327).
% On the SEPARATE TITLE PAGE put authors + Acknowledgements; keep this block anonymized.

\section*{Declarations}

\textbf{Funding.} [TODO: state grant numbers / funders, or "The authors received no specific
funding for this work."]

\textbf{Competing interests.} The authors declare that they have no competing interests within
the last three years relevant to this work. [TODO: confirm/replace.]

\textbf{Ethics approval.} This study did not involve human participants or animals; it audits
publicly available language-model outputs. [TODO: confirm no IRB applies.]

\textbf{Consent to participate / Consent for publication.} Not applicable.

\textbf{Data, Materials and Code availability.} All generated stories, audit datasets, and
analysis code are openly available at [TODO: repository DOI / URL], including the reproduction
notebook and the [TODO: 896] audit checks. % REQUIRED by JBE.

\textbf{Authors' contributions.} [TODO: e.g., "O.B. designed the experiments, generated the
data, and performed the analysis; both authors interpreted results and wrote the manuscript."]

\textbf{Use of large language models.} The GPT-family models studied here are the object of the
audit and are not authors. [TODO: declare any use of LLMs in drafting/editing; per Springer
policy, LLMs cannot be authors and any such use must be documented in the Methods section. No
AI-generated images are included; all figures are plotted directly from the audit data.]
```

Also add to the **Methods** section a one-sentence LLM-use note (Springer requires LLM use documented there):

```latex
% Append to \section{Methodology}:
We document our use of large language models for transparency: the GPT-family models named in
Table~[TODO] are the systems under audit and the source of all generated text; [TODO: state any
LLM assistance used in preparing the manuscript itself]. No AI-generated images are used.
```

## 5. Template & citation conversion notes

**Template (sn-jnl).**
1. Download the Springer Nature template (Overleaf: https://www.overleaf.com/latex/templates/springer-nature-latex-template/myxmhdsbzkyd) or `sn-jnl.cls` (https://github.com/godkingjay/springer-nature-latex-template/blob/master/sn-jnl.cls).
2. Replace the preamble `\documentclass[12pt,a4paper]{article}` with `\documentclass[sn-basic]{sn-jnl}` (or `[sn-apa]` for the APA-rendered author-date look JBE typeset house style shows).
3. For the review version, enable single-column, double-spacing and line numbers (`\usepackage{lineno}\linenumbers`, or the class's review option). Two-column is proof-only.
4. Move `\maketitle` author/affiliation/acknowledgements to a **separate title-page file** not sent to reviewers; in the main file keep the title anonymized.
5. Move the appendix (currently `\appendix`-style content after Results / regressions) into an electronic **Supplementary Information** file; reference SI figures/tables with separate numbering.
6. Confirm every figure is data-plotted (matplotlib/etc.), never model-generated — Springer bars AI-generated images.

**Citation-style switch (natbib `apalike` → Springer Basic).**
- Change `\bibliographystyle{apalike}` (line 37) to `\bibliographystyle{sn-basic}` (ships with the template; falls back to `spbasic.bst`).
- `\citet{key}` → narrative `Author (Year)`; `\citep{key}` → parenthetical `(Author, Year)` **with comma**. natbib commands work under the SN class, so `\citet`/`\citep` can stay; the style file handles the comma rendering. Verify against a current issue if the comma form matters (dossier flags SPBASIC-default vs APA-comma as the one UNCONFIRMED citation point — published JBE evidence favors the comma).
- Reference list: alphabetical by first-author surname (already the case under author-date); **add `doi = {...}` fields** to all journal entries in `referencias.bib`. Springer expects DOIs for citation linking.
- Source: https://citationsy.com/styles/springer-basic-author-date ; dossier §2.

## 6. Apply checklist (anchors in main_english.tex)

Work in a **copy** of `/home/user/Reversal-and-Persistence-of-Gender-Biases-in-GPT-Models/paper/latex/main_english.tex`. Confirmed line anchors:

| Snippet | Where to insert |
|---|---|
| **Rewritten abstract** (§2) | Replace the two-paragraph abstract body at **lines ~102–104** (between `\noindent\textbf{ABSTRACT}` line 98 and the `\medskip` / Keywords at 106–108). Collapse to one paragraph. |
| **Keywords** | Keep at **line 108**; optionally add "business ethics" / "responsible AI" to reach the 4–6 range with an ethics signal. |
| **Theory & Hypothesis Development** (§3a) | Insert after the Introduction (ends ~line 148), **before `\section{Methodology}` (line 305)**. Optionally rename/merge `\section{Literature Review}` (line 149) into it. |
| **LLM-use note in Methods** (§4) | Append inside `\section{Methodology}` (starts line 305). |
| **Discussion + Implications + Limitations** (§3b) | Insert after `\section{Results}` content (Results starts line 871) and **before `\section{Conclusion}` (line 1289)**. |
| **Declarations block** (§4) | Insert **before `\bibliography{referencias}` (line 1327)**. |
| **Bibliography style** | Change `\bibliographystyle{apalike}` at **line 37** → `sn-basic`. |
| **Appendix → SI** | Extract regression appendix content (after line 1289 region / appendix) into a separate SI file. |

## 7. Honest notes / open items

- **Adaptation effort: HIGH.** Mechanics (template, citation comma, abstract trim, declarations) are Low; the substance — a real theory section, a full Discussion + Implications, an explicit ethics contribution, and a voice shift from economist-audit to management-ethics — is the bulk of the work and rewrites roughly a third of the prose. This is a re-genre-ing, not a reformat.
- **The single biggest reframing:** stop presenting gender bias as an econometric **outcome variable** and present it as a **business-ethics problem**. The β₁ = −0.61 (−61pp) overcorrection finding must become evidence inside a moral + managerial argument ("explain the ethics"), not the contribution itself. Without this the paper is desk-reject territory regardless of empirical quality.
- **Scope candor:** the *topic* (algorithmic gender bias / responsible AI in business) is squarely in scope, and there is now direct precedent (Cao et al. 2025, 10.1007/s10551-025-06216-1). But the *method register* — an LLM output audit with OLS linear-probability models — is atypical for JBE, where quantitative AI-ethics papers are usually behavioral experiments on humans (vignettes/MTurk + mediation). Strongest path to in-register: pair the audit with a human-perception or normative layer. The current *Public Choice* target remains a far more natural home for the econometric form.
- **UNCONFIRMED guideline points** (from dossier; all Springer pages returned 403 to direct fetch, assembled via search): exact in-text comma convention (SPBASIC default omits the comma; published JBE evidence favors the comma form — verify against a current issue); formal-requirement status of numbered hypotheses (treat as strong convention, optional); per-Section structured-abstract mandates; exact JBE no-citations-in-abstract wording (uniformly observed in practice); SI size limits; positionality/reflexivity (treated as not required).
- All nine citation keys used in the skeletons (`lucy2021`, `liu2025`, `wang2024`, `mirza2024`, `karvonen2025`, `joshi2024`, `obermeyer2019`, `openai2023`, plus `abid2021`) were verified present in `paper/latex/referencias.bib`.
