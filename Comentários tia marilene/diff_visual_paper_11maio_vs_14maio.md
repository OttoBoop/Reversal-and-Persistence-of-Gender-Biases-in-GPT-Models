# Diff visual do paper — snapshot 11/05 vs. versão de 14/05

Gerado em 2026-05-14 para acelerar a revisão manual do Otávio. Compara o snapshot histórico tirado antes das edições (`archive/snapshot_2026-05-11/paper_full_english.pdf`) com a versão fresca atual (`paper_full_english.pdf` na raiz).

**Resumo numérico**: paper passou de 34 → 34 páginas (compactação dos listings absorveu a página extra do B1). PDF era 1.38 MB, agora 1.40 MB. 10 trechos modificados + 2 parágrafos novos + 1 footnote.

Os PDFs estão lado-a-lado em:
- Antes: [archive/snapshot_2026-05-11/paper_full_english.pdf](../archive/snapshot_2026-05-11/paper_full_english.pdf)
- Depois: [paper_full_english.pdf](../paper_full_english.pdf)

---

## 1. Intro § 1 — Expansão de "LLM" (atende #3)

**Antes**:
> Bias problems in artificial intelligence systems are not new and predate the popularization of **LLMs**.

**Depois**:
> Bias problems in artificial intelligence systems are not new and predate the popularization of **Large Language Models (LLMs)**.

---

## 2. Intro § 2 — Citação Obermeyer verbatim + página (atende #4)

**Antes**:
> Regarding the origin of the disparity in care recommended to Black and white patients, **OBERMEYER et al. conclude**: *"This bias arises because the algorithm predicts health costs and not illness, but unequal access to the health system means that less money is spent on Black patients"*.

**Depois**:
> Regarding the origin of the disparity in care recommended to Black and white patients, **OBERMEYER et al. (2019, p. 447) conclude**: *"The bias arises because the algorithm predicts health care costs rather than illness, but unequal access to care means that we spend less money caring for Black patients than for White patients"*.

Cinco mudanças na citação (verbatim do abstract do Science 366):
- `This bias` → `The bias`
- `health costs and not illness` → `health care costs rather than illness`
- `unequal access to the health system` → `unequal access to care`
- `less money is spent on Black patients` → `we spend less money caring for Black patients than for White patients`
- Adicionado `(2019, p. 447)` na atribuição

---

## 3. Intro § 3 — C2: três aims + dois eixos transversais (atende #5)

**Antes** (texto pula direto para a descrição dos testes):
> ...and then analyzing the gender of the generated characters. The first test consists of asking the model...

**Depois** (frase nova inserida entre o método geral e o detalhe dos testes):
> ...and then analyzing the gender of the generated characters. **More precisely, we pursue three empirical aims: to measure how desirable workplace characteristics, the valence of supervisor feedback, and occupational power-level cues each shape the gender of model-generated characters. We also examine two cross-cutting axes: the evolution of bias across three model generations (GPT-3, GPT-4, GPT-5) and, for the first two experiments, the role of language (English vs. Portuguese).** The first test consists of asking the model...

---

## 4. Literature Review — Sigla BERT expandida (sweep)

**Antes**: `word representations in BERT and GPT-2`

**Depois**: `word representations in Bidirectional Encoder Representations from Transformers (BERT) and GPT-2`

---

## 5. Literature Review — Sigla RLHF acrescentada (sweep)

**Antes**: `extensive use of Reinforcement Learning from Human Feedback, where`

**Depois**: `extensive use of Reinforcement Learning from Human Feedback (RLHF), where`

---

## 6. Literature Review — Liu 2025 BiasUnlearn (citation audit)

**Antes**:
> \citet{liu2025} directly address the risk of overcorrection in their framework *"Bias Unlearn"* — proposing an *"unlearning"* method that removes stereotyped associations while avoiding creating the inverse bias.

**Depois**:
> \citet{liu2025} directly address the risk of overcorrection in their **\textit{BiasUnlearn}** framework — an unlearning method that removes stereotyped associations while avoiding creating the inverse bias.

Motivo: nome correto do framework é `BiasUnlearn` (uma palavra), e `unlearning` é nome do método deles, não termo a colocar entre aspas.

---

## 7. Methodology §3.1 General — i.i.d. expandido (atende #24)

**Antes**:
> we obtain a set of **identically distributed** random variables, and the behavior of these **i.i.d.** variables reveals the model's latent biases.

**Depois**:
> we obtain a set of **independent and identically distributed (i.i.d.)** random variables, and the behavior of these **i.i.d.** variables reveals the model's latent biases.

---

## 8. Methodology §3.2 — Capitalização "Good Leadership" (atende #29)

**Antes**: `"Poor Leadership"`, and for the positive valence, `"good leadership"`.

**Depois**: `"Poor Leadership"`, and for the positive valence, `"Good Leadership"`.

---

## 9. Methodology — Prompts em PT com acentos (atende #30/#34)

Três listings foram corrigidos. Aqui o exemplo da Listing 19 (Classification PT) — o resto segue mesmo padrão:

**Antes** (sem acentos):
```
"Classifique o genero do personagem principal como Homem, Mulher, Nao-Binario...
Forneca uma explicacao curta baseada em pronomes... mencoes explicitas ao seu
genero, ANTES de chegar na sua conclusao. Note que para a classificacao 'nao
binario' e chave que o texto explicite este fato. Alem disso... portugues
possuem generos explicitos. Voce pode classificar... mas isto so deve acontecer
nas circunstancias mais raras, e requer uma explicacao completa... estarao
acompanhados de pronomes de genero, permitindo sua classificacao entre as
outras opcoes. Leia a historia abaixo: ```{story}```"
```

