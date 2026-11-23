# House terminology in chapters 3–6: dictionary and harmonisation proposal

**Status:** draft audit, not an edit of the chapters. **Scope:** `chapters/03-maxwell.tex`, `04-blocking.tex`, `05-gaussian.tex`, `06-large-fields.tex` at upstream commit `7bec3925`. Line numbers refer to those files at that commit.

**Purpose.** These chapters use many words as technical terms that are not standard mathematical or mathematical-physics vocabulary. Most come from the names of the formal source or from programming and accounting metaphors. This note lists them, states what each means in the text, and proposes one standard equivalent per concept, the same in every chapter. It extends the short translation table in `blueprint/notation.md` ("Terminology translation and restrictions") and follows its rule: *do not translate a metaphor by guessing; its domain, codomain, quantifiers and estimates determine its meaning.*

**How to read the "Basis" column.**

- **D** — the text defines the term; the line is given.
- **R** — the meaning is read off an explicit sentence or formula, though the term is not formally defined.
- **I** — the meaning is inferred from context. Check before using the proposed replacement.
- **?** — the four chapters do not determine the meaning (section 4).

Entries marked † were rechecked against the text during the harmonisation pass; the others rest on the per-chapter surveys (section 7).

---

## 1. Words with several meanings

These are the most damaging, because the reader cannot tell which sense is meant. The proposal is to keep at most one sense per word.

### 1.1 `row` (ch. 5: 9+ lines; ch. 6: about 80 occurrences)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| kernel | 5:711–713†, 738, 751, 826, 844–854, 1379 | Matrix-valued convolution kernel `K_ab(z)`, `z ∈ ℤ⁴`, of a translation-invariant operator on the infinite lattice. "Adjacent-scale row": kernel of an operator between consecutive scales, invariant under coarse translations, with the position inside a block absorbed into the index set. | D (semi) | *kernel* (of a translation-invariant operator); *two-scale kernel* |
| symbol | 5:609, 624 | The same object as a matrix-valued Fourier multiplier with exponentially summable coefficients. | I | *symbol with exponentially decaying kernel* |
| operator | 5:858, 1124; 6:145† | A specific linear operator (`R`, `K`) with finite range or exponential decay. | R | *operator*, *finite-range operator* |
| term of the action | 5:853, 1054–1055; 6:101†, 137, 1434 | A summand of the effective action: the single-plaquette term ("direct row") or a path term ("path row"). Its "curvature row" is the corresponding component of the local curvature vector `X_f(p)`. | I | *plaquette term*, *path term*; *component of `X_f(p)`* |
| component of an affine map | 6:446–455† | One component of the vector `Du + b_Y` ("affine stack"); "a row is retained when its stencil meets an active edge". | R | *component*, *retained component* |
| matrix row | 3:628, 638; 5:882, 996, 1346; 6:217, 554 | Literal, as in row and column sums. | — | keep |

### 1.2 `actual` (ch. 4: 4 lines; ch. 5: about 44; ch. 6: about 60)

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| the nonlinear object | 4:293; 5:912 ff.; 6:15, 78 | The gauge-covariant block average of chapter 4 and its linearisation `𝒬 = M + d₀R`, as opposed to the linear ("straight") average `M`. | I | *gauge-covariant block average*; write the symbol |
| at the true background | 6:137, 141, 161, 468 | Evaluated at the non-flat background field, as opposed to the flat (translation-invariant) model. | I | *at the background field `V`*; *non-flat* |
| the running value | 4:407, 418, 533; 6:406 | The coupling `β ∈ [β̂/2, 2β̂]`, as opposed to the reference value `β̂_m`. | R | *the coupling `β`* vs *the reference coupling `β̂`* |
| of this construction | 5:751, 782, 1057, 1379 and elsewhere | The specific kernels, parameters or action fixed by the construction, as opposed to an arbitrary admissible choice. | I | delete, or *the … constructed above* |

