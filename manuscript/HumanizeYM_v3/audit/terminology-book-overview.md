# House terminology across the whole manuscript: overview

**Status:** draft audit. **Scope:** all chapter files under `chapters/`, plus `main-theorem.tex` and `reading-guide.tex`. Line numbers are those of upstream commit `7bec3925`; the sentence repairs made on this branch (section 6) keep every line number.

This note is the cross-chapter synthesis. The detailed entries are in:

| Chapters | Dictionary or survey | Independent check |
|---|---|---|
| 3–6 | [`terminology-ch03-06.md`](terminology-ch03-06.md) | applied in the file (its section 9) |
| 1, 2, 7, 8, 9 | [`terminology-surveys/ch01-02-07-09.md`](terminology-surveys/ch01-02-07-09.md) | [`audit-ch01-02-07-09.md`](terminology-surveys/audit-ch01-02-07-09.md) |
| 10, 11 | [`terminology-surveys/ch10-11.md`](terminology-surveys/ch10-11.md) | [`audit-ch10-11.md`](terminology-surveys/audit-ch10-11.md) |
| 12–16 (with the two `18-` files input from chapter 13) | [`terminology-surveys/ch12-16.md`](terminology-surveys/ch12-16.md) | [`audit-ch12-16.md`](terminology-surveys/audit-ch12-16.md) |
| 17–19, main theorem, reading guide | [`terminology-surveys/ch17-19.md`](terminology-surveys/ch17-19.md) | [`audit-ch17-19.md`](terminology-surveys/audit-ch17-19.md) |

The four later surveys are kept as returned. **Where a survey and its audit disagree, read the audit**; this overview already incorporates the audits' corrections.

