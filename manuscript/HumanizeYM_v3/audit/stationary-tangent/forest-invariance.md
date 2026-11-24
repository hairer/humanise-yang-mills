# Is a translation-invariant forest a missing hypothesis in v3?

Read-only check. Paths: v3 = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/ (cited as NN:line),
Scott = .../HumanizeYM_v2/part2, Martin = .../manuscript/existence, Lean = /Users/mgubi/OpenAI-YM/YM.
Labels: [v3 states], [v3 proves], [mine] = my inference, [unsettled].

## 0. Short answer

- Yes, there is a gap of formulation, at ONE place for certain: 17-current-contraction.tex:163-183. There a
  forest-dependent operator (`Pi_F C^{-1} Pi_F^*`, and the jets `z_2,z_3` "on the forest slice") is given a bound "on one
  fixed smaller coarse Fourier strip" with "intermediate momentum sums". v3's strip norm is defined only for
  translation-invariant coefficients (07:30-33, 41-43). For a forest that is not invariant under coarse translations these
  operators have no Fourier symbol, so the sentence has no meaning as written.
- A second place is probable and more serious, and is NOT cured by Fourier-free norms: 09-renormalization.tex:362
  ("Translation covariance makes F_x(1)=F_0(1)") and 09:521 ("By translation and hypercubic covariance"). These use
  covariance of local terms built in a sector with a fixed forest. Martin obtains exactly this covariance by an explicit
  average over forests (existence/forest-average-log.tex:9-11, 81-121); v3 contains no forest average and no covariance
  statement for its activities. [unsettled whether the v3 terms at 09:362/521 really depend on the forest; see 1.6]
- Everywhere else the forest enters only through matrix identities, counting/row-sum norms, or the weighted kernel norm
  `||T||_eta` of 05:873-877, all valid for an arbitrary forest. The Fourier/alias computations of chapters 7 and 17 are
  explicitly done with the forest-free representatives `W_a`/`W_s` and the forest-free completed inverse `C^{-1}`.
- The forest is a free choice (a gauge choice for the fine gauge transformations that are trivial at block roots);
  nothing in chapter 6 forces it to vary in space. A translated reference tree can be assumed without loss in chapters
  7 and 17 and does not conflict with chapter 6. It gives translation covariance but not hypercubic covariance.

## 1. Inventory of forest-dependent objects and whether covariance is used

### 1.1 Definitions (chapter 5) - no covariance used, arbitrary forest intended
- 05:916-918 [v3 states] "Fix j,L, a coarse period s>=100(j+8), and in each centered block Ly+B_{(L-1)/2} a spanning tree
  rooted at Ly. Trees contain only internal block edges." No relation between blocks is imposed.
- 05:961-966 "At fixed j,L every such equation reads a translate of one fixed finite patch ... There are finitely many
  directions and local tree shapes at fixed L; take their common radius and bounds." Uniformity over trees by finiteness;
  this presupposes that trees may differ from block to block.
- 05:1041 "Both constants are uniform in the period and in the allowed trees."; 05:1327 "independent of the allowed
  period and block trees".
- Norms used for the forest chart in chapter 5: counting l2 norm (05:1036-1040, tree comparison), sup-norm operator norms
  (05:1164, 1173-1186), and the weighted kernel norm 05:873-877
  `||T||_eta = max{ sup_i sum_j e^{eta d(a_i,a_j)}|T_ij| , sup_j sum_i ... }`, with the inverse bound "It follows by
  conjugating with e^{eta d(a_i,a_{i_0})} and applying the resolvent identity" (05:886-889). None needs translation
  invariance. [v3 proves, for any forest]
- 05:1139-1154 `W_F` = `W_a` minus the root-zero gradient killing tree edges; "Estimate (ch05:actual-bridge) is asserted
  for W_a, not for tree coordinates." No Fourier statement about `W_F` is made in chapter 5.
- The translation-covariant objects of chapter 5 (`W_s`, `R`, `E`, `W_a`, `Q=M+d_{0,c}R`, 05:975-998, 1094-1117) do not
  involve the trees (also verify-ch5.md, part D).