`selected` and `chosen` are used as near-synonyms of the last sense (5:738, 858, 1314; 6:134–177, 362). Proposal: delete or replace by *fixed*.

### 1.3 `selection`, `selected`, `selector`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| large-field set | 6:49–51† and about 40 further | A triple `A = (A_f, A_n, A_c)` of fine plaquettes, coarse edges and coarse sites at which the small-field conditions are allowed to fail. | D | *large-field set* `A`; *large-field plaquettes / edges / sites* |
| retained | 6:1405, 1435, 491–505 | A component of the affine map kept in `D` (sense 5 of `row`). | R | *retained* |
| chosen | 4:160, 210, 383, 393, 456, 616; 5 and 6 passim | Chosen by the random index, or fixed by the construction. | I | *chosen*; *for every value of `α`* |

In chapter 6 a "selected row" (retained component) lies far from the "selected set" (large-field set); the two senses must be separated.

### 1.4 `test`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| condition | 4:65–106, 209 ff.; 5:967 | A Borel condition on the configuration deciding which case of a definition applies ("loop test", "eligibility test", "minimum-cost test"). The minimum-cost test compares the minimum of the block-average objective `P_e` with `ε_pred` (4:391†). | I | *condition*; *smallness condition* |
| variable | 6:54† | The numbers `r_p`, `n_e` compared with thresholds. | R | *plaquette and edge variables* |
| location | 6:89† | The plaquette or edge itself ("tests exceeding `t_hi`"). | R | *plaquettes and edges* |
| cutoff | 6:108, 687 | A smooth cutoff function `χ^rel` ("relaxed small-field test"). | R | *cutoff function* |
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
| minimiser | 6:846, 947–972, 1493, 1545 | Linear map from the coarse field to the fine critical point of the quadratic form. | D (6:953) | *minimiser*; *background-field operator* |

### 1.7 `transport`

