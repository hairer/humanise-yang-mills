# House terminology in chapters 3–6: dictionary and harmonisation proposal

**Status:** draft audit, not an edit of the chapters. **Scope:** `chapters/03-maxwell.tex`, `04-blocking.tex`, `05-gaussian.tex`, `06-large-fields.tex` at upstream commit `7bec3925`. Line numbers refer to those files at that commit.

**Purpose.** These chapters use many words as technical terms that are not standard mathematical or mathematical-physics vocabulary. Most come from the names of the formal source or from programming and accounting metaphors. This note lists them, states what each means in the text, and proposes one standard equivalent per concept, the same in every chapter. It extends the short translation table in `blueprint/notation.md` ("Terminology translation and restrictions") and follows its rule: *do not translate a metaphor by guessing; its domain, codomain, quantifiers and estimates determine its meaning.*

**How to read the "Basis" column.**

- **D** — the text defines the term; the line is given.
- **R** — the meaning is read off an explicit sentence or formula, though the term is not formally defined.
- **I** — the meaning is inferred from context. Check before using the proposed replacement.
- **?** — the four chapters do not determine the meaning (section 4).

Line references marked † were reread during the audit (section 8); the others rest on the per-chapter surveys (section 7).

---

## 1. Words with several meanings

These are the most damaging, because the reader cannot tell which sense is meant. The proposal is to keep at most one sense per word.

### 1.1 `row` (ch. 5: 9+ lines; ch. 6: about 80 occurrences)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| kernel | 5:711–713, 738, 751, 826, 844, 849, 854, 1379 | Matrix-valued convolution kernel `K_ab(z)`, `z ∈ ℤ⁴`, of a translation-invariant operator on the infinite lattice. The text only introduces the notation ("Write a translation-invariant row as `K_ab(z)`"). "Adjacent-scale row": kernel of an operator between consecutive scales, with the position inside a block absorbed into the index set (inferred). | R | *kernel* (of a translation-invariant operator); *two-scale kernel* |
| symbol | 5:609, 624 | The same object as a matrix-valued Fourier multiplier with exponentially summable coefficients. | I | *symbol with exponentially decaying kernel* |
| operator | 5:858, 1124; 6:145† | A specific linear operator (`R`, `K`) with finite range or exponential decay. | R | *operator*, *finite-range operator* |
| component of the action vector | 5:853, 1054–1055; 6: about 68 of 82 occurrences, e.g. 101, 109–112, 186, 453, 1397–1398, 1434 | One component, indexed by its plaquette or edge, of the stacked vector whose half-square is the action; by extension the same component of its linearisation and of its affine approximation `Du + b_Y`. "Direct row": the single-plaquette component; "path row": a path component; "capped coarse rows": `v_c(p)`; "the rows `Φv_c`, `Φ_n v_c`": the comparison vectors; "complement-row", "null-row" (6:203, 1408): components of `N`. | R | *component* (of the curvature vector `X_f(p)`, of the affine map); *plaquette component*, *path component* |
| factorisation | 6:125, 136, 164, 377 | "Row factorization / realization / identities": the factorisation `C_ν*C_ν = H_ν` and the identities written through it. | R | *factorisation `C*C = H`* |
| matrix row | 3:628; 5:882, 996, 1346; 6: about 13, e.g. 217, 240, 280, 330, 554, 636, 812, 828, 907, 972, 994, 1501 | Literal, as in row and column sums. | — | keep |

### 1.2 `actual` (ch. 4: 4 lines; ch. 5: about 44; ch. 6: about 60)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| the nonlinear object | 4:293; 5: 12 prose uses (857, 912, 930, 986, 1000, 1078, 1118, 1234, 1289, 1304, 1311, 1321); 6:161, 165, 361, 445, 478, 490, 1554 | The gauge-covariant block average of chapter 4 and its linearisation `𝒬 = M + d₀R`, as opposed to the linear ("straight") average `M`, and objects built with it. | I | *gauge-covariant block average*; write the symbol |
| at the true background | 6: about 26 uses, e.g. 15, 183, 439, 463, 466, 468, 515, 542, 1397–1400, 1551 | Nonlinear or evaluated at the non-flat background, as opposed to the flat or linearised model ("without identifying actual and flat matrices", 6:468; "the actual nonlinear row … its actual affine approximation", 6:1397). The most frequent sense in chapter 6; absent from chapter 5. | I | *at the background field `V`*; *nonlinear*; *non-flat* |
| the running value | 4:407, 418, 533; 6:878, 1155 | The coupling `β ∈ [β̂/2, 2β̂]` ("the actual coupling band"), as opposed to the reference value `β̂_m`. | R | *the coupling `β`* vs *the reference coupling `β̂`* |
| of this construction | 5:302, 751, 782, 1324, 1379, 1380; 6: about 11 uses, e.g. 137 ("rows actually used"), 305, 342, 1022, 1162 | The specific kernels, parameters or action fixed by the construction, as opposed to an arbitrary admissible choice. | I | delete, or *the … constructed above* |
| exact (emphatic) | 5:1052, 1071, 1303, 1374, 1382 | "Its actual quadratic Taylor coefficient": the true coefficient, not an approximation; 5:1057 calls the same hypothesis "an exact coefficient condition". | R | *exact*, or delete |
| determined by the configuration | 6:78, 1343 | "The actual coarse large-field set", as opposed to the stored or selected one ("the stored coarse large-field indicators equal the actual coarse large-field indicators"). | R | *the large-field set of the configuration* |

