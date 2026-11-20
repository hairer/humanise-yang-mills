# Humanise Yang-Mills

This project coordinates a crowd-sourced effort to turn the announced Lean
formalisation of four-dimensional Yang–Mills theory into a human-readable proof.
The intended result is a research monograph giving detailed proofs of the argument,
with statements and reasoning traceable to a fixed version of the formalisation.
Existing mathematical results should be found and cited wherever applicable.
Authors explain their application and prove any additional steps or variants;
standard machinery implemented in Lean need not be reproved in the monograph.

The current authoritative manuscript is [HumanizeYM_v3](manuscript/HumanizeYM_v3/).
The [monograph PDF](manuscript/HumanizeYM_v3/monograph.pdf) opens with the main
theorem and a guide to its proof.

At this stage, the overall structure of the document is frozen. Anyone is still 
welcome to contribute PRs with improvements to the exposition or to the proof
itself.

**Lean source and dependency mapping.** The
source is pinned to revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464`.
The 17 audited release roots and a first-pass mathematical decomposition are
recorded in the [source audit](source/audit.md), [proof outline](blueprint/outline.md),
and [provisional unit plan](blueprint/unit-plan.md). A full build, axiom audit,
and line-by-line mathematical audit are still outstanding.

## Repository map

| Path | Purpose |
| --- | --- |
| `Lean/` | The upstream formalisation, preserved at a fixed revision |
| `source/` | Source provenance, build instructions, and audit evidence |
| `blueprint/` | Interfaces, literature notes, source correspondence, and review records |
| `manuscript/HumanizeYM_v3/` | Current authoritative manuscript, LaTeX sources and compiled PDF |
| `Bots/` | Durable discoveries and handoffs for future sessions |
| `templates/` | Proof unit and review templates |
| `docs/` | Contributor, coordinator, and mathematical review guidance |
| `scripts/` | Small structural checks, with no third-party Python dependencies |

The Lean source, proof map, and English exposition have separate roles. Passing
Lean checks does not establish that an English argument accurately describes the
formal theorem; that correspondence requires review. See Lean's
[proof validation guidance](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).

## Prior dependency mapping

The initial source clustering and much of the navigation data used by this
repository come from Scott Armstrong's
[Yang-Mills informalization project](https://github.com/scottnarmstrong/yang-mills-informalization).
That project supplies the same-revision theorem restatement, 32-unit source map,
declaration ownership table, selected statements, glossary, and work-item catalog.
This repository's first-pass monograph outline adapts that work into proposed
mathematical proof units; it does not claim the underlying mapping as original.
See the [pinned attribution and methodological limits](blueprint/outline.md#evidence-used-for-this-map).

## Licence

Except where another notice applies, original material in this repository is
licensed under the [Creative Commons Attribution 4.0 International
licence](LICENSE). The imported formalisation under `Lean/` retains its separate
[upstream licence](Lean/LICENSE) and other notices; the root licence does not
relicense that third-party material.