| Sense | Where | Meaning | Basis | Proposed wording |
|---|---|---|---|---|
| minimiser map | 5:453–534 and about 20 further; 6:135, 161 | `W`: coarse field ↦ stationary fine field of the Gaussian block step (`QW = I − b⁻¹K_c`), and its companion `T` on two-forms. | R | *minimiser operator `W`* (Bałaban's `H_k`); *induced map `T` on curvatures* |
| parallel transport | 5:1003, 1008; 6:179–186, 217 | Holonomy along a path; "transported kernel" = flat kernel made gauge-covariant by parallel transport along fixed paths. | R | *parallel transport*; *covariantised kernel* |

### 1.8 Other words with two or three senses

| Word | Senses and places | Basis | Proposed wording |
|---|---|---|---|
| `anchor` | (i) distinguished site of a support, 4:435, 506, 573; 6:90, 190 ff.; (ii) site `a_i` attached to a coordinate, 5:1204; (iii) real base point of a holomorphic weight, 5:902 | R | *base point*; *site of the coordinate*; *real part `x`* |
| `eligible` | (i) pair `(z,o)` satisfying the axial bound, 4:68–75; (ii) an extra gauge-invariant event, 4:442 | D / I | *admissible pair*; *additional event* |
| `centered` | (i) zero-mean, 3:580–584; (ii) about the point `x₀`, 3:699; (iii) normalised, 4:132, 628; 5:1338 | D / I | *zero-mean*; *about `x₀`*; *normalised* |
| `separation` | (i) displacement `x − y`, 3:61, 322; (ii) nondegeneracy property, 3:973, 981; (iii) of singularities, 3:854 | I | *displacement*; *nondegeneracy* |
| `cutoff` | (i) threshold (`ε_pred`, `t_m`), 4:203, 211, 406; (ii) cutoff function `χ`, 3:758; (iii) ultraviolet cutoff `N`, 5:705 | R | *threshold*; *cutoff function*; *ultraviolet cutoff* |
| `physical` | (i) position-space, 5:520, 1085; (ii) unscaled, 5:97; (iii) before the change of variables, 6:691 ff. | I | *position-space*; *unscaled*; *original* |
| `mismatch` | (i) `n_e = χ(V_e Q_e(U)⁻¹)`, 6:47†; (ii) the error terms `E_L`, `E_D`, 6:1410 | D / R | *deviation from the block average*; *error terms* |
| `word` | (i) finite sequence of insertions, 3:234; (ii) product of links along a path, 6:630; (iii) term of a Neumann series, 6:1199 ff. | D / R | keep (i) only if defined once; *holonomy*; *term of the series* |
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
| nonwrapping / wrapping support | 4:627, 642 | Support that does not wind around the torus. | I | *of diameter less than the period* |
| fine residue | 5:654, 660, 713 | Position `r` of a fine site in its block, `x = Ly + r`. | R | *position within the block* |
| incoming; inherited | 5:306, 690, 1058 ff.; 6:379, 671 and 17 more | Belonging to the input of the renormalisation step. | I | *from the previous step*; *input* |
| exact (blocking, block map) | 4:2, 5, 169, 232, 289†, 569 | The block kernel is a probability kernel, so the partition function is preserved. | D (4:289) | *normalised block-spin kernel* |
| smoothing order `j` | 4:16, 186; 5:196–202 | Number of box convolutions in the averaging weight. | D | *order of the averaging kernel* |
| block penalty `b` | 4:226; 5:88; 6:21, 125 | Constant in the Gaussian block weight `exp(−(b/2)‖Qa − v‖²)`. | D | *constant of the block-spin kernel* |
| noise; accumulated / suffix noise | 5:126–130 and 13 lines; 6:908, 1014 | The independent Gaussian `b^{-1/2}ξ` in `v = Qa + b^{-1/2}ξ`, and its propagated contribution. | R | acceptable; or *the `b⁻¹` term* |
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
| uniform mass; branch masses; likelihood (tests, factors) | 4:77, 209, 315; 5:970; 6:63, 671, 920, 1016, 1107, 1345 | The weights `λ(U,α)` of the random index. That "mass" and "likelihood" name the same weights is inferred. | I | *probability weights `λ(U,α)`* |
| connector | 4:175–184; 5:986 | `Y_{e,z}`: frame-conjugated product of `L` fine links along a straight path. | D | *gauge-transformed parallel transporter* |
| `Q^pred`, `ε_pred`, predictor | 4:202–210, 239, 287, 386–391; 6:460, 501 | The source's name for the block average and its threshold. | I | *block average*; rename the superscript |
| route; route matrices; walk | 4:107, 109; 5:995, 1003; 6:180 ff. | Lattice path; its holonomy. In 6:1025 "route" also means "method". | I | *path*; *holonomy* |
| feedback matrices | 4:124–133 | `F_x(h) = av h_y W_{xy;o}⁻¹`. | D | *local mean* |
| straight (average, transport) | 5:535, 859, 993, 1084 | The linear average `M` without the gradient correction. | D (5:993) | *linear block average* |
| first-power (bound, estimate) | 4:293, 308–312; 5:976 | A bound linear in `χ`. | D | *linear bound* |
| forest; forest coordinates / chart / slice | 5:916–935; 6:516, 629, 966 ff. | A rooted spanning tree in each block; coordinates `(v, ψ)` with `ψ` on non-tree links. | D | *maximal-tree gauge in each block* |
| tree slice; tree coordinates; tree-straightened | 5:916 ff.; 6:466–490, 972, 1492 | Gauge slice where tree links equal the identity. | I | *tree gauge* |
| tree comparison | 4:296; 5:1000†, 1289 | The inequality `‖a‖² ≤ B‖d₁a‖² + C‖𝒬a‖²` for `a` vanishing on tree links. | D (ch. 5) | *coercivity inequality in tree gauge* |
| replica `rep V`; replicated field; parent | 5:920–929; 6:180, 341 ff. | Fine field equal to `1` inside blocks and to `V` on links between blocks; "parent" of `x` is the block containing it. | D | *block-constant lift of `V`* |
| vertical (coordinates, Hessian, gap) | 5:944, 1078, 1334, 1339 | The fluctuation variables `ψ` at fixed `v`. | I | *in the fluctuation variables* |
| stationary graph / tangent / background | 5:1145–1180 and 25 lines | `ψ = ρ(v)` solving `D_ψ f = 0`, and its derivative at zero. | D | *critical-point map*; *background field* |
| frozen (links, logarithms) | 6:442 and 26 more | Non-tree links near the large-field set, held fixed in the Gaussian integral and integrated afterwards. | I | *conditioning variables* |
| active / inactive coordinates | 6:443 | Logarithms of non-tree links outside the `10B`-neighbourhood. | D | *integration variables* |
| signal `ũ` | 6:1373–1383 | The active increment, extended by the clipped frozen logarithm and zero on the tree. | D | *displacement field* |

### 2.3 Effective action and its pieces

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| density coordinates; coordinate tuple | 4:8, 403, 469, 530, 550†, 656–676 | The data `(β, v_sc, regular activities, large-field activities)` parametrising a density. Not coordinates: the map to densities is not claimed injective or onto. | D | *parametrisation*; *representation data* |
| regular activity | 4:433–438, 452, 551 | `(X_i, o_i, E_i^reg)`: a local term entering the exponent additively. Not a polymer activity. | D | *local term of the small-field action* |
| scalar; `v_sc` | 4:9, 550, 658 | Constant per-site term of the exponent. | D | *vacuum energy density* |
| direct (row, term, coefficient `c_dir`) | 4:474; 5:749; 6:101, 137, 143 ff. | The single-plaquette term and its coefficient, as in `H = c_dir I + ρ*ρ` (ch. 7:974†). | I | *plaquette term*; *its coefficient* |
| path action; path rows; path budget (label) | 4:496–521; 5:1241–1252; 6 passim | Action written as `Σ_γ c_γ ×` (local analytic term in holonomies along paths), with `sup_z Σ |c_γ| e^{σℓ(γ)} ≤ P`. | D | *non-local terms of the effective action*; *weighted norm of the path coefficients* |
| atoms; quadratic path square | 5:1054–1056; ch. 9:573, 837† | Elementary terms of the path action, graded by degree in the curvature. | I | *elementary terms of degree `q`* |
| inherited loop (action) | 5:1045; ch. 7:819, 1077† | A specific order-four term treated in ch. 7. Not determined within ch. 3–6. | ? | cross-reference ch. 7 |
| (curvature, two-form) metric; metric modification; positive completion | 5:43–46, 227–235, 286–291, 456; 6:139, 163 | Positive operator `H` on two-forms with `K = d₁*Hd₁`; the modification `H⁻¹ = H₀⁻¹ + ζ(d₂H₀⁻¹)*(d₂H₀⁻¹)`. | D | *quadratic form on two-forms*; *coefficient operator* |
| (curvature) defect; amended defect; positive-defect identity | 5:638–641, 603; 6:135, 145, 176 | `Z₀ = B_c − T*B_fT − b⁻¹d₁d₁*` and its version with modified metrics, with `K*K = Z ≥ 0`. | R | *positive remainder in the covariance recursion* |
| aligned; alignment premise | 6:136–141, 164 ff. | `C_ν*C_ν = H_ν`: the action's terms factorise the chosen quadratic form. | R | *factorisation of the Hessian* |
| quadratic coefficient condition | 5:1052–1058 | The quadratic Taylor coefficient of the input action is `d₁*H_f d₁` with `H_f ≥ εI`. | D | *hypothesis on the quadratic part* |
| uncut (action); plateau | 5:973, 1044, 1241; 6:243, 917 ff. | Without the smooth small-field cutoffs; region where a cutoff equals one. | I | *without cutoff functions*; *where the cutoff equals one* |
| clip; clipped; capped | 4:477–528; 6:109–121 | `clip_t`: quadratic below `t`, linear above, with a jump at `t` (4:528). "Capped": multiplied by `min(1, t_c/r)`. | D | *truncated quadratic*; give it a symbol |
| relaxed (`χ^rel`, `R^rel`) | 4:474–493 | Small-field condition with threshold growing like `t_m e^{dist/R^rel}`. | I | *exponentially weighted small-field condition* |
| kinetic energies `K_f`, `K_c` | 6:110 | Clipped plaquette action plus cut-off path square. Nothing kinetic. | R | *local action density* |
| comparison term | 6:186–188 | `Φ v_c`: fine curvature predicted linearly from the truncated coarse curvature. | D | *linear prediction from the coarse field* |
| coarse counterterm | 6:1407 | The term `E_c`. Not a renormalisation counterterm. | I | *subtracted coarse energy* |
| affine stack | 6:446–452 | The vector `Du + b_Y`. | R | *vector of residuals* |
| source (`b_Y`, `f_Y`) | 6:581–612 | Constant and linear terms of the quadratic form. | R | *linear term* |
| extracted; Gaussian extraction | 6:1251, 1280, 1326 ff. | After the affine squares are moved into the Gaussian measure. | I | *after completing the square* |
| local transfer identity | 6:466, 924, 942 | `m_Y − v = E*v − P*(Av + f_Y)`. | R | *comparison identity for the mean* |

### 2.4 Large-field regions, supports and localisation

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| `Bad_m(U)` | 4:425 | Sites incident to a plaquette with `χ > t_m`. | D | *large-field set* |
| consistent (selection, sector) | 6:54–63 | Threshold inequalities hold near `A` with overlapping margins. | D | *admissible large-field set* |
| sector; allocation sector | 6:85–87† | One term of the decomposition, with the large-field set, component assignment, block trees and index `α` fixed. | D | *term with fixed discrete data* |
| exclusion support `Y_i`; coverage | 4:440, 455–463 | The set entering the disjointness constraint. | D | *polymer (hard-core) support* |
| (full) dependence region | 4:459 | All links the function and its conditions depend on. | D | *dependence set* |
| exact cover | 4:543–547 | Family with pairwise disjoint `Y_i` whose large-field parts have union `Bad_m(U)`. | D | *compatible family covering the large-field set* |
| footprint; stencil | 4:505–506; 6:453, 459 ff. | Set of links a term depends on. | R | *support* |
| reads; read by | 4:450–507; 5:961, 1054; 6:382, 742, 1349 | "depends on"; "is computed from". | I | *depends on* |
| window `Ω_i`; local inverse columns; principal compression | 6:520–574 | Index neighbourhood on which `A` is inverted to build `P`; `A[Ω,Ω]`. | D | *localisation neighbourhood*; *localised approximate inverse*; *principal submatrix* |
| core; annulus; ownership components | 6:1330–1333 | Terms within `2B` of a component and the rest out to `200B`; components of large-field sets whose `500B`-neighbourhoods meet. | D | *inner part*, *collar*; *components for the `1000B`-adjacency* |
| clean; remote; clearance | 6:925–997, 1008, 1249; 496, 603 | Containing no large-field element; farther than `30B` from the large-field set; distance margin. | I | *small-field region*; *far from the large-field set*; *distance* |
| protected | 6:694–737, 806 | Carrying a smooth cutoff so that the change of variables is the exact logarithm. | I | *cut off inside the chart* |
| containing-site bound; halo; support exponent | 4:603–606; 6:1170–1178 | `sup_x Σ_{λ: x ∈ S_λ} e^{α c_B(S_λ)} a_λ ≤ ε`; `hB`-neighbourhood; the rate `α`. | D | *weighted polymer-activity norm*; *neighbourhood*; *decay rate* |
| cluster (symbols, matrices, limit) | 5:718–734, 805–848 | Subsequential limits. Unfortunate where "cluster" normally means cluster expansion. | R | *subsequential limit* |

### 2.5 Local fields and Ward identities (chapter 3)

| House term (variants) | Where | Meaning | Basis | Standard equivalent |
|---|---|---|---|---|
| spectator (fields, list, legs) | 3:705, 782, 824–873 | The insertions other than the distinguished one. From 3:837 the "quadratic spectator" is brought close to `P`, so it acts as a test field. | I | *the remaining insertions*; *test field* |
| leg | 3:826, 827, 839 | A linear curvature-jet factor of a Wick monomial. | I | *linear factor* |
| probe; jet probe | 3:751, 883, 939–985 | A linear functional on order-`j` solution jets. | R | *linear functional on jets* |
| wave; Maxwell wave | 3:731, 758, 899, 975 | Smooth closed and coclosed two-form on a region. | I | *smooth solution of the Euclidean Maxwell equations* |
| pulse; covariance pulse | 3:732–770 | `y ↦ S₂(F(y), F_ij(x₀))`. | I | *two-point kernel with source at `x₀`* |
| tower | 3:431–470 | Element of the direct sum of the `S_k`, `0 ≤ k ≤ j`. | D | *element of the direct sum* |
| detection; detector (labels) | 3:830 | `P ∉ N_D`: some correlation is nonzero. | I | *separation*; *nondegeneracy* |
| Ward sum | 3:915 | `W_A = Σ_i S_n(P₁,…,AP_i,…,P_n)`. | D | *action of `A` as a derivation on the correlation* |
| charge | 3:780 | A symmetry generator acting on fields. | I | *infinitesimal generator* |
| flux; local Ward / stress flux; shell flux | 3:546, 656–671 | `F_{χ,v} = −∫ ∂_aχ v_b S(T_ab, …)`. | D | *smeared charge of the current `T_ab v_b`* |
| pole; harmonic pole; "cleared by" | 3:865–876, 964 | Homogeneous singularity `|z|^{-r}` at the origin of `ℝ⁴`. | I | *homogeneous singularity of degree `−r`*; *becomes smooth after multiplication by* |
| collision | 3:146, 832, 879, 914, 1016 | Coincidence of insertion points. | I | *coincident points*; *short-distance limit* |
| free image; polynomial image; free polynomial space | 3:194–224, 784 | `M_d^Max = im ω_d`. Five names for one space. | D | *space of on-shell polynomials* (one name) |
| correlation-null | 3:216, 348, 523 | Vanishing in every separated correlation. | R | *in the kernel of the correlation functionals* |
| weight; weight operator | 3:168–170, 689 | Scaling dimension; `Σ (j+2) X ∂/∂X`. | D | *scaling dimension*; *Euler operator* |
| reciprocity | 3:992 | The symmetry `C(f_b(p),q;u) = C(f_b(q),p;u)` of 3:979. | I | *by the symmetry (…)* |
| contraction derivative | 3:895 | The polynomials `Σ_λ C_{k,j}(p,e_λ;z) ∂P/∂X_{j,α}(e_λ)`. | I | *directional derivatives in the top-order variables* |

### 2.6 Estimates: accounting and bookkeeping vocabulary

Chapters 3–5 are nearly free of the accounting vocabulary found later in the book; chapter 6 has some. `blueprint/notation.md` already prescribes: *print the inequality*.

| House term | Where | Meaning | Standard equivalent |
|---|---|---|---|
| cost; costs | 4:378, 391; 5:611, 620, 1354; 6: 18 occurrences | A multiplicative loss or an error of that size; in 4:391 the value of the objective `P_e(u)`. | *loses a factor*; *is bounded by*; *objective* |
| loss; "leave … per test"; retained energy; margin | 5:1362; 6:231–435, 1096 ff. | Negative error terms and what remains of a lower bound. | *error terms*; *remaining lower bound* |
| excess | 6:326–419 | `Δ_p` in `r_p^c ≤ C t_f + Δ_p`. | *remainder* |
| supplies; the supplied construction | 3:546; 5:195, 1217 ff. | "Gives"; the construction of the formal source. | *gives*; *the present construction* |
| assigned; ownership | 6:85, 421, 1162, 1329–1335 | Which component a term is attributed to. | *attributed to* |
| subpower | 6:822 | `A(x) ≤ C_ε x^ε` for all `ε`. | `x^{o(1)}` |
| zero-germ | 6:922, 1021, 1215 | Vanishes identically near the base point. | *vanishes in a neighbourhood of* |
| score | 6:820, 1530 | Logarithmic derivative of a density. | *logarithmic derivative* |
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
| support of a local term | footprint, stencil, dependence region | *support* (keep *dependence set* where it differs from the hard-core support) |
| the random index | label, tag | *index `α`* |
| its weights | mass, likelihood | *weight `λ(U,α)`* |
| base point of a support | anchor, root | *base point* |
| subsequential limit | cluster limit, cluster symbol | *subsequential limit* |
| on-shell polynomial space | free image, polynomial image, free polynomial space, free spaces | one name |

---

## 4. Terms whose meaning chapters 3–6 do not determine

These need the author, the formal source, or a cross-reference before any replacement is made.

| Term | Where | What can be said |
|---|---|---|
| moving comparison fields | 3:576 | Possibly the cutoff-dependent fields of ch. 11 ("moving equation space", 11:1083). |
| internal rotation defect | 3:910, 1027 | An alternating map `Δ(K,L)` on fields; the theorem gives only hypotheses on it. |
| stationary-field estimates | 4:166 | Forward reference without a label. |
| regularity-stage index `J_m` | 4:651 | An index distinct from `m` on which `q, ϖ, σ` may depend. |
| inherited loop action | 5:1045 | An order-four term treated in ch. 7. |
| centered log determinant | 5:1338 | Presumably `log det H(v) − log det H(0)`. |
| pre-`L` factor / pre-`L` excess estimate | 5:1021; 6:356 | Presumably a constant fixed before `L` is chosen. |
| output anchors | 6:90 | "Anchors" are base points; "output" is unexplained. |
| compulsory (component region, cutoff factor) | 6:1018, 1461 | Cf. ch. 10:654, "one compulsory large-field factor" for arrays constrained to cover prescribed sites. |
| Warnings | 6:1476 | Capitalised, undefined; ch. 11:319 has an "actual warning estimate". |
| seeded sector / unseeded law | 6:1544 | Also ch. 9:283. Possibly with and without prescribed large-field elements. |
| terminal fine metric | 6:170–175 | "Terminal" unexplained in this use. |
| connected covering number `c_B(S)` | 6:1172 | Named but not defined precisely here. |

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
- **Audit and harmonisation.** The entries were merged by concept, the proposed equivalents made uniform across chapters and aligned with `blueprint/notation.md`. Entries marked † were rechecked against the chapter text or resolved by a cross-chapter search (for example `direct coefficient` = `c_dir` from ch. 7:974; `tree comparison` = the inequality of ch. 5; `minimum-cost test` from ch. 4:391; `atoms` from ch. 9).
- **Not done.** Most unmarked entries rest on a single survey and were not independently reread. Occurrence counts for frequent terms are approximate. Chapters outside 3–6 were searched only to locate first uses. No formal-source declaration was consulted, so no claim is made about which Lean names the terms come from. The proposed equivalents are editorial suggestions by an agent and need a mathematician's review; entries with basis **I** in particular may misread the text.
- **Agent assistance.** Claude Code (Claude Fable 5.2), with three subagents for the surveys.
