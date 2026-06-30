# AI & Society -- Style & Fit Dossier

> Comparison target: *"Reversal and Persistence of Gender Biases in GPT Models"* (Otavio Oliveira Bopp & Valdemar Pinho Neto), an applied-labor-economics / algorithmic-fairness manuscript currently styled for **Public Choice** (Springer) on the conservative Motoki-et-al.-(2024) template. This dossier evaluates the journal **AI & SOCIETY: Knowledge, Culture and Communication** (Springer Nature) as an alternative venue and itemizes exactly what adapting the manuscript would require.

---

## 1. Snapshot

**Publisher and identity.** *AI & SOCIETY: Knowledge, Culture and Communication* is a Springer Nature journal (journal number 146), one of the oldest standing venues at the intersection of artificial intelligence and the human/social sciences. Its journal home is at https://link.springer.com/journal/146 and it operates as a hybrid (subscription + open-access) title with an article-processing charge that, at time of indexing, was on the order of £2390 / $3390 / €2790 for the open-access option (source: https://link.springer.com/journal/146/submission-guidelines). It is a peer-reviewed, **double-blind** journal: per the guidelines, "No article is accepted without two complete and final reviews. Only the Editor-in-Chief can make a final decision."

**Aims and scope.** The journal's self-description (https://link.springer.com/journal/146/aims-and-scope) centers on societal questions raised by computing and AI: it focuses on "the design, use, management, and policy of information, communications and new media technologies, with a particular emphasis on cultural, social, cognitive, economic, ethical, and philosophical implications." Crucially for fit, it states that it "positions the significance of values for critical thinking, a diversity of cultural perspectives and practices... to shape AI mediated futures for the common good," and that it is "strongly interdisciplinary, and welcomes reflective and contextual contributions and participation from researchers and practitioners in a variety of fields including humanities, social sciences." The disciplinary center of gravity is therefore the **humanities and social sciences with a critical / STS / ethics orientation** -- not computer science as a benchmarking discipline, and not economics as a quantitative-modeling discipline, though "economic ... implications" are explicitly within scope.

**Article types it publishes.** The journal is organized into four parts plus a News section: **(a) Research**, **(b) Open Forum**, **(c) Curmudgeon Corner**, and **(d) Reviews / Book Reviews**. Per the guidelines it "publishes refereed scholarly articles, position papers, debates, short communications, systematic reviews and reviews of books and other publications." Research articles are required to be "strictly focused, academically coherent, theoretically grounded, methodologically sound and empirically strong." This means the journal publishes the full method spectrum: rigorous **empirical** work (including computational/NLP audits), **conceptual / normative / critical-theory** essays, **theory-building / framework** papers, and **systematic reviews** (PRISMA-style). Empirical strength is welcomed but is explicitly co-equal with -- and often subordinate to -- theoretical grounding and societal framing.

**Typical audience and disciplinary center of gravity.** Readers are interdisciplinary scholars of technology-and-society: philosophers of technology, STS researchers, HCI and information-systems academics, communication scholars, critical social theorists, ethicists, and policy researchers. The flavor that unifies the journal is a **critical, society-facing, values-first** register. Even its most quantitative papers are wrapped in a social/ethical argument rather than a state-of-the-art leaderboard framing. For a paper written in an economist's voice with regression coefficients as the headline product, this audience is reachable but will expect the social-theoretical and ethical stakes to be foregrounded.

---

## 2. Style guide / author guidelines

> Primary source: the AI & SOCIETY submission-guidelines page, https://link.springer.com/journal/146/submission-guidelines. Note: link.springer.com returns HTTP 403 to automated fetchers; the quotations below are drawn from the indexed text of that page plus Springer Nature's publisher-wide manuscript-preparation pages, which AI & SOCIETY inherits. Points that could be tied only to inherited Springer-wide norms rather than the journal page itself are explicitly marked **UNCONFIRMED**.

### Template / format (LaTeX class or Word)

