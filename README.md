# Vies de Genero Paper

This repository contains the paper, final datasets, reproducible notebook, generated tables, generated figures, and audit materials for **"Reversal and Persistence of Gender Biases in GPT Models"**.

## Start Here: PDFs For Human Review

The PDFs at the repository root are the main review artifacts. Start with these before looking at LaTeX sources.

- [paper_full_english.pdf](paper_full_english.pdf): full English paper PDF.
- [paper_abstract_rethink_ai_ethics.pdf](paper_abstract_rethink_ai_ethics.pdf): one-page abstract/resumo PDF.

The LaTeX files are kept for source editing and rebuilding, but the PDF files above are the practical entry point for human revision.

## Main Reproducibility Notebook

- [analysis/notebooks/replicate_gender_bias_paper.ipynb](analysis/notebooks/replicate_gender_bias_paper.ipynb): new reproducible notebook for peer review.
- [docs/plano_notebook_replicavel.md](docs/plano_notebook_replicavel.md): living implementation and audit plan.
- [analysis/notebooks/march_2026_tcc_publicavel.ipynb](analysis/notebooks/march_2026_tcc_publicavel.ipynb): historical working notebook kept for provenance, not the recommended entry point.

The new notebook is saved with `RUN_MODE = "analysis_only"` by default. In that mode it uses the final CSVs in `data/raw/`, does not need an API key, and regenerates/audits the paper outputs under `analysis/generated/notebook_analysis/`.

Current analysis-only coverage:

- compares regenerated outputs with `data/derived/`: 9/9 passing;
- compares regenerated outputs with `data/supporting/`: 4/4 passing;
- audits paper and appendix LaTeX tables/results: 35/35 blocks and 896/896 numeric checks passing;
- audits paper figures: 10/10 figures, 68 plotted bars, and 272 numeric checks passing;
- preserves the one documented non-substantive LaTeX exception for the `appendix_t1_chat_simple` intercept t-statistic instead of changing the paper silently.

The notebook also includes optional `dry_run` and `smoke` modes for small API-boundary tests. Those modes write only to `analysis/generated/test_runs/` and do not overwrite `data/raw/`, `data/derived/`, or `data/supporting/`.

## Repository Map

- `data/raw/`: final unified CSVs for Tests 1, 2, and 3.
- `data/derived/`: main exported regression and proportion tables included in the project.
- `data/supporting/`: supporting tables and summaries.
- `analysis/notebooks/`: reproducibility notebook and historical notebook.
- `analysis/scripts/`: script-based analysis entrypoint preserved from the project.
- `analysis/generated/`: regenerated outputs, audit reports, figures, and local test runs.
- `paper/latex/`: English and Portuguese LaTeX sources, bibliography, and figure assets.
- `paper/pdf/`: older or preserved PDF artifacts from the working project.
- `docs/`: living plan and submission/support documents.
- `presentations/`: slide decks.
- `archive/`: original source archive kept intact for provenance.

## Quick Start

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Open and run the main notebook:

```text
analysis/notebooks/replicate_gender_bias_paper.ipynb
```

For a non-interactive check from the repository root, run the notebook with `nbclient` in an environment that has `requirements.txt` installed. The default `analysis_only` path should complete without an OpenAI API key.

## LaTeX Sources

The main manuscript sources are:

- `paper/latex/main_english.tex`
- `paper/latex/appendix.tex`
- `paper/latex/main_portuguese.tex`

The English PDF at the repository root was copied from `paper/latex/main_english.pdf`. Rebuild LaTeX only when editing the manuscript source; for review, use the root PDFs first.

## Provenance

The repository was assembled from local working materials, including:

- `C:\prova-ai\Working paper data`
- `C:\Users\otavi\Downloads\Copia_de_March_2026_TCC_E_PUBLICAVEL_.ipynb`
- additional supporting files in `C:\Users\otavi\Downloads`

Filenames were normalized where useful for repository readability, but the imported content was not substantively rewritten unless documented in the living plan.