### 1.2 Chapter 7
- 07:30-48 [v3 states] the only definition of the strip norm: "A translation-invariant coefficient is specified by its
  values on plane waves ... For sigma>0, write |f|_sigma<=A when every component is holomorphic and bounded by A on the
  strip |Im p_i^a|<sigma." So `|.|_sigma` exists only for translation-invariant coefficients. The other norm of chapter 7
  is the path norm 07:164-167 `sum_a |a| e^{w length(a)}`, again for a translation-invariant family.
- 07:241-259 gauge completion: `det C=(det G)^2 det(I^* J I)`, with "I a slice embedding" and `C=J+F^*F`. [mine] This
  identity removes the slice: the right side `(1/2)log det C - log|det G|` does not contain the forest. All subsequent
  Fourier work (07:466-823) is on `C_0`, `A_mu`, `Theta`, i.e. forest-free completed matrices.
- 07:521-565 contact term: "Use rooted coordinates ...", "restore the chosen tree gauge" (07:550-551), "At fixed L, the
  finite-stencil block average and the analytic inverse of A(0) give common holomorphic kernels ... Write M(p) for the
  mixed kernel of DY" (07:557-562). `M_core`, `M_act` (07:527-529) are not defined in the v3 chapter. [unsettled] If
  "rooted coordinates" are tree-slice coordinates, then "common holomorphic kernels" of `A(0)^{-1}` and the "momentum
  mesh averages" (07:559-560) need a translation-invariant forest. The use of the tree gauge at 07:549-554 itself is
  pointwise (uniqueness of the stationary branch) and needs no covariance.
- 07:574-582, 598 the weighted estimates use `W_a` ("External smooth bridge legs ... by (ch05:actual-bridge)").
- 07:866-870 [v3 states] "The fixed-L stationary chart of Chapter 5 provides existence and differentiation, but its
  tree-coordinate inverse alone does not provide these stronger bounds. We obtain them from the weighted quotient just
  constructed." 07:877-883: `C^{-1}=(H+F^*F)^{-1}`, `Tu=(u,W_a u,r_u)` "in the smooth centered representative".
- 07:888-893 the only use of the forest slice in the classical matching: "Stationarity in all joint internal directions
  follows from stationarity on the forest slice and gauge invariance: the forest slice together with the joint gauge
  directions spans the internal tangent space." Pure linear algebra, any forest. [v3 proves]
- 07:938-967 the jets `D^3E(0), D^4E(0)` are written with `T` (smooth) and `C^{-1}` only; "The gauge-annihilation
  argument makes the formulas independent of the representative chosen to differentiate the stationary branch"
  (07:952-953). The momentum argument 07:955-960 is therefore about forest-free objects. No gap.
- 07:812-814 and 07:1112-1118, 1135-1148 alias amplitudes `N_l`: 07:1112-1118 says explicitly "it is legitimate to use
  W_s in this calculation, even if the tree-gauge representative itself has poor difference bounds". No gap.
- 07:1150-1155 nonlinear pullback has the same Hessian; uses "identified up to gauge". No covariance of `W_F` needed.
Conclusion for chapter 7: apart from the unclear contact paragraph 07:521-565, chapter 7 never Fourier-transforms a
forest-dependent object. Its outputs (stationary value `E(v)`, thermal term `T(v)` of 07:231-234) are gauge invariant
and hence forest independent [mine; v3 does not state forest independence; Lean states it as `YM.Bid.F05`, see 4].

### 1.3 Chapter 17 (17-current-contraction.tex)
- 17:48-53 "is the forest representative W_F ... Since W_F-W_a is a fine gradient, the Ward identities of E_b allow us to
  compute with the smooth representative W=W_a." 17:61 "N_l is the alias amplitude of W" - with W=W_a this is defined.
  17:112-117 again `W=W_a`. No gap in 17:46-136 as now written.
