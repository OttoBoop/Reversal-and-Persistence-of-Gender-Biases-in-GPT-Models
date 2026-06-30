# Adaptation package: Proceedings of the ACM on Human-Computer Interaction (PACMHCI)

> PACMHCI (the CSCW track is its center of gravity) is an ACM house-style journal that publishes human-centered social-computing scholarship, not free-standing computational audits. At a glance it demands: the `acmart` class (`\documentclass[acmsmall]{acmart}`, single column; double-anonymous `[acmsmall,anonymous,review]{acmart}` for review), **numeric `[n]` ACM-Reference-Format citations** with an alphabetical-then-numbered list and DOIs (the *reverse* of your current author-date setup), a single unstructured citation-free abstract (~150-250 words), mandatory CCS Concepts + `\keywords{}`, a `\Description{}` alt-text on every figure, booktabs tables, an effectively-mandatory CSCW-theory Related Work section, and a Discussion + Implications section. The single biggest demand is a re-genre-ing: shift the unit of analysis from the model's coefficients to the humans and social systems the bias affects. The snippets below are ready to paste into a **copy** of `paper/latex/main_english.tex` — the canonical file is not modified. **Adaptation-effort rating from the dossier: HIGH** (re-genre-ing, not a reformat; real risk of scope rejection — pure audits cluster at FAccT/EAAMO/AIES, not PACMHCI).

## 1. Conversion checklist (must-adopt, with where each is documented)

| Item | Status | What to do | Source |
|---|---|---|---|
| **Template / class** | MUST ADOPT | Replace generic `article` with `\documentclass[acmsmall]{acmart}` (single column). Use the interim ACM Small template from the PACMHCI submission-templates page. | dossier §2 "Manuscript template"; https://dl.acm.org/journal/pacmhci/submission-templates |
| **Anonymization** | MUST ADOPT (for review) | Use `\documentclass[acmsmall,anonymous,review]{acmart}`; strip names, affiliations, cities, grant IDs, metadata, acknowledgements. Desk-reject if violated. | dossier §2 "double-anonymous"; https://dl.acm.org/journal/pacmhci |
| **Citation style** | MUST ADOPT | Switch author-date (natbib/apalike `\citet`/`\citep`) → ACM numeric `[n]` via `\citestyle{acmnumeric}` + `ACM-Reference-Format.bst`; list alphabetical-then-numbered; **DOIs required**. | dossier §2 "Citation style"; https://www.acm.org/publications/authors/reference-formatting |
| **Abstract** | MUST ADOPT (light) | Merge your 2-paragraph, 8-citation, ~229-word abstract into ONE unstructured paragraph, **zero in-text citations**, ~150-250 words. | dossier §2 "Abstract rules" |
| **Structure** | MUST ADOPT | Add a CSCW-theory Related Work section and a Discussion + Implications section (currently absent); consider thematic Findings ("overcorrection" / "persistent occupational stereotypes") over Test 1/2/3. No hypotheses (already satisfied). | dossier §2 "Structure"; §4 table |
| **Hypotheses** | ALREADY SATISFIED | Paper has no H1/H2; matches venue norm. | dossier §2; §4 table |
| **Figure captions below / table captions above** | ALREADY SATISFIED | Your paper already does this (ACM convention). | dossier §2 "Figures and tables" |
| **Figure alt-text** | MUST ADOPT | Add `\Description{...}` to every one of the 10 figures (enforced). | dossier §2 "Accessibility" |
| **Tables** | MUST ADOPT (light) | Use `booktabs` rules, no vertical rules. | dossier §2 "Tables" |
| **CCS Concepts** | MUST ADOPT | Add CCSXML block + `\ccsdesc{}` (mandatory >2 pages) via the ACM CCS tool. | dossier §2 "Keywords" |
| **Author keywords** | ALREADY SATISFIED (reformat) | You have 5 keywords; move into `\keywords{...}` (comma-separated). | dossier §2 "Keywords" |
| **Length** | ALREADY SATISFIED | No cap; ~5,500 words + appendix is fine. 12k words is only a scrutiny threshold. | dossier §2 "Length norms" |
| **Generative-AI disclosure** | MUST ADOPT (if applicable) | If GenAI used to create content, disclose in Acknowledgements; AI cannot be an author. Note: your GPT models are the *object of study* — distinguish that from authoring use. | dossier §2 "Declarations"; https://respect.acm.org/2026 |
| **Ethics / generated-data handling** | MUST ADOPT (statement) | Address research-ethics handling of the generation pipeline (no human subjects, but state it). | dossier §2 "Ethics" |
| **Data/artifact sharing** | ALREADY SATISFIED (surface it) | Your notebook/CSVs/896-check audit are a strength; add a data-availability statement (encouraged). | dossier §2 "Data availability" |

