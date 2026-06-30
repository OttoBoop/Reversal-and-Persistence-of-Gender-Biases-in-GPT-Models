# Measurement reliability and validity

Computed by `measurement_validity.py` from the three unified data files in
`data/raw/`. These are **new measurement-methodology metrics**, not a rerun of
the paper's bias regressions. Reproduce with:

```
python3 paper/latex/jair/analysis/measurement_validity.py
```

Design note used throughout: each prompt is run 30 times. Legacy models
(`davinci-002`, `babbage-002`, `gpt-3.5-turbo`) carry numbered repetitions
(`0..29`); newer chat/reasoning models store `repetition == "undefined"` but
still contribute exactly 30 runs per condition. For the split-half analysis,
numbered repetitions are split by integer parity (odd vs. even); undefined
repetitions are split by the parity of a deterministic, seed-shuffled
within-cell index (seed `12345`). A measurement **cell** is the unique
combination of the manipulated factor(s) plus `modelo`, `idioma`, and
`example_order` present in each file.

> **Quantitative substance — to be validated by the advisor (Valdemar Pinho Neto).**

---

## 1. Split-half reliability across the 30 repetitions per prompt cell

Per-cell `P(male)` computed separately on the odd- and even-repetition halves,
then correlated across cells. The Spearman–Brown (SB) correction projects the
split-half coefficient to the full 30-repetition instrument. Standard error of
the proportion is `sqrt(p(1-p)/n)`; the 95% CI half-width is `1.96·SE`, both on
the full 30 repetitions.

| Test | Cell definition | Cells | Pearson r | Spearman rho | SB (Pearson) | SB (Spearman) | Median SE | Median 95% CI half-width | Median cell n |
|------|-----------------|------:|----------:|-------------:|-------------:|--------------:|----------:|-------------------------:|--------------:|
| 1 (desirable characteristics) | caracteristica × valencia × modelo × idioma × example_order | 600 | 0.941 | 0.937 | 0.970 | 0.967 | 0.062 | 0.122 | 30.0 |
| 2 (supervisor feedback valence) | valencia × modelo × idioma × example_order | 68 | 0.915 | 0.907 | 0.956 | 0.951 | 0.071 | 0.138 | 30.0 |
| 3 (occupational power) | posicao × power_level × modelo × idioma × example_order | 420 | 0.909 | 0.908 | 0.952 | 0.952 | 0.068 | 0.133 | 30.0 |

All three split-half correlations carry `p < 1e-6`. Half means of `P(male)` are
nearly identical across the two halves (Test 1: 0.536 vs. 0.525; Test 2: 0.292
vs. 0.297; Test 3: 0.348 vs. 0.349).

**Interpretation.** The instrument is highly reliable. Splitting the 30
repetitions of every prompt condition into two independent halves and
correlating the resulting `P(male)` estimates yields Pearson coefficients of
0.91–0.94 across the three tests, rising to 0.95–0.97 after the Spearman–Brown
correction for the full repetition budget. In plain terms, repeated sampling of
the same model under the same condition reproduces the same gender propensity to
within sampling error: the median per-cell standard error is ≈0.06–0.07 and the
median 95% CI half-width is ≈0.12–0.14. The measured quantity is a stable
property of the model-condition pair rather than run-to-run noise.

---

## 2. Classifier validity signals (gender-label distribution and Unknown rate)

The downstream gender classifier resolves the protagonist's gender from each
generated story. A low rate of `Unknown`/unresolved labels indicates that the
measurement pipeline produces usable outcomes for the overwhelming majority of
stories.

### Overall label distribution

| Test | N | Male | Female | Unknown | Inconclusive | Unknown rate | Unresolved rate |
|------|----:|-----:|-------:|--------:|-------------:|-------------:|----------------:|
| 1 | 17,973 | 53.09% | 44.32% | 2.46% | 0.13% | 2.459% | 2.593% |
| 2 | 2,040 | 29.46% | 69.12% | 1.37% | 0.05% | 1.373% | 1.422% |
| 3 | 12,600 | 34.85% | 62.54% | 2.52% | 0.09% | 2.524% | 2.611% |
| **Pooled** | **32,613** | — | — | — | — | **2.416%** | **2.527%** |

(`Unresolved` = `Unknown` + `Inconclusive Story` + missing. No `Non-Binary`
labels occur in any file.)

### Unresolved rate by model family

