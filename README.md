# Reversal and Persistence of Gender Biases in GPT Models

This repository contains the paper PDFs, final data, reproducibility notebook, original result tables, paper figures, and audit outputs for the working paper.

## Paper PDFs

Start with the PDFs in the repository root:

- [paper_full_english.pdf](paper_full_english.pdf): full English working paper.
- [paper_appendix_english.pdf](paper_appendix_english.pdf): English appendix.
- [paper_full_portuguese.pdf](paper_full_portuguese.pdf): Portuguese version preserved as a single paper PDF.

The LaTeX source is available in `paper/latex/`, but these PDFs are the review entry points.

## Reproducibility Notebook

Use this notebook to reproduce the paper tables, metrics, and figures from the final CSVs:

- [analysis/notebooks/replicate_gender_bias_paper.ipynb](analysis/notebooks/replicate_gender_bias_paper.ipynb)

The notebook is saved in `RUN_MODE = "analysis_only"` by default. This mode does not need an OpenAI API key. It reads the final CSVs in `data/raw/`, regenerates the analytical outputs, and writes audit reports under `analysis/generated/notebook_analysis/`.

Current validation status:

- `data/derived`: 9/9 regenerated files match.
- `data/supporting`: 4/4 regenerated files match.
- Paper/appendix table audit: 35/35 LaTeX result blocks pass, with 896/896 numeric checks.
- Figure audit: 10/10 paper figures pass, with 68 plotted bars and 272/272 numeric checks.
- One non-substantive historical exception is documented: the intercept t-statistic in `appendix_t1_chat_simple`; the coefficient, standard error, N, R2, p-value, and substantive regressor all match.

The notebook also contains optional small API test modes. Those runs are for checking the generation/classification pipeline and do not replace the final CSVs.

## Final Data

The final unified CSVs used by the paper are:

- [data/raw/df_teste_1_unified.csv](data/raw/df_teste_1_unified.csv)
- [data/raw/df_teste_2_unified.csv](data/raw/df_teste_2_unified.csv)
- [data/raw/df_teste_3_unified.csv](data/raw/df_teste_3_unified.csv)

These are the canonical data files for reproducing the paper results.

## Original Results And Figures

Original exported result tables:

- [data/derived/](data/derived/)
- [data/supporting/](data/supporting/)

Original paper figures used by LaTeX:

- [paper/latex/figuras_final/](paper/latex/figuras_final/)

## Regenerated Outputs And Audits

The reproducibility notebook writes regenerated outputs here:

- [analysis/generated/notebook_analysis/](analysis/generated/notebook_analysis/)
- [analysis/generated/notebook_analysis/figures/](analysis/generated/notebook_analysis/figures/)
- [analysis/generated/notebook_analysis/latex_audit/](analysis/generated/notebook_analysis/latex_audit/)
- [analysis/generated/notebook_analysis/figure_audit/](analysis/generated/notebook_analysis/figure_audit/)

## Extra References

For historical notebooks, LaTeX source files, older PDFs, presentations, and archive notes, see:

- [docs/extra_references.md](docs/extra_references.md)