`selected` and `chosen` are used as near-synonyms of the last sense (5:738, 858, 1314; 6:134–177, 362). Proposal: delete or replace by *fixed*.

### 1.3 `selection`, `selected`, `selector`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| large-field selection | 6:49–51 and about 30 further | A triple `A = (A_f, A_n, A_c)` of fine plaquettes, coarse edges and coarse sites. It is a chosen index, not the set determined by the configuration: on `A_f` and `A_n` the variables are required to be at least moderately large (`r_p ≥ t_f/4`, `n_e ≥ W t_f`), off them at most `t_f/2`, `2W t_f` (6:56–59), so the thresholds overlap. | D | *admissible large-field index set* `A`; keep it distinct from `Bad_m(U)` (section 2.4) |
| retained | 6:1405, 1435, 491–505 | A component of the affine map kept in `D` (sense 5 of `row`). | R | *retained* |
| chosen | 4:160, 210, 383, 393, 456, 616; 5 and 6 passim | Chosen by the random index, or fixed by the construction. | I | *chosen*; *for every value of `α`* |

In chapter 6 a "selected row" (retained component) lies far from the "selected set" (large-field set); the two senses must be separated.

### 1.4 `test`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| condition | 4:65–106, 209 ff.; 5:967 | A Borel condition on the configuration deciding which case of a definition applies ("loop test", "eligibility test", "minimum-cost test"). The minimum-cost test compares the minimum of the block-average objective `P_e` with `ε_pred` (4:391†). | I | *condition*; *smallness condition* |
| variable | 6:320, 337, 604 | The numbers `r_p`, `n_e` compared with thresholds ("every fine or mismatch test … is at most `t_hi`"). | R | *plaquette and edge variables* |
| location | 6:19, 54, 79, 89, 323, 416, 1156, 1162, 1329, 1349 | The plaquette or mismatch edge itself ("on all tests meeting `A^[5B]`", "tests exceeding `t_hi`"). The most frequent sense in chapter 6. | R | *plaquettes and edges* |
| indicator | 4:481–493; 6:83, 109, 231, 687, 776, 920, 1324, 1340, 1416 | The indicator of such a condition; `χ^rel` ("relaxed small-field test") is `1{χ(U_p) ≤ t_m e^{dist/R^rel} for every p}`. Not a smooth cutoff: "fixed Borel tests. Their indicators are not differentiated" (6:687). | D | *indicator of the small-field condition* |
| test function | elsewhere in the book | Standard. | — | keep; reserve *test* for this |

This agrees with `blueprint/notation.md`, which reserves "test" for test functions.

### 1.5 `label`, `tag`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| formal polynomial | 3:524, 677, 687, 777 (def. ch. 2:58) | An element of `V_d`, a formal invariant polynomial in jet variables. | D | *polynomial label* (house term, defined; keep) |
| random index | 4:78†, 209–217†, 316; 5:948–970; 6:63, 87, 363, 486, 1108, 1344 | The auxiliary discrete variable `α` with law `λ(U,α)` recording which case of the frame and block-average definition is used. "Tag" is the same object. | D (4:217) | *auxiliary index `α`*; drop "tag" |
| index | 4:322, 330, 539; 6:1168, 1236, 1317 | Index of a path or activity; in ch. 6 the index stands for the term. | R | *index*; *term* |

### 1.6 `response`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| two-point function | 3:409–451, 899, 975 | `y ↦` two-point function of the linear field `ℓ_P(F)(0)` with `F(y)`. | D (3:409) | *two-point function with source `ℓ_P`* |
| variation operator | 3:657, 1084, 1086 | A candidate linear map on local fields giving an infinitesimal symmetry variation. | I | *infinitesimal variation*; *linear map on local fields* |
| term of a sum | 3:964 | "The third response": the third term of the Ward sum. | I | *third term* |
| stationary point | 6:947, 953, 967, 972, 1493, 1545 | "The stationary fine response to a coarse logarithmic field `h`", `a = 𝒰_F h` (6:953). The text names it without a formula; that it is the critical point of the quadratic form of chapter 5 is inferred. 6:846 "block average response" may be a different object. | R / I | *stationary (critical) fine field*; say *minimiser* only where a gap is proved |