## 2. Rewritten abstract (ready to paste)

```latex
\begin{abstract}
The rapid uptake of large language models (LLMs) in everyday and
workplace settings means that the social biases these systems encode are
increasingly mediated into the lives of the people and organizations that
rely on them. We examine how gender bias in the GPT family of models has
evolved across three generations released since 2020, and what that
evolution implies for the human and social systems now entangled with
these tools. Using a prompt-based generation paradigm, we elicited more
than sixty-two thousand short workplace narratives from over a dozen GPT
models and analyzed the gender of the characters the models produced
under three conditions: the presence or absence of desirable workplace
characteristics, the valence of supervisor feedback, and occupational
cues tied to differing levels of social power. We find a marked
generational shift: early completion-style models associate gender with
valued characteristics in a near-neutral way, whereas aligned chat-style
models (from GPT-3.5 onward) swing strongly toward associating positive
characteristics with non-male characters---an overcorrection rather than
a removal of bias. At the same time, stereotypical associations between
gender and occupation persist even in the newest models. We interpret
this reversal-and-persistence pattern as a sociotechnical phenomenon,
discuss what it means for the people subject to these systems, and draw
out implications for design, governance, and accountability in
collaborative AI use.
\end{abstract}
```

**Word count: 213 words** (single paragraph, no in-text citations — compliant with the ~150-250-word PACMHCI norm).

## 3. New / restructured sections (ready-to-paste LaTeX skeletons)

> All prose below is a **DRAFT requiring advisor (Valdemar) validation** — especially the CSCW-theory claims and the framing that recasts the econometric finding as a sociotechnical one. Citation keys used are confirmed to exist in `referencias.bib`.

### 3a. CSCW-theory Related Work / framing section (paper currently has none)

```latex
\section{Related Work and Conceptual Framing}
\label{sec:related}
% DRAFT — requires advisor (Valdemar) validation, esp. CSCW grounding.

\subsection{Algorithmic bias as a social, not merely technical, phenomenon}
Bias in computational systems is not solely a property of a model; it is
realized in the social systems that deploy and depend on those systems.
Documented harms---from a healthcare risk algorithm that systematically
underestimated the needs of Black patients~\cite{obermeyer2019} to
gender and identity bias in generative models~\cite{lucy2021}---show that
the consequential unit of analysis is the affected person or community,
not the coefficient. We adopt this human-centered stance: we treat
GPT-generated gendered associations as a sociotechnical signal about how
millions of downstream interactions may be shaped, rather than as an
isolated model property.

\subsection{Value alignment, overcorrection, and the limits of mitigation}
Efforts to align LLMs to human values---documented in artifacts such as
the GPT-4 System Card~\cite{openai2023}---can move a model away from one
biased equilibrium without landing it at neutrality. Prior work suggests
mitigation can overshoot~\cite{liu2025} without fully reversing bias
across domains~\cite{joshi2024}, a tension corroborated across recent
audits~\cite{mirza2024,wang2024,karvonen2025}. We frame this
\emph{reversal-and-persistence} dynamic as a core sociotechnical concern
for CSCW: alignment is a continuous, contested negotiation between
designers, institutions, and affected publics, not a solved state.

\subsection{Why this matters for cooperative and social computing}
As LLMs become collaborators in hiring, writing, evaluation, and
everyday organizational work, their gendered output distributions become
inputs to human cooperative processes. A model that disproportionately
casts non-male characters as competent, while still binding occupations
to gender stereotypes, embeds contradictory signals into the shared
sociotechnical fabric. This motivates our research questions and our
attention, in the Discussion, to implications for design and governance.
```

### 3b. Discussion + Implications section (paper currently has none)