**Depois** (com acentos, fiel aos prompts produção no `analysis/generated/test_runs/.../jsonl`):
```
"Classifique o gênero do personagem principal como Homem, Mulher, Não-Binário...
Forneça uma explicação curta baseada em pronomes... menções explícitas ao seu
gênero, ANTES de chegar na sua conclusão. Note que para a classificação 'não
binário' é chave que o texto explicite este fato. Além disso... português
possuem gêneros explícitos. Você pode classificar... mas isto só deve acontecer
nas circunstâncias mais raras, e requer uma explicação completa... estarão
acompanhados de pronomes de gênero, permitindo sua classificação entre as
outras opções. Leia a história abaixo: ```{story}```"
```

Foi necessário também adicionar `extendedchars=true` + um bloco `literate` ao `\lstset` para o pacote `listings` digerir UTF-8 dentro de listings — sem isso, o compile falhava com `Invalid UTF-8 byte sequence`.

---

## 10. Methodology §3.5 (Gender Determination) — API + footnote temperature (atende #42)

**Antes**:
> we made a **second API call** to determine the gender... gpt-4o-mini was used, with **temperature set to 1**.

**Depois**:
> we made a **second Application Programming Interface (API) call** to determine the gender... gpt-4o-mini was used, with temperature set to 1.¹
>
> ¹ *The temperature parameter scales the model's output distribution at inference time: values near 0 yield nearly deterministic outputs, while higher values produce more diverse generations. Generation parameters are discussed in detail in Section 3.7.*

---

## 11. Methodology §3.6 (Econometric Specification) — Frente B1: dois parágrafos novos no topo

Antes do `\subsection{Econometric Specification}` ir direto pro "For each test, we estimated linear regressions (OLS) with the following general structure", agora tem dois parágrafos novos:

> **We adopt Ordinary Least Squares (OLS) linear regression as our main analytical tool for two reasons. First, regression isolates the effect of each experimentally manipulated treatment — the desirable characteristic in Test 1, the valence of supervisor feedback in Test 2, and the occupational power level in Test 3 — from confounders such as the specific model in use, the language of the prompt, and, for completion models, the order of examples in the few-shot context. Second, the regression framework supports standard statistical inference and enables the robustness checks reported in the appendix.**
>
> **Because our outcome variable is binary (whether the generated character is male), the linear-probability formulation yields coefficients that map directly to differences in probabilities. A β₁ of −0.61 in the desirable-characteristics test, for instance, indicates that switching the prompt from a negative to a positive valence reduces the probability of generating a male character by 61 percentage points, all else equal. This econometric approach follows that of MOTOKI et al. (2024) in their study of political bias in large language models.**

Em seguida, a frase original foi tightenada (não repete "OLS linear regressions" pela segunda vez):

**Antes**: `For each test, we estimated linear regressions (OLS) with the following general structure:`
**Depois**: `For each test, the OLS regression takes the following general structure:`

---

## 12. Apêndice — Siglas

**Antes** (l.229): `U.S. legislation in EEOC, CM-625`
**Depois**: `U.S. legislation in Equal Employment Opportunity Commission (EEOC) document CM-625`

**Antes** (l.148): `Machine Learning models in general`
**Depois**: `Machine Learning (ML) models in general`

---

## 13. Layout: visual dos prompts (frente B4)

Não dá pra mostrar em diff textual. Mudanças no `\lstset`:
- `breakatwhitespace=true` — palavras inteiras preservadas, não quebra mais em "caracter / ística"
- `basicstyle=\ttfamily\footnotesize` (era `\small`) — caixa mais compacta
- `framerule=0.4pt`, `rulecolor=gray!50` — borda mais fina e clara
- `aboveskip=4pt`, `belowskip=4pt`, `framesep=4pt` — padding apertado
- Resultado: o paper voltou de 35 → 34 páginas após o B4

---

## TODOs deixados para o Otávio decidir (descobertos na auditoria de citações)

Estão como `% TODO (audit-2026-05-14): ...` no `.tex`. Grep para localizar:

```bash
grep -n "TODO (audit-2026-05-14)" paper/latex/main_english.tex
```

Há **2 ocorrências** (linhas ~125 e ~185), ambas sobre atribuição de terminologia ("different levels of power" / "High Power" / "Low Power") a Lucy & Bamman (2021). Detalhes na entrada 20 do log.

Lucy & Bamman não usa essas labels capitalizadas; usa "high power verbs" e lexicons de Fast et al. (2016b). Decisão de prosa cabe a você.

---

## O que NÃO mudou

- Conclusion (mantida na íntegra)
- Tabelas (incluindo `\caption` que já estava acima das tabelas, padrão Springer)
- Figuras (gráficos) e seus `\caption{}` (já abaixo, padrão Springer)
- Bibliografia (`referencias.bib`)
- Versão portuguesa (`main_portuguese.tex` / `paper_full_portuguese.pdf`) — adiada por design no plano D
- Conteúdo substantivo de resultados/regressões

---

## Frentes ainda em aberto

Nenhuma frente ativa. O paper está, pelo meu lado, **pronto para a revisão manual do Otávio**. Itens que requerem decisão dele estão marcados como TODO no `.tex`, listados em entrada 20 do log.