- 17:140-183 THE GAP. Quotes: "What must remain uniform before L is the coarse coefficient width on which these constants
  are measured" (142-143); "On the forest slice implicit differentiation gives H z_2[u,v]=-D^3 S[Tu,Tv,.] ..." (150-158)
  with `Tu=(u,Dz(0)u)` (149), i.e. the forest tangent; "These formulas have period-independent bounds C_{j,L} on one fixed
  smaller coarse Fourier strip. To check the width statement, let Pi_F be projection onto the forest slice along the
  joint gauge directions. At zero it is computed by finite sums along the block tree and the root frame; its
  coefficients and those of Pi_F^* have norm bounded by a finite C_{j,L}, but bounded range in coarse blocks."
  (163-168); "Thus the slice inverse is Pi_F C^{-1} Pi_F^*. The completed inverse has a common positive coarse width
  chosen before L; multiplication by the finite-range projections does not destroy it." (172-177); "Restrict the
  external strips by a fixed factor so all intermediate momentum sums lie in this inverse strip." (179-181).
  Here `Pi_F`, `Dz(0)`, `z_2`, `z_3` depend on the forest; "Fourier strip", "strips", "momentum sums" presuppose that
  they commute with coarse translations. That holds iff the forest is invariant under coarse translations. v3 does not
  say so. No norm other than the strip norm is defined in chapter 17 for these operators ("weighted norm" at 17:110, 222
  is not defined there).
  [mine] The mathematics survives for any forest in the norm `||.||_eta` of 05:873-877 (coarse distance): `Pi_F` and
  `Pi_F^*` have range O_j(1) coarse blocks and entries bounded by C_{j,L} uniformly in the trees (path length <= L^4,
  finitely many tree shapes, 05:964); `C^{-1}` is forest free and translation covariant, so its strip bound gives
  `||C^{-1}||_eta<infinity` for eta below the strip width; hence
  `||Pi_F C^{-1} Pi_F^*||_eta <= e^{2 eta r} ||Pi_F|| ||C^{-1}||_eta ||Pi_F^*||` at the same eta, and the multilinear
  vertices compose in the usual way. "Width chosen before L, constants C_{j,L}" is preserved.
- 17:185-200 radial gauge: `|W^rad(x,y)| <= C_j L^{-2}(1+|x|)e^{C|x|/L}e^{-c_j d(0,y)}` is a kernel bound relative to an
  anchor; "A common strip reduction handles the coarse weight" is again strip language but about an anchored kernel,
  where strip = exponential weight around the anchor; no covariance needed. [mine]
- 17:265-271 "At coarse anchor zero the displaced coarse current is Y'_b=L^5 sum_x K_0(x)(R_f+d_V R_0)Y_b^x(U_stat(V)).
  Translations give the other anchors." `U_stat(V)` is the forest-chart stationary field. [mine] The sentence is correct
  for any forest only because `Y`, `R_f`, `R_0` (which carries `Ad(h(y)U(gamma_{y,f}))`, 17:261-262) are covariant and
  the stationary field is unique up to fine gauge transformations trivial at block roots; v3 does not say this. With a
  translated reference tree it is literally true.
- 17:282 "All derivatives of R_f+d_V R_0 have finite C_{j,L} bounds on the common coarse strip": `R_f,R_0` are built from
  the frame routes of 05:975-983, not from the trees; translation covariant. No gap.
- 17-marked-trace-rates.tex:263-270 uses `W_a` and gauge invariance. 17-trace-transfer.tex:417 "Translation covariance
  makes contraction by the inverse R commute with translating the anchor" concerns the fine translation structure of
  17-trace-transfer.tex:14-29, no forest object appears. [not read in full]

### 1.4 09-stationary-remainder.tex
- 09sr:33-45 `y` = "free fine coordinates after tree gauge fixing", `A(x)=D_y^2 phi`, `s=(1/2)log det A`; all estimates are
  sup-norm / operator-norm bounds "uniform in the auxiliary volume at the fixed block ratio" (42-43). No Fourier.
- 09sr:188-196 "Its tangent is the forest-coordinate lift W_F ... Its curl agrees with that of the smooth actual lift W_a
  ... ||H_f^{-1}TH_c||_{inf->inf} <= C_j L^{-2}. The operator norm here sums each fine-output row over coarse inputs".
  Row-sum norm of a forest-free operator. No covariance of `W_F` needed. [v3 states; correct for any forest]
- 09sr:258-277 `W=d_c-psi(.,rho)-(1/2)log det A`: "The quadratic quantum matching bounds D^2W(0) by an exponentially small
  finite-period error". [mine] this compares a tree-slice determinant with the chapter-7 symbol; it is legitimate
  through 07:241-259 (slice-free completion), not through any Fourier property of the slice.

### 1.5 09-renormalization.tex, 10, 11
- 09:74-76 "The flat reference determinant uses the same forest as the sector. It is extracted once"; 09:239-240 "use the
  same forest and physical local coordinates on both sides"; 09:924-926 "Use the same forest, path realization, clipped
  frozen source and cutoff choices throughout". Consistency statements; no covariance.
