# Independent review: forest average (v3 chapter 9 draft repair)

Reviewed: uncommitted change in /Users/mgubi/ym-terminology (new `chapters/09-forest-average.tex`, 699 lines; 21 line
edits in `09-renormalization.tex`; 2 in `17-current-contraction.tex`). Read-only; nothing edited, staged or built.
The draft and diff were read and checked before the author's report. "v3" = manuscript/HumanizeYM_v3/chapters (NN:line),
"FA" = 09-forest-average.tex (line), "Martin" = manuscript/existence.
Classification used below: ERROR (wrong mathematics), GAP (unproved or unstated), RISK (plausible, unverified
downstream effect), NOTE.

## 0. Verdicts

| part | verdict |
|---|---|
| new subsection 09-forest-average.tex | ACCEPT WITH CHANGES (as a draft). No wrong mathematics found. Changes C1-C6 below; C1 and C2 are real gaps in what is assumed. |
| line edits to 09-renormalization.tex | ACCEPT WITH CHANGES. Every new sentence is true given the subsection; three need rewording (C5, C7, C8). |
| edit to 17-current-contraction.tex | ACCEPT AS A DRAFT. True as a clarification; the reason why the choice is "free" is still not given (C9). |

Smaller repair (equivariance only as a hypothesis, G_x and L_x unchanged): logically sufficient for a conditional
step theorem, but NOT safer; see section 7.

No ERROR was found in any definition, lemma, proposition or proof of the new subsection. The four results that carry
proofs (FA Lemma forest-determinant, Lemma symmetric-localization, Lemma isotropy, Proposition output-equivariance) were
recomputed and are correct. What is open is (i) the Assumption, which v3 neither proves nor displays, (ii) three
things used beyond the Assumption (C1, C2, k_i), (iii) chapters 10 and 11, which the change makes conditional or
incomplete without saying so.

## 1. The new subsection, statement by statement

### 1.1 Introduction (FA 6-31)
- "for L>=3 no spanning tree of the centered block rooted at the center is invariant under the coordinate permutations"
  (FA 13-16): correct. (1,1,1,1) lies in the block (radius (L-1)/2 >= 1), is not the root, is fixed by S_4, and none
  of its eight neighbours is fixed.
- "an average over one global choice would not preserve the product structure" (FA 24-25), and FA 329-332 "It fails ...
  for the uniform measure on the translates and signed images of one reference forest": the first is right; the
  second should read "can fail / is not available" (a product formula can hold by accident). Wording only.

### 1.2 Group, action, Definition ch09:equivariant (FA 33-91)
- g(y)=hy+b on the coarse torus, x -> hx+Lb on the fine torus, maps B(y) onto B(gy) and roots to roots: correct (odd
  L, centered blocks; 05:916-917).
- (g^*U)(x,x')=U(gx,gx') agrees with 01:186-189 ("pulling back oriented paths, using inverse links when orientation is
  reversed"). (g1 g2)^* = g2^* g1^*: checked. (ch09:bad-transport): checked from 04:424-427 (Bad_m is defined by
  plaquette chords; the periodic distance is the sup-norm distance, 01:176-182, so N_r(hx)=hN_r(x)).
- Definition: exact as stated. The bijections i -> g.i are not required to form an action; no proof below needs that.
- Remark 2 (fine-torus equivariance restricts to x -> hx+Lb): correct, this is a subgroup.
- Remark 3 (equal shares): correct as a device. Its effect on anchored norms is not examined (see C4).

### 1.3 Lemma ch09:forest-determinant (FA 95-174): CORRECT, fully proved
Recomputed every step:
- edge count: |Lambda|(L^4-1) tree edges, 4L^4|Lambda| positive fine edges.
- four facts about alpha_F, B_F (both orientations of a tree edge checked: (d alpha)(e) = -u(e)); alpha_F d phi = -phi
  for root-zero phi.
- T_HF T_FH = 1 (uses B_F D_F = D_F and B_F d(alpha_H D_F u)=0); integer matrices, so |det|=1.
- A^0 B_H D_F = A^0 D_F by the hypothesis; (B_H D_F)^* A^0 = D_F A^0 by symmetry; T^* P_H T = P_F from the quadratic
  form identity (polarisation, both sides symmetric). Hence T^*(D_H A^0 D_H + P_H)T = D_F A^0 D_F + P_F and the
  determinants agree.
