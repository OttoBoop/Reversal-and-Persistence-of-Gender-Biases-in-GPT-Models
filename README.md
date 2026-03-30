# Vies de Genero Paper

This repository consolidates the manuscript, datasets, analysis code, notebook workflow, presentation materials, and supporting files for the paper "Reversal and Persistence of Gender Biases in GPT Models" / "Reversao e Persistencia de Vieses de Genero em Modelos GPT".

## What is here

- `paper/latex/`: Portuguese and English LaTeX sources, bibliography, and figure assets.
- `paper/pdf/`: compiled PDFs and image bundles preserved from the working project.
- `analysis/scripts/`: the main reproducible analysis entrypoint.
- `analysis/notebooks/`: the working notebook used during data generation and exploration.
- `data/raw/`: unified input datasets for the three tests.
- `data/derived/`: main exported regression and proportion tables already included in the project.
- `data/supporting/`: extra tables and supporting summaries.
- `docs/`: cover/support documents.
- `presentations/`: slide decks.
- `archive/`: original source archive kept intact for provenance.

## Key entrypoints

- Portuguese manuscript: `paper/latex/main_portuguese.tex`
- English manuscript: `paper/latex/main_english.tex`
- Analysis script: `analysis/scripts/tcc_complete_analysis.py`
- Main notebook: `analysis/notebooks/march_2026_tcc_publicavel.ipynb`

## Quick start

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the analysis from the repository root:

```bash
python analysis/scripts/tcc_complete_analysis.py
```

By default the script now reads from `data/raw/` and writes regenerated outputs to `analysis/generated/`.

To override paths explicitly:

```bash
python analysis/scripts/tcc_complete_analysis.py \
	--input-dir data/raw \
	--output-dir analysis/generated
```

You can also use environment variables:

```bash
TCC_INPUT_DIR=/path/to/raw TCC_OUTPUT_DIR=/path/to/output python analysis/scripts/tcc_complete_analysis.py
```

## Manuscript notes

- The LaTeX sources expect `figuras_final/` to remain adjacent to the main `.tex` files.
- The repository preserves both manuscript languages and the original bundled zip for archival reference.
- Existing PDFs are treated as preserved artifacts, not rebuilt outputs.

## LaTeX build

The main manuscript entrypoints are:

- `paper/latex/main_portuguese.tex`
- `paper/latex/main_english.tex`

From the repository root, an expected local build command is:

```bash
cd paper/latex
pdflatex main_portuguese.tex
bibtex main_portuguese
pdflatex main_portuguese.tex
pdflatex main_portuguese.tex
```

If `latexmk` is available, the shorter equivalent is:

```bash
cd paper/latex
latexmk -pdf main_portuguese.tex
```

The English manuscript can be built the same way by replacing `main_portuguese.tex` with `main_english.tex`.

## Notebook notes

- The notebook was sanitized before publication: saved outputs and execution counts were removed.
- It still reflects the original Colab and Drive-based workflow, so some paths and API setup are historical rather than plug-and-play.
- Treat the notebook as a research artifact and the script in `analysis/scripts/` as the cleaner rerun path.

## Provenance

The repository was assembled from local working materials including:

- `C:\prova-ai\Working paper data`
- `C:\Users\otavi\Downloads\Copia_de_March_2026_TCC_E_PUBLICAVEL_.ipynb`
- additional supporting files in `C:\Users\otavi\Downloads`

Filenames were normalized where useful for repository readability, but the imported content was not substantively rewritten.