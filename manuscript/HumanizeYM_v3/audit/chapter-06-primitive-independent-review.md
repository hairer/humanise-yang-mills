# Independent review: Chapter6 primitive factors and component extraction

Reviewed the new primitive/component/linear-comparison and mean-cancellation sections. No chapter edits by this reviewer. Findings were sent to root and the Chapter6 author while corrections were being incorporated.

## Mean cancellation: checked

The identity `p=Tw` is correct for the same compatible quadratic pair. Here `p=(X_f^lin(a),Z^lin(a,h))`, `w=X_c^lin(h)`, and a is the actual stationary forest response. Exact quadratic minimization in physical counting norms gives `||p||²=||w||²`. With `T*p=w` and `T*T+N*N=I`,

`||p−Tw||² = ||w||²−2||w||²+||Tw||² = −||Nw||²`.

Nonnegativity on the left proves both `p=Tw` and `Nw=0`. This also supplies the null-row identity used in Martin's annular argument; it need not be separately assumed. It uses the actual same-stage curvature row factors and predictor, not just identical numerical bounds. Harmonic modes cause no exception.

The local mean transfer identity is also exact: with E=AP−I and m=−P*f, `m−v=E*v−P*(Av+f)`. On a common clean neighborhood, the one candidate tree-relative field and the same guide give row residual O(poly(B)t²+poly(B)t exp(−cR*)). Locality/decay transfers this to the actual mean. The full windows, row stencils and inactive-coordinate restriction must fit in that neighborhood, as stated; separate gauges/candidates for separate rows would not suffice.

## Important component error found and repaired in progress

The original component paragraph used only the six-term **core** lower bound to claim a pointwise small component amplitude after Gaussian extraction. That implication was invalid: extraction subtracts selected affine squares, leaving a potentially positive quadratic exponential in unbounded Gaussian coordinates.

Martin `actual-harvested-owner-energy.tex` supplies the required stronger identity (`eq:owner-ceiling-identity`, `eq:owner-actual-heft`): the charged energy is the signed average of core energy plus annular energy minus the **actual selected affine squares**, plus nonnegative mean squares. The current author added `ch06:annulus-extraction` and `ch06:component-extracted-energy` after this finding. The square-difference argument is correct on the protected actual signal: nonlinear residual is O(poly(B)t), its affine error is O(poly(B)t²+poly(B)t exp(−cR*)), so each subtracted row costs O(poly(B)t³+poly(B)t²exp(−cR*)). Coarse subtraction is O(t⁴), and unselected residual squares are nonnegative. There are O(B⁴ n) rows. Thus the extracted energy retains a positive multiple of t² n. The correction must be kept before asserting bounded pointwise product jets.

## Exact conditions still requiring explicit treatment in the edited paragraph

1. **Weak masks through300B.** Martin `packet-annulus.tex`353–379 requires fine chords≤t/2, predictor mismatches≤2Wt, coarse flag agreement/absence away from the selected set, and positive frame likelihood through300B, together with active-variable bounds through304B. Original selection consistency only within5B does not imply these conditions. They must be compulsory masks of the actual component. Then an annular anchor in (2B,200B] has all its relevant B-neighborhood and B/4 interior patches in the weak clean region.
2. **Actual signal reconstruction.** Active increments are bounded by the304B interfaces; frozen relative logarithms are cut off but equal the true logarithms on their clean inner plateau; tree coordinates are zero. This one signal reconstructs the actual fine field on every selected stencil. The affine square cannot be evaluated at an independent chart field or unrestricted z. Where a compulsory interface vanishes, the full component is zero.
3. **Selected rows avoid the core.** This is justified by active coordinates outside10B and selected stencils of radius≤B/50: a stencil touching such an active coordinate lies outside (10−2/50)B, hence outside2B. Merely saying its anchor is outside2B would not suffice.
4. **Orientation normalization once.** The global matrix D uses square roots of orientation probabilities. If X_Hsigma selects already weighted rows of D, applying Av_sigma a second time double counts those weights. Define within-orientation extracted squares with the sqrt weight stripped off and apply one Av_sigma, or sum the globally weighted squares without an extra average. Martin's displayed owner identity uses raw per-orientation rows and one average. Author notified.
5. **Ownership and exact row partition.** Martin `gaussian-reassembly.tex`115–117 explicitly uses disjoint halos of radius at least500B. Pairwise owner distance205B is not enough to make200B action sets or304B Haar sets disjoint. The harvested-energy file only assumes a separation-radius parameter R≥205B together with separate ownership hypotheses; it does not license interpreting that as sufficient point-distance separation. An explicit safe convention is to merge components whose500B halos meet, giving disjoint500B halos and pairwise seed-set distance>1000B. This preserves finite-range entropy estimates. Alternatively specify an exact disjoint ownership assignment and prove every annular/mask condition for it. Do not silently count a row twice.
6. **Different near sets.** Local determinant corrections use200B; Haar corrections use304B. Both belong to the unique500B halo. The global flat determinant scalar is extracted once and is not assigned to every component. Positive mean squares have the sign in `eq:reassembly-packet-log`; the component bound now uses that sign correctly.