### 1.7 `transport`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| stationary-field map | 5:453–534 and about 20 further; 6:135, 161 | `W`: coarse field ↦ stationary fine field of the Gaussian block step (`QW = I − b⁻¹K_c`; 5:105 "sends a coarse field to the stationary fine field"), and its companion `T` on two-forms. Minimality is asserted only for specific objects (5:1118, 1143). | R | *stationary-field operator `W`*; *induced map `T` on curvatures* |
| image under a lattice symmetry | 6:966 | "Each signed orientation with its transported forest". | R | *image of the forest under the symmetry* |
| parallel transport | 5:1003, 1008; 6:179–186, 217 | Holonomy along a path; "transported kernel" = flat kernel made gauge-covariant by parallel transport along fixed paths. | R | *parallel transport*; *covariantised kernel* |

### 1.8 Other words with two or three senses

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

## 2. Dictionary by theme

One row per concept. Chapters are abbreviated `3`–`6`.

### 2.1 Scales, lattices and renormalisation steps

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

### 2.2 Gauge choices and the block average

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

### 2.3 Effective action and its pieces

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

### 2.4 Large-field regions, supports and localisation

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

### 2.5 Local fields and Ward identities (chapter 3)

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

### 2.6 Estimates: accounting and bookkeeping vocabulary

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

## 3. Synonym clusters to reduce to one word

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

## 4. Terms whose meaning chapters 3–6 do not determine

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

### 4.1 Terms first listed as undetermined and resolved by the independent check

| Term | Where | Meaning | Basis |
|---|---|---|---|
| internal rotation defect | 3:910, 1027; ch. 14:932 | `[L(K), L(M)] − L([K, M])`: the failure of the rotation generators to act as a Lie-algebra representation (ch. 14: "the internal defect `[L(K),L(M)]−L([K,M])` has zero correlation sums"). | R (ch. 14) |
| connected covering number `c_B(S)` | 4:587–589; 6:1172, 1296 | Defined in chapter 4 as `cov_B(X)`: the minimum number of radius-`B` periodic balls whose union is connected in the nearest-neighbour graph and covers `X`. Chapter 6 writes `c_B`. | D |
| terminal fine metric | 6:174–175 | The fine metric at the ultraviolet cutoff scale `N` ("at Wilson initialization"), unmodified (`ζ_f = 0`). "Terminal" as in section 2.1. | R |
| pre-`L` factor / pre-`L` excess estimate | 5:1021; 6:356, 517–518 | A bound whose constant is fixed before `L` is chosen, hence independent of `L` ("the excess constant in (macro-comparison), which is needed before `L` is chosen"). | R |
| stationary-field estimates | 4:166 | The estimates for the stationary background of chapter 5, which use analyticity of the frame (5:950–959). | I |

### 4.2 House terms not yet glossed in detail

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

## 5. Symbols with several meanings

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

## 6. Suggested order of work

1. Fix the eleven multi-sense words of section 1; each change is local once the sense is identified.
2. Resolve the section 4 terms with the author or the formal source; do not replace them by guesswork.
3. Apply the synonym reductions of section 3 mechanically.
4. Either define once and keep, or replace, the house terms that are harmless when defined (`polynomial label`, `insertion`, `word` in sense (i), `history`, `smoothing order`, `forest coordinates`, `Ward sum`).
5. Rename the Lean-flavoured equation labels (`ch05:horizon-*`, `ch05:path-budget`, `ch05:actual-bridge`, `ch04:tag-law`, `ch04:predictor-*`) only if labels are being touched anyway; they do not appear in the PDF.

---

## 7. Method and limits

- **Data gathering.** Three independent agent surveys, one for chapters 3–4, one for chapter 5 and one for chapter 6, each reading its chapters in full and reporting every non-standard term with line numbers, the decisive sentence, and whether the meaning was read or inferred. They returned 34 + 48, 69 and 93 entries.
- **Harmonisation.** The entries were merged by concept, the proposed equivalents made uniform across chapters and aligned with `blueprint/notation.md`.
- **Self-audit** (section 8) and **independent check** by a fresh agent (section 9).
- **Not done.** No formal-source declaration was consulted, so no claim is made about which Lean names the terms come from. No proposed equivalent was checked against the literature (Bałaban, Bałaban–Feldman–Knörrer–Trubowitz or others). Sections 3 and 5 were not checked row by row by anyone. All of this is agent work and needs a mathematician's review; entries with basis **I** in particular may misread the text.
- **Agent assistance.** Claude Code (Claude Fable 5.2), with three subagents for the surveys and a fourth, given only this note and the chapter files, for the independent check.
- **The † marks** on line references record what was reread in the self-audit. Rows rewritten after the independent check carry no marks.

## 8. Self-audit record

A script extracted every chapter-and-line reference from the tables (421 references) and tested whether the cited lines contain the term; 409 matched, and of the other 12 three were wrong line numbers and nine were artefacts of the matcher. The defining passages of about 45 entries were reread. This pass corrected three line numbers and four entries (`actual`, `comparison term`, `window`, `transport`). It was done by the agent that wrote the note, and the independent check below shows it missed a good deal.

## 9. Independent check

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