- 10:256-257 "Choose one such history for each N,p, retaining its path arrays, forests, local integral choices".
  11-restarted-history.tex:247 "forest charts keep their original adjacent values". The forest is part of the chosen
  history: a free choice made once.
- 11-marked-insertions.tex:617-666: CONFIRMED pure matrix identities, valid for every forest. Check: `A=K+bQ^*Q`,
  `A_F=I_F^*AI_F>0`, `X=I_FA_F^{-1}I_F^*`, `XA=P` (rooted gauge projection), `DP=D`; `AW=bQ^*` holds for `W_F` (and
  `W_a`) because `K d phi=0`, `Q d phi=0` for root-zero phi; `DXbQ^*=DXAW=DPW=DW`; result
  `(DI_F)A_F^{-1}(DI_F)^* = P_f - J P_c J^*` (11:656-659). [mine] The right side contains no forest, so the conditional
  curvature covariance is forest independent and translation invariant; the later Fourier analysis (11:1675-1698,
  `P(p)=X{X^*HX+UU^*}^{-1}X^*`) is on that forest-free object.
- 11:679-690 "Fix a clean neighborhood and one forest, tag, coarse gauge and Gaussian sample ... the gauge-invariance of
  each polynomial then permits its physical evaluation in a different local frame". No covariance.

### 1.6 Sums over sites done by translation (chapter 9) - probable second gap
- 09:360-365 "Sum (ch09:localization) over x ... Translation covariance makes F_x(1)=F_0(1), giving exactly
  sum_x M_x=|Lambda|F_0(1)+...". `F_x=sum_a p_{xa} f_a^0` (09:319), the `f_a^0` being "selected low-order" terms of the
  sector expansion, whose law is "the one sector Gaussian/Haar law" (09:105) on forest coordinates (09:57-76).
- 09:521-523 "By translation and hypercubic covariance, sum_{o_i=o} q_{f_i}(q,r)=Delta delta_{qr}."
- v3 nowhere states that the regular activities are translation or hypercubic covariant, and it has no forest average
  (grep "forest" over all chapters: no averaging; the only symmetry sentences are 06:966-967 "each signed orientation
  with its transported forest; it never assumes that a rooted response commutes with the symmetry", 06:1420-1424, and
  09:574 "After the common signed-symmetry average").
- [unsettled] I could not determine from v3 whether `f_a^0` depend on the forest. If they do, then with an arbitrary
  forest 09:362 and 09:521 fail; with a translated reference tree translation covariance holds but hypercubic covariance
  still needs an average (no spanning tree is invariant under the signed permutations).
- Martin: "The exact block gas ... was constructed with a fixed forest. To restore the lattice symmetries we average
  over forests before taking the logarithm of the flag-free gas." (forest-average-log.tex:9-11); "At each coarse site x,
  choose independently a uniform forest F_x from this finite set" (85-86); "A signed lattice transformation permutes the
  site choices and transforms every chosen forest by a bijection. Its product uniform measure is unchanged. The
  covariance of the individual sector formulas consequently gives the same covariance for bar a_M" (117-121).
  five-period-localization.tex:79-81 lists as a hypothesis "the auxiliary densities transform covariantly under signed
  lattice symmetries", then 176-177 "Translation covariance makes f_Lambda(o,1) independent of o".
- Scott D-section:528 "Translation covariance makes the result independent of the anchor"; D:314 "The frame average
  transports the support and anchor under lattice symmetries" (I did not locate the definition of this average);
  D:840 "We therefore fix, once for each continuous input curve, all choices ...: the tree gauge, ...".

### 1.7 Chapter 6
- 06:85-88 "An allocation sector fixes the selection, its assignment to connected components of its neighborhoods, a
  rooted spanning tree in every block, and all frame and block average tags. Tree links are set to the identity. These
  choices fix the coordinates and supports before differentiation."
