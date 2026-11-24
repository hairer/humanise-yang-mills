# Chapter 9: the two covariance steps (09:362 and 09:521)

Read-only check. v3 = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters (cited NN:line; "09sr" =
09-stationary-remainder.tex). Scott = HumanizeYM_v2/part2 (D:line = D-section.tex, a "line" there is a whole paragraph).
Martin = manuscript/existence. Lean = /Users/mgubi/OpenAI-YM/YM.
Tags: [v3 states], [v3 proves], [mine] = my inference or computation, [unsettled].

## 0. Verdicts

- (A) 09:362 "Translation covariance makes F_x(1)=F_0(1)": TRUE under a translation-invariant forest and a
  translation-invariant selection, but NOT JUSTIFIED in v3 (no covariance statement for the low-order terms exists; the
  forest is not required to be translation invariant; Scott's sentence making the selected set invariant was dropped).
  The sentence itself is dispensable (replace |Lambda| F_0(1) by sum_x F_x(1)). The real dependence on symmetry is eight
  lines earlier, 09:348-357 (L_x = 0), which needs translation AND axis-reflection covariance of the local formula F,
  term by term. A translated reference tree (17:164-166) is enough for the sentence at 362 but not for 09:348-357,
  unless the reference tree is invariant under the axis reflections through its root (an axial tree is).
- (B) 09:521 "By translation and hypercubic covariance, sum_{o_i=o} q_{f_i}(q,r) = Delta delta_{qr}": GAP in v3 as
  written. The step needs equivariance of the whole preliminary regular family {f_i} under translations and the full
  hypercubic group. v3 neither assumes this for inputs nor proves it for outputs, and with one fixed forest it is false
  term by term in general (no rooted spanning tree of a block is invariant under coordinate permutations). Scott,
  Martin and Lean all carry family equivariance as part of the class; Martin and Lean obtain it by an independent
  per-coarse-site forest average taken before the logarithm.

## 1. The objects

### (A)
- `f_a^0`: 09:313-316 "Truncate the selected low-order formula, retaining a weighted tail eps_tr. Give an ordinary
  selected term f_a^0 the shares p_{xa}=1_{X_a}(x)/|X_a|, and a path term the share 1_{o_a}(x)." v3 does not define
  f_a^0 further; "low-order" refers to 09:290 "One- and two-factor terms". The source definition is Scott D:353:
  "Write f_a^0 for a regular summand of the negative logarithm in (D-cluster), including its coefficient ... low-order if
  it is a connected term with at most two polymers of at most two elementary factors each, every path atom having
  length at most B, with no incoming activity factor or large-field component, or a path term of length at most B."
- Where the terms come from [v3 states]: 09:81-89 (expand e^V = 1+(e^V-1); "Connected components of intersecting
  dependence regions define the first polymer activities"), integrated under "the one sector Gaussian/Haar law"
  (09:105), then the logarithm by Theorem ch08:kp (09:148-155). Elementary factors: table 09:123-135 (stationary cubic
  remainder, centered determinant variation, Haar remainder, inherited loop variation, covariance and stationary
  residual). The sector: 06:85-88 "An allocation sector fixes the selection, its assignment to connected components of
  its neighborhoods, a rooted spanning tree in every block, and all frame and block average tags. Tree links are set to
  the identity. These choices fix the coordinates and supports before differentiation."
- `F_x = sum_a p_{xa} f_a^0`, `M_x = sum_a p_{xa} h_{X_a} f_a^0` (09:319-320). `F_y^{(i)}` = "the same local formula on
  Lambda_i with its flat value subtracted" (09:331-332). `G_x`, `L_x`: (ch09:localization) 09:333-342.
- Dependence on sector choices [mine, from the definitions]:
  * forest: yes. The integration variables are "the free fine coordinates after tree gauge fixing" (09sr:33-35), the
    chart is "the actual tree-gauge configuration map" (09sr:114), the finite-range covariance and windows live on
    those coordinates (09:53-54, 06:442-451), "The flat reference determinant uses the same forest as the sector"
    (09:74-75). Which links are free, and hence each Haar remainder, cubic remainder and covariance residual, depends
    on the tree.
  * large-field selection: empty for these terms ("no incoming activity factor or large-field component").
  * frame / block-average tags: no dependence left in the pure small-field integral: "Tag probabilities sum to one, so
    there is no additional tag-count factor" and "all live tag actions coincide with phi" (09sr:127-135); on the
    minimizing branch the tags are redundant labels with uniform mass (04:208-209).
  * roots: block roots are the coarse sites Ly of centered blocks (05:916-918); canonical, H_4-symmetric.
  * orientations: the action is the H_4 average (04:518-520), the stack carries the square roots of the weights
    (06:452-453); symmetric.
  * the selected finite set and the truncation: a choice. Scott D:353 makes it symmetric: "Fix an exhaustion of the
    low-order addresses by finite sets invariant under translations and signed permutations, and select the low-order
    terms in one of these sets." v3 has no such sentence (09:383-387 only says the coefficients "depend only on the
    prescribed path, actual inverse coupling and fixed labels").
  * incoming activities: none (09:383-384).

### (B)
- `f_i`: all preliminary regular functions of (ch09:early), 09:397-406: the localized low-order activities G_x, the
  degree >= 3 cluster terms (09:170-194), the inherited terms linear in an incoming regular activity (09:204-286), and
  the truncation tail. All are produced in the same fixed-forest sector; the inherited ones also depend on the incoming
  family.
- `q_f(q,r) = D^2[f(exp .)](0)[A^{q,T_*},A^{r,T_*}]`, with `A^{q,T}_c(y)=1_{c=b} xi_o(y)^a T` for q=(a,b), `q_f=0` if
  Z=X u N_2(o) wraps (09:462-472). A real symmetric 6x6 matrix in plaquette orientations, depending on f and its anchor.
- The sum over `o_i=o` is the anchored sum of (ch09:early-bounds), 09:413; absolutely convergent by
  t^2|q_f(q,r)| <= 3 a_f (09:503).

## 2. Is the covariance available in v3?

What is needed.
- For 09:362 literally: for every coarse translation b a bijection a -> a' of the selected labels with X_{a'}=X_a+b,
  share transported, and f_{a'}^0(1)=f_a^0(1). (Only flat values.)
- For 09:348-357 (L_x=0): the same with full values f_{a'}^0(U)=f_a^0(tau_b^* U), plus the same for the reflection
  of each coordinate axis about a coarse site, plus compatibility between the formula on the auxiliary tori and on the
  actual torus. Computation [mine]: the number of all-interior sites of Lambda_i is 2^4 (w+i-2R+1)^4, the factor 2^4
  being the 16 choices of fold slope (pi_v(q)=min(qbar,2v-qbar), 09:327; on the decreasing branch the field is the
  reflected field with "Reversed links ... inverted", 09:330). sum_i (-1)^i C(4,i) i^4 = -4+96-324+256 = 24, so the
  weights lambda_i = (-1)^i C(4,i)/(2^4 4!) return (1/16) sum over the 16 slopes eps of [F_x^eps(U)-F_x^eps(1)], where
  F^eps is the formula evaluated on the eps-reflected field. This equals F_x(U)-F_x(1) only if F is reflection
  covariant. v3's "only the all-interior class has degree four, with leading coefficient 2^4" (09:353-354) merges the
  16 slope classes silently. Scott says it: "Signed-permutation invariance identifies the values of the 2^4 interior
  slope classes with F_x(V)-F_x(1)" (D:397). Martin: "the auxiliary densities transform covariantly under signed lattice
  symmetries" is a listed hypothesis (five-period-localization.tex:79-81) and "Reflection covariance first moves q to
  its canonical folded representative" (ibid. 123-124).
- For 09:521: for every g in (torus translations) x| H_4 a permutation i -> g.i of the regular labels with
  o_{g.i}=g o_i, X_{g.i}=g X_i and f_{g.i}(U)=f_i(g^*U). Then sum_{o_i=o} q_{f_i} is independent of o and invariant
  under the stabilizer H_4 of o acting on orientation pairs with signs; the reflection/permutation argument of
  09:525-526 is then correct (checked: for q != r some axis lies in exactly one of them, e.g. q=(1,2), r=(3,4): axis 1;
  q=(1,2), r=(1,3): axis 2; its reflection flips the sign of exactly one curl).

What v3 contains.
- [v3 proves] covariance of the block kernel: "It is covariant under fine gauge transformations ... It is also covariant
  under signed coordinate permutations and corresponding fine/coarse translations" (04:262-264, proof 04:277-282).
- [v3 states] the path action is the H_4 average (04:518-520), coefficients independent of the site.
- [v3 states] regular activities are "gauge-invariant" and local (04:435-438). Nothing about lattice symmetries: neither
  Definition ch04:activities, nor the tuple/density definition (04:550-562), nor the admissibility section (04:622-668),
  nor the preparatory output (09:397-423), nor Theorem ch09:step-theorem (09:909-952) requires or asserts that the
  activity families are equivariant. grep for "equivarian", "covarian", "hypercub", "symmetr" in chapters 4, 6, 8, 9,
  10 finds, about activities, only the two sentences 09:362 and 09:521.
- The symmetry sentences about the forest in v3 are of a different kind: 06:966-967 "This argument also applies to each
  signed orientation with its transported forest; it never assumes that a rooted response commutes with the symmetry";
  06:1420-1424 "let sigma range over the signed lattice orientations with their probability weights omega_sigma,
  transforming the field, forest, tags, selection, and rows together" - an average of energies (rows of the H_4-averaged
  action), eq. (ch06:component-extracted-energy), not an average of the construction; 09:574 "After the common
  signed-symmetry average" - again the action. v3 has no average over forests.
- Invariance of the function Z_blk under the lattice group follows from 04:262-264 and invariance of the input density
  [mine; v3 does not state invariance of dens(rho) anywhere]. This is a statement about the total only.
- Forest independence of the total: the pure block integral (09sr:117) and Z_blk are integrals of a gauge-invariant
  integrand over Haar measure; tree gauge is an exact change of variables for the gauge transformations trivial at block
  roots. Scott states it: "Tree gauge is an exact Haar change of variables ... For fixed V, gauge transformations fixing
  every block root leave the kernel of Definition D04 invariant" (B-section.tex:583). v3 does not state this (closest:
  09:72-79 on recovering the Haar integral; 07:889-893). So the SUM of all terms and the integrated result are forest
  independent [mine], but that gives nothing term by term: the terms are produced by a Taylor/cluster split in tree
  coordinates, and a partial sum by number of elementary factors (which is what "low-order" selects) is not a
  gauge-invariant grading. Lean records exactly this warning: "The fixed-forest E6 formula cannot be averaged factor by
  factor just because it has a sum/integral invariant under changing the tree. Use a SPECIFIC law with independent
  choices in the rooted blocks." (YM/PhysicalNext/RG_NEXT_ALL_FIELD_EXPANSION_DERIVATIVES/Wood.lean:6-8).
  [unsettled] I cannot exhibit from the texts a specific term whose flat value differs between two trees; the claim that
  individual f_a^0 are forest dependent is an inference from how they are built.

## 3. Scott, Martin, Lean

Scott.
- Class: Lemma D1 (D:583) "both activity families are countable and equivariant under translations and H_4, including
  supports, anchors, inventories and tests." Proof sentence (D:607): "Subtraction and path replacement transport the
  entire address under translations. Signed permutations transform the curvature orientations with their signs; the
  finite group average includes every transformed term."
- Sector expansion (D:197, end of Step 6): "Translation and signed permutations transport complete read supports, factors
  and sectors; their finite average gives equivariance." This one sentence is the whole justification; the average is
  not constructed. The tree is fixed: "We therefore fix, once for each continuous input curve, all choices ...: the tree
  gauge, the address identifications, the truncation index and the auxiliary tori" (D:840); "Choose one reference tree
  and translate it over the cells" (D:1197); "In each block ... fix an axial spanning tree rooted at l y" (B:437).
- (A): "Translation symmetry makes F_x(1) independent of x." (D:382); D:353 and D:397 quoted above.
- (B): "Sum q_{f_{i,u}} at each anchor. Translation covariance makes the result independent of the anchor. Reflection in
  an axis belonging to exactly one of two distinct orientations changes the sign of the off-diagonal entry ... Permuting
  axes identifies the diagonal entries." (D:528).
- [mine] Scott therefore assumes equivariance as a property of the class and asserts it for the output by a "finite
  average" that the text does not carry out. With one global forest a global average over transported sectors does not
  produce a polymer gas (Martin's remark below), so Scott's text is itself incomplete here.

Martin.
- "The exact block gas ... was constructed with a fixed forest. To restore the lattice symmetries we average over forests
  before taking the logarithm of the flag-free gas." (forest-average-log.tex:9-11). Flat determinant forest independent
  (15-79). "At each coarse site x, choose independently a uniform forest F_x from this finite set. On the block with
  root x, use only the restriction of F_x." (85-87). Factorization E_F prod a_M^F = prod E_F a_M^F for compatible
  components, with the remark "it does not hold for an arbitrary average over one global forest" (104-110). "A signed
  lattice transformation permutes the site choices and transforms every chosen forest by a bijection. Its product
  uniform measure is unchanged. The covariance of the individual sector formulas consequently gives the same covariance
  for bar a_M" (117-121).
- (A): hypotheses five-period-localization.tex:79-86; "Translation covariance makes f_Lambda(o,1) independent of o"
  (176-177).
- (B): hypothesis physical-reset-reorganization.tex:22-24 "All entries transform under the same permutations of labels
  for translations and signed lattice symmetries"; then 139-146 "Reindexing the label series by a translation shows that
  Q_o is independent of o. Reindexing by a reflection of an axis ... An unsigned permutation carries any plaquette pair
  to any other ... Consequently there is one real number Delta with Q_o(a,d)=Delta delta_{ad}".

Lean (files read; `lake env lean` run once on a scratch file, no build).
- Statement of (B): `YM.AnalyticBridge.VerifiedReset.Averaging.isotropic`
  (YM/AnalyticBridge/VERIFIED_RESET_STEP/Isotropy.lean:77): for `G.Simple`, `Projects A p c`, `4 <= n`, and
  `hm : forall s b, Nonempty (A.Moves s b)`, `total A o a b = if a=b then delta A else 0`, where
  `total A o a b = sum' i, if (A.reg i).site = o then projection (A.reg i) (A.E i) a b else 0` and
  `delta A = total A 0 axes01 axes01`. `#print axioms`: propext, Classical.choice, Quot.sound. Companion
  `identity` (:100) and `delta_bound` (:103, `p.threshold^2 * |delta A| <= c`, v3's (ch09:delta-bound)).
- The symmetry hypothesis: `YM.RG.Activities.Moves s b` (YM/RG/Activities.lean:87-96, "Transports of whole labels"):
  permutations `ep, kp` of the labels with `reg_site`, `reg_support`, `forced_support`, `forced_inventory`,
  `forced_tests`, `valuesE : A.E (ep i) U = A.E i (pull s b U)`, `valuesK`. It is a field of the class:
  `YM.RG.Activities.Valid` has `moves : forall s b, Nonempty (A.Moves s b)` (:104-109, confirmed by `#print`). The reset
  step takes it as hypothesis `Collection.Local.transforms` (VERIFIED_RESET_STEP/Trays.lean:38) and proves it for its
  output (`fittings`, Trays.lean:131-150).
- How Lean gets it for the sector expansion: independent forest tags per coarse site. Header of
  YM/PhysicalNext/AFTERNOON_INTERACTING_RANK_COMPARISON/Orchards.lean:22-30: "Shuffle local tree tags independently by
  physical coarse site ... across any signed orientation a Perm"; `transportable` (:92): there is a permutation E of the
  seeds with `(canopy S).grow (E t) = Locations.forest s b ((canopy S).grow t)`. Wood.lean header quoted in section 2.
  `Islet.lean:40` "Weighted theta and forest average, mask-free principal calculation" (the inherited term).
  So Lean follows Martin, not a fixed translated tree, for the activities. (`YM.Bid.F05`, Bid/Station.lean:94-99, is a
  `def ... : Prop` stating forest independence of the stationary value and of the thermal term up to a constant; it
  concerns the chapter-7 quantities, not the activities.)
  [unsettled] I did not trace the chain from `transportable` to the `transforms` hypothesis of the reset step.

## 4. (B): what holds without hypercubic covariance

- Gauge invariance and the Ward argument of 09:472-481 give [v3 proves]: the affine Hessian depends only on constant
  curls, and in the colour indices it is a multiple of the invariant metric. This fixes the colour structure only. In
  the orientation indices any real symmetric 6x6 matrix S gives a gauge-invariant quadratic form
  (1/2) sum S_{qr} <F_q,F_r>; nothing in gauge invariance selects delta_{qr}. v3 has no other argument; 09:525-526 uses
  the lattice group and nothing else.
- With translation covariance only: sum_{o_i=o} q_{f_i}(q,r) = Delta_{qr}, a symmetric matrix independent of o (21
  numbers).
- With translations and axis reflections (e.g. translated axial tree): off-diagonal entries vanish, leaving six diagonal
  numbers Delta_q, not shown equal.
- No single tree gives the rest [mine]: let sigma be a coordinate permutation and p the parent map of a rooted spanning
  tree invariant under S_4. At x=(1,1,1,1) invariance forces p(x) to be fixed by S_4, but no neighbour x +- e_a is. So
  for L >= 3 no block tree is S_4-invariant; an average is unavoidable.
- The anisotropic part cannot be discarded: (1/2) sum_o h_o sum (Delta_{qr}-Delta delta_{qr}) <F_q,F_r>(o) has a
  nonzero affine Hessian at every anchor, so it violates the normalization condition 04:627-642 and is of the marginal
  size t^2 |Delta'|; it is neither path action nor admissible regular activity.
- From invariance of the total alone [mine, sketch]: on globally small-field fields sum_i f_i is H_4-invariant, hence
  (1/2) sum_o (Delta - h.Delta)_{qr} <F_q,F_r>(o) = - sum_i [R_{f_i}(U) - R_{f_i}(hU)]. The right side has zero affine
  Hessian term by term but does not vanish on slowly varying fields; testing with a field varying on scale l gives
  only |Delta - h.Delta| = O(H_pre t^{-2} / l), l at most the torus side. This is not the exact identity needed, and
  affine fields do not exist globally on the torus. The "intrinsic" identification 09:748-766 does not help: it
  determines the scalar "only because the full-field identity has already been established" (09:764-765).

## 5. Conclusions and repairs

(A) 09:362.
- Status: TRUE but justification incomplete. Missing statement: translation covariance of the selected low-order family
  (labels, supports, shares, values), which requires (i) a forest invariant under coarse translations, (ii) a selected
  set and truncation invariant under them (Scott D:353), (iii) the same formula on the auxiliary tori.
- A translated reference tree (17:164-166) suffices for the sentence at 09:362. Alternatively the sentence can be
  deleted: summing (ch09:localization) over x gives sum_x M_x = sum_x F_x(1) + sum_x h G_x + sum_x L_x with no
  covariance, and the constant is fixed afterwards by v_sc = |Lambda|^{-1} log Z_blk(1) (09:727).
- It does NOT suffice for 09:348-357 (L_x=0), which additionally needs covariance under axis reflections about coarse
  sites; otherwise L_x = F_x - (1/16) sum_eps F_x^eps - (flat part) is nonzero on small-field regions and is not a
  large-field correction. Smallest repair consistent with a fixed forest: take the reference tree invariant under the
  axis reflections through its root (the axial tree of Scott B:437: route to the root changing coordinates in a fixed
  order) and say so, together with Scott's sentences D:353 (invariant selection) and D:397 (identification of the 2^4
  slope classes). If the forest average of (B) is adopted, this is automatic.

(B) 09:521.
- Status: GAP. Not derivable from what v3 contains. Needed:
  1. add to the class of density tuples and to Theorem ch09:step-theorem (hypothesis and conclusion) that both activity
     families are equivariant under translations and H_4 "including supports, anchors, inventories and tests" (Scott
     D:583; Lean `Activities.Valid.moves`; Martin physical-reset-reorganization.tex:22-24); the Wilson start has it
     (09:885-886 "with the signed average"; Scott D:835);
  2. make the sector construction equivariant by Martin's forest average: forest-independent flat determinant, an
     independent uniform forest at each coarse site, average of the integrated polymer activities before the logarithm,
     factorization for compatible components (forest-average-log.tex:15-121). An independent per-site choice among the
     24 axial orders would be a smaller symmetric family [mine, not checked]. A fixed translated tree, or a global
     average over transported forests, does not do it;
  3. keep selected sets, truncations and auxiliary tori invariant (Scott D:353).
  Then 09:521 is Martin's reindexing argument (physical-reset-reorganization.tex:139-146) and 09:362, 09:348-357 follow
  as well.
- Interaction with chapter 17: under the per-site average the sector forests are not translation invariant, so the
  assumption at 17:164-166 must be read as a choice made for the zero-background, forest-independent computation there
  (or 17:163-181 reworded in the kernel norm of 05:873-877, as the earlier report's option (b)).

## 6. Not read / not checked

- v3: chapters 1-3, 5 (only 905-925 and greps), 6 except 55-100, 440-460, 955-975, 1355-1440, 1555-1568; 7 (greps only);
  8 (grep only); 10-19 (greps only). 09-renormalization.tex and 09-stationary-remainder.tex were read in full.
- Scott: D-section only at lines 83-96, 197-209, 314, 345-400, 500-536, 582-610, 838-846; B-section by grep; C-section
  only the line 412 match; part1 not read.
- Martin: forest-average-log.tex in full; five-period-localization.tex 60-200; physical-reset-reorganization.tex 10-30,
  120-152 and grep; gaussian-reassembly.tex, selected-nonlinear-offering and all other files not read.
- Lean: Isotropy.lean in full; RG/Activities.lean 70-125; Trays.lean 20-60, 105-155; Orchards.lean 1-30, 60-100; Wood.lean
  header; Islet.lean 25-60; Bid/Station.lean 85-100. One `lake env lean` run (#check/#print/#print axioms on
  `Averaging.isotropic` and `Activities.Valid`). The Lean proof that the sector output satisfies `Moves` was not traced.
- No LaTeX build, no edits, no git operations.