Both **Microsoft Word and LaTeX** are accepted; there is no ACM `acmart`, JAIR, or other numeric-CS template here. The LaTeX template is the current Springer Nature article class **`sn-jnl.cls`** (the "Springer Nature LaTeX template," available on Overleaf at https://www.overleaf.com/latex/templates/springer-nature-latex-template/myxmhdsbzkyd and as source at https://github.com/godkingjay/springer-nature-latex-template/blob/master/sn-jnl.cls; older Springer journals used `svjour3.cls`). Springer explicitly does not require authors to mimic the final typeset layout at submission -- a plain, readable, **single-column, double-spaced** manuscript is acceptable for review, with the formal template mainly needed at production. (The specific single-vs-double-column requirement for the AI & SOCIETY *review* PDF is **UNCONFIRMED** from the journal page itself; this is the inherited Springer norm.) Springer house style requires the **decimal heading numbering system, no more than three levels, never skipping a level** (source: https://www.springernature.com/gp/authors/publish-a-book/manuscript-guidelines).

**Hard requirement -- double-blind anonymization.** Verbatim from the guidelines: "The journal follows a double-blind reviewing procedure. This means that the author will remain anonymous to the reviewers throughout peer review. It is the responsibility of the author to anonymize the manuscript and any associated materials." And: "Author names, affiliations and any other potentially identifying information should be removed from the manuscript text and any accompanying files (such as figures [or] supplementary material); A separate Title Page should be submitted, containing title, author names, affiliations, and the contact information of the corresponding author." Acknowledgements, disclosures, and funding go on that separate Title Page.

### Citation style (with exact in-text form)

The journal uses the Springer Nature **"Basic" author-date** house style -- an author-date (Harvard-derived) system. It is **not numeric/Vancouver, not ACM Reference Format, and not APA or Chicago by name**, though it resembles Harvard. (Style reference: https://citationsy.com/styles/springer-basic-author-date; CSL definition: https://github.com/citation-style-language/styles/blob/master/springer-basic-author-date.csl; journal-specific entry: https://citationsy.com/styles/ai-and-society.)

- **Exact in-text form:** `(Author Year)`, e.g. **(Petit and Sieffermann 2007)** -- note **no comma** between author and year, two authors joined by "and," three-or-more authors use "et al." in text.
- **Reference list:** alphabetical by first-author surname.
- **Journal-article entry (exact Springer Basic form):** `Surname FN (Year) Article title. Journal name Volume:page-range. https://doi.org/...` -- author initials carry **no periods**, year in parentheses, volume and pages joined by a colon, DOI as a full `https://doi.org/...` URL.
- **Book entry:** `Surname FN (Year) Title, edition. Publisher, City` -- e.g. *Angelou M (1969) I Know Why the Caged Bird Sings, 1st edn. Random House, New York.*
- DOIs are required where available; data citations must include a persistent identifier (DOI).

(Generator/format reference: https://paperpal.com/tools/citation-generator/springer-basic-author-date-citation-generator.)

### Abstract rules

Standard Springer abstract length is **150-250 words**, and AI & SOCIETY explicitly allows extension: "The abstract length can be increased from the 250-word limit (to up to 450 words) if the topic dictates, and to allow full compliance with the relevant reporting guidelines." The abstract is **single-paragraph and unstructured** (no sub-headings) -- a structured-abstract requirement is **UNCONFIRMED / not required**. Springer house rule: the abstract "must not contain any undefined abbreviations or unspecified references" (i.e. **no citations in the abstract**). Curmudgeon Corner pieces carry no abstract at all.

### Structure expectations (IMRaD? hypotheses? theory? Discussion?)

There is **no rigid IMRaD mandate.** Because the journal is "strongly interdisciplinary" and publishes conceptual, philosophical, critical, empirical, and qualitative work, it sets a quality bar rather than a skeleton: research articles must be "strictly focused, academically coherent, theoretically grounded, methodologically sound and empirically strong." A **theory / conceptual development** component is genuinely expected -- the journal "positions the significance of values for critical thinking" and (for Open Forum) expects submissions "to expose key concepts, ideas, and theories through deep and detailed engagement with foundational works." **Formal numbered hypotheses (H1/H2) are NOT required or expected** (this is not a hypothetico-deductive social-psych venue) -- **UNCONFIRMED as any requirement; effectively not required.** A **separate Discussion + Implications section is not formally mandated** (appropriate for empirical pieces, not prescribed for conceptual ones) -- **UNCONFIRMED as a requirement.** **Researcher positionality / reflexivity** is culturally valued ("welcomes reflective and contextual contributions," "a diversity of cultural perspectives") but is **NOT a stated formal requirement** -- **UNCONFIRMED as mandatory.**

### Figures / tables conventions

Springer house style (inherited): **figure captions are placed BELOW the figure; table captions/titles are placed ABOVE the table.** Both are numbered consecutively with Arabic numerals in order of citation. Reused material must "identify previously published material by giving the original source in the form of a reference citation at the end of the figure caption" (and table caption). Resolution norms (general Springer; specific AS restatement **UNCONFIRMED**): line art ~1200 dpi, halftone ~300 dpi, combination ~600 dpi; vector EPS/PDF or raster TIFF preferred; color free online. For double-blind review, figures and supplementary files must be stripped of identifying information. AI-edited images: "The use of non-generative machine learning tools to manipulate, combine, or enhance existing images or figures should be disclosed in the respective figure captions."

### Keyword count

**4 to 6 keywords required:** "Please provide 4 to 6 keywords which can be used for indexing purposes." (Curmudgeon Corner pieces carry no keywords.)

### Length norms (per article type)

- **Research articles: ~10,000 words.**
- **Open Forum: ~8,000 words.**
- **Review articles: ~8,000 words.**
- **Curmudgeon Corner: ~1,000-1,500 words** -- straight essay, no abstract, no keywords, no subsections, **no more than 3 references and no more than 2 co-authors.**
- **Book Reviews: ~1,000-1,500 words.**

Supplementary material / appendices are supported (standard Springer ESM policy) and must also be anonymized for review; the detailed AS-specific supplementary-format policy is **UNCONFIRMED**.

### Required statements / declarations

The journal mandates a **"Statements and Declarations"** section: "The following statements should be included under the heading 'Statements and Declarations' for inclusion in the published paper. Submissions that do not include relevant declarations will be returned as incomplete."

- **Competing Interests (Conflict of Interest):** REQUIRED -- "Author Contribution information and Competing Interest information must be provided at submission via the submission interface." Example wording: "The authors have no competing interests to declare that are relevant to the content of this article." Editorial-board-member authors must declare that status.
- **Author Contributions:** REQUIRED, via the submission interface.
- **Funding:** REQUIRED -- "Funding information (as it is a potential competing interest) needs to be disclosed upon submission... funding information should be included in the 'Declarations' section."
- **Disclosure statement:** "Review articles require a disclosure statement," and other types may depending on content.
- **Ethics approval / IRB & Consent:** Springer Nature research-integrity policy applies (the exact AS restatement of an "Ethics approval" line is **UNCONFIRMED** from the captured page, but it is part of the inherited Statements-and-Declarations block).
- **Data availability / reproducibility:** Springer Data-availability-statement policy applies; data citations require a DOI (the specific AS mandatory data-availability line is **UNCONFIRMED** from the captured page; it is the inherited Springer expectation).
- **AI-use disclosure:** REQUIRED per Springer policy -- "Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript." AI-assisted image manipulation must be disclosed in figure captions; LLMs cannot be authors.
- **Positionality / reflexivity:** NOT a formal declaration requirement -- **UNCONFIRMED as required.**

---

## 3. Published-paper exemplars

> Access caveat: in this session, direct fetching of Springer, DOI resolvers, and the OA mirrors was 403-blocked; characterizations below are reconstructed from search-index snippets (full abstracts, author lists, volume/page data, partial structural descriptions). The four papers are real and verified across multiple independent indexes. Details that could not be confirmed at the verbatim-heading or exact-figure-count level are marked **[INFERRED]** or **[UNCONFIRMED]**. The exemplars were chosen to span the journal's contribution-type range.

**Headline fit finding: LLM / gender-bias / fairness topics are NOT rare in AI & SOCIETY -- they are actively and currently published.** Beyond the four profiled below there is a visible 2025-2026 cluster, e.g. "Algorithmic bias, fairness, and inclusivity: a multilevel framework for justice-oriented AI" (10.1007/s00146-025-02451-2, https://link.springer.com/article/10.1007/s00146-025-02451-2) and "Emerging roles and trends of equity, diversity, and inclusion in AI" (10.1007/s00146-026-02969-z, https://link.springer.com/article/10.1007/s00146-026-02969-z). So the user's GPT-gender-bias topic is a **good topical fit**. The decisive nuance is *flavor*: even the most quantitative AS paper foregrounds social/ethical/sociolinguistic framing rather than benchmarking.

### Exemplar 1 -- the closest analogue (empirical GPT gender-bias audit)

- **Title:** *ChatGPT is a gender bias echo-chamber in HR recruitment: an NLP analysis and framework to uncover the language roots of bias*
- **Authors / year / venue:** Siva Sankari Sivakaminathan & Elena Musi (Univ. Liverpool); AI & SOCIETY Vol. 41, pp. 2841-2861 (2026 print; online 28 Aug 2025).
- **Links:** https://link.springer.com/article/10.1007/s00146-025-02564-8 ; OA PDF https://livrepository.liverpool.ac.uk/3194240/1/ChtGPT_AI_&_SOCIETY.pdf ; https://philpapers.org/rec/SIVCIA
- **Structure & methods:** Mixed-method, quantitatively grounded NLP -- corpus analysis of job descriptions across industries; keyword extraction (target vs. reference corpora), POS tagging of verbs/adjectives, agentic-vs-communal trait coding, and prompt engineering to make ChatGPT screen resumes. Recognizable empirical arc (Intro -> critique of AI-debiasing claims -> methodology -> findings -> discussion -> conclusion); verbatim headings **[UNCONFIRMED]**.
- **Abstract style:** narrative, single-paragraph, unstructured, ~200-230 words, no citations; names the "dual-stage methodological framework combining NLP techniques with prompt engineering."
- **Citations:** Springer author-date **[INFERRED]**. **Hypotheses:** none -- framed as a research question ("does AI mitigate or perpetuate existing gender bias in hiring?"), grounded in gendered-language theory and a critique of the "AI reduces human bias" hype. **Figures/tables:** corpus/keyword/trait tables + a pipeline diagram **[INFERRED; exact counts UNCONFIRMED]**. **Length:** ~21 pages. **Contribution type:** empirical finding **plus** a reusable methodological framework. **Tone:** computational social science / NLP-for-social-critique -- rigorous computation framed as a social-ethical intervention. **This is the single best "what our kind of paper looks like in AS" exemplar.**

### Exemplar 2 -- conceptual / normative critical-theory essay (contrast case)

- **Title:** *Social Bias in AI: Re-coding Innovation through Algorithmic Political Capitalism*
- **Authors / year:** Samuel O. Carter & John G. Dale; online 7 Aug 2025.
- **Links:** https://link.springer.com/article/10.1007/s00146-025-02540-2 ; https://philpapers.org/rec/CARSBI-6
- **Structure & methods:** **No empirical data, no methods section, no statistics, no hypotheses** -- theory-building applying complexity theory (Morcol) and extending Keller & Block's "technology-dependent political capitalism" to algorithmic bias; thematic argument-driven headings **[INFERRED; verbatim UNCONFIRMED]**.
- **Abstract:** narrative single paragraph, ~180-230 words, no citations. **Keywords (confirmed):** Complexity; Complex social systems; Political capitalism; Artificial intelligence; Society; Public policy (6 -- matches the 4-6 rule). **Citations:** Springer author-date **[INFERRED]**. **Figures/tables:** few/none, possibly one conceptual diagram **[UNCONFIRMED]**. **Tone:** critical social theory / political economy / STS. Demonstrates the journal's strong appetite for non-empirical work a pure-CS venue would reject.

### Exemplar 3 -- theory/framework paper (mid-spectrum, HCI/IS)

- **Title:** *Understanding how users may work around algorithmic bias*
- **Authors / year:** Hannah Overbye-Thompson & Ronald E. Rice (UC Santa Barbara); online ~27 Jul 2025.
- **Links:** https://link.springer.com/article/10.1007/s00146-025-02498-1 ; OA https://escholarship.org/uc/item/2fm62554
- **Structure & methods:** **No new empirical data** -- a conceptual framework synthesis: a 2x2 typology of "four epistemic categories of algorithmic bias," the information-systems concept of "workarounds," and the HAII-TIME model (cue routes / action routes). Explicit theory section; no hypotheses. **Abstract:** narrative, ~200 words, no citations. **Citations:** author-date **[INFERRED]**, theory-dense. **Figures/tables:** likely a 2x2 typology and a process model **[INFERRED; UNCONFIRMED]**. **Tone:** HCI / information systems / communication theory -- measured, framework-oriented.

### Exemplar 4 -- systematic review (PRISMA; the "Review" mode)

- **Title:** *Exploring automation bias in human-AI collaboration: a review and implications for explainable AI*
- **Authors / year / venue:** Giuseppe Romeo & Daniela Conti; AI & SOCIETY Vol. 41, pp. 259-278 (Jan 2026 print; online 3 Jul 2025).
- **Links:** https://link.springer.com/article/10.1007/s00146-025-02422-7 ; https://philpapers.org/rec/ROMEAB-2
- **Structure & methods:** **PRISMA 2020 systematic review** -- 35 peer-reviewed studies from SCOPUS/ScienceDirect/PubMed/Google Scholar, Jan 2015-Apr 2025. Standard PRISMA skeleton (Intro -> Methods/search strategy/PRISMA flow -> thematic Findings -> Discussion -> Implications -> Conclusion) **[INFERRED; verbatim UNCONFIRMED]**. **Abstract:** longer narrative single paragraph (~230-260 words) that names the method inside it -- consistent with the up-to-450-word allowance for reporting compliance. **Figures/tables:** PRISMA flow diagram + study-summary table(s) **[INFERRED]**. **Tone:** HCI / cognitive psychology / human-factors. **Length:** ~20 pages.

**Cross-paper patterns:** (1) topic fit is strong; (2) framing flavor (social-science/ethics/critical/HCI) matters more than method; (3) method pluralism is real (empirical, normative, framework, review side by side); (4) abstracts are uniformly narrative, single-paragraph, unstructured, ~180-260 words, no citations; (5) citations are Springer author-date throughout, never numeric/ACM; (6) keywords 4-6; (7) research/review articles run ~20-21 typeset pages; (8) none state formal hypotheses; (9) figure captions below, table captions above.

---

## 4. How it differs from YOUR paper

The user paper is an applied-labor-economics / algorithmic-fairness manuscript in an econometric idiom (OLS linear-probability models, robust SEs, coefficients-as-percentage-points), ~80% empirical, ~15 main pages plus a large appendix, currently on the conservative Public Choice / Motoki-et-al. template. AS would accept the topic but expects a different idiom.

| Dimension | YOUR paper (baseline) | AI & SOCIETY norm | Gap |
|---|---|---|---|
| Discipline / framing | Applied labor economics (Bertrand-Mullainathan audit) + algorithmic fairness; economist's voice; bias = regression outcome variable | Critical / social-science / ethics / STS / HCI; bias = sociotechnical harm with values + theory foregrounded | Large -- reframing, not just edits |
| Template / format | Generic LaTeX article (12pt, a4paper), no journal template | Word or LaTeX `sn-jnl.cls`; single-column double-spaced review copy; decimal headings <=3 levels; **double-blind anonymization required** | Medium (anonymization is a hard, easily-missed gate) |
| Citation style | natbib + apalike, author-date Chicago/APA (citet/citep), ~80-100 refs | Springer "Basic" author-date: `(Author Year)`, no comma, initials no periods, `Volume:pages` colon, DOI as URL | Small-medium (re-style, not re-think) |
| Abstract | ~240 words, two paragraphs, narrative + quantitative, no headings, no hypotheses | Single paragraph, unstructured, 150-250 (up to 450) words, no citations | Small (merge to one paragraph; already no headings) |
| Section structure | Intro -> Lit Review (4) -> Methodology (8, equations in-text) -> Results (Test 1/2/3) -> Conclusion; no Discussion, no H1/H2, no theory section | No IMRaD mandate; theory/conceptual grounding expected; hypotheses not expected; Discussion not mandated but valued for empirical work | Medium -- add explicit theory/framing + Discussion/Implications |
| Methods presentation | OLS LPM, robust SEs, p-values, R^2, coefficients as percentage points, equations in-text, heavy appendix | Empirical-strong welcomed, but mixed-method/computational-social-science idiom; econometric tables tolerated only if narrated for a non-economist reader | Medium-large -- keep rigor, translate it |
| Empirical vs conceptual weight | ~80% empirical | Empirical co-equal with (often subordinate to) theory; pure-conceptual papers thrive | Medium -- rebalance toward framing |
| Tone / voice | Formal, first-person plural, hedged, policy-aware, conservative, reproducibility-heavy | Critical, society-facing, values-first; less leaderboard, more "what does this mean for society" | Medium |
| Length | ~15 pp main + extensive appendix | Research ~10,000 words (~20 pp typeset); appendices as anonymized supplementary material | Small (room to grow main text) |
| Figures/tables | 4 main + 2 detailed reg tables, 10 figures; fig captions below, table captions above | Same caption placement (below/above); fewer dense reg tables, more interpretive figures | Small -- caption convention already matches |
| Contribution type | Empirical finding ("overcorrection"; persistent occupational stereotypes) | Empirical finding co-billed with a reusable framework / conceptual contribution (cf. Exemplar 1) | Medium -- elevate a named framework/concept |

**In prose.** The largest gap is not mechanical but rhetorical. The user paper treats gender bias as an outcome variable measured by regression -- `beta1 = -0.61` reads as "-61 percentage points on P(male character)." AS readers will want that same number, but framed as evidence about a sociotechnical phenomenon (the "overcorrection" of aligned chat models toward pro-female association while occupational stereotypes persist) with explicit engagement of gendered-language / algorithmic-fairness *theory* and the ethical stakes. The closest published analogue (Exemplar 1) keeps real NLP rigor but leads with a critique of the "AI removes bias" narrative and co-bills a *named framework* as a contribution; the user paper currently leads with method and tables. Mechanically, the citation restyle (apalike -> Springer Basic) is light; the abstract needs only to collapse to one paragraph; the figure/table caption convention already matches AS. The genuinely new work is (a) a theory/framing section, (b) a Discussion + Implications section, (c) translating the econometrics for a non-economist audience, and (d) double-blind anonymization plus the full Statements-and-Declarations block (Competing Interests, Author Contributions, Funding, AI-use, data availability).

---

## 5. Fit & recommendation

**Topic and method scope.** The topic is squarely **in scope** -- LLM/GPT gender bias and algorithmic fairness are actively published here (Exemplars 1-3 plus the 2025-2026 fairness cluster). The *method* (OLS linear-probability audit) is also acceptable in principle: AS demands "methodologically sound and empirically strong" work and publishes computational/NLP audits. What is at risk is not admissibility but *register*: a pure econometrics-and-leaderboard presentation would read as out of place. The journal's most quantitative papers wrap their numbers in social-theoretical and ethical framing.

**Fit as-is.** Moderate. The empirical core, the reproducibility apparatus, the author-date citation habit, and even the figure/table caption conventions already align. The mismatches are the missing theory/framing section, the missing Discussion/Implications, the economist-only idiom, and the production gates (anonymization, declarations).

**Specific changes required.** (1) Add an explicit **theory / conceptual-framing section** engaging gendered-language and algorithmic-fairness scholarship, and open by problematizing the "alignment makes models fairer / AI removes bias" narrative -- the "overcorrection" finding is a natural hook. (2) Add a **Discussion + Implications** section (societal, policy, design implications), since the current paper jumps Results -> Conclusion. (3) **Translate the econometrics**: keep the OLS LPM, robust SEs, and percentage-point interpretation, but narrate every coefficient for a non-economist reader and move the densest of the 20+ appendix regressions into anonymized supplementary material. (4) **Co-bill a named contribution** beyond the finding -- e.g. the prompt-based audit pipeline / 896-check reproducibility protocol as a reusable framework (cf. Exemplar 1). (5) **Restyle citations** to Springer "Basic" author-date (`(Author Year)`, no comma; `Volume:pages`; DOIs as URLs). (6) **Collapse the abstract** to a single unstructured paragraph (<=250 words, ideally) with no citations. (7) Expand main text toward **~10,000 words / ~20 pp**. (8) **Anonymize fully** for double-blind review and supply a separate Title Page. (9) Add the **Statements and Declarations** block: Competing Interests, Author Contributions, Funding, AI-use disclosure (document GPT-model usage in Methods), and a data-availability statement -- "Submissions that do not include relevant declarations will be returned as incomplete." (10) Provide **4-6 keywords** (current 5 already complies).

**Adaptation effort rating: MEDIUM.** Justification: the mechanical conversions are light (citation restyle, abstract merge, caption conventions already match, keyword count already compliant, plenty of length headroom). What pushes it above Low is substantive, not formatting: the paper needs a genuinely new theory/framing section, a new Discussion/Implications section, a tone shift from econometric report to society-facing argument, and the elevation of a named framework contribution. None of these require new data, so it stays below High.

**The single most important reframing.** Stop presenting gender bias as an econometric outcome variable and start presenting it as a **sociotechnical phenomenon with ethical and policy stakes** -- lead with the critique that newer "aligned" chat models do not simply reduce bias but *overcorrect* (swinging to pro-female association, `beta ~ -0.61`) while occupational stereotypes persist, and frame the regressions as evidence in that argument rather than as the argument itself.

> **UNCONFIRMED items** (tied only to inherited Springer-wide norms, not the AS page, or not recoverable from blocked PDFs): single-vs-double-column review-PDF requirement; structured-abstract requirement (appears not required); explicit-hypothesis requirement (appears not required); separate Discussion+Implications as a mandate (valued, not mandated); exact figure dpi/format restatement; exact AS wording of the Ethics-approval and Data-availability declaration lines; positionality/reflexivity as a formal requirement; and the verbatim heading lists and exact figure/table counts of all four exemplars.
