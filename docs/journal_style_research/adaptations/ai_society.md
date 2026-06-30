# Adaptation package: AI & Society (Springer)

> **At a glance.** *AI & SOCIETY: Knowledge, Culture and Communication* (Springer Nature, journal 146) is a strongly interdisciplinary, **double-blind**, values-first venue where LLM gender-bias work is squarely in scope but must be framed as a **sociotechnical / ethical phenomenon**, not an econometric leaderboard. The mechanical conversions are light (you already use author-date; caption placement already matches; 5 keywords already complies; you have length headroom toward ~10,000 words). The substantive lift is rhetorical: add an explicit **theory/framing** section, add a **Discussion + Implications** section, translate the econometrics for a non-economist reader, co-bill a **named audit framework**, fully **anonymize**, and supply the **Statements and Declarations** block (missing block => returned as incomplete). All snippets below are ready to paste into a *copy* of `paper/latex/main_english.tex` — the canonical file is **not** modified. **Adaptation-effort rating from the dossier: MEDIUM.**

---

## 1. Conversion checklist (must-adopt, with where each is documented)

| Item | Status | What it requires | Source |
|---|---|---|---|
| **Template** | **MUST ADOPT** | Switch generic `article` to Springer Nature `sn-jnl.cls` (sn-basic option); single-column, double-spaced review copy; decimal headings, **≤3 levels, never skip a level**. | Dossier §2 (template); https://www.overleaf.com/latex/templates/springer-nature-latex-template/myxmhdsbzkyd ; https://www.springernature.com/gp/authors/publish-a-book/manuscript-guidelines |
| **Anonymization (double-blind)** | **MUST ADOPT (hard gate)** | Strip author names, affiliations, acknowledgements, funding, and identifying info from manuscript + figures + supplementary; submit a **separate Title Page**. | Dossier §2 (hard requirement); https://link.springer.com/journal/146/submission-guidelines |
| **Citation style** | **MUST ADOPT (light restyle)** | Springer **"Basic" author-date**: `(Author Year)` **no comma**; initials **no periods**; `Volume:pages` colon; DOI as full `https://doi.org/...` URL; refs alphabetical. You already use natbib author-date → swap the bib style. | Dossier §2 (citation style); https://citationsy.com/styles/ai-and-society ; https://github.com/citation-style-language/styles/blob/master/springer-basic-author-date.csl |
| **Abstract** | **MUST ADOPT** | **Single unstructured paragraph**, 150–250 words (up to 450 allowed), **NO in-text citations**, no undefined abbreviations. Current abstract is 2 paragraphs with 8 citations. | Dossier §2 (abstract rules); https://link.springer.com/journal/146/submission-guidelines |
| **Structure** | **MUST ADOPT** | No IMRaD mandate, but **add a theory/framing section** and a **Discussion + Implications** section (current paper jumps Results → Conclusion). No formal hypotheses expected. | Dossier §2 (structure), §5 (changes 1–2) |
| **Figures / tables** | **ALREADY SATISFIED** | Figure captions **below**, table titles **above** — already your convention. (For review, strip identifying info from figure files.) | Dossier §2 (figures/tables); §4 table row |
| **Keywords** | **ALREADY SATISFIED** | 4–6 keywords required; you have 5. | Dossier §2 (keyword count) |
| **Length** | **ALREADY SATISFIED (room to grow)** | Research articles ~10,000 words / ~20 pp; current ~5,500 words leaves headroom for the new sections. | Dossier §2 (length norms), §5 (change 7) |
| **Declarations** | **MUST ADOPT (hard gate)** | Add **"Statements and Declarations"**: Competing Interests, Author Contributions, Funding, Data Availability, plus **AI-use documented in Methods**. Missing block ⇒ returned as incomplete. | Dossier §2 (required statements); https://link.springer.com/journal/146/submission-guidelines |
| **Named-framework co-billing** | **MUST ADOPT (recommended)** | Elevate the prompt-based audit pipeline / 896-check protocol to a named, reusable framework (cf. Exemplar 1). | Dossier §5 (change 4), §4 contribution row |

