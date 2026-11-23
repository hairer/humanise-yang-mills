# House terminology in the v3 manuscript: dictionary

**Status:** draft audit, not an edit of the chapters (apart from the sentence repairs listed in Part I, section 6). **Scope:** all chapter files under `chapters/`, plus `main-theorem.tex` and `reading-guide.tex`. Line numbers are those of upstream commit `7bec3925`; the sentence repairs keep every line number.

**Purpose.** The manuscript uses many words as technical terms that are not standard mathematical vocabulary. This file lists them, states what each means in the text, and proposes a standard equivalent. It extends the translation table in `blueprint/notation.md`.

| Part | Content |
|---|---|
| [I](#part-i) | Overview of the whole book: words with several meanings, terms explained in another chapter, open terms, synonym clusters, damaged sentences, equivalents to avoid |
| [II](#part-ii) | Dictionary for chapters 3–6 |
| [III](#part-iii) | Dictionary for chapters 1, 2, 7, 8, 9 |
| [IV](#part-iv) | Dictionary for chapters 10–11 |
| [V](#part-v) | Dictionary for chapters 12–16 |
| [VI](#part-vi) | Dictionary for chapters 17–19, the main theorem and the reading guide |

**How to read it.** Each of Parts II–VI is one corrected text: the survey of its chapters with the corrections of two rounds of independent checks applied. Each ends with "Changes folded in" and "Verification status". Section numbers are local to each part.

**Basis codes.** D: the text defines the term at the cited line. R: the meaning is read off an explicit sentence or formula. I: inferred from context; check before using the proposed equivalent. ?: the text does not determine the meaning.


---

<a id="part-i"></a>

## Part I. Overview of the whole book

This part is the cross-chapter synthesis: words whose meaning changes from chapter to chapter, terms that one chapter uses and another defines, and synonyms that span the book. The entries for individual terms are in Parts II–VI.

References are `chapter:line`; suffixes distinguish included files as in Parts III–VI (`11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, `15sp`, `17w`, `17t`, `17c`, `17m`, `18r`, `9s`, `2e`; `MT`, `RG` for the two front-matter files). Entries marked ✓ were reread by the coordinating agent; the rest rests on a survey and at least one independent check (section 9).

---

### 1. The picture by part of the book

- **Chapters 1, 2, 8** are nearly free of house vocabulary.
- **Chapter 3** has a vocabulary of its own (probe, wave, pulse, tower, spectator, leg, response). **Chapter 4** introduces "test / tag / label / branch". **Chapters 5–6** carry the "row / actual / selected" vocabulary (Part II).
- **Chapters 7 and 9** continue it and add "response", "insertion" and "weight" in several senses each, with an accounting layer of `cost`, `gain`, `loss`, `reserve`, `share`, `fits`.
- **Chapters 10–11** have been through a translation pass: `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector` no longer occur in prose. What remains is a scheduling vocabulary (stage, plateau, floor, delay, request, window), many nouns used without a defining sentence for the objects of the expansion with insertions (principal, incidence, graph, column, trial, lift, mass, normalized local insertion, localization, terminal), and sentences damaged by mechanical replacement (section 6).
- **Chapters 12–16** use "graph" for a linear map from coefficients to remainders (already in chapter 11: 11:379–382, 447), "column" for a coefficient vector, "heat" for the semigroup `e^{-tH}`, "mixed" for the undecomposed mixture of phases before it is explained (from 14:12; explained 15:5–6), and let "label" drift from a polynomial to a field.
- **Chapters 17–19** reuse "window", "source", "response" and "transport" in further senses, refer to earlier results by nickname, and add a layer of their own ("coupling threshold", "pre-ratio / post-ratio / fixed-ratio constants", "alias", "crop", "score").
- **The front matter** uses "phase" without saying it is a character of a commutative algebra, and "admissible physical periods" without definition (MT:14–15 ✓, MT:19). The requirement on the periods is at 1:202 and the choice `R_p = 4(M+p+1)` at 10:193–197 ✓; neither place uses the word "admissible", so the identification is inferred (19:20–21 has "admissible physical periods `R_p`").

The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund` do not occur in the prose of any chapter; every independent check confirmed this for its files (`budget` survives in label names only). The accounting vocabulary that is present is `cost` (over 100 uses outside chapters 3–6), `reserve`, `gain`, `loss`, `margin`, `excess`, `share`, `spent`, `request`, `fits`.

---

### 2. Words with several meanings, across the book

Counts are occurrences in prose, with label names and references stripped. Totals were recounted by two independent checks and agree to within a few; the split between neighbouring senses is a judgement in many cases and was recounted once only.

#### 2.1 `actual` (about 280 uses in the book)

| Sense | ch. 3–6 | ch. 1, 2, 7–9 | ch. 10–11 | ch. 12–16 | ch. 17–19 |
|---|---|---|---|---|---|
| of this construction (as opposed to an abstract or separately chosen object); mostly deletable | 17 | about 24 | about 54 | 14 | about 24 |
| nonlinear / at the non-flat background, against flat or linearised | 26 | — | about 10 | — | — |
| the gauge-covariant block average and objects built with it, in particular the tangent `W_a` (but see the note on "actual tangent" at the end of section 3) | 20 | about 14 | — | — | 7 |
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
| component of the stacked vector whose half-square is the action | ch. 6 (about 68); 5:853, 1054–1055; 7:352, 976–993, 1168; 9:544, 568, 835, 840; 10:356; 11:668, 710; 11R:101–122 |
| kernel of a translation-invariant operator, or a displacement-indexed coefficient of it | ch. 5 (9); 10:354 ✓ ("convergence of the actual quadratic rows", citing the chapter 5 proposition); 12:55 |
| symbol; operator; factorisation `C*C = H` | ch. 5, 6 only |
| row of a matrix or of a kernel at a fixed output index; "row mass" = row sum | everywhere; in chapter 17 all ten uses (17w:12; 17c:237, 280, 336–367; 17m:237–260), where the kernels are not translation-invariant |
| vector in a finite list of coefficient vectors ("The rows `(I−Π_i)u_{j,i}` are bounded") | 11:2253; 13:159 |
| row of the matrix of correlation pairings ("reference rows"); inferred, the text does not say what a reference row is | 15:275, 278; also 13:168, 182; 14:277 |
| row of a displayed table | 9:140, 145 |

#### 2.3 `selected`, `selection`

| Sense | Where |
|---|---|
| large-field selection `A` and membership in it (chapter 6) | ch. 6 (28); 9:108, 153, 279, 440; ch. 11 and 11R (about 25) |
| fixed by the construction: "selected trajectory / schedule / history / stage requirements" | 4:160; 5:738, 858, 1378; ch. 6 (5); ch. 7, 10, 11, 12, 13, 17–19 (about 40) |
| retained component of an affine map, or of a stencil | ch. 6 (11) |
| a finite subfamily of terms ("finite selections") | 4:616; 9:157, 215, 637–687, 890; 17m:92 |
| retained low-order terms | 9:312–383 |
| the continuum family along the chosen subsequence; choice of a subsequence | 13:6, 7, 143, 172; 15:257; 17m:446; 19:38, 112 |
| the phase `ξ_*` (also "chosen", "retained") | 15:301; 17:15, 31, 351; 19:117; MT:91, 93 |
| pairs with nonzero weight; picked out by a formula | 18:297, 352, 358; 17t:419, 454 |

In chapter 11 the large-field and the "fixed" senses occur in adjacent paragraphs (11:1933 and 11:1965) and within one proof (11R:89, 159).

#### 2.4 `test`

| Sense | Where |
|---|---|
| test function (standard); integration against one | ch. 1; 3:147, 319; ch. 13–16 (about 30), 17–18 (12); 14:207 |
| "tested against" = paired with all spectators or words; "tested correlation" = value of a correlation functional | 11:2233–2320; 13:272; 15:243; 16:46; 18:7, 215, 248; 18r:36 |
| Borel condition, its indicator, the plaquette or edge it concerns, its numerical value | ch. 4–6; "tested" at 9:541, 547 |
| "tested links", "tested neighborhood" = the links a function depends on | 11:402, 413; 11R:107 |
| classical test connection; one evaluation of a symbol | 2:13, 103, 150, 416; 7:215 |

"Event indicator" already alternates with "test" in chapters 4 and 6 (4:507, 532, 658; eight times in chapter 6). "Cutoff condition" does not occur in chapters 3–6; it appears from chapter 10 on.

#### 2.5 `label`, `tag`

| Sense | Where |
|---|---|
| polynomial label: an abstract index set in chapter 1 (1:330–331), the pair `v = (d,c)` with `c ∈ V_d` from chapter 2 (2:96–97) | ch. 1–3, 11, 12, 13; MT, RG, ch. 19 |
| element of the quotient `F_d` or `F`, i.e. a field | ch. 14–16 (about 26 of 31 uses); probably 18:140–222, 18r:61, 64 |
| element of the free Maxwell spaces ("convergent moving free labels", "convergent moving labels") | 17:97, 370 |
| insertion label, element of the index set of insertions | ch. 11 (13) |
| polymer label (defined 8:24 ✓); large-field label `η` | ch. 8; 9:154 |
| index of an activity, path or large-field term | ch. 4, 6, 9, 10, 11R |
| random index `α` ("tag") | ch. 4–6; 9:83, 85; 9s; 11:244, 679; 11R:358 |
| the index `d` of `V_d` ("tag") | 2:98, 99 |
| event label / cutoff-failure label | ch. 6; 9:111, 133 |

`blueprint/notation.md` requires the first two to be distinguished; from chapter 14 on they are not.

#### 2.6 `mark`, `marked`, `marker`; `source`

- **marked** = carrying insertions tracked by nilpotent variables `z_i` (12:200–206 ✓; 11:70–75: the unmarked density is the coefficient of `z_∅`). About 100 uses in chapters 11–19, and about 20 of "unmarked".
- **mark** = one insertion point or its index (about 35 uses). In most of `17-marked-trace-rates.tex` the inserted factor is a differentiated block kernel, not an observable. At 7:378–385 "a mark of direction `a` and Lie algebra direction `u`" is an external background leg with polarisation `a` and colour `u` in a first-order vertex (inferred from the formula).
- **marker** = the nilpotent variable (18:123) or the insertion (18:124).
- **source** has at least six senses: the nilpotent source variable; the source weight; the source algebra; the inserted observable or density itself; the inhomogeneous term of an affine map or of a recursion (ch. 6; 17c); a generating-function source (ch. 8). At RG:82 "source locations" refers to the formalisation the book was written from; 18:411 probably does too; "the source construction" at 14:186 is the construction of `14-lattice-comparison.tex` (same parameters at 14lc:26, 85–86 with `M_k = H_k`); whether "source" there means the formalisation is not determined.

Proposal: *insertion* for the object, *insertion point* for its place, *source variable* for `z_i`, *with insertions* for "marked", *inhomogeneous term* for the recursion sense.

#### 2.7 `response` (ten senses)

| Sense | Where |
|---|---|
| two-point function with a linear source | 3:409 ff. |
| candidate infinitesimal variation; a term of the Ward sum | 3:657, 964 |
| the map from a coarse field to the stationary fine field (elsewhere "transport", "tangent", "lift"), in several versions | 6:953 ("Let `a = 𝒰_F h` be the stationary fine response": the image field; `𝒰_F` is not identified with `W` in the text); 11:642 ("the actual stationary forest response `W`"); 17m:193 (`W_a`); 17m:202 (`W_s`); 19:159 |
| the nonlinear version of that map ("the stationary nonlinear response") | 17m:278 |
| curvature response `J = H_{0,f}⁻¹ T H_{0,c}` (11:646–648 ✓) and its installed form `Ψ_i` | 11:647, 1729–1775; 17w:11, 60, 67, 68 |
| a log-determinant as a function of the background; an operator with its background derivatives; "response layers" | 7:277, 367, 454, 624, 743, 791; 17t:90 |
| one-slot response `L_{v,f}(c) = ∫ f S(c(x₀), v(x))` (defined 13:119–122 ✓); "correlation responses" | ch. 13, 18gq; 14:406, 992; 18:182; RG:18 |
| the Laplace transform `ℒf(E)` of a frequency profile (a function of `E`; 14:450–451, 465–470); and its integral against the spectral measure, `Resp_i(g)` (a number; 14:503–505) | 14:465–761 |
| shell integral `−∫ ∂_μ V_c S(J_{μc}, A)` ("total shell response"; "flux" is this note's word) | 14:777, 796 |
| "anchored vector response" | 17:224 (inferred) |

#### 2.8 `transport`, `transfer` and their synonyms

Three objects share these words: parallel transport along a path; the map `W` (and its companion `T` on two-forms); and the propagation of a density, coefficient or current through the block steps. The last is also called *transfer*, *pullback*, *propagation*, *update*, *push*, *descent*. Further uses: application of, or conjugation by, the comparison maps `U_{k,d}` (14:229–302, 946) and image under a lattice symmetry (6:966).

The phrase `response bound` (10:626) fits none of these rows and is undetermined (section 4).

#### 2.9 `window`

| Sense | Where |
|---|---|
| index neighbourhood on which a matrix is inverted | ch. 6; 9:142, 278, 279; 10:358; 11:135, 673–684 |
| interval of levels | 10:185, 189; 11 (6); 11R (4); 17w (about 11); 17m:429 |
| compact set of separated configurations | 11:2078, 2149; 14:173–237; 14lc:6; probably 17:140 |
| interval of radii | 17:129 (ambiguous: the cited argument of chapter 14 works on a compact separated window), 131, 146; 17w:6 |
| range of distances; length of an average | 11:1726; 17m:476 |

#### 2.10 `history`, `stage`, `level`

- **history** is defined at 11:18–19 ✓: "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations". Chapter 10 uses it for the finite sequence of densities and couplings at one cutoff, with its choices attached (10:256). Chapter 5 uses it for the list of block ratios and averaging orders alone (5:303). Chapters 1, 2, 8, 9 say "trajectory" ("renormalization trajectory" at 1:208, 1:488–489, 2:436); 2e:253 and 7:1202 already say "history".
- **stage** is defined at 10:25 ✓: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds". It is a regularity class, not a renormalisation step; `J(m) = j` for `A_j ≤ m < A_{j+1}` (10:129–134 ✓). Chapters 7 and 9 already use it in this sense (about 15 uses). The three uses in chapters 5–6 (5:689 "each adjacent pair of stages"; 6:21 "Fix a stage, a block ratio"; 6:96 "the fixed stage and ratio") probably have it too: compare 9:110 "at fixed stage and ratio", and chapter 6 says "step" where it means a step (6:950). Inferred; an earlier version of this note read them as "step". Chapters 4, 5 and 7 also write `j` for the averaging order, which chapter 10 calls `ȷ_j`.
- **level**, **scale**, **depth**, **step** are all used for the scale index.

Proposal: *level `m`* for the index, *step* for the map, *stage `j`* only for the regularity class (defined once), and one word for history.

#### 2.11 `phase`, `word`, `probe`, `insertion`, `weight`, `stopping`, `request`

- **phase**: "a character of a commutative operator algebra, not a set of gauge configurations" (15:8–9 ✓); about 105 uses, one sense. "The compact phase space `Ξ`" (16:15 ✓) is the character space, which collides with the usual meaning of phase space. Complex phase factors occur in ch. 7.
- **word**: a finite sequence of insertions (3:234); "a finite list of labels and positions" (13:282 ✓); in chapter 16 a finite sequence of letters, where "a letter is a pair `(A,f)` with `A ∈ F` and `f ∈ 𝒮(ℝ⁴)`" (16:291–294 ✓; "word" itself is not defined there, and the words span a free algebra `𝒫`); a product of links along a path (6:630); a term of a Neumann series (6:1199); "transfer word", "difference word" (ch. 11).
- **probe**: a linear functional on jets (ch. 3); "a fixed word `v` at distinct nonzero positions", defining `λ(A) = S(A(0)v)` (18:38–39 ✓). The uses in `18-lattice-products.tex` and 14:354 are this second sense ("fixed cells for exterior probes", 18lp:332 ✓). 17m:251 "the fixed probe order" is probably the chapter 3 sense (3:939 "the scalar order-`j` probes").
- **insertion**: a local observable at a point (ch. 1–3, 8); a derivative of an operator in the background field (ch. 7, about 28); a linear map (7:243).
- **weight**: scaling dimension; exponential support weight; Fourier weight `h_l`; source weight; probability weight; numerical coefficient.
- **stopping**: in chapter 12, stopping at level `m` *and* deleting the terms of source degree at least two; in chapters 13 and 18lp, the level at which the transfer is halted and a chessboard bound applied, with nothing deleted (13sb:10–11). Chapters 10–11 have the second sense (10:172; 11:781, 816, 945; 11E:65).
- **request**: a numerical lower bound imposed on a stage constant (10:66–69 "countably many finite numerical requests … At stage `j` take the maximum of the first `j` such requests"); a finite tuple of data (11:2056–2057; 14:224–227); a prescribed lower bound on a level.

#### 2.12 Further words with more than one sense

These were found by the checks and are treated in the part named.

- **mixed** (Parts V, VI): of the undecomposed mixture of phases ("mixed correlation hierarchy" 14:12, "mixed reflection Hilbert space" 15:24); "mixed measures" obtained by polarisation (14:424); "mixed signs" (14:658); "the mixed table" = the mixed correlations `S` (18:72).
- **cutoff** (Part V): the ultraviolet cutoff `N`, and a smooth cutoff function (14:324; 16:459).
- **profile** (Part V): large-field profile, "the sum of activities having one particular support and prescribed set of large-field sites" (12:26–27); frequency profile, a one-variable factor of a product test function in momentum space (14:448 ff.).
- **vacuum** (Part V): the vector `Ω` of the reflection space (14:34; 15:25); the lattice integral without insertions ("vacuum normalization bound" 12:247).
- **terminal** (Parts IV, V): at the cutoff level `N` ("terminal trial", "inverse terminal coordinates"); chapters 5–6 use it differently (Part II).
- **lift** (Part V): besides the operator `W`, a polynomial preimage of a free field (14:172; 14lc:32; 15:256).
- **ordinary**, **regular** (Parts IV, VI): "ordinary" is the small-field part in chapters 10–11 (10:97; 11:940, 1589) and 17 (`Z_ord`); "regular" is one term `E_reg` of it at 17m:107 but the whole non-large-field part at 17w:78.
- **threshold** (Part VI): a lower bound on `β̂` ("coupling threshold", about 19 uses in chapter 17), and the small-field threshold `t`, an upper bound on the field (17c:316; 17m:304).
- **graph** (Parts IV, V, VI): a linear map `G` from coefficients to remainders (11:379–382; 12:82); also "intersection graph" (11:247) and "stationary graph" (10:922–924) in the ordinary senses; see section 8.

---

### 3. Terms settled by another chapter

Each of these is used in one chapter and defined or explained in another. Rows that end "inferred" are narrowed, not settled.

| Term | Settled by | Meaning |
|---|---|---|
| regularity-stage index `J_m` (4:651) | 10:25–29, 129–134 ✓; 17w:15 | `J(m)` is the stage in force at level `m`. |
| inherited loop action | 9:20–28 ✓; 7:237 | `P^path = β𝒦 + ℒ`, where "`ℒ` is the quadratic loop correction"; the `β`-independent quadratic part of the path action. |
| coupling band | 10:212 ✓ | "The admissible inverse coupling band at level `m` is `[β̂_m/2, 2β̂_m]`". |
| admissible periods (MT) | 10:193–197 ✓ | `R_p = 4(M+p+1)`, `p ≥ 0`, with `M` large enough for the first plateau. |
| connected covering number | 4:587–589 | Minimum number of radius-`B` balls with connected union covering the set. |
| `c_lin` (9:846) | 4:474–480 | Slope constant of `clip_t` above `t`. |
| quadratic-tilt criterion (9:115) | 9:114–116 ✓, citing a proposition of chapter 6 (6:1123–1138) | An alternative hypothesis in terms of tilted Gaussians; not needed in chapter 9. |
| plaquette "whose relaxed small-field condition is not automatic" (9:548; "nonautomatic" before the repair) | 4:489–492 | The finitely many plaquettes on which the relaxed small-field condition is not automatically satisfied. |
| width | 10:375–381 | The weight `e^{wℓ(γ)}` on path coefficients; a "width reserve" is a bound at `w' > w`. |
| derivative reserve (9:34) | 10:737–739 | Derivative orders beyond the order of the output norm. |
| eligible, eligibility | 4:440–450 ✓; 8:289–295 ✓ | An additional Borel gauge-invariant condition `ℰ_i^extra` attached to each large-field activity ("an additional Borel gauge-invariant eligibility test"). In the abstract setting of chapter 8 it appears as a restriction on the allowed covering families: "The exact rules for eligibility are part of the definition of an effective density; they may exclude some otherwise possible covers". Later uses (9:902 "eligibility criteria"; 18:127 "eligibility condition") read as the per-activity kind; 11:125 fits the family rule and 11:153 is not decided by the text (Part IV). |
| section | 2:138–146 | "A local polynomial section is a complex-linear map …; the term section simply means a right inverse of the Taylor map". |
| separated test function | 1:359 | An element of `C_c^∞(Conf_n)`, extended by zero. |
| conserved line | 3:590–596 ✓; 14:258 ff. | `{J ∈ 𝒯_{≤4} : div J = 0} = ℝ T^Max` for the free fields. The use at 17:341 needs the statement for the interacting fields, section "The conserved stress line" of chapter 14 (not read in full). |
| one-slot response; correlation responses | 13:119–122 ✓ | `L_{v,f}(c) = ∫ f S(c(x₀), v(x))`. |
| ordered tails | 13:213–214 ✓ | "the filter is generated by ordered tails: `p = P(k)` with `k ≥ k₀`, and `N = n(j)` with `j ≥ j₀(k)`". |
| strip removal; scaled mesh; grid errors | 14:174–200 | Coordinate-equality strips of width `4δ_k`, grid spacing `s_k`, and the errors on that grid. |
| derivative-transport argument | 14:229–238 | The proposition "Derivative transport and smooth comparison". |
| physical inclusion | 14:210–212 | The inclusion for the interacting theory, against the free one. |
| exceptional vacua (19:107) / exceptional phases | 16:379–381 ✓; 15:324–328 | "the zero-energy space is a line for almost every phase … To remove the exceptional set requires a bound uniform in `ξ`": the exception is a null set of phases. |
| trial encoding | 11:943–951, 1074 | The reference label `v_{N,p}` approximating a trial `F`, with bounded inverse terminal coordinates. |
| attachment | 9:687; 11:147–156, 924–941 | Joining an insertion stencil or a large-field part to an existing support in the polymer expansion, and the sum over the places where this can happen. Not defined in one sentence. |
| site conversion | 9:513; 11:266–272; 11R:141 | Conversion of sums anchored at a point into sums over terms containing a site. |
| weight restoration | 11:1374–1590 | Named lemmas at 11:1436 ("Regular weight restoration") and 11:1471 ("Large-field weight restoration"): passage to the larger source weight. |
| root estimate | 11:817–822, 2072–2079 | "Taking the number-of-cells root": the chessboard-seminorm bound. |
| top polynomial extraction `T` (17w:100; the phrase is not in chapter 11) | 11:1141–1146, 1292–1293, 2085–2088 | Probably the localization map `T` onto frame coefficients built at the top level of the comparison window. Chapter 11 has a second map `T` (11:373). Inferred. |
| restarted history; restarted representation | 11:736–741; 11R:2, 18 ✓ | The restarted history is the history with the coupling held constant below a comparison level. The restarted representation is the local representation of the densities along it, with new radius `B_i = b(x_i)²` and threshold `ϑ(x_i)`. |
| equation calibration floor (19:30) | 11E:25–30 ✓ | A lower bound on the block ratio `L` (`L^{1/8} ≥ max …` "in the stage-`j` block floor"). The same sentence adds a coupling condition `β̂_N ≥ a_{d,J(N)}` to the stage conditions, which 19:29–31 may also cover. |
| subpower | 6:822–823 ✓; 9:109; 18lp:18 | "`A_k` is subpower, meaning `A_k(x) ≤ C_ε x^ε` eventually for each `ε > 0`". Defined in chapter 6 itself and again where reused. |
| parent | 1:218–220 | The coarse site `y` in the unique decomposition `x = Ly + z` ("the resulting parent map"). |
| matching | 7:988–998, 1159–1167 | As in Part II. Not rechecked. |
| envelope | 9:794; 11:1972, 2136; 17m:283 | A majorant ("a polynomial envelope for the finite Gaussian coordinates", 17m:283). Read at 17m:283 only; Part II leaves the use at 6:1187 unglossed. |
| thermal (7:765) | 7:231–233 ✓ | The label `ch07:thermal` names `T(v) = ℒ_{m+1}(U_v) + ½ log det Q(v) − log J_Haar(v)`, "the Gaussian contribution at a stationary fine configuration"; the "thermal coefficient" is then a coefficient of `T(v)`. Inferred from the label. |
| recording estimate (7:461, 742) | 7:457–461 ✓ | The bound `C_μ e^{-c_μ n}` on the difference between the mesh mean and the integral of a periodic analytic function. The object is read; why it is called "recording" is not explained. |
| block bridge (10:921) | 5:1132, 1152; 7:597–598 | Probably the tangent `W_a`: the label `ch05:actual-bridge` names a bound for `W_a`. Inferred. |
| exposure (11:1285) | 11:1285–1293 | A linear map `𝓔` from labels to coefficients in a fixed polynomial frame. The object is constrained; the word is unexplained. Inferred. |
| `v_eom` (17m:385–386) | 17:171–172 ✓; 17m:375, 383 ✓ | Probably the kernel vector `v = (0,0,1)` of the free quotient `s : E → V` ("in the notation of the stability argument"); the symbol is never introduced. Inferred. |
| `E_reg` (17m:107) | 4:436 | The regular activities `E_i^reg`. At 17m:161 the same symbol is reused for an error coefficient. |
| unit endpoints (17m) | 17m:379–380, 467–475 | Probably the two end terms of a telescoping sum, which are multiples of the identity field. Inferred. |
| moving (labels, comparison fields) | 14:238, 250; 17t:97 | Varying along the sequence while converging ("convergent moving labels"). This narrows `moving comparison fields` (3:576), which has no definition. Inferred. |
| Warnings (6:1476) | 11:319 ✓, 1613 | Probably cutoff-failure events. Still inferred. |
| centered log determinant (5:1338) | 9s:47, 59 | Probably `s(x) − s(0)` with `s = ½ log det A`. Still inferred. |
| compulsory (10:654); mandatory (11R:161) | 10:654 ✓; 11R:161 ✓ | In chapters 10–11: the large-field factor that an activity covering prescribed sites must contain ("retain one compulsory large-field factor throughout fusion"). This does not settle the chapter 6 uses ("compulsory component region" 6:1018, "compulsory cutoff factor" 6:1461), which stay inferred (Part II). |

**The tangent `W`.** The symbols `W_s` ("the straight-average transport", 5:1084 ✓) and `W_a = W_s − d_{0,f} E R W_s` (5:1108 ✓) are used consistently in chapters 5, 7 and 17. The phrase "actual tangent" is not: it names `W_a` at 7:574 and 17m:263 ✓ ("The actual tangent is `W_a = W_s − d_f E R W_s`"), but at 17c:48 ✓ "the actual stationary tangent" is an operator `W`, the first derivative of the nonlinear stationary substitution, which "may be replaced by the smooth representative `W_a`" (17c:112 ✓). By 5:1151 ✓ the smooth representative `W_a` and the forest representative `W_F` are distinct. Whether the `W` of 17c:48 is `W_a` or `W_F` is not settled by the text.

---

### 4. Terms still undetermined

After the surveys and two rounds of checks, the text does not determine the following. Each phrase was searched for in every chapter file.

- **Chapters 3–6:** `seeded sector / unseeded law` (6:1544; 9:283); `output anchors` (6:90); `likelihood tests` (6:920) and `likelihood factors` (6:1016), perhaps the allocation weights `ϑ`, `1 − ϑ` of 6:68–76, whose plateaux are at the thresholds named there (inferred); `𝒰_F` (6:953, 976), never defined.
- **Chapters 7, 9:** `direction selectors` (7:427); `live tag actions` (9s:127); `missing-coordinate factor` (9:77); `read-count polynomials` (9:147); `support compression` (9:231); `inspected support` (9:220).
- **Chapters 10–11:** `Hilbert encoding` (10:381); `response bound` (10:626); `preselection bound` (11:382); `selected slot` (11:424); `front-column` (11:1343); `alphabet` (11:1911); `coarse forecast` (11:725–726); `corrected body product estimate` (11:1662–1663); `same-data restart conditions` (11:1666); `finite decorations` (11R:304); `protected trial` (11:2306; 13:229).
- **Chapters 12–16:** `coordinate hybrids` (14lc:95; perhaps configurations with some coordinates rounded to the grid); `admissible comparison depth` (14lc:23; "comparison depth" is used at 11:1149, 1343 and 13:163 without "admissible").
- **Chapters 17–19:** `actual free history` (17w:71); `protected-path errors` (17w:72); `fixed-ratio jet errors` (17w:72; "fixed-ratio" elsewhere means "may depend on `L`", 17c:138, 17m:429–430); `with these same frames` (17w:122); `E_stat`, `E_tail`, `E_mark` (17m:161–176; only bounds are given); `polynomial-source propagation constants` (17w:12); `resolution heights` (18r:54–55).

The symbol `hot(s)` at 11:1934 ✓ is the function written `h(s)` at 11R:114 ✓: a leaked source name.

---

### 5. Synonym clusters that span the book

| Concept | Words in use | Proposed |
|---|---|---|
| scale index | level, scale, depth, step | *level* |
| one block transformation | step, stage, update | *step* |
| the fixed construction of chapter 10 | common trajectory, selected trajectory, selected schedule, selected histories, same history, same family | one phrase |
| moving an object through the block steps | transport, transfer, pullback, propagation, update, push, descent | *transfer* |
| the operator `W` | transport, stationary tangent, lift, response | one word, and say which representative (`W_a`, `W_F`) is meant |
| the constant `b` | block penalty, soft constraint, penalty parameter, block parameter | one phrase |
| the other fields in a correlation | spectators, exterior word, exterior insertions, external positions | *spectators*, defined once |
| position of an insertion | anchor, origin | one word |
| family of functionals separating fields | separating family, detecting family, reference rows, detector (labels) | *separating family* |
| value of a correlation functional | response, tested correlation, measurement, correlation pairing | *value of the functional* |
| event that a Gaussian coordinate is large on a small-field region | cutoff failure, failed cutoff condition, warning | *cutoff-failure event*. Not "large-field event": chapter 6 separates the two mechanisms (6:7–11 ✓). |
| activity covering prescribed large-field sites | forced (symbols), "with prescribed set of large-field sites", compulsory, mandatory | one phrase, usable as a noun phrase |
| polymer-activity norms | site norm, support norm, containing-site norm, attachment norm, rooted activity norm | Not verified to be one norm: 9:513–518 distinguishes anchored from containing-site bounds. Name each normalisation once. |
| chessboard seminorm | `‖·‖_𝒯`, `‖·‖_k`, `‖·‖_cell(m)`, `‖·‖_{𝒞_k}`, `𝓡_m`, `‖·‖_root` | one notation |
| copies in a chessboard estimate | copies, replica cells, reflected copies, repetitions | *copies* |
| subsequence | refinement, extraction, selection | *subsequence* |
| for all large `N` | cutoff tail, eventually | *for all sufficiently large `N`* |
| slack in an estimate | reserve, margin, room, excess, spare | print the inequality |
| factor in an estimate | cost, gain, loss, expense, inflation | *contributes a factor*; `cost` is used for gains as well as losses (7:618–619) |
| lower bound on `β̂` or `L` | floor, threshold, entry, margin | *lower bound on …*. Only where the word has this meaning: "threshold" is also the small-field threshold `t`, and 17t:107 has a "floor" for an operator. |
| identity field | unit, unit field, unit insertion, identity | *identity* |
| annihilate | kill, annihilate | *annihilate* |
| lattice link | link, edge, bond | *link* |

The following are **not** synonyms, although they look it:

- `ordinary` and `regular` in chapter 17: `Z_ord = 𝒞 exp[−βS − ℒ − E_reg]` (17m:106–115 ✓), so "ordinary" is the whole small-field part and "regular" one term of it.
- `contact`: a coincident-point term in chapters 18–19, but the "contact term" of 7:501–568 and the "contact identity" of chapter 17 are not.
- `ordered tail` and "for all sufficiently large `N`": an ordered tail is a tail in two indices, `p = P(k)` with `k ≥ k₀` and `N = n(j)` with `j ≥ j₀(k)` (13:213–214 ✓; used so at 19:37–39). Keep the term with its definition.
- `representative` and the operator `W`: the word distinguishes `W_a` from `W_F` (5:1151 ✓).
- `cutoff failure` and `large field`: see the table.
- `padded block` (7:599) and `macro-box`: the wording at 7:599 fits the block-average patch of radius `(j+3)L`, not the macro-box of radius `(j+7)L`.

---

### 6. Damaged sentences

**Repaired on this branch** (commits `ac15effb` and `75cdd683`; wording recovered from the pre-replacement text where possible; line numbers unchanged): 6:730; 7:1086; 9:212, 548; 10:922; 11:247, 296, 365, 938, 1312, 1589, 1595, 1636, 1868–1869; 11R:302; 14:832; 16:380; 17w:76; 17m:144, 285, 303; 18lp:43, 136. Three fresh readers reread every repaired sentence: all now parse, and all are plausible in context except 11:1595, listed below.

**Left for the author**, because the intended meaning is not certain:

- 17t:159–160 "the order-two pullback must annihilate its affine–affine and affine–quadratic polynomial moment conditions" (earlier wording: "polynomial tests"). One satisfies conditions or annihilates polynomials; 17c:24–25 has "the affine–affine and affine–quadratic polynomial cancellations" for the same thing.
- 17c:359–360 "Only a bounded number of coarse output edges are within the gauge-covariant block average and averaging patches" (earlier: "the predictor and averaging patches").
- 9:893–894 "A connected prescribed set of `r` large-field sites is bounded in number by a rooted spanning-walk count."
- 9:949 "Output inverse coupling-band membership additionally requires".
- 18lp:27 "a remainder with vanishing extracted coefficient of norm `r_l`" and 18lp:36 "… of size `q`" (the size belongs to the remainder).
- 19:152–154 lists "the fact that inserting the identity leaves correlations unchanged" among things that "require additional normalization conditions"; a fact cannot require conditions. 18:430 still says "unit removal", which is the property meant. The same replacement phrase parses at 14:990 and 17:33.
- 11:1595–1596 "Split the positive decay of the prescribed set of large-field sites in Chapter 6 into reserved fractions": grammatical after the repair, but "decay of a set" is loose; probably the decay rate that chapter 6 gives per prescribed large-field site.
- 11R:300–301 "components with an actual selected prescribed set of large-field sites, and to a selected component within each such component".
- 17t:157–158 "with the gauge-covariant block average frame correction" and 17c:161 "with all mixed gauge-covariant block average and frame terms included": noun piles left by the replacement of "predictor".
- 10:98 "the relaxed small-field smooth cutoff is one": the relaxed condition is an indicator, not a smooth cutoff, so this may be a replacement artefact. Conjecture.
- Awkward but grammatical uses of "prescribed set of large-field sites" as a noun phrase: 11:941; 12:27, 162; 13ba:153; 18lp:40, 185; 18:127.

---

### 7. Jargon in label names

Not visible in the PDF, so of low priority: `ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`, `ch09:fusion*`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch11:detectors`, `ch11:detector-bound`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`, `ch12:stopped`, `ch13:coarse-residual-supplier`, `ch14:grid-cost`, `ch15:detector-moments`, `ch17:current-suppliers`, `ch18:raw-replacement`, `ch19:conditional`. The last is misleading where the statement is no longer conditional.

Some label words are also in the prose and so are visible: `shooting` (10:272–274 ✓ "uniqueness of the shooting parameter"), `forgetting` (title "Forgetting the terminal graph", 12:131), `floor`, `mass`, `root`, `replication`.

---

### 8. Equivalents that must not be used, and three that need a mathematician

These proposals were made at some stage and rejected on checking, because they change the mathematics or collide with established usage:

| House term | Rejected proposal | Why | Use instead |
|---|---|---|---|
| stopping (ch. 12) | truncated correlation | "truncated" is the standard name for connected functions; and nothing is deleted in ch. 13 | describe the operation |
| graph (ch. 11, 12) | remainder map | collides with the text's own "remainder map" `J_G` | keep *graph*; see below |
| unmarked gas (18lp:186) | partition function without insertions; density without insertions | the gas is a polynomial in the large-field profiles (12:180–183 ✓), one factor of the density; the density is its product with the exponential of the regular action, and the partition function the integral of that product | *the large-field polymer sum without insertions*, or the text's "exact-cover gas" defined once. That the two phrases name one object is inferred. |
| heat semigroup | transfer semigroup | not a standard term | *the translation semigroup `e^{-tH}`*; see below |
| hard / soft (10:656–666) | large-field factor / small-field corrections | "soft" bounds the logarithmic correction factors, which are not small-field | *preliminary large-field activity* / *logarithmic correction factor* |
| moment norm (10:630, 633; the quantity is displayed at 10:466–471) | norm of the functional on `c₀` | wrong space | *sup norm of the moment sequence* |
| left-coordinate Hessian | Hessian in left-invariant coordinates | increments act by left multiplication, generated by right-invariant fields | *second derivative in left-multiplication increments* |
| block-completed form (7:687) | gauge-fixed Hessian | it is completed by the block penalty and is still gauge-degenerate | *the form `⟨u, K_f u⟩ + b\|Mu − d_{0,c}r\|²`* |
| principal | leading part | collides with "leading interval / map" in ch. 11 | keep *principal*, defined once |
| corrected coefficients `R_I` | truncated (connected) coefficients | they are the coefficients after division by the free moment polynomial | keep *corrected*; see below |
| row (ch. 17) | kernel | the uses are rows at a fixed output index | *row of the kernel* |
| mixed ground space | space of invariant vectors of the mixed theory | the text's own phrase is clearer | *zero-energy subspace of the reflection Hilbert space of the undecomposed family* |
| exceptional vacua | further invariant vectors | loses that the exception is a null set of phases | *possible non-uniqueness of the vacuum on a null set of phases* (the text never shows that it occurs) |
| `ker H` | vacuum | chapter 15 stresses the space need not be one-dimensional | *zero-energy subspace* |
| cutoff failure, warning | large-field event | merges it with the large-field set, which chapter 6 keeps apart (6:7–11 ✓) | *cutoff-failure event* |
| ordered tail | for all sufficiently large `N` | loses the second index (13:213–214 ✓) | keep, with its definition |

Three identifications with standard notions were suggested by a checking agent from general knowledge. No sentence of the manuscript states them and no source was consulted; they need a mathematician.

- **graph.** `G : V_d → 𝓡_m` with `ΦG = J_G I_G⁻¹` (12:82–92; 11:447 `G' = R_G M_G⁻¹`) and a lemma "Graph contraction" (12:94) match the graph transform of invariant-manifold theory. If so, "graph" is standard and should be kept, with one sentence saying that the remainder is described as the graph of a linear map over the coefficients.
- **corrected coefficients `R_I`.** Division of the source polynomial by the free moment polynomial (14lc:49–57; 11:2066–2070) is the definition of Wick ordering with respect to the free moments.
- **heat semigroup.** It is built from translations in the reflected direction (14:39–56 ✓), so it is the translation semigroup of Osterwalder–Schrader reconstruction, and `H` the Hamiltonian. In chapter 14 it is used for every coordinate axis, and from 14:41 before 15:26 names it.

---

### 9. Method and limits

- **Surveys.** Seven agent surveys in two rounds: three for chapters 3–6, four for the rest. Each read its files in full and marked each meaning as defined, read, inferred or undetermined.
- **First independent checks.** Five fresh agents, one for chapters 3–6 and one for each later survey, read the chapter files in full and rechecked meanings, basis codes, sense assignments and line references. They found between six and ten definite errors per survey, above all terms declared undetermined that another chapter defines.
- **Re-audit.** Four further fresh agents checked this overview, Part II and a sample of the first checks against the text. They found 25 definite errors in Parts I and II (wrong counts, two rows contradicting quotations given elsewhere in the note, wrong line references, three contradictions between Parts I and II), and 60 doubtful or overstated claims. Of about 115 assertions sampled from the first checks, 4 were wrong or overstated.
- **Folding.** Five agents then folded the corrections of both rounds into the chapter-group dictionaries, opening the cited lines before applying each correction. Each of Parts II–VI ends with a list of the changes made and a statement of what has been read by more than one reader. They found five further errors in the checks themselves.
- **Verification by the coordinating agent.** About 60 passages in the first round and about 45 in the re-audit, including every finding that changed section 3, 5 or 8 of this overview. All agreed with the checks. The folded Parts III–VI were assembled without rereading their rows.
- **Not done.**
  - Rows that the "Verification status" sections name as resting on the survey alone have had one reader. This holds for most of the symbol tables and synonym clusters of Parts III–VI.
  - Rows added during the checks and the fold (about 110) have had one reader.
  - No proposed equivalent was checked against the literature; judgements on what is standard come from the agents' general knowledge. No Lean declaration was consulted. Figures were not read.
  - `monograph.pdf` and the booklets were not rebuilt after the sentence repairs.
- **Agent assistance.** Claude Code (Claude Fable 5.2) with subagents throughout. This needs a mathematician's review; agreement between agents is not evidence of correctness.

---

<a id="part-ii"></a>

## Part II. Chapters 3–6

**Status:** draft audit, not an edit of the chapters. **Scope:** `chapters/03-maxwell.tex`, `04-blocking.tex`, `05-gaussian.tex`, `06-large-fields.tex` at upstream commit `7bec3925`. Line numbers refer to those files at that commit.

**Companion parts.** The rest of the book is covered by Part I and the dictionaries in Parts III–VI.

**Purpose.** These chapters use many words as technical terms that are not standard mathematical or mathematical-physics vocabulary. Most come from the names of the formal source or from programming and accounting metaphors. This note lists them, states what each means in the text, and proposes one standard equivalent per concept, the same in every chapter. It extends the short translation table in `manuscript/HumanizeYM_v3/blueprint/notation.md` ("Terminology translation and restrictions") and follows its rule: "Do not translate a source metaphor by guessing: its domain, codomain, quantifiers and estimates determine its meaning."

**How to read the "Basis" column.**

- **D** — the text defines the term; the line is given.
- **R** — the meaning is read off an explicit sentence or formula, though the term is not formally defined.
- **I** — the meaning is inferred from context. Check before using the proposed replacement.
- **?** — the four chapters do not determine the meaning (section 4).

Where a row gives two codes (`D / I`), the first applies to the first statement of the Meaning column and the second to the rest.

Line references marked † were opened and found to contain the term, either in the fold that produced this text or in the re-audit. The absence of a mark does not mean a reference is unchecked; see "Verification status" at the end for what was checked.

---

### 1. Words with several meanings

These are the most damaging, because the reader cannot tell which sense is meant. The proposal is to keep at most one sense per word.

#### 1.1 `row` (ch. 3: 1 occurrence; ch. 4: none; ch. 5: 19 occurrences on 18 lines; ch. 6: 82 occurrences)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| kernel | 5:711–713, 738, 751, 826, 844, 849, 854, 1379 | Matrix-valued convolution kernel `K_ab(z)`, `z ∈ ℤ⁴`, of a translation-invariant operator on the infinite lattice. The text only introduces the notation ("Write a translation-invariant row as `K_ab(z)`"). "Adjacent-scale row": kernel of an operator between consecutive scales, with the position inside a block absorbed into the index set (inferred). | R | *kernel* (of a translation-invariant operator); *two-scale kernel* |
| symbol | 5:609, 624 | The same object as a matrix-valued Fourier multiplier with exponentially summable coefficients. | I | *symbol with exponentially decaying kernel* |
| operator | 5:858, 1124; 6:145† | A specific linear operator (`R`, `K`) with finite range or exponential decay. | R | *operator*, *finite-range operator* |
| component of the action vector | 5:853, 1054–1055; 6: about 68 of 82 occurrences, e.g. 101, 109–112, 186, 453, 1397–1398, 1434 | One component, indexed by its plaquette or edge, of the stacked vector whose half-square is the action; by extension the same component of its linearisation and of its affine approximation `Du + b_Y`. "Direct row": the single-plaquette component; "path row": a path component; "capped coarse rows": `v_c(p)`; "the rows `Φv_c`, `Φ_n v_c`": the comparison vectors; "complement-row", "null-row" (6:203, 1408): components of `N`. | R | *component* (of the curvature vector `X_f(p)`, of the affine map); *plaquette component*, *path component* |
| factorisation | 6:125, 136, 164, 377 | "Row factorization / realization / identities": the factorisation `C_ν*C_ν = H_ν` and the identities written through it. | R | *factorisation `C*C = H`* |
| matrix row | 3:628; 5:882, 996, 1346; 6: about 13, e.g. 217, 240, 280, 330, 554, 636, 812, 828, 907, 972, 994, 1501 | Literal, as in row and column sums. | — | keep |

#### 1.2 `actual` (prose uses, label names excluded: ch. 3: none; ch. 4: 4; ch. 5: 23; ch. 6: 48)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| the nonlinear object | 4:293; 5: 12 prose uses (857, 912, 930, 986, 1000, 1078, 1118, 1234, 1289, 1304, 1311, 1321); 6:161, 165, 361, 445, 478, 490, 1554 | The gauge-covariant block average of chapter 4 and its linearisation `𝒬 = M + d₀R`, as opposed to the linear ("straight") average `M`, and objects built with it. | I | *gauge-covariant block average*; write the symbol |
| at the true background | 6: about 26 uses, e.g. 15, 183, 439, 463, 466, 468, 515, 542, 1397–1400, 1551 | Nonlinear or evaluated at the non-flat background, as opposed to the flat or linearised model ("without identifying actual and flat matrices", 6:468; "the actual nonlinear row … its actual affine approximation", 6:1397). The most frequent sense in chapter 6; absent from chapter 5. | I | *at the background field `V`*; *nonlinear*; *non-flat* |
| the running value | 4:407, 418, 533; 6:878, 1155 | The coupling `β ∈ [β̂/2, 2β̂]` ("the actual coupling band"), as opposed to the reference value `β̂_m`. | R | *the coupling `β`* vs *the reference coupling `β̂`* |
| of this construction | 5:302, 751, 782, 1324, 1379, 1380; 6: about 11 uses, e.g. 137 ("rows actually used"), 305, 342, 1022, 1162 | The specific kernels, parameters or action fixed by the construction, as opposed to an arbitrary admissible choice. | I | delete, or *the … constructed above* |
| exact (emphatic) | 5:1052, 1071, 1303, 1374, 1382 | "Its actual quadratic Taylor coefficient": the true coefficient, not an approximation; 5:1057 calls the same hypothesis "an exact coefficient condition". | R | *exact*, or delete |
| determined by the configuration | 6:78, 1343 | "The actual coarse large-field set", as opposed to the stored or selected one ("the stored coarse large-field indicators equal the actual coarse large-field indicators"). | R | *the large-field set of the configuration* |

`selected` and `chosen` are used as near-synonyms of the sense "of this construction" (5:738, 858, 1314, 1378; 6:134–177, 362; e.g. 5:738 "Convergence of the selected Gaussian rows", 6:177 "an invariant of the selected construction"). Proposal: delete or replace by *fixed*.

#### 1.3 `selection`, `selected`, `selector`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| large-field selection | 6:49–51 and about 27 further | A triple `A = (A_f, A_n, A_c)` of fine plaquettes, coarse mismatch edges and coarse sites (6:49–51); as such it satisfies no condition. `A_f` and `A_n` are chosen indices, not sets determined by the configuration: a *consistent* selection (6:54–63, section 2.4) requires the variables to be at least moderately large on them (`r_p ≥ t_f/4`, `n_e ≥ W t_f`) and at most `t_f/2`, `2W t_f` off them (6:56–59), so the thresholds overlap. `A_c` is determined by the configuration: it is "exactly the set of coarse sites incident to plaquettes with `r_p^c > t_c`" near `A` (6:62–63), and the allocation takes it "to be the actual coarse large-field set" (6:77–78). | D | *large-field index triple* `A` (no adjective: a bare selection satisfies nothing); keep it distinct from `Bad_m(U)` (section 2.4) |
| retained | 6:1405, 1435, 491–505 | A component of the affine map kept in `D` (the component sense of `row`, fourth row of the table in section 1.1). | R | *retained* |
| chosen | 4:160, 210, 383, 393, 456, 616; 5:738, 858, 1378; 6:134, 165, 177, 362, 1557 | Chosen by the random index, or fixed by the construction (the sense "of this construction" of `actual`, section 1.2). | I | *chosen*; *for every value of `α`*; *fixed* |

In chapter 6 a "selected row" (retained component) lies far from the "selected set" (large-field set); the two senses must be separated. One classification of the 44 occurrences of `select*` in chapter 6 gives 28 for the large-field selection, 11 for retained components or stencils and 5 for "fixed by the construction"; the assignment was not repeated occurrence by occurrence.

#### 1.4 `test`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| condition | 4:65–106, 209 ff.; 5:967 | A Borel condition on the configuration deciding which case of a definition applies ("loop test", "eligibility test", "minimum-cost test"). The minimum-cost test compares the minimum of the block-average objective `P_e` with `ε_pred` (4:391†). | I | *condition*; *smallness condition* |
| variable | 6:320, 337, 604 | The numbers `r_p`, `n_e` compared with thresholds ("every fine or mismatch test … is at most `t_hi`"). | R | *plaquette and edge variables* |
| location | 6:19, 54, 79, 89, 323, 416, 1156, 1162, 1329, 1349 | The plaquette or mismatch edge itself ("on all tests meeting `A^[5B]`", "tests exceeding `t_hi`"). The most frequent sense in chapter 6. | R | *plaquettes and edges* |
| indicator | 4:483–493; 6:83, 109, 231, 687, 776, 920, 1324, 1340, 1416 | The indicator of such a condition; `χ^rel` (defined at 4:483–487†; called "the relaxed small-field test" at 6:108–109†) is `1{χ(U_p) ≤ t_m e^{dist/R^rel} for every p}`. Not a smooth cutoff: "fixed Borel tests. Their indicators are not differentiated" (6:687). | D | *indicator of the small-field condition* |
| test function | 3:147†, 319†; elsewhere in the book | Standard. | — | keep; reserve *test* for this |

This agrees with `blueprint/notation.md`, which reserves "test" for test functions.

`event indicator` alternates with `test` in the indicator sense already in these chapters: three times in chapter 4 (4:507† "its event indicator may read additional adjacent plaquettes", 4:532†, 4:658† "extra tests and event indicators") and eight times in chapter 6 (e.g. 6:1022). It is the better of the two words and could replace `test` in that sense throughout.

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
| stationary point | 6:947, 953, 967, 972, 1493, 1545 | "The stationary fine response to a coarse logarithmic field `h`", `a = 𝒰_F h` (6:953). The text names it without a formula; that it is the critical point of the quadratic form of chapter 5 is inferred. The symbol `𝒰_F` occurs only at 6:953 and 6:976 and is neither defined nor identified with the maps `W`, `W_a`, `W_F` of chapter 5. "Response" names the field `a` at 6:953 and the operator at 6:972 ("has a bounded row norm"). 6:846 "block average response" may be a different object. | R / I | *stationary (critical) fine field*; say *minimiser* only where a gap is proved |

#### 1.7 `transport`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| stationary-field map | 5:453–534 and about 20 further; 6:135 (at 6:161 only inside a label name) | `W`: coarse field ↦ stationary fine field of the Gaussian block step (`QW = I − b⁻¹K_c`; 5:105 "sends a coarse field to the stationary fine field"), and its companion `T` on two-forms. Minimality is asserted only for specific objects (5:1118†, 1144†). | R | *stationary-field operator `W`*; *induced map `T` on curvatures* |
| image under a lattice symmetry | 6:966 | "Each signed orientation with its transported forest". | R | *image of the forest under the symmetry* |
| parallel transport | 5:1003, 1008; 6:179–186, 217 | Holonomy along a path; "transported kernel" = flat kernel made gauge-covariant by parallel transport along fixed paths. | R | *parallel transport*; *covariantised kernel* |

#### 1.8 Other words with two or three senses

| Word | Senses and places | Basis | Proposed wording |
|---|---|---|---|
| `anchor` | (i) distinguished site of a support, 4:435, 506, 573; 6:90, 190 ff.; (ii) site `a_i` attached to a coordinate, 5:1204; (iii) real base point of a holomorphic weight, 5:902 | R | *base point*; *site of the coordinate*; *real part `x`* |
| `eligible` | (i) pair `(z,o)` satisfying the axial bound, 4:68–75; (ii) an extra gauge-invariant event, 4:442 | D / I | *pair satisfying the axial bound*; *additional event* |
| `centered` | (i) zero-mean, 3:580–584; (ii) about a point: `x₀` at 3:699, the anchor `o_i` at 4:628; (iii) normalised, 4:132; (iv) symmetric about the origin or block centre, 5:202, 307, 341, 916. "Centered log determinant" (5:1338) is undetermined (section 4). | D / I | *zero-mean*; *about `x₀`*; *normalised*; *symmetric* |
| `separation` | (i) displacement `x − y`, 3:61†, 431†; (ii) nondegeneracy property, 3:973†, 981†; (iii) of singularities, 3:854† | I | *displacement*; *nondegeneracy* (the same word as proposed for `detection`, section 2.5) |
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
| history; blocking history; history depth | 5:303–305; 18 prose occurrences on about 17 lines (25 occurrences counting label names) | Odd ratios `L₁,…,L_n ≥ 3` and averaging orders `j₀,…,j_n ≥ 4` with `j_{h−1} − j_h ∈ {0,1}`. | D | *sequence of blocking parameters* |
| nested histories; (nested, scale) schedule | 4:421; 5:703–707, 740, 1378; 6:1557 | Parameters fixed at every scale, only the ultraviolet cutoff `N` increases. | R | *fixed parameter sequence `(L_m, j_m, ζ_m)`, with increasing cutoff* |
| terminal cutoff; terminal scale; horizon (labels only) | 5:705–706; labels `ch05:horizon-*` | The finest scale `N`. Note that "terminal" names the scale where the flow *starts*. | R | *ultraviolet cutoff `N`* |
| observation scale | 5:700 | The fixed scale `m` while `N` varies. | I | *fixed scale `m`* |
| suffix | 5:378–380, 394, 418, 779 | Steps `h+1,…,n`. | D | *subsequent (coarser) steps* |
| step; update; nonlinear step | 5:1380; 6:950 | One renormalisation transformation, or its index. | I | *renormalisation step*; *scale* |
| stage | 4:651†; 5:689†; 6:21†, 96† | Probably the *regularity stage* of chapter 10, not a renormalisation step: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds … At a fixed stage there are only finitely many permitted adjacent pairs" (ch. 10:25–31), to be compared with 5:689–690 "For each adjacent pair of stages choose the coarse modification large enough for its finitely many incoming possibilities" and 6:21 "Fix a stage, a block ratio `L`, the penalty `b > 0`", 6:96 "The constants may depend on the fixed stage and ratio". Chapter 4 keeps the two apart ("a regularity-stage index `J_m`; that index is different from the scale `m`", 4:651–652), and chapter 6 writes "step" where it means the step (6:950). Chapters 5–6 do not say this themselves; the reading "renormalisation step" is not excluded at 5:689. | I | *regularity stage*, defined or referenced at first use; do not replace by *step* |
| adjacent pair (of scales, of stages); adjacent quadratic pair | 5:689†; 6:13†, 946†, 1553†; ch. 10:30† | The fine and the coarse scale of one step, with the data attached to them ("We work at one adjacent pair of scales", 6:13). Not defined; at 5:689 the pair is of stages. | R / I | *two consecutive scales*; *the fine and coarse data of one step* |
| total dilation `M`; total ratio | 5:240, 305, 757; 5:379–380† | `M_h = L₁⋯L_h` (5:305), the total dilation over several steps. "Total ratio" occurs once and refers to a suffix: "that suffix has total ratio `D = M_n/M_h`" (5:379–380). | D | *total scaling factor*; *scaling factor of the steps `h+1,…,n`* |
| period; torus side; torus size | 5:320, 446, 731, 916 | Side length of the periodic lattice. | R | *side length* (one word) |
| cover; covering lattice; cover coefficients; cover row | 4:18; 5:735†, 751, 806–849 | `ℤ⁴` as universal cover of the tori; the kernel on `ℤ⁴` as opposed to its periodisation. | R | *the infinite lattice `ℤ⁴`*; *infinite-volume kernel* |
| period recovery | 5:730–733, 828, 849 | An infinite-lattice kernel is the limit of its periodisations on tori of unbounded size. | R | *infinite-volume limit of the periodised kernels* |
| nonwrapping / wrapping support | 4:627, 642 | Support that does not wind around the torus. The text gives no criterion. | I | state the condition explicitly |
| fine residue | 5:654, 660, 713 | Position `r` of a fine site in its block, `x = Ly + r`. | R | *position within the block* |
| incoming; inherited | 5:306, 690, 1058 ff.; 6:379, 671 and 17 more | Belonging to the input of the renormalisation step. | I | *from the previous step*; *input* |
| exact (blocking, block map) | 4:2, 5, 169, 232, 289†, 569 | The block kernel is a probability kernel, so the partition function is preserved. | D (4:289) | *normalised block-spin kernel* |
| smoothing order `j` | 4:16, 186; 5:196–202 | Number of box convolutions in the averaging weight. | D | *order of the averaging kernel* |
| block penalty `b` | 4:226; 5:88; 6:21, 125 | Constant in the Gaussian block weight `exp(−(b/2)‖Qa − v‖²)`. | D | *constant of the block-spin kernel* |
| noise; accumulated / suffix noise | 5:250–251†, 377–378†, and about 10 further lines | The independent Gaussian `b^{-1/2}ξ` in `v = Qa + b^{-1/2}ξ` (the decomposition is at 5:126–130, where the word is not yet used), and its propagated contribution ("The independent noise introduced at step `h` is propagated only through the suffix", 5:378–379). | R | acceptable; or *the `b⁻¹` term* |
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
| uniform mass; branch masses; positive mass / likelihood (of tags) | 4:77, 209†, 315; 5:970; 6:63–64†, 671†, 1107†, 1344–1345† | The weights `λ(U,α)` of the random index. For tags the two words are used in parallel sentences ("Every chosen frame tag must have positive mass", 6:63–64; "Retained frame tags have positive likelihood", 6:1344–1345), so there they name the same weights (inferred from the parallel). | I | *probability weights `λ(U,α)`* |
| likelihood tests / factors | 6:920†, 1016† | A second referent of `likelihood`: probably the allocation weights `ϑ_f`, `ϑ_n` and `1 − ϑ` of 6:68–76. They are "on their plateaux" when the plaquette distance is below `t_f/4` and the block-average discrepancy below `W t_f` (6:1014–1016), which are the lower thresholds of `ϑ_f`, `ϑ_n` (6:68–70); these weights are the only factors found in the chapter with plateaux at those values. Inferred from the thresholds; the text does not name the factors. The other reading, the weights `λ(U,α)` of the previous row, does not explain the thresholds. | I | *allocation (partition-of-unity) weights `ϑ`*; confirm with the author |
| connector | 4:175–184; 5:986 | `Y_{e,z}`: frame-conjugated product of `L` fine links along a straight path. | D | *gauge-transformed parallel transporter* |
| `Q^pred`, `ε_pred`, `r_pred` | 4:202–210, 239, 287, 386–391; 6:460†, 501 | The block average with its label, and its threshold. The superscript is never explained in the chapters: "predictor" occurs there only in label names (`ch04:predictor-*`). The translation table `notation.md` glosses `Q_e^pred` as "gauge-covariant block average" (source label `eq:I12-predictor`). `r_pred` occurs once (6:460, a radius) and is not defined. | R | *block average*; rename the superscript |
| route; route matrices; walk | 4:107, 109; 5:995, 1003; 6:180 ff. | Lattice path; its holonomy. In 6:1025 "route" also means "method". | I | *path*; *holonomy* |
| feedback matrices | 4:124–133 | `F_x(h) = av h_y W_{xy;o}⁻¹`. | D | *local mean* |
| straight (average, transport) | 5:535, 859, 993, 1084 | The linear average `M` without the gradient correction. | D (5:993) | *linear block average* |
| first-power (bound, estimate) | 4:293, 308–312; 5:1007 | A bound linear in `χ`, as opposed to a square-root consequence of a squared-energy bound. Never defined; read off 4:308–310. | R | *linear bound* |
| forest; forest coordinates / chart / slice | 5:916–935; 6:516, 629, 966 ff. | A rooted spanning tree in each block; coordinates `(v, ψ)` with `ψ` on non-tree links. | D | *maximal-tree gauge in each block* |
| tree slice; tree coordinates; tree-straightened | 5:916 ff.; 6:466–490, 972, 1492 | Gauge slice where tree links equal the identity. | I | *tree gauge* |
| tree comparison | 4:296; 5:1000, 1036–1040, 1289 | The inequality `‖a‖² ≤ B‖d₁a‖² + C‖𝒬a‖²` for `a` vanishing on tree links. | D (ch. 5) | *Poincaré-type inequality in the block-tree gauge* (the text reserves "coercivity" for the resulting Hessian bound, 5:1143) |
| replica `rep V`; replicated field; parent | 5:920–929; 6:180, 341 ff.; ch. 1:218–220† | Fine field equal to `1` inside blocks and to `V` on links between blocks (defined). The "parent" of a fine site `x = Ly + z`, `z ∈ {−(L−1)/2,…,(L−1)/2}⁴`, is the coarse site `y`; the "parent map" is defined in chapter 1 (1:218–220), not in chapters 3–6. | D | *pull-back of `V` under the block projection* (5:1137 uses "block-constant extension" for something else) |
| vertical (coordinates, Hessian, gap) | 5:944, 1078, 1334, 1339 | The fluctuation variables `ψ` at fixed `v`. | I | *in the fluctuation variables* |
| stationary graph / tangent / background | 5:1145–1180 and 25 lines | `ψ = ρ(v)` solving `D_ψ f = 0`, and its derivative at zero (defined). "Background" is used in titles and in prose (5:7†, 14†, 1222†, 1287†) without a definition; the nearest to a gloss is 5:1286–1287, the action "whose germ at zero defines the background". | D / I | *critical-point map*; *background field* |
| frozen (links, logarithms) | 6:442 and 26 more | Non-tree ("free") links near the large-field set, held fixed in the Gaussian integral and integrated afterwards. | I | *conditioning variables* |
| free (links, bonds, edges, coordinates) | 5:918†, 1161†; 6:442†, 443†, 489†, 588†, 1376† | The links not in the block trees, i.e. the non-tree links: "free bonds, and zero on tree bonds" (6:1376); "Tree links are not integration variables. Active coordinates are logarithms of the remaining free links" (6:442–443). Not defined. Collides with "free field" and "free polynomial space" of chapter 3 (section 2.5). | R | *non-tree links* |
| logarithm; logarithmic field; link logarithms | 5:100†; 6:443†, 694†, 953–954†, 1255†; about 28 occurrences in ch. 4–6, 25 of them in ch. 6 | The Lie-algebra coordinate of a link or of a link increment ("unscaled link logarithms", 5:100; "coarse logarithmic field `h`", 6:953–954; "frozen logarithms"; "local Haar logarithms", 6:1255). Not defined as a term; the reading as the exponential coordinate is inferred from these uses. | I | *Lie-algebra (exponential) coordinate of the link*; acceptable if stated once |
| distance from the identity; mismatch distance; (squared) group distance | 4:56†, 337†, 397†; 6:49†, 1014†, 1404†; 9 + 2 + 13 lines in ch. 4, 5, 6 | `χ(U)`, the normalised Hilbert–Schmidt distance of a group element from the identity (4:56; 6:49). The phrase is written out where a symbol would do: "adds a nonnegative squared distance from the identity which is zero at the minimizer" (4:337), "mismatch distances from the identity" (4:397), "the squared group distance" (6:1404). | D (4:56) | define `χ` once and write `χ(U_p)`, `χ(·)²` |
| active / inactive coordinates | 6:443 | Logarithms of non-tree links outside the `10B`-neighbourhood. | D | *integration variables* |
| signal `ũ` | 6:1373–1383 | The active increment, extended by the clipped frozen logarithm and zero on the tree. | D | *displacement field* |

#### 2.3 Effective action and its pieces

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| density coordinates; coordinate tuple | 4:8, 403, 469, 530, 550†, 656–676 | The data `(β, v_sc, regular activities, large-field activities)` parametrising a density. The text says that the tuples satisfying the norm bounds form a "much larger set" than the reachable outputs (4:674–677†) and that a tuple "need not give a positive density" (4:567†); it says nothing on injectivity. That these are therefore not coordinates in the usual sense is an inference. | D | *parametrisation*; *representation data* |
| regular activity | 4:433–438†, 452, 555† | `(X_i, o_i, E_i^reg)`: a local term entering the exponent additively. Not a polymer activity. | D | *local term of the small-field action* |
| scalar; `v_sc` | 4:9†, 550–551†, 555†, 658† | The constant term `−v_sc\|Λ\|` of `V_ρ`, where the density is `e^{−V_ρ}`; the text calls it "a scalar normalization". | D | *constant term per site*; *normalisation constant* |
| direct (row, term, coefficient `c_dir`) | 4:474; 5:749; 6:101, 137, 143 ff. | The single-plaquette term and its coefficient, as in `H = c_dir I + ρ*ρ` (ch. 7:974†). | I | *plaquette term*; *its coefficient* |
| path action `P^path`; prescribed leading action | 4:466, 496–521; 6 passim | The explicit leading part of the effective action. It includes the single-plaquette `clip` term (4:512) as well as the path sums, so it is not only the non-local part. | D | *leading part of the effective action* |
| admissible path action; path budget (label) | 5:1241–1252† (hypothesis, label `ch05:path-budget`); 5:1386† (the name) | A generic hypothesis: an action `Σ_γ c_γ ×` (local analytic term in holonomies along paths) with `sup_z Σ \|c_γ\| e^{σℓ(γ)} ≤ P`. The hypothesis is stated at 5:1241–1252 without a name; "the admissible path action" occurs only at 5:1386 ("These conditions will be imposed on the admissible path action"), and that it means an action satisfying this hypothesis is inferred. | R / I | *action with exponentially summable path coefficients* |
| atoms; quadratic path square | 5:1054–1056; ch. 9:573, 837† | Elementary terms of the path action, graded by degree in the curvature. | I | *elementary terms of degree `q`* |
| inherited (quadratic) loop action; loop correction; separate quadratic correction | 4:517†, 525†; 5:1045; 6:170, 1261–1262; ch. 7:237†; ch. 9:21–28† | The `β`-independent quadratic part `ℒ` of the path action: "`P^path_{N,m}(β,U) = β𝒦(U) + ℒ(U)`, where `𝒦` includes its cubic and quartic terms and `ℒ` is the quadratic loop correction. This identity defines `𝒦, ℒ`" from the path action (ch. 9:21–28). As the path action is affine in `β` with fixed coefficients (4:522–523), `ℒ` is its term not multiplied by `β`, `Σ A_i^(2)` (4:517), which 4:525 calls "the separate quadratic correction". Ch. 7:237 "`ℒ_{m+1}` is the inherited quadratic loop action"; 6:170 "the separate loop correction is not part of the classical metric". The text does not fix a loop order. ("Order four" in ch. 7:1160 is a property of its symbol.) | R (ch. 9) | *`β`-independent quadratic term `ℒ` of the path action* |
| kinetic operator | 5:44–46† | `K = d₁*Hd₁`, the operator of the quadratic action `S₀(a) = ½⟨d₁a, Hd₁a⟩`. | D | *operator of the quadratic form*; or keep, but then do not call `K_f(p)`, `K_c(p)` of chapter 6 "kinetic energies" (below and section 5) |
| (curvature, two-form) metric; metric modification; positive completion | 5:43–46, 227–235, 286–291, 456; 6:139, 163 | Positive operator `H` on two-forms with `K = d₁*Hd₁`; the modification `H⁻¹ = H₀⁻¹ + ζ(d₂H₀⁻¹)*(d₂H₀⁻¹)`. | D | *quadratic form on two-forms*; *coefficient operator* |
| (curvature) defect; amended defect; positive-defect identity | 5:638–641, 603; 6:135, 145, 176 | `Z₀ = B_c − T*B_fT − b⁻¹d₁d₁*` with `B = H⁻¹`, and its version with modified metrics, with `K*K = Z ≥ 0`. In 6:213 "the two signed defects" are instead `E_L`, `E_D`. | R | *positive remainder in the recursion for `H⁻¹`* (no standard name known) |
| aligned; alignment premise | 6:136–141, 164 ff. | `C_ν*C_ν = H_ν`: the components of the action factorise the chosen two-form operator `H_ν` (the Hessian is `d₁*H_ν d₁`). | R | *factorisation of the two-form coefficient operator* |
| quadratic coefficient condition | 5:1052–1058 | The quadratic Taylor coefficient of the input action is `d₁*H_f d₁` with `H_f ≥ εI`. | D | *hypothesis on the quadratic part* |
| uncut (action); plateau | 5:973†, 1044, 1241; 6:281†, 917 ff. | Without the smooth small-field cutoffs; region where a cutoff equals one. | I | *without cutoff functions*; *where the cutoff equals one* |
| clip; clipped; capped | 4:476–480, 528; 6:109–121 | `clip_t`: quadratic below `t`, linear above, with a downward jump at `t` (4:528). "Capped": multiplied by `min(1, t_c/r)`. | D | keep the symbol; *piecewise quadratic–linear function* |
| relaxed (`χ^rel`, `R^rel`) | 4:483–487† (definition); 6:108–109† (the word) | Indicator of the small-field condition with threshold `t_m e^{dist/R^rel}`. In chapter 4 the word appears only in the superscript and in the label `ch04:relaxed-test`; the first prose use is "the relaxed small-field test" (6:108–109). | D | *exponentially weighted small-field condition* |
| kinetic energies `K_f`, `K_c` | 6:110 | Clipped plaquette action plus cut-off path square. Nothing kinetic. | R | *local action density* |
| comparison term | 6:186–188† | The specified quantities `Φ v_c` and `Φ_n v_c` (defined). That they are the fine curvature and mismatch predicted linearly from the truncated coarse curvature is inferred. | D / I | *linear prediction from the coarse field* |
| six anchored quantities; local energy `𝓔_A`; core energy | 6:190–213†; 6:80†, 1327† | The six local terms `E_f, E_n, E_c, E_N, E_L, E_D` (6:190–200), each evaluated at a plaquette, edge or complement-component anchor, whose sum over the torus is `ΣK_f + (b/2)Σ n_e² − ΣK_c` (6:205–208). The local energy `𝓔_A` is the sum of the six terms at anchors in `A^[2B]` (6:210–212). "Core energy" (6:80, 1327) is not defined; presumably `𝓔_A` (inferred). | D / I | *local energy `𝓔_A`* (keep, it is defined); write `𝓔_A` for "core energy" if that is meant |
| full maps | 6:948†, 987†, 1006† | Not defined. Read as the untruncated maps `M_f`, `M_n` of the flat identities, as opposed to their transported and truncated versions `Φ`, `Φ_n` in the comparison term ("the comparison term defined by transporting and truncating those full maps", 6:947–948). | I | *the untruncated maps `M_f`, `M_n`* |
| coarse counterterm | 6:1407 | The term `E_c`. Not a renormalisation counterterm. | I | *subtracted coarse energy* |
| affine stack | 6:446–452 | The vector `Du + b_Y`. | R | *the affine map `u ↦ Du + b_Y`* (avoid "residual", which the chapter uses otherwise) |
| source (`b_Y`, `f_Y`) | 6:448–449, 581–612 | `b_Y` is the inhomogeneous term of the affine map; `f_Y = D*b_Y` is the linear coefficient of the quadratic form. | R | *inhomogeneous term*; *linear coefficient* |
| extracted; Gaussian extraction | 6:1251, 1280, 1326 ff. | After the affine squares are moved into the Gaussian measure. | I | *after completing the square* |
| local transfer identity | 6:924–931, 942 | `m_Y − v = E*v − P*(Av + f_Y)` with `E = AP − I`. (The subsection at 6:466, "Transferring a local tree estimate", is a different statement.) | R | *comparison identity for the mean* |

#### 2.4 Large-field regions, supports and localisation

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| `Bad_m(U)` | 4:425 | Sites incident to a plaquette with `χ > t_m`; determined by the configuration. | D | *large-field set of `U`* |
| consistent (selection, sector) | 6:54–63† | The threshold inequalities of 6:56–59 hold on `A^[5B]` with overlapping margins, and `A_c` is exactly the set of coarse sites incident to plaquettes with `r_p^c > t_c` there (section 1.3). | D | keep *consistent*, which the text defines; if a replacement is wanted, *admissible large-field triple*, and then *admissible* must not also be used for the bare selection |
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
| containing-site bound; halo; support exponent | 4:603–606; 6:1170–1178 | `sup_x Σ_{λ: x ∈ S_λ} e^{α c_B(S_λ)} a_λ ≤ ε` (defined); the `hB`-neighbourhood of a support ("a halo multiplier `h`", 6:1170†; "its projected `hB` halo", 6:1297†); the rate `α`. | D / R | *weighted polymer-activity norm*; *neighbourhood*; *decay rate* |
| cutoff remainder; large-coordinate event; small-coordinate event | 6:739†, 834–843†, 892–897†, 1040† | The central objects of the tail estimates of chapter 6. "A cutoff remainder is bounded but need not be pointwise small. Its smallness comes from a large-coordinate event" (6:834–835): a remainder with event label `w` vanishes unless `ℰ_w = {∃i: d(i,w) ≤ 2B, \|z_i\| ≥ T}`, `T = ξ t_f/(2g)`, occurs (6:837–843). On the complementary "small-coordinate event" `v = m_Y + gz` has size `O(t_f)` (6:897). The remainder itself is not defined; that it is the difference produced by a smooth cutoff being different from one is inferred. These Gaussian-tail events are distinct from the large-field selection `A` and from `Bad_m(U)`, which the chapter treats by a separate mechanism (6:7–11†). `Warnings` (section 4) probably refers to them. | R / I | *cutoff remainder* (acceptable once defined); *the event `{\|z_i\| ≥ T for some i near w}`*; do not call it a large-field event |
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
| detection; detector (labels) | 3:830† | `P ∉ N_D`: some correlation is nonzero. The text's own word nearby is "separates", "separating family" (3:775†, 779†, 806†). | I | *nondegeneracy* (as for sense (ii) of `separation`, section 1.8); if the text's *separating family* is preferred, use it in both places and keep *separation* for nothing else |
| Ward sum | 3:915 | `W_A = Σ_i S_n(P₁,…,AP_i,…,P_n)`. | D | *action of `A` as a derivation on the correlation* |
| charge | 3:780 | A symmetry generator acting on fields. | I | *infinitesimal generator* |
| flux; local Ward / stress flux; shell flux | 3:546, 656–671 | `F_{χ,v} = −∫ ∂_aχ v_b S(T_ab, …)`. | D | *smeared charge of the current `T_ab v_b`* |
| pole; harmonic pole; "cleared by" | 3:865–876, 964 | Homogeneous singularity `\|z\|^{-r}` at the origin of `ℝ⁴`. | I | *homogeneous singularity of degree `−r`*; *becomes smooth after multiplication by* |
| collision | 3:146, 832, 879, 914, 1016 | Coincidence of insertion points. | I | *coincident points*; *short-distance limit* |
| free image; polynomial image; free polynomial space | 3:194–224, 784 | `M_d^Max = im ω_d`. Five names for one space. | D | *space of on-shell polynomials* (one name) |
| correlation-null | 3:216†, 523† | Vanishing in every separated correlation. | R | *in the kernel of the correlation functionals* |
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
| supplies; the supplied construction | 3:547†; 5:195, 1217 ff. | "Gives"; presumably the construction being transcribed (the text does not say who supplies it). | *gives*; *the present construction* |
| assigned; ownership | 6:85, 421, 1162, 1329–1335 | Which component a term is attributed to. | *attributed to* |
| subpower | 6:822–823† | Defined there: `A_k(x) ≤ C_ε x^ε` eventually, for each `ε > 0`. | `x^{o(1)}` |
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
| renormalisation step | step, update | *step*. `stage` does not belong here: it is probably the regularity stage (section 2.1) |
| side length of the torus | period, torus side, torus size, volume | *side length* |
| satisfying the standing constraints | admitted, permitted, allowed, admissible | *admissible*, with the conditions stated |
| enlarged block | macro-box, macro-patch | *enlarged block* |
| support of a local term | footprint, stencil | *support of the expression*; do not merge with *dependence set*, which the text distinguishes (4:507) |
| the random index | label, tag | *index `α`* |
| its weights | mass; likelihood where it is said of tags (6:1345) | *weight `λ(U,α)`*. "Likelihood tests / factors" (6:920, 1016) are probably different weights (section 2.2) and must not be merged |
| base point of a support | anchor, root | *base point* |
| subsequential limit | cluster limit, cluster symbol | *subsequential limit* |
| on-shell polynomial space | free image, polynomial image, free polynomial space, free spaces | one name |

---

### 4. Terms whose meaning chapters 3–6 do not determine

These need the author, the formal source, or a cross-reference before any replacement is made. Five terms originally listed here were resolved by the independent check and are in section 4.1.

| Term | Where | What can be said |
|---|---|---|
| moving comparison fields | 3:576† | Not defined anywhere in the book. Possibly the cutoff-dependent fields of ch. 11 ("moving equation space", 11:1083). "Moving labels" recurs elsewhere with one meaning, labels that vary along the sequence while converging (`14-reflection-ward.tex`:238†, 250†; `17-trace-law.tex`:97†), which suggests "comparison fields that vary with the cutoff" (inferred). |
| regularity-stage index `J_m` | 4:651† | An index distinct from `m` on which `q, ϖ, σ` may depend. Settled outside chapters 3–6 (section 4.1a); see also `stage` in section 2.1. |
| centered log determinant | 5:1338 | Presumably `log det H(v) − log det H(0)`. |
| output anchors | 6:90 | Probably anchors on the coarse (output) lattice: `H` indexes the sums of `E_L + E_D` (6:287), and "every coarse plaquette with `r_p^c > δ` lies in `H`" (6:295). Inferred. |
| compulsory (component region, cutoff factor) | 6:1018†, 1461† | Possibly the chart cutoffs "retained throughout `304B`" (6:1350–1351†) belonging to the component factor; this fits 6:1461 ("where a compulsory cutoff factor vanishes the full component factor is zero"). Ch. 10:654† uses the word for another noun ("one compulsory large-field factor") and does not determine "compulsory component region". Open. |
| Warnings | 6:1476 | Capitalised, undefined. Probably the cutoff remainders indexed by event labels (6:834–843; row `cutoff remainder` in section 2.4); ch. 11:319 has an "actual warning estimate". Inferred. |
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

See Part I, section 3. In short: `regularity-stage index J_m` is defined in chapter 10 (10:25–31†, 129–134†: `J(m)` is the stage in force at level `m`, a stage being a finite set of orders, exponents and bounds); the translation table `notation.md` agrees ("`J_m, q_j, ϖ_j, σ_j`: stage, derivative order, spatial power, support exponent … not interchangeable with scale `m`"). `inherited loop action` is the `β`-independent quadratic part `ℒ` of `P^path = β𝒦 + ℒ` (9:21–28†; row in section 2.3). `parent` is defined in chapter 1 (1:218–220†; section 2.2). `Warnings` are probably cutoff-failure events (11:319), and `centered log determinant` is probably `s(x) − s(0)` with `s = ½ log det A` (9s:47, 59). Narrowed but not settled: `likelihood tests / factors` (probably the allocation weights, section 2.2); `moving comparison fields` (table above); `compulsory`, which 10:654 uses only in "one compulsory large-field factor" and so does not settle for the chapter 6 phrases. Still open after a search of all chapter files, `main-theorem.tex` and `reading-guide.tex`: `seeded / unseeded` (only 6:1544 and 9:283–284), `output anchors` (only 6:90).

#### 4.2 House terms not yet glossed in detail

Reported by the independent check as missing from the dictionary. Meanings are as that check read them; they were not rechecked, except that a later spot check found the term at every cited line. The last three rows (`residual`, `principal`, `base`) were added afterwards; their cited lines were opened (†), and their readings are inferred from the quoted phrases.

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
| residual | 5:1072†; 6:564†, 575, 639, 668†, 1080†, 1090†, 1214, 1257, 1404†, 1406 | Several senses: what is left of an identity or equation ("its residual vanishes at zero", 5:1072; the residual of a column of the approximate inverse outside its window, 6:564); a leftover linear or quadratic term in an exponent (6:668, 1214); the "residual Gaussian density" (6:1080, 1090); "nonlinear residual squares" (6:1404). |
| principal (beyond the alias sense of section 2.1) | 5:541†; 6:548†, 753†, 1494† | "Principal covariance split" (5:541), not glossed; "principal compression" (6:548), the principal submatrix of section 2.4; "principal covariance block `Γ_I`" (6:753), the diagonal block of the covariance on an index set `I`; "principal resolvent identity" (6:1494), not glossed. |
| base (field, point, parameter, affine row, row remainder) | 6:694†, 738, 809†, 981†, 1278† | The reference point of an expansion or change of variables: "at a base field `V_0`" (6:694), "at the base point `T_{V_0}z = z`" (6:809); "base affine row" (6:1278) and "base-row remainder" (6:981) are the affine component and its nonlinear remainder at that point (inferred). A further synonym of `anchor` in its sense (iii) (section 1.8). |

---

### 5. Symbols with several meanings

Not terminology, but they compound the difficulty.

| Symbol | Meanings |
|---|---|
| `M` | averaging operator (5:156); total dilation (5:240) |
| `H` | two-form metric; frame variable `H_{y,r}` (5:980); axial gauge; Hessian; output anchors (6:90); tail parameter (6:854); annulus rows (6:1355) |
| `R` | `d₁*Hd₁` (5:474); frame operator (5:981) |
| `D` | covariance (5:468); suffix ratio (5:380); large-field subset (6:89); matrix `AΓ − I` (6:1186) |
| `W` | stationary-field operator `W = A⁻¹bQ*` (5:92†; see `transport`, section 1.7); lift `W₀` (5:626†); threshold multiplier (6:54†); annulus energy (6:1387†) |
| `K` | kinetic operator `d₁*Hd₁` (5:46†); operator (6:145†); counting constant (6:93, 1221); majorant matrix (6:1100) |
| `K_f`, `K_c` | fine and coarse quadratic-form operators, `K_c = bI − b²QA⁻¹Q*` (5:89–93†); the local quantities `K_f(p)`, `K_c(p)` = clipped plaquette term plus cut-off path square (6:115–118†). Related letters: large-field activity value `K_i^lf` (4:443†); `𝒦` in `P^path = β𝒦 + ℒ` (ch. 9:23†) |
| `χ` | normalised Hilbert–Schmidt distance from the identity (4:56†; 6:49†); smooth cutoff function (3:664†; 6:705–706†); indicator `χ^rel` (4:483†) |
| `w` | plaquette energy; averaging weight `w^av` (4:186–192); box symbol; penalty function (5:1048) |

Symbols used without a definition in these chapters: `𝒰_F` (6:953†, 976†, its only occurrences; see `response`, section 1.6); `r_pred` (6:460†, its only occurrence); `a_*` (6:733–736†; no definition in chapter 6, other chapters not searched).

---

### 6. Suggested order of work

1. Fix the multi-sense words of section 1 (the seven groups of sections 1.1–1.7 and the eleven further words of section 1.8); each change is local once the sense is identified.
2. Resolve the section 4 terms with the author or the formal source; do not replace them by guesswork.
3. Apply the synonym reductions of section 3 mechanically.
4. Either define once and keep, or replace, the house terms that are harmless when defined (`polynomial label`, `insertion`, `word` in sense (i), `history`, `smoothing order`, `forest coordinates`, `Ward sum`).
5. Rename the Lean-flavoured equation labels (`ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`) only if labels are being touched anyway; they do not appear in the PDF.

---

### 7. Method and limits

- **Data gathering.** Three independent agent surveys, one for chapters 3–4, one for chapter 5 and one for chapter 6, each reading its chapters in full and reporting every non-standard term with line numbers, the decisive sentence, and whether the meaning was read or inferred. They returned 34 + 48, 69 and 93 entries.
- **Harmonisation.** The entries were merged by concept, the proposed equivalents made uniform across chapters and aligned with `blueprint/notation.md`.
- **Checks.** A self-audit by the agent that wrote the note, an independent check by a fresh agent, and a later re-audit by a further agent; their corrections are all applied in the tables above. See "Changes folded in" and "Verification status" below.
- **Not done.** No formal-source declaration was consulted, so no claim is made about which Lean names the terms come from. No proposed equivalent was checked against the literature (Bałaban, Bałaban–Feldman–Knörrer–Trubowitz or others). Section 3 was not checked row by row by anyone (four of its rows were spot-checked); the occurrence counts given as "about" were not recounted. All of this is agent work and needs a mathematician's review; entries with basis **I** in particular may misread the text.
- **Agent assistance.** Claude Code (Claude Fable 5.2), with three subagents for the surveys, a fourth, given only this note and the chapter files, for the independent check, a fifth for the re-audit and a sixth for folding the re-audit into this text.
- **The † marks** on line references mean that the cited line was opened, and found to contain the term or formula, in the re-audit or in the fold of its corrections. Marks inherited from the self-audit were kept only where one of these two readings confirmed them. Most unmarked references in sections 1, 2, 4 and 5 were also confirmed by the re-audit (see "Verification status"); the mark was added only where the fold touched the row.

### Changes folded in

Origin: **R** = re-audit report (items E, D, the table of line references "L", the list "S" of terms settled by the text, and the omissions "O"); **own** = found while confirming. "Verified" means the cited chapter lines were opened during this fold. The corrections of the earlier self-audit and independent check were already in the tables and are not listed.

**Preamble and section 7**
- Path of the translation table given in full; its rule quoted exactly instead of paraphrased (R L354; verified in `notation.md`).
- Pipes inside formulas in four table rows escaped so that the tables render (own; formatting only).
- Meaning of † restated; sections 8 and 9 replaced by the two closing sections; note on two-part basis codes added (R D13; own).
- "Sections 3 and 5 were not checked by anyone" updated: the re-audit checked section 5 and four rows of section 3 (R, its confirmed list).

**Section 1**
- 1.1, 1.2 headers: counts replaced by recounted values, 19 on 18 lines and 82 for `row`; prose counts 4 / 23 / 48 for `actual` (R D10; counts taken from R, not recounted).
- 1.2 closing remark: "last sense" → sense "of this construction"; 5:1378 added (R E1; verified at 5:738, 6:177, 5:1378).
- 1.3 `large-field selection`: `A_c` is determined by the configuration, only `A_f`, `A_n` are chosen; the inequalities define a *consistent* selection; proposal "admissible large-field index set" → "large-field index triple" (R E3, D7; verified at 6:49–63, 77–78).
- 1.3 `retained`: "sense 5 of `row`" → the component sense, fourth row (R E2; verified in the table).
- 1.3 `chosen`: "5 and 6 passim" replaced by the lines; classification counts 28 / 11 / 5 of `select*` in ch. 6 added below the table (R D11; lines 5:738, 858, 1378, 6:134, 165, 177, 362, 1557 verified; the counts are R's).
- 1.4 `indicator`: the word "relaxed" is not in chapter 4 prose; references split into definition (4:483–487) and first prose use (6:108–109) (R L534; verified).
- 1.4: `test function` occurs at 3:147, 319 (R O15; verified); paragraph on `event indicator` in chapters 4 and 6 added (R E7; 4:507, 532, 658 and the count 8 in ch. 6 verified).
- 1.6 `response` (stationary point): `𝒰_F` undefined and not identified with `W`; the word names a field at 6:953 and an operator at 6:972 (R D6; verified by grep and at 6:953, 972, 976).
- 1.7 `transport`: 6:161 removed as a use (label name only); minimality reference 5:1143 → 5:1144 (R L438; own; both verified).
- 1.8 `separation`: 3:429 → 3:431; cross-reference to `detection` (R L449, D12; verified).

**Section 2.1**
- `history`: "24 lines" → 18 prose occurrences on about 17 lines (R L468; my grep gives 16 lines free of labels, so "about").
- `stage` separated from `step`: new row reading it as the regularity stage of ch. 10, basis I, with the alternative reading stated (R D1; verified at 4:651–652, 5:689–695, 6:21, 96, 950, 10:25–31).
- `adjacent pair`: row added (R O10; verified at 5:689, 6:13, 946, 1553, 10:30).
- `total dilation; total ratio`: `M_h = L₁⋯L_h`; "total ratio" is the suffix ratio `D = M_n/M_h` (R L474; verified at 5:305, 379–380; "total ratio" occurs nowhere else in ch. 4–6).
- `noise`: reference 5:126–130 → 5:250–251, 377–378 (R L484; verified).

**Section 2.2**
- `mass / likelihood`: parallel of 6:63–64 and 6:1344–1345 stated (R D5; verified).
- `likelihood tests / factors`: basis ? → I, read as the allocation weights `ϑ`, with the other reading stated (R D5; thresholds verified at 6:68–70, 1014–1016; that no other factor has those plateaux is R's observation, not rechecked).
- `Q^pred`: gloss from `notation.md` added; `r_pred` undefined, one occurrence (R S, O6; verified by grep and in `notation.md`).
- `parent`: basis D / I → D, defined at 1:218–220 (R E4; verified).
- `stationary graph / background`: "background" also in prose, lines given (R E8; verified at 5:7, 14, 1222, 1287).
- Rows added: `free` links (R O2), `logarithm` (R O4), `distance from the identity` (R O3); cited lines verified, occurrence counts by my grep.

**Section 2.3**
- `density coordinates`: the remark on injectivity marked as inference, with what the text says (R D16; verified at 4:567, 674–677).
- `regular activity` 554 → 555; `scalar` 554 → 550–551, 555 (own, following R's confirmed list; verified).
- `admissible path action`: name occurs only at 5:1386; basis D → R / I (R L525; verified).
- `inherited loop action`: identified with `ℒ` by 9:21–28 and 4:517, 522–525; basis R / I → R; "one-loop" withdrawn (R E9, D8; verified).
- `relaxed`: references as in 1.4 (R L534; verified).
- Rows added: `kinetic operator` (R O5), `six anchored quantities / local energy / core energy` (R O12), `full maps` (R O13); cited lines verified; the reading of `full maps` is R's and is marked I.

**Section 2.4**
- `consistent`: `A_c` clause added; proposal no longer shares "admissible" with the bare selection (R E3, D7; verified).
- `halo`: basis I → R, with 6:1297 (R S; verified at 6:1170, 1297).
- Row added: `cutoff remainder`, `large-coordinate event`, `small-coordinate event` (R O1, D2; verified at 6:7–11, 739, 834–843, 897, 1040).

**Sections 2.5, 2.6, 3**
- `detection`: one proposal instead of two, aligned with 1.8 (R D12; 3:775, 779, 806, 830 verified).
- `correlation-null`: 3:348 removed (R L579; verified). `the supplied construction`: 3:546 → 3:547 (R L593; verified). `subpower`: marked as defined, 6:822–823 (R S; verified).
- Section 3: `stage` taken out of the `step` cluster; `mass` / `likelihood` no longer merged unconditionally (R D1, D5).

**Section 4**
- `moving comparison fields`: "moving labels" parallel added (R S; verified at `14-reflection-ward.tex`:238, 250 and `17-trace-law.tex`:97).
- `compulsory`: 10:654 does not settle the chapter 6 phrases; removed from the "settled" list of 4.1a (R D3; verified at 6:1018, 1461, 1350–1351, 10:654).
- 4.1a: `parent` and the `notation.md` row for `J_m` added; `likelihood tests` moved from "open" to "narrowed"; the dangling sentence about 6:730 deleted (R E4, S, D5, E5; `notation.md` verified).
- 4.2: rows `residual` (R O9), `principal` (R O11), `base` (R O14) added; cited lines verified.

**Sections 5, 6**
- `W`: "minimiser operator" → stationary-field operator; `W₀` at 5:626, not 5:630 (R D15, L692; verified at 5:92, 626, 630).
- Rows `K_f`, `K_c` and `χ` added; `K` gains the kinetic operator; list of undefined symbols `𝒰_F`, `r_pred`, `a_*` added (R O6, O7, O8; verified).
- Section 6, item 1: "eleven" → seven groups plus eleven words (R E6; verified by counting).

**† marks.** Of the nineteen inherited marks, seventeen were confirmed (twelve by R's reading, five by mine: 3:61, 4:78, 4:209–217, 5:735, 6:281) and kept. Two were wrong and were replaced by the correct lines: 3:429 → 3:431 and 4:554 → 4:555. No mark was removed without replacement. Marks were added on the lines opened in this fold.

**Corrections proposed by R and not applied**
- R E7, D2, D4, D9, D11 (first half) and L226 concern statements of Part I only; Part II was already consistent with R on `eligible` (D4) and on the vocabulary of chapter 3 (D9). Left to the Part I fold.
- R D14 (thirteen "undetermined" terms against twelve now listed): a statement of the deleted section 9; nothing to correct in the tables. Recorded below.
- R O3's remark that "distance from the identity" looks like a mechanical replacement: a conjecture about the history of the text, not entered.
- R's item for `𝒦_m` in O8 is entered as `𝒦` (ch. 9:23), the form found in the text opened.

**Found wrong on inspection:** none of R's corrections for Part II. One imprecision: R cites "moving labels" as 14:238, 250; the lines are in `14-reflection-ward.tex`, which is written out here.

### Verification status

**What the earlier checks established.** The self-audit (by the author of the note) matched 409 of 421 line references against the term by script and reread about 45 defining passages; it corrected three line numbers and four entries. The independent check (a fresh agent reading the four chapters in full) checked every row of sections 1, 2 and 4, replaced the wrong senses of `test`, `actual`, `row`, `inherited loop action`, `connected covering number` and `noise`, lowered or raised a dozen basis codes, changed about fifteen proposed equivalents, resolved five "undetermined" terms (section 4.1) and reported the terms of section 4.2. Its record speaks of thirteen undetermined terms where sections 4 and 4.1 hold twelve; this could not be reconciled. The re-audit showed that the script result does not establish the line references: one †-marked reference and seven others did not contain the term (all corrected above).

**Checked against the text by a reader other than the author** (the re-audit's confirmed list, plus the lines opened in this fold):
- Section 1: all senses of `row`, `actual`, `test`, `label / tag`, `response`, `transport`, the definition of a selection and of consistency, and every word of 1.8, at the cited lines. The counts in the headers of 1.1 and 1.2 are recounts by grep.
- Section 2: nearly every row of 2.1–2.6 at its cited lines (the re-audit lists them); all rows of 2.5; the rows added in this fold at the lines marked †.
- Section 4: the open terms were searched for in all chapter files, `main-theorem.tex` and `reading-guide.tex`; 4.1 confirmed; 4.2 spot-checked only for the presence of the term at each cited line.
- Section 5: all rows at the cited lines.

**Resting on one reading only, or unverified.**
- The occurrence-by-occurrence classification of `row` and `actual` in chapter 6, and the counts 28 / 11 / 5 for `select*` (one reader each); all counts given as "about" (`transport`, `frame`, `stationary`, `frozen` and others).
- The meanings in section 4.2 (one check, not repeated), and the three rows added there (inferred from the quoted phrases).
- Section 3 row by row, apart from link / edge / bond, mass / likelihood, anchor / root and footprint / stencil.
- Whether each gloss of section 2.6 fits every listed occurrence.
- Chapter 3 outside the cited lines: the re-audit did not read 3:1–57, 64–143, 243–344, 473–519, 599–653, 713–725.
- The new readings with basis I introduced here: `stage` as regularity stage, `likelihood tests` as the weights `ϑ`, `full maps`, `core energy`, `logarithm`, the nature of a `cutoff remainder`.
- Every proposed equivalent: judged from general mathematical knowledge by agents; none was compared with the literature (Bałaban; Bałaban–Feldman–Knörrer–Trubowitz), with the Lean source or with the figures.
- All readers were agents. Agreement between them is not evidence of correctness; the text needs a mathematician's review.

---

<a id="part-iii"></a>

## Part III. Chapters 1, 2, 7, 8, 9

> **Status.** One corrected text: the survey of these chapters with the corrections of the independent audit and of the re-audit folded in. What was changed is listed in "Changes folded in" at the end, and what has been checked by a second reader in "Verification status". Meanings marked I are inferences; proposed equivalents were judged from general mathematical knowledge and were not checked against the literature. The chapter text is that of commit `eb97dec6`; it differs from the text the survey was written against (`7bec3925`) only at 7:1086, 9:212 and 9:548.

**Scope.** `chapters/01-lattice.tex`, `02-observables.tex`, `02-equation-section.tex`, `07-matching.tex`, `08-polymers.tex`, `09-renormalization.tex`, `09-stationary-remainder.tex` in the worktree `manuscript/HumanizeYM_v3/`. All seven files were read in full, after Part II (all sections) and the translation table in `blueprint/notation.md`. Nothing in the repository was edited.

**Conventions.** File abbreviations: `1`, `2`, `2e` (02-equation-section), `7`, `8`, `9`, `9s` (09-stationary-remainder). Line numbers are worktree lines. Counts are numbers of matching lines or matches from `grep` after stripping `\label`, `\ref`, `\eqref`. Basis: D defined, R read off an explicit sentence or formula, I inferred, ? not determined. Category: (a) accounting, (b) program/Lean leakage, (c) ordinary or standard word in unusual sense, (d) coined, (e) other. "Dict" means Part II.

**Overall.** Chapters 1, 2 and 8 are nearly free of house jargon. Chapters 7 and 9 (with 9s) carry most of it. The accounting words `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund`, and the words `detector`, `probe`, `readout`, `word`, `warning`, `compulsory`, `export`, `stored` do not occur in the prose of these files (`budget` survives in two labels, 7:422 and 7:1055). The accounting vocabulary present is `cost` (32 matches), `gain` (9), `loss` (6), `reserve` (4), `share` (4), `spent` (1), `fits … fraction` (about 6), `allocate` (1), `unused` (2).

---

### 1. New terms (not in Part II)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| row transport | 1:80 | defined 1:80–81 | Holonomies act on row vectors: "multiplying a row vector at the initial point by that ordered product transports it to the final point". | D | keep, defined; or *holonomies act on the right* | d |
| physical placement `ŷ` | 1:209 | defined 1:209–212 | `ŷ = a_N r(y)`, the position of a lattice site in continuum units. | D | *position in continuum units* | c |
| placements (other uses) | 1:322; 7:753 | undefined | 1:322 "More flexible placements used later require explicit control of support, seams and divisibility": positions of the observables in the chessboard tiling. 7:753 "bounded in both placements needed for `d_U^*d_U` and `d_Ud_U^*`": the derivative of `d_U` standing on either side of the product, with the "compatible input/output norms" of 7:754. | I | *positions*; at 7:753 *as either factor* | c |
| lattice family | 1:371, 391, 398; "common family" 1:503 | undefined | The cutoff-indexed data chosen once: "The lattice family, including its normalizations, is chosen before `p_seq`" (1:398). That it comprises couplings `β_{N,p}` and insertions `I_{N,p}` is inferred from 1:331–339. | R / I | *family of lattice models (couplings and normalised observables)*; define once | c |
| refinement | 1:393 | undefined | A further subsequence: `P = p_seq ∘ q_seq` (1:395–397). | R | *subsequence* | c |
| retained volumes | 1:379 | undefined | The volumes `P(k)` of the chosen subsequence. | R | *the volumes `P(k)`* | c |
| ordered convergence | 1:369 | defined 1:369–386 | First `N → ∞` at fixed volume, then volume along `P`. | D | keep, defined | d |
| transfer matrix | 1:473 | undefined | Matrix of the mixing of polynomial labels of fixed scaling dimension under one block step: "A transfer matrix records this mixing at each fixed scaling dimension". Not the Euclidean time-evolution operator, which is the standard meaning in lattice field theory. The phrase occurs nowhere else under `chapters/`. | R | *mixing matrix*; *matrix of the block step on `V_d`* | c |
| defects | 1:457 | undefined | "Connected sets of defects are summed": the places where the small-curvature condition fails. | I | *large-field regions* (or *sites*) | c |
| seam; seam links; strip seams | 1:284, 287, 316, 323 | undefined | Links or planes on the reflection planes of the chessboard tiling: "An observable local on this cell reads no seam links". | I | *links meeting the reflection planes* | d |
| slots | 1:314 | stated 1:314–315 | "The slots are the `2q` strips in that coordinate": the positions of the cyclic product in the abstract chessboard theorem. | R | *factors of the cyclic product*; not sure a standard word exists | c |
| positive sector; positive algebra | 1:244–247, 265 | 1:244–247 | The half `1 ≤ t < h` or `0 ≤ t < h` of the torus; observables depending only on links with both endpoints there. A different "sector" from Dict's. | D | *positive half*; "positive algebra" is close to standard | c |
| collision diagonals; collisions | 1:365, 426, 477 | undefined | The set where two positions coincide: "Compactness of their support gives a positive distance from the collision diagonals" (1:364–365). Dict 2.5 has "collision" in this sense for chapter 3. | R | *coincident points*; *the diagonals* | c |
| observable label `v = (d, c)`; tag `d` | 2:97–99 | named 2:97–98 | The pair of the index `d` and a polynomial `c ∈ V_d`: "The same polynomial `c` can occur at different tags `d`". Dict takes a label to be the element of `V_d`; here it is the pair. In chapter 1 the labels are still an abstract index set: "For now let `𝒯` be an arbitrary set of local-observable labels" (1:330–331). | R | *pair `(d, c)`*; *index `d`* | b |
| normalization index | 2:402 | undefined | The same `d`: "Its eventual physical normalization still depends on the normalization index". Third name with "tag" and (in `notation.md`) "filtration index". | I | *index `d`*, one name | d |
| the unit | 2:192, 281, 400; 2e:227, 236; "unit column" 2:259–260 | undefined | The constant polynomial `𝟏` and the constant function 1: "The unit illustrates the simplest section: `P_d^loc[𝟏] = 1` for every `d`" (2:400). | R | *the constant polynomial `𝟏`* | c |
| raw | 2:404; 9:571 | undefined | Before normalisation or modification: "the raw constant section" (2:404), i.e. the section without its normalising coefficient; "the raw channels restricted by their event indicators" (9:571). | I | *unnormalised*; *unmodified* | c |
| factor count; factor-count operator `N_fac` | 2:53, 67–72, 79, 202, 308; 2e:19, 33–35, 186–187 | defined 2:52–53 | Ordinary polynomial degree in jet coordinates: "The ordinary polynomial degree counts factors of jet coordinates; to distinguish it from scaling dimension we call it the *factor count*". | D | *polynomial degree*; keep if defined | d |
| factor count (second use) | 7:613 | undefined | "The factor count is `(n+2) + number of differences = 4`": the number of small factors (legs plus finite differences) in a power count. Not the degree of 2:53. | R | *number of small factors* | c |
| bidegree | 2:79, 91 | undefined | The pair (scaling dimension, factor count): "The constant has bidegree `(0,0)`"; the curvature square has "bidegree `(4,2)`". 2e:34–35 orders the same pair the other way, "(factor count, scaling dimension)", for the lexicographic order. | R | keep; fix one order of the pair | d |
| test configuration; test holonomy; test connection | 2:13, 103, 116 (label), 150, 416 | 2:13–16 | Smooth classical connections built from a jet, inserted into a lattice observable to read off its Taylor polynomial. | R | *classical (smooth) connection* | c |
| Taylor map `Tay_d`; local polynomial section | 2:133–146 | defined | Right inverse of the Taylor map. | D | keep | – |
| curvature measurement; plaquette measurement | 2:220, 238, 362 | undefined | The functions `σ_{γ,□}` or their linearisations. | I | *transported curvatures* | c |
| curvature coordinate; admissible for a link `e` | 2e:65–68, 104, 124, 172, 184, 194 | defined 2e:62–67 | `U ↦ ⟨u, σ_{γ,□}(U)⟩`; admissible if neither plaquette nor path uses `e`. The subsection title (2e:60) calls them "curvature tests". | D | keep "curvature coordinate"; drop "tests" in the title | d |
| basis column; unit column; column by column | 2:200, 260, 374, 390 | undefined | The image `P_d^loc[b_{d,i}]` of a basis vector. | I | *image of the basis element `b_{d,i}`* | c |
| permitted direction at threshold `t`; spatial exponent `p_0` | 2:325–330, 340, 388 | defined 2:326–329 | `\|A_e\| ≤ t(1 + dist(e⁻, y))^{p_0}`. | D | *admissible direction*; keep if defined | d |
| equation ideal `𝓘_d`; Maxwell solution potential | 2e:10–21; 2:445 "free equation ideal" | defined | Polynomials vanishing on solution jets. | D | keep | – |
| regrading `R_d` | 2e:52 (name), 27–36 (object) | object defined; name not | The automorphism with `R_d p − p` strictly higher in (factor count, scaling dimension); `R_d = I + T_d` with `T_d` nilpotent (2e:229–233). | R | *unipotent (triangular) automorphism `R_d`* | d |
| exterior spectator | 2e:195, 205–206, 213, 221, 254 | 2e:39–41 gives the object | The bounded measurable function `S` of links farther than `r_d` from the anchor. Differs from Dict 2.5 (the other insertions). | R | *the function `S`*; *exterior function* | c |
| Wilson force `F_e` | 2e:110–129 | defined 2e:117–121 | Gradient of the Wilson action in one link. | D | standard enough; keep | – |
| common symbol; common kernel; common strip bound | 7:27–46 and passim (28 matches of `common` in ch. 7) | defined 7:36–39 | "one function chosen on the infinite lattice whose restriction to each finite momentum grid describes the corresponding torus coefficient". | D | *volume-independent (infinite-lattice) symbol* | c |
| strip bound `\|f\|_σ ≤ A`; order-`r` zero | 7:41–48 | defined | Holomorphic and bounded on `\|Im p\| < σ`; vanishing of momentum Taylor coefficients below degree `r`. | D | keep | – |
| leg (one-form, two-form, internal, external, differentiated) | 7:61, 76, 79, 131, 159 and 30 matches in ch. 7 | undefined | An argument of a multilinear Taylor symbol, with its direction index, Lie-algebra argument and momentum (7:33–34, 61). Dict 2.5 has "leg" as a factor of a Wick monomial. | R | *argument*; "leg" is standard in physics, define once | c |
| bridge legs | 7:597 | undefined | "External smooth bridge legs have the same powers in supremum norm, by (ch05:actual-bridge)": the cited bound is on `∇^r W_a` (5:1129–1132), and 5:1151–1152 says it "is asserted for `W_a`", "the smooth representative". So the legs are external arguments of the form `W_a u`; the word "bridge" comes from the label only. | I | *external arguments `W_a u`* | b |
| integral shear | 7:118 | undefined | "replace `p_1` by `p_0` as independent variable … This invertible integral shear only reduces the strip by a fixed factor": a linear change of the momentum variables with integer coefficients. | I | *unimodular linear change of variables* | d |
| elementary division `D_a`; coordinate, scalar, two-leg, curvature division | 7:89–97, 124, 611, 904, 1028, 1162, 1182 | defined 7:89–91 | `D_a f = (f − f\|_{p_a=0})/(e^{ip_a} − 1)`. | D | keep | – |
| curvature insertion `F_{γ,ab}` | 7:147–152 | defined | Transported projected plaquette curvature. Same object as ch. 2 "transported curvature". | D | *transported curvature* (one name) | c |
| kinetic symbol `b_H`; kinetic coefficient, action, Hessian, normalization | 7:184, 193, 216, 275, 312, 478, 603–621, 743, 856, 874 | 7:184–190 | The quadratic form `½⟨d_1 v, H d_1 v⟩` and its symbol. The text says "kinetic symbol `b_H` of `J`" (7:184–185), but `J` is introduced only at 7:976. Not the "kinetic energies" of Dict 2.3. | R | *quadratic curvature form*; "kinetic term" is physics usage | c |
| exchange symmetry | 7:195 | undefined | A hypothesis on a quadratic symbol ("with exchange symmetry and signed-coordinate symmetry"); presumably symmetry under exchange of its two arguments. Unrelated to "exchange term" below. | I | *symmetry in the two arguments* | c |
| kills | 7:201; 9:525 | – | Makes vanish: "The Ward identity first kills the constant term"; "An axis reflection kills off-diagonal orientation pairs". | R | *annihilates*; *makes … vanish* | c |
| gauge completion; completed | 7:229 (title), 251–252, 313, 371, 879, 935, 1025 | 7:251–252 | Adding `F*F` (or `d_U d_U*`) to a gauge-degenerate Hessian: "Given a gauge condition `F` with invertible `G = Fℛ`, put `C = 𝖩 + F*F`", where `𝖩` is the joint Hessian of 7:242 (not the action `J` of 7:976). Dict's "positive completion" is unrelated. | R | *gauge-fixed Hessian* | c |
| block-completed form `𝒢` | 7:687–691; "blocked completed matrix `C_0`" 7:773 | 7:687–691 | A different completion: the kinetic form completed by the block penalty, `𝒢(u,r) = ⟨u, K_f u⟩ + b\|Mu − d_{0,c} r\|²`, still gauge-degenerate ("The block-completed form needs a quotient estimate"). The gauge term is added afterwards: "a positive weighted floor for `𝒢 + F*F`" (7:728–729). The matrix `C_0` of 7:773 appears to contain both completions (inferred). | R (7:687–691); I (7:773) | *kinetic form plus block penalty*; not "gauge-fixed" | c |
| infinitesimal gauge insertion `ℛ` | 7:243 | named only | The linear map from gauge parameters to tangent vectors; 7:877 calls it "infinitesimal internal gauge action". | R | *infinitesimal gauge action* | c |
| (background) insertion: first, second | 7:332–333, 380–391, 416–418, 603–612 and passim | 7:331–333 | Derivatives of an operator with respect to the background field: "`b(p;k)` its first background insertion, and `c(p,p′;k)` its second insertion. These are actual derivatives of the same operator". | R | *first and second derivative in the background field*; *vertex* | c |
| denominator (zero-background, vector, ghost, channel) | 7:331, 371, 376, 407, 414–415, 440 | 7:331 | The zero-background operator symbol `a(k)`, a matrix. | R | *symbol of the quadratic form*; *inverse propagator* | c |
| floor (metric, denominator, weighted, ratio, period) | 7:323, 407, 684–686, 706, 729, 732, 738, 828; 9:928, 935 | undefined | A uniform positive lower bound: "the weighted floor `2^{-10} min(1, ε)`, where `H_f ≥ εI`" (7:685). | R | *lower bound* | c |
| response | see section 3 | – | – | – | – | – |
| thermal coefficient | 7:765 (prose); label `ch07:thermal` at 7:232 | undefined | "the actual stationary thermal coefficient" (7:764–765). The label marks `T(v) = ℒ_{m+1}(U_v) + ½ log det Q(v) − log J_Haar(v)`, which the text introduces as "The Gaussian contribution at a stationary fine configuration" (7:231). The thermal coefficient is then a coefficient extracted from `T(v)`; the word occurs only at 7:765. | I | *coefficient of the Gaussian contribution `T(v)`* | b |
| radial bound, radial inequality, radial constants | 7:437, 451, 462 | undefined | The bounds on `I_μ(k)` in terms of `\|k\|` in Proposition 7:310. | I | *the bounds of Proposition …* | d |
| recording estimate; "Trace norms and recording" | 7:461, 742 | object stated 7:457–460; name unexplained | At 7:461 "this last recording estimate" is the bound `C_μ e^{-c_μ n}` on the difference between the mesh mean and the integral of a periodic analytic function (7:457–460). The text later calls it "The Fourier mesh estimate at the end of Proposition (ch07:integrand-input)" (7:762–763). Why it is called "recording", and what "recording" means in the paragraph title 7:742 (the paragraph ends with the passage to finite-torus representations), is not said; the "recording scale" of 11R:25 ff. is a different object. | R (object); ? (name) | *Fourier mesh estimate* (the text's own phrase, 7:762) | b |
| direction selectors | 7:427 | undefined | "The four constant direction selectors in the vector regulator"; `M_μ` "applies `m_μ` to each one-form component" (7:276). | I | *projections onto the one-form components* | b |
| trace-class cube | 7:495, 745 | undefined | The factor `P_μ³` in `(P_μ³)³`: "distribute at most two derivatives among the three factors in `(P_μ³)³`. Every term retains one undifferentiated trace-class cube" (7:493–495). | R | *the factor `P_μ³`, which is trace class* | d |
| contact term; contact correction; contact assertion | 7:501–504, 568, 764, 773, 807 | 7:529–545 | The second-order difference `D²(log det M_act − log det M_core)(0)`, due to the second derivative of the nonlinear block average. Not a coincident-point term. | R | *second-order block-average correction to the determinant* (no standard name known) | c |
| stationary branch; selected branch | 7:501, 517, 553, 766, 949, 953, 1152; 9:292; 9s:36, 39 | 9s:36 "`ρ(x)` for its stationary branch" | The locally unique solution of the stationarity equation as a function of the coarse field. Dict's "branch" is a case of a piecewise definition; Dict's "stationary graph" is this object. | R | *branch of critical points*; *critical-point map* | c |
| rooted coordinates; centered coordinates; recentering | 7:505–507, 521, 530, 581, 626–678, 693–700, 883 | 7:655–656, 693–695 | Rooted: `Q = M + d_{0,c}R` with scalar `r_root`. Centered: `r = r_root − Ru`, with the frame normalised by `Σ_x ω(x) Π F_x = Π 1`. | R | *frame normalised at the root* / *normalised in the mean* | d |
| coarse scalar component; scalar principal alias; coarse-frame directions, projection | 7:477, 507, 580, 591, 696–703, 721–722, 892, 915 | undefined | The zero-form (frame, gauge-parameter) variable at coarse sites carried along with the fine field in the joint space. | I | *coarse frame variable `r`* | c |
| principal real cube | 7:704–705 | undefined | "bounded away from zero after division by `μ²` on the principal real cube": apparently the real momentum cube of the principal (zero) alias. | I / ? | none proposed; needs the author | d |
| internal / external (direction, leg, momentum, coordinates) | 7:334, 366, 522, 595–630, 872–873, 899–915, 1033–1044 | 7:872–873 | Internal: "internal fine-plus-frame coordinates `z`", the integration variables. External: coarse-field directions. | R | *fluctuation* / *background (coarse)* | c |
| left increment; left-coordinate Hessian; split-field definition | 7:242, 313, 362–363, 522, 624 | 7:362–363 | Hessian "obtained from `S(log(e^{x_+}e^{x_-}))` by two `x_+` derivatives". The increments act by left multiplication, as in the left derivative `D_A^L F(U) = d/dε F((exp(εA_e)U_e))` of 2:318–321. | R | *second derivative in left-multiplication increments* (proposal; no fixed standard phrase known). Not "left-invariant coordinates": left multiplication is generated by right-invariant vector fields. | d |
| padded block; padded block average patch | 7:599, 628 | undefined | An enlarged block containing the support of the block average: "Extending to the fixed padded block average patch only changes constants: its number of residue blocks is fixed at the given smoothing order". Two candidates: the block-average patch `Ly + 𝔹_R`, `R = (j+3)L` (4:17, 172–173), or Dict's macro-box of radius `(j+7)L` (4:298–299). The wording "block average patch" favours the first; the text does not decide. | I | *block-average patch* (or *enlarged block*) | d |
| fixed-position read; coordinatewise splice | 7:637, 710 | undefined | "a fixed-position read is a coordinatewise splice of its endpoints"; "each fixed-position averaged read has coefficients `O_j(L^{-4})` on `O_j(L^4)` sites … Summing its `L` connector positions" (7:710–712). Read with the connector `Y_{e,z} = h_{y,z} (∏_{r=0}^{L−1} U(Ly + z + re_μ, μ)) h_{y+e_μ,z}^{-1}`, averaged over offsets `z` with weights `w^av` (4:174–189): the link at a fixed position `r` of the connector, as a function of the offset. "Coordinatewise splice" is not explained. | I | *the link at a fixed position of the connector*; the second phrase needs the author | b |
| exterior identity | 7:408, 686 | undefined | Used to control "the sum of transverse and longitudinal parts". Presumably `d_1*d_1 + d_0 d_0* = Δ` on one-forms; 11:1692 "The exterior identity gives coercivity at least `c\|q\|²`" agrees with this. 5:840 uses the phrase for a different identity. Not displayed in these files. | I | state the identity | d |
| quotient estimate; weighted quotient | 7:688, 719, 728, 870 | 7:719 | `inf_a ‖(u,r) − ℛa‖_p² ≤ C_j 𝒢(u,r)`. | R | *coercivity modulo gauge directions* (unsure) | – |
| weight conversion; weighted-to-Euclidean conversion | 7:498, 748, 751, 917 | undefined | Passing between the `h_l`-weighted and unweighted norms, at a factor `O(μ^{-1})`. | R | *comparison of the weighted and Euclidean norms* | d |
| stationary identification | 7:578, 829; cf. 7:1154 | undefined | The identification of the tangent of the stationary branch with the operators `W` of ch. 5 ("once the actual and straight stationary tangents have been identified up to gauge"). | I | *the identity (ch05:stationary-tangent)* | d |
| interpolated link fields | 7:817 | undefined | "`L^{-2}` from the two interpolated link fields": apparently the two fine fields obtained from coarse ones by the stationary tangent, each of size `L^{-1}` (cf. 5:1129–1132). | I | *the two factors `W`* (unsure) | d |
| adjacent pair; adjacent quadratic pair | 7:580, 828; 9:15, 912, 963 | 9:15 | "Fix one adjacent pair of scales, with fine scale `m+1` and coarse scale `m`". "Quadratic pair" adds their quadratic forms (inferred). | D (pair); I (quadratic pair) | *consecutive scales* | d |
| one-loop drift; downward blocking | 7:825–856; 9:42 | 7:855–856 | "the coefficient `β` of the kinetic action decreases by `κ_G log L` at one loop"; downward = from `m+1` to `m`. | R | *one-loop shift of the coupling per step* | d |
| one-step integral identity | 7:859 | undefined | A result cited by nickname: "Connected interactions contribute to that recursion and are handled by the one-step integral identity". No reference is given; presumably the exact local integral of 9:44 ff. | I | cite the statement | d |
| local-integral estimate, bounds | 7:1075, 1205; 9:34 | undefined | The nonlinear bounds on the one-step fluctuation integral, cited by nickname ("They do not replace the nonlinear local-integral bounds"); cf. the section title "The exact local integral and its first expansion" (9:44) and the proposition "Common local integral bound" (6:1123). | I | cite the propositions | d |
| exchange term, inverse, pairing | 7:935, 955, 1048, 1050 | 7:944–945 | The term `B 𝒞^{-1} B` in `D⁴E(0)`. | R | physics usage; or *tree term with one propagator* | – |
| matched (coarse metric, determinant coefficient) | 7:982, 1073; 9:410, 738 | undefined | Fixed by the matching conditions of chapter 7: "the coarse metric matched to the incoming Gaussian form, not an arbitrary positive coarse metric" (7:982–983); "the matched determinant coefficient, not an adjustable trial inverse coupling" (9:410–411). | R | *determined by the matching conditions* | d |
| curvature family (cubic, quartic, quadratic) | 7:1054, 1060–1062, 1071, 1163, 1168 | undefined | The collections of curvature terms `S_3`, `S_4` and the quadratic one. | R | *the terms `S_3`, `S_4`* | d |
| pulled back; (stationary, linear) pullback | 7:1085, 1120, 1150–1151 | undefined | Composition of the inherited loop action with the stationary map: "the nonlinear stationary pullback has the same Hessian as this linear pullback" (7:1150–1151). In the display (ch07:inherited) the object is written in words, "`ℒ_{m+1}` pulled back". 1:290 and 9:328 use "pullback" in the ordinary sense. | R | *composition with the stationary map*; give the object a symbol | c |
| path (short for path action); normalized path; incoming, outgoing, prescribed path | 7:576, 786, 789, 828, 1199, 1203; 9:13 (9s), 385, 914, 926 | undefined | The path action, not a lattice path: "the selected path and block average" (7:576); "the incoming path" (9:914). "Normalized": `H(0) = I` (7:312–313). | R | *path action* in full | c |
| classical bound contraction; inherited-loop contraction | 9:970 | – | The inequalities (ch07:classical-budget), `A_out ≤ a_stage + P_stage(A)/L` (7:1055–1057), and (ch07:inherited), `‖ℒ_{m+1} pulled back‖ ≤ C L^{-2} Λ^loop_{m+1}` (7:1084–1087); 10:35–36 names both with these equation references. The first is an invariance of a bound, not a contraction. | R | *the bounds (…)* | c |
| quantitative descent | 7:1187 | undefined | The step from the loop bound at `m+1` to that at `m`. | I | *induction step* | d |
| coupling entry threshold | 7:1190 | undefined | Lower bound on the coupling above which the estimates hold; elsewhere "(inverse) coupling threshold". | I | *lower bound on `β̂`* | d |
| site norm `‖z‖_α`; support norm | 8:69–79, 143, 196 | defined 8:69–74 | `sup_x Σ_{γ: x ∈ X_γ} \|z_γ\| e^{α c(X_γ)}`: "It counts every polymer at each site in its support. A norm which counts only the chosen anchor of a polymer is different" (8:75–76). This is Dict's "containing-site bound". "The support norm" (8:196) has no formula; that it is the same norm is inferred. | D (site norm); I (support norm) | *weighted polymer-activity norm* (one name) | – |
| occurrences; distinguished occurrence | 8:85, 178, 193 | defined 8:84–86 | The positions `1, …, n` of a tuple of polymer labels, the vertices of its incompatibility graph ("form the graph on the *occurrences* `1,…,n`"). Distinguished: the one designated to contain a given site or insertion ("An insertion selected in this way is a distinguished occurrence", 8:193). | D | keep | – |
| support-weight reserve; "will be spent" | 8:150–151, 362; 9:438, 919 | 8:146–151 | The extra `δ > 0` in `‖z‖_{α+δ} ≤ γ_0`. | R | *margin `δ` in the decay rate* | a |
| derivative reserves | 9:34 | undefined here | "with the prescribed derivative reserves for the local integral estimates". 10:737–739 has "through one order beyond the outgoing order. This is a numerical derivative reserve for the integration kernels": extra derivative orders beyond those of the output norm. That 9:34 means the same is inferred. | R (10:737–739); I (9:34) | *additional derivative orders* | a |
| inflated activities | 8:170; 9:180 | defined 8:171 | `q^{-1}\|z_γ\| e^{α c(X_γ)}`. | D | *rescaled activities* | – |
| hypothesis matching | 8:169 | – | Verification of the hypotheses of the cited theorem. | R | *verification of the hypotheses* | d |
| sites declared to be in the large-field region; sites assigned to an activity | 8:284–288 | defined | The set `D` and the subsets `I_η`. | D | *prescribed large-field set `D`* | b |
| exact reassembly | 8:279, 355; 9:57 | 8:310–316 | The factorisation `Z_D = e^{𝓛} Σ_B Π K_η e^{−𝓛_{Y(B)}}`. | R | *factorisation identity* | d |
| regular activity (ch. 8 sense) | 8:285, 318, 322, 331, 333 | 8:285 | The polymer-gas activities `z_γ`. Conflicts with Dict 2.3, where a regular activity is an additive term of the exponent and "not a polymer activity"; ch. 9 uses that sense (9:132, 867) and says "ordinary" for the gas (9:150, 153, 172). | R | reserve *regular activity* for one of the two | c |
| source-deformed activities | 8:268, 364 | undefined | Activities of the gas with generating-function sources `t_j`. | R | *activities depending on the source parameters* | – |
| first expansion; first polymer activities; second cluster expansion | 9:44, 88–89, 148, 173, 192 | 9:81–89 | First: expand `e^V = 1 + (e^V − 1)` and take connected components of intersecting dependence regions. Second: the logarithm of ch. 8. | R | *Mayer expansion* (the standard name for this step); *cluster expansion of the logarithm* | – |
| scalar bookkeeping; measure multiplier | 9:56, 63 | undefined | The field-independent prefactors of the Gaussian change of variables. | I | *constant prefactors* | a / b |
| dummy Gaussian coordinates | 9:59, 72 | partly stated | Coordinates added to reach dimension `D`: "let `D` be the dimension after dummy Gaussian coordinates have been added" (9:59); "The dummy Gaussian integral equals one after the inactive Haar variables have been frozen" (9:72–73). Which coordinates are added is not said. | R | *auxiliary Gaussian variables* | b |
| missing-coordinate factor | 9:77 | undefined | Presumably `e^{−(N_free − n_act) log 𝔪}` (9:68). | I | name the formula | b |
| Haar logarithm; Haar remainder; Haar correction | 9:63, 76, 127, 141; 9s:39 | 9s:38–39 | "minus the logarithm of the product Haar-chart Jacobian". | R | *logarithm of the Haar density in the chart* | d |
| sector allocation indicators | 9:81–82 | undefined here | "retain all sector allocation indicators": the partition-of-unity weights of chapter 6 (Dict 1.8, `allocation` (i), 6:67–79; "allocation sector" 6:85). | I | *partition-of-unity weights* | b |
| common law; one sector Gaussian/Haar law; common-law estimate; joint bound; common Gaussian moments, estimate | 9:97–118, 139, 785; "common Gaussian" 9:266, 966 | 9:105 | The single measure `ν` under which all factors of a product are integrated together. "The common Gaussian estimate" (9:966) is the estimate under that measure, "supplied by the complete factor construction in Chapter 6". | R | *joint estimate under one measure* | c |
| selected large-field condition set `A_M` | 9:108, 440 | undefined | Presumably the large-field selection `A` of Dict 1.3 restricted to the region. | I | *large-field index set* | c |
| cutoff-failure label | 9:111, 133 | undefined here | The event label of ch. 6:835 (Dict 4.2). | I | *event label* (one name) | d |
| "factor after deterministic subtraction" and the seven factor names in the table | 9:124–133 | undefined | Names of local factors with their majorants; e.g. "stationary cubic remainder", "covariance and stationary residual". Which subtraction is meant is not said. | R (table only) | define each by a formula or a reference to ch. 6 | d |
| read-count polynomials | 9:147 | undefined | Presumably the factors `(1 + s_M)^{d_j}` of 9:100. | I | *polynomial factors in the size of the dependence region* | b |
| ordinary gas; ordinary polymers; elementary ordinary factor; exact-cover gas | 9:150, 153, 172, 593 | undefined | The polymer gas without large-field sites ("the ordinary gas without large-field sites", 9:150); `ℱ⁰` is the "exact-cover gas". | I | *small-field polymer gas*; *constrained sum `ℱ⁰`* | c |
| prescribed large-field site set; prescribed set of large-field sites | 9:151, 643, 673, 675, 893 | 8:287–288 (object `I_η`); 4:440–441 (`I_i^bad`) | The set of large-field sites attached to an activity: "nonempty sets `I_η ⊂ D ∩ Y_η`. The set `I_η` records the large-field sites assigned to that activity" (8:287–288); in chapter 4, "a nonempty prescribed set `I_i^bad ⊂ Y_i`" (4:440–441). This is the `notation.md` rendering of "inventory". | R | keep, with the symbol | – |
| degree (of an elementary factor, polymer, cluster) | 9:172–174, 182, 193 | defined | Number of elementary factors. | D | *number of elementary factors* | c |
| affine Hessian; affine-Hessian cancellation, condition | 9:207, 213, 480, 497, 564 | 4:627–641; used 9:458–480 | The Hessian at zero of `A ↦ E(exp A)` restricted to pairs of affine link fields `A_{(y,μ)} = u_μ + Σ_ν ξ(y)^ν v_{μν}`; the condition requires it to vanish. "The meaning of the affine Hessian condition is fixed in the chosen local coordinates" (4:640–641). | R | keep; it is defined in chapter 4, so refer to 4:627–641 at 9:207 | d |
| inverse-ratio sizes | 9:208 | – | Powers of `L^{-1}`. | R | *powers of `L^{-1}`* | d |
| inspected support | 9:220 | undefined | Probably the dependence region. | I | *dependence region* | b |
| support compression | 9:231 | undefined | Probably the passage from a fine support to its coarse image, reducing the covering number. | ? | needs the author | d |
| principal (norm, estimate) | 9:235, 268 | undefined | The leading contribution of the linear inherited term, before the comparison with the block integral. | I | *leading term* | c |
| Gaussian units; stationary units | 9:242; 9s:165 | undefined | Rescaled by `g`; relative to `Ω e^{−Φ}`. | I | *in units of `g`*; *relative to `Ω e^{−Φ}`* | d |
| pure (small-field) block integral; pure integrand | 9s:12–17, 117, 130, 243; 9:969 | 9s:12–15 | "incoming activities are omitted, the prescribed path and block kernel are unchanged, and the fine-field indicator … is retained". | D | *block integral of the path action alone* | d |
| extra exponent `ψ` | 9s:38–40 | defined | Fine loop term minus the logarithm of the Haar-chart Jacobian. | D | keep with the symbol | – |
| cutoff amplitude `M = M^cut` | 9s:23; 9:137 and passim | ch. 4:411 | `exp((log log β̂)²)`; `t_m = β̂^{-1/2} M^cut`. | D (ch. 4) | *threshold ratio* (unsure; nothing better found); keep the symbol | c |
| truncated mass | 9s:69, 78 | 9s:67 | `N(0, A(x)^{-1}){\|ξ\| ≤ D}`. | R | *Gaussian measure of the ball* | – |
| retained region `𝒮_x`; retained ball | 9s:111–116, 168, 220 | defined 9s:115–116 | `𝒟_x(ρ(x) + g B̄(0, D))`. | D | keep with the symbol | – |
| pass the cutoff | 9s:126–127 | undefined | "all its fine plaquettes pass the cutoff": satisfy the fine small-field (cutoff) condition. | I | *satisfy the cutoff condition* | c |
| live tag actions; tag-count factor; tag-coincidence radius | 9s:127, 134–135, 221 | undefined | "all live tag actions coincide with `φ`"; probably the actions for the values of the index `α` that have positive weight. | I / ? | *the actions for every `α` with `λ(U, α) > 0`* (unsure) | b |
| safe chart; chart recognition; "recognizes" | 9s:139–141, 232 | undefined | "The actual tree comparison recognizes a fine configuration as lying in a fixed safe chart whenever its fine plaquettes and … mismatches are below a fixed `δ`". The estimate used is the nonlinear tree estimate (ch05:nonlinear-tree), 5:1009–1015, in the subsection "The tree comparison and the actual Hessian" (5:1000); the inequality that Dict 2.2 calls "tree comparison" (5:1036–1040) is derived from it. | R | *by the nonlinear tree estimate (…), a configuration with … below `δ` lies in the chart* | b |
| folded (auxiliary configuration, field); folding map | 9s:169–175, 233 | 9:326–330 gives the map, unnamed | Pullback of the field under the reflection map `π_v(q) = min(q̄, 2v − q̄)`. | R | *reflected periodic extension* | d |
| plaquette filling bounds | 9s:175 | undefined | "Plaquette filling bounds give logarithmic coordinates with …", after a coordinate axial gauge has been chosen: presumably the bound of a link in axial gauge by the plaquettes filling the surface between it and the gauge axis. | I | *axial-gauge bound of the links by the enclosed plaquettes* | d |
| microscopic (neighborhood, term) | 9s:219, 223, 233, 254 | undefined | Of radius `z^{-1}` (9s:93, 214–215). | I | *neighbourhood of radius `β̂^{-1}`* | c |
| corrected logarithm; centered expression | 9s:264, 274, 283 | 9s:266–267 | `log 𝒵 + β′ a_c + d_c`; "centered" is not explained. | R / ? | name the formula | d |
| prescribed coarse classical action `a_c`; quantum contribution `d_c`; quantum matching | 9s:258–259, 271; 9:291, 927 | undefined | "Let `a_c` be the prescribed coarse classical action and `d_c` its quantum contribution". No formula. Narrowed by 9s:270–271: "Classical matching gives `D^r C(0) = 0` for `0 ≤ r ≤ 4`" with `C = a_c − φ(·,ρ)`, which matches 7:994–998, so `a_c` is `J + S_3 + S_4` (the `𝒦` of 9:23–25); "The quadratic quantum matching bounds `D²W(0)`" ties `d_c` to the determinant matching of 7:1159–1167. Ch. 7 never uses the phrase "quantum matching". | I | define `a_c`, `d_c` by formulas | – |
| shares `p_{xa}` | 9:314–316, 323 | defined | `1_{X_a}(x)/\|X_a\|`, weights summing to one. | D | *weights* | a |
| auxiliary tori `Λ_i`; reflection cubes, faces; reflected tori | 9:324–325, 350, 769, 932 | defined 9:324–329 | Tori of sides `2(w+i)` carrying the folded field. | D | keep | – |
| logarithmic correction `L_x`, `ℓ_a`; logarithmic label, term, selection | 9:368, 432, 607, 630–638, 671, 677, 698 | 9:367–369, 633–635 | Terms of the exponent that vanish on small-field supports. | R | *large-field correction terms in the exponent* | c |
| preparatory output; preliminary (large-field) activities | 9:394–399, 462, 637–643 | 9:397–406 | The intermediate representation (ch09:early). | R | *intermediate representation* | – |
| trial inverse coupling (correction) `d` | 9:411, 756–757 | 9:756–759 | A variable shift of the inverse coupling: "Hold the constructed activities fixed and vary only a trial inverse coupling correction `d`. The scalar discrepancy is `f(d) = (β′ + α + d)𝒦(U_*) + …`". | R | *variable shift `d` of the inverse coupling* | d |
| health domains; health event indicator | 9:563, 839 | undefined | The cases `h = 1` and `h = 0` of the small-field indicator `h_X` (4:427: "write its indicator as `h_X(U)`"). The text never says what "health" is: 9:563 is read through the factor `(1 − h_{Y_d})` of 9:553, and 9:839 "write `h_p` for the health event indicator on its vertices" through 4:427. The word occurs in no other chapter file (grep). | I | *small-field and large-field cases*; *small-field indicator* | b |
| plaquette channel; channel `d`; low, high, raw channels; clover substitute | 9:543–546, 571, 609–612, 770, 861 | 9:543–547 | One term of the quadratic part of the path action (a plaquette term or an ordered pair of entries of a row square). | R | *term* | b |
| local projection; projection | 9:731, 746, 770, 814 | undefined | Apparently the map `f ↦ q_f` (or `Q_f`) of 9:467–470. | I | *extraction of the quadratic coefficient* | c |
| discrepancy series; scalar discrepancy | 9:517, 757 | undefined | The family of `ζ_f`; the function `f(d)` of 9:759. | I | name the objects | d |
| the reset; `C_reset` | 9:597, 599, 748 | undefined in prose | "There is a second, intrinsic way to identify the reset". The label `ch09:reset` marks `β = β′ + α + Δ`, `v_sc = τ − \|Λ\|^{-1} Σ f_i(1)`. | I (via label) | *the redefinition of the coupling and the constant* | b |
| attachment norm; number of attachments; strict attachment margin | 9:687, 697, 794 | undefined | The norm of 9:659, `sup_x Σ_{a: x ∈ Z_a} e^{(σ+1)c(Z_a)} v_a`, with the condition `(2B+1)^4 γ ≤ 1`. It has the form of the site norm of 8:69 at exponent `σ+1`, applied to majorants. | I | *the norm (…)* | d |
| flattening | 9:676 | undefined | Replacing a family of new labels by the union of their constituents. | R | *taking the union of the constituents* | d |
| residual energy `𝒲_p` | 9:842–850, 877, 885 | defined | – | D | keep | – |
| restriction compatibility | 9:391, 815, 948 | undefined | The construction is unchanged when the parameter interval is restricted. | R | say so in words | d |
| local read diameter | 9:932 | undefined | Diameter of the largest dependence region. | I | *diameter of the dependence regions* | b |
| numerical band margin | 9:950 | undefined | A condition in the choice of scales ensuring `β` stays in the band. Possibly the inner barriers of 10:212–222; not determined. | ? | needs a reference | d |
| quadratic-tilt criterion | 9:115 | by reference | "The alternative quadratic-tilt criterion in Proposition (ch06:common-majorant) is not required here" (9:115–116). That proposition (6:1123–1138) assumes "uniform polynomial moment bounds for `P_k` under the corresponding tilted Gaussians": the criterion is this hypothesis. | R | *the hypothesis of Proposition … on tilted Gaussians* | – |
| stationary residual | 9:77, 130 | undefined here | Probably `𝖠 m_Y + f_Y = (I − 𝖠P^*) f_Y`, bounded by `C t_f e^{-cB}` (6:615–621); this matches the majorant `e^{-c'_j B}` in the table at 9:130–131. 6:1257 has "linear Gaussian residual". | I | *the residual `𝖠 m_Y + f_Y`* | – |
| determinant inverse identity | 9:140 | undefined here | Probably the expansions of 6:1192–1203 ("The exact inverse and trace expansions … This determinant identity"). | I | replace by a reference | – |
| normalized affine directions; reflected normalized directions | 9:35, 502; 9s:296 | undefined here | Directions scaled by the threshold: the seminorm directions with `\|(A_r)_e\| ≤ t_m(1 + dist(e⁻, o_i))^ϖ` (4:580–581); "dimensionless variation parameters … bounded by `C_k t_f` … in these normalized directions" (6:626–638); 9:503 `t²\|q_f(q,r)\| ≤ 3a_f` agrees. Cf. Dict 4.2 "normalized directions". "Affine" and "reflected" are not explained. | R (scaling); I (affine, reflected) | *directions of size `t_m`* | d |

---

### 2. Dictionary terms

#### 2.1 Same sense (sample references)

| Term | References in these chapters |
|---|---|
| `row`, component of the action vector | 7:352, 976–977, 993, 1168; 9:544, 568, 835, 840 |
| `row`, matrix row | 7:711; 9s:192, 197 |
| polynomial label | 2:58–75, 106, 433; 1:481 |
| label as index of a term | 9:385, 771, 816, 939 ("fixed labels") |
| tag as the random index `α` | 9:83, 85; 9s:127, 134, 242 |
| transport, parallel | 1:153–154; 2:171–176; 2e:80–83; 7:147, 1005–1009 |
| transport, stationary-field map `W`, `T` | 7:1088, 1112, 1136, 1141, 1201; 9:913; 9s:170, 192 (the last two are the map `T` on two-forms, see section 3) |
| transported (covariantised) rows | 7:975–977 |
| anchor, base point | 2e:39, 83, 126; 7:154, 619, 912, 1119; 8:76; 9:234, 462, 513 |
| anchor, real base point of a continuation | 7:733 |
| frame | 2:181; 7:272, 642–679; 9:541 |
| connector; straight | 7:636–640, 670, 693, 709–712; 7:1112, 1154 |
| forest; tree gauge | 7:574, 890–892; 9:74, 239, 924; 9s:34, 114, 189 |
| alias, principal / nonprincipal; fine residue | 7:488, 701–722, 812–816, 1135–1148; 7:585, 595, 599 |
| layer, homogeneous degree | 2e:91, 102, 131–133, 142, 151 |
| incoming / inherited / outgoing | 7:311, 1022, 1082; 9:17, 132, 204–235, 649 (22 lines in ch. 7, 27 in ch. 9) |
| level | 7:15; 9:262 |
| schedule | 7:1075, 1206 |
| lift, primitive under the contraction `δ` (Dict 4.2, first sense) | 7:131–135 ("zeroth-factor lift", "first lift", "scalar lift") |
| lift to the covering lattice (Dict 4.2, second sense) | 1:181 |
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
| test as indicator of a Borel condition (Dict; here adjectival, "tested") | 9:541 "the tested and clipped density of (ch04:path-action)", 9:547; cf. 4:489–493 |
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
| allocation (i), partition-of-unity weights | 9:81–82 ("sector allocation indicators") |
| collision | 1:365, 426, 477 |
| weight = scaling dimension | 2:50–51 (defined here, earlier than Dict's 3:168); 7:350–357, 609, 1026; 9:211–215 |
| cost | see section 3 |

`stage` and `history` are not in this table: in these chapters neither has the sense Part II records (see 2.2 and section 3).

#### 2.2 New senses of dictionary words

Listed in section 3: `row` (table row, row vector), `actual` (original torus; with cutoffs), `selected` (subfamily of terms), `test`, `label` (polymer label; pair `(d, c)`), `tag` (the index `d`), `mark`, `response`, `stage`, `history`. Further:

- `stage` (14 lines: 7:22, 833, 1056, 1067, 1069, 1072, 1203; 9:110, 421, 427, 928, 935; 9s:83, 214; at 7:1056 and 1067 only as the subscripts `a_stage`, `P_stage`). Dict 2.1 has stage = "one renormalisation transformation, or its index". Here it is the regularity class with subscript `j`, fixed before `L`: "fixed stage bounds … chosen before `L`" (7:22–23), "a finite collection of stage data" (7:1069), "at fixed stage and ratio" (9:110), "The positive stage constant `c_j^pre`" (9:421), "finite-stage requirements" (9s:83). This is the sense defined at 10:25–26: "A stage `j ≥ 1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds". None of the 14 lines means "step". Basis R (through 10:25–26).
- `history` (2e:253; 7:1202). Dict: the list of block ratios and averaging orders. Here: the whole renormalisation trajectory with its fixed data, see section 3.
- `frozen` (7:733–737): weights held at their value at a real base point.
- `layer` (7:454–455 "All three response layers"): the zeroth, first and second background derivatives.
- `primitive` (7:114, 125, 135): preimage under the contraction `δ`, the standard sense.
- `lift` (9s:189–191: the operators `W_F`, `W_a`; 9:208 "lifted potential"). The uses at 7:131–135 and 1:181 are Dict's senses (2.1).
- `extracted` (7:1161, 9:535: coefficient taken out; 9:75: determinant factored out).
- `completion`: two senses in chapter 7, the gauge completion `𝖩 + F*F` and the block completion `𝒢` (section 1); neither is Dict's "positive completion".
- `columns` (ch. 2), `spectator` (2e), `regular activity` (ch. 8), `kinetic`, `branch`, `principal`, `centered`, `scalar`, `amplitude`: see sections 1 and 3.

#### 2.3 Dictionary terms that these chapters define or clarify

| Dictionary term | What these chapters add | Basis |
|---|---|---|
| parent (Dict 2.2, "used undefined") | 1:218–220: "every fine site can be written uniquely as `Ly + z` … The resulting parent map commutes with signed coordinate permutations." | R |
| insertion (Dict section 6) | 1:331–334: "A family of insertions assigns to `v ∈ 𝒯` and `y ∈ Λ_{R_pD_N}` a continuous gauge-invariant function `I_{N,p}(v, y; U)`", local on a translate of a fixed stencil. | D |
| weight (Dict 2.5) | First defined at 2:50–51, not 3:168. | D |
| inherited loop action (Dict 2.3, identification inferred) | 9:21–28: `P^path = β𝒦 + ℒ`, "`ℒ` is the quadratic loop correction. This identity defines `𝒦`, `ℒ` from (ch04:path-action)". 7:1089–1091: its coefficient matrix `r(z)` "has exponential sum bounded by `Λ^loop` and zero zeroth and first moments". So it is the `β`-independent quadratic part of the path action. | R |
| matching (Dict 4.2) | Classical: `E − J − S_3 − S_4 = O(v⁵)` with equal Hessians (7:988–998). Quadratic: subtraction of `α b_H` from the determinant symbol (7:1159–1167). | R |
| subpower (Dict 2.6) | 9:109–110: "The function `P_j` has subpower growth: `log P_j(𝔟)/log 𝔟 → 0` at fixed stage and ratio"; 9s:27. Agrees with Dict. | D |
| envelope (Dict 4.2, not glossed) | 9:793–794: "Their sum added to the majorant at `u_0` is a common summable envelope"; also 9:159, 690, 796. A summable dominating majorant. | R |
| regrouping (Dict 4.2: "the cluster expansion step") | 9:651–667 is narrower: the identity "exact-cover sum of the `K_P` equals `ℱ⁰ e^{Σ ℓ_a}`". The labels call it "fusion". | R |
| Wilson initialization (Dict 4.2) | 9:818–904 is the construction: the representation of the Wilson density at the finest scale. | R |
| centered log determinant (Dict section 4) | 9s:47, 59: the exponent contains `s(x) − s(0)` with `s = ½ log det A`; 9:126 lists "centered determinant variation" with majorant `P_j(t_{m+1} + g)`. Supports Dict's presumption; the identification of the two is inferred. | R / I |
| seeded / unseeded law (Dict section 4) | 9:283–284 only: "no comparison between unrelated event indicators or a seeded and an unseeded law has been made", after requiring windows to be clean and assigning a window meeting a large-field component to that component (9:278–280). Consistent with "with / without a prescribed large-field component"; still undefined. The only other occurrence is 6:1544. | I |
| regularity-stage index `J_m` (Dict section 4) | Not named in these files. 9:30–36 says `q_m` are derivative orders and `ϖ_m` spatial exponents with `q_{m+1} ≥ q_m ≥ 6`, `ϖ_{m+1} ≥ ϖ_m ≥ 2`. The constants of ch. 9 carry a subscript `j` called "stage" ("the positive stage constant `c_j^pre`", 9:421; "at fixed stage and ratio", 9:110), fixed before `L`. Chapter 10 settles the reading: 10:25–29 defines a stage `j`, 10:129–134 defines `J(m) = j` for `A_j ≤ m < A_{j+1}`, and 10:124 distinguishes it from the smoothing order ("`ȷ_j` is the largest smoothing order used in stage `j`"). Chapters 4, 5 and 7 write `j` for the smoothing order (4:16 "fix a positive integer smoothing order `j`"; 7:600 "fixed at the given smoothing order"; `C_j` at 7:664), chapter 9 for the stage. So two different indices share the letter `j`. | R (ch. 10); I (that the `j` of ch. 7 is the smoothing order throughout) |
| moving (Dict section 4: "moving comparison fields") | Not that phrase. "Moving" appears to mean depending on the variable, against "frozen": "the moving Haar Jacobian" (7:262–263), "these frozen weights are uniformly comparable to the moving weights" (7:734–735). The text does not say so. | I |
| eligible (Dict 1.8 (ii), inferred) | Two forms of one notion. Per activity (4:440–450): a large-field activity has "an additional Borel gauge-invariant eligibility test `𝓔_i^extra`" and vanishes outside `{Bad_m(U) ∩ Y_i = I_i^bad} ∩ 𝓔_i^extra`. In the abstract setting of chapter 8 it appears as the restriction to allowed covering families (8:289–295): "the allowed finite families `B` of such labels with disjoint supports and `⋃ I_η = D` … The exact rules for eligibility are part of the definition of an effective density; they may exclude some otherwise possible covers." The uses in chapter 9 are of the per-activity kind ("The large-field indicators in their eligibility criteria can read outside `Y_i`", 9:94; "The activity labels and eligibility criteria are independent of `β`", 9:902). | D (4:440–450); R (8:294–295) |
| compulsory; Warnings; output anchors; likelihood tests | Do not occur in these files. | – |
| width; counting; representative; lift; event label; amplitude; level | Width as in Dict (7:360, 1000, 1128, 1177). "Normalized counting measure" (7:618, 644) is the normalised version, unlike Dict's "counting norm". | R |

---

### 3. Multi-sense words

Counts are lines unless stated.

**row** (17 lines). (i) component of the action vector / row of `ρ`: 11 (7:352, 976, 977, 985, 993, 1059, 1168; 9:544, 568, 835, 840); of these 7:1059 "the prescribed coarse quadratic row" is doubtful (singular; presumably the whole quadratic term `J`). (ii) matrix row: 3 (7:711; 9s:192, 197). (iii) row of the displayed table: 2 (9:140, 145). (iv) row vector: 1 (1:80). The kernel, symbol, operator and factorisation senses of Dict 1.1 do not occur, though 9:568 "row coefficient matrix `S(0)`" with `c_dir I + S(0)*S(0) = I` is the factorisation written with the letter `S` where 7:974 writes `ρ`.

**actual** (53 matches of the word: 2e 1, ch. 7 26, ch. 8 2, ch. 9 15, 9s 9; and "actually" once, 7:504).
- (i) the gauge-covariant block average and objects built with it, against "straight" or "linear": 14 (7:554, 574 "actual stationary tangent `W_a`", 780, 786, 829, 874, 888, 1042 "The actual smooth tangent bounds", 1114, 1154, 1200; 9:913; 9s:191, 230 "the actual stationary tangent"). 7:786 and 7:829 could also be read as (ii). 7:504 "the block average actually used in the block integral" makes the same contrast.
- (ii) of this construction, against a model or a separately chosen object: 23 (7:11, 313, 344, 498, 572, 623, 640, 764, 901, 1154; 9:239, 304, 541, 960, 964; 9s:35, 111, 114, 138–139, 299; 2e:253; 8:18). "Actual sector" (9:304–305; 9s:299 "actual-sector inputs") is a fixed compound from chapter 6, whose section 6:439 is titled "The actual sector Gaussian".
- (iii) the running coupling: 3 (7:574; 9:17, 385).
- (iv) exact, emphatic: 5 (7:215, 333, 389; 9:284; 8:269).
- (v) the regulated lattice denominator at zero background against the free quadratic one: 1 (7:440 "The actual denominator minus the free quadratic denominator"; the denominator is the "zero-background denominator" of 7:331, so the contrast is not non-flat against flat).
- (vi) determined by the configuration: 1 (9:890 "the actual set of these components").
- (vii) new: with its indicators and clipping, against the bare quadratic expression: 3 (9:547, 612, 861 "actual clipped … channel").
- (viii) new: the original torus or field against the auxiliary reflected ones: 3 (9:931, 936; 9s:295).

Senses (i) and (ii) are hard to separate in ch. 7; the split is approximate and could shift by two or three lines.

**selected / selection** (26 lines). (i) fixed by the construction: 6 (7:286, 553, 576, 667, 1202; 9:567); 7:427 "selectors" is separate, see section 1. (ii) large-field selection as in Dict 1.3: 4 (9:108, 153, 279, 440). (iii) retained for joint treatment, "selected low-order terms": 5 (9:312, 314, 319, 320, 383). (iv) new: a finite subfamily of terms or labels: 7 (9:157, 215, 637, 671, 677, 687, 890); at 9:215 "Every surviving selection in the ordered Taylor expansion" it is a choice of one term per factor. (v) ordinary: 3 (2:292; 2e:103; 8:193). **chosen** (26 lines) is ordinary throughout, except "chosen before `L`" (7:23), which carries the order-of-constants meaning Dict records as "pre-`L`".

**test** (16 lines). (i) test function: 7 (1:353–393). (ii) classical test connection: 4 (2:13, 103, 150, 416). (iii) "curvature tests" = curvature coordinates: 1 (2e:60, title only). (iv) one evaluation of a symbol: 1 (7:215 "One transverse test"). (v) "tested" = restricted by the indicator of a small-field condition: 2 (9:541, 547); this is Dict's indicator sense used as an adjective (cf. 4:489–493 "the remaining tested plaquettes"), not a new sense. (vi) "tested" = under consideration: 1 (9s:224 "each tested small-field coarse configuration"; inferred). Dict's senses "location" and "variable" do not occur.

**label** (46 prose lines; 1:390 is the LaTeX option `[label=…]`). (i) polynomial label or its index set: 17 (ch. 1: 331, 393, 481; ch. 2: 13 lines; 2e:254). At 1:331 the labels are an abstract set `𝒯`; from 2:97 the observable label is the pair `v = (d, c)`. (ii) polymer label `γ`, defined 8:24: 13 in ch. 8, plus 9:154. (iii) index of a large-field or logarithmic activity: 8 (8:290, the labels `η`; 9:638, 671, 674, 676, 678, 684, 902). (iv) index of an incoming regular activity: 1 (9:221 "the per-label gain is `L^{-5}`"). (v) "fixed labels", the discrete data of a representation: 4 (9:385, 771, 816, 939). (vi) cutoff-failure label = event label: 2 (9:111, 133).

**tag** (8 lines). (i) the index `d` of `V_d`: 2 (2:98, 99). (ii) the random index `α`: 6 (9:83, 85; 9s:127, 134, 221, 242).

**mark** (2). 7:378 "For a mark of direction `a` and Lie algebra direction `u`": an external background leg with polarisation `e_a` and colour `u`; the sentence goes on to give "the linear vector insertion" `b_lin(p;k)`, the first-order background-field vertex with external momentum `p` (7:378–385). Inferred; not Dict's "with observable insertions". 9:263 "marking one changed factor": ordinary.

**window** (3: 9:142, 278, 279). Dict sense.

**history** (2: 2e:253 "the section used along the actual renormalization history"; 7:1202–1203 "an entire selected history requires that its incoming paths obey the fixed stage bounds"). The renormalisation trajectory with its fixed data (a history has incoming paths); not Dict's list of block ratios and averaging orders. Basis R. Elsewhere the same thing is a "renormalization trajectory" (1:208, 488–489; 2:436) or simply a "trajectory" (1:465, 467; 8:374; 9:974).

**stage**: see 2.2 and the row on the regularity-stage index in 2.3.

**source** (6). (i) generating-function source: 4 (8:252, 266, 268, 364), standard. (ii) Dict's `b_Y`: 1 (9:924 "clipped frozen source"). (iii) ordinary: 1 (9:168).

**cost / costs / costing** (32 matches: ch. 2 1, ch. 7 20, ch. 9 6, 9s 5). (i) "contributes the factor", whether small or large: about 22 (small: 7:618 "costs `O(μ⁴)`", 905–910; large: 7:619 "costs `L⁴`", 674, 749–751, 1120, 1126, 1175; loss: 7:359, 1178; 9:510, 610). (ii) a polynomial loss as a noun: 5 (9:267, 434, 438, 712; 9s:273). (iii) an increase of the exponent: 3 (9s:147 "costs at least `Δ` in the exponent", 153, 160). (iv) a small probability: 1 (2:392 "probability cost of a large-field region"). In sense (i) the word is used for gains as well as losses, so "contributes a factor" is the safe replacement. **gain** (9: 1:454; 2:391; 7:1043, 1153; 9:221, 245, 260, 264, 282): a small factor. **loss** (6: 7:1012; 8:77; 9:265, 437; 9s:160, 184): a polynomial or width loss. **fits** (5 lines: 7:1195; 9:201, 378, 426, 900): "is at most (a fraction of)". `price`, `pay`: none.

**detector, probe, readout, table, word**: no occurrences (the table at 9:123–134 is referred to through "rows").

**response** (6, all ch. 7; none of Dict's four senses). (i) a log-determinant as a function of the background field: 7:277 "Its determinant response is `Π_μ = ½ log det A_μ − log det G`"; 7:791 "blocked response". (ii) an operator with its background derivatives: 7:367 "the Wilson response", 624 "left-coordinate response", 743 "The kinetic response cancels". (iii) 7:454–455 "All three response layers": `a`, `b`, `c`. Basis I for all; nearest standard wording: *dependence on the background field through second order*.

**transport** (about 43 lines; recounts give 42 to 44). Parallel transport: ch. 1, 2, 2e throughout and 7:147, 347, 643, 1005, 1009, 1178 (about 32). Stationary-field map `W`: 7:1088, 1112, 1136, 1141, 1201; 9:913 (6). The map `T` on two-forms: 9s:170 "the curvature transport", 9s:192 "the two-form transport", with `d_{1,f} W_a = H_f^{-1} T H_c d_{1,c}` (9s:194) (2). Covariantised rows: 7:975, 977 (2). "Row transport" (1:80) is the convention of section 1.

**frame** (16 lines). All Dict's sense. In 7:873, 892 the frame is an integration variable ("fine-plus-frame coordinates", "coarse-frame directions").

**anchor** (16 lines). Base point: 15. Real base point of a continuation: 1 (7:733).

**phase** (6). (i) phase of the theory: 1:415, 418, 499 (undefined; `notation.md` restricts it). (ii) complex phase factor: 7:204, 600, 1108.

**Further multi-sense words found.**

- **insertion** (39 matches). (i) local observable at a site: 1:331, 350, 476; 2:99, 403; 8:192–193. (ii) derivative of an operator in the background field: about 27 in ch. 7. (iii) transported curvature factor: 7:147. (iv) the linear map `ℛ`: 7:243.
- **weight** (62 matches). (i) scaling dimension: 2:51; 7:350–357, 609, 1026; 9:211–215. (ii) exponential support or path-length weight: 7:165, 999, 1082; 8:16, 78, 155, 176–177, 362; 9:179–182, 231, 283, 438, 516. (iii) the Fourier weights `h_l` and the weighted Hilbert norms: 7:589–751 and 870–916 (about 20). (iv) numerical coefficients: 7:299 "bubble weights"; 9:355 "fourth-difference weights"; 8:54 "probability weights". (v) density factors: 9:264 "nonquadratic local weights".
- **common** (45 matches). (i) volume-independent, defined 7:36: most of ch. 7. (ii) shared or joint: 7:154 "common anchor"; 9:115, 139, 266, 785, 966 "common law", "common Gaussian"; 1:490, 503.
- **scalar** (28 matches). (i) zero-form or frame component: 7:507, 580, 591, 696–703, 721–722, 915. (ii) field-independent constant: 8:359; 9:56, 399, 717, 757, 764, 814, 904; 9s:123. (iii) number-valued: 7:124, 134, 207, 214, 508, 519, 686; 9s:20.
- **sector** (13 lines). (i) reflection half: 1:244, 247. (ii) Dict's: 8:28, 359; 9:50, 75, 81, 105, 305, 436; 9s:16, 170, 299.
- **branch**. (i) branch of stationary solutions: 10 lines (above). (ii) branch of the logarithm: 8:129. Dict's "case of a definition" does not occur.
- **channel**. (i) vector or ghost field type: 7:331, 414. (ii) term of the quadratic path action: 8 in ch. 9.
- **completion / completed**. (i) gauge completion `𝖩 + F*F`: 7:229, 251–252 and the lines of section 1. (ii) block completion `𝒢`: 7:687–691. 7:773 "blocked completed matrix" appears to combine both.
- **centered**. Symmetric: 1:183, 217; 2:188, 285; 7:407, 703. Frame normalised in the mean: 7:505–700, 883, 914; "recentering" of the frame: 7:507, 581, 643. "Recentering" as translation of the reflection cube: 9:350. Zero-mean Gaussian: 9:774. With a constant or the flat value subtracted (inferred): 9:126, 294; 9s:236, 283.
- **rooted**. (i) rooted coordinates of the frame: 7:521, 530, 674, 693. (ii) rooted cluster sums and estimates, as in the rooted form of the Kotecký–Preiss theorem: 8:15, 116, 170, 179; 9:179, 197, 685, 796, 894. The second is standard.
- **lift**. Primitive under `δ`: 7:131–135. Lift to the cover: 1:181. The operators `W_F`, `W_a`: 9s:189–191. "Lifted potential": 9:208.
- **principal**. Zero alias: 7:701–722, 812–816, 1146. Leading: 9:235, 268.
- **amplitude**. Fourier amplitude: 7:815, 1136, 1144–1145, 1173. Bound: 7:1196. `M^cut`: 9s:23.
- **logarithmic** (23 matches). Lie-algebra coordinate: 9s:33, 176, 295. Term of the exponent: 9:368, 607, 633–698. Logarithmic derivative: 7:522, 673; 9:247. Of a log-determinant: 7:335. In `log β`: 1:50, 462; 9:712 (the last is unclear).
- **fold**. Aliasing sum: 7:810. Reflected extension: 9s:169–175, 233.
- **flat**. `U = 1`: 7:24, 226; 9:332, 496, 726. "Flattening": 9:676.
- **auxiliary** (24). Regulated fine determinant: ch. 7 (8). Small reflected tori: 9 and 9s (16).
- **degree**. Polynomial degree; Taylor degree = field factors (7:1079); number of elementary factors (9:172).
- **path**. Lattice path; path action (section 1); matrix path `M(t)` (7:397).
- **placement**. Position in continuum units (1:209); position in the tiling (1:322); side of a product (7:753).
- **cutoff**. Ultraviolet cutoff `N` (1:15, 209, 387; 9:947); threshold or indicator (7:25; 9:111, 840; 9s:10, 127); cutoff function (9:476). Agrees with Dict 1.8.

**Occurrences fitting none of the senses:** 7:1059 "the prescribed coarse quadratic row" (counted under `row` (i) with a doubt); 9:712 "polynomial logarithmic costs"; 7:742 "Trace norms and recording"; 9s:283 "centered expression".

---

### 4. Terms these chapters do not determine

#### 4.1 Still undetermined

No definition or explicit gloss was found in these files or, by grep, elsewhere under `chapters/`.

| Term | Where | What can be said |
|---|---|---|
| recording (the word) | 7:461, 742 | The estimate meant at 7:461 is determined (section 1); the word is not explained. `notation.md` has "recording-scale change" for ch. 11, and 11R:25 ff. "recording scale" is a different object. |
| coordinatewise splice | 7:637 | The "fixed-position read" is narrowed in 4.2; the splice is not explained. |
| exterior identity | 7:408, 686 | Not displayed. Presumably `d_1*d_1 + d_0 d_0* = Δ`; 11:1692 agrees, 5:840 uses the phrase for another identity. |
| direction selectors | 7:427 | – |
| principal real cube | 7:704–705 | – |
| live tag actions; tag-coincidence radius | 9s:127, 221 | – |
| seeded / unseeded law | 9:283–284 | Section 2.3; the only other occurrence is 6:1544. |
| missing-coordinate factor | 9:77 | – |
| "factor after deterministic subtraction" | 9:124 | Which subtraction is not said. |
| read-count polynomials; support compression; inspected support | 9:147, 231, 220 | – |
| centered (expression, auxiliary bound) | 9:294; 9s:283 | – |
| numerical band margin | 9:950 | Possibly the inner barriers of 10:212–222. |
| "affine" and "reflected" in normalized affine directions, reflected normalized directions | 9:35, 502; 9s:296 | The normalisation itself is settled, see 4.2. |
| phase (of the theory) | 1:415, 418, 499 | Deferred to later chapters. |

#### 4.2 Settled or narrowed by another chapter or by a reference

These terms are not explained where they are used, but the text fixes or narrows their meaning elsewhere. Details and quotations are in sections 1 and 2.3.

| Term | Where | Settled or narrowed by | Basis |
|---|---|---|---|
| `c_lin` | 9:846 | 4:474–480: "fix constants `c_dir, c_lin, R^rel > 0` with `16 c_lin < c_dir`"; the slope of `clip_t` above `t`. | D |
| plaquette whose relaxed small-field condition is not automatic | 9:548 | 4:489–492: "`χ ≤ 2` makes all tests with `t_m e^{dist(x,y)/R^rel} ≥ 2` automatic". The conditions that are not automatic are those of the finitely many remaining plaquettes. | R |
| quadratic-tilt criterion | 9:115 | 9:115–116 cites Proposition (ch06:common-majorant), 6:1123–1138 ("tilted Gaussians"). | R |
| the stage index `j` | ch. 7 and 9 subscripts | 10:25–29 (stage), 10:124 (`ȷ_j`, smoothing order), 10:129–134 (`J(m)`). Two indices share the letter `j`; section 2.3. | R / I |
| classical bound contraction; inherited-loop contraction | 9:970 | 10:35–36 gives the equation references (ch07:classical-budget), (ch07:inherited). | R |
| safe chart; "recognizes" | 9s:139–141 | 5:1009–1015, the estimate (ch05:nonlinear-tree). | R |
| dummy Gaussian coordinates | 9:59, 72 | 9:59 and 9:72–73 themselves, in part. | R |
| recording estimate (the object) | 7:461 | 7:457–460; called "The Fourier mesh estimate" at 7:762. | R |
| derivative reserves | 9:34 | 10:737–739: "through one order beyond the outgoing order. This is a numerical derivative reserve". | R there; I for 9:34 |
| normalized directions | 9:35, 502; 9s:296 | 4:580–581; 6:626–638: directions scaled by the threshold. | R |
| stationary residual | 9:77, 130 | 6:615–621: `𝖠 m_Y + f_Y`, bounded by `C t_f e^{-cB}`. | I |
| determinant inverse identity | 9:140 | Probably 6:1192–1203. | I |
| thermal | 7:765 | The label `ch07:thermal` on `T(v)` (7:232–233), "The Gaussian contribution at a stationary fine configuration" (7:231). | I |
| bridge legs | 7:597 | The label `ch05:actual-bridge` (5:1132) on the bound for `W_a`; 5:1151–1152. | I |
| padded block | 7:599, 628 | The block-average patch of radius `(j+3)L` (4:17) or the macro-box of radius `(j+7)L` (4:298–299); the wording favours the patch. | I |
| fixed-position read | 7:637, 710 | 4:174–189: the connector `Y_{e,z}` and its average over offsets. | I |
| prescribed coarse classical action `a_c`; quantum contribution `d_c` | 9s:258–259 | 9s:270–271 with 7:994–998 and 7:1159–1167. No formula is displayed. | I |
| health | 9:563, 839 | 9:553 and 4:427: the small-field indicator `h_X`. | I |

---

### 5. Synonym clusters

| Concept | Words in use |
|---|---|
| the operator `W` (coarse field ↦ stationary fine field) and its versions | "stationary tangent" (7:574, 780, 882), "transport" (7:1112 "straight stationary transport `W_s`"), "lift" (9s:189–191 "forest-coordinate lift `W_F`", "smooth actual lift `W_a`"), "representative" (7:574 "its forest representative is `W_F`"), "fine-wave amplitude of the transport" (7:1136). The "curvature transport" and "two-form transport" of 9s:170, 192 are the related map `T` on two-forms, not `W`. |
| the critical-point map | "stationary branch" (ch. 7, 9, 9s), "stationary representative `ζ(x)`" (7:505), "stationary chart" (7:867), Dict's "stationary graph" |
| the constant `b` | "soft constraint" (1:409; 7:574), "block penalty" (7:523, 874), "penalty Hessian" (7:476), "block parameter" (1:420) |
| the index `d` of `V_d` | "tag" (2:98), "normalization index" (2:402), "filtration index" (`notation.md`) |
| transported plaquette curvature | "transported curvature" (2:171), "curvature measurement" (2:362), "curvature coordinate" (2e:65), "curvature test" (2e:60), "curvature insertion" (7:147) |
| sequence of scales and couplings | "renormalization trajectory" (1:208, 488–489; 2:436), "trajectory" (1:465, 467; 8:374; 9:974), "history" (2e:253; 7:1202), "scale schedule" (7:1075, 1206) |
| one-parameter family of density data | "curve" (9:768, 903, 938), "activity curve" (9:390) |
| lower bound | "floor", "gap" (9s:42, 138), "margin" |
| lower bound on `β̂` | "threshold", "inverse coupling threshold", "coupling threshold", "coupling entry threshold" |
| the reference coupling `β̂_{m+1}` | `𝔟` (9:17) and `z` (9s:19) |
| the polymer-activity norm counting each polymer at every site of its support | "site norm" (8:69; 9:607), "containing-site norm" (9:518, against "anchored bounds", 9:513; 8:76), "support norm" (8:196, no formula; inferred), "attachment norm" (9:697; the same form applied to majorants, 9:659; inferred). That the four are one norm is not stated by the text. |
| the margin `δ` | "additional exponential support decay" (8:150; 9:148, 687), "support-weight reserve" (8:362; 9:438), "support reserve" (9:919), "unused support exponent" (9:267) |
| small-field indicator `h_X` | "event indicator" (11 matches in ch. 9), "health event indicator" (9:839), "small-field conditions" (9:510) |
| the gas of small-field polymers | "regular" (ch. 8), "ordinary" (ch. 9) |
| the set `I_η` | "large-field sites assigned to that activity" (8:288), "prescribed large-field site set" (9:643), "prescribed set" (9:893) |
| the identity of Proposition 9:651 | "exact regrouping", "absorbing", "fusion" (labels), "exact reassembly" (ch. 8, for the related identity) |
| event label | "cutoff-failure label" (9:111), "event label" (ch. 6) |
| enlarged block | "padded block", "padded block average patch" (7:599, 628); whether this is the block-average patch (4:17) or Dict's "macro-box" (4:298) is not determined |
| makes vanish | "kills" (7:201; 9:525), "removes" (9:210–213) |
| the mesh-mean error bound | "recording estimate" (7:461), "Fourier mesh estimate" (7:762) |
| link | "link" throughout; "bond" at 9:58; "edge" at 7:204, 349; 9:456 |
| summable majorant | "envelope" (9:159, 690, 793–796), "majorant" (9:124, 607, 655) |
| field-independent constant | "scalar" (ch. 9), "field-independent term" (9:714), "scalar normalization" (9:904; 9s:123), "scalar factor" (8:359) |

---

### 6. Overloaded symbols noticed

| Symbol | Meanings |
|---|---|
| `W` | stationary-field operators `W`, `W_a`, `W_s`, `W_F` (7:506, 574, 1112); Wilson plaquette energy `W(u)` (9:823), written `w(u)` at 1:92; bound on coordinate counts (9s:152); `W = d_c − ψ − ½ log det A` (9s:262) |
| `W_a` | "smooth actual" representative, distinct from the forest one `W_F` (7:574; 9s:189–191; 5:1151–1152). `blueprint/notation.md` line 242 speaks of "the actual forest-coordinate response `W_a`", which contradicts this. |
| `H` | two-form metric (7:312, 974); "block average derivative" (7:476); coarse symbol `H(p)` (7:1138); `H_pre` (9:420); `H_4` |
| `B` | penalty Hessian (7:476); `B_x` (7:649); covector `B(u, v)` (7:896); block radius `B = B_m` (9:16); family `B ∈ 𝔠(D)` (8:289); bounds `B_H`, `B_loop` |
| `Z` | coarse-frame projection (7:477); `Z(x) = S_x(r(x))` (7:527); tensor in a proof (7:123); `Z = X ∪ N_2(o)` (9:463); partition functions |
| `K` | `K = m_μ X` (7:477); operators `K_c`, `K_f`; constant (7:77); large-field activities `K_η`, `K_P`, `K_I`; `𝒦` path action (9:23); norm `𝒦_m` (9:665); exponent `K` (9:299) |
| `M` | `M_μ`; matrix path (7:397); `M_act`, `M_core`; mixed kernel `M(p)` (7:562); straight averaged connector (7:693); `M^cut`; `M = (2q)⁴` (1:289); number of measurements (2:243); `M_x` (9:320); `M_i` (9:807); index set in `G_M` (9:99) |
| `R` | regrading `R_d` (2e); gauge action `ℛ`; resolvent (7:418); `R(T)` (7:652); block-average correction (7:694); loop bound (7:1160); `R_f` (9:486); Wilson remainder `R(u)` (9:832); `R(g, x)` (9s:61); dependence radius (9:322); physical period `R_p` |
| `S` | spectator function (2e:39); `S_W` (2e:115); `𝒮(J)` (2:242); `S_x(a)` (7:526); joint action `𝒮` (7:872); loop symbol `S(p)` (7:1094); `S_3`, `S_4`; row coefficient matrix `S(0)` (9:568, the `ρ` of 7:974); region `𝒮_x` (9s:116); Schwinger kernels `S_n` |
| `T` | `T(v)` (7:233); `T = \|k\| + μ` (7:397); stationary tangent `Tu` (7:882); two-form map (9s:194); `T_4` (9:828); `T_d` (2e:229); `T_d f` (2:256); Lie-algebra element (9:464) |
| `F` | curvature; gauge condition (7:251); frame `F_x` (7:642); force `F_e` (2e:117); `F_d`, `F` (9:552, 574); `F_x` (9:319); `ℱ⁰`; `ℱ_d` (2e:227); observable (1:265) |
| `J` | jet (ch. 2); action `J(v)` (7:976, used at 7:185 before its definition); `J = −K_c` (7:539); joint Hessian `𝖩` (7:242, 252); `J_0` (7:648); `J_d`, `J` (9:553, 575); `J_Haar` |
| `E` | action difference (7:51); stationary value `E(v)` (7:938); `E_{xy}` (7:643); `E = Σ h_Z R_f + F` (9:590); `E` (9s:239); norm `ℰ_m`; projection `ℰ` (2e:152); edge set `E_s`; energy `E_s^W` |
| `L` | block ratio; `ℒ` loop action (7:237; 9:26); cluster series `𝓛(z)` (8:111); `L(g, x)` (9s:62); `L_x` (9:337); `L_d`, `L_p` (9:546, 861); constants `L_0, L_1, L_h` (9:597); Lipschitz constant `L_0` (9s:212) |
| `h` | scale parameter (2:112); element of `H_4`; half side (1:242); weights `h_l` (7:587); integrand `h(k)` (7:303); `h = 𝔟^{3/8}` (9:176) and `h = 𝔟^{-7/16}` (9:295; 9s:20); indicator `h_X`; constant in `\|X\| ≤ h c(X)` (8:59) |
| `j` | smoothing order (4:16; ch. 7, e.g. `C_j` at 7:664) and regularity stage (ch. 9, e.g. `c_j^pre` at 9:421; defined 10:25); chapter 10 writes `ȷ_j` for the smoothing order used in stage `j` (10:124) |
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

### 7. The ten most confusing terms

1. **actual** — 53 matches, eight senses; in ch. 7 the reader cannot tell "gauge-covariant, not linear" from "of this construction" from "exact".
2. **response** (ch. 7) — a log-determinant, an operator with its background derivatives, or the triple of orders; a fifth and sixth sense beyond Dict's four.
3. **insertion** — a local observable (ch. 1, 2, 8), a derivative in the background field (ch. 7), a curvature factor (7:147), a linear map (7:243).
4. **fixed-position read / coordinatewise splice** (7:637, 710) — undefined; a load-bearing step of the frame estimate. The first can be inferred from the connector of chapter 4, the second cannot.
5. **regular activity** — a polymer activity in ch. 8, an additive term of the exponent in ch. 4 and 9; ch. 9 says "ordinary" for what ch. 8 calls "regular".
6. **the reset / thermal / bridge / fusion / health** — words that reach the prose (9:748, 7:765, 7:597) or only the labels, and are intelligible only through the label names; "health" (9:563, 839) is intelligible only through the symbol `h` of 4:427.
7. **weight** — scaling dimension, exponential support weight, Fourier weight `h_l`, numerical coefficient, density factor; several within single paragraphs of ch. 7 and 9.
8. **cost** — used for small factors, large factors and energy increases alike; 7:618–619 has both directions in consecutive sentences.
9. **stationary tangent / transport / lift / representative** — four words for the operators `W`, with subscripts `a`, `s`, `F`, a contradiction with `notation.md` on `W_a`, and "transport" also for the two-form map `T` (9s:170, 192).
10. **selected / selection** in ch. 9 — the large-field selection, the low-order terms retained, and arbitrary finite subfamilies of labels, within one chapter.

Close behind: **stage** with the letter `j`, which means the regularity class in ch. 9 and the smoothing order in ch. 7, neither being Dict's "step"; **completion**, with a gauge completion and a block completion a few pages apart in ch. 7; **transfer matrix** (1:473), a standard term used for the mixing matrix of labels; **contact term** (7:501), not a coincident-point term; **scalar**; **common**; **path** for "path action".

---

### 8. Not read / not checked

- All seven assigned files were read in full. The figure files input at 1:304, 2:184, 8:300 (`figures/*.tex`) were not read.
- Chapters 4, 5, 6, 10 and 11 were not read; they were consulted by `grep` and at the lines cited in this section (4:16–17, 172–189, 298–299, 427, 440–450, 474–493, 580–581, 627–641; 5:840, 1000, 1009–1015, 1123–1137, 1151–1152; 6:85, 439, 615–638, 1123–1128, 1192–1203, 1257, 1544; 10:25–29, 35–36, 124–134, 212–214, 737–739; 11:1692). Chapters 12–19 were searched only by `grep`, for the terms of section 4.1.
- The occurrence classifications for `actual` and `cost` rest on the full read plus the grep line lists; the split between senses (i) and (ii) of `actual` could shift by a few lines.
- Dictionary line numbers refer to commit `7bec3925`; the ones that point into these files (7:237, 7:974, 7:1160, 9:283, 9:573, 9:837) agree with the worktree.
- No proposed equivalent was checked against the literature. No Lean source was consulted.
- Sections 5 and 6 list what was noticed while reading; they are not exhaustive. The per-sense splits of `weight`, `common`, `scalar` and `logarithmic`, and the counts "22 lines in ch. 7, 27 in ch. 9" for incoming / inherited / outgoing, were not recounted.

---

### Changes folded in

Origin: B = independent audit; R = re-audit report R2. "Verified" means the cited chapter lines were opened for this fold and support the change; "not reopened" means the change rests on the audit's reading.

**Header.**
- Notices "Audited" and "Status: reproduced as returned" replaced by one status paragraph; commit of the text stated (own reading; `git diff 7bec3925 eb97dec6` on the seven files shows changes only at 7:1086, 9:212, 9:548).
- Pipes inside table cells escaped so that every row has the stated number of columns (own; no change of content).

**Section 1.**
- gauge completion: row split; "block-completed form `𝒢`" is the completion by the block penalty, not the gauge completion; equivalent "gauge-fixed Hessian" withdrawn for 7:687 (B error 1; verified 7:687–691, 728–729, 773).
- gauge completion quotation: `C = 𝖩 + F*F`, not `J` (B error 5; verified 7:242, 251–252).
- slots: basis I → R (B error 6; verified 1:314–315).
- quadratic-tilt criterion: no longer "by name only"; explicit proposition reference (B error 3; verified 9:115–116, 6:1123–1128). Row split from "determinant inverse identity" and "stationary residual", which are now I with their chapter 6 lines (B; verified 6:615–621, 1192–1203, 1257).
- health domains: basis R → I (B; verified 9:553, 563, 839; 4:427).
- adjacent pair: basis R / I → D for the pair (B; verified 9:15).
- classical bound contraction / inherited-loop contraction: equation references confirmed by 10:35–36 (B; verified).
- dummy Gaussian coordinates: separated from the scalar-bookkeeping row, basis I → R in part (B; verified 9:59, 72–73).
- derivative reserves: own row, narrowed by 10:737–739 (B; verified).
- affine Hessian: "define at first use" replaced by "defined in chapter 4" (B; verified 4:627–641).
- normalized affine directions: basis ? → R for the scaling, I for "affine", "reflected" (B; verified 4:580–581, 6:626–638; 9:503 not reopened).
- factor count: "187 (def.)" corrected, definition is at 2:52–53 (B; verified 2:52–53, 2e:186–187).
- left-coordinate Hessian: equivalent "Hessian in left-invariant coordinates" withdrawn, replaced by a marked proposal (B, R; verified 2:318–321; 7:362–363 not reopened).
- padded block: "probably Dict's macro-box" replaced by two readings, the block-average patch favoured (B, R; verified 7:599–600, 4:17, 4:298–299).
- safe chart: the estimate (ch05:nonlinear-tree) named (B; verified 5:1000, 1009–1015).
- fixed-position read: basis ? → I, narrowed by the connector of chapter 4 (B; verified 4:174–189, 7:710–712).
- exterior identity: supporting and conflicting occurrences added (B; verified 11:1692, 5:840).
- thermal coefficient: kept at I; the object `T(v)` is identified through the label (R D6, B note; verified 7:231–233, 764–765).
- recording estimate: object now R, name ?; the text's own name "Fourier mesh estimate" added as equivalent (R D6 for the object, verified 7:457–461; the phrase at 7:762 is own reading).
- bridge legs: reference to 5:1151–1152 added (B, R D5; verified).
- quantum contribution `d_c`, `a_c`: basis ? → I, narrowed (B; verified 9s:258–271; 7:994–998, 1159–1167 not reopened).
- numerical band margin: possible referent added, still ? (B; verified 10:212–214 only).
- observable label: the abstract label set of chapter 1 noted (R D11; verified 1:330–331).
- defects: equivalent changed to "large-field regions" (B).
- transfer matrix: "occurs nowhere else" added (B; not reopened).
- regrading: `R_d = I + T_d` added (B; verified 2e:229–233).
- site norm / support norm: basis split D / I; the anchored norm distinguished (R D8; verified 8:69–79, 196).
- attachment norm: formula of 9:659 quoted (own reading, prompted by R D8; verified).
- prescribed large-field site set: chapter 4 definition added (R omission 2; verified 4:440–441, 8:286–288).
- common law: variants "common Gaussian moments / estimate" added with their lines (R omission 12; verified 9:266, 966, which do not say "common law").
- first expansion: "(unsure the first is exactly Mayer)" dropped (B).
- Rows added (B's omitted terms, all verified at the cited lines; meanings marked I are my reading, not the audit's): placements; collision diagonals; the unit; raw; bidegree; integral shear; exchange symmetry; kills; trace-class cube; principal real cube; interpolated link fields; one-step integral identity; local-integral estimate; matched; pulled back / pullback; occurrences / distinguished occurrence; sector allocation indicators; pass the cutoff; plaquette filling bounds; trial inverse coupling. 20 rows, plus 6 rows produced by splitting (block-completed form; derivative reserves; dummy Gaussian coordinates and missing-coordinate factor; quadratic-tilt criterion, stationary residual and determinant inverse identity).

**Section 2.**
- 2.1: `stage` removed (B error 2; verified at all 14 lines and 10:25–26) and `history` removed (B error 4; verified 2e:253, 7:1202–1203); both moved to 2.2 and section 3.
- 2.1: rows added for lift (7:131–135; 1:181), "tested" as Dict's indicator sense, allocation, collision (B; verified). 9:840 added to `row` (R confirmed list; not reopened).
- 2.2: rewritten as a list; `stage`, `history`, `completion` added; `lift` restricted to 9s:189–191 and 9:208 (B; verified).
- 2.3 insertion: quotation completed with `y ∈ Λ_{R_pD_N}` (B; verified 1:331–333).
- 2.3 regularity-stage index: "not determined" replaced by the chapter 10 definitions; "7:600, 664" corrected (7:600 has no subscript) (B; verified 10:25–29, 124–134; 4:16; 7:600, 664).
- 2.3 moving: basis R → I (B; verified 7:262–263, 734–735).
- 2.3 eligible: the per-activity test of 4:440–450 put first, the chapter 8 form described as its abstract version (R D1; verified 4:440–450, 8:289–295, 9:94, 902).
- 2.3 seeded / unseeded: 6:1544 noted (B; verified). 2.3 envelope: 9:796 added (own).

**Section 3.**
- row: 7:1059 no longer listed twice (B).
- actual: 53 matches plus "actually" at 7:504; 7:1042 and 9s:230 moved from (ii) to (i); 9:964 moved from (iv) to (ii); counts 14 / 23 / 3 / 5 / 1 / 1 / 3 / 3; sense (v) reworded; "actual sector" noted as a compound (B; verified 7:504, 1042; 9s:230; 9:964; 7:440; 9:304–305; 6:439. The other lines of the lists were not reopened).
- selected: sense (i) is 6 lines, not 7 (B; list recounted).
- test: sense (v) is Dict's indicator sense, not new; (vi) marked inferred (B; verified 9:541, 547; 9s:224).
- label: 46 prose lines; 1:390 excluded; (i) 17; 8:290 and 9:221 reassigned; pair sense noted (B; recounted by script, verified 1:390, 8:290, 9:221).
- mark: "external plane wave" replaced by "external background leg … first-order background-field vertex" (R D7; verified 7:378–385).
- history: gloss kept, basis R, contradiction with 2.1 removed; "renormalization trajectory" references corrected (B error 4, R E6; verified, see below).
- transport: the two-form map `T` separated from `W` (B; verified 9s:170, 192, 194); count given as "about 43" (survey 43, B 42, my script 44).
- sector: 13 lines, not 15 (B; recounted).
- centered: 7:704 → 7:703; "recentering" at 9:350 added (B; verified).
- fits: 5 lines (B). response: 7:454 → 7:454–455.
- Entries added to "Further multi-sense words": completion, rooted, lift, placement (B; verified).
- "fitting none": 7:461 replaced by 7:742.

**Section 4.**
- Divided into 4.1 (still undetermined) and 4.2 (settled or narrowed elsewhere). Moved to 4.2: `c_lin`, relaxed condition not automatic, quadratic-tilt criterion, stage index `j`, the two contractions, safe chart, dummy Gaussian coordinates, derivative reserves, normalized directions, stationary residual, determinant inverse identity, thermal, bridge legs, padded block, fixed-position read, `a_c` / `d_c` (B table and R section 4; verified as listed under section 1). `slots` removed from the section (B error 6). The 9:548 entry reworded to the present text ("plaquette whose relaxed small-field condition is not automatic") (R; verified).
- `thermal`: B says both "label leak with identifiable object" and "still undetermined"; R points out the contradiction. The text decides for the first: the label `ch07:thermal` stands on `T(v)` at 7:232–233. Entry placed in 4.2 with basis I.
- `recording`: B "still undetermined", R "object determined, name unexplained". The text supports R (7:457–461); the object is in 4.2, the word in 4.1.
- Added to 4.1: principal real cube, coordinatewise splice (own).

**Section 5.**
- "renormalization trajectory" row corrected (R E6, with the correction below).
- polymer-activity norm row: caveat that the identity of the four norms is not stated (R D8; verified 8:75–78, 9:513–518, 9:659).
- enlarged block row: macro-box no longer asserted (B).
- `W` row: note on the two-form transport (B). Rows added: "makes vanish", "the mesh-mean error bound" (own).

**Section 6.** Row `j` added (B; verified). `W_a` row: 5:1151–1152 added. `J` row: 7:252 added.

**Section 7.** Item 1 count 54 → 53; item 4 and item 9 qualified; item 6 reworded ("health" is not a label word); "stage" and "completion" added to the runners-up (consequences of B errors 1, 2). The section is otherwise kept.

**Section 8.** The list of consulted lines in other chapters brought up to date.

**Corrections proposed but not applied, or found wrong on inspection.**
- R E6 says the phrase "renormalization trajectory" occurs only at 1:208 and 2:436. Wrong in part: it also occurs at 1:488–489, across a line break ("stability of the renormalization / trajectory"). R is right that 1:465, 8:374 and 9:974 say "trajectory" alone. The text decided; both facts are in section 3 and section 5.
- R D17 counts 15 matches of `stage` against B's 14. Both are right (14 lines, 15 matches, 7:1056 having two subscripts); the section gives lines.
- B: "`stationary residual` … Identification is I but strong". Applied as I, not upgraded.
- B's and R's findings on Part I (overview sections 2.1, 2.4, 2.6, 2.10, 4, 5; R E1–E5, E7, D2–D4, D9–D16) are outside this section and were not applied here. Where they rest on facts about these chapters, the facts are in the tables above.
- B's list of damaged sentences in these chapters (9:212, 7:1083–1088, 9:547–548, 9:949, 9:893–894, and the noun stacks at 9:108, 636, 839, 840; 2:158, 308) and R's table of their present state: not a terminology matter, and the survey has no section for it; it belongs to Part I, section 6. For the record, 9:212, 7:1083–1088 and 9:547–548 are repaired in the present text (verified); 9:893–894 and 9:949–951 stand as B quotes them (verified).
- R omissions 3, 10, 11, 13, 14 (health, factor count, channel, seam and slots, folded) and item 2 in part: these are omissions of Part I; the survey already had rows for them, so nothing was added.
- B on `transport`: "42 lines (survey 43)". Not applied as a number; three counts disagree by one each way.
- B: "defects → large-field sites. Plausible, I". Kept at I; only the equivalent was changed.

### Verification status

**Checked against the text by a reader other than the survey's author.**
- Every row of section 1 in the survey was confirmed by B as to meaning, basis and lines, apart from the rows changed above (B's "Confirmed rows", sections 1, ch. 1–2, 7, 8, 9 and 9s). B read all seven files in full.
- Section 2.1: all rows opened by B, except the counts "22 lines in ch. 7, 27 in ch. 9". Section 2.3: all rows confirmed by B, with the changes above.
- Section 3: B recounted `actual`, `row`, `selected`, `test`, `label`, `tag`, `mark`, `window`, `history`, `source`, `response`, `transport`, `cost`, `gain`, `loss`, `sector`, `frame`, `anchor`, `phase` and checked the assignments; totals of `weight`, `common`, `scalar`, `auxiliary`, `logarithmic` by script.
- R opened 31 of B's assertions about these chapters and found all correct apart from the `thermal` contradiction; R separately confirmed, for these chapters, the `actual` total (53), the `row`, `selected`, `test`, `label`, `tag`, `window`, `history`, `stage` lines, the chapter 7 `response` and `insertion` lines, and the rows on inherited loop action, subpower, matching, parent, centered log determinant, `c_lin`, the relaxed condition, derivative reserve, `kill`, `bond`, the constant `b`.
- For this fold, every correction listed above as "verified" was opened in the chapter files at `eb97dec6`, and the totals for `actual`, `label`, `sector`, `stage`, `transport` were recounted by script.

**Checked by one second reader only (B), not reopened for this fold.** The unchanged rows of sections 1 and 2; the `selected`, `tag`, `window`, `source`, `cost` line lists; the lines 7:313, 371, 879, 935, 1025 of the gauge-completion row; 7:362–363; 7:994–998 and 7:1159–1167; 9:503; the statement that "transfer matrix" and "health" occur in no other chapter file.

**Resting on one reading only.**
- The meanings I supplied for the 20 added rows of section 1. B listed these terms with their lines but gave meanings for few of them; the meanings and proposed equivalents are from my reading of the cited lines and have had no second reader. This applies in particular to the inferred ones: placements (7:753), raw, integral shear, exchange symmetry, principal real cube, interpolated link fields, one-step integral identity, local-integral estimate, pass the cutoff, plaquette filling bounds.
- The identification of the "recording estimate" with "The Fourier mesh estimate" of 7:762, and the two added cluster rows of section 5.
- The per-line assignment of `actual` to senses (i) and (ii) beyond the lines named above; the per-sense splits of `weight`, `common`, `scalar`, `logarithmic` (survey only; B read but did not tally them).
- Section 5 (synonym clusters): B read the lines during the full read but did not reopen them one by one; "event indicator (11 matches in ch. 9)" by count only. Whether the words of each cluster denote one object was not verified, except where a row says so.
- Section 6 (overloaded symbols): B spot-checked about a dozen entries, all correct; the rest rests on the survey alone.
- All proposed equivalents: judged from general knowledge by the survey, B and this fold; none checked against the literature. No Lean source was consulted. The figure files were not read.

---

<a id="part-iv"></a>

## Part IV. Chapters 10–11

Files (worktree `manuscript/HumanizeYM_v3/chapters/`), all read in full:
`10` = `10-common-trajectory.tex` (935 lines); `11` = `11-marked-insertions.tex` (2355); `11R` = `11-restarted-history.tex` (393); `11E` = `11-equation-calibration.tex` (185).
Also read: Part II (all), `blueprint/notation.md` from line 146 to the end. Counts are from `grep -oiE` after stripping `\label{}`, `\ref{}`, `\eqref{}`; they are given per file in the order 10 / 11 / 11R / 11E.
Basis codes: D defined, R read off an explicit sentence, I inferred, ? undetermined. Categories: (a) accounting, (b) program leakage, (c) ordinary/standard word in unusual sense, (d) coined, (e) other.
Line numbers are those of the chapter files at commit `eb97dec6`; the survey was first written against `7bec3925`, and the later repairs of damaged sentences kept the line numbers. Cross-references to chapters 4, 5, 7, 8, 9 and 13 use the chapter number (`13sb` = `13-sharp-bounds.tex`).

General observation. These chapters have already been through a translation pass (no "price", "pay", "budget", "receipt", "readout", "table", "probe", "detector" in prose). What remains is (i) a large "reserve / cost / absorb / retain" vocabulary, (ii) scheduling vocabulary (stage, plateau, floor, delay, request, window, entry), (iii) many undefined nouns for objects of the marked expansion (principal, incidence, graph, column, trial, lift, mass, unit), and (iv) a few remaining artefacts of mechanical replacement (section 4; most were repaired in the chapter files).

---

### 1. New terms (not in Part II)

#### 1.1 Scheduling and order of choices

| Term (variants) | Where | Def.? | Meaning and decisive quote | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| stage `j`; stage bound / constant / threshold / requirement; adjacent stage pair | 10:25, 28–30, 45, 50, 55; counts 32/33/7/7 | defined 10:25–31; index `J(m)` 10:129–134 | A regularity level: "A stage `j≥1` specifies finitely many derivative orders, support exponents, path widths and coefficient bounds"; nested; `J(m)=j` for `A_j≤m<A_{j+1}`. Not an RG step (Part II's sense of "stage"). | D | *regularity class `j`* ("regularity level" would collide with "level `m`", the scale index of section 5; keep "stage" only if "step" is used for RG steps everywhere) | c |
| (stage) plateau | 10:123, 139, 189, 193, 195, 199, 206, 749; 11:1965 | used, read off 10:123–140 | Maximal interval of levels `m` with `J(m)=j`: "lies in the `j`th plateau: its lower endpoint is at least `A_j` … less than `A_{j+1}`". | R | *interval of constancy of `J`* | c |
| schedule; numerical / stage schedule | 10:12, 114, 118, 684, 808, 926; 11:1059 | defined by construction 10:121–147 | The functions `J(m)`, `L_m=𝓛_{J(m+1)}`, `τ_m`, `a_m`. Narrower than Part II's "fixed parameter sequence" but compatible. | D | *scale sequence `(J(m),L_m,a_m)`* | c |
| floor; stage / ratio / block floor; additional floor; metric floors | 10:55, 90, 102, 299, 324; 11:1958, 2176; 11R:247; 11E:29, 133 | used | A lower bound imposed on the block ratio `𝓛_j` ("odd integers `𝓛_j≥3` above every stage floor", 10:55; display 10:91–94). 11R:247 "metric floors": lower bounds of the quadratic forms (inferred). In 11E:25–30 the "stage-`j` block floor" is the inequality `L^{1/8}≥max_{d≤j}2(1+C_j)Q_{dj}δ_d^{-1}`; the accompanying coupling condition `β̂_N≥a_{d,J(N)}` is placed among "the adjacent stage conditions on the starting scale" and is not called a floor. | R / I | *lower bound on the block ratio*; *lower bound* | c |
| delay; stage delay; finite delays; uniform delay | 10:107, 111; 11:1192, 1199, 1214, 1267, 1270, 1402, 1764, 1944, 2022, 2085, 2111, 2146 (2/12/0/0) | undefined | Postponing the level at which a stage starts so that a fixed constant is dominated by a slowly growing quantity: "The stage delay can impose `C_k≤H^γ`" (11:1192); cf. 10:157–159 "satisfied by increasing its starting scale". The identification with increasing `b_j` is inferred. The terminal delays of 10:107–112 are of another kind: conditions at the cutoff level `N`, "absorbed by choosing sufficiently large inverse-coupling thresholds" and imposing `β̂_N≥a_{d,J(N)}` (read). | I (R for 10:107–112) | *after increasing the starting scale of the stage* (11:1192–1200); *lower bound on `β̂_N`* (10:107–112); state the inequality imposed | c |
| threshold for the starting scale; choice of sufficiently large starting scale(s); condition(s) on the starting scale; stage entrance; post-length threshold conditions | 10:63, 606, 692; 11:1070, 1397; 11R:79, 219, 336; 11E:30, 106, 113, 148 | undefined; mechanism 10:157–183 | Same thing as the stage "delay": requirement `τ_m≥b_j log 3` (10:181–182). "Post-length" = imposed after the block ratio `L` is fixed (11E:113, cf. Part II "pre-`L`"). | R | one phrase: *lower bound on the starting scale `b_j`* | c |
| mesh threshold | 11:1119, 1129–1131, 1815, 2351 | undefined; read off 11:1123–1131 | A lower bound on the cutoff `N`, not on the starting scale of a stage: "once the mesh is sufficiently fine relative to the fixed physical cell" (11:1123–1125); "one mesh threshold ensures the required nonwrapping and separation for every period" (11:1129–1131). | R | *for `N` large enough (mesh fine relative to the physical cell)* | c |
| request; numerical / finite / degree and derivative requests; requested (order, power, window) | 10:67, 69, 75, 123, 189, 745; 11:356, 1634, 1777, 2057, 2084, 2090, 2208; 11R:217, 241, 296; 11E:13, 30 | read off 10:66–70 | A finite numerical requirement which a later chapter adds to the schedule: "Future applications may prescribe countably many finite numerical requests … At stage `j` take the maximum of the first `j`". | R | *requirement*; *prescribed (order, power)* | b |
| inner barriers `ℓ_m,u_m` | 10:213, 245, 250, 271 | defined 10:213–217 | Two sequences inside the admissible band between which the tuned couplings stay. Standard "barrier" usage; listed only because of "barrier inequalities". | D | keep | — |
| shooting; shooting parameter | 10:273, 818 (and label) | undefined | The bare coupling chosen at level `N` so that `β_{N,p,0}=β̄` (10:243–251). Standard ODE metaphor. | I | *tuning of the bare coupling*; or keep with one sentence | c |
| tuned (history, endpoint) | 10:12, 17, 232, 808 | Thm 10:232 | `β_{N,p,0}=β̄`. | D | keep | — |
| coarse target `β̄`; coarse endpoint | 10:153, 209, 268, 813 | 10:153 | Value of the inverse coupling at level 0. | R | *value of the coupling at unit scale* | c |
| comparison level / depth `k`; top level; opening (level, sites, estimate, bound); middle level `ℓ`; output (level) `w`; leading interval; lower interval; restoration levels; (fixed) deep comparison level | 11:734–737, 1149, 1405–1406, 1551, 1564, 1646, 1753, 1889, 1919, 1949, 1952, 1960, 2032, 2085–2088, 2151, 2200; 11R:70, 218 | never defined together | Three levels `k>ℓ>w` (`m=k−ℓ`, 11:1754; `ℓ−w`, 11:1571): `k` = level at which the restart begins ("top level `k`", 11R:218; "opening"); `ℓ` = "middle"; `w` = "output". "Leading interval" = `k→ℓ` (11:1952), "lower interval" = `ℓ→w` (11:1960). That "opening" = "top" = `k` is inferred from 11:1889 (`C=⌈(log s)^2⌉`, `s=β̂_k`). "Restoration levels" (11:1405): probably the middle levels `ℓ`, where the weight is restored ("the corrected leading coefficients at the middle level … their rooted contribution at the restored weight", 11:1551–1553; "On the lower interval … at the restored weight", 11:1564–1569); 11:1405–1407 contrasts them with "the separated opening sites". A strong inference, not a definition. | I | name the three levels once by symbols `k,ℓ,w` and use only the symbols | d |
| comparison window (finite windows; window of at most `(log log s)^4` steps) | 11:1462, 1675, 1795, 1965, 2091–2092; 11R:215–222, 298 | Prop. 11R:215–219 | Interval of levels below `k` on which the restarted history lives. | R | *interval of levels `[w,k]`* | c |
| stopping pair `(m,k)`; stopping representation; stopping scale; "stopped at `a_k`" | 10:172; 11:781, 816, 945; 11E:65 | read off 11:815–816 | `m` = scale of the reflected tiling, `k` = level at which the block evolution is stopped and the representation used: "A reflected tiling at scale `a_m`, stopped at `a_k`, has `(a_m/a_k)^4` sites per cell". The "sparse stopping scale" of 10:172 is the level `k(m)` chosen in 13sb:104–109 (section 1.2, last row). | R | *pair (cell scale `m`, evaluation level `k`)* | c |
| restart; restarted history / representation / threshold / small-field indicator | 11:26, 734–765, 1155, 1220, 1309, 1663, 1967, 2058, 2090, 2198; 11R:2, 7, 18, 215 | history described 11:736–741; representations constructed 11R:2–242 | Two objects. The restarted *history* is the auxiliary sequence `D_i=𝓑_{i,β}D_{i+1}`, `D_k=ρ_{N,p,k}`, with the actual inverse coupling frozen at `β=β_{N,p,k}` below `k`. The restarted *representation* is the local representation of the densities along that history ("Constructing the restarted representations", 11R:2), with new radius and threshold: "The new representation at level `i` has radius `B_i=b(x_i)^2`" and threshold `ϑ(x_i)` (11R:18). | D | *auxiliary constant-coupling sequence* and *its local representation*; keep "restarted" if defined at first use | d |
| recording scale / parameter `r(x)` | 11R:25, 33, 44, 248, 263 | defined 11R:26–28 | The solution of `r^{-1/2}H(r)=ϑ(x)`; "a recording parameter for the local calculation, not the actual inverse coupling". | D | *auxiliary reference parameter `r(x)`* | b |
| re-expression of the endpoint; endpoint re-expression | 11R:68; 11:1930 | Prop. 11R:68–81 | Rewriting the density at level `k` with radius `b(x_k)^2` and threshold `ϑ(x_k)`. | D | *change of representation at level `k`* | c |

#### 1.2 Histories and the comparison argument of chapter 10

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| history (ch. 11 sense) | 11:18–19 | defined | "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations." New sense relative to Part II (section 3 below). | D | *RG trajectory (with its choices)* | c |
| finite history; tuned finite history; coupled histories; auxiliary / zero-terminal-array / zero-array history; history with prescribed inverse couplings | 10:13, 232–256, 447, 781–799, 805, 826, 918 | Thm 10:232 (not a formal definition) | For fixed `(N,p)`: the sequence of densities `ρ_{N,p,m}`, `0≤m≤N`, with couplings and activity arrays, from the Wilson density down. "Zero-array": started from activity array zero at a level `k` with couplings prescribed (10:824–826). | R | *finite RG trajectory*; *trajectory started from zero activities* | c |
| dictionary; common (coefficient) dictionary; support dictionary; fixed dictionaries | 10:316, 376, 379, 382, 393, 727, 905; 11:472 | undefined | No sentence says what a dictionary is; from use, the index set on which coefficient or activity families are defined, common to all cutoffs: "coefficients `c_N(γ)` on a common dictionary" (10:375–376). | R / I | *index set* (*of paths*, *of supports*) | b |
| Hilbert encoding; encoding weights | 10:381–382 | undefined | Not determined; some `ℓ²`-type parametrisation of path coefficients. | ? | ask author | b |
| pad absent labels by zero | 10:394–395 | — | Extend a family by zero to the common index set. | R | *extended by zero* | b |
| prescribed-site rules; cutoff-failure catalogue; clipping rule / clipping data | 10:393, 727, 921 | undefined | The fixed combinatorial data of a level (which large-field sites an activity must cover; list of cutoff events; `clip` parameters). "Prescribed-site" is the notation.md translation of "forced/inventory". | I | *the fixed data: prescribed large-field sets, list of cutoff events, clip parameters* | b |
| finite parameter evaluation(s); finite-evaluation bound / inequalities; moment norm `M_q` of an evaluation | 10:457, 462, 486, 498, 609, 630–652, 668, 799 | read off 10:464–471 | A finite linear combination `Σ a_i F(z+t_i v)`; its "moment norm at radius `q`" is `sup_n\|Σ a_i (t_i/q)^n\|` (inferred from 10:468, 630–635). (Labels `finite-tests`, `broad-test`.) | R / I | *finite linear combinations of values along a real line*; *sup norm of the moment sequence* `(Σ a_i(t_i/q)^n)_n`, an element of `c_0` (10:476–477); equivalently the norm of `f↦Σ a_if(t_i)` on power series normed by `Σ\|f_n\|q^n` | d |
| narrow band; reserved band; inverse coupling reserve | 10:405, 430, 491–492, 529, 676 | 10:406, 492 | `17/20≤χ_mλ≤23/20`; enlarged to `33/40…47/40`. | D | keep, with the inequalities | — |
| compensation | 10:529–531, cf. 678 | read off | "the Gaussian coordinate is rescaled by `ℓ(t)` while its fluctuation coefficient is divided by `ℓ(t)`", so the fine field is unchanged. Clarifies Part II 4.2 "compensating map". | R | *compensating rescaling of the Gaussian variable* | c |
| held fine reads; fine (field) read(s); local read set; read coordinates | 10:508, 530, 587, 678, 721, 741, 765; 11:696, 700, 718, 720 | undefined | Noun use of Part II's "reads": the fine variables on which a factor depends, kept fixed under a change of variables. | I | *the fine variables on which the factor depends* | b |
| real nodes; node sign | 10:553–561, 573, 631, 675 | — | Interpolation nodes; standard. | — | keep | — |
| hard bound `a_h` / hard factor; soft correction `a_s` | 10:656–667 | undefined; an instance of the proposition "Exact regrouping" (`ch09:fusion-prop`, 9:651–666) | Hard = the bound on the preliminary large-field activities (hypothesis `\|k_i\|≤e^{-κ}v_i` of 9:656; here `a_h≤Ce^{-cP(y)^2}`). Soft = the bound on the logarithmic correction factors `e^{ℓ_a}−1` (hypothesis `\|e^{ℓ_a}−1\|≤v_a`; here `a_s≤y^{-1/8}`). The soft terms are not small-field terms: "`ℓ_a=0` when `Z_a` is small-field" (9:634–635). The conclusion `𝒦_m(K)≤e^{-κ}(e^γ−1)` matches `e^{-ζ}(e^I−1)≤φ` (10:664). | R / I (by matching 10:656–666 with 9:651–666) | *preliminary large-field activity*; *logarithmic correction factor `e^{ℓ_a}−1`* | c |
| fusion; connected fusion estimate | 10:655, 666, 774, 914 | not defined: in ch. 9 the word occurs only in labels (`ch09:fusion`, `ch09:before-fusion`, `ch09:fusion-prop`; section at 9:631 ff., proposition "Exact regrouping" 9:651) | The regrouping of preliminary large-field terms with logarithmic corrections into connected components. | I (identified through label names) | *regrouping into connected components* | d |
| reset | 10:651 | ch. 9 (labels `ch09:path-reset`, `ch09:reset`, 09:539–748) | The fixing of the output inverse coupling together with the scalar after a step: "The output inverse coupling and scalar are now fixed: `β=β'+α+Δ`" (9:716–719, eq. `ch09:reset`). Not explained in ch. 10. | I | *definition of the output coupling (and scalar)* | b |
| low-order collection / projection; finite local / auxiliary projection; projected scalar | 10:509, 606–608, 615, 747, 772–776, 902, 914 | ch. 9 (09:41, 313, 383) | Finite set of low-order local terms extracted from the activities, and the linear map extracting them; "projected scalar" = the resulting number `q_m`. | I | *extraction of the low-order local terms* | c |
| residual scalar inverse coupling correction `q_m`; scalar correction | 10:421–422, 445, 816, 842 | defined 10:416–422 | `q_m=β_m−β_{m+1}−α_{N,m}`; "It is not the vacuum normalization". It corresponds to `Δ` of `(ch09:reset)` (`β=β'+α+Δ`, 9:719; bound `\|Δ\|≤C_jH_pre/t_m^2`, 9:733, against `f_m=Cεx^{-11/10}/t(x)^2`, 10:648); this identification is by the form of the bound. | D (I for the identification with `Δ`) | *coupling correction `q_m`* | c |
| path coefficient `α_{N,m}`; path correction | 10:422–423, 441, 855 | ch. 9 | Explicit part of the coupling increment. Chapter 10 says only "the one already used in the exact step" (10:422–423); chapter 9 gives the meaning: "The coefficient `α` is the matched determinant coefficient, not an adjustable trial inverse coupling" (9:409–411), `α=−κ_G log L+O_j(1)` (9:739). | R (by ch. 9) | *explicit coupling increment* | c |
| response bound `ε` | 10:626 | undefined | A fixed small constant in the one-step remainder estimate of ch. 9. Why "response" is not determined here. | ? | *the constant `ε` of (ch. 9 ref.)* | c |
| block bridge | 10:921 | undefined | Probably the smooth tangent transport `W_a` of chapter 5: the label `ch05:actual-bridge` (5:1132) names the bound "asserted for `W_a`" (5:1152), and 7:597–598 has "External smooth bridge legs have the same powers in supremum norm, by (ch05:actual-bridge)". At 10:921 it is something that must be "the same" in the auxiliary histories, with clipping data and stationary graph. | I (label name) | name the object (`W_a`?); ask | d |
| stationary branch | 10:920 | undefined | Presumably the chosen stationary solution (Part II "branch" = case). | I | *stationary solution* | c |
| moving expression / moving threshold surface | 10:730–734 | — | Changing with the parameter that is varied: an indicator "would move with the mean or precision" (10:730). In ch. 11 (11:1083, 2218) "moving" means depending on the cutoff `(N,p)`. | R | *parameter-dependent* (10:730–734); *cutoff-dependent* (ch. 11) | c |
| replication costs; sparse stopping scale; Haar-ball normalization argument | 10:169–172 | undefined here; settled in ch. 11 and 13 | Forward references to the chessboard argument: "The Haar-ball argument of Section `ch11:replicated`" (13sb:36–37), which restricts all links to a Haar ball at a cost per site; the replication cost is the factor `e^{(a_m/a_k)^4q_k}` of 11:819. The stopping scale is `k=k(m)`, "the first level `k≥m` with `B_k^2≤a_m/a_k`", for which `(a_m/a_k)^4q_k^{site}≤(L_{k-1}B_{k-1}^2)^4q_k^{site}=o(τ_k)` (13sb:104–109); this is the condition imposed at 10:167. The word "sparse" is not explained. | R ("sparse": ?) | cite the later estimates | a |

#### 1.3 The source algebra and the marked expansion (ch. 11)

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| squarefree source algebra `𝒜_𝓘`; source variables `z_i`; source monomial `z_S`; source variable set | 11:23, 33–49, 1324, 1384, 1487, 1493, 1584, 2095 | defined 11:33–40 | `ℂ[z_i]/(z_i^2)`; generating variables for insertions. | D | *exterior-free truncated polynomial algebra* is not standard either; keep, it is defined | — |
| source weight `ω_i`; residual source weight; weight restoration; restored weight | 11:43–49, 192–196, 496, 938, 953, 1374–1388, 1436, 1471, 1552, 2130 | 11:43–47; restoration read off 11:1380–1388, 1436–1442 | Weights in the norm `‖a‖_ω=Σ\|a_S\|∏ω_i`. "Restoration": passing from the bound at `(ω_−,e+2)` to one at the larger weight `ω=H^{U}ω_−` and smaller exponent `e`. | D / R | *weights `ω_i`*; *change of weight from `ω_−` to `ω`* | c |
| insertion label | 11:33, 132, 178, 185, 193 (13 lines) | 11:33 | Element of the index set `𝓘`. | D | *insertion index* | c |
| mark; marked point / site / ancestor; marked factor / term / component / activity; marked density / expansion / step / polynomial; unmarked | see section 3 | never defined; read off 11:70–75 | Unmarked = coefficient of `z_∅`: "let `ρ_N≥0` be the unmarked density" (11:70), `q_N=ρ_N∏(1+z_iF_i)` (11:75). Marked = carrying a source monomial `z_S`, `S≠∅`. A mark = an insertion (its point or index). notation.md: mark = observable insertion. Three uses, section 3. | R | *insertion (point)*; *term carrying insertions*; *density with insertions* | c |
| push; pushed (polynomial, density); exact push | 11:95, 97, 773, 1671, 1950 | read off 11:76, 95 | Apply the block maps coefficientwise: `q_m=𝓑_m q_{m+1}`. | R | *image under the block maps* | c |
| unit; unit insertion; unit coordinate; exact unit rule; "the circle deletes the unit coordinate" | 11:87–90, 389, 451, 1050 | R | The constant field `e_0` (identity insertion) and its coefficient. | R | *identity insertion `e_0`* | c |
| principal (term, factor, component); purely principal; nonprincipal; nonleading; leading | 11:179, 279, 288–289, 297, 314, 319, 321, 329, 339, 425, 608, 728, 1043, 1410–1413, 1606, 1614, 1625–1632, 1646 (principal 17; nonleading/nonprincipal 7; leading 12) | never defined | Principal = the main part of a single-insertion factor on the small-field event, to be evaluated by the joint Gaussian comparison: "Purely principal connected components have the one-cell support bound proved earlier. Their actual integral is the joint moment … since it contains neither an unmarked correction nor an incoming large-field factor" (11:329–332); the split `(1+γWz_S)(1+(1−γ)Wz_S)` (11:314–319) calls the second factor "nonleading". "Nonleading" and "nonprincipal" appear to be synonyms (11:279 vs 288). 11:1737 "principal alias" is the ch. 5 sense. | I | keep *principal* / *nonprincipal*, defined once ("leading" is already used for other things: section 3) | c |
| inflation factors `m,l`; inflated; uninflated | 11:274–278, 294, 337, 522, 1593–1603; 11R:313, 319–322, 333, 371, 383; 10:602 | read off 11:274–277 | Factors `≥1` by which the amplitude bounds are multiplied before the local integral bound is applied. | R | *enlargement factors `m,l` of the bounds* | a |
| incidence (bound, sum); marked-point incidence; insertion incidence; source variable incidence | 11:208, 258, 265, 302, 322, 340–342, 506–507, 783, 1398, 1577, 1606, 1614, 1649, 2135 (17) | never defined | Sum of the weighted bounds of all terms whose label set contains a given mark ("the insertion incidence sum at a fixed mark", 11:258); contrasted with the "site bound" (sum over terms containing a site), with conversion 11:266–272. | I | *sum over terms containing a given insertion* | d |
| site bound / site sum; root-to-site conversion; site conversion | 11:257, 266, 300, 1473, 1918; 11R:74, 125, 141–142, 170–181 | Part II "containing-site bound" | Same as Part II. "turn an anchored bound into a site bound" (11R:141). | — | as Part II | — |
| occupancy `g` | 11:345; 10:109 (the symbol `g` is introduced at 11:260, without the word) | 11:260 (symbol) | "at most `g` marks project to a coarse site". | R | *maximal number of insertions per coarse site* | c |
| menu (of stencil radii and degrees); degree menu | 11:161, 516 | — | Finite list. | R | *finite list* | e |
| complementary part / stencil / insertion factor / attachment / cutoff | 11:139, 147–151, 922, 941, 1613, 1636; 11E:81, 101, 119; 10:99 | use at 11:147–151; explicit only at 11:1490–1494 | The part of an insertion multiplied by one minus the small-field indicator. That formula is not in 11:147–151; it is explicit at 11:1490–1494 ("Expand it as a product of factors `1−(1−χ)Rz_I`"). | R / I | *large-field part of the insertion* | c |
| join; attach; attachment(s); attachment reserve `u_N`; attachment margin | 11:148–149, 169, 215, 252, 502, 510, 922, 937; 11E:57, 81, 93–104; 10:760, 775 | R | Merging an insertion's large-field part with the large-field supports it meets into one component. | R | *merging into the large-field component* | c |
| (linear) graph `G`; coefficient graph; graph norm; graph estimates; inhomogeneous graph estimate; graph of normalized local insertions | 11:347, 379, 447, 454, 468, 886, 892, 899, 911 | 11:379–380 (notation only) | A linear map from the coefficient vector `x∈V_d` to families of regular and large-field remainders ("an incoming linear graph of regular vanishing-jet and large-field remainders, with norm at most `s_f` per coefficient"); one step maps `G` to `G'=R_G M_G^{-1}` (11:447). The word is used as in "graph transform". | R | *remainder map `G`* (linear in the coefficient); *graph transform* is standard for `G↦G'` | c |
| raw (remainder map, error, inequalities, polynomial, stencil, transport, labels, coefficient, triangular construction) | 3/11/0/1; e.g. 11:382, 466, 651, 894, 900, 958, 1013, 1208; 10:103, 609, 656 | — | "Before normalisation / correction"; meaning varies by noun. | I | delete or say *unnormalised*, *uncorrected* | b |
| rebasing contraction | 11:467 | undefined | Presumably the contraction for `G↦R_GM_G^{-1}` (11:454–465). | I | *contraction of the map `G↦G'`* | d |
| preselection bound | 11:382 | undefined | `C_d/L+o_x(1)`; "preselection" not explained. | ? | *the bound `C_d/L+o(1)`* | d |
| column; stage column bound / constant; inverse(-front)-column bound; free comparison columns; target columns | 10:83; 11:446, 1057, 1103, 1144, 1200, 1237, 1304, 1340, 1343, 2033; 11E:19 | undefined | Column = image of a basis vector of `V_d` under a coefficient map; "column bound" = `ℓ¹` operator-norm bound of the map or its inverse ("`\|x\|≤s_f\|M_Gx\|` after fixing a suitable stage column constant", 11:445). "Front-column" (11:1343) not determined. | I / ? | *operator-norm bound `C_j`*; *image of a basis vector* | b |
| vanishing-jet remainder | 11:379 | cf. 11:1181 | Regular remainder whose extracted polynomial is zero ("all regular remainders have zero extracted polynomial"). | I | *remainder with zero local part* | d |
| screened; screening | 11:400, 413 | undefined | Restricting a polynomial direction to the links on which the function depends. | I | *restricted to the relevant links* | c |
| mass (of a large-field input); normalized mass; reserved mass | 11:423–429; 11E:104–105, 117 | undefined | The support-weighted norm of a large-field contribution, `m`, and `m/κ_f`. | I | *weighted norm* | c |
| selected slot | 11:424 | undefined | Not determined. | ? | ask | b |
| common Gaussian; common sample; coarse forecast | 11:537, 725–726, 1043, 1878 | "forecast" undefined | One Gaussian array used for all subsets. "Coarse forecast": presumably the conditional mean given the coarse field. | I | *one Gaussian family*; *conditional mean* | c |
| corrected source `Jq_N`; corrected coefficients `R_I`; corrected pair bound | 11:769–771, 2066–2070, 1836 | defined | Product with `exp(−C^ref)` / recursion 11:2068–2070. | D | keep *corrected* (defined). `R_I` is the coefficient of the source polynomial multiplied by the inverse of `Σ_IG_Iz_I` (11:2096–2098; "Equivalently subtract its finite connected logarithm", 11:2099); it is not the truncated (connected) coefficient, so no standard name is proposed | — |
| near part / near sum `F_u^near`; distant part; `f^{near,mask}` | 11:1161–1169, 1229, 1310–1321 | defined 11:1161–1168, 1310–1311 | Split of the regular series at connected cover number `M`; "mask" = with the original event indicators restored. | D | keep; rename superscript "mask" | b |
| common localization / extraction; localization onto the polynomial label space `T`; coefficient extraction; low-weight coefficient extraction | 11:29, 372, 438, 1141, 1180–1182, 1203, 1288, 1292–1293, 1307, 1326, 1330, 2057 | (i) 11:372–377; (ii) constructed 11:1285–1305 | Two different maps, both written `T`. (i) The one-step localization: "Localization by Taylor expansion of the fine local section on the free interpolated coarse jet gives a triangular change of basis `T`" (11:372–374); "the leading map is `TS_L`" (11:377). (ii) The common localization map at the comparison level (also `T_{k,N,p,d}`): "Define `Tu` to be precisely these frame coefficients" (11:1292–1293). The "localization by radial Taylor expansion" of the near sum (11:1180, 1203) is a third object (the `Au` compared with `Tu`; this last identification rests on one reader). "Localization" and "extraction" are used for the same operations. | D | *one-step localization* and *common localization map*, with different symbols | — |
| exposure `𝓔`; fixed radial polynomial frame | 11:1285–1293 | undefined | A linear map `𝓔` from labels to coefficient arrays in a fixed polynomial basis ("frame"), bounded below: `‖v‖_1≤c_d‖𝓔v‖_coeff` (11:1285–1287); `Tu` is then defined as "precisely these frame coefficients" (11:1292–1293). The object is constrained in this way; the word is unexplained and no formula for `𝓔` is given. | I | define `𝓔` by a formula | d |
| (simultaneous, normalized) lift; lift equations; lifted vectors | 11:1306, 1326, 1341, 1351–1354, 1839–1842, 2059–2063, 2159–2162, 2197, 2208, 2215 | eq. 11:1352 | Solution `u` of `S_{g/θ}Tu=W_ρ v`. A fourth sense of "lift" (Part II 4.2 has three); 11:400, 414 "centered nonwrapping lift" is the covering-lattice sense. | D | *preimage `u` of `W_ρv`* | c |
| magnification `ρ=H^b`; measurement magnification; geometric magnification; amplification | 11:1365–1366, 1806, 2054, 1963 | 11:1350, 1806 | Dilation factor in `W_ρ`; "amplification" = growth factor of a bound. | R | *dilation factor* | c |
| measurement (matrix, cell); averaged measurements; tested correlation; correlation pairing | 11:983, 1806, 1920, 2177, 2233–2235, 2248, 2255, 2276, 2288, 2314, 2320 | undefined | Value of the finite family of correlation functionals `L_i` on a coefficient; `G` its free counterpart. | I | *value of the functional `L_i`*; *matrix of correlations* | c |
| trial; local / terminal / fixed-stencil / difference / protected trial; bounded coarse polynomial trials; trial descent; trial encoding | 10:95; 11:27, 890–957, 1074, 2235, 2276, 2294, 2306–2311, 2329, 2349; 11E:94, 148 | undefined | A local observable `F` (e.g. `f=a_N^eF`, 11:919) to be approximated by a normalized local insertion `O_{N,p}(e,v)` (11:949). The "trial encoding" (11:1074) is the reference label `v_{N,p}` of 11:945–951, for which `𝓡_m{F−O_{N,p}(e,v_{N,p})}` is small. | I (R for "trial encoding") | *local observable (to be approximated)* | d |
| backward comparison; descent; bulk descent bound | 11:27, 890, 945; 11E:121, 125 | — | The propagation of the terminal trial down the block steps, which gives the decay `c_i+\|x_i\|≤4(1+C_N)we^{-(τ_N−τ_i)/8}` (11:913–915). It is not a downward induction: the induction on the cone condition "starts at the bottom with zero coefficient" (11:909) and runs upward (`A_{i+1}\|x_{i+1}\|≤c_{i+1}`, 11:908). | R | *propagation of the terminal trial down the block steps* | c |
| cone inequality | 11E:125 | undefined; read off | The step "If `A_i\|x_i\|≤c_i`, substitution gives `y_i≤4K_ie_ic_{i+1}`" (11:905–906), used at 11E:125–128 in the form `\|e_j−u_j\|≤4K_{N-1}L_{N-1}^{-3/8}c_N`, with `e_i=s_i^{-3}=L_i^{-3/8}` (11:893). | R | cite the inequality | d |
| terminal map `𝖹_{N,p,d}`; inverse terminal coordinates; reference level / label / coefficient; reference coordinates | 11:883–885, 946–947, 958, 1047–1049, 1075, 1136; 11E:9, 154, 184 | defined 11:1047–1049 | Composition of the single-insertion coefficient maps from `N` to the reference level; "inverse terminal coordinates" = `𝖹^{-1}c`. | D | *coefficient map from the cutoff scale to the reference scale* | c |
| calibration; calibrated; local calibration | 11:1034, 1061, 1159; 11R:6; 11E:2 | undefined | Normalisation of coefficients through `𝖹` and comparison of sections; no single definition. | I | *normalisation*; *comparison of the two sections* | c |
| admissible (comparison coefficient / family) | 11:884–886, 1101–1105, 2253, 2311–2324 | defined twice (11:884; 11:1101) | `‖X_i^{-1}z_i‖_1` subpower in `a_N^{-1}`, uniformly in `p`. | D | keep | — |
| equation subspace / space / kernel / labels / component; moving, varying, actual equation space; moving complement | 11:966, 989, 1083, 1093, 1107, 2218, 2224; 11E:43–46, 154–159 | 11E:155–159 | `𝖤_{N,p,d}=𝖹PS_{t_N}R_d𝓘_d`; "moving" = depending on `(N,p)`. | D | *cutoff-dependent subspace of field equations* | c |
| positional modulus | 11:827, 1025–1027, 2242 | read off 11:861–866 | Lipschitz bound of a correlation in the position of one insertion. | R | *modulus of continuity in the insertion point* | d |
| transfer word; slab kernel; tour length; gaps | 11:842–863 | 11:842–845 | `tr∏B_iT^{H_i}`; total length `M`; exponents `H_i`. | R | *cyclic product of transfer operators*; *total length*; *separations* | c |
| finite difference word `l` | 11:2227, 2251, 2278, 2297, 2304 | undefined | Finite sequence of coordinate directions; `D_l` the iterated difference. | I | *multi-index `l`* | c |
| plant; planting | 11:2332, 2349 | read off 11:2332–2343 | Placing the points of a tuple in distinct interior cells of a tiling. | R | *placing in distinct cells* | e |
| spans `t,T`; margin `3t` | 11:2336–2339, 2351 | 11:2337 | Cell sides in lattice units. | R | *cell sides* | c |
| chessboard seminorm `𝓡_m`, `‖·‖_root`; root bound | 11:822, 2027, 2075, 2140 | named 11:815–822 | The number-of-cells root of the normalised product moment on a reflected tiling. Standard name now used; the subscript "root" is a leftover. | R | keep; rename subscript ("chessboard estimate" is the established name; whether "chessboard seminorm" is established usage was not checked) | — |
| reflected replica cell; reflection cell; measurement cell; comparison cell; copies | 11:178, 194, 345, 781, 835–846, 1122–1126, 1468, 1920, 2073 | undefined | Cells of the reflected tiling. At 11:781 ("the stopping representation on `V` sites has `n` copies") `n` is the number of reflected cells: the bound `e^{Vq+n(x+y+2)}` (11:809) becomes `e^{(a_m/a_k)^4q_k+x+y+2}` on "Taking the number-of-cells root" (11:817–819), which requires `V=n(a_m/a_k)^4`. | I | *cell of the tiling* (one word) | c |
| (weighted output, scalar) envelope | 11:1972, 2136 (label 1580) | display 11:1580–1582 (the word is not there) | The bound `exp{unmarked exponent+q_0(1+n)}`. | R | *majorant* | c |
| expense | 11:2137–2138 | — | Additive constant per site in an exponent. | R | *contributes at most `1+n` per site* | a |

#### 1.4 Restarted history (11R)

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| presentation; exact / genuine / coarse presentation `P_i` | 11R:71, 196, 222, 251, 339 | — | A representation of a density by path action, clip, regular and large-field activities; synonym of "local representation" (11:19, 122) and Part II's "density coordinates". | I | *representation* (one word) | c |
| genuine (density, presentation, multipliers, value cost) vs neutral (reference, version, estimates, Gaussian integral) | 11R:195–213, 254–259, 282, 310, 319, 334; 11:613 | defined 11R:196–198 | `R=e^{-E}R^0`; neutral `R^0` = "obtained by deleting only the regular additive family `E`". | D | *full density* / *density without the regular terms* | d |
| local multipliers / additive multipliers `h_α=e^{-E_α}−1` | 11R:205, 259, 310, 319, 330 | defined 11R:205 | | D | *factors `h_α`* | c |
| local energy contributions `d_z`, `b'_z`; selected site factor `X_z`; mandatory factor | 11R:96–116, 159–162, 170 | defined | `X_z=exp[−β(d_z+b'_z)]`. | D | keep | — |
| half-square | 11R:103–111 | R | Half the square of a truncated path component. Clarifies Part II 4.2. | R | *`½\|·\|²`* | c |
| new-small-field | 11R:107, 124, 149 | — | Small-field for the new threshold `ϑ`. | R | *small-field at threshold `ϑ`* | d |
| coalesce | 11R:147, 184 | — | Sum the terms with equal support. | R | *collect by support* | c |
| optional factors / optional subset | 11R:155, 165 | — | Factors `W_Y` that may or may not be chosen when `∏(1+W_Y)` is expanded. | R | keep | — |
| value cost `q_n`; additive value cost / error | 11R:225–227, 254, 352; 11:2014 | R | Bound for the sup of the regular additive terms per site. | R | *sup-norm bound per site* | a |
| unselected local exponent / components | 11R:264, 313 | — | Not carrying a failed cutoff condition (inferred as complement of "selected", section 3). | I | *small-field (local term)* | c |
| determinant-word series | 11R:270 | ch. 6 (Part II `word` (iii)) | Neumann-series terms. | — | as Part II | — |
| finite decorations | 11R:304 | undefined | Not determined. | ? | ask | d |
| sliced-integrand level; slices; tag-count factor; tag average | 11R:358–360 | undefined | Integrand at a fixed value of the random index `α`; number of values; average over `α`. | I | *for fixed `α`*; *number of values of `α`* | b |
| regular logarithms with holes; raised hole correction | 11R:365–369 | undefined (refers to `ch08:reassembly`) | Probable reading: in `Z_D=e^{𝓛(z)}Σ_B(∏K_η)e^{−𝓛_{Y(B)}(z)}` (8:311–315) the "hole" is the deleted set `Y(B)` and the "raised hole correction" is `e^{−𝓛_Y}−1`, consistent with "using `\|e^{-c}−1\|≤e^{\|c\|}\|c\|`" (11R:369). "Hole" does not occur in ch. 8. | I | *correction `e^{−𝓛_Y}−1` for the deleted set `Y`* | d |
| installed (entry; transport; response); lower / higher entry | 11R:384–385; 11:648, 1729 | — | "Fixed as part of the family"; "entry" = member `P_i` of the family. | I | *constructed*; *member* | b |
| deletion-of-support identities | 11R:239 | ch. 8 (probably) | Probably `(ch08:deletion-identity)`: "delete all labels whose supports meet `Y`", `Z_pol(z^Y)/Z_pol(z)=e^{−𝓛_Y(z)}` (8:208–215). Inferred from the name and from the reference to chapter 8 at 11R:367. | I | cite the identity | b |
| same-data restart conditions; corrected body product estimate | 11:1666; 11:1662 | undefined | Not determined. | ? | ask | b |
| frozen (inverse coupling) | 11R:246 | — | Held constant. Different from Part II "frozen links". | R | *held constant* | c |

#### 1.5 Accounting vocabulary (print the inequality instead)

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
| subpower | 2 / 11 / 1 / 4 | 10:172, 178; 11:886, 943, 1102; 11E:73 | Same as Part II (`x^{o(1)}`), here in `a_N^{-1}` or in `x`. Defined in ch. 6:822. | — |
| unit(s) of support exponent; cover units | see section 3 "unit" | 11:396, 495, 502, 528, 533, 939, 1446 | One unit in the exponent multiplying `c_B(X)`. | a |
| fit(s) (inside a margin) | not counted | 11R:305–306, 330–332 | "Is at most": "its site bound fits `ω_n=q_nA_s`. The other components fit `δ_n−ω_n`"; "fit inside the remaining margin". | a |

#### 1.6 Further terms

| Term | Where | Def.? | Meaning | Basis | Proposed | Cat. |
|---|---|---|---|---|---|---|
| prescribed set of large-field sites; prescribed large-field set; activities / arrays constrained to cover prescribed (large-field) sites | 10:654; 11:153, 247–250, 296, 365, 941, 1595, 1636–1637, 2133; 11R:300–302, 366 (about 20 uses) | defined in ch. 8 (8:286–288) and ch. 4 (4:440–441) | The nonempty set `I_η⊂D∩Y_η` attached to a large-field activity: "The set `I_η` records the large-field sites assigned to that activity"; the allowed families satisfy the exact cover `⋃I_η=D` (8:289–292). In ch. 4: "a nonempty prescribed set `I_i^bad⊂Y_i`". | D (ch. 8) | keep, used as a noun with its symbol (`I_η`) | d |
| normalized local insertion | 11:353, 355, 438, 455, 895, 899, 911, 1842, 2191, 2210, 2234, 2242, 2247, 2323 (14 uses) | not defined under this name | notation.md (line 158) gives it as the replacement of "primary source": "Normalized local insertion, with its local polynomial coefficient when expressed in the chosen basis". Presumably `O_{N,p}(d,c)` of 11:1051–1054, which the text there calls "the physical insertion"; cf. `O_{N,p}(e,v_{N,p})` at 11:949. | I | define at 11:1051 under one name | d |
| ordinary (chart bound, remainder, norm bound, contribution) | 10:97; 11:940, 1589; 11E:83, 93, 111, 118 | undefined | "Small-field / regular", as opposed to large-field or complementary: "ordinary chart bound" (10:97), "ordinary remainder" (11:940), "ordinary norm bound" (11E:83), "ordinary contribution" (11E:111). At 11:1589 "The ordinary bound by one" is the bound without source weight. The remaining uses are the everyday word (10:16, 536, 718; 11:1173, 1203); 10:327 "ordinary output bounds" is unclear. | I | *regular (small-field)*; *unweighted* | c |
| factor count; curvature-factor count | 11:369, 1135, 1364; 11E:42, 49, 174, 177 | ch. 2 (2:52–53; not opened for this section) | The number of curvature factors of a homogeneous basis vector, i.e. its polynomial degree in the curvature. | R (ch. 2, one reader) | *degree in the curvature* | c |
| block length; length | 11E:20, 31–32; 11:1873 | undefined | The block ratio `L`: "These quantities are fixed before the block length" (11E:20); "then the length, then the inverse coupling threshold" (11E:31–32). At 11:1873 "Choose the block length after `A_{2D}`" may instead mean the number of steps `m` (the preceding sentence bounds a product "over `m` steps"); not determined. | I / ? | *block ratio `L`* | c |
| pre-threshold constants | 11:1396 | undefined | Constants fixed before the inverse-coupling thresholds are chosen; counterpart of "post-length" (1.1). | I | *constants fixed before the thresholds* | b |
| energy; suppression (of a large-field component) | 11:167–168, 521; 11R:63 | undefined | The decay factor of a large-field component and its exponent: "whose suppression is `exp(−cβ_Nt_N^2n)`" (11:167–168); "selected-component energy" (11R:63); "energy reserve" (11:521). | R / I | *decay factor*; *its exponent* | c |
| value (as opposed to derivative) | 10:106, 391, 765; 11:925 | undefined | The part of a norm that bounds the function itself: "weighted derivative and value norm" (10:391), "terminal value norms" (10:106), "value tails" (10:765), "global value" (11:925). Cf. "value cost" (1.4). | I | *sup norm (of the function, not its derivatives)* | c |
| bottom | 10:850; 11:896, 909 | — | The lowest level of the range considered: "common bottom endpoint", "bottom residual coefficient", "The induction starts at the bottom". | R | *lowest level* | c |
| kill | 11:970, 1691 | — | Annihilate: "Each conjugate kills `E_i`"; "killed by `X`". | R | *annihilates* | e |
| returned; reported; declared / declaration; encoded | 10:777–778, 785; 11:1597; 11:441, 534; 11:991 | — | Program-style words. Output of the step: "the actual returned arrays", "the returned inverse coupling". Stated: "the reported bound `G(x)`". Classified or assumed: "never declared large-field", "A declaration that exponents lie in `[98,100]`". Expressed in coordinates: "encoded coefficients of a normalized lattice difference". | I | *output*; *stated*; *classified*; *coefficients of* | b |
| (fixed common) coefficient functionals | 10:373, 813, 889 | undefined here | Not determined in these chapters. | ? | ask | b |
| curl-division and path-placement operations | 10:314 | undefined here | Linear operations fixed for the comparisons; not determined in these chapters. | ? | ask | d |
| exchange term | 10:337 | ch. 7 (not looked up) | A term of the stationary formula `(ch07:uniform-stationary-jets)`; not determined from chapter 10. | ? | cite ch. 7 | c |
| polynomial attenuation; true-length; consume; weaken; discarded-support; tolerance exponent; arity | 11:1657; 11R:102, 133, 274; 11:1740; 11R:275, 279; 11:1201, 1235; 11:1673; 11:343, 2041–2047 | undefined | Smaller unexplained words. In order: a polynomial decay factor; measured by the actual path length ("Truncate each row at true path length `B`"); "consume one box factor" = use one factor; replace a bound by a weaker one; the error `η` from dropped supports; the fixed exponent `q`; the number of insertions. | I | ordinary words | b |

---

### 2. Part II terms in these chapters

#### 2.1 Same sense (confirming references)

| Term | Refs here | Note |
|---|---|---|
| terminal (= finest scale `N`) | 10:102–112, 432, 728, 890; 11:133, 166, 895; 11E:57, 78 | same; plus the derived "terminal map `𝖹`" (1.3) |
| reads / read by | 10:568, 587; 11:680; 11R:104, 106, 161 | same; the noun "a read" is new (1.2) |
| protected (change of variables, chart, neighborhood) | 10:505, 672, 720, 737, 898; 11:472, 1773 | same. New, unexplained use: "protected local representative / trial" for a finite difference, 11:1063, 2306 (?) |
| tag (random index) | 11:244, 679; 11R:358–359 | same; "tag" survives although Part II proposes dropping it |
| sector | 11:244, 293; 10:676 | same |
| forest; forest coordinates / charts; tree gap; block root | 11:617, 628–633, 679; 11R:247; 11:1975 | same |
| full dependence region; exclusion support; exact cover / coverage | 11:134–136, 150, 180, 246–251; 11R:8, 124, 157, 167–168 | same; variants "full region", "full support", "full dependence supports", "full read supports" (11R:167) |
| stencil | 11:135, 148–151, 161, 919–938; 11E:15, 80, 95 | same (set of links an insertion is built from) |
| clean; clearance; remote | 11:679, 709, 721 | same |
| plateau (where a cutoff equals one) | 11:712–713 ("fine plateau", "strict plateau width") | same; a second sense (stage plateau) is new, 1.1 |
| clip; clipped | 10:727, 921; 11:751–760, 1777; 11R:19–23, 43, 72, 85, 198, 250 | same; 11:751 gives "piecewise quadratic/linear clip `d_t`" (symbol `d_t` here, `clip_t` in ch. 4) |
| relaxed small-field condition | 11R:104 | same. **Conflict (probably an artefact of replacement, section 4):** 10:98 says "the relaxed small-field *smooth cutoff* is one", whereas Part II (section 9) established that `χ^rel` is an indicator |
| noise | 11:713; 11R:61 ("cutoff-to-noise ratio") | ch. 6 sense (Gaussian fluctuation, scale `g`) |
| scalar (constant term of the action) | 10:266; 11:609, 726, 789 ("`v_0` is the scalar"), 814, 2014; 11R:73, 190, 362 | same; two further senses in section 3 |
| direct (row coefficient); `c_dir` | 10:356; 11:752 | same |
| inherited (loop, bounds) | 10:36, 338; 11R:272–275 | same (10:761 "multiplicities inherited from the input arrays" is the ordinary word) |
| atoms (path atoms of degree `j`) | 11R:137, 349 | same |
| metric (curvature / two-form / quadratic metric) | 10:33, 328, 356; 11:627, 649, 662, 1681 | same |
| stationary graph; stationary jets | 10:717 (jets), 920–924 (graph); 10:336 has "stationary formula" ("jets" only in the equation label) | same |
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

#### 2.2 New senses of Part II words

| Word | New sense here | Refs | Basis |
|---|---|---|---|
| history | (ii) the whole choice of kernels, couplings, path pairs and representations (11:18, D); (iii) the finite trajectory of densities for a cutoff (10:232–256, R). Part II sense (blocking parameters) survives at 10:373, 933 ("nested quadratic history"), 11:92 ("Changing the block history": only kernels are replaced) and 11:1699 ("kernel history") | see section 3 | D / R |
| stage | regularity level `j`, not an RG step | 10:25–31 | D |
| eligible; eligibility criteria / indicators | Two uses. (i) Condition on a family `𝓕` in the polymer sum ("`Σ_{𝓕 eligible}`", 11:125): the allowed covering families of 8:289–295, finite families of large-field labels with disjoint supports and `⋃I_η=D`; "The exact rules for eligibility are part of the definition of an effective density; they may exclude some otherwise possible covers". (ii) "original eligibility criteria" kept by a merged component (11:153; also 11R:80, 156, 166–168; 10:669): the conditions attached to each large-field activity, which fits the per-activity "additional Borel gauge-invariant eligibility test `𝓔_i^extra`" of 4:440–450; whether the text means this or again the family rule is not settled. Not the axial-bound sense of Part II | 11:125, 131, 153, 762, 791 | R (i) / I (ii) |
| response | "stationary forest response `W`" (11:642) — the object ch. 5 calls *transport* `W`; "curvature response `J=H_{0,f}^{-1}TH_{0,c}`" (11:647, D); "installed curvature response `Ψ_i`" with `Δ_wΨ_i=Q_{i,w}Δ_w` (11:1729–1735); "response paths" (11:1773). Also 10:626 "response bound" (?) | | R |
| transport | (iv) `𝖹` "transports a cutoff coefficient to its fixed reference level" (11:883); (v) "transported mean / coarse covariance" `𝓛u`, `𝓛κ_ℓ𝓛^T` = image under the product of responses (11:1788, 1812–1813); (vi) "polynomial transport steps / norm" = action of one step on polynomials (11:1870, 1958). Part II senses also occur: stationary-field map (10:354 "free transports"; 11:648, 651 two-form transport `T`), parallel transport (10:313) | | R / I |
| mass | weighted norm of a large-field input (1.3); "mass-one identity" = normalisation of the kernels (11R:389). Not the weights `λ(U,α)` | | I |
| lift | preimage under `S_{g/θ}T` (1.3) | 11:1352 | D |
| window | interval of levels; range of `\|x\|`; compact set of configurations (section 3) | | R |
| frozen | coupling held constant | 11R:246 | R |
| physical | at least five uses (section 3) | | I |
| selected | "selected trajectory / history / stage requirements" and "selected component" (section 3) | | I |
| target | "coarse target `β̄`" (10:153); "normalized target columns", "finite target list", "fixed separated targets" (11:1237, 1364, 2207) | | I |
| envelope | the majorant displayed at 11:1580–1582 | 11:1972, 2136 | R |
| extraction | besides the coefficient-extraction maps of 1.3: "The estimates are before extraction" (11:2037), where the word is not one of those maps (compare 11:2214 "a comparison before any cutoff limit"); not determined | 11:2037 | ? |
| weight | source weight, support weight, filtration weight, probability weight (section 3); Part II's "weight = scaling dimension" appears only as "scaling dimension" here | | R |

#### 2.3 Terms Part II marks open, clarified here

| Open term | What chapters 10–11 add | Basis |
|---|---|---|
| regularity-stage index `J_m` (4:651) | **Defined.** Stage: 10:25–31. Index: `J(m)=j` for `A_j≤m<A_{j+1}` with `k_j=c_j+2A_j+1`, `A_{j+1}=A_j+b_{j+1}+2k_j+1` (10:129–134); "`J(m+1)` is the stage used for this step" (10:50); `L_m=𝓛_{J(m+1)}` (10:144). | D |
| Warnings (6:1476) | 11:319: after the exact split `(1+γWz_S)(1+(1−γ)Wz_S)`, "the actual warning estimate gives its supporting event probability at most `x^{-1}`"; 11:1612–1614 says of the same step "`l/x≤1` … the actual cutoff-failure probability absorbs the complementary principal cutoff". So a "warning" is a cutoff-failure event (the event where a local smooth cutoff is not one) and the "warning estimate" the bound on its probability. The link between the two passages is an inference. | R / I |
| compulsory (6:1018, 1461) | 10:654: "Arrays constrained to cover prescribed large-field sites retain one compulsory large-field factor throughout fusion … with the hard factor retained once" (10:666); 11R:161 "The factor at that site is mandatory". Reading: the large-field factor that every such component necessarily contains. Does not settle "compulsory component region". | I |
| moving comparison fields (3:576) | Not used. "Moving" is used for cutoff-dependent objects: "moving equation space" (11:1083), "moving equation kernel `K_i`" (11:2218), "varying equation subspace" (11E:154), "moving threshold surface" (10:734). Supports Part II's guess, does not define the phrase. | I |
| centered log determinant; seeded / unseeded; output anchors; likelihood tests | Do not occur in chapters 10–11. | — |
| width (4.2) | **Made precise:** weight `e^{wℓ(γ)}` on path coefficients; "strict width reserve" = bound at `w'>w` giving tails `Ce^{-(w'-w)r}` (10:375–381). | D |
| compensating map (4.2) | 10:529–531 (see 1.2). | R |
| half-square (4.2) | 11R:101–111. | R |
| envelope (4.2) | The display 11:1580–1582 (a majorant, label `ch11:weighted-output-envelope`); the word itself at 11:1972 ("the weighted output envelope") and 11:2136 ("Their scalar envelope"). | R |
| coupling band (4.2) | 10:212 "The admissible inverse coupling band at level `m` is `[β̂_m/2,2β̂_m]`". | D |
| anchored vs containing-site sum (4.2) | conversion argument 11:266–272; 11R:141. | R |
| marked (4.2) | read off 11:70–75 (1.3); three uses (section 3). | R |
| event label (4.2) | here "event indicator(s)" throughout (10: 11 uses; 11: 8; 11R: 8); "cutoff-failure labels" not used. | — |

---

### 3. Multi-sense words (all occurrences classified; counts approximate to ±2 where "≈")

**row** (2 / 10 / 4 / 0).
(a) kernel of a translation-invariant operator (the chapter 5 sense, "Write a translation-invariant row as `K_{ab}(z)`", 5:711): 10:354 ("actual quadratic rows"; the sentence cites Proposition `ch05:horizon-limit`, "Convergence of the selected Gaussian rows", 5:738) — 1.
(b) component of the action vector (Part II sense 4): 10:356 ("direct row coefficient", cf. 5:749), 11:668 ("row Gram"), 11:710 ("linear fine comparison row"), 11R:101, 102, 122 ("quadratic path rows", "row pairs") — 6.
(c) literal matrix row / row sum: 11:684 ("curl rows"), 1210, 1212, 1262 ("axial row": row of the linear substitution links→curvatures), 1731, 1749, 1755 — 7.
(d) vector in a finite list: 11:2253 ("The rows `(I−Π_i)u_{j,i}` are bounded") — 1.
(e) undetermined: 11R:266 ("exterior row, determinant and Haar bounds") — 1.

**actual** (18 / 58 / 15 / 0).
(a) of this construction / on this same history (not an abstract or substituted object): 10: ≈14 (353, 373, 390, 414, 430, 473, 504, 609, 705, 728, 777, 889, 900, 906, 933); 11: ≈37 (27, 221, 268, 319, 330, 361, 381, 466, 642, 668, 1029, 1043, 1107, 1145, 1146, 1158, 1241, 1269, 1307, 1325, 1333, 1456, 1564, 1663, 1675, 1685, 1729, 1765, 1839, 1950, 1971, 2036, 2057, 2086, 2097, 2137, 2196); 11R: 4 (45 "these actual thresholds" `ϑ(x_i)`, 261, 288, 301).
(b) the running coupling `β` (or quantities in it) as opposed to the reference `β̂` or recording parameter: 10:808; 11:470, 693, 736, 1670; 11R:34, 47, 50, 57, 61, 115, 223, 246, 268, 272, 276 — 16.
(c) nonlinear / at the true background, as opposed to flat, linearised or polynomial: 11:415, 558, 672, 676 (title of the subsection on the actual-to-flat comparison, 11:681), 681, 704, 1183, 1222, 1783, 1867 — ≈10.
(d) the density or function itself as opposed to a representation or a modified density (= "genuine"): 10:265, 517; 11:1216 ("the Taylor polynomial of the actual function is unique; it does not require a linear choice of its separate activity representatives") — 3; 11:1325, 1950, 2097 ("actual density", "actual pushed density", "actual source"), listed under (a), fit here equally, which would make 6.
(e) the modified ("repaired") metrics as opposed to the unmodified `H_0`: 11:627, 649, 662 — 3.
(f) under the law in force (probabilities): 11:280, 293, 1613 — 3.
None fits Part II's "gauge-covariant block average" sense.

**selected / selection / select** (5 / 30 / 12 / 3) and **chosen** (4 / 18 / 3 / 1).
(a) large-field: a "selected" large-field support, activity, component, site factor or cutoff condition, i.e. one belonging to the large-field index set of the term (ch. 6 "selection"): 11:139, 149, 151, 154, 248, 339, 424, 425, 434, 520, 761, 923, 1933; 11R:63, 159, 170, 182, 286, 288, 301 (×2), 305, 312, 316; 11E:82 — ≈25. "Unselected" 11R:264, 313.
(b) fixed by the construction (trajectory, history, stage requirements, block kernels, plateau, comparison levels, schedule inequalities, forest): 10:883, 923; 11:111, 617, 1045, 1059, 1200, 1401, 1965, 2056, 2176, 2182, 2294; 11R:89; 11E:34 — ≈15.
(c) ordinary "choose": 10:273, 746, 892 ("A new selection of equally bounded coefficients"); 11:219 ("before the history thresholds are selected"), 1766, 1857, 1885, 2000, 2084 ("before selecting the stage orders"); 11E:30 ("the selection order") — 10.
Senses (a) and (b) do not meet inside one paragraph; the nearest cases are adjacent paragraphs (11:1933 "Its selected site factor" and 11:1965 "The selected plateau") and one proof (11R:89 "the selected trajectory's endpoint bounds" and 11R:159 "a selected `X_z`").
`chosen` is ordinary throughout (26 uses), e.g. 10:63, 11:218, 713, 1392; none in the "random index" sense.

**test** (1 / 11 / 1 / 0).
(a) standard (test against a function; sign-valued test function): 11:115, 1755 — 2.
(b) "tested correlation" = value of the functionals `L_i` on an insertion: 11:2233, 2235, 2276, 2288, 2320 — 5.
(c) "tested links / neighborhood" = links (sites) on which a function depends: 11:402, 413; 11R:107 — 3.
(d) evaluate / check: 10:113 ("degrees are tested at a stage"), 11:355 ("is tested with one additional derivative"), 11:1016 ("to test finite differences") — 3.
Part II's senses "condition", "variable", "location", "indicator" do not occur under the word "test"; they now appear as "event indicator", "cutoff condition", "finite parameter evaluation".

**label / tag** (6 / 27 / 5 / 2).
(a) polynomial label, element of `V_d` (Part II sense 1): 11:15, 29, 946, 958, 965, 1307, 2052, 2057, 2065, 2162, 2169; 11E:43, 55 ("equation labels" = elements of `S_{t_N}R_d𝓘_d`) — 13.
(b) insertion label, element of `𝓘`: 11:33, 39, 132, 178, 185, 193, 195, 204, 246, 341, 344, 517, 1371 — 13.
(c) index of an activity, path or large-field term: 10:249, 395, 709, 757, 895; 11R:80, 144, 184 — 8 (at 11R:144 "enlarged old large-field labels" the label stands for the term).
(d) tag = random index `α`: 11:244, 679; 11R:358, 359 — 4.
(e) not prose / standard: 10:461 (LaTeX `label=`), 11:871 ("tagged partitions", Riemann sums).

**mark / marked** (0 / 50 lines / 6 / 0; "unmarked", 17 more in file 11, not counted).
(a) mark (noun) and marked point / site / ancestor (adjective) = an insertion point, its lattice site or its index ("marks project to a coarse site", "per mark", "marks from many cells"): ≈30, e.g. 11:184, 216, 258, 260, 268, 272, 496, 516, 542, 727, 783–784, 1380, 1417, 1578 (noun); 11:180, 181, 187, 189, 208, 301, 340, 482, 1411, 1434, 1439, 1894 (adjective).
(b) carrying a nonempty label set (marked term, factor, component, activity, coefficient, region): ≈10, e.g. 11:138, 176, 252, 312, 393, 784, 1384, 1457, 1931.
(c) with insertions, of a whole object (marked density, expansion, step, polynomial, family, exponential): ≈16, e.g. 11:2, 218, 221, 381, 608, 1386, 1564, 1579, 1581; 11R:9, 212, 239, 291, 381, 391.
"Unmarked" = coefficient of `z_∅` (11:70 "unmarked density") or factor with empty label set (11:244).

**window** (3 / 13 / 4 / 0).
(a) index neighbourhood on which an operator is inverted (Part II `Ω_i`): 10:358; 11:135, 673, 683, 684 — 5.
(b) interval of levels: 10:185, 189; 11:1462, 1675, 1795, 1965, 2091, 2092; 11R:215, 218, 222, 298 — 12.
(c) range of distances `|x|≤H^c`: 11:1726 — 1.
(d) compact set of point configurations: 11:2078, 2149 — 2.

**history** (22 / 14 prose / 3 / 4).
(a) finite trajectory for a cutoff (densities, couplings, arrays): 10: ≈20 (13, 15, 209, 232–256, 295, 447, 517, 792, 799, 805, 826, 849, 862, 889, 918, 927).
(b) the fixed choice of kernels, couplings, path pairs and representations (11:18): 11:18, 21, 26, 117, 219, 736–741, 1665, 2058, 2091, 2183; 11R:5, 215, 392; 11E:2, 8, 34, 144 — ≈18.
(c) sequence of blocking kernels / parameters (Part II): 10:373, 933; 11:92 ("Changing the block history": "Replace any kernels below a fixed level `k`"), 1699 — 4.
(11:765 is an `\input` file name.)
Senses (a) and (b) are close: chapter 10 already attaches the choices to the trajectory ("Choose one such history for each `N,p`, retaining its path arrays, forests, local integral choices and output representations", 10:256–257). Treating them as one sense is a judgement.

**source** (3 / 36 / 1 / 2).
(a) source variable / monomial / "linear in the sources": ≈16 (11:49, 133–134, 507, 509, 1324, 1384, 1458, 1477, 1487, 1493, 1577, 1584, 1881, 1891, 2129; 11E:144).
(b) source weight: ≈12 (11:29, 192, 195, 496, 938, 953, 1044, 1370, 1374, 1377, 1590, 2200).
(c) source algebra: 11:13, 23, 2095 — 3.
(d) the source polynomial or density itself ("terminal regular source", "corrected source", "source density `q_k`", "actual source", "corrected source coefficient", "complete source norm bound"): 11:133, 769, 1671, 2097, 2140; 11E:84 — 6.
(e) an insertion ("local sources", "source anchors"): 10:173, 178 — 2.
(f) ch. 6 sense (inhomogeneous term of the affine map), undefined here: 10:900 ("actual source and event indicator"), 11R:43 ("clipped source") — 2.
(g) not classified: 11:1632 ("Reassigning a principal source term to its prescribed enlarged support"), probably a term of the source polynomial, i.e. (a) or (d) (inferred).

**price / pay**: do not occur. `cost` etc.: section 1.5.

**detector, probe, readout, table**: do not occur in prose (labels only, section 4). `detect`: 3 uses, section 2.1.

**response**: 10:626 (?); 11:642 (`W`), 647 (`J`), 1729, 1730, 1750, 1773, 1775 (`Ψ_i`). See 2.2. None is the ch. 3 two-point function.
**leading** (three uses, none defined). (a) leading-order part of the one-step map: "The leading rescaling", "the leading map is `TS_L`" (11:370–377). (b) the upper interval `k→ℓ` and its steps: "an earlier leading step" (11:1410), "the leading recurrence" (11:1643), "The leading interval" (11:1952). (c) the principal coefficients: "the corrected leading coefficients at the middle level" (11:1551, 1886).

**transport**: 10:313 (parallel), 10:354 (stationary-field map); 11:648, 651 (two-form map `T`), 883 (`𝖹`), 1751 ("exterior-transport identities", ch. 5), 1788, 1812, 1813 (image under `𝓛`), 1870, 1958 (step acting on polynomials). See 2.2.

**frame**: 10:128 ("frame-choice variables", Part II sense); 11:688, 690 ("root frame", "local frame": gauge choice); 11:1286, 1288, 1293 ("fixed radial polynomial frame", "frame coefficients": a basis of polynomials — third type of notation.md's "frame").

**anchor**: 10:178 ("source anchors") and 11:161 ("insertion anchor"): the site of an insertion (Part II sense i/ii); 11:362, 364; 11R:141, 199, 209, 340, 375: "anchored" sums.

**phase**: 11:1714 ("phase difference", Fourier; standard). **word**: transfer word (11:842, 849, 863); difference word (11:2227, 2251, 2278, 2297, 2304); determinant-word series (11R:270, ch. 6 sense).

**root / rooted** (4 / 25 / 2 / 1).
(a) root of a tree or of a rooted sum (standard): 11:267–272, 300, 310, 393, 456, 508–510, 1918; 11R:329; 10:889.
(b) block root / rooted gauge (Part II): 11:628, 631, 633, 688.
(c) number-of-cells root = chessboard seminorm: 11:817, `‖·‖_root` 2027, 2075.
(d) "rooted activity norm / bound / contribution" (11:1437, 1440, 1552, 1892, 1936): a norm with sums pinned at a marked site (inferred).
(e) square root (10:100, 108; 11:360; 11E).

**scalar** (16 / 13 / 4 / 0): (a) constant term of the action / normalisation (`v_0`, `σ`): 10:266; 11:609, 726, 789, 814, 2014; 11R:73, 190, 362–363. (b) the coupling correction `q_m` ("scalar correction", "projected scalar", "scalar recursion", "cumulative scalar bound"): 10:421, 645, 684, 772, 816, 826, 842, 849, 868–870, 902. (c) "scalar coordinates" = `λ` (10:443). (d) ordinary (scalar multiple, scalar majorant): 11:85, 1011, 1105, 1579, 2136.

**physical** (9 / 28 / 2 / 4): (a) in continuum units (period, volume, separation, cell): 10:128, 389; 11:981, 1030, 1124, 2190, 2301. (b) "physical coordinates" = the same fine link variables at both cutoffs (10:711, 725, 732, 896–898; 11:472). (c) "physical inverse couplings" = `β` as opposed to the coordinate `λ` (10:880). (d) "physical insertion / normalization / section / unit" = with the factor `a_N^{-d}`, as opposed to dimensionless (11:72, 86, 88, 920, 1051, 1109, 1158; 11E:7; 11R:5). (e) before division by `g` / unnormalised fluctuation (11:696; 11R:60). (e′) 11:588 "replace the physical coordinates by `a+η_t`": the "actual normalized local curvature coordinates" `ξ_{t,I}` of 11:558–560, as opposed to their Gaussian model. (f) "physical counting coordinates" (11:621), "physical Lipschitz bound" (11:866), "physical jet block" (11:1832), "physical support-weighted mass" (11:423): not clearly any of these.

**unit** (1 / 18 / 1 / 0): identity insertion (11:87, 89, 389, 451, 1050); unit of support exponent (11:396, 495, 502, 528, 533, 939, 1446; 11R:141); units of measurement (10:128; 11:704, 861, 2301); "two unit bounds" = bounds by one (11:792).

**endpoint** (10 / 4 / 4 / 1): (a) the level-0 coupling (10:18, 209, 268–272, 278, 813, 850); (b) endpoints of an interval (10:139–140, 247); (c) the top level `k` of the restart window (11R:68, 89, 384, 387; 11:1930, 2092); (d) the last step at `N` (11E:124); (e) ends of a finite difference (11:2287); (f) 11:877 "normalized endpoint inequalities" (?).

**weight**: source weight `ω` (≈20); support weight `e^{σc_B}` (11:198, 204, 1369, 1446; 11R:188); filtration / scaling weight (11:407, 411, 1288, 1848); spatial / derivative weight (10:79; 11:351, 1068); probability / averaging weights (10:465; 11:563, 602; 11R:112, 361); "encoding weights" (10:382, ?).

**cutoff**: ultraviolet cutoff `N` (10 passim); smooth cutoff `γ` (11:314, 544–557, 708); threshold ("cutoff-to-noise ratio", 11R:61); path-length truncation (11:672); "failed cutoff condition / factor", "cutoff failure" = large-field event (10:532, 595–597; 11:151, 1476–1500, 1613; 11R:283, 311, 378). All but the last are Part II senses.

---

### 4. Terms the chapters do not determine

| Term | Where | What can be said |
|---|---|---|
| Hilbert encoding; encoding weights | 10:381–382 | An alternative parametrisation of path coefficients requiring summable weights. Occurs only here. |
| response bound `ε` | 10:626 | A constant of the ch. 9 remainder estimate; the word "response" does not occur in chapter 9 (one reader). |
| "sparse" (sparse stopping scale) | 10:172 | The stopping scale itself is settled (1.2, last row); the adjective is unexplained. |
| preselection bound | 11:382 | Value `C_d/L+o_x(1)` given, name unexplained. |
| selected slot | 11:424 | "Its selected slot has no purely principal component." |
| coarse kernel level | 11:352 | "coarse kernel level at least `d+3`" beside "fine kernel order"; whether level = order is not stated. |
| front-column (inverse front-column bounds) | 11:1343 | Gives `‖u‖_1≤D_k‖Au‖_1`. |
| alphabet ("original marked alphabet") | 11:1911 | Possibly the original index set of terms. |
| coarse forecast | 11:726 | Possibly the conditional mean. |
| corrected body product estimate | 11:1662 | "Body" unexplained. |
| same-data restart conditions | 11:1666 | Not stated anywhere in these files under that name. |
| extraction ("The estimates are before extraction") | 11:2037 | Not the coefficient-extraction map of 1.3; compare 11:2214 "a comparison before any cutoff limit". |
| block length | 11:1873 | The block ratio `L` (as at 11E:20) or the number of steps `m`; not determined. |
| protected local representative / protected trial | 11:1063, 2306 | Not the "protected change of variables" sense; 13:229 ("the protected trial construction") reuses the phrase without explaining it. |
| finite decorations | 11R:304 | — |
| tail events; tail-event factors | 11R:43, 284 | Possibly the Gaussian tail events of the chapter 6 chart rather than the large-field event; not determined. |
| powered-curvature-factor estimate | 11E:14 | Refers to ch. 2; not checked. |
| exterior row | 11R:266 | — |
| (fixed common) coefficient functionals; curl-division and path-placement operations; exchange term | 10:373, 813, 889; 10:314; 10:337 | Undefined in these chapters (1.6); the last refers to ch. 7. |

Narrowed by the text, without a definition (all inferences; details in the rows cited):

| Term | Where | Reading | Row |
|---|---|---|---|
| block bridge | 10:921 | probably the smooth tangent transport `W_a` (5:1132, 1152; 7:597–598) | 1.2 |
| sparse stopping scale; replication costs; Haar-ball normalization argument | 10:169–172 | the level `k(m)` of 13sb:104–109 and the chessboard argument of 11:795–819 | 1.2 |
| exposure `𝓔` | 11:1285 | linear map to coefficients in a fixed polynomial basis, bounded below | 1.3 |
| "n copies" | 11:781 | `n` = number of reflected cells | 1.3 (reflected replica cell) |
| restoration levels | 11:1405 | the middle levels `ℓ` | 1.1 (comparison level) |
| deletion-of-support identities | 11R:239 | `(ch08:deletion-identity)`, 8:208–215 | 1.4 |
| regular logarithms with holes; raised hole correction | 11R:365–369 | `e^{−𝓛_Y}−1` for the deleted set `Y=Y(B)` of 8:311–315 | 1.4 |
| `hot(s)` | 11:1934 | `u=a_*hot(s)^2`; by comparison with 11R:114 (`u=a_*h(s)^2`) this is the function `h(s)`. A leaked source name; not a word for the large-field event. | — |

Sentences damaged by mechanical replacement. The replaced source words were "inventory" (→ "prescribed set of large-field sites", per notation.md), "unmasked", "guarded" and "entry-controlled". The nine sentences first listed were reread in the present files; all now parse:

| Line | Present text | Parses |
|---|---|---|
| 11:247–250 | "The exact condition on prescribed sets of large-field sites says that every selected incoming prescribed large-field set is supplied by the unmarked local correction factors in its component." | yes ("supplied by" remains a house verb, 1.5) |
| 11:296–297 | "If none occurs, the condition on prescribed sets of large-field sites removes incoming large-field factors;" | yes |
| 11:363–365 | "… large-field majorants, with their original indices of support and prescribed set of large-field sites." | yes |
| 11:1312 | "It equals `F_u^near` without its event indicator wherever `χ=1`," | yes |
| 11:1595–1596 | "Split the positive decay of the prescribed set of large-field sites in Chapter 6 into reserved fractions" | grammatical, meaning doubtful (below) |
| 11:1636–1637 | "Its complementary cutoff part retains the original prescribed set of large-field sites." | yes |
| 11:1867–1870 | "use (ch11:raw-polynomial-error), the common Gaussian estimate with a smooth cutoff, and telescope the finitely many polynomial transport steps." | yes |
| 11R:302–303 | "Coverage of the original prescribed set of large-field sites ensures that an incoming large-field factor cannot occur without such a component." | yes |
| 11:2133 | "the regrouping of activities constrained to cover prescribed sites has bound" | yes (a long noun phrase for the former "forced" activities) |

Three further sentences that were damaged now read correctly: 10:922–923 ("identifies an auxiliary graph"), 11:938 ("has cover at most 81;"), 11:1589–1590 ("The ordinary bound by one for terms involving at least two insertions has neither the source weight nor the small initial remainder needed here.").

Still damaged or doubtful:

| Line | Present text | Problem |
|---|---|---|
| 11:1595–1596 | "Split the positive decay of the prescribed set of large-field sites in Chapter 6 into reserved fractions" | "decay of a set" and "in Chapter 6" attach loosely. Probably: the positive decay rate that Chapter 6 gives per prescribed large-field site (inferred). |
| 11R:300–301 | "Apply the factor `m` only to components with an actual selected prescribed set of large-field sites, and to a selected component within each such component." | "a selected component within each such component" and "actual selected prescribed set" are unclear; this sentence was not touched by the repair. |
| 10:98 | "On that chart the relaxed small-field smooth cutoff is one." | Parses, but conflicts with Part II (section 9), where `χ^rel` is an indicator; `blueprint/notation.md` line 93 says of `χ^rel`, `clip_t`: "Relaxed small-field test … clip has a jump, not a smooth cutoff". Probably "smooth cutoff" replaced another word ("guarded"?); conjecture. The same caveat applies to "with a smooth cutoff" at 11:1868–1869. |

Jargon surviving only in labels (the word does not occur in the prose of these four files): `ch10:finite-tests`, `ch10:broad-test`, `ch10:parameter-supplier`, `ch10:cutoff-supplier`, `ch10:late-entry`, `ch10:prefix`; `ch11:higher-modes`, `ch11:n-mark-root`, `ch11:actual-reader`, `ch11:detectors`, `ch11:detector-bound`, `ch11:uniform-detector`, `ch11:finite-detector-input`, `ch11:simultaneous-detector-lifts`, `ch11:uniform-sweep`, `ch11:dispersal`, `ch11:restore-forced`.
Labels whose word is also in the prose: `ch10:shooting` ("the shooting parameter", 10:273; "the choices made in shooting", 10:818); `ch10:drift-floor`, `ch10:equation-floor`, `ch11:calibration-floor` ("floor", 10:55, 90; 11E:29); `ch11:mass` (11:423); `ch11:root-bound` ("number-of-cells root", 11:817); `ch11:replicated(-bound)` ("replication costs", 10:172); `ch11:weighted-output-envelope` (11:1972); `ch11:opening-higher-weight` ("the opening level", 11:1889).
Symbols: `ε^{for}`, `w^{for}` ("forced": 11:360, 888; 11E:94–98), `z_{forced}` (11:1628), `‖·‖_root`, `hot(s)`, `f^{near,mask}`, `C_{orb}` (11:428), `M_f^{cut}` (11:715).

---

### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| lower bound on the level where a stage starts | delay; stage delay; threshold for the starting scale; choice of a sufficiently large starting scale; condition on the starting scale; stage entrance; late entry (label); inverse coupling threshold | *lower bound on the starting scale* (and *coupling threshold* where it is a bound on `β̂`, as for the terminal delays of 10:107–112) |
| lower bound on the cutoff | mesh threshold; "once the mesh is sufficiently fine" (11:1123–1131) | *for `N` large enough* |
| lower bound on the block ratio | floor; stage floor; ratio floor; block floor | *lower bound on `𝓛_j`* |
| strict spare margin | reserve; margin; room to spare; retained unit; spare support (label) | *margin*, with the inequality |
| loss in an estimate | cost; expense; loss; inflation; amplification | *factor*; *loses a factor* |
| the top of the restart interval | comparison level; comparison depth; top level; opening (level); endpoint. (The "stopping" words of 1.1 do not belong here: the chessboard normalisation of the restart argument is at the output level, "At the output `V=q_0`", 11:2019.) | *level `k`* |
| the restart sequence and its representations | the sequence: restarted history; auxiliary history; restarted family. Its local representations: restarted representation(s); presentations `P_i` | one name for each of the two |
| representation of a density | local representation; presentation; (ch. 4) density coordinates | *representation* |
| main part of an insertion factor | principal; leading ("corrected leading coefficients", 11:1551, 1886) | *principal* ("leading" has two other uses, section 3) |
| its complement | nonprincipal; nonleading; remainder | *nonprincipal* |
| large-field part of an insertion | complementary part / stencil / cutoff; failed-cutoff factor; tail-event factor | *large-field part* |
| large-field event | cutoff failure; failed cutoff condition; warning. Possibly also tail event (11R:43, 284), which may instead be the Gaussian tail event of the ch. 6 chart (section 4) | *large-field event* (one word) |
| activities constrained to cover given large-field sites | "large-field" activities; activities "with prescribed set of large-field sites"; "forced" (symbols); "selected" components; "hard" factor; compulsory / mandatory factor | *large-field activity with prescribed large-field set*; *its mandatory factor* |
| true density | actual; genuine; exact; "the object integrated" | *the density `ρ`* vs *its representation* |
| the localization maps `T` (two maps, 1.3) | localization; extraction; coefficient extraction; common extraction; localization onto the polynomial label space | *one-step localization* and *common localization map*, with different symbols |
| value of a correlation functional | measurement; tested correlation; correlation pairing; detection | *value of `L_i`* |
| cell of the reflected tiling | replica cell; reflected replica cell; reflection cell; measurement cell; comparison cell; copy | *cell* |
| insertion | insertion; mark; source (10:173); normalized local insertion; trial (when to be approximated) | *insertion*; *insertion point* |
| index of an insertion | insertion label; mark; source variable index | *insertion index* |
| sum over terms containing a site | site bound; site sum; containing-site bound | *site sum* |
| scale index | level; scale; depth; step (10 passim; "comparison depth", "cell depth" 11:2192) | *level* |
| cutoff-dependent | moving; varying; changing (10:450). Not 10:730–734, where "moving" is dependence on the mean or precision | *cutoff-dependent* |
| inverse coupling in use | actual; tuned; common (11R:223); frozen | *the coupling `β`* vs *reference `β̂`* |
| `W` of chapter 5 | transport (ch. 5); (stationary forest) response (11:642) | one word |

---

### 6. Overloaded symbols noticed

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

### 7. The ten most confusing terms

1. **actual** (91 uses, six senses) — in most places it only means "of this construction", but in 11R it mostly means the running coupling and in 11:627–662 the modified metrics.
2. **principal / nonprincipal / leading / nonleading** — carries the main case distinction of the marked step (11:284–292) and is never defined; "leading" has two further uses (section 3).
3. **selected** — "selected component" (large-field) and "selected trajectory" (fixed by the construction) occur in adjacent paragraphs (11:1933 and 11:1965) and within one proof (11R:89 and 11R:159), though never in the same paragraph.
4. **stage / plateau / delay / floor / request / threshold for the starting scale** — a whole scheduling vocabulary; "stage" is defined, the others are not, "delay" has four or five paraphrases, and "mesh threshold" is a different condition (on the cutoff).
5. **comparison level, top, opening, middle, output, leading interval, lower interval, restoration levels, stopping pair** — three levels with many names and no single definition.
6. **reserve / cost** (44 + 42 uses) — the reader must reconstruct each inequality.
7. **graph `G`, column bound, raw map, rebasing** (11:379–468) — the single-insertion recursion is stated in undefined nouns.
8. **mark / marked** — three uses, and "source" used for the same objects in a further six ways.
9. **history** — defined in 11:18 in a sense different from chapter 5 and close to, but wider than, chapter 10's "finite history".
10. **prescribed set of large-field sites** and its relatives (forced, compulsory, mandatory, hard, selected site factor) — defined in chapter 8 (1.6) but used as an adjective phrase; the sentences it broke are mostly repaired (section 4). **incidence**, **trial**, **lift** and the two maps **`T`** are close runners-up.

---

### 8. Not read / not checked

- All four files were read in full by the survey's author and by one later reader. The `figures/cutoff-histories` file input at 10:835 was not read.
- Occurrence lists come from `grep` on single lines; a term split across a line break is missed. Per-sense counts marked "≈" were assigned from one-line contexts plus the full read and may shift by a few.
- Cross-chapter passages opened: 4:438–450; 5:710–712, 738, 749–752, 1132, 1152; 7:597–598; 8:208–216, 286–295, 311–315; 9:409–411, 631–635, 651–666, 716–719, 733, 739; 13sb:34–38, 102–110; 13:229. Not looked up: "powered-curvature-factor estimate" (ch. 2), "factor count" (2:52–53), "principal norm" (ch. 9:235), "kernel level", "exchange term" (ch. 7), the ch. 13 uses of "trial".
- No Lean source was consulted; no proposed equivalent was checked against the literature. Proposals are judgements from general mathematical knowledge.
- Section 6 is a list of what was noticed while reading, not a systematic symbol audit.

---

### Changes folded in

Origin: B = independent audit of the survey; R = re-audit report; "own" = own reading while folding. "v" = verified by opening the cited lines for this fold; "nv" = taken over without opening every line.

Whole section
- Status notices removed; headings lowered one level; "the dictionary" written "Part II" (the house term "dictionary" of 10:376 is unchanged). Pipes inside code spans of table rows escaped. (own)

1.1
- stage: proposed equivalent "regularity level" replaced by "regularity class" (B; collision with "level `m`"; judgement).
- floor: added the coupling condition that accompanies the 11E block floor (R D3; v 11E:25–32).
- delay: terminal delays of 10:107–112 separated; basis and proposal adjusted (B; v).
- threshold for the starting scale: "mesh threshold" removed from the row; new row "mesh threshold" = lower bound on the cutoff (B; v 11:1119–1131, 1815).
- comparison level: "restoration levels" read as the middle levels `ℓ`, basis I (B; v 11:1405–1407, 1551–1553, 1564–1569).
- stopping pair: pointer to 13sb:104–109 (B; v).
- restart: restarted history and restarted representation separated (R D2; v 11R:2, 18; 11:736–741 nv).

1.2
- dictionary: basis R → R / I (B; v 10:375–382).
- finite parameter evaluation: equivalent "norm of the functional on `c_0`" replaced by "sup norm of the moment sequence" (B, R E4; v 10:464–477, 630–635).
- hard / soft: meaning and equivalent replaced (B; v 10:654–666, 9:631–635, 651–666).
- fusion: basis D → I, "defined in ch. 9" withdrawn (B; v 9:631, 651–652; the section title was not opened).
- reset: meaning and equivalent corrected (B; v 9:716–719).
- residual scalar correction `q_m`: correspondence with `Δ` added, marked as an identification (B; v 9:719, 733; 10:648).
- path coefficient `α`: meaning sourced to ch. 9 (B; v 9:409–411, 739; 10:421–423).
- block bridge: ? → I, probable reading `W_a` (R D5; v 5:1132, 1152; 7:597–598).
- moving expression: 10:730–734 separated from "cutoff-dependent" (B; v).
- replication costs / sparse stopping scale / Haar-ball: settled by 13sb and 11:809–822; only "sparse" left open (B; v 13sb:34–38, 102–110; 11:809–822; 11:795–805 nv).

1.3
- mark: basis I → R (B; v 11:70–75).
- principal: quotation corrected; equivalent "leading part" withdrawn (B; v 11:314–332, 377, 1410, 1643, 1952).
- occupancy: locator corrected (B; v 11:258–260, 345; 10:109).
- complementary part: basis R → R / I, explicit formula cited (B; v 11:147–156, 1490–1494).
- raw: 11:901 → 900, 1014 → 1013 (B; v).
- common localization: two maps `T` separated (B, R; v 11:370–377, 1180, 1203, 1285–1293; the name `Au` nv).
- exposure: ? / I → I, object described (R D5; v 11:1285–1293).
- trial: "trial encoding" identified (B; v 11:945–951, 1074–1076).
- backward comparison / descent: meaning and equivalent replaced (B; v 11:893–915).
- cone inequality: I → R (B; v 11:905–906, 893; 11E:125–128).
- corrected coefficients `R_I`: equivalent "truncated (connected) coefficients" withdrawn (B; v 11:2096–2099).
- chessboard seminorm: usage caveat added (B; judgement).
- reflected replica cell: "n copies" explained (B; v 11:781, 809–822).
- envelope: "Def." cell now says display 11:1580–1582 (R E3; v). The survey's locator for the word (11:1972, 2136) was already right.

1.4
- presentation: 11R:250 → 251 (B; v).
- regular logarithms with holes: ? → I with probable reading (B; v 8:311–315; 11R:365–369).
- deletion-of-support identities: separate row, ? → I (B; v 8:208–216; 11R:239).

1.5
- row "fit(s)" added (B; v 11R:305–306, 330–332).

1.6 (new subsection; 15 rows added)
- prescribed set of large-field sites (B, R; v 8:286–295, 4:438–450); normalized local insertion (B, R; v count, 11:1051–1054, notation.md line 158); ordinary (B, R; v by grep of all uses); factor count (R; uses v, the ch. 2 definition nv); block length (B; v 11E:20, 31–32; 11:1873); pre-threshold constants (B; v 11:1396); energy / suppression (B; v); value (B; v 10:106, 391, 765; 11:925); bottom (B; v); kill (B; v 11:970, 1691); returned / reported / declared / encoded (B; v); coefficient functionals (B; v 10:373, 813, 889); curl-division and path-placement (B; v 10:314); exchange term (B; v 10:337); smaller words (B; v except 11:343, 2041–2047 "arity" read at 2041–2047 only).

2.1
- stationary graph / jets: locator corrected (B; v 10:336, 717).
- inherited: 10:761 removed (B; v).

2.2
- history: 11:92 added to the kernel sense (B; v 11:92–95).
- eligible: I → R (family sense) / I (per-activity sense); both readings stated (B and R D1 differ; v 8:286–295, 4:438–450, 11:125, 153).
- envelope: reference to the display corrected (R E3; v).
- extraction: row added for 11:2037 (B; v 11:2037, 2214).

2.3
- envelope: locator corrected (R E3; v 11:1580–1582, 1972, 2136).
- marked: basis I → R (B; v).

3
- row: 10:354 moved to a new kernel sense; component sense 7 → 6 (B, R; v 10:353–356; 5:710–712, 738, 749–752).
- actual: 11R:45 (b) → (a); 11:676 (a) → (c); 11:1216 (c) → (d); note on 11:1325, 1950, 2097 (B; v each line).
- selected: 10:892, 11:219, 2084, 11E:30 moved from "fixed" to ordinary; sentence on paragraphs added (B; v each line and 11:1933, 1965; 11R:89, 159).
- mark / marked: senses (a) and (b) merged (B; judgement, examples nv).
- history: chapter 10 count 23 → 22; 11:92 moved to (c); remark on closeness of (a) and (b) (B; v count, 11:92, 10:256–257).
- source: 11:1632 added as unclassified (B; v).
- physical: 11:588 separated from sense (e) (B; v 11:558–560, 588).
- leading: new entry, three uses (B; v 11:370–377, 1410, 1551, 1643, 1886, 1952).

4
- Removed from the undetermined table and moved to a "narrowed" table: block bridge, sparse stopping scale, exposure, "n copies", restoration levels, deletion-of-support identities, holes, `hot(s)` (B, R; v as above).
- Added to the undetermined table: extraction (11:2037), block length (11:1873), tail events, the three undefined terms of 1.6; protected trial: 13:229 cited (B; v).
- Damaged sentences: all nine reread; all parse; 11:1595–1596 kept as doubtful; 11R:300–301 and 10:98 added (R section 6, B; v each line and notation.md line 93). Three further repairs noted (10:922–923, 11:938, 11:1589–1590; v).
- Label list split into "label only" and "word also in prose" (B; v by grep for prefix, sweep, dispersal, supplier, detector, reader, broad, "finite tests", "higher modes", "late entry": none in prose; shooting, floor, mass, root, replication, envelope, opening: in prose).

5
- "mesh threshold" taken out of the first cluster; new cluster "lower bound on the cutoff" (B; v).
- "the stopping level `k`" removed: the phrase does not occur (B; v grep; 11:2019).
- restart sequence: history and representations separated (R D2; v).
- principal: proposal changed to keep "principal" (B).
- large-field event: `"hot"` removed; "tail event" flagged as uncertain (B; v 11:1934, 11R:114, 43, 284).
- maps `T`: two maps (B; v). cutoff-dependent: 10:730–734 excluded (B; v).

7
- Item 3 corrected (not "within single paragraphs"); items 2, 4, 8, 9, 10 adjusted to the corrected sections (B; v).

8
- List of cross-chapter passages replaced by those actually opened.

Corrections proposed but not applied
- R E3 for the survey's row 1.3 "envelope": nothing to change, the row already cites 11:1972, 2136 with the label at 1580. B's confirmation "envelope (11:1581)" is wrong as a locator of the word (line 1581 is inside the display); only rows 2.2 and 2.3 needed the correction.
- R E5 (compulsory at 11R:161), D15 (Warnings 11:1612), D16 (weight restoration range): these concern the overview; the survey rows already quote "mandatory" at 11R:161, cite 11:1612–1614 and list the lemmas at 11:1436 and 1471. No change.
- R section 5, items already present in the survey (arrays, terminal, localization, inner barriers, tuned, opening, magnification, common Gaussian, occupancy, menu, plant, screened, stopping): no rows added.
- B: merging history senses (a) and (b) into one: kept as two senses with a remark, since B itself calls it a judgement.
- B and R on "eligible": B takes the word as settled by the family rule of 8:286–295, R reads the later uses as the per-activity test of 4:440–450. The text supports the first at 11:125 and does not decide the second at 11:153; both are recorded.
- B: "chessboard seminorm" possibly not established usage: recorded as a caveat, the name is kept.

### Verification status

Checked against the text by at least one reader other than the survey's author
- Rows confirmed by B (meaning, basis, references): in 1.1 stage, plateau, schedule, floor, delay, request, inner barriers, shooting, tuned, coarse target, comparison level family, comparison window, stopping pair, restart, recording scale, re-expression of the endpoint; in 1.2 both history rows, pad by zero, prescribed-site rules, finite parameter evaluation (meaning), narrow / reserved band, compensation, held fine reads, real nodes, low-order collection, stationary branch; in 1.3 source algebra, source weight and restoration, insertion label, push, unit, inflation factors, incidence, site bound, menu, join / attach, graph `G`, raw, rebasing contraction, column, vanishing-jet remainder, screened, mass, common Gaussian, corrected source, near part, lift, magnification, measurement, terminal map, calibration, admissible, equation subspace, positional modulus, transfer word, difference word, plant, spans, expense; all rows of 1.4 not changed above; the counts of 1.5 (cost, reserve, retain, supplies, subpower exact; absorb, margin, input within three); all rows of 2.2 not changed above; all rows of 2.3.
- Section 3: B recounted row, actual, selected, test (13 assignments), label / tag (40), window (20), history, source, response, transport, mark; R recounted the totals of actual and window and reread the row, test, label and window lines it lists.
- Every correction marked "v" above was opened for this fold, together with the present text of the damaged sentences.
- R confirmed, for these chapters: 11:18–19 (history), 10:25–26 and 10:129–133 (stage, `J(m)`), 10:212–213 (coupling band), 10:375–381 (width), 11:736–741 (restarted history), 11E:25–29, 11:817–822 and 11:2072–2076 (chessboard seminorm), 11:1934 against 11R:114.

Checked only in part
- Section 2.1: B spot-checked about 25 of 35 rows; two were corrected here; the rest of the rows are otherwise the survey's.
- Section 6 (overloaded symbols): B spot-checked about 30 entries, all correct; not audited systematically.
- Section 3: per-occurrence assignment of scalar, unit, endpoint, weight, cutoff, root, frame, anchor: totals checked by B, assignments only sampled; physical checked for senses (a)–(e) only.
- The "≈" example lists for mark / marked after the merge of two senses were not re-tallied.

Resting on one reader only
- On the survey alone: the unsampled rows of 2.1; most of section 6; the sense lists named in the previous paragraph; the cluster table of section 5 apart from the rows changed above (that the words of a cluster denote one object was not checked by anyone else).
- On B alone: the identification of `Au` as the radial Taylor localization; the statement that "response" does not occur in chapter 9; the title of the chapter 9 section on fusion; the check that `W` of 11:642 is the chapter 5 transport.
- On R alone: the definition of "factor count" at 2:52–53.
- New rows of 1.6 were written from B's and R's findings and the lines opened for this fold; their meanings marked I have had no second reader.
- No proposed equivalent was checked against the literature, and no Lean source was consulted. `figures/cutoff-histories` and the chapter 2 "powered-curvature-factor estimate" remain unread.

---

<a id="part-v"></a>

## Part V. Chapters 12–16

Dictionary of the house terminology of chapters 12–16 and of the files input from chapter 13. It is the survey of these chapters with the corrections of the independent audit and of the re-audit folded in. The changes are listed under "Changes folded in" at the end; "Verification status" says what has been checked by more than one reader. Meanings marked I are inferences. Proposed equivalents are proposals judged from general mathematical knowledge; none was checked against the literature.

Conventions. Line references are `chapter:line` in `manuscript/HumanizeYM_v3/chapters/` at commit `eb97dec6`; the commits that repaired damaged sentences after the survey kept the line numbers.

File abbreviations:
`12` = 12-ultraviolet-limit.tex; `13` = 13-continuum-fields.tex; `13sb` = 13-sharp-bounds.tex; `13ba` = 13-bounded-approximations.tex; `18gq` = 18-graded-quotient.tex; `18lp` = 18-lattice-products.tex; `14` = 14-reflection-ward.tex; `14lc` = 14-lattice-comparison.tex; `15` = 15-phases.tex; `15sp` = 15-sharp-phase-bounds.tex; `16` = 16-reconstruction.tex. Other chapters are consulted for definitions only, by grep and short excerpts: `1:` = 01-lattice.tex; `2:` = 02-observables.tex; `9:` = 09-renormalization.tex; `10:` = 10-common-trajectory.tex; `11:` = 11-marked-insertions.tex; `11R:` = 11-restarted-history.tex; `18:` = 18-operator-products.tex. `notation.md` = `blueprint/notation.md`. "Part II" is the dictionary of chapters 3–6.

Basis codes: D defined in text; R read off an explicit sentence or formula; I inferred; ? not determined. Categories: (a) accounting, (b) program/Lean leakage, (c) ordinary/standard word in unusual sense, (d) coined, (e) other.
Counts are occurrences from `grep -o -i` after stripping `\label/\ref/\eqref/\input/\cite` arguments and comment lines.

General observation. The accounting words `price, pay, purchase, budget, fund, receipt, ledger, portfolio, owner` do not occur in these files (grep: 0). `readout`, `table`, `tag`, `likelihood`, `compulsory`, `warning`, `seeded` also do not occur. What remains is (i) `cost`/`reserve`/`loss`/`request`/`supply` vocabulary, (ii) a large vocabulary inherited from chapters 2, 10 and 11 and not explained again here (graph, column, trial, attachment, section, incidence, mode, stage, history), concentrated in `12`, `13sb`, `13ba`, `18gq`, `18lp`, `14lc`, and (iii) coined analytic names in `14`–`16` (heat, damping, height, tied, padding, slab, whole word). Chapters `14` (after line 258), `15`, `16` are close to ordinary mathematical prose.

---

### 1. New terms (not in Part II)

#### 1.1 Renormalisation-group / marked-density vocabulary (ch. 12, 13 fragments, 18 fragments, 14lc)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| graph; admissible graph; remainder graph; output graph; terminal graph; selected graph; graph contraction | 12:37–39, 82, 89, 91, 94 (17 occurrences, all in `12`) | D at 12:82–83; used at 12:37–38 before the definition | A map `G: V_d → R_m` from labels to remainder arrays with `‖Gx‖ ≤ s_m‖x‖_1`: "An admissible graph $G:V_d\to\mathcal R_m$ obeys …". Linearity is not stated at 12:82; it is read off 11:379 ("incoming linear graph") and the formula `ΦG = J_G I_G^{-1}` (12:90–92). No sentence in `chapters/` explains the name. Probable reading: the remainder is represented as the graph `{(x, Gx)}` of a map over the coefficient space and `Φ` is the graph transform of invariant-manifold theory (12:94 "Graph contraction"); this is general knowledge, not in the text. | D (bound); linear R (ch. 11); name I | keep *graph*, with one explaining sentence ("the remainder is described as the graph of a linear map `G` over the coefficients; `Φ` is the graph transform"), subject to a mathematician's confirmation; otherwise *the linear map `G` from coefficients to remainders*. Not *remainder map*: the text uses that for `J_G` (12:91) and `R_G` (11:381). | c |
| fixed-input (cutoff) continuity; fixed-input comparison | 12:36, 41, 128, 133, 141 | D at 12:36–38 | "applying the cutoff-dependent marked map to any fixed admissible remainder graph gives Cauchy output graphs and coefficient maps" | D | *continuity in the cutoff at fixed argument* | b/d |
| coefficient map `I_G`; unreparametrized remainder map `J_G` | 12:90–91 | R | Named and given notation only; `ΦG = J_G I_G^{-1}`. "Unreparametrized" = before composing with `I_G^{-1}` (I). | R / I | *remainder map before renormalising the coefficient* | d |
| forgetting (the terminal graph) | 12:131 (printed title of a proposition) | no | Independence of the level-`m` graph from the graph inserted at level `m+h`, up to `2^{1-h}` (12:139–143). The title is the only occurrence of "terminal" in `12`, and which graph is "terminal" is not said. Two readings: the graph at the cutoff level `N` (the sense of "terminal" everywhere else, see §2.2), whose influence is what is forgotten; or the graph replaced at level `m+h` in the proof (12:139–140, which does not contain the word). | R (gloss); "terminal" I | *independence of the initial remainder map* (proposal; see "graph" for the noun) | c |
| stopping (level, scale, estimate, errors, data); stopped expression; sparse-stopping argument | 12:10, 225, 251, 302, 304; 13sb:85, 102, 137; 13ba:193; 18lp:159 (11 with "stopped") | R at 12:207–217 | Two senses. (1) Chapter 12: evaluating at an intermediate level `m` after setting to zero all terms with two or more source variables: "Keep the complete terms linear in the sources and set only these higher entries to zero" → `C_{N,p,m}` (12:212). (2) 13sb:85, 102, 137; 13ba:193; 18lp:159: the level `k = k(m)` at which the transfer is halted and the normalized chessboard bound is applied, "the first level $k\ge m$ with $B_k^2\le a_m/a_k$" (13sb:104); nothing is deleted there (13sb:9–11 "We keep all incoming joint marked components"). "Sparse" (18lp:159; 10:172 "a nearby sparse stopping scale") is not explained; probably the wide spacing of the anchors at that level (13sb:85–86). | R; "sparse" I | (1) *correlation with the terms of source degree ≥ 2 deleted at level m*; (2) *the level `k(m)` at which the bound is applied*. Not *truncated correlation* (the usual name for connected functions). Avoid "stopping" (stopping times). | c |
| dictionary (of local supports and inventories) | 12:23, 25 | no | A common index set of supports and large-field site sets used for all cutoffs `N>m` (cf. 10:376 "common dictionary"). | I | *common index set* | b |
| (large-field) inventory | 12:24, 239 | no | `blueprint/notation.md`: "prescribed set of large-field sites". Elsewhere already replaced by that phrase (12:27, 162). | R (notation.md) | *prescribed set of large-field sites* (two survivors at 12:24, 239) | b |
| large-field profile; grouped profiles; prescribed-site profiles; complementary profile | 12:26, 28, 78, 161, 180, 288 (10 in `12`); 13ba:165 | D at 12:26–27 | "the sum of activities having one particular support and prescribed set of large-field sites". "Complementary profile" (13ba:165) is not defined; 13ba:16 has "its complete bound, including the complementary large-field part", so it is the large-field part of a term. | D; 13ba:165 R (13ba:16) | *total large-field activity with given support and large-field set* | d |
| exact-cover gas; unmarked gas | 12:180; 18lp:186 | no | The sum over exact covers (Part II 2.4 "exact cover") of products of large-field activities: "a finite polynomial in the latter profiles and fixed eligibility indicators" (12:180–182). It is a function of the configuration and only one factor of the density: `ρ̃ = e^{-s}ρ` is its product with the exponential of the regular action, and `Z⁰ = ∫ρ̃ dμ` (12:172–183). "Unmarked gas" (once, 18lp:186) = the exact-cover gas without source variables (I). | R; unmarked I | *large-field polymer sum over exact covers*, *… without insertions*; or keep "exact-cover gas", defined once. Not *partition function*, which is the integral of the gas times the exponential of the regular action. | c |
| complete (remainder, source, bound, transfer, push, marked version) | 12:67, 115, 160, 208, 252; 13sb:65; 13ba 8×; 18lp:90; 15:184 (16) | no | Including both regular and large-field parts and (usually) all terms with ≥2 insertions: "the complete regular and large-field remainder on common supports" (12:115); "its complete bound, including the complementary large-field part" (13ba:16). | R | say what is included each time; *full* | c |
| terms linear in the sources; terms involving at least two insertions; higher (regular) entries; (joint, partial, incoming) modes; absolute mode sums | "linear in the sources" 19×; "at least two" 15×; "higher entries" 12:202, 209; "mode(s)" 13sb:73; 18lp:73, 74, 184, 245 | R at 12:200–209 | Coefficients of the monomials `z_S` in the nilpotent source variables; "mode" is the untranslated word (notation.md: "higher modes … Terms involving two or more insertions, indexed by the source monomial"). "Partial modes of a group" = monomials containing only some of the group's variables (I). | R; partial modes I | *coefficient of z_S*; *terms of source degree ≥ 2* (the text itself says "source degree" at 12:270). Use one phrase. | b |
| source weight(s); mark weights; marker weight / marker amplitude; residual weight `ϖ`, `ω^res`; available (product) weight `ω`; weight reserve; weight-reduction factors | 12:247, 281, 282; 13sb:72–75; 13ba:44, 124; 14lc:58, 61; 18lp:73, 84, 105, 128, 138, 168, 188 (≈25) | no | Positive numbers `w_i`, `ω` by which source variables are scaled in the marked norm, so that the coefficient of `z_S` is bounded by `1/∏w_i` (12:243–244; 11:812). "Marker amplitude $e^{2q}$" (14lc:61) appears to be the same weight (I; supported by notation.md:216 "source amplitude"). | R; marker = weight I | *weight of the source variable `z_i` in the norm*; one word | c |
| normalized local insertion | 13sb:53, 13ba:119, 174, 18lp:243 | no (notation.md:158 "primary source": "Normalized local insertion, with its local polynomial coefficient") | The canonical insertion density of a label, which is subtracted from a trial: 11:895 "Subtract one normalized local insertion density from the terminal trial, choosing its reference coefficient"; 13ba:119 "the negative normalized local insertion used in the subtraction". `ω_k = a_k^d β̂_k^{-w_d} E_k^{-1}` (13sb:58) is the weight attached to it (18lp:243 "The weights of normalized local insertions"), not part of its definition; 13sb:65 describes the multiplication by that weight. | R (ch. 11, notation.md) | keep, but define | d |
| column; coefficient column; column coefficient `x_l`; column map; inverse-column bound; prescribed column bounds `C_l`; trial / label / output / compensating / terminal / free column | 13:164; 13sb:15, 49, 75, 92; 13ba:13, 14, 109, 276, 278; 18gq:25, 92; 18lp:26, 40, 46, 48, 56, 64, 213, 305 (≈20) | no | The coefficient vector of the polynomial (local) part of a marked density, and the linear map on it: "A local degree-$t$ marked density consists of a column coefficient $x_l$ and a remainder" (18lp:26); "Invertibility of the column map" (18lp:47–48); 11:446 "column constant $s_f$. Thus $M_G$ is invertible". "Trial columns" = images of basis vectors (13ba:276). | R / I | *coefficient vector*; *coefficient map*; *bound on the inverse coefficient map* | b |
| inverse terminal coordinates; subpower inverse terminal coordinates | 13:159, 217 | defined in 11:1101–1102 | `‖X_i^{-1}z_i‖_1` (coordinates at the cutoff scale) bounded by a sequence subpower in `a_N^{-1}`. Not explained in ch. 13, whose two lines say only "subpower inverse terminal coordinates" without naming the variable. | R (ch. 11) | *coefficients at the cutoff scale* | b |
| admissible coefficient family / admissible coefficients | 13:215, 219, 239 | D in 11:1101–1102 | "Call a coefficient family $z_i$ admissible here if $\|X_i^{-1}z_i\|_1$ is bounded by a sequence subpower in $a_N^{-1}$" | D (ch. 11) | *family of subpolynomial growth at the cutoff scale* | c |
| trial; local trial; coarse trial `V_h`; protected trial construction; inclusion trial; trial descent; trial encoding; trial residual; trial columns | 13:229, 232, 239, 394; 13ba:12, 15, 24, 30, 48, 157, 213, 276; 18gq:105; 18lp:34 (14) | `V_h` D by formula 13ba:213–217; otherwise no | A candidate local observable at some level whose image under the block maps is compared with a normalized local insertion (11:891–896 "Subtract one normalized local insertion density from the terminal trial"). "Protected" (13:229) = with small-field cutoff (I, as Part II 2.4; 11:2306 uses "protected trial" without definition). "Trial encoding" (13:394) = the reference label `v_{N,p}` attached to a trial `F` by 11:943–951 ("a reference label $v_{N,p}$ with inverse terminal coordinates bounded by $2E_{N,p}$ and $\mathcal R_m\{F-O_{N,p}(e,v_{N,p})\}\le\ldots$"; 11:1074 "supplies the trial encoding"). | I; "encoding" R (ch. 11); "protected" I | *candidate observable*; *comparison of a candidate observable under the block maps* | d |
| equation space; (finite) equation kernel; equation comparison; equation inclusion; equation remainder | 13:14, 15–16, 157, 220, 394; 18gq:10, 110 | defined in ch. 11 (11:1089–1093) | `K_i = X_i P S_t R_e I_e`: the image at cutoff `(N,p)` of the ideal of labels vanishing on Maxwell solutions; `ker Π_{d,N,p}` (13:136–137). "Equation remainder" (18gq:110): 18gq:108–110 applies the argument of 13:195–203, where the remainder is `(x_u − Π_u x_u)/(1+‖Π_u x_u‖)`; 13:220 "Their difference lies in the exact finite equation kernel." | R (13:136; ch. 11) | *space of equation-of-motion labels*; *comparison of the two realisations of the equations of motion* | d |
| section; degree-`d` section; finite-section constants; section constant `C^sec`; global section | 13:234; 13sb:15, 60; 13ba:67, 75, 223 | D in 2:138–146 (notation.md: "finite-stencil section") | "A local polynomial section is a complex-linear map $P_d^{\mathrm{loc}}:V_d\longrightarrow$ {polynomial functions of finitely many link entries and their conjugates} with $\operatorname{Tay}_dP_d^{\mathrm{loc}}[c]=c$ … The term section simply means a right inverse of the Taylor map." Hence the map from polynomial labels to lattice observables: "its section is a fixed polynomial in compact group variables" (13ba:223; symbol `P_d^{loc}` at 13ba:217). Not recalled in these chapters. | D (ch. 2) | keep (*section* = right inverse is standard); recall the definition once. Gloss: *lattice representative of the label* | c |
| attachment; source / terminal / local / joint / complementary attachment (bound, estimate) | 13sb:63, 69, 73; 13ba:58, 62, 77, 78, 99, 123, 145; 18lp:148 (11) | no | Not defined in one sentence anywhere. Usage in chapters 9 and 11 fixes it as the joining of an insertion stencil or of a complementary (large-field) part to an existing support in the polymer expansion, and the sum over the places where this can happen: 9:687 "One additional unit of exponential support decay bounds the number of attachments"; 11:922–923 "Attach the latter to the original selected large-field factors"; 11:937 "$u_N>0$ the terminal attachment reserve"; 11:941 "the complementary attachment". The "attachment bound" `u_i` (13ba:61–62; "$u_i=\tfrac14\widehat\beta_i^{-1/2}$", 13ba:77) is that reserve. | I | none proposed; define once (*joining of an insertion or large-field part to an existing support*) | b |
| incidence norm / sum / bound | 13ba:69, 96, 171; 18lp:85, 86 (5) | no (11:258) | Sum over all terms containing a given insertion point ("insertion incidence sum at a fixed mark", 11:258). | R (ch. 11) | *sum over terms containing a given insertion* | d |
| rooted (activity norm, majorant sums, component estimates) | 12:178, 236; 18lp:214 | no | Sum over supports containing a fixed site ("Summing a rooted activity norm over the finitely many sites", 12:178). Same idea as Part II "containing-site bound". | I | *norm with one site fixed* | d |
| reserve (width, support, weight, exponent); "reserve four units"; room | 12:62, 126, 278, 282; 13ba:78, 144, 148, 153; 18lp:177; room 13ba:194 | no | Slack in an exponent kept to absorb later losses: "common bound at width $w>v$ … A strict width reserve" (12:48, 62). | R | *strict margin `w − v > 0`*; *we keep four units of the exponent* | a |
| request; finite (comparison, degree, threshold, admissible) request; lower-level request | 13:96; 13ba:100, 336; 18lp:103, 151; 14:224, 225, 227; 14lc:9, 79, 108; 15:207 (12) | no | Three uses. (1) A finite tuple of data (arity, degrees, window, error) for which constants or thresholds are then chosen: "All constants … are chosen for this one finite request" (14lc:9); 14:224–227; 14lc:79, 108. (2) A requirement placed on the schedule: "countably many finite degree requests to the single schedule of coupling thresholds" (13ba:100); 18lp:103, 151. (3) A prescribed lower bound on a level: 13:96; 13ba:336; 15:207. | R | (1) *finite set of data `(n, D, K, ε)`*; (2) *condition on the schedule*; (3) *lower bound on the level* | b |
| block floor(s) | 18gq:25; 18lp:41 | no | Lower bound imposed on the block ratio `L_l` ("above every stage floor", 10:55). | I | *lower bound on `L_l`* | d |
| first-below scale / choices; first-crossing levels; "first permitted such scale" | 13sb:145, 155; 18lp:21; 13:358 | R at 13sb:146–147 | "let $m(r)$ be the first level with $a_m<cr$". | R | *the first level with `a_m < cr`* | d |
| comparison depth; comparison level | 13:163–165; 14lc:23; 15:253 | no | The level `k` at which the Gaussian (free) comparison is made, `H_k=\exp((\log\log\widehatβ_k)^2)` (14lc:23–24). "Admissible comparison depth" (14lc:23) is undefined: "comparison depth" occurs without "admissible" at 13:163–164 and in ch. 11, and 11:884 defines an admissible comparison *coefficient*, not a depth. Probably a depth allowed by the schedule (I). | I | *comparison level `k`* (one word) | d |
| lift (coefficient lift `u_{k,N,p}`) | 14:172, 192, 210; 14lc:32, 41, 100; 15:256 | D by formula 14lc:32–34 | Solution of `S_{g/θ}T u = W_{H_k^{α_0}} v` for a free representative `v`. (A fourth sense beyond Part II 4.2.) | D | *preimage under the extraction map* | c |
| ancestor cone; cones; disjoint-cone identity; marked ancestors | 13ba:131, 181, 194, 232, 234, 241, 251, 270 | D at 13ba:232–233 | "The full ancestor cone of a stencil contains its fine-link reads and all these random variables at every intermediate level". It therefore contains the auxiliary random variables as well as links. | D | *domain of dependence* (proposal; Part II already has "dependence region") | d |
| (shared) frame seed; primitive random variables | 13ba:231, 247, 270 | R | The independent auxiliary random variables used for gauge choices ("independent primitive random variables for those choices"). | R | *auxiliary random variables* | b |
| group; grouping; merger; live group; representative (of a group); joining bound `h_l`; occupancy factors | 18lp:67–136 (group 12×, merger 4×) | D at 18lp:71–72 | "A group is a set of these marks with a common representative." "Live" (18lp:110) undefined (I: not yet merged). | D; live I | keep, define once | d |
| recentering | 18lp:42 | R | Subtracting the output column to restore a vanishing extracted coefficient (18lp:40–43). | R | none proposed (*renormalisation of the remainder* would mislead); keep, define as *subtraction of the output coefficient* | d |
| remainder with vanishing extracted coefficient | 18lp:27, 36, 40, 114, 115 | no | A term whose local polynomial part is zero; cf. 11:379 "vanishing-jet". For the regular part this is a zero radial Taylor polynomial through degree `t` (18lp:38); the large-field part has no Taylor characterisation there (18lp:39–40 "the large-field term retains half the suppression"). | I | *term with vanishing Taylor polynomial of degree t* fits the regular part only; for the whole object none proposed | e (translation residue) |
| low plane; low / high coordinates; low part | 18gq:53–54, 70–84, 94, 119 | R | `PV_t`, with `P` the projection onto scaling dimensions below `i` (18gq:51, 76). | R | *span of the basis polynomials of scaling dimension below `i`* | d |
| cell census `𝓘`; replica census; replica cells | 13ba:53, 173; 18lp:91; 15:261 | R (13ba:173) | The index set of reflected cells / the number of copies. | R / I | *set of cells*; *number of copies* | b |
| inspected (plaquette, stencil) | 12:186; 13ba:219, 250 | no | On which the function or its conditions depend. | I | *on which … depends* | b |
| "Open the centered cells at `m`" | 13ba:127 | no | Probably "start with the centered cells at level `m`": chapter 11 uses "opening" for the starting level of an estimate (11:1889 "at the opening level"; 11:1919 "At the opening all distinct sites …"). | I | *start from the centered cells at level m* | e |
| coordinate hybrids | 14lc:95 | no | Not determined; "hybrid" occurs nowhere else in `chapters/`. Guess: configurations obtained by rounding some coordinates to the grid and not others ("used in rounding"). | ? | resolve | d |
| the source construction | 14:186 | no | "For example the source construction uses $r_k=a_kM_k^{α_0}$…". The parameters are those of `14lc` with the generic sequence `M_k` (14:171) taken to be `H_k`: 14:187–189 against 14lc:26, 85–86. What is not determined is the word "source": the formal source of the monograph, or "the construction with source variables" (14lc:45 "corrected-source estimate", 14lc:53 "squarefree source polynomial"). | parameters R; "source" ? | *the construction of Section … (`14-lattice-comparison.tex`)* | b |
| corrected coefficients `R_I`; corrected-source estimate; corrected word; corrected moment estimates | 14lc:45–57; 15:17, 253, 258 (defined also at 11:2064–2070) | D by formula 14lc:48–52 | `R_∅ = 1`, `R_I = ∏_{i∈I} I_i − Σ_{∅≠J⊆I} G_J R_{I∖J}` with `G_J` the free moments: "These are precisely the coefficients of the actual squarefree source polynomial divided by the free moment polynomial … For the limiting Gaussian variables every nonempty coefficient has expectation zero." notation.md:216: "Corrected subset source". | D | keep *corrected*; possibly *Wick-ordered with respect to the free moments* (general knowledge, to be confirmed). Not *truncated* or *connected*. | d |
| corrected projection; corrected (physical) inclusions | 18gq:8, 110, 114 | no | The projection `Π_u x_u` of the normalized-null argument (13:195–203) and the maps `ι_{d,e}: F_d → F_e` of 13:263–264. "Corrected" is relative to the naive inclusion: "it is not the naive inclusion of unnormalized polynomials" (18gq:94–95; cf. 13:117–118 "the same formal polynomial in $V_d$ and $V_e$ can have different cutoff normalizations"). A second sense of "corrected", unrelated to the row above. | R | *the inclusions `ι_{d,e}`*; *the projection `Π`* | d |
| site conversion; support conversion cost `T_l`; root-to-site conversion | 13ba:145; 18lp:112–113 | no (ch. 9, 11) | Passing from a bound for supports anchored (rooted) at a point to a bound for supports containing a given site, at the cost of one unit of support decay: 9:513 "The conversion of anchored bounds to containing-site bounds"; 11R:141–142 "the extra unit used to turn an anchored bound into a site bound. These are the support conversions"; 11:1918 "Root-to-site conversion costs only $\mathcal W(B)$". `T_e=\exp(15^4(e+7))` is defined by formula at 11:233–238. | R (ch. 9, 11) | *passage from anchored to containing-site bounds* | d |
| (insertion, physical) origins | 12:22, 208, 230, 239, 279 | no | Positions of the insertions: "Fix finitely many labels … and distinct physical origins" (12:22); "All insertion origins belong to its support" (12:208). Synonym of "anchor" (§2.2). | R | *insertion points* | c |
| background convergence; background limits | 12:31, 41, 175 | R at 12:31–34 | "Cauchy convergence of $\beta_{N,p,m}$, of the path coefficients in their exponentially weighted sums, and of the regular and large-field activity arrays": convergence of the data without insertions. | R | *convergence of the action data* | d |
| normalized null condition / estimate; normalized-null (representative) argument | 13:192, 215, 240; 18gq:9, 108 | D by formula at 13:195–203 | The hypothesis `L_{i,u}((x_u − Π_u x_u)/(1+‖Π_u x_u‖)) → 0` for every `i`, together with `L_{i,u}(x_u) → t_i`, in a finite-dimensional lemma on convergent idempotents and functionals. | D | keep, with the display cited | d |
| microscopic | 18gq:10, 76, 84, 94, 97–98; 18lp:36 (7) | no | At the cutoff level `N`: "the exact microscopic equation space" (18gq:10); "this microscopic low plane" against "physical lower degrees" (18gq:94). Same as "terminal" (§2.2). | R (contrast at 18gq:94) | *at the cutoff level* | c |
| reference label / coefficient / insertion / limit; reference level | 18gq:12, 85, 106, 112; 13ba:200, 275; 12:23, 135 | no | A fixed label or coefficient, independent of the cutoff, against which the cutoff-dependent ones are compared ("a real reference coefficient $c$" 13ba:200; "a bounded reference limit" 18gq:112); "reference level" = the level at which coefficients are normalized (12:135). For "reference rows" see `row` in §3. | I | *fixed label*; *level of normalization* | d |
| raw (representatives, coordinate, replacement error, angular response) | 13sb:173; 18lp:318, 324–325; 14:777 | no | Before a correction or normalization is applied: "fixed raw representatives" (13sb:173); "raw replacement error", "each raw coordinate" (18lp:324–325). Which correction is meant has to be read from each context. | I | *uncorrected*, naming the correction | b |
| ordinary (norm bound, chart, derivative constant) | 13ba:15, 37 | no | Of the small-field part, as opposed to "complete": "$Q_h$ for the ordinary norm bound of a normalized local trial, and $E_h$ for its complete bound, including the complementary large-field part" (13ba:15–16). | R | *small-field* | c |
| endpoint estimate / comparison; fine end | 13ba:18, 34; 18lp:46, 63 | no | "The last-step endpoint estimate" (13ba:18): the estimate at the last level of the interval. "Fine end" = the finest level `k_*` of the interval `[k_*, m]` (18lp:46, 63). | I | *estimate at the last step*; *at the finest level* | d |
| vacuum normalization bound `q_r`; vacuum denominator | 12:247, 286 | no | "Vacuum" here is the insertion-free lattice integral `Z⁰`: the bound on, and the division by, the integral without sources. Not the vector `Ω` of chapters 14–16 (§1.2). | I | *bound on the normalization without insertions*; *denominator `Z⁰`* | c |
| grid (word, points, error, restriction, target, rounding); cofinal grids | 13ba:305–336; 18lp:225, 300, 327–342; 14:177–200; 14lc:29, 75; 15:178, 207 (20) | no | A lattice of spacing `s_k` in the rescaled variables, on which configurations are rounded ("$r_ks_k=a_k$: grid rounding occurs on the actual construction lattice", 14lc:29). Used alongside "lattice"; the two are the same set in different units at 14lc:29. | R / I | *lattice*, or define "grid" once | c |
| target (derivative target; grid target; target exponent) | 13:252, 260; 18lp:341, 344 | no | The statement or exponent to be proved in the current step. | I | *the required bound* | b |
| replacement (local replacement, replacement field `C_D(ρ,z)`, replacement error); reconstruction `𝒫_D` | 14:349, 353; 18lp:4, 220, 266–279, 282, 324 | D by formula in 18lp:266–279 (not re-read here) | Replacing a cluster of nearby insertions by a single field of `F_D` chosen through the fixed probes (14:353–355); `𝒫_D` rebuilds the field from its probe coordinates ("finite correlation reconstruction maps"). | R (14:353–355); 18lp from the audit only | keep, define once | d |
| positional (modulus, derivatives) | 14lc:92; 14:813–814, 841; 18lp:296 | no | With respect to the positions of the insertions, as opposed to the labels. | I | *in the positions* | c |
| signed (symmetry orbit; local transport; regular costs) | 14:26; 14lc:8; 13ba:60; 18lp:24, 65; 13sb:35 | no | Three uses: signed coordinate permutations (with reflections) (14:26; 14lc:8; 13ba:60 "signed symmetry orbit"); "with its sign kept" (18lp:24 "Signed local transport", 18lp:65 "The sign of the local difference has been retained throughout"); 13sb:35 "Signed regular costs" against "absolute". | R / I | say which | c |
| transitions (between stages); degree ceiling | 13sb:49; 13ba:81; 13ba:56 | no | The levels where the regularity stage `J(m)` changes; the maximal degree fixed before the schedule ("Fix the degree ceiling before the schedule"). | I | *where `J` jumps*; *maximal degree* | b |

#### 1.2 Continuum fields, reflection spaces, phases, reconstruction (ch. 13 main, 14, 15, 16)

| Term (variants) | Where | Defined? | Meaning and decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| ordered limit(s); ordered tails; cutoff tail; (coefficient, volume) refinement | ordered: 13 7×, 13ba 3×, 15 3×, 18gq, 18lp, 14lc; tail 23× | "ordered tails" D at 13:213–214; ordered limit R at 13:45–50 | `lim_k lim_N`. An ordered tail is a set of pairs (volume index, cutoff index) with the cutoff threshold depending on the volume, along the chosen sequences: "$p=P(k)$ with $k\ge k_0$, and $N=n(j)$ with $j\ge j_0(k)$" (13:213–214; the sequence `N=n(j)` is fixed at 13:140–143). "Cutoff tail" = all sufficiently large `N` (12:190, 249; 13sb:84). "Refinement" = subsequence. | D / R | *iterated limit*; ordered tail: *for all `k ≥ k₀` and all `j ≥ j₀(k)` along the chosen sequences*; cutoff tail: *for all sufficiently large N*; *subsequence* | d |
| separated (correlation, test function, configuration, response, bound, smearing) | 67× | "separated test function" D in 1:359; not in these chapters | At pairwise distinct points / supported away from coincident points: "A separated test function is an element of $C_c^\infty(\Conf_n)$, extended by zero" (1:359). 14:17–18 states the convention without the word ("evaluated at distinct points or against test functions supported away from collisions"). | D (ch. 1) for test functions; otherwise R | acceptable; recall the definition once | c |
| slot; one-slot response | 13:120, 132; 14:172, 220; 14lc:46; 15:115; 16:239 | R | Argument position of a correlation. | R | *argument*, *entry* | c |
| arity | 17× (13:39, 93, 330; 14:170; 16:120 …) | no | Number of insertions. | R | *number of points*, *n-point* | b/c |
| cell; centered (cell, scale, seminorm, chessboard estimate, tiling); interior; margin; strip count; residue patterns | cell 57×; centered in this sense ≈16; 13:81–90, 367–368 | R at 13:68–90 | Cell of a reflected tiling, the unit of the chessboard estimate; "centered" bounds hold when the insertion lies in a cell with margin `3a_k` (13:87–88) — never defined as a term. | R; centered I | keep *cell* (ordinary in chessboard estimates); *seminorm for an insertion at distance ≥ 3a_k from the cell boundary* | c |
| buffer; slab margins | 13:335, 348; 14:111, 151; 14:99 | D at 13:335 | "We call $r$ its buffer in the slab of width $h$" (pairwise separation ≥ r, times in `[r,h−r]`). 14:99 calls the same thing "slab margins". | D | keep *buffer* and use it at 14:99 as well; not *margin*, which already names the length `3a_k` (13:88) | d |
| exterior word; exterior spectator | 13:336, 349; 18lp:8, 286, 294, 308; 14:106; 15:244; 16:46; "exterior spectator" 14:354–355 | no | The word of remaining insertions on which `A_w`/`B_h(w)` acts or against which a cluster is paired; synonym of "spectator word" (14:722, 898; 14lc:43). | I | *spectator word* (one term) | d |
| slab; slab word; slab insertion; slab operator `B_h(w)`; reflected slab word `w^♯` | 14:83–141; 15; 16:35–37 (24×); used earlier at 13:335, 391 | D at 14:86–88, 97–104 | "A word $w$ lies in a slab of width $h$ if $0<x_i^\mu<h$". | D | keep; move the definition before 13:335 or refer forward | d |
| heat (semigroup, operator, energy, orbit, analyticity, damping, limit, pairing, intertwiner) | 14:80, 414, 435, 855, 858; 15 6×; 16 7× (18) | R at 14:39–56, 15:26 | `E(t)=e^{-tH}`, the self-adjoint contraction semigroup induced on the reflection Hilbert space by positive translations in the reflected direction: "On formal word sums put $T_tc=[\tau_tc]_\mu$ … The operators descend and extend to self-adjoint contractions $E_\mu(t)$ … $E_\mu(t)=e^{-tH_\mu}$" (14:39–56). In chapter 14 there is one for every coordinate axis `μ`, not only for time. The name is given only at 15:26 ("$E(t)=e^{-tH}$ for the heat semigroup"), after uses from 14:80 ("heat analyticity"). "Heat energy" (14:414) = spectral variable of `H`. No heat equation appears. | R | *the translation semigroup `e^{-tH}`* (in Osterwalder–Schrader reconstruction, the Euclidean time-translation semigroup with `H` the Hamiltonian; general knowledge); *energy*. Not *transfer semigroup*, which is not a standard term. | c |
| damping; undamped measure; damped moment | 14:416, 430, 435, 436, 489, 513, 752, 765 | "undamped measure" D at 14:416–419 | The factor `e^{-2uE}` produced by translating the insertion to time `u>0`; the undamped measure removes it. | D / R | *weight `e^{-2uE}`*; *spectral measure with the factor `e^{2uE}` restored* | d |
| coordinate half-space spectrum; coordinate spectral measures; word measures; mixed measures | 14:76, 410, 422, 424 | R | Joint spectral measure `P_μ` of `H_μ` and transverse momenta; "mixed" here = off-diagonal, obtained by polarization ("Polarization defines mixed measures", 14:424). | R | *joint spectral measure*; *the complex measures obtained by polarization* | d |
| (frequency) profile; transverse / temporal / annular / residual / dyadic / line profile | 14: 21× (448–764) | no | A function of one momentum variable used as a factor of a product test function in Fourier space. | R | *one-variable factor of the product test function in momentum space* (not *multiplier*, which suggests a Fourier multiplier operator) | c |
| annular correction `C_{m,ρ}`; residual (profile, response); sign transfer; mixed-sign estimate; spectral sign | 14:458, 465, 520, 526 (label), 531, 725, 748, 750; 447 | D by formula 14:458–471 | Subtraction of the first `2m` moments by Lagrange interpolation; `R_{m,ρ}f` its Laplace transform. "Spectral sign `ε_i`" (14:447) R. | D | keep the symbols; drop the names or define | d |
| conserved stress line; physical line; centered conserved line; orientation of the line | 14:258, 293–294, 308, 1019 | R | The one-dimensional kernel of the divergence on `𝒦` (14:294). | R | *the line `ker(div\|_𝒦)`* | d |
| line axis; line time axis; transverse-to-line axes | 14:497, 723, 731, 753–755 | no | The coordinate axis `e_l` carrying the spectators (14:711–712). | I | *the axis `e_l`* | d |
| shell factor; total (raw angular, shell) response; angular boundary / flux at infinity | 14:358, 410, 708, 777, 796 | no | `ρ^{3+ϰ}` (14:340, 358); the integral `−∫∂_μV_c S(J_{μc},A)` (14:777), which the text calls a "response", not a flux. | R | *the flux integral* (proposal) | d |
| Ward kernel; Ward normalization; spin operators | 14:821, 309, 903 | no | Common kernel of the vector correlation functionals in the mixed vector-map space (I); the constant `c_*` (I, 14:825–837); the generators `L(K)` (I). | I | state the object | c/d |
| phase | 52 (15: 21, 16: 19, …); used before the definition at 13:393; 13ba:5, 304; 18lp:7; 14:351, 371 | D at 15:8–9 | "A phase will be a character of a commutative operator algebra, not a set of gauge configurations"; `S^ξ(w)=ξ(M(w))`. notation.md warns against reading it as an extremal state. | D | keep (defined); see §3 for "phase space" | c |
| compression `M(w)`; compression algebra `𝔄`; ground algebra; compressed (whole words, operators, errors, product moments) | 15:10, 50–59, 91–93, 123, 155–156, 213, 267; 15sp:15 | D at 15:56, 93 | `M(w)=P_0B_h(w)\|_{H_0}`. "Ground algebra" (15:155) is the same algebra. | D | keep; one name for `𝔄` | d (compression is standard operator theory) |
| whole word; whole-word identity | 15:10, 129; 15sp:10 | no | `M` of the entire concatenated word, as opposed to a product of `M`'s of its parts (15:123–130). | R | *of the concatenated word* | d |
| cluster (of insertions); cluster limit; separated-cluster limit; cluster-separating ray | 18lp 11×; 14:352; 15 8×; 15sp:14 | no | A finite set of nearby insertions (18lp:222 "Let a cluster contain $n$ fields"); in `15` a word translated as a block. "Cluster limit" = (15:79–84). Not the Part II sense (subsequential limit), which survives at 13:206, 211 as "cluster point". | R | acceptable (cf. cluster property); define | c |
| generic (grid word, grid points, configuration); cofinal grids | 13ba:306, 311; 18lp:300, 342; 14:391; 14lc:75; 15:178, 207–208 | D at 15:178 | "generic real grid word $w$ (distinct projections in each coordinate)". | D | *with pairwise distinct coordinates in every direction* | c |
| coordinate ties; coordinate-equality strips | 14:179, 196, 206, 369 | R | Distinct points sharing a coordinate ("coordinate ties which are not collisions"). | R | *coincident coordinates* | d |
| height; gap; tied (heights, pair, gap); weakly / strictly ordered heights | height 19×, tied 7× in `16` | R at 16:48, 75, 85–89 | Height = imaginary part `y_j` of the complex time; gap = `y_{j+1}−y_j`; tied = equal. | R | *imaginary parts*; *differences*; *equal* | d |
| padding identity | 16:45, 64 | R at 16:40–41 | `B_{ε+u}=E(u)B_εE(u)`. | R | *the identity (…)* | d |
| letter; field word | 16:291–293, 322 | "letter" D at 16:291; "word" not defined there | "A letter is a pair $(A,f)$ with $A\in F$ and $f\in\mathscr S(\RR^4)$. The star of a word reverses its order and replaces every letter by $(A^*,\overline f)$. Let $\mathcal P$ be their algebraic span, including the empty word $1$." A word is thus a finite sequence of letters, a formal object; no product of operators is formed at this point. | D (letter); R (word) | keep. General knowledge, to be confirmed: `𝒫` with this star is the tensor (Borchers–Uhlmann type) algebra over `F ⊗ 𝒮`. | c |
| barycenter identity | 16:118 | no | Presumably `S=∫S^ξ dν` and its analytic continuation (16:88 "ν-average"). | I | *the integral representation (15:mixture)* | c |
| partial boundary | 16:225, 280, 554 | R at 16:226–231 | Boundary value in some imaginary directions only (`W_{n,Y}`, `Y∈C_n`). | R | acceptable | d |
| local charge `Q_K(f,c)`; (local) charge fields `p_b`, `Y_d(K)` | 14:312, 408; 16:464, 521–523, 535 | D (16:523; 14:376–379) | Two objects: linear maps on `F_d` (ch. 14) and smeared operators (ch. 16). | D | *generators `p_b`, `Y_d(K)`*; *smeared charge* | c |
| moment (= correlation) | 12:293 "actual cutoff moment"; 14lc:47 "free moment"; 15:213 "compressed product moments"; 14:898 | no | Correlation function `M_{N,p}(v;x)` (the symbol `M_{N,p}` is used at 12:262 without definition in this chapter). Exception: the "compressed product moments" of 15:213 are expectations `⟨Ω, M(w_1)⋯M(w_k)Ω⟩` of products of compressions, which are not correlations of a word (15:123 "Compression is not multiplication of finite-separation words"). | I | *correlation* at 12:293, 14lc:47, 14:898; not at 15:213 | c |
| unit; distinguished unit; unit vacuum | 13:58; 14:220, 283, 408, 974; "unit vacuum" 14:34, 15:25 | no | The identity field (the class of the constant polynomial 1): "The unit is fixed at degree zero" (14:220); "preserving reality and the unit" (14:974). In "unit vacuum" the adjective means "of norm one" (`Ω_μ=[∅]_μ`, 14:34). | R / I | *identity field*; *unit vector `Ω`* | c |
| vacuum | 14:34; 15:25; 16:446 | R | The vector `Ω = [∅]` of the reflection Hilbert space. A second sense, the insertion-free lattice integral, is in §1.1 ("vacuum normalization bound"). | R | keep for `Ω` only | c |
| zero-energy subspace; ground space (of the mixture); ground vector; ground projection | 15:7, 47–48; 16:379, 437 | R | `ker H` in the reflection Hilbert space of the undecomposed family, with projection `P_0` (in a phase: `Q_ξ`, 16:437). "This conclusion concerns the ground space of the mixture; it does not say that this space is one dimensional" (15:47–48). | R | *zero-energy subspace of the reflection Hilbert space*, adding *of the undecomposed family* where the mixture is meant | c |
| exceptional phases; the exceptional set | 15:325, 328, 339; 16:380 | R | The `ν`-null set of phases outside which `ker H_ξ = ℂΩ_ξ` is proved (15:320–326). The text does not show that non-uniqueness occurs there; uniqueness is later obtained for every phase (16:379–381, 446 ff.). | R | *the null set of phases on which uniqueness of the vacuum is not yet known* | d |
| mixed (correlation hierarchy, fields, reflection Hilbert space, mean) | 18lp:8; 14:12, 165, 349, 820; 15:24, 155, 277 (see §3) | no; "mixture" explained at 15:5–7 | Of the undecomposed family `S`, before decomposition into phases: "A translation-invariant correlation family can be a mixture of states with different long-distance behavior" (15:5–6). Used from 18lp:8 and 14:12 before that sentence. | R | *of the undecomposed family `S`* | c |
| scalar heights; scalar imaginary gaps; scalar operators; scalar corrections | 16:218, 248; 16:481; 14:283–284 | no | Three uses beside the Part II sense (constant term of the exponent): purely time-directed imaginary parts (16:218 "strictly ordered scalar heights", 16:248 "positive scalar imaginary gaps"); multiples of the identity (16:481); the two constants subtracted in centering (14:283–284). | I / R (16:481) | *imaginary times*; *multiples of the identity* | c |
| collision orders; Ward sum; vector-map space; defect space | 14:519, 579, 611; 14:812, 841, 901, 917; 14:817, 820; 14:937 | no | Not examined beyond the occurrence of the phrases: orders of the singularity at coincident points (I); the sum over insertions in a Ward identity ("the translation Ward sum for $p_b$", 14:812); a finite-dimensional space of linear maps into vectors on which the correlation functionals are injective (14:817–820); the space of "internal defects" (14:932–937). | I | state the object each time | d |

---

### 2. Part II terms: same sense / new sense / clarified

#### 2.1 Same sense

| Term | Where here | Note |
|---|---|---|
| atom (of degree q) | 12:60 | same (elementary path term of degree q) |
| width (decay rate of path coefficients) | 12:48, 62, 126 | same as 4.2. New senses in §3. |
| walk | 12:54; 14:546 | path; 14:546 is a walk through an index set |
| scalar; scalar normalization | 12:34, 166, 170; 13sb:26, 29; 13ba:164, 219 | same (constant term of the exponent); "scalar part" of a polynomial = coefficient of the identity (13ba:164) |
| regular / large-field activities; activity arrays; array | 12:33, 70–77; 13ba:151–152 | same |
| exact cover | 12:180, 188 | same |
| (relaxed) small-field condition | 13ba:220 | same, already translated |
| smoothing order `j_i`; connector; frame (gauge frame) | 13ba:229–248 | same; 13ba:244–245 restates the radius without the Part II word "macro-box" (which occurs in none of these files): "each endpoint frame reads a box of fine-lattice radius $(j_i+3)L_i$" |
| reads / fine-link reads | 13ba:232, 244 | same ("depends on"); note the noun "reads" |
| stencil | 12:345, 362, 389, 390; 13:236; 13sb:138; 13ba:216–250, 297; 18gq:102 | same as "footprint/stencil"; in `12` it is a finite-difference stencil (standard) |
| incoming / outgoing | 13sb:10, 72; 13ba 6×; 18lp 4×; 14lc:60 | same |
| supplies / supply | 20× (12:14, 40, 42, 353, 354 …) | same ("gives"). Lemma name "coarse-residual-supplier" survives in a label (13ba:49). |
| inputs | 15:12, 32, 338; 16:27, 332; 13:391 | same ("hypotheses") |
| spectator | 33× (13: 10, 18gq: 2, 18lp: 3, 14: 15, 14lc: 1, 16: 2) | same (remaining insertions). Never defined in these chapters. |
| collision | 12:402; 14:18, 206, 369; 15:245; 16:27 | same |
| flux; shell | 14:318–328, 373; 16:538, 558 | same; `𝒬^J_v` defined at 14:318 |
| internal defect | 14:932–933 | same (the passage Part II cites) |
| cluster point | 13:206, 211 | same as "cluster limit" (subsequential) |
| subpower | 13:159, 217, 235; 13ba:18; 18gq:103; 18lp:18, 257 | same; see 2.3 |
| cost; loss; excess; margin | see §3 | same family as Part II 2.6 |
| coupling threshold | 13:237; 13sb:16, 41, 45; 13ba:39, 50, 83, 101, 258, 261; 18lp:101, 148; 14lc:69 | same as 4.2 ("for β̂ sufficiently large"); ch. 10 says "inverse coupling threshold" |
| eligibility (criteria, indicators, event, conditions) | 12:25, 181; 13sb:72; 13ba:249 | sense (ii)-like: conditions attached to activities (9:94 "large-field indicators in their eligibility criteria"). I. |
| protected | 13:229 | presumably same (with cutoff); I |
| detection / detecting | 13sb:9 "rank detection"; 14:221 "detecting families" | same (nondegeneracy). Elsewhere replaced by "separating family" (13:14, 395; 14:386, 832; 15:17, 250, 256); "detector" survives only in labels. |
| probe | 18gq:131; 18lp:269, 293, 321, 332; 14:354 | a different object from the Part II one: see 2.2 |
| physical (continuum units) | 16 (12:5, 22, 230, 352 …) | same as 4.2 "physical spacing/period"; new senses in §3 |

#### 2.2 New senses of Part II words

| Word | New sense here | Where | Basis |
|---|---|---|---|
| response | "one-slot response" `L_{v,f}(c)=∫ f S_{n+1}(c(x_0),v(x))`: a smeared correlation as a linear functional of one label | D at 13:120–122; 13 10×, 18gq 3×, 14:406, 992 | D |
| response | two objects: the Laplace transform `𝓛f(E)` of a frequency profile and its corrected form `𝓡_{m,ρ}f(E)` ("its exact response"), functions of `E`; and the integral of that function against the spectral measure, the number `Resp_i(g)` | functions: 14:450–451, 465–470, 531, 688, 697, 740, 761; numbers: 14:503–505 (D by formula), 654, 672 | D / R |
| response | the integral `−∫∂_μV_c S(J_{μc},A)` over the shell ("total raw angular response", "total shell response") | 14:777, 796 | R |
| transport | (i) transfer of a marked density or coefficient down the levels by the block maps (12:277; 18gq:13, 76, 84; 18lp:24, 47, 197, 216); (ii) conjugation by the comparison maps `U_{k,d}` (14:229, 302, 946) and application of `U_{k,d}` to a field array (14:281, 282); (iii) "carries over" (14:819) | lines as given | R / R / R |
| anchor | position of an insertion to be placed in a cell | 13:83, 86, 89; 13sb:85, 157, 159 | R |
| probe | a fixed word of exterior insertions whose correlations with a field give coordinate functionals on `F_D` (18:38 "A probe is a fixed word $v$ at distinct nonzero positions"). Probes occupy cells (18lp:332 "using fixed cells for exterior probes") and are chosen before the spectator (14:354); the coordinates are "finite linear combinations of separated probe correlations" (18lp:268–269), which are not themselves the probes | 18gq:131; 18lp:269, 293, 321, 332; 14:354 | D (18:38) |
| label | element of the quotient `F_d` or of `F` (a field), not a polynomial in `V_d` | 14:26, 98, 147 …; 15; 16 (see §3) | R (14:147) |
| word | Euclidean word (D 13:282) and field word, a finite sequence of letters (16:291–294; "letter" is defined there, "word" is not); see §3 | | D / R |
| row | member of a finite list of coefficient vectors (13:159 "bounded rows"; 11:2253 "The rows $(I-\Pi_i)u_{j,i}$ are bounded, hence admissible"); "reference rows", probably the rows of the matrix of correlation pairings of 15:288–289; see §3 | 13:159; 15:275, 278 | R (ch. 11); reference rows I |
| window | compact set `K` of separated configurations | 14:173, 197, 226, 237; 14lc:6, 97 | R (14lc:6) |
| representative | representative point of a group of marks | 18lp:72, 79, 93–95 | D-ish |
| charge | smeared operator `Q_K(f,c)` | 16:523 | D |
| centered | placed inside a cell with margin; zero expectation (D at 14:263; also the verbs "center", "centers" 14:281, 283); see §3 | | |
| cutoff | "outer cutoff" = `N` (13ba:53, 221); "level-`m` cutoff" = small-field threshold (12:187); "cutoff threshold" = the `N_0` beyond which a bound holds (12:265; 13:27, 388); smooth cutoff function (≈17: 13ba:36, 165; 14:252, 324, 328, 347, 396, 614, 620, 625, 736; 16:205, 232, 235, 283, 459, 539) — at 14:324 "independent of the cutoff" is the function `χ`, not `N` | lines as given | R |
| terminal | at the cutoff level `N`, or at the last level of the history considered: "inverse terminal coordinates" 13:159, 217; "terminal column" 13sb:92; "terminal attachment bound" 13ba:61, 77; "its terminal source satisfies the joint attachment bound at $N$" 13ba:123; 13ba:153, 174; 11:895 "the terminal trial". For "terminal graph" (12:131, title only) see §1.1 "forgetting" | 9 occurrences | R (13ba:123); 12:131 I |
| request | three uses; see §1.1 | | R |
| lift | coefficient lift (see §1.1) and "bounded lifts of the separating family" (15:256): a polynomial preimage of a free field | 14:172; 14lc:32; 15:256 | D / R |

#### 2.3 Open items of Part II clarified by these chapters

| Part II item | What these chapters add |
|---|---|
| regularity-stage index `J_m` (§4) | Resolved outside my files, used inside them. 10:25: "A stage $j\ge1$ specifies finitely many derivative orders, support exponents, path widths and coefficient bounds"; 10:133 `J(m)=j` for `A_j≤m<A_{j+1}`; 10:808 "$J(m)$ is the stage at scale $m$". Used as `C_{J(i)}`, `J(k)` at 13sb:28, 57; "When $J(i+1)=q>1$" 13ba:262; "stage" 22× in my files. Basis D (ch. 10). Proposed: *regularity class j* / *parameter set j*. |
| subpower (2.6) | Defined locally at 18lp:18: "A factor $e^{o(T)}$ is called subpower in this paragraph"; with 18lp:15–17 `f ≼ e^{cT}`. 13:159, 217 say "subpower inverse terminal coordinates" without naming the variable; the definition behind them is "subpower in $a_N^{-1}$" (11:1101–1102), and 13ba:18 has "subpower in $a_h^{-1}$". D. |
| history; schedule (2.1) | "History" is defined at 11:18–19: "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations." Here it is used for that choice at a given cutoff, i.e. the sequence of renormalisation steps started at one cutoff, not for the list `(L_h, j_h)`: "the history restricted from the actual cutoff $N$" (13ba:31–32); "selected histories" (plural, one per cutoff) 13ba:50, 200, 304; "on the same history" 18lp:48; "actual histories" 18lp:229. Basis D (ch. 11); "one per cutoff" R. "Schedule" = the fixed choice of block ratios and coupling thresholds (13sb:16–23, 50–51; 13ba:101, 256–262; 18lp:20) — R, consistent with Part II. |
| moving comparison fields (§4) | Partial. "Moving" here means depending on the sequence index: "convergent moving labels … handled by expansion in fixed finite bases" (14:238, 250); "moving test functions" (13:295, lattice-dependent). Supports the reading "cutoff-dependent" but does not define the ch. 3 phrase. I. |
| seeded sector / unseeded law (§4) | Not clarified. 13ba:247, 270 "shared frame seed(s)" are the auxiliary random variables for gauge choices; whether this is the same "seed" is not determined. |
| marked (4.2) | Confirmed and sharpened: 12:200–206 gives the structure of "the exact marked density" (polynomial in nilpotent `z_i`). See §3 for `mark`. |
| event label / indicator (4.2) | 12:25, 163–164 "fixed Borel event indicator … no continuity of the event indicator as a function of $U$ is required" — consistent with Part II 1.4 (indicator, not smooth). |
| centered log determinant, compulsory, Warnings, output anchors, likelihood tests | No occurrence, no information. |

---

### 3. Multi-sense words (all occurrences classified)

**row** (8). (a) quadratic path term of the action, indexed by a displacement and summed over `x ∈ ℤ⁴`: 12:55 ("For a row their length is $|x|_1+4$", contrasted with "an atom of degree $q$") — the Part II kernel sense (cf. 10:354 "quadratic rows"), I; 1. (b) literal matrix row, each row being a correlation functional: 13:168, 182; 14:277; 3. (c) member of a finite list of coefficient vectors: 13:159 ("bounded rows have uniformly subpower inverse terminal coordinates"), restating 11:2253 "The rows $(I-\Pi_i)u_{j,i}$ are bounded, hence admissible" — R (ch. 11); 1. (d) "row constant", "free row moments" (15:275), "finite reference rows use fixed free labels" (15:278): probably the rows of the matrix of correlation pairings of 15:288–289, a reference row being a fixed free word whose correlations give one row; the text does not say so, and if this is right (d) is the same sense as (b) — I; 3 (two on 15:275). None unclassified.

**actual** (20). (a) "of this construction", emphatic, as opposed to a generic or model object: 12:63, 75, 118, 119, 169, 252; 13:162; 18lp:12; 14:15, 168, 332, 971; 14lc:29, 53 — 14. (b) the sequence produced by the construction as opposed to a substituted one: 12:143 ("actual graphs" vs the fixed admissible graph), 12:293 ("actual cutoff moment" vs the stopped expression) — 2. (c) belonging to cutoff `N`: 13ba:32, 18lp:229 — 2. (d) the true function as opposed to the model solution `Q`: 14:868, 869 — 2. The Part II senses "nonlinear/at the true background" and "running coupling" do not occur. Almost all of (a) can be deleted. Borderline: 18lp:229 ("on the actual histories") reads equally as (a); 12:118 ("actual inserted density") contrasts the complete density with its regular part; 13:162 and 14lc:53 contrast the interacting object with the free one.

**selected / select / selection** (23 with "Selecting"). (a) fixed by the construction of ch. 10 (trajectory, schedule, ratio, history): 12:123, 133, 298, 370; 13:307; 13sb:50; 13ba:17, 50, 195, 200, 304 — 11. (b) the continuum family obtained along the chosen subsequence: 13:172, 395; 15:257 — 3. (c) literal choice of a subsequence: 13:6, 7, 143 — 3. (d) the graph produced by the trajectory: 12:134, 139 — 2. (e) other fixed choices: 13sb:136 (stopping level), 13ba:30 ("selected level-$h$ polynomial coordinates", I), 18lp:328 ("selected coefficients of $A_t$", obtained by a refinement) — 3. Also "Selecting a phase" 15:301 (literal choice of `ξ_*`). `chosen` is used as a synonym of (a)/(b) at 14lc:101, 109. Two assignments are uncertain: 13:395 ("all refer to the same selected family") lists lattice estimates and may be sense (a) (parallel passages say "the same lattice family", 15:250–251); 13ba:30 is most simply "on the selected history", again sense (a).

**test** (47). (a) test function: 13:43, 44, 109, 119, 193, 242, 291, 295; 14:17, 197, 224, 507, 510, 612, 614, 766; 16:92, 94, 154, 162, 171, 177, 215 ("the tested function", the argument of the distribution), 282, 295, 311, 358, 362, 385, 459 — 30. (b) "test against" = pair with all spectators / exterior words / word vectors: 13:272; 18lp:307, 310, 320; 15:243, 248; 16:46 — 7. (c) "tested"/"testing" = smeared with a test function or paired with fixed spectators: 18lp:218 ("one tested mean"), 330; 14:207 ("Testing against each fixed $f$ separately", integration against a test function), 242, 1016; 16:87, 117, 150, 151, 300 — 10. The ch. 4–6 senses (condition, variable, location, indicator) do not occur; all uses comply with notation.md except that (b)/(c) should name the pairing.

**label** (59); **tag** 0. (a) polynomial label in `V_d` (Part II sense): 12:22, 147; 13 (16×); 13sb:176; 13ba:312; 18gq:13, 48, 85, 96, 106; 18lp:17, 228, 295, 303; 14lc:7 — ≈30. (b) element of the quotient `F_d`/`F`, i.e. a field: 14:26, 98, 101, 147, 658, 842, 864, 879, 980, 991, 1025; 15:109, 119, 178, 316; 16:19, 20, 36, 83, 132, 153, 260, 369, 373, 515, 520 — ≈26. (c) sequence-dependent label: "moving labels" 14:238, 250; "free labels" 15:278 (free field space) — 3. (d) "the field labeling is faithful" 16:345: the map `A ↦ Φ_ξ(A,·)` — 1. notation.md:150 requires (a) and (b) to be distinguished ("distinguish from quotient field"); from ch. 14 on they are not. Not decidable from the text between (a) and (b): 13:282–285 (labels of a "word", stated after the quotient is defined), 18lp:295, 14lc:7 ("finite label list"), 13sb:176; 15:278 ("fixed free labels") is filed under (c).

**mark / marked / marker** (53). (a) "marked" = carrying source insertions (density, step, estimate, norm, transfer, remainder, construction): 12 15×; 13sb:10, 26; 13ba:11, 44; 18gq:7, 24, 55, 70; 18lp:26, 42, 79, 90, 126, 210, 245; 14:16, 168, 191, 971 — ≈34. (b) "mark" = one insertion point: 18lp:67, 71, 72, 80, 86, 127, 183, 215; 13ba:131 ("marked ancestors"); 15:252; "two-mark" 14:332, 15:260 — 12. (c) "mark weights" 13sb:72; "marker-weight", "marker amplitude" 14lc:58, 61 = source weights — 3. (d) symbol `δ^mark` 18lp:142, 192 — 2. Also "unmarked" 18lp:89, 186.

**window** (6). One sense, compact set of separated configurations: 14:173, 197, 226, 237; 14lc:6; "physical windows" 14lc:97 (unrescaled, I). The ch. 6 sense does not occur.

**history** (7): see 2.3; all 7 in the sense "renormalisation sequence at a given cutoff" (13ba:31, 50, 195, 200, 304; 18lp:48, 229).

**source** (49). (a) nilpotent source variable / "in the sources": 12 (14×), 13sb:11, 66, 67; 13ba (9); 18lp:9, 69, 210; 14lc:53, 57 — 31. (b) the inserted observable itself as a density ("complete source", "terminal source", "pushed negative source", "physical source (density)", "incoming source term"): 13sb:65, 72; 13ba:123, 158, 284; 18lp:29, 180 — 7. (c) source weight: 12:247, 281; 13ba:44; 18lp:73 — 4 (+ §1.1). (d) "source attachment", "source constants", "corrected-source estimate": 13sb:15, 63, 73; 18lp:148; 14lc:45, 69 — 6; "pertaining to insertions". Of these "corrected-source estimate" (14lc:45) is settled by 14lc:48–55: the estimate for the corrected coefficients `R_I` (§1.1); "source attachment" is the attachment of §1.1. (e) "the source construction" 14:186 — 1; the construction is that of `14lc`, the word "source" is unclassified (§1.1, §4).

**price / pay**: 0. **cost** (25). (a) multiplicative factor lost: 18lp:41, 64, 85 (a combinatorial factor, "at most $(1+\mathfrak N)n$ assignments per representative", 18lp:88), 110, 113, 119, 178, 210, 212; 14:500, 589; 14lc:82; 13:237 — 13. (b) additive loss in an exponent or logarithm: 13sb:37; 14:757; 15sp:23; 18lp:107 — 4. (c) an error term: 14:199; 18lp:343 — 2. (d) a named bound: "per-site normalization cost `q^site`" 13sb:25, 112, 18lp:163; "normalized cost at most `ζ_h`" 13ba:120; "cost `q_fin`" 18lp:56; "Signed regular costs" 13sb:35 (cf. 11:789 "absolute action cost per site") — 6. **reserve** 9, **loss/lose** 7, **excess** 5 (all = the `ε` above the sum of degrees: 13sb:7, 164; 18lp:334; 15sp:6, 24 — a different use from Part II `Δ_p`), **margin** 14 (geometric distance to a cell boundary 12×; strict inequality margin 18lp:257, 16:201).

**detector**: 0 in prose (labels only); **detection/detecting** 2 (13sb:9; 14:221).

**probe** (6): one sense, a fixed exterior word whose correlations realise coordinate functionals (§2.2): 18gq:131; 18lp:269, 293, 321, 332; 14:354.

**response** (25): one-slot response 15 (13:9, 10, 120, 151, 152, 161, 177, 183, 210, 265; 18gq:111, 113, 130; 14:406, 992); spectral/Laplace response 8, of which 6 are a function of `E` (14:465, 531, 688, 697, 740, 761) and 2 a number (14:654, 672; cf. the display `Resp_i(g)` at 14:503); shell integral 2 (14:777, 796). None in the four senses of Part II.

**transport** (14): RG transfer 8; comparison maps 5 (conjugation 14:229, 302, 946; application to a field array 14:281, 282); "carry over" 1 (lines in §2.2). No parallel transport.

**frame** (4): gauge frame, 13ba:230, 241, 244, 247.

**anchor** (6): insertion position (§2.2).

**readout, table**: 0.

**phase** (52). (a) a character `ξ` / the correlation family `S^ξ` (D 15:8): nearly all. (b) "the compact phase space `Ξ`" 16:15: the character space (15:136 "the space of unital star characters of $\mathfrak A$") — collides with the standard meaning of "phase space". (c) attributive "phase X" = X built from `S^ξ` (phase reflection space, phase slab operators, phase pair, phase matrices, phase measure `ν`, phase continuity = continuity in `ξ`, 16:112). No other sense.

**word** (≈96). (a) Euclidean word, "a finite list of labels and positions" (D 13:282; "positive word" D 14:23): all of 13, 13ba, 18lp, 14, 14lc, 15, 15sp (71) and 16:46, 365, 555. (b) field word, a finite sequence of letters `(A,f)` ("letter" D 16:291; "word" itself is not defined there, and no product is formed): 16:10, 288–323, 348–351, 385, 458, 468, 484–485 (≈20); at 16:485 "For a word $A$" the letter `A` denotes a word, elsewhere a field. (c) "formal word sums" 14:39, 94 = formal linear combinations of (a). The Part II senses (holonomy; Neumann term) do not occur.

Further multi-sense words found:

- **centered** (24): (i) insertion well inside a cell — "centered scale/cell/seminorm/tiling/chessboard estimate" 13:87, 98, 301, 314, 346, 361, 372, 382, 395; 13sb:102, 121, 159; 13ba:28, 127, 201, 312 (16); (ii) zero expectation, D 14:263: 14:261, 263, 302, 1004, 1019 (5), and the verbs "Center", "centers" at 14:281, 283 (not counted); (iii) centered difference: 12:389; 14:432 (2); (iv) "centered level-(m+1) block" 18lp:224 (1): a block centred on a site, as in 1:217 "Odd block ratios give centered blocks" — R (ch. 1).
- **physical** (31): (i) in continuum units (16); (ii) carrying the factor `a^{-d}`: 13ba:7, 71, 122; 18gq:99; 18lp:29, 180, 200 (7); (iii) of the interacting continuum theory as opposed to free or microscopic: 18gq:2, 8, 94, 112; 14:212, 291, 308 (7); (iv) "physical Hilbert space" 14:1026 (1).
- **mixed** (23): (i) of the undecomposed mixture `S` ("mixed correlation hierarchy" 14:12; used at 18lp:8 and from 14:12 before 15:5 explains "mixture"): 18lp:8, 263, 282, 350; 14:12, 165, 263, 349, 820, 946; 15:24, 155, 248, 277, 329; 15sp:5, 8; 16:88 (18); (ii) off-diagonal, obtained by polarization: 14:424; 16:360 (2); (iii) of both signs: 14:658, 725, 750 (3).
- **column** (22): coefficient vector/map (≈20, §1.1); column of a figure 13:51; column of the exponent table 14:795.
- **cone** (17): ancestor cone 13ba (7); cone condition in a recursion ("The cone calculation" 18lp:48; "The cone $32(1+C_l)^2U\le r_l$" 18lp:61) (2); spectral/forward cone 14:76, 804; 16 (8).
- **admissible** (15): graph (D 12:82) 7, including "admissible remainder graph" 12:37, which is used 45 lines before the definition; coefficient family (D 11:1101–1102) 13:215, 219, 239; period cell 12:375 (D in 1:359–361: a separated test function "is admissible at volume $p$ if its support is contained in $((-R_p/2,R_p/2)^4)^n$"); undefined: majorant 12:80, trial encoding 13:394, path-action representation 13sb:27 (Part II 2.3), bounds 13sb:36, request 18lp:103, comparison depth 14lc:23.
- **threshold** (≈30): coupling threshold (≈14); small-field threshold 13sb:62, 13ba:75, 18lp:179; cutoff/convergence threshold (an `N_0`) 12:265, 395; 13:27, 388; 13sb:139; "approximation / translation thresholds" 13ba:307; 15:262.
- **width**: path-coefficient decay rate (12:48, 62, 126); slab width `h` (14:86 ff., 15:53); width of a frequency profile and "width exponents" (14:550–665).
- **degree**: filtration degree `d` of `V_d`/`F_d`; "source degree" 12:270; "radial degree" 18lp:173; "degree of the Killing field" 14:347; 18gq:19 warns "scaling dimension …, not its factor count".
- **stage**: regularity stage `j` (22); idiom "at this stage" 14:65, 15:324.
- **extraction**: coefficient / Taylor / polynomial extraction (12:240; 18lp:138–186; 14lc:30, 57) vs subsequence extraction (12:400; 13:15, 31, 42).
- **mass**: measure-theoretic (12:190; 14:422, 760, 764; 15:326; 16:387, 440); "mass gap" 16:383; norm bound of incoming terms ("incoming mass $\mathfrak m$", "total mass $p_l$", "normalized mass $f_l$") 18lp:115–116.
- **profile**: large-field profile (ch. 12) vs frequency profile (ch. 14) vs "complementary profile" (13ba:165).
- **residual**: trial residual / residual coefficient (13ba, 18lp) vs residual profile after moment subtraction (14:520–748) vs replacement error (18lp:307–336; 14:355).
- **comparison** (47): equation comparison, Gaussian/covariance comparison, local-trial comparison, adjacent comparison, interior-cell comparison, comparison maps `U_{k,d}`, smooth comparison, comparison cells/level/depth/labels/matrix/sequence — at least six distinct objects.
- **stopping**: two senses (deletion of the terms of source degree ≥ 2 at level `m` in ch. 12; the level at which a bound is applied, with nothing deleted, in 13sb, 13ba, 18lp); see §1.1.
- **request** (12): three uses; see §1.1.
- **cutoff** (66): the ultraviolet cutoff `N` (most uses); small-field threshold; a smooth cutoff function (≈17); see §2.2.
- **terminal** (9): at the cutoff level `N` (8); "terminal graph" in the title 12:131 (1, reading open); see §2.2.
- **vacuum**: the vector `Ω` of the reflection space (14:34, 15:25, 16:446) against the insertion-free lattice integral ("vacuum normalization bound" 12:247, "vacuum denominator" 12:286).
- **scalar**: constant term of the exponent (§2.1) against purely time-directed imaginary parts (16:218, 248), multiples of the identity (16:481) and the constants of 14:283–284.
- **gap**: time separation between words (14:731 "a genuine temporal gap", 15:76); difference of heights (16, ≈15); spectral gap (15:340; 16:383 "mass gap").
- **corrected**: with the free moments divided out (14lc:45; 15:17, 253, 258) against "corrected projection / inclusions" (18gq:8, 110, 114); see §1.1.
- **signed**: signed coordinate permutations and reflections (14:26; 14lc:8; 13ba:60) against "with its sign kept" (18lp:24, 65) against "Signed regular costs" (13sb:35).
- **lift**: coefficient lift `u_{k,N,p}` (14:172; 14lc:32) and "bounded lifts of the separating family" (15:256), both polynomial preimages of free fields; a further sense beside those of Part II 4.2.
- **unit**: the identity field (13:58; 14:220, 283, 974) against "unit vacuum" = vector of norm one (14:34; 15:25) against units of support decay or of an exponent ("reserve four units").

---

### 4. Terms the chapters do not determine

#### 4.1 Not determined by any chapter consulted

| Term | Where | What can be said |
|---|---|---|
| coordinate hybrids | 14lc:95 | Undetermined; no other occurrence of "hybrid" in `chapters/`. Guess: configurations with some coordinates rounded to the grid and others not. |
| admissible comparison depth | 14lc:23 | "Comparison depth" is used without "admissible" at 13:163–164 and in ch. 11; 11:884 defines an admissible comparison coefficient, not a depth. Guess: a depth allowed by the schedule. |
| protected trial (construction) | 13:229 | 11:2306 uses "protected trial" without definition. Guess: with small-field cutoff. |
| "source" in "the source construction" | 14:186 | The construction is that of `14lc` (same parameters with `M_k = H_k`). Whether "source" names the formal source of the monograph or the source variables is not stated. |
| why the map `G` is called a "graph" | 12:82 | No sentence in `chapters/` says. Probably the graph-transform usage of invariant-manifold theory (§1.1); general knowledge. |
| "terminal" in "Forgetting the terminal graph" | 12:131 | The graph at the cutoff level `N`, or the graph replaced at level `m+h` in the proof; the text does not say (§1.1). |
| selected level-`h` polynomial coordinates | 13ba:30 | Which coordinates are "selected" is not said; most simply "on the selected history" (I). |
| seeded / unseeded; centered log determinant; compulsory; Warnings; output anchors; likelihood tests | — | No occurrence in these files. |

#### 4.2 Not explained here, determined by other chapters

| Term | Where | Meaning and source | Basis |
|---|---|---|---|
| attachment (source, terminal, local, joint, complementary) | 13sb:63, 69, 73; 13ba:58–145; 18lp:148 | Joining of an insertion stencil or a complementary large-field part to an existing support, and the sum over the places where it can happen; `u_i` is the attachment reserve (9:687; 11:922–923, 937, 941). No one-sentence definition exists. See §1.1. | I |
| sparse (stopping) | 18lp:159 | Refers to the argument of 13sb:104–117. 10:167–172 imposes the last condition of the schedule and says "It will keep replication costs subpower at a nearby sparse stopping scale"; 13sb:85–86 has the anchors at the stopping level widely spaced. "Sparse" = widely spaced anchors at that level. | I |
| trial encoding | 13:394 | The reference label `v_{N,p}` attached to a trial by 11:943–951; 11:1074 "supplies the trial encoding with subpower inverse terminal coordinates". | R (ch. 11) |
| equation remainder; corrected projection; corrected (physical) inclusions | 18gq:8, 110, 114 | `(x_u − Π_u x_u)/(1+‖Π_u x_u‖)`, `Π_u x_u` (13:195–203, 220) and the maps `ι_{d,e}` (13:263–264); "corrected" against "the naive inclusion of unnormalized polynomials" (18gq:94–95). See §1.1. | R |
| "Open the centered cells" | 13ba:127 | "Start with the centered cells at level `m`", by the use of "opening level" at 11:1889, 1919. | I |
| admissible period cell | 12:375 | 1:359–361: a separated test function "is admissible at volume $p$ if its support is contained in $((-R_p/2,R_p/2)^4)^n$". | D (ch. 1) |
| site conversion; support conversion cost `T_l` | 13ba:145; 18lp:112–113 | Passage from anchored (rooted) bounds to containing-site bounds (9:513; 11R:141–142; 11:1918); `T_e` by formula at 11:233–238. See §1.1. | R (ch. 9, 11) |
| common (trajectory, construction, lattice) | 12:13, 40, 370; 12:230, 296, 299 | "Common trajectory / construction": common to all ultraviolet cutoffs, "a single sequence of scales and a consistent choice of coefficient arrays … compare theories with different ultraviolet cutoffs" (10:4–9). "One common lattice" (12:230, 299): one of the nested lattices containing all the points. | R (ch. 10); lattice R |
| corrected-source estimate | 14lc:45 | The estimate for the corrected coefficients `R_I` of 14lc:48–55. See §1.1. | D |

---

### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| index of a lattice in the sequence | level (≈77), scale ("cell scale", "centered scale", "stopping scale"), stage (misleadingly close), depth ("comparison depth"), "base level", "reference level" | *level m*; keep *stage* only for `J(m)` |
| applying the block maps downward | transport, transfer (12:237, 252, 259), push (13ba:124, 158, 185), descend / descent (13ba:170; 13:239), propagate (12:140) | one verb |
| the fixed construction of ch. 10 | selected trajectory, common trajectory, selected schedule, selected histories, the single schedule | *the parameter sequence of Chapter 10* |
| remaining insertions | spectators, spectator word, exterior word, exterior spectator, exterior insertions | *spectators* |
| correlation function | correlation, moment, kernel (13:24 "periodic kernels"), response, hierarchy/family | *correlation function*; *family* |
| distance from a boundary | margin, buffer, slab margin, "room" | *margin* |
| slack in an estimate | reserve, room, margin, excess, loss | print the inequality |
| repeated translates in a chessboard estimate | copies, replica cells, repetitions, reflected copies, "replicate" | *copies* |
| subsequence | refinement, extraction, selection, "cofinal" | *subsequence* |
| all large `N` | cutoff tail, "eventually", "on a full cutoff tail" | *for all sufficiently large N* |
| tail of the iterated limit | ordered tail, "ordered cutoff and volume tail" (18lp:16–17) | *for all `k ≥ k₀` and all `j ≥ j₀(k)` along the chosen sequences* (not "for all sufficiently large N": the volume index and the dependence `j₀(k)` matter) |
| `ker H` | zero-energy subspace, ground space, `H_0`; ground projection | *zero-energy subspace* (of the reflection Hilbert space). "Ground vector / vacuum" name the vector `Ω`, not the space: 15:47–48 "it does not say that this space is one dimensional" |
| the algebra `𝔄` | compression algebra, ground algebra | one name |
| pairing with spectators | response, tested correlation, correlation pairing, correlation functional, probe | *correlation functional* |
| family of functionals detecting a field | separating family, detecting family, (detector, in labels), reference rows; the probes are the words that define such functionals | *separating family* |
| source-variable scale | source weight, mark weight, marker weight/amplitude, residual weight, available weight | *weight* |
| large-field index data | inventory, prescribed set of large-field sites, "prescribed-site" | *prescribed large-field set* |
| terms with ≥2 sources | higher entries, modes, terms involving at least two insertions, terms of source degree at least two | *terms of source degree ≥ 2* |
| the interacting limit theory | mixed, physical, (plain) continuum | say *of S* |
| chessboard seminorm notation | `‖·‖_𝒯` (13:74), `‖O‖_k` (13:302), `‖·‖_{cell(m)}` (13sb:79), `‖·‖_{cell(m,y)}` (13sb:126), `‖·‖_{𝒞_k}` (13ba:24), `𝓡_m` (11:820), `‖·‖_{cell}` (14lc:64) | one notation (that these all denote one seminorm was not checked) |
| position of an insertion | origin ("physical origins", "insertion origins"), anchor, position | *insertion point* |
| at the cutoff level | terminal, microscopic, "outer cutoff" | *at the cutoff level N* |
| discrete set of points | lattice, grid | *lattice*, or define "grid" once |
| the correction by free moments | corrected coefficients, corrected-source, corrected word, corrected moment estimates | one name |

---

### 6. Overloaded symbols noticed

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

### 7. The ten most confusing terms

1. **graph** (ch. 12): a map called a graph; 17 uses, name never motivated in the text (probably the graph-transform usage; linearity stated only in ch. 11).
2. **column / inverse-column bound**: the coefficient vector and coefficient map; ≈20 uses, never defined in these chapters.
3. **label**: silently changes from a polynomial in `V_d` (ch. 12–13) to an element of the quotient `F_d` (ch. 14–16), against notation.md.
4. **mixed**: the undecomposed mixture, used from 14:12 before any mixture is mentioned; also "polarised" and "of both signs".
5. **stopping / stopped**: in ch. 12 evaluation at an intermediate level with the terms of source degree ≥ 2 deleted, in 13sb, 13ba, 18lp the level at which a bound is applied with nothing deleted; suggests stopping times.
6. **attachment** and **incidence**: 11 and 5 uses, meaning recoverable only from chapters 9 and 11, and for "attachment" only by inference.
7. **trial** (local, coarse, protected, descent, encoding): central to 13ba and 13:226–242, defined only by formula for `V_h`.
8. **heat** (semigroup, energy, orbit, damping): the semigroup `e^{-tH}` of translations in the reflected direction; no heat equation appears, and the word is used from 14:80 before 15:26 names the semigroup. How unusual the name is remains a matter of judgement.
9. **centered**: "inside a cell with margin" in ch. 13, "zero expectation" in ch. 14.
10. **history / schedule / trajectory / stage / level**: five words around the scale sequence; "history" is defined at 11:18–19 and used here per cutoff; plus **physical** in four senses.

Residue of mechanical term replacement. The sentences that were ungrammatical have been repaired in the text (18lp:43, 18lp:136, 14:832; also 16:380, where a bare `\ref` became `\eqref`); they now parse. Still defective: 18lp:27 "a remainder with vanishing extracted coefficient of norm $r_l$" and 18lp:36 "a remainder with vanishing extracted coefficient of size $q$", where the norm or size belongs to the remainder, not to the coefficient. Grammatical but heavy, all from the phrase "prescribed set of large-field sites": 12:27, 12:162, 13ba:153, 18lp:40, 18lp:185 ("Each term is assigned the union of its supports and original prescribed set of large-field sites"), 12:288 ("support and prescribed-site profiles"), 18lp:31; likewise 13sb:63 ("its counterpart constrained to cover the prescribed large-field sites, as well as the source attachment bound") and 14:990 ("the fact that inserting the identity leaves correlations unchanged").

Jargon surviving only in labels (not in the PDF; but "Forgetting the terminal graph" is also a printed title, 12:131): `ch12:inputs`, `ch12:forgetting`, `ch12:omission`, `ch12:stopped`, `ch12:root-bound`, `ch13:coarse-residual-supplier`, `ch13:sharp-root`, `ch13:residual-height(-bound)`, `ch13:scale-thickness`, `ch13:sharp-schedule`, `ch14:grid-input`, `ch14:grid-cost`, `ch14:balanced-stress`, `ch14:subset-root`, `ch14:diagonal-mass`, `ch14:heat-pairing`, `ch15:detector-moments`, `ch15:compression-defect`, `ch15:whole-gram`, `ch18:graded-room`, `ch18:low-cone`, `ch18:high-step`, `ch18:group-weight`; referenced from ch. 11: `ch11:uniform-sweep`, `ch11:finite-detector-input`, `ch11:simultaneous-detector-lifts`, `ch11:replicated(-bound)`, `ch11:n-mark-comparison`, `ch11:higher-induction`, `ch11:one-graph`. Note `ch13:sharp-phase` is a label defined in `15sp` (15sp:21).

---

### 8. Not read / not checked

- The survey read all eleven assigned files in full (3869 lines), with Part II and the translation table of `blueprint/notation.md`; the audit also read them in full; the re-audit read about 45% of them (the cited ranges with context).
- Chapters 1, 2, 9, 10 and 11 were consulted only by grep and short excerpts to locate definitions; meanings marked "(ch. 11)" and the like rest on those excerpts, not on a full reading. Chapters 17–19 were not opened, apart from 18:36–56 for "probe"; `18-raw-replacement.tex` was not opened.
- Figures (`figures/ordered-limits`, `ward-shell`, `cluster-exchange`) were not opened.
- Counts are grep counts of occurrences. `row`, `actual`, `select-`, `test`, `label`, `mark`, `window`, `history`, `probe`, `response`, `transport`, `frame`, `anchor`, `cost`, `centered`, `mixed`, `column`, `cone`, `admissible` were classified line by line from one-line contexts; borderline assignments could shift by one or two. Sub-counts within `threshold`, `comparison`, `stage`, `margin`, `admissible` were not recounted by a second reader.
- No Lean declaration was consulted; no proposed equivalent was checked against the literature. Section 6 is a list of what was noticed, not a complete symbol audit.

---

### Changes folded in

Origin: B = independent audit; R = re-audit report; own = found while checking the cited lines. "Verified" means the cited chapter lines were opened for this fold and support the change.

**Header and conventions**
- Status notices removed; conventions extended by the abbreviations `1:`, `2:`, `9:`, `11R:`, `18:`; "the dictionary" renamed "Part II" throughout (brief).
- General observation: "undefined vocabulary inherited from chapter 11" changed to "inherited from chapters 2, 10 and 11 and not explained again here" (B: `section`, `history`, `stage` are defined there; verified at 2:138–146, 11:18–19).

**Section 1.1**
- `graph`: "linear" no longer under D (B; verified 12:82, 11:379); forward use at 12:37–38 (B; verified); probable origin of the name and new proposed equivalent, "remainder map" withdrawn (B, R; the text facts verified at 12:90–94, 11:379; the graph-transform reading is general knowledge).
- `forgetting`: the claim that the terminal graph is at level `m+h` replaced by two readings, basis I (B, R; verified that 12:139 lacks the word and that 12:131 is its only occurrence in `12`).
- `stopping`: split into two senses, count 11, "truncated correlation" withdrawn, "sparse" from ? to I (B, R; verified 12:207–216, 13sb:9–11, 85, 104, 10:167–172).
- `large-field profile`: "complementary profile" I → R via 13ba:16 (B; verified); 12:288 added (R).
- `exact-cover gas / unmarked gas`: meaning sharpened (a factor of the density, not the density), "partition function" withdrawn (B, R; verified 12:172–183, 18lp:185–186).
- `source weights`: support from notation.md:216 added (B; verified).
- `normalized local insertion`: meaning replaced (the insertion itself, not the source times `ω_k`) (B; verified 11:895, 13ba:119, 18lp:243, 13sb:58, 65, notation.md:158).
- `inverse terminal coordinates`, `admissible coefficient family`: definition line 11:1101–1102; ch. 13 does not name the variable (B, R; verified).
- `trial`: "trial encoding" ? → R (ch. 11) (B; verified 11:943–951, 1074); "protected" stays I, with 11:2306 (B; verified).
- `equation space`: line 11:1089–1093 (B; verified); "equation remainder" ? → R (B; verified 18gq:108–110, 13:195–203, 220).
- `section`: "no / I" → D (ch. 2) (B; verified 2:138–146); equivalent changed to "keep".
- `attachment`: ? → I with meaning (B; verified 9:687, 11:937, 941, 13ba:61, 77; the quotation "Attach the latter …" is at 11:922–923, not 11:924–925 as the audit has it: own).
- `request`: three uses (B; verified at 13ba:100, 336, 18lp:103, 151, 15:207, 14lc:108; 14:224–227 and 14lc:9, 79 rest on B and R).
- `comparison depth`: note on "admissible" (B, R; verified 14lc:23, 11:884).
- `ancestor cone`, `recentering`, `remainder with vanishing extracted coefficient`, `low plane`: proposed equivalents qualified, withdrawn or replaced (B; verified 13ba:232–233, 18lp:36–43; 18gq:51, 76 not re-read).
- `"Open the centered cells"`: ? → I (B; verified 11:1889, 1919).
- `coordinate hybrids`: guess added, stays ? (R; verified single occurrence by grep).
- `the source construction`: the parameter mismatch removed; parameters R, "source" ? (B, R; verified 14:171, 186–189, 14lc:26, 85–86).
- Rows added (18): corrected coefficients `R_I` (B, R; verified 14lc:45–57, 11:2064–2070, notation.md:216; "Wick-ordered" is R's proposal from general knowledge); corrected projection / inclusions (B; verified 18gq:8, 94–95, 110, 114, 13:263–264); site conversion (B; verified 9:513, 11R:141–142, 11:1918, 11:233–238); origins (B; verified 12:22, 208, 230, 239, 279); background convergence (B; verified 12:31–34, 41); normalized null condition (B; verified 13:195–203, 215, 18gq:8–9, 108); microscopic (B, R; verified 18gq:10, 76, 94, 18lp:36); reference label etc. (B; verified 18gq:12, 85, 106, 112, 13ba:200, 275, 12:135; the gloss is own, I); raw (B; verified 13sb:173, 18lp:318, 324–325, 14:777; gloss own, I); ordinary (B; verified 13ba:15–16, 37); endpoint estimate, fine end (B; verified 13ba:18, 34, 18lp:46, 63; gloss own, I); vacuum normalization bound (B, R; verified 12:247, 286; gloss I); grid (B, R; verified 14:177, 14lc:29, 75, 15:178, 207, 13ba:336); target (B; verified 13:252, 260, 18lp:341, 344); replacement / reconstruction (B; verified 14:349, 353–355, 18lp:266–267, 279); positional (B; verified 14lc:92, 14:813–814, 841, 18lp:296); signed (B; verified all cited lines); transitions, degree ceiling (B; verified 13sb:49, 13ba:56, 81).

**Section 1.2**
- `ordered tails`: meaning and equivalent corrected, "for all sufficiently large N" kept for "cutoff tail" only (R; verified 13:140–143, 213–214, 12:190, 249, 13sb:84, 18lp:16–17).
- `separated`: defined in 1:359; 14:17–18 does not contain the word (B; verified).
- `cell`, `buffer`: equivalents "tile" and "margin" withdrawn (B, judgement; 13:88 not re-read).
- `exterior word`: 14:354 is "exterior spectator" (B; verified).
- `slab`: forward uses 13:335, 391 (B, R; verified).
- `heat`: meaning made specific, equivalent "transfer semigroup" replaced by "translation semigroup", count 18 (B, R; verified 14:39–56, 80, 414, 15:26).
- `mixed measures`, `profile`: equivalents "polarised measures", "multiplier" replaced (B; 14:424, 448 verified).
- `shell factor`: the text's word is "response"; "flux integral" marked as a proposal (R; verified 14:777).
- `phase`: count 52; forward uses listed (B, R; verified 13:393, 14:351, 371; 13ba:5, 304, 18lp:7 rest on B).
- `letter; field word`: "word" is a finite sequence of letters, not a product; "word" itself undefined at 16:291 (R; verified 16:291–294).
- `moment`: exception for 15:213 (B; 15:123 verified, the formula for the product moments rests on B).
- Rows added (7): unit (B; verified 13:58, 14:34, 220, 283, 974, 15:25); vacuum (R; verified); zero-energy subspace / ground space (B, R; verified 15:7, 47–48, 16:379, 437); exceptional phases (B, R; verified 15:320–326, 328, 339, 16:379–381); mixed (R; verified 14:12, 165, 349, 820, 15:5–7, 155, 277); scalar heights etc. (B; verified 16:218, 248, 481, 14:283–284); collision orders, Ward sum, vector-map space, defect space (B; lines verified, meanings own and I).

**Section 2**
- 2.1: "macro-box radius" removed from the smoothing-order row (B; verified by grep and at 13ba:244–245); `spectator` 49 → 33 (B, R; recounted); `subpower` + 13:235 (B; verified); `physical` ≈17 → 16 (B).
- 2.2: spectral `response` split into function and number (B, R; verified 14:448–451, 465–470, 503–505, 654, 672); shell `response` no longer called "the flux integral" (R; verified); `transport` (ii) split into conjugation and application (B; verified 14:281–282); `probe` meaning replaced, basis D from 18:38 (B; verified 18lp:268–269, 332, 14:354; the definition at 18:38 is own reading); `row` rewritten (B, R; verified 13:159, 11:2253, 15:274–279, 288–289); `centered` verbs (B; verified); `cutoff` + smooth cutoff function (B, R; verified 13ba:36, 14:252, 324, 328, 396, 16:205, 459; the other ten lines rest on B); `terminal` rewritten (B, R; all nine occurrences verified by grep, 13sb:92 and 13ba:61, 77, 153, 174 added: own); row `request` added and row `lift` extended by 15:256 (B, R; 15:256, 14lc:32 verified); `word` basis D / R (R).
- 2.3: `subpower` wording (B, R; verified 13:159, 217, 13ba:18, 11:1101–1102; R's version of the lines preferred to B's, see below); `history` I → D (ch. 11) (B; verified 11:18–19).

**Section 3**
- `row` 7 → 8, senses regrouped, (c) I → R (B, R; verified; total recounted).
- `actual`: borderline cases noted (B; not re-read).
- `selected`: total 23; two doubtful assignments noted, not moved (B; 13:395, 13ba:30 verified as quoted, the text does not settle them).
- `test`: 14:207 from (b) to (c), 16:215 from (c) to (a); 30 / 7 / 10 (B, R; verified both lines).
- `label`: 59; undecidable lines listed; notation.md:150 (B, R; verified 13:282–285, 14lc:7, notation.md:150).
- `mark`: ≈35 → ≈34 (B).
- `source`: ≈60 → 49, sense (a) ≈38 → 31; "corrected-source estimate" settled; (e) reworded (B, R; total recounted; per-sense figures are B's).
- `cost`: 18lp:85 from "error term" to "multiplicative factor"; 11:808 → 11:789 (B; verified both).
- `probe`, `response`, `transport`: as in 2.2.
- `phase` ≈53 → 52; 15:136 added (B, R; verified).
- `word` (b): "product of letters" → "finite sequence of letters" (R; verified).
- `centered` 23 → 24; verbs; (iv) I → R (ch. 1) (B; verified 1:217, 18lp:224).
- `physical` 37 → 31, sense (i) 16 (B, R; total recounted).
- `mixed`: forward use at 18lp:8; "polarised" reworded (B, R).
- `cone`: 18lp:48 is "The cone calculation" (R; verified).
- `admissible`: 12:37 is a forward use of 12:82; "period cell" defined at 1:359–361; 11:1101–1102 (B; verified).
- Bullets added: stopping, request, cutoff (66), terminal (9), vacuum, scalar, gap, corrected, signed, lift, unit (B, R; counts for cutoff and terminal recounted).

**Section 4**
- Table divided into 4.1 (still undetermined) and 4.2 (determined by other chapters). Moved to 4.2 with meanings: attachment, sparse stopping, trial encoding, equation remainder / corrected projection / inclusions, "Open the centered cells", admissible period cell, site conversion, common, corrected-source estimate (B; verified as listed under 1.1; `common` verified at 10:4–9, 12:230, 296, 299). Added to 4.1: the name "graph", "terminal" in the title 12:131, "source" in "the source construction" (B, R).

**Section 5**
- "all large N" divided into two rows (R); `ker H`: "vacuum" not for the space (B, R; verified 15:47–48); "probes" and "exterior probes" taken out of the lists of synonyms (follows from the corrected meaning of `probe`); seminorm row: 13sb:126 added and a caution (R); four rows added: position of an insertion (B), at the cutoff level (R), lattice / grid (B, R), correction by free moments (B).

**Section 7**
- Items 1, 5, 6, 8, 10 reworded to agree with the corrected rows.
- The list of damaged sentences replaced by the present state: 18lp:43, 18lp:136, 14:832, 16:380 are repaired (verified in the text); 18lp:27, 36 keep a misplaced modifier (B, R; verified); 18lp:185, 13sb:63 and the other instances parse (B, R; verified 18lp:185, 13sb:63, 12:27, 162, 288, 13ba:153, 18lp:31, 40, 14:990).
- "Forgetting the terminal graph" noted as a printed title, not only a label (R; verified).

**Section 8**
- Rewritten as a statement of what the three readings covered.

**Proposed corrections not applied**
- B, "11:258 for the incidence sum is 11:257": the quoted phrase "the insertion incidence sum at a fixed mark" is on 11:258. The survey's reference is kept. Found wrong on inspection.
- B, "Attach the latter to the original selected large-field factors" cited as 11:924–925: the sentence is at 11:922–923. The meaning was applied with the corrected line. Line reference found wrong on inspection.
- B, "'in $a_h^{-1}$' is at 13ba:18 and 11:1101": 11:1101–1102 has `a_N^{-1}`, as R points out. R's version used; the correction it supports is unaffected.
- B, `terminal graph` "probably a wrong" inference: not adopted as a fact. The text supports neither reading explicitly, so both are stated with basis I.
- B, `selected` at 13:395 and 13ba:30 "could be sense (a)": recorded as doubts; the lines were not reassigned because the text does not decide.
- B, `complementary profile` to plain R: applied as "R (13ba:16)"; the identification of "profile" at 13ba:165 with the "part" of 13ba:16 is evident but is not stated in one sentence.
- R, count of `cell` 58 against the survey's 57: not recounted; the survey's figure is kept.
- R, D5, D8, D9, E4 (as a quotation matter) and E5 concern the wording of Part I only; E4 and E5 are reflected in section 7 here.
- B section 7 (errors in the overview) concerns Part I.

### Verification status

**Checked against the text by at least one reader other than the survey's author**
- Section 1.1, confirmed by B (meaning, basis and lines): fixed-input continuity; `I_G` / `J_G`; forgetting (the gloss); dictionary; inventory; large-field profile; complete; terms linear in the sources / modes; source weights; column; inverse terminal coordinates; admissible coefficient family; trial; equation space; incidence; rooted; reserve; block floors; first-below scale; comparison depth; lift; ancestor cone; frame seed; group / merger / live; recentering (meaning); low plane; cell census; inspected. Confirmed by R at the cited lines: graph (12:82), column (13:164, 13ba:276, 18lp:26), the marked density (12:200–206).
- Section 1.2, confirmed by B: ordered limits; slot; arity (17); cell / centered; buffer; exterior word; slab; heat (meaning); damping; coordinate spectral measures; profile (meaning); annular correction; conserved stress line; line axis; shell factor; Ward kernel / normalization / spin operators (as inferences); phase; compression; whole word; cluster; generic; coordinate ties; height / gap / tied; padding identity; letter; barycenter identity; partial boundary; local charge.
- Section 2.2: response, transport, anchor, label, word, window, lift, representative, charge, centered (B); window, request as a tuple of data, probe, physical inclusion, ordered tails (R).
- Section 2.3: regularity stage (10:25, 133, 808), subpower (18lp:18), schedule, moving, marked, event indicator (B).
- Section 3 totals reproduced by B and again by R: actual 20, select 23, test 47, label 59, mark 53, window 6, history 7, response 25, transport 14, cost 25, mixed 23, column 22, cone 17, centered 24, probe 6, anchor 6, frame 4, phase 52, word 96, cluster 23, heat 18, level 77, row 8, spectator 33, source 49, physical 31; price / pay / readout / table / tag 0. Recounted for this fold: spectator, source, physical, row, stopping (11), subpower (7), terminal (9), microscopic (7), slab (24), profile (32), height (19), cutoff (66), grid (20).
- Every change listed above as "verified" was checked at the cited lines for this fold. This covers all rows whose meaning or basis was altered, and all rows added in sections 1.1 and 1.2 as far as the occurrence of the term at the cited lines goes.
- Section 7: the present state of the sentences at 18lp:27, 36, 43, 136, 185, 13sb:63, 14:832, 14:990, 16:380, 12:27, 162, 288, 13ba:153, 18lp:31, 40; the labels `ch12:forgetting`, `ch12:stopped`, `ch13:coarse-residual-supplier`, `ch14:grid-cost`, `ch15:detector-moments` (R); B reports all listed labels present.

**Resting on one reader only, or not verified**
- Section 2.1 (same-sense rows): B checked that the terms occur at the cited lines, not that the sense agrees with chapters 3–6. This rests on the survey.
- Section 5 (synonym clusters) and section 6 (overloaded symbols): spot-checked only (`χ`, `r_d`, `R_d`, the seminorm notations; in section 5 the members occurring at lines R looked up). Section 6 is unchanged from the survey and unverified row by row.
- Per-sense splits were not redone occurrence by occurrence by a second reader for `label` (field against polynomial), `mark`, `source`, and in part `actual`; the per-sense figures for `source` and `test` are B's.
- Sub-counts for `threshold`, `comparison`, `stage`, `margin`, `admissible`, `width`, `degree`, `mass`, `residual`, and the counts 17 for `graph`, 57 for `cell`, 67 for `separated`, rest on the survey.
- Glosses written for this fold and marked I (reference, raw, endpoint / fine end, target, positional, transitions, collision orders, Ward sum, vector-map space, defect space, the three uses of `unit`) were read at the cited lines by one reader only and are inferences.
- Lines taken from B without re-reading: the list of smooth-cutoff occurrences beyond the seven checked; forward uses of "phase" at 13ba:5, 304, 18lp:7; 13:96, 14:224–227, 14lc:9, 79 for `request`; the borderline remarks on `actual`; 18gq:51, 76 for the low plane; the meaning of "compressed product moments" (15:213).
- Chapters 1, 2, 9, 10, 11 and 18 were read only at the excerpts cited. No figure, Lean source or literature was consulted.
- General knowledge, not in the text, needing a mathematician: the graph-transform reading of "graph"; "translation semigroup" for the heat semigroup; "Wick-ordered with respect to the free moments" for the corrected coefficients; the Borchers–Uhlmann description of `𝒫`; all other proposed equivalents.

---

<a id="part-vi"></a>

## Part VI. Chapters 17–19, main theorem, reading guide

> **Status.** Corrected dictionary for chapters 17–19, the main theorem and the reading guide. It is the survey of these files with the corrections of one independent audit and one re-audit folded in; each correction was checked against the chapter text before it was applied. What was changed, and what has been read by more than one reader, is stated in the last two sections. Meanings marked I are inferences. No proposed equivalent was checked against the literature.

Worktree `manuscript/HumanizeYM_v3/`. The survey was made at commit `9e227b1a`, the corrections were checked at `eb97dec6`; chapter line numbers did not move between them.

**File abbreviations** (line numbers are those of the worktree files):
`17` = chapters/17-trace-law.tex, `17w` = 17-variable-windows.tex, `17t` = 17-trace-transfer.tex, `17c` = 17-current-contraction.tex, `17m` = 17-marked-trace-rates.tex, `18` = 18-operator-products.tex, `18r` = 18-raw-replacement.tex, `19` = 19-assembly.tex, `MT` = main-theorem.tex, `RG` = reading-guide.tex. Other chapters are cited as `ch10:25` etc.; `ch11` = 11-marked-insertions.tex, `ch11E` = 11-equation-calibration.tex, `ch11R` = 11-restarted-history.tex, `ch13` = 13-continuum-fields.tex, `ch13ba` = 13-bounded-approximations.tex, `ch14` = 14-reflection-ward.tex, `ch18lp` = 18-lattice-products.tex.

**Basis codes**: D defined in the text; R read off an explicit sentence or formula; I inferred; ? not determined. "via ch. N" means that the sentence read is in chapter N. **Categories**: (a) accounting metaphor, (b) program/Lean leakage, (c) ordinary or standard word in unusual technical sense, (d) coined, (e) other.

Counts were obtained by `grep` on copies with `\label{}`, `\ref{}`, `\eqref{}`, `\pageref{}` arguments blanked. Occurrences in `\input{...}` file names are excluded where noted.

"Part II" means the dictionary for chapters 3–6.

---

### 1. New terms (not in Part II, or there only in §4.2 without a gloss)

#### 1.1 Scales, schedules and windows

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| stage; change of stage; stage plateau; adjacent-stage cases; fixed-stage tail; stage orders | 17:132; 17w:2, 13, 14, 49, 50, 69, 71, 97, 125; 17c:12, 107, 135, 238; 17m:39, 141, 197, 301, 346, 347, 430; 19:30; RG:34 (23 in all) | Not in these files. Defined ch10:25–29 ("A stage j≥1 specifies finitely many derivative orders, support …"), with `J(m)=j` for `A_j ≤ m < A_{j+1}` (ch10:129–134) | Index `j` of a finite package of requirements (derivative orders, weights, constants); `J(m)` is the stage in force at scale `m`. 17w:14–15: "`𝓛_j` for the ratio chosen at stage j, so `L_i=𝓛_{J_i}` with `J_i=J(i+1)`" | R (via ch. 10) | *stage `j`*, defined once per chapter. Never use for "scale" or "step" | (d) |
| plateau (of a stage) | 17w:7 | Not here; ch10:123, 139 | Maximal interval of scales on which `J(m)` is constant ("requiring every window to lie inside a plateau would leave gaps") | R (via ch. 10) | *interval of scales with constant stage*. Different from the Part II plateau (region where a cutoff equals one) | (c) |
| level; insertion level `k_i`; radius level `n_i`; comparison level `k`; output level; stopping levels; late level | 17:85, 86, 120; 17w:41, 102; 17t:405; 17c:241, 391; 17m:136, 331, 416 | Named only: 17:84–87 "`β_i` … at a finer insertion level `k_i` … The radius level `n_i` precedes `k_i`"; `k(n)` by formula 17:108 | *Level* = scale index. `n_i`: scale whose spacing `a_n` fixes the radius `r=a_nM_n^u`; `k_i`: finer scale at which the insertion and its coupling are taken. That `k_i=k(n_i)` is never written; it is inferred from 17:108, 139–142 and 17m:386, 420. "Output level" (17t:405; 17c:241, 391): the fixed scale at which the transferred current is evaluated (inferred). "Comparison level" is the ch. 11 term (ch11:734) | R for the names `n_i`, `k_i`; I for `k_i=k(n_i)` and for output level | *scale `n_i`*, *scale `k_i`*; say what each indexes | (c) |
| (radius, comparison) window | see §3.4 | Radius window by formula 17:107 | Four objects under one word: interval of radii `{a_nM_n^u: α₀≤u≤α₀+1}`; the set of RG steps between `n` and a stopping scale; a compact set of separated configurations (17:140, ch. 14 sense); the length of an average (17m:476) | R | *interval of radii*; *range of scales*; *compact set of separated configurations* | (c) |
| stop backwards; first (backward) crossing; overshoot; stopping integers; stopping levels; stopping pair | 17:138, 142; 17w:31–36, 102, 105; 17m:425, 432, 469 | No | The quantity that crosses is a difference of `τ_m=log(1/a_m)` (ch10:145–146: "`τ_{m+1}=τ_m+log L_m`, `a_m=e^{−τ_m}`"), i.e. the logarithm of a ratio of lattice spacings. 17m:422–425: "`τ_{k(n)}−τ_n ≥ T_n` is the first crossing" (towards finer scales, as in `k(n)` of 17:108); 17m:432–433: "Replicate at the first backward crossing of `B_n²`, so `B_n² ≤ a_m/a_n ≤ L_*B_n²`" (towards coarser scales). At 17w:31 ("stop backwards from n at the first crossing of `(b+2)log H_n`") the crossing quantity is not named; by the same reading it is `log(a_m/a_n)`. Overshoot = excess of that logarithm over the target (17w:36) | R at 17m:423, 432–433; I at 17w:31 | *the first scale `m<n` with `log(a_m/a_n) ≥ …`*; print the definition | (b) |
| request (degree, arity, derivative, window request); requested | 17:140; 17w:10, 13, 73, 85; 17m:88, 142, 285; 18:144 | No | A fixed finite list of parameters (degree bound `D`, arity bound `N_*`, derivative order, error exponent) for which an estimate is to hold. 17w:10 "Fix a finite degree, arity and derivative request". No sentence defines the word; the meaning is read from its uses | I | *fixed finite data `(D, N_*, r)`*; *for the given orders* | (b) |
| Diagonalize (… requests); diagonal radius selection | 17:139; 17m:446 | No; cf. ch14:224–227 "A single sequence for all requests is obtained only by explicitly diagonalizing arity, degree, compact windows and errors" | Take a diagonal subsequence over the countably many finite requests | R (via ch. 14) | *take a diagonal subsequence over …* | (c) |
| pre-ratio / post-ratio / fixed-ratio constants | 17w:24, 72, 75, 76; 17c:138; 17m:249, 428, 429 | 17w:13, 21 | Constants fixed before the block ratio `𝓛_j` of the stage is chosen (hence independent of it), respectively depending on the already chosen ratio. 17c:138–143: fixed-ratio constants "may depend on `L`, because the coupling threshold is chosen after the ratio". Same idea as the Part II "pre-`L` factor" | R | *independent of `L`* / *depending on `L`* | (d) |
| coupling threshold(s); coupling-threshold-controlled | 17:134; 17w:23, 42, 74, 76, 95; 17c:141, 234, 236, 384, 386; 17m:142–143, 174, 185, 315, 346–347, 365, 430; 19:20 (19; two are split across lines) | No | Lower bound imposed on `β̂` at a stage ("sufficiently large coupling thresholds"). Same as Part II §4.2 "coupling threshold". `threshold` alone has other meanings in these chapters (§3.14) | R | *for `β̂` sufficiently large (depending on `j`, `L`)* | (c) |
| (common, scale) schedule | 17w:35; 19:18, 31; RG:32 | ch10:118 | The choice of all stage data and of `J(m)`: "The common schedule … selects all block lengths, derivative orders, support weights, coupling thresholds and admissible physical periods" (19:18–21) | R | as Part II: *fixed parameter sequence* | (d) |
| equation calibration floor | 19:30 | Not here; ch11E:23–30 | A lower bound on the block ratio `L` at stage `j`: "Include the finite maximum `L^{1/8} ≥ max_{d≤j} 2(1+C_j)Q_{dj}δ_d^{-1}` in the stage-`j` block floor" (ch11E:23–29, label `ch11:calibration-floor`). The same passage adds a separate condition on the coupling, "`β̂_N ≥ a_{d,J(N)}` in the adjacent stage conditions on the starting scale" (ch11E:29–30); 19:29–31 ("finite stage requirements, such as the equation calibration floor") may be meant to cover both | R (via ch. 11E) | *the lower bound on the block ratio in (11.calibration-floor)*, with the accompanying condition on `β̂_N` | (d) |
| floor | 17t:107 ("denominator floor … `a_μ ≥ cT²I`"); 19:30 | by formula | Lower bound: on an operator at 17t:107, on the block ratio at 19:30 | R | *lower bound* | (c) |
| shooting; coarse endpoint | 19:21–23 | No; the section ch10:209 ff. is titled "Tuning a finite history to the coarse endpoint" (its label is `ch10:shooting`); the word is in prose at ch10:273, 818 | Choice of the bare coupling so that the trajectory ends at the prescribed coarse value `β̄` | R | acceptable (shooting method); or *tuning of the bare coupling* (MT:62 already says "tune") | (e) |
| current depth; deep transferred current | 17m:29, 361 | No | Number of RG transfers applied to the current | I | *number of steps* | (c) |
| restart; restarted representation / histories | 17w:33, 102; 19:49 | Not here; ch11:734–741; ch11R:12–18 | "A useful auxiliary history keeps the actual inverse coupling constant below a comparison level while retaining the paths, adjacent quadratic identities, and block geometry" (ch11:736–738). `B_n`, "the radius of the restarted representation" (17w:33): "The new representation at level `i` has radius `B_i=b(x_i)^2`", `b(x)=⌈(log x)²⌉`, `x_i=β̂_i` (ch11R:12–18). Open point: 17m:438 uses "`B_n=O((log β̂_n)²)`", which does not match `b(x_n)²`; whether the two `B` are the same object was not determined | R (via ch. 11) | *history with the coupling frozen below scale `k`*; cite ch. 11 | (b) |
| replicate (verb) | 17m:432 | No. `ch11:replicated` (ch11:780) is the label of the section "The normalized integral with several insertions"; the verb is not used in ch. 11 prose (it is at ch13ba:283) | "Replicate at the first backward crossing of `B_n²`": take a reflected tiling at that scale, as in ch11:815–817 "A reflected tiling at scale `a_m`, stopped at `a_k`, has `(a_m/a_k)⁴` sites per cell. Taking the number-of-cells root …", for the estimate (11.replicated-bound) | R (via ch. 11) for the operation; the verb itself is not explained | *apply the chessboard estimate (11.root-bound) with a reflected tiling at the scale …* | (b) |
| amplification | 17w:78, 79 | No | The product `∏(2+C_{J_i})` of the linear propagation constants over a window, (17.window-product) | R | *the product (17.window-product)* | (c) |
| endpoint constants; endpoint factors | 17w:23, 26 | No | Constants that enter a bounded number of times, at the ends of the comparison window, as opposed to once per step ("Only a bounded number of endpoint factors is multiplied") | I | *constants entering a bounded number of times* | (d) |
| bottom stage; middle and output stopping levels; top (polynomial extraction) | 17w:97–102 | No; ch11:2085–2088 "Construct `T` at the top level `k` … Neither … depends on the choice of middle or output level" | Positional words for the scales of a comparison window: top = the level at which `T` is constructed. Whether "bottom stage" uses `stage` for a level (it would be the only such use in these files) is not determined | R (via ch. 11) for top; ? for bottom stage | name the scales by their symbols | (b) |

#### 1.2 Transfer of the current (chapter 17)

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| current defect `𝓔_b`; defect; quadratic defect; defect Ward identity | 17:194, 244; 17t:157, 408, 416; 17c:6, 13, 17 and 13 more; 17m:154 (22) | 17:194–195 | `𝓔_b = Σ_a∇_aJ_ab − D𝖲[Y_b]`: the failure of the lattice Ward identity, that is, of current conservation up to the equation-of-motion term. New sense relative to the Part II "curvature defect" | D | *defect of the lattice Ward identity* | (c) |
| "(quadratic defect) has order at least four" | 17c:17–23 | 17c:17 | `E_b(p,q)=O((\|p\|+\|q\|)⁴)` near 0: vanishing order of the Fourier symbol of the Hessian; "spatial momentum degree, not the field degree" | D | keep | — |
| low moments; low-moment cancellations / estimate; polynomial moment conditions; zero (exterior) moments | 17:19, 308; 17t:160; 17c:46; 17m:70, 155, 156, 191, 402, 443; 19:157 | No | Two things under one word. (i) Vanishing of low-order Taylor coefficients in momentum, equivalently annihilation of affine/quadratic polynomial fields (17t:159–160; 17c:24). (ii) "Exterior moments": integrals against spectators independent of the varied links (17m:67–70) | R / R | (i) *vanishing of the symbol to order …*; (ii) *integral against every function independent of the varied links* | (c) |
| stationary substitution `𝓘`; stationary pullback; exact pulled-back defect | 17t:28, 157, 159; 17c:51, 72, 77, 91, 208, 304 | 17t:28 | `𝓘F = F(U_stat(V))`: composition with the stationary fine field | D | *composition with the stationary field* | (c) |
| (actual) stationary tangent `W`; smooth representative `W_a`; `W_s`; forest representative `W_F`; radial `W^rad` | 17c:8, 48, 112, 187, 210, 323, 348; 17m:263; 17t:162; ch5:1084, 1108, 1151, 1234; ch7:574 | 17c:48–50 for `W`; ch5:1084, 1108 for `W_s`, `W_a` | `W` (17c:48–50): "the actual stationary tangent from coarse link variables to fine link variables … The first derivative of the nonlinear stationary substitution is this `W`". `W_s` = "the straight-average transport" (ch5:1084); `W_a=W_s−d_{0,f}ERW_s` (ch5:1108; 17m:263–264, "Its difference from `W_s` is a fine gradient"). The symbols are used consistently in chapters 5, 7 and 17. The phrase "actual (stationary) tangent" is not: it names `W_a` at ch7:574 and 17m:263, and at 17c:48, 112 an operator `W` which "may be replaced by the smooth representative `W_a` because the quadratic Ward identities kill its gradient correction". ch5:1234 gives the reading that reconciles them: "`W_a` is the smooth representative of the actual stationary tangent, whereas `W_F` is its representative in the forest coordinates". Which representative the `W` of 17c:48 is (the forest one, or the tangent up to fine gauge gradients) is not stated | D for `W`; R for `W_s`, `W_a`; I for the relation of `W` to `W_a`, `W_F` | *derivative of the stationary map*; say which representative (`W_a`, `W_F`) is meant | (c) |
| anchor average `K_0`; mass (of a kernel); kernels `K_a`, `K_a^e`, `K_a^t` | 17t:19–27, 34, 41–43; 17c:71, 82, 85, 120, 324 | by formula 17t:19–26; "anchor average" at 17c:120 | Finite Laurent polynomials in the shifts, acting on the base point (fine anchor) of a local function before stationary substitution. `K_a`, `K_a^e`, `K_a^t` have no name in the text ("finite Laurent polynomial `K_a^t`", 17t:34). "Mass" = sum of coefficients (17t:41–43) | D (formula) / R (mass) | *average over translates of the base point*; *with total sum one* | (c) |
| (forward-difference) primitive `q_a`, `t_abc`; difference-primitive bounds; primitive norms | 17c:309, 313, 377, 382, 388, 390; 17m:380, 469 | 17t:62, 72; restated 17c:312–315 | Functions with `tr J = Σ_aδ_aq_a`, `J_ab−J_ba = Σ_cδ_ct_abc`. New sense (Part II: elementary factor) | D | "primitive" (antiderivative for the forward difference) is tolerable if the identity is stated; no other equivalent proposed ("discrete potential" is not a standard term) | (c) |
| displacement `Y`; left link displacement; curvature displacement; displaced coarse current | 17:193; 17t:182, 297, 340, 355; 17c:247–291, 312–373; 17m:27, 57 (20) | 17:191–193; 17t:182–186 | A vector field on the product of link groups (link-wise Lie-algebra valued), generating `U ↦ e^{sY}U` | D | *vector field (infinitesimal left variation)* | (c) |
| leg | 17t:149, 152 (three times), 318; 17c:16, 76, 100, 101, 105, 109, 120, 326, 346, 363 (15) | No | One of the two field arguments of a Hessian / bilinear kernel, with its own momentum ("two independent field momenta. Gauge invariance gives a Ward identity on each leg", 17c:15–16). New sense relative to Part II | R | *argument*; *each of the two variables* | (c) |
| channel | 17t:97; 17c:97, 136 | No | 17t:97: each of the two determinants (vector, ghost). 17c:97, 136: the field-order-two component of the defect recursion | I | *term*; *the order-two component* | (c) |
| field order; field degree | 17c:23, 93, 209, 303, 305, 369, 371, 375, 377; 17m:28, 178, 187, 188, 303; 17t:361; 19:157 | No; 17c:222 defines `e_r`, not the term | Order of differentiation in the field at zero ("`e_r` is the weighted norm of the field derivative of order r"), contrasted with scaling dimension and momentum degree (17c:23; 19:157–159) | R | keep; use one of *order*/*degree* | — |
| diagonal / below the diagonal; diagonal factor / transfer; row sum | 17c:140, 211, 228, 235–237, 346, 367, 369, 375, 383 | No | Entries of the triangular matrix of the recursion (17c:216) for the norms `e_r`: diagonal = coefficient of `e_r` in `e'_r` | R | *the coefficient `a_{j,r}(L)`*; *terms with `s<r`* | (c) |
| source (in a recursion); forcing | 17c:132, 225, 245; 17c:380, 382, 385, 386 | No | Inhomogeneous term of a linear recursion ("homogeneous … No constant source term") | R | *inhomogeneous term* (one word) | (c) |
| division (analytic, homotopy, Taylor, curl) | 17c:99, 102, 104, 346 | No; pointer to ch. 7 (17c:99 "The analytic division argument of Section …") | Factoring difference symbols out of a symbol that vanishes to a given order: "Their homotopy divisions lower Taylor order by one each"; "Coordinatewise Taylor division in the remaining eight variables factors two additional differences" (17c:102–105) | R | *factorisation of the symbol through difference symbols* (proposal) | (c) |
| box-filter identity | 17c:365; ch11:1731 | No | An identity that moves a lattice difference through the block average: at 17c:365–366 it "gives `Σ_f\|∇_fM_{ef}\| ≤ C_j`"; at ch11:1731–1735 "`Δ_wΨ_i=Q_{i,w}Δ_w`". "Box filter" = average over a block | R for the two consequences; I for the name | cite the formula | (b) |
| completed (vector operator, kinetic matrix, inverse, quotient calculation) | 17t:86; 17c:64, 144, 170, 176, 300 | 17t:86–87 by formula | With the gauge-fixing term added: `H+dd*`; `𝒞⁻¹` its inverse (ch. 7) | R | *gauge-fixed operator `H+dd*`* | (c) |
| (finite) covariant (path) completion | 17m:28, 30, 34, 179 | 17m:30–33 | Extension of a finite jet to a gauge-covariant function, obtained by replacing each monomial by a plaquette / parallel-transported expression and correcting lower jets | R | *gauge-covariant extension of the jet* | (d) |
| infinitesimal gauge insertion `d`; background insertions `b,c` | 17:234–235; 17t:85, 96, 102 | No | `d`: differential of the gauge action (17t:182 "infinitesimal gauge map at U"); `b,c`: first and second derivatives of an operator in the background field (vertices) | R / I | *infinitesimal gauge map*; *vertices* | (c) |
| admissible (path) action | 17t:84; 17c:12 | No; pointer to ch. 7 ("the same admissible path action used in Chapter 7") | Not determined in these files | ? | cite the ch. 7 definition | (c) |
| twelve-plane coefficient convention | 17:235–236; 17t:120 | 17:235–236 | The normalisation of the functional `𝗾`: "Its normalization counts twelve ordered transverse planes", whence `R(μ)=12κ_G log μ+O(1)` (17t:122) | R | *with the normalisation of (17.…), which counts the twelve ordered pairs of directions* | (d) |
| regulated current; (scalar) regulator; regulator criterion / estimate / interval / factor | 17:152, 227, 249; 17t:3, 91, 104, 336, 382, 385, 428, 481, 487, 497; 17c:319, 392; 17m:354, 362 | 17:229 | The mass `μ` in `Γ_μ`; "regulator criterion" = hypotheses (17.regulator-input) / the list at 17t:404–411 | R | *mass regularisation*; *the hypotheses of §…* | (c) |
| (group-coordinate) contact identity | 17t:175, 229, 333, 414, 424, 496, 500 | Proposition 17t:229–237 | The identity (17.contact). Why "contact" is not explained; it is an algebraic identity, unrelated to the contact (coincident-point) terms of ch. 18–19 | D (object) / ? (name) | keep, cited by proposition number, with a remark that it is not a coincident-point term | (d) |
| chart velocity `𝒴_U`; left frame | 17t:188–197 | 17t:190 | `∂_s log(Ψ_s(e^zU)Ψ_s(U)⁻¹)`: the vector field in the moving left-exponential chart | D | keep | — |
| action-gradient terms | 17t:286, 332, 402, 473 | No | Terms of the form `DF[Z]` in (17.contact) | R | *terms `DS[Z]`, `DΓ[Y]`* | (d) |
| Haar coefficient `𝔥(Y)`; coefficient functional `𝗾`, `𝗹`, `𝗵`, `𝖼`; cubic momentum functional; lattice (coefficient) correction; anchored correction | 17:213–237; 17t:239, 288, 395, 482; 17m:351, 356 | 17:213–225; 17t:395 | Explicit Taylor-coefficient functionals; `𝔥(Y)=𝗵(div_Haar Y)`. "Lattice correction"/"anchored correction" = the term `𝖼` | D | keep symbols; drop the nicknames | — |
| trace functional `ρ`; raw divergence `div_raw`; raw vector coordinates | 17:179–183, 301; 17m:356, 462 | 17:164–181 | `ρ(x,y,z)=−2x−8y` on `E=ℝ³`, the coordinates of divergences "before imposing the Maxwell equation" | D | *coordinates before passing to the quotient by the equation of motion* | (c) |
| equation direction `v_i^eq`; `v_eom` | 17m:375, 385–386 | `v_i^eq` by formula 17m:386; the symbol `v_eom` is not introduced (it occurs only at 17m:385–386) | `v_eom` is the kernel vector `v=(0,0,1)` of the free quotient `s` (17:171–172). Indications: 17m:383 "in the notation of the stability argument", where 17:262–264 has "one-dimensional kernel `ℝv`" and "`v_i→v`"; the third coordinate of `E` is `Σ⟨F_bc,∂_aF_ac⟩` (17:169), the Maxwell-equation term; the subsection is titled "The equation direction" (17m:375); and 17m:386 has `v_i^eq → v_eom` | D for `v_i^eq`; I (strongly indicated) for `v_eom` | define `v_eom`; *kernel vector of `s`* | (d) |
| conserved line | 17:341 | Not here. Free statement: ch3:591–596, Proposition "Conserved tensor line", `{J ∈ 𝒯_{≤4}: div J=0} = ℝT^Max`. Interacting statement: ch14:258 ff., Section "The conserved stress line" (cf. ch14:1019 "the same centered conserved line as `J`"), to which 17:173 refers | "The conserved line gives `Z_i=ν_iT`": the conserved centred tensors of this type form a line. At 17:341 `Z_i` is a combination of the interacting transferred tensors and `T` the interacting stress tensor, so the statement used is the interacting one of ch. 14; that section was read only at ch14:257–272 and 1014–1021 | R for the free statement; I for the statement used at 17:341 | *one-dimensionality of the space of conserved tensors (Section 14.…)* | (d) |
| rates `e_i`, `q_i` (stability of the trace functional) | 17:261–289 | 17:284–285 | `e_i=exp((log log b_i)²/5)`, `q_i=exp((log log b_i)²/6)`. The text gives them no name; `q_i` "is a scalar bound, unrelated to the inserted densities of Chapter 11" (17:288–289) | D | keep symbols | — |
| same-family; common family; lattice family; one family | 17:100, 281, 295; 18:172; 19:12, 46, 56, 58, 112; MT:58; RG:36 | 19:15–23 | The single family of Wilson measures indexed by cutoff `N` and period `p`, with all choices fixed once | R | *for the same family of measures* | (c) |
| density identity | 17m:62 | 17m:63–66 (emphasised) | `div_Haar(FY)=∫𝒟_Yk f dU` | D | keep or *differentiated kernel identity* | — |
| density-valued (kernel) insertion; score source; zero-moment source | 17m:68, 155, 391, 400, 443, 459 | No | The factor `𝒟_Yk` inserted in the block integral in place of `k` | R | *the differentiated kernel `𝒟_Yk`* | (d) |
| complementary (marked sum, part, large-field estimate); failure | 17m:121–131, 321 | No | Terms in which some small-field or chart condition is violated somewhere in the connected component of the inserted factor ("Every term with a failure anywhere in the marked connected component … is kept in the complementary marked sum") | R | *large-field terms*; *violation of a small-field condition* | (c) |
| attach (a condition to its dependence support) | 17m:125 | No | "Attach this condition to its actual dependence support": count the failed chart condition with the set of links on which it depends | I | *assign the condition to the set of links it depends on* | (b) |
| ordinary (contribution, expansion, selections, logarithm, score, factors, cancellation) | 17m:86, 90, 92, 102, 112, 119, 131, 185 | No. 17m:104 says "By its definition in Chapter 9", but neither `Z_ord` nor `E_reg` occurs in chapter 9; ch9:150 has "the ordinary gas without large-field sites" | The whole small-field part of the expansion: `Z_ord=𝒞 exp[−βS−𝓛−E_reg]` (17m:106–107). Not a synonym of `regular`, which is one term of it (next row) | R | *small-field part* | (c) |
| regular (term, error, norm, power gain; regular local sources) | 17m:114, 115, 132, 166, 193, 290, 303; 17w:78, 93 | Not here; ch4:435–436 "A regular activity consists of a support `X_i`, an anchor `o_i ∈ X_i`, and a real Borel gauge-invariant function `E_i^reg` local on `X_i`" | The term `E_reg` in the exponent of `Z_ord`, built from the regular activities: "The regular term is estimated using its already proved differentiated regular norm" (17m:114–115). At 17w:78 ("The regular and large-field source recurrences") the word is paired against "large-field" and covers the whole non-large-field part | R (via ch. 4) for `E_reg`; I at 17w:78 | *the regular term `E_reg`*; not *small-field* | (c) |
| threshold coordinates; `𝒫_{5,t}`; threshold ball; fine threshold | 17m:143–148, 153, 272, 304, 378 | `𝒫_{5,t}` at 17m:145 | Coefficients rescaled by `t^{f−2}` (`f` = number of curvature factors); ball of radius `t` in link logarithms | R / I | *coefficients normalised by `t^{f−2}`* | (d) |
| crop; cropping; crop radius / tail | 17m:258, 279, 289, 310, 313 | 17m:258 | Restriction of the coarse field to radius `C_j(log β̂_k)²` | R | *truncation to a ball* | (b) |
| jet menu | 17m:255 | No; cf. ch11:161 "fixed finite menu" | Finite set of admitted tuples of polynomials (total scaling dimension ≤ 5) | R | *finite set of jets* | (b) |
| (deterministic) coefficient evaluation; coefficient recovery; coefficient conversions | 17m:251–301, 471 | No | Evaluation of the extraction functional on polynomial inputs without Gaussian fluctuation; inversion of a finite matrix of pairings | I | *value of the coefficient functional at `gz=0`*; *inversion of the finite system* | (d) |
| reserve (derivative, support, width) | 17w:84; 17m:49, 103, 198, 282 | No | An extra derivative order, or part of an exponential decay rate, kept unused for a later step ("one derivative reserve") | I | *one additional derivative*; *a strictly smaller rate* | (a) |
| units (of the exponential support exponent) | 17m:332, 413 | No | "Retaining two units of the exponential support exponent bounds these terms by `C exp[−2R/(2B_k+1)]`" (17m:413–414): keeping a decay rate 2 per unit of covering number | R | *keeping the factor `e^{−2n}` for covering number `n`* | (a) |
| gain; loss; cost; margin; absorb | cost: 24 (17t:105, 108, 110, 163, 478; 17c:119, 364; 17w:59, 73, 108, 115; 17m:45, 130, 172, 180, 261, 301, 427, 428, 434; 18:230, 256; 18r:33; RG:26). gain: 17c:351, 361, 366, 378; 17m:132, 187, 330; 18:256. loss: 17c:107; 17m:79, 166, 174, 417; 17w:91, 119; 18:128, 257 | No | As in Part II §2.6. RG:26 "a positive action cost is retained" = a lower bound on the action | I | *is bounded by*; *improves by a factor*; print the inequality | (a) |
| trial descent; descending graph; endpoint error | 17m:444, 461, 469, 470 | No; ch11:890 "Backward comparison of a local trial" | Fine-to-coarse propagation of a local lattice function compared with a normalised insertion | R (via ch. 11) | *backward comparison (Section 11.x)* | (d) |
| graph (descending graph; one-insertion graph contraction) | 17m:444; 18:124 | No; ch11:347 (section title "The one-insertion graph estimates"), ch11:911 "the bound on the graph of normalized local insertions" | Not glossed in these files or at the two ch. 11 places | ? | cite the ch. 11 estimate by number | (b) |
| vacuum bound `q_n`; positive-density estimate; positive partition estimate | 17m:433, 439; 17w:97 | Not here; ch11:801–812, 819 | `q` is the per-site exponent in the bound obtained from the lower bound on the partition function: "positivity gives `Z ≥ e^{v_0−V[…]}`", `q=2b_act+κ+βb_loc(ρ)+4D_G log(16/ρ)` (ch11:801–812). The "positive-density estimate in (11.replicated-bound)" is that bound; its exponent `(a_m/a_k)⁴q_k` in (11.root-bound) (ch11:819) is the `L_*⁴B_n⁸q_n` of 17m:436. "Positive partition estimate" (17w:97) is presumably the same lower bound | R (via ch. 11); I for 17w:97 | *the lower bound on the partition function, (11.replicated-bound)* | (b) |
| terminal norm bounds; accumulated pre-ratio column costs; inverse source-weight bounds; physical mark normalization; exterior discrepancy | 17m:426–442 | No | Named ch. 11 quantities; see §4.2. "Terminal" seems to mean the starting scale `k(n)` of the backward comparison | ? | cite equations | (b) |
| empty coefficient; empty density; denominator | 17w:88; 17m:418 | No; ch11:604, 773, 2101 | The coefficient of the empty source monomial, i.e. the density without insertions: "The empty coefficient is exactly one" (ch11:604); "the empty density, hence its partition function, unchanged" (ch11:2101). The denominator is its integral, the partition function | R (via ch. 11) | *the density without insertions*; *the partition function* | (b) |
| squarefree polynomial | 17w:86 | No; ch11:23 "the squarefree source algebra" | Polynomial in the nilpotent source variables (each of square zero) | R (via ch. 11) | *polynomial in the source variables `z_i`, `z_i²=0`* | (b) |
| cross-modes (pushed spectator cross-modes) | 17m:401 | No | Not determined; the phrase occurs once | ? | none proposed (meaning not determined) | (d) |

#### 1.3 Operator products (chapter 18)

| Term (variants) | Where | Defined? | Meaning; decisive quote | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| probe; probe word; probe family; probe coordinates | 18:38–77, 115, 168, 215, 222, 241 (16); 18r:37 (twice), 60, 62, 65 (5) | 18:38–39 | "A probe is a fixed word v at distinct nonzero positions. It defines `λ(A)=S(A(0)v)`". Different from the Part II probe (linear functional on jets, ch. 3). 17m:251 "fixed probe order" is probably the chapter 3 sense (§3.10) | D | *test configuration `v`*, *the functional `λ_v`*; rename one of the two | (c) |
| (unsymmetrized, symmetric) field reconstruction `H_d(w)`, `A_dw`, `B_dw`; reconstruction identity / comparison | 18:67, 82, 149, 212, 227, 228; 18r:7, 35 | 18:67–69, 84–85 | `H_d(w)=Σ b_α(w)u_α`: the field in `F_d` on which the functionals `b_α`, `\|α\|≤d`, take the same values as on the cluster | D | *the field in `F_d` with the same values of the functionals `b_α`, `\|α\|≤d`* (not a projection: a cluster word is not an element of a space containing `F_d`) | (c) |
| measurement | 18:73 | No | Evaluation of `b_α(w)` in the mixed correlations | R | *evaluation* | (c) |
| the mixed table | 18:72 | No | The mixed correlations `S`; `blueprint/notation.md` prescribes "family of Schwinger functions" | R (via notation.md) | *the mixed correlations `S`* | (b) |
| correlation-null fields; field-null spaces | 18:40; 19:68 | No | Fields all of whose correlations with separated spectators vanish; `F_d` is the quotient by them ("These functionals separate `F_d`, by the definition of correlation-null fields") | R | *fields with vanishing correlations*; *the null spaces of the correlations* | (d) |
| compression; compression algebra `𝔄`; compressed (limit, exterior words) | 18:19, 20, 186; 18r:14, 36; 19:98 | Not here; ch. 15 | `M(w)` is "the compression of a whole separated word `w`" (18:20), an element of the commutative compression algebra of ch. 15. Standard operator-theory word (compression of an operator to a subspace), used here as a noun for the resulting element; 19:98 "compresses whole words to the mixed ground space" | R | keep; borderline house use | (c) |
| cluster; cluster word; cluster labels | 18:6, 67–78, 123, 135, 140, 222, 247, 249, 404; 18r:65; RG:74 (15) | 18:6 | A group of insertions at mutual distance `O(r)` about a centre `o`. Third meaning of "cluster" in the book (cluster expansion; Part II: subsequential limit) | R | keep in ch. 18; avoid elsewhere | (c) |
| clearance; clear region | 18:76, 79, 215, 252 | 18:76–79 | Positive distance between the cluster (and its rotations) and the probe points. Same sense as Part II | R | *separation* | (c) |
| (marked, lattice) replacement; replacement error / estimate; `Z_D` | 18:21, 119, 133, 146, 158, 215, 240, 247, 251; 18r:30; RG:74 | 18:154–157 | `Z_D=M(wv)−M((H_D(τ_{−o}w))(o)v)`: error of replacing the cluster by one field | D | keep, defined | — |
| signed (residual, difference, replacement, local transport, effective activity, density) | 18:129, 158, 174, 248, 255, 413; 18r:21, 26; RG:73 | 18:129–131 | Before absolute values are taken, so that cancellations survive | R | *the difference itself (not its absolute value)* | (c) |
| same-history | 18:130, 146 | No; `history` is defined at ch11:18–19 (§3.5) | For the same history, i.e. the same fixed choice of kernels, couplings, paths and local representations | R (via ch. 11) | *along the same sequence of block transformations* | (d) |
| nilpotent marker (coefficient); markers; marks | 18:123, 124, 128; 17m:441 | No; RG:37–38 says it in plain words | Marker = auxiliary commuting variable with square zero attached to an insertion; in 18:124 "Markers may merge" and 18:128 "several marks" the word means the insertions themselves | R / I | *source variable `t_i` with `t_i²=0`*; *insertion* | (b) |
| source weights | 18:125; 17m:440 | No; ch11:192 | Weights given to the source variables in the norm | ? here | cite ch. 11 | (b) |
| eligibility condition | 18:127 | Not here; ch4:440–450; ch8:294–295 | An additional condition attached to a large-field activity: "A large-field activity has an exclusion support `Y_i`, a nonempty prescribed set `I_i^bad ⊂ Y_i`, and an additional Borel gauge-invariant eligibility test `𝓔_i^extra`" (ch4:440–442). It restricts which covers of the large-field set are allowed: "The exact rules for eligibility are part of the definition of an effective density; they may exclude some otherwise possible covers" (ch8:294–295). The rule itself is part of the data and is not stated | R (via ch. 4, 8) | *the additional gauge-invariant condition `𝓔^extra` of the activity* | (b) |
| raw (coefficient estimate, operator error) | 18:226, 231 | No | The bounds of Proposition 18.replacement-input for the unsymmetrised `H_D` | I | *the bounds of Proposition …* | (b) |
| physical inclusions; physical quotient; graded quotient comparison | 18:43, 130, 174; 18r:33 | Not here; ch14:210–212 | "Write `i_d:F_d^0→F_{d+1}^0` for the free inclusion, `j_d` for the physical inclusion" (ch14:210–212): physical = of the interacting field spaces, against free. So the physical inclusions are the `ι_{d,e}` between the `F_d`; "physical quotient" = `F_d` (inferred) | R (via ch. 14) for inclusions; I for quotient | *the inclusions `ι_{d,e}` of the interacting field spaces*; *the field space `F_d`* | (c) |
| moving field; moving (free) labels | 18:175; 17:97, 370 | No; ch14:238 | A sequence of labels/fields depending on the sequence index, convergent (17:97 "convergent moving free labels"; 17:370 "convergent moving labels") or of size `ε_m` at scale `m` (18:175). At 17:97, 370 the labels are elements of the free Maxwell spaces `𝓜_d^Max` (17:81) | R | *convergent sequences of labels* | (c) |
| normalized-null lemma | 18:183 | ch13:202–240 | Reference by nickname | — | cite by number | (d) |
| uniform in the number of (reflected) copies; replica number; repeated-word identity / bound; repeated copies; full-copy estimates | 17:130; 17w:120; 18:159, 185; 18r:6, 13, 20; 19:52, 91; RG:74 | 18:161–165 | Moment bounds `⟨(Z*Z)^k⟩ ≤ C^{2k}` with `C` independent of `k` | R | *with a constant independent of the number of reflected copies* (one phrase) | (d) |
| exterior (factors, words, separation); interior (difference, seminorms) | 18:251; 18r:9–12, 33, 36 | No; ch18lp:8, 154, 207, 238 use the words, also without definition | Exterior = the spectator word outside the cluster's cell; interior = supported inside its cell | I | *spectator*; *supported in the cell* | (c) |
| resolution heights | 18r:54–55 | No; the phrase occurs nowhere else under `chapters/` | Two of the parameters `θ_−<θ<θ_+` (ratios of scale logarithms to `T=log(1/r)`). "Letting the two resolution heights tend to one yields" the exponent `D+1−W`; since `Z_0=Wθ_++4n_cl(θ_+−θ)` (18r:32) must then tend to `W`, the two are presumably `θ` and `θ_+` | I | name the two parameters | (d) |
| crude and grid constants; grid configurations; low-coordinate errors; omitted degrees | 18r:29, 38–39, 51, 53 | No; they belong to the proof in ch18lp (searched, not read in full) | Quantities of the proof of Proposition 18.mixed-bound | ? here | cite | (d) |
| derivative descent; descending induction | 18r:48, 53 | No | Downward induction on the degree. Different from "trial descent" | R | *downward induction* | (c) |
| subtraction convention / prescription; pair weights `a_h`; selected pair; normal Taylor polynomial | 18:281–322, 352, 358 | 18:290–318 | Explicit and defined | D | keep ("selected pair" → *pair with `a_h≠0`*) | — |
| slots | 18:299 | No | Argument positions | I | *arguments* | (c) |
| contact projection; shell; one-shell estimate; child / parent operators; descendants | 18:257, 404–418 | No | Tree vocabulary for nested collision subsets; "shell" = region where `ρ` is comparable to one value | I | *in the region `ρ≤\|…\|≤2ρ`*; *operators of the nested subsets* | (c) |
| the source prescription; forest prescription | 18:411, 419 | No | "This explains the source prescription and its proposed sharper local-order bound": the prescription of the formal source. Leakage: the reader has no "source" | R (via notation.md, "unverified sharper source forest prescription") | *a degree-sensitive (forest-type) prescription* | (b) |
| unit removal | 18:430 | No | The property that inserting the identity field leaves correlations unchanged (wording of 17:33 and 19:153) | R | *invariance of the correlations under insertion of the identity* | (d) |

#### 1.4 Assembly, main theorem, reading guide

| Term | Where | Defined? | Meaning | Basis | Proposed equivalent | Cat. |
|---|---|---|---|---|---|---|
| phase; space of phases; phase hierarchies; character phase; selected / retained / chosen phase | MT:34, 35, 41, 45, 50, 73–95; RG:47; 19:40, 66–80, 107, 117, 139–144; 17:15, 31, 99, 130, 351; 18 (12) — 46 in all, one sense | ch15:8; MT:32–35 describes it without defining | A character of the commutative compression algebra; equivalently one component `S^ξ` of the integral decomposition | R in MT | acceptable; MT should say "(characters of a commutative algebra, Ch. 15)". `notation.md` warns not to read it as an extremal Gibbs state | (c) |
| polynomial labels; local labels; label basis elements | MT:26; RG:15, 43, 55, 56; 19:29, 36 | MT:26–27 parenthesis gives the grading only; ch2:58 | Part II sense (formal invariant polynomial). 19:29 ("act simultaneously on all labels") and 19:36 are plausibly this sense, not certainly | D (ch. 2) | keep; RG:55 "local labels" → *polynomial labels* | — |
| penalty parameter for the block transformation; soft-block penalty `b` | MT:12; 19:17 | — | Part II "block penalty" | R | one phrase in both places | — |
| admissible (physical) periods | MT:14–15, 19; 19:20–21 | Not in MT; ch10:193–197 | The periods `R_p=4(M+p+1)`, `p≥0`, where the integer `M` is chosen "large enough that the lattice side `R_p/a_m` meets the required lower bound at every step of [the first] plateau for all `p≥0`" (ch10:193–197). 19:20–21 ("admissible physical periods `R_p`") links the phrase to that formula | R (via ch. 10) | say "periods `R_p=4(M+p+1)`" or "periods in a fixed sequence `R_p→∞`" | (c) |
| normalizations of local observables; "normalized quantum field"; coefficient normalizations | MT:15; RG:13, 16; 19:25 | No | Scale-dependent linear maps on labels (ch. 11) | I | fine for an introduction | — |
| microscopic sections | 19:28 | Not here; ch11E:31–38 "Define the normalized microscopic section at the origin by `O^𝒱_{N,p}(v)` …" | The maps from labels to normalised lattice observables, "fixed before `N,p`" (19:28); the definition in ch11E was read only at its first lines | I | *the lattice representatives of the labels (Section 11.…)* | (d) |
| correlation responses; spectator responses | RG:18; 18:182 | Not here; ch13:119–122 | The one-slot response: "For `c ∈ V_d`, a fixed spectator list `v`, and a separated smooth test function `f`, define the one-slot response `L_{v,f}(c)=∫f(x_0,x)S_{n+1}(c(x_0),v(x))`" | R (via ch. 13) | *correlations with all other fields* | (c) |
| transporting all coefficients together | RG:17 | No | RG transfer of the coefficient vector | I | *by propagating … through the block steps* | (c) |
| positive action cost | RG:26 | No | Lower bound on the action in large-field regions | I | *a lower bound on the action* | (a) |
| scale schedule; stage; common trajectory | RG:32–36 | No | See §1.1 | — | — | (d) |
| slab operators / insertions / bounds | RG:44; 19:92, 103; 18:270 | ch14:86 | Operators from words supported in a slab `0<x^μ<h` | R (ch. 14) | keep | — |
| hierarchy | 19:60, 67 | No | Family of `n`-point correlations for all `n` | I | standard enough | — |
| fixed-input convergence; bounded approximations; annular estimates; common diagonal extraction; rank bounds; real approximation; moments for separating families; word reconstruction | 19:47–52, 89–105 | No | Pointers by nickname to earlier results | ? here | cite by theorem number | (d) |
| mixed ground space | 19:98–99 | ch15:7, 47 | The "zero-energy subspace of [the] reflection Hilbert space" of the mixture (ch15:7); "the ground space of the mixture" (ch15:47) | R (via ch. 15) | *zero-energy subspace of the reflection Hilbert space of the mixture* | (c) |
| exceptional vacua | 19:107 | Not here (the phrase occurs once); ch16:379–381; ch15:324–328 | "the zero-energy space is a line for almost every phase … To remove the exceptional set requires a bound uniform in `ξ`" (ch16:379–381); "we have not eliminated exceptional phases" (ch15:325). "Exceptional" refers to the `ν`-null set of phases on which the vacuum might not be unique, not to a kind of vector | R (via ch. 15, 16) | *non-uniqueness of the vacuum on the `ν`-null set of phases* | (d) |
| low-energy estimate | 19:107, 134 | ch16:424–428 | `μ_ξ{0<E≤u} ≤ Cu²`; 19:135 "bounds spectral mass near zero by a power" | R | keep | — |
| finite-list senses | 19:74 | No | Uniform for each fixed finite list of fields | I | *for every fixed finite list of fields* | (d) |
| ordered tails | 19:38 | Not here; ch13:213–214 | "the filter is generated by ordered tails: `p=P(k)` with `k≥k_0`, and `N=n(j)` with `j≥j_0(k)`": a filter in two indices (period and cutoff), the cutoff threshold depending on the period index | R (via ch. 13) | keep with its definition, or *along `N=n(j)→∞` first, then `p=P(k)→∞`*. Not *for all sufficiently large `N`*, which drops the period index | (d) |
| ordered period limit; joint ordered limit | 17m:338, 365 | No | Limits taken first in the cutoff, then in the period | I | *in the iterated limit `N→∞`, then `p→∞`* | (d) |
| rate-sensitive tensor cancellation; prescribed-radius squeeze | 19:126–127 | No | Nicknames for 17.coefficient and the monotonicity argument of 17.all-radii | I | cite | (d) |
| "source locations" | RG:82 | — | The formal source of the audits; the only mention of a "source" in the front matter | R | *locations in the formalisation* | (b) |

---

### 2. Part II terms in these chapters

#### 2.1 Same sense (2–3 references each)

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
- **score**: 17m:73–400 (12). Here the kernel score: a derivative of the block kernel relative to the kernel itself, as in the bound (17.kernel-score) `|D^r q_γ(u)| ≤ C_r(1+γ)^r q_γ(u)` (17m:17–18) and "its extra factor is a finite sum of smooth local kernel scores" (17m:73). The statistical sense (logarithmic derivative of a density); the reading is inferred from these two places.
- **spectator**: 17t:141; 17m:67, 394–418; 18:7, 74, 116, 141, 154, 182, 231; 18r:44; 19:29.
- **collision**: 18:5, 8, 281, 359, 399; MT:89.
- **flux; shell flux**: 17:99 ("Shell integrals"), 341–344; 17w:122.
- **covering number; support exponent**: 17m:331–332, 412–413.
- **width** (§4.2): 17c:106, 143, 164; 17m:35.
- **levels** (§4.2) = scales: §1.1.
- **word**, sense (i): all 12 occurrences (17:34, 44; 18:20, 38, 67, 154, 215; 18r:13, 36; 19:91, 98, 105); definition at ch14:23.
- **regular** (activity, norm, term): 17m:114, 132, 166; 17w:93. The regular term `E_reg` built from the regular activities `E_i^reg` of ch4:435–436; see the row in §1.2 for the wider use at 17w:78.
- **history**: see §3.5; defined at ch11:18–19.

#### 2.2 New senses of Part II words

Detailed in §3: `actual` (one further sense), `row` ("row mass"; every use is a row at a fixed output index), `test` (pairing), `label` (entry of a word; free Maxwell field), `mark` (insertion of a non-observable factor), `window` (three new senses), `source` (five senses), `probe`, `response` (curvature response `Ψ_i`; quadratic coefficient), `transport` (RG transfer), `plateau`, `primitive`, `defect`, `leg`, `amplitude` ("alias amplitude" = Fourier coefficient at alias `l`, 17c:61), `mass` (sum of kernel coefficients, 17t:42), `cluster`, `physical` (of the interacting field spaces), `descent`.

#### 2.3 Part II items marked inferred or undetermined that these chapters clarify

| Part II item | Clarification | Basis |
|---|---|---|
| regularity-stage index `J_m` (§4) | 17w:14–15: "Write `𝓛_j` for the ratio chosen at stage j, so `L_i=𝓛_{J_i}` with `J_i=J(i+1)` in the scale convention of Chapter 10". With ch10:25–29, 129–134: `J(m)` is a nondecreasing map from scales to stages; a stage fixes finitely many orders, weights and constants | R |
| moving comparison fields (§4) | Not used verbatim. "Moving" elsewhere means "depending on the sequence index": 17:97 "convergent moving free labels"; 18:175 "a moving field has coefficient size `ε_m` at scale m"; ch14:238 "convergent moving labels". Supports reading 3:576 as index-dependent comparison fields; still an inference | I |
| matching (§4.2) | 17c:301–303: "Matching replaces `S_stat` by an action with identical Taylor coefficients through field order four" | R |
| envelope (§4.2) | 17m:283: "`p(z)≥1` is a polynomial envelope for the finite Gaussian coordinates" — a majorising function. Part II leaves its own occurrence (6:1187) unglossed | R |
| inherited loop action (R/I) | 17m:106–107: `Z_ord=𝒞 exp[−βS−𝓛−E_reg]`; 17t:147–150: its Hessian is "a sum with two lattice differences on each leg", so it annihilates constant and affine fields | R |
| protected (I) | 17m:74–76: "On a protected dependence region the incoming measurable product remains fixed under the change of variables" | R |
| nonwrapping / wrapping (I) | No criterion, but a consequence: "a wrapping term has covering number at least `N_per/[10(2B_k+1)]−1`" (17m:331–332) | R (partial) |
| representative (§4.2) | 17c:112 "smooth representative `W_a`"; 17m:32 "plaquette and transported-path representative". For `W` the word distinguishes gauge representatives (`W_a`, `W_F`) of one tangent; it is not a name for the operator | R |
| output (in "output anchors", §4) | "output" consistently means the coarse side of a step or the image index of a map: 17c:352–361 "output link", "coarse output edge"; 17t:302. Supports the Part II reading; "output anchors" itself does not occur | I |
| eligible (Part II: an extra gauge-invariant event) | 18:127 "eligibility condition" is this sense; see §1.3 | R (via ch. 4, 8) |

Not present in these files: centered log determinant, seeded / unseeded, compulsory, Warnings, likelihood tests, witness, target (grep: no hits). `Lift` occurs once, as an ordinary verb of linear algebra (18:60 "Lift a quotient basis through it"), not in the Part II sense.

---

### 3. Multi-sense words

#### 3.1 `actual` — 41 occurrences (17: 3; 17w: 8; 17t: 10; 17c: 8; 17m: 10; 18: 1; 19: 1)

| Sense | Count | Lines |
|---|---|---|
| of this construction (the specific lattice object, as opposed to a continuum, perturbative or separately chosen one) | 24 | 17:236, 246; 17t:8 (twice), 95, 102, 126, 172, 404, 498; 17w:41, 66, 68, 71, 86, 97, 100, 124; 17c:71, 87; 17m:352, 433; 18:158; 19:47 |
| the tangent `W` / `W_a` and the gauge-covariant block average (Part II sense 1): actual stationary tangent, actual stationary pullback, actual response | 7 | 17c:8, 48, 112, 248; 17m:193, 263; 17t:157 |
| the true object versus an idealised or substituted model (new): actual conditional insertion vs deterministic evaluation; "an actual exponentially local spectator" vs a finite-range one | 4 | 17m:276, 284, 294, 409 |
| exact / emphatic | 4 | 17t:114; 17c:132, 242; 17m:125 |
| the running value (coupling `β_i` vs reference `b_i`; "actual coupling band") | 2 | 17:84; 17m:312 |

17t:157 ("the actual stationary pullback of the current defect, with the gauge-covariant block average frame correction") is counted with the tangent sense because it is contrasted with "the usual smooth transport bound `∇_f^rW_a=O(L^{-1-r})`" (17t:161–162). 17w:68 ("the product of the subsequent actual responses. It uses no replacement by a common stage's quadratic form") is borderline between the first and the third sense. The third sense is not "nonlinear against linearised": 17m:409 has nothing to do with nonlinearity. For the two readings of "actual tangent" see the row "stationary tangent" in §1.2.

No occurrence of the Part II senses "at the true background" or "determined by the configuration". Unclassifiable: none; the 24 in the first row are mostly deletable. Borderline assignments could move by two.

#### 3.2 `row` — 10 occurrences

Every use is a row of a matrix or kernel at a fixed output index; none is "the kernel of a translation-invariant operator".

- Rows of the curvature response `Ψ`: 17w:12 ("curvature-response row constants"; cf. ch11:1735 "`sup_x Σ_y|Q_{i,w}(x,y)| ≤ R L_i^{−|w|−2}`", the `R_{J_i}` of 17w:63).
- Rows of `W_s`: 17m:237 ("Let `A_x^{ab}(z)` be the physical row from coarse direction b at `⌊x/L⌋+z` to fine direction a at x"; the row depends on `x`), 245, 249, 260.
- Rows of `M_{ef}`: 17c:336 ("Its row mass is L"), 349, 367. Rows of `R_0`: 17c:280 ("a rough root-path row").
- Row of the 3×3 recursion matrix: 17c:237 (row sum).

"Row mass" = row sum. Proposed equivalent: *row of the kernel*, or *for fixed output index*; not *kernel* alone.

#### 3.3 `selected`, `selection`, `selects` — 19; `chosen` — 18

| Sense | Lines |
|---|---|
| the phase `ξ_*` (also "chosen", 17:15; "retained", 19:117) | 17:31, 351; MT:91, 93 |
| fixed by the construction or schedule | 17:11; 17w:21; 17c:135; 18:172; 19:19, 31 |
| subsequence / diagonal choice | 17m:446; 19:38, 112 |
| picked out by a formula | 17t:419, 454 |
| pairs with nonzero weight `a_h` | 18:297, 352, 358 |
| "finite ordinary selections" (17m:92): finite subfamilies of terms of the small-field expansion (ch9:157 "finite selections") | 17m:92 |

`chosen` (17:15, 101, 134, 456; 17w:14, 84; 17t:9; 17c:142, 176, 249; 17m:179, 197; 18:42, 183; 18r:38; 19:58, 111; RG:33): ordinary, except 17:15 ("the phase `ξ_*` chosen in Section …"), which is the phase sense of the first row.

#### 3.4 `window` — 18 in prose, and two `\input` file names (17:148, 150)

| Sense | Count | Lines |
|---|---|---|
| interval of radii `r(n,u)` | 4 | 17:129, 131, 146; 17w:6 |
| range of RG scales between `n` and the stopping scale | 11 | 17w:2, 37, 43, 49, 54, 55, 56, 102, 107, 124; 17m:429 |
| either of the two | 1 | 17w:7 ("requiring every window to lie inside a plateau": a plateau is a set of scales, but the sentence continues "would leave gaps in radius coverage") |
| compact set of separated configurations (ch. 14 sense) | 1 | 17:140 "Diagonalize finite degree, arity, window and derivative requests", parallel to ch14:225–226 "explicitly diagonalizing arity, degree, compact windows and errors". Strongly indicated, not explicit (I) |
| length of an average ("physical averaging window `ma_k`") | 1 | 17m:476 |

Notes. 17w:2 and 17w:124 ("windows crossing changes of stage") are counted as ranges of scales; since a radius window `r(n,·)` comes with the scales from `n` to its stopping scale, the two readings nearly coincide there (I). At 17:129 ("the strip removal and derivative-transport argument of Section 14 applies to these windows") the antecedent is the radius intervals, while chapter 14 runs that argument on "a compact separated window" (ch14:173).

The Part II sense (localisation neighbourhood `Ω_i`) does not occur.

#### 3.5 `history` — 9

All: one fixed choice of the data of the RG steps (17c:87, 391; 17w:103; 18:130, 146; 19:25, 27, 49). 19:25 "The same finite histories must define the coefficient normalizations of every local insertion". Not defined in these files; defined at ch11:18–19: "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations" (basis R via ch. 11). The Part II definition (ratios and averaging orders) is narrower. 17w:103 and 19:49 are the restarted history of ch11:734–741 (§1.1). Undetermined: 17w:71 "the actual free history".

#### 3.6 `source` — 21

| Sense | Count | Lines |
|---|---|---|
| the inserted differentiated-kernel factor `𝒟_Yk` ("full source", "zero-moment source", "score source") | 7 | 17m:68, 155, 391, 400, 412, 443, 459 |
| "regular (local) sources": the local expressions (`div_Haar Y − D𝓛[Y]` etc.) whose Taylor coefficient is extracted | 5 | 17m:193, 265, 291, 303, 307 |
| source variables / weights of ch. 11 | 2 | 18:125; 17m:440 |
| undetermined: "polynomial-source propagation constants", "regular and large-field source recurrences" (neither phrase occurs elsewhere under `chapters/`; perhaps the ch. 11 source variables) | 2 | 17w:12, 78 |
| inhomogeneous term of a recursion | 3 | 17c:132, 225, 245 |
| the formal source | 2 | 18:411; RG:82 |

#### 3.7 `mark`, `marked`, `marker` — 32 in prose (and the file name at 17:311)

- "marked" (27) = with insertions tracked by nilpotent variables, as in `notation.md`. With observable insertions: 17:119, 132; 17w:11, 124; 17c:316, 396; 18:9, 119, 146, 158, 173, 174, 240; 19:48. With the non-observable factor `𝒟_Yk` as the insertion (new use, covering most of 17m): 17t:145 ("retained as marked remainders"); 17m:72 ("an admissible marked conditional integral. Its extra factor is a finite sum of smooth local kernel scores"), 81, 84, 120, 121, 122 ("the marked connected component"), 150, 176, 381, 393, 411; also the section title 17m:2. Where to draw the line between the two is a matter of judgement.
- "mark(s)" = an insertion: 18:128; 17m:441.
- "marker" = nilpotent source variable: 18:123; = insertion: 18:124.
- Symbol `E_mark`: 17m:161.

#### 3.8 `test` — 16

- test function (standard): 12 — 17:69, 70; 18:8, 257, 304, 320, 339 (twice), 364, 405, 414, 415.
- "tested against" = evaluated in correlations with (pairing): 4 — 18:7, 215, 248; 18r:36. `notation.md` asks that the pairing be specified.

None of the Part II senses (condition, variable, location, indicator) occurs.

#### 3.9 `label` — 15 in prose (MT:18 is an `enumerate` option)

- polynomial label (Part II sense), 7: MT:26; RG:15, 43, 55, 56; 19:29, 36 (19:29 uncertain).
- the field entry `A_i` of a word `((x_i,A_i))` (ch14:23–26), 6: 18:140, 141, 205, 222; 18r:61, 64. Whether these are elements of `V_d` or of the quotient `F_d` is not stated (I).
- free Maxwell field, 2: 17:97 ("convergent moving free labels"), 370 ("convergent moving labels"). These are elements of the free Maxwell spaces `𝓜_d^Max`: 17:81 "`U_{i,d}:𝓜_d^Max→F_d`"; 17:320 "`β_i r_i^4U_{i,4}^{-1}Θ → −κ_G𝒪`" (R).
- `tag`: no occurrence.

#### 3.10 `probe` — 22

- ch. 18 sense (a word `v`, or the functional `S(A(0)v)`): 18 (16), 18r (5).
- 17m:251 "Choose `j` above the fixed probe order": probably the chapter 3 sense, not a third one. Context: 17m:240 "every vector polynomial `p` of degree less than `j`", 17m:252 "tuples of potential polynomials"; ch3:939 "the scalar order-`j` probes". Inferred, not settled.

#### 3.11 `response` — 13

| Sense | Count | Lines |
|---|---|---|
| the curvature response `Ψ_i` (17w:62 displays `Ψ_{n−1}⋯Ψ_ℓ`; ch11:647 "`J=H_{0,f}^{-1}TH_{0,c}` is the curvature response"; ch11:1729 "the actual installed curvature response `Ψ_i`"): "curvature-response row constants", "differentiated response estimate", "unequal responses", "actual responses" | 4 | 17w:11, 60, 67, 68 |
| the link tangent from coarse to fine fields (ch11:642 "the actual stationary forest response `W`"): "the actual response" = `W_a` (17m:193, with 17m:263); "the polynomial response" = `W_s`, in (17.polynomial-response) (17m:202); "the linear response" (19:159; by "exact polynomial preservation" the property of `W_s`, inferred) | 3 | 17m:193, 202; 19:159 |
| the stationary nonlinear fine field ("The stationary nonlinear response") | 1 | 17m:278 |
| second-order coefficient in the background field: "normalized quadratic response of `Γ_μ`", "regulated response" | 2 | 17t:90, 91 |
| "anchored vector response": the Hessian kernel of an anchored vector function (I) | 1 | 17:224 |
| one-slot response: correlation with other fields, defined at ch13:119–122 ("spectator responses", "correlation responses") | 2 | 18:182; RG:18 |

Part II reads 6:953 ("the stationary fine response to a coarse logarithmic field") as the image `a=𝒰_F h`; that it is the same map as `W` is an inference.

#### 3.12 `transport` — 13; `transfer` — 15

- RG transfer through block steps (7): 17t:3; 17c:322; 17m:377, 381; 18:130, 174; RG:17 ("transporting all coefficients together"). Same meaning as `transfer` (17:19, 202, 246, 253, 290, 295; 17t:6, 72, 73, 498; 17c:3, 241, 347; 17m:29, 467) and overlapping with `pullback` (17c:51, 77, 91, 208, 304; 17t:157, 159), `propagation` (17:132; 17w:12, 24, 52, 75, 91), `update` (17c:91, 340), `push` (17m:401), `descent`.
- conjugation of a covariance by linear maps (1): 17w:68 "each conditional covariance is transported by the product of the subsequent actual responses".
- the stationary-field map (Part II sense) (3): 17t:161; 17m:213, 221.
- parallel transport (1): 17m:32.
- "derivative-transport argument" (1): 17:128. It is the Proposition "Derivative transport and smooth comparison" (ch14:229–238): `r_kU_{k,d+1}^{-1}∂_aU_{k,d} → ∂_a^0`, i.e. conjugation of the derivative by the comparison maps (R via ch. 14).
- 17c:347 "its diagonal transfer is `C_jL⁴L⁻⁵`": here "transfer" is a numerical factor.

#### 3.13 `frame` — 16

- gauge frame (Part II): 14 — 17c:148, 161, 167, 248, 249, 255, 300, 370, 374, 375; 17m:13, 56; 17t:158, 331.
- left-trivialisation of the group chart: 17t:195.
- "with these same frames" (17w:122): undetermined; "frames" has no antecedent in 17w. Perhaps the comparison maps `U_{i,d}` (`notation.md`: frame = "local gauge choice, basis, or scaling map, according to type").

#### 3.14 Others

| Word | Senses and places |
|---|---|
| `table` | 1: 18:72 (the mixed correlations) |
| `phase` | 46, one sense (§1.4) |
| `word` | 12, one sense (§2.1) |
| `reconstruction` (17) | relativistic reconstruction (8): 17:16, 20; 18:32; 19:93, 105, 128, 162; RG:62. Field reconstruction `H_d` (8): 18:67, 82, 149, 212, 227, 228; 18r:7, 35. Fourier inversion (1): 17m:239 |
| `raw` (7 in prose) | before the quotient by the equation of motion: 17:180, 301; 17m:356, 462. Before radial-gauge substitution: 17c:202 (I). For the unsymmetrised reconstruction: 18:226, 231 |
| `physical` (11) | in continuum units: 17m:441, 476; 19:20, 33, 34; MT:14; RG:5, 60. Position-space: 17m:237. Of the interacting field spaces, against free (ch14:210–212): 18:43, 130 |
| `mixed` (11) | of the mixture over phases (9): 17:32; 18:15, 72, 185, 207, 221, 277, 340; 19:98. Cross terms: 17c:161. Ordinary: 17m:246 |
| `regular` (11) | the regular term `E_reg` and what is built from the regular activities (norm, error, sources, power gain): 17m:114, 115, 132, 166, 193, 290, 303; 17w:93. The whole non-large-field part, paired against "large-field": 17w:78. Non-singular: 17m:221, 227 |
| `ordinary` (13) | the whole small-field part (house; `Z_ord`, 17m:106–107): 17m:86, 90, 92, 102, 112, 119, 131, 185. Usual: 17m:8, 461, 479; 17t:196, 217 |
| `threshold` | lower bound on `β̂` (19 occurrences, §1.1); small-field threshold `t`, an upper bound on field size: 17c:316; 17m:153, 272, 304, 378, 427; small-`r` threshold: 18:165, 205; 18r:70; cutoff / translation thresholds (= `N` large): 18:165; 18r:20. 17m:197 "stage orders and thresholds" is not assigned |
| `tail` | all sufficiently large indices: "fixed-stage tail" (17c:135), "ordered tails" (19:38). The far part of a kernel, sum or support: 17c:259, 360; 17m:50, 52, 260, 261, 280, 313, 316, 416. Symbol `E_tail`: 17m:161, 165 |
| `strip` | analyticity strip in momentum: 17t:127; 17c:164, 179, 181, 196, 282. Coordinate-equality strips of ch. 14: 17:122, 128; 17w:118. Settled by ch14:179–200: the gradient bound is required "outside coordinate-equality strips of width `4δ_k`", `δ_k=M_k^c`; the grid has spacing `s_k=M_k^{−α_0}`; "strip removal" is the estimate that these strips "have volume `O(δ_k)`" and contribute `O((A_k^n+1)δ_k)` (R via ch. 14) |
| `mass` | physical mass / mass shell / mass gap; regulator mass `μ`; sum of kernel coefficients: 17t:42, 43; 17c:324, 336, 367; measure of a set: 17:70; 19:135 |
| `contraction` | strict contraction of norms: 17:252, 256; 17t:167, 172; 17c:136, 239, 395; 17m:234; 18:124. Tensor contraction with `R`: 17t:330, 416, 417, 419, 420 |
| `descent` | fine-to-coarse propagation: 17m:444, 461, 469. Downward induction on degree: 18r:48, 53 |
| `contact` | chart identity of ch. 17 (7), an algebraic identity; coincident-point terms of ch. 18–19 (12 + RG:64) |
| `unit` | identity field: 17:32, 40, 82, 401; 17m:380; 18:109, 382, 430; 19:63. Unit of measure: 17m:331, 416 ("level-`k` units"), and "two units of the … support exponent" (17m:332, 413). "unit endpoints" (17m:474): partly settled, see §4.2. Others ordinary |
| `kernel` | null space (17:172, 262; 17m:455); block probability kernel (17m:10–54, 391); Fourier/quadratic kernel (17:207; 17t:294; 17m:350, 352); correlation kernel (18:355). "the kernel identities" (17:308): "The next section proves them using the kernel identities"; the next section is 17m, on the block kernel `k` (17m:10–66, 396–398), so the identities are probably (17.kernel-divergence) and the two integrals at 17m:396–398, not those of `K_0`, `K_a` (I, likely, not explicit) |
| `column` | ch. 11 coefficient maps: 17w:11; 17m:428 (not determined here). Literal column sum: 17c:332, 336, 337. Column vectors / alias component: 17m:204, 232 |
| `centered` | zero-mean: 17:23, 44, 163, 290, 345, 351, 390, 402, 409; 19:122. 17:163 "centered degree-four symmetric hypercubic tensors" is this sense: ch14:261–264 "Centered means that each component has zero expectation" (also ch3:584–585). Centred difference: 17t:17; 17c:29 |
| `root` | block-tree base point (6, §2.1); rooted cluster expansion: 17m:80, 87, 118, 119, 400; "root estimate" (17w:93): the chessboard-seminorm bound obtained by "taking the number-of-cells root" (ch11:817–822), namely (11.n-mark-root) `‖R_I‖_root ≤ H^{−1/(16n)}` with "cell side … at most `a_kH^{b_j+5}`" (ch11:2072–2079), matching 17w:93–96 (R via ch. 11) |
| `price`, `pay`, `budget`, `receipt`, `detector`, `readout`, `tag` | no occurrence in prose |

---

### 4. Terms these chapters do not determine

#### 4.1 Determined by another chapter

These terms are used in chapters 17–19 without explanation; the cited passage elsewhere fixes them. Each passage was read at the cited lines only.

| Term | Where used | Settled by | Meaning | Basis |
|---|---|---|---|---|
| history | 17c:87, 391; 17w:103; 18:130, 146; 19:25, 27, 49 | ch11:18–19 | "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations" | R |
| restarted representation / histories; `B_n` | 17w:33, 102; 19:49 | ch11:734–741; ch11R:12–18 | History with the inverse coupling held constant below a comparison level; "The new representation at level `i` has radius `B_i=b(x_i)^2`" | R |
| equation calibration floor | 19:30 | ch11E:23–30 | Lower bound (11.calibration-floor) on the block ratio `L` at stage `j`, with an accompanying condition on `β̂_N` (§1.1) | R |
| root estimate | 17w:93 | ch11:817–822; 2072–2079 | The chessboard-seminorm bound (11.n-mark-root), "`‖R_I‖_root ≤ H^{−1/(16n)}`" (§3.14) | R |
| weight restoration; regular-restoration bounds | 17w:89, 93 | ch11:1374–1375 (subsection "Absorbing the larger source weight", label `ch11:weight-restoration`); ch11:1436, 1471 (lemmas "Regular weight restoration", "Large-field weight restoration"); ch11:2131 | Passage to the larger source weight; "Regular weight restoration therefore gives `H^{-1}`" | R |
| top polynomial extraction `T` | 17w:100 | ch11:1141–1146; 2085–2088 | "Construct `T` at the top level `k` from the actual insertion and its original same-insertion covariance"; a common localization map for the separating family. `notation.md` glosses `T` as "common polynomial extraction" | R |
| vacuum bound `q_n`; positive-density estimate | 17m:433, 439 | ch11:801–812, 819 | Per-site exponent `q` in the bound from the lower bound on the partition function, (11.replicated-bound) (§1.2) | R |
| replicate | 17m:432 | ch11:815–817 | Take a reflected tiling at scale `a_m` (§1.1) | R |
| strip removal; strip width `M_n^c`; scaled mesh; grid errors | 17:121–129; 17w:118 | ch14:174–200 | "coordinate-equality strips of width `4δ_k`", `δ_k=M_k^c`; grid spacing `s_k=M_k^{−α_0}`; error `ε_k` "on its grid"; the strips "have volume `O(δ_k)`" | R |
| derivative-transport argument | 17:128 | ch14:229–238 | Proposition "Derivative transport and smooth comparison": `r_kU_{k,d+1}^{-1}∂_aU_{k,d} → ∂_a^0` | R |
| centered (degree-four symmetric hypercubic tensors) | 17:163 | ch14:261–264; ch3:580–585 | "Centered means that each component has zero expectation" | R |
| conserved line | 17:341 | ch3:591–596 (free); ch14:258 ff. (interacting) | The conserved centred tensors form a line (§1.2) | R / I |
| ordered tails | 19:38 | ch13:213–214 | Filter generated by `p=P(k)`, `k≥k_0`, and `N=n(j)`, `j≥j_0(k)` (§1.4) | R |
| admissible (physical) periods | MT:14–15, 19; 19:20 | ch10:193–197 | `R_p=4(M+p+1)`, `p≥0` (§1.4) | R |
| exceptional vacua | 19:107 | ch16:379–381; ch15:324–328 | Refers to the `ν`-null exceptional set of phases (§1.4) | R |
| physical inclusions | 18:43 | ch14:210–212 | "`j_d` for the physical inclusion", against the free inclusion `i_d` | R |
| spectator responses; correlation responses | 18:182; RG:18 | ch13:119–122 | The one-slot response `L_{v,f}(c)` | R |
| eligibility condition | 18:127 | ch4:440–450; ch8:294–295 | The additional gauge-invariant test `𝓔^extra` of a large-field activity; the rule itself is data (§1.3) | R |
| what crosses in "first crossing" | 17:138; 17w:31–32; 17m:425, 432 | ch10:145–146; 17m:422–425, 433 | A difference of `τ_m=log(1/a_m)` (§1.1) | R; I at 17w:31 |
| empty coefficient / density; squarefree polynomial | 17w:86, 88; 17m:418 | ch11:23, 604, 773, 2101 | Coefficient of the empty source monomial; polynomial in the nilpotent source variables (§1.2) | R |
| "window … requests" | 17:140 | ch14:225–226 | Compact windows of separated configurations (§3.4) | I (strongly indicated) |
| "the kernel identities" | 17:308 | 17m:10–66, 396–398 | The block-kernel identities of the next section (§3.14) | I (likely) |
| positive partition estimate | 17w:97 | ch11:801–805 | Presumably the lower bound `Z ≥ …` obtained from positivity | I |

#### 4.2 Still undetermined, or settled only in part

| Term | Where | What can be said |
|---|---|---|
| `v_eom` | 17m:385, 386 | Symbol not introduced. By inference the kernel vector `v=(0,0,1)` of 17:172 (basis I, strongly indicated; §1.2) |
| unit endpoints | 17m:474 | Partly settled (I). "the trace is a forward difference of a degree-three primitive, whose invariant projection is a unit" (17m:379–380); at 17m:473–474 one averages over `m` consecutive differences, so the sum telescopes and the two endpoint terms are multiples of the identity field. The phrase occurs once |
| fixed probe order | 17m:251 | Probably the chapter 3 sense of probe (§3.10); not settled |
| actual free history | 17w:71 | — |
| protected-path errors | 17w:72 | Not defined. Related uses of "protected" (17m:74; Part II) narrow it but do not define it |
| fixed-ratio jet errors | 17w:72 | By 17c:138–143 and 17m:429–430 ("Fixed-ratio nonlinear jet constants"): errors of the nonlinear stationary jets, whose constants may depend on `L` (I) |
| finite incidence costs | 17w:72–73 | Partly: "incidence" bounds at ch11:208–342 |
| corrected free-subset polynomial | 17w:87 | Partly: ch11:2064–2071 has the free moments `G_I` and "the corrected coefficients" `R_I=∏F_i−Σ G_JR_{I∖J}` |
| polynomial-source propagation constants; (regular and large-field) source recurrences | 17w:12, 78 | Neither phrase occurs elsewhere under `chapters/`. "Linear propagation constants" (17w:52) are the same group `C_j` |
| bottom stage | 17w:97 | Whether `stage` here means a level is not determined (§1.1) |
| "with these same frames" | 17w:122 | §3.13 |
| admissible marked conditional integral | 17m:72 | "admissible" in the ch. 9/11 sense; not looked up |
| admissible (path) action | 17t:84; 17c:12 | Pointer to ch. 7; not looked up |
| normalized large-field majorants | 17m:414 | — |
| terminal norm bounds; accumulated pre-ratio column costs; inverse source-weight bounds; physical mark normalization; exterior discrepancy | 17m:426–442 | Ch. 11 quantities. "terminal" here seems to mean the starting scale `k(n)` of the backward comparison |
| cross-modes | 17m:401 | — |
| graph (descending graph; one-insertion graph contraction) | 17m:444; 18:124 | Used at ch11:347, 911 without definition |
| finite momentum approximation | 17m:362 | — |
| anchored marked support bound; signed local transport; graded quotient comparison | 18:174–175 | Nicknames for results of 18-lattice-products.tex / 18-graded-quotient.tex |
| crude and grid constants; grid configurations; low-coordinate errors; omitted degrees | 18r:29–53 | Quantities of the proof in 18-lattice-products.tex |
| fixed-input convergence; bounded approximations; real approximation | 19:47–50, 99 | Nicknames for results of ch. 9–10, 13, 15 |
| why "contact" in "contact identity" | 17t:175 | — |
| `E_stat`, `E_tail`, `E_mark` | 17m:161–165 | Only bounds are given for `E_stat`, `E_tail` (17m:163–165); `E_mark` is not bounded by name, only as "the marked remainder" (17m:176). `E_reg` in the same display is an error coefficient ("The regular error satisfies `t^{-2}ε_k^reg=…`", 17m:166–169) and reuses the symbol of 17m:107 |
| `B_n` at 17m:438 | 17m:438; 17w:33–34 | "`B_n=O((log β̂_n)²)`" against ch11R:15–18, `B_i=b(x_i)²` with `b(x)=⌈(log x)²⌉`. The arithmetic at 17m:436 (`L_*⁴B_n⁸q_n=O((log β̂_n)^{22})`) uses the `(log)²` size. Whether the two are the same `B` is not determined |

---

### 5. Synonym clusters

| Concept | Words in use | Proposed |
|---|---|---|
| scale index | level, scale, stage (wrongly), step | *scale* for the index, *step* for the map, *stage* only for `j` |
| RG transfer of a function or current | transfer, transport, pullback, propagation, update, push, descent | *transfer* (one word); *pull-back* only for `𝓘` |
| inhomogeneous term | source, forcing | *inhomogeneous term* |
| the identity field | unit, unit field, unit insertion, identity (MT:27; 19:153) | *identity* |
| other fields in a correlation | spectator, exterior factor / word, external positions (18:310) | *spectator* or *remaining insertions* |
| number of reflected copies | copies, reflected copies, replica number, repeated word, full-copy, replicate | one phrase |
| the phase `ξ_*` | chosen (17:15), selected (17:31), retained (19:117) | *the fixed phase `ξ_*`* |
| small-field part of the expansion | ordinary, small-field | *small-field part*. `regular` is not a member: it names the one term `E_reg` of the small-field exponent (17m:106–115), and must stay distinct |
| order in the field | field order, field degree, factor count | one of them; keep distinct from scaling dimension |
| the same Wilson family | same-family, common family, one family, selected family, selected lattice construction | *the same family of measures*. "Same history" is narrower (one fixed choice of kernels, couplings, paths and representations, ch11:18–19) and is not a synonym |
| `exp((log log β̂_n)²)` | `M_n = M_n^cut` (17:104), `H_n` (17w:29), `H` (17m:138) | one symbol |
| total cluster degree | `w_0` (18:135), `W` (18r:32, 58) | one symbol |
| coincident points | collision, contact, coincident points, diagonal | *coincident points*; *diagonal* for the set. The "contact identity" of ch. 17 does not belong here |
| unused extra regularity | reserve, margin, spare (17m:316) | *additional* |
| bound | cost, loss, gain, price-type phrases | print the inequality |
| annihilate | kill (17t:291; 17c:66, 113, 335; 17m:350; 18:59, 225), annihilate | *annihilate* / *vanish on* |

Two words that look like members of a cluster but are not: `representative` (of `W`: it distinguishes the gauge representatives `W_a`, `W_F`, §1.2) and `threshold` (a lower bound on `β̂` in "coupling threshold", but an upper bound on field size for the small-field threshold `t`, §3.14).

---

### 6. Overloaded symbols noticed

| Symbol | Meanings |
|---|---|
| `W`, `W_a`, `W_s`, `W_F` | The symbols are consistent across chapters 5, 7 and 17: `W_s` straight-average transport (ch5:1084); `W_a=W_s−d_{0,f}ERW_s`, the smooth representative (ch5:1108; 17m:263–264); `W_F` the forest representative (ch5:1151; ch7:574); `W` the derivative of the stationary substitution (17c:48–50). What varies is the phrase "actual (stationary) tangent": `W_a` at ch7:574 and 17m:263, an operator `W` that `W_a` replaces up to a fine gradient at 17c:48, 112 (§1.2). `notation.md`:242 ("the smooth gauge-fixed response `W_s` and the actual forest-coordinate response `W_a`") agrees with 17m:263 on which is actual; only its word "forest-coordinate" conflicts with ch5:1151, where the forest representative is `W_F`. Other uses of the letter: `W^{(1)},W^{(0)}` remainder operators (17t:339), `W_{H^b}` dilation (17w:106), `W^rad` (17c:192), `W_2` Wightman function (17:58), exponent `W` (18r:32) |
| `𝒲` | Fourier-type transform (17:51); subtraction operator (18:315) |
| `E_reg` | small-field term in the exponent (17m:107), built from the regular activities `E_i^reg` of ch4:436; error coefficient in (17.finite-sigma) (17m:161, 166–169) |
| `ρ` | trace functional (17:179); spectral measure `ρ_Θ` (17:55); smooth minimum distance (18:283); inner radius (18:247) |
| `H` | Hessian (17:234; 17t:181); `H_n` (17w:29), `H=e^h` (17m:138); orthogonal matrix (17:364); reconstruction `H_d(w)` (18:69); auxiliary degree, giving `H_H` (18:213) |
| `R` | `R(μ)=𝗾(Γ_μ)` (17:231); resolvent (17t:209), also in "`Ra=I`" (17t:106); `R_f,R_0` (17c:249–262); constants `R_{J_i}` (17w:63); inclusion `F_d→F_{d+1}` (18:55); rotation action `R_d(K)` (18:81); radius (18:247); distance (17m:412) |
| `D` | degree bound (17:110); tensor `D_ab` (17:158); `𝒟(μ)` (17:232); operator `D_b` (17t:348); covariance symbols `D_l,D` (17m:203); `𝒟_Yk` (17m:59); derivative |
| `L` | block ratio; `L=T^Max` (17:158); loop term `𝓛` (17m:107); ratio `𝓛_j` (17w:14); `L_{i,q}` (18:94); `L_h` (18:402); `L_*` (17m:433) |
| `Z` | vector (17t:218); `Z_i` (17:328); index `Z=X,D` (17:302); `Z_ord` (17m:92); `Z_γ` (17m:15); `Z_D` (18:155); compressed limit (18r:14); exponent `Z_0` (18r:32) |
| `T` | stress tensor; `T=\|k\|+μ` (17t:104); `T_b^{(r)}` (17t:349); `Tu=(u,Dz(0)u)` (17c:149); extraction `T` (17w:100); `T_n=(log β̂_n)^{48}` (17m:422); `T_{h,k}` (18:306); exponent variable (18r:42) |
| `t` | small-field threshold (17m:140); right inverse (17:262); momentum parameter (17:216); primitives `t_abc` (17t:72; flagged at 17c:315); distance (17:372); auxiliary degree (18r:31) |
| `q` | bound `q_i` (17:285; flagged at 17:288); primitives `q_a` (17t:62); density `q_γ` (17m:15); `q_n` (17m:439); quotient map (18:58); degree (18:94, 404); number of factors (18r:10); `q_h` (18:400); momentum |
| `b` | block penalty (19:17; 17m:14); reference coupling `b_i` (17:86); window parameter (17w:30); vertices `b,c` (17t:96); functionals `b_α` (18:46); coefficients `b_{y,f}` (17c:255) |
| `B` | radius `B_n` of the restarted representation (17w:33; 17m:438, with the open mismatch of §4.2); `B_k` in covering numbers (17m:332, 413); polynomial argument `P(B)` (17m:271); transferred tensors `B_i^L,B_i^X,B_i^D` (17:290); `B_dw` (18:84), map `B:F_{d+1}→F_d` (18:56); seminorm bounds `B`, `B_l` (18r:10–11) |
| `S` | correlations; lattice action (17t:180; 17m:107 — `notation.md` reserves `S` for correlations); ratio `a_ℓ/a_n` (17w:64); section `S_0` (18:57); `𝖲` (17:193); `𝒮` (17c:148) |
| `K` | kernels `K_0,K_a` (17t:23); `K_i` (17:293); kinetic symbols `K_f,K_c` (17c:58); rotation (18:81); compact set (18:273); Laplace kernels (17:426) |
| `M` | `M_n` (17:104); block average `M_a` (17t:20); operator `M_b` (17t:347); straight average (17c:277); compression `M(w)` (18:20); bound on `\|z_i\|` (18:138) |
| `A` | `A_i` (17:292); amplitude `A_l` (17c:61); coefficients (17t:306); kernel `A_x^{ab}` (17m:237); action `𝒜` (17t:137); `𝒜_l` (17m:223); interval length (17t:486); `A_dw` (18:84); spectator (17m:403); fields |
| `χ` | site indicator (17t:346); scalar correction (17m:210); cutoff (18:311); elsewhere the distance `χ(u)` |
| `j` | stage (`C_j`); smoothing order (17m:230, 239, 251, "order less than j"); current coefficient `j_k` (17m:152); current `j_a` (17:389); degree (18:98) |
| `n`, `k` | scale; arity (18:265); number of copies (`k` at 18:162, `n` at 18r:14); Taylor order `k` (18:279) |
| `e` | `e_i` (17:284); norms `e_r` (17c:222); variation `e_{x,c}(u)` (17:205); link |
| `τ` | trace field (17:26); `τ_m=log(1/a_m)` (defined ch10:145–146; used at 17m:423, 470); translation (18:75); path average (17c:256) |
| `f` | incoming density (17m:54); curvature-factor count (17m:144); plaquette field `f_ab` (17:186); fine link index (17c:352); test function (ch13:119) |
| `α`, `θ`, `c`, `h`, `u`, `p`, `N`, `G`, `V`, `E`, `I`, `J`, `λ`, `ν`, `δ`, `η`, `μ`, `ω`, `X` | each has three or more meanings across 17–18 (e.g. `X`: tensor 17:159, norm sum 17c:389) |

---

### 7. The ten most confusing terms

1. **`actual`** — 41 uses, five senses, 24 of them deletable; and the phrase "actual tangent" names `W_a` in one place (17m:263) and an operator `W` that `W_a` replaces in another (17c:48, 112), although the symbols themselves are consistent (§1.2, §6).
2. **`marked` / `mark` / `marker` / `source` / `score`** — five words around one construction (insertions tracked by nilpotent variables), with `source` in five senses; in 17m the "source" is a differentiated kernel, not an observable.
3. **`stage` / `level` / `plateau` / `window` / `stopping`** — the scale bookkeeping of §17.2; `window` means an interval of radii, a range of scales, a compact set of configurations and the length of an average.
4. **`history` / `same-history` / `same-family`** — `history` is not defined in these files (its definition is at ch11:18–19), yet 19:25–31 makes it a hypothesis of the main assembly.
5. **`transport` / `transfer` / `pullback` / `propagation` / `response`** — several words for moving an object through block steps; `transport` also names the stationary-field map, and `response` names two different operators (the link tangent `W` and the curvature response `Ψ_i`) besides four other things.
6. **`probe`** — defined in 18:38 with a meaning different from chapter 3; "tested against" for pairing.
7. **`ordinary` / `regular` / `complementary`** — unannounced names in 17m:86–132: `ordinary` is the whole small-field part, `regular` one term of it (`E_reg`), `complementary` the large-field part. The pointer "By its definition in Chapter 9" (17m:104) does not resolve by symbol.
8. **`request` / `reserve` / `cost` / `gain` / `pre-ratio`** — the accounting and program vocabulary of 17w and 17m.
9. **`raw` / `physical` (quotient, inclusion) / `reconstruction`** — `reconstruction` means both the Wightman reconstruction and the map `H_d`; `physical` means "interacting" here and "in continuum units" elsewhere.
10. **`low moments` / `exterior moments` / `equation direction`** — the key mechanism of the trace argument is named by three undefined phrases, and the symbol `v_eom` is used without being introduced.

Also worth a note for the first pages: **`phase`** (MT) is used without saying that it is a character of a commutative algebra, **`admissible` periods** is undefined in MT (the definition is `R_p=4(M+p+1)`, ch10:193–197), and 18:411 and RG:82 mention "the source".

**Jargon surviving only in labels** (not visible in the PDF): `ch17:current-suppliers`, `ch17:scalar-log-supplier`, `ch17:regulator-input`, `ch17:kernel-score`, `ch17:stable-functional`, `ch18:input`, `ch18:replacement-input`, `ch18:raw-replacement`, `ch19:conditional`, `ch19:conditional-trace` (the statements are no longer conditional), `ch15:selection`, `ch14:stress-line`, `ch11:detector-bound`, `ch11:replicated`, `ch10:shooting`.

---

### 8. Not read / not checked

- Read in full for the survey: all ten assigned files, Part II, and `blueprint/notation.md`.
- **Not read**: `chapters/18-lattice-products.tex` (352 lines) and `chapters/18-graded-quotient.tex` (131 lines). They were not in the assignment and are `\input` from `chapters/13-continuum-fields.tex:402–403`, not from chapter 18; they were only searched for definitions (resolution heights, exterior word, crude/grid exponent, probes).
- `figures/radius-windows.tex` and `figures/pair-subtraction.tex`: captions only.
- Definitions in other chapters (ch. 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16) were located by `grep` and read a few lines at a time; entries marked "via ch. …" rest on those excerpts, not on a full reading.
- Multi-sense classifications were made from a full reading plus `grep` line lists. The `actual`, `row`, `window`, `source`, `test`, `probe`, `transport`, `frame`, `reconstruction`, `physical` counts add up to the grep totals; borderline assignments (especially "of this construction" versus "emphatic" for `actual`) could move by two or three.
- No Lean source was consulted. No proposed equivalent was checked against the literature. §6 is a list of what was noticed, not a complete symbol audit.
- One mathematical point noticed, not pursued: the size of `B_n` at 17m:438 against ch11R:15–18 (§4.2).

**Sentences damaged by mechanical replacement: present state.** Four sentences that did not parse have been repaired in the text (line numbers unchanged): 17w:76 ("plus a coupling-threshold-controlled small error"), 17m:144 ("let `f` be the curvature-factor count"), 17m:284–285 ("the difference … is bounded by"), 17m:303 ("There are no invariant terms that are constant spacetime vectors or linear in the `𝔤`-valued field"). Still damaged:

| Place | Present text | Defect |
|---|---|---|
| 17t:159–160 | "the order-two pullback must annihilate its affine--affine and affine--quadratic polynomial moment conditions" | One satisfies conditions, or annihilates polynomials. 17c:24–25 has "the affine--affine and affine--quadratic polynomial cancellations" for the same thing; probably meant: "must have the affine–affine and affine–quadratic polynomial cancellations" (inferred) |
| 17c:359–360 | "Only a bounded number of coarse output edges are within the gauge-covariant block average and averaging patches; exponential coefficient tails control the rest." | Barely parses. Plausibly "within the supports of the block-average kernel `M_{ef}` and of the anchor average `K_0`" (inferred from 17c:349–357) |
| 19:152–154 | "Positivity at contacts, contact Ward identities, the fact that inserting the identity leaves correlations unchanged, and uniqueness of contact terms require additional normalization conditions." | A fact cannot require conditions. The item meant is the property at contacts that 18:430 still calls "unit removal" in the same list |
| 17t:157–158 | "with the gauge-covariant block average frame correction" | Noun pile after replacement |
| 17c:161 | "with all mixed gauge-covariant block average and frame terms included" | Noun pile after replacement |

Awkward but parsing: 18:127 "with its support, prescribed set of large-field sites and eligibility condition"; 19:99 "The real approximation and moments for separating families prove symmetries and the equality of field spaces".

---

### Changes folded in

Origin: B = independent audit, R = re-audit. "verified" = the cited chapter lines were opened for this fold and support the change.

**Header.** Notices "Audited" / "Status: reproduced as returned" replaced by one status paragraph; abbreviations for the chapter 11, 13, 14, 18 fragment files added.

**§1.1**
- `equation calibration floor`: meaning changed from a bound on `β̂_N` to a bound on the block ratio `L`, basis `?` → R (B error 1; verified at ch11E:23–30). The accompanying condition on `β̂_N` added (R D12; verified).
- `stage`: equivalent "parameter regime `j`" dropped (B; judgement).
- `level`: basis for `k_i=k(n_i)` lowered to I (B; verified at 17:84–87, 108).
- `window` row: four senses instead of two (B; verified, see §3.4).
- `stop backwards / first crossing`: crossing quantity identified as a difference of `τ_m` (B; verified at ch10:145–146, 17m:422–425, 432–433); "stopping levels" moved from 17w:101 to 17w:102 (B; verified).
- `request`: basis R → I (B; verified, no defining sentence).
- `coupling threshold`: count 17 → 19, two split occurrences added (B, R; verified by grep).
- `floor`: what is bounded stated for each use (R D11; verified at 17t:107).
- `shooting`: "ch10:210" was a label line; title line and prose lines given (B; verified).
- `restart`: `?` → R via ch. 11 (B; verified at ch11:734–741, ch11R:12–18); `B_n` mismatch recorded (B, R; verified, unresolved).
- `replicate`: "ch11:780" was a label line; supporting text ch11:815–817 (B error 6; verified).
- Rows added: `Diagonalize … requests`, `amplification`, `endpoint constants / factors`, `bottom stage / middle / output / top` (B omissions; verified at the cited lines).

**§1.2**
- `current defect`: equivalent changed to "defect of the lattice Ward identity" (B; verified at 17:194–195).
- `stationary tangent`: rewritten; the claimed inconsistency of the symbols removed, the two uses of the phrase "actual tangent" recorded (B error 2 and R D1; verified at ch5:1084, 1108, 1151, 1234, ch7:574, 17c:48–53, 112–113, 17m:263–264).
- `anchor average`: the phrases "component average `K_a`" and "difference primitive `K_a^t`" removed, as they are not in the text (B error 5; verified at 17t:19–43).
- `primitive`: equivalent "discrete potential" withdrawn (B; judgement).
- `leg`: 16 → 15; 17c:373 ("legitimate") removed (B; verified).
- `field order`: basis D → R (B; verified at 17c:222).
- `contact identity`: equivalent "chart identity" withdrawn (B; judgement).
- `equation direction` / `v_eom`: basis `?` → I with the indications (R D7; verified at 17:169–172, 262–264, 17m:375–386).
- `conserved line`: free and interacting statements cited, basis I → R / I (B, R D5; verified at ch3:591–596, ch14:258–264, 1019).
- Row "trace stability amplification `e_i`; stable functional" renamed "rates `e_i`, `q_i`": the two phrases are not in the text (B error 5; verified at 17:261–289).
- `ordinary`: meaning "the whole small-field part"; unresolved pointer at 17m:104 noted (B error 3, R D9; verified at 17m:104–115 and by grep of chapter 9). Row `regular` added (B error 3, R D8, D9; verified at ch4:435–436, 17w:78).
- `gain`: 17c:375 ("again") removed, 18:256 added (B; verified).
- `vacuum bound q_n`: split from the still-undetermined ch. 11 quantities, basis `?` → R via ch. 11 (B; verified at ch11:801–822).
- Rows added: `division`, `box-filter identity`, `admissible (path) action`, `twelve-plane coefficient convention`, `attach`, `units`, `graph`, `empty coefficient / density / denominator`, `squarefree polynomial`, `cross-modes` (B omissions; verified at the cited lines).

**§1.3**
- `probe`: 17m:251 no longer called a third sense (B; verified at ch3:939, 17m:240–252; still I).
- `field reconstruction`: equivalent "projection of the cluster onto `F_d`" replaced (B; judgement, verified against 18:67–74).
- `same-history`: basis I → R via ch11:18–19 (follows from B's `history`; verified).
- `eligibility condition`: `?` → R via ch. 4, 8 (R D6, B "partly settled"; verified at ch4:440–450, ch8:294–295).
- `physical inclusions`: I → R via ch14:210–212 (B; verified).
- `moving labels`: 17:370 has "moving labels" without "free"; the labels are free Maxwell fields (R, B; verified).
- `exterior / interior`: R → I (B; verified at 18r:9–12, ch18lp:8, 154, 207, 238).
- `resolution heights`: separated from the other proof quantities, R → I, the claim "defined in 18-lattice-products" removed (B; verified by grep and at 18r:28–58).
- `unit removal`: equivalent reworded, since the 19:153 sentence is itself defective (R D14; verified).
- Rows added: `correlation-null fields / field-null spaces`, `compression` (B omissions; verified).

**§1.4**
- `admissible periods`: `?` → R via ch10:193–197; lines MT:14–15, 19 (B, R; verified).
- `correlation responses`: I → R via ch13:119–122 (B; verified).
- `mixed ground space`: equivalent replaced by the text's own phrase (B; verified at ch15:7, 47).
- `exceptional vacua`: I → R via ch. 15, 16; equivalent replaced (B; verified).
- `ordered tails`: I → R via ch13:213–214; separated from "ordered period limit / joint ordered limit"; equivalent "for all large `N`" excluded (B, R E4; verified).
- `polynomial labels`: uncertainty of 19:29, 36 noted (B, R).
- Row added: `microscopic sections` (B omission; verified at 19:28, ch11E:31–38, basis I).

**§2**
- §2.1 `regular`: 17w:78 moved out, gloss added (B error 3, R D9). `score`: gloss added (R omission 9; verified at 17m:17–18, 73; I). `history`: pointer to ch11:18–19.
- §2.2: list adjusted to the §3 corrections.
- §2.3: `moving comparison fields` cites ch14:238 (ch14:250 not confirmed; own reading); `envelope` notes that Part II leaves 6:1187 unglossed (R E2); `representative` notes that it distinguishes representatives of `W` (R D2); row `eligible` added (R D6); `lift` removed from the "no hits" list: the verb occurs at 18:60 (own reading; verified).

**§3**
- §3.1 `actual`: 25 / 6 → 24 / 7, 17t:157 moved to the tangent sense; 17w:68 marked borderline; third sense relabelled (B; verified at 17t:156–162).
- §3.2 `row`: the two senses merged into "row at a fixed output index" (B, R; verified at 17m:237–238, 17c:237, 280, 336, ch11:1735).
- §3.3 `chosen`: 17:15 is the phase sense (B; verified).
- §3.4 `window`: 6 / 10 / undetermined → 4 / 11 / 1 ambiguous / 1 compact set / 1; 17w:2 moved to scales; 17:140 assigned to the ch. 14 sense (B, R D13; verified at ch14:173, 225–226; I).
- §3.5 `history`: definition ch11:18–19 cited, basis I → R (B; verified).
- §3.6 `source`: 17w:12, 78 moved to "undetermined" (B; verified that the phrases are not explained).
- §3.7 `mark`: 33 → 32 in prose plus the file name; extent of the `𝒟_Yk` use widened (B; verified at 17m:72–84).
- §3.9 `label`: 14 → 15; third sense (free Maxwell field) added (B; verified at 17:81, 97, 320, 370).
- §3.10 `probe`: see §1.3.
- §3.11 `response`: first sense split into curvature response `Ψ_i` and link tangent, with `W_a` / `W_s` distinguished (B error 4, R D3; verified at 17w:60–68, ch11:642–647, 1729, 17m:193, 202, 241–244, 263); last sense identified with the one-slot response (B; verified).
- §3.12 `transport` 12 → 13 (RG:17 added), `transfer` 17 → 15; 17w:68 separated; "derivative-transport" settled (B; verified).
- §3.14: `mixed` 12 → 11; `regular`, `ordinary`, `threshold` rewritten; rows `tail` added (B omission); `strip`, `centered`, `root`, `kernel identities`, `unit` updated with the settling passages (B; R D11; verified); `physical` gloss "interacting" (B).

**§4**
- Split into "determined by another chapter" (23 rows, from B's table and R §4; all cited passages verified except where a row says I) and "still undetermined". `unit endpoints` and `fixed-ratio jet errors` given partial glosses (R §4; verified at 17m:379–380, 473–474, 17c:138–143). `E_reg` double use, `E_mark` remark and the `B_n` mismatch added (R D8; B; verified).

**§5**
- `regular` removed from the small-field cluster (B error 3; verified).
- "same history" removed from the family cluster (own reading, from ch11:18–19).
- Remarks on `contact`, `representative`, `threshold` added (R D2, D11; verified).

**§6**
- `W` row rewritten (B error 2, R D1; verified; `notation.md`:242 read).
- `τ`: "`τ_m=log D_m` (17m:423)" replaced by `τ_m=log(1/a_m)`, ch10:145–146 (B error 7; verified).
- `E_reg`: ch4:436 added (R D8). Rows `B` and `f` added (R, B remarks; own reading of the cited lines).

**§7**
- Items 1, 3, 4, 5, 7, 9, 10 corrected to match the above; `ch17:stable-functional`, `ch11:replicated`, `ch10:shooting` added to the label list (B).

**§8**
- The two "typographical slips" (17w:76, 17m:284–285) are repaired in the text and were removed; a table of the sentences still damaged added (B overview list, R §6; all verified in the present text).

**Proposed corrections not applied**
- B error 2, as worded ("there is no inconsistency"): applied to the symbols only. The text (17c:48–53, 112 against 17m:263) supports R D1 that the phrase "actual tangent" has two uses; here B and R disagree and the text decides for R.
- B on `window`: 17w:7 counted as "range of scales (ambiguous)". Kept as a separate ambiguous line, since the sentence speaks of "gaps in radius coverage".
- B on `replicate` and `exceptional vacua` as fully settled: the operation and the reference of "exceptional" are settled; the single-use phrases themselves are not explained, and the rows say so.
- R D3 on 6:953, D10 (book-wide counts of `marked`), E1, E3 and the other items about Part I or Part II statements: outside this chapter group. Only the consequences for terms in these chapters were used.
- R D5 (cite the interacting conserved-line statement): applied as a pointer only; the statement in ch. 14 was not read in full, so no quotation is given.
- B's suggestion that "bottom stage" uses `stage` for a level: recorded as undetermined, as B itself could not decide.

### Verification status

**Checked against the text by a reader other than the survey's author** (the audit B, the re-audit R, or this fold):
- All quotations in §§1.1–1.4, 2.3, 3.1–3.6 (B: about 40 checked, none misquoted); the wrong line references found are corrected above.
- Counts by grep: `actual` 41, `row` 10, `selected` 19, `chosen` 18, `test` 16, `label` 15, `window` 18, `history` 9, `source` 21, `response` 13, `transport` 13, `transfer` 15, `probe` 22, `stage` 23, `phase` 46, `word` 12, `mixed` 11, `regular` 11, `ordinary` 13, `raw` 7, `leg` 15, `coupling threshold` 19 (B and R; `mixed`, `leg`, `label`, `transport`, `transfer`, `window`, `regular`, `ordinary`, `response`, `source`, `history`, `probe`, `frame` recounted for this fold).
- Rows confirmed by B for meaning, lines and basis (apart from the corrections above): in §1.1 stage, plateau, level, radius window, stop backwards / overshoot, pre-ratio, coupling threshold, schedule, floor, shooting, current depth; in §1.2 current defect, order at least four, low moments, stationary substitution, anchor average and mass, primitive, displacement, leg, channel, diagonal, source / forcing, completed, covariant completion, gauge and background insertions, regulator, contact identity, chart velocity, action-gradient terms, Haar coefficient, trace functional, equation direction, same-family, density identity, density-valued insertion, complementary, ordinary, threshold coordinates, crop, jet menu, coefficient evaluation, reserve, cost / gain / loss, trial descent; in §1.3 probe, field reconstruction, measurement, mixed table, cluster, clearance, replacement, signed, same-history, nilpotent marker, source weights, raw, moving field, normalized-null lemma, uniform in the number of copies, derivative descent, subtraction convention, slots, contact projection / shell, source prescription, unit removal; in §1.4 phase, polynomial labels, penalty parameter, normalizations, correlation responses, transporting, positive action cost, slab, hierarchy, the nickname pointers, low-energy estimate, finite-list senses, rate-sensitive cancellation / squeeze, source locations; §2.3 (nine rows); in §5 the three symbol rows and the `kill` list.
- All passages in other chapters cited in §4.1 and in the rows marked "via ch. …" that were changed or added here were opened for this fold (ch3:580–596, 939; ch4:434–450; ch5:1084, 1108, 1151, 1234; ch7:574; ch8:286–296; ch9:148–158; ch10:25–29, 121–147, 183–198, 208–214, 273, 818; ch11:16–24, 347, 604, 640–649, 732–742, 773, 778–823, 911, 1140–1146, 1372–1376, 1436, 1471, 1727–1736, 2062–2090, 2101, 2131; ch11E:22–38; ch11R:12–20; ch13:118–123, 211–215; ch13ba:283; ch14:22–27, 172–240, 256–272, 1014–1021; ch15:5–9, 45–48, 323–329; ch16:378–382, 424–428), as were 17w and 18r in full and the cited parts of 17, 17t, 17c, 17m, 18, 19, MT, RG.
- The present state of the damaged sentences in §8 (R and this fold).
- The labels `ch17:current-suppliers`, `ch18:raw-replacement`, `ch19:conditional` (B, R).

**Resting on the survey alone** (not rechecked by anyone):
- §6, except the rows `W`, `τ`, `E_reg`, `B`, `f`: the line references of the other symbol rows were not checked.
- §2.1: about half of the cited lines were spot-checked by B; the rest not.
- §5: checked only for meaning-changing merges and for the rows with line references.
- The sense-by-sense assignment of the 24 "of this construction" uses of `actual`, and of `stage`, `phase`, `reconstruction`, `raw`, `physical`, `contraction`, `mass`, `kernel`, `column`, `strip` (momentum sense) in §3.14.
- The survey's pointers ch10:118 (schedule), ch2:58 (polynomial labels), ch14:86 (slab), ch13:202–240 (normalized-null lemma), ch11:161, 192, 890 (seen here only as single lines), and its statements about `blueprint/notation.md` other than line 242.
- The rows of §1 not named above as confirmed or changed: `request` sense, `current depth`, `rates e_i, q_i` (formulas seen), and the new rows added from B's list of omissions, whose meanings are this fold's reading of the cited lines and have had no second reader: `amplification`, `endpoint constants`, `division`, `box-filter identity`, `attach`, `units`, `twelve-plane coefficient convention`, `compression`, `correlation-null fields`, `microscopic sections`, `tail`.
- All proposed equivalents: judged from general mathematical knowledge by the survey, B or R; none was checked against the literature.
- Not read by anyone in full: `18-lattice-products.tex`, `18-graded-quotient.tex`, the two figure files, and the interacting conserved-line section of chapter 14 beyond ch14:257–272, 1014–1021.
