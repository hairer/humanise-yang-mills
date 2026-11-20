# Monograph project

Start with [the master blueprint](BLUEPRINT.md). Its chapter specifications, shared notation and source packets are intended to let a writer work on one chapter without rereading the other manuscripts.

The supplied sources are preserved unchanged. Work in this directory is an editorial and mathematical reconstruction of those sources, not an independent certification of their full existence theorem. The chapter audits distinguish checked arguments, imported standard results, and source-specific obligations still to be matched.

## Working files

- `BLUEPRINT.md`: reading order, page allocation, dependencies and writing assignments.
- `PROGRESS.md`: current drafting status and precise continuation priorities.
- `blueprint/editorial-contract.md`: mathematical and editorial rules for every writer.
- `blueprint/notation.md`: shared symbols and source-to-book translation.
- `blueprint/foundations-chapters.md`, `uv-chapters.md`, `continuum-chapters.md`: detailed chapter specifications and bounded reading packets.
- `blueprint/*-audit.md`: source comparisons and unresolved hypothesis matching.
- `blueprint/source-index.json` and `source-index.md`: all headings and labels in 312 supplied LaTeX files, with snapshot line numbers and file hashes in the JSON.
- `blueprint/scott-trish-comparison.md`: comparison locating the substantive differences between the two similar manuscripts.
- `chapters/`: book text and included proof fragments.
- `audit/`: chapter-specific source checks and independent mathematical reviews.
- `monograph.tex`, `preamble.tex`, `references.bib`: standalone LaTeX build.

Find a source assertion without reading the entire manuscript:

```sh
python3 Output/tools/source_excerpt.py prop:restart-actual-closure --context 180
```

From this directory, build the book with:

```sh
python3 tools/check_draft.py
python3 tools/collect_references.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build monograph.tex
```

The most recently reviewed draft PDF is copied to `monograph.pdf`; build logs and rendered review images stay in `build/`. The current source covers all nineteen planned chapters, including the current-transfer and arbitrary-radius estimates. The delivered PDF is 271 pages. Pages i–ii state the main theorem and point to the proofs of its parts. Consult `PROGRESS.md` for the final review record and the scope of the claims.
