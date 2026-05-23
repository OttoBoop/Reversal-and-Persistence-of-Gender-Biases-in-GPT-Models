# Makefile for Vies_de_Genero_Paper
#
# Builds the LaTeX sources in paper/latex/ and copies the resulting PDFs to the
# repo root, where they are tracked as the "shareable" versions. Avoids the
# drift that happened in May/2026 where root-level PDFs sat at April-12 while
# paper/latex/ had moved forward.
#
# Usage:
#   make english   # build main_english.pdf + copy to paper_full_english.pdf
#   make appendix  # build appendix.pdf + copy to paper_appendix_english.pdf
#   make all       # both above
#   make clean     # latexmk -C in paper/latex/ (removes aux files, keeps PDFs)
#   make distclean # also removes the copied root PDFs
#
# Notes:
# - We do NOT touch main_portuguese.tex (PT version is deferred per the
#   long-term plan).
# - latexmk -pdf -g forces a full rebuild every invocation; -interaction=
#   nonstopmode makes errors non-blocking in CI-like flows.

LATEX_DIR := paper/latex
LATEXMK := latexmk -pdf -g -interaction=nonstopmode

.PHONY: all english appendix clean distclean help

all: english appendix

english:
	cd $(LATEX_DIR) && $(LATEXMK) main_english.tex
	cp $(LATEX_DIR)/main_english.pdf paper_full_english.pdf
	@echo "[ok] paper_full_english.pdf refreshed"

appendix:
	cd $(LATEX_DIR) && $(LATEXMK) appendix.tex
	cp $(LATEX_DIR)/appendix.pdf paper_appendix_english.pdf
	@echo "[ok] paper_appendix_english.pdf refreshed"

clean:
	cd $(LATEX_DIR) && latexmk -C
	@echo "[ok] aux files cleaned (PDFs in $(LATEX_DIR)/ preserved)"

distclean: clean
	rm -f paper_full_english.pdf paper_appendix_english.pdf
	@echo "[ok] root-level PDFs removed"

help:
	@echo "make english   - build main_english.pdf and copy to root"
	@echo "make appendix  - build appendix.pdf and copy to root"
	@echo "make all       - both above"
	@echo "make clean     - remove aux files but keep PDFs"
	@echo "make distclean - clean + remove root PDFs"