- Hypothesis check (FA 112-119): A^0 = d_1^* H_f d_1 + b Q^*Q annihilates root-zero gradients by (ch05:actual-Q),
  05:988-992. Confirmed. v3 states the same fact independently at 11-marked-insertions.tex:631-634 ("A P = A ... since
  its gauge potential vanishes at each block root"; "At zero background the actual row Gram is precisely A_F",
  11:667), which supports the draft's reading of what the flat reference matrix is.
- This is Martin forest-average-log.tex:15-79 with the two steps Martin leaves implicit written out. The tree-edge
  count is by "a spanning tree has L^4-1 edges" instead of Martin's height argument; both fine.
- NOTE: the lemma is unconditional, but its application to v3's "flat reference determinant" is not: v3 never gives a
  formula for that determinant (09:74-79 is prose). See C5.
- NOTE: 06:680-682 ("A change of tree coordinates preserves this combined integral, not its determinant factor in
  isolation") is about the field-dependent sector scalar C_Y, not the flat reference; no contradiction.

### 1.4 Assumption ch09:forest-assumption (FA 188-258): see section 2.

### 1.5 Proposition ch09:forest-average-prop (FA 272-327): CORRECT from (a), (b) [(c), (d) where stated]
- (i): for fixed U and fixed admissible family the factors depend on disjoint coordinate sets of a product measure;
  the index set does not depend on F (labels, X_M, I_M are F-independent by (a)); finite average exchanged with an
  absolutely convergent sum. Correct. This is exactly Martin (eq:forest-product-average) and lines 112-116.
- (ii): correct (triangle inequality).
- (iii): (gF)_{gy}=g(F_y) is a bijection of the forest set (g maps trees of B(y) rooted at Ly to trees of B(gy)
  rooted at L(gy)); uniform measure invariant; the displayed chain is right.
- Does an activity depend only on the trees of the blocks in its support? That is exactly part (b); the proposition
  is honest about using it. See 2(b).
- FA 334-352 ("apply without change"): the reasoning is sound at the level of detail of v3. I checked
  09-stationary-remainder.tex in full: (ch09:pure-small-bound) bounds the centred logarithm of the complete pure
  integral, a forest-independent quantity that may be computed in any one forest; the selected sum equals that total
  minus the non-selected terms, and those are bounded through majorants (09:170-202) that are label-based and uniform
  in F. So the remark at FA 343-352 is correct. The inherited single-activity bound (09:204-286) is per forest and
  linear in the activity, so it passes to the average (edit at 09:239-240 is right).
- FA 354-362 (tori): correct given (b) on both tori AND fixed-forest agreement between tori. The latter is a
  hypothesis that appears nowhere in the Assumption or in the theorem. GAP, see C2.

### 1.6 Proposition ch09:family-equivariance (FA 366-429)
- (i) correct: incompatibility = intersecting supports (08:83-88), preserved by g; values by (iii) above.
- (ii) correct as an argument, with one GAP (C1): the display (ch09:share-equivariance) for F_x uses
  "f^0_{a'}(U)=f^0_a(g^*U)" (FA 420) for the UNMASKED selected terms f_a^0 of 09:319, whereas (i) and Assumption (d)
  only transport the activities a_M (which, as in Martin's w_i = 1_{X_i cap Flags = empty} f_i, carry their small-field
  indicator; v3's M_x has h_{X_a} f_a^0). The unmasked extension off the small-field set is a choice; its equivariance
  does not follow from that of the masked function.
- (ii) "The path terms ... are transported because the path action is invariant" with a forward reference to the proof
  of Proposition output-equivariance: that proof (FA 656-663) is correct (k^* k'^* = (k'k)^*,
  k^* tau_b^* = tau_{k^{-1}b}^* k^*; P^raw is a site sum with site-independent coefficients, 04:511-520). Fine, but
  the forward reference should become a short lemma placed before both uses.
- (ii) applies equal shares also to "the terms linear in an incoming regular activity". That conflicts in letter with
  09:234-237 ("There are L^4 fine anchors above each coarse anchor. Consequently the inherited principal norm is at
  most V_j L^{-1} eps"), which counts one coarse anchor per term. RISK, see C4.
- (iii) correct, conditional on the Assumption for each auxiliary torus.
- FA 431-434: a G-invariant finite set containing a given finite set exists. True, but not enough for the use at
  09:331 ("the same local formula on Lambda_i"): the selected sets on Lambda and on the five Lambda_i must correspond
  under local identification. See C2.
- FA 436-443: equivariance of the preliminary large-field family (k_i) is not proved (v3 has no formula for k_i); it
  is put into the hypotheses of Proposition output-equivariance and of the theorem. Acceptable in a draft, must stay
  listed as open.

### 1.7 Lemma ch09:symmetric-localization (FA 456-529): CORRECT, fully proved
- Identity: recomputed. Uses only M_{hx}(U)=M_x(h^*U) (the MASKED functions; so C1 does not touch this lemma),
  N_r(hx)=hN_r(x), substitution x=h^{-1}x', linearity.
- Vanishing of hat L_x: Bad(h^*U)=h^{-1}Bad(U), so N_{2 bar w}(h^{-1}x) is small-field for h^*U. Correct.
- (h^*U)_{i,h^{-1}x} is the pullback of U under q -> x+h pi_{w+i}(q): checked. Dependence region x+h({0..w+4}^4),
  inside the sup-norm ball N_{bar w}(x), bar w = w+5. Correct.
- H_4-equivariance by h=kh'; translation covariance by tau_b h = h tau_{h^{-1}b}: both checked.
- The motivating claim (FA 447-454) that (G_x) is not reflection-covariant is right, and I verified it explicitly:
  with r the reflection of axis c about x, pi_v(q+v)=v-pi_v(q) gives
  G_x(r^*U) = sum_i lambda_i S_i(U; x-(w+i)e_c), S_i(U;z)=sum_y F_y^{(i)}(U_{i,z}),
  whereas G_x(U)=sum_i lambda_i S_i(U;x). The shift depends on i, so no reindexing identifies them.
- FA 519-529 (bounds): each term of the average is a fold of the same type (nearest neighbours to nearest neighbours,
  direction kept or reversed, distance from the anchor preserved), so Martin's derivative cost
  (eq:five-period-derivative-cost) applies with the same constant. Plausible; unproved in the same sense as v3's own
  one-sentence derivation at 09:371-372. Martin charges an explicit constant C_turn for this average
  (selected-nonlinear-offering.tex:138, 418); v3's P_j absorbs it. GAP of the pre-existing kind.

### 1.8 Lemma ch09:isotropy (FA 533-627): CORRECT, fully proved
Redone independently.
- Affine pullback: for eps_a=+1 and eps_a=-1 separately, (g^*A)(x,x+e_a)=u'_a+sum_nu xi_o(x)^nu eps_a eps_nu
  v_{sigma(a)sigma(nu)}; the constant v_{sigma(a)sigma(a)} in the reversed case is right. Curl:
  w'_{ab}=eps_a eps_b w_{sigma(a)sigma(b)} = s_h(q) w_{h.q}. Checked, including the sign when sigma(a)>sigma(b).
- Hessian identity D^2[f(exp .)](0)[A,A~]=sum q_f(q,r)<w_q,w~_r>: follows from 09:462-481 (dependence on curls only,
  colour form a multiple of the metric, |T_*|=1). q_{f_{g.i}}(h.q,h.r)=s_h(q)s_h(r)q_{f_i}(q,r): checked. Wrapping
  convention is preserved (Z_{g.i}=gZ_i).
- Clover: the loop (eps' e_{sigma(a)}, eta' e_{sigma(b)}, -, -) from go is the reverse of
  (eta' e_{sigma(b)}, eps' e_{sigma(a)}, -, -) from the same base point; proj(u-u^{-1}) is odd. So
  F^cl_q(g^*U,o)=s_h(q)F^cl_{h.q}(U,go). Checked.
- (ii): i -> g.i maps {o_i=o} onto {o_i=go}. Translations: S_{o+b}=S_o. Reflection of an axis c lying in exactly one
  of q != r (exists: symmetric difference of two distinct 2-subsets), about o (b=o-ho): h.q=q, h.r=r,
  s_h(q)s_h(r)=-1, so S_o(q,r)=0. Unsigned permutation: s_h(q)=+-1, squared 1, S_o(q',q')=S_o(q,q); the six planes are
  one S_4-orbit. All correct.
- Martin (physical-reset-reorganization.tex:139-146) only says "Reindexing the label series by a translation ... by a
  reflection of an axis lying in exactly one of two distinct plaquette pairs changes the sign ... An unsigned
  permutation carries any plaquette pair to any other". The transformation law is asserted there (ibid. 165-167 "a
  signed lattice symmetry permutes these four loops and their signs. This gives exactly the signed two-form
  transformation law"). The draft proves what Martin asserts.

### 1.9 Proposition ch09:output-equivariance and the Wilson paragraph (FA 631-699): CORRECT from its hypotheses
- Q_{f_i}(g^*U)=Q_{f_{g.i}}(U), R, zeta: checked. Channels (k,d) of the averaged path action: checked. K_P: connected
  selections, Y_P, I_P and the indicator are transported; correct.
- Hypothesis list is honest: (f_i), (k_i) equivariant and L_x symmetrised.
- Wilson: R(u) is a class function even under inversion (W, |F|^2 and T_4 are; T_4 is Ad-invariant because psi is
  Ad-equivariant, and homogeneous of degree four). Four equal shares give 24/4 = 6 terms per anchor, the same count
  as one anchor per plaquette, so the bound C_j beta t^5 at 09:868 is unaffected. The large-field assignment is
  canonical: two components with witnesses within B of one plaquette would have overlapping 2B-neighbourhoods. Correct.
  Martin instead labels the oriented plaquettes by (s,x,b) with weight 1/|S| (wilson-startup-construction.tex:147-158);
  the four-share device is the draft's own, equivalent in effect.

## 2. The Assumption, part by part

General: as mathematics (a)-(d) are precise. As a claim about v3 they are checkable only once chapters 6/9 display
the reassembly identity; v3 itself says (06:1560-1568) that "those identities, and the subsequent connected
regrouping, are distinct from the analytic bounds proved here". The objects \mathscr S, c, \mathsf A^0 and the label
set are not tied to named objects of v3.
Wording: the Assumption begins "Under the hypotheses of Theorem ch09:step-theorem", and the theorem (09:926) assumes
the Assumption. Not a logical circle, but must be rephrased (C3).

- (a) Form. v3: LEAVES OPEN (prose only, 09:56-96, 09:148-161, 06:1549-1568). Not false as far as I can see; it is
  Martin's (eq:reassembly-block-gas) with scalar (eq:reassembly-overhead) "O = L m^N (det A_0)^{-1/2}". Three points:
  1. compatibility by disjoint full dependence regions X_M and exact cover of Bad_m by the I_M agrees with 09:82-95.
  2. F-independence of the label set by the "absent factor has value zero" convention is the draft's device; fine.
  3. MISSING: that a label with I_M empty has a_M^F = h_{X_M} f_M^F with a local extension f_M^F (Martin
     forest-average-log.tex:187-193, eq:forest-cluster-mask). v3 uses it at 09:319-320. See C1.
- (b) Locality in the forest. v3: MAKES PLAUSIBLE, does not state. 06:777-778 "A factor's dependence region includes
  every cutoff test, block average path, window matrix entry and frozen coordinate needed to evaluate it"; the
  covariance is built from window inverses A[Omega_i,Omega_i] (06:520-537) of a matrix that depends on the forest
  only through which edges are coordinates, and m_Y=-P^*f_Y is equally local. So if X_M is a union of whole blocks
  containing every window of every coordinate read, (b) holds. Not written anywhere in v3; and v3 warns
  (06:779-783) that the reference law is conditional on the frozen links, so even the fixed-forest factorisation of
  09:82-87 is asserted rather than proved. Martin gives a three-sentence argument (lines 93-103). OPEN, plausible.
- (c) Uniform bounds. v3: SUPPORTS for the local constants (05:961-966 "finitely many directions and local tree
  shapes at fixed L; take their common radius and bounds"; 05:1041 "uniform in the period and in the allowed trees";
  06:353-355 "Any tree in a fixed block has uniformly bounded path length"). Chapter 5 is written for arbitrary
  per-block trees and puts its Fourier bounds on the forest-free W_a (05:1151-1154, 1234), so independent trees are
  admissible. For (ch09:joint-input), the table and the comparison estimates uniformity is not stated. OPEN, plausible.
  "Finitely many tree shapes" alone does not give it for supports of unbounded size; the local form of the constants
  does.
- (d) Transport. v3: PROVES for the block kernel (04:255-282) and has the H_4-averaged path action (04:511-520);
  everything else OPEN. I found no choice in the parts of chapter 6 I read that is visibly non-covariant (cutoffs are
  functions of chords, windows are defined by distance, ownership by neighbourhoods; axial/radial gauges occur only in
  estimates). 06:1420-1424 transports "field, forest, tags, selection, and rows together", which is the same idea.
  Martin only asserts it ("The covariance of the individual sector formulas", line 119).
- None of (a)-(d) looks false.

Used in the new proofs beyond (a)-(d):
 1. equivariance (and forest locality, bounds) of the unmasked extensions f_a^0 [C1];
 2. fixed-forest agreement between tori, and selected sets that correspond between tori [C2];
 3. equivariance of the preliminary large-field family (k_i) [stated as a hypothesis, FA 436-443];
 4. that L_x=0 on small-field N_{2 bar w}(x) (hypothesis of Lemma symmetric-localization; needs (iii) on the Lambda_i);
 5. the folded-derivative bound for the h-twisted folds (FA 519-526);
 6. compatibility of equal-share anchoring with the anchored bound (ch09:early-bounds) and with 09:234 [C4].

## 3. Faithfulness to Martin

Corresponding passages.
- Average and its law. Martin forest-average-log.tex:85-91: "At each coarse site x, choose independently a uniform
  forest F_x from this finite set. On the block with root x, use only the restriction of F_x." Draft: uniform measure on
  the product of the sets of block trees (FA 262-265). Same law when global forests are products of block trees, which
  is v3's definition.
- Factorisation. Martin 103-110: "Independence of the site choices therefore gives E_F prod a_M^F = prod E_F a_M^F.
  This is the factorization of a product measure over disjoint coordinate sets; it does not hold for an arbitrary
  average over one global forest." Draft: Proposition (i), FA 329-332. Same.
- Covariance. Martin 117-121: "A signed lattice transformation permutes the site choices and transforms every chosen
  forest by a bijection. Its product uniform measure is unchanged. The covariance of the individual sector formulas
  consequently gives the same covariance for bar a_M". Draft: (d) assumed, (iii) proved. Same content.
- Equivariance as a hypothesis of the reset. Martin physical-reset-reorganization.tex:22-24: "All entries transform
  under the same permutations of labels for translations and signed lattice symmetries." Draft: 09:919.
- Symmetrised localisation. Martin selected-nonlinear-offering.tex:417-418: "The regular output consists of T_{x,d}
  and the folded counterterms, followed by the fixed symmetry average"; marked-block-integral.tex:268-275: "Write <.>
  for the uniform average over signed translations of the coarse lattice ... A = A_rem + < sum_o chi_o g_o >,
  R_0 = - < sum_o t_o >"; five-period-localization.tex:257-258: "A fixed signed-orientation average and its local
  allocation multiply this bound by the already purchased orientation cost." Draft: Lemma symmetric-localization. The
  H_4 average of G_x and L_x is therefore Martin's, not an invention.

The draft proves what Martin asserts: transformation law of q_f and of the clover (1.8); exactness and equivariance of
the symmetrised localisation (1.7); equivariance of the output of subtraction, path replacement and regrouping (1.9;
Martin: "with the original locality, symmetry and affine-Hessian conditions", reset:407-408).

Martin argues what the draft only assumes: forest locality (93-103); compatibility between tori by replication to a
product period (selected-nonlinear-offering.tex:190-272, incl. "Apply the displayed identity first to the block and
frame tags, then to the forest choices").

Dropped from Martin:
 - the masked form c_Gamma = 1_{X_Gamma healthy} F_Gamma and the derivative bounds for cluster terms
   (forest-average-log.tex:187-234) [relevant: C1];
 - the separation of the forced labels and the deletion ratio (123-185) [v3 uses 08 and 09:148-155; fine];
 - the forest average of the MARKED activities (marked-block-integral.tex:140-156: "We may therefore average
   independent forest choices ... a_C = E_F a_C^F, b_C = E_F b_C^F") [relevant: section 5];
 - the constant C_turn for the symmetry average.
Added relative to Martin: the four equal anchor shares at the Wilson start; equal shares for all cluster terms.
Nothing in the draft contradicts Martin.

## 4. The line edits

09-renormalization.tex
- 75: true only when the flat reference matrix satisfies the hypothesis of the lemma. v3 does not define that matrix.
  Reword (C5).
- 148: true (the cluster theorem is applied to the averaged activities, same majorants).
- 161: `\input` appended to a text line. Works; put it on its own line when line numbers no longer matter.
- 239-240: true; cites (c).
- 313: true but too weak for 09:331; see C2.
- 331: true given C2.
- 351: true, and it repairs a silent step. Checked: r: q_c -> -q_c on Lambda_i leaves U_{i,z} invariant because
  pi_v(-q)=pi_v(q), so F^{(i)}_{ry}(U_{i,z})=F^{(i)}_y(U_{i,z}). This is Martin's "Reflection covariance first moves q
  to its canonical folded representative" (five-period-localization.tex:123-124).
- 362: true.
- 367: true. Downstream effect of the redefinition: G_x, L_x occur nowhere outside 09:335-376 (grep over all chapters).
  After 367 they are used only through the bounds 09:373-376 (hold for the averages, 1.7), as members of (f_i) and of
  the logarithmic corrections. 09:357 ("L_x=0") precedes the redefinition and refers to the original L_x; the lemma
  gives the same for the average. Nothing later becomes false.
- 398: overstated. Equivariance of (f_i) depends on the Assumption and C1; that of (k_i) is assumed. Reword (C7).
- 521, 525, 526: true; Lemma isotropy.
- 867, 903: true (1.9).
- 919, 924-926, 939, 955: consistent. 926 is one very long sentence carrying four hypotheses; split and add C2 (C8).

Step theorem and chapter 10.
- Start: the Wilson families are equivariant (09:903, FA 688-695); zero arrays (10:780-783) trivially so.
- Each step: conclusion 09:939 by Proposition output-equivariance. Restriction of the parameter interval and replacing
  the returned coupling (10:784-788) do not touch labels or values. The coarse group is the full lattice group of the
  next fine torus. So the induction closes PROVIDED the Assumption (and items 1-3 of section 2) hold at every step.
- RISK 10a: Theorem ch10:finite-history (10:232-254) is stated unconditionally and now rests on an explicit unproved
  Assumption through 09:926. It must say so, or the Assumption must be discharged.
- RISK 10b: Proposition ch10:stability-assumption (10:428-447) defines the maps "for every allowed activity array of
  norm at most 1/8". The step is only defined on equivariant arrays (otherwise sum q_{f_i} is a 6x6 matrix, not
  Delta delta). Equivariance is a linear condition with fixed label bijections, so affine parameter lines between
  equivariant arrays stay equivariant (cf. 10:349 "The extrapolation preserves all linear symmetry and moment
  conditions"); "allowed" must include it. This defect existed before the change (the covariance was used silently);
  the change makes it visible.
- 10c: 10:256-257 "retaining its path arrays, forests, local integral choices" is stale: a history no longer has a
  forest.

## 5. Other chapters

- Chapter 6: no statement becomes false. A sector still fixes one forest (06:85-87); the average is taken afterwards.
  06:680-682 and 06:1565-1566 are compatible with the lemma. Chapter 6 should eventually say that the forest is
  averaged in chapter 9.
- Chapter 11 (RISK, not addressed by the change): 11-marked-insertions.tex:335 "normalize the unmarked local gas by
  the same exact connected expansion as in Chapter 9", 11:617 "on the selected forest", 11:679 "Fix a clean
  neighborhood and one forest, tag, coarse gauge and Gaussian sample", 11-restarted-history.tex:247 "forest charts".
  At zero source the marked expansion must reduce to the chapter 9 representation of the same history, which is now
  forest-averaged; so the marked activities must be averaged in the same way (Martin does exactly this,
  marked-block-integral.tex:140-156). The per-forest estimates of 11:617-690 survive (the identity
  (ch11:conditional-curvature) has a forest-independent right side), but the statement is missing. I did not read
  chapter 11 in full.
- Chapter 17: section 6.
- Chapters 12, 13: no use of forests or of G_x, L_x (grep). 13-continuum-fields.tex:59, 274 use hypercubic covariance of
  correlations, which is a property of totals and is unaffected.
- Chapter 7: computations are on W_a and the completed inverse; alpha is determined by a forest-independent total.
  Not affected as far as greps show.

## 6. Chapter 17 edit

New sentence (17:164-165): "take the forest ... to consist of the coarse translates of one reference tree. This fixes
a free choice for the present computation only; the average over forests of Section 9 is not used here, and
independence of the forest is not claimed for the forest-dependent jets z_2,z_3 themselves."
- True, and more careful than the old "this restricts only a free choice".
- GAP (pre-existing, unchanged): why the choice is free. The bounds on z_2,z_3 are used at 17:185-213 only inside
  pullbacks of anchored gauge-invariant functions along the stationary branch. Those are forest independent if two
  forest slices give stationary fields that differ by a gauge transformation equal to one at the block roots. v3 does
  not state this. With the per-site average the forests that occur in chapter 9 are not translation invariant, so this
  is exactly the statement needed to transfer the chapter 17 bound to them. Suggested addition (C9).

## 7. Is the smaller repair sufficient and safer?

Smaller repair = (1) equivariance of both incoming families as a hypothesis and of both outgoing families as a
conclusion of the step theorem, (2) an assumption that the preliminary families (f_i), (k_i) and the auxiliary
families F^{(i)} are equivariant, with a remark that this is arranged as in Martin, (3) G_x, L_x unchanged.
- Sufficient for a conditional theorem: yes. Lemma isotropy and Proposition output-equivariance need nothing else.
- Safer: no. With G_x unchanged, assumption (2) is contradicted by the construction on the page: G_x is not
  reflection-covariant even when F is (1.7, explicit formula), so the family (f_i) of 09:398 would not satisfy the
  hypothesis and 09:521 would remain false for the objects defined. The "remark on how it is arranged" would have to
  describe both the forest average and the symmetrisation anyway, i.e. the draft without its proofs.
- The redefinition of G_x, L_x is the least risky part of the draft: it is an exact linear identity, fully proved,
  it is what Martin does, and the symbols have no use outside 09:335-376.
- The risk in the draft lies elsewhere: the breadth of the Assumption and chapters 10-11. A defensible reduced
  version keeps Lemma forest-determinant, Lemma symmetric-localization, Lemma isotropy, Proposition
  output-equivariance (all unconditional given equivariant inputs) and states the forest-average part
  (Assumption, Propositions forest-average-prop and family-equivariance) as it is. That is the draft; I see no
  smaller change that is both true and closes 09:521.

## 8. Required changes

C1 (GAP; Assumption (a), Proposition family-equivariance). Add at the end of Assumption (a):
> For a label with $I_M=\varnothing$ there is a real Borel gauge-invariant function $f_M^F$, local on $X_M$, with
> $a_M^F=h_{X_M}f_M^F$. Parts (b)--(d) hold for the functions $f_M^F$ as well as for the $a_M^F$.
and in Proposition family-equivariance (i) define $F_\Gamma=\frac1{n!}\varphi^T(\Gamma)\prod_r\bar f_{M_r}$, note
$c_\Gamma=h_{X_\Gamma}F_\Gamma$ (as Martin (eq:forest-cluster-mask)), and state the transport for $F_\Gamma$; the
$f_a^0$ of 09:319 are these $F_\Gamma$. (Minimal alternative: claim (ch09:share-equivariance) for $M_x$ everywhere
and for $F_x$ only on configurations small-field on the support; that is all the later arguments use.)

C2 (GAP; hypotheses). Add a part (e) to the Assumption, cite it at 09:313, 09:331, 09:351 and FA 354-362:
> (e) \emph{Agreement between tori.} The selected low-order terms are those whose shape (support and factor data
> modulo translation) lies in one finite set of shapes invariant under $H_4$; the same set is used on $\Lambda$ and on
> every $\Lambda_i$. If a set of blocks of one of these tori is identified isometrically with a set of blocks of
> another, corresponding labels have equal fixed-forest values on corresponding fields whenever the trees in these
> blocks correspond.
and replace FA 431-434 by a reference to it.

C3 (wording). Assumption, first sentence: "Under the hypotheses of Theorem~\ref{ch09:step-theorem} other than the
present assumption, ...".

C4 (RISK). Proposition family-equivariance (ii): do not re-anchor the inherited terms. Replace "to the terms linear in
an incoming regular activity" by
> to the terms linear in an incoming regular activity, which keep the coarse anchor $y$ of the block
> $\mathbb B(y)$ containing the incoming anchor (this rule commutes with $\mathfrak G$ because $g\mathbb B(y)
> =\mathbb B(gy)$),
and add to the open points that re-anchoring a cluster term at an arbitrary site of its support costs a polynomial in
its diameter in the norm $\|\cdot\|_m$, to be absorbed in the support reserve of (ch09:early-bounds).

C5 (wording, 09:75). "sector; when the flat matrix annihilates gradients of site functions vanishing at the block
roots, as $d_{1,f}^*H_fd_{1,f}+b\mathcal Q^*\mathcal Q$ does, its value does not depend on that forest
(Lemma~\ref{ch09:forest-determinant})."

C6 (notation; FA). Real clashes inside chapter 9:
 - $F_y$ (tree of block $y$, FA 95, 216) against $F_x$, $F_y^{(i)}$ (09:319-336, FA 390); rename the forest ($T$ or
   $\mathsf F$) or its components;
 - $\mathfrak F$ (set of forests) against $\mathfrak F_m(U)$, the exact covers of 04:543;
 - $\mathcal Q$ (block-average derivative, FA 113-115) against $\mathcal Q$ (quadratic part of the path action,
   09:403, 408);
 - $h\in H_4$ against the indicators $h_X$, in the same formula at FA 486 ($h_{N_{\bar w}(x)}(h^*U)$); also $h$ of
   09:176;
 - $g\in\mathfrak G$ against $g=(\beta')^{-1/2}$ of 09:60;
 - $b$ (translation) against $b$ (penalty) at FA 37 and 113; $\sigma$ (permutation) against the support exponent;
   $\varepsilon_a$ (signs of $h$) against the loop signs $\varepsilon,\eta$ of 09:451 (FA 602 distinguishes them only
   by \epsilon/\varepsilon); $M$ (label) against $M_x$; $\tau_b$ against the scalar $\tau$; $k\in H_4$ against $k_i$;
   $\theta$ against $\theta$ of $H_{\rm pre}$; $\mathcal P$ against $P$ of Section fusion.
 All labels and macros resolve (checked every \ref/\eqref target; `assumption`, `enumitem`, `\gLie`, `\ZZ` exist).

C7 (wording, 09:398). "... give, under Assumption~\ref{ch09:forest-assumption} and the regrouping hypothesis stated
after Proposition~\ref{ch09:family-equivariance}, equivariant families ...".

C8 (wording, 09:924-926). Split into sentences and add "(including its part (e))"; FA 329-332 "fails" -> "is not
available in general".

C9 (suggestion, 17:165). Append: "The bounds are used below only for pullbacks of gauge-invariant functions along the
stationary branch; that these do not depend on the forest (two forest slices differ by a gauge transformation equal
to one at the block roots) is used here and is not proved in this chapter."

Follow-ups to record with the change (outside its files): 10a, 10b, 10c (section 4); chapter 11 marked activities
(section 5); a sentence in chapter 6.

## 9. Not read / not checked

- v3: chapters 2, 3, 12-16, 18, 19 (greps only); chapter 1 only 176-192; chapter 4 only 250-285, 415-470, 495-677;
  chapter 5 only 905-1160, 1228-1316; chapter 6 only 19-100, 336-356, 436-580, 645-684, 736-784, 958-1000, 1165-1262,
  1320-1440, 1482-1500, 1545-1568; chapter 7 only 570-578, 884-896; chapter 8 only 60-135; chapter 10 only 1-60,
  232-265, 415-470, 500-516, 620-632, 780-795; chapter 11 only 8-30, 296-345, 612-700 and restarted-history 240-250;
  chapter 17 only 36-60, 120-215. 09-renormalization.tex, 09-stationary-remainder.tex and the new file were read in
  full.
- Martin: forest-average-log, five-period-localization, physical-reset-reorganization, gaussian-reassembly in full;
  selected-nonlinear-offering 128-200, 258-272, 325-446; marked-block-integral 140-156, 262-306;
  wilson-startup-construction 140-160; projected-parameter-prices excerpts. Nothing else.
- Audit notes: ch9-covariance.md in full, forest-invariance.md lines 1-60 and its chapter 17 entries; the author's
  report in full (after forming the above).
- Not done: no LaTeX build (the author reports a clean build; I checked labels and macros by grep only); no Lean; no
  check of the Lean or v2 ("Scott") counterparts; the derivative-norm cost of signed pullbacks was not rederived; the
  claim that no step of chapter 6 breaks covariance rests on the excerpts listed.
