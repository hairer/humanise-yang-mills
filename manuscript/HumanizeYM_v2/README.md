# HumanizeYM_v2

HumanizeYM_v2 is a 306-page, AI-assisted working manuscript, submitted for
discussion by Trishen Gunaratnam. It gives a conditional construction from
Wilson's lattice model and documents several checked local repairs. Its main
construction still depends on the estimates listed in the opening proof-status
section and at their uses in the proof. See [Proof status](PROOF-STATUS.md).

- [Manuscript PDF](HumanizeYM_v2.pdf)
- [LaTeX entry point](main.tex)
- [Source attribution and licenses](ATTRIBUTION.md)

Build from this directory with a LaTeX distribution, BibTeX and TikZ.

    latexmk -pdf -jobname=HumanizeYM_v2 -halt-on-error main.tex

`source-sha256.json` records all 31 TeX inputs and the bibliography. The checked
PDF has SHA-256 `8695468ab2164a365597b8b5628d5f6ea5da3c27760347b5844c99d56d02b4e0`.