```latex
\section{Discussion}
\label{sec:discussion}
% DRAFT — requires advisor (Valdemar) validation.

\subsection{Reversal and persistence as a sociotechnical pattern}
Our central finding---a pro-female swing in aligned chat models alongside
persistent occupational stereotypes---is best read not as "bias fixed" or
"bias broken" but as a relocation of bias. Alignment moved the models'
character-competence associations past neutrality (an overcorrection
consistent with~\cite{liu2025}) while leaving gender-occupation
associations largely intact (consistent with the incomplete reversal
of~\cite{joshi2024}). For the people and institutions that delegate
narrative, evaluative, or screening work to these systems, this means
neither the older nor the newer regime is neutral.

\section{Implications}
\label{sec:implications}

\subsection{Implications for design}
Designers cannot treat de-biasing as a one-dimensional dial. Mitigation
that targets one axis (competence-by-gender) can overshoot while another
axis (occupation-by-gender) is untouched. We argue for
\emph{multi-axis, auditable} mitigation with visible reporting of
residual and inverted disparities, so that downstream users can reason
about the directionality of bias rather than assuming its absence.

\subsection{Implications for CSCW and collaborative use}
When an LLM is a partner in shared work, its output distribution becomes
a structuring resource for the group. We recommend that collaborative
tooling surface provenance and directionality of model bias at the point
of use, enabling teams to contest and correct rather than silently
inherit the model's gendered defaults.

\subsection{Implications for policy and accountability}
Audit regimes should test for \emph{over}correction and persistence, not
only for under-mitigation; "less stereotyping than GPT-3" is not a
sufficient standard. Our reproducible pipeline (notebook, generated
corpora, and automated checks) is offered as a template for the kind of
standing, multi-axis accountability such governance requires.

\section{Limitations}
\label{sec:limitations}
% DRAFT
Our evidence is the models' generated text, not the lived experience of
affected users; we characterize a sociotechnical signal, not its
downstream reception. A complementary qualitative layer---an interpretive
reading of the generated stories, or a study of how practitioners
perceive these biases---would strengthen the human-centered claim and is
a clear direction for future work. We also study English and Portuguese
only, and the OpenAI GPT family only.
```

> **Suggested move for native fit (dossier §5.5):** consider adding a qualitative/interpretive strand (a close reading of a sampled subset of the 62k stories, or a small practitioner-perception study) so the paper reads as native mixed-methods rather than a pure quantitative audit. This is the highest-leverage change for acceptance and should be discussed with Valdemar.

## 4. Declarations / required statements (ready to paste)

```latex
% --- Place in Acknowledgements (REMOVE for anonymized review build) ---
\begin{acks}
% [TODO: funding] This work was supported by [TODO: grant/agency].
% Generative-AI disclosure (ACM policy): the GPT-family models studied
% here are the OBJECT of analysis, not authoring tools. [TODO: confirm]
% No generative-AI tool was used to create or write the content of this
% manuscript beyond [TODO: e.g. none / editorial grammar checking only,
% which is exempt from disclosure]. Generative AI is not an author of
% this work.
\end{acks}

% --- Ethics statement ---
\section*{Research Ethics}
This study analyzes text generated by large language models and does not
involve human participants; no IRB/ethics-board approval was required.
% [TODO: confirm institutional position]

% --- Data / artifact availability (encouraged) ---
\section*{Data Availability}
The generated story corpora, analysis notebook, and the automated audit
checks supporting this study are available at [TODO: repository / DOI].
% [TODO: deposit and mint an archival DOI; DOIs are required for cited
% archived datasets under ACM Reference Format.]

% --- Conflict of interest (declared via submission system) ---
% [TODO: declare any COI in the submission form; not an in-text section.]
```

## 5. Template & citation conversion notes

