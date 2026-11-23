# House terminology across the whole manuscript: overview

**Status:** draft audit; no chapter text is changed. **Scope:** all chapter files under `chapters/`, plus `main-theorem.tex` and `reading-guide.tex`, at upstream commit `7bec3925`.

This note is the cross-chapter synthesis. The detailed entries are in:

| Chapters | File | Entries reviewed? |
|---|---|---|
| 3–6 | [`terminology-ch03-06.md`](terminology-ch03-06.md) | harmonised, self-audited, independently checked |
| 1, 2, 7, 8, 9 | [`terminology-surveys/ch01-02-07-09.md`](terminology-surveys/ch01-02-07-09.md) | one agent survey, as returned |
| 10, 11 | [`terminology-surveys/ch10-11.md`](terminology-surveys/ch10-11.md) | one agent survey, as returned |
| 12–16 (with the two `18-` files input from chapter 13) | [`terminology-surveys/ch12-16.md`](terminology-surveys/ch12-16.md) | one agent survey, as returned |
| 17–19, main theorem, reading guide | [`terminology-surveys/ch17-19.md`](terminology-surveys/ch17-19.md) | one agent survey, as returned |

References are `chapter:line`; suffixes distinguish included files as in the surveys (`11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, `15sp`, `17w`, `17t`, `17c`, `17m`, `18r`, `9s`, `2e`; `MT`, `RG` for the two front-matter files). Entries marked ✓ were reread by the coordinating agent while writing this overview; everything else rests on one survey.

---

## 1. The picture by part of the book

- **Chapters 1, 2, 8** are nearly free of house vocabulary.
- **Chapters 3–6** carry the "row / actual / selected / test / tag" vocabulary analysed in the chapter 3–6 dictionary.
- **Chapters 7 and 9** continue it and add "response", "insertion" and "weight" in several senses each, with an accounting layer of `cost`, `gain`, `loss`, `reserve`, `share`, `fits`.
- **Chapters 10–11** have been through a translation pass: `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector` no longer occur in prose. What remains is a scheduling vocabulary (stage, plateau, floor, delay, request, window), many undefined nouns for the objects of the expansion with insertions (principal, incidence, graph, column, trial, lift, mass), and sentences broken by mechanical replacement (section 6).
- **Chapters 12–16** use "graph" for a linear map, "column" for a coefficient vector, "heat" for the reflection-positivity semigroup, and let "label" drift from a polynomial to a field.
- **Chapters 17–19** reuse "window", "source", "probe", "response" and "transport" in new senses, and refer to earlier results by nickname.
- **The front matter** uses "phase" without saying it is a character of a commutative algebra, and "admissible periods" without definition (MT:12–15 ✓).

The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund` do not occur in the prose of any chapter surveyed; they survive only in `\label` names. The accounting vocabulary that is present is `cost` (over 100 uses outside chapters 3–6), `reserve`, `gain`, `loss`, `margin`, `excess`, `share`, `spent`, `request`.

---

## 2. Words with several meanings, across the book

Counts are occurrences in prose as reported by the surveys; "—" means the sense does not occur there.

### 2.1 `actual` (about 380 uses in the book)

| Sense | ch. 3–6 | ch. 7, 9 | ch. 10–11 | ch. 12–16 | ch. 17–19 |
|---|---|---|---|---|---|
| of this construction (as opposed to a model, an abstract or a substituted object); mostly deletable | 17 | about 20 | about 55 | 14 | 25 |
| nonlinear / at the non-flat background, against flat or linearised | 26 | 1 | about 10 | — | 4 |
| the gauge-covariant block average and objects built with it | 20 | about 13 | — | — | 6 |
| the running coupling `β`, against the reference `β̂` | 5 | 3 | 17 | — | 2 |
| exact, emphatic | 5 | 6 | — | — | 4 |
| determined by the configuration | 2 | 1 | — | — | — |
| with its indicators and clipping, against the bare expression | — | 3 | — | — | — |
| the original torus or field, against auxiliary reflected ones | — | 3 | — | — | — |
| the modified metrics, against the unmodified `H₀` | — | — | 3 | — | — |
| the density itself, against a representation of it | — | — | 2 | — | — |
| belonging to cutoff `N`; the sequence produced, against a substituted one | — | — | — | 4 | — |

Proposal: delete the word in the first sense; in every other sense name the contrast (`nonlinear`, `gauge-covariant`, `the coupling β`, `exact`).

### 2.2 `row`

| Sense | Where |
|---|---|
| component of the stacked vector whose half-square is the action | ch. 6 (about 68); 7:352, 976–993, 1168; 9:544, 568, 835, 840; 10:354, 356; 11:668, 710; 11R:101–122; 12:55 |
| kernel of a translation-invariant operator | ch. 5 (9); 17w:12; 17c:280; 17m:237–260 |
| symbol; operator; factorisation `C*C = H` | ch. 5, 6 only |
| bounded coefficient family | 13:159 |
| member of a finite separating family ("reference rows", "row constant") | 15:275, 278 |
| vector in a finite list | 11:2253 |
| row of a displayed table | 9:140, 145 |
| literal matrix row; "row mass" = row sum | everywhere |

### 2.3 `selected`, `selection`

| Sense | Where |
|---|---|
| large-field selection `A` and membership in it (chapter 6) | ch. 6 (about 31); 9:108, 153, 279, 440; ch. 11 and 11R (about 25) |
| fixed by the construction: "selected trajectory / schedule / history / stage requirements" | ch. 7, 10, 11, 12, 13, 17–19 (about 45) |
| retained component of an affine map | ch. 6 (about 12) |
| a finite subfamily of terms ("finite selections") | 9:157, 215, 637–687, 890; 17m:92 |
| retained low-order terms | 9:312–383 |
| the continuum family along the chosen subsequence | 13:172, 395; 15:257 |
| the phase `ξ_*` (also "chosen", "retained") | 17:15, 31, 351; 19:117; MT:91, 93 |
| pairs with nonzero weight | 18:297, 352, 358 |

In chapter 11 "selected component" (large-field) and "selected trajectory" (fixed) alternate within single paragraphs.

### 2.4 `test`

| Sense | Where |
|---|---|
| test function (standard) | ch. 1, 13–16, 17–18 |
| "tested against" = paired with all spectators or words; "tested correlation" = value of a correlation functional | 11:2233–2320; 13:272; 14:207; 15:243; 16:46; 18:7, 215, 248 |
| Borel condition, its indicator, the plaquette or edge it concerns, its numerical value | ch. 4–6 only |
| "tested links" = links a function depends on | 11:402, 413; 11R:107 |
| "tested" = multiplied by a small-field indicator | 9:541, 547 |
| classical test connection | 2:13, 103, 150, 416 |

From chapter 10 on, the chapter 4–6 senses are replaced by "event indicator" and "cutoff condition".

### 2.5 `label`, `tag`

| Sense | Where |
|---|---|
| polynomial label, element of `V_d` | ch. 1–3, 11, 12, 13; MT, RG, ch. 19 |
| element of the quotient `F_d` or `F`, i.e. a field | ch. 14–16 (about 26); probably 18:140–222 |
| insertion label, element of the index set of insertions | ch. 11 (13) |
| polymer label (defined 8:24 ✓) | ch. 8; 9:154 |
| index of an activity, path or large-field term | ch. 4, 6, 9, 10, 11R |
| random index `α` ("tag") | ch. 4–6; 9:83, 85; 9s; 11:244, 679; 11R:358 |
| the index `d` of `V_d` ("tag") | 2:98, 99 |
| event label / cutoff-failure label | ch. 6; 9:111, 133 |

`blueprint/notation.md` requires the first two to be distinguished; from chapter 14 on they are not.

### 2.6 `mark`, `marked`, `marker`; `source`

- **marked** = carrying insertions tracked by nilpotent variables `z_i` (12:200–206 ✓): densities, expansions, steps, norms. About 80 uses in chapters 11–19.
- **mark** = one insertion point or its index (about 45 uses); in 7:378 an external plane wave; in 17m the inserted factor is a differentiated block kernel, not an observable.
- **marker** = the nilpotent variable (18:123) or the insertion (18:124).
- **source** has at least six senses: the nilpotent source variable; the source weight; the source algebra; the inserted observable or density itself; the inhomogeneous term of an affine map or of a recursion (ch. 6; 17c); a generating-function source (ch. 8). In 14:186, 18:411 and RG:82 "the source" is the formalisation the book was written from.

Proposal: *insertion* for the object, *insertion point* for its place, *source variable* for `z_i`, *with insertions* for "marked", *inhomogeneous term* for the recursion sense.

### 2.7 `response` (ten senses)

| Sense | Where |
|---|---|
| two-point function with a linear source | 3:409 ff. |
| candidate infinitesimal variation; a term of the Ward sum | 3:657, 964 |
| stationary fine field / the map `W` (elsewhere "transport", "tangent", "lift") | 6:953; 11:642; 17w, 17m; 19:159 |
| curvature response `J = H₀⁻¹ T H₀` (defined 11:647); installed curvature response `Ψ_i` | 11:647, 1729–1775 |
| a log-determinant as a function of the background; an operator with its background derivatives; "response layers" | 7:277, 367, 454, 624, 743, 791; 17t:90 |
| one-slot response `L_{v,f}(c) = ∫ f S(c(x₀), v(x))` (defined 13:120) | ch. 13, 18gq, 14:406, 992 |
| Laplace-transformed pairing with a spectral measure | 14:465–761 |
| flux integral ("total shell response") | 14:777, 796 |
| correlation with other fields ("correlation responses") | 18:182; RG:18 |

### 2.8 `transport`, `transfer` and their synonyms

Three objects share these words: parallel transport along a path; the map `W` from a coarse field to the stationary fine field; and the propagation of a density, coefficient or current through the block steps. The last is also called *transfer*, *pullback*, *propagation*, *update*, *push*, *descent*. Two further uses: conjugation by comparison maps (14:229–302, 946) and image under a lattice symmetry (6:966).

### 2.9 `window`

| Sense | Where |
|---|---|
| index neighbourhood on which a matrix is inverted | ch. 6; 9:142, 278; 10:358; 11:135, 673–684 |
| interval of levels | 10:185, 189; 11 (6); 11R (4); 17w (9); 17m:429 |
| compact set of separated configurations | 11:2078, 2149; 14:173–237; 14lc:6 |
| interval of radii | 17:129–146; 17w:2–7 |
| length of an average | 17m:476 |

### 2.10 `history`, `stage`, `level`

- **history** has three senses: the list of block ratios and averaging orders (5:303); the finite sequence of densities and couplings for one cutoff (ch. 10); and "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations" (11:17–18 ✓). Chapters 1, 2, 8, 9 say "renormalization trajectory" for the same thing.
- **stage** is defined at 10:25 ✓: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds". It is a regularity class, not a renormalisation step. `J(m) = j` for `A_j ≤ m < A_{j+1}` (10:129–134 ✓). Chapters 5 and 6 use "stage" for a step.
- **level**, **scale**, **depth**, **step** are all used for the scale index.

Proposal: *level `m`* for the index, *step* for the map, *stage `j`* only for the regularity class, *parameter sequence* for history in the first sense and *trajectory* for the other two.

### 2.11 `phase`, `word`, `probe`, `insertion`, `weight`

- **phase**: "a character of a commutative operator algebra, not a set of gauge configurations" (15:6–10 ✓); about 100 uses, one sense. "The compact phase space `Ξ`" (16:15 ✓) is the character space, which collides with the usual meaning of phase space. Complex phase factors occur in ch. 7.
- **word**: a finite sequence of insertions (3:234); "a finite list of labels and positions" (13:282 ✓); a product of smeared fields (16:291); a product of links along a path (6:630); a term of a Neumann series (6:1199); "transfer word", "difference word" (ch. 11).
- **probe**: a linear functional on jets (ch. 3); "a fixed word `v` at distinct nonzero positions", defining `λ(A) = S(A(0)v)` (18:36–38 ✓); a finite combination of separated correlations (18lp:268).
- **insertion**: a local observable at a point (ch. 1–3, 8); a derivative of an operator in the background field (ch. 7, about 27); a linear map (7:243).
- **weight**: scaling dimension; exponential support weight; Fourier weight `h_l`; source weight; probability weight; numerical coefficient.

---

## 3. Terms from the chapter 3–6 list that other chapters settle

| Term | Settled by | Meaning |
|---|---|---|
| regularity-stage index `J_m` (4:651) | 10:25–29, 129–134 ✓; 17w:14 | `J(m)` is the stage in force at level `m`; a stage fixes finitely many orders, exponents and bounds. |
| inherited loop action | 9:20–28 ✓ | `P^path = β𝒦 + ℒ`, where "`ℒ` is the quadratic loop correction"; the `β`-independent quadratic part of the path action. |
| coupling band | 10:212 ✓ | "The admissible inverse coupling band at level `m` is `[β̂_m/2, 2β̂_m]`". |
| width | 10:375–381 | The weight `e^{wℓ(γ)}` on path coefficients; a "width reserve" is a bound at `w' > w`. |
| eligible | 8:294–295 | "The exact rules for eligibility are part of the definition of an effective density". |
| subpower | 9:109; 18lp:18 | Agrees with the chapter 6 definition. |
| envelope | 9:793; 11:1581; 17m:283 | A summable or polynomial majorant. |
| matching | 7:988–998, 1159–1167; 17c:301 | Equality of Taylor coefficients through order four; subtraction of `α b_H` from the determinant symbol. |
| parent | 1:218–220 | The map `Ly + z ↦ y`. |
| Warnings (6:1476) | 11:319 ✓, 1612 | Probably cutoff-failure events; "the actual warning estimate gives its supporting event probability at most `x⁻¹`". Still inferred. |
| centered log determinant (5:1338) | 9s:47, 59 | `s(x) − s(0)` with `s = ½ log det A`; the identification is inferred. |
| compulsory | 10:654; 11R:161 | The large-field factor that an activity covering prescribed sites must contain. Partly inferred. |

Still open after all surveys: **moving comparison fields** (3:576; "moving" elsewhere means cutoff-dependent), **seeded sector / unseeded law** (6:1544; 9:283), **output anchors** (6:90), **likelihood tests** (6:920, 1016).

---

## 4. New undetermined terms, by chapter group

Each survey lists the terms its chapters do not determine. The ones that carry an argument:

- **Chapters 7, 9:** `fixed-position read`, `coordinatewise splice` (7:637, 710); `recording estimate`; `thermal`; `bridge legs`; `live tag actions`; `dummy Gaussian coordinates`; `derivative reserves`; `quadratic-tilt criterion`; `read-count polynomials`.
- **Chapters 10–11:** `Hilbert encoding`; `block bridge`; `preselection bound`; `selected slot`; `front-column`; `exposure`; `alphabet`; `coarse forecast`; `restoration levels`; `finite decorations`; `regular logarithms with holes`.
- **Chapters 12–16:** `attachment` (11 uses); `sparse stopping`; `trial encoding`; `protected trial`; `corrected inclusions`; `coordinate hybrids`; `site conversion`.
- **Chapters 17–19:** `strip removal`; `derivative-transport argument`; `weight restoration`; `root estimate`; `fixed probe order`; `unit endpoints`; `exceptional vacua`; and the results cited by nickname in 19:47–52, 89–105.

Two symbols leak source names: `hot(s)` at 11:1934 ✓, where 11R:114 ✓ writes `h(s)` for the same quantity; and `v_eom` at 17m:385–386 ✓, which is never introduced.

---

## 5. Synonym clusters that span the book

| Concept | Words in use | Proposed |
|---|---|---|
| scale index | level, scale, stage, depth, step | *level* |
| one block transformation | step, stage, update | *step* |
| the fixed construction of chapter 10 | common trajectory, selected trajectory, selected schedule, selected histories, same history, same family | *the parameter sequence of Chapter 10* |
| moving an object through the block steps | transport, transfer, pullback, propagation, update, push, descent | *transfer* |
| the operator `W` | transport, stationary tangent, lift, representative, response | one word |
| the constant `b` | block penalty, soft constraint, penalty parameter, block parameter | one phrase |
| the other fields in a correlation | spectators, exterior word, exterior insertions, external positions | *spectators*, defined once |
| family of functionals separating fields | separating family, detecting family, probes, reference rows, detector (labels) | *separating family* |
| value of a correlation functional | response, tested correlation, measurement, correlation pairing | *value of the functional* |
| large-field event | cutoff failure, failed cutoff condition, warning, tail event | *large-field event* |
| activity covering prescribed large-field sites | forced (symbols), "with prescribed set of large-field sites", compulsory, mandatory, hard | one phrase used as a noun phrase |
| small-field part | ordinary, regular, small-field | *small-field* |
| leading part of an insertion factor | principal, leading | *leading* |
| polymer-activity norm | site norm, support norm, containing-site norm, attachment norm, rooted norm | one name |
| chessboard seminorm | `‖·‖_𝒯`, `‖·‖_k`, `‖·‖_cell(m)`, `‖·‖_{𝒞_k}`, `𝓡_m`, `‖·‖_root` | one notation |
| copies in a chessboard estimate | copies, replica cells, reflected copies, repetitions | *copies* |
| subsequence | refinement, extraction, selection | *subsequence* |
| for all large `N` | cutoff tail, ordered tail, eventually | *for all sufficiently large `N`* |
| slack in an estimate | reserve, margin, room, excess, spare | print the inequality |
| factor in an estimate | cost, gain, loss, expense, inflation | *contributes a factor*; `cost` is used for gains as well as losses (7:618–619) |
| lower bound on a parameter | floor, threshold, delay, entry, margin | *lower bound on …* |
| coincident points | collision, contact, diagonal | *coincident points* |
| identity field | unit, unit field, unit insertion, identity | *identity* |
| annihilate | kill, annihilate | *annihilate* |

---

## 6. Sentences broken by mechanical replacement

A replacement of the source words "inventory" and "forced" by the phrase "prescribed set of large-field sites" has left sentences that no longer parse. Examples, all reread:

- 11:247 ✓ "The exact prescribed set of large-field sites condition says that every selected incoming prescribed large-field set is supplied by the unmarked …"
- 11:1312 ✓ "It equals the without its event indicator `F_u^near` wherever `χ = 1`"
- 18lp:43 ✓ "including the prescribed set of large-field sites terms"
- reported, not reread: 11:296, 365, 1595, 1637, 1868; 11R:302; 18lp:136, 185; 13sb:63; 6:730.

These are errors in the text, not terminology choices, and should be fixed first.

---

## 7. Jargon that survives only in labels

Not visible in the PDF, so of low priority: `ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch10:shooting`, `ch11:detectors`, `ch11:detector-bound`, `ch11:replicated`, `ch11:root-bound`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`, `ch12:forgetting`, `ch12:stopped`, `ch13:coarse-residual-supplier`, `ch14:grid-cost`, `ch15:detector-moments`, `ch17:current-suppliers`, `ch18:raw-replacement`, `ch19:conditional`. The last is misleading where the statement is no longer conditional.

---

## 8. Suggested order of work

1. Repair the broken sentences of section 6.
2. Define once, near first use, the house terms that the book keeps: *polynomial label*, *insertion*, *word*, *spectator*, *phase*, *stage*, *history*, *marked*.
3. Remove `actual` where it means "of this construction" (about 130 uses) and name the contrast elsewhere.
4. Separate the senses of `selected`, `label`, `response`, `transport`, `window`, `source`.
5. Apply the synonym reductions of section 5.
6. Resolve the undetermined terms of sections 3 and 4 with the author or the formal source.
7. Replace nickname references in chapter 19 by theorem numbers.

---

## 9. Method and limits

- **Surveys.** Seven agent surveys in two rounds: three for chapters 3–6, four for the rest. Each read its files in full. The four later surveys first read the chapter 3–6 dictionary and its record of earlier errors, classified occurrences of the multi-sense words line by line, and marked each meaning as defined, read, inferred or undetermined.
- **Synthesis.** The coordinating agent merged the surveys' cross-cutting sections into this note. It reread about 25 passages (marked ✓), all of which agreed with the surveys.
- **Not done.**
  - The four later surveys have not been audited or independently checked. The chapter 3–6 dictionary needed substantial correction at that stage, so errors of the same kind (wrong sense assignments, inferences presented as definitions, equivalents that change the meaning) should be expected in them.
  - The per-sense counts in section 2 add the surveys' own counts, several of which are approximate.
  - No Lean declaration was consulted, and no proposed equivalent was checked against the literature.
  - Figures were not read.
- **Agent assistance.** Claude Code (Claude Fable 5.2) with subagents. This is agent work throughout and needs a mathematician's review; agreement between agents is not evidence of correctness.