---

## 2. Rewritten abstract (ready to paste)

```latex
% --- AI & SOCIETY abstract: single unstructured paragraph, no in-text citations ---
\begin{abstract}
The rapid adoption of Large Language Models (LLMs) has intensified concerns
that these systems do not merely reflect but actively reshape gendered
expectations about work, competence, and worth. A common narrative holds that
newer, ``aligned'' chat models are progressively debiased relative to their
predecessors. We interrogate that narrative empirically. Treating gender bias
as a sociotechnical phenomenon rather than a purely technical defect, we audit
more than fourteen models of the GPT family released since 2022, generating
over sixty-two thousand short workplace narratives across three prompt-based
experiments and two languages (English and Portuguese). Each experiment varies
a single cue---the presence of an employer-valued characteristic, the valence
of supervisor feedback, or an occupation---and records the gender of the
character the model invents. We find that alignment does not simply reduce
bias: completion-style GPT-3 models are close to gender-neutral, whereas
chat-style models from GPT-3.5 onward swing strongly toward associating
positive characteristics with non-male characters, an effect on the order of
sixty-one percentage points. This pattern, which we term ``overcorrection,''
coexists with stubbornly persistent occupational stereotypes: receptionists
are rendered almost uniformly female and blue-collar roles almost uniformly
male, even in the most recent models. Bias is therefore not being removed but
redistributed---reversed along some axes while entrenched along others. We
contribute both this finding and a reusable, fully reproducible audit pipeline
for surfacing such redistribution, and we draw out its implications for the
ethics, governance, and design of generative AI.
\end{abstract}
```

**Word count: 233 words** (abstract body, within the 150–250 target; no in-text citations).

---

## 3. New / restructured sections (ready-to-paste LaTeX skeletons)

> **DRAFTS — require advisor (Valdemar Pinho Neto) validation before submission.** Citation keys used below all exist in `referencias.bib`.

### 3a. Theory / framing section (insert before Methodology)

```latex
% ===== DRAFT — advisor (Valdemar) validation required =====
\section{Gender bias as a sociotechnical phenomenon}
\label{sec:framing}

\subsection{From a technical defect to a values-laden artifact}
Algorithmic gender bias is not a malfunction to be patched but a reflection of
the social world the training data encodes and of the value choices made during
alignment. Documented harms---hiring tools that penalise women, risk scores
that misjudge marginalised groups, and clinical algorithms that ration care by
predicted cost rather than need \citep{obermeyer2019}---show that statistical
optimisation can entrench social hierarchy even when no protected attribute is
named. LLMs sharpen this concern because they infer and act upon gender from
ostensibly neutral cues, so removing explicit demographic information does not
remove the bias.

\subsection{The ``alignment-removes-bias'' narrative and its limits}
Industry framing presents successive aligned models as steadily fairer, a claim
echoed in system documentation \citep{openai2023}. Yet alignment is itself a
normative intervention that can overshoot: recent work suggests debiasing can
invert rather than neutralise an association \citep{liu2025}, and that such
reversals are uneven across domains \citep{joshi2024}. Convergent evidence finds
that ``corrected'' models acquire new, opposite skews
\citep{mirza2024,wang2024,karvonen2025}. We synthesise these strands into a
single claim---that alignment \emph{redistributes} bias rather than removing
it---and test it directly.

\subsection{Occupational stereotypes as a persistence channel}
Where valence-linked bias may reverse, occupation-linked bias appears sticky:
the gendering of roles is woven through the textual web of meaning models learn
\citep{lucy2021}. We therefore distinguish two axes---an evaluative axis (who is
``good'') and an occupational axis (who does which job)---and argue that fairness
claims must be evaluated separately on each, since progress on one can mask
stagnation on the other.
```

### 3b. Discussion + Implications section (insert before Conclusion)