- All estimates are counting norms (06:504), exponentially weighted row/column norms (06:635-636), row norms
  (06:972-975: "The tree-straightened response has a bounded row norm at fixed L: the exponentially decaying stationary
  kernel is summed absolutely, and its straightening correction is a sum along finitely many tree edges per block").
  06:399-400 "not merely a decay estimate for a flat Fourier kernel". No Fourier symbol of a forest object. No gap.

## 2. Which forest is in force

- [v3 states] The forest is fixed with the sector (06:85-88) and with the history (10:256-257). Nothing in chapter 6
  makes the tree depend on the large-field selection, a tag or a patch: selection and tags are summed with weights
  (06:67-79), the tree is merely "fixed". 06:486 "No coordinate change to an unrelated tree is made", 06:516 "preserves
  the original forest".
- [mine] So the forest is a free choice made once; one may take the translates of one reference tree. This is the
  period-independent choice that the "common symbol" requirement of 07:36-39 wants anyway.
- In the zero-background computations of chapters 7 and 17 there is no selection at all, and the computed quantities are
  invariant under fine gauge transformations trivial at block roots (the forest is a gauge fixing for exactly that
  group: 05:1139-1144; Scott B:583 "gauge transformations fixing every block root leave the kernel ... invariant").
  Hence the forest can be taken translation invariant there without loss. v3's own tools for this: 07:241-259 and
  07:889-893.
- 06:966 / 06:1420-1422 transform the forest by signed lattice orientations. A translated-reference forest is mapped by a
  signed coordinate permutation to the translated forest of the image tree (odd L, centered blocks, roots Ly are
  preserved), so the class "translates of one reference tree" is stable; the constants must be uniform over the finitely
  many reference trees, which 05:964, 1041 already give.

## 3. Scott, Martin, Lean

- Scott D-section:1197 "For the actual axial curve, Lemma B3(ii) identifies its fine tangent as the tree representative
  of W_0 v. Choose one reference tree and translate it over the cells. The map P_tree taking a fine field to that
  representative adds the gradient of its signed tree-path sums; at fixed ratio it is a finite-range map."
  C-section:391 "For each fixed history the flat axial Hessian is the periodization of a single translated-tree, path
  and patch kernel ... a small complex displacement and a Neumann expansion give a uniformly summable inverse row".
  B-section:437 "In each block ... fix an axial spanning tree rooted at l y ... (Section B-energy allows every rooted
  block-tree gauge.)". C:412 "After a signed motion, regauge to the fixed tree with root gauge one; uniqueness of the
  stationary branch ... identifies the resulting branch." So Scott assumes a translated tree exactly where the tree
  Hessian or tree tangent is treated as a common kernel, and gets signed symmetry by regauging.
- Martin: forests arbitrary ("uniform in every forest", primary-calibration-producer.tex:118;
  "forest-independence of the stationary data", path-attachment-producer.tex:1283), symmetry restored by the
  independent per-site forest average quoted in 1.6.
