#!/usr/bin/env python3
"""
Measurement reliability and validity analysis for the JAIR submission.

This script computes NEW measurement-methodology metrics from the existing
experimental data (it is *not* a rerun of the paper's bias regressions):

  1. RELIABILITY across the 30 repetitions per prompt condition
     - split-half reliability (odd vs. even repetition) of P(male) across cells
       reported as Pearson r, Spearman rho, and Spearman-Brown corrected r
     - median per-cell standard error of the proportion and median 95% CI half-width

  2. CLASSIFIER VALIDITY SIGNALS
     - distribution of the gender label overall and by model family
     - rate of Unknown / unresolved labels (low rate -> higher measurement validity)

  3. CONSTRUCT / CONVERGENT VALIDITY across tests
     - per-model overall P(male) in each test, correlated across the three tests

Data files (no API key / network needed):
  data/raw/df_teste_1_unified.csv  (Test 1: desirable characteristics)
  data/raw/df_teste_2_unified.csv  (Test 2: supervisor feedback valence)
  data/raw/df_teste_3_unified.csv  (Test 3: occupational power)

Run:
  python3 paper/latex/jair/analysis/measurement_validity.py
Optional:
  --data-dir DIR   directory holding the three CSVs (default: repo data/raw)
  --out FILE       also write the printed report to FILE
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
from scipy import stats

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

# Family map reused from analysis/scripts/tcc_complete_analysis.py
FAMILY_MAP = {
    'davinci-002': 'GPT-3 Legacy',
    'babbage-002': 'GPT-3 Legacy',
    'gpt-3.5-turbo': 'GPT-3.5',
    'gpt-4o-2024-08-06': 'GPT-4o',
    'gpt-4o-mini': 'GPT-4o',
    'gpt-4.1-2025-04-14': 'GPT-4.1',
    'gpt-4.1-mini-2025-04-14': 'GPT-4.1',
    'gpt-4.1-nano-2025-04-14': 'GPT-4.1',
    'o3-mini-2025-01-31': 'Serie o',
    'o3-2025-04-16': 'Serie o',
    'o4-mini-2025-04-16': 'Serie o',
    'gpt-5-mini': 'GPT-5',
    'gpt-5-nano': 'GPT-5',
    'gpt-5.1-2025-11-13': 'GPT-5',
    'gpt-5.2-2025-12-11': 'GPT-5',
}
FAMILY_ORDER = ['GPT-3 Legacy', 'GPT-3.5', 'GPT-4o', 'GPT-4.1', 'Serie o', 'GPT-5']

DATA_FILES = {
    1: 'df_teste_1_unified.csv',
    2: 'df_teste_2_unified.csv',
    3: 'df_teste_3_unified.csv',
}

# Candidate factor columns that define the manipulated condition per test.
# We only keep those actually present in a given file (robust to header diffs).
FACTOR_CANDIDATES = {
    1: ['caracteristica', 'valencia'],
    2: ['valencia'],
    3: ['posicao', 'power_level'],
}
# Design columns common across tests (kept only if present).
DESIGN_CANDIDATES = ['modelo', 'idioma', 'example_order']

# Labels that count as "resolved" vs "unresolved" for the classifier.
RESOLVED_LABELS = {'Male', 'Female', 'Non-Binary'}
UNRESOLVED_LABELS = {'Unknown', 'Inconclusive Story'}

RANDOM_SEED = 12345


# ----------------------------------------------------------------------------
# Loading / preparation
# ----------------------------------------------------------------------------

def load_test(test: int, data_dir: str) -> pd.DataFrame:
    path = os.path.join(data_dir, DATA_FILES[test])
    df = pd.read_csv(path)
    df['family'] = df['modelo'].map(FAMILY_MAP)
    df['is_male'] = (df['gender'] == 'Male').astype(int)
    # is_resolved: the classifier returned a usable gender label
    df['is_resolved'] = df['gender'].isin(RESOLVED_LABELS).astype(int)
    return df


def cell_columns(df: pd.DataFrame, test: int) -> List[str]:
    """Columns defining a measurement cell (manipulated factor(s) + design),
    using only those present in this file."""
    cols = [c for c in FACTOR_CANDIDATES[test] if c in df.columns]
    cols += [c for c in DESIGN_CANDIDATES if c in df.columns]
    return cols


def assign_half(df: pd.DataFrame, cell_cols: List[str]) -> pd.Series:
    """Assign each row to half A (0) or B (1) by repetition parity.

    Legacy models carry numbered repetitions (0..29); newer models carry the
    string 'undefined'. For numbered reps we use the integer parity directly;
    for undefined reps we assign a deterministic, shuffled within-cell index and
    use its parity. This yields a balanced odd/even split per cell either way.
    """
    rng = np.random.default_rng(RANDOM_SEED)
    rep_str = df['repetition'].astype(str)
    rep_num = pd.to_numeric(rep_str, errors='coerce')

    half = pd.Series(np.nan, index=df.index, dtype='float')

    # Numbered repetitions: parity of integer rep number.
    numbered = rep_num.notna()
    half.loc[numbered] = (rep_num[numbered].astype(int) % 2).astype(float)

    # Undefined repetitions: shuffle within cell, then parity of position.
    undef = ~numbered
    if undef.any():
        sub = df.loc[undef, cell_cols].copy()
        sub['__order'] = rng.random(undef.sum())
        # stable within-cell rank by random order
        sub_sorted = sub.sort_values('__order')
        pos = sub_sorted.groupby(cell_cols, dropna=False).cumcount()
        half.loc[pos.index] = (pos.values % 2).astype(float)

    return half.astype(int)


# ----------------------------------------------------------------------------
# 1. Reliability
# ----------------------------------------------------------------------------

def spearman_brown(r: float, factor: float = 2.0) -> float:
    """Spearman-Brown prophecy for lengthening test by `factor` (=2 for split-half)."""
    if pd.isna(r):
        return float('nan')
    return (factor * r) / (1.0 + (factor - 1.0) * r)


def reliability_for_test(df: pd.DataFrame, test: int) -> Dict:
    cell_cols = cell_columns(df, test)
    df = df.copy()
    df['__half'] = assign_half(df, cell_cols)

    # P(male) per cell per half. Use unstack (NOT pivot_table) so the index is
    # the set of ACTUALLY-OBSERVED cells, not the Cartesian product of factor
    # levels (pivot_table would inflate the row count for multi-factor tests).
    means = df.groupby(cell_cols + ['__half'], dropna=False)['is_male'].mean()
    pivot = means.unstack('__half')
    pivot = pivot.rename(columns={0: 'half_A', 1: 'half_B'})
    for col in ('half_A', 'half_B'):
        if col not in pivot.columns:
            pivot[col] = np.nan

    # total observed cells (full data) and cells with both halves populated
    n_cells_total = df.groupby(cell_cols, dropna=False).ngroups
    valid = pivot.dropna(subset=['half_A', 'half_B'])
    n_cells_used = len(valid)

    a = valid['half_A'].values
    b = valid['half_B'].values

    if n_cells_used >= 3 and np.std(a) > 0 and np.std(b) > 0:
        pearson_r, pearson_p = stats.pearsonr(a, b)
        spearman_rho, spearman_p = stats.spearmanr(a, b)
    else:
        pearson_r = pearson_p = spearman_rho = spearman_p = float('nan')

    sb_pearson = spearman_brown(pearson_r)
    sb_spearman = spearman_brown(spearman_rho)

    # Per-cell SE of the proportion on the FULL 30 reps (not split halves)
    full = (df.groupby(cell_cols, dropna=False)['is_male']
              .agg(['mean', 'size']).reset_index())
    p = full['mean'].values
    n = full['size'].values
    se = np.sqrt(np.clip(p * (1 - p), 0, None) / n)
    ci_half = 1.96 * se

    return {
        'test': test,
        'cell_cols': cell_cols,
        'n_cells_total': n_cells_total,
        'n_cells_used': n_cells_used,
        'half_A_mean': float(np.mean(a)) if n_cells_used else float('nan'),
        'half_B_mean': float(np.mean(b)) if n_cells_used else float('nan'),
        'pearson_r': float(pearson_r),
        'pearson_p': float(pearson_p),
        'spearman_rho': float(spearman_rho),
        'spearman_p': float(spearman_p),
        'sb_pearson': float(sb_pearson),
        'sb_spearman': float(sb_spearman),
        'median_se': float(np.median(se)),
        'mean_se': float(np.mean(se)),
        'median_ci_halfwidth': float(np.median(ci_half)),
        'median_cell_n': float(np.median(n)),
    }


# ----------------------------------------------------------------------------
# 2. Classifier validity signals
# ----------------------------------------------------------------------------

def label_distribution(df: pd.DataFrame) -> Dict:
    overall = df['gender'].value_counts(dropna=False)
    total = len(df)
    overall_pct = (overall / total * 100).round(3)

    unresolved_mask = df['gender'].isin(UNRESOLVED_LABELS) | df['gender'].isna()
    unknown_only_mask = df['gender'] == 'Unknown'

    by_fam = []
    for fam in FAMILY_ORDER:
        sub = df[df['family'] == fam]
        if len(sub) == 0:
            continue
        u = sub['gender'].isin(UNRESOLVED_LABELS) | sub['gender'].isna()
        by_fam.append({
            'family': fam,
            'n': len(sub),
            'male_pct': float((sub['gender'] == 'Male').mean() * 100),
            'female_pct': float((sub['gender'] == 'Female').mean() * 100),
            'unknown_pct': float((sub['gender'] == 'Unknown').mean() * 100),
            'unresolved_pct': float(u.mean() * 100),
        })

    return {
        'total': total,
        'counts': overall.to_dict(),
        'pct': overall_pct.to_dict(),
        'unresolved_rate_pct': float(unresolved_mask.mean() * 100),
        'unknown_rate_pct': float(unknown_only_mask.mean() * 100),
        'by_family': by_fam,
    }


# ----------------------------------------------------------------------------
# 3. Construct / convergent validity across tests
# ----------------------------------------------------------------------------

def model_propensities(dfs: Dict[int, pd.DataFrame]) -> pd.DataFrame:
    """Per-model overall P(male) within each test (resolved-label denominator
    is not used; P(male) over all rows, consistent with the bias outcome)."""
    rows = {}
    for t, df in dfs.items():
        s = df.groupby('modelo')['is_male'].mean()
        rows[f'test{t}'] = s
    out = pd.DataFrame(rows)
    out.index.name = 'modelo'
    return out


def cross_test_correlations(prop: pd.DataFrame) -> List[Dict]:
    pairs = [('test1', 'test2'), ('test1', 'test3'), ('test2', 'test3')]
    results = []
    for x, y in pairs:
        sub = prop[[x, y]].dropna()
        n = len(sub)
        if n >= 3 and sub[x].std() > 0 and sub[y].std() > 0:
            pr, pp = stats.pearsonr(sub[x], sub[y])
            sr, sp = stats.spearmanr(sub[x], sub[y])
        else:
            pr = pp = sr = sp = float('nan')
        results.append({
            'pair': f'{x} vs {y}',
            'n_models': n,
            'pearson_r': float(pr), 'pearson_p': float(pp),
            'spearman_rho': float(sr), 'spearman_p': float(sp),
        })
    return results


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

def fmt(x, nd=3):
    if isinstance(x, float) and (np.isnan(x)):
        return 'nan'
    if isinstance(x, float):
        return f'{x:.{nd}f}'
    return str(x)


def build_report(data_dir: str) -> str:
    lines: List[str] = []
    out = lines.append

    out('=' * 78)
    out('MEASUREMENT RELIABILITY AND VALIDITY  --  JAIR submission')
    out('=' * 78)
    out(f'data_dir = {os.path.abspath(data_dir)}')
    out(f'random seed (undefined-rep split) = {RANDOM_SEED}')
    out('')

    dfs = {t: load_test(t, data_dir) for t in (1, 2, 3)}

    # ---- 1. Reliability ----
    out('-' * 78)
    out('1) SPLIT-HALF RELIABILITY ACROSS THE 30 REPETITIONS PER PROMPT CELL')
    out('-' * 78)
    rel_results = {}
    header = (f'{"test":<6}{"cells":>7}{"used":>6}{"pearson":>9}{"spearman":>10}'
              f'{"SB(pear)":>10}{"SB(spear)":>11}{"med_SE":>9}{"med_CI95":>10}{"med_n":>7}')
    out(header)
    for t in (1, 2, 3):
        r = reliability_for_test(dfs[t], t)
        rel_results[t] = r
        out(f'{t:<6}{r["n_cells_total"]:>7}{r["n_cells_used"]:>6}'
            f'{fmt(r["pearson_r"]):>9}{fmt(r["spearman_rho"]):>10}'
            f'{fmt(r["sb_pearson"]):>10}{fmt(r["sb_spearman"]):>11}'
            f'{fmt(r["median_se"]):>9}{fmt(r["median_ci_halfwidth"]):>10}'
            f'{fmt(r["median_cell_n"],1):>7}')
    out('')
    for t in (1, 2, 3):
        r = rel_results[t]
        out(f'  Test {t} cell = {" x ".join(r["cell_cols"])}')
        out(f'    half-A mean P(male)={fmt(r["half_A_mean"])}, '
            f'half-B mean P(male)={fmt(r["half_B_mean"])}, '
            f'Pearson p={fmt(r["pearson_p"],2 if r["pearson_p"]>=0.01 else 6)}')
    out('')

    # ---- 2. Classifier validity ----
    out('-' * 78)
    out('2) CLASSIFIER VALIDITY SIGNALS (gender-label distribution & Unknown rate)')
    out('-' * 78)
    lab_results = {}
    for t in (1, 2, 3):
        lab = label_distribution(dfs[t])
        lab_results[t] = lab
        out(f'Test {t}: N={lab["total"]}')
        for k in ['Male', 'Female', 'Non-Binary', 'Unknown', 'Inconclusive Story']:
            if k in lab['counts']:
                out(f'    {k:<20}{lab["counts"][k]:>7}  ({fmt(lab["pct"][k],2)}%)')
        out(f'    >> Unknown rate          = {fmt(lab["unknown_rate_pct"],3)}%')
        out(f'    >> Unresolved rate (Unknown+Inconclusive+NaN) = '
            f'{fmt(lab["unresolved_rate_pct"],3)}%')
        out('    by family:')
        out(f'      {"family":<14}{"n":>6}{"male%":>9}{"female%":>9}'
            f'{"unknown%":>10}{"unresolved%":>13}')
        for f in lab['by_family']:
            out(f'      {f["family"]:<14}{f["n"]:>6}{fmt(f["male_pct"],2):>9}'
                f'{fmt(f["female_pct"],2):>9}{fmt(f["unknown_pct"],2):>10}'
                f'{fmt(f["unresolved_pct"],2):>13}')
        out('')

    # Pooled unknown rate across all tests
    all_df = pd.concat([dfs[t][['gender', 'family']] for t in (1, 2, 3)],
                       ignore_index=True)
    pooled_unknown = float((all_df['gender'] == 'Unknown').mean() * 100)
    pooled_unresolved = float(
        (all_df['gender'].isin(UNRESOLVED_LABELS) | all_df['gender'].isna()).mean() * 100)
    out(f'POOLED across tests: N={len(all_df)}, '
        f'Unknown rate={fmt(pooled_unknown,3)}%, '
        f'Unresolved rate={fmt(pooled_unresolved,3)}%')
    out('')

    # ---- 3. Convergent validity ----
    out('-' * 78)
    out('3) CONSTRUCT / CONVERGENT VALIDITY: model-level P(male) across tests')
    out('-' * 78)
    prop = model_propensities(dfs)
    out('Per-model overall P(male):')
    out(f'  {"modelo":<28}{"test1":>8}{"test2":>8}{"test3":>8}')
    for m in prop.index:
        out(f'  {m:<28}{fmt(prop.loc[m,"test1"]):>8}'
            f'{fmt(prop.loc[m,"test2"]):>8}{fmt(prop.loc[m,"test3"]):>8}')
    out('')
    cross = cross_test_correlations(prop)
    out(f'  {"pair":<18}{"n_models":>9}{"pearson_r":>11}{"p":>9}'
        f'{"spearman":>10}{"p":>9}')
    for c in cross:
        out(f'  {c["pair"]:<18}{c["n_models"]:>9}{fmt(c["pearson_r"]):>11}'
            f'{fmt(c["pearson_p"],3):>9}{fmt(c["spearman_rho"]):>10}'
            f'{fmt(c["spearman_p"],3):>9}')
    out('')
    out('=' * 78)
    out('NOTE: Quantitative substance -- to be validated by the advisor '
        '(Valdemar Pinho Neto).')
    out('=' * 78)

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, '..', '..', '..', '..'))
    default_data = os.path.join(repo_root, 'data', 'raw')
    parser.add_argument('--data-dir', default=default_data,
                        help=f'directory with the three CSVs (default: {default_data})')
    parser.add_argument('--out', default=None,
                        help='optional path to also save the printed report')
    args = parser.parse_args()

    if not os.path.isdir(args.data_dir):
        sys.exit(f'data-dir not found: {args.data_dir}')

    report = build_report(args.data_dir)
    print(report)
    if args.out:
        with open(args.out, 'w') as fh:
            fh.write(report + '\n')
        print(f'\n[saved report to {args.out}]')


if __name__ == '__main__':
    main()