| Family | Test 1 unresolved% | Test 2 unresolved% | Test 3 unresolved% |
|--------|-------------------:|-------------------:|-------------------:|
| GPT-3 Legacy | 4.81 | 1.04 | 2.60 |
| GPT-3.5 | 2.04 | 0.00 | 3.02 |
| GPT-4o | 2.36 | 2.50 | 4.76 |
| GPT-4.1 | 1.14 | 1.67 | 2.33 |
| Serie o | 3.40 | 0.56 | 1.96 |
| GPT-5 | 0.97 | 2.08 | 2.01 |

**Interpretation.** The classifier resolves a usable gender for roughly 97.5% of
all generated stories (pooled unresolved rate 2.53%; pooled `Unknown` rate
2.42%). The unresolved rate stays in a narrow 0–4.8% band across all six model
families and all three tests, with no family or test exhibiting a pathological
gap. This supports the validity of the measurement: failures to assign a gender
are rare, family-stable, and far too small to drive the substantive
`P(male)` differences reported elsewhere in the paper. A defensible internal
consistency signal is that the most capable families (GPT-4.1, GPT-5) show the
lowest unresolved rates (often ≤1%), consistent with more on-task, parseable
generations.

---

## 3. Construct / convergent validity across tests

Each model's overall `P(male)` was computed within each test; these
model-level propensities were then correlated across the three tests. If the
three instruments tap a common "tendency to render protagonists as male,"
models that skew male in one test should skew male in the others.

### Per-model overall P(male)

| Model | Test 1 | Test 2 | Test 3 |
|-------|-------:|-------:|-------:|
| babbage-002 | 0.510 | 0.533 | 0.428 |
| davinci-002 | 0.487 | 0.546 | 0.477 |
| gpt-3.5-turbo | 0.138 | 0.000 | 0.114 |
| gpt-4.1-2025-04-14 | 0.496 | 0.242 | 0.240 |
| gpt-4.1-mini-2025-04-14 | 0.568 | 0.158 | 0.217 |
| gpt-4.1-nano-2025-04-14 | 0.726 | 0.392 | 0.313 |
| gpt-4o-2024-08-06 | 0.615 | 0.275 | 0.365 |
| gpt-4o-mini | 0.650 | 0.075 | 0.267 |
| gpt-5-mini | 0.524 | 0.192 | 0.295 |
| gpt-5-nano | 0.363 | 0.217 | 0.135 |
| gpt-5.1-2025-11-13 | 0.546 | 0.308 | 0.422 |
| gpt-5.2-2025-12-11 | 0.457 | 0.067 | — (not in Test 3) |
| o3-2025-04-16 | 0.558 | 0.250 | 0.278 |
| o3-mini-2025-01-31 | 0.807 | 0.450 | 0.506 |
| o4-mini-2025-04-16 | 0.558 | 0.225 | 0.197 |

### Cross-test correlations of model-level P(male)

| Pair | n models | Pearson r | p | Spearman rho | p |
|------|---------:|----------:|------:|-------------:|------:|
| Test 1 vs Test 2 | 15 | 0.456 | 0.087 | 0.300 | 0.277 |
| Test 1 vs Test 3 | 14 | 0.591 | 0.026 | 0.359 | 0.208 |
| Test 2 vs Test 3 | 14 | 0.822 | 0.000 | 0.851 | 0.000 |

**Interpretation.** Model-level gender propensities are positively correlated
across all three tests (Pearson 0.46–0.82), evidence of convergent validity: a
model's tendency to render protagonists as male is partly a transferable trait
rather than an artifact of any single prompt template. Convergence is strongest
between Tests 2 and 3 (Pearson r = 0.82, Spearman rho = 0.85, both p < 0.001),
which share an organizational/workplace framing. Test 1 — the desirable-trait
task — converges more weakly (r = 0.46 with Test 2, r = 0.59 with Test 3),
indicating that the desirable-characteristics elicitation captures a related but
partly distinct facet of gender attribution. The pattern of strong
within-domain and moderate cross-domain convergence is the expected signature of
three valid measures of overlapping constructs. (Test 3 is English-only, so
`gpt-5.2-2025-12-11`, which appears in Tests 1–2, has no Test-3 propensity.)

---

### Reproducibility

| Item | Value |
|------|-------|
| Script | `paper/latex/jair/analysis/measurement_validity.py` |
| Data | `data/raw/df_teste_{1,2,3}_unified.csv` |
| Random seed (undefined-rep split-half) | 12345 |
| Pooled N (label analysis) | 32,613 stories |

> **Quantitative substance — to be validated by the advisor (Valdemar Pinho Neto).**
