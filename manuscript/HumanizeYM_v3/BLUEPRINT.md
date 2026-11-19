# Blueprint for a monograph on the four-dimensional Yang–Mills construction

## Editorial objective

Produce a single logical account of the construction described in the supplied Martin, Trish and Scott manuscripts. The initial map is Scott's `Outline`, with Martin used for detailed arguments and Trish used both for alternative explanations and for its explicit qualifications. The target is **450 pages**, including 16 pages for front matter, references and notation. Standard arguments are cited, not expanded merely to fill the allocation. The first full draft occupies **265 pages**; the allocations remain ceilings for revision.

The book concerns gauge-invariant local correlations, their ordered continuum limits and phasewise relativistic reconstruction. It is not a proof of a mass gap. The source claims are to be checked at their actual hypotheses; this blueprint does not certify all of them. See the audit files for the distinction between missing exposition, a candidate repair elsewhere in the sources, and an argument not yet checked.

## How to write one chapter independently

1. Read [the editorial contract](blueprint/editorial-contract.md) and the relevant rows of [the notation registry](blueprint/notation.md).
2. Read the chapter's specification below: its required inputs are the only earlier results it may assume. Its outputs are the contract with later chapters. A theorem contract is not permission to assume its truth without proof or an explicit conditional designation.
3. Open its bounded source packet by path and LaTeX label. The [source index](blueprint/source-index.md) gives locations; `tools/source_excerpt.py` retrieves labelled passages. Most Scott–Trish text is close; use [the comparison](blueprint/scott-trish-comparison.md) to identify where reading both adds value.
4. Check the original literature before including a proof. Follow the [literature policy](blueprint/literature-policy.md) and record the actual theorem and hypothesis match in the chapter's audit.
5. Deliver `chapters/NN-short-title.tex` and an audit note. Do not silently change a shared symbol, normalization, constant dependence, or the family to which an imported result applies.

## Implemented dependency refinement

The original chapter allocation below remains a ceiling, rather than a request to fill pages. In the working draft, Chapter 13 also contains the sharp fixed-arity bounds, bounded real approximations, graded quotient estimate and mixed local cluster replacement. The latter is the lattice/probe part of Scott `part2/J-section.tex:17–414`, followed by its fixed-spectator consequence. It uses Chapters 10–13 only. Chapter 14 uses it to prove the annular annihilator bound with error `r^(1−epsilon)`, before phases or rotations have been constructed. Chapter 18 then converts the same lattice estimate to a phase-uniform norm estimate and the fixed OPE prescription. Do not duplicate the local cluster proof there or introduce a backward dependency through phase decomposition.

The three-scale free comparison is proved in `chapters/14-lattice-comparison.tex` using the fixed-arity export of Chapter 11; its source packet is Scott `part2/G-section.tex:223–310`. Chapter 11's polynomial extraction must be common to all three scales and all spectators. At each scale use its own normalized singleton, then compare them by the exact scaling-dimension dilation.

Proof fragments are included by the master chapter files. Their historical filename or label prefix need not equal their current chapter number: `18-graded-quotient.tex` and `18-lattice-products.tex` belong in Chapter 13. Follow `monograph.tex` and its actual inputs. `tools/check_draft.py` checks that input graph and reports unattached fragments, so a label in an unintegrated file cannot conceal a missing reference.

The current Chapter17 includes a proved comparison over windows crossing arbitrarily many stages (`17-variable-windows.tex`). Its per-step constants must be selected before the stage block ratio; constants depending on that ratio belong only to delayed local errors and bounded endpoint factors. The low-moment estimate for spatial remainders in `17-marked-trace-rates.tex` is now proved using the exact polynomial-preserving smooth response and normalized Gaussian fluctuation gain. A vanishing scaling-dimension jet alone does not give an extra field-amplitude factor. Chapter19 separates the trace conclusion from the construction and finite-order OPE to display its additional dependencies. See the final resolution sections of the Chapter17 audits.