## Other primitive and linear-comparison checks

- Exact series are correctly ordered: for E_s=A_s P_s−I, `A_s^-1=P_s(I+E_s)^-1`; with D=A Gamma−I, `Gamma^-1−A=[(I+D)^-1−I]A`. The nonsymmetric determinant identity is legitimate because A Gamma is similar to a positive matrix and the small logarithm series is convergent.
- Finite-range word counting is consistent with truncated A and finite-window Gamma/P; supports must include all windows and protected cutoffs. Endpoint cutoffs, not small operator norm alone, supply bounded pointwise quadratic factors.
- The local nonlinear-versus-linear mean discrepancy in Gaussian units is `g^-1 O(poly(B)t²)=x^-1/2+o(1)`, since t≈gM. Covariance discrepancy O(poly(B)t) has the same negative-power order. Polynomial Gaussian score moments therefore yield a local small comparison under the same law, on clean full windows. This is not a comparison of a seeded sector with an unrelated unseeded law.
- Holding physical fine links fixed avoids demanding a (k+1)st derivative from an incoming activity with only k derivatives. The text correctly warns against Taylor expanding its kth derivative at two different physical configurations.

This review checks the corrected local implications. Reconstruction of the exact block density still needs the stated compulsory masks and disjoint row assignment to be implemented, not merely assumed by terminology.

## Final integration check after the corrections

The current text now explicitly uses global smooth allocation weights before forming components. The products of theta and (1−theta) sum to one over all fine and mismatch selections; a nonzero weight forces the weak inequalities globally. Coarse flags are the actual set. Restricting these global allocation conditions to300B therefore supplies the required annular weak tests without deleting configurations or adding an unsupported hypothesis. Smoothness at the identity is harmless because theta is constant below a positive threshold, despite the chord norm itself not being differentiable at its zero.

The component definition now merges selected sets with intersecting closed500B halos, so the resulting200B action and304B Haar assignments are disjoint. Periodic wrap does not invalidate this rule: on a small enough torus there is simply at most one such owner. The enlarged adjacency remains fixed-range O(B), and its entropy and containing-site counts are still polynomial in B per selected test. No probabilistic independence is inferred from this geometric separation.

The selected-row clearance is explicitly derived from active coordinates outside10B and stencil radius≤B/50. The component square uses raw single-orientation D_sigma,b_sigma; the global precision stack uses sqrt(omega_sigma)D_sigma, and the final average applies omega_sigma exactly once. Thus the earlier normalization ambiguity is resolved. With these corrections, the displayed harvested energy implication establishes the claimed pointwise component amplitude on its compulsory protected interfaces; no unbounded positive extracted quadratic has been left unaccounted for. Zero interfaces make the whole component factor zero. The remaining reference to exact reconstruction is an assignment obligation in Chapter9, not an extra unexplained energy estimate.