```latex
% ===== DRAFT — advisor (Valdemar) validation required =====
\section{Discussion and implications}
\label{sec:discussion}

\subsection{Interpreting overcorrection}
Read through the framework of Section~\ref{sec:framing}, our results show
alignment redistributing rather than removing bias. Completion-era GPT-3 sits
near neutrality; chat-era models swing sharply toward associating valued
characteristics with non-male characters (on the order of sixty-one percentage
points), while occupational stereotypes persist almost untouched. This is the
``overcorrection'' anticipated by \citet{liu2025} and the uneven, domain-specific
reversal reported by \citet{joshi2024}, and it converges with
\citet{mirza2024}, \citet{wang2024}, and \citet{karvonen2025}.

\subsection{Implications for fairness measurement and governance}
A single aggregate fairness score can certify a model as ``debiased'' while it
remains stereotyped on the occupational axis---echoing how an objective chosen
for convenience can encode harm \citep{obermeyer2019}. Audits and disclosures
should report bias \emph{per axis and per direction}, not as a scalar.

\subsection{Implications for design and deployment}
Designers should treat alignment as a value choice with measurable directional
side effects, and stakeholders deploying these models in hiring- or
evaluation-adjacent settings should not assume that ``newer'' means ``fairer.''

\subsection{A reusable audit framework}
Beyond the finding, we offer the prompt-based generative audit pipeline---its
three experiments, multilingual design, and reproducibility protocol (the
896-check suite)---as a reusable instrument for detecting redistributed bias in
future models.

\subsection{Limitations}
Our evidence is behavioural, not mechanistic; it covers the GPT family and two
languages; and the linear-probability estimates summarise associations in
model-generated text rather than downstream real-world decisions.
```

---

## 4. Declarations / required statements (ready to paste)

> Insert immediately **before** `\bibliography{referencias}`. For the **anonymized review copy**, leave author-identifying values as `[TODO]` / "blinded"; move funding and acknowledgements to the **separate Title Page**.

```latex
% ===== Statements and Declarations (REQUIRED — missing block => returned incomplete) =====
\section*{Statements and Declarations}

\paragraph{Competing Interests.}
The authors have no competing interests to declare that are relevant to the
content of this article. % [TODO: confirm; declare any editorial-board roles]

\paragraph{Funding.}
[TODO: list grant/funding sources, or state ``The authors did not receive
support from any organization for the submitted work.''] % NOTE: on Title Page for blinded review

\paragraph{Author Contributions.}
[TODO, e.g.] Both authors contributed to the study conception and design.
Data collection, the audit pipeline, and analysis were performed by [TODO].
The first draft was written by [TODO] and all authors commented on previous
versions. All authors read and approved the final manuscript.

\paragraph{Data Availability.}
The generated story corpus (62{,}000+ texts), analysis notebooks, CSV outputs,
and the 896-check reproducibility suite are available at
[TODO: repository URL / DOI]. % data citations require a persistent DOI

\paragraph{Use of Generative AI.}
The GPT-family models audited in this study are the object of investigation;
their versions, access dates, and prompting procedures are documented in the
Methodology section. [TODO: disclose any use of LLMs in writing/editing, or
state that none was used.]

\paragraph{Ethics Approval.}
Not applicable: the study does not involve human participants, their data, or
animals. % [TODO: confirm]
```

---

## 5. Template & citation conversion notes

