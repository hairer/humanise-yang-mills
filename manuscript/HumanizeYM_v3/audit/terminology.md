# House terminology in the v3 manuscript

**Status:** draft audit, not an edit of the chapters (apart from the sentence repairs listed in Part I, section 6). **Scope:** all chapter files under `chapters/`, plus `main-theorem.tex` and `reading-guide.tex`. Line numbers are those of upstream commit `7bec3925`; the sentence repairs keep every line number.

This file gathers what were ten separate notes. Their text is unchanged apart from heading levels and the cross-references between them.

| Part | Content | Former file |
|---|---|---|
| [I](#part-i) | Overview of the whole book: words with several meanings, terms settled by another chapter, open terms, synonym clusters, damaged sentences | `terminology-book-overview.md` |
| [II](#part-ii) | Dictionary and harmonisation proposal for chapters 3–6, with its self-audit and independent check | `terminology-ch03-06.md` |
| [III](#part-iii) | Chapters 1, 2, 7, 8, 9: survey (A) and independent audit (B) | `terminology-surveys/ch01-02-07-09.md`, `audit-ch01-02-07-09.md` |
| [IV](#part-iv) | Chapters 10–11: survey (A) and independent audit (B) | `terminology-surveys/ch10-11.md`, `audit-ch10-11.md` |
| [V](#part-v) | Chapters 12–16: survey (A) and independent audit (B) | `terminology-surveys/ch12-16.md`, `audit-ch12-16.md` |
| [VI](#part-vi) | Chapters 17–19, main theorem, reading guide: survey (A) and independent audit (B) | `terminology-surveys/ch17-19.md`, `audit-ch17-19.md` |

**How the parts relate.** Part I is the synthesis and already incorporates the audits. Part II is the detailed dictionary for chapters 3–6. In Parts III–VI the surveys (A) are kept as returned; **where a survey and its audit (B) disagree, read the audit.** Section numbers are local to each part: "section 4.2" inside Part II means Part II, section 4.2, and "the dictionary" in Parts III–VI means Part II.


---

<a id="part-i"></a>

## Part I. House terminology across the whole manuscript: overview

**Status:** draft audit. **Scope:** all chapter files under `chapters/`, plus `main-theorem.tex` and `reading-guide.tex`. Line numbers are those of upstream commit `7bec3925`; the sentence repairs made on this branch (section 6) keep every line number.

This part is the cross-chapter synthesis. The detailed entries are in:

| Chapters | Dictionary or survey | Independent check |
|---|---|---|
| 3–6 | Part II | applied in Part II (its section 9) |
| 1, 2, 7, 8, 9 | Part III.A | Part III.B |
| 10, 11 | Part IV.A | Part IV.B |
| 12–16 (with the two `18-` files input from chapter 13) | Part V.A | Part V.B |
| 17–19, main theorem, reading guide | Part VI.A | Part VI.B |

The four later surveys are kept as returned. **Where a survey and its audit disagree, read the audit**; this overview already incorporates the audits' corrections.

References are `chapter:line`; suffixes distinguish included files as in the surveys (`11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, `15sp`, `17w`, `17t`, `17c`, `17m`, `18r`, `9s`, `2e`; `MT`, `RG` for the two front-matter files). Entries marked ✓ were reread by the coordinating agent; the rest rests on a survey and its audit.

---

### 1. The picture by part of the book

- **Chapters 1, 2, 8** are nearly free of house vocabulary.
- **Chapters 3–6** carry the "row / actual / selected / test / tag" vocabulary analysed in the chapter 3–6 dictionary.
- **Chapters 7 and 9** continue it and add "response", "insertion" and "weight" in several senses each, with an accounting layer of `cost`, `gain`, `loss`, `reserve`, `share`, `fits`.
- **Chapters 10–11** have been through a translation pass: `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector` no longer occur in prose. What remains is a scheduling vocabulary (stage, plateau, floor, delay, request, window), many undefined nouns for the objects of the expansion with insertions (principal, incidence, graph, column, trial, lift, mass), and sentences damaged by mechanical replacement (section 6).
- **Chapters 12–16** use "graph" for a map from coefficients to remainders, "column" for a coefficient vector, "heat" for the semigroup `e^{-tH}`, and let "label" drift from a polynomial to a field.
- **Chapters 17–19** reuse "window", "source", "probe", "response" and "transport" in further senses, and refer to earlier results by nickname.
- **The front matter** uses "phase" without saying it is a character of a commutative algebra, and "admissible periods" without definition (MT:12–15 ✓); the periods are `R_p = 4(M+p+1)` (10:193–197 ✓).

The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund` do not occur in the prose of any chapter; all four audits confirmed this for their files. The accounting vocabulary that is present is `cost` (over 100 uses outside chapters 3–6), `reserve`, `gain`, `loss`, `margin`, `excess`, `share`, `spent`, `request`, `fits`.

---

### 2. Words with several meanings, across the book

Counts are occurrences in prose. Those for chapters 7–19 were recounted by the audits and agree with the surveys to within a few; the split between neighbouring senses is a judgement in many cases.

#### 2.1 `actual` (about 370 uses in the book)

| Sense | ch. 3–6 | ch. 1, 2, 7–9 | ch. 10–11 | ch. 12–16 | ch. 17–19 |
|---|---|---|---|---|---|
| of this construction (as opposed to an abstract or separately chosen object); mostly deletable | 17 | about 24 | about 54 | 14 | about 24 |
| nonlinear / at the non-flat background, against flat or linearised | 26 | — | about 10 | — | — |
| the gauge-covariant block average and objects built with it, in particular the tangent `W_a` | 20 | about 14 | — | — | 7 |
| the running coupling `β`, against the reference `β̂` | 5 | 3 | 16 | — | 2 |
| exact, emphatic | 5 | about 6 | — | — | 4 |
| the true object against a model, a representation of it, or a substituted object | — | 1 | about 5 | 6 | about 4 |
| determined by the configuration | 2 | 1 | — | — | — |
| with its indicators and clipping, against the bare expression | — | 3 | — | — | — |
| the original torus or field, against auxiliary reflected ones | — | 3 | — | — | — |
| the modified metrics, against the unmodified `H₀` | — | — | 3 | — | — |
| under the law in force (of probabilities) | — | — | 3 | — | — |

Proposal: delete the word in the first sense; in every other sense name the contrast (`nonlinear`, `gauge-covariant`, `the coupling β`, `exact`).

#### 2.2 `row`

| Sense | Where |
|---|---|
| component of the stacked vector whose half-square is the action | ch. 6 (about 68); 7:352, 976–993, 1168; 9:544, 568, 835, 840; 10:356; 11:668, 710; 11R:101–122 |
| kernel of a translation-invariant operator, or a displacement-indexed coefficient of it | ch. 5 (9); 10:354 ✓ ("convergence of the actual quadratic rows", citing the chapter 5 proposition); 12:55 |
| symbol; operator; factorisation `C*C = H` | ch. 5, 6 only |
| row of a matrix or of a kernel at a fixed output index; "row mass" = row sum | everywhere; in chapter 17 all ten uses (17w:12; 17c:237, 280, 336–367; 17m:237–260), where the kernels are not translation-invariant |
| vector in a finite list of coefficient vectors ("bounded rows") | 11:2253; 13:159 |
| row of the matrix of correlation pairings ("reference rows") | 15:275, 278 |
| row of a displayed table | 9:140, 145 |

#### 2.3 `selected`, `selection`

| Sense | Where |
|---|---|
| large-field selection `A` and membership in it (chapter 6) | ch. 6 (about 31); 9:108, 153, 279, 440; ch. 11 and 11R (about 25) |
| fixed by the construction: "selected trajectory / schedule / history / stage requirements" | ch. 7, 10, 11, 12, 13, 17–19 (about 40) |
| retained component of an affine map | ch. 6 (about 12) |
| a finite subfamily of terms ("finite selections") | 9:157, 215, 637–687, 890; 17m:92 |
| retained low-order terms | 9:312–383 |
| the continuum family along the chosen subsequence; choice of a subsequence | 13:6, 7, 143, 172; 15:257; 17m:446; 19:38, 112 |
| the phase `ξ_*` (also "chosen", "retained") | 17:15, 31, 351; 19:117; MT:91, 93 |
| pairs with nonzero weight; picked out by a formula | 18:297, 352, 358; 17t:419, 454 |

In chapter 11 the large-field and the "fixed" senses occur in adjacent paragraphs (11:1933 and 11:1965) and within one proof (11R:89, 159).

#### 2.4 `test`

| Sense | Where |
|---|---|
| test function (standard); integration against one | ch. 1, 13–16 (about 30), 17–18 (12); 14:207 |
| "tested against" = paired with all spectators or words; "tested correlation" = value of a correlation functional | 11:2233–2320; 13:272; 15:243; 16:46; 18:7, 215, 248; 18r:36 |
| Borel condition, its indicator, the plaquette or edge it concerns, its numerical value | ch. 4–6; "tested" at 9:541, 547 |
| "tested links" = links a function depends on | 11:402, 413; 11R:107 |
| classical test connection; one evaluation of a symbol | 2:13, 103, 150, 416; 7:215 |

From chapter 10 on, the chapter 4–6 senses appear as "event indicator" and "cutoff condition".

#### 2.5 `label`, `tag`

| Sense | Where |
|---|---|
| polynomial label, element of `V_d` | ch. 1–3, 11, 12, 13; MT, RG, ch. 19 |
| element of the quotient `F_d` or `F`, i.e. a field | ch. 14–16 (about 26); probably 18:140–222 |
| element of the free Maxwell spaces ("moving free labels") | 17:97, 370 |
| insertion label, element of the index set of insertions | ch. 11 (13) |
| polymer label (defined 8:24 ✓); large-field label `η` | ch. 8; 9:154 |
| index of an activity, path or large-field term | ch. 4, 6, 9, 10, 11R |
| random index `α` ("tag") | ch. 4–6; 9:83, 85; 9s; 11:244, 679; 11R:358 |
| the index `d` of `V_d` ("tag") | 2:98, 99 |
| event label / cutoff-failure label | ch. 6; 9:111, 133 |

`blueprint/notation.md` requires the first two to be distinguished; from chapter 14 on they are not.

#### 2.6 `mark`, `marked`, `marker`; `source`

- **marked** = carrying insertions tracked by nilpotent variables `z_i` (12:200–206 ✓; 11:70–75: the unmarked density is the coefficient of `z_∅`). About 80 uses in chapters 11–19.
- **mark** = one insertion point or its index (about 45 uses). In most of `17-marked-trace-rates.tex` the inserted factor is a differentiated block kernel, not an observable. At 7:378 "a mark of direction `a`" seems to be an external plane wave (inferred).
- **marker** = the nilpotent variable (18:123) or the insertion (18:124).
- **source** has at least six senses: the nilpotent source variable; the source weight; the source algebra; the inserted observable or density itself; the inhomogeneous term of an affine map or of a recursion (ch. 6; 17c); a generating-function source (ch. 8). At RG:82 "source locations" refers to the formalisation the book was written from; 18:411 probably does too; for 14:186 ("the source construction") it is not determined.

Proposal: *insertion* for the object, *insertion point* for its place, *source variable* for `z_i`, *with insertions* for "marked", *inhomogeneous term* for the recursion sense.

#### 2.7 `response` (about ten senses)

| Sense | Where |
|---|---|
| two-point function with a linear source | 3:409 ff. |
| candidate infinitesimal variation; a term of the Ward sum | 3:657, 964 |
| the map `W` from a coarse field to the stationary fine field (elsewhere "transport", "tangent", "lift") | 6:953; 11:642; 17m:193, 202; 19:159 |
| curvature response `J = H_{0,f}⁻¹ T H_{0,c}` (11:646–648 ✓) and its installed form `Ψ_i` | 11:647, 1729–1775; 17w:11, 60, 67, 68 |
| a log-determinant as a function of the background; an operator with its background derivatives; "response layers" | 7:277, 367, 454, 624, 743, 791; 17t:90 |
| one-slot response `L_{v,f}(c) = ∫ f S(c(x₀), v(x))` (defined 13:119–122 ✓); "correlation responses" | ch. 13, 18gq; 14:406, 992; 18:182; RG:18 |
| Laplace transform of a profile against a spectral measure (a function of `E`), and the number obtained by evaluating it | 14:465–761 |
| flux integral ("total shell response") | 14:777, 796 |
| "anchored vector response" | 17:224 (inferred) |

#### 2.8 `transport`, `transfer` and their synonyms

Three objects share these words: parallel transport along a path; the map `W` (and its companion `T` on two-forms); and the propagation of a density, coefficient or current through the block steps. The last is also called *transfer*, *pullback*, *propagation*, *update*, *push*, *descent*. Further uses: application of, or conjugation by, the comparison maps `U_{k,d}` (14:229–302, 946) and image under a lattice symmetry (6:966).

#### 2.9 `window`

| Sense | Where |
|---|---|
| index neighbourhood on which a matrix is inverted | ch. 6; 9:142, 278, 279; 10:358; 11:135, 673–684 |
| interval of levels | 10:185, 189; 11 (6); 11R (4); 17w (about 11); 17m:429 |
| compact set of separated configurations | 11:2078, 2149; 14:173–237; 14lc:6; probably 17:140 |
| interval of radii | 17:129, 131, 146; 17w:6 |
| range of distances; length of an average | 11:1726; 17m:476 |

#### 2.10 `history`, `stage`, `level`

- **history** is defined at 11:18–19 ✓: "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations". Chapter 10 uses it for the finite sequence of densities and couplings at one cutoff, with its choices attached (10:256). Chapter 5 uses it for the list of block ratios and averaging orders alone (5:303). Chapters 1, 2, 8, 9 say "renormalization trajectory".
- **stage** is defined at 10:25 ✓: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds". It is a regularity class, not a renormalisation step; `J(m) = j` for `A_j ≤ m < A_{j+1}` (10:129–134 ✓). Chapters 7 and 9 already use it in this sense (14 uses); chapters 5 and 6 use "stage" for a step. Chapters 4, 5 and 7 also write `j` for the averaging order, which chapter 10 calls `ȷ_j`.
- **level**, **scale**, **depth**, **step** are all used for the scale index.

Proposal: *level `m`* for the index, *step* for the map, *stage `j`* only for the regularity class (defined once), and one word for history.

#### 2.11 `phase`, `word`, `probe`, `insertion`, `weight`, `stopping`, `request`

- **phase**: "a character of a commutative operator algebra, not a set of gauge configurations" (15:6–10 ✓); about 100 uses, one sense. "The compact phase space `Ξ`" (16:15 ✓) is the character space, which collides with the usual meaning of phase space. Complex phase factors occur in ch. 7.
- **word**: a finite sequence of insertions (3:234); "a finite list of labels and positions" (13:282 ✓); a product of smeared fields (16:291); a product of links along a path (6:630); a term of a Neumann series (6:1199); "transfer word", "difference word" (ch. 11).
- **probe**: a linear functional on jets (ch. 3); "a fixed word `v` at distinct nonzero positions", defining `λ(A) = S(A(0)v)` (18:38–39 ✓). The uses in `18-lattice-products.tex` and 14:354 are this second sense ("fixed cells for exterior probes", 18lp:331–333 ✓).
- **insertion**: a local observable at a point (ch. 1–3, 8); a derivative of an operator in the background field (ch. 7, about 28); a linear map (7:243).
- **weight**: scaling dimension; exponential support weight; Fourier weight `h_l`; source weight; probability weight; numerical coefficient.
- **stopping**: in chapter 12, stopping at level `m` *and* deleting the terms of source degree at least two; in chapters 13 and 18lp, the level at which the transfer is halted and a chessboard bound applied, with nothing deleted.
- **request**: a finite tuple of data; a requirement placed on the schedule; a prescribed lower bound on a level.

---

### 3. Terms settled by another chapter

Each of these was listed as inferred or undetermined by at least one survey; the audits located the defining passage.

| Term | Settled by | Meaning |
|---|---|---|
| regularity-stage index `J_m` (4:651) | 10:25–29, 129–134 ✓; 17w:14 | `J(m)` is the stage in force at level `m`. |
| inherited loop action | 9:20–28 ✓; 7:237 | `P^path = β𝒦 + ℒ`, where "`ℒ` is the quadratic loop correction"; the `β`-independent quadratic part of the path action. |
| coupling band | 10:212 ✓ | "The admissible inverse coupling band at level `m` is `[β̂_m/2, 2β̂_m]`". |
| admissible periods (MT) | 10:193–197 ✓ | `R_p = 4(M+p+1)`, `p ≥ 0`, with `M` large enough for the first plateau. |
| connected covering number | 4:587–589 | Minimum number of radius-`B` balls with connected union covering the set. |
| `c_lin` (9:846) | 4:474–480 | Slope constant of `clip_t` above `t`. |
| quadratic-tilt criterion (9:115) | 9:114–116 ✓, citing a proposition of chapter 6 (6:1123–1138) | An alternative hypothesis in terms of tilted Gaussians; not needed in chapter 9. |
| nonautomatic relaxed condition (9:548) | 4:489–492 | The finitely many plaquettes on which the relaxed small-field condition is not automatically satisfied. |
| width | 10:375–381 | The weight `e^{wℓ(γ)}` on path coefficients; a "width reserve" is a bound at `w' > w`. |
| derivative reserve (9:34) | 10:737–739 | Derivative orders beyond the order of the output norm. |
| eligible | 8:286–295; 4:440–450 | Families of large-field labels with disjoint supports covering the large-field set; "The exact rules for eligibility are part of the definition of an effective density". |
| section | 2:138–146 | "A local polynomial section is a complex-linear map …; the term section simply means a right inverse of the Taylor map". |
| separated test function | 1:359 | An element of `C_c^∞(Conf_n)`, extended by zero. |
| conserved line | 3:590–596 ✓ | `{J ∈ 𝒯_{≤4} : div J = 0} = ℝ T^Max`. |
| one-slot response; correlation responses | 13:119–122 ✓ | `L_{v,f}(c) = ∫ f S(c(x₀), v(x))`. |
| ordered tails | 13:212–214 ✓ | "the filter is generated by ordered tails: `p = P(k)` with `k ≥ k₀`, and `N = n(j)` with `j ≥ j₀(k)`". |
| strip removal; scaled mesh; grid errors | 14:174–200 | Coordinate-equality strips of width `4δ_k`, grid spacing `s_k`, and the errors on that grid. |
| derivative-transport argument | 14:229–238 | The proposition "Derivative transport and smooth comparison". |
| physical inclusion | 14:210–212 | The inclusion for the interacting theory, against the free one. |
| exceptional vacua / phases | 16:378–381 ✓; 15:324–328 | "the zero-energy space is a line for almost every phase … To remove the exceptional set requires a bound uniform in `ξ`": the exception is a null set of phases. |
| trial encoding | 11:943–951, 1074 | The reference label `v_{N,p}` approximating a trial `F`, with bounded inverse terminal coordinates. |
| attachment | 9:687; 11:147–156, 924–941 | Joining an insertion stencil or a large-field part to an existing support in the polymer expansion, and the sum over the places where this can happen. Not defined in one sentence. |
| site conversion | 9:513; 11:266–272; 11R:141 | Conversion of sums anchored at a point into sums over terms containing a site. |
| weight restoration | 11:1374–1454 | Named lemmas: passage to the larger source weight. |
| root estimate | 11:817–822, 2072–2079 | "Taking the number-of-cells root": the chessboard-seminorm bound. |
| top polynomial extraction `T` | 11:1142 ff., 2085–2088 | The map `T` built at the top level of the comparison window. |
| restarted representation | 11:736–741; 11R:18 | The history with the coupling held constant below a comparison level. |
| equation calibration floor (19:30) | 11E:25–30 ✓ | A lower bound on the block ratio `L` ("in the stage-`j` block floor"), not on the coupling. |
| subpower; envelope; matching; parent | 9:109, 18lp:18; 9:793, 11:1581, 17m:283; 7:988–998, 1159–1167; 1:218–220 | As in the chapter 3–6 dictionary. |
| Warnings (6:1476) | 11:319 ✓, 1612 | Probably cutoff-failure events. Still inferred. |
| centered log determinant (5:1338) | 9s:47, 59 | Probably `s(x) − s(0)` with `s = ½ log det A`. Still inferred. |
| compulsory | 10:654; 11R:161 | The large-field factor that an activity covering prescribed sites must contain. Partly inferred. |

A claimed inconsistency was withdrawn: the symbols `W_s` (linear-average transport, 5:1084 ✓) and `W_a = W_s − d_{0,f} E R W_s` (5:1108 ✓) are used consistently in chapters 5, 7 and 17.

---

### 4. Terms still undetermined

After the surveys and their audits, the text does not determine:

- **Chapters 3–6:** `moving comparison fields` (3:576; "moving" elsewhere means depending on the cutoff or sequence index); `seeded sector / unseeded law` (6:1544; 9:283); `output anchors` (6:90); `likelihood tests` (6:920, 1016).
- **Chapters 7, 9:** `recording estimate` (7:461, 742); `thermal` (7:765); `direction selectors`; `live tag actions`; `missing-coordinate factor`; `read-count polynomials`; `support compression`; `inspected support`.
- **Chapters 10–11:** `Hilbert encoding`; `block bridge`; `response bound` (10:626); `preselection bound`; `selected slot`; `front-column`; `exposure`; `alphabet`; `coarse forecast`; `corrected body product estimate`; `same-data restart conditions`; `finite decorations`; `protected trial`.
- **Chapters 12–16:** `coordinate hybrids` (14lc:95); `admissible comparison depth` (14lc:23); why a map is called a "graph".
- **Chapters 17–19:** `v_eom` (17m:385–386 ✓, never introduced); `actual free history`; `protected-path errors`; `fixed-ratio jet errors`; `with these same frames`; `unit endpoints`; `E_stat`, `E_tail`, `E_mark` (only bounds are given); `polynomial-source propagation constants`.

The symbol `hot(s)` at 11:1934 ✓ is the function written `h(s)` at 11R:114 ✓: a leaked source name.

---

### 5. Synonym clusters that span the book

| Concept | Words in use | Proposed |
|---|---|---|
| scale index | level, scale, depth, step (and "stage", wrongly, in ch. 5–6) | *level* |
| one block transformation | step, stage, update | *step* |
| the fixed construction of chapter 10 | common trajectory, selected trajectory, selected schedule, selected histories, same history, same family | one phrase |
| moving an object through the block steps | transport, transfer, pullback, propagation, update, push, descent | *transfer* |
| the operator `W` | transport, stationary tangent, lift, representative, response | one word |
| the constant `b` | block penalty, soft constraint, penalty parameter, block parameter | one phrase |
| the other fields in a correlation | spectators, exterior word, exterior insertions, external positions | *spectators*, defined once |
| position of an insertion | anchor, origin, representative point | one word |
| family of functionals separating fields | separating family, detecting family, reference rows, detector (labels) | *separating family* |
| value of a correlation functional | response, tested correlation, measurement, correlation pairing | *value of the functional* |
| large-field event | cutoff failure, failed cutoff condition, warning | *large-field event* |
| activity covering prescribed large-field sites | forced (symbols), "with prescribed set of large-field sites", compulsory, mandatory | one phrase, usable as a noun phrase |
| polymer-activity norm | site norm, support norm, containing-site norm, attachment norm, rooted norm | one name |
| chessboard seminorm | `‖·‖_𝒯`, `‖·‖_k`, `‖·‖_cell(m)`, `‖·‖_{𝒞_k}`, `𝓡_m`, `‖·‖_root` | one notation |
| copies in a chessboard estimate | copies, replica cells, reflected copies, repetitions | *copies* |
| subsequence | refinement, extraction, selection | *subsequence* |
| for all large `N` | cutoff tail, ordered tail, eventually | *for all sufficiently large `N`* |
| slack in an estimate | reserve, margin, room, excess, spare | print the inequality |
| factor in an estimate | cost, gain, loss, expense, inflation | *contributes a factor*; `cost` is used for gains as well as losses (7:618–619) |
| lower bound on a parameter | floor, threshold, entry, margin | *lower bound on …* |
| identity field | unit, unit field, unit insertion, identity | *identity* |
| annihilate | kill, annihilate | *annihilate* |
| lattice link | link, edge, bond | *link* |

Three mergers proposed by the surveys were rejected by the audits and are **not** synonyms:

- `ordinary` and `regular` in chapter 17: `Z_ord = 𝒞 exp[−βS − ℒ − E_reg]` (17m:106–115 ✓), so "ordinary" is the whole small-field part and "regular" one term of it.
- `contact`: a coincident-point term in chapters 18–19, but the "contact term" of 7:501–568 and the "contact identity" of chapter 17 are not.
- `padded block` (7:599) and `macro-box`: the wording at 7:599 fits the block-average patch of radius `(j+3)L`, not the macro-box of radius `(j+7)L`.

---

### 6. Damaged sentences

**Repaired on this branch** (commits `ac15effb` and `75cdd683`; wording recovered from the pre-replacement text where possible; line numbers unchanged): 6:730; 7:1085; 9:212, 548; 10:923; 11:247, 296, 365, 938, 1312, 1589, 1595, 1636, 1868–1869; 11R:302; 14:832; 16:380; 17w:76; 17m:144, 285, 303; 18lp:43, 136.

**Left for the author**, because the intended meaning is not certain:

- 17t:159–160 "the order-two pullback must annihilate its affine–affine and affine–quadratic polynomial moment conditions" (earlier wording: "polynomial tests").
- 17c:359–360 "Only a bounded number of coarse output edges are within the gauge-covariant block average and averaging patches" (earlier: "the predictor and averaging patches").
- 9:893–894 "A connected prescribed set of `r` large-field sites is bounded in number by a rooted spanning-walk count."
- 9:949 "Output inverse coupling-band membership additionally requires".
- 18lp:27, 36 "a remainder with vanishing extracted coefficient of norm `r_l`" (the norm belongs to the remainder).
- 19:152–154 lists "the fact that inserting the identity leaves correlations unchanged" where 18:430 still says "unit removal".
- 10:98 "the relaxed small-field smooth cutoff is one": the relaxed condition is an indicator, not a smooth cutoff, so this may be a replacement artefact. Conjecture.
- Awkward but grammatical uses of "prescribed set of large-field sites" as a noun phrase: 11:941; 12:27, 162; 13ba:153; 13sb:63; 18lp:40, 185; 18:127.

---

### 7. Jargon in label names

Not visible in the PDF, so of low priority: `ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`, `ch09:fusion*`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch11:detectors`, `ch11:detector-bound`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`, `ch12:forgetting`, `ch12:stopped`, `ch13:coarse-residual-supplier`, `ch14:grid-cost`, `ch15:detector-moments`, `ch17:current-suppliers`, `ch18:raw-replacement`, `ch19:conditional`. The last is misleading where the statement is no longer conditional.

Some label words are also in the prose and so are visible: `shooting` (10:272–274 ✓ "uniqueness of the shooting parameter"), `floor`, `mass`, `root`, `replication`.

---

### 8. Proposed equivalents withdrawn after the audits

The surveys proposed standard equivalents; the audits rejected these because they change the mathematics or collide with established usage:

| House term | Rejected proposal | Why | Use instead |
|---|---|---|---|
| stopping (ch. 12) | truncated correlation | "truncated" is the standard name for connected functions; and nothing is deleted in ch. 13 | describe the operation |
| graph (ch. 12) | remainder map | collides with the text's own "remainder map" `J_G` | *the map `G` from coefficients to remainders* |
| unmarked gas | partition function without insertions | it is a function of the configuration; the partition function is its integral | *the density without insertions* |
| heat semigroup | transfer semigroup | not a standard term | *the contraction semigroup `e^{-tH}`* |
| hard / soft (10:656–666) | large-field factor / small-field corrections | "soft" bounds the logarithmic correction factors, which are not small-field | *preliminary large-field activity* / *logarithmic correction factor* |
| moment norm (10:476) | norm of the functional on `c₀` | wrong space | *sup norm of the moment sequence* |
| left-coordinate Hessian | Hessian in left-invariant coordinates | increments act by left multiplication, generated by right-invariant fields | *second derivative in left-multiplication increments* |
| block-completed form (7:687) | gauge-fixed Hessian | it is completed by the block penalty and is still gauge-degenerate | *the form `⟨u, K_f u⟩ + b|Mu − d₀r|²`* |
| principal | leading part | collides with "leading interval / map" in ch. 11 | keep *principal*, defined once |
| corrected coefficients `R_I` | truncated (connected) coefficients | they are the coefficients after division by the free moment polynomial | keep *corrected* |
| row (ch. 17) | kernel | the uses are rows at a fixed output index | *row of the kernel* |
| mixed ground space | space of invariant vectors of the mixed theory | the text's own phrase is clearer | *zero-energy subspace of the reflection Hilbert space* |
| exceptional vacua | further invariant vectors | loses that the exception is a null set of phases | *non-uniqueness of the vacuum on a null set of phases* |
| `ker H` | vacuum | chapter 15 stresses the space need not be one-dimensional | *zero-energy subspace* |

---

### 9. Method and limits

- **Surveys.** Seven agent surveys in two rounds: three for chapters 3–6, four for the rest. Each read its files in full and marked each meaning as defined, read, inferred or undetermined.
- **Independent checks.** Five fresh agents, one for the chapter 3–6 dictionary and one for each later survey. Each read its chapter files in full, rechecked the stated meanings and basis codes, reclassified the multi-sense words occurrence by occurrence, and checked the claims of this overview about its chapters. They found the surveys reliable on line references and quotations, and found between six and ten definite errors per survey: wrong sense assignments, merged or invented terms, equivalents that change the mathematics, and above all terms declared undetermined that another chapter defines (about forty in total; section 3).
- **Verification by the coordinating agent.** About 60 passages marked ✓ here or checked while applying the audits, including the main finding of every "definite error" that changed this overview. All agreed with the audits.
- **Not done.**
  - The audits themselves are unchecked agent work. Two of them noted points they could not decide, and their judgements on what is standard terminology come from their own knowledge.
  - The four later surveys are not rewritten; their corrections are in the audit files.
  - Sections on overloaded symbols and synonym clusters in the surveys were only spot-checked by the audits.
  - No Lean declaration was consulted, and no proposed equivalent was checked against the literature. Figures were not read.
- **Agent assistance.** Claude Code (Claude Fable 5.2) with subagents throughout. This needs a mathematician's review; agreement between agents is not evidence of correctness.

---

<a id="part-ii"></a>

## Part II. House terminology in chapters 3–6: dictionary and harmonisation proposal

**Status:** draft audit, not an edit of the chapters. **Scope:** `chapters/03-maxwell.tex`, `04-blocking.tex`, `05-gaussian.tex`, `06-large-fields.tex` at upstream commit `7bec3925`. Line numbers refer to those files at that commit.

**Companion parts.** The rest of the book is covered by Part I and the surveys in Parts III–VI.

**Purpose.** These chapters use many words as technical terms that are not standard mathematical or mathematical-physics vocabulary. Most come from the names of the formal source or from programming and accounting metaphors. This note lists them, states what each means in the text, and proposes one standard equivalent per concept, the same in every chapter. It extends the short translation table in `blueprint/notation.md` ("Terminology translation and restrictions") and follows its rule: *do not translate a metaphor by guessing; its domain, codomain, quantifiers and estimates determine its meaning.*

**How to read the "Basis" column.**

- **D** — the text defines the term; the line is given.
- **R** — the meaning is read off an explicit sentence or formula, though the term is not formally defined.
- **I** — the meaning is inferred from context. Check before using the proposed replacement.
- **?** — the four chapters do not determine the meaning (section 4).

Line references marked † were reread during the audit (section 8); the others rest on the per-chapter surveys (section 7).

---

### 1. Words with several meanings

These are the most damaging, because the reader cannot tell which sense is meant. The proposal is to keep at most one sense per word.

#### 1.1 `row` (ch. 5: 9+ lines; ch. 6: about 80 occurrences)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| kernel | 5:711–713, 738, 751, 826, 844, 849, 854, 1379 | Matrix-valued convolution kernel `K_ab(z)`, `z ∈ ℤ⁴`, of a translation-invariant operator on the infinite lattice. The text only introduces the notation ("Write a translation-invariant row as `K_ab(z)`"). "Adjacent-scale row": kernel of an operator between consecutive scales, with the position inside a block absorbed into the index set (inferred). | R | *kernel* (of a translation-invariant operator); *two-scale kernel* |
| symbol | 5:609, 624 | The same object as a matrix-valued Fourier multiplier with exponentially summable coefficients. | I | *symbol with exponentially decaying kernel* |
| operator | 5:858, 1124; 6:145† | A specific linear operator (`R`, `K`) with finite range or exponential decay. | R | *operator*, *finite-range operator* |
| component of the action vector | 5:853, 1054–1055; 6: about 68 of 82 occurrences, e.g. 101, 109–112, 186, 453, 1397–1398, 1434 | One component, indexed by its plaquette or edge, of the stacked vector whose half-square is the action; by extension the same component of its linearisation and of its affine approximation `Du + b_Y`. "Direct row": the single-plaquette component; "path row": a path component; "capped coarse rows": `v_c(p)`; "the rows `Φv_c`, `Φ_n v_c`": the comparison vectors; "complement-row", "null-row" (6:203, 1408): components of `N`. | R | *component* (of the curvature vector `X_f(p)`, of the affine map); *plaquette component*, *path component* |
| factorisation | 6:125, 136, 164, 377 | "Row factorization / realization / identities": the factorisation `C_ν*C_ν = H_ν` and the identities written through it. | R | *factorisation `C*C = H`* |
| matrix row | 3:628; 5:882, 996, 1346; 6: about 13, e.g. 217, 240, 280, 330, 554, 636, 812, 828, 907, 972, 994, 1501 | Literal, as in row and column sums. | — | keep |

#### 1.2 `actual` (ch. 4: 4 lines; ch. 5: about 44; ch. 6: about 60)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| the nonlinear object | 4:293; 5: 12 prose uses (857, 912, 930, 986, 1000, 1078, 1118, 1234, 1289, 1304, 1311, 1321); 6:161, 165, 361, 445, 478, 490, 1554 | The gauge-covariant block average of chapter 4 and its linearisation `𝒬 = M + d₀R`, as opposed to the linear ("straight") average `M`, and objects built with it. | I | *gauge-covariant block average*; write the symbol |
| at the true background | 6: about 26 uses, e.g. 15, 183, 439, 463, 466, 468, 515, 542, 1397–1400, 1551 | Nonlinear or evaluated at the non-flat background, as opposed to the flat or linearised model ("without identifying actual and flat matrices", 6:468; "the actual nonlinear row … its actual affine approximation", 6:1397). The most frequent sense in chapter 6; absent from chapter 5. | I | *at the background field `V`*; *nonlinear*; *non-flat* |
| the running value | 4:407, 418, 533; 6:878, 1155 | The coupling `β ∈ [β̂/2, 2β̂]` ("the actual coupling band"), as opposed to the reference value `β̂_m`. | R | *the coupling `β`* vs *the reference coupling `β̂`* |
| of this construction | 5:302, 751, 782, 1324, 1379, 1380; 6: about 11 uses, e.g. 137 ("rows actually used"), 305, 342, 1022, 1162 | The specific kernels, parameters or action fixed by the construction, as opposed to an arbitrary admissible choice. | I | delete, or *the … constructed above* |
| exact (emphatic) | 5:1052, 1071, 1303, 1374, 1382 | "Its actual quadratic Taylor coefficient": the true coefficient, not an approximation; 5:1057 calls the same hypothesis "an exact coefficient condition". | R | *exact*, or delete |
| determined by the configuration | 6:78, 1343 | "The actual coarse large-field set", as opposed to the stored or selected one ("the stored coarse large-field indicators equal the actual coarse large-field indicators"). | R | *the large-field set of the configuration* |

`selected` and `chosen` are used as near-synonyms of the last sense (5:738, 858, 1314; 6:134–177, 362). Proposal: delete or replace by *fixed*.

#### 1.3 `selection`, `selected`, `selector`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| large-field selection | 6:49–51 and about 30 further | A triple `A = (A_f, A_n, A_c)` of fine plaquettes, coarse edges and coarse sites. It is a chosen index, not the set determined by the configuration: on `A_f` and `A_n` the variables are required to be at least moderately large (`r_p ≥ t_f/4`, `n_e ≥ W t_f`), off them at most `t_f/2`, `2W t_f` (6:56–59), so the thresholds overlap. | D | *admissible large-field index set* `A`; keep it distinct from `Bad_m(U)` (section 2.4) |
| retained | 6:1405, 1435, 491–505 | A component of the affine map kept in `D` (sense 5 of `row`). | R | *retained* |
| chosen | 4:160, 210, 383, 393, 456, 616; 5 and 6 passim | Chosen by the random index, or fixed by the construction. | I | *chosen*; *for every value of `α`* |

In chapter 6 a "selected row" (retained component) lies far from the "selected set" (large-field set); the two senses must be separated.

#### 1.4 `test`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| condition | 4:65–106, 209 ff.; 5:967 | A Borel condition on the configuration deciding which case of a definition applies ("loop test", "eligibility test", "minimum-cost test"). The minimum-cost test compares the minimum of the block-average objective `P_e` with `ε_pred` (4:391†). | I | *condition*; *smallness condition* |
| variable | 6:320, 337, 604 | The numbers `r_p`, `n_e` compared with thresholds ("every fine or mismatch test … is at most `t_hi`"). | R | *plaquette and edge variables* |
| location | 6:19, 54, 79, 89, 323, 416, 1156, 1162, 1329, 1349 | The plaquette or mismatch edge itself ("on all tests meeting `A^[5B]`", "tests exceeding `t_hi`"). The most frequent sense in chapter 6. | R | *plaquettes and edges* |
| indicator | 4:481–493; 6:83, 109, 231, 687, 776, 920, 1324, 1340, 1416 | The indicator of such a condition; `χ^rel` ("relaxed small-field test") is `1{χ(U_p) ≤ t_m e^{dist/R^rel} for every p}`. Not a smooth cutoff: "fixed Borel tests. Their indicators are not differentiated" (6:687). | D | *indicator of the small-field condition* |
| test function | elsewhere in the book | Standard. | — | keep; reserve *test* for this |

This agrees with `blueprint/notation.md`, which reserves "test" for test functions.

#### 1.5 `label`, `tag`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| formal polynomial | 3:524, 677, 687, 777 (def. ch. 2:58) | An element of `V_d`, a formal invariant polynomial in jet variables. | D | *polynomial label* (house term, defined; keep) |
| random index | 4:78†, 209–217†, 316; 5:948–970; 6:63, 87, 363, 486, 1108, 1344 | The auxiliary discrete variable `α` with law `λ(U,α)` recording which case of the frame and block-average definition is used. "Tag" is the same object. | D (4:217) | *auxiliary index `α`*; drop "tag" |
| index | 4:322, 330, 539; 6:1168, 1236, 1317 | Index of a path or activity; in ch. 6 the index stands for the term. | R | *index*; *term* |

#### 1.6 `response`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| two-point function | 3:409–451, 899, 975 | `y ↦` two-point function of the linear field `ℓ_P(F)(0)` with `F(y)`. | D (3:409) | *two-point function with source `ℓ_P`* |
| variation operator | 3:657, 1084, 1086 | A candidate linear map on local fields giving an infinitesimal symmetry variation. | I | *infinitesimal variation*; *linear map on local fields* |
| term of a sum | 3:964 | "The third response": the third term of the Ward sum. | I | *third term* |
| stationary point | 6:947, 953, 967, 972, 1493, 1545 | "The stationary fine response to a coarse logarithmic field `h`", `a = 𝒰_F h` (6:953). The text names it without a formula; that it is the critical point of the quadratic form of chapter 5 is inferred. 6:846 "block average response" may be a different object. | R / I | *stationary (critical) fine field*; say *minimiser* only where a gap is proved |

#### 1.7 `transport`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| stationary-field map | 5:453–534 and about 20 further; 6:135, 161 | `W`: coarse field ↦ stationary fine field of the Gaussian block step (`QW = I − b⁻¹K_c`; 5:105 "sends a coarse field to the stationary fine field"), and its companion `T` on two-forms. Minimality is asserted only for specific objects (5:1118, 1143). | R | *stationary-field operator `W`*; *induced map `T` on curvatures* |
| image under a lattice symmetry | 6:966 | "Each signed orientation with its transported forest". | R | *image of the forest under the symmetry* |
| parallel transport | 5:1003, 1008; 6:179–186, 217 | Holonomy along a path; "transported kernel" = flat kernel made gauge-covariant by parallel transport along fixed paths. | R | *parallel transport*; *covariantised kernel* |

#### 1.8 Other words with two or three senses

| Word | Senses and places | Basis | Proposed wording |
|---|---|---|---|
| `anchor` | (i) distinguished site of a support, 4:435, 506, 573; 6:90, 190 ff.; (ii) site `a_i` attached to a coordinate, 5:1204; (iii) real base point of a holomorphic weight, 5:902 | R | *base point*; *site of the coordinate*; *real part `x`* |
| `eligible` | (i) pair `(z,o)` satisfying the axial bound, 4:68–75; (ii) an extra gauge-invariant event, 4:442 | D / I | *pair satisfying the axial bound*; *additional event* |
| `centered` | (i) zero-mean, 3:580–584; (ii) about a point: `x₀` at 3:699, the anchor `o_i` at 4:628; (iii) normalised, 4:132; (iv) symmetric about the origin or block centre, 5:202, 307, 341, 916. "Centered log determinant" (5:1338) is undetermined (section 4). | D / I | *zero-mean*; *about `x₀`*; *normalised*; *symmetric* |
| `separation` | (i) displacement `x − y`, 3:61†, 429†; (ii) nondegeneracy property, 3:973†, 981; (iii) of singularities, 3:854 | I | *displacement*; *nondegeneracy* |
| `cutoff` | (i) threshold (`ε_pred`, `t_m`), 4:203, 211, 406; (ii) cutoff function `χ`, 3:758; (iii) ultraviolet cutoff `N`, 5:705; (iv) truncation of path length at `R_*`, 6:23, 905 | R | *threshold*; *cutoff function*; *ultraviolet cutoff*; *path-length truncation* |
| `physical` | (i) position-space, 5:520, 1085; (ii) unscaled, 5:97; (iii) before the change of variables, 6:691 ff. | I | *position-space*; *unscaled*; *original* |
| `mismatch` | (i) `n_e = χ(V_e Q_e(U)⁻¹)`, 6:47; (ii) "the two signed mismatch terms", 6:1410, plausibly the terms `E_L`, `E_D` that 6:213 calls "the two signed defects" | D / I | *deviation from the block average*; *error terms* |
| `word` | (i) finite sequence of insertions, 3:234; (ii) product of links along a path, 6:630 (inferred); (iii) term of a Neumann series, 6:1199 ff. | D / I / R | keep (i) only if defined once; *holonomy*; *term of the series* |
| `layer` | (i) homogeneous degree of a jet, 3:185; (ii) lattice hyperplane, 4:147–161 | I | *degree*; *hyperplane* |
| `rotation` | (i) lattice or Euclidean rotation; (ii) constant group element `c ∈ G`, 4:359, 370, 394 | I | (ii) *constant gauge transformation* |
| `allocation` | (i) partition of unity over large-field sets, 6:67–79; (ii) assignment of action terms to core or annulus, 6:1327, 1460 | R | *partition of unity*; *assignment* |

---

### 2. Dictionary by theme

One row per concept. Chapters are abbreviated `3`–`6`.

#### 2.1 Scales, lattices and renormalisation steps

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| history; blocking history; history depth | 5:303–305 and 24 lines | Odd ratios `L₁,…,L_n ≥ 3` and averaging orders `j₀,…,j_n ≥ 4` with `j_{h−1} − j_h ∈ {0,1}`. | D | *sequence of blocking parameters* |
| nested histories; (nested, scale) schedule | 4:421; 5:703–707, 740, 1378; 6:1557 | Parameters fixed at every scale, only the ultraviolet cutoff `N` increases. | R | *fixed parameter sequence `(L_m, j_m, ζ_m)`, with increasing cutoff* |
| terminal cutoff; terminal scale; horizon (labels only) | 5:705–706; labels `ch05:horizon-*` | The finest scale `N`. Note that "terminal" names the scale where the flow *starts*. | R | *ultraviolet cutoff `N`* |
| observation scale | 5:700 | The fixed scale `m` while `N` varies. | I | *fixed scale `m`* |
| suffix | 5:378–380, 394, 418, 779 | Steps `h+1,…,n`. | D | *subsequent (coarser) steps* |
| stage; step; update; nonlinear step | 5:689, 1380; 6:21, 96, 950 | One renormalisation transformation, or its index. | I | *renormalisation step*; *scale* |
| total dilation `M`; total ratio | 5:240, 305, 757 | `M = L₁⋯L_n`. | D | *total scaling factor* |
| period; torus side; torus size | 5:320, 446, 731, 916 | Side length of the periodic lattice. | R | *side length* (one word) |
| cover; covering lattice; cover coefficients; cover row | 4:18; 5:735†, 751, 806–849 | `ℤ⁴` as universal cover of the tori; the kernel on `ℤ⁴` as opposed to its periodisation. | R | *the infinite lattice `ℤ⁴`*; *infinite-volume kernel* |
| period recovery | 5:730–733, 828, 849 | An infinite-lattice kernel is the limit of its periodisations on tori of unbounded size. | R | *infinite-volume limit of the periodised kernels* |
| nonwrapping / wrapping support | 4:627, 642 | Support that does not wind around the torus. The text gives no criterion. | I | state the condition explicitly |
| fine residue | 5:654, 660, 713 | Position `r` of a fine site in its block, `x = Ly + r`. | R | *position within the block* |
| incoming; inherited | 5:306, 690, 1058 ff.; 6:379, 671 and 17 more | Belonging to the input of the renormalisation step. | I | *from the previous step*; *input* |
| exact (blocking, block map) | 4:2, 5, 169, 232, 289†, 569 | The block kernel is a probability kernel, so the partition function is preserved. | D (4:289) | *normalised block-spin kernel* |
| smoothing order `j` | 4:16, 186; 5:196–202 | Number of box convolutions in the averaging weight. | D | *order of the averaging kernel* |
| block penalty `b` | 4:226; 5:88; 6:21, 125 | Constant in the Gaussian block weight `exp(−(b/2)‖Qa − v‖²)`. | D | *constant of the block-spin kernel* |
| noise; accumulated / suffix noise | 5:126–130 and 13 lines | The independent Gaussian `b^{-1/2}ξ` in `v = Qa + b^{-1/2}ξ`, and its propagated contribution. | R | acceptable; or *the `b⁻¹` term* |
| noise coordinates | 6:908, 1014 | A different object: the Gaussian fluctuation coordinates `g z_i` of the local integral. | R | *fluctuation variables* |
| filter; accumulated / directional filter; link factor | 5:328–336, 759–763 | Fourier multiplier of the composed averaging maps. | D | *symbol of the averaging operator* |
| principal / nonprincipal alias; principal / nonprincipal columns | 5:351–353, 402; 5:581–600† | Alias index `0` versus nonzero; "columns" are the alias components `𝒜_l`, `𝒯_l`. | R / I | *zero alias*, *nonzero aliases*; *alias components* |
| tail `U` | 5:548 | Nonzero aliases plus the current noise. | D | *remainder* |

#### 2.2 Gauge choices and the block average

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| frame; gauge / axial / minimising / constant frame; frame patch | 4:23–43 and about 30 lines; 5:950–1020 | A `G`-valued function on the sites of a patch, `g_x = T_U(z→x;o)`. | R | *local gauge transformation* |
| macro-box; macro-patch; macro-frame; macro axial gauge | 4:298, 367, 398; 5:1005–1032; 6:303–325 | Box of radius `(j+7)L` about `Ly`, and an axial gauge on it. | R (4:298) | *enlarged block*; *axial gauge on it* |
| root; block roots | 4:36, 89, 161; 5:916–935 | Base point of the axial-gauge tree. | R | *base point* |
| branch; minimising / fallback / alternative branch | 4:32, 76, 106, 208–211, 361–393; 5:948–970 | A case of a piecewise definition; "fallback" is the complementary case in which the smallness condition fails. | I | *case*; *in the complementary case* |
| uniform mass; branch masses; positive mass / likelihood | 4:77, 209, 315; 5:970; 6:63, 671, 1107, 1345 | The weights `λ(U,α)` of the random index. That "mass" and "likelihood" name the same weights is inferred. | I | *probability weights `λ(U,α)`* |
| likelihood tests / factors | 6:920, 1016 | Doubtful: these are "on their plateaux" when the plaquette distance is below `t_f/4` and the block-average discrepancy below `W t_f` (6:1014–1015), which are the thresholds of the partition-of-unity weights `ϑ_f`, `ϑ_n` (6:68–70), not of `λ(U,α)`. | ? | resolve with the author |
| connector | 4:175–184; 5:986 | `Y_{e,z}`: frame-conjugated product of `L` fine links along a straight path. | D | *gauge-transformed parallel transporter* |
| `Q^pred`, `ε_pred`, `r_pred` | 4:202–210, 239, 287, 386–391; 6:460, 501 | The block average with its label, and its threshold. The superscript is never explained in the text. | R | *block average*; rename the superscript |
| route; route matrices; walk | 4:107, 109; 5:995, 1003; 6:180 ff. | Lattice path; its holonomy. In 6:1025 "route" also means "method". | I | *path*; *holonomy* |
| feedback matrices | 4:124–133 | `F_x(h) = av h_y W_{xy;o}⁻¹`. | D | *local mean* |
| straight (average, transport) | 5:535, 859, 993, 1084 | The linear average `M` without the gradient correction. | D (5:993) | *linear block average* |
| first-power (bound, estimate) | 4:293, 308–312; 5:1007 | A bound linear in `χ`, as opposed to a square-root consequence of a squared-energy bound. Never defined; read off 4:308–310. | R | *linear bound* |
| forest; forest coordinates / chart / slice | 5:916–935; 6:516, 629, 966 ff. | A rooted spanning tree in each block; coordinates `(v, ψ)` with `ψ` on non-tree links. | D | *maximal-tree gauge in each block* |
| tree slice; tree coordinates; tree-straightened | 5:916 ff.; 6:466–490, 972, 1492 | Gauge slice where tree links equal the identity. | I | *tree gauge* |
| tree comparison | 4:296; 5:1000, 1036–1040, 1289 | The inequality `‖a‖² ≤ B‖d₁a‖² + C‖𝒬a‖²` for `a` vanishing on tree links. | D (ch. 5) | *Poincaré-type inequality in the block-tree gauge* (the text reserves "coercivity" for the resulting Hessian bound, 5:1143) |
| replica `rep V`; replicated field; parent | 5:920–929; 6:180, 341 ff. | Fine field equal to `1` inside blocks and to `V` on links between blocks (defined). "Parent" of `x`, used undefined, is the coarse site of the block containing it (inferred). | D / I | *pull-back of `V` under the block projection* (5:1137 uses "block-constant extension" for something else) |
| vertical (coordinates, Hessian, gap) | 5:944, 1078, 1334, 1339 | The fluctuation variables `ψ` at fixed `v`. | I | *in the fluctuation variables* |
| stationary graph / tangent / background | 5:1145–1180 and 25 lines | `ψ = ρ(v)` solving `D_ψ f = 0`, and its derivative at zero (defined). "Background" is used in titles without definition. | D / I | *critical-point map*; *background field* |
| frozen (links, logarithms) | 6:442 and 26 more | Non-tree links near the large-field set, held fixed in the Gaussian integral and integrated afterwards. | I | *conditioning variables* |
| active / inactive coordinates | 6:443 | Logarithms of non-tree links outside the `10B`-neighbourhood. | D | *integration variables* |
| signal `ũ` | 6:1373–1383 | The active increment, extended by the clipped frozen logarithm and zero on the tree. | D | *displacement field* |

#### 2.3 Effective action and its pieces

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| density coordinates; coordinate tuple | 4:8, 403, 469, 530, 550†, 656–676 | The data `(β, v_sc, regular activities, large-field activities)` parametrising a density. Not coordinates: the map to densities is not claimed injective or onto. | D | *parametrisation*; *representation data* |
| regular activity | 4:433–438†, 452, 554† | `(X_i, o_i, E_i^reg)`: a local term entering the exponent additively. Not a polymer activity. | D | *local term of the small-field action* |
| scalar; `v_sc` | 4:9, 554, 658 | The constant term `−v_sc|Λ|` of `V_ρ`, where the density is `e^{−V_ρ}`; the text calls it "a scalar normalization". | D | *constant term per site*; *normalisation constant* |
| direct (row, term, coefficient `c_dir`) | 4:474; 5:749; 6:101, 137, 143 ff. | The single-plaquette term and its coefficient, as in `H = c_dir I + ρ*ρ` (ch. 7:974†). | I | *plaquette term*; *its coefficient* |
| path action `P^path`; prescribed leading action | 4:466, 496–521; 6 passim | The explicit leading part of the effective action. It includes the single-plaquette `clip` term (4:512) as well as the path sums, so it is not only the non-local part. | D | *leading part of the effective action* |
| admissible path action; path budget (label) | 5:1241–1252 | A generic hypothesis: an action `Σ_γ c_γ ×` (local analytic term in holonomies along paths) with `sup_z Σ |c_γ| e^{σℓ(γ)} ≤ P`. | D | *action with exponentially summable path coefficients* |
| atoms; quadratic path square | 5:1054–1056; ch. 9:573, 837† | Elementary terms of the path action, graded by degree in the curvature. | I | *elementary terms of degree `q`* |
| inherited (quadratic) loop action; loop correction | 4:516–517, 525; 5:1045; 6:170, 1261–1262; ch. 7:237 | A quadratic term of the action carried from the previous step and not multiplied by `β`: ch. 7:237 "`ℒ_{m+1}` is the inherited quadratic loop action"; 6:170 "the separate loop correction is not part of the classical metric". Its identification with the term `Σ A_i^(2)` of 4:516 is inferred. ("Order four" in ch. 7:1160 is a property of its symbol.) | R / I | *one-loop quadratic correction from the previous step* |
| (curvature, two-form) metric; metric modification; positive completion | 5:43–46, 227–235, 286–291, 456; 6:139, 163 | Positive operator `H` on two-forms with `K = d₁*Hd₁`; the modification `H⁻¹ = H₀⁻¹ + ζ(d₂H₀⁻¹)*(d₂H₀⁻¹)`. | D | *quadratic form on two-forms*; *coefficient operator* |
| (curvature) defect; amended defect; positive-defect identity | 5:638–641, 603; 6:135, 145, 176 | `Z₀ = B_c − T*B_fT − b⁻¹d₁d₁*` with `B = H⁻¹`, and its version with modified metrics, with `K*K = Z ≥ 0`. In 6:213 "the two signed defects" are instead `E_L`, `E_D`. | R | *positive remainder in the recursion for `H⁻¹`* (no standard name known) |
| aligned; alignment premise | 6:136–141, 164 ff. | `C_ν*C_ν = H_ν`: the components of the action factorise the chosen two-form operator `H_ν` (the Hessian is `d₁*H_ν d₁`). | R | *factorisation of the two-form coefficient operator* |
| quadratic coefficient condition | 5:1052–1058 | The quadratic Taylor coefficient of the input action is `d₁*H_f d₁` with `H_f ≥ εI`. | D | *hypothesis on the quadratic part* |
| uncut (action); plateau | 5:973†, 1044, 1241; 6:281†, 917 ff. | Without the smooth small-field cutoffs; region where a cutoff equals one. | I | *without cutoff functions*; *where the cutoff equals one* |
| clip; clipped; capped | 4:476–480, 528; 6:109–121 | `clip_t`: quadratic below `t`, linear above, with a downward jump at `t` (4:528). "Capped": multiplied by `min(1, t_c/r)`. | D | keep the symbol; *piecewise quadratic–linear function* |
| relaxed (`χ^rel`, `R^rel`) | 4:481–493 | Indicator of the small-field condition with threshold `t_m e^{dist/R^rel}`. | D | *exponentially weighted small-field condition* |
| kinetic energies `K_f`, `K_c` | 6:110 | Clipped plaquette action plus cut-off path square. Nothing kinetic. | R | *local action density* |
| comparison term | 6:186–188† | The specified quantities `Φ v_c` and `Φ_n v_c` (defined). That they are the fine curvature and mismatch predicted linearly from the truncated coarse curvature is inferred. | D / I | *linear prediction from the coarse field* |
| coarse counterterm | 6:1407 | The term `E_c`. Not a renormalisation counterterm. | I | *subtracted coarse energy* |
| affine stack | 6:446–452 | The vector `Du + b_Y`. | R | *the affine map `u ↦ Du + b_Y`* (avoid "residual", which the chapter uses otherwise) |
| source (`b_Y`, `f_Y`) | 6:448–449, 581–612 | `b_Y` is the inhomogeneous term of the affine map; `f_Y = D*b_Y` is the linear coefficient of the quadratic form. | R | *inhomogeneous term*; *linear coefficient* |
| extracted; Gaussian extraction | 6:1251, 1280, 1326 ff. | After the affine squares are moved into the Gaussian measure. | I | *after completing the square* |
| local transfer identity | 6:924–931, 942 | `m_Y − v = E*v − P*(Av + f_Y)` with `E = AP − I`. (The subsection at 6:466, "Transferring a local tree estimate", is a different statement.) | R | *comparison identity for the mean* |

#### 2.4 Large-field regions, supports and localisation

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| `Bad_m(U)` | 4:425 | Sites incident to a plaquette with `χ > t_m`; determined by the configuration. | D | *large-field set of `U`* |
| consistent (selection, sector) | 6:54–63 | Threshold inequalities hold near `A` with overlapping margins. | D | *admissible large-field set* |
| sector; allocation sector | 6:85–87† | One term of the decomposition, with the large-field set, component assignment, block trees and index `α` fixed. | D | *term with fixed discrete data* |
| exclusion support `Y_i`; coverage | 4:440, 455–464 | The set entering the disjointness constraint. The activity also depends on links outside `Y_i` (4:457–464). | D | keep *exclusion support*, or *the set `Y_i` of the disjointness constraint*; "polymer support" would wrongly suggest dependence only on `Y_i` |
| (full) dependence region | 4:459 | All links the function and its conditions depend on. | D | *dependence set* |
| exact cover | 4:543–547 | Family with pairwise disjoint `Y_i` whose large-field parts have union `Bad_m(U)`. | D | *compatible family covering the large-field set* |
| footprint; stencil | 4:505–507; 6:453, 459 ff. | Set of links a term is built from. Not the full dependence set: "its event indicator may read additional adjacent plaquettes" (4:507). | R | *support of the expression*; keep it distinct from the *dependence set* |
| reads; read by | 4:450–507; 5:961, 1054; 6:382, 742, 1349 | "depends on"; "is computed from". | I | *depends on* |
| window `Ω_i`; local inverse columns; principal compression | 6:520–574 | Two index neighbourhoods `Ω_i^sec` (radius `B/20`) and `Ω_i^loc` (radius `B`) of an edge coordinate (6:522–529), on which `A` is inverted to build `P` (6:534–535). That the compression is `A[Ω,Ω]` is inferred. | D | *localisation neighbourhood*; *localised approximate inverse*; *principal submatrix* |
| core; annulus; ownership components | 6:1330–1333 | Terms within `2B` of a component and the rest out to `200B`; components of large-field sets whose `500B`-neighbourhoods meet. | D | *inner part*, *collar*; *components for the `1000B`-adjacency* |
| clean; remote; clearance | 6:925–997, 1008, 1249; 496, 603 | Containing no large-field element; farther than `30B` from the large-field set; distance margin. | I | *small-field region*; *far from the large-field set*; *distance* |
| protected | 6:694–737, 806 | Carrying a smooth cutoff so that the change of variables is the exact logarithm. | I | *cut off inside the chart* |
| containing-site bound; halo; support exponent | 4:603–606; 6:1170–1178 | `sup_x Σ_{λ: x ∈ S_λ} e^{α c_B(S_λ)} a_λ ≤ ε` (defined); `hB`-neighbourhood (inferred from "halo multiplier `h`"); the rate `α`. | D / I | *weighted polymer-activity norm*; *neighbourhood*; *decay rate* |
| cluster (symbols, matrices, limit) | 5:718–734, 805–848 | Subsequential limits. Unfortunate where "cluster" normally means cluster expansion. | R | *subsequential limit* |

#### 2.5 Local fields and Ward identities (chapter 3)

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| spectator (fields, list, legs) | 3:705, 782, 824–873 | The insertions other than the distinguished one. From 3:837 the "quadratic spectator" is brought close to `P`, so it is no longer passive. | I | *the remaining insertions*; *auxiliary insertion* |
| leg | 3:826, 827, 839 | A linear curvature-jet factor of a Wick monomial. | I | *linear factor* |
| probe; jet probe | 3:751, 883, 939–985 | A linear functional on order-`j` solution jets. | R | *linear functional on jets* |
| wave; Maxwell wave | 3:731, 758, 899, 975 | Smooth closed and coclosed two-form on a region. | I | *smooth solution of the Euclidean Maxwell equations* |
| pulse; covariance pulse | 3:732–770 | `y ↦ S₂(F(y), F_ij(x₀))`. | I | *two-point kernel with source at `x₀`* |
| tower | 3:431–470 | `Σ_z P`, a family `(Σ_z P)_k`, `0 ≤ k ≤ j` (the map is defined at 3:431); an element of the direct sum of the `S_k`. | R | *element of the direct sum* |
| detection; detector (labels) | 3:830 | `P ∉ N_D`: some correlation is nonzero. | I | *separation*; *nondegeneracy* |
| Ward sum | 3:915 | `W_A = Σ_i S_n(P₁,…,AP_i,…,P_n)`. | D | *action of `A` as a derivation on the correlation* |
| charge | 3:780 | A symmetry generator acting on fields. | I | *infinitesimal generator* |
| flux; local Ward / stress flux; shell flux | 3:546, 656–671 | `F_{χ,v} = −∫ ∂_aχ v_b S(T_ab, …)`. | D | *smeared charge of the current `T_ab v_b`* |
| pole; harmonic pole; "cleared by" | 3:865–876, 964 | Homogeneous singularity `|z|^{-r}` at the origin of `ℝ⁴`. | I | *homogeneous singularity of degree `−r`*; *becomes smooth after multiplication by* |
| collision | 3:146, 832, 879, 914, 1016 | Coincidence of insertion points. | I | *coincident points*; *short-distance limit* |
| free image; polynomial image; free polynomial space | 3:194–224, 784 | `M_d^Max = im ω_d`. Five names for one space. | D | *space of on-shell polynomials* (one name) |
| correlation-null | 3:216, 348, 523 | Vanishing in every separated correlation. | R | *in the kernel of the correlation functionals* |
| weight; weight operator | 3:168–170, 689–692 | Scaling dimension; `Σ (j+2) X ∂/∂X`. | D | *scaling dimension*; *generator of dilations* or *weighted Euler operator* (the unweighted one measures degree) |
| reciprocity | 3:992 | The symmetry `C(f_b(p),q;u) = C(f_b(q),p;u)` of 3:979. | I | *by the symmetry (…)* |
| contraction derivative | 3:895 | The polynomials `Σ_λ C_{k,j}(p,e_λ;z) ∂P/∂X_{j,α}(e_λ)`. | I | *directional derivatives in the top-order variables* |

#### 2.6 Estimates: accounting and bookkeeping vocabulary

Chapters 3–5 are nearly free of the accounting vocabulary found later in the book; chapter 6 has some. `blueprint/notation.md` already prescribes: *print the inequality*. This table has no Basis column: the glosses of `the supplied construction`, `reachable`, `interface conditions` and `export` are inferences.

| House term | Where | Meaning | Standard equivalent |
|---|---|---|---|
| cost; costs | 4:378, 391; 5:611, 620, 1354; 6: 18 occurrences | A multiplicative loss or an error of that size; in 4:391 the value of the objective `P_e(u)`. | *loses a factor*; *is bounded by*; *objective* |
| loss; "leave … per test"; retained energy; margin | 5:1362; 6:231–435, 1157–1161 | Negative error terms and what remains of a lower bound. | *error terms*; *remaining lower bound* |
| excess | 6:326–328; 6:417 | Two uses: `Δ_p` in `r_p^c ≤ C t_f + Δ_p`, the contribution of the large variables, which is not small; and the surplus of a lower bound ("enough linear excess to absorb"). | *large-field contribution `Δ_p`*; *surplus* |
| supplies; the supplied construction | 3:546; 5:195, 1217 ff. | "Gives"; presumably the construction being transcribed (the text does not say who supplies it). | *gives*; *the present construction* |
| assigned; ownership | 6:85, 421, 1162, 1329–1335 | Which component a term is attributed to. | *attributed to* |
| subpower | 6:822 | `A(x) ≤ C_ε x^ε` for all `ε`. | `x^{o(1)}` |
| zero-germ | 6:922, 1021, 1215 | Vanishes identically near the base point. | *vanishes in a neighbourhood of* |
| score | 6:1530, 1541 | Logarithmic derivative of a density. Standard in statistics. | keep, or *logarithmic derivative* |
| interface conditions | 5:1385 | Hypotheses to be verified where the chapter is applied. | *standing hypotheses* |
| declared; inputs; export; reachable; stored | 3:441; 4:20, 505, 626, 674; 6:1343, 1543 | Program vocabulary for "stated", "hypotheses", "result", "obtained by iteration", "prescribed". | as glossed |

---

### 3. Synonym clusters to reduce to one word

| Concept | Words in use | Proposed |
|---|---|---|
| lattice link | link, edge, bond (4:356–362; 5:1006; 6 throughout) | *link* |
| lattice path | path, route, walk | *path* |
| renormalisation step | stage, step, update | *step* |
| side length of the torus | period, torus side, torus size, volume | *side length* |
| satisfying the standing constraints | admitted, permitted, allowed, admissible | *admissible*, with the conditions stated |
| enlarged block | macro-box, macro-patch | *enlarged block* |
| support of a local term | footprint, stencil | *support of the expression*; do not merge with *dependence set*, which the text distinguishes (4:507) |
| the random index | label, tag | *index `α`* |
| its weights | mass, likelihood | *weight `λ(U,α)`* |
| base point of a support | anchor, root | *base point* |
| subsequential limit | cluster limit, cluster symbol | *subsequential limit* |
| on-shell polynomial space | free image, polynomial image, free polynomial space, free spaces | one name |

---

### 4. Terms whose meaning chapters 3–6 do not determine

These need the author, the formal source, or a cross-reference before any replacement is made. Five terms originally listed here were resolved by the independent check and are in section 4.1.

| Term | Where | What can be said |
|---|---|---|
| moving comparison fields | 3:576 | Possibly the cutoff-dependent fields of ch. 11 ("moving equation space", 11:1083). |
| regularity-stage index `J_m` | 4:651 | An index distinct from `m` on which `q, ϖ, σ` may depend. |
| centered log determinant | 5:1338 | Presumably `log det H(v) − log det H(0)`. |
| output anchors | 6:90 | Probably anchors on the coarse (output) lattice: `H` indexes the sums of `E_L + E_D` (6:287), and "every coarse plaquette with `r_p^c > δ` lies in `H`" (6:295). Inferred. |
| compulsory (component region, cutoff factor) | 6:1018, 1461 | Possibly the chart cutoffs "retained throughout `304B`" (6:1350) belonging to the component factor; cf. ch. 10:654. Not certain. |
| Warnings | 6:1476 | Capitalised, undefined. Probably the cutoff remainders indexed by event labels (6:834–843); ch. 11:319 has an "actual warning estimate". Inferred. |
| seeded sector / unseeded law | 6:1544 | Also ch. 9:283. Possibly with and without prescribed large-field elements. |

#### 4.1 Terms first listed as undetermined and resolved by the independent check

| Term | Where | Meaning | Basis |
|---|---|---|---|
| internal rotation defect | 3:910, 1027; ch. 14:932 | `[L(K), L(M)] − L([K, M])`: the failure of the rotation generators to act as a Lie-algebra representation (ch. 14: "the internal defect `[L(K),L(M)]−L([K,M])` has zero correlation sums"). | R (ch. 14) |
| connected covering number `c_B(S)` | 4:587–589; 6:1172, 1296 | Defined in chapter 4 as `cov_B(X)`: the minimum number of radius-`B` periodic balls whose union is connected in the nearest-neighbour graph and covers `X`. Chapter 6 writes `c_B`. | D |
| terminal fine metric | 6:174–175 | The fine metric at the ultraviolet cutoff scale `N` ("at Wilson initialization"), unmodified (`ζ_f = 0`). "Terminal" as in section 2.1. | R |
| pre-`L` factor / pre-`L` excess estimate | 5:1021; 6:356, 517–518 | A bound whose constant is fixed before `L` is chosen, hence independent of `L` ("the excess constant in (macro-comparison), which is needed before `L` is chosen"). | R |
| stationary-field estimates | 4:166 | The estimates for the stationary background of chapter 5, which use analyticity of the frame (5:950–959). | I |

#### 4.1a Settled or narrowed by the surveys of the other chapters

See Part I, section 3. In short: `regularity-stage index J_m` is defined in chapter 10 (10:25–29, 129–134: `J(m)` is the stage in force at level `m`, a stage being a finite set of orders, exponents and bounds); `inherited loop action` is the `β`-independent quadratic part `ℒ` of `P^path = β𝒦 + ℒ` (9:20–28); `Warnings` are probably cutoff-failure events (11:319), `centered log determinant` is probably `s(x) − s(0)` with `s = ½ log det A` (9s:47), and `compulsory` the large-field factor an activity covering prescribed sites must contain (10:654). Still open: `moving comparison fields`, `seeded / unseeded`, `output anchors`, `likelihood tests`. The line 6:730 quoted in section 2.3 as garbled was repaired on this branch.

#### 4.2 House terms not yet glossed in detail

Reported by the independent check as missing from the dictionary. Meanings are as that check read them; they were not rechecked.

| Term | Where | Reading |
|---|---|---|
| lift | 5:626–633, 746; 4:298, 628; 6:356 | Three senses: solution `V` of `A = V d_{r+1}`; lift to the covering lattice; "parent lift" of a coarse gauge. |
| event label | 6:835–877, 1106 | Defined: "specifies one particular cutoff and its anchor". |
| counting norm / scalar product / adjoint | 5:40, 528; 6:504 | Unnormalised `ℓ²` sums. |
| width | 5:744–745, 854, 1380 | Width of the analyticity strip, equivalently the exponential decay rate. |
| three-form metric / factor | 5:683, 747, 1371 | The operator on three-forms in the amended defect. |
| rooted derivative; lattice shell sum | 5:1205, 1345; 5:1212 | Mixed derivative with decay measured from one index; `sup_v Σ_i e^{−η d(v,a_i)}`. |
| array; marked | 5:861, 945; 6:479 | A field or family indexed by sites or polymers; "marked" = with observable insertions. |
| matching | 4:471, 526; 6:169, 956 | Conditions relating fine and coarse quadratic forms; the subject of chapter 7. |
| witness | 6:232, 852 | The plaquette or coordinate realising a failure or an event. |
| amplitude | 6:1076, 1107, 1173, 1451 | A bound on a local factor. |
| jet (ch. 6) | 6:1025, 1473 | Derivatives through order `k` of a product. |
| primitive | 6:1165, 1242 | Elementary local factors or estimates. |
| target; candidate field | 6:916, 934; 6:925, 975 | Prescribed value or location; trial field with small residual. |
| normalized / dimensionless directions | 6:627–628, 638, 824 | Derivatives along variations of size `t_f`. |
| envelope; half-square; compensating map | 6:1187; 6:1371, 1402; 6:1540 | Not glossed. |
| coupling band / threshold | 6:623, 878; 6:322, 432 | `[β̂/2, 2β̂]`; "for `β̂` sufficiently large". |
| complement map, penalty map | 6:125–126 | The maps `N`, `M_n`. |
| anchored sum vs containing-site sum | 4:603–605 | Two ways of summing activities over supports. |
| regular expression | 4:532, 584 | The smooth formula with indicators held fixed. |
| connected expansion / regrouping | 4:461; 6:1480, 1567 | The cluster expansion step. |
| representative | 5:1151; 6:1405 | Gauge representative; "squared curvature representative". |
| Wilson initialization; levels | 6:172; 4:15 | The starting Wilson action; "levels" = scales. |
| physical spacing / period | 4:13–14 | In continuum units: a further sense of `physical`. |

---

### 5. Symbols with several meanings

Not terminology, but they compound the difficulty.

| Symbol | Meanings |
|---|---|
| `M` | averaging operator (5:156); total dilation (5:240) |
| `H` | two-form metric; frame variable `H_{y,r}` (5:980); axial gauge; Hessian; output anchors (6:90); tail parameter (6:854); annulus rows (6:1355) |
| `R` | `d₁*Hd₁` (5:474); frame operator (5:981) |
| `D` | covariance (5:468); suffix ratio (5:380); large-field subset (6:89); matrix `AΓ − I` (6:1186) |
| `W` | minimiser operator (ch. 5); lift `W₀` (5:630); threshold multiplier (6:54); annulus energy (6:1387) |
| `K` | operator (6:145); counting constant (6:93, 1221); majorant matrix (6:1100) |
| `w` | plaquette energy; averaging weight `w^av` (4:186–192); box symbol; penalty function (5:1048) |

---

### 6. Suggested order of work

1. Fix the eleven multi-sense words of section 1; each change is local once the sense is identified.
2. Resolve the section 4 terms with the author or the formal source; do not replace them by guesswork.
3. Apply the synonym reductions of section 3 mechanically.
4. Either define once and keep, or replace, the house terms that are harmless when defined (`polynomial label`, `insertion`, `word` in sense (i), `history`, `smoothing order`, `forest coordinates`, `Ward sum`).
5. Rename the Lean-flavoured equation labels (`ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`) only if labels are being touched anyway; they do not appear in the PDF.

---

### 7. Method and limits

- **Data gathering.** Three independent agent surveys, one for chapters 3–4, one for chapter 5 and one for chapter 6, each reading its chapters in full and reporting every non-standard term with line numbers, the decisive sentence, and whether the meaning was read or inferred. They returned 34 + 48, 69 and 93 entries.
- **Harmonisation.** The entries were merged by concept, the proposed equivalents made uniform across chapters and aligned with `blueprint/notation.md`.
- **Self-audit** (section 8) and **independent check** by a fresh agent (section 9).
- **Not done.** No formal-source declaration was consulted, so no claim is made about which Lean names the terms come from. No proposed equivalent was checked against the literature (Bałaban, Bałaban–Feldman–Knörrer–Trubowitz or others). Sections 3 and 5 were not checked row by row by anyone. All of this is agent work and needs a mathematician's review; entries with basis **I** in particular may misread the text.
- **Agent assistance.** Claude Code (Claude Fable 5.2), with three subagents for the surveys and a fourth, given only this note and the chapter files, for the independent check.
- **The † marks** on line references record what was reread in the self-audit. Rows rewritten after the independent check carry no marks.

### 8. Self-audit record

A script extracted every chapter-and-line reference from the tables (421 references) and tested whether the cited lines contain the term; 409 matched, and of the other 12 three were wrong line numbers and nine were artefacts of the matcher. The defining passages of about 45 entries were reread. This pass corrected three line numbers and four entries (`actual`, `comparison term`, `window`, `transport`). It was done by the agent that wrote the note, and the independent check below shows it missed a good deal.

### 9. Independent check

A fresh agent read the four chapters in full and checked every row of sections 1, 2 and 4, classifying each occurrence of `row`, `actual`, `select-` and `test` in chapters 5 and 6. Its main findings were verified against the text before being applied.

**Errors it found, now corrected.**

- **`test` as a "smooth cutoff function".** Wrong: `χ^rel` is the indicator of a Borel condition (4:483–487), and 6:687 says the tests' "indicators are not differentiated". The sense is now "indicator".
- **`actual`.** Three cited lines were in the wrong sense or did not contain the word (6:15, 6:78, 6:406). Two senses were missing: "exact" (five uses in chapter 5) and "determined by the configuration" (6:78, 1343). The non-flat sense, which the self-audit had reduced to one confirmed line, is in fact the most frequent in chapter 6 (about 26 of 48 prose uses).
- **`row` in chapter 6.** The note's "term of the action" and "component of an affine map" are one sense, a component of a stacked vector, covering about 68 of 82 occurrences; a further sense, the factorisation `C*C = H`, was missing.
- **`inherited loop action`.** Described as "an order-four term"; it is a quadratic term of the action (ch. 7:237), and chapters 4–6 already refer to it.
- **`connected covering number`.** Listed as undefined; it is defined at 4:587–589 under the notation `cov_B`.
- **`noise` in chapter 6** is the Gaussian fluctuation variable `g z`, not the block noise of chapter 5.
- **`large-field set`** was proposed for both the selection `A` and `Bad_m(U)`, which the text contrasts (6:1343). They now have different names.
- **Line references** corrected for `local transfer identity`, `score`, `loss`, `centered`, `first-power`.

**Basis codes** that overstated (D or R for what is partly inferred) were lowered for `row` (kernel), `first-power`, `response`, `mismatch`, `word`, `stationary background`, `parent`, `halo`, `tower`, and a claim about the formal source under `Q^pred` was removed. Two were raised: `relaxed` and the role of the windows are explicit in the text.

**Proposed equivalents changed** because they altered the meaning or were themselves non-standard: "minimiser" → "stationary point" (the text says stationary; minimality is proved only for specific objects); "coercivity inequality" → "Poincaré-type inequality"; "vacuum energy density" → "constant term per site"; "polymer support" withdrawn; "Euler operator" → "generator of dilations"; "truncated quadratic", "factorisation of the Hessian", "remainder" (for excess), "linear term" (for source), "vector of residuals", "block-constant lift", "test field" and "admissible pair" replaced.

**Section 4.** Five of the thirteen "undetermined" terms were resolved (section 4.1), three more given a probable reading, and the reviewer agreed that `moving comparison fields`, `regularity-stage index`, `centered log determinant` and `seeded / unseeded` remain undetermined. One entry was added to the doubtful list: `likelihood tests / factors` at 6:920, 1016.

**Omissions.** About 25 further house terms were reported and are listed in section 4.2 without detailed glosses.

**Confirmed by the independent check** (meaning and basis as stated): all rows of section 2.5; in section 2.1 history, schedule, terminal cutoff, suffix, cover, period recovery, exact, smoothing order, block penalty, filter, aliases and columns; in 2.2 frame, macro-box, branch, connector, route, feedback, straight, forest, tree slice, vertical, frozen, active, signal; in 2.3 density coordinates, regular activity, direct, atoms, metric and its modification, quadratic coefficient condition, uncut, kinetic, comparison term, extracted; in 2.4 consistent, sector, dependence region, exact cover, reads, core/annulus/ownership, clean/remote/clearance, protected, cluster.

**Limits of the independent check.** It classified `row` and `actual` in chapter 6 from one-line contexts plus a full read, so borderline assignments could shift by a few. It judged the proposed equivalents from its own knowledge, not from the literature. It is one more agent reading, not a mathematician's review; agreement between agents is not evidence of correctness.

---

<a id="part-iii"></a>

## Part III. Chapters 1, 2, 7, 8, 9

### III.A Survey

*Original title: Terminology survey A: chapters 1, 2, 7, 8, 9*

> **Audited.** An independent check of this survey is in Part III.B; its corrections supersede the text below, which is kept as returned.
>
> **Status.** Survey by one agent (Claude Fable 5.2 subagent), reproduced as returned. It was written against upstream commit `7bec3925`. Meanings marked I are inferences; proposed equivalents were not checked against the literature. See Part I for the cross-chapter synthesis and for what was verified.


**Scope.** `chapters/01-lattice.tex`, `02-observables.tex`, `02-equation-section.tex`, `07-matching.tex`, `08-polymers.tex`, `09-renormalization.tex`, `09-stationary-remainder.tex` in the worktree `manuscript/HumanizeYM_v3/`. All seven files were read in full, after Part II (all sections) and the translation table in `blueprint/notation.md`. Nothing in the repository was edited.

**Conventions.** File abbreviations: `1`, `2`, `2e` (02-equation-section), `7`, `8`, `9`, `9s` (09-stationary-remainder). Line numbers are worktree lines. Counts are numbers of matching lines or matches from `grep` after stripping `\label`, `\ref`, `\eqref`. Basis: D defined, R read off an explicit sentence or formula, I inferred, ? not determined. Category: (a) accounting, (b) program/Lean leakage, (c) ordinary or standard word in unusual sense, (d) coined, (e) other. "Dict" means Part II.

**Overall.** Chapters 1, 2 and 8 are nearly free of house jargon. Chapters 7 and 9 (with 9s) carry most of it. The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund`, and the words `detector`, `probe`, `readout`, `word`, `warning`, `compulsory`, `export`, `stored` do not occur in the prose of these files (`budget` survives in two labels). The accounting vocabulary present is `cost` (32 matches), `gain` (9), `loss` (6), `reserve` (4), `share` (4), `spent` (1), `fits … fraction` (about 6), `allocate` (1), `unused` (2).

---

#### 1. New terms (not in the dictionary)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| row transport | 1:80 | defined 1:80–81 | Holonomies act on row vectors: "multiplying a row vector at the initial point by that ordered product transports it to the final point". | D | keep, defined; or *holonomies act on the right* | d |
| physical placement `ŷ` | 1:209 | defined 1:209–212 | `ŷ = a_N r(y)`, the position of a lattice site in continuum units. | D | *position in continuum units* | c |
| lattice family | 1:371, 391, 398; "common family" 1:503 | undefined | The cutoff-indexed data chosen once: "The lattice family, including its normalizations, is chosen before `p_seq`" (1:398). That it comprises couplings `β_{N,p}` and insertions `I_{N,p}` is inferred from 1:331–339. | R / I | *family of lattice models (couplings and normalised observables)*; define once | c |
| refinement | 1:393 | undefined | A further subsequence: `P = p_seq ∘ q_seq` (1:395–397). | R | *subsequence* | c |
| retained volumes | 1:379 | undefined | The volumes `P(k)` of the chosen subsequence. | R | *the volumes `P(k)`* | c |
| ordered convergence | 1:369 | defined 1:369–386 | First `N → ∞` at fixed volume, then volume along `P`. | D | keep, defined | d |
| transfer matrix | 1:473 | undefined | Matrix of the mixing of polynomial labels of fixed scaling dimension under one block step: "A transfer matrix records this mixing at each fixed scaling dimension". Not the Euclidean time-evolution operator, which is the standard meaning in lattice field theory. | R | *mixing matrix*; *matrix of the block step on `V_d`* | c |
| defects | 1:457 | undefined | "Connected sets of defects are summed": the places where the small-curvature condition fails. | I | *large-field sites* | c |
| seam; seam links; strip seams | 1:284, 287, 316, 323 | undefined | Links or planes on the reflection planes of the chessboard tiling: "An observable local on this cell reads no seam links". | I | *links meeting the reflection planes* | d |
| slots | 1:314 | undefined | "The slots are the `2q` strips in that coordinate": the positions of the cyclic product in the abstract chessboard theorem. | I | *factors of the cyclic product*; not sure a standard word exists | c |
| positive sector; positive algebra | 1:244–247, 265 | 1:244–247 | The half `1 ≤ t < h` or `0 ≤ t < h` of the torus; observables depending only on links with both endpoints there. A different "sector" from the dictionary's. | D | *positive half*; "positive algebra" is close to standard | c |
| observable label `v = (d, c)`; tag `d` | 2:97–99 | named 2:97–98 | The pair of the index `d` and a polynomial `c ∈ V_d`: "The same polynomial `c` can occur at different tags `d`". The dictionary takes a label to be the element of `V_d`; here it is the pair. | R | *pair `(d, c)`*; *index `d`* | b |
| normalization index | 2:402 | undefined | The same `d`: "Its eventual physical normalization still depends on the normalization index". Third name with "tag" and (in `notation.md`) "filtration index". | I | *index `d`*, one name | d |
| factor count; factor-count operator `N_fac` | 2:53, 67–72, 79, 202, 308; 2e:19, 33–35, 187 (def.) | defined 2:52–53 | Ordinary polynomial degree in jet coordinates. | D | *polynomial degree*; keep if defined | d |
| factor count (second use) | 7:613 | undefined | "The factor count is `(n+2) + number of differences = 4`": the number of small factors (legs plus finite differences) in a power count. Not the degree of 2:53. | R | *number of small factors* | c |
| test configuration; test holonomy; test connection | 2:13, 103, 116 (label), 150, 416 | 2:13–16 | Smooth classical connections built from a jet, inserted into a lattice observable to read off its Taylor polynomial. | R | *classical (smooth) connection* | c |
| Taylor map `Tay_d`; local polynomial section | 2:133–146 | defined | Right inverse of the Taylor map. | D | keep | – |
| curvature measurement; plaquette measurement | 2:220, 238, 362 | undefined | The functions `σ_{γ,□}` or their linearisations. | I | *transported curvatures* | c |
| curvature coordinate; admissible for a link `e` | 2e:65–68, 104, 124, 172, 184, 194 | defined 2e:62–67 | `U ↦ ⟨u, σ_{γ,□}(U)⟩`; admissible if neither plaquette nor path uses `e`. The subsection title (2e:60) calls them "curvature tests". | D | keep "curvature coordinate"; drop "tests" in the title | d |
| basis column; unit column; column by column | 2:200, 260, 374, 390 | undefined | The image `P_d^loc[b_{d,i}]` of a basis vector. | I | *image of the basis element `b_{d,i}`* | c |
| permitted direction at threshold `t`; spatial exponent `p_0` | 2:325–330, 340, 388 | defined 2:326–329 | `|A_e| ≤ t(1 + dist(e⁻, y))^{p_0}`. | D | *admissible direction*; keep if defined | d |
| equation ideal `𝓘_d`; Maxwell solution potential | 2e:10–21; 2:445 "free equation ideal" | defined | Polynomials vanishing on solution jets. | D | keep | – |
| regrading `R_d` | 2e:52 (name), 27–36 (object) | object defined; name not | The automorphism with `R_d p − p` strictly higher in (factor count, scaling dimension). | R | *unipotent (triangular) automorphism `R_d`* | d |
| exterior spectator | 2e:195, 205–206, 213, 221, 254 | 2e:39–41 gives the object | The bounded measurable function `S` of links farther than `r_d` from the anchor. Differs from Dict 2.5 (the other insertions). | R | *the function `S`*; *exterior function* | c |
| Wilson force `F_e` | 2e:110–129 | defined 2e:117–121 | Gradient of the Wilson action in one link. | D | standard enough; keep | – |
| common symbol; common kernel; common strip bound | 7:27–46 and passim (28 matches of `common` in ch. 7) | defined 7:36–39 | "one function chosen on the infinite lattice whose restriction to each finite momentum grid describes the corresponding torus coefficient". | D | *volume-independent (infinite-lattice) symbol* | c |
| strip bound `|f|_σ ≤ A`; order-`r` zero | 7:41–48 | defined | Holomorphic and bounded on `|Im p| < σ`; vanishing of momentum Taylor coefficients below degree `r`. | D | keep | – |
| leg (one-form, two-form, internal, external, differentiated) | 7:61, 76, 79, 131, 159 and 30 matches in ch. 7 | undefined | An argument of a multilinear Taylor symbol, with its direction index, Lie-algebra argument and momentum (7:33–34, 61). Dict 2.5 has "leg" as a factor of a Wick monomial. | R | *argument*; "leg" is standard in physics, define once | c |
| bridge legs | 7:597 | undefined | "External smooth bridge legs have the same powers in supremum norm, by (ch05:actual-bridge)": the cited bound is on `∇^r W_a` (ch. 5:1129–1132), so presumably legs of the form `W_a u`. | I | *external arguments `W_a u`* | b |
| elementary division `D_a`; coordinate, scalar, two-leg, curvature division | 7:89–97, 124, 611, 904, 1028, 1162, 1182 | defined 7:89–91 | `D_a f = (f − f|_{p_a=0})/(e^{ip_a} − 1)`. | D | keep | – |
| curvature insertion `F_{γ,ab}` | 7:147–152 | defined | Transported projected plaquette curvature. Same object as ch. 2 "transported curvature". | D | *transported curvature* (one name) | c |
| kinetic symbol `b_H`; kinetic coefficient, action, Hessian, normalization | 7:184, 193, 216, 275, 312, 478, 603–621, 743, 856, 874 | 7:184–190 | The quadratic form `½⟨d_1 v, H d_1 v⟩` and its symbol. The text says "kinetic symbol `b_H` of `J`", but `J` is introduced only at 7:976. Not the "kinetic energies" of Dict 2.3. | R | *quadratic curvature form*; "kinetic term" is physics usage | c |
| gauge completion; completed, block-completed | 7:229 (title), 313, 371, 687, 773, 879, 935, 1025 | 7:251–252 | Adding `F*F` (or `d_U d_U*`) to a gauge-degenerate Hessian: "put `C = J + F*F`". Dict's "positive completion" is unrelated. | R | *gauge-fixed Hessian* | c |
| infinitesimal gauge insertion `ℛ` | 7:243 | named only | The linear map from gauge parameters to tangent vectors; 7:877 calls it "infinitesimal internal gauge action". | R | *infinitesimal gauge action* | c |
| (background) insertion: first, second | 7:332–333, 380–391, 416–418, 603–612 and passim | 7:331–333 | Derivatives of an operator with respect to the background field: "`b(p;k)` its first background insertion, and `c(p,p′;k)` its second insertion. These are actual derivatives of the same operator". | R | *first and second derivative in the background field*; *vertex* | c |
| denominator (zero-background, vector, ghost, channel) | 7:331, 371, 376, 407, 414–415, 440 | 7:331 | The zero-background operator symbol `a(k)`, a matrix. | R | *symbol of the quadratic form*; *inverse propagator* | c |
| floor (metric, denominator, weighted, ratio, period) | 7:323, 407, 684–686, 706, 729, 732, 738, 828; 9:928, 935 | undefined | A uniform positive lower bound: "the weighted floor `2^{-10} min(1, ε)`, where `H_f ≥ εI`" (7:685). | R | *lower bound* | c |
| response | see section 3 | – | – | – | – | – |
| thermal coefficient | 7:765 (prose); label `ch07:thermal` at 7:232 | undefined | "the actual stationary thermal coefficient". The label marks `T(v) = ℒ + ½ log det Q − log J_Haar`, which the text introduces as "the Gaussian contribution". | I | *coefficient of the Gaussian contribution `T(v)`* | b |
| radial bound, radial inequality, radial constants | 7:437, 451, 462 | undefined | The bounds on `I_μ(k)` in terms of `|k|` in Proposition 7:310. | I | *the bounds of Proposition …* | d |
| recording estimate; "Trace norms and recording" | 7:461, 742 | undefined | At 7:461 it refers to the bound for mesh mean minus integral. The paragraph at 7:742–766 ends with the passage to finite-torus representations. | I / ? | *finite-volume error estimate* (unsure) | b |
| direction selectors | 7:427 | undefined | "The four constant direction selectors in the vector regulator"; `M_μ` "applies `m_μ` to each one-form component" (7:276). | I | *projections onto the one-form components* | b |
| contact term; contact correction; contact assertion | 7:501–504, 568, 764, 773, 807 | 7:529–545 | The second-order difference `D²(log det M_act − log det M_core)(0)`, due to the second derivative of the nonlinear block average. Not a coincident-point term. | R | *second-order block-average correction to the determinant* (no standard name known) | c |
| stationary branch; selected branch | 7:501, 517, 553, 766, 949, 953, 1152; 9:292; 9s:36, 39 | 9s:36 "`ρ(x)` for its stationary branch" | The locally unique solution of the stationarity equation as a function of the coarse field. Dict's "branch" is a case of a piecewise definition; Dict's "stationary graph" is this object. | R | *branch of critical points*; *critical-point map* | c |
| rooted coordinates; centered coordinates; recentering | 7:505–507, 521, 530, 581, 626–678, 693–700, 883 | 7:655–656, 693–695 | Rooted: `Q = M + d_{0,c}R` with scalar `r_root`. Centered: `r = r_root − Ru`, with the frame normalised by `Σ_x ω(x) Π F_x = Π 1`. | R | *frame normalised at the root* / *normalised in the mean* | d |
| coarse scalar component; scalar principal alias; coarse-frame directions, projection | 7:477, 507, 580, 591, 696–703, 721–722, 892, 915 | undefined | The zero-form (frame, gauge-parameter) variable at coarse sites carried along with the fine field in the joint space. | I | *coarse frame variable `r`* | c |
| internal / external (direction, leg, momentum, coordinates) | 7:334, 366, 522, 595–630, 872–873, 899–915, 1033–1044 | 7:872–873 | Internal: "internal fine-plus-frame coordinates `z`", the integration variables. External: coarse-field directions. | R | *fluctuation* / *background (coarse)* | c |
| left increment; left-coordinate Hessian; split-field definition | 7:242, 313, 362–363, 522, 624 | 7:362–363 | Hessian "obtained from `S(log(e^{x_+}e^{x_-}))` by two `x_+` derivatives". | R | *Hessian in left-invariant coordinates* | d |
| padded block; padded block average patch | 7:599, 628 | undefined | An enlarged block containing the support of the block average; "its number of residue blocks is fixed at the given smoothing order". Probably Dict's "macro-box". | I | *enlarged block* | d |
| fixed-position read; coordinatewise splice | 7:637, 710 | undefined | "a fixed-position read is a coordinatewise splice of its endpoints"; "each fixed-position averaged read has coefficients `O_j(L^{-4})` on `O_j(L^4)` sites". Apparently the link at a fixed position of a connector path, as a function of the averaged endpoints. | ? | none proposed; needs the author | b |
| exterior identity | 7:408, 686 | undefined | Used to control "the sum of transverse and longitudinal parts". Presumably `d_1*d_1 + d_0 d_0* = Δ` on one-forms. | I | state the identity | d |
| quotient estimate; weighted quotient | 7:688, 719, 728, 870 | 7:719 | `inf_a ‖(u,r) − ℛa‖_p² ≤ C_j 𝒢(u,r)`. | R | *coercivity modulo gauge directions* (unsure) | – |
| weight conversion; weighted-to-Euclidean conversion | 7:498, 748, 751, 917 | undefined | Passing between the `h_l`-weighted and unweighted norms, at a factor `O(μ^{-1})`. | R | *comparison of the weighted and Euclidean norms* | d |
| stationary identification | 7:578, 829; cf. 7:1154 | undefined | The identification of the tangent of the stationary branch with the operators `W` of ch. 5 ("once the actual and straight stationary tangents have been identified up to gauge"). | I | *the identity (ch05:stationary-tangent)* | d |
| adjacent pair; adjacent quadratic pair | 7:580, 828; 9:15, 912, 963 | 9:15 | Two consecutive scales `m+1`, `m`; "quadratic pair" adds their quadratic forms. | R / I | *consecutive scales* | d |
| one-loop drift; downward blocking | 7:825–856; 9:42 | 7:855–856 | "the coefficient `β` of the kinetic action decreases by `κ_G log L` at one loop"; downward = from `m+1` to `m`. | R | *one-loop shift of the coupling per step* | d |
| exchange term, inverse, pairing | 7:935, 955, 1048, 1050 | 7:944–945 | The term `B 𝒞^{-1} B` in `D⁴E(0)`. | R | physics usage; or *tree term with one propagator* | – |
| curvature family (cubic, quartic, quadratic) | 7:1054, 1060–1062, 1071, 1163, 1168 | undefined | The collections of curvature terms `S_3`, `S_4` and the quadratic one. | R | *the terms `S_3`, `S_4`* | d |
| path (short for path action); normalized path; incoming, outgoing, prescribed path | 7:576, 786, 789, 828, 1199, 1203; 9:13 (9s), 385, 914, 926 | undefined | The path action, not a lattice path: "the selected path and block average" (7:576); "the incoming path" (9:914). "Normalized": `H(0) = I` (7:312–313). | R | *path action* in full | c |
| classical bound contraction; inherited-loop contraction | 9:970 | – | The inequalities `A_out ≤ a_stage + P_stage(A)/L` (7:1055–1057) and `‖ℒ pulled back‖ ≤ C L^{-2} Λ^loop` (7:1084–1087). The first is an invariance of a bound, not a contraction. | R | *the bounds (…)* | c |
| quantitative descent | 7:1187 | undefined | The step from the loop bound at `m+1` to that at `m`. | I | *induction step* | d |
| coupling entry threshold | 7:1190 | undefined | Lower bound on the coupling above which the estimates hold; elsewhere "(inverse) coupling threshold". | I | *lower bound on `β̂`* | d |
| site norm `‖z‖_α`; support norm | 8:69–79, 143, 196 | defined 8:69–74 | `sup_x Σ_{γ: x ∈ X_γ} |z_γ| e^{α c(X_γ)}`; "support norm" (8:196) is the same. Dict's "containing-site bound". | D | *weighted polymer-activity norm* (one name) | – |
| support-weight reserve; "will be spent" | 8:150–151, 362; 9:34 ("derivative reserves"), 438, 919 | 8:146–151 | The extra `δ > 0` in `‖z‖_{α+δ} ≤ γ_0`. "Derivative reserves" (9:34) is not explained. | R / ? | *margin `δ` in the decay rate* | a |
| inflated activities | 8:170; 9:180 | defined 8:171 | `q^{-1}|z_γ| e^{α c(X_γ)}`. | D | *rescaled activities* | – |
| hypothesis matching | 8:169 | – | Verification of the hypotheses of the cited theorem. | R | *verification of the hypotheses* | d |
| sites declared to be in the large-field region; sites assigned to an activity | 8:284–288 | defined | The set `D` and the subsets `I_η`. | D | *prescribed large-field set `D`* | b |
| exact reassembly | 8:279, 355; 9:57 | 8:310–316 | The factorisation `Z_D = e^{𝓛} Σ_B Π K_η e^{−𝓛_{Y(B)}}`. | R | *factorisation identity* | d |
| regular activity (ch. 8 sense) | 8:285, 318, 322, 331, 333 | 8:285 | The polymer-gas activities `z_γ`. Conflicts with Dict 2.3, where a regular activity is an additive term of the exponent and "not a polymer activity"; ch. 9 uses that sense (9:132, 867) and says "ordinary" for the gas (9:150, 153, 172). | R | reserve *regular activity* for one of the two | c |
| source-deformed activities | 8:268, 364 | undefined | Activities of the gas with generating-function sources `t_j`. | R | *activities depending on the source parameters* | – |
| first expansion; first polymer activities; second cluster expansion | 9:44, 88–89, 148, 173, 192 | 9:81–89 | First: expand `e^V = 1 + (e^V − 1)` and take connected components of intersecting dependence regions. Second: the logarithm of ch. 8. | R | *Mayer expansion*; *cluster expansion of the logarithm* (unsure the first is exactly Mayer) | – |
| scalar bookkeeping; measure multiplier; missing-coordinate factor; dummy Gaussian coordinates | 9:56, 59, 63, 72, 77 | undefined | The field-independent prefactors of the Gaussian change of variables. "Dummy": coordinates added to reach dimension `D`. "Missing-coordinate factor": presumably `e^{−(N_free − n_act) log 𝔪}` (9:68). | I | *constant prefactors*; *auxiliary Gaussian variables* | a / b |
| Haar logarithm; Haar remainder; Haar correction | 9:63, 76, 127, 141; 9s:39 | 9s:38–39 | "minus the logarithm of the product Haar-chart Jacobian". | R | *logarithm of the Haar density in the chart* | d |
| common law; one sector Gaussian/Haar law; common-law estimate; joint bound | 9:97–118, 139, 266, 785, 966 | 9:105 | The single measure `ν` under which all factors of a product are integrated together. | R | *joint estimate under one measure* | c |
| selected large-field condition set `A_M` | 9:108, 440 | undefined | Presumably the large-field selection `A` of Dict 1.3 restricted to the region. | I | *large-field index set* | c |
| cutoff-failure label | 9:111, 133 | undefined here | The event label of ch. 6:835 (Dict 4.2). | I | *event label* (one name) | d |
| "factor after deterministic subtraction" and the seven factor names in the table | 9:124–133 | undefined | Names of local factors with their majorants; e.g. "stationary cubic remainder", "covariance and stationary residual". | R (table only) | define each by a formula or a reference to ch. 6 | d |
| read-count polynomials | 9:147 | undefined | Presumably the factors `(1 + s_M)^{d_j}` of 9:100. | I | *polynomial factors in the size of the dependence region* | b |
| ordinary gas; ordinary polymers; elementary ordinary factor; exact-cover gas | 9:150, 153, 172, 593 | undefined | The polymer gas without large-field sites; `ℱ⁰` is the "exact-cover gas". | I | *small-field polymer gas*; *constrained sum `ℱ⁰`* | c |
| prescribed large-field site set | 9:151, 643, 673, 675, 893 | 8:287–288 (object `I_η`) | The set `I_η` of large-field sites attached to an activity. This is the `notation.md` rendering of "inventory". | R | keep, with the symbol | – |
| degree (of an elementary factor, polymer, cluster) | 9:172–174, 182, 193 | defined | Number of elementary factors. | D | *number of elementary factors* | c |
| affine Hessian; affine-Hessian cancellation, condition | 9:207, 213, 480, 497, 564 | 9:458–480; ch. 4:627–640 | The Hessian at the identity restricted to affine potentials `A_μ(y) = u_μ + Σ y^ν v_{μν}`. | R | keep, define at first use | d |
| inverse-ratio sizes | 9:208 | – | Powers of `L^{-1}`. | R | *powers of `L^{-1}`* | d |
| inspected support | 9:220 | undefined | Probably the dependence region. | I | *dependence region* | b |
| support compression | 9:231 | undefined | Probably the passage from a fine support to its coarse image, reducing the covering number. | ? | needs the author | d |
| principal (norm, estimate) | 9:235, 268 | undefined | The leading contribution of the linear inherited term, before the comparison with the block integral. | I | *leading term* | c |
| Gaussian units; stationary units | 9:242; 9s:165 | undefined | Rescaled by `g`; relative to `Ω e^{−Φ}`. | I | *in units of `g`*; *relative to `Ω e^{−Φ}`* | d |
| pure (small-field) block integral; pure integrand | 9s:12–17, 117, 130, 243; 9:969 | 9s:12–15 | "incoming activities are omitted, the prescribed path and block kernel are unchanged, and the fine-field indicator … is retained". | D | *block integral of the path action alone* | d |
| extra exponent `ψ` | 9s:38–40 | defined | Fine loop term minus the logarithm of the Haar-chart Jacobian. | D | keep with the symbol | – |
| cutoff amplitude `M = M^cut` | 9s:23; 9:137 and passim | ch. 4:411 | `exp((log log β̂)²)`; `t_m = β̂^{-1/2} M^cut`. | D (ch. 4) | *threshold ratio* (unsure); keep the symbol | c |
| truncated mass | 9s:69, 78 | 9s:67 | `N(0, A(x)^{-1}){|ξ| ≤ D}`. | R | *Gaussian measure of the ball* | – |
| retained region `𝒮_x`; retained ball | 9s:111–116, 168, 220 | defined 9s:115–116 | `𝒟_x(ρ(x) + g B̄(0, D))`. | D | keep with the symbol | – |
| live tag actions; tag-count factor; tag-coincidence radius | 9s:127, 134–135, 221 | undefined | "all live tag actions coincide with `φ`"; probably the actions for the values of the index `α` that have positive weight. | I / ? | *the actions for every `α` with `λ(U, α) > 0`* (unsure) | b |
| safe chart; chart recognition; "recognizes" | 9s:139–141, 232 | undefined | "The actual tree comparison recognizes a fine configuration as lying in a fixed safe chart whenever its fine plaquettes and … mismatches are below a fixed `δ`". Not the inequality that Dict 2.2 calls "tree comparison". | R | *lies in the chart domain whenever …* | b |
| folded (auxiliary configuration, field); folding map | 9s:169–175, 233 | 9:326–330 gives the map, unnamed | Pullback of the field under the reflection map `π_v(q) = min(q̄, 2v − q̄)`. | R | *reflected periodic extension* | d |
| microscopic (neighborhood, term) | 9s:219, 223, 233, 254 | undefined | Of radius `z^{-1}` (9s:93, 214–215). | I | *neighbourhood of radius `β̂^{-1}`* | c |
| corrected logarithm; centered expression | 9s:264, 274, 283 | 9s:266–267 | `log 𝒵 + β′ a_c + d_c`; "centered" is not explained. | R / ? | name the formula | d |
| quantum contribution `d_c`; quantum matching | 9s:259, 271; 9:291, 927 | undefined | "Let `a_c` be the prescribed coarse classical action and `d_c` its quantum contribution". Ch. 7 never uses the phrase "quantum matching". | ? | define `d_c` by a formula | – |
| shares `p_{xa}` | 9:314–316, 323 | defined | `1_{X_a}(x)/|X_a|`, weights summing to one. | D | *weights* | a |
| auxiliary tori `Λ_i`; reflection cubes, faces; reflected tori | 9:324–325, 350, 769, 932 | defined 9:324–329 | Tori of sides `2(w+i)` carrying the folded field. | D | keep | – |
| logarithmic correction `L_x`, `ℓ_a`; logarithmic label, term, selection | 9:368, 432, 607, 630–638, 671, 677, 698 | 9:367–369, 633–635 | Terms of the exponent that vanish on small-field supports. | R | *large-field correction terms in the exponent* | c |
| preparatory output; preliminary (large-field) activities | 9:394–399, 462, 637–643 | 9:397–406 | The intermediate representation (ch09:early). | R | *intermediate representation* | – |
| health domains; health event indicator | 9:563, 839 | undefined | The cases `h = 1` and `h = 0` of the small-field indicator `h_X` (ch. 4:427). The word "health" occurs nowhere in chapters 4–6, 10, 11 (grep). | R | *small-field and large-field cases*; *small-field indicator* | b |
| plaquette channel; channel `d`; low, high, raw channels; clover substitute | 9:543–546, 571, 609–612, 770, 861 | 9:543–547 | One term of the quadratic part of the path action (a plaquette term or an ordered pair of entries of a row square). | R | *term* | b |
| local projection; projection | 9:731, 746, 770, 814 | undefined | Apparently the map `f ↦ q_f` (or `Q_f`) of 9:467–470. | I | *extraction of the quadratic coefficient* | c |
| discrepancy series; scalar discrepancy | 9:517, 757 | undefined | The family of `ζ_f`; the function `f(d)` of 9:759. | I | name the objects | d |
| the reset; `C_reset` | 9:597, 599, 748 | undefined in prose | "There is a second, intrinsic way to identify the reset". The label `ch09:reset` marks `β = β′ + α + Δ`, `v_sc = τ − |Λ|^{-1} Σ f_i(1)`. | I (via label) | *the redefinition of the coupling and the constant* | b |
| attachment norm; number of attachments; strict attachment margin | 9:687, 697, 794 | undefined | The norm of 9:659 with the condition `(2B+1)^4 γ ≤ 1`. | I | *the norm (…)* | d |
| flattening | 9:676 | undefined | Replacing a family of new labels by the union of their constituents. | R | *taking the union of the constituents* | d |
| residual energy `𝒲_p` | 9:842–850, 877, 885 | defined | – | D | keep | – |
| restriction compatibility | 9:391, 815, 948 | undefined | The construction is unchanged when the parameter interval is restricted. | R | say so in words | d |
| local read diameter | 9:932 | undefined | Diameter of the largest dependence region. | I | *diameter of the dependence regions* | b |
| numerical band margin | 9:950 | undefined | A condition in the choice of scales ensuring `β` stays in the band. | ? | needs a reference | d |
| quadratic-tilt criterion; determinant inverse identity; stationary residual | 9:115; 9:140; 9:77, 130 | undefined here | References to ch. 6 by name only. | ? | replace by references | – |
| normalized affine directions; reflected normalized directions | 9:35, 502; 9s:296 | undefined here | Cf. Dict 4.2 "normalized directions". | ? | – | d |

---

#### 2. Dictionary terms

##### 2.1 Same sense (sample references)

| Term | References in these chapters |
|---|---|
| `row`, component of the action vector | 7:352, 976–977, 993, 1168; 9:544, 568, 835 |
| `row`, matrix row | 7:711; 9s:192, 197 |
| polynomial label | 2:58–75, 106, 433; 1:481 |
| label as index of a term | 9:385, 771, 816, 939 ("fixed labels") |
| tag as the random index `α` | 9:83, 85; 9s:127, 134, 242 |
| transport, parallel | 1:153–154; 2:171–176; 2e:80–83; 7:147, 1005–1009 |
| transport, stationary-field map `W`, `T` | 7:1088, 1112, 1136, 1141, 1201; 9:913; 9s:192 |
| transported (covariantised) rows | 7:975–977 |
| anchor, base point | 2e:39, 83, 126; 7:154, 619, 912, 1119; 8:76; 9:234, 462, 513 |
| anchor, real base point of a continuation | 7:733 |
| frame | 2:181; 7:272, 642–679; 9:541 |
| connector; straight | 7:636–640, 670, 693, 709–712; 7:1112, 1154 |
| forest; tree gauge | 7:574, 890–892; 9:74, 239, 924; 9s:34, 114, 189 |
| alias, principal / nonprincipal; fine residue | 7:488, 701–722, 812–816, 1135–1148; 7:585, 595, 599 |
| layer, homogeneous degree | 2e:91, 102, 131–133, 142, 151 |
| incoming / inherited / outgoing | 7:311, 1022, 1082; 9:17, 132, 204–235, 649 (22 lines in ch. 7, 27 in ch. 9) |
| stage (as in "stage bounds") | 7:22, 833, 1069; 9:110, 421, 928 — but see 2.3 |
| level | 7:15; 9:262 |
| history; schedule | 2e:253; 7:1202; 7:1075, 1206 |
| cover / covering lattice | 2:291–295, 366, 381; 2e:210 |
| torus period | 2:292; 7:324; 9:931 |
| nonwrapping / wraps | 2:352; 9:220, 463, 472 (still no criterion) |
| exact (normalised block kernel) | 1:440; 9:49 |
| block penalty `b` | 7:476, 523, 874; called "soft constraint" at 1:409, 7:574 |
| direct term, `c_dir` | 7:352–354, 974–975; 9:36, 568, 752 |
| path action | 9:21–28 (here defined as `β𝒦 + ℒ`) |
| atoms | 9:573, 837 |
| metric | 7:312, 323, 973–983, 1142; 9:567, 913 |
| clip; relaxed | 9:541, 547, 612, 861; 9:548, 840, 853, 862, 889 |
| `Bad_m` | 9:645, 882 |
| exclusion support / dependence region / exact cover | 8:336–347; 9:82–95, 407, 634–641, 890 |
| reads | 1:287; 2:179; 8:337; 9:84, 94, 457; also as a noun: 9:681, 932 |
| window; clean; remote; protected | 9:142, 278–279; 9:279; 9:280; 9:258 |
| halo | 9:84, 278 |
| frozen / active / inactive | 9:51, 58, 72–73 |
| density coordinates; scalar `v_sc` | 9:7; 9:399, 717–720, 904 |
| mismatch (i) | 9s:141, 149, 163 |
| physical (iii), original variables | 9:240, 257, 773; 9s:188, 213 |
| physical, continuum units | 1:11, 174, 202–209, 224, 329 |
| score | 9:252, 785; 9s:92 |
| witness | 9:889 |
| primitive (elementary factor); jet (ch. 6 sense) | 9:113; 9:112, 9s:255 |
| margin | 9:701, 794, 950; 9s:221 |
| supplies = gives | 1:408, 456; 2:10, 392; 2e:55; 7:113, 986; 9:870, 966 |
| assigned | 8:288; 9:280, 672, 877–889; 9s:16 |
| interface | 9:443 |
| coupling band; threshold | 9:386, 429, 949; 9:145, 430, 709; 9s:207 |
| eligible (ii), extra conditions on large-field activities | 8:294, 330; 9:94, 902, 918 |
| weight = scaling dimension | 2:50–51 (defined here, earlier than Dict's 3:168); 7:350–357, 609, 1026; 9:211–215 |
| cost | see section 3 |

##### 2.2 New senses of dictionary words

Listed in section 3: `row` (table row, row vector), `actual` (original torus; with cutoffs), `selected` (subfamily of terms), `test`, `label` (polymer label; pair `(d, c)`), `tag` (the index `d`), `mark`, `response`, `frozen` (7:733–737: weights held at their value at a real base point), `layer` (7:455 "response layers": the zeroth, first and second background derivatives), `primitive` (7:114, 125, 135: preimage under the contraction `δ`, the standard sense), `lift` (9s:189–191: the operators `W_F`, `W_a`; 9:208 "lifted potential"), `extracted` (7:1161, 9:535: coefficient taken out; 9:75: determinant factored out), `columns` (ch. 2), `spectator` (2e), `regular activity` (ch. 8), `kinetic`, `completion`, `branch`, `principal`, `centered`, `scalar`, `amplitude`.

##### 2.3 Dictionary terms that these chapters define or clarify

| Dictionary term | What these chapters add | Basis |
|---|---|---|
| parent (Dict 2.2, "used undefined") | 1:218–220: "every fine site can be written uniquely as `Ly + z` … The resulting parent map commutes with signed coordinate permutations." | R |
| insertion (Dict section 6) | 1:331–334: "A family of insertions assigns to `v ∈ 𝒯` and `y` a continuous gauge-invariant function `I_{N,p}(v, y; U)`", local on a translate of a fixed stencil. | D |
| weight (Dict 2.5) | First defined at 2:50–51, not 3:168. | D |
| inherited loop action (Dict 2.3, identification inferred) | 9:21–28: `P^path = β𝒦 + ℒ`, "`ℒ` is the quadratic loop correction. This identity defines `𝒦`, `ℒ` from (ch04:path-action)". 7:1089–1091: its coefficient matrix `r(z)` "has exponential sum bounded by `Λ^loop` and zero zeroth and first moments". So it is the `β`-independent quadratic part of the path action. | R |
| matching (Dict 4.2) | Classical: `E − J − S_3 − S_4 = O(v⁵)` with equal Hessians (7:988–998). Quadratic: subtraction of `α b_H` from the determinant symbol (7:1159–1167). | R |
| subpower (Dict 2.6) | 9:109–110: "`log P_j(𝔟)/log 𝔟 → 0` at fixed stage and ratio"; 9s:27. Agrees with Dict. | D |
| envelope (Dict 4.2, not glossed) | 9:793–794: "Their sum added to the majorant at `u_0` is a common summable envelope"; also 9:159, 690. A summable dominating majorant. | R |
| regrouping (Dict 4.2: "the cluster expansion step") | 9:651–667 is narrower: the identity "exact-cover sum of the `K_P` equals `ℱ⁰ e^{Σ ℓ_a}`". The labels call it "fusion". | R |
| Wilson initialization (Dict 4.2) | 9:818–904 is the construction: the representation of the Wilson density at the finest scale. | R |
| centered log determinant (Dict section 4) | 9s:47, 59: the exponent contains `s(x) − s(0)` with `s = ½ log det A`; 9:126 lists "centered determinant variation" with majorant `P_j(t_{m+1} + g)`. Supports Dict's presumption; the identification of the two is inferred. | R / I |
| seeded / unseeded law (Dict section 4) | 9:283–284 only: "no comparison between unrelated event indicators or a seeded and an unseeded law has been made", after requiring windows to be clean and assigning a window meeting a large-field component to that component (9:278–280). Consistent with "with / without a prescribed large-field component"; still undefined. | I |
| regularity-stage index `J_m` (Dict section 4) | Not named. 9:30–36 says `q_m` are derivative orders and `ϖ_m` spatial exponents with `q_{m+1} ≥ q_m ≥ 6`, `ϖ_{m+1} ≥ ϖ_m ≥ 2`. The constants of ch. 9 carry a subscript `j` called "stage" ("the positive stage constant `c_j^pre`", 9:421; "at fixed stage and ratio", 9:110), fixed before `L`. In ch. 7 the same subscript appears as the smoothing order (7:600, 664). Whether these are one index is not determined. | ? |
| moving (Dict section 4: "moving comparison fields") | Not that phrase. "Moving" = depending on the variable: "the moving Haar Jacobian" (7:262), "frozen weights are uniformly comparable to the moving weights" (7:734–735). | R |
| eligible (Dict 1.8 (ii), inferred) | 8:294–295: "The exact rules for eligibility are part of the definition of an effective density; they may exclude some otherwise possible covers." | R |
| compulsory; Warnings; output anchors; likelihood tests | Do not occur in these files. | – |
| width; counting; representative; lift; event label; amplitude; level | Width as in Dict (7:360, 1000, 1128, 1177). "Normalized counting measure" (7:618, 644) is the normalised version, unlike Dict's "counting norm". | R |

---

#### 3. Multi-sense words

Counts are lines unless stated.

**row** (17 lines). (i) component of the action vector / row of `ρ`: 11 (7:352, 976, 977, 985, 993, 1059, 1168; 9:544, 568, 835, 840). (ii) matrix row: 3 (7:711; 9s:192, 197). (iii) row of the displayed table: 2 (9:140, 145). (iv) row vector: 1 (1:80). The kernel, symbol, operator and factorisation senses of Dict 1.1 do not occur, though 9:568 "row coefficient matrix `S(0)`" with `c_dir I + S(0)*S(0) = I` is the factorisation written with the letter `S` where 7:974 writes `ρ`.

**actual** (54 matches: 2e 1, ch. 7 27, ch. 8 2, ch. 9 15, 9s 9).
- (i) the gauge-covariant block average and objects built with it, against "straight" or "linear": about 13 (7:504, 554, 574 "actual stationary tangent `W_a`", 780, 786, 829, 874, 888, 1114, 1154, 1200; 9:913; 9s:191).
- (ii) of this construction, against a model or a separately chosen object: about 20 (7:11, 313, 344, 498, 572, 623, 640, 764, 901, 1042, 1154; 9:239, 304, 541, 960; 9s:35, 111, 114, 138–139, 230, 299; 2e:253; 8:18).
- (iii) the running coupling: 3 (7:574; 9:17, 385).
- (iv) exact, emphatic: 6 (7:215, 333, 389; 9:284, 964; 8:269).
- (v) the full operator against the free one: 1 (7:440).
- (vi) determined by the configuration: 1 (9:890 "the actual set of these components").
- (vii) new: with its indicators and clipping, against the bare quadratic expression: 3 (9:547, 612, 861 "actual clipped … channel").
- (viii) new: the original torus or field against the auxiliary reflected ones: 3 (9:931, 936; 9s:295).
Senses (i) and (ii) are hard to separate in ch. 7; the split is approximate.

**selected / selection** (26 lines). (i) fixed by the construction: 7 (7:286, 553, 576, 667, 1202; 9:567; 7:427 "selectors" is separate, see section 1). (ii) large-field selection as in Dict 1.3: 4 (9:108, 153, 279, 440). (iii) retained for joint treatment, "selected low-order terms": 5 (9:312, 314, 319, 320, 383). (iv) new: a finite subfamily of terms or labels: 7 (9:157, 215, 637, 671, 677, 687, 890). (v) ordinary: 3 (2:292; 2e:103; 8:193). **chosen** (26 lines) is ordinary throughout, except "chosen before `L`" (7:23), which carries the order-of-constants meaning Dict records as "pre-`L`".

**test** (16 lines). (i) test function: 7 (1:353–393). (ii) classical test connection: 4 (2:13, 103, 150, 416). (iii) "curvature tests" = curvature coordinates: 1 (2e:60, title only). (iv) one evaluation of a symbol: 1 (7:215 "One transverse test"). (v) "tested" = multiplied by the indicator of a small-field condition: 2 (9:541, 547). (vi) "tested" = under consideration: 1 (9s:224). Dict's senses "location" and "variable" do not occur.

**label** (47 lines). (i) polynomial label or its index set: 18 (ch. 1: 331, 390–393, 481; ch. 2: 13 lines; 2e:254). (ii) polymer label, defined 8:24: 14 in ch. 8, plus 9:154. (iii) index of a large-field or logarithmic activity: 7 (9:221, 638, 671–684, 902). (iv) "fixed labels", the discrete data of a representation: 4 (9:385, 771, 816, 939). (v) cutoff-failure label = event label: 2 (9:111, 133).

**tag** (8 lines). (i) the index `d` of `V_d`: 2 (2:98, 99). (ii) the random index `α`: 6 (9:83, 85; 9s:127, 134, 221, 242).

**mark** (2). 7:378 "For a mark of direction `a` and Lie algebra direction `u`": an external background plane wave with that polarisation (I); not Dict's "with observable insertions". 9:263 "marking one changed factor": ordinary.

**window** (3: 9:142, 278, 279). Dict sense.

**history** (2: 2e:253; 7:1202). The renormalisation trajectory with its fixed data. Chapter 1 says "renormalization trajectory" (1:208, 465, 489), as do 2:436, 8:374, 9:974.

**source** (6). (i) generating-function source: 4 (8:252, 266, 268, 364), standard. (ii) Dict's `b_Y`: 1 (9:924 "clipped frozen source"). (iii) ordinary: 1 (9:168).

**cost / costs / costing** (32 matches: ch. 2 1, ch. 7 20, ch. 9 6, 9s 5). (i) "contributes the factor", whether small or large: about 22 (small: 7:618 "costs `O(μ⁴)`", 905–910; large: 7:619 "costs `L⁴`", 674, 749–751, 1120, 1126, 1175; loss: 7:359, 1178; 9:510, 610). (ii) a polynomial loss as a noun: 5 (9:267, 434, 438, 712; 9s:273). (iii) an increase of the exponent: 3 (9s:147 "costs at least `Δ` in the exponent", 153, 160). (iv) a small probability: 1 (2:392 "probability cost of a large-field region"). In sense (i) the word is used for gains as well as losses, so "contributes a factor" is the safe replacement. **gain** (9: 1:454; 2:391; 7:1043, 1153; 9:221, 245, 260, 264, 282): a small factor. **loss** (6: 7:1012; 8:77; 9:265, 437; 9s:160, 184): a polynomial or width loss. **fits** (7:1195; 9:201, 378, 426, 900): "is at most (a fraction of)". `price`, `pay`: none.

**detector, probe, readout, table, word**: no occurrences (the table at 9:123–134 is referred to through "rows").

**response** (6, all ch. 7; none of Dict's four senses). (i) a log-determinant as a function of the background field: 7:277 "Its determinant response is `Π_μ = ½ log det A_μ − log det G`"; 7:791 "blocked response". (ii) an operator with its background derivatives: 7:367 "the Wilson response", 624 "left-coordinate response", 743 "The kinetic response cancels". (iii) 7:454 "All three response layers": `a`, `b`, `c`. Basis I for all; nearest standard wording: *dependence on the background field through second order*.

**transport** (43 lines). Parallel transport: ch. 1, 2, 2e throughout and 7:147, 347, 643, 1005, 1009, 1178 (about 32). Stationary-field map: 7:1088, 1112, 1136, 1141, 1201; 9:913; 9s:170, 192 (8). Covariantised rows: 7:975, 977 (2). "Row transport" (1:80) is the convention of section 1.

**frame** (16 lines). All Dict's sense. In 7:873, 892 the frame is an integration variable ("fine-plus-frame coordinates", "coarse-frame directions").

**anchor** (16 lines). Base point: 15. Real base point of a continuation: 1 (7:733).

**phase** (6). (i) phase of the theory: 1:415, 418, 499 (undefined; `notation.md` restricts it). (ii) complex phase factor: 7:204, 600, 1108.

**Further multi-sense words found.**

- **insertion** (39 matches). (i) local observable at a site: 1:331, 350, 476; 2:99, 403; 8:192–193. (ii) derivative of an operator in the background field: about 27 in ch. 7. (iii) transported curvature factor: 7:147. (iv) the linear map `ℛ`: 7:243.
- **weight** (62 matches). (i) scaling dimension: 2:51; 7:350–357, 609, 1026; 9:211–215. (ii) exponential support or path-length weight: 7:165, 999, 1082; 8:16, 78, 155, 176–177, 362; 9:179–182, 231, 283, 438, 516. (iii) the Fourier weights `h_l` and the weighted Hilbert norms: 7:589–751 and 870–916 (about 20). (iv) numerical coefficients: 7:299 "bubble weights"; 9:355 "fourth-difference weights"; 8:54 "probability weights". (v) density factors: 9:264 "nonquadratic local weights".
- **common** (45 matches). (i) volume-independent, defined 7:36: most of ch. 7. (ii) shared or joint: 7:154 "common anchor"; 9:115, 139, 266, 785, 966 "common law"; 1:490, 503.
- **scalar** (28 matches). (i) zero-form or frame component: 7:507, 580, 591, 696–703, 721–722, 915. (ii) field-independent constant: 8:359; 9:56, 399, 717, 757, 764, 814, 904; 9s:123. (iii) number-valued: 7:124, 134, 207, 214, 508, 519, 686; 9s:20.
- **sector** (15 lines). (i) reflection half: 1:244, 247. (ii) Dict's: 8:28, 359; 9:50, 75, 81, 105, 305, 436; 9s:16, 170, 299.
- **branch**. (i) branch of stationary solutions: 10 lines (above). (ii) branch of the logarithm: 8:129. Dict's "case of a definition" does not occur.
- **channel**. (i) vector or ghost field type: 7:331, 414. (ii) term of the quadratic path action: 8 in ch. 9.
- **centered**. Symmetric: 1:183, 217; 2:188, 285; 7:407, 704. Frame normalised in the mean: 7:505–700, 883, 914. Zero-mean Gaussian: 9:774. With a constant or the flat value subtracted (inferred): 9:126, 294; 9s:236, 283.
- **principal**. Zero alias: 7:701–722, 812–816, 1146. Leading: 9:235, 268.
- **amplitude**. Fourier amplitude: 7:815, 1136, 1144–1145, 1173. Bound: 7:1196. `M^cut`: 9s:23.
- **logarithmic** (23 matches). Lie-algebra coordinate: 9s:33, 176, 295. Term of the exponent: 9:368, 607, 633–698. Logarithmic derivative: 7:522, 673; 9:247. Of a log-determinant: 7:335. In `log β`: 1:50, 462; 9:712 (the last is unclear).
- **fold**. Aliasing sum: 7:810. Reflected extension: 9s:169–175, 233.
- **flat**. `U = 1`: 7:24, 226; 9:332, 496, 726. "Flattening": 9:676.
- **auxiliary** (24). Regulated fine determinant: ch. 7 (8). Small reflected tori: 9 and 9s (16).
- **degree**. Polynomial degree; Taylor degree = field factors (7:1079); number of elementary factors (9:172).
- **path**. Lattice path; path action (section 1); matrix path `M(t)` (7:397).
- **cutoff**. Ultraviolet cutoff `N` (1:15, 209, 387; 9:947); threshold or indicator (7:25; 9:111, 840; 9s:10, 127); cutoff function (9:476). Agrees with Dict 1.8.

**Occurrences fitting none of the senses:** 7:1059 "the prescribed coarse quadratic row" (singular; presumably the whole quadratic term `J`); 9:712 "polynomial logarithmic costs"; 7:461 "recording estimate"; 9s:283 "centered expression".

---

#### 4. Terms these chapters do not determine

| Term | Where | What can be said |
|---|---|---|
| fixed-position read; coordinatewise splice | 7:637, 710 | See section 1. |
| recording (estimate) | 7:461, 742 | `notation.md` has "recording-scale change" for ch. 11; no definition here. |
| thermal | 7:765 | Known only through the label of `T(v)`. |
| bridge legs | 7:597 | Known only through the label `ch05:actual-bridge`. |
| padded block | 7:599, 628 | Probably the macro-box. |
| exterior identity | 7:408, 686 | Not displayed. |
| direction selectors | 7:427 | – |
| live tag actions; tag-coincidence radius | 9s:127, 221 | – |
| seeded / unseeded law | 9:283–284 | Section 2.3. |
| dummy Gaussian coordinates; missing-coordinate factor | 9:59, 72, 77 | – |
| derivative reserves | 9:34 | – |
| "factor after deterministic subtraction" | 9:124 | Which subtraction is not said. |
| quadratic-tilt criterion; determinant inverse identity; stationary residual | 9:115, 140, 77 | Chapter 6 by name only. |
| read-count polynomials; support compression; inspected support | 9:147, 231, 220 | – |
| normalized affine directions; reflected normalized directions | 9:35, 502; 9s:296 | – |
| quantum contribution `d_c`; prescribed coarse classical action `a_c` | 9s:258–259 | No formula. |
| centered (expression, auxiliary bound) | 9:294; 9s:283 | – |
| numerical band margin | 9:950 | – |
| nonautomatic relaxed small-field condition | 9:548 | – |
| the stage index `j` | ch. 7 and 9 subscripts | Section 2.3. |
| `c_lin` | 9:846 | Not defined in these files. |
| slots | 1:314 | – |
| phase (of the theory) | 1:415, 418, 499 | Deferred to later chapters. |

---

#### 5. Synonym clusters

| Concept | Words in use |
|---|---|
| the operator `W` (coarse field ↦ stationary fine field) and its versions | "stationary tangent" (7:574, 780, 882), "transport" (7:1112 "straight stationary transport `W_s`"), "lift" (9s:189–191 "forest-coordinate lift `W_F`", "smooth actual lift `W_a`"), "representative" (7:574 "its forest representative is `W_F`"), "fine-wave amplitude of the transport" (7:1136) |
| the critical-point map | "stationary branch" (ch. 7, 9, 9s), "stationary representative `ζ(x)`" (7:505), "stationary chart" (7:867), Dict's "stationary graph" |
| the constant `b` | "soft constraint" (1:409; 7:574), "block penalty" (7:523, 874), "penalty Hessian" (7:476), "block parameter" (1:420) |
| the index `d` of `V_d` | "tag" (2:98), "normalization index" (2:402), "filtration index" (`notation.md`) |
| transported plaquette curvature | "transported curvature" (2:171), "curvature measurement" (2:362), "curvature coordinate" (2e:65), "curvature test" (2e:60), "curvature insertion" (7:147) |
| sequence of scales and couplings | "renormalization trajectory" (1:208, 465; 2:436; 8:374; 9:974), "history" (2e:253; 7:1202), "scale schedule" (7:1075, 1206) |
| one-parameter family of density data | "curve" (9:768, 903, 938), "activity curve" (9:390) |
| lower bound | "floor", "gap" (9s:42, 138), "margin" |
| lower bound on `β̂` | "threshold", "inverse coupling threshold", "coupling threshold", "coupling entry threshold" |
| the reference coupling `β̂_{m+1}` | `𝔟` (9:17) and `z` (9s:19) |
| the polymer-activity norm | "site norm" (8:69), "support norm" (8:196), "containing-site norm" (9:518), "attachment norm" (9:697) |
| the margin `δ` | "additional exponential support decay" (8:150; 9:148, 687), "support-weight reserve" (8:362; 9:438), "support reserve" (9:919), "unused support exponent" (9:267) |
| small-field indicator `h_X` | "event indicator" (11 matches in ch. 9), "health event indicator" (9:839), "small-field conditions" (9:510) |
| the gas of small-field polymers | "regular" (ch. 8), "ordinary" (ch. 9) |
| the set `I_η` | "large-field sites assigned to that activity" (8:288), "prescribed large-field site set" (9:643), "prescribed set" (9:893) |
| the identity of Proposition 9:651 | "exact regrouping", "absorbing", "fusion" (labels), "exact reassembly" (ch. 8, for the related identity) |
| event label | "cutoff-failure label" (9:111), "event label" (ch. 6) |
| enlarged block | "padded block" (7:599, 628), Dict's "macro-box" |
| link | "link" throughout; "bond" at 9:58; "edge" at 7:204, 349; 9:456 |
| summable majorant | "envelope" (9:159, 690, 793–796), "majorant" (9:124, 607, 655) |
| field-independent constant | "scalar" (ch. 9), "field-independent term" (9:714), "scalar normalization" (9:904; 9s:123), "scalar factor" (8:359) |

---

#### 6. Overloaded symbols noticed

| Symbol | Meanings |
|---|---|
| `W` | stationary-field operators `W`, `W_a`, `W_s`, `W_F` (7:506, 574, 1112); Wilson plaquette energy `W(u)` (9:823), written `w(u)` at 1:92; bound on coordinate counts (9s:152); `W = d_c − ψ − ½ log det A` (9s:262) |
| `W_a` | "smooth actual" representative, distinct from the forest one `W_F` (7:574; 9s:189–191). `blueprint/notation.md` line 242 speaks of "the actual forest-coordinate response `W_a`", which contradicts this. |
| `H` | two-form metric (7:312, 974); "block average derivative" (7:476); coarse symbol `H(p)` (7:1138); `H_pre` (9:420); `H_4` |
| `B` | penalty Hessian (7:476); `B_x` (7:649); covector `B(u, v)` (7:896); block radius `B = B_m` (9:16); family `B ∈ 𝔠(D)` (8:289); bounds `B_H`, `B_loop` |
| `Z` | coarse-frame projection (7:477); `Z(x) = S_x(r(x))` (7:527); tensor in a proof (7:123); `Z = X ∪ N_2(o)` (9:463); partition functions |
| `K` | `K = m_μ X` (7:477); operators `K_c`, `K_f`; constant (7:77); large-field activities `K_η`, `K_P`, `K_I`; `𝒦` path action (9:23); norm `𝒦_m` (9:665); exponent `K` (9:299) |
| `M` | `M_μ`; matrix path (7:397); `M_act`, `M_core`; mixed kernel `M(p)` (7:562); straight averaged connector (7:693); `M^cut`; `M = (2q)⁴` (1:289); number of measurements (2:243); `M_x` (9:320); `M_i` (9:807); index set in `G_M` (9:99) |
| `R` | regrading `R_d` (2e); gauge action `ℛ`; resolvent (7:418); `R(T)` (7:652); block-average correction (7:694); loop bound (7:1160); `R_f` (9:486); Wilson remainder `R(u)` (9:832); `R(g, x)` (9s:61); dependence radius (9:322); physical period `R_p` |
| `S` | spectator function (2e:39); `S_W` (2e:115); `𝒮(J)` (2:242); `S_x(a)` (7:526); joint action `𝒮` (7:872); loop symbol `S(p)` (7:1094); `S_3`, `S_4`; row coefficient matrix `S(0)` (9:568, the `ρ` of 7:974); region `𝒮_x` (9s:116); Schwinger kernels `S_n` |
| `T` | `T(v)` (7:233); `T = |k| + μ` (7:397); stationary tangent `Tu` (7:882); two-form map (9s:194); `T_4` (9:828); `T_d` (2e:229); `T_d f` (2:256); Lie-algebra element (9:464) |
| `F` | curvature; gauge condition (7:251); frame `F_x` (7:642); force `F_e` (2e:117); `F_d`, `F` (9:552, 574); `F_x` (9:319); `ℱ⁰`; `ℱ_d` (2e:227); observable (1:265) |
| `J` | jet (ch. 2); action `J(v)` (7:976, used at 7:185 before its definition); `J = −K_c` (7:539); joint Hessian `𝖩` (7:242); `J_0` (7:648); `J_d`, `J` (9:553, 575); `J_Haar` |
| `E` | action difference (7:51); stationary value `E(v)` (7:938); `E_{xy}` (7:643); `E = Σ h_Z R_f + F` (9:590); `E` (9s:239); norm `ℰ_m`; projection `ℰ` (2e:152); edge set `E_s`; energy `E_s^W` |
| `L` | block ratio; `ℒ` loop action (7:237; 9:26); cluster series `𝓛(z)` (8:111); `L(g, x)` (9s:62); `L_x` (9:337); `L_d`, `L_p` (9:546, 861); constants `L_0, L_1, L_h` (9:597); Lipschitz constant `L_0` (9s:212) |
| `h` | scale parameter (2:112); element of `H_4`; half side (1:242); weights `h_l` (7:587); integrand `h(k)` (7:303); `h = 𝔟^{3/8}` (9:176) and `h = 𝔟^{-7/16}` (9:295; 9s:20); indicator `h_X`; constant in `|X| ≤ h c(X)` (8:59) |
| `z` | polymer activity (ch. 8); reference coupling (9s:19); internal coordinates (7:873); displacement (7:146); Gaussian variable (9:63); position in a block (1:219) |
| `q` | `q_a(p)` (7:50); `dim 𝔤` (9:60); orientation pair (9:464) and `q_f`; smallness (8:148); derivative order (2:337; 9:32); cyclic coordinate (9:326); `2q` strips (1:284) |
| `g` | `β′^{-1/2}` (9:60; 9s:19); gauge transformation; local inverse (2:250); tensor (7:78) |
| `D` | `D_m`; dimension (9:60); `D = d_0 M` (9s:24), where `d_0` is also the lattice differential; large-field set (8:284); division `D_a`; derivative |
| `α` | quadratic coefficient `α(f)`, `α_{N,m}`; decay exponent (8:69); basis index (1:32); the random index in ch. 4–6 |
| `γ` | polymer label (ch. 8); lattice path; `γ_0` bound (8:145) and Gaussian measure (9s:57); Hessian gap (9s:142); bound (9:659) |
| `ρ` | density data `ρ`, `ρ′` (9:48); row operator (7:974); stationary branch `ρ(x)` (9s:36); radius (8:242) |
| `μ` | Wilson measure; direction index; `μ = L^{-1}` (7:267); mean (9:63) |
| `c` | support-size function (8:56, with a warning at 8:66); polynomial label (2:97); coefficients `c(z)` (7:170); second insertion (7:332) |
| `κ` | `κ_G`; exponent in 9:657 |
| `w` | plaquette energy (1:92); width (7:165, 1128); `w = 4R + 100(1+B)` (9:323); `w_x(v)` (7:521); `w = 𝒞^{-1}B` (7:929); scaling dimension `w_i` (2:67) |
| `P` | sections `P_d^loc`; volume map (1:372); `P_μ`, `P_f`; block Fourier transform (7:585); nearest-group map `𝒫` (7:645); polynomials `P(A)`, `P_j`; selection `P` (9:637); `P^path`; polymer set `𝒫` |
| `N` | cutoff; `N_fac`; amplitude `N_l` (7:1136); number of free links (9s:122); neighbourhood `N_r(x)`; Gaussian law |
| `C_G` / `C_𝔤` | the adjoint Casimir is `C_𝔤` at 1:35 and `C_G` at 7:15 |

---

#### 7. The ten most confusing terms

1. **actual** — 54 matches, eight senses; in ch. 7 the reader cannot tell "gauge-covariant, not linear" from "of this construction" from "exact".
2. **response** (ch. 7) — a log-determinant, an operator with its background derivatives, or the triple of orders; a fifth and sixth sense beyond Dict's four.
3. **insertion** — a local observable (ch. 1, 2, 8), a derivative in the background field (ch. 7), a curvature factor (7:147), a linear map (7:243).
4. **fixed-position read / coordinatewise splice** (7:637, 710) — undefined; a load-bearing step of the frame estimate.
5. **regular activity** — a polymer activity in ch. 8, an additive term of the exponent in ch. 4 and 9; ch. 9 says "ordinary" for what ch. 8 calls "regular".
6. **the reset / health / thermal / bridge / fusion** — words that reach the prose (9:748, 9:563 and 839, 7:765, 7:597) or only the labels, and are intelligible only through the label names.
7. **weight** — scaling dimension, exponential support weight, Fourier weight `h_l`, numerical coefficient, density factor; several within single paragraphs of ch. 7 and 9.
8. **cost** — used for small factors, large factors and energy increases alike; 7:618–619 has both directions in consecutive sentences.
9. **stationary tangent / transport / lift / representative** — four words for the operators `W`, with subscripts `a`, `s`, `F`, and a contradiction with `notation.md` on `W_a`.
10. **selected / selection** in ch. 9 — the large-field selection, the low-order terms retained, and arbitrary finite subfamilies of labels, within one chapter.

Close behind: **transfer matrix** (1:473), a standard term used for the mixing matrix of labels; **contact term** (7:501), not a coincident-point term; **scalar**; **stage**; **common**; **path** for "path action".

---

#### 8. Not read / not checked

- All seven assigned files were read in full. The figure files input at 1:304, 2:184, 8:300 (`figures/*.tex`) were not read.
- Definitions in other chapters were checked only by `grep` in `04-blocking.tex`, `05-gaussian.tex`, `06-large-fields.tex`, `10-*.tex`, `11-*.tex` for: health, live tag, folded, seeded, affine Hessian, cutoff amplitude, padded, bridge, thermal, event label, eligibility, dummy, splice, reserve, halo, `h_X`, `M^cut`. Those chapters were not read; chapters 12–18 were not searched.
- The occurrence classifications for `actual` and `cost` rest on the full read plus the grep line lists; the split between senses (i) and (ii) of `actual` could shift by a few lines.
- Dictionary line numbers refer to commit `7bec3925`; the ones that point into these files (7:237, 7:974, 7:1160, 9:283, 9:573, 9:837) agree with the worktree.
- No proposed equivalent was checked against the literature. No Lean source was consulted.
- Sections 5 and 6 list what was noticed while reading; they are not exhaustive.

### III.B Independent audit

*Original title: Audit A: Part III.A*

> **Status.** Independent check of Part III.A by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in Part I, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Independent read-only check against the worktree `manuscript/HumanizeYM_v3/`. All seven chapter files were read in full (`01-lattice`, `02-observables`, `02-equation-section`, `07-matching`, `08-polymers`, `09-renormalization`, `09-stationary-remainder`), plus sections 1–4, 8, 9 of Part II and all of Part I. Occurrence counts were redone with a script that strips `\label`, `\ref`, `\eqref`, `\input`, `\cite`. Other chapters were consulted only by grep and short excerpts. No repository file was edited.

Abbreviations as in the survey: `1`, `2`, `2e`, `7`, `8`, `9`, `9s`; other chapters by number.

**Overall verdict.** The survey is largely reliable: nearly every cited line contains the term, the quotations are essentially verbatim, and the per-sense counts hold to within a few. The real defects are (a) two sense misfilings (`stage`, `block-completed`), (b) about ten terms called undetermined or "by name only" that other chapters, or an explicit cross-reference in chapter 9, settle or narrow, and (c) a handful of omitted house terms.

---

#### Definite errors

1. **`block-completed` (7:687) is filed under gauge completion, but is a different completion.** The survey row "gauge completion; completed, block-completed" gives the meaning "Adding `F*F` (or `d_U d_U*`) to a gauge-degenerate Hessian". At 7:687–691 "The block-completed form needs a quotient estimate. In centered coordinates it is `𝒢(u,r) = ⟨u,K_f u⟩ + b|Mu − d_{0,c} r|²`": the kinetic form completed by the *block penalty*, still gauge-degenerate. The gauge term is added afterwards (7:728–729 "a positive weighted floor for `𝒢 + F*F`"). The proposed equivalent "gauge-fixed Hessian" is therefore wrong for 7:687. (7:773 "blocked completed matrix `C_0`" does appear to include both.)

2. **`stage` is filed in section 2.1 as "same sense" as the dictionary; it is not.** Dict 2.1 has stage = "one renormalisation transformation, or its index". In these chapters it is the regularity class with subscript `j`: 7:22 "fixed stage bounds … chosen before `L`", 7:1069 "a finite collection of stage data", 9:110 "at fixed stage and ratio", 9:421 "The positive stage constant `c_j^pre`", 9s:83 "finite-stage requirements", 9s:214 "fixed-stage derivative bounds". This is the sense defined at 10:25 ("A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds"). None of the 14 prose lines (7:22, 833, 1056, 1067, 1069, 1072, 1203; 9:110, 421, 427, 928, 935; 9s:83, 214) means "step". The survey hedges with "but see 2.3" but the filing is wrong.

3. **`quadratic-tilt criterion` is not a reference "by name only".** Survey section 1 (last rows) and section 4 say "References to ch. 6 by name only" / "Chapter 6 by name only". 9:115–116 reads "The alternative quadratic-tilt criterion in Proposition~\ref{ch06:common-majorant} is not required here": an explicit proposition reference. That proposition (6:1123–1138) assumes "(ch06:majorant-form)–(ch06:quadratic-control), with uniform polynomial moment bounds for `P_k` under the corresponding tilted Gaussians". The overview section 4 repeats the error.

4. **`history` is filed in 2.1 as the dictionary sense but glossed otherwise in section 3.** Dict: the list of block ratios and averaging orders. Survey section 3: "The renormalisation trajectory with its fixed data". The text supports the second: 7:1202–1203 "an entire selected history requires that its incoming paths obey the fixed stage bounds" (a history has incoming paths), 2e:253 "the section used along the actual renormalization history". The two sections of the survey contradict each other; 2.1 is the wrong one.

5. **Symbol mis-transcribed in a quotation.** Row "gauge completion": "put `C = J + F*F`". The text (7:251–252) has `C=\mathsf J+F^*F`, the joint Hessian `𝖩` of 7:242. `J` is a different object in the same chapter (the action `J(v)`, 7:976; `J = −K_c`, 7:539), which the survey's own section 6 lists separately.

6. **Section 4 lists `slots` as undetermined although the text states what they are.** 1:314–315 "The slots are the `2q` strips in that coordinate". Section 1 gives the same row Basis I. It is R, and does not belong in section 4.

---

#### Basis codes that overstate or understate

Overstated:

- **health domains (9:563), Basis R.** The text never says what "health" is. 9:563 "The equality follows on each of the two health domains" is read through the factor `(1 − h_{Y_d})` at 9:553, and 9:839 "write `h_p` for the health event indicator on its vertices" through 4:427 "write its indicator as `h_X(U)`". Correct reading, but it is I.
- **`moving` (2.3), Basis R.** "the moving Haar Jacobian" (7:262) and "comparable to the moving weights" (7:735) do not say "depending on the variable"; I.
- **`mark` in the overview (2.6)** is stated flatly as "in 7:378 an external plane wave". The survey marks it I; the overview drops the qualifier.
- **lattice family, R / I** is honest; no change. Listed here only because the overview does not carry the I.

Understated (text is more explicit than the code says):

- **slots (1:314), I → R** (see above).
- **adjacent pair (9:15), "R / I" → D** for the pair: "Fix one adjacent pair of scales, with fine scale `m+1` and coarse scale `m`".
- **classical bound contraction / inherited-loop contraction (9:970), R → settled.** 10:35–36 names them with equation references: "the classical contraction (ch07:classical-budget), inherited-loop contraction (ch07:inherited)". The survey's identification is correct and can be stated as fact.
- **dummy Gaussian coordinates, I / section 4 "–".** Partly R: 9:59 "`D` be the dimension after dummy Gaussian coordinates have been added"; 9:72–73 "The dummy Gaussian integral equals one after the inactive Haar variables have been frozen".
- **affine Hessian: "keep, define at first use".** It is defined, at 4:627–640 ("The meaning of the affine Hessian condition is fixed in the chosen local coordinates"); the survey cites those lines but then proposes defining it.

---

#### Sense misassignments (with my per-sense counts)

**actual.** 54 matches confirmed if "actually" (7:504) is counted; 53 of the word itself (2e 1, ch. 7 26 + "actually", ch. 8 2, ch. 9 15, 9s 9). Survey senses and my counts:

| Sense | Survey | Mine | Remarks |
|---|---|---|---|
| (i) gauge-covariant block average and objects built with it | about 13 | 14–15 | 7:504 is "actually used", not "actual". 7:1042 "The actual smooth tangent bounds" is `W_a` (5:1129–1132), so (i) not (ii). 9s:230 "the actual stationary tangent" is the phrase the survey puts in (i) at 7:574, yet it is filed in (ii). 7:786 and 7:829 are borderline (ii). |
| (ii) of this construction | "about 20" | 22–24 | The survey's own list has 24 entries, not about 20. |
| (iii) running coupling | 3 | 3 | 7:574, 9:17, 9:385. Confirmed. |
| (iv) exact, emphatic | 6 | 5–6 | 9:964 "the actual quadratic coefficient … cannot be replaced by unrelated bounds of the same numerical size" is (ii), judgement. |
| (v) full operator against the free one | 1 | 1 | 7:440. This is a zero-background lattice denominator against the free continuum one; see the overview section below. |
| (vi) determined by the configuration | 1 | 1 | 9:890. |
| (vii) with indicators and clipping | 3 | 3 | 9:547, 612, 861. |
| (viii) original torus or field against reflected | 3 | 3 | 9:931, 936; 9s:295. |

"actual sector" (9:304; 9s:299 "actual-sector inputs") is a fixed compound from chapter 6 (6:439 section title "The actual sector Gaussian"); the survey files both lines under (ii) without noting this.

**row.** 17 lines confirmed. (i) 11, (ii) 3, (iii) 2, (iv) 1 all correct. 7:1059 is listed both in (i) and under "fitting none".

**selected / selection.** 26 lines confirmed (2:292; 2e:103; 7:286, 427, 553, 576, 667, 1202; 8:193; 9:108, 153, 157, 215, 279, 312, 314, 319, 320, 383, 440, 567, 637, 671, 677, 687, 890). (i) 6 plus "selectors" 7:427; (ii) 4; (iii) 5; (iv) 7; (v) 3. All assignments correct. 9:215 "Every surviving selection in the ordered Taylor expansion" is a choice of one term per factor, slightly different from "finite subfamily of labels" but close enough.

**test.** 16 lines confirmed; assignments correct. One merge to consider: (v) "tested" (9:541 "the tested and clipped density of (ch04:path-action)", 9:547) is the dictionary's indicator sense used adjectivally (4:489–493 "tests … automatic", "the remaining tested plaquettes"), not a new sense. (vi) 9s:224 "each tested small-field coarse configuration" is inferred.

**label.** 46 prose lines (survey 47; 1:390 is the LaTeX option `[label=…]`, wrongly included in "390–393"). (i) 17 not 18; (ii) 14 + 9:154; (iii) 8 not 7 (9:221, 638, 671, 674, 676, 678, 684, 902); (iv) 4; (v) 2. Misassignments: 9:221 "the per-label gain is `L^{-5}`" is the index of an incoming *regular* activity, not of a large-field or logarithmic one; 8:290 "families `B` of such labels" are the large-field labels `η`, not polymer labels `γ`. Section 3 also folds the pair sense `v = (d,c)` (2:97) into (i).

**tag.** 8 lines, 2 + 6. Confirmed.

**mark.** 2. Confirmed (7:378 is I).

**window.** 3. Confirmed.

**history.** 2. See definite error 4.

**source.** 6: 4 + 1 + 1. Confirmed.

**response.** 6, all ch. 7. Confirmed.

**transport.** 42 lines (survey 43). Parallel 32, stationary-field family 8, covariantised rows 2. One refinement: 9s:170 "the curvature transport" and 9s:192 "the two-form transport" are the map `T` on two-forms (9s:194 `d_{1,f}W_a = H_f^{-1}TH_c d_{1,c}`), not `W`.

**New-sense words of section 2.2.**
- `lift`: the survey cites only 9s:189–191 and 9:208. It misses 7:131–135 ("zeroth-factor lift", "first lift", "scalar lift"), where lift = primitive under the contraction `δ`, i.e. Dict 4.2 sense 1, and 1:181 (covering lifts).
- `completion`: two senses, see definite error 1.
- `frozen` (7:733–737), `layer` (7:454–455), `primitive` (7:114, 125, 135), `extracted` (7:1161; 9:75, 535): confirmed.

**Other counts.** cost 32 (1/20/6/5) confirmed; gain 9, loss 6, reserve 4, share 4, spent 1, unused 2 confirmed; `fits` 5 lines. `sector`: the survey says 15 lines but lists 13, and 13 is right. `frame` 16, `anchor` 16, `phase` 6 confirmed. `centered`: 7:704 should be 7:703; the sense "recentering" at 9:350 (translating the reflection cube) is missed. `rooted` has a second sense the survey does not record: rooted cluster sums (8:15, 116, 170, 179; 9:179, 197, 685, 796, 894) against rooted coordinates (7:521, 674, 693).

---

#### Wrong line references and misquotations

- factor count: "2e:… 187 (def.)". The definition is at 2:52–53 (as the same row says); 2e:186–187 is an ordinary use.
- label (i): "ch. 1: 331, 390–393". 1:390 is `\begin{enumerate}[label=…]`; the prose line is 393.
- actual (i): 7:504 reads "actually used".
- centered: 7:704 → 7:703 ("centered box sums").
- insertion (2.3): the quotation "assigns to `v ∈ 𝒯` and `y` a continuous gauge-invariant function" silently drops "`∈ Λ_{R_pD_N}`" (1:332).
- gauge completion: `J` for `𝖩` (definite error 5).
- 2.3, regularity-stage row: "the same subscript appears as the smoothing order (7:600, 664)". 7:600 has no subscript ("fixed at the given smoothing order"); 7:664 has `C_j`.

All other cited lines I opened contain the term or object, and the other quotations are verbatim up to line breaks. Checked in particular: every quotation in sections 1, 2.3 and 3.

---

#### Omitted terms

House terms in these files that the survey does not list:

- **sector allocation indicators** (9:81–82 "retain all sector allocation indicators"): Dict 1.8 `allocation` (i), the partition-of-unity weights of 6:67–79; "allocation sector" 6:85.
- **kills** (7:201 "The Ward identity first kills the constant term"; 9:525 "An axis reflection kills off-diagonal orientation pairs"). The overview has the cluster but no chapter 7/9 reference.
- **collision diagonals, collisions** (1:365, 426, 477): Dict 2.5 term, absent from the survey's section 2.1.
- **the unit** for the constant polynomial or constant section (2:192, 260, 281, 400; 2e:227, 236).
- **trace-class cube** (7:495, 745): `P_μ³`.
- **trial inverse coupling (correction)** (9:411, 756–757).
- **matched** (7:982, 1073 "matched coarse metric"; 9:410 "matched determinant coefficient"; 9:738).
- **pulled back / pullback** of the loop action by the stationary map (7:1085, 1120, 1150–1151).
- **placements** (7:753 "bounded in both placements needed for `d_U^*d_U` and `d_Ud_U^*`"; 1:322 in another sense).
- **Plaquette filling bounds** (9s:175).
- **pass the cutoff** (9s:126–127).
- **local-integral estimate / bounds** (7:1075, 1205; 9:34) and **one-step integral identity** (7:859): references by nickname.
- **exchange symmetry** (7:195), unrelated to "exchange term" in the survey.
- **occurrences** (8:85, emphasised and defined) and **distinguished occurrence** (8:193).
- **integral shear** (7:118); **principal real cube** (7:704–705); **interpolated link fields** (7:817).
- **bidegree** (2:79, 91): written (scaling dimension, factor count), e.g. "(4,2)", while 2e:34–35 orders the pair "(factor count, scaling dimension)". A notational inconsistency more than a term.
- **raw** (2:404 "raw constant section"; 9:571 "raw channels" is listed).

---

#### Questionable equivalents

- **left-coordinate Hessian → "Hessian in left-invariant coordinates".** Misleading. The increments act by left multiplication (2:320 `F((exp(εA_e)U_e))`; 7:362–363), whose generators are right-invariant vector fields. I would write "second derivative in left-multiplication increments". I am sure of the mathematics; I do not know a fixed standard phrase.
- **gauge completion → "gauge-fixed Hessian".** Fine for `𝖩 + F*F`; wrong for 7:687 (definite error 1).
- **padded block → "enlarged block", "Probably Dict's macro-box".** The macro-box has radius `(j+7)L` (4:298). 7:599 says "the fixed padded block average patch … its number of residue blocks is fixed at the given smoothing order", which matches the block-average patch `Ly + 𝔹_R`, `R = (j+3)L`, of 4:17 and 4:172–173. Which is meant is not determined, but the wording favours the patch. The overview's cluster "enlarged block: padded block, macro-box" inherits the guess.
- **safe chart / tree comparison.** The survey says 9s:139 is "Not the inequality that Dict 2.2 calls tree comparison". True, but the text supplies the object: the nonlinear estimate (ch05:nonlinear-tree), 5:1009–1015, in the subsection titled "The tree comparison and the actual Hessian" (5:1000), from which the Dict inequality (5:1035–1040) is derived. Equivalent: "by the nonlinear tree estimate (…), a configuration with … below `δ` lies in the chart".
- **defects → "large-field sites".** Plausible, I; "large-field regions" is the usual phrase.
- **first expansion → "Mayer expansion".** `e^V = 1 + (e^V − 1)` with connected components is the standard Mayer / polymer step; acceptable. "Second cluster expansion → cluster expansion of the logarithm" is accurate.
- **contact term → "second-order block-average correction to the determinant".** Not standard, as the survey says; mathematically accurate (7:521–545).
- **transfer matrix → "mixing matrix".** Good; the remark on the standard meaning is correct. The phrase occurs nowhere else under `chapters/`.
- **regrading → "unipotent (triangular) automorphism".** Accurate (2e:229–233).
- **cutoff amplitude → "threshold ratio".** Flagged unsure by the survey; I have nothing better.
- **site norm → "weighted polymer-activity norm"**, **floor → "lower bound"**, **denominator → "inverse propagator"**, **exchange term → "tree term with one propagator"**, **refinement → "subsequence"**: acceptable.

---

#### Overview claims (errors / confirmed)

**Errors or imprecisions.**

- **Section 2.1 table, column "ch. 7, 9".** (a) "about 20" for "of this construction": the survey's list has 24 entries; the eight rows as given sum to 50, not 54. (b) The "1" in the row "nonlinear / at the non-flat background, against flat or linearised" is the survey's sense (v), 7:440 "The actual denominator minus the free quadratic denominator". That denominator is the zero-background one (7:331 "zero-background denominator"); the contrast is regulated lattice against free continuum, not non-flat against flat. (c) The column silently includes 2e:253 and 8:18, 269.
- **Section 2.4**, "Borel condition, its indicator … ch. 4–6 only": 9:541 and 9:547 "tested" are that sense. The table also omits 2e:60 ("Curvature tests"), 7:215 ("One transverse test") and 9s:224.
- **Section 2.10**, "Chapters 5 and 6 use stage for a step": nothing is said of chapters 7 and 9, where all 14 uses are the chapter-10 sense. The history sentence does not place 2e:253 or 7:1202.
- **Section 4, chapters 7, 9 list.** `quadratic-tilt criterion` is not undetermined (definite error 3). `derivative reserves` is narrowed by 10:737–739. `bridge legs` and `thermal` are label leaks with identifiable objects (`W_a` bound 5:1128–1133; `T(v)` 7:231–234). `dummy Gaussian coordinates` is partly stated at 9:59, 72–73.
- **Section 5**, "coincident points: collision, contact, diagonal": in chapter 7 "contact term" (7:501–568) is not a coincident-point term, as the survey itself notes; the cluster needs that exception. "Enlarged block: padded block, macro-box": see above.
- **Section 2.6**: 7:378 stated without the inference flag.

**Confirmed.**

- Section 1 bullets on chapters 1, 2, 8 and 7, 9; absence of `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund` in prose of my files (`budget` only in labels 7:422, 7:1055).
- Section 2.2 `row` references (7:1059 omitted but harmless); 2.3 `selected` references; 2.5 `label`/`tag` references including "defined 8:24"; 2.7 chapter 7 line list; 2.9 `window` (9:279 also); 2.11 `insertion` ("about 27" in ch. 7: I count 28) and `weight`.
- Section 3: inherited loop action (9:21–28, with 4:516–523 supporting "`β`-independent quadratic part"); eligible (8:294–295; fuller definition at 4:440–450); subpower (9:109–110); envelope (9:793–794); matching (7:988–998, 1159–1167); parent (1:218–220); centered log determinant (9s:47, 59, inferred as stated); seeded / unseeded still open (9:283–284; 6:1544 only other occurrence).
- Section 5 rows citing my chapters: constant `b`; small-field part; polymer-activity norm; subsequence; cost for gains and losses (7:618–619); lower bound on a parameter; kill (7:201, 9:525).

**Section 6 (broken sentences).** No line in my chapters is cited there (6:730 is chapter 6, outside my scope; not reread). Further broken or damaged sentences found in my chapters:

- 9:212 "Invariance under constant gauge transformations remove linear curvature terms," (subject–verb).
- 7:1083–1088 "We prove the estimate [display ending with a full stop] from the transports of Chapter 5." The sentence continues after a terminated display.
- 9:547–548 "Its support `Y_d` contains both paths and every nonautomatic relaxed small-field condition." A support containing a condition; apparently "test" (as a plaquette) replaced by "condition".
- 9:949 "Output inverse coupling-band membership additionally requires" (hyphenation after replacing "coupling").
- 9:893–894 "A connected prescribed set of `r` large-field sites is bounded in number by a rooted spanning-walk count."
- Noun stacks that look like replacement residue but still parse: 9:108 "its selected large-field condition set"; 9:636 "Their extra large-field indicator dependence regions are retained"; 9:839 "the health event indicator"; 9:840 "its row cutoff condition".
- Awkward, possibly edited: 2:158 "It also does not prescribe"; 2:308 "factor count counts curvature-jet factors instead of their scaling dimensions".
- 7:184–185 "The kinetic symbol `b_H` of `J`": forward reference to an object defined at 7:976 (noted by the survey).

---

#### Terms the survey calls undetermined that the text settles

| Term | Survey | Settled or narrowed by |
|---|---|---|
| `c_lin` (9:846) | "Not defined in these files" | 4:474–480: "fix constants `c_dir, c_lin, R^rel > 0` with `16 c_lin < c_dir`"; slope of `clip_t` above `t`. |
| nonautomatic relaxed small-field condition (9:548) | "–" | 4:489–492: "`χ ≤ 2` makes all tests with `t_m e^{dist(x,y)/R^rel} ≥ 2` automatic". Nonautomatic = the finitely many remaining plaquettes. |
| quadratic-tilt criterion (9:115) | "by name only" | 9:115–116 cites Proposition (ch06:common-majorant), 6:1123–1138 ("tilted Gaussians"). |
| stationary residual (9:77, 130) | "by name only" | 6:615–621: "`|𝖠 m_Y + f_Y|_∞ ≤ C t_f e^{-cB}`", with "`𝖠 m_Y + f_Y = (I − 𝖠P^*) f_Y`"; matches the majorant `e^{-c'_j B}` in the table at 9:130–131. Identification is I but strong; 6:1257 has "linear Gaussian residual". |
| determinant inverse identity (9:140) | "by name only" | Probably 6:1192–1203 ("The exact inverse and trace expansions … This determinant identity"). I. |
| derivative reserves (9:34) | "–" | 10:737–739: "through one order beyond the outgoing order. This is a numerical derivative reserve"; also 11:2089, 17m:103, 282. Extra derivative orders beyond the output norm. |
| normalized (affine) directions (9:35, 502; 9s:296) | "?" | 4:580–581: seminorm directions with "`|(A_r)_e| ≤ t_m(1 + dist(e^-, o_i))^ϖ`"; 6:626–638: "dimensionless variation parameters … bounded by `C_k t_f` … in these normalized directions". Directions scaled by the threshold; 9:503 "`t²|q_f(q,r)| ≤ 3a_f`" agrees. R for the scaling, I for "affine" and "reflected". |
| the stage index `j` | "?" | 10:25–29 (stage), 10:124 "`ȷ_j` is the largest smoothing order used in stage `j`", 10:129–134 (`J(m)`). Chapter 10 distinguishes stage `j` from smoothing order `ȷ_j`; chapters 4, 5, 7 write `j` for the smoothing order (4:16; 7:600, 664) and chapter 9 for the stage. So two indices share the letter. |
| classical bound contraction; inherited-loop contraction (9:970) | R, inferred | 10:35–36 gives the two equation references. |
| safe chart; "recognizes" (9s:139–141) | R, "not Dict's tree comparison" | 5:1009–1015 (ch05:nonlinear-tree). |
| fixed-position read; coordinatewise splice (7:637, 710) | "?" | Narrowed by 4:174–189: connector `Y_{e,z}` = product of links `U(Ly + z + re_μ, μ)`, `r = 0..L−1`, averaged over offsets `z` with weights `w^av`. A "fixed-position read" is the link at fixed `r` as a function of `z`; 7:710–712 "coefficients `O_j(L^{-4})` on `O_j(L^4)` sites … Summing its `L` connector positions" fits. I, not ?. |
| slots (1:314) | "–" | 1:314–315 itself. |
| bridge legs (7:597) | "known only through the label" | 5:1123–1137, 1151–1152: `W_a` is "the smooth representative"; legs `W_a u`. I, as the survey has it in section 1. |
| quantum contribution `d_c`; `a_c` (9s:258–259) | "No formula" | Narrowed: 9s:270 "Classical matching gives `D^r C(0) = 0` for `0 ≤ r ≤ 4`" with `C = a_c − φ(·,ρ)` matches 7:994–998, so `a_c` is `J + S_3 + S_4` (the `𝒦` of 9:23–25); 9s:271 ties `d_c` to the determinant matching of 7:1159–1167. I; still no displayed formula. |
| numerical band margin (9:950) | "?" | Possibly the inner barriers of 10:212–222. Not determined. |

Still undetermined after my search of `chapters/`: recording estimate (7:461, 742; 11R:25–44 "recording scale" is a different object); thermal (word occurs only at 7:765); direction selectors; live tag actions and tag-coincidence radius; missing-coordinate factor; "factor after deterministic subtraction"; read-count polynomials; support compression; inspected support; centered expression (9s:283); seeded / unseeded; exterior identity (7:408, 686; 11:1692 "The exterior identity gives coercivity at least `c|q|²`" supports the survey's guess; 5:840 uses the phrase for a different identity).

---

#### Confirmed rows

Meaning, basis and lines as stated (apart from points above):

- **Section 1, ch. 1–2:** row transport; physical placement; lattice family; refinement; retained volumes; ordered convergence; transfer matrix; defects; seam; positive sector / algebra; observable label and tag; normalization index; factor count (both uses); test configuration; Taylor map and section; curvature measurement; curvature coordinate / admissible; basis column; permitted direction; equation ideal; regrading; exterior spectator; Wilson force.
- **Section 1, ch. 7:** common symbol; strip bound and order-`r` zero; leg; bridge legs; elementary division; curvature insertion; kinetic symbol; infinitesimal gauge insertion; background insertion; denominator; floor; thermal coefficient; radial bound; recording estimate; direction selectors; contact term; stationary branch; rooted / centered coordinates; coarse scalar component; internal / external; left increment (meaning); exterior identity; quotient estimate; weight conversion; stationary identification; adjacent pair; one-loop drift; exchange term; curvature family; path; quantitative descent; coupling entry threshold.
- **Section 1, ch. 8:** site norm; support-weight reserve; inflated activities; hypothesis matching; declared / assigned sites; exact reassembly; regular activity (the conflict with Dict 2.3 and with "ordinary" in ch. 9 is real); source-deformed activities.
- **Section 1, ch. 9 and 9s:** first expansion; scalar bookkeeping group; Haar logarithm; common law; selected large-field condition set; cutoff-failure label; table factor names; read-count polynomials; ordinary gas; prescribed large-field site set; degree; affine Hessian; inverse-ratio sizes; inspected support; support compression; principal; Gaussian / stationary units; pure block integral; extra exponent; cutoff amplitude (4:411); truncated mass; retained region; live tag actions; folded; microscopic; corrected logarithm; shares; auxiliary tori; logarithmic correction; preparatory output; plaquette channel; local projection; discrepancy series; reset; attachment norm; flattening; residual energy; restriction compatibility; local read diameter.
- **Section 2.3:** parent; insertion; weight; inherited loop action; matching; subpower; envelope; regrouping; Wilson initialization; centered log determinant; seeded / unseeded; eligible; absence of compulsory, Warnings, output anchors, likelihood tests; width and counting measure.
- **Section 2.1 references** (all rows opened except as listed under "Not checked"): row, label, tag, transport, anchor, frame, connector, forest, alias, layer, incoming, level, cover, torus period, nonwrapping, exact, block penalty, direct term, path action, atoms, metric, clip / relaxed, `Bad_m`, exclusion support, reads, window group, halo, frozen / active, density coordinates, mismatch, physical, score, witness, primitive / jet, margin, supplies, assigned, interface, coupling band / threshold, eligible, weight.
- **Sections 5–8 statements checked:** `C_G` / `C_𝔤` (1:35, 7:15); `h = 𝔟^{3/8}` and `𝔟^{-7/16}` (9:176, 295; 9s:20); `𝔟` and `z` for the same coupling (9:17; 9s:19); bond / edge (9:58; 7:204, 349; 9:456); `W` meanings; the `W_a` contradiction with `blueprint/notation.md` line 242 (present as described); "health" occurs in no other chapter file; "transfer matrix" occurs nowhere else.

---

#### Not checked

- Section 6 of the survey (overloaded symbols): about a dozen entries spot-checked, all correct; the rest not verified.
- Section 5 (synonym clusters): each cited line read during the full read, but not re-opened one by one; "event indicator (11 matches in ch. 9)" confirmed by count only.
- Section 2.1: the occurrence counts "22 lines in ch. 7, 27 in ch. 9" for incoming / inherited / outgoing were not recounted.
- Counts for `insertion` (39), `weight` (62), `common` (45), `scalar` (28), `auxiliary` (24), `logarithmic` (23): totals confirmed by script (weight, common, scalar, auxiliary, logarithmic) or by reading (insertion in ch. 7); the per-sense splits of `weight`, `common`, `scalar`, `logarithmic` were read but not tallied.
- Figures (`figures/*.tex`) not read. Chapters outside the seven were consulted only at the lines cited above; no claim is made about their other content.
- Proposed equivalents were judged from my own knowledge; none was checked against the literature. No Lean source was consulted.
- Overview section 6 lines in other chapters (11:296, 365, …; 6:730) are outside my chapters and were not reread.

---

<a id="part-iv"></a>

## Part IV. Chapters 10–11

### IV.A Survey

*Original title: Terminology survey, chapters 10–11 (extension B)*

> **Audited.** An independent check of this survey is in Part IV.B; its corrections supersede the text below, which is kept as returned.
>
> **Status.** Survey by one agent (Claude Fable 5.2 subagent), reproduced as returned. It was written against upstream commit `7bec3925`. Meanings marked I are inferences; proposed equivalents were not checked against the literature. See Part I for the cross-chapter synthesis and for what was verified.


Files (worktree `manuscript/HumanizeYM_v3/chapters/`), all read in full:
`10` = `10-common-trajectory.tex` (935 lines); `11` = `11-marked-insertions.tex` (2355); `11R` = `11-restarted-history.tex` (393); `11E` = `11-equation-calibration.tex` (185).
Also read: Part II (all), `blueprint/notation.md` from line 146 to the end. Counts are from `grep -oiE` after stripping `\label{}`, `\ref{}`, `\eqref{}`; they are given per file in the order 10 / 11 / 11R / 11E.
Basis codes: D defined, R read off an explicit sentence, I inferred, ? undetermined. Categories: (a) accounting, (b) program leakage, (c) ordinary/standard word in unusual sense, (d) coined, (e) other.

General observation. These chapters have already been through a translation pass (no "price", "pay", "budget", "receipt", "readout", "table", "probe", "detector" in prose). What remains is (i) a large "reserve / cost / absorb / retain" vocabulary, (ii) scheduling vocabulary (stage, plateau, floor, delay, request, window, entry), (iii) many undefined nouns for objects of the marked expansion (principal, incidence, graph, column, trial, lift, mass, unit), and (iv) visible artefacts of mechanical replacement (section 4, last table).

---

#### 1. New terms (not in the ch. 3–6 dictionary)

##### 1.1 Scheduling and order of choices

| Term (variants) | Where | Def.? | Meaning and decisive quote | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| stage `j`; stage bound / constant / threshold / requirement; adjacent stage pair | 10:25, 28–30, 45, 50, 55; counts 32/33/7/7 | defined 10:25–31; index `J(m)` 10:129–134 | A regularity level: "A stage `j≥1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds"; nested; `J(m)=j` for `A_j≤m<A_{j+1}`. Not an RG step (the dictionary's sense of "stage"). | D | *regularity level `j`* (keep "stage" only if "step" is used for RG steps everywhere) | c |
| (stage) plateau | 10:123, 139, 189, 193, 195, 199, 206, 749; 11:1965 | used, read off 10:123–140 | Maximal interval of levels `m` with `J(m)=j`: "lies in the `j`th plateau: its lower endpoint is at least `A_j` … less than `A_{j+1}`". | R | *interval of constancy of `J`* | c |
| schedule; numerical / stage schedule | 10:12, 114, 118, 684, 808, 926; 11:1059 | defined by construction 10:121–147 | The functions `J(m)`, `L_m=𝓛_{J(m+1)}`, `τ_m`, `a_m`. Narrower than the dictionary's "fixed parameter sequence" but compatible. | D | *scale sequence `(J(m),L_m,a_m)`* | c |
| floor; stage / ratio / block floor; additional floor; metric floors | 10:55, 90, 102, 299, 324; 11:1958, 2176; 11R:247; 11E:29, 133 | used | A lower bound imposed on the block ratio `𝓛_j` ("odd integers `𝓛_j≥3` above every stage floor", 10:55; display 10:91–94). 11R:247 "metric floors": lower bounds of the quadratic forms (inferred). | R / I | *lower bound on the block ratio*; *lower bound* | c |
| delay; stage delay; finite delays; uniform delay | 10:107, 111; 11:1192, 1199, 1214, 1267, 1270, 1402, 1764, 1944, 2022, 2085, 2111, 2146 (2/12/0/0) | undefined | Postponing the level at which a stage starts so that a fixed constant is dominated by a slowly growing quantity: "The stage delay can impose `C_k≤H^γ`" (11:1192); cf. 10:157–159 "satisfied by increasing its starting scale". The identification with increasing `b_j` is inferred. | I | *after increasing the starting scale of the stage*; state the inequality imposed | c |
| threshold for the starting scale; choice of sufficiently large starting scale(s); condition(s) on the starting scale; stage entrance; post-length threshold conditions; mesh threshold | 10:63, 606, 692; 11:1070, 1119, 1397, 1815; 11R:79, 219, 336; 11E:30, 106, 113, 148 | undefined; mechanism 10:157–183 | Same thing as "delay": requirement `τ_m≥b_j log 3` (10:181–182). "Post-length" = imposed after the block ratio `L` is fixed (11E:113, cf. dictionary "pre-`L`"). | R | one phrase: *lower bound on the starting scale `b_j`* | c |
| request; numerical / finite / degree and derivative requests; requested (order, power, window) | 10:67, 69, 75, 123, 189, 745; 11:356, 1634, 1777, 2057, 2084, 2090, 2208; 11R:217, 241, 296; 11E:13, 30 | read off 10:66–70 | A finite numerical requirement which a later chapter adds to the schedule: "Future applications may prescribe countably many finite numerical requests … At stage `j` take the maximum of the first `j`". | R | *requirement*; *prescribed (order, power)* | b |
| inner barriers `ℓ_m,u_m` | 10:213, 245, 250, 271 | defined 10:213–217 | Two sequences inside the admissible band between which the tuned couplings stay. Standard "barrier" usage; listed only because of "barrier inequalities". | D | keep | — |
| shooting; shooting parameter | 10:273, 818 (and label) | undefined | The bare coupling chosen at level `N` so that `β_{N,p,0}=β̄` (10:243–251). Standard ODE metaphor. | I | *tuning of the bare coupling*; or keep with one sentence | c |
| tuned (history, endpoint) | 10:12, 17, 232, 808 | Thm 10:232 | `β_{N,p,0}=β̄`. | D | keep | — |
| coarse target `β̄`; coarse endpoint | 10:153, 209, 268, 813 | 10:153 | Value of the inverse coupling at level 0. | R | *value of the coupling at unit scale* | c |
| comparison level / depth `k`; top level; opening (level, sites, estimate, bound); middle level `ℓ`; output (level) `w`; leading interval; lower interval; restoration levels; (fixed) deep comparison level | 11:734–737, 1149, 1405–1406, 1551, 1564, 1646, 1753, 1889, 1919, 1949, 1952, 1960, 2032, 2085–2088, 2151, 2200; 11R:70, 218 | never defined together | Three levels `k>ℓ>w` (`m=k−ℓ`, 11:1754; `ℓ−w`, 11:1571): `k` = level at which the restart begins ("top level `k`", 11R:218; "opening"); `ℓ` = "middle"; `w` = "output". "Leading interval" = `k→ℓ` (11:1952), "lower interval" = `ℓ→w` (11:1960). That "opening" = "top" = `k` is inferred from 11:1889 (`C=⌈(log s)^2⌉`, `s=β̂_k`). "Restoration levels" (11:1405) not identified. | I / ? | name the three levels once by symbols `k,ℓ,w` and use only the symbols | d |
| comparison window (finite windows; window of at most `(log log s)^4` steps) | 11:1462, 1675, 1795, 1965, 2091–2092; 11R:215–222, 298 | Prop. 11R:215–219 | Interval of levels below `k` on which the restarted history lives. | R | *interval of levels `[w,k]`* | c |
| stopping pair `(m,k)`; stopping representation; stopping scale; "stopped at `a_k`" | 10:172; 11:781, 816, 945; 11E:65 | read off 11:815–816 | `m` = scale of the reflected tiling, `k` = level at which the block evolution is stopped and the representation used: "A reflected tiling at scale `a_m`, stopped at `a_k`, has `(a_m/a_k)^4` sites per cell". | R | *pair (cell scale `m`, evaluation level `k`)* | c |
| restart; restarted history / representation / threshold / small-field indicator | 11:26, 734–765, 1155, 1220, 1309, 1663, 1967, 2058, 2090, 2198; 11R:2, 7, 215 | described 11:736–741; constructed 11R:215–242 | The auxiliary sequence `D_i=𝓑_{i,β}D_{i+1}`, `D_k=ρ_{N,p,k}`, with the actual inverse coupling frozen at `β=β_{N,p,k}` below `k`, new radius `B_i=b(x_i)^2` and threshold `ϑ(x_i)`. | D | *auxiliary constant-coupling sequence*; keep "restarted" if defined at first use | d |
| recording scale / parameter `r(x)` | 11R:25, 33, 44, 248, 263 | defined 11R:26–28 | The solution of `r^{-1/2}H(r)=ϑ(x)`; "a recording parameter for the local calculation, not the actual inverse coupling". | D | *auxiliary reference parameter `r(x)`* | b |
| re-expression of the endpoint; endpoint re-expression | 11R:68; 11:1930 | Prop. 11R:68–81 | Rewriting the density at level `k` with radius `b(x_k)^2` and threshold `ϑ(x_k)`. | D | *change of representation at level `k`* | c |

##### 1.2 Histories and the comparison argument of chapter 10

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| history (ch. 11 sense) | 11:18–19 | defined | "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations." New sense relative to the dictionary (section 3 below). | D | *RG trajectory (with its choices)* | c |
| finite history; tuned finite history; coupled histories; auxiliary / zero-terminal-array / zero-array history; history with prescribed inverse couplings | 10:13, 232–256, 447, 781–799, 805, 826, 918 | Thm 10:232 (not a formal definition) | For fixed `(N,p)`: the sequence of densities `ρ_{N,p,m}`, `0≤m≤N`, with couplings and activity arrays, from the Wilson density down. "Zero-array": started from activity array zero at a level `k` with couplings prescribed (10:824–826). | R | *finite RG trajectory*; *trajectory started from zero activities* | c |
| dictionary; common (coefficient) dictionary; support dictionary; fixed dictionaries | 10:316, 376, 379, 382, 393, 727, 905; 11:472 | undefined | Index set on which coefficient or activity families are defined, common to all cutoffs: "coefficients `c_N(γ)` on a common dictionary" (10:376). | R | *index set* (*of paths*, *of supports*) | b |
| Hilbert encoding; encoding weights | 10:381–382 | undefined | Not determined; some `ℓ²`-type parametrisation of path coefficients. | ? | ask author | b |
| pad absent labels by zero | 10:394–395 | — | Extend a family by zero to the common index set. | R | *extended by zero* | b |
| prescribed-site rules; cutoff-failure catalogue; clipping rule / clipping data | 10:393, 727, 921 | undefined | The fixed combinatorial data of a level (which large-field sites an activity must cover; list of cutoff events; `clip` parameters). "Prescribed-site" is the notation.md translation of "forced/inventory". | I | *the fixed data: prescribed large-field sets, list of cutoff events, clip parameters* | b |
| finite parameter evaluation(s); finite-evaluation bound / inequalities; moment norm `M_q` of an evaluation | 10:457, 462, 486, 498, 609, 630–652, 668, 799 | read off 10:464–471 | A finite linear combination `Σ a_i F(z+t_i v)`; its "moment norm at radius `q`" is `sup_n|Σ a_i (t_i/q)^n|` (inferred from 10:468, 630–635). (Labels `finite-tests`, `broad-test`.) | R / I | *finite linear combinations of values along a real line*; *norm of the functional on `c_0`* | d |
| narrow band; reserved band; inverse coupling reserve | 10:405, 430, 491–492, 529, 676 | 10:406, 492 | `17/20≤χ_mλ≤23/20`; enlarged to `33/40…47/40`. | D | keep, with the inequalities | — |
| compensation | 10:529–531, cf. 678 | read off | "the Gaussian coordinate is rescaled by `ℓ(t)` while its fluctuation coefficient is divided by `ℓ(t)`", so the fine field is unchanged. Clarifies dictionary 4.2 "compensating map". | R | *compensating rescaling of the Gaussian variable* | c |
| held fine reads; fine (field) read(s); local read set; read coordinates | 10:508, 530, 587, 678, 721, 741, 765; 11:696, 700, 718, 720 | undefined | Noun use of the dictionary's "reads": the fine variables on which a factor depends, kept fixed under a change of variables. | I | *the fine variables on which the factor depends* | b |
| real nodes; node sign | 10:553–561, 573, 631, 675 | — | Interpolation nodes; standard. | — | keep | — |
| hard bound `a_h` / hard factor; soft correction `a_s` | 10:656–667 | undefined | Hard = the large-field factor each such activity contains (bound `Ce^{-cP(y)^2}`); soft = remaining small corrections (`≤y^{-1/8}`). | I | *large-field factor*; *small-field corrections* | c |
| fusion; connected fusion estimate | 10:655, 666, 774, 914 | defined in ch. 9 (section label `ch09:fusion`, 09:631 ff.) | The regrouping of preliminary large-field terms with logarithmic corrections into connected components. | D (ch. 9) | *regrouping into connected components* | d |
| reset | 10:651 | ch. 9 (labels `ch09:path-reset`, `ch09:reset`, 09:539–748) | The redefinition of the inverse coupling after a step (eq. `ch09:reset`). Not explained in ch. 10. | I | *redefinition of the coupling* | b |
| low-order collection / projection; finite local / auxiliary projection; projected scalar | 10:509, 606–608, 615, 747, 772–776, 902, 914 | ch. 9 (09:41, 313, 383) | Finite set of low-order local terms extracted from the activities, and the linear map extracting them; "projected scalar" = the resulting number `q_m`. | I | *extraction of the low-order local terms* | c |
| residual scalar inverse coupling correction `q_m`; scalar correction | 10:421–422, 445, 816, 842 | defined 10:416–422 | `q_m=β_m−β_{m+1}−α_{N,m}`; "It is not the vacuum normalization". | D | *coupling correction `q_m`* | c |
| path coefficient `α_{N,m}`; path correction | 10:422–423, 441, 855 | R | Explicit part of the coupling increment. | R | *explicit coupling increment* | c |
| response bound `ε` | 10:626 | undefined | A fixed small constant in the one-step remainder estimate of ch. 9. Why "response" is not determined here. | ? | *the constant `ε` of (ch. 9 ref.)* | c |
| block bridge | 10:921 | undefined | Not determined (cf. label `ch05:actual-bridge`). | ? | ask | d |
| stationary branch | 10:920 | undefined | Presumably the chosen stationary solution (dictionary "branch" = case). | I | *stationary solution* | c |
| moving expression / moving threshold surface | 10:730–734 | — | Depending on the cutoff `N`. | R | *cutoff-dependent* | c |
| replication costs; sparse stopping scale; Haar-ball normalization argument | 10:169–172 | undefined | Forward references to the chessboard argument (11:795–805): cost of restricting all links to a Haar ball, per site. "Sparse" not determined. | I / ? | cite the later estimate | a |

##### 1.3 The source algebra and the marked expansion (ch. 11)

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| squarefree source algebra `𝒜_𝓘`; source variables `z_i`; source monomial `z_S`; source variable set | 11:23, 33–49, 1324, 1384, 1487, 1493, 1584, 2095 | defined 11:33–40 | `ℂ[z_i]/(z_i^2)`; generating variables for insertions. | D | *exterior-free truncated polynomial algebra* is not standard either; keep, it is defined | — |
| source weight `ω_i`; residual source weight; weight restoration; restored weight | 11:43–49, 192–196, 496, 938, 953, 1374–1388, 1436, 1471, 1552, 2130 | 11:43–47; restoration read off 11:1380–1388, 1436–1442 | Weights in the norm `‖a‖_ω=Σ|a_S|∏ω_i`. "Restoration": passing from the bound at `(ω_−,e+2)` to one at the larger weight `ω=H^{U}ω_−` and smaller exponent `e`. | D / R | *weights `ω_i`*; *change of weight from `ω_−` to `ω`* | c |
| insertion label | 11:33, 132, 178, 185, 193 (13 lines) | 11:33 | Element of the index set `𝓘`. | D | *insertion index* | c |
| mark; marked point / site / ancestor; marked factor / term / component / activity; marked density / expansion / step / polynomial; unmarked | see section 3 | never defined | notation.md: mark = observable insertion. Three uses, section 3. | I | *insertion (point)*; *term carrying insertions*; *density with insertions* | c |
| push; pushed (polynomial, density); exact push | 11:95, 97, 773, 1671, 1950 | read off 11:76, 95 | Apply the block maps coefficientwise: `q_m=𝓑_m q_{m+1}`. | R | *image under the block maps* | c |
| unit; unit insertion; unit coordinate; exact unit rule; "the circle deletes the unit coordinate" | 11:87–90, 389, 451, 1050 | R | The constant field `e_0` (identity insertion) and its coefficient. | R | *identity insertion `e_0`* | c |
| principal (term, factor, component); purely principal; nonprincipal; nonleading; leading | 11:179, 279, 288–289, 297, 314, 319, 321, 329, 339, 425, 608, 728, 1043, 1410–1413, 1606, 1614, 1625–1632, 1646 (principal 17; nonleading/nonprincipal 7; leading 12) | never defined | Principal = the main part of a single-insertion factor on the small-field event, to be evaluated by the joint Gaussian comparison: "Purely principal connected components … contain neither an unmarked correction nor an incoming large-field factor" and "Their actual integral is the joint moment" (11:329–332); the split `(1+γWz_S)(1+(1−γ)Wz_S)` (11:314–319) calls the second factor "nonleading". "Nonleading" and "nonprincipal" appear to be synonyms (11:279 vs 288). 11:1737 "principal alias" is the ch. 5 sense. | I | *leading (Gaussian) part* / *remainder part*, defined once | c |
| inflation factors `m,l`; inflated; uninflated | 11:274–278, 294, 337, 522, 1593–1603; 11R:313, 319–322, 333, 371, 383; 10:602 | read off 11:274–277 | Factors `≥1` by which the amplitude bounds are multiplied before the local integral bound is applied. | R | *enlargement factors `m,l` of the bounds* | a |
| incidence (bound, sum); marked-point incidence; insertion incidence; source variable incidence | 11:208, 258, 265, 302, 322, 340–342, 506–507, 783, 1398, 1577, 1606, 1614, 1649, 2135 (17) | never defined | Sum of the weighted bounds of all terms whose label set contains a given mark ("the insertion incidence sum at a fixed mark", 11:258); contrasted with the "site bound" (sum over terms containing a site), with conversion 11:266–272. | I | *sum over terms containing a given insertion* | d |
| site bound / site sum; root-to-site conversion; site conversion | 11:257, 266, 300, 1473, 1918; 11R:74, 125, 141–142, 170–181 | dictionary "containing-site bound" | Same as dictionary. "turn an anchored bound into a site bound" (11R:141). | — | as dictionary | — |
| occupancy `g` | 11:260, 345; 10:109 | 11:260 | "at most `g` marks project to a coarse site". | R | *maximal number of insertions per coarse site* | c |
| menu (of stencil radii and degrees); degree menu | 11:161, 516 | — | Finite list. | R | *finite list* | e |
| complementary part / stencil / insertion factor / attachment / cutoff | 11:139, 147–151, 922, 941, 1613, 1636; 11E:81, 101, 119; 10:99 | read off 11:147–151 | The part of an insertion multiplied by one minus the small-field indicator. | R | *large-field part of the insertion* | c |
| join; attach; attachment(s); attachment reserve `u_N`; attachment margin | 11:148–149, 169, 215, 252, 502, 510, 922, 937; 11E:57, 81, 93–104; 10:760, 775 | R | Merging an insertion's large-field part with the large-field supports it meets into one component. | R | *merging into the large-field component* | c |
| (linear) graph `G`; coefficient graph; graph norm; graph estimates; inhomogeneous graph estimate; graph of normalized local insertions | 11:347, 379, 447, 454, 468, 886, 892, 899, 911 | 11:379–380 (notation only) | A linear map from the coefficient vector `x∈V_d` to families of regular and large-field remainders ("an incoming linear graph of regular vanishing-jet and large-field remainders, with norm at most `s_f` per coefficient"); one step maps `G` to `G'=R_G M_G^{-1}` (11:447). The word is used as in "graph transform". | R | *remainder map `G`* (linear in the coefficient); *graph transform* is standard for `G↦G'` | c |
| raw (remainder map, error, inequalities, polynomial, stencil, transport, labels, coefficient, triangular construction) | 3/11/0/1; e.g. 11:382, 466, 651, 894, 901, 958, 1014, 1208; 10:103, 609, 656 | — | "Before normalisation / correction"; meaning varies by noun. | I | delete or say *unnormalised*, *uncorrected* | b |
| rebasing contraction | 11:467 | undefined | Presumably the contraction for `G↦R_GM_G^{-1}` (11:454–465). | I | *contraction of the map `G↦G'`* | d |
| preselection bound | 11:382 | undefined | `C_d/L+o_x(1)`; "preselection" not explained. | ? | *the bound `C_d/L+o(1)`* | d |
| column; stage column bound / constant; inverse(-front)-column bound; free comparison columns; target columns | 10:83; 11:446, 1057, 1103, 1144, 1200, 1237, 1304, 1340, 1343, 2033; 11E:19 | undefined | Column = image of a basis vector of `V_d` under a coefficient map; "column bound" = `ℓ¹` operator-norm bound of the map or its inverse ("`|x|≤s_f|M_Gx|` after fixing a suitable stage column constant", 11:445). "Front-column" (11:1343) not determined. | I / ? | *operator-norm bound `C_j`*; *image of a basis vector* | b |
| vanishing-jet remainder | 11:379 | cf. 11:1181 | Regular remainder whose extracted polynomial is zero ("all regular remainders have zero extracted polynomial"). | I | *remainder with zero local part* | d |
| screened; screening | 11:400, 413 | undefined | Restricting a polynomial direction to the links on which the function depends. | I | *restricted to the relevant links* | c |
| mass (of a large-field input); normalized mass; reserved mass | 11:423–429; 11E:104–105, 117 | undefined | The support-weighted norm of a large-field contribution, `m`, and `m/κ_f`. | I | *weighted norm* | c |
| selected slot | 11:424 | undefined | Not determined. | ? | ask | b |
| common Gaussian; common sample; coarse forecast | 11:537, 725–726, 1043, 1878 | "forecast" undefined | One Gaussian array used for all subsets. "Coarse forecast": presumably the conditional mean given the coarse field. | I | *one Gaussian family*; *conditional mean* | c |
| corrected source `Jq_N`; corrected coefficients `R_I`; corrected pair bound | 11:769–771, 2066–2070, 1836 | defined | Product with `exp(−C^ref)` / recursion 11:2068–2070. | D | *truncated (connected) coefficients* — unsure; keep, defined | — |
| near part / near sum `F_u^near`; distant part; `f^{near,mask}` | 11:1161–1169, 1229, 1310–1321 | defined 11:1161–1168, 1310–1311 | Split of the regular series at connected cover number `M`; "mask" = with the original event indicators restored. | D | keep; rename superscript "mask" | b |
| common localization / extraction; localization onto the polynomial label space `T`; coefficient extraction; low-weight coefficient extraction | 11:29, 372, 438, 1141, 1180–1182, 1288, 1307, 1326, 1330, 2057 | constructed 11:1285–1305 | The linear map `T` (also `T_{k,N,p,d}`) taking the coefficient vector to the frame coefficients of the Wick-ordered Taylor polynomial. Two words for one map. | D | *localization map `T`* (one word) | — |
| exposure `𝓔`; fixed radial polynomial frame | 11:1285–1293 | undefined | A linear map with `‖v‖_1≤c_d‖𝓔v‖_coeff`; apparently the expansion of a label as a polynomial in a fixed basis ("frame"). | ? / I | define `𝓔` by a formula | d |
| (simultaneous, normalized) lift; lift equations; lifted vectors | 11:1306, 1326, 1341, 1351–1354, 1839–1842, 2059–2063, 2159–2162, 2197, 2208, 2215 | eq. 11:1352 | Solution `u` of `S_{g/θ}Tu=W_ρ v`. A fourth sense of "lift" (dictionary 4.2 has three); 11:400, 414 "centered nonwrapping lift" is the covering-lattice sense. | D | *preimage `u` of `W_ρv`* | c |
| magnification `ρ=H^b`; measurement magnification; geometric magnification; amplification | 11:1365–1366, 1806, 2054, 1963 | 11:1350, 1806 | Dilation factor in `W_ρ`; "amplification" = growth factor of a bound. | R | *dilation factor* | c |
| measurement (matrix, cell); averaged measurements; tested correlation; correlation pairing | 11:983, 1806, 1920, 2177, 2233–2235, 2248, 2255, 2276, 2288, 2314, 2320 | undefined | Value of the finite family of correlation functionals `L_i` on a coefficient; `G` its free counterpart. | I | *value of the functional `L_i`*; *matrix of correlations* | c |
| trial; local / terminal / fixed-stencil / difference / protected trial; bounded coarse polynomial trials; trial descent; trial encoding | 10:95; 11:27, 890–957, 1074, 2235, 2276, 2294, 2306–2311, 2329, 2349; 11E:94, 148 | undefined | A local observable `F` (e.g. `f=a_N^eF`, 11:919) to be approximated by a normalized local insertion `O_{N,p}(e,v)` (11:949). | I | *local observable (to be approximated)* | d |
| backward comparison; descent; bulk descent bound | 11:27, 890, 945; 11E:121, 125 | — | Downward induction in the level from `N`. | R | *downward induction* | c |
| cone inequality | 11E:125 | undefined | Presumably the implication `A_i|x_i|≤c_i ⇒ A_{i+1}|x_{i+1}|≤c_{i+1}` (11:905–908). | I | cite the inequality | d |
| terminal map `𝖹_{N,p,d}`; inverse terminal coordinates; reference level / label / coefficient; reference coordinates | 11:883–885, 946–947, 958, 1047–1049, 1075, 1136; 11E:9, 154, 184 | defined 11:1047–1049 | Composition of the single-insertion coefficient maps from `N` to the reference level; "inverse terminal coordinates" = `𝖹^{-1}c`. | D | *coefficient map from the cutoff scale to the reference scale* | c |
| calibration; calibrated; local calibration | 11:1034, 1061, 1159; 11R:6; 11E:2 | undefined | Normalisation of coefficients through `𝖹` and comparison of sections; no single definition. | I | *normalisation*; *comparison of the two sections* | c |
| admissible (comparison coefficient / family) | 11:884–886, 1101–1105, 2253, 2311–2324 | defined twice (11:884; 11:1101) | `‖X_i^{-1}z_i‖_1` subpower in `a_N^{-1}`, uniformly in `p`. | D | keep | — |
| equation subspace / space / kernel / labels / component; moving, varying, actual equation space; moving complement | 11:966, 989, 1083, 1093, 1107, 2218, 2224; 11E:43–46, 154–159 | 11E:155–159 | `𝖤_{N,p,d}=𝖹PS_{t_N}R_d𝓘_d`; "moving" = depending on `(N,p)`. | D | *cutoff-dependent subspace of field equations* | c |
| positional modulus | 11:827, 1025–1027, 2242 | read off 11:861–866 | Lipschitz bound of a correlation in the position of one insertion. | R | *modulus of continuity in the insertion point* | d |
| transfer word; slab kernel; tour length; gaps | 11:842–863 | 11:842–845 | `tr∏B_iT^{H_i}`; total length `M`; exponents `H_i`. | R | *cyclic product of transfer operators*; *total length*; *separations* | c |
| finite difference word `l` | 11:2227, 2251, 2278, 2297, 2304 | undefined | Finite sequence of coordinate directions; `D_l` the iterated difference. | I | *multi-index `l`* | c |
| plant; planting | 11:2332, 2349 | read off 11:2332–2343 | Placing the points of a tuple in distinct interior cells of a tiling. | R | *placing in distinct cells* | e |
| spans `t,T`; margin `3t` | 11:2336–2339, 2351 | 11:2337 | Cell sides in lattice units. | R | *cell sides* | c |
| chessboard seminorm `𝓡_m`, `‖·‖_root`; root bound | 11:822, 2027, 2075, 2140 | named 11:815–822 | The number-of-cells root of the normalised product moment on a reflected tiling. Standard name now used; the subscript "root" is a leftover. | R | keep; rename subscript | — |
| reflected replica cell; reflection cell; measurement cell; comparison cell; copies | 11:178, 194, 345, 781, 835–846, 1122–1126, 1468, 1920, 2073 | undefined | Cells of the reflected tiling. | I | *cell of the tiling* (one word) | c |
| (weighted output, scalar) envelope | 11:1972, 2136 (label 1580) | eq. 11:1581–1582 | The bound `exp{unmarked exponent+q_0(1+n)}`. | R | *majorant* | c |
| expense | 11:2137–2138 | — | Additive constant per site in an exponent. | R | *contributes at most `1+n` per site* | a |

##### 1.4 Restarted history (11R)

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| presentation; exact / genuine / coarse presentation `P_i` | 11R:71, 196, 222, 250, 339 | — | A representation of a density by path action, clip, regular and large-field activities; synonym of "local representation" (11:19, 122) and the dictionary's "density coordinates". | I | *representation* (one word) | c |
| genuine (density, presentation, multipliers, value cost) vs neutral (reference, version, estimates, Gaussian integral) | 11R:195–213, 254–259, 282, 310, 319, 334; 11:613 | defined 11R:196–198 | `R=e^{-E}R^0`; neutral `R^0` = "obtained by deleting only the regular additive family `E`". | D | *full density* / *density without the regular terms* | d |
| local multipliers / additive multipliers `h_α=e^{-E_α}−1` | 11R:205, 259, 310, 319, 330 | defined 11R:205 | | D | *factors `h_α`* | c |
| local energy contributions `d_z`, `b'_z`; selected site factor `X_z`; mandatory factor | 11R:96–116, 159–162, 170 | defined | `X_z=exp[−β(d_z+b'_z)]`. | D | keep | — |
| half-square | 11R:103–111 | R | Half the square of a truncated path component. Clarifies dictionary 4.2. | R | *`½|·|²`* | c |
| new-small-field | 11R:107, 124, 149 | — | Small-field for the new threshold `ϑ`. | R | *small-field at threshold `ϑ`* | d |
| coalesce | 11R:147, 184 | — | Sum the terms with equal support. | R | *collect by support* | c |
| optional factors / optional subset | 11R:155, 165 | — | Factors `W_Y` that may or may not be chosen when `∏(1+W_Y)` is expanded. | R | keep | — |
| value cost `q_n`; additive value cost / error | 11R:225–227, 254, 352; 11:2014 | R | Bound for the sup of the regular additive terms per site. | R | *sup-norm bound per site* | a |
| unselected local exponent / components | 11R:264, 313 | — | Not carrying a failed cutoff condition (inferred as complement of "selected", section 3). | I | *small-field (local term)* | c |
| determinant-word series | 11R:270 | ch. 6 (dict. `word` (iii)) | Neumann-series terms. | — | as dictionary | — |
| finite decorations | 11R:304 | undefined | Not determined. | ? | ask | d |
| sliced-integrand level; slices; tag-count factor; tag average | 11R:358–360 | undefined | Integrand at a fixed value of the random index `α`; number of values; average over `α`. | I | *for fixed `α`*; *number of values of `α`* | b |
| regular logarithms with holes; raised hole correction | 11R:365–367 | undefined (refers to `ch08:reassembly`) | Not determined from these files. | ? | check ch. 8 | d |
| installed (entry; transport; response); lower / higher entry | 11R:384–385; 11:648, 1729 | — | "Fixed as part of the family"; "entry" = member `P_i` of the family. | I | *constructed*; *member* | b |
| deletion-of-support identities; same-data restart conditions; corrected body product estimate | 11R:239; 11:1666; 11:1662 | undefined | Not determined. | ? | ask | b |
| frozen (inverse coupling) | 11R:246 | — | Held constant. Different from dictionary "frozen links". | R | *held constant* | c |

##### 1.5 Accounting vocabulary (print the inequality instead)

| Term | Counts 10 / 11 / 11R / 11E | Examples | Meaning | Cat. |
|---|---|---|---|---|
| cost, costs (noun and verb) | 10 / 22 / 10 / 0 | 10:63, 166, 172, 178, 575, 601, 645; 11:197, 241, 432, 596, 789, 910, 925, 939, 1069; 11R:225, 254, 340 | A multiplicative loss, an additive term in an exponent, or the bound itself ("additive value cost", "coefficient plus remainder cost at most `w`", 11:910). At least three types. | a |
| reserve, reserved (support / width / derivative / energy / numerical / attachment reserve; reserved band, fraction, mass, factor) | 19 / 18 / 5 / 2 | 10:37, 375, 426, 594, 738; 11:168, 225, 495, 521, 937, 1596; 11R:9, 170, 180; 11E:104 | A strict margin in an exponent, width or order, left unused by one estimate and used by a later one; as a verb, to set aside part of a decaying factor ("Reserve `e^{-u}` per selected site factor"). Never defined; 10:375–381 gives the one precise instance (width `w'>w`). | a |
| margin | 3 / 2 / 3 / 0 | 10:615, 776, 915; 11R:261, 278, 306 | Same as reserve. | a |
| absorb | 8 / 18 / 3 / 0 | 11:217, 295, 321, 420 | "Is bounded using the spare factor". Common in analysis; acceptable if the inequality is shown. | a |
| retain | 9 / 31 / 18 / 2 | 11:24, 131, 495; 11R:22 | Keep (a factor, a condition). Mostly harmless; 11R:22 defines "retaining the clip". | — |
| gain, loss, lose | 1 / 3 / 0 / 0; 0 / 2 / 5 / 0 | 10:597; 11:502, 724; 11R:57, 143, 178 | Improvement or worsening of a bound by a factor. | a |
| supplies / supplied | 3 / 13 / 1 / 0 | 11:248, 686, 1036, 1074, 1587 | "Gives". 11:248 "is supplied by the unmarked local correction factors" = "is covered by". Labels `parameter-supplier`, `cutoff-supplier`. | b |
| input(s) | 19 / 11 / 0 / 0 | 10:252, 443, 886; 11:173, 964 | Argument of the step map (fine) or hypothesis ("a quantitative local-section input", "analytic inputs"). | b |
| subpower | 2 / 11 / 1 / 4 | 10:172, 178; 11:886, 943, 1102; 11E:73 | Same as dictionary (`x^{o(1)}`), here in `a_N^{-1}` or in `x`. Defined in ch. 6:822. | — |
| unit(s) of support exponent; cover units | see section 3 "unit" | 11:396, 495, 502, 528, 533, 939, 1446 | One unit in the exponent multiplying `c_B(X)`. | a |

---

#### 2. Dictionary terms in these chapters

##### 2.1 Same sense (confirming references)

| Term | Refs here | Note |
|---|---|---|
| terminal (= finest scale `N`) | 10:102–112, 432, 728, 890; 11:133, 166, 895; 11E:57, 78 | same; plus the derived "terminal map `𝖹`" (1.3) |
| reads / read by | 10:568, 587; 11:680; 11R:104, 106, 161 | same; the noun "a read" is new (1.2) |
| protected (change of variables, chart, neighborhood) | 10:505, 672, 720, 737, 898; 11:472, 1773 | same. New, unexplained use: "protected local representative / trial" for a finite difference, 11:1063, 2306 (?) |
| tag (random index) | 11:244, 679; 11R:358–359 | same; "tag" survives although the dictionary proposes dropping it |
| sector | 11:244, 293; 10:676 | same |
| forest; forest coordinates / charts; tree gap; block root | 11:617, 628–633, 679; 11R:247; 11:1975 | same |
| full dependence region; exclusion support; exact cover / coverage | 11:134–136, 150, 180, 246–251; 11R:8, 124, 157, 167–168 | same; variants "full region", "full support", "full dependence supports", "full read supports" (11R:167) |
| stencil | 11:135, 148–151, 161, 919–938; 11E:15, 80, 95 | same (set of links an insertion is built from) |
| clean; clearance; remote | 11:679, 709, 721 | same |
| plateau (where a cutoff equals one) | 11:712–713 ("fine plateau", "strict plateau width") | same; a second sense (stage plateau) is new, 1.1 |
| clip; clipped | 10:727, 921; 11:751–760, 1777; 11R:19–23, 43, 72, 85, 198, 250 | same; 11:751 gives "piecewise quadratic/linear clip `d_t`" (symbol `d_t` here, `clip_t` in ch. 4) |
| relaxed small-field condition | 11R:104 | same. **Conflict:** 10:98 says "the relaxed small-field *smooth cutoff* is one", whereas the dictionary (section 9) established that `χ^rel` is an indicator |
| noise | 11:713; 11R:61 ("cutoff-to-noise ratio") | ch. 6 sense (Gaussian fluctuation, scale `g`) |
| scalar (constant term of the action) | 10:266; 11:609, 726, 789 ("`v_0` is the scalar"), 814, 2014; 11R:73, 190, 362 | same; two further senses in section 3 |
| direct (row coefficient); `c_dir` | 10:356; 11:752 | same |
| inherited (loop, bounds) | 10:36, 338, 761; 11R:272–275 | same |
| atoms (path atoms of degree `j`) | 11R:137, 349 | same |
| metric (curvature / two-form / quadratic metric) | 10:33, 328, 356; 11:627, 649, 662, 1681 | same |
| stationary graph; stationary jets | 10:336, 716, 920–924 | same |
| spectator | 11:1029, 2093, 2182, 2276; 11E:74–75, 163, 169 | same |
| detect / detection | 11:960 (title), 976; 11E:171 | same (nondegeneracy on the quotient); prose now mostly says "separating family" (defined ch. 3:484, 806) |
| amplitude | 11:255–256, 276, 280–281, 339 | same (bound on a local factor) |
| primitive (bound, exponent decomposition) | 10:582; 11R:262 | same |
| connected expansion / regrouping | 10:599, 913; 11:335, 1460, 1480; 11R:165, 329 | same |
| halo | 11R:139, 158 | same (fixed neighbourhood `Y^{[8]}`) |
| anchored (majorant, bound, cost) | 11:362–364; 11R:141, 199, 209, 340, 375 | same as "anchored sum" (4.2) |
| alias; principal alias; box filter | 11:1731–1740 | same |
| counting coordinates | 11:621 | same (unnormalised sums) |
| score | 10:595, 718, 743–745 | same |
| Wilson initialization | 10:40 | same |
| array | 10:6, 256, 390–395, 421 and passim | same; 10:421 "`x_m` is the activity array" |
| lift (to the covering lattice) | 11:399–400, 414 | same as 4.2 sense two |
| representative | 10:317; 11:1217, 1347 | same |
| cover (coefficients / paths) | 10:81 "fixed cover paths" | same |
| cluster | — | not used in the "subsequential limit" sense here |

##### 2.2 New senses of dictionary words

| Word | New sense here | Refs | Basis |
|---|---|---|---|
| history | (ii) the whole choice of kernels, couplings, path pairs and representations (11:18, D); (iii) the finite trajectory of densities for a cutoff (10:232–256, R). Dictionary sense (blocking parameters) survives at 10:373, 933 ("nested quadratic history") and 11:1699 ("kernel history") | see section 3 | D / R |
| stage | regularity level `j`, not an RG step | 10:25–31 | D |
| eligible; eligibility criteria / indicators | condition on a family `𝓕` of supports in the polymer sum ("`Σ_{𝓕 eligible}`", 11:125) and the conditions attached to a large-field term ("original eligibility criteria", 11:153; 11R:80, 156, 166–168; 10:669). Neither dictionary sense (axial bound; extra event) is clearly meant | 11:125, 131, 153, 762, 791 | I |
| response | "stationary forest response `W`" (11:642) — the object ch. 5 calls *transport* `W`; "curvature response `J=H_{0,f}^{-1}TH_{0,c}`" (11:647, D); "installed curvature response `Ψ_i`" with `Δ_wΨ_i=Q_{i,w}Δ_w` (11:1729–1735); "response paths" (11:1773). Also 10:626 "response bound" (?) | | R |
| transport | (iv) `𝖹` "transports a cutoff coefficient to its fixed reference level" (11:883); (v) "transported mean / coarse covariance" `𝓛u`, `𝓛κ_ℓ𝓛^T` = image under the product of responses (11:1788, 1812–1813); (vi) "polynomial transport steps / norm" = action of one step on polynomials (11:1870, 1958). Dictionary senses also occur: stationary-field map (10:354 "free transports"; 11:648, 651 two-form transport `T`), parallel transport (10:313) | | R / I |
| mass | weighted norm of a large-field input (1.3); "mass-one identity" = normalisation of the kernels (11R:389). Not the weights `λ(U,α)` | | I |
| lift | preimage under `S_{g/θ}T` (1.3) | 11:1352 | D |
| window | interval of levels; range of `|x|`; compact set of configurations (section 3) | | R |
| frozen | coupling held constant | 11R:246 | R |
| physical | at least five uses (section 3) | | I |
| selected | "selected trajectory / history / stage requirements" and "selected component" (section 3) | | I |
| target | "coarse target `β̄`" (10:153); "normalized target columns", "finite target list", "fixed separated targets" (11:1237, 1364, 2207) | | I |
| envelope | the majorant of 11:1581 | 11:1972, 2136 | R |
| weight | source weight, support weight, filtration weight, probability weight (section 3); the dictionary's "weight = scaling dimension" appears only as "scaling dimension" here | | R |

##### 2.3 Terms the dictionary marks open, clarified here

| Open term | What chapters 10–11 add | Basis |
|---|---|---|
| regularity-stage index `J_m` (4:651) | **Defined.** Stage: 10:25–31. Index: `J(m)=j` for `A_j≤m<A_{j+1}` with `k_j=c_j+2A_j+1`, `A_{j+1}=A_j+b_{j+1}+2k_j+1` (10:129–134); "`J(m+1)` is the stage used for this step" (10:50); `L_m=𝓛_{J(m+1)}` (10:144). | D |
| Warnings (6:1476) | 11:319: after the exact split `(1+γWz_S)(1+(1−γ)Wz_S)`, "the actual warning estimate gives its supporting event probability at most `x^{-1}`"; 11:1612–1614 says of the same step "`l/x≤1` … the actual cutoff-failure probability absorbs the complementary principal cutoff". So a "warning" is a cutoff-failure event (the event where a local smooth cutoff is not one) and the "warning estimate" the bound on its probability. The link between the two passages is an inference. | R / I |
| compulsory (6:1018, 1461) | 10:654: "Arrays constrained to cover prescribed large-field sites retain one compulsory large-field factor throughout fusion … with the hard factor retained once" (10:666); 11R:161 "The factor at that site is mandatory". Reading: the large-field factor that every such component necessarily contains. Does not settle "compulsory component region". | I |
| moving comparison fields (3:576) | Not used. "Moving" is used for cutoff-dependent objects: "moving equation space" (11:1083), "moving equation kernel `K_i`" (11:2218), "varying equation subspace" (11E:154), "moving threshold surface" (10:734). Supports the dictionary's guess, does not define the phrase. | I |
| centered log determinant; seeded / unseeded; output anchors; likelihood tests | Do not occur in chapters 10–11. | — |
| width (4.2) | **Made precise:** weight `e^{wℓ(γ)}` on path coefficients; "strict width reserve" = bound at `w'>w` giving tails `Ce^{-(w'-w)r}` (10:375–381). | D |
| compensating map (4.2) | 10:529–531 (see 1.2). | R |
| half-square (4.2) | 11R:101–111. | R |
| envelope (4.2) | 11:1581 (a majorant). | R |
| coupling band (4.2) | 10:212 "The admissible inverse coupling band at level `m` is `[β̂_m/2,2β̂_m]`". | D |
| anchored vs containing-site sum (4.2) | conversion argument 11:266–272; 11R:141. | R |
| marked (4.2) | confirmed, three uses (section 3). | I |
| event label (4.2) | here "event indicator(s)" throughout (10: 11 uses; 11: 8; 11R: 8); "cutoff-failure labels" not used. | — |

---

#### 3. Multi-sense words (all occurrences classified; counts approximate to ±2 where "≈")

**row** (2 / 10 / 4 / 0).
(a) component of the action vector (dictionary sense 4): 10:354 ("actual quadratic rows"), 10:356 ("direct row"), 11:668 ("row Gram"), 11:710 ("linear fine comparison row"), 11R:101, 102, 122 ("quadratic path rows", "row pairs") — 7.
(b) literal matrix row / row sum: 11:684 ("curl rows"), 1210, 1212, 1262 ("axial row": row of the linear substitution links→curvatures), 1731, 1749, 1755 — 7.
(c) vector in a finite list: 11:2253 ("The rows `(I−Π_i)u_{j,i}`") — 1.
(d) undetermined: 11R:266 ("exterior row, determinant and Haar bounds") — 1.

**actual** (18 / 58 / 15 / 0).
(a) of this construction / on this same history (not an abstract or substituted object): 10: ≈14 (353, 373, 390, 414, 430, 473, 504, 609, 705, 728, 777, 889, 900, 906, 933); 11: ≈38 (27, 221, 268, 319, 330, 361, 381, 466, 642, 668, 676, 1029, 1043, 1107, 1145, 1146, 1158, 1241, 1269, 1307, 1325, 1333, 1456, 1564, 1663, 1675, 1685, 1729, 1765, 1839, 1950, 1971, 2036, 2057, 2086, 2097, 2137, 2196); 11R: 3 (261, 288, 301).
(b) the running coupling `β` (or quantities in it) as opposed to the reference `β̂` or recording parameter: 10:808; 11:470, 693, 736, 1670; 11R:34, 45, 47, 50, 57, 61, 115, 223, 246, 268, 272, 276 — 17.
(c) nonlinear / at the true background, as opposed to flat, linearised or polynomial: 11:415, 558, 672, 681, 704, 1183, 1216, 1222, 1783, 1867 — ≈10.
(d) the density itself as opposed to a representation or a modified density (= "genuine"): 10:265, 517 — 2.
(e) the modified ("repaired") metrics as opposed to the unmodified `H_0`: 11:627, 649, 662 — 3.
(f) under the law in force (probabilities): 11:280, 293, 1613 — 3.
None fits the dictionary's "gauge-covariant block average" sense.

**selected / selection / select** (5 / 30 / 12 / 3) and **chosen** (4 / 18 / 3 / 1).
(a) large-field: a "selected" large-field support, activity, component, site factor or cutoff condition, i.e. one belonging to the large-field index set of the term (ch. 6 "selection"): 11:139, 149, 151, 154, 248, 339, 424, 425, 434, 520, 761, 923, 1933; 11R:63, 159, 170, 182, 286, 288, 301 (×2), 305, 312, 316; 11E:82 — ≈25. "Unselected" 11R:264, 313.
(b) fixed by the construction (trajectory, history, stage requirements, block kernels, plateau, comparison levels, schedule inequalities, forest): 10:883, 892, 923; 11:111, 219, 617, 1045, 1059, 1200, 1401, 1965, 2056, 2084, 2176, 2182, 2294; 11R:89; 11E:30, 34 — ≈19.
(c) ordinary "choose": 10:273, 746; 11:1766, 1857, 1885, 2000 — 6.
`chosen` is ordinary throughout (26 uses), e.g. 10:63, 11:218, 713, 1392; none in the "random index" sense.

**test** (1 / 11 / 1 / 0).
(a) standard (test against a function; sign-valued test function): 11:115, 1755 — 2.
(b) "tested correlation" = value of the functionals `L_i` on an insertion: 11:2233, 2235, 2276, 2288, 2320 — 5.
(c) "tested links / neighborhood" = links (sites) on which a function depends: 11:402, 413; 11R:107 — 3.
(d) evaluate / check: 10:113 ("degrees are tested at a stage"), 11:355 ("is tested with one additional derivative"), 11:1016 ("to test finite differences") — 3.
The dictionary's senses "condition", "variable", "location", "indicator" do not occur under the word "test"; they now appear as "event indicator", "cutoff condition", "finite parameter evaluation".

**label / tag** (6 / 27 / 5 / 2).
(a) polynomial label, element of `V_d` (dictionary sense 1): 11:15, 29, 946, 958, 965, 1307, 2052, 2057, 2065, 2162, 2169; 11E:43, 55 ("equation labels" = elements of `S_{t_N}R_d𝓘_d`) — 13.
(b) insertion label, element of `𝓘`: 11:33, 39, 132, 178, 185, 193, 195, 204, 246, 341, 344, 517, 1371 — 13.
(c) index of an activity, path or large-field term: 10:249, 395, 709, 757, 895; 11R:80, 144, 184 — 8 (at 11R:144 "enlarged old large-field labels" the label stands for the term).
(d) tag = random index `α`: 11:244, 679; 11R:358, 359 — 4.
(e) not prose / standard: 10:461 (LaTeX `label=`), 11:871 ("tagged partitions", Riemann sums).

**mark / marked** (0 / 50 lines / 6 / 0; "unmarked" not counted).
(a) mark = an insertion point or its index ("marks project to a coarse site", "per mark", "marks from many cells"): ≈18, e.g. 11:184, 216, 258, 260, 268, 272, 496, 516, 542, 727, 783–784, 1380, 1417, 1578.
(b) "marked point / site / ancestor" = lattice site of an insertion: ≈12, e.g. 11:180, 181, 187, 189, 208, 301, 340, 482, 1411, 1434, 1439, 1894.
(c) carrying a nonempty label set (marked term, factor, component, activity, coefficient, region): ≈10, e.g. 11:138, 176, 252, 312, 393, 784, 1384, 1457, 1931.
(d) with insertions, of a whole object (marked density, expansion, step, polynomial, family, exponential): ≈16, e.g. 11:2, 218, 221, 381, 608, 1386, 1564, 1579, 1581; 11R:9, 212, 239, 291, 381, 391.
"Unmarked" = coefficient of `z_∅` (11:70 "unmarked density") or factor with empty label set (11:244).

**window** (3 / 13 / 4 / 0).
(a) index neighbourhood on which an operator is inverted (dictionary `Ω_i`): 10:358; 11:135, 673, 683, 684 — 5.
(b) interval of levels: 10:185, 189; 11:1462, 1675, 1795, 1965, 2091, 2092; 11R:215, 218, 222, 298 — 12.
(c) range of distances `|x|≤H^c`: 11:1726 — 1.
(d) compact set of point configurations: 11:2078, 2149 — 2.

**history** (23 / 14 prose / 3 / 4).
(a) finite trajectory for a cutoff (densities, couplings, arrays): 10: ≈21 (13, 15, 209, 232–256, 295, 447, 517, 792, 799, 805, 826, 849, 862, 889, 918, 927).
(b) the fixed choice of kernels, couplings, path pairs and representations (11:18): 11:18, 21, 26, 92, 117, 219, 736–741, 1665, 2058, 2091, 2183; 11R:5, 215, 392; 11E:2, 8, 34, 144 — ≈19.
(c) sequence of blocking kernels / parameters (dictionary): 10:373, 933; 11:1699 — 3.
(11:765 is an `\input` file name.)

**source** (3 / 36 / 1 / 2).
(a) source variable / monomial / "linear in the sources": ≈16 (11:49, 133–134, 507, 509, 1324, 1384, 1458, 1477, 1487, 1493, 1577, 1584, 1881, 1891, 2129; 11E:144).
(b) source weight: ≈12 (11:29, 192, 195, 496, 938, 953, 1044, 1370, 1374, 1377, 1590, 2200).
(c) source algebra: 11:13, 23, 2095 — 3.
(d) the source polynomial or density itself ("terminal regular source", "corrected source", "source density `q_k`", "actual source", "corrected source coefficient", "complete source norm bound"): 11:133, 769, 1671, 2097, 2140; 11E:84 — 6.
(e) an insertion ("local sources", "source anchors"): 10:173, 178 — 2.
(f) ch. 6 sense (inhomogeneous term of the affine map), undefined here: 10:900 ("actual source and event indicator"), 11R:43 ("clipped source") — 2.

**price / pay**: do not occur. `cost` etc.: section 1.5.

**detector, probe, readout, table**: do not occur in prose (labels only, section 4). `detect`: 3 uses, section 2.1.

**response**: 10:626 (?); 11:642 (`W`), 647 (`J`), 1729, 1730, 1750, 1773, 1775 (`Ψ_i`). See 2.2. None is the ch. 3 two-point function.

**transport**: 10:313 (parallel), 10:354 (stationary-field map); 11:648, 651 (two-form map `T`), 883 (`𝖹`), 1751 ("exterior-transport identities", ch. 5), 1788, 1812, 1813 (image under `𝓛`), 1870, 1958 (step acting on polynomials). See 2.2.

**frame**: 10:128 ("frame-choice variables", dictionary sense); 11:688, 690 ("root frame", "local frame": gauge choice); 11:1286, 1288, 1293 ("fixed radial polynomial frame", "frame coefficients": a basis of polynomials — third type of notation.md's "frame").

**anchor**: 10:178 ("source anchors") and 11:161 ("insertion anchor"): the site of an insertion (dictionary sense i/ii); 11:362, 364; 11R:141, 199, 209, 340, 375: "anchored" sums.

**phase**: 11:1714 ("phase difference", Fourier; standard). **word**: transfer word (11:842, 849, 863); difference word (11:2227, 2251, 2278, 2297, 2304); determinant-word series (11R:270, ch. 6 sense).

**root / rooted** (4 / 25 / 2 / 1).
(a) root of a tree or of a rooted sum (standard): 11:267–272, 300, 310, 393, 456, 508–510, 1918; 11R:329; 10:889.
(b) block root / rooted gauge (dictionary): 11:628, 631, 633, 688.
(c) number-of-cells root = chessboard seminorm: 11:817, `‖·‖_root` 2027, 2075.
(d) "rooted activity norm / bound / contribution" (11:1437, 1440, 1552, 1892, 1936): a norm with sums pinned at a marked site (inferred).
(e) square root (10:100, 108; 11:360; 11E).

**scalar** (16 / 13 / 4 / 0): (a) constant term of the action / normalisation (`v_0`, `σ`): 10:266; 11:609, 726, 789, 814, 2014; 11R:73, 190, 362–363. (b) the coupling correction `q_m` ("scalar correction", "projected scalar", "scalar recursion", "cumulative scalar bound"): 10:421, 645, 684, 772, 816, 826, 842, 849, 868–870, 902. (c) "scalar coordinates" = `λ` (10:443). (d) ordinary (scalar multiple, scalar majorant): 11:85, 1011, 1105, 1579, 2136.

**physical** (9 / 28 / 2 / 4): (a) in continuum units (period, volume, separation, cell): 10:128, 389; 11:981, 1030, 1124, 2190, 2301. (b) "physical coordinates" = the same fine link variables at both cutoffs (10:711, 725, 732, 896–898; 11:472). (c) "physical inverse couplings" = `β` as opposed to the coordinate `λ` (10:880). (d) "physical insertion / normalization / section / unit" = with the factor `a_N^{-d}`, as opposed to dimensionless (11:72, 86, 88, 920, 1051, 1109, 1158; 11E:7; 11R:5). (e) before division by `g` / unnormalised fluctuation (11:588, 696; 11R:60). (f) "physical counting coordinates" (11:621), "physical Lipschitz bound" (11:866), "physical jet block" (11:1832), "physical support-weighted mass" (11:423): not clearly any of these.

**unit** (1 / 18 / 1 / 0): identity insertion (11:87, 89, 389, 451, 1050); unit of support exponent (11:396, 495, 502, 528, 533, 939, 1446; 11R:141); units of measurement (10:128; 11:704, 861, 2301); "two unit bounds" = bounds by one (11:792).

**endpoint** (10 / 4 / 4 / 1): (a) the level-0 coupling (10:18, 209, 268–272, 278, 813, 850); (b) endpoints of an interval (10:139–140, 247); (c) the top level `k` of the restart window (11R:68, 89, 384, 387; 11:1930, 2092); (d) the last step at `N` (11E:124); (e) ends of a finite difference (11:2287); (f) 11:877 "normalized endpoint inequalities" (?).

**weight**: source weight `ω` (≈20); support weight `e^{σc_B}` (11:198, 204, 1369, 1446; 11R:188); filtration / scaling weight (11:407, 411, 1288, 1848); spatial / derivative weight (10:79; 11:351, 1068); probability / averaging weights (10:465; 11:563, 602; 11R:112, 361); "encoding weights" (10:382, ?).

**cutoff**: ultraviolet cutoff `N` (10 passim); smooth cutoff `γ` (11:314, 544–557, 708); threshold ("cutoff-to-noise ratio", 11R:61); path-length truncation (11:672); "failed cutoff condition / factor", "cutoff failure" = large-field event (10:532, 595–597; 11:151, 1476–1500, 1613; 11R:283, 311, 378). All but the last are dictionary senses.

---

#### 4. Terms the chapters do not determine

| Term | Where | What can be said |
|---|---|---|
| Hilbert encoding; encoding weights | 10:381–382 | An alternative parametrisation of path coefficients requiring summable weights. |
| block bridge | 10:921 | Something that must be "the same" in the auxiliary histories, with clipping data and stationary graph. |
| response bound `ε` | 10:626 | A constant of the ch. 9 remainder estimate. |
| sparse stopping scale | 10:172 | "Sparse" unexplained. |
| preselection bound | 11:382 | Value `C_d/L+o_x(1)` given, name unexplained. |
| selected slot | 11:424 | "Its selected slot has no purely principal component." |
| coarse kernel level | 11:352 | "coarse kernel level at least `d+3`" beside "fine kernel order"; whether level = order is not stated. |
| front-column (inverse front-column bounds) | 11:1343 | Gives `‖u‖_1≤D_k‖Au‖_1`. |
| exposure `𝓔` | 11:1285 | Only its lower bound is stated. |
| alphabet ("original marked alphabet") | 11:1911 | Possibly the original index set of terms. |
| coarse forecast | 11:726 | Possibly the conditional mean. |
| corrected body product estimate | 11:1662 | "Body" unexplained. |
| same-data restart conditions | 11:1666 | Not stated anywhere in these files under that name. |
| restoration levels | 11:1405 | Levels at which the weight is changed; not identified with `k`, `ℓ` or `w`. |
| `hot(s)` | 11:1934 | `u=a_*hot(s)^2`; by comparison with 11R:114 (`u=a_*h(s)^2`) this is `h(s)`. A leaked source name. |
| protected local representative / protected trial | 11:1063, 2306 | Not the "protected change of variables" sense. |
| finite decorations | 11R:304 | — |
| regular logarithms with holes; raised hole correction | 11R:365–367 | Refers to `ch08:reassembly`; not checked there. |
| deletion-of-support identities | 11R:239 | — |
| powered-curvature-factor estimate | 11E:14 | Refers to ch. 2; not checked. |
| exterior row | 11R:266 | — |
| "n copies" | 11:781 | "the stopping representation on `V` sites has `n` copies": copies of what is not said (marks? cells?). |

Garbled sentences produced by mechanical replacement (the intended term is recoverable from notation.md, "inventory → prescribed set of large-field sites", but the sentences no longer parse):
11:247 "The exact prescribed set of large-field sites condition says"; 11:296; 11:365 "support--prescribed set of large-field sites indices"; 11:1312 "It equals the without its event indicator `F_u^near`"; 11:1595 "the positive prescribed set of large-field sites decay"; 11:1637 "the original large-field prescribed set of large-field sites"; 11:1868 "the common with a smooth cutoff Gaussian estimate"; 11R:302 "The original prescribed set of large-field sites coverage"; 11:2133 "activities constrained to cover prescribed sites" as a noun phrase for the former "forced" activities.

Jargon surviving only in labels or symbols: labels `ch10:finite-tests`, `ch10:broad-test`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch10:shooting`, `ch10:prefix`, `ch10:drift-floor`, `ch10:equation-floor`; `ch11:mass`, `ch11:higher-modes`, `ch11:replicated(-bound)`, `ch11:root-bound`, `ch11:n-mark-root`, `ch11:actual-reader`, `ch11:detectors`, `ch11:detector-bound`, `ch11:uniform-detector`, `ch11:finite-detector-input`, `ch11:simultaneous-detector-lifts`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`, `ch11:weighted-output-envelope`, `ch11:opening-higher-weight`, `ch11:calibration-floor`. Symbols: `ε^{for}`, `w^{for}` ("forced": 11:360, 888; 11E:94–98), `z_{forced}` (11:1628), `‖·‖_root`, `hot(s)`, `f^{near,mask}`, `C_{orb}` (11:428), `M_f^{cut}` (11:715).

---

#### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| lower bound on the level where a stage starts | delay; stage delay; threshold for the starting scale; choice of a sufficiently large starting scale; condition on the starting scale; stage entrance; late entry (label); mesh threshold; inverse coupling threshold | *lower bound on the starting scale* (and *coupling threshold* where it is a bound on `β̂`) |
| lower bound on the block ratio | floor; stage floor; ratio floor; block floor | *lower bound on `𝓛_j`* |
| strict spare margin | reserve; margin; room to spare; retained unit; spare support (label) | *margin*, with the inequality |
| loss in an estimate | cost; expense; loss; inflation; amplification | *factor*; *loses a factor* |
| the top of the restart interval | comparison level; comparison depth; top level; opening (level); endpoint; "the stopping level `k`" | *level `k`* |
| the restart sequence | restarted history; auxiliary history; restarted representation(s); restarted family; presentations `P_i` | one name |
| representation of a density | local representation; presentation; (ch. 4) density coordinates | *representation* |
| main part of an insertion factor | principal; leading | *leading part* |
| its complement | nonprincipal; nonleading; remainder | *remainder part* |
| large-field part of an insertion | complementary part / stencil / cutoff; failed-cutoff factor; tail-event factor | *large-field part* |
| large-field event | cutoff failure; failed cutoff condition; warning; tail event; "hot" (symbol) | *large-field event* (one word) |
| activities constrained to cover given large-field sites | "large-field" activities; activities "with prescribed set of large-field sites"; "forced" (symbols); "selected" components; "hard" factor; compulsory / mandatory factor | *large-field activity with prescribed large-field set*; *its mandatory factor* |
| true density | actual; genuine; exact; "the object integrated" | *the density `ρ`* vs *its representation* |
| the map `T` | localization; extraction; coefficient extraction; common extraction; localization onto the polynomial label space | *localization map* |
| value of a correlation functional | measurement; tested correlation; correlation pairing; detection | *value of `L_i`* |
| cell of the reflected tiling | replica cell; reflected replica cell; reflection cell; measurement cell; comparison cell; copy | *cell* |
| insertion | insertion; mark; source (10:173); normalized local insertion; trial (when to be approximated) | *insertion*; *insertion point* |
| index of an insertion | insertion label; mark; source variable index | *insertion index* |
| sum over terms containing a site | site bound; site sum; containing-site bound | *site sum* |
| scale index | level; scale; depth; step (10 passim; "comparison depth", "cell depth" 11:2192) | *level* |
| cutoff-dependent | moving; varying; changing (10:450) | *cutoff-dependent* |
| inverse coupling in use | actual; tuned; common (11R:223); frozen | *the coupling `β`* vs *reference `β̂`* |
| `W` of chapter 5 | transport (ch. 5); (stationary forest) response (11:642) | one word |

---

#### 6. Overloaded symbols noticed

| Symbol | Meanings (line of first use) |
|---|---|
| `H` | dimensionless density `H_m` (11:84); `H_s=e^{(log log s)^2}` (11:746, 1151; the text itself disclaims at 11:1668); metric symbol `H(p)` (11:1681); `H_{0,f}` (11:647); incidence bounds `H_f,H_c` (11:506); gaps `H_i` (11:843); `H(J)_e` (11:405); function in 11:2282; in ch. 10 `H(q)` (10:546), arrays `H,K` (10:343), family `H(t)` (10:611) |
| `B` | support radius `B_m` (10:166); Gaussian bound `B≥1` (11:546) and `B=H^λ` (11:1862); slab kernels `B_i` (11:843); `B_0` covariance (11:1789); `B_k` lift bound (11:1360); `B_i^ref` base action (11R:356, text disclaims); `𝓑_m` block map |
| `b` | block constant (11:625); schedule `b_j` (10:122); endpoint `b` (10:269); `b_m(λ)` (10:402, text disclaims); `b_f(i)` (10:906); `b(x)=⌈(log x)^2⌉` (11R:15); patch radius `b=8B` (11:1152); exponent in `ρ=H^b` (11:1350); shift `b>0` (11:2246); factor bounds `b_j` (11:285); `b'_z` (11R:109) |
| `q` | density polynomial `q_m` (11:76); coupling correction `q_m` (10:417); site cost `q` (11:810); tolerance exponent `q` (11:1438; text disclaims at 11:1671–1673); number of slabs (11:843); `q_0` sites (11:1578); `q_d` stencil bound (10:79); `q_n` value cost (11R:227); gauge polynomial `q(x)` (11:405); `q_μ(p)` (11:1683); `q=Γ(U)` (10:544); `q^{site}` (10:167) |
| `T` | constant `T_e` (11:237); triangular map (11:373); transfer operator (11:843); two-form transport (11:648); localization map (11:1292); cell span (11:2336); affine map (10:342). notation.md already warns that `T` is not the stress tensor here |
| `R` | radius `R=x^{-3/8}` (11:693), `R` (11:863), `R=y^{1/256}` (10:520); remainder map `R_G` (11:382); automorphism `R_d`; corrected coefficient `R_I` (11:2068); support bound `R_f` (11:1395); constant `R` (11:1735); seminorm `𝓡_m`; density `R=e^{-E}R^0` (11R:197); period `R_p` (10:197); regular remainder `R` in `exp_*(χW−R)` (11:1490); iterates `R_i^{(q)}` (11:306) |
| `Z` | partition function; matrices `Z,Z'` (11:636); constant `Z` (11:978); terminal map `𝖹`; `Z_N^{val}` (11E:90); `Z_a` (ch. 9) |
| `D` | degree `D` (11:546, 1147); curls `D,D'` (11:622); `D_G` (11:796); union stencil `D` (11:922; 11E:95); densities `D_i` (11R:232); exponent difference `D`, `D_Y` (11R:119, 147); `D'` distance (11:1416); `D_k` inverse bound (11:1344); `D_l` difference (11:2234); `D=sup d_m` (10:870); number of coordinates (10:563) |
| `K` | `K=D^*M_fD` (11:624); activity `K_Y` (11:124); equation space `K_i` (11:1091) vs constants `K_i` (11:894); covariance `K_k` (11:1241); constant `K` (11:983, 2239); kernel `K(x,y)` (11:872); `K_j` (10:61, 558) |
| `L` | block ratio; functionals `L_i` (11:975); `𝓛` product of responses (11:1753); `𝓛_j` stage ratio |
| `M` | algebra element (11:51); `M_G` (11:381); metrics `M_f,M_c` (11:627); tour length (11:845); `M=⌈(log s)^2⌉` (11:1152; 11R:84); integer `M` (10:194); `M_q` (10:630); `M_f^{cut}` |
| `m` | level; inflation factor (11:274); mass (11:423); number of steps (11:1760); number of marked sites (11:1894); `(m,k)` stopping pair |
| `e` | support exponent `e` (11:226); degree `e` (11:919, 1089); `e_i=s_i^{-3}` (11:893); basis vectors `e_0,e_j`; edges; `e_{N,N',i}` errors (10:361) |
| `a` | lattice spacing `a_m`; incidence bound `a` (11:258); `a=‖G−H‖/s_f` (11:454); `a=4bϑ` (11:1222); means `a_j` (11:553); exponents; `a_*` (11R:78); `a_{dj}` (10:78); `a_h,a_s` (10:656) |
| `x`, `y` | activity array `x_m` (10:421); coefficient vector `x` (11:384, 899); `x=β̂` (11:320, 693; 11R:12); single-insertion bounds `x,y` (11:782); positions; `y=r(x_i)` (11R:52), `y=β̂_{m+1}` (10:520) |
| `z` | source variables `z_i`; incidence bounds `z`, `z_j` (11:322, 1542); complex shift (11:862); normalised coefficient `z_i` (11:995); `z=θ/g` (11:1254); weight `z` (11:2008); sites |
| `t` | threshold `t`, `t_N`; number of cells `t(S)` (11:194); mixture index (11:549); `t_C` (11:284); line parameter (10:464); span (11:2336); `t(x)` (10:649) |
| `g` | `β^{-1/2}`; occupancy (11:260); auxiliary `e^g` (11:1504), `g_i` (11:1637); `g_α` (11:1823) |
| `λ` | Haar measure `λ_N`; mixture weights `λ_t`; `λ=D'/3(2B+1)` (11:1423); exponent `λ` (11:1762, 1862); coupling coordinate `λ_m` (10:401) |
| `ρ` | density `ρ_N`; distance `ρ` (11:181); radius `ρ` (11:795, 865); dilation `ρ=H^b` (11:1350); `ρ_s` (11R:173) |
| `κ` | `κ_G`; `κ_i=(ε_i^{for})^{1/2}` (11:360); site sum `κ` (11:790); exponent `κ` (11:1438, 1955); covariance `κ_k` (11:1722) |
| `σ`, `η`, `δ`, `χ`, `ω`, `C`, `U`, `A`, `P`, `S`, `W`, `G`, `I`, `J`, `E` | each has at least three unrelated uses; e.g. `χ` is the plaquette function (11:797), the restarted indicator (11:1309) and `χ_m=β̂_m^{-1/32}` (10:399); `U` is a field and an exponent (11:196, 1380) and a matrix (11E:136); `G` is a graph (11:379), the group, a free matrix (11:983), a bound `G(x)` (11R:76), moments `G_I` (11:2064); `P` is `P_d^{loc}`, projections `P_f,P_c` (11:639), `P_{N,p,d}`, `P=H^{λ/4}` (11:1764), presentations `P_i` (11R:222), `P(p)` (11:1687), `𝒫` rooted projection (11:631), `𝒫(S)` partitions; `W` is a factor (11:314), the stationary response (11:642), `W_u` (11:1208), `W_ρ` (11:1135), `W_Y` (11R:148), `𝒲(B)` (11:262); `J` is the stage function (10:133), a local factor (10:540), a field-independent polynomial (11:97), the curvature response (11:647), radial coefficients (11:406); `C` is also `⌈(log s)^2⌉` at 11:1889 (elsewhere `M`) |

---

#### 7. The ten most confusing terms

1. **actual** (91 uses, six senses) — in most places it only means "of this construction", but in 11R it means the running coupling and in 11:627–662 the modified metrics.
2. **principal / nonprincipal / leading / nonleading** — carries the main case distinction of the marked step (11:284–292) and is never defined.
3. **selected** — "selected component" (large-field) and "selected trajectory" (fixed) alternate within single paragraphs (e.g. 11:1045 vs 11:1933).
4. **stage / plateau / delay / floor / request / threshold for the starting scale** — a whole scheduling vocabulary; "stage" is defined, the others are not, and "delay" has four or five paraphrases.
5. **comparison level, top, opening, middle, output, leading interval, lower interval, restoration levels, stopping pair** — three levels with many names and no single definition.
6. **reserve / cost** (44 + 42 uses) — the reader must reconstruct each inequality.
7. **graph `G`, column bound, raw map, rebasing** (11:379–468) — the single-insertion recursion is stated in undefined nouns.
8. **mark / marked** — three or four uses, and "source" used for the same objects in a further six ways.
9. **history** — defined in 11:18 in a sense different from chapter 5 and from chapter 10's "finite history".
10. **prescribed set of large-field sites** and its relatives (forced, compulsory, mandatory, hard, selected site factor) — the replacement phrase is used as an adjective and breaks sentences (section 4); **incidence**, **trial** and **lift** are close runners-up.

---

#### 8. Not read / not checked

- All four files were read in full. The `figures/cutoff-histories` file input at 10:835 was not read.
- Occurrence lists come from `grep` on single lines; a term split across a line break is missed. Per-sense counts marked "≈" were assigned from one-line contexts plus the full read and may shift by a few.
- Cross-chapter definitions were looked up only by grep, and only for: fusion, reset, low-order, principal (ch. 9); Warnings, compulsory, subpower (ch. 6); separating family (ch. 3); exchange term (ch. 7). I did not read those passages in full. Not looked up: "holes" / `ch08:reassembly`, "powered-curvature-factor estimate" (ch. 2), "principal norm" (ch. 9:235), "block bridge", "kernel level", the ch. 13 uses of "trial" and "stopping".
- No Lean source was consulted; no proposed equivalent was checked against the literature. Proposals marked "unsure" or "keep, but define" are my own judgement.
- Section 6 is a list of what I noticed while reading, not a systematic symbol audit.

### IV.B Independent audit

*Original title: Audit B: Part IV.A and the overview claims for chapters 10–11*

> **Status.** Independent check of Part IV.A by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in Part I, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only audit. All four chapter files were read in full (`10` = `10-common-trajectory.tex`, `11` = `11-marked-insertions.tex`, `11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`), plus sections 1, 8, 9 of Part II, the whole overview, and the passages of chapters 5, 8, 9, 12, 13, 18 cited below. No repository file was edited.

**The worktree changed during the audit.** Commit `ac15effb` ("Repair thirteen sentences broken by mechanical term replacement") landed while I was reading. It rewrote 11:247, 296, 365, 1312, 1595, 1868–1869 and 11R:302; line numbers are preserved. The survey and overview were written against the earlier text. Where this matters I say "pre-repair" or "at HEAD". The commit message names the replaced source words: *inventory*, *unmasked*, *guarded*, *entry-controlled*.

Occurrence counts were re-done with `grep -noiE` after stripping `\label`, `\ref`, `\eqref`, `\input`, `\cite`.

---

#### Definite errors

1. **`row` at 10:354 is assigned to the wrong sense.** The survey (section 3) and the overview (2.2) put "actual quadratic rows" under "component of the action vector". The sentence cites Proposition `ch05:horizon-limit`, whose title is "Convergence of the selected Gaussian rows" and which is introduced by "Write a translation-invariant row as $K_{ab}(z)$" (5:711–712); its conclusion is "All limits are for the actual chosen rows on the cover" (5:752). This is the chapter 5 sense, kernel of a translation-invariant operator. 10:356 ("direct row coefficient") is correctly the component sense (5:749 "the fixed direct coefficient $c$").

2. **"Selected component and selected trajectory alternate within single paragraphs" is false.** Survey section 7 item 3 cites "11:1045 vs 11:1933", which are about 900 lines apart; overview 2.3 repeats the claim. Using the survey's own line lists for senses (a) and (b), no blank-line-delimited paragraph in any of the four files contains both. The nearest cases are adjacent paragraphs (11:1933 vs 11:1965) and one proof (11R:89 vs 11R:159).

3. **"the stopping level `k`" is quoted but does not occur.** Survey section 5 lists it, in quotation marks, as a name for the top of the restart interval. `grep "stopping level"` finds nothing in chapters 10–11 (only "stopping pair", "stopping scale", "stopping representation", "stopped at"). The identification is also doubtful: in the restart argument the chessboard normalisation is done at the output level ("At the output $V=q_0$", 11:2019), not at the top level `k`.

4. **`hot` is not a word for the large-field event.** Survey section 5 lists `"hot" (symbol)` among names of the large-field event. `hot(s)` is a function: "$u=a_*\,\mathrm{hot}(s)^2$" (11:1934) against "put $u=a_*h(s)^2$" (11R:114), so `hot(s) = h(s) = e^{(\log\log s)^{3/2}}`. The survey's own section 4 says this; the cluster entry reads meaning off the name.

5. **`mesh threshold` is not a synonym of `delay`.** Survey 1.1 files "mesh threshold" (11:1119, 1815) under "Same thing as delay: requirement `τ_m ≥ b_j log 3`". The text makes it a lower bound on the cutoff `N`: "once the mesh is sufficiently fine relative to the fixed physical cell" (11:1123–1124), "one mesh threshold ensures the required nonwrapping and separation for every period" (11:1129–1131).

6. **`backward comparison / descent` is not "downward induction in the level from N".** The induction on the cone condition runs upward: "The induction starts at the bottom with zero coefficient" (11:909), concluding "$A_{i+1}|x_{i+1}|\le c_{i+1}$" (11:908). "Descent" is the propagation of the terminal trial down the block steps, which gives the decay $e^{-(\tau_N-\tau_i)/8}$ (11:915).

7. **`common localization / extraction`: "two words for one map" merges two maps.** 11:372–377 is the one-step map: "Localization by Taylor expansion of the fine local section … gives a triangular change of basis $T$", leading map $TS_L$. The common localization map is a different `T`, built at the comparison level: "Define $Tu$ to be precisely these frame coefficients" (11:1292–1293), with $\|Au-Tu\|_1\le\tfrac12\|Au\|_1$. 11:1180 and 1203 ("localization by radial Taylor expansion") give `Au`, a third object. The survey's own section 6 lists the two `T`s separately.

8. **`hard` / `soft`: the proposed "small-field corrections" is wrong.** 10:656–666 is an instance of Proposition `ch09:fusion-prop` (9:652–666): hypotheses "$|k_i|\le e^{-\kappa}v_i$, $|e^{\ell_a}-1|\le v_a$", conclusion "$\mathcal K_m(K)\le e^{-\kappa}(e^\gamma-1)$", matching "$e^{-\zeta}(e^I-1)\le\phi$" (10:664). So hard = bound on the preliminary large-field activities; soft = bound on the logarithmic correction factors $e^{\ell_a}-1$. These are not small-field: "with $\ell_a=0$ when $Z_a$ is small-field" (9:634–635).

9. **`ch10:shooting` is listed as jargon "surviving only in labels"** (survey section 4 last paragraph; overview section 7), but the word is in prose: "uniqueness of the shooting parameter" (10:273), "the choices made in shooting" (10:818). The survey's own row 1.1 cites both lines. The same list contains other labels whose words are in prose: `drift-floor`, `equation-floor`, `calibration-floor` ("floor", 10:55, 90), `ch11:mass` (11:423), `ch11:root-bound` (11:817), `ch11:replicated` ("replication costs", 10:172).

---

#### Basis codes that overstate or understate

**Overstated**

- **fusion — "D (ch. 9)", "defined in ch. 9".** The word occurs in chapter 9 only inside labels (`ch09:fusion`, `ch09:before-fusion`, `ch09:fusion-prop`). The section is titled "Absorbing logarithmic corrections into large-field activities" and the proposition "Exact regrouping". The stated meaning is right; the basis is I (identified through label names).
- **dictionary — R.** No sentence says what a dictionary is; "coefficients $c_N(\gamma)$ on a common dictionary" (10:375–376) supports "index set" only by inference. R / I.
- **path coefficient `α_{N,m}` — R at the cited lines.** 10:422–423 says only "the one already used in the exact step". The meaning is settled in chapter 9: "The coefficient $\alpha$ is the matched determinant coefficient, not an adjustable trial inverse coupling" (9:409–411), "$\alpha=-\kappa_G\log L+O_j(1)$" (9:739). R, but by chapter 9.
- **complementary part — R.** "One minus the small-field indicator" is not in 11:147–151; it is explicit only at 11:1490–1494 ("factors $1-(1-\chi)Rz_I$"). R / I.

**Understated**

- **mark / marked — I, resting on `notation.md`.** The text gives it: "let $\rho_N\ge0$ be the unmarked density" (11:70) and $q_N=\rho_N\prod(1+z_iF_i)$ (11:75), so unmarked = coefficient of $z_\varnothing$, marked = carrying $z_S$, $S\ne\varnothing$. R.
- **eligible (2.2) — I, "neither dictionary sense is clearly meant".** Settled by 8:286–295: families of large-field labels with disjoint supports and $\bigcup I_\eta=D$; "The exact rules for eligibility are part of the definition of an effective density". The overview section 3 already records this; the survey row does not.
- **cone inequality — I, "presumably".** 11E:125–128 uses "$|e_j-u_j|\le4K_{N-1}L_{N-1}^{-3/8}c_N$", which is 11:905–906 ("If $A_i|x_i|\le c_i$, substitution gives $y_i\le4K_ie_ic_{i+1}$") with $e_i=s_i^{-3}=L_i^{-3/8}$ (11:893). R.
- **residual scalar correction `q_m`.** D is right; add that it is `Δ` of `(ch09:reset)`: "$\beta=\beta'+\alpha+\Delta$" (9:719), bound "$|\Delta|\le C_jH_{\rm pre}/t_m^2$" (9:733), matching "$f_m=C\varepsilon x^{-11/10}/t(x)^2$" (10:648).

---

#### Sense misassignments (with my per-sense counts)

Total counts per file agree with the survey for every word below.

**row** (2 / 10 / 4 / 0). Mine: kernel of a translation-invariant operator 1 (10:354; missed sense, see Definite errors 1); component of the action vector 6 (10:356; 11:668, 710; 11R:101, 102, 122); literal matrix row 7; vector in a list 1 (11:2253); undetermined 1 (11R:266).

**actual** (18 / 58 / 15 / 0). The survey's six senses and counts hold to within three. Borderline lines:
- 11R:45 "these actual thresholds" is under (b) running coupling; the thresholds are $\vartheta(x_i)$, functions of the reference coupling. Belongs to (a).
- 11:676 (section title "Actual local coordinate and cutoff estimates") is under (a); the section is the actual-to-flat comparison (11:681). Belongs to (c).
- 11:1216 "the Taylor polynomial of the actual function is unique; it does not require a linear choice of its separate activity representatives" is under (c); the contrast is function against representation, sense (d).
- 11:1325, 1950, 2097 ("actual density", "actual pushed density", "actual source") are under (a) and fit (d) equally.
- My counts: (a) about 54, (b) 16, (c) 10, (d) 3 to 6, (e) 3, (f) 3.
- I agree that the chapter 5 "gauge-covariant block average" sense does not occur.

**selected / selection** (5 / 30 / 12 / 3, excluding "preselection" and counting "unselected" separately). Mine: (a) large-field 25, (b) fixed by the construction 15, (c) ordinary "choose" 10. Four lines the survey puts in (b) are ordinary: 10:892 "A new selection of equally bounded coefficients", 11:219 "before the history thresholds are selected", 11:2084 "before selecting the stage orders", 11E:30 "the selection order". No sense missed.

**test** (1 / 11 / 1 / 0). All 13 assignments confirmed: standard 2, tested correlation 5, tested links 3, evaluate/check 3.

**label / tag** (6 / 27 / 5 / 2). All 40 confirmed: polynomial label 13, insertion label 13, index of a term 8, random index 4, not prose 2.

**mark / marked** (11: 67 hits including 17 "unmarked", so 50; 11R: 6). The survey's four groups sum to 56 and the examples are correctly placed. (a) "mark" and (b) "marked point / site / ancestor" are one sense, noun and adjective, and should be merged.

**window** (3 / 13 / 4 / 0). All 20 confirmed: index neighbourhood 5, interval of levels 12, range of distances 1, compact configuration set 2.

**history** (22 / 14 / 3 / 4 by my count; survey says 23 for chapter 10).
- 11:92 "Changing the block history" is under (b); the proposition replaces kernels only ("Replace any kernels below a fixed level $k$"), so it is (c), the kernel sequence.
- Senses (a) and (b) are close to one sense: chapter 10 already attaches the choices to the trajectory ("Choose one such history for each $N,p$, retaining its path arrays, forests, local integral choices and output representations", 10:256–257). Judgement.

**source** (3 / 36 / 1 / 2). 11:1632 ("Reassigning a principal source term") is in no list. Otherwise confirmed.

**response** (1 / 7 / 0 / 0) and **transport** (2 / 9 / 0 / 0). Lists complete and correctly assigned. That `W` of 11:642 is the chapter 5 transport checks out: $AW=bQ^*$ and $KW=Q^*K'$ with $A=K+bQ^*Q$ give $QW=I-b^{-1}K'$.

**New senses claimed in 2.2.** stage, history, lift, frozen, envelope, mass, target, window confirmed. Missed: `extraction` has a further sense at 11:2037, "The estimates are before extraction", which is not the coefficient-extraction map (compare 11:2214 "a comparison before any cutoff limit"); I could not determine it. `leading` has three uses the survey does not separate: leading-order map ("the leading map is $TS_L$", 11:370–377), the upper interval `k→ℓ` ("leading interval", "leading recurrence", 11:1643, 1952), and the principal coefficients ("corrected leading coefficients", 11:1551, 1886).

**physical.** 11:588 "replace the physical coordinates by $a+\eta_t$" is under (e) "before division by `g`"; those coordinates are the "normalized local curvature coordinates" $\xi_{t,I}$ (11:558–560), contrasted with the Gaussian model.

---

#### Wrong line references and misquotations

- raw: 11:901 should be 900 ("the raw inequalities give"); 11:1014 should be 1013.
- presentation: 11R:250 should be 251 ("incoming presentation").
- stationary graph / jets (2.1): 10:336 has "stationary formula"; "jets" is only in the `\eqref` label there. "Stationary jets" is at 10:717.
- inherited (2.1): 10:761 "multiplicities inherited from the input arrays" is the ordinary word.
- occupancy: 11:260 defines `g` but the word is at 11:345 and 10:109 only.
- principal row: "Purely principal connected components … contain neither" alters the text, which reads "since it contains neither an unmarked correction nor an incoming large-field factor" (11:331–332).
- "the stopping level `k`": not in the text (Definite errors 3).
- Overview 2.7: "`J = H₀⁻¹ T H₀`" drops the subscripts; the text has "$J=H_{0,f}^{-1}T H_{0,c}$" (11:647), two different operators.
- Overview 2.10: the history sentence is at 11:18–19, not 17–18.
- All other quotations I checked are verbatim up to line breaks and TeX markup (about 60, including every quotation in sections 1.1, 2.3, 3 and 4).

---

#### Omitted terms

House terms in these chapters with no row in the survey:

- **prescribed set of large-field sites / prescribed large-field set** (about 20 uses). Only in the garbled-sentence list and section 7. It is defined: sets $I_\eta\subset D\cap Y_\eta$, "The set $I_\eta$ records the large-field sites assigned to that activity" (8:286–288), with exact cover $\bigcup I_\eta=D$.
- **normalized local insertion** (14 uses, e.g. 11:353, 895, 2191). `notation.md` gives it as the replacement of "primary source"; presumably $O_{N,p}(d,c)$ of 11:1051–1054, which the text calls "the physical insertion".
- **ordinary** as "small-field / regular part": "ordinary remainder" (11:940), "ordinary norm bound" (11E:83), "ordinary contribution" (11E:111), "ordinary chart bound" (10:97).
- **block length / length** for the block ratio `L`: "fixed before the block length" (11E:20), "then the length, then the inverse coupling threshold" (11E:31–32). 11:1873 "Choose the block length after $A_{2D}$" may instead mean the number of steps `m`; not determined.
- **pre-threshold constants** (11:1396), the counterpart of "post-length".
- **energy / suppression** of a large-field component: "whose suppression is $\exp(-c\beta_Nt_N^2 n)$" (11:167–168), "selected-component energy" (11R:63), "energy reserve" (11:521).
- **value** against derivative: "weighted derivative and value norm" (10:391), "terminal value norms" (10:106), "global value" (11:925), "value tails" (10:765). Only "value cost" has a row.
- **bottom**: "common bottom endpoint" (10:850), "bottom residual coefficient" (11:896).
- **fit(s)** in the accounting sense: "its site bound fits $\omega_n$ … The other components fit $\delta_n-\omega_n$" (11R:330–332), "fit inside the remaining margin" (11R:305–306).
- **kill**: "Each conjugate kills $E_i$" (11:970), "killed by $X$" (11:1691). The overview has it; the survey does not.
- Program-style words: **returned** ("the actual returned arrays", 10:777–778; "the returned inverse coupling", 10:785); **reported** ("the reported bound $G(x)$", 11:1597); **declared / declaration** (11:441, 534); **encoded** ("encoded coefficients of a normalized lattice difference", 11:991).
- **coefficient functionals** ("fixed common coefficient functionals", 10:373, 813, 889) and **curl-division and path-placement operations** (10:314): undefined here.
- Smaller: **attenuation** ("polynomial attenuation", 11:1657), **true-length** (11R:102, 133, 274), **consume** ("consume one box factor", 11:1740), **weaken** (11R:275, 279), **discarded-support** (11:1201, 1235), **tolerance exponent** (11:1673), **arity** (11:343, 2041–2047), **exchange term** (10:337; the survey's section 8 says it was looked up but there is no row).

---

#### Questionable equivalents

- **moment norm → "norm of the functional on `c_0`".** Wrong space. $\sup_n|\sum_ia_i(t_i/q)^n|$ is the sup norm of the moment sequence, an element of $c_0$ (10:476–477); equivalently the norm of $f\mapsto\sum a_if(t_i)$ on power series with norm $\sum|f_n|q^n$ (the norm $|f|_R$ of 10:535–536). I would write "sup norm of the moment sequence". The duality is standard; the name "moment norm" is the text's.
- **principal → "leading part".** Collides with "leading interval / step / recurrence" (11:1410, 1643, 1952) and "leading map" (11:377). Keep "principal", defined once.
- **stage → "regularity level `j`".** Collides with "level `m`", which the survey's own section 5 proposes for the scale index. The overview's "regularity class" is safer.
- **hard / soft → "large-field factor / small-field corrections".** Changes the mathematics (Definite errors 8). Use "preliminary large-field activity" and "logarithmic correction factor $e^{\ell_a}-1$".
- **backward comparison, descent → "downward induction".** See Definite errors 6. I would use "propagation of the terminal trial down the block steps".
- **corrected coefficients `R_I` → "truncated (connected) coefficients"** (the survey marks this unsure). It would be wrong: $R_I$ is the coefficient of the source polynomial multiplied by the inverse of $\sum_IG_Iz_I$ (11:2096–2098); only its logarithm differs from the connected coefficients by the free ones. Keep "corrected".
- **reset → "redefinition of the coupling".** `(ch09:reset)` fixes the output coupling and the scalar together ("The output inverse coupling and scalar are now fixed", 9:716). "Definition of the output coupling" is closer.
- **moving → "cutoff-dependent".** Right at 11:1083, 2218; at 10:730–731 the expression "would move with the mean or precision".
- **delay → "after increasing the starting scale of the stage".** Fits 11:1192–1200. The terminal delays of 10:107–112 are conditions at the cutoff level `N` ("$\widehat\beta_N\ge a_{d,J(N)}$").
- **Section 5 cluster "large-field event: … tail event".** "Tail events" (11R:43) and "tail-event factors" (11R:284) may be Gaussian tail events of the chapter 6 chart; the merge is an inference.
- Sound, as far as I know the standard usage: "graph transform" for $G\mapsto R_GM_G^{-1}$; "column bound" as the $\ell^1\to\ell^1$ operator norm; "identity insertion" for unit; "modulus of continuity in the insertion point"; "cyclic product of transfer operators"; "majorant" for envelope; "extended by zero"; "index set" for dictionary. I am unsure whether "chessboard seminorm" (as opposed to "chessboard estimate") is established usage.

---

#### Overview claims (errors / confirmed)

**Errors**

- 2.2 `row`: 10:354 is in the wrong row (kernel sense).
- 2.3: the "alternate within single paragraphs" sentence is unsupported.
- 2.1 table, chapters 10–11 column: the survey's sense (f), "under the law in force" (11:280, 293, 1613), has no row, so the column sums to 87 against 91 uses. The other entries match the survey (55 / 10 / — / 17 / — / 3 / 2) and my recount to within three.
- 2.7: heading says "ten senses", the table has nine rows; `J` formula misquoted; "response bound" (10:626) is not placed.
- 2.9: the survey's sense "range of distances" (11:1726) is omitted.
- Section 4 lists as undetermined, under other chapter groups, terms that chapters 10–11 or 13 settle:
  - `attachment`: mechanism at 11:147–156 ("Join each complementary stencil to every selected large-field support it meets").
  - `site conversion`: 11:266–272.
  - `weight restoration`: 11:1374–1454.
  - `trial encoding`: the reference label $v_{N,p}$ of 11:945–951 (11:1074–1076).
  - `root estimate`: "Taking the number-of-cells root" (11:817–822).
  - `sparse stopping`: 13sb:102–110.
- Section 7: `ch10:shooting` and several others are not label-only (Definite errors 9).
- Section 6, further broken text in these chapters at HEAD:
  - 11:1636–1637 "retains the original large-field prescribed set of large-field sites" (not repaired by `ac15effb`).
  - 10:922–923 "identifies a / auxiliary graph" (article).
  - 11:938 "has cover at most81;" (missing space).
  - 11:1589 "The ordinary bound for terms involving at least two insertions by one has neither …" (parses with difficulty).
  - 10:98 "the relaxed small-field smooth cutoff is one": `notation.md` line 93 says of the same object "Relaxed small-field test … not a smooth cutoff", and the repair commit names "guarded" as a replaced word, so this is probably the same kind of artefact. Conjecture, not verified.

**Confirmed**

- Section 1 bullet for chapters 10–11: none of `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector`, `purchase`, `ledger`, `fund`, `share`, `spent`, `excess` occurs in the prose of the four files.
- 2.4, 2.5, 2.6 as far as they cite these chapters; 2.9 lists; 2.10 quotations for history and stage, and `J(m)`; 2.11 "transfer word", "difference word".
- Section 3 rows: regularity-stage index (10:25–31, 129–134), coupling band (10:212, verbatim), width (10:375–381), envelope (11:1581), Warnings (11:319–320 verbatim; correctly "still inferred"; the word occurs only at 6:1476 and 11:319), compulsory (10:654; 11R:161), eligible (8:294–295, verbatim).
- Section 4: `hot(s)` against `h(s)` (11:1934; 11R:114).
- Section 6 reread:
  - 11:247 and 11:1312 were verbatim pre-repair.
  - 11:365, 1595, 1868 and 11R:302 were broken pre-repair as reported.
  - 11:296 parsed, as a noun stack.
  - 11:2133 parses.
  - All except 11:1637 are repaired at HEAD, so the overview's quotations no longer match the files.
- Section 7 labels for chapters 10–11 all exist.

---

#### Terms the survey calls undetermined that the text settles

- **sparse stopping scale** (10:172). 13sb:104–109: "Choose $k=k(m)$ as the first level $k\ge m$ with $B_k^2\le a_m/a_k$", then "$(a_m/a_k)^4q_k^{\rm site}\le(L_{k-1}B_{k-1}^2)^4q_k^{\rm site}=o(\tau_k)$", which is the condition imposed at 10:167. Also 18lp:156–160. The word "sparse" itself is still unexplained.
- **Haar-ball normalization argument; replication costs** (10:169–172). 13sb:36–37 "The Haar-ball argument of Section `ch11:replicated`", i.e. 11:795–805; the cost is the factor $e^{(a_m/a_k)^4q_k}$ of 11:819. The survey's guess is right and can be R.
- **"n copies"** (11:781). `n` is the number of reflected cells: the bound $e^{Vq+n(x+y+2)}$ (11:809) becomes $e^{(a_m/a_k)^4q_k+x+y+2}$ on "Taking the number-of-cells root" (11:817–819), which requires $V=n(a_m/a_k)^4$.
- **restoration levels** (11:1405). The middle levels `ℓ`: "the corrected leading coefficients at the middle level … their rooted contribution at the restored weight" (11:1551–1553); "On the lower interval … at the restored weight" (11:1564–1569); 11:1405–1407 contrasts them with "the separated opening sites". Strong inference, not a definition.
- **deletion-of-support identities** (11R:239). Probably `(ch08:deletion-identity)`: "delete all labels whose supports meet $Y$", $Z_{\rm pol}(z^Y)/Z_{\rm pol}(z)=e^{-\mathcal L_Y(z)}$ (8:208–215). Inferred from the name and the reference at 11R:367.
- **regular logarithms with holes; raised hole correction** (11R:365–368). 11R:367 refers to `(ch08:reassembly)`, $Z_D=e^{\mathcal L(z)}\sum_B(\prod K_\eta)e^{-\mathcal L_{Y(B)}(z)}$ (8:311–315). The "hole" would be the deleted set $Y(B)$ and the "raised hole correction" $e^{-\mathcal L_Y}-1$, consistent with "using $|e^{-c}-1|\le e^{|c|}|c|$" (11R:369). Probable reading only; "hole" does not occur in chapter 8.

I agree these remain undetermined: Hilbert encoding, block bridge, response bound `ε` (no "response" anywhere in chapter 9), preselection bound, selected slot, coarse kernel level, front-column, exposure, alphabet, coarse forecast, corrected body product estimate, same-data restart conditions, finite decorations, exterior row (no "exterior" in chapter 6), protected local representative / protected trial (13:229 reuses the phrase without explaining it).

---

#### Confirmed rows

Meaning, basis and references as stated, apart from the points above.

- **1.1:** stage; plateau; schedule; floor; delay; request; inner barriers; shooting; tuned; coarse target; comparison level and its family (except restoration levels); comparison window; stopping pair; restart; recording scale; re-expression of the endpoint.
- **1.2:** history (both rows); pad by zero; prescribed-site rules; finite parameter evaluation (meaning); narrow / reserved band; compensation; held fine reads; real nodes; reset (meaning); low-order collection; residual scalar correction; stationary branch; moving expression.
- **1.3:** source algebra; source weight and restoration; insertion label; push; unit; principal (meaning, I); inflation factors; incidence; site bound; occupancy; menu; join / attach; graph `G`; raw; rebasing contraction; column; vanishing-jet remainder; screened; mass; common Gaussian; corrected source; near part; lift; magnification; measurement; trial; terminal map; calibration; admissible; equation subspace; positional modulus; transfer word; difference word; plant; spans; chessboard seminorm; replica cell; envelope; expense.
- **1.4:** all rows except the two settled above.
- **1.5:** counts for cost (10/22/10/0), reserve (19/18/5/2), retain (9/31/18/2), supplies (3/13/1/0), subpower (2/11/1/4) exact; absorb, margin, input within three.
- **2.2:** history, stage, response, transport, mass, lift, window, frozen, target, envelope, weight.
- **2.3:** all rows.
- **Section 4:** all rows except those listed in the previous section. The garbled-sentence list was accurate pre-repair.

---

#### Not checked

- Survey section 2.1 was spot-checked (about 25 of 35 rows), not checked row by row.
- Survey section 6 (overloaded symbols): about 30 entries spot-checked, all correct; not audited systematically.
- Per-occurrence classification of `scalar`, `unit`, `endpoint`, `weight`, `cutoff`, `root`, `frame`, `anchor`: totals checked, assignments only sampled. `physical` was checked for senses (a)–(e) only.
- "powered-curvature-factor estimate" (11E:14) was not traced in chapter 2.
- `figures/cutoff-histories` was not read.
- No Lean source and no literature were consulted; the judgements on proposed equivalents are from my own knowledge.

---

<a id="part-v"></a>

## Part V. Chapters 12–16

### V.A Survey

*Original title: House terminology in chapters 12–16 (survey C)*

> **Audited.** An independent check of this survey is in Part V.B; its corrections supersede the text below, which is kept as returned.
>
> **Status.** Survey by one agent (Claude Fable 5.2 subagent), reproduced as returned. It was written against upstream commit `7bec3925`. Meanings marked I are inferences; proposed equivalents were not checked against the literature. See Part I for the cross-chapter synthesis and for what was verified.


Read-only survey; no repository file was edited. Worktree `manuscript/HumanizeYM_v3/chapters/`.

File abbreviations (line numbers are those of the worktree files):
`12` = 12-ultraviolet-limit.tex; `13` = 13-continuum-fields.tex; `13sb` = 13-sharp-bounds.tex; `13ba` = 13-bounded-approximations.tex; `18gq` = 18-graded-quotient.tex; `18lp` = 18-lattice-products.tex; `14` = 14-reflection-ward.tex; `14lc` = 14-lattice-comparison.tex; `15` = 15-phases.tex; `15sp` = 15-sharp-phase-bounds.tex; `16` = 16-reconstruction.tex. `10:`/`11:` = 10-common-trajectory.tex / 11-marked-insertions.tex (consulted by grep only, for definitions).

Basis codes: D defined in text; R read off an explicit sentence or formula; I inferred; ? not determined. Categories: (a) accounting, (b) program/Lean leakage, (c) ordinary/standard word in unusual sense, (d) coined, (e) other.
Counts are occurrences from `grep -o -i` after stripping `\label/\ref/\eqref/\input` arguments.

General observation. The accounting words `price, pay, purchase, budget, fund, receipt, ledger, portfolio, owner` do not occur in these files (grep: 0). `readout`, `table`, `tag`, `likelihood`, `compulsory`, `warning`, `seeded` also do not occur. What remains is (i) `cost`/`reserve`/`loss`/`request`/`supply` vocabulary, (ii) a large undefined vocabulary inherited from chapter 11 (graph, column, trial, attachment, section, incidence, mode, stage, history), concentrated in `12`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, and (iii) coined analytic names in `14`–`16` (heat, damping, height, tied, padding, slab, whole word). Chapters `14` (after line 258), `15`, `16` are close to ordinary mathematical prose.

---

#### 1. New terms (not in the ch. 3–6 dictionary)

##### 1.1 Renormalisation-group / marked-density vocabulary (ch. 12, 13 fragments, 18 fragments, 14lc)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| graph; admissible graph; remainder graph; output graph; terminal graph; selected graph; graph contraction | 12:38, 39, 82, 89, 91 (17 occurrences, all in `12`) | D at 12:82–83 | A linear map `G: V_d → R_m` from labels to remainder arrays with `‖Gx‖ ≤ s_m‖x‖_1`: "An admissible graph $G:V_d\to\mathcal R_m$ obeys …". Why it is called a graph is not said (presumably the remainder viewed as a function of the coefficient; 11:379 "incoming linear graph"). | D (name unexplained: I) | *remainder map* `G`; *admissible remainder map* | c |
| fixed-input (cutoff) continuity; fixed-input comparison | 12:36, 41, 128, 133, 141 | D at 12:36–38 | "applying the cutoff-dependent marked map to any fixed admissible remainder graph gives Cauchy output graphs and coefficient maps" | D | *continuity in the cutoff at fixed argument* | b/d |
| coefficient map `I_G`; unreparametrized remainder map `J_G` | 12:90–91 | R | Named and given notation only; `ΦG = J_G I_G^{-1}`. "Unreparametrized" = before composing with `I_G^{-1}` (I). | R / I | *remainder map before renormalising the coefficient* | d |
| forgetting (the terminal graph) | 12:131 (title) | no | Independence of the level-`m` graph from the graph inserted at level `m+h`, up to `2^{1-h}` (12:139–143). | R | *independence of the initial remainder map* | c |
| stopping (level, scale, estimate, errors, data); stopped expression; sparse-stopping argument | 12:10, 225, 251, 302, 304; 13sb:85, 102, 137; 13ba:193; 18lp:159 (10) | R at 12:207–217 | Evaluating at an intermediate level `m` after setting to zero all terms with two or more source variables: "Keep the complete terms linear in the sources and set only these higher entries to zero" → `C_{N,p,m}` (12:212). In `13sb` the "stopping level" is `k(m)`, "the first level $k\ge m$ with $B_k^2\le a_m/a_k$" (13sb:104). "Sparse" (18lp:159; 10:172) is not explained. | R; "sparse" ? | *truncation at level m*; *truncated correlation* `C_{N,p,m}`. Avoid "stopping" (stopping times). | c |
| dictionary (of local supports and inventories) | 12:23, 25 | no | A common index set of supports and large-field site sets used for all cutoffs `N>m` (cf. 10:376 "common dictionary"). | I | *common index set* | b |
| (large-field) inventory | 12:24, 239 | no | `blueprint/notation.md`: "prescribed set of large-field sites". Elsewhere already replaced by that phrase (12:27, 162). | R (notation.md) | *prescribed set of large-field sites* (two survivors at 12:24, 239) | b |
| large-field profile; grouped profiles; prescribed-site profiles; complementary profile | 12:26, 28, 78, 161, 180 (10 in `12`); 13ba:165 | D at 12:26–27 | "the sum of activities having one particular support and prescribed set of large-field sites". "Complementary profile" (13ba:165) is not defined (I: the large-field part of a term). | D; 13ba:165 I | *total large-field activity with given support and large-field set* | d |
| exact-cover gas; unmarked gas | 12:180; 18lp:186 | no | The sum over exact covers (dictionary 2.4 "exact cover") of products of large-field activities; "a finite polynomial in the latter profiles and fixed eligibility indicators". "Unmarked gas" = the same without insertions (I). | R / I | *polymer sum over compatible families*; *partition function without insertions* | c |
| complete (remainder, source, bound, transfer, push, marked version) | 12:67, 115, 160, 208, 252; 13sb:65; 13ba 8×; 18lp:90; 15:184 (16) | no | Including both regular and large-field parts and (usually) all terms with ≥2 insertions: "the complete regular and large-field remainder on common supports" (12:115); "its complete bound, including the complementary large-field part" (13ba:16). | R | say what is included each time; *full* | c |
| terms linear in the sources; terms involving at least two insertions; higher (regular) entries; (joint, partial, incoming) modes; absolute mode sums | "linear in the sources" 19×; "at least two" 15×; "higher entries" 12:202, 209; "mode(s)" 13sb:73; 18lp:73, 74, 184, 245 | R at 12:200–209 | Coefficients of the monomials `z_S` in the nilpotent source variables; "mode" is the untranslated word (notation.md: "higher modes … Terms involving two or more insertions, indexed by the source monomial"). "Partial modes of a group" = monomials containing only some of the group's variables (I). | R; partial modes I | *coefficient of z_S*; *terms of source degree ≥ 2* (the text itself says "source degree" at 12:270). Use one phrase. | b |
| source weight(s); mark weights; marker weight / marker amplitude; residual weight `ϖ`, `ω^res`; available (product) weight `ω`; weight reserve; weight-reduction factors | 12:247, 281, 282; 13sb:72–75; 13ba:44, 124; 14lc:58, 61; 18lp:73, 84, 105, 128, 138, 168, 188 (≈25) | no | Positive numbers `w_i`, `ω` by which source variables are scaled in the marked norm, so that the coefficient of `z_S` is bounded by `1/∏w_i` (12:243–244; 11:812). "Marker amplitude $e^{2q}$" (14lc:61) appears to be the same weight (I). | R; marker = weight I | *weight of the source variable `z_i` in the norm*; one word | c |
| normalized local insertion | 13sb:53, 13ba:119, 174, 18lp:243 | R (notation.md "primary source") | The source multiplied by `ω_k = a_k^d β̂_k^{-w_d} E_k^{-1}` (13sb:58, 65). | R | keep, but define | d |
| column; coefficient column; column coefficient `x_l`; column map; inverse-column bound; prescribed column bounds `C_l`; trial / label / output / compensating / terminal / free column | 13:164; 13sb:15, 49, 75, 92; 13ba:13, 14, 109, 276, 278; 18gq:25, 92; 18lp:26, 40, 46, 48, 56, 64, 213, 305 (≈20) | no | The coefficient vector of the polynomial (local) part of a marked density, and the linear map on it: "A local degree-$t$ marked density consists of a column coefficient $x_l$ and a remainder" (18lp:26); "Invertibility of the column map" (18lp:47–48); 11:446 "column constant $s_f$. Thus $M_G$ is invertible". "Trial columns" = images of basis vectors (13ba:276). | R / I | *coefficient vector*; *coefficient map*; *bound on the inverse coefficient map* | b |
| inverse terminal coordinates; subpower inverse terminal coordinates | 13:159, 217 | defined in 11:1100–1101 | `‖X_i^{-1}z_i‖_1` (coordinates at the cutoff scale) bounded by a sequence subpower in `a_N^{-1}`. Not explained in ch. 13. | R (ch. 11) | *coefficients at the cutoff scale* | b |
| admissible coefficient family / admissible coefficients | 13:215, 219, 239 | D in 11:1100 | "Call a coefficient family $z_i$ admissible here if $\|X_i^{-1}z_i\|_1$ is bounded by a sequence subpower in $a_N^{-1}$" | D (ch. 11) | *family of subpolynomial growth at the cutoff scale* | c |
| trial; local trial; coarse trial `V_h`; protected trial construction; inclusion trial; trial descent; trial encoding; trial residual; trial columns | 13:229, 232, 239, 394; 13ba:12, 15, 24, 30, 48, 157, 213, 276; 18gq:105; 18lp:34 (14) | `V_h` D by formula 13ba:213–217; otherwise no | A candidate local observable at some level whose image under the block maps is compared with a normalized local insertion (11:891–896 "Subtract one normalized local insertion density from the terminal trial"). "Protected" (13:229) = with small-field cutoff (I, as dictionary 2.4). "Trial encoding" (13:394) ?. | I; "encoding" ? | *candidate observable*; *comparison of a candidate observable under the block maps* | d |
| equation space; (finite) equation kernel; equation comparison; equation inclusion; equation remainder | 13:14, 15–16, 157, 220, 394; 18gq:10, 110 | defined in ch. 11 (11:1094) | `K_i = X_i P S_t R_e I_e`: the image at cutoff `(N,p)` of the ideal of labels vanishing on Maxwell solutions; `ker Π_{d,N,p}` (13:136–137). "Equation remainder" (18gq:110) ?. | R (13:136; ch. 11) | *space of equation-of-motion labels*; *comparison of the two realisations of the equations of motion* | d |
| section; degree-`d` section; finite-section constants; section constant `C^sec`; global section | 13:234; 13sb:15, 60; 13ba:67, 75, 223 | no (notation.md: "finite-stencil section") | The map from polynomial labels to lattice observables: "its section is a fixed polynomial in compact group variables" (13ba:223). | I | *lattice representative of the label* | c |
| attachment; source / terminal / local / joint / complementary attachment (bound, estimate) | 13sb:63, 69, 73; 13ba:58, 62, 77, 78, 99, 123, 145; 18lp:148 (11) | no | Not determined here. A smallness condition `u_i` under which a source term may be inserted ("fits every local attachment … bound", 13ba:58; "$u_i=\tfrac14\widehat\beta_i^{-1/2}$", 13ba:77). | ? | resolve from ch. 11 (11:169, 215, 937) | b |
| incidence norm / sum / bound | 13ba:69, 96, 171; 18lp:85, 86 (5) | no (11:258) | Sum over all terms containing a given insertion point ("insertion incidence sum at a fixed mark", 11:258). | R (ch. 11) | *sum over terms containing a given insertion* | d |
| rooted (activity norm, majorant sums, component estimates) | 12:178, 236; 18lp:214 | no | Sum over supports containing a fixed site ("Summing a rooted activity norm over the finitely many sites", 12:178). Same idea as dictionary "containing-site bound". | I | *norm with one site fixed* | d |
| reserve (width, support, weight, exponent); "reserve four units"; room | 12:62, 126, 278, 282; 13ba:78, 144, 148, 153; 18lp:177; room 13ba:194 | no | Slack in an exponent kept to absorb later losses: "common bound at width $w>v$ … A strict width reserve" (12:48, 62). | R | *strict margin `w − v > 0`*; *we keep four units of the exponent* | a |
| request; finite (comparison, degree, threshold, admissible) request; lower-level request | 13:96; 13ba:100, 336; 18lp:103, 151; 14:224, 225, 227; 14lc:9, 79, 108; 15:207 (12) | no | A finite list of requirements (arity, degrees, window, error) for which constants or thresholds are then chosen: "All constants … are chosen for this one finite request" (14lc:9). | R | *finite set of data `(n, D, K, ε)`*; *condition* | b |
| block floor(s) | 18gq:25; 18lp:41 | no | Lower bound imposed on the block ratio `L_l` ("above every stage floor", 10:55). | I | *lower bound on `L_l`* | d |
| first-below scale / choices; first-crossing levels; "first permitted such scale" | 13sb:145, 155; 18lp:21; 13:358 | R at 13sb:146–147 | "let $m(r)$ be the first level with $a_m<cr$". | R | *the first level with `a_m < cr`* | d |
| comparison depth; comparison level | 13:163–165; 14lc:23; 15:253 | no | The level `k` at which the Gaussian (free) comparison is made, `H_k=\exp((\log\log\widehatβ_k)^2)` (14lc:23–24). "Admissible comparison depth" undefined. | I | *comparison level `k`* (one word) | d |
| lift (coefficient lift `u_{k,N,p}`) | 14:172, 192, 210; 14lc:32, 41, 100; 15:256 | D by formula 14lc:32–34 | Solution of `S_{g/θ}T u = W_{H_k^{α_0}} v` for a free representative `v`. (A fourth sense beyond dictionary 4.2.) | D | *preimage under the extraction map* | c |
| ancestor cone; cones; disjoint-cone identity; marked ancestors | 13ba:131, 181, 194, 232, 234, 241, 251, 270 | D at 13ba:232–233 | "The full ancestor cone of a stencil contains its fine-link reads and all these random variables at every intermediate level". | D | *domain of dependence* | d |
| (shared) frame seed; primitive random variables | 13ba:231, 247, 270 | R | The independent auxiliary random variables used for gauge choices ("independent primitive random variables for those choices"). | R | *auxiliary random variables* | b |
| group; grouping; merger; live group; representative (of a group); joining bound `h_l`; occupancy factors | 18lp:67–136 (group 12×, merger 4×) | D at 18lp:71–72 | "A group is a set of these marks with a common representative." "Live" (18lp:110) undefined (I: not yet merged). | D; live I | keep, define once | d |
| recentering | 18lp:42 | R | Subtracting the output column to restore a vanishing extracted coefficient. | R | *renormalisation of the remainder* (unsure) / keep, define | d |
| remainder with vanishing extracted coefficient | 18lp:27, 36, 40, 114, 115 | no | A term whose local polynomial part (Taylor polynomial through degree `t`) is zero; cf. 11:379 "vanishing-jet". | I | *term with vanishing Taylor polynomial of degree t* | e (translation residue) |
| low plane; low / high coordinates; low part | 18gq:53–54, 70–84, 94, 119 | R | `PV_t`, with `P` the projection onto scaling dimensions below `i` (18gq:51, 76). | R | *subspace of dimension < i* | d |
| cell census `𝓘`; replica census; replica cells | 13ba:53, 173; 18lp:91; 15:261 | R (13ba:173) | The index set of reflected cells / the number of copies. | R / I | *set of cells*; *number of copies* | b |
| inspected (plaquette, stencil) | 12:186; 13ba:219, 250 | no | On which the function or its conditions depend. | I | *on which … depends* | b |
| "Open the centered cells at `m`" | 13ba:127 | no | Verb not determined (choose? place?). | ? | resolve | e |
| coordinate hybrids | 14lc:95 | no | Not determined (points mixing coordinates of two configurations in the rounding step?). | ? | resolve | d |
| the source construction | 14:186 | no | "For example the source construction uses $r_k=a_kM_k^{α_0}$…". Either the formal source of the monograph or "the construction with sources"; note the parameters there are `M_k` while 14lc uses `H_k`. | ? | delete or cite a section | b |

##### 1.2 Continuum fields, reflection spaces, phases, reconstruction (ch. 13 main, 14, 15, 16)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| ordered limit(s); ordered tails; cutoff tail; (coefficient, volume) refinement | ordered: 13 7×, 13ba 3×, 15 3×, 18gq, 18lp, 14lc; tail 23× | "ordered tails" D at 13:213–214; ordered limit R at 13:45–50 | `lim_k lim_N`; tails "$p=P(k)$ with $k\ge k_0$, and $N=n(j)$ with $j\ge j_0(k)$". "Cutoff tail" = all sufficiently large `N` (12:190). "Refinement" = subsequence. | D / R | *iterated limit*; *for all sufficiently large N*; *subsequence* | d |
| separated (correlation, test function, configuration, response, bound, smearing) | 67× | no | At pairwise distinct points / supported away from coincident points (14:17–18). | R | acceptable; define once | c |
| slot; one-slot response | 13:120, 132; 14:172, 220; 14lc:46; 15:115; 16:239 | R | Argument position of a correlation. | R | *argument*, *entry* | c |
| arity | 17× (13:39, 93, 330; 14:170; 16:120 …) | no | Number of insertions. | R | *number of points*, *n-point* | b/c |
| cell; centered (cell, scale, seminorm, chessboard estimate, tiling); interior; margin; strip count; residue patterns | cell 57×; centered in this sense ≈17; 13:81–90, 367–368 | R at 13:68–90 | Tile of a reflected tiling; "centered" bounds hold when the insertion lies in a cell with margin `3a_k` (13:87–88) — never defined as a term. | R; centered I | *tile*; *seminorm for an insertion at distance ≥ 3a_k from the cell boundary* | c |
| buffer; slab margins | 13:335, 348; 14:111, 151; 14:99 | D at 13:335 | "We call $r$ its buffer in the slab of width $h$" (pairwise separation ≥ r, times in `[r,h−r]`). 14:99 calls the same thing "slab margins". | D | *margin r* (one word) | d |
| exterior word | 13:336, 349; 18lp:8, 286, 294, 308; 14:106, 354; 15:244; 16:46 | no | The word of remaining insertions on which `A_w`/`B_h(w)` acts or against which a cluster is paired; synonym of "spectator word" (14:722, 898; 14lc:43). | I | *spectator word* (one term) | d |
| slab; slab word; slab insertion; slab operator `B_h(w)`; reflected slab word `w^♯` | 14:83–141; 15; 16:35–37 (24×) | D at 14:86–88, 97–104 | "A word $w$ lies in a slab of width $h$ if $0<x_i^\mu<h$". | D | keep | d |
| heat (semigroup, operator, energy, orbit, analyticity, damping, limit, pairing, intertwiner) | 14:80, 414, 435, 855, 858; 15 6×; 16 7× | R at 14:55–56, 15:26 | `E(t)=e^{-tH}`, the reflection-positivity semigroup of translations in the reflected direction. "Heat energy" (14:414) = spectral variable of `H`. | R | *(Osterwalder–Schrader) transfer semigroup*; *energy* | c |
| damping; undamped measure; damped moment | 14:416, 430, 435, 436, 489, 513, 752, 765 | "undamped measure" D at 14:416–419 | The factor `e^{-2uE}` produced by translating the insertion to time `u>0`; the undamped measure removes it. | D / R | *weight `e^{-2uE}`*; *spectral measure with the factor `e^{2uE}` restored* | d |
| coordinate half-space spectrum; coordinate spectral measures; word measures; mixed measures | 14:76, 410, 422, 424 | R | Joint spectral measure `P_μ` of `H_μ` and transverse momenta; "mixed" here = polarised (off-diagonal). | R | *joint spectral measure*; *polarised measures* | d |
| (frequency) profile; transverse / temporal / annular / residual / dyadic / line profile | 14: 21× (448–764) | no | A function of one momentum variable used as a factor of a product test function in Fourier space. | R | *one-variable multiplier* / *factor* | c |
| annular correction `C_{m,ρ}`; residual (profile, response); sign transfer; mixed-sign estimate; spectral sign | 14:458, 465, 520, 526 (label), 531, 725, 748, 750; 447 | D by formula 14:458–471 | Subtraction of the first `2m` moments by Lagrange interpolation; `R_{m,ρ}f` its Laplace transform. "Spectral sign `ε_i`" (14:447) R. | D | keep the symbols; drop the names or define | d |
| conserved stress line; physical line; centered conserved line; orientation of the line | 14:258, 293–294, 308, 1019 | R | The one-dimensional kernel of the divergence on `𝒦` (14:294). | R | *the line `ker(div|_𝒦)`* | d |
| line axis; line time axis; transverse-to-line axes | 14:497, 723, 731, 753–755 | no | The coordinate axis `e_l` carrying the spectators (14:711–712). | I | *the axis `e_l`* | d |
| shell factor; total (raw angular, shell) response; angular boundary / flux at infinity | 14:358, 410, 708, 777, 796 | no | `ρ^{3+ϰ}` (14:340, 358); the flux integral `−∫∂_μV_c S(J_{μc},A)` (14:777). | R | *the flux integral* | d |
| Ward kernel; Ward normalization; spin operators | 14:821, 309, 903 | no | Common kernel of the vector correlation functionals in the mixed vector-map space (I); the constant `c_*` (I, 14:825–837); the generators `L(K)` (I). | I | state the object | c/d |
| phase | ≈50 (15: 21, 16: 19, …) | D at 15:8–9 | "A phase will be a character of a commutative operator algebra, not a set of gauge configurations"; `S^ξ(w)=ξ(M(w))`. notation.md warns against reading it as an extremal state. | D | keep (defined); see §3 for "phase space" | c |
| compression `M(w)`; compression algebra `𝔄`; ground algebra; compressed (whole words, operators, errors, product moments) | 15:10, 50–59, 91–93, 123, 155–156, 213, 267; 15sp:15 | D at 15:56, 93 | `M(w)=P_0B_h(w)|_{H_0}`. "Ground algebra" (15:155) is the same algebra. | D | keep; one name for `𝔄` | d (compression is standard operator theory) |
| whole word; whole-word identity | 15:10, 129; 15sp:10 | no | `M` of the entire concatenated word, as opposed to a product of `M`'s of its parts (15:123–130). | R | *of the concatenated word* | d |
| cluster (of insertions); cluster limit; separated-cluster limit; cluster-separating ray | 18lp 11×; 14:352; 15 8×; 15sp:14 | no | A finite set of nearby insertions (18lp:222 "Let a cluster contain $n$ fields"); in `15` a word translated as a block. "Cluster limit" = (15:79–84). Not the dictionary's sense (subsequential limit), which survives at 13:206, 211 as "cluster point". | R | acceptable (cf. cluster property); define | c |
| generic (grid word, grid points, configuration); cofinal grids | 13ba:306, 311; 18lp:300, 342; 14:391; 14lc:75; 15:178, 207–208 | D at 15:178 | "generic real grid word $w$ (distinct projections in each coordinate)". | D | *with pairwise distinct coordinates in every direction* | c |
| coordinate ties; coordinate-equality strips | 14:179, 196, 206, 369 | R | Distinct points sharing a coordinate ("coordinate ties which are not collisions"). | R | *coincident coordinates* | d |
| height; gap; tied (heights, pair, gap); weakly / strictly ordered heights | height 19×, tied 7× in `16` | R at 16:48, 75, 85–89 | Height = imaginary part `y_j` of the complex time; gap = `y_{j+1}−y_j`; tied = equal. | R | *imaginary parts*; *differences*; *equal* | d |
| padding identity | 16:45, 64 | R at 16:40–41 | `B_{ε+u}=E(u)B_εE(u)`. | R | *the identity (…)* | d |
| letter; field word | 16:291–293, 322 | D at 16:291 | "A letter is a pair $(A,f)$ with $A\in F$ and $f\in\mathscr S(\RR^4)$". | D | keep (Borchers-algebra language is the standard alternative) | c |
| barycenter identity | 16:118 | no | Presumably `S=∫S^ξ dν` and its analytic continuation (16:88 "ν-average"). | I | *the integral representation (15:mixture)* | c |
| partial boundary | 16:225, 280, 554 | R at 16:226–231 | Boundary value in some imaginary directions only (`W_{n,Y}`, `Y∈C_n`). | R | acceptable | d |
| local charge `Q_K(f,c)`; (local) charge fields `p_b`, `Y_d(K)` | 14:312, 408; 16:464, 521–523, 535 | D (16:523; 14:376–379) | Two objects: linear maps on `F_d` (ch. 14) and smeared operators (ch. 16). | D | *generators `p_b`, `Y_d(K)`*; *smeared charge* | c |
| moment (= correlation) | 12:293 "actual cutoff moment"; 14lc:47 "free moment"; 15:213 "compressed product moments"; 14:898 | no | Correlation function `M_{N,p}(v;x)` (the symbol `M_{N,p}` is used at 12:262 without definition in this chapter). | I | *correlation* | c |

---

#### 2. Dictionary terms: same sense / new sense / clarified

##### 2.1 Same sense

| Term | Where here | Note |
|---|---|---|
| atom (of degree q) | 12:60 | same (elementary path term of degree q) |
| width (decay rate of path coefficients) | 12:48, 62, 126 | same as 4.2. New senses in §3. |
| walk | 12:54; 14:546 | path; 14:546 is a walk through an index set |
| scalar; scalar normalization | 12:34, 166, 170; 13sb:26, 29; 13ba:164, 219 | same (constant term of the exponent); "scalar part" of a polynomial = coefficient of the identity (13ba:164) |
| regular / large-field activities; activity arrays; array | 12:33, 70–77; 13ba:151–152 | same |
| exact cover | 12:180, 188 | same |
| (relaxed) small-field condition | 13ba:220 | same, already translated |
| smoothing order `j_i`; connector; frame (gauge frame); macro-box radius | 13ba:229–248 | same; 13ba:244–248 restates "each endpoint frame reads a box of fine-lattice radius $(j_i+3)L_i$" |
| reads / fine-link reads | 13ba:232, 244 | same ("depends on"); note the noun "reads" |
| stencil | 12:345, 362, 389, 390; 13:236; 13sb:138; 13ba:216–250, 297; 18gq:102 | same as "footprint/stencil"; in `12` it is a finite-difference stencil (standard) |
| incoming / outgoing | 13sb:10, 72; 13ba 6×; 18lp 4×; 14lc:60 | same |
| supplies / supply | 20× (12:14, 40, 42, 353, 354 …) | same ("gives"). Lemma name "coarse-residual-supplier" survives in a label (13ba:49). |
| inputs | 15:12, 32, 338; 16:27, 332; 13:391 | same ("hypotheses") |
| spectator | 49× (13:97, 119; 14:316, 335; 16:543) | same (remaining insertions). Never defined in these chapters. |
| collision | 12:402; 14:18, 206, 369; 15:245; 16:27 | same |
| flux; shell | 14:318–328, 373; 16:538, 558 | same; `𝒬^J_v` defined at 14:318 |
| internal defect | 14:932–933 | same (the passage the dictionary cites) |
| cluster point | 13:206, 211 | same as "cluster limit" (subsequential) |
| subpower | 13:159, 217; 13ba:18; 18gq:103; 18lp:18, 257 | same; see 2.3 |
| cost; loss; excess; margin | see §3 | same family as dictionary 2.6 |
| coupling threshold | 13:237; 13sb:16, 41, 45; 13ba:39, 50, 83, 101, 258, 261; 18lp:101, 148; 14lc:69 | same as 4.2 ("for β̂ sufficiently large"); ch. 10 says "inverse coupling threshold" |
| eligibility (criteria, indicators, event, conditions) | 12:25, 181; 13sb:72; 13ba:249 | sense (ii)-like: conditions attached to activities (9:94 "large-field indicators in their eligibility criteria"). I. |
| protected | 13:229 | presumably same (with cutoff); I |
| detection / detecting | 13sb:9 "rank detection"; 14:221 "detecting families" | same (nondegeneracy). Elsewhere replaced by "separating family" (13:14, 395; 14:386, 832; 15:17, 250, 256); "detector" survives only in labels. |
| probe | 18gq:131; 18lp:269, 293, 321, 332; 14:354 | related but different object: see 2.2 |
| physical (continuum units) | ≈17 (12:5, 22, 230, 352 …) | same as 4.2 "physical spacing/period"; new senses in §3 |

##### 2.2 New senses of dictionary words

| Word | New sense here | Where | Basis |
|---|---|---|---|
| response | "one-slot response" `L_{v,f}(c)=∫ f S_{n+1}(c(x_0),v(x))`: a smeared correlation as a linear functional of one label | D at 13:120–122; 13 10×, 18gq 3×, 14:406, 992 | D |
| response | Laplace-transformed pairing of a profile with a spectral measure: `𝓛f(E)`, `𝓡_{m,ρ}f(E)`, `Resp_i(g)` | 14:465, 503 (D by formula), 531, 654, 672, 688, 697, 740, 761 | D / R |
| response | the flux integral ("total raw angular response", "total shell response") | 14:777, 796 | R |
| transport | (i) transfer of a marked density or coefficient down the levels by the block maps (12:277; 18gq:13, 76, 84; 18lp:24, 47, 197, 216); (ii) conjugation by the comparison maps `U_{k,d}` (14:229, 281, 282, 302, 946); (iii) "carries over" (14:819) | R / R / R |
| anchor | position of an insertion to be placed in a cell | 13:83, 86, 89; 13sb:85, 157, 159 | R |
| probe | finite linear combination of separated correlations used as a coordinate functional on `F_D` ("dual coordinates realized by finite linear combinations of separated probe correlations") | 18lp:268–269 | R |
| label | element of the quotient `F_d` or of `F` (a field), not a polynomial in `V_d` | 14:26, 98, 147 …; 15; 16 (see §3) | R (14:147) |
| word | Euclidean word (13:282) and field word (16:291); see §3 | | D |
| row | bounded coefficient family; member of a separating family; see §3 | 13:159; 15:275, 278 | I |
| window | compact set `K` of separated configurations | 14:173, 197, 226, 237; 14lc:6, 97 | R (14lc:6) |
| lift | coefficient lift; see §1.1 | 14lc:32 | D |
| representative | representative point of a group of marks | 18lp:72, 79, 93–95 | D-ish |
| charge | smeared operator `Q_K(f,c)` | 16:523 | D |
| centered | placed inside a cell with margin; zero expectation (D at 14:263); see §3 | | |
| cutoff | "outer cutoff" = `N` (13ba:53, 221); "level-`m` cutoff" = small-field threshold (12:187); "cutoff threshold" = the `N_0` beyond which a bound holds (12:265; 13:27, 388) | R |
| terminal | "terminal graph" (12:131) is at the intermediate level `m+h`, not at `N` | 12:131, 139 | R |

##### 2.3 Dictionary open items clarified by these chapters

| Dictionary item | What these chapters add |
|---|---|
| regularity-stage index `J_m` (§4) | Resolved outside my files, used inside them. 10:25: "A stage $j\ge1$ specifies finitely many derivative orders, support exponents, path widths and coefficient bounds"; 10:133 `J(m)=j` for `A_j≤m<A_{j+1}`; 10:808 "$J(m)$ is the stage at scale $m$". Used as `C_{J(i)}`, `J(k)` at 13sb:28, 57; "When $J(i+1)=q>1$" 13ba:262; "stage" 22× in my files. Basis D (ch. 10). Proposed: *regularity class j* / *parameter set j*. |
| subpower (2.6) | Defined locally at 18lp:18: "A factor $e^{o(T)}$ is called subpower in this paragraph"; with 18lp:15–17 `f ≼ e^{cT}`. 13:159, 217 use "subpower in `a_N^{-1}`" (11:1101). D. |
| history; schedule (2.1) | Here "history" is not the list `(L_h, j_h)` but the sequence of renormalisation steps started at a given cutoff: "the history restricted from the actual cutoff $N$" (13ba:31–32); "selected histories" (plural, one per cutoff) 13ba:50, 200, 304; "on the same history" 18lp:48; "actual histories" 18lp:229. Basis I. "Schedule" = the fixed choice of block ratios and coupling thresholds (13sb:16–23, 50–51; 13ba:101, 256–262; 18lp:20) — R, consistent with the dictionary. |
| moving comparison fields (§4) | Partial. "Moving" here means depending on the sequence index: "convergent moving labels … handled by expansion in fixed finite bases" (14:238, 250); "moving test functions" (13:295, lattice-dependent). Supports the reading "cutoff-dependent" but does not define the ch. 3 phrase. I. |
| seeded sector / unseeded law (§4) | Not clarified. 13ba:247, 270 "shared frame seed(s)" are the auxiliary random variables for gauge choices; whether this is the same "seed" is not determined. |
| marked (4.2) | Confirmed and sharpened: 12:200–206 gives the structure of "the exact marked density" (polynomial in nilpotent `z_i`). See §3 for `mark`. |
| event label / indicator (4.2) | 12:25, 163–164 "fixed Borel event indicator … no continuity of the event indicator as a function of $U$ is required" — consistent with dictionary 1.4 (indicator, not smooth). |
| centered log determinant, compulsory, Warnings, output anchors, likelihood tests | No occurrence, no information. |

---

#### 3. Multi-sense words (all occurrences classified)

**row** (7). (a) quadratic path term of the action, indexed by a displacement: 12:55 ("For a row their length is $|x|_1+4$", contrasted with "an atom of degree $q$") — dictionary kernel/component sense, I; 1. (b) literal matrix row, each row being a correlation functional: 13:168, 182; 14:277; 3. (c) bounded coefficient family: 13:159 ("bounded rows have uniformly subpower inverse terminal coordinates"; cf. 11:1103 "every bounded coefficient family") — I; 1. (d) member of a finite separating family: 15:275 ("row constant", "free row moments"), 15:278 ("finite reference rows use fixed free labels") — I; 3 (two on 15:275). None unclassified.

**actual** (20). (a) "of this construction", emphatic, as opposed to a generic or model object: 12:63, 75, 118, 119, 169, 252; 13:162; 18lp:12; 14:15, 168, 332, 971; 14lc:29, 53 — 14. (b) the sequence produced by the construction as opposed to a substituted one: 12:143 ("actual graphs" vs the fixed admissible graph), 12:293 ("actual cutoff moment" vs the stopped expression) — 2. (c) belonging to cutoff `N`: 13ba:32, 18lp:229 — 2. (d) the true function as opposed to the model solution `Q`: 14:868, 869 — 2. The dictionary senses "nonlinear/at the true background" and "running coupling" do not occur. Almost all of (a) can be deleted.

**selected / select / selection** (22). (a) fixed by the construction of ch. 10 (trajectory, schedule, ratio, history): 12:123, 133, 298, 370; 13:307; 13sb:50; 13ba:17, 50, 195, 200, 304 — 11. (b) the continuum family obtained along the chosen subsequence: 13:172, 395; 15:257 — 3. (c) literal choice of a subsequence: 13:6, 7, 143 — 3. (d) the graph produced by the trajectory: 12:134, 139 — 2. (e) other fixed choices: 13sb:136 (stopping level), 13ba:30 ("selected level-$h$ polynomial coordinates", I), 18lp:328 ("selected coefficients of $A_t$", obtained by a refinement) — 3. Also "Selecting a phase" 15:301 (literal choice of `ξ_*`). `chosen` is used as a synonym of (a)/(b) at 14lc:101, 109.

**test** (≈47). (a) test function: 13:43, 44, 109, 119, 193, 242, 291, 295; 14:17, 197, 224, 507, 510, 612, 614, 766; 16:92, 94, 154, 162, 171, 177, 282, 295, 311, 358, 362, 385, 459 — 29. (b) "test against" = pair with all spectators / exterior words / word vectors: 13:272; 18lp:307, 310, 320; 14:207; 15:243, 248; 16:46 — 8. (c) participle "tested" = smeared with a test function or paired with fixed spectators: 18lp:218 ("one tested mean"), 330; 14:242, 1016; 16:87, 117, 150, 151, 215, 300 — 10. The ch. 4–6 senses (condition, variable, location, indicator) do not occur; all uses comply with notation.md except that (b)/(c) should name the pairing.

**label** (≈60); **tag** 0. (a) polynomial label in `V_d` (dictionary sense): 12:22, 147; 13 (16×); 13sb:176; 13ba:312; 18gq:13, 48, 85, 96, 106; 18lp:17, 228, 295, 303; 14lc:7 — ≈30. (b) element of the quotient `F_d`/`F`, i.e. a field: 14:26, 98, 101, 147, 658, 842, 864, 879, 980, 991, 1025; 15:109, 119, 178, 316; 16:19, 20, 36, 83, 132, 153, 260, 369, 373, 515, 520 — ≈26. (c) sequence-dependent label: "moving labels" 14:238, 250; "free labels" 15:278 (free field space) — 3. (d) "the field labeling is faithful" 16:345: the map `A ↦ Φ_ξ(A,·)` — 1. notation.md requires (a) and (b) to be distinguished; from ch. 14 on they are not.

**mark / marked / marker** (53). (a) "marked" = carrying source insertions (density, step, estimate, norm, transfer, remainder, construction): 12 15×; 13sb:10, 26; 13ba:11, 44; 18gq:7, 24, 55, 70; 18lp:26, 42, 79, 90, 126, 210, 245; 14:16, 168, 191, 971 — ≈35. (b) "mark" = one insertion point: 18lp:67, 71, 72, 80, 86, 127, 183, 215; 13ba:131 ("marked ancestors"); 15:252; "two-mark" 14:332, 15:260 — 12. (c) "mark weights" 13sb:72; "marker-weight", "marker amplitude" 14lc:58, 61 = source weights — 3. (d) symbol `δ^mark` 18lp:142, 192 — 2. Also "unmarked" 18lp:89, 186.

**window** (6). One sense, compact set of separated configurations: 14:173, 197, 226, 237; 14lc:6; "physical windows" 14lc:97 (unrescaled, I). The ch. 6 sense does not occur.

**history** (7): see 2.3; all 7 in the sense "renormalisation sequence at a given cutoff" (13ba:31, 50, 195, 200, 304; 18lp:48, 229).

**source** (≈60). (a) nilpotent source variable / "in the sources": 12 (15×), 13sb:11, 66, 67; 13ba (≈10); 18lp:9, 69, 210; 14lc:53, 57 — ≈38. (b) the inserted observable itself as a density ("complete source", "terminal source", "pushed negative source", "physical source (density)", "incoming source term"): 13sb:65, 72; 13ba:123, 158, 284; 18lp:29, 180 — 7. (c) source weight: 12:247, 281; 13ba:44; 18lp:73 — 4 (+ §1.1). (d) "source attachment", "source constants", "corrected-source estimate": 13sb:15, 63, 73; 18lp:148; 14lc:45, 69 — 6, meaning not determined beyond "pertaining to insertions". (e) "the source construction" 14:186 — unclassified (formal source? see §4).

**price / pay**: 0. **cost** (25). (a) multiplicative factor lost: 18lp:41, 64, 110, 113, 119, 178, 210, 212; 14:500, 589; 14lc:82; 13:237 — 12. (b) additive loss in an exponent or logarithm: 13sb:37; 14:757; 15sp:23; 18lp:107 — 4. (c) an error term: 14:199; 18lp:85, 343 — 3. (d) a named bound: "per-site normalization cost `q^site`" 13sb:25, 112, 18lp:163; "normalized cost at most `ζ_h`" 13ba:120; "cost `q_fin`" 18lp:56; "Signed regular costs" 13sb:35 (cf. 11:808 "absolute action cost per site") — 6. **reserve** 9, **loss/lose** 7, **excess** 5 (all = the `ε` above the sum of degrees: 13sb:7, 164; 18lp:334; 15sp:6, 24 — a different use from dictionary `Δ_p`), **margin** 14 (geometric distance to a cell boundary 12×; strict inequality margin 18lp:257, 16:201).

**detector**: 0 in prose (labels only); **detection/detecting** 2 (13sb:9; 14:221).

**probe** (6): one sense (§2.2): 18gq:131; 18lp:269, 293, 321, 332; 14:354.

**response** (25): one-slot response 15 (13:9, 10, 120, 151, 152, 161, 177, 183, 210, 265; 18gq:111, 113, 130; 14:406, 992); spectral/Laplace response 8 (14:465, 531, 654, 672, 688, 697, 740, 761); flux integral 2 (14:777, 796). None in the dictionary's four senses.

**transport** (14): RG transfer 8; comparison-map conjugation 5; "carry over" 1 (lines in §2.2). No parallel transport.

**frame** (4): gauge frame, 13ba:230, 241, 244, 247.

**anchor** (6): insertion position (§2.2).

**readout, table**: 0.

**phase** (≈53). (a) a character `ξ` / the correlation family `S^ξ` (D 15:8): nearly all. (b) "the compact phase space `Ξ`" 16:15: the character space — collides with the standard meaning of "phase space". (c) attributive "phase X" = X built from `S^ξ` (phase reflection space, phase slab operators, phase pair, phase matrices, phase measure `ν`, phase continuity = continuity in `ξ`, 16:112). No other sense.

**word** (≈96). (a) Euclidean word, "a finite list of labels and positions" (D 13:282; "positive word" D 14:23): all of 13, 13ba, 18lp, 14, 14lc, 15, 15sp (71) and 16:46, 365, 555. (b) field word, product of letters `(A,f)` (D 16:291–293): 16:10, 288–323, 348–351, 385, 458, 468, 484–485 (≈20); at 16:485 "For a word $A$" the letter `A` denotes a word, elsewhere a field. (c) "formal word sums" 14:39, 94 = formal linear combinations of (a). The dictionary senses (holonomy; Neumann term) do not occur.

Further multi-sense words found:

- **centered** (23): (i) insertion well inside a cell — "centered scale/cell/seminorm/tiling/chessboard estimate" 13:87, 98, 301, 314, 346, 361, 372, 382, 395; 13sb:102, 121, 159; 13ba:28, 127, 201, 312 (16); (ii) zero expectation, D 14:263: 14:261, 263, 302, 1004, 1019 (5); (iii) centered difference: 12:389; 14:432 (2); (iv) "centered level-(m+1) block" 18lp:224 (1, I).
- **physical** (37): (i) in continuum units (≈17); (ii) carrying the factor `a^{-d}`: 13ba:7, 71, 122; 18gq:99; 18lp:29, 180, 200 (7); (iii) of the interacting continuum theory as opposed to free or microscopic: 18gq:2, 8, 94, 112; 14:212, 291, 308 (7); (iv) "physical Hilbert space" 14:1026 (1).
- **mixed** (23): (i) of the undecomposed mixture `S` ("mixed correlation hierarchy" 14:12, used before 15:5 explains "mixture"): 18lp:8, 263, 282, 350; 14:12, 165, 263, 349, 820, 946; 15:24, 155, 248, 277, 329; 15sp:5, 8; 16:88 (18); (ii) polarised/off-diagonal: 14:424; 16:360 (2); (iii) of both signs: 14:658, 725, 750 (3).
- **column** (22): coefficient vector/map (≈20, §1.1); column of a figure 13:51; column of the exponent table 14:795.
- **cone** (17): ancestor cone 13ba (7); cone condition in a recursion "The cone $32(1+C_l)^2U\le r_l$" 18lp:48, 61 (2); spectral/forward cone 14:76, 804; 16 (8).
- **admissible** (15): graph (D 12:82) 6; coefficient family (D 11:1100) 13:215, 219, 239; undefined: remainder graph 12:37, majorant 12:80, period cell 12:375, trial encoding 13:394, path-action representation 13sb:27 (dictionary 2.3), bounds 13sb:36, request 18lp:103, comparison depth 14lc:23.
- **threshold** (≈30): coupling threshold (≈14); small-field threshold 13sb:62, 13ba:75, 18lp:179; cutoff/convergence threshold (an `N_0`) 12:265, 395; 13:27, 388; 13sb:139; "approximation / translation thresholds" 13ba:307; 15:262.
- **width**: path-coefficient decay rate (12:48, 62, 126); slab width `h` (14:86 ff., 15:53); width of a frequency profile and "width exponents" (14:550–665).
- **degree**: filtration degree `d` of `V_d`/`F_d`; "source degree" 12:270; "radial degree" 18lp:173; "degree of the Killing field" 14:347; 18gq:19 warns "scaling dimension …, not its factor count".
- **stage**: regularity stage `j` (22); idiom "at this stage" 14:65, 15:324.
- **extraction**: coefficient / Taylor / polynomial extraction (12:240; 18lp:138–186; 14lc:30, 57) vs subsequence extraction (12:400; 13:15, 31, 42).
- **mass**: measure-theoretic (12:190; 14:422, 760, 764; 15:326; 16:387, 440); "mass gap" 16:383; norm bound of incoming terms ("incoming mass $\mathfrak m$", "total mass $p_l$", "normalized mass $f_l$") 18lp:115–116.
- **profile**: large-field profile (ch. 12) vs frequency profile (ch. 14) vs "complementary profile" (13ba:165).
- **residual**: trial residual / residual coefficient (13ba, 18lp) vs residual profile after moment subtraction (14:520–748) vs replacement error (18lp:307–336; 14:355).
- **comparison** (47): equation comparison, Gaussian/covariance comparison, local-trial comparison, adjacent comparison, interior-cell comparison, comparison maps `U_{k,d}`, smooth comparison, comparison cells/level/depth/labels/matrix/sequence — at least six distinct objects.

---

#### 4. Terms the chapters do not determine

| Term | Where | What can be said |
|---|---|---|
| attachment (source, terminal, local, joint, complementary) | 13sb:63, 69, 73; 13ba:58–145; 18lp:148 | A smallness requirement for inserting a source term; object not stated here. |
| "the source construction" | 14:186 | Formal source or a construction of this book; parameters `M_k` do not match 14lc (`H_k`). |
| sparse (stopping) | 18lp:159 | Refers to the argument of 13sb:104–117; "sparse" unexplained. |
| trial encoding; protected trial construction | 13:394; 13:229 | Defined, if at all, in 11:891 ff. |
| equation remainder; corrected projection; corrected (physical) inclusions | 18gq:8, 110, 114 | Probably the maps `ι_{d,e}` of 13:263–264 and `Π`; "corrected" relative to what is not said. |
| "Open the centered cells" | 13ba:127 | Verb undetermined. |
| coordinate hybrids | 14lc:95 | Undetermined. |
| admissible comparison depth; admissible period cell | 14lc:23; 12:375 | Admissibility conditions not stated in these chapters. |
| selected level-`h` polynomial coordinates | 13ba:30 | Which coordinates are "selected" is not said. |
| site conversion; support conversion cost `T_l` | 13ba:145; 18lp:112–113 | Refers to 11:238 (cover-transfer); not explained here. |
| common (trajectory, construction, lattice) | 12:13, 40, 370 | "Common" to what (all cutoffs? all volumes?) is left to ch. 10. |
| seeded / unseeded; centered log determinant; compulsory; Warnings; output anchors; likelihood tests | — | No occurrence in these files. |

---

#### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| index of a lattice in the sequence | level (≈77), scale ("cell scale", "centered scale", "stopping scale"), stage (misleadingly close), depth ("comparison depth"), "base level", "reference level" | *level m*; keep *stage* only for `J(m)` |
| applying the block maps downward | transport, transfer (12:237, 252, 259), push (13ba:124, 158, 185), descend / descent (13ba:170; 13:239), propagate (12:140) | one verb |
| the fixed construction of ch. 10 | selected trajectory, common trajectory, selected schedule, selected histories, the single schedule | *the parameter sequence of Chapter 10* |
| remaining insertions | spectators, spectator word, exterior word, exterior insertions, exterior probes | *spectators* |
| correlation function | correlation, moment, kernel (13:24 "periodic kernels"), response, hierarchy/family | *correlation function*; *family* |
| distance from a boundary | margin, buffer, slab margin, "room" | *margin* |
| slack in an estimate | reserve, room, margin, excess, loss | print the inequality |
| repeated translates in a chessboard estimate | copies, replica cells, repetitions, reflected copies, "replicate" | *copies* |
| subsequence | refinement, extraction, selection, "cofinal" | *subsequence* |
| all large `N` | cutoff tail, ordered tail, "eventually", "on a full cutoff tail" | *for all sufficiently large N* |
| `ker H` | zero-energy subspace, ground space, `H_0`; ground vector / vacuum; ground projection | *zero-energy subspace*; *vacuum* |
| the algebra `𝔄` | compression algebra, ground algebra | one name |
| pairing with spectators | response, tested correlation, correlation pairing, correlation functional, probe | *correlation functional* |
| family of functionals detecting a field | separating family, detecting family, (detector, in labels), probes, reference rows | *separating family* |
| source-variable scale | source weight, mark weight, marker weight/amplitude, residual weight, available weight | *weight* |
| large-field index data | inventory, prescribed set of large-field sites, "prescribed-site" | *prescribed large-field set* |
| terms with ≥2 sources | higher entries, modes, terms involving at least two insertions, terms of source degree at least two | *terms of source degree ≥ 2* |
| the interacting limit theory | mixed, physical, (plain) continuum | say *of S* |
| chessboard seminorm notation | `‖·‖_𝒯` (13:74), `‖O‖_k` (13:302), `‖·‖_{cell(m)}` (13sb:79), `‖·‖_{𝒞_k}` (13ba:24), `𝓡_m` (11:820), `‖·‖_{cell}` (14lc:64) | one notation |

---

#### 6. Overloaded symbols noticed

| Symbol | Meanings |
|---|---|
| `M` | second cutoff index (12:152); correlation `M_{N,p}` (12:262) and `M^{UV}` (12:357); `M=sup‖T_tc‖` (14:48); energy bound (14:422); `M_k→∞` (14:171); skew matrix (14:933); leading map `M_l` (18gq:15); compression `M(w)` (15:56); supremum bounds `M_i` (13ba:328); mass bound (16:388) |
| `H` | graph (12:86); higher entries `H_X` (12:203); Hamiltonian `H_μ`; `H_k=\exp((\log\logβ̂)^2)` (14lc:24); `H=F−Q` (14:871); normalisation `H_l` (18lp:29); Hilbert spaces |
| `E` | energy; semigroup `E_μ(t)`; error family `E_{N,p}` (13:92); products of constants `E_k` (13sb:57), `E_h` (13ba:16), `E_m` (18lp:171); matrix units `E_{ab}` (14:711) |
| `B` | support radius `B_m`; slab operator `B_h(w)`, `B_ε^ξ(A)`; `B_v` constant (13:352); `𝓑` bounded approximant (13ba:202) and `𝓑_l` (18lp:29); projected spectator word `B` (14:723); matrices `B_{k,i}` (14:946); `B_k=H_k^{-1/32}` (15:254); weak-commutant operator `B` (16:469); ball `B_u` |
| `C` | constants; `C_j`, `C_l` column bounds; `C_{N,p,m}` stopped correlation (12:212); `C_k` isomorphism (14:282); `𝓒_k` tiling (13ba:28); `𝓒_{m,ρ}` correction (14:458); `𝓒_k` Casimir-type operator (14:951); `C_n` cone (16:195); `C_i` free matrices (14:946); `C_D(ρ,z)` replacement field (14:354) |
| `D` | dimension of `ℝ^D` (12:316); `D_m` (12:6); `D=C^n(n/r)^{κn}` (14:113); max degree (14lc:6); `D=d+1−ϰ` (14:334); moment exponent (14:439); Taylor order (14:611); `D_{k,d,a}` (14:233); differential operator (16:94); `D_i` constant (13ba:60); `D_G`; truncation degree (18lp:266); `D_1,D_2` polynomials (14:651) |
| `K` | compact window (14lc:6); skew matrix (14:317); kernel `K_{ab,cd}` (14:610); width bound (14:549); `𝒦`, `𝒦^0` tensor spaces (14:261); `𝒦_λ` profile (14:699); `K_Q` large-field factor (12:205); `𝓚_{N,h}` kernel (13ba:225); `K_l` stage constant (18gq:23); cone `K_n` (16:181); Killing vector (16:518); `K∈O(4)` (15:37) |
| `L` | block ratio `L_i`; functional `L_{v,f}` (13:122); left inverse `L_d` (14:212) vs generator `L_d(K)` (14:837) in the same chapter; Lagrange polynomials `L_j` (14:457); injective map `L` (14:243); `𝓛` Laplace transform (14:450) |
| `R` | coefficient radius; `𝓡_m` remainder space (12:70) vs chessboard seminorm `𝓡_m` (11:820); `R_p` period; `R_d` representation (14:972) vs `R_d` label automorphism (13:137; notation.md flags this); `R_{ab,cd}` (14:616); `𝓡_{m,ρ}` (14:467); `R_E(z)` (14:685); `R_I` (14lc:49); `R_ε` (15:188); `R_0` radius (14:562) |
| `S` | correlations `S_n`; scaling maps `S_t` (14lc:36), `S_{t_N}` (13:137); `S_m=e^{B_m/64}` (12:271); `S_k` rescaled kernels (14:172) |
| `T` | `log(1/r)` (18lp:15); stress tensor; `T=I_{w^♯}I_w` (14:112); translations `T_t` (14:40); extraction map (14lc:30); support cost `T_l` (18lp:113); `𝓣` tiling; tube `𝒯_n`; cutoff parameter (14:513) |
| `P` | `P(k)` volume subsequence (13:32); projections `P_0`, `P_μ^0`; spectral measure `P_μ` (14:70); `P_{N,p,d}` (13:137); `𝓟_{N,h}` (13ba:227); `𝓟_D` reconstruction (18lp:279); `𝓟` word algebra (16:293); `P` low projection (18gq:51); `P_d^{loc}` (13ba:217) |
| `Q` | support with large-field set (12:162); `Q_h` bound (13ba:15); `Q_{A,B}` model function (14:860); `Q_0,Q_1,Q_2` (14:646); `𝒬^J_v` flux (14:319); zero-energy projection `Q_ξ` (16:437); local charge `Q_K` (16:523) |
| `q` | `q_r` vacuum normalization bound (12:247); `q^{site}` (13sb:24); `q=\log H_k/(16n)` (14lc:61); exponent `q<0` (14:538); `q_j` momenta (16:174); `q` copies (15:196); `q_A` (16:39); remainder size (18lp:36) |
| `r` | base level (12:233); separation/buffer (13:334); rank `r_d` (13:146); `r_k` rescaling (14:171); stencil radius `r_d` (13ba:251) — `r_d` has two meanings in chapter 13 and its fragments; `r_l` remainder norm (18lp:27); moment order (14:439) |
| `w` | Euclidean word; width (12:48, 14:473); weights `w_i` (12:247), `w` (13ba:105); `w_d` exponent (13sb:58); functional `w_ξ` (16:295) |
| `ω`, `ϖ` | weights `ω_k` (13sb:58), `ω` (18lp:168) vs width exponents `ω_j` (14:559); `ϖ` residual weight (18lp:188) vs `ϖ(E)=(1−\cos E)/E` (16:410) |
| `ζ` | `ζ_i` smallness (13ba:57); cutoff `ζ` (14:736); `ζ_a` Wick factors (16:503) |
| `χ` | cutoff function (14:315; 16:205) vs Hilbert–Schmidt distance `χ(U)` (13sb:30) |
| `θ`, `ϑ` | reflection `θ` (13:284) vs exponent ratio `θ` (18lp:19) vs normalisation `θ` (14lc:38) vs angle (14:862); `ϑ` linear time reflection (15:177) |
| `σ` | support exponent `σ_m` (12:237); bump `σ` (14:456); permutation (16:239) |
| `ν` | spectral measures `ν_μ^A` (14:418) vs phase measure `ν` (15:142) |
| `*`, `†`, `♯` | `w^*` (13:283), `w^†=τ_{se_4}θw` (13:338), `w^♯=τ_hθ_μw` (14:88: the same construction, new symbol), `A^{†_a}` (14:893), field adjoint `A^*=R(s_4)\bar A` (16:130) |

---

#### 7. The ten most confusing terms

1. **graph** (ch. 12): a linear map called a graph; 17 uses, name never motivated.
2. **column / inverse-column bound**: the coefficient vector and coefficient map; ≈20 uses, never defined in these chapters.
3. **label**: silently changes from a polynomial in `V_d` (ch. 12–13) to an element of the quotient `F_d` (ch. 14–16), against notation.md.
4. **mixed**: the undecomposed mixture, used from 14:12 before any mixture is mentioned; also "polarised" and "of both signs".
5. **stopping / stopped**: truncation at an intermediate level; suggests stopping times.
6. **attachment** and **incidence**: 11 and 5 uses, meaning not recoverable from these chapters.
7. **trial** (local, coarse, protected, descent, encoding): central to 13ba and 13:226–242, defined only by formula for `V_h`.
8. **heat** (semigroup, energy, orbit, damping): the reflection-positivity semigroup; nothing to do with a heat equation.
9. **centered**: "inside a cell with margin" in ch. 13, "zero expectation" in ch. 14.
10. **history / schedule / trajectory / stage / level**: five words around the scale sequence, with "history" shifted from the dictionary's sense; plus **physical** in three senses.

Also noteworthy: mechanical-translation residue produces ungrammatical phrases, e.g. "including the prescribed set of large-field sites terms" (18lp:43), "all support and prescribed set of large-field sites data" (18lp:136), "Each term is assigned the union of its supports and original prescribed set of large-field sites" (18lp:185), "its counterpart constrained to cover the prescribed large-field sites" (13sb:63), "A finite separating family of correlation pairings justify" (14:832).

Jargon surviving only in labels (not in the PDF): `ch12:inputs`, `ch12:forgetting`, `ch12:omission`, `ch12:stopped`, `ch12:root-bound`, `ch13:coarse-residual-supplier`, `ch13:sharp-root`, `ch13:residual-height(-bound)`, `ch13:scale-thickness`, `ch13:sharp-schedule`, `ch14:grid-input`, `ch14:grid-cost`, `ch14:balanced-stress`, `ch14:subset-root`, `ch14:diagonal-mass`, `ch14:heat-pairing`, `ch15:detector-moments`, `ch15:compression-defect`, `ch15:whole-gram`, `ch18:graded-room`, `ch18:low-cone`, `ch18:high-step`, `ch18:group-weight`; referenced from ch. 11: `ch11:uniform-sweep`, `ch11:finite-detector-input`, `ch11:simultaneous-detector-lifts`, `ch11:replicated(-bound)`, `ch11:n-mark-comparison`, `ch11:higher-induction`, `ch11:one-graph`. Note `ch13:sharp-phase` is a label defined in `15sp` (15sp:21).

---

#### 8. Not read / not checked

- All eleven assigned files were read in full (3869 lines), as were Part II and the translation table of `blueprint/notation.md`.
- Chapters 10 and 11 were consulted only by grep and short excerpts (10:20–32, 133, 808; 11:370–400, 780–826, 889–960, 1070–1112) to locate definitions; meanings marked "R (ch. 11)" rest on those excerpts, not on a full reading. Chapters 17–19 and `18-operator-products.tex`, `18-raw-replacement.tex` were not opened.
- Figures (`figures/ordered-limits`, `ward-shell`, `cluster-exchange`) were not opened.
- Counts are grep counts of occurrences, not hand-verified one by one except for `row`, `actual`, `select-`, `test`, `label`, `mark`, `window`, `history`, `probe`, `response`, `transport`, `frame`, `anchor`, `cost`, `centered`, `mixed`, `column`, `cone`, `admissible`, which were classified line by line from one-line contexts after the full read; borderline assignments could shift by one or two. The counts marked ≈ (`phase`, `word`, `source`, `physical`, `threshold`, `level`) are approximate.
- No Lean declaration was consulted; no proposed equivalent was checked against the literature. Section 6 is a list of what was noticed, not a complete symbol audit.

### V.B Independent audit

*Original title: Independent audit of Part V.A (survey C)*

> **Status.** Independent check of Part V.A by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in Part I, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only audit; no repository file was edited. All eleven chapter files (3869 lines) were read in full, then every row of the survey's sections 1, 2.2, 2.3 and 4 was checked against the cited lines, and the multi-sense words were re-classified from `grep -n` output with `\label/\ref/\eqref/\input/\cite` arguments stripped. Abbreviations are the survey's (`12`, `13`, `13sb`, `13ba`, `18gq`, `18lp`, `14`, `14lc`, `15`, `15sp`, `16`); other chapters are cited as `1:`, `2:`, `9:`, `10:`, `11:`, `11R:`.

**The worktree changed during the audit.** HEAD moved to `ac15effb` ("Repair thirteen sentences broken by mechanical term replacement"). In my files it rewrote 14:832, 18lp:43 and 18lp:136; line numbers are preserved. Quotations of those three lines in the survey and overview were verbatim before that commit and no longer match the text.

Overall: the survey is mostly reliable on line references and quotations (I found no misquotation inside my chapters). Its weak points are (i) several terms declared undetermined or inferred that other chapters define, (ii) four wrong or shifted meanings (`terminal graph`, `normalized local insertion`, `probe`, `stopping` in 13sb), (iii) three occurrence counts that are off by much more than "a few" (`spectator`, `source`, `physical`), and (iv) a handful of proposed equivalents that collide with existing or standard usage.

---

#### 1. Definite errors

1. **`terminal graph` "is at the intermediate level m+h, not at N" (§2.2, basis R, cited 12:131, 139).** Not supported. The word "terminal" occurs only in the title 12:131 ("Forgetting the terminal graph"); 12:139 says "Replace the selected graph at $m+h$ by one fixed admissible graph" and does not contain the word. Every other "terminal" in these files means "at the cutoff N": 13ba:123 "its terminal source satisfies the joint attachment bound at $N$"; 13:217 "inverse terminal coordinates"; 11:895 "the terminal trial". The natural reading is that the dependence on the graph at the cutoff level is what is forgotten; the replacement at m+h is the proof device. The R code is an inference, and probably a wrong one.

2. **`normalized local insertion` = "the source multiplied by ω_k" (§1.1, basis R).** Wrong object. ω_k is the *weight* attached to the insertion: 18lp:243 "The weights of normalized local insertions in \eqref{ch13:weight-size}". The normalized local insertion is the canonical insertion of a label, which is subtracted from a trial: 11:895 "Subtract one normalized local insertion density from the terminal trial, choosing its reference coefficient"; 13ba:119 "the negative normalized local insertion used in the subtraction". notation.md:158 agrees ("primary source | Normalized local insertion, with its local polynomial coefficient"). 13sb:65 ("multiplication of the complete source by $\omega_k$") describes the weighting, not the definition.

3. **`spectator` "49×" (§2.1).** The count is 33 (13: 10, 18gq: 2, 18lp: 3, 14: 15, 14lc: 1, 16: 2).

4. **`source` "≈60" with sense (a) "≈38" (§3).** The count is 49. Senses (b)–(e) are 7 + 4 + 6 + 1 as stated, so sense (a) is 31, not ≈38 (12: 14, 13sb: 3, 13ba: 9, 18lp: 3, 14lc: 2).

5. **`physical` "(37)" (§3).** The count is 31; the survey's own sub-counts (≈17 + 7 + 7 + 1) also give 32, not 37. Sense (i) is 16.

6. **`test`, 14:207 assigned to "pair with all spectators / exterior words" (§3 (b)).** 14:207 is "Testing against each fixed $f$ separately would be weaker" where f is a test function (14:203–204). It is integration against a test function. The overview repeats the misassignment (§2.4).

7. **`macro-box radius` listed as occurring at 13ba:229–248 (§2.1).** The word "macro" does not occur in any of the eleven files. The text is "each endpoint frame reads a box of fine-lattice radius $(j_i+3)L_i$" (13ba:244–245).

8. **`the source construction` (§1.1, §4): "the parameters there are M_k while 14lc uses H_k".** This is not a mismatch. M_k is the generic sequence of 14:171 ("let $M_k\to\infty$, $r_k\to0$"), and 14lc instantiates it as H_k term by term: 14:187 "$r_k=a_kM_k^{\alpha_0}$, $s_k=M_k^{-\alpha_0}$" against 14lc:26 "$r_k=a_kH_k^{\alpha_0},\qquad s_k=H_k^{-\alpha_0}$"; 14:188–189 against 14lc:85–86. So the phrase refers to the construction given in 14lc (or to its counterpart in the formal source). Which of the two is still not stated.

9. **`admissible`: "undefined: remainder graph 12:37".** 12:37–38 "any fixed admissible remainder graph" is the admissible graph defined at 12:82, used 45 lines early. It is a forward reference, not an undefined term.

10. **`row` "(7)".** There are 8 occurrences, and the survey's own sub-counts add to 8.

---

#### 2. Basis codes that overstate or understate

**Overstated (R or D for what is inferred)**

- `terminal graph` (§2.2): R → I at best; see 1.1.
- `normalized local insertion`: R → wrong; see 1.2.
- `graph` (§1.1): "A linear map" is given under D, but 12:82 does not say "linear". Linearity comes from 11:379 "Let $G$ be an incoming linear graph". D for the bound `‖Gx‖ ≤ s_m‖x‖_1`; "linear" is R from chapter 11.
- `probe` (§2.2, R): see section 3 below; the stated meaning is not what 18lp:332 shows.
- `separated` (§1.2, R, cited 14:17–18): the cited lines do not contain the word ("evaluated at distinct points or against test functions supported away from collisions").
- `subpower` (§2.3): "13:159, 217 use 'subpower in a_N^{-1}'". Those lines say only "subpower inverse terminal coordinates"; "in $a_h^{-1}$" is at 13ba:18 and 11:1101.

**Understated (I, ? or "not defined" for what the text settles)**

- `section` (§1.1, "no", I): defined at 2:138–146, "A local polynomial section is a complex-linear map $P_d^{\mathrm{loc}}:V_d\longrightarrow$ {polynomial functions of finitely many link entries …}" and "The term section simply means a right inverse of the Taylor map". 11:15 recalls it and 13ba:217 uses the symbol. D (ch. 2).
- `history` (§2.3, I): defined at 11:18–19, "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations." The survey's gloss ("the sequence of renormalisation steps started at a given cutoff") is close but is not the definition.
- `separated` test function (§1.2, "no"): defined at 1:359, "A separated test function is an element of $C_c^\infty(\Conf_n)$, extended by zero".
- `complementary profile` (13ba:165, I): 13ba:16 gives the sense explicitly, "its complete bound, including the complementary large-field part". R.
- `bounded rows` (13:159, I): 11:2253 "The rows $(I-\Pi_i)u_{j,i}$ are bounded, hence admissible." R (ch. 11).
- `centered` sense (iv), 18lp:224 (I): 1:217 "Odd block ratios give centered blocks". R (ch. 1).
- `marker amplitude` = source weight (14lc:61, I): notation.md:216 "R_I, G_I, omega | Corrected subset source, free subset moment, and source amplitude". Supported, though only by the blueprint.
- The §4 terms listed in section 8 below.

---

#### 3. Sense misassignments, with my per-sense counts

Counts are mine, from stripped `grep -o -i`.

**actual (20; survey 20, correct).** (a) of this construction 14, (b) produced against substituted 2, (c) belonging to cutoff N 2, (d) true function against the model Q 2. I agree with the assignment. Borderline, judgement only:
- 18lp:229 "on the actual histories" sits in (c) by analogy with 13ba:32; it reads equally as (a).
- 12:118 "actual inserted density" contrasts with "only … the regular part" (complete against partial).
- 13:162 and 14lc:53 contrast the interacting object with the free one.

The dictionary senses "nonlinear" and "running coupling" do not occur, as the survey says.

**row (8; survey "7").** 12:55 displacement-indexed quadratic path coefficient 1; literal matrix row 3 (13:168, 182; 14:277); 13:159 1; 15:275 (two), 278 3. Two merges are suggested:
- 15:275–278 "reference rows" are the rows of the matrix of correlation pairings of 15:288–289, so survey senses (d) and (b) are one sense.
- 13:159 is the usage of 11:2253 (rows of a finite list of coefficient vectors), which the overview files separately as "vector in a finite list".

**selected / select / selection (23; survey 22 + "Selecting", correct).** (a) 11, (b) 3, (c) 3, (d) 2, (e) 3, plus 15:301. Assignment accepted, with two doubts:
- 13:395 "all refer to the same selected family" is put under "continuum family". The items listed there are lattice estimates, and parallel passages say "the same lattice family" (15:250–251; title of 14lc:2). It could be sense (a).
- 13ba:30 "selected level-$h$ polynomial coordinates" is most simply "on the selected history" (sense (a)), since J_h is a map along that history (13ba:274–276).

**test (47; survey ≈47, correct).** Mine: test function 30, paired with spectators or words 7, "tested" as smeared or evaluated 10. Two moves:
- 14:207 goes from (b) to (c); see 1.6.
- 16:215 "the tested function and all its derivatives decay exponentially" is the test function itself (the argument of the distribution), so it belongs in (a), not (c).

The chapter 4–6 senses do not occur.

**label (59; survey ≈60, correct); tag 0.** (a) ≈30, (b) ≈26, (c) 3, (d) 1 accepted. Not decidable from the text: 13:282–285 (labels of a "word", stated after the quotient is defined), 18lp:295, 14lc:7, 13sb:176. The claim that notation.md requires (a) and (b) to be kept apart is correct (notation.md:150 "distinguish from quotient field").

**mark / marked / marker (53; survey 53, correct).** 34 / 12 / 3 / 2 symbols / 2 "unmarked". No misassignment.

**window (6), history (7).** Correct, one sense each. For `history` see section 2.

**source (49; survey "≈60").** Variable 31, inserted observable 7, weight 4, "source attachment / constants / corrected-source" 6, 14:186 1. The assignment of lines is accepted; only the totals are wrong. In sense (d), "corrected-source estimate" (14lc:45) is not undetermined: 14lc:49–54 defines the corrected coefficients R_I and says "These are precisely the coefficients of the actual squarefree source polynomial divided by the free moment polynomial".

**response (25; correct).** One-slot 15, spectral 8, flux 2. The "spectral" sense holds two different objects:
- a function of E, the Laplace transform of a profile: 14:465, 531, 688, 697, 740, 761 (6);
- the number obtained by evaluating a functional on a product of profiles: 14:654 "the transverse responses of $Q_0,Q_1,Q_2$", 14:672 (2), and the displayed `Resp_i(g)` at 14:503.

**transport (14; correct).** RG transfer 8, comparison maps 5, "carries over" 1. In the second group 14:281–282 ("Center the componentwise map $U_{k,4}$ after transport … its inverse transports back") is application of U_{k,d} to a field array, not conjugation. "Conjugation" fits only 14:229, 302, 946.

**Words given a "new sense" in §2.2**

- `probe` (6): one sense, but not the survey's. The survey reads it as "finite linear combination of separated correlations used as a coordinate functional". 18lp:332 has "using fixed cells for exterior probes and shrinking cells only for cluster factors", and 14:354 "chosen by fixed probes before the exterior spectator". Probes occupy cells, so they are the fixed exterior insertions (words) whose correlations realise the coordinates. That is the sense the overview reports from 18:36–38 ("a fixed word v …").
- `stopping` (11 with "stopped"; survey 10): two senses merged.
  - Chapter 12: stop at level m *and* delete the terms of source degree ≥ 2 (12:207–216).
  - 13sb:85, 102, 137; 13ba:193; 18lp:159: the level k at which the transfer is halted and the normalized chessboard bound applied, with nothing deleted. 13sb:9–11: "We keep all incoming joint marked components; replacing them … would invalidate the estimate."
- `request` (12): three uses merged.
  - A finite tuple of data (14:224–227; 14lc:9, 79, 108).
  - A requirement placed on the schedule (13ba:100 "countably many finite degree requests to the single schedule of coupling thresholds"; 18lp:103, 151).
  - A prescribed lower bound on a level (13:96; 13ba:336; 15:207).
- `cutoff`: the survey lists three senses and omits the most frequent one in chapters 14–16, a smooth cutoff function (≈17 uses: 13ba:36, 165; 14:252, 324, 328, 347, 396, 614, 620, 625, 736; 16:205, 232, 235, 283, 459, 539). 14:324 "independent of the cutoff" is the function χ, not N.
- `cost`, 18lp:85 ("The incidence norm has a second cost") is filed under "error term". It is a combinatorial factor, "at most $(1+\mathfrak N)n$ assignments per representative" (18lp:88).
- `anchor`, `lift`, `representative`, `charge`, `centered`, `word`: accepted. "Center … centers" as verbs at 14:281, 283 belong to the zero-expectation sense and are not listed.

**Multi-sense words the survey does not treat as such**

- `scalar`: besides the constant term of the exponent, "strictly ordered scalar heights" (16:218) and "positive scalar imaginary gaps" (16:248) mean purely time-directed imaginary parts; also "scalar operators" (16:481) and "the two scalar corrections" (14:283–284).
- `gap`: time separation (14:731 "a genuine temporal gap", 15:76), difference of heights (16, 15×), spectral (15:340; 16:383).
- `corrected`: with free moments subtracted (14lc:45; 15:17, 253, 258) against "corrected projection / inclusions" (18gq:8, 110, 114).
- `signed`: signed coordinate permutations and reflections (14:26; 14lc:8; 13ba:60 "signed symmetry orbit") against "with its sign kept" (18lp:24 "Signed local transport", 18lp:65) against 13sb:35 "Signed regular costs".

---

#### 4. Wrong line references and misquotations

No misquotation found in my chapters (subject to the `ac15effb` note above).

Lines that do not contain the cited term:
- 12:139 for "terminal" (§2.2).
- 14:17–18 for "separated" (§1.2).
- 14:354 for "exterior word" (the text is "exterior spectator", continuing on 355).
- 13ba:229–248 for "macro-box" (absent from all files).
- 13:159, 217 for "subpower in a_N^{-1}".

Cross-chapter references off by a few lines (outside my files):
- "11:808 'absolute action cost per site'" is at 11:789.
- "11:1094" for the equation space is 11:1089–1093.
- "11:258" for the incidence sum is 11:257.

Missed occurrence: `subpower` also at 13:235.

---

#### 5. Omitted terms

House usages in my files with no entry in the survey:

- **origins** ("physical origins", "insertion origins": 12:22, 208, 230, 239, 279). Position of an insertion; a synonym of `anchor` that the synonym table does not list.
- **background convergence / background limits** (12:31, 41, 175). R at 12:31–34: Cauchy convergence of β, the path coefficients and the activity arrays.
- **normalized null condition / estimate / representative argument** (13:192, 215, 240; 18gq:9, 108). D by formula at 13:198–203.
- **microscopic** (18gq:10, 76, 84, 94, 97–98) = at the cutoff level N.
- **unit** ("the distinguished unit" 13:58; "the unit" 14:220, 283, 408, 974; "unit vacuum" 14:34, 15:25) = identity field.
- **grid** (14:177–200; 14lc:29, 75; 18lp:225, 300, 327–342; 15:178, 207; 13ba:305–336): "grid word", "grid error", "grid restriction", "grid target", alongside "lattice".
- **target** ("derivative target" 13:252, 260; "grid target" 18lp:341; "target exponent" 18lp:344).
- **raw** ("raw representatives" 13sb:173; "raw coordinate", "raw replacement error" 18lp:318, 324–325; "total raw angular response" 14:777).
- **ordinary** = small-field ("ordinary norm bound", "ordinary chart", "ordinary derivative constant", 13ba:15, 37).
- **signed**, **corrected**, **scalar** (ch. 16), **gap**: see section 3.
- **replacement** ("local replacement", "replacement field" 14:353; titles 18lp:4, 220, 282) and **reconstruction** $\mathcal P_D$ (18lp:266–279, "finite correlation reconstruction maps").
- **collision orders** (14:519, 579, 611); **Ward sum** (14:812, 841, 901, 917); **vector-map space**, **defect space** (14:817, 820, 937).
- **endpoint estimate / endpoint comparison** (13ba:18, 34); **fine end** (18lp:46, 63).
- **vacuum normalization bound**, **vacuum denominator** (12:247, 286): "vacuum" for the insertion-free lattice integral.
- **exceptional phases** (15:325–340; 16:380).
- **positional** ("positional modulus" 14lc:92; "positional derivatives" 14:813–814, 841; 18lp:296).
- **reference label / coefficient / insertion / rows** (18gq:12, 85, 106; 13ba:200, 275; 15:278).
- **transitions** between stages (13sb:49; 13ba:81); **degree ceiling** (13ba:56).
- Forward uses not noted: "slab" at 13:335, 391 before its definition at 14:86; "phase" at 13:393, 13ba:5, 304, 18lp:7, 14:351, 371 before 15:8; "mixed" at 18lp:8 (input into chapter 13) and 14:12 before 15:5.

---

#### 6. Questionable equivalents

- **stopping → "truncated correlation `C_{N,p,m}`".** Misleading. "Truncated correlation function" is, to my knowledge, the standard name for connected (Ursell) functions in this literature. It is also wrong for 13sb/13ba/18lp, where nothing is deleted. I would write "correlation with the terms of source degree ≥ 2 deleted at level m" for chapter 12 and "the level k(m) at which the bound is applied" for 13sb.
- **graph → "remainder map".** Collides with the text's own "unreparametrized remainder map" J_G (12:91) and "raw remainder map $R_G$" (11:381). I would write "the linear map G from coefficients to remainders".
- **unmarked gas → "partition function without insertions".** Changes the meaning. The gas is a function of the configuration U (12:180–183 "a finite polynomial in the latter profiles and fixed eligibility indicators"); the partition function is its integral (12:173).
- **heat semigroup → "(Osterwalder–Schrader) transfer semigroup".** I do not know "transfer semigroup" as a standard term ("transfer matrix" is the discrete-time lattice object). "The contraction semigroup $e^{-tH}$ of time translations" is safe. The remark "nothing to do with a heat equation" is a judgement; I am unsure how unusual "heat semigroup" for $e^{-tH}$ is.
- **profile → "one-variable multiplier".** "Multiplier" suggests a Fourier multiplier operator. I would write "one-variable factor of the product test function in momentum space".
- **moment → "correlation".** Acceptable at 12:293, 14lc:47, 14:898. Wrong at 15:213 "compressed product moments": these are $\langle\Omega,M(w_1)\cdots M(w_k)\Omega\rangle$, and 15:123 says "Compression is not multiplication of finite-separation words", so they are not correlations of a word.
- **remainder with vanishing extracted coefficient → "term with vanishing Taylor polynomial of degree t".** Fits only the regular part (18lp:38). The large-field part has no Taylor characterisation there (18lp:39–40 "the large-field term retains half the suppression").
- **low plane → "subspace of dimension < i".** Ambiguous between linear and scaling dimension. Write "span of the basis polynomials of scaling dimension below i".
- **recentering → "renormalisation of the remainder".** The survey flags it as unsure; I agree it should not be used. 18lp:40–43 is the subtraction of the output coefficient.
- **ancestor cone → "domain of dependence".** Usable, but the cone also contains the auxiliary random variables (13ba:232–233), and the dictionary already has "dependence region". Judgement.
- **`ker H` → "zero-energy subspace; vacuum"** (§5). "Vacuum" must not replace "ground space" in chapter 15: 15:47–48 "it does not say that this space is one dimensional".
- **cell → "tile"**, **buffer → "margin"**: neither is an improvement. "Cell" is ordinary in chessboard estimates, and "margin" already names a different length (3a_k at 13:88). Judgement.
- **mixed measures → "polarised measures"**: I am not sure "polarised" is standard; "the complex measures $\nu^{AB}$ obtained by polarization" is.

Accepted as standard: iterated limit; argument (slot); n-point (arity); coincident coordinates; with pairwise distinct coordinates in every direction; imaginary parts; coefficient vector / coefficient map (the text itself says "coefficient map" at 12:90).

---

#### 7. Overview claims concerning these chapters

**Errors**

- **§2.1 `actual`, column "ch. 12–16": 14 and 4.** These sum to 18 of 20. The two uses "the true function against the model solution Q" (14:868, 869) appear in no row. They fit the first row, which should then read 16.
- **§2.2 `row`: 12:55 placed under "component of the stacked vector whose half-square is the action".** At 12:53–55 the object is indexed by a displacement and summed over $x\in\ZZ^4$ ("The canonical indices enumerate displacement vectors … For a row their length is $|x|_1+4$"). That is the kernel sense (cf. 10:354 "quadratic rows"). Judgement, but the survey itself wrote "kernel/component sense, I".
- **§2.2 `row`: "bounded coefficient family 13:159" and "vector in a finite list 11:2253" as separate senses.** 13:159 restates 11:2253; they are one sense.
- **§2.4 `test`: 14:207 under "paired with all spectators or words".** It is a test function; see 1.6.
- **§2.6: "In 14:186, 18:411 and RG:82 'the source' is the formalisation the book was written from."** Stated as fact. It is clear for RG:82 ("source locations") and probable for 18:411 ("the source prescription and its proposed sharper local-order bound"; notation.md:206). For 14:186 the survey itself marks "?", and the parameters quoted there are those of 14lc (see 1.8). Should read "probably".
- **§2.7: heading "ten senses"; the table has nine rows.**
- **§2.11 `probe`: the 18lp:268 sense ("a finite combination of separated correlations") listed apart from the 18:36 sense ("a fixed word v").** 18lp:332 and 14:354 indicate one sense; see section 3.
- **§4, chapters 12–16.** Of the seven listed terms, three are settled elsewhere (`trial encoding`, `site conversion`, `corrected inclusions`) and `attachment` is largely settled; see section 8. `sparse stopping` can be inferred. Only `coordinate hybrids` and `protected trial` stay open.
- **§6 broken sentences.**
  - 18lp:43 and 18lp:136 were broken as quoted and are repaired in `ac15effb`.
  - 18lp:185 ("Each term is assigned the union of its supports and original prescribed set of large-field sites") and 13sb:63 ("its counterpart constrained to cover the prescribed large-field sites, as well as the source attachment bound") parse. They are awkward, not broken, and the repair commit left them alone.
  - Further candidates in my files: 18lp:27 "a remainder with vanishing extracted coefficient of norm $r_l$" and 18lp:36 "… of size $q$" (the norm or size belongs to the remainder, not the coefficient); 16:380 "by \ref{ch15:ae-ground}", a bare `\ref` where `\eqref` is meant.
  - 14:832 "justify" (survey §7) is fixed in `ac15effb`.

**Confirmed**

- §1: the description of chapters 12–16; no accounting words `price, pay, purchase, budget, receipt, ledger, fund` in prose (grep: 0).
- §2.3: 13:172, 15:257 as "continuum family along the chosen subsequence" (13:395 doubtful, section 3).
- §2.5: the label split and the notation.md requirement.
- §2.6: "marked" at 12:200–206.
- §2.7: the three chapter 13–14 rows.
- §2.8: 14:229–302, 946 (with the nuance on 14:281–282).
- §2.9: 14:173–237; 14lc:6.
- §2.10: 10:25 and 10:129–134 quotations (verified); 11:17–18 definition of history (verified at 11:18–19).
- §2.11: phase at 15:6–10 and 16:15; word at 13:282 and 16:291.
- §3: `subpower` at 18lp:18 agrees with 6:822; regularity stage at 10:25–29, 129–134.
- §5: the chessboard-seminorm notations (13:74, 13:302, 13sb:79, 13ba:24, 14lc:64).
- §7: all labels named from chapters 12–16 and 18 exist.

---

#### 8. Terms the survey calls undetermined that the text settles

- **trial encoding** (13:394; §4). 11:943–951: "a reference label $v_{N,p}$ with inverse terminal coordinates bounded by $2E_{N,p}$ and $\mathcal R_m\{F-O_{N,p}(e,v_{N,p})\}\le\ldots$"; 11:1074 "now supplies the trial encoding with subpower inverse terminal coordinates and a vanishing chessboard-seminorm error". The encoding of a trial F is that reference label.
- **site conversion; support conversion cost `T_l`** (13ba:145; 18lp:112–113).
  - 9:513 "The conversion of anchored bounds to containing-site bounds is explicit."
  - 11R:141–142 "the extra unit used to turn an anchored bound into a site bound. These are the support conversions".
  - 11:267 and 11:1918 "Root-to-site conversion costs only $\mathcal W(B)$".
  - $T_e$ is defined by formula at 11:233–237 (`ch11:cover-transfer`).
- **admissible period cell** (12:375). 1:359–361: a separated test function "is admissible at volume $p$ if its support is contained in $((-R_p/2,R_p/2)^4)^n$".
- **equation remainder; corrected projection; corrected (physical) inclusions** (18gq:8, 110, 114).
  - 18gq:108–110 applies the argument of 13:198–205; there the "corrected projection" is $\Pi_ux_u$ and the remainder is $(x_u-\Pi_ux_u)/(1+\|\Pi_ux_u\|)$, of which 13:220 says "Their difference lies in the exact finite equation kernel."
  - The inclusions are $\iota_{d,e}$ of 13:263–264.
  - "Corrected relative to what" *is* said: 18gq:94–95 "it is not the naive inclusion of unnormalized polynomials" (cf. 13:117–118).
- **attachment** (11 uses). Not defined in one sentence, but usage elsewhere fixes it as the joining of an insertion stencil or a complementary (large-field) part to an existing support in the polymer expansion, and the sum over the places where this can happen.
  - 9:687 "One additional unit of exponential support decay bounds the number of attachments, since a support has at most $(2B+1)^4c(Z)$ sites."
  - 11:924–925 "Attach the latter to the original selected large-field factors".
  - 11:937 "$u_N>0$ the terminal attachment reserve"; 11:941 "the complementary attachment".
  - So the "attachment bound" $u_i$ of 13ba:62, 77 is that reserve. Basis I rather than ?.
- **"Open the centered cells at m"** (13ba:127). Chapter 11 uses "opening" for the starting level of an estimate: 11:1889 "already present at the opening level"; 11:1919 "At the opening all distinct sites … are separated". By that usage, 13ba:127 means "start with the centered cells at level m". I, not ?.
- **sparse stopping** (18lp:159). 10:167–172 imposes the last condition of `ch13:sharp-schedule` and says "It will keep replication costs subpower at a nearby sparse stopping scale"; 13sb:85–86 has the anchors at the stopping level with "spacing at least $B_k^2$". "Sparse" = widely spaced anchors at that level. I.
- **common** (§4, cited 12:13, 40, 370). The cited lines are "common trajectory / construction"; 10:4–9 says what is common ("a single sequence of scales and a consistent choice of coefficient arrays … compare theories with different ultraviolet cutoffs"). "One common lattice" is at 12:230, 296, 299 and is clear in place: one of the nested lattices containing all the points (12:352).
- **corrected-source estimate** (§3 `source` (d)): 14lc:46–55; see section 3.

Remain open after my search of `chapters/`:
- `coordinate hybrids` (14lc:95; no other occurrence of "hybrid").
- `admissible comparison depth` (14lc:23; 11:884 defines an admissible comparison *coefficient*, not a depth).
- `protected trial` (13:229; 11:2306 uses it without definition).
- Whether "the source construction" (14:186) names the formal source.
- Why a linear map is called a "graph".

---

#### 9. Confirmed rows (meaning, basis and lines as stated)

- **§1.1:** fixed-input continuity; I_G / J_G; forgetting (the R gloss, apart from "terminal"); dictionary; inventory; large-field profile; complete; terms linear in the sources / modes; source weights; column; inverse terminal coordinates; admissible coefficient family (quotation verified at 11:1101–1102); trial; equation space; incidence; rooted; reserve; block floors (10:55 verified); first-below scale; comparison depth; lift; ancestor cone; frame seed; group / merger / live; recentering (meaning only); low plane; cell census; inspected.
- **§1.2:** ordered limits / tails; slot; arity (17); cell / centered; buffer; exterior word; slab; heat (meaning); damping; coordinate spectral measures; profile (meaning); annular correction; conserved stress line; line axis; shell factor; Ward kernel / normalization / spin operators (all I, as stated); phase (including the notation.md warning, verified at notation.md:169); compression; whole word; cluster; generic; coordinate ties; height / gap / tied; padding identity; letter; barycenter identity; partial boundary; local charge.
- **§2.2:** response (three rows); transport; anchor; label; word; window; lift; representative; charge; centered; cutoff (incomplete, see section 3).
- **§2.3:** regularity stage (10:25, 133, 808 verified); subpower (18lp:18); schedule; moving; marked; event indicator.
- **§3 counts verified:** actual 20, select 23, test 47, label 59, mark 53, window 6, history 7, response 25, transport 14, cost 25, mixed 23, column 22, cone 17, centered 24, probe 6, anchor 6, frame 4, phase 52, word 96, cluster 23, heat 18, level 77; price / pay / readout / table / tag 0.
- **§7 label list:** all present.

---

#### 10. Not checked

- Survey §5 (synonym clusters) and §6 (overloaded symbols): only spot-checked (`χ` at 13sb:30; `r_d` at 13:146 and 13ba:251; `R_d` at 14:972 and 13:137; the seminorm notations). Not verified row by row.
- Survey §2.1 (same-sense rows): cited lines were checked for the presence of the term; "same as the dictionary" was not re-derived against chapters 3–6.
- `label`: the split between V_d and F_d was checked at the lines listed, not for all 59 occurrences one by one.
- Sub-counts within `threshold`, `comparison`, `stage`, `margin`, `admissible` were not recounted.
- Chapters 10 and 11 were consulted by grep and excerpts only (10:4–22, 23–29, 53–56, 129–134, 165–176, 350–383, 806–809; 11:14–19, 160–172, 208–270, 374–382, 440–448, 496–504, 806–822, 880–960, 1056–1108, 1398–1410, 1880–1930, 2248–2256, 2296–2310); chapters 17–19 only for 18:405–413.
- Figures were not opened. No Lean declaration was consulted. No equivalent was checked against the literature; the judgements in section 6 are from my own knowledge.

---

<a id="part-vi"></a>

## Part VI. Chapters 17–19, main theorem, reading guide

### VI.A Survey

*Original title: House terminology survey D: chapters 17–19, main theorem, reading guide*

> **Audited.** An independent check of this survey is in Part VI.B; its corrections supersede the text below, which is kept as returned.
>
> **Status.** Survey by one agent (Claude Fable 5.2 subagent), reproduced as returned. It was written against upstream commit `7bec3925`. Meanings marked I are inferences; proposed equivalents were not checked against the literature. See Part I for the cross-chapter synthesis and for what was verified.


Worktree `manuscript/HumanizeYM_v3/` at commit `9e227b1a`. Read-only; no repository file was edited.

**File abbreviations** (line numbers are those of the worktree files):
`17` = chapters/17-trace-law.tex, `17w` = 17-variable-windows.tex, `17t` = 17-trace-transfer.tex, `17c` = 17-current-contraction.tex, `17m` = 17-marked-trace-rates.tex, `18` = 18-operator-products.tex, `18r` = 18-raw-replacement.tex, `19` = 19-assembly.tex, `MT` = main-theorem.tex, `RG` = reading-guide.tex. Other chapters are cited as `ch10:25` etc.

**Basis codes**: D defined in the text; R read off an explicit sentence or formula; I inferred; ? not determined. **Categories**: (a) accounting metaphor, (b) program/Lean leakage, (c) ordinary or standard word in unusual technical sense, (d) coined, (e) other.

Counts were obtained by `grep` on copies with `\label{}`, `\ref{}`, `\eqref{}`, `\pageref{}` arguments blanked. Occurrences in `\input{...}` file names are excluded where noted.

---

#### 1. New terms (not in the ch. 3–6 dictionary, or there only in §4.2 without a gloss)

##### 1.1 Scales, schedules and windows

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| stage; change of stage; stage plateau; adjacent-stage cases; fixed-stage tail; stage orders | 17:132; 17w:2, 13, 14, 49, 50, 69, 71, 97, 125; 17c:12, 107, 135, 238; 17m:39, 141, 197, 301, 346, 347, 430; 19:30; RG:34 (23 in all) | Not in these files. Defined ch10:25–29 ("A stage j≥1 specifies finitely many derivative orders, support …"), with `J(m)=j` for `A_j ≤ m < A_{j+1}` (ch10:129–134) | Index `j` of a finite package of requirements (derivative orders, weights, constants); `J(m)` is the stage in force at scale `m`. 17w:14–15: "`𝓛_j` for the ratio chosen at stage j, so `L_i=𝓛_{J_i}` with `J_i=J(i+1)`" | R (via ch. 10) | *stage* is acceptable if defined once per chapter; otherwise *parameter regime `j`*. Never use for "scale" or "step" | (d) |
| plateau (of a stage) | 17w:7 | Not here; ch10:123, 139 | Maximal interval of scales on which `J(m)` is constant ("requiring every window to lie inside a plateau would leave gaps") | R (via ch. 10) | *interval of scales with constant stage*. Different from the dictionary's plateau (region where a cutoff equals one) | (c) |
| level; insertion level `k_i`; radius level `n_i`; comparison level `k`; output level; stopping levels; late level | 17:85, 86, 120; 17w:41, 102; 17t:405; 17c:241, 391; 17m:136, 331, 416 | Named only: 17:84–87 "`β_i` … at a finer insertion level `k_i` … The radius level `n_i` precedes `k_i`"; `k(n)` by formula 17:108 | *Level* = scale index. `n_i`: scale whose spacing `a_n` fixes the radius `r=a_nM_n^u`; `k_i=k(n_i)`: finer scale at which the insertion and its coupling are taken. "Output level" (17t:405; 17c:241, 391): the fixed scale at which the transferred current is evaluated (inferred). "Comparison level" is the ch. 11 term (ch11:734) | R for `n_i,k_i`; I for output level | *scale `n_i`*, *scale `k_i`*; say what each indexes | (c) |
| (radius, comparison) window | see §3.4 | Radius window by formula 17:107 | Two objects: interval of radii `{a_nM_n^u: α₀≤u≤α₀+1}`, and the set of RG steps between `n` and a stopping scale | R | *interval of radii*; *range of scales* | (c) |
| stop backwards; first (backward) crossing; overshoot; stopping integers; stopping levels; stopping pair | 17:138, 142; 17w:31–36, 101, 105; 17m:425, 432, 469 | No | "stop backwards from n at the first crossing of `(b+2)log H_n`" (17w:31): first coarser scale at which a logarithmic length (presumably `log(a_m/a_n)`, cf. 17:108 and 17m:433) reaches the stated value; the quantity that crosses is not named at 17w:31. Overshoot = excess of that length over the target (17w:36) | I | *the first scale `m<n` with `log(a_m/a_n) ≥ …`*; print the definition | (b) |
| request (degree, arity, derivative, window request); requested | 17:140; 17w:10, 13, 73, 85; 17m:88, 142, 285; 18:144 | No | A fixed finite list of parameters (degree bound `D`, arity bound `N_*`, derivative order, error exponent) for which an estimate is to hold. 17w:10 "Fix a finite degree, arity and derivative request" | R | *fixed finite data `(D, N_*, r)`*; *for the given orders* | (b) |
| pre-ratio / post-ratio / fixed-ratio constants | 17w:24, 72, 75, 76; 17c:138; 17m:249, 428, 429 | 17w:13, 21 | Constants fixed before the block ratio `𝓛_j` of the stage is chosen (hence independent of it), respectively depending on the already chosen ratio. Same idea as the dictionary's "pre-`L` factor" | R | *independent of `L`* / *depending on `L`* | (d) |
| coupling threshold(s); coupling-threshold-controlled | 17:134; 17w:23, 42, 74, 76, 95; 17c:141, 234, 236, 384, 386; 17m:174, 185, 315, 365, 430; 19:20 (17) | No | Lower bound imposed on `β̂` at a stage ("sufficiently large coupling thresholds"). Same as dictionary §4.2 "coupling threshold" | R | *for `β̂` sufficiently large (depending on `j`, `L`)* | (c) |
| (common, scale) schedule | 17w:35; 19:18, 31; RG:32 | ch10:118 | The choice of all stage data and of `J(m)`: "The common schedule … selects all block lengths, derivative orders, support weights, coupling thresholds and admissible physical periods" (19:18–21) | R | as dictionary: *fixed parameter sequence* | (d) |
| equation calibration floor | 19:30 | No; ch11-equation-calibration:27–30 | A lower bound on `β̂_N` required by the ch. 11 comparison of microscopic equations. Not determined in ch. 19 | ? here | *the lower bound (11.x)* | (d) |
| floor | 17t:107 ("denominator floor … `a_μ ≥ cT²I`"); 19:30 | by formula | Lower bound | R | *lower bound* | (c) |
| shooting; coarse endpoint | 19:21–23 | No; ch10:210 | Choice of the bare coupling so that the trajectory ends at the prescribed coarse value `β̄` | R | acceptable (shooting method); or *tuning of the bare coupling* (MT:62 already says "tune") | (e) |
| current depth; deep transferred current | 17m:29, 361 | No | Number of RG transfers applied to the current | I | *number of steps* | (c) |
| restart; restarted representation / histories | 17w:33, 102; 19:49 | No; ch11:734 ff. | Not determined here ("`B_n` is the radius of the restarted representation") | ? here | cite the ch. 11 definition | (b) |
| replicate (verb) | 17m:432 | No; ch11:780 | "Replicate at the first backward crossing of `B_n²`": place reflected copies at that scale, for the estimate (11.replicated-bound) | I | *apply the chessboard estimate at the scale …* | (b) |

##### 1.2 Transfer of the current (chapter 17)

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| current defect `𝓔_b`; defect; quadratic defect; defect Ward identity | 17:194, 244; 17t:157, 408, 416; 17c:6, 13, 17 and 13 more; 17m:154 (22) | 17:194–195 | `𝓔_b = Σ_a∇_aJ_ab − D𝖲[Y_b]`: the failure of the lattice current-conservation identity. New sense relative to the dictionary's "curvature defect" | D | *conservation error of the lattice current* | (c) |
| "(quadratic defect) has order at least four" | 17c:17–23 | 17c:17 | `E_b(p,q)=O((|p|+|q|)⁴)` near 0: vanishing order of the Fourier symbol of the Hessian; "spatial momentum degree, not the field degree" | D | keep | — |
| low moments; low-moment cancellations / estimate; polynomial moment conditions; zero (exterior) moments | 17:19, 308; 17t:160; 17c:46; 17m:70, 155, 156, 191, 402, 443; 19:157 | No | Two things under one word. (i) Vanishing of low-order Taylor coefficients in momentum, equivalently annihilation of affine/quadratic polynomial fields (17t:159–160; 17c:24). (ii) "Exterior moments": integrals against spectators independent of the varied links (17m:67–70) | R / R | (i) *vanishing of the symbol to order …*; (ii) *integral against every function independent of the varied links* | (c) |
| stationary substitution `𝓘`; stationary pullback; exact pulled-back defect | 17t:28, 157, 159; 17c:51, 72, 77, 91, 208, 304 | 17t:28 | `𝓘F = F(U_stat(V))`: composition with the stationary fine field | D | *composition with the stationary field* | (c) |
| (actual) stationary tangent `W`; smooth representative `W_a`; `W_s`; radial `W^rad` | 17c:8, 48, 112, 187, 210, 323, 348; 17m:263; 17t:162 | 17c:48–50 | First derivative at zero of the stationary map, coarse links → fine links. See §6 for an inconsistency between `W`, `W_a`, `W_s` | D | *derivative of the stationary map* | (c) |
| anchor average `K_0`; mass-one; component average `K_a`; difference primitive `K_a^t` | 17t:19–27, 41–43; 17c:71, 82, 85, 120, 324 | by formula 17t:19–26 | Convolution operators acting on the base point of a local function before substitution. "Mass" = sum of coefficients (17t:41–43) | D (formula) / R (mass) | *average over translates of the base point*; *with total sum one* | (c) |
| (forward-difference) primitive `q_a`, `t_abc`; primitive norms | 17c:309, 313, 377, 382, 388, 390; 17m:380, 469 | 17t:62, 72; restated 17c:312–315 | Functions with `tr J = Σ_aδ_aq_a`, `J_ab−J_ba = Σ_cδ_ct_abc`. New sense (dictionary: elementary factor) | D | *discrete potential*; "primitive" is tolerable if defined | (c) |
| displacement `Y`; left link displacement; curvature displacement; displaced coarse current | 17:193; 17t:182, 297, 340, 355; 17c:247–291, 312–373; 17m:27, 57 (20) | 17:191–193; 17t:182–186 | A vector field on the product of link groups (link-wise Lie-algebra valued), generating `U ↦ e^{sY}U` | D | *vector field (infinitesimal left variation)* | (c) |
| leg | 17t:149, 152, 318; 17c:16, 76, 100–120, 326, 346, 363, 373 (16) | No | One of the two field arguments of a Hessian / bilinear kernel, with its own momentum ("two independent field momenta. Gauge invariance gives a Ward identity on each leg", 17c:15–16). New sense relative to the dictionary | R | *argument*; *each of the two variables* | (c) |
| channel | 17t:97; 17c:97, 136 | No | 17t:97: each of the two determinants (vector, ghost). 17c:97, 136: the field-order-two component of the defect recursion | I | *term*; *the order-two component* | (c) |
| field order; field degree | 17c:23, 93, 209, 303, 305, 369, 371, 375, 377; 17m:28, 178, 187, 188, 303; 17t:361; 19:157 | 17c:222 | Order of differentiation in the field at zero ("`e_r` is the weighted norm of the field derivative of order r"), contrasted with scaling dimension and momentum degree | D | keep; use one of *order*/*degree* | — |
| diagonal / below the diagonal; diagonal factor / transfer; row sum | 17c:140, 211, 228, 235–237, 346, 367, 369, 375, 383 | No | Entries of the triangular matrix of the recursion (17c:216) for the norms `e_r`: diagonal = coefficient of `e_r` in `e'_r` | R | *the coefficient `a_{j,r}(L)`*; *terms with `s<r`* | (c) |
| source (in a recursion); forcing | 17c:132, 225, 245; 17c:380, 382, 385, 386 | No | Inhomogeneous term of a linear recursion ("homogeneous … No constant source term") | R | *inhomogeneous term* (one word) | (c) |
| completed (vector operator, kinetic matrix, inverse, quotient calculation) | 17t:86; 17c:64, 144, 170, 176, 300 | 17t:86–87 by formula | With the gauge-fixing term added: `H+dd*`; `𝒞⁻¹` its inverse (ch. 7) | R | *gauge-fixed operator `H+dd*`* | (c) |
| (finite) covariant (path) completion | 17m:28, 30, 34, 179 | 17m:30–33 | Extension of a finite jet to a gauge-covariant function, obtained by replacing each monomial by a plaquette / parallel-transported expression and correcting lower jets | R | *gauge-covariant extension of the jet* | (d) |
| infinitesimal gauge insertion `d`; background insertions `b,c` | 17:234–235; 17t:85, 96, 102 | No | `d`: differential of the gauge action (17t:182 "infinitesimal gauge map at U"); `b,c`: first and second derivatives of an operator in the background field (vertices) | R / I | *infinitesimal gauge map*; *vertices* | (c) |
| regulated current; (scalar) regulator; regulator criterion / estimate / interval / factor | 17:152, 227, 249; 17t:3, 91, 104, 336, 382, 385, 428, 481, 487, 497; 17c:319, 392; 17m:354, 362 | 17:229 | The mass `μ` in `Γ_μ`; "regulator criterion" = hypotheses (17.regulator-input) / the list at 17t:404–411 | R | *mass regularisation*; *the hypotheses of §…* | (c) |
| (group-coordinate) contact identity | 17t:175, 229, 333, 414, 424, 496, 500 | Proposition 17t:229–237 | The identity (17.contact). Why "contact" is not explained; unrelated to the contact terms of ch. 18 | D (object) / ? (name) | *chart identity for `div_Haar Y`* or keep with a remark | (d) |
| chart velocity `𝒴_U`; left frame | 17t:188–197 | 17t:190 | `∂_s log(Ψ_s(e^zU)Ψ_s(U)⁻¹)`: the vector field in the moving left-exponential chart | D | keep | — |
| action-gradient terms | 17t:286, 332, 402, 473 | No | Terms of the form `DF[Z]` in (17.contact) | R | *terms `DS[Z]`, `DΓ[Y]`* | (d) |
| Haar coefficient `𝔥(Y)`; coefficient functional `𝗾`, `𝗹`, `𝗵`, `𝖼`; cubic momentum functional; lattice (coefficient) correction; anchored correction | 17:213–237; 17t:239, 288, 395, 482; 17m:351, 356 | 17:213–225; 17t:395 | Explicit Taylor-coefficient functionals; `𝔥(Y)=𝗵(div_Haar Y)`. "Lattice correction"/"anchored correction" = the term `𝖼` | D | keep symbols; drop the nicknames | — |
| trace functional `ρ`; raw divergence `div_raw`; raw vector coordinates | 17:179–183, 301; 17m:356, 462 | 17:164–181 | `ρ(x,y,z)=−2x−8y` on `E=ℝ³`, the coordinates of divergences "before imposing the Maxwell equation" | D | *coordinates before passing to the quotient by the equation of motion* | (c) |
| equation direction `v_i^eq`; `v_eom` | 17m:375, 385–386 | `v_i^eq` by formula 17m:386; `v_eom` never defined in these files | Presumably `v_eom = v=(0,0,1)`, the kernel of `s` (17:172) | I / ? | define `v_eom`; *kernel vector of `s`* | (d) |
| conserved line | 17:341 | No | "The conserved line gives `Z_i=ν_iT`": the conserved tensors of this type form a line (ch. 14, label `stress-line`) | I | *one-dimensionality of the space of conserved tensors* | (d) |
| trace stability amplification `e_i`; stable functional | 17:261–289 | 17:284 | Rates `e_i`, `q_i` | D | keep symbols | — |
| same-family; common family; lattice family; one family | 17:100, 281, 295; 18:172; 19:12, 46, 56, 58, 112; MT:58; RG:36 | 19:15–23 | The single family of Wilson measures indexed by cutoff `N` and period `p`, with all choices fixed once | R | *for the same family of measures* | (c) |
| density identity | 17m:62 | 17m:63–66 (emphasised) | `div_Haar(FY)=∫𝒟_Yk f dU` | D | keep or *differentiated kernel identity* | — |
| density-valued (kernel) insertion; score source; zero-moment source | 17m:68, 155, 391, 400, 443, 459 | No | The factor `𝒟_Yk` inserted in the block integral in place of `k` | R | *the differentiated kernel `𝒟_Yk`* | (d) |
| complementary (marked sum, part, large-field estimate); failure | 17m:121–131, 321 | No | Terms in which some small-field or chart condition is violated somewhere in the connected component of the inserted factor ("Every term with a failure anywhere in the marked connected component … is kept in the complementary marked sum") | R | *large-field terms*; *violation of a small-field condition* | (c) |
| ordinary (contribution, expansion, selections, logarithm, score, factors, cancellation) | 17m:86, 90, 92, 102, 112, 119, 131, 185 | No; ch9:150 "the ordinary gas without large-field sites" | The purely small-field part of the expansion | R (via ch. 9) | *small-field* | (c) |
| threshold coordinates; `𝒫_{5,t}`; threshold ball; fine threshold | 17m:143–148, 153, 272, 304, 378 | `𝒫_{5,t}` at 17m:145 | Coefficients rescaled by `t^{f−2}` (`f` = number of curvature factors); ball of radius `t` in link logarithms | R / I | *coefficients normalised by `t^{f−2}`* | (d) |
| crop; cropping; crop radius / tail | 17m:258, 279, 289, 310, 313 | 17m:258 | Restriction of the coarse field to radius `C_j(log β̂_k)²` | R | *truncation to a ball* | (b) |
| jet menu | 17m:255 | No; cf. ch11:161 "fixed finite menu" | Finite set of admitted tuples of polynomials (total scaling dimension ≤ 5) | R | *finite set of jets* | (b) |
| (deterministic) coefficient evaluation; coefficient recovery; coefficient conversions | 17m:251–301, 471 | No | Evaluation of the extraction functional on polynomial inputs without Gaussian fluctuation; inversion of a finite matrix of pairings | I | *value of the coefficient functional at `gz=0`*; *inversion of the finite system* | (d) |
| reserve (derivative, support, width) | 17w:84; 17m:49, 103, 198, 282 | No | An extra derivative order, or part of an exponential decay rate, kept unused for a later step ("one derivative reserve") | I | *one additional derivative*; *a strictly smaller rate* | (a) |
| gain; loss; cost; margin; absorb | cost: 24 (17t:105, 108, 110, 163, 478; 17c:119, 364; 17w:59, 73, 108, 115; 17m:45, 130, 172, 180, 261, 301, 427, 428, 434; 18:230, 256; 18r:33; RG:26). gain: 17c:351, 361, 366, 375, 378; 17m:132, 187, 330. loss: 17c:107; 17m:79, 166, 174, 417; 17w:91, 119; 18:128, 257 | No | As in dictionary §2.6. RG:26 "a positive action cost is retained" = a lower bound on the action | I | *is bounded by*; *improves by a factor*; print the inequality | (a) |
| trial descent; descending graph; endpoint error | 17m:444, 461, 469, 470 | No; ch11:890 "Backward comparison of a local trial" | Fine-to-coarse propagation of a local lattice function compared with a normalised insertion | R (via ch. 11) | *backward comparison (Section 11.x)* | (d) |
| vacuum bound `q_n`; positive-density / positive partition estimate; terminal norm bounds; inverse source-weight bounds; physical mark normalization; exterior discrepancy | 17m:426–442; 17w:97 | No | Named ch. 11 quantities; see §4 | ? | cite equations | (b) |

##### 1.3 Operator products (chapter 18)

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| probe; probe word; probe family; probe coordinates | 18:38–77, 115, 168, 215, 222, 241 (16); 18r:37, 60, 62, 65 | 18:38–39 | "A probe is a fixed word v at distinct nonzero positions. It defines `λ(A)=S(A(0)v)`". Different from the dictionary's probe (linear functional on jets, ch. 3). 17m:251 "fixed probe order" is a third, undetermined use | D | *test configuration `v`*, *the functional `λ_v`*; rename one of the two | (c) |
| (unsymmetrized, symmetric) field reconstruction `H_d(w)`, `A_dw`, `B_dw`; reconstruction identity / comparison | 18:67, 82, 149, 212, 227, 228; 18r:7, 35 | 18:67–69, 84–85 | `H_d(w)=Σ b_α(w)u_α`: the field in `F_d` having the same probe values as the cluster | D | *projection of the cluster onto `F_d`* | (c) |
| measurement | 18:73 | No | Evaluation of `b_α(w)` in the mixed correlations | R | *evaluation* | (c) |
| the mixed table | 18:72 | No | The mixed correlations `S`; `blueprint/notation.md` prescribes "family of Schwinger functions" | R (via notation.md) | *the mixed correlations `S`* | (b) |
| cluster; cluster word; cluster labels | 18:6, 67–78, 123, 135, 140, 222, 247, 249, 404; 18r:65; RG:74 (15) | 18:6 | A group of insertions at mutual distance `O(r)` about a centre `o`. Third meaning of "cluster" in the book (cluster expansion; dictionary: subsequential limit) | R | keep in ch. 18; avoid elsewhere | (c) |
| clearance; clear region | 18:76, 79, 215, 252 | 18:76–79 | Positive distance between the cluster (and its rotations) and the probe points. Same sense as dictionary | R | *separation* | (c) |
| (marked, lattice) replacement; replacement error / estimate; `Z_D` | 18:21, 119, 133, 146, 158, 215, 240, 247, 251; 18r:30; RG:74 | 18:154–157 | `Z_D=M(wv)−M((H_D(τ_{−o}w))(o)v)`: error of replacing the cluster by one field | D | keep, defined | — |
| signed (residual, difference, replacement, local transport, effective activity, density) | 18:129, 158, 174, 248, 255, 413; 18r:21, 26; RG:73 | 18:129–131 | Before absolute values are taken, so that cancellations survive | R | *the difference itself (not its absolute value)* | (c) |
| same-history | 18:130, 146 | No | For the same sequence of RG steps and choices | I | *along the same sequence of block transformations* | (d) |
| nilpotent marker (coefficient); markers; marks | 18:123, 124, 128; 17m:441 | No; RG:37–38 says it in plain words | Marker = auxiliary commuting variable with square zero attached to an insertion; in 18:124 "Markers may merge" and 18:128 "several marks" the word means the insertions themselves | R / I | *source variable `t_i` with `t_i²=0`*; *insertion* | (b) |
| source weights | 18:125; 17m:440 | No; ch11:192 | Weights given to the source variables in the norm | ? here | cite ch. 11 | (b) |
| eligibility condition | 18:127 | No | Not determined here (dictionary: `eligible`) | ? | cite | (b) |
| raw (coefficient estimate, operator error) | 18:226, 231 | No | The bounds of Proposition 18.replacement-input for the unsymmetrised `H_D` | I | *the bounds of Proposition …* | (b) |
| physical inclusions; physical quotient; graded quotient comparison | 18:43, 130, 174; 18r:33 | No; ch14:212 | Inclusions `ι_{d,e}` between the quotient field spaces `F_d`; "physical quotient" = `F_d` | I | *the inclusions `ι_{d,e}` of field spaces*; *the field space `F_d`* | (c) |
| moving field; moving (free) labels | 18:175; 17:97, 370 | No; ch14:238, 250 | A sequence of labels/fields depending on the sequence index, convergent (17:97 "convergent moving free labels") or of size `ε_m` at scale `m` (18:175) | R | *convergent sequences of labels* | (c) |
| normalized-null lemma | 18:183 | ch13:202–240 | Reference by nickname | — | cite by number | (d) |
| uniform in the number of (reflected) copies; replica number; repeated-word identity / bound; repeated copies; full-copy estimates | 17:130; 17w:120; 18:159, 185; 18r:6, 13, 20; 19:52, 91; RG:74 | 18:161–165 | Moment bounds `⟨(Z*Z)^k⟩ ≤ C^{2k}` with `C` independent of `k` | R | *with a constant independent of the number of reflected copies* (one phrase) | (d) |
| exterior (factors, words, separation); interior (difference, seminorms) | 18:251; 18r:9–12, 33, 36 | No; 18-lattice-products:8 | Exterior = the spectator word outside the cluster's cell; interior = supported inside its cell | R | *spectator*; *supported in the cell* | (c) |
| resolution heights; crude and grid constants; grid configurations; low-coordinate errors; omitted degrees | 18r:29, 38–39, 51, 53, 55 | No (defined in 18-lattice-products:223–341) | `θ_−<θ<θ_+`, the ratios of scale logarithms to `T=log(1/r)` | R (via that file) | cite | (d) |
| derivative descent; descending induction | 18r:48, 53 | No | Downward induction on the degree. Different from "trial descent" | R | *downward induction* | (c) |
| subtraction convention / prescription; pair weights `a_h`; selected pair; normal Taylor polynomial | 18:281–322, 352, 358 | 18:290–318 | Explicit and defined | D | keep ("selected pair" → *pair with `a_h≠0`*) | — |
| slots | 18:299 | No | Argument positions | I | *arguments* | (c) |
| contact projection; shell; one-shell estimate; child / parent operators; descendants | 18:257, 404–418 | No | Tree vocabulary for nested collision subsets; "shell" = region where `ρ` is comparable to one value | I | *in the region `ρ≤|…|≤2ρ`*; *operators of the nested subsets* | (c) |
| the source prescription; forest prescription | 18:411, 419 | No | "This explains the source prescription and its proposed sharper local-order bound": the prescription of the formal source. Leakage: the reader has no "source" | R (via notation.md, "unverified sharper source forest prescription") | *a degree-sensitive (forest-type) prescription* | (b) |
| unit removal | 18:430 | No | 19:153 gives the plain wording: "the fact that inserting the identity leaves correlations unchanged" | R | use the 19:153 wording | (d) |

##### 1.4 Assembly, main theorem, reading guide

| Term | Where | Defined? | Meaning | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| phase; space of phases; phase hierarchies; character phase; selected / retained / chosen phase | MT:34, 35, 41, 45, 50, 73–95; RG:47; 19:40, 66–80, 107, 117, 139–144; 17:15, 31, 99, 130, 351; 18 (12) — 46 in all, one sense | ch15:8; MT:32–35 describes it without defining | A character of the commutative compression algebra; equivalently one component `S^ξ` of the integral decomposition | R in MT | acceptable; MT should say "(characters of a commutative algebra, Ch. 15)". `notation.md` warns not to read it as an extremal Gibbs state | (c) |
| polynomial labels; local labels; label basis elements | MT:26; RG:15, 43, 55, 56; 19:29, 36 | MT:26–27 parenthesis gives the grading only; ch2:58 | Dictionary sense (formal invariant polynomial) | D (ch. 2) | keep; RG:55 "local labels" → *polynomial labels* | — |
| penalty parameter for the block transformation; soft-block penalty `b` | MT:12; 19:17 | — | Dictionary "block penalty" | R | one phrase in both places | — |
| admissible (physical) periods | MT:14, 19; 19:20 | No | Not determined in MT; fixed by the schedule (19:18–21) | ? in MT | say "periods in a fixed sequence `R_p→∞`" | (c) |
| normalizations of local observables; "normalized quantum field"; coefficient normalizations | MT:15; RG:13, 16; 19:25 | No | Scale-dependent linear maps on labels (ch. 11) | I | fine for an introduction | — |
| correlation responses | RG:18; 18:182 | No | "equality of all separated correlation responses": the functions `v ↦ S(A v)` | I | *correlations with all other fields* | (c) |
| transporting all coefficients together | RG:17 | No | RG transfer of the coefficient vector | I | *by propagating … through the block steps* | (c) |
| positive action cost | RG:26 | No | Lower bound on the action in large-field regions | I | *a lower bound on the action* | (a) |
| scale schedule; stage; common trajectory | RG:32–36 | No | See §1.1 | — | — | (d) |
| slab operators / insertions / bounds | RG:44; 19:92, 103; 18:270 | ch14:86 | Operators from words supported in a slab `0<x^μ<h` | R (ch. 14) | keep | — |
| hierarchy | 19:60, 67 | No | Family of `n`-point correlations for all `n` | I | standard enough | — |
| fixed-input convergence; bounded approximations; annular estimates; common diagonal extraction; rank bounds; real approximation; moments for separating families; word reconstruction | 19:47–52, 89–105 | No | Pointers by nickname to earlier results | ? here | cite by theorem number | (d) |
| mixed ground space | 19:98–99 | ch15:47 | Zero-energy subspace of the mixture's Hilbert space | I | *space of invariant vectors of the mixed theory* (unsure) | (c) |
| exceptional vacua | 19:107 | No (no other occurrence in `chapters/`) | Invariant vectors other than multiples of `Ω` | I | *further invariant vectors* | (d) |
| low-energy estimate | 19:107, 134 | ch16:424–428 | `μ_ξ{0<E≤u} ≤ Cu²`; 19:135 "bounds spectral mass near zero by a power" | R | keep | — |
| finite-list senses | 19:74 | No | Uniform for each fixed finite list of fields | I | *for every fixed finite list of fields* | (d) |
| ordered tails; ordered period limit; joint ordered limit | 19:38; 17m:338, 365 | No; ch13:143, 213 | Limits taken first in the cutoff, then in the period | I | *in the iterated limit `N→∞`, then `p→∞`* | (d) |
| rate-sensitive tensor cancellation; prescribed-radius squeeze | 19:126–127 | No | Nicknames for 17.coefficient and the monotonicity argument of 17.all-radii | I | cite | (d) |
| "source locations" | RG:82 | — | The formal source of the audits; the only mention of a "source" in the front matter | R | *locations in the formalisation* | (b) |

---

#### 2. Dictionary terms in these chapters

##### 2.1 Same sense (2–3 references each)

- **cost / loss / margin / absorb** (§2.6): 17t:105, 17c:119, 17m:434; see §1.2 for counts.
- **supplies** ("gives"): 17:17, 17t:452, 19:45 (16 occurrences: 17:17, 247; 17t:452; 17w:103; 17c:327; 17m:479; 18:27, 184, 186, 270; 19:36, 45, 48, 103, 131, 160).
- **reads** ("depends on"): 17m:408 "the spectator does not read the varied links".
- **anchor / anchored** (base point of a local function): all 20 occurrences, e.g. 17t:27, 17c:13, 18:174.
- **root** (base point of the block tree): 17c:167, 259, 275, 280, 291, 339.
- **frame** (local gauge transformation / frame variables): 14 of 16 occurrences, e.g. 17c:148, 249; 17m:13.
- **alias; principal / nonprincipal; principal column**: 17c:56–87, 323–335; 17m:215–232. 17c:56 defines the alias as `k_l(p)=(p+2πl)/L`.
- **stationary** (field, branch, jets): 17c:147, 186; 17t:28.
- **forest slice**: 17c:150, 165.
- **straight (average, transport)**: 17c:280; 17m:221, 274.
- **incoming / inherited**: 17m:54, 74; 17t:147; 17c:123.
- **protected**: 17m:74; 17w:72.
- **score**: 17m:73–400 (12).
- **spectator**: 17t:141; 17m:67, 394–418; 18:7, 74, 116, 141, 154, 182, 231; 18r:44; 19:29.
- **collision**: 18:5, 8, 281, 359, 399; MT:89.
- **flux; shell flux**: 17:99 ("Shell integrals"), 341–344; 17w:122.
- **covering number; support exponent**: 17m:331–332, 412–413.
- **width** (§4.2): 17c:106, 143, 164; 17m:35.
- **levels** (§4.2) = scales: §1.1.
- **word**, sense (i): all 12 occurrences (17:34, 44; 18:20, 38, 67, 154, 215; 18r:13, 36; 19:91, 98, 105); definition at ch14:23.
- **regular** (activity, norm, term): 17m:114, 132, 166; 17w:78.
- **history**: see §3.5; closer to `notation.md` ("RG trajectory") than to the dictionary's definition.

##### 2.2 New senses of dictionary words

Detailed in §3: `actual` (one further sense), `row` ("row mass"), `test` (pairing), `label` (entry of a word), `mark` (insertion of a non-observable factor), `window` (two new senses), `source` (five senses), `probe`, `response` (two new), `transport` (RG transfer), `plateau`, `primitive`, `defect`, `leg`, `amplitude` ("alias amplitude" = Fourier coefficient at alias `l`, 17c:61), `mass` (sum of kernel coefficients, 17t:42), `cluster`, `physical` (of the quotient field spaces), `descent`.

##### 2.3 Dictionary items marked inferred or undetermined that these chapters clarify

| Dictionary item | Clarification | Basis |
|---|---|---|
| regularity-stage index `J_m` (§4) | 17w:14–15: "Write `𝓛_j` for the ratio chosen at stage j, so `L_i=𝓛_{J_i}` with `J_i=J(i+1)` in the scale convention of Chapter 10". With ch10:25–29, 129–134: `J(m)` is a nondecreasing map from scales to stages; a stage fixes finitely many orders, weights and constants | R |
| moving comparison fields (§4) | Not used verbatim. "Moving" elsewhere means "depending on the sequence index": 17:97 "convergent moving free labels"; 18:175 "a moving field has coefficient size `ε_m` at scale m"; ch14:250. Supports reading 3:576 as index-dependent comparison fields; still an inference | I |
| matching (§4.2) | 17c:301–303: "Matching replaces `S_stat` by an action with identical Taylor coefficients through field order four" | R |
| envelope (§4.2) | 17m:283: "`p(z)≥1` is a polynomial envelope for the finite Gaussian coordinates" — a majorising function | R |
| inherited loop action (R/I) | 17m:106–107: `Z_ord=𝒞 exp[−βS−𝓛−E_reg]`; 17t:147–150: its Hessian is "a sum with two lattice differences on each leg", so it annihilates constant and affine fields | R |
| protected (I) | 17m:74–76: "On a protected dependence region the incoming measurable product remains fixed under the change of variables" | R |
| nonwrapping / wrapping (I) | No criterion, but a consequence: "a wrapping term has covering number at least `N_per/[10(2B_k+1)]−1`" (17m:331–332) | R (partial) |
| representative (§4.2) | 17c:112 "smooth representative `W_a`"; 17m:32 "plaquette and transported-path representative" | R |
| output (in "output anchors", §4) | "output" consistently means the coarse side of a step or the image index of a map: 17c:352–361 "output link", "coarse output edge"; 17t:302. Supports the dictionary's reading; "output anchors" itself does not occur | I |

Not present in these files: centered log determinant, seeded / unseeded, compulsory, Warnings, likelihood tests, lift, witness, target (grep: no hits).

---

#### 3. Multi-sense words

##### 3.1 `actual` — 41 occurrences (17: 3; 17w: 8; 17t: 10; 17c: 8; 17m: 10; 18: 1; 19: 1)

| Sense | Count | Lines |
|---|---|---|
| of this construction (the specific lattice object, as opposed to a continuum, perturbative or separately chosen one) | 25 | 17:236, 246; 17t:8 (twice), 95, 102, 126, 157, 172, 404, 498; 17w:41, 66, 68, 71, 86, 97, 100, 124; 17c:71, 87; 17m:352, 433; 18:158; 19:47 |
| the nonlinear / gauge-covariant object (dictionary sense 1): actual stationary tangent, actual block average | 6 | 17c:8, 48, 112, 248; 17m:193, 263 |
| the true object versus an idealised model (new): actual conditional insertion vs deterministic evaluation; "an actual exponentially local spectator" vs a finite-range one | 4 | 17m:276, 284, 294, 409 |
| exact / emphatic | 4 | 17t:114; 17c:132, 242; 17m:125 |
| the running value (coupling `β_i` vs reference `b_i`; "actual coupling band") | 2 | 17:84; 17m:312 |

No occurrence of the dictionary senses "at the true background" or "determined by the configuration". Unclassifiable: none, but the 25 in the first row are mostly deletable.

##### 3.2 `row` — 10 occurrences

- Kernel of an operator (dictionary "kernel"/"operator"): 6 — 17w:12 ("curvature-response row constants"); 17c:280 ("a rough root-path row"); 17m:237 ("Let `A_x^{ab}(z)` be the physical row from coarse direction b … to fine direction a at x"), 245, 249, 260.
- Literal matrix row: 4 — 17c:237 (row sum of the recursion matrix), 336 ("Its row mass is L"), 349, 367. "Row mass" = row sum.

##### 3.3 `selected`, `selection`, `selects` — 19; `chosen` — 18

| Sense | Lines |
|---|---|
| the phase `ξ_*` (also "chosen", 17:15; "retained", 19:117) | 17:31, 351; MT:91, 93 |
| fixed by the construction or schedule | 17:11; 17w:21; 17c:135; 18:172; 19:19, 31 |
| subsequence / diagonal choice | 17m:446; 19:38, 112 |
| picked out by a formula | 17t:419, 454 |
| pairs with nonzero weight `a_h` | 18:297, 352, 358 |
| "finite ordinary selections" (17m:92): finite subfamilies of terms of the small-field expansion (ch9:157 "finite selections") | 17m:92 |

`chosen` (17:15, 101, 134, 456; 17w:14, 84; 17t:9; 17c:142, 176, 249; 17m:179, 197; 18:42, 183; 18r:38; 19:58, 111; RG:33): all ordinary.

##### 3.4 `window` — 20 (two are `\input` file names: 17:148, 150)

| Sense | Count | Lines |
|---|---|---|
| interval of radii `r(n,u)` | 6 | 17:129, 131, 146; 17w:2, 6, 7 |
| range of RG scales between `n` and the stopping scale | 10 | 17w:37, 43, 49, 54, 55, 56, 102, 107, 124; 17m:429 |
| "window … requests" | 1 | 17:140 — undetermined (radius window, or the compact separated window of ch14:237) |
| length of an average ("physical averaging window `ma_k`") | 1 | 17m:476 |

The dictionary's sense (localisation neighbourhood `Ω_i`) does not occur.

##### 3.5 `history` — 9

All: the finite sequence of RG steps with its choices (17c:87, 391; 17w:103; 18:130, 146; 19:25, 27, 49). 19:25 "The same finite histories must define the coefficient normalizations of every local insertion". Basis I: none of the files defines it; the dictionary's definition (ratios and averaging orders) is narrower. Undetermined: 17w:71 "the actual free history".

##### 3.6 `source` — 21

| Sense | Count | Lines |
|---|---|---|
| the inserted differentiated-kernel factor `𝒟_Yk` ("full source", "zero-moment source", "score source") | 7 | 17m:68, 155, 391, 400, 412, 443, 459 |
| "regular (local) sources": the local expressions (`div_Haar Y − D𝓛[Y]` etc.) whose Taylor coefficient is extracted | 5 | 17m:193, 265, 291, 303, 307 |
| source variables / weights of ch. 11 | 4 | 17w:12, 78; 18:125; 17m:440 |
| inhomogeneous term of a recursion | 3 | 17c:132, 225, 245 |
| the formal source | 2 | 18:411; RG:82 |

##### 3.7 `mark`, `marked`, `marker` — 33 (17:311 is a file name)

- "marked" = with insertions, as in `notation.md` (27): 17:119, 132; 17w:11, 124; 17c:316, 396; 17m:2, 72, 81, 84, 150, 176, 381, 393, 411; 18:9, 119, 146, 158, 173, 174, 240; 19:48; and with the non-observable factor `𝒟_Yk` as the insertion (new use): 17t:145 ("retained as marked remainders"); 17m:120, 121, 122 ("the marked connected component").
- "mark(s)" = an insertion: 18:128; 17m:441.
- "marker" = nilpotent source variable: 18:123; = insertion: 18:124.
- Symbol `E_mark`: 17m:161.

##### 3.8 `test` — 16

- test function (standard): 12 — 17:69, 70; 18:8, 257, 304, 320, 339 (twice), 364, 405, 414, 415.
- "tested against" = evaluated in correlations with (pairing): 4 — 18:7, 215, 248; 18r:36. `notation.md` asks that the pairing be specified.

None of the dictionary senses (condition, variable, location, indicator) occurs.

##### 3.9 `label` — 14 in prose

- polynomial label (dictionary sense): MT:26; RG:15, 43, 55, 56; 19:29, 36.
- the field entry `A_i` of a word `((x_i,A_i))` (ch14:23–26): 18:140, 141, 205, 222; 18r:61, 64. Whether these are elements of `V_d` or of the quotient `F_d` is not stated (I).
- "moving (free) labels": 17:97, 370 (§2.3).
- `tag`: no occurrence.

##### 3.10 `probe` — 22

- ch. 18 sense (a word `v`, or the functional `S(A(0)v)`): 18 (16), 18r (5).
- 17m:251 "the fixed probe order": undetermined; possibly the order of the polynomials used in the coefficient evaluation.

##### 3.11 `response` — 13

| Sense | Lines |
|---|---|
| linear fine-from-coarse map (the kernels `Ψ_i`, or `W`): "unequal responses", "actual response", "polynomial response", "linear response", "curvature-response" | 17w:11, 60, 67, 68; 17m:193, 202; 19:159 |
| stationary nonlinear fine field | 17m:278 |
| second-order coefficient in the background field: "normalized quadratic response of `Γ_μ`" | 17t:90, 91 |
| "anchored vector response" (17:224): the Hessian kernel of an anchored vector function | 17:224 (I) |
| correlation with other fields ("spectator responses", "correlation responses") | 18:182; RG:18 |

##### 3.12 `transport` — 12; `transfer` — 17

- RG transfer through block steps: 17t:3; 17c:322; 17m:377, 381; 17w:68; 18:130, 174. Same meaning as `transfer` (17:19, 202, 246, 253, 290, 295; 17t:6, 72, 73, 498; 17c:3, 241, 347; 17m:29, 467) and overlapping with `pullback` (17c:51, 77, 91, 208, 304; 17t:157, 159), `propagation` (17:132; 17w:12, 24, 52, 75, 91), `update` (17c:91, 340), `push` (17m:401), `descent`.
- the stationary-field map (dictionary sense): 17t:161; 17m:213, 221.
- parallel transport: 17m:32.
- "derivative-transport argument" (17:128): undetermined pointer to ch. 14.
- 17c:347 "its diagonal transfer is `C_jL⁴L⁻⁵`": here "transfer" is a numerical factor.

##### 3.13 `frame` — 16

- gauge frame (dictionary): 14 — 17c:148, 161, 167, 248, 249, 255, 300, 370, 374, 375; 17m:13, 56; 17t:158, 331.
- left-trivialisation of the group chart: 17t:195.
- "with these same frames" (17w:122): undetermined; perhaps the comparison maps `U_{i,d}` (`notation.md`: frame = "local gauge choice, basis, or scaling map, according to type").

##### 3.14 Others

| Word | Senses and places |
|---|---|
| `table` | 1: 18:72 (the mixed correlations) |
| `phase` | 46, one sense (§1.4) |
| `word` | 12, one sense (§2.1) |
| `reconstruction` (17) | relativistic reconstruction (8): 17:16, 20; 18:32; 19:93, 105, 128, 162; RG:62. Field reconstruction `H_d` (8): 18:67, 82, 149, 212, 227, 228; 18r:7, 35. Fourier inversion (1): 17m:239 |
| `raw` (7 in prose) | before the quotient by the equation of motion: 17:180, 301; 17m:356, 462. Before radial-gauge substitution: 17c:202 (I). For the unsymmetrised reconstruction: 18:226, 231 |
| `physical` (11) | in continuum units: 17m:441, 476; 19:20, 33, 34; MT:14; RG:5, 60. Position-space: 17m:237. Of the quotient field spaces: 18:43, 130 |
| `mixed` (12) | of the mixture over phases: 17:32; 18:15, 72, 185, 207, 221, 277, 340; 19:98. Cross terms: 17c:161. Ordinary: 17m:246 |
| `regular` (11) | small-field local term (dictionary): 17m:114, 115, 132, 166, 193, 290, 303; 17w:78, 93. Non-singular: 17m:221, 227 |
| `ordinary` (13) | small-field (house): 17m:86, 90, 92, 102, 112, 119, 131, 185. Usual: 17m:8, 461, 479; 17t:196, 217 |
| `threshold` | lower bound on `β̂` (17 occurrences, §1.1); small-field threshold `t`: 17c:316; 17m:153, 272, 304, 378, 427; small-`r` threshold: 18:165, 205; 18r:70; cutoff / translation thresholds (= `N` large): 18:165; 18r:20 |
| `strip` | analyticity strip in momentum: 17t:127; 17c:164, 179, 181, 196, 282. Integration strip of ch. 14: 17:122, 128; 17w:118 (not determined here) |
| `mass` | physical mass / mass shell / mass gap; regulator mass `μ`; sum of kernel coefficients: 17t:42, 43; 17c:324, 336, 367; measure of a set: 17:70; 19:135 |
| `contraction` | strict contraction of norms: 17:252, 256; 17t:167, 172; 17c:136, 239, 395; 17m:234; 18:124. Tensor contraction with `R`: 17t:330, 416, 417, 419, 420 |
| `descent` | fine-to-coarse propagation: 17m:444, 461, 469. Downward induction on degree: 18r:48, 53 |
| `contact` | chart identity of ch. 17 (7); coincident-point terms of ch. 18–19 (12 + RG:64) |
| `unit` | identity field: 17:32, 40, 82, 401; 17m:380; 18:109, 382, 430; 19:63. "unit endpoints" (17m:474): undetermined. Others ordinary |
| `kernel` | null space (17:172, 262; 17m:455); block probability kernel (17m:10–54, 391); Fourier/quadratic kernel (17:207; 17t:294; 17m:350, 352); correlation kernel (18:355). "the kernel identities" (17:308) is ambiguous between the block-kernel identity (17.kernel-divergence) and the kernels `K_0,K_a` |
| `column` | ch. 11 coefficient maps: 17w:11; 17m:428 (not determined here). Literal column sum: 17c:332, 336, 337. Column vectors / alias component: 17m:204, 232 |
| `centered` | zero-mean: 17:23, 44, 290, 345, 351, 390, 402, 409; 19:122. Centred difference: 17t:17; 17c:29. "centered degree-four symmetric hypercubic tensors" (17:163): undetermined |
| `root` | block-tree base point (6, §2.1); rooted cluster expansion: 17m:80, 87, 118, 119, 400; "root estimate" (17w:93): undetermined, probably the chessboard-seminorm bound (`notation.md`: "replicated root norm") |
| `price`, `pay`, `budget`, `receipt`, `detector`, `readout`, `tag` | no occurrence in prose |

---

#### 4. Terms these chapters do not determine

| Term | Where | What can be said |
|---|---|---|
| `v_eom` | 17m:385, 386 | Symbol never introduced; presumably `v` of 17:172 |
| strip removal; derivative-transport argument; strip width `M_n^c`; scaled mesh; grid errors | 17:121–129; 17w:118 | Pointers to ch14 (label `comparison`) |
| actual free history | 17w:71 | — |
| protected-path errors; fixed-ratio jet errors; finite incidence costs | 17w:72–73 | Three named error terms of ch. 11 |
| weight restoration; regular-restoration bounds; root estimate; corrected free-subset polynomial; top polynomial extraction `T`; positive partition estimate | 17w:87–100 | Steps of the proof of Proposition 11.n-mark-comparison, referred to by nickname. `notation.md` glosses `T` as "common polynomial extraction" |
| "with these same frames" | 17w:122 | §3.13 |
| fixed probe order | 17m:251 | §3.10 |
| admissible marked conditional integral | 17m:72 | "admissible" in the ch. 9/11 sense |
| normalized large-field majorants | 17m:414 | — |
| vacuum bound `q_n`; terminal norm bounds; accumulated pre-ratio column costs; inverse source-weight bounds; physical mark normalization | 17m:426–441 | Ch. 11 quantities. "terminal" here seems to mean the starting scale `k(n)` of the backward comparison |
| unit endpoints | 17m:474 | Perhaps the boundary terms of a telescoping sum, which are multiples of the identity field |
| finite momentum approximation | 17m:362 | — |
| "the kernel identities" | 17:308 | §3.14 |
| eligibility condition | 18:127 | — |
| anchored marked support bound; signed local transport; graded quotient comparison | 18:174–175 | Nicknames for results of 18-lattice-products.tex / 18-graded-quotient.tex |
| equation calibration floor; fixed-input convergence; restarted histories; bounded approximations; real approximation | 19:30, 47–50, 99 | Nicknames for results of ch. 11–13, 15 |
| why "contact" in "contact identity" | 17t:175 | — |
| `E_stat`, `E_tail`, `E_mark` | 17m:161–165 | Only their bounds are given, not their definitions |

---

#### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| scale index | level, scale, stage (wrongly), step | *scale* for the index, *step* for the map, *stage* only for `j` |
| RG transfer of a function or current | transfer, transport, pullback, propagation, update, push, descent | *transfer* (one word); *pull-back* only for `𝓘` |
| inhomogeneous term | source, forcing | *inhomogeneous term* |
| the identity field | unit, unit field, unit insertion, identity (MT:27; 19:153) | *identity* |
| other fields in a correlation | spectator, exterior factor / word, external positions (18:310) | *spectator* or *remaining insertions* |
| number of reflected copies | copies, reflected copies, replica number, repeated word, full-copy, replicate | one phrase |
| the phase `ξ_*` | chosen (17:15), selected (17:31), retained (19:117) | *the fixed phase `ξ_*`* |
| small-field part of the expansion | ordinary, regular, small-field | *small-field* |
| order in the field | field order, field degree, factor count | one of them; keep distinct from scaling dimension |
| the same Wilson family | same-family, common family, same history, one family, selected family, selected lattice construction | *the same family of measures* |
| `exp((log log β̂_n)²)` | `M_n = M_n^cut` (17:104), `H_n` (17w:29), `H` (17m:138) | one symbol |
| total cluster degree | `w_0` (18:135), `W` (18r:32, 58) | one symbol |
| coincident points | collision, contact, coincident points, diagonal | *coincident points*; *diagonal* for the set |
| unused extra regularity | reserve, margin, spare (17m:316) | *additional* |
| bound | cost, loss, gain, price-type phrases | print the inequality |
| annihilate | kill (17t:291; 17c:66, 113, 335; 17m:350; 18:59, 225), annihilate | *annihilate* / *vanish on* |

---

#### 6. Overloaded symbols noticed

| Symbol | Meanings |
|---|---|
| `W`, `W_a`, `W_s` | 17c:48 "Let W be the actual stationary tangent"; 17c:112 "The actual tangent may be replaced by the smooth representative `W_a`"; but 17m:263–264 "The actual tangent is `W_a=W_s−d_fERW_s`". `notation.md` says the opposite again ("smooth gauge-fixed response `W_s` and the actual forest-coordinate response `W_a`"), and ch5:1234 calls `W_a` "the smooth representative of the actual stationary tangent". Needs one convention. Also `W^{(1)},W^{(0)}` remainder operators (17t:339), `W_{H^b}` dilation (17w:106), `W^rad` (17c:192), `W_2` Wightman function (17:58), exponent `W` (18r:32) |
| `𝒲` | Fourier-type transform (17:51); subtraction operator (18:315) |
| `E_reg` | small-field term in the exponent (17m:107); error term in (17.finite-sigma) (17m:161) |
| `ρ` | trace functional (17:179); spectral measure `ρ_Θ` (17:55); smooth minimum distance (18:283); inner radius (18:247) |
| `H` | Hessian (17:234; 17t:181); `H_n` (17w:29), `H=e^h` (17m:138); orthogonal matrix (17:364); reconstruction `H_d(w)` (18:69); auxiliary degree, giving `H_H` (18:213) |
| `R` | `R(μ)=𝗾(Γ_μ)` (17:231); resolvent (17t:209), also in "`Ra=I`" (17t:106); `R_f,R_0` (17c:249–262); constants `R_{J_i}` (17w:63); inclusion `F_d→F_{d+1}` (18:55); rotation action `R_d(K)` (18:81); radius (18:247); distance (17m:412) |
| `D` | degree bound (17:110); tensor `D_ab` (17:158); `𝒟(μ)` (17:232); operator `D_b` (17t:348); covariance symbols `D_l,D` (17m:203); `𝒟_Yk` (17m:59); derivative |
| `L` | block ratio; `L=T^Max` (17:158); loop term `𝓛` (17m:107); ratio `𝓛_j` (17w:14); `L_{i,q}` (18:94); `L_h` (18:402); `L_*` (17m:433) |
| `Z` | vector (17t:218); `Z_i` (17:328); index `Z=X,D` (17:302); `Z_ord` (17m:92); `Z_γ` (17m:15); `Z_D` (18:155); compressed limit (18r:14); exponent `Z_0` (18r:32) |
| `T` | stress tensor; `T=|k|+μ` (17t:104); `T_b^{(r)}` (17t:349); `Tu=(u,Dz(0)u)` (17c:149); extraction `T` (17w:100); `T_n=(log β̂_n)^{48}` (17m:422); `T_{h,k}` (18:306); exponent variable (18r:42) |
| `t` | small-field threshold (17m:140); right inverse (17:262); momentum parameter (17:216); primitives `t_abc` (17t:72; flagged at 17c:315); distance (17:372); auxiliary degree (18r:31) |
| `q` | bound `q_i` (17:285; flagged at 17:288); primitives `q_a` (17t:62); density `q_γ` (17m:15); `q_n` (17m:439); quotient map (18:58); degree (18:94, 404); number of factors (18r:10); `q_h` (18:400); momentum |
| `b` | block penalty (19:17; 17m:14); reference coupling `b_i` (17:86); window parameter (17w:30); vertices `b,c` (17t:96); functionals `b_α` (18:46); coefficients `b_{y,f}` (17c:255) |
| `S` | correlations; lattice action (17t:180; 17m:107 — `notation.md` reserves `S` for correlations); ratio `a_ℓ/a_n` (17w:64); section `S_0` (18:57); `𝖲` (17:193); `𝒮` (17c:148) |
| `K` | kernels `K_0,K_a` (17t:23); `K_i` (17:293); kinetic symbols `K_f,K_c` (17c:58); rotation (18:81); compact set (18:273); Laplace kernels (17:426) |
| `M` | `M_n` (17:104); block average `M_a` (17t:20); operator `M_b` (17t:347); straight average (17c:277); compression `M(w)` (18:20); bound on `|z_i|` (18:138) |
| `A` | `A_i` (17:292); amplitude `A_l` (17c:61); coefficients (17t:306); kernel `A_x^{ab}` (17m:237); action `𝒜` (17t:137); `𝒜_l` (17m:223); interval length (17t:486); `A_dw` (18:84); spectator (17m:403); fields |
| `χ` | site indicator (17t:346); scalar correction (17m:210); cutoff (18:311); elsewhere the distance `χ(u)` |
| `j` | stage (`C_j`); smoothing order (17m:230, 239, 251, "order less than j"); current coefficient `j_k` (17m:152); current `j_a` (17:389); degree (18:98) |
| `n`, `k` | scale; arity (18:265); number of copies (`k` at 18:162, `n` at 18r:14); Taylor order `k` (18:279) |
| `e` | `e_i` (17:284); norms `e_r` (17c:222); variation `e_{x,c}(u)` (17:205); link |
| `α`, `θ`, `c`, `h`, `u`, `p`, `f`, `B`, `N`, `G`, `V`, `E`, `I`, `J`, `τ`, `λ`, `ν`, `δ`, `η`, `μ`, `ω` | each has three or more meanings across 17–18 (e.g. `τ`: trace field 17:26, `τ_m=log D_m` 17m:423, translation 18:75, path average 17c:256; `X`: tensor 17:159, norm sum 17c:389) |

---

#### 7. The ten most confusing terms

1. **`actual`** — 41 uses, five senses, 25 of them deletable; and the `W` / `W_a` / `W_s` conflict (§6) makes "actual tangent" ambiguous.
2. **`marked` / `mark` / `marker` / `source` / `score`** — five words around one construction (insertions tracked by nilpotent variables), with `source` in five senses; in 17m the "source" is a differentiated kernel, not an observable.
3. **`stage` / `level` / `plateau` / `window` / `stopping`** — the scale bookkeeping of §17.2; `window` means both an interval of radii and a range of scales.
4. **`history` / `same-history` / `same-family`** — never defined in these files, yet 19:25–31 makes it a hypothesis of the main assembly.
5. **`transport` / `transfer` / `pullback` / `propagation` / `response`** — seven words for moving an object through block steps, with `transport` and `response` each also naming the map `W`.
6. **`probe`** — defined in 18:38 with a meaning different from chapter 3; "tested against" for pairing.
7. **`ordinary` / `regular` / `complementary`** — unannounced names for the small-field and large-field parts in 17m:86–132.
8. **`request` / `reserve` / `cost` / `gain` / `pre-ratio`** — the accounting and program vocabulary of 17w and 17m.
9. **`raw` / `physical` (quotient, inclusion) / `reconstruction`** — `reconstruction` means both the Wightman reconstruction and the map `H_d`.
10. **`low moments` / `exterior moments` / `equation direction`** — the key mechanism of the trace argument is named by three undefined phrases, and `v_eom` is never introduced.

Also worth a note for the first pages: **`phase`** (MT) is used without saying that it is a character of a commutative algebra, **`admissible` periods** is undefined in MT, and 18:411 and RG:82 mention "the source".

**Jargon surviving only in labels** (not visible in the PDF): `ch17:current-suppliers`, `ch17:scalar-log-supplier`, `ch17:regulator-input`, `ch17:kernel-score`, `ch18:input`, `ch18:replacement-input`, `ch18:raw-replacement`, `ch19:conditional`, `ch19:conditional-trace` (the statements are no longer conditional), `ch15:selection`, `ch14:stress-line`, `ch11:detector-bound`.

---

#### 8. Not read / not checked

- Read in full: all ten assigned files, the dictionary Part II, and `blueprint/notation.md`.
- **Not read**: `chapters/18-lattice-products.tex` (352 lines) and `chapters/18-graded-quotient.tex` (131 lines). They were not in the assignment and are `\input` from `chapters/13-continuum-fields.tex:402–403`, not from chapter 18; they were only searched for definitions (resolution heights, exterior word, crude/grid exponent, probes).
- `figures/radius-windows.tex` and `figures/pair-subtraction.tex`: captions only.
- Definitions in other chapters (ch. 9, 10, 11, 13, 14, 15, 16) were located by `grep` and read a few lines at a time; entries marked "via ch. …" rest on those excerpts, not on a full reading.
- Multi-sense classifications were made from a full reading plus `grep` line lists. The `actual`, `row`, `window`, `source`, `test`, `probe`, `transport`, `frame`, `reconstruction`, `physical` counts add up to the grep totals; borderline assignments (especially "of this construction" versus "emphatic" for `actual`) could move by two or three.
- No Lean source was consulted. No proposed equivalent was checked against the literature. §6 is a list of what was noticed, not a complete symbol audit.
- Typographical slips noticed in passing: "an coupling-threshold-controlled" (17w:76); "the difference … are bounded" (17m:284–285).

### VI.B Independent audit

*Original title: Audit D: Part VI.A (chapters 17–19, main theorem, reading guide)*

> **Status.** Independent check of Part VI.A by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in Part I, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only check against the worktree `manuscript/HumanizeYM_v3/` (HEAD `16317fd1`). No repository file was edited.

**Overall verdict.** The survey's line references and counts are mostly accurate (three or four wrong lines, a few counts off by one or two). Its main weakness is the "undetermined" list: at least twelve terms it calls undetermined or inferred are settled elsewhere under `chapters/`, mostly in chapter 11. It also contains one wrong meaning (`equation calibration floor`), one claimed inconsistency that does not exist (`W`, `W_a`, `W_s`), two merged senses that the text keeps apart (`response`; `ordinary` against `regular`), and a few "terms" that are the survey's own coinages.

Method: I read all ten assigned files in full, blanked `\label`, `\ref`, `\eqref`, `\pageref`, `\input`, `\cite` arguments, and re-ran `grep -n` for every multi-sense word. Cross-chapter claims were checked by reading the cited lines with context. File abbreviations are the survey's; `11`, `11E`, `11R`, `14lc`, `18lp`, `18gq` are the chapter 11, 14 and 18 fragment files.

---

#### Definite errors

1. **`equation calibration floor` (§1.1, 19:30): wrong meaning.** The survey says "A lower bound on `β̂_N`". The cited passage is a lower bound on the block ratio `L`: 11E:25–29 "`L^{1/8} ≥ max_{d≤j} 2(1+C_j)Q_{dj}δ_d^{-1}`" (label `ch11:calibration-floor`) "in the stage-`j` block floor". The `β̂_N` condition at 11E:30 is a separate "adjacent stage condition on the starting scale". The proposed equivalent should be "the lower bound on the block ratio in (11.calibration-floor)".

2. **`W` / `W_a` / `W_s` "inconsistency" (§1.2 row "stationary tangent", §6, §7 item 1): there is none in the chapters.**
   - 5:1084 defines `W_s` as "the straight-average transport"; 5:1108 defines `W_a=W_s-d_{0,f}ERW_s`.
   - 5:1151 "The smooth representative `W_a` and the forest representative `W_F` are distinct"; 7:574 "The actual stationary tangent is `W_a` … its forest representative is `W_F`".
   - So 17c:112 ("may be replaced by the smooth representative `W_a`") and 17m:263 ("The actual tangent is `W_a=W_s−d_fERW_s`") agree: `W_a` is the actual tangent in its smooth representative.
   - `notation.md`:242 agrees with 17m:263; the survey's "says the opposite again" is wrong. Only its word "forest-coordinate" conflicts with 5:1151.

3. **`ordinary` and `regular` are not synonyms (§5 cluster "small-field part", §7 item 7; copied into overview §5).** 17m:106–115: "`Z_ord=𝒞 exp[−βS−𝓛−E_reg]`" and "The regular term is estimated using its already proved differentiated regular norm". `ordinary` is the whole small-field part; `regular` is one term of it, the remainder `E_reg`. Replacing both by "small-field" changes 17m:114 and 17w:78.

4. **`response`, first sense (§3.11): two different operators merged.** 17w:11, 60, 67, 68 concern the curvature response `Ψ_i` (17w:62 displays `Ψ_{n-1}⋯Ψ_ℓ`; 11:647 "`J=H_{0,f}^{-1}TH_{0,c}` is the curvature response"; 11:1729 "the actual installed curvature response `Ψ_i`"). 17m:193, 202 and 19:159 concern the link tangent `W` (11:642 "the actual stationary forest response `W`"). These need separate rows.

5. **Survey coinages listed as house terms.** These phrases do not occur in the text:
   - "component average `K_a`" and "difference primitive `K_a^t`" (§1.2). The text has "finite Laurent polynomial `K_a^t`" (17t:34); "difference-primitive" (17c:309) refers to `q_a`, `t_abc`.
   - "trace stability amplification `e_i`" and "stable functional" (§1.2). The second is only the label `ch17:stable-functional`; "amplification" occurs at 17w:78–79 for the product (17.window-product).

6. **`replicate`, "ch11:780".** That line is `\label{ch11:replicated}`. The verb does not occur in chapter 11 prose (it does at 13ba:283). The supporting text is 11:815–817 "A reflected tiling at scale `a_m`, stopped at `a_k` … Taking the number-of-cells root".

7. **§6, `τ`: "`τ_m=log D_m` (17m:423)".** 17m:423 reads "`τ_{k(n)}−τ_n ≥ T_n`"; there is no `log D_m`. `τ` is defined at 10:145–146: "`τ_{m+1}=τ_m+log L_m`, `a_m=e^{−τ_m}`". This also settles what "crosses" in "first crossing" (see below).

---

#### Basis codes that overstate or understate

**Overstated (given D or R, really I or weaker).**
- `level`, `k_i` (R): `k_i=k(n_i)` is never written. 17:85–87 only names "insertion level `k_i`"; the identification rests on 17:108, 139–142 and 17m:386, 420.
- `request` (R): no sentence defines it; the meaning is read from usage. I.
- `field order` (D, "17c:222"): that line defines `e_r`, not the term. R.
- `exterior` / `interior` (R): 18r:9–11 uses "interior lattice difference", "exterior factors", "interior seminorms" undefined; 18lp:154, 207, 238 use them, also undefined. I.
- `resolution heights` (R "via that file", "defined in 18lp:223–341"): the phrase occurs only at 18r:54–55 and nowhere in 18lp. That two of `θ_−<θ<θ_+` are meant is an inference. Since `Z_0=Wθ_++4n_cl(θ_+−θ)` (18r:32) must tend to `W`, the two are `θ` and `θ_+`, not `θ_−`.
- `anchor average`, "mass" (D/R) is fine; the two invented names in the same row are not (see error 5).

**Understated (given I or ?, the text settles it).** See the section "Terms the survey calls undetermined that the text settles". In brief: `history`, `conserved line`, `ordered tails`, `replicate`, `physical inclusions`, `spectator responses`, `vacuum bound q_n`, `root estimate`, `weight restoration`, `top polynomial extraction`, `strip removal`, `derivative-transport argument`, `centered … tensors`, `admissible periods`, `restarted representation`, `exceptional vacua`.

---

#### Sense misassignments (with my per-sense counts)

**`actual` — 41 (grep agrees).**
| Sense | Mine | Survey |
|---|---|---|
| of this construction | 23–24 | 25 |
| the tangent `W_a` / gauge-covariant block average | 7 | 6 |
| true object against an idealised or substituted one | 4–5 | 4 |
| emphatic | 4 | 4 |
| running coupling | 2 | 2 |
- 17t:157 "the actual stationary pullback of the current defect, with the gauge-covariant block average frame correction" belongs with the tangent sense (it is contrasted with "the usual smooth transport bound", 17t:161), not "of this construction".
- 17w:68 "product of the subsequent actual responses. It uses no replacement by a common stage's quadratic form" is true-against-substituted; borderline.
- No missed sense. Counts are right to within two.

**`row` — 10 (agrees).** The split into "kernel of an operator" (6) and "literal matrix row" (4) should be merged. Every use is a row of a matrix or kernel at a fixed output index:
- `Ψ` row sums: 17w:12 (11:1735 "`sup_x Σ_y|Q_{i,w}(x,y)| ≤ R L_i^{−|w|−2}`", the `R_{J_i}` of 17w:63).
- `M_{ef}`: 17c:336, 349, 367. `R_0`: 17c:280. `W_s`: 17m:237, 245, 249, 260. The 3×3 recursion matrix: 17c:237.
- "Kernel of a translation-invariant operator" (overview §2.2) is wrong for 17m:237: "`A_x^{ab}(z)` … from coarse direction `b` at `⌊x/L⌋+z` to fine direction `a` at `x`" depends on `x`.

**`selected` / `selection` / `selects` — 19 (agrees); all six sense assignments confirmed.** `chosen` — 18 (agrees). "All ordinary" contradicts the survey's own table: 17:15 "the phase `ξ_*` chosen in Section…" is the phase sense.

**`test` — 16 (agrees): 12 test function, 4 pairing.** Confirmed.

**`label` — 15 in prose, not 14** (the survey's own lists sum to 15). Missed sense: at 17:97 and 17:370 "moving (free) labels" are elements of the free Maxwell spaces `𝓜_d^Max`. 17:81 "`U_{i,d}:𝓜_d^Max→F_d`"; 17:320 "`β_i r_i^4U_{i,4}^{-1}Θ → −κ_G𝒪`". So three senses: polynomial label (7; 19:29 is uncertain), field entry of a word (6), free Maxwell field (2).

**`tag` — 0.** Confirmed.

**`mark` / `marked` / `marker` — 32 in prose plus the file name at 17:311 (agrees with 33).** The "new use" (the inserted factor is `𝒟_Yk`, not an observable) is not confined to 17t:145 and 17m:120–122. It covers most of 17m: 72 "an admissible marked conditional integral. Its extra factor is a finite sum of smooth local kernel scores", and 81, 84, 150, 176, 381, 393, 411. Judgement on where to draw the line, not an error.

**`window` — 18 in prose plus two file names (agrees with 20).**
| Sense | Mine | Survey |
|---|---|---|
| interval of radii | 4: 17:129, 131, 146; 17w:6 | 6 |
| range of scales | 11–12: 17w:2, (7), 37, 43, 49, 54, 55, 56, 102, 107, 124; 17m:429 | 10 |
| compact set of separated configurations | 1: 17:140 | 0 (called undetermined) |
| length of an average | 1: 17m:476 | 1 |
- 17w:2 "Comparison windows crossing changes of stage" is assigned to radii, while the same phrase at 17w:124 is assigned to scales. Both are scales.
- 17w:7 "requiring every window to lie inside a plateau" is ambiguous (a plateau is a set of scales).
- 17:140 "Diagonalize finite degree, arity, window and derivative requests" parallels 14:225–226 "explicitly diagonalizing arity, degree, compact windows and errors". This is the chapter 14 sense, which the survey says is absent from these chapters.

**`history` — 9 (agrees).** The sense is right, but "none of the files defines it" overlooks 11:18–19: "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations". 17w:103 and 19:49 are the restarted history of 11:736–741.

**`source` — 21 (agrees).** Five senses confirmed, with one unsupported assignment: 17w:12 "polynomial-source propagation constants" and 17w:78 "regular and large-field source recurrences" are put under "source variables / weights of ch. 11". Neither phrase occurs anywhere else in `chapters/`; they should be listed as undetermined. That leaves 2 (18:125; 17m:440) in that sense.

**`response` — 13 (agrees).** See error 4. My split: `W` 3; curvature response `Ψ_i` 4; nonlinear stationary field 1 (17m:278); quadratic coefficient of `Γ_μ` 2; "anchored vector response" 1 (I); correlation with spectators 2. The last (18:182; RG:18) is the "one-slot response" defined at 13:120–122, not a new sense.

**`transport` — 13, not 12.** RG:17 "transporting all coefficients together" is in §1.4 but missing from §3.12. 17:128 "derivative-transport argument" is not undetermined (see below). 17w:68 "each conditional covariance is transported by the product of the subsequent actual responses" is conjugation by linear maps; assigning it to "RG transfer" is a stretch.

**`transfer` — 15 in prose, not 17.** The survey's list has 15; a sixteenth hit, 17c:2, is a TeX comment.

**`probe` — 22 (agrees).** 17m:251 "fixed probe order" is probably not a third sense. Context: 17m:240 "every vector polynomial `p` of degree less than `j`", 17m:252 "tuples of potential polynomials". This matches chapter 3 (3:939 "the scalar order-`j` probes"). Inference, not settled.

**Other counts.** `stage` 23, `phase` 46, `word` 12, `anchor` 20, `supplies` 16, `raw` 7, `physical` 11, `regular` 11, `ordinary` 13 all agree. `mixed` is 11, not 12. `leg` is 15, not 16. `coupling threshold` is 19, not 17 (two occurrences are split across lines: 17m:142–143, 346–347).

---

#### Wrong line references and misquotations

- `leg`, "17c:373": the line reads "gauge is legitimate for this covariant displacement". Substring artefact.
- `gain`, "17c:375": the line reads "frame derivatives again occur only below the field-order diagonal". Substring artefact. 18:256 "residual gain `(ρ/R)^{D+1}`" is missing from the list.
- `shooting`, "ch10:210": that line is `\label{ch10:shooting}`. The word is in prose at 10:273 and 10:818; the section title (10:209) is "Tuning a finite history to the coarse endpoint".
- `replicate`, "ch11:780": a label line (error 6).
- `stopping levels`, "17w:101": the words are on 17w:102.
- Overview §2.11, probe "(18:36–38 ✓)": the definition is at 18:38–39; 18:36 is a label.
- No misquotation found. Every quotation I checked is verbatim up to marked ellipses and TeX markup (about 40 checked, including all those in §§1.1–1.4, 2.3, 3.1–3.6).

---

#### Omitted terms

House terms in these files that the survey does not list:

- **`graph`**: 18:124 "the one-insertion graph contraction" (cf. 11:347 "The one-insertion graph estimates", 11:911 "the graph of normalized local insertions"). 17m:444 "descending graph" is listed, but "graph" is not glossed.
- **`Diagonalize … requests`** (17:139): "take a diagonal subsequence over", an unusual use; also "diagonal radius selection" (17m:446).
- **`empty coefficient` / `empty density` / `denominator`**: 17w:88 "the empty coefficient, and hence the denominator, is unchanged"; 17m:418 "Every spectator subset uses the same empty density". This is the coefficient of the empty source monomial, i.e. the density without insertions (11:604, 773, 2101).
- **`squarefree polynomial`** (17w:86): polynomial in the nilpotent source variables (11:23 "squarefree source algebra").
- **`cross-modes`** (17m:401 "all pushed spectator cross-modes"): coined; `notation.md` has "higher modes".
- **`microscopic sections`** (19:28); cf. 11E:36 "normalized microscopic section".
- **`correlation-null fields`** (18:40) and **`field-null spaces`** (19:68).
- **`endpoint constants` / `endpoint factors`** (17w:23, 26); only "endpoint error" is listed.
- **`bottom stage`, `middle` and `output` stopping levels, `top` extraction** (17w:97–102): positional words for the comparison window. "Bottom stage" may use `stage` for a level, which would be the only such use in these files (I could not determine this).
- **`division`**: "analytic division argument" (17c:99), "homotopy divisions" (17c:102), "Coordinatewise Taylor division" (17c:104), "Two-leg curl division" (17c:346).
- **`box-filter identity`** (17c:365; 11:1731).
- **`units` of the support exponent**: "Retaining two units of the exponential support exponent" (17m:332, 413).
- **`admissible` (path) action** (17t:84; 17c:12): only "admissible periods" and "admissible marked conditional integral" are listed.
- **`attach`** (17m:125 "Attach this condition to its actual dependence support").
- **`tail`** as a multi-sense word: for all large indices ("fixed-stage tail" 17c:135; "ordered tails" 19:38) against the far part of a kernel ("exponential row tail" 17m:260; "crop tail" 17m:313).
- **`compression`** (18:19–20; 18r:14, 36; 19:98): standard operator theory, but used as a noun for an element; borderline.
- **`twelve-plane coefficient convention`** (17t:120; 17:236).

---

#### Questionable equivalents

- **`ordinary`, `regular` → "small-field"**: changes the meaning (error 3). Keep "small-field part" for `ordinary`; for `regular` say "the remainder `E_reg`" or "small-field remainder".
- **`primitive` → "discrete potential"**: I do not know "discrete potential" as a standard term for `q` with `tr J=Σ_aδ_aq_a`. "Primitive" (antiderivative for the forward difference) is closer to standard; better to state the identity.
- **`current defect` → "conservation error of the lattice current"**: `𝓔_b=Σ_a∇_aJ_{ab}−D𝖲[Y_b]` (17:195) is the failure of the Ward identity, i.e. conservation up to the equation-of-motion term. "Defect of the lattice Ward identity" is safer.
- **`field reconstruction H_d(w)` → "projection of the cluster onto `F_d`"**: a cluster word is not an element of a space containing `F_d`. More exact: "the field in `F_d` with the same values of the functionals `b_α`, `|α|≤d`".
- **`contact identity` → "chart identity for `div_Haar Y`"**: not standard either; keep the proposition number.
- **`exceptional vacua` → "further invariant vectors"**: loses the measure-theoretic point (see below). Use "non-uniqueness of the vacuum on the `ν`-null set of phases".
- **`mixed ground space` → "space of invariant vectors of the mixed theory"**: the text's own phrase is "zero-energy subspace of its reflection Hilbert space" (15:7); use that.
- **`row` → "kernel"**: in chapter 17 "row" is a literal matrix row; "row of the kernel" or "for fixed output index" is right, "kernel" alone is not.
- **`replicate` → "apply the chessboard estimate at the scale…"**: acceptable given 11:815–822, but that text should be cited.
- **`stage` → "parameter regime `j`"**: not standard; "stage `j`" defined once is better (the survey's first option).
- Fine as proposed, to my knowledge standard: "inhomogeneous term", "annihilate", "vertices", "truncation to a ball", "downward induction", "arguments" for slots, "identity" for unit. I did not check any of these against the literature.

---

#### Overview claims (errors / confirmed)

**Errors or inconsistencies.**
- **§2.1 table, column ch. 17–19.** The numbers 25 / 4 / 6 / 2 / 4 sum to 41 and reproduce the survey. But the "4" is entered in the row "nonlinear / at the non-flat background, against flat or linearised", whereas the survey's four lines (17m:276, 284, 294, 409) are "true object versus an idealised model". 17m:409 "an actual exponentially local spectator" has nothing to do with nonlinearity. The row label does not fit.
- **§2.2**, "kernel of a translation-invariant operator … 17w:12; 17c:280; 17m:237–260": not translation-invariant (see `row` above).
- **§2.7**, row "stationary fine field / the map `W` … 17w, 17m; 19:159": the 17w uses are the curvature response `Ψ_i` and belong in the next row (11:647, 1729). Row "correlation with other fields … 18:182; RG:18" duplicates the row "one-slot response … (defined 13:120)". 17:224 "anchored vector response" is missing. The heading says ten senses; the table has nine rows.
- **§2.3**: 17m:446, 19:38 and 19:112 (subsequence choice) and 17t:419, 454 (picked out by a formula) are not represented.
- **§2.4**: 18r:36 is missing from the pairing row.
- **§2.9**: 17:140 belongs in the row "compact set of separated configurations".
- **§2.11**: line reference 18:36–38 should be 18:38–39.
- **§4, chapters 17–19.** Of the seven named terms, five are settled in other chapters: `strip removal`, `derivative-transport argument`, `weight restoration`, `root estimate`, `exceptional vacua`. The overview's own §2.8 cites 14:229 for "conjugation by comparison maps", which is the derivative-transport proposition. `fixed probe order` and `unit endpoints` remain open.
- **§5**, "small-field part: ordinary, regular, small-field": not synonyms (error 3).
- **§6**: no cited line lies in my files. Further sentences in my files that look damaged by replacement or do not parse:
  - 17m:303 "There are no invariant constant spacetime-vector or terms linear in the `𝔤`-valued field." (a noun is missing).
  - 17t:159–160 "the order-two pullback must annihilate its affine--affine and affine--quadratic polynomial moment conditions" (one annihilates moments, not conditions).
  - 17c:359–360 "Only a bounded number of coarse output edges are within the gauge-covariant block average and averaging patches".
  - 17t:157–158 "with the gauge-covariant block average frame correction"; 17c:161 "all mixed gauge-covariant block average and frame terms included" (noun piles after replacement).
  - 19:152–154 "Positivity at contacts, contact Ward identities, the fact that inserting the identity leaves correlations unchanged, and uniqueness of contact terms require…" (18:430 still has "unit removal" in the same list).
  - 17m:284–285 "the difference … are bounded"; 17w:76 "an coupling-threshold-controlled"; 17m:144 "let `f` be curvature-factor count".

**Confirmed.**
- §1: chapters 17–19 reuse `window`, `source`, `probe`, `response`, `transport`; front matter uses `phase` without "character" (MT:32–35) and "admissible periods" without definition (MT:14, 19).
- §1: none of `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund`, `readout`, `detector`, `share`, `spent`, `excess` occurs in the prose of my ten files.
- §2.3: the phase row (17:15, 31, 351; 19:117; MT:91, 93) and the pair-weight row (18:297, 352, 358).
- §2.5: polynomial labels in MT, RG, ch. 19; 18:140–222 "probably" fields.
- §2.6: `marker` 18:123 / 18:124; the inserted factor in 17m is a differentiated block kernel; "the source" at 18:411 and RG:82 (supported by `notation.md`:206 "the unverified sharper source forest prescription" and 14:186 "the source construction uses").
- §2.9: rows for 17w, 17m:429, 17m:476.
- §3: 17w:14 for `J(m)`; 17m:283 for `envelope`; 17c:301 for `matching`.
- §4: `v_eom` occurs only at 17m:385–386 and is never introduced.
- §7: `ch17:current-suppliers` (17t:4), `ch18:raw-replacement` (18r:3), `ch19:conditional` (19:57).

---

#### Terms the survey calls undetermined that the text settles

| Term (survey place) | Settled by | Meaning |
|---|---|---|
| `history` (§3.5, I) | 11:18–19 | "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations" |
| `restarted representation`, `B_n` (§1.1, ?) | 11:736–741; 11R:18 | History with the inverse coupling held constant below a comparison level; "The new representation at level `i` has radius `B_i=b(x_i)^2`" |
| `root estimate` (§3.14, §4) | 11:817–822; 11:2072–2079 | "Taking the number-of-cells root … `𝓡_m` denotes that chessboard seminorm"; the bound is (11.n-mark-root) "`‖R_I‖_root ≤ H^{−1/(16n)}`", with "cell side … at most `a_kH^{b_j+5}`", matching 17w:96 |
| `weight restoration`, `regular-restoration bounds` (§4) | 11:1374–1375, 1436, 1471, 2131 | Named lemmas "Regular weight restoration" and "Large-field weight restoration": passage to the larger source weight; "Regular weight restoration therefore gives `H^{-1}`" |
| `top polynomial extraction T` (§4) | 11:1142 ff.; 11:2085–2088 | "Construct `T` at the top level `k` from the actual insertion and its original same-insertion covariance"; "top" is the top level of the comparison window |
| `vacuum bound q_n`, `positive-density estimate` (§1.2, §4) | 11:801–812, 819 | `q` is the per-site exponent in the lower bound for the partition function ("positivity gives `Z ≥ …`"); `(a_m/a_k)^4q_k` in (11.root-bound) is the `L_*^4B_n^8q_n` of 17m:436 |
| `replicate` (§1.1, I) | 11:815–817 | Take a reflected tiling at scale `a_m` |
| `strip removal`, `strip width`, `scaled mesh`, `grid errors` (§3.14, §4) | 14:174–200 | "coordinate-equality strips of width `4δ_k`", `δ_k=M_k^c`; grid spacing `s_k=M_k^{−α_0}`; `ε_k` on the grid; the strips "have volume `O(δ_k)`" |
| `derivative-transport argument` (§3.12, §4) | 14:229–238 | Proposition "Derivative transport and smooth comparison": `r_kU_{k,d+1}^{-1}∂_aU_{k,d} → ∂_a^0` |
| `centered … tensors` at 17:163 (§3.14) | 3:580–584; 14:261–264 | "Centered means that each component has zero expectation"; the same sense as the other uses |
| `conserved line` (§1.2, I) | 3:591–596 | Proposition "Conserved tensor line": `{J∈𝒯_{≤4}: div J=0}=ℝT^Max` |
| `ordered tails` (§1.4, I) | 13:213–214 | "the filter is generated by ordered tails: `p=P(k)` with `k≥k_0`, and `N=n(j)` with `j≥j_0(k)`" |
| `admissible periods` (§1.4, ? in MT) | 10:193–197 | `R_p=4(M+p+1)`, `p≥0`, with `M` large enough for the first plateau |
| `exceptional vacua` (§1.4, I, "no other occurrence") | 16:379–381; 15:324–328 | "the zero-energy space is a line for almost every phase … To remove the exceptional set requires a bound uniform in `ξ`". "Exceptional" refers to the null set of phases, not to a kind of vector |
| `physical inclusions` (§1.3, I) | 14:210–212 | "`i_d` … for the free inclusion, `j_d` for the physical inclusion": physical means interacting, against free |
| `spectator responses` (§3.11, I) | 13:120–122 | "one-slot response `L_{v,f}(c)=∫f(x_0,x)S_{n+1}(c(x_0),v(x))`" |
| "what crosses" in `first crossing` (§1.1) | 10:145–146; 17m:422–425, 433 | `τ_m=log(1/a_m)`; "`τ_{k(n)}−τ_n ≥ T_n` is the first crossing"; "`B_n^2 ≤ a_m/a_n ≤ L_*B_n^2`" |
| `window … requests` at 17:140 (§3.4) | 14:225–226 | "diagonalizing arity, degree, compact windows and errors": strongly indicated, not explicit |
| "the kernel identities" at 17:308 (§3.14, §4) | 17m:10–66, 396–398 | "The next section proves them using the kernel identities": the next section is 17m, on the block kernel `k`. Likely, not explicit |

Partly settled: `corrected free-subset polynomial` (11:2064–2071: free moments `G_I`, corrected coefficients `R_I`); `eligibility condition` (8:294–295 and 9:94 use it without stating the rule); `finite incidence costs` ("incidence" bounds at 11:208–342).

Still undetermined, as the survey says: `v_eom`; `actual free history`; `protected-path errors`; `fixed-ratio jet errors`; `with these same frames`; `unit endpoints`; `normalized large-field majorants`; `finite momentum approximation`; `E_stat`, `E_tail`, `E_mark`; `polynomial-source propagation constants`; `source recurrences`; why "contact" in "contact identity".

---

#### Confirmed rows

Meaning, line references and basis as stated (apart from the points above):

- **§1.1**: stage; plateau; level (except `k_i`); radius window; stop backwards / overshoot; pre-ratio / post-ratio / fixed-ratio; coupling threshold; schedule; floor (17t:107); shooting (meaning); current depth; restart (pointer).
- **§1.2**: current defect (definition); "order at least four"; low moments (both senses); stationary substitution; stationary tangent (meaning); anchor average `K_0` and mass; primitive `q_a`, `t_abc` (meaning); displacement; leg; channel; diagonal / below the diagonal; source / forcing; completed; covariant completion; infinitesimal gauge insertion and background insertions; regulated current / regulator; contact identity; chart velocity; action-gradient terms; Haar coefficient and coefficient functionals; trace functional and raw divergence; equation direction; same-family; density identity; density-valued insertion; complementary; ordinary; threshold coordinates; crop; jet menu; coefficient evaluation; reserve; cost / gain / loss; trial descent.
- **§1.3**: probe; field reconstruction (definition); measurement; mixed table; cluster; clearance; replacement and `Z_D`; signed; same-history; nilpotent marker; source weights; raw; moving field; normalized-null lemma; uniform in the number of copies; derivative descent; subtraction convention; slots; contact projection / shell; source prescription; unit removal.
- **§1.4**: phase; polynomial labels; penalty parameter; normalizations; correlation responses; transporting; positive action cost; slab; hierarchy; nickname pointers 19:47–52, 89–105; low-energy estimate; finite-list senses; rate-sensitive cancellation / squeeze; source locations.
- **§2.2**: amplitude, mass, and the list of new senses (subject to the §3 corrections).
- **§2.3**: all nine rows.
- **§4**: the rows listed above as still undetermined.
- **§5**: the three symbol rows (`M_n`/`H_n`/`H`; `w_0`/`W`; `spare`) and the `kill` list.

---

#### Not checked

- **§6 (overloaded symbols)**: only the `W` row and the `τ` entry were checked (both wrong); the other rows were not.
- **§2.1 (same-sense list)**: spot-checked by count and by about half the cited lines; no errors found, not exhaustive.
- **§5**: checked only for meaning-changing merges and for the rows with line references.
- **Figures** (`figures/radius-windows.tex`, `figures/pair-subtraction.tex`): not read.
- **Other chapters**: read only at the cited passages, a few lines each. `18-lattice-products.tex` and `18-graded-quotient.tex` were searched, not read in full.
- **`blueprint/notation.md`**: only the lines the survey quotes; all were found as quoted.
- **Literature**: no proposed equivalent was checked against it; my judgements on what is standard are from my own knowledge.
- **Overview**: only statements citing my ten files.
- **One mathematical point noticed, not pursued**: 17m:438 has "`B_n=O((log β̂_n)^2)`", whereas 11R:15–18 gives `B_i=b(x_i)^2` with `b(x)=⌈(log x)^2⌉`. I could not determine whether these are the same `B`.