**Template (generic `article` → `acmart`):**
1. Replace your preamble's `\documentclass[...]{article}` with `\documentclass[acmsmall]{acmart}` (camera-ready) or `\documentclass[acmsmall,anonymous,review]{acmart}` (review). Source: https://dl.acm.org/journal/pacmhci/submission-templates
2. Download the **interim ACM Small template** from the PACMHCI submission-templates page (not the generic CTAN `acmart`), per the CSCW CfP nuance in the dossier.
3. Add the journal metadata block before `\begin{document}`: `\acmJournal{PACMHCI}`, `\setcopyright{...}`, `\acmDOI{...}`, `\acmArticle{...}`, `\acmYear{...}`.
4. Add a CCSXML block + `\ccsdesc[300]{...}` generated from the ACM CCS tool (https://dl.acm.org/ccs), and `\keywords{Bias in artificial intelligence, gender bias, large language models, natural language processing, algorithmic fairness}`.
5. Add `\Description{...}` inside every `figure` environment (10 figures). Convert tables to `booktabs` (`\toprule/\midrule/\bottomrule`, no `|` rules).
6. `\maketitle` stays; remove `\tableofcontents`/`\newpage` scaffolding (acmart journals don't carry a TOC).

**Citation switch (author-date → numeric `[n]`):**
1. Remove `natbib`/`apalike` setup. acmart loads its own citation machinery — add `\citestyle{acmnumeric}` after `\documentclass`. Source: https://github.com/borisveytsman/acmart
2. Bibliography backend: `\bibliographystyle{ACM-Reference-Format}` + `\bibliography{referencias}` (or biblatex `acmnumeric`). Source: https://www.acm.org/publications/authors/reference-formatting
3. Replace every `\citet{key}` with `\citet{key}` is no longer needed — under acmnumeric use `\cite{key}` (renders `[n]`); for an author-as-subject sentence ("Lucy and Bamman show...") write the author names in prose and append `\cite{lucy2021}`. The in-text marker becomes `[n]`; multiple: `\cite{a,b}` → `[1, 2]`.
4. The reference list will auto-render **alphabetical by lead-author surname, then numbered** — so `[7]` is the 7th *alphabetized* entry, not citation order. No manual ordering needed.
5. **Add DOIs** to all `referencias.bib` entries that have them (`doi = {...}`); acmart renders them as `https://doi.org/...`. This is required, not optional.

## 6. Apply checklist (anchors in a copy of `main_english.tex`)

| Snippet | Where to insert |
|---|---|
| `\documentclass`, `\citestyle{acmnumeric}`, journal metadata, CCSXML, `\keywords{}` | Preamble (replace current `\documentclass` line; current preamble ends near `\date{2025}` / `\begin{document}` at lines ~90-92) |
| **Rewritten abstract** (§2) | Replace lines **~98-108** (the `\noindent\textbf{ABSTRACT}` block + the two `\noindent` paragraphs + the `Keywords:` line). Wrap in `\begin{abstract}...\end{abstract}`; move keywords to `\keywords{}` in the preamble. |
| Remove `\newpage \tableofcontents \newpage` | Lines **~110-112** |
| **Related Work / framing** (§3a) | Insert as a new `\section` **after `\section{Introduction}`** (starts line ~114) and **before `\section{Methodology}`** |
| `\Description{}` on each figure; booktabs on each table | At each `figure`/`table` environment throughout the body |
| **Discussion + Implications + Limitations** (§3b) | Insert **before `\section{Conclusion}`** |
| **Declarations** (§4: `\begin{acks}`, Research Ethics, Data Availability) | After Conclusion, **before `\bibliography{referencias}`** (acks before bibliography; remove acks for anonymized build) |
| `\bibliographystyle{ACM-Reference-Format}` | At the `\bibliography{referencias}` line |

## 7. Honest notes / open items

- **Adaptation effort: HIGH** (per dossier §5). The template and citation switches are mechanical (Medium alone), but the substantive work — adding a CSCW-theory section, adding Discussion/Implications, demoting the econometrics to a clean strand (move the 20+ appendix regressions to supplementary material), and ideally adding a qualitative layer — amounts to rewriting the paper's argument for a different epistemic community.
- **Single biggest reframing:** shift the unit of analysis from *the model and its coefficients* (β₁ = −0.61 → −61pp) to *the humans and social systems affected by the bias*, grounded in CSCW theory, with explicit design/governance implications. Keep the econometrics as evidence, not as the headline.
- **Scope candor (genre mismatch):** PACMHCI is a **poor as-is fit**. Pure prompt-and-measure GPT bias audits — exactly this paper's genre — systematically publish at **FAccT, EAAMO, AIES, ACM Multimedia, and CHI**, not PACMHCI, and the CSCW track applies an explicit "social aspects of technology mediation" scope test that can trigger desk-level scope rejection. If the qualitative reframing is not feasible, **FAccT/AIES/EAAMO are far better-matched homes** for this method and framing.
- **UNCONFIRMED guideline points (verify on live pages before submission):** the exact abstract word maximum (the 150-250 figure is a strong norm corroborated by exemplars, but the cited 150-250 limit formally applies to the CSCW Doctoral Consortium abstract); the "no citations in abstract" rule (near-universal convention, not located as a verbatim PACMHCI rule); exact required counts for CCS concepts / author keywords; whether a Data Availability Statement is mandatory vs encouraged; the exact interim ACM Small template file (download from the PACMHCI submission-templates page). The dossier also flags that dl.acm.org/acm.org/cscw.acm.org were proxy-blocked during research, so a live re-check is advised.
