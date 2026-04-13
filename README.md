# Reversal and Persistence of Gender Biases in GPT Models

This repository is organized for human review of the working paper and for reproducing its tables, metrics, and figures from the final CSVs.

## Paper PDFs

Start here:

- [paper_full_english.pdf](paper_full_english.pdf): full English working paper.
- [paper_appendix_english.pdf](paper_appendix_english.pdf): English appendix.

The LaTeX source is available in `paper/latex/`, but the PDFs above are the review entry points.

## Reproducibility Notebook

Use this notebook:

- [analysis/notebooks/replicate_gender_bias_paper.ipynb](analysis/notebooks/replicate_gender_bias_paper.ipynb)

This is the new peer-review notebook. It is saved in `RUN_MODE = "analysis_only"` by default, so it does not need an OpenAI API key. In that mode it reads the final CSVs, regenerates the paper tables and figures, and writes audit reports under `analysis/generated/notebook_analysis/`.

Current validation status:

- `data/derived`: 9/9 regenerated files match.
- `data/supporting`: 4/4 regenerated files match.
- Paper/appendix table audit: 35/35 LaTeX result blocks pass, with 896/896 numeric checks.
- Figure audit: 10/10 paper figures pass, with 68 plotted bars and 272/272 numeric checks.
- One non-substantive historical exception is documented: the intercept t-statistic in `appendix_t1_chat_simple`; the coefficient, standard error, N, R2, p-value, and substantive regressor all match.

Historical notebook, kept only for provenance:

- [analysis/notebooks/march_2026_tcc_publicavel.ipynb](analysis/notebooks/march_2026_tcc_publicavel.ipynb)

## Final Data

The final unified CSVs used by the paper are:

- [data/raw/df_teste_1_unified.csv](data/raw/df_teste_1_unified.csv)
- [data/raw/df_teste_2_unified.csv](data/raw/df_teste_2_unified.csv)
- [data/raw/df_teste_3_unified.csv](data/raw/df_teste_3_unified.csv)

These are the canonical data files for reproducing the paper results. The notebook can also run small API smoke tests, but those runs are optional and do not replace the final CSVs.

## Original Results And Figures

Original exported result tables:

- [data/derived/](data/derived/)
- [data/supporting/](data/supporting/)

Original paper figures used by LaTeX:

- [paper/latex/figuras_final/](paper/latex/figuras_final/)

Regenerated outputs from the reproducibility notebook:

- [analysis/generated/notebook_analysis/](analysis/generated/notebook_analysis/)
- [analysis/generated/notebook_analysis/figures/](analysis/generated/notebook_analysis/figures/)
- [analysis/generated/notebook_analysis/latex_audit/](analysis/generated/notebook_analysis/latex_audit/)
- [analysis/generated/notebook_analysis/figure_audit/](analysis/generated/notebook_analysis/figure_audit/)

## Source Files

Manuscript source:

- [paper/latex/main_english.tex](paper/latex/main_english.tex)
- [paper/latex/appendix.tex](paper/latex/appendix.tex)

Project plan and audit log:

- [docs/plano_notebook_replicavel.md](docs/plano_notebook_replicavel.md)

The Portuguese LaTeX version is preserved in the repository, but the current review target is the English paper plus appendix.