- Lean. `YM.Tree.Forest` (YM/Tree/Pines.lean:24-29): fields `up, height, bound, rise, stays`; no periodicity. Header:
  "Chosen independently per physical coarse site in applications. Branches can prove for arbitrary Forest".
  `YM.Bid.F05` (YM/Bid/Station.lean:94-99, a `def ... : Prop`): for any two forests `H T`, the stationary value agrees
  near 0 and `thermal H ... = thermal T ... + cd` - i.e. forest independence of exactly the chapter-7 quantities.
  Translation-invariant forests are used where a forest-dependent matrix is asserted to be a translation-invariant
  stencil with an exponential width (`Tagged sigma p K A`, YM/RG08/Rows/Algebra.lean:59, which extends `Priced` with
  `city : Packets.city 1 K`, :20-24):
  * `YM.RG08.Line.NativeLine S G b := let Q:=project G S (green S); Q*meal G S b*Q.transpose`
    (YM/RG08/Line/Recipe.lean:20), `project` = "Full potential response to gauge projection" (Line/Project.lean:46),
    `meal` = the completed cell inverse (Line/Golden.lean:16). This is v3's `Pi_F C^{-1} Pi_F^*` with `F=green S`,
    the translation-invariant forest of YM/RG08/Line/Pine.lean:53 (`up x := parentDir (lift (residue x))`).
  * `YM.RG08.Line.preheat` (Recipe.lean:61-65): "Pre-block strip, post-block cost ... Integral Wick contractions read the
    whole inverse from the tree slice (zero-padded on trunks); no averaging of trees or signed choices in this formal
    rule." Conclusion `Tagged eta (post P.L) (warm P K G b) (cellLine P K G b)` with `eta` chosen before the patch and
    `post P.L` after: the Lean counterpart of 17:163-177, stated for `green`.
  * `stencil_projection` (Line/Financing.lean:59): `project G S (green S)` is a `Fund` (common priced stencil).
  * `YM.RG08.Repeated` (RG08/Gaussian/Repeated.lean:16, "The fixed, repeated tree used for the formal conditional
    expansion"), `Frosty`/`enquire`/`turn_fee` (RG08/Invert/Limb.lean:21-26, Gaussian/Turning.lean:47-52): the
    tree-straightened transport `straighten S (X.forest S.ratio) (installed S.ratio U)` is a `Cross` stencil for a
    `Repeated` tree; i.e. "alias amplitudes of W_F" exist in Lean only for a repeated tree.
  * `spreadForest` (WilsonBulk/Trees/Repeat.lean:24) for the Wilson bulk rows/covariance.
  Forest averages exist in Lean (e.g. PhysicalNext/RG_NEXT_COMPLETE_REPEATABLE_NONLINEAR_STEP/Islet.lean:40 "Weighted
  theta and forest average"; PhysicalNext/INTERPOLATED_SECANTS_FC/Blueprint.lean:55 `average`).
  [unsettled] I did not identify the Lean theorems for 17:150-158 (`z_2,z_3`) or 07:938-946, nor trace which final
  theorems consume `preheat`; users of `NativeLine` are all inside YM/RG08 (Cell, Prism, Weald, Supplies, Spar).

## 4. Conclusion and smallest repair

1. Gap as written: 17:163-183 (certain; a statement in a norm that is undefined for the object). Possibly 07:557-565
   (depends on what "rooted coordinates" means). Probably 09:362 and 09:521 (covariance of sector-built terms; different
   in nature, concerns the nonlinear step, and also involves hypercubic symmetry).
2. Not gaps: 05 (all), 06 (all), 07:866-967 and 07:1077-1155, 09-stationary-remainder:188-196, 09:74/239/924,
   11:617-690, 17:46-136, 17:282.
3. Smallest repair for chapters 7 and 17 - either of:
   (a) one sentence, e.g. after 05:918 or at the head of 07 and of 17:138: "Whenever a forest-dependent operator is
       expanded in coarse Fourier modes (Chapters 7 and 17) the forest consists of the coarse translates of one
       reference tree; this is no restriction, because the stationary value, the completed determinant and the pulled-
       back defect are invariant under fine gauge transformations trivial at block roots and so do not depend on the
       forest." This matches Scott D:1197 and Lean `green`/`Repeated`. It needs the (short, currently unstated)
       forest-independence remark; the ingredients are 07:241-259 and 07:889-893.
   (b) or reword 17:163-181 in the kernel norm of 05:873-877 (coarse distance): `Pi_F`, `Pi_F^*` finite coarse range and
       C_{j,L} entries uniformly in the trees; `C^{-1}` has `||.||_eta` bounded for eta below its strip width; products
       keep eta. Then no hypothesis on the forest is needed, in line with 05:1041, 1327 and 06:966-967.
   (b) is the more robust choice if v3 later adopts Martin's per-site forest average, since then sector forests are
   not periodic.
4. Conflicts: a translated reference tree does not conflict with chapter 6 (the sector merely "fixes" a tree, 06:85-88;
   signed orientations map translated forests to translated forests). It would conflict only with a per-site
   independent forest average as in Martin, which v3 does not contain. It does not by itself supply the hypercubic
   covariance used at 09:521.

## 5. Not read / not checked

- v3: chapters 01-03, most of 04, 05:1-860 (only grepped), 06 except the quoted passages, 08, 10 (grep only), 11 except
  610-700 and 1668-1700, 12-16, 17-trace-law, 17-trace-transfer (grep only), 17-variable-windows, 18, 19.
  The origin of the "selected low-order terms" `f_a^0` of 09:313-320 was not traced.
- Scott: only B:437, 583, C:391, 412, D:314, 528, 840, 1197 and greps; the "frame average" of D:314 not located.
- Martin: forest-average-log.tex:1-200 and five-period-localization.tex:74-84, 170-180; other files by grep only.
- Lean: only the files cited; no `lake env lean` was run; whether `YM.Bid.F05` is proved somewhere was not checked.