## Chapters and page allocation

| Ch. | Title | Pages | Detailed writing instructions |
|---|---|---:|---|
| 1 | Lattice gauge theory and the continuum problem | 18 | [Foundations, Chapter 1](blueprint/foundations-chapters.md) |
| 2 | Local gauge-invariant observables | 16 | [Foundations, Chapter 2](blueprint/foundations-chapters.md) |
| 3 | The free Maxwell comparison theory | 20 | [Continuum C1](blueprint/continuum-chapters.md) |
| 4 | Exact blocking and effective densities | 18 | [UV U2](blueprint/uv-chapters.md) |
| 5 | Gaussian kernels and stationary backgrounds | 26 | [UV U3](blueprint/uv-chapters.md) |
| 6 | Large fields and local Gaussian integration | 24 | [UV U4](blueprint/uv-chapters.md) |
| 7 | Local matching and the running coupling coefficient | 26 | [UV U5](blueprint/uv-chapters.md) |
| 8 | Polymer expansions and connected correlations | 18 | [UV cluster tools, split from U6](blueprint/uv-chapters.md) |
| 9 | The nonlinear renormalization step | 30 | [UV U6](blueprint/uv-chapters.md) |
| 10 | A common trajectory and fixed-scale stability | 24 | [UV U7](blueprint/uv-chapters.md) |
| 11 | Renormalized insertions and uniform difference estimates | 30 | [UV U8](blueprint/uv-chapters.md) |
| 12 | The full ultraviolet limit at fixed volume | 24 | [UV U9](blueprint/uv-chapters.md) |
| 13 | Continuum correlations and local fields | 20 | [Continuum C2](blueprint/continuum-chapters.md) |
| 14 | Reflection spaces, Ward identities and Euclidean symmetry | 34 | [Continuum C3](blueprint/continuum-chapters.md) |
| 15 | Decomposition into phases | 18 | [Continuum C4](blueprint/continuum-chapters.md) |
| 16 | Relativistic reconstruction in every phase | 28 | [Continuum C5](blueprint/continuum-chapters.md) |
| 17 | The trace law and its consequences | 24 | [Continuum C6](blueprint/continuum-chapters.md) |
| 18 | Operator products and extensions across diagonals | 30 | [Continuum C7](blueprint/continuum-chapters.md) |
| 19 | Assembly and scope of the construction | 6 | [Continuum C8](blueprint/continuum-chapters.md) |
| — | Front matter, references and notation | 16 | Editor |
| | **Total** | **450** | |

The UV packet's stable identifier U1 refers to the local-observable material already assigned to Chapter 2; it is not an additional chapter. The abstract polymer part of U6 is assigned to Chapter 8. Stable identifiers remain useful in the source audits even when subjects move.

## Logical order and interfaces

**Finite theory (1–4).** Chapter 1 fixes the representation of the gauge group, Wilson measure, reflection conventions and order of limits. Chapter 2 constructs local polynomial representatives without assuming a continuum field. Chapter 3 independently establishes the free comparison calculations. Chapter 4 defines the exact block kernel and the coordinates and norms of effective densities. Defining admissible coordinates does not prove the existence of an infinite trajectory.

**One step (5–9).** Chapter 5 constructs the Gaussian and stationary data under finite-scale hypotheses. Chapter 6 handles the large-field complement and local integration. Chapter 7 matches the local action and isolates the one-loop coefficient with its uniform error estimate. Chapter 8 supplies standard cluster theorems with explicit norm matching. Chapter 9 combines these estimates into an exact nonlinear step and coupling adjustment. If matching and stationary data are defined by a joint induction, state that induction explicitly; do not assert two existence theorems circularly.