References are `chapter:line`; suffixes distinguish included files as in the surveys (`11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, `15sp`, `17w`, `17t`, `17c`, `17m`, `18r`, `9s`, `2e`; `MT`, `RG` for the two front-matter files). Entries marked ✓ were reread by the coordinating agent; the rest rests on a survey and its audit.

---

## 1. The picture by part of the book

- **Chapters 1, 2, 8** are nearly free of house vocabulary.
- **Chapters 3–6** carry the "row / actual / selected / test / tag" vocabulary analysed in the chapter 3–6 dictionary.
- **Chapters 7 and 9** continue it and add "response", "insertion" and "weight" in several senses each, with an accounting layer of `cost`, `gain`, `loss`, `reserve`, `share`, `fits`.
- **Chapters 10–11** have been through a translation pass: `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector` no longer occur in prose. What remains is a scheduling vocabulary (stage, plateau, floor, delay, request, window), many undefined nouns for the objects of the expansion with insertions (principal, incidence, graph, column, trial, lift, mass), and sentences damaged by mechanical replacement (section 6).
- **Chapters 12–16** use "graph" for a map from coefficients to remainders, "column" for a coefficient vector, "heat" for the semigroup `e^{-tH}`, and let "label" drift from a polynomial to a field.
- **Chapters 17–19** reuse "window", "source", "probe", "response" and "transport" in further senses, and refer to earlier results by nickname.
- **The front matter** uses "phase" without saying it is a character of a commutative algebra, and "admissible periods" without definition (MT:12–15 ✓); the periods are `R_p = 4(M+p+1)` (10:193–197 ✓).

The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund` do not occur in the prose of any chapter; all four audits confirmed this for their files. The accounting vocabulary that is present is `cost` (over 100 uses outside chapters 3–6), `reserve`, `gain`, `loss`, `margin`, `excess`, `share`, `spent`, `request`, `fits`.

---

## 2. Words with several meanings, across the book

Counts are occurrences in prose. Those for chapters 7–19 were recounted by the audits and agree with the surveys to within a few; the split between neighbouring senses is a judgement in many cases.

### 2.1 `actual` (about 370 uses in the book)

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

### 2.2 `row`

| Sense | Where |
|---|---|
| component of the stacked vector whose half-square is the action | ch. 6 (about 68); 7:352, 976–993, 1168; 9:544, 568, 835, 840; 10:356; 11:668, 710; 11R:101–122 |
| kernel of a translation-invariant operator, or a displacement-indexed coefficient of it | ch. 5 (9); 10:354 ✓ ("convergence of the actual quadratic rows", citing the chapter 5 proposition); 12:55 |
| symbol; operator; factorisation `C*C = H` | ch. 5, 6 only |
| row of a matrix or of a kernel at a fixed output index; "row mass" = row sum | everywhere; in chapter 17 all ten uses (17w:12; 17c:237, 280, 336–367; 17m:237–260), where the kernels are not translation-invariant |
| vector in a finite list of coefficient vectors ("bounded rows") | 11:2253; 13:159 |
| row of the matrix of correlation pairings ("reference rows") | 15:275, 278 |
| row of a displayed table | 9:140, 145 |

### 2.3 `selected`, `selection`

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

### 2.4 `test`

| Sense | Where |
|---|---|
| test function (standard); integration against one | ch. 1, 13–16 (about 30), 17–18 (12); 14:207 |
| "tested against" = paired with all spectators or words; "tested correlation" = value of a correlation functional | 11:2233–2320; 13:272; 15:243; 16:46; 18:7, 215, 248; 18r:36 |
| Borel condition, its indicator, the plaquette or edge it concerns, its numerical value | ch. 4–6; "tested" at 9:541, 547 |
| "tested links" = links a function depends on | 11:402, 413; 11R:107 |
| classical test connection; one evaluation of a symbol | 2:13, 103, 150, 416; 7:215 |

From chapter 10 on, the chapter 4–6 senses appear as "event indicator" and "cutoff condition".

### 2.5 `label`, `tag`

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

### 2.6 `mark`, `marked`, `marker`; `source`

- **marked** = carrying insertions tracked by nilpotent variables `z_i` (12:200–206 ✓; 11:70–75: the unmarked density is the coefficient of `z_∅`). About 80 uses in chapters 11–19.
- **mark** = one insertion point or its index (about 45 uses). In most of `17-marked-trace-rates.tex` the inserted factor is a differentiated block kernel, not an observable. At 7:378 "a mark of direction `a`" seems to be an external plane wave (inferred).
- **marker** = the nilpotent variable (18:123) or the insertion (18:124).
- **source** has at least six senses: the nilpotent source variable; the source weight; the source algebra; the inserted observable or density itself; the inhomogeneous term of an affine map or of a recursion (ch. 6; 17c); a generating-function source (ch. 8). At RG:82 "source locations" refers to the formalisation the book was written from; 18:411 probably does too; for 14:186 ("the source construction") it is not determined.

Proposal: *insertion* for the object, *insertion point* for its place, *source variable* for `z_i`, *with insertions* for "marked", *inhomogeneous term* for the recursion sense.

### 2.7 `response` (about ten senses)

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

### 2.8 `transport`, `transfer` and their synonyms

Three objects share these words: parallel transport along a path; the map `W` (and its companion `T` on two-forms); and the propagation of a density, coefficient or current through the block steps. The last is also called *transfer*, *pullback*, *propagation*, *update*, *push*, *descent*. Further uses: application of, or conjugation by, the comparison maps `U_{k,d}` (14:229–302, 946) and image under a lattice symmetry (6:966).

### 2.9 `window`

| Sense | Where |
|---|---|
| index neighbourhood on which a matrix is inverted | ch. 6; 9:142, 278, 279; 10:358; 11:135, 673–684 |
| interval of levels | 10:185, 189; 11 (6); 11R (4); 17w (about 11); 17m:429 |
| compact set of separated configurations | 11:2078, 2149; 14:173–237; 14lc:6; probably 17:140 |
| interval of radii | 17:129, 131, 146; 17w:6 |
| range of distances; length of an average | 11:1726; 17m:476 |

### 2.10 `history`, `stage`, `level`

- **history** is defined at 11:18–19 ✓: "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations". Chapter 10 uses it for the finite sequence of densities and couplings at one cutoff, with its choices attached (10:256). Chapter 5 uses it for the list of block ratios and averaging orders alone (5:303). Chapters 1, 2, 8, 9 say "renormalization trajectory".
- **stage** is defined at 10:25 ✓: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds". It is a regularity class, not a renormalisation step; `J(m) = j` for `A_j ≤ m < A_{j+1}` (10:129–134 ✓). Chapters 7 and 9 already use it in this sense (14 uses); chapters 5 and 6 use "stage" for a step. Chapters 4, 5 and 7 also write `j` for the averaging order, which chapter 10 calls `ȷ_j`.
- **level**, **scale**, **depth**, **step** are all used for the scale index.

Proposal: *level `m`* for the index, *step* for the map, *stage `j`* only for the regularity class (defined once), and one word for history.

### 2.11 `phase`, `word`, `probe`, `insertion`, `weight`, `stopping`, `request`

- **phase**: "a character of a commutative operator algebra, not a set of gauge configurations" (15:6–10 ✓); about 100 uses, one sense. "The compact phase space `Ξ`" (16:15 ✓) is the character space, which collides with the usual meaning of phase space. Complex phase factors occur in ch. 7.
- **word**: a finite sequence of insertions (3:234); "a finite list of labels and positions" (13:282 ✓); a product of smeared fields (16:291); a product of links along a path (6:630); a term of a Neumann series (6:1199); "transfer word", "difference word" (ch. 11).
- **probe**: a linear functional on jets (ch. 3); "a fixed word `v` at distinct nonzero positions", defining `λ(A) = S(A(0)v)` (18:38–39 ✓). The uses in `18-lattice-products.tex` and 14:354 are this second sense ("fixed cells for exterior probes", 18lp:331–333 ✓).
- **insertion**: a local observable at a point (ch. 1–3, 8); a derivative of an operator in the background field (ch. 7, about 28); a linear map (7:243).
- **weight**: scaling dimension; exponential support weight; Fourier weight `h_l`; source weight; probability weight; numerical coefficient.
- **stopping**: in chapter 12, stopping at level `m` *and* deleting the terms of source degree at least two; in chapters 13 and 18lp, the level at which the transfer is halted and a chessboard bound applied, with nothing deleted.
- **request**: a finite tuple of data; a requirement placed on the schedule; a prescribed lower bound on a level.

---

## 3. Terms settled by another chapter

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

## 4. Terms still undetermined

After the surveys and their audits, the text does not determine:

- **Chapters 3–6:** `moving comparison fields` (3:576; "moving" elsewhere means depending on the cutoff or sequence index); `seeded sector / unseeded law` (6:1544; 9:283); `output anchors` (6:90); `likelihood tests` (6:920, 1016).
- **Chapters 7, 9:** `recording estimate` (7:461, 742); `thermal` (7:765); `direction selectors`; `live tag actions`; `missing-coordinate factor`; `read-count polynomials`; `support compression`; `inspected support`.
- **Chapters 10–11:** `Hilbert encoding`; `block bridge`; `response bound` (10:626); `preselection bound`; `selected slot`; `front-column`; `exposure`; `alphabet`; `coarse forecast`; `corrected body product estimate`; `same-data restart conditions`; `finite decorations`; `protected trial`.
- **Chapters 12–16:** `coordinate hybrids` (14lc:95); `admissible comparison depth` (14lc:23); why a map is called a "graph".
- **Chapters 17–19:** `v_eom` (17m:385–386 ✓, never introduced); `actual free history`; `protected-path errors`; `fixed-ratio jet errors`; `with these same frames`; `unit endpoints`; `E_stat`, `E_tail`, `E_mark` (only bounds are given); `polynomial-source propagation constants`.

The symbol `hot(s)` at 11:1934 ✓ is the function written `h(s)` at 11R:114 ✓: a leaked source name.

---

## 5. Synonym clusters that span the book

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

## 6. Damaged sentences

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

## 7. Jargon in label names

Not visible in the PDF, so of low priority: `ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`, `ch09:fusion*`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch11:detectors`, `ch11:detector-bound`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`, `ch12:forgetting`, `ch12:stopped`, `ch13:coarse-residual-supplier`, `ch14:grid-cost`, `ch15:detector-moments`, `ch17:current-suppliers`, `ch18:raw-replacement`, `ch19:conditional`. The last is misleading where the statement is no longer conditional.

Some label words are also in the prose and so are visible: `shooting` (10:272–274 ✓ "uniqueness of the shooting parameter"), `floor`, `mass`, `root`, `replication`.

---

## 8. Proposed equivalents withdrawn after the audits

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

## 9. Method and limits

- **Surveys.** Seven agent surveys in two rounds: three for chapters 3–6, four for the rest. Each read its files in full and marked each meaning as defined, read, inferred or undetermined.
- **Independent checks.** Five fresh agents, one for the chapter 3–6 dictionary and one for each later survey. Each read its chapter files in full, rechecked the stated meanings and basis codes, reclassified the multi-sense words occurrence by occurrence, and checked the claims of this overview about its chapters. They found the surveys reliable on line references and quotations, and found between six and ten definite errors per survey: wrong sense assignments, merged or invented terms, equivalents that change the mathematics, and above all terms declared undetermined that another chapter defines (about forty in total; section 3).
- **Verification by the coordinating agent.** About 60 passages marked ✓ here or checked while applying the audits, including the main finding of every "definite error" that changed this overview. All agreed with the audits.
- **Not done.**
  - The audits themselves are unchecked agent work. Two of them noted points they could not decide, and their judgements on what is standard terminology come from their own knowledge.
  - The four later surveys are not rewritten; their corrections are in the audit files.
  - Sections on overloaded symbols and synonym clusters in the surveys were only spot-checked by the audits.
  - No Lean declaration was consulted, and no proposed equivalent was checked against the literature. Figures were not read.
- **Agent assistance.** Claude Code (Claude Fable 5.2) with subagents throughout. This needs a mathematician's review; agreement between agents is not evidence of correctness.
