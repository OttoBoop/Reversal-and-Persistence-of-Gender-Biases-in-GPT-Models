# Proceedings of the ACM on Human-Computer Interaction (PACMHCI) -- Style & Fit Dossier

## 1. Snapshot

**Proceedings of the ACM on Human-Computer Interaction (PACMHCI)** is a peer-reviewed, archival journal published by the **Association for Computing Machinery (ACM)** through its Digital Library (https://dl.acm.org/journal/pacmhci). It occupies a distinctive structural position in the publishing landscape: rather than being a single-track journal with one editorial board, PACMHCI is a **multi-track umbrella journal** that aggregates the proceedings of several major Human-Computer Interaction (HCI) sub-communities into one indexed publication. Its constituent tracks include **CSCW** (Computer-Supported Cooperative Work and Social Computing -- by far the largest and most active track), **EICS** (Engineering Interactive Computing Systems), **GROUP**, **MobileHCI**, and **ISS** (Interactive Surfaces and Spaces), among others. Each track has its own chairs, editorial board, deadlines, and a track-specific Call for Papers, but all tracks publish into the single PACMHCI volume/issue series and share the same ACM house format (the `acmart` LaTeX class, the ACM Reference Format, and the ACM Computing Classification System for keywords). In practical terms, "the journal's style" equals **ACM house style (acmart) + per-track scope and review process**. Because CSCW is the dominant track and the most likely landing spot for an AI-bias paper, this dossier treats the CSCW track's norms as the operative center of gravity. (Sources: https://dl.acm.org/journal/pacmhci/about ; https://dl.acm.org/journal/pacmhci/tracks/cscw ; https://cscw.acm.org/2026/papers.html)

The **aims and scope** of PACMHCI center on research at the intersection of human factors and computing systems. The CSCW track, which is representative of the journal's social-computing heart, publishes "empirical and critical work on the design and use of technologies that affect groups, organizations, communities, and networks." Crucially, contributions "must have a focus on social aspects of technology mediation and be properly contextualized in the CSCW literature, with clear reference to CSCW concepts and/or theories informing, being affected, or being proposed." Work whose benefit accrues primarily to an *individual* user, or pure systems/algorithmic work that does not make its cooperative, collaborative, or social-computing dimension explicit, is considered **out of scope**. This is a pivotal fact for any incoming author from a different discipline: the journal demands that the *human and social system* -- not the computational artifact alone -- be the unit of analysis. (Source: https://dl.acm.org/journal/pacmhci/tracks/cscw ; https://cscw.acm.org/2026/papers.html)

In terms of **article types**, PACMHCI is deliberately and explicitly inclusive. It publishes: novel empirical research results (qualitative, quantitative, and mixed-methods); designs; systems and engineering/technical enablers (including new services/applications and lab or field evaluations of early-stage and fully-built systems); new conceptual ways of thinking about, studying, or supporting shared activities; and **standalone theoretical contributions** (conceptual frameworks, theory underpinning CSCW domains, theoretical analysis). The venue invites "a variety of human-centered research techniques, methods, approaches, and domains." However, the *modal* paper in this journal -- the one most representative of its real publishing pattern -- is a **qualitative or mixed-methods empirical study with a strong theoretical framing and explicit design/policy implications**. The disciplinary center of gravity is HCI/CSCW with a pronounced social-science inflection (organizational behavior, sociology, ethics, science-and-technology studies). It is emphatically **not** a computer-science-systems venue, **not** a formal-proofs venue, and **not** an economics/econometrics venue. (Sources: https://dl.acm.org/journal/pacmhci/about ; https://dl.acm.org/journal/pacmhci/tracks/cscw)

The **typical audience** consists of HCI and social-computing researchers, interaction designers, CSCW scholars, and increasingly researchers in AI ethics and responsible computing who work from a human-centered (rather than purely technical) standpoint. Readers expect to see participant quotes, thematic analyses, conceptual frameworks, and discussions of implications for design and society -- not regression tables and p-values as the dominant evidentiary mode.

## 2. Style guide / author guidelines

### Manuscript template and format

PACMHCI accepts **both LaTeX and Word** submissions; manuscripts are converted to PDF before upload to the review system. The PACMHCI submission-templates page states: *"Authors should submit manuscripts for review in a single column format, which is available for Word and LaTeX. Manuscripts should be converted to PDF before submission."* The LaTeX class is ACM's **`acmart`**, and the document-class line authors are instructed to use is:

```
\documentclass[acmsmall]{acmart}
```

The submission-templates page states: *"the document class should read `\documentclass[acmsmall]{acmart}`. LaTeX users can download the template provided by the ACM, or may use the Overleaf template."* (Source: https://dl.acm.org/journal/pacmhci/submission-templates ; https://github.com/borisveytsman/acmart)

> **UNCONFIRMED / NUANCE:** There is a conflicting historical signal that PACMHCI once used the `acmlarge` format. This appears to be **outdated**; the current operational instruction is `acmsmall` (the small, single-column journal format). Additionally, because PACMHCI is produced through Sheridan, the CSCW Call for Papers directs authors to use an "interim ACM Small template" available *only* from the PACMHCI submission-templates page, rather than the generic current `acmart` download. Treat `acmsmall` as correct, and point authors to the PACMHCI submission-templates page for the exact template file. (Source: search summary of cscw.acm.org submit-papers — this access was proxy-blocked and not eyeball-verified.)

The format is **single column** for both review and final publication (`acmsmall` is the small single-column journal format).

For **double-anonymous (two-way blind) review**, which PACMHCI requires, the typical anonymized preamble is:

```
\documentclass[acmsmall,anonymous,review]{acmart}
```

The `anonymous` option strips identifying material, and `review` adds line numbers for reviewers. Anonymization is mandatory and strictly enforced: *"Submissions must have authors' names and affiliations removed, including references to universities, companies, labs, and cities. Any grant information that identifies the author(s) and their institution should be removed as well."* Authors must also scrub document metadata, headers/footers, image metadata, and acknowledgements; violations are desk-rejected. (Sources: https://dl.acm.org/journal/pacmhci ; https://github.com/borisveytsman/acmart)

### Citation style

The citation style is the **ACM Reference Format** (`ACM-Reference-Format.bst` / biblatex `acmnumeric`). For PACMHCI the default and the norm is **numeric citation**, set via `\citestyle{acmnumeric}`. The acmart documentation states: *"Numeric citations are the default mode for most formats. Authors can choose either author-year citations with `\citestyle{acmauthoryear}`, or numeric citations with `\citestyle{acmnumeric}`."*

- **Exact in-text form:** a bracketed number, e.g. `[1]`; multiple sequential references in one bracket separated by commas, e.g. `[1, 2]`. ACM's reference-formatting page states: *"ACM encloses the number of the reference in square brackets, thus: [1]. Sequential parenthetical citations are enclosed in square brackets and separated by commas, thus [1, 2]."*
- **Reference-list ordering (commonly misunderstood):** under `acmnumeric`, the reference list is ordered **alphabetically by the lead author's surname and then numbered consecutively**. The in-text number `[7]` therefore points to the 7th entry in the *alphabetized* list, **not** to citation order of appearance. ACM's summary: *"all references appear alphabetically by the lead author's last name and are numbered consecutively."*
- **Reference entry format:** full ACM Reference Format -- authors (full first names), year, title, venue, volume/issue/article number, page count, and DOI. ACM's worked example: `[1] Sarah Cohen, Werner Nutt, and Yehoshua Sagiv. 2007. Deciding equivalences among conjunctive aggregate queries. J. ACM 54, 2, Article 5 (April 2007), 50 pages. https://doi.org/10.1145/1219092.1219093`
- **DOIs are required** whenever one exists (journal articles, conference papers, archived datasets); acmart auto-renders them as `https://doi.org/...`. For sources without a DOI, provide the most stable URL and a retrieval date.
- acmart auto-generates the boxed **"ACM Reference Format:"** self-citation block on page 1, mandatory for papers over one page.

(Sources: https://www.acm.org/publications/authors/reference-formatting ; https://github.com/borisveytsman/acmart ; https://github.com/borisveytsman/acmart/blob/primary/ACM-Reference-Format.bst)

### Abstract rules

The abstract goes in the acmart `\begin{abstract}...\end{abstract}` environment as a **single unstructured paragraph** -- **not** a structured abstract with sub-headings.

> **UNCONFIRMED:** No hard numeric word limit for the full-paper abstract was verifiable from a primary PACMHCI page in this research (the 150-250-word figure that surfaced applies to the CSCW Doctoral Consortium abstract, a different submission type). In practice the norm is roughly **150-250 words**. Verify the exact maximum against the live submission-templates page if a number is needed.

> **STRONG CONVENTION / UNCONFIRMED as written rule:** ACM/acmart convention is to **avoid citations in the abstract** (it must stand alone and is reused in indexing metadata). This is near-universal in practice but was not located as an explicit verbatim rule on a PACMHCI primary page.

Some tracks (CSCW) additionally require a **separate scope/contribution statement** at submission that must be **fully anonymized**: *"The scope statement should be fully anonymized... must not contain any information that can identify any of the authors, their institutions, partners, or cities."* (Source: https://cscw.acm.org/2026/papers.html)

### Structure expectations

The publisher mandates **no fixed section structure**; acmart imposes none. However:

- **IMRaD is common but not required.** Empirical PACMHCI papers commonly follow Introduction -> Related Work -> Method -> Findings -> Discussion -> Conclusion, but conceptual, critical, design, and methodological papers deviate freely.
- **Hypotheses are NOT required and are NOT the norm.** Formal, pre-registered-style hypotheses (H1/H2) appear only in some quantitative submissions; much of the venue is qualitative or interpretivist, where formal hypotheses are inappropriate.
- **Theory / conceptual framing is effectively expected.** CSCW requires that contributions be "properly contextualized in the CSCW literature, with clear reference to CSCW concepts and/or theories." A related-work / theoretical-framing section is, in practice, mandatory; standalone conceptual contributions are explicitly welcomed.
- **Discussion + Implications is a strong genre norm** (not a formatted requirement). The community rewards papers that articulate how findings advance CSCW concepts/theory and design; an "Implications for design" or "Implications for CSCW" discussion is a strong genre expectation, especially for empirical/systems work. (Mark "separate Implications section" as a NORM, not a written rule.)
- **Headings:** acmart provides auto-numbered hierarchical `\section` / `\subsection` / `\subsubsection` with ACM typographic styling.

(Sources: https://cscw.acm.org/2026/papers.html ; https://dl.acm.org/journal/pacmhci/tracks/cscw ; https://github.com/borisveytsman/acmart)

### Figures and tables

- **Caption placement:** table captions **above** the table; figure captions **below** the figure (ACM/acmart convention).
- **Numbering:** auto-numbered via `\caption` + `\label`/`\ref`; figures and tables numbered in separate sequences.
- **Tables:** acmart recommends `booktabs` rules; vertical rules are discouraged (ACM table style).
- **Accessibility:** acmart requires a `\Description{...}` (alt-text) for each figure -- this is a real, enforced requirement.
- **Resolution:** print-quality figures (vector preferred; raster ideally >=300 dpi). *(Exact DPI on a PACMHCI primary page is UNCONFIRMED, but this is ACM production norm.)*
- **Source/attribution:** provide attribution in the caption or a note for reused material; permissions required for copyrighted third-party figures.

(Sources: https://github.com/borisveytsman/acmart ; https://github.com/borisveytsman/acmart/issues/312)

### Keywords

Two distinct things are **required for all papers over two pages** (effectively all full papers):

1. **ACM CCS Concepts**, chosen via the ACM Computing Classification System tool, pasted as a CCSXML block plus `\ccsdesc{...}` commands (with High/Medium/Low significance weighting).
2. **Author keywords**, a comma-separated free-text list via `\keywords{...}`.

The acmart changelog states CCS concepts and keywords are "mandatory for papers over two pages." ACM guidance: *"User-defined keywords are a comma-separated list of words and phrases of the authors' choosing."*

> **UNCONFIRMED:** No strict required *count* for CCS concepts or author keywords was found. Norm: 1-3 CCS concepts and roughly 3-6 author keywords.

(Sources: https://github.com/borisveytsman/acmart ; https://www.acm.org/publications/authors/submissions)

### Length norms

**No fixed minimum or maximum page count.** PACMHCI/CSCW states: *"Papers have no fixed minimum or maximum number of pages. Papers that are widely over the typical length (e.g., above 12,000 words) will be examined carefully to ensure that the size of the contribution warrants the length of the paper. Papers whose lengths are incommensurate with their contributions will be rejected."* So 12,000 words is a **soft scrutiny threshold, not a cap**. Long papers (30-42 pages) are routine. Supplementary materials, datasets, video figures, and appendices are supported.

> **UNCONFIRMED:** Whether references/appendices are formally excluded from any word count was not confirmed; treat the 12k figure as main-text guidance.

(Sources: https://dl.acm.org/journal/pacmhci ; https://cscw.acm.org/2026/papers.html ; https://cscw.acm.org/rolling.html)

### Required statements / declarations

- **Anonymization (review):** required; desk-reject if violated (see above).
- **Generative AI / LLM disclosure (ACM-wide, applies to PACMHCI):** use of generative AI to *create content* is permitted but **must be disclosed in the Work**, normally in the Acknowledgements, specifying which tools and how (e.g. *"ChatGPT was utilized to generate sections of this Work, including ..."*). Generative AI **cannot be an author** under any conditions. **Exception:** purely editorial use (Grammarly-style improvement of existing text) does not require disclosure. Authors also complete an AI Declaration in the submission form. (Sources: https://respect.acm.org/2026/index.php/policies-on-generative-ai-llms-and-related-tools/ ; https://medium.com/sigchi/acm-publications-policy-guidance-for-sigchi-venues-87332173aad1)
- **Ethics / human subjects (IRB):** research with human participants is expected to meet ACM/SIGCHI research-ethics expectations, including IRB/ethics-board approval where applicable. *(UNCONFIRMED as a single quotable PACMHCI sentence, but an established SIGCHI/ACM expectation; reviewers assess research ethics.)*
- **Conflict of interest:** authors/reviewers declare conflicts via the submission system (ACM COI policy). *(UNCONFIRMED as an in-text required section; it is a submission-process declaration.)*
- **Data availability / reproducibility:** ACM supports artifact/data sharing and badging; sharing is **encouraged and increasingly expected**, but a mandatory in-paper Data Availability Statement with fixed wording was **not confirmed** (ENCOURAGED / partly UNCONFIRMED). DOIs required for cited archived datasets.
- **Funding:** acknowledged in Acknowledgements (removed for anonymized review).
- **Author contributions:** a CRediT-style statement is **not confirmed as mandatory** at PACMHCI (UNCONFIRMED; allowed, not required).
- **Positionality / reflexivity:** **not** a formatted publisher requirement, but a **strong and increasingly expected community norm** for qualitative/critical CSCW/CHI work; reviewers frequently expect authors to address reflexivity and positionality. Present it as an expected element of qualitative PACMHCI papers (grounded in community methodological literature, e.g. Fiesler's "Qualitative Methods for CSCW"; CHI 2025 "Exploring Positionality in HCI"), not a publisher mandate. (Sources: https://dl.acm.org/doi/10.1145/3311957.3359428 ; https://dl.acm.org/doi/full/10.1145/3706598.3713280)

### Canonical preambles (reusable)

- **Camera-ready:** `\documentclass[acmsmall]{acmart}` + `\setcopyright{...}`, `\acmJournal{PACMHCI}`, CCSXML/`\ccsdesc`, `\keywords{...}`, `\begin{abstract}`, `\maketitle`, numeric `\citestyle{acmnumeric}`, `ACM-Reference-Format.bst`.
- **Anonymized review:** `\documentclass[acmsmall,anonymous,review]{acmart}`.

> **ACCESS CAVEAT:** `dl.acm.org`, `acm.org`, `cscw.acm.org`, `respect.acm.org`, and CTAN were not directly fetchable during this research (tool/proxy HTTP 403). The dl.acm.org and acm.org content above is sourced via the web-search engine's reading of those exact primary pages and corroborated by readable acmart docs (GitHub) and the CSCW Call for Papers. A live re-check of the abstract word limit and the keyword/CCS counts is recommended before final submission.

## 3. Published-paper exemplars

**Headline signal:** PACMHCI does publish LLM/ChatGPT and AI-bias/fairness work, but with a strong **human-centered HCI/CSCW slant** rather than the pure computational-audit slant of the user's paper. Repeated targeted searching showed that **pure GPT/LLM bias *audits*** -- prompt the model, measure demographic skew, report quantitative bias metrics, which is exactly the user paper's genre -- **overwhelmingly land at FAccT, EAAMO, AIES, ACM Multimedia, and CHI, not PACMHCI.** Non-PACMHCI examples confirming this clustering: *"The Silicon Ceiling: Auditing GPT's Race and Gender Biases in Hiring"* (EAAMO '24, https://dl.acm.org/doi/10.1145/3689904.3694699), *"Identifying and Improving Disability Bias in GPT-Based Resume Screening"* (FAccT '24, https://dl.acm.org/doi/10.1145/3630106.3658933), and *"New Job, New Gender? Measuring the Social Bias in Image Generation Models"* (ACM MM '24, https://dl.acm.org/doi/10.1145/3664647.3681433). What PACMHCI publishes on this topic instead is (i) mixed-method studies of people's experiences/perceptions of AI bias and ethics, (ii) qualitative thematic analyses of user discourse about LLMs, and (iii) justice/ethics-framed empirical studies of AI in social/organizational settings. The three closest *native* PACMHCI exemplars follow.

### Exemplar 1 — "AI Ethics and Social Norms: Exploring ChatGPT's Capabilities From What to How" (the single most on-topic PACMHCI exemplar)

- **Authors / year / venue:** Omid Veisi, Sasan Bahrami, Roman Englert, Claudia Müller. 2025. *Proc. ACM Hum.-Comput. Interact.* 9, 7 (CSCW), Article CSCW216, pp. 1-34.
- **Links:** https://doi.org/10.1145/3757397 ; landing https://dl.acm.org/doi/10.1145/3757397 ; open preprint https://arxiv.org/abs/2504.18044.
- **Topical fit:** As LLM/bias-adjacent as PACMHCI gets. Keywords: "AI ethics, ChatGPT, bias, large language models, social norms, trustworthiness." **Bias is one of its six core themes** (bias, trustworthiness, security, toxicology, social norms, ethical data). It explicitly positions ChatGPT "as an everyday-life tool *in the CSCW community*" -- i.e., it performs exactly the human-centered reframing the user's paper would need. **This is the template to imitate for fit.**
- **Structure (arc CONFIRMED; subsection granularity UNCONFIRMED):** Introduction -> Related Work/Background (AI ethics, social norms, machine ethics, CSCW situating) -> Methodology (survey design + interview design + thematic-analysis coding) -> Findings organized by the six themes -> Discussion (transparency and bias in unsupervised data collection; implications for CSCW/design) -> Limitations -> Conclusion -> References.
- **Methods:** **Mixed-methods.** Quantitative strand = Likert-scale online **survey, N=111**. Qualitative strand = **semi-structured expert interviews, N=38**, analyzed by **thematic analysis** with combined deductive+inductive coding by two coders. Findings presented theme-by-theme, blending survey descriptives with interview quotes. **No formal hypotheses, no regression** -- exploratory/characterizing.
- **Theory:** dedicated background/related-work framing on AI ethics, social norms, machine ethics, and CSCW.
- **Abstract:** single narrative paragraph (acmart unstructured), ~180-230 words (UNCONFIRMED exact), motivation -> method (two N's) -> six-aspect findings; no citations.
- **Citations:** ACM numeric `[n]`, alphabetical-then-numbered list (journal-wide CONFIRMED).
- **Tone:** HCI/CSCW + applied AI-ethics; human-centered, qualitative-leaning, empirically descriptive.
- **Length:** **34 pages** -- upper-normal PACMHCI band.
- **Contribution type:** empirical finding + a light conceptual framework (the six-theme organization) + design/CSCW implications. Not a new method, not a formal model.

### Exemplar 2 — "Interrogating AI: Characterizing Emergent Playful Interactions with ChatGPT" (LLM-direct, the dominant qualitative genre)

- **Authors / year / venue:** Mohammad Ronagh Nikghalb, Jinghui Cheng. 2025. *Proc. ACM Hum.-Comput. Interact.* 9, 2 (CSCW), Article CSCW117.
- **Links:** https://doi.org/10.1145/3711015 ; landing https://dl.acm.org/doi/10.1145/3711015 ; open preprint https://arxiv.org/abs/2401.08405.
- **Topical fit:** Directly about ChatGPT (topically adjacent to the user's LLM focus) but its lens is **human-AI relationship / agency**, not bias. The prototypical **qualitative social-computing PACMHCI paper**: it analyzes online *discourse about* an LLM rather than auditing the model -- a sharp contrast to the user's computational-audit approach.
- **Structure (arc CONFIRMED):** Introduction -> Related Work (play in HCI; human-AI interaction; AI agency) -> Methods (Reddit data collection via Pushshift API; sampling; thematic-analysis procedure) -> Findings (six playful-interaction types + sub-types) -> Discussion (what play reveals about users negotiating AI agency; design implications) -> Conclusion -> References.
- **Methods:** **Purely qualitative** thematic analysis of **372 r/ChatGPT posts**; finds 54% of discourse "playful" and builds a **preliminary six-type framework** (reflecting, jesting, imitating, challenging, tricking, contriving). Results = framework + illustrative quotes. **No hypotheses, no statistics.**
- **Abstract:** single narrative paragraph, ~150-200 words (UNCONFIRMED exact); no citations.
- **Citations:** ACM numeric `[n]`.
- **Tone:** HCI/CSCW, interpretivist-qualitative, reflexive, theory-aware, humanities-inflected (play, agency). Strongly representative of the *modal* PACMHCI paper.
- **Length:** standard CSCW article length (~20-28 pp typical; exact UNCONFIRMED).
- **Contribution type:** conceptual framework + empirical characterization (a data-grounded taxonomy) with design implications.

### Exemplar 3 — "U.S. Job-Seekers' Organizational Justice Perceptions of Emotion AI-Enabled (Asynchronous) Interviews" (AI bias/fairness, justice-framed empirical genre)

- **Authors / year / venue:** Cassidy Pyle, Kat Roemmich, Nazanin Andalibi. 2024. *Proc. ACM Hum.-Comput. Interact.* 8, CSCW2, Article 454, pp. 1-42.
- **Links:** https://doi.org/10.1145/3686993 ; landing https://dl.acm.org/doi/abs/10.1145/3686993.
- **Topical fit:** Not LLM-specific, but **squarely about AI bias and fairness** -- it studies people's perceptions of **identity-related bias** and (un)fairness in an AI hiring system. It exemplifies how PACMHCI frames "AI bias" through a **social-science justice-theory** lens (organizational/distributive/procedural/interactional justice) rather than a technical bias-metric lens -- the key contrast for the user's paper. Andalibi's lab is a canonical PACMHCI fairness-of-AI source.
- **Structure (arc CONFIRMED):** Introduction -> Related Work/Background (emotion AI; hiring/algorithmic fairness; organizational-justice theory) -> Methods (recruitment; 14 interviews; analysis) -> Findings (organized by the three justice dimensions) -> Discussion (implications for fairness, design, and policy; tensions with vendor "reduces bias" claims) -> Limitations -> Conclusion -> References.
- **Methods:** **Qualitative.** Exploratory semi-structured **interviews, N=14** U.S. job-seekers; thematic coding. Findings mapped onto three justice dimensions: inaccurate inferences = *distributive injustice*; identity-related **bias** = *procedural injustice*; lack of transparency = *interactional injustice*. **No hypotheses, no statistics.**
- **Theory:** notably **theory-forward** -- organizational-justice theory is the explicit analytic scaffold.
- **Abstract:** single narrative paragraph, ~180-220 words (UNCONFIRMED exact); no citations.
- **Citations:** ACM numeric `[n]`.
- **Tone:** HCI/CSCW with social-science (organizational-behavior / ethics-justice) flavor; critical, theory-grounded, qualitative, policy-aware.
- **Length:** **42 pages** -- confirms the no-cap, contribution-commensurate norm.
- **Contribution type:** empirical finding (qualitative characterization of perceived (in)justice/bias) framed by existing theory, with design/policy implications.

### Cross-exemplar synthesis

All three use **ACM numeric `[n]` citations** with an alphabetical-then-numbered list. All three use a **single narrative, unstructured abstract** (~150-230 words; motivation -> method -> findings -> implications; no citations). All three follow an **IMRaD-like arc with thematically organized findings** and a **Discussion heavy on implications for design/CSCW/policy**. **None has formal hypotheses or significance tables.** A **theoretical / related-work framing section is effectively mandatory**, and two of the three build or apply an explicit conceptual framework. **Qualitative or mixed-methods dominate;** a pure quantitative model-audit was not found among native PACMHCI papers on this topic. **No length cap; long is normal** (34 and 42 pages here). Contribution type is **empirical findings + conceptual frameworks grounded in data**, never new algorithms, formal proofs, or normative-only philosophy.

## 4. How it differs from YOUR paper

The user's paper -- *"Reversal and Persistence of Gender Biases in GPT Models"* -- is an **applied labor-economics + algorithmic-fairness audit** in the Bertrand-Mullainathan resume-audit tradition, currently styled for *Public Choice* (Springer). It is ~80% empirical, regression-driven (OLS linear-probability model with robust SEs), author-date cited, hypothesis-free but econometrics-heavy, and treats gender bias as a measured **outcome variable**. PACMHCI's norms diverge from this on nearly every axis.

| Dimension | User paper (baseline, Public Choice style) | PACMHCI norm | Severity of gap |
|---|---|---|---|
| Discipline / framing | Applied labor economics + algorithmic fairness; economist's voice; bias as a regression outcome variable | HCI/CSCW human-centered social computing; bias as a social/justice/ethics phenomenon situated in CSCW theory | **Very high** |
| Manuscript template | Generic LaTeX article (12pt, a4paper), no journal template; natbib/apalike | acmart class, `\documentclass[acmsmall]{acmart}`, single column, CCSXML + `\Description{}` | **High** |
| Citation style | Author-date (citet/citep), Chicago/APA, ~80-100 refs; numeric NOT used | ACM Reference Format, **numeric `[n]`**, alphabetical-then-numbered list | **High** |
| Abstract format | ~240 words, two paragraphs, narrative + quantitative, no headings | Single unstructured paragraph, ~150-250 words, no citations | **Low-medium** (just trim/merge) |
| Section structure | Intro -> Lit Review -> Methodology (8 subsections, equations in-text) -> Results (Test 1/2/3) -> Conclusion; **no Discussion section** | Intro -> Related Work (theory-bearing) -> Methods -> Findings (thematic) -> **Discussion + Implications** -> Limitations -> Conclusion | **High** (must add Discussion/Implications + theory framing) |
| Hypotheses | None (no H1/H2) -- aligns | None expected -- aligns | **None** |
| Theory / conceptual section | None dedicated | Effectively mandatory; explicit CSCW concepts/theory required | **High** |
| Methods presentation | OLS linear-probability model, robust SEs, p-values, R-squared, coefficients as percentage points | Qualitative/mixed-methods dominant (thematic analysis, interviews, surveys); pure quant audit is an outlier | **Very high** |
| Empirical vs conceptual weight | ~80% empirical quantitative | Empirical, but interpretive/qualitative weight + conceptual framing expected | **High** |
| Tone / voice | Formal economist, first-person plural, hedged, policy-aware, reproducibility-heavy | Human-centered, interpretivist, reflexive, design/implications-oriented; positionality norm for qual work | **High** |
| Length | ~15 pp main + large appendix | No cap; 30-42 pp routine; appendices fine | **Low** (length itself is welcome) |
| Figures/tables | 4 main + 2 detailed regression tables, 10 bar/distribution figures; fig captions below, table captions above | Fig captions below, table captions above (**aligns**); booktabs, no vertical rules; `\Description{}` required; regression-table-heavy presentation is atypical | **Low-medium** on mechanics; **medium** on the regression-heavy *style* |
| Contribution type | Quantitative empirical finding ("overcorrection"); audit method | Empirical finding + conceptual framework grounded in data + design/policy implications | **High** |

**In prose:** The two biggest gaps are **disciplinary framing** and **methods presentation**. PACMHCI does not want a stand-alone econometric audit; it wants the audit *embedded in a human-centered, CSCW-theory-grounded argument about people and social systems.* The user's OLS-with-robust-SEs apparatus, percentage-point coefficient interpretation, and 20+ appendix regressions are alien to a venue whose modal evidence is thematic analysis of interviews and discourse. The user paper's **lack of a Discussion/Implications section** is a serious structural mismatch: in PACMHCI the Discussion-and-implications move is where a paper earns its keep. The **citation switch** (author-date -> numeric `[n]`) and the **template switch** (generic article -> acmart) are mechanical but unavoidable. Several things actually align and reduce friction: the paper already has **no formal hypotheses** (matching the venue), already uses **figure-captions-below / table-captions-above**, has a **narrative abstract close to the right length**, and its **long-with-appendix shape** is welcome under PACMHCI's no-cap norm. But none of those alignments touch the core problem: the paper's *epistemology* (model-as-object, regression-as-evidence) is the opposite of PACMHCI's (human-as-subject, interpretation-as-evidence).

## 5. Fit & recommendation

**Fit as-is: poor.** The user's paper is **adjacent to, but not native to,** PACMHCI's dominant genre. The topic (gender bias in GPT models) is within the broad sphere of AI-ethics work the journal will read, but the **method (a pure quantitative computational audit) and the framing (labor economics / regression outcome) are not in the venue's center of scope.** As the exemplar research showed, papers of exactly this type -- prompt the model, measure demographic skew, report bias metrics -- systematically publish at **FAccT, EAAMO, AIES, ACM Multimedia, and CHI**, not at PACMHCI. PACMHCI would likely judge a straight audit as insufficiently grounded in CSCW concepts and insufficiently focused on the *social aspects of technology mediation* -- the explicit scope test the CSCW track applies, which can trigger desk-level scope rejection.

**Specific changes required to make it fit:**

1. **Reframe disciplinarily.** Recast the paper as a human-centered / social-computing contribution: not "we estimate the coefficient on gender" but "what does the reversal-and-persistence pattern in GPT outputs *mean for the people and social systems* that increasingly rely on these models, and how should designers and platforms respond?" Ground it explicitly in CSCW concepts/theory (e.g. algorithmic fairness as a social/justice construct, value alignment, sociotechnical systems).
2. **Re-platform to acmart.** `\documentclass[acmsmall]{acmart}`, single column, CCSXML + `\ccsdesc`, `\keywords{}`, `\Description{}` on every figure, booktabs tables.
3. **Switch citations** from author-date to numeric ACM Reference Format `[n]` with an alphabetical-then-numbered reference list.
4. **Restructure:** add a **theory/related-work section** with explicit CSCW grounding, and add a substantial **Discussion + Implications** section (currently absent) -- implications for users, society, design, and policy. Keep findings but consider organizing them thematically (e.g. "overcorrection," "persistent occupational stereotypes") rather than purely as Test 1/2/3.
5. **Rebalance methods.** Demote the econometric machinery from foreground to a clean, well-justified empirical strand, move the 20+ appendix regressions to supplementary material, and -- ideally -- **add a qualitative or interpretive layer** (e.g. qualitative reading of generated stories, or a small study of how users/practitioners perceive these biases) to read as native mixed-methods.
6. **Adjust abstract** to a single unstructured paragraph (~200 words), no citations.
7. **Add required statements:** generative-AI disclosure if applicable, ethics handling of the generated-data pipeline, and a data/reproducibility statement (its existing Jupyter/CSV reproducibility assets are a strength here).
8. **Consider a reflexivity/positionality note** if any qualitative layer is added (community norm, not a mandate).

**ADAPTATION EFFORT RATING: HIGH.** This is not a reformat -- it is a re-genre-ing. The citation and template changes are mechanical (Medium at most on their own), but the substantive demands -- adding a theory section, adding a Discussion/Implications section, demoting the econometrics, grounding everything in CSCW theory, and ideally adding a qualitative strand -- amount to **rewriting the paper's argument and evidence structure for a different epistemic community.** The risk of scope rejection remains real even after this work.

**The single most important reframing the journal would demand:** shift the unit of analysis from **the model and its measured coefficients** to **the human and social systems affected by the model's biases**, and make the contribution a *human-centered, CSCW-theory-grounded* one with explicit implications for design, users, and society -- not a free-standing econometric audit of GPT outputs.

**Candid bottom line:** Unless the user is prepared to substantially re-conceive the paper as social-computing scholarship, **FAccT, AIES, or EAAMO are far better-matched homes** for this exact method and framing than PACMHCI. PACMHCI is viable only with the High-effort reframing above.