**Template (`article` → `sn-jnl.cls`).**
1. Obtain the Springer Nature template (Overleaf: https://www.overleaf.com/latex/templates/springer-nature-latex-template/myxmhdsbzkyd ; class source: https://github.com/godkingjay/springer-nature-latex-template/blob/master/sn-jnl.cls).
2. Set the document class with the basic-citation option: `\documentclass[sn-basic]{sn-jnl}`. For the double-spaced single-column review copy add the review/line-numbered options the template exposes (e.g. `referee`).
3. Map your preamble: title/authors go in the template's `\title{}` / `\author{}` / `\affil{}` macros **on the separate Title Page only**; for the blinded manuscript replace with anonymized placeholders.
4. Convert headings to decimal numbering, **≤3 levels, never skipping a level** (`\section`/`\subsection`/`\subsubsection`); flatten any deeper nesting.
5. Move the 20+ appendix regressions into anonymized **supplementary material** (Springer ESM); keep interpretive figures/tables in the main text.

**Citation switch (natbib/apalike → Springer Basic author-date).**
- You are already author-date, so this is a restyle, not a rethink. Use the Springer Basic bibstyle: in the sn-jnl setup select the `sn-basic` reference style (the template ships the matching `.bst`), or apply the CSL `springer-basic-author-date` (https://github.com/citation-style-language/styles/blob/master/springer-basic-author-date.csl) if compiling via a CSL-aware path.
- Verify the rendered in-text form matches **`(Author Year)` with no comma**, two authors joined by "and", 3+ authors as "et al.".
- Verify reference-list entries render as `Surname FN (Year) Title. Journal Vol:pages. https://doi.org/...` — **initials no periods**, **colon** between volume and pages, **DOI as full URL**. Add missing DOIs in `referencias.bib`.
- `\citet{key}` / `\citep{key}` commands carry over under natbib-compatible Springer styles; no command renaming needed (unlike a numeric `[n]` or `theapa` switch — not applicable here).

---

## 6. Apply checklist (anchors in a copy of `main_english.tex`)

| Snippet | Where to insert (current anchors) |
|---|---|
| **Rewritten abstract (§2)** | Replace the abstract block at **lines ~98–104** (the `\textbf{ABSTRACT}` + two `\noindent` paragraphs). Under `sn-jnl` use the template's `\begin{abstract}…\end{abstract}` instead of the manual `\noindent\textbf{ABSTRACT}` form. |
| **Keywords** | Keep the 5 keywords at **line ~108**; move into the template's `\keywords{}` macro. |
| **Theory/framing section (§3a)** | Insert **before `\section{Methodology}`** (after the Introduction / Lit Review, ~after line 129 region leading into Methodology). |
| **Discussion + Implications (§3b)** | Insert **before `\section{Conclusion}`** (between Results/Tests and Conclusion). |
| **Statements and Declarations (§4)** | Insert **immediately before `\bibliography{referencias}`**. |
| **AI-use sentence** | Add the version/access-date/prompting disclosure **inside the Methodology section** (Springer requires AI-use documented in Methods); the Declarations block then points to it. |
| **Anonymization** | At the preamble/`\maketitle` region (**lines ~90–94**): replace real author/affiliation macros with blinded placeholders; create a **separate Title Page** file with the real metadata, funding, and acknowledgements. |

---

## 7. Honest notes / open items

- **Adaptation effort: MEDIUM.** Mechanics are light (author-date already used, caption placement already matches, 5 keywords compliant, ~5,500 words leaves room toward ~10,000). The lift is substantive, not formatting.
- **Single biggest reframing.** Stop presenting `β₁ = −0.61` as an econometric outcome variable and present it as **evidence of a sociotechnical phenomenon**: aligned chat models *overcorrect* (swing pro-female, ~−61 pp) while occupational stereotypes persist — bias is **redistributed, not removed**. The regressions become evidence in a values-first argument, not the argument itself.
- **Scope candor.** Fit is genuinely good — this is *not* a genre mismatch. LLM gender-bias/fairness work is actively published here (dossier §3, Exemplar 1 is a near-direct analogue). The risk is **register**, not admissibility: a pure econometrics-and-leaderboard presentation reads as out of place, so every coefficient must be narrated for a non-economist and the dense appendix regressions moved to supplementary material.
- **Co-billed framework.** Recommend naming the audit pipeline + 896-check protocol as a reusable contribution (drafted in §3b.4) to match the journal's appetite for a framework alongside a finding.
- **UNCONFIRMED guideline points (from dossier §2 and §7, tied to inherited Springer-wide norms or blocked source pages):** the single-vs-double-column requirement for the *review* PDF; whether a separate Discussion+Implications section is formally *mandated* (it is valued, not required — but adding it is low-risk and recommended); the exact AS wording of the Ethics-approval and Data-availability declaration lines; formal-hypothesis and positionality requirements (appear **not** required); and exact figure dpi/format restatements. Treat the Declarations wording in §4 as inherited-Springer defaults to confirm against the live submission interface.