**One family (10–12).** Chapter 10 chooses constants, scales and couplings on a common trajectory. It owns the final simultaneous selection, so earlier chapters need not forward-reference an already existing schedule. Chapter 11 constructs coefficient transfers and renormalized insertions on that family and proves all the uniform estimates later used. Chapter 12 proves Cauchy convergence through all ultraviolet cutoffs at each fixed volume; compactness is not a substitute for this argument.

**Continuum theory (13–16).** Chapter 13 extracts one volume subsequence serving all finite label lists and tests, then identifies field quotients using the already available Maxwell comparison. Chapter 14 begins with coordinate reflection spaces, obtains bounded slab operators and spectral estimates, and only then proves continuous rotations and normalized Ward identities. Chapter 15 forms the commutative ground-space algebra, its phases, and the uniform phase estimates. Chapter 16 carries out continuation and reconstruction, including the additional argument needed for every phase rather than almost every phase.

**Identification (17–19).** Chapter 17 proves the all-radius trace law, retaining control of moving field coefficients and logarithmic amplification. Chapter 18 obtains a finite-order, phase-uniform OPE and separately extends distributions across collisions. These two chapters may use the same earlier inputs without depending on each other. Chapter 19 checks that every conclusion belongs to one family, one refinement and compatible normalizations.

The early Maxwell chapter avoids a major forward reference. Splitting elementary local sections from their RG transport avoids introducing renormalized insertions before their defining map exists. Splitting finite-cutoff comparison from continuum rank avoids using a limiting field space to prove the bounds needed to construct it.

## Coverage of Scott's outline

| Outline units | Home in this monograph |
|---|---|
| I.1 | 1; cover geometry in 4 |
| II.1 | 2; renormalized transfer in 11; quotient identification in 13 |
| II.2; III.1 | 4 |
| III.2 | Local assumptions in 4–9; simultaneous choice in 10 |
| III.3; III.6 | 5 |
| III.4 | 5–6, with integration tools used in 9 |
| III.5 | 8–9 |
| III.7 | 7 |
| III.8 | 9 and marked version in 11 |
| III.9 | Exact adjustment in 9; tuning in 10 |
| III.10 | 6 and 9 |
| III.11 | Finite-cutoff comparison in 11; rank in 13; stress in 14 |
| III.12 | 11–13 |
| III.13 | Audit of alternative family; excluded from main proof unless identification is established |
| III.14 | Selected construction in 10; fixed-scale convergence in 12 |
| III.15 | 11; use in 18 |
| III.16 | Elementary analytic tools placed at use in 5, 11, 16 |
| IV.1 | 13 |
| V.1 | 14–15 |
| V.2–V.3 | 16 |
| VI.1–VI.2 | 14; phase inheritance in 15 |
| VII.1 | 3; actual comparison in 11 and 14 |
| VII.2 | 17 |
| VII.3 | Free positivity/rigidity in 3; interacting normalization in 14 and 17 |
| VII.4 | 18 |
| VII.5 | 7 and 10 |
| VII.6 | Finite comparison in 11; normalization in 14 and 17 |
| VIII.1 | 19; upstream definitions moved to their first use |

## Priority checks and drafting policy

Read [the UV audit](blueprint/uv-audit.md) and [the continuum audit](blueprint/continuum-audit.md). In particular, Trish's conditional warnings concerning marked support propagation, restarted Gaussian comparison, and finite-cutoff continuity have detailed proposed suppliers in Martin. Their existence in another file does not by itself establish that the hypotheses match. The audit must compare the actual density, coupling trajectory, Gaussian law, support norms and parameter thresholds.

The first drafting pass covers the foundations, elementary free comparison, and abstract polymer tools. These can be written without presenting the unresolved global supplier matching as settled. Later drafting should follow Chapters 4–12 in dependency order, using Chapter 8's standard tools rather than reproducing their proofs.

Check account usage periodically and before launching substantial new work. Stop with a margin above 10% remaining, preserving a precise progress record. Do not mark an unfinished full-monograph goal complete because a draft or a usage limit has been reached.
