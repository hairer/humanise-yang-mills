# Independent review of Chapters 5–6

Integration follow-up: the false continuity wording for the clip was corrected, and the explicit two-sided lift chain was added to Chapter 5 before the integrated build of 19 November 2026. Chapter 6 was subsequently strengthened by the actual predictor comparison; see `chapter-06.md` for that later verification.

Reviewed snapshot: `chapters/05-gaussian.tex` and `chapters/06-large-fields.tex`, 2026-11-19. Scope: new finite-history, transport, curvature-defect, scalar energy, window, common-majorant and correlated-tail arguments. No author chapter was edited. This is an independent algebra/scaling review, not a verification of every upstream selected-data supplier.

## Actionable correction

**Chapter6, line101:** “The clip is the continuous quadratic/linear function” is false for `ch04:clip`. The two branches are c_dir r²/2 for r<=t and c_lin tr for r>t, with16c_lin<c_dir; the downward jump is explicitly documented in Chapter4. Delete “continuous” (or replace it by “piecewise quadratic/linear”). The energy inequalities actually use the displayed discontinuous clip, so this correction does not require changing those inequalities. Keeping “continuous” would suggest a different action with different intermediate-range bounds.

No other definite mathematical error was found in the reviewed arguments.

## Chapter5 checks

### Finite histories and common analytic curvature metric

- Alias normalization L^-2 is consistent with counting scalar products: the averaging symbol contributes L, Fourier subsampling L^-4, and covariance volume ratio L^4.
- Accumulated filter formula `ch05:history-filter` has the correct prefix M_h at each smoothing-order drop. For two steps it reduces to w_(L1L2)^j2 times w_L1^(j0-j1) w_(L1L2)^(j1-j2), as required by direct composition.
- Noise introduced at h is propagated only through suffix h+1,...,n, with covariance prefactor D^-2. Sum over suffixes is geometric because ratios>=3. The principal h=n term equals1.
- Uniformity in final smoothing order rather than initial smoothing order is legitimate: extra box factors occur at geometrically increasing prefix sizes, and their principal logarithmic deviations sum like sum M_h/M_n, rather than multiplying a fixed lower bound an unbounded number of times.
- The reciprocal-bound argument avoids circularity. First bound G and the positive real F,A_mu,B_mu; obtain reciprocals by complex perturbation; then deduce the real lower bound for h from sum|q_mu|²/B_mu divided by lambda_M, and finally its complex reciprocal. The pole cancellation is exact. Uniformity here is boundedness, not convergence of histories, which the chapter states correctly.

### Transports and L factors

- Quotient identities R=D^-1−rho^-1D^-1xx*D^-1 and DR=I−x pi imply the four identities `ch05:transport-identities` when combined with F_(r+1,l)delta_r=d_r F_(r,l). In particular d1*(I−C)=0 and (I−C)H d1=0, so the complementary term is compatible with both intertwining equations.
- Restoring counting adjoints: a coarse-to-fine field reconstructed with L^-1 sum_l A_l has full fine Fourier coefficient L³ A_l times the coarse coefficient. The corresponding two-form map has coefficient L² T_l. Its adjoint therefore has coarse Fourier factor L^-2 sum_l T_l*, and d_f=delta/L gives L^-3 d_c sum_l F1,l, exactly d_c Q. The physical identities have no missing L power.
- A fine difference multiplies an alias by q(theta_l)=O(L^-1(1+|l|)); with Gamma(l)^-j, summation remains uniform for derivative order r<=j−2. Taking Fourier coefficients after the alias sum is important because individual columns need not be periodic. The text keeps the block-boundary phases.
- The principal cancellation formulas use s=lambda_(M_c), for which D0=L^-2 c_f(p/L) has the same denominator as D. This accounts for the otherwise easy-to-miss L² factor.

### Two-sided Koszul lift

The asserted two-sided factorization is valid, but its brief paragraph would benefit from the following four-line proof in the monograph (editorial recommendation, not a counterexample). I checked the construction against Martin `existence/curvature-horizon-producer.tex:81–101`:

1. Left lift d2*W=E. Then V=W d1 satisfies d2*V=0, so lift d3*T=V.
2. Since d3*T d0=V d0=0 and the top Koszul differential d3* on four-forms has trivial analytic kernel, T d0=0. Equivalently its next left lift would take values in zero five-form space.
3. Right lift X d1=T and set W'=W−d3*X. Then W'd1=0 and d2*W'=E.
4. Right lift C d2=W', then symmetrize C. This gives E=d2*C d2 with the same reduced-strip bounds.

All adjoints mean coefficient transposition with momentum reversal; it preserves exponential norms. The proof acts on infinite-lattice coefficients and only then periodizes, avoiding finite-torus zero-mode obstructions.

### Positive defect and residue count

- From TH_c d1,c=H_f d1,f W and T*d1,f=d1,c Q, the identity Z0 H_c d1,c=0 follows exactly using QW=I−b^-1 d1,c*H_c d1,c.
- The one-sided lift is applied separately to each fine residue. It does not sum over output residues. Thus fixed-residue T and B_fT bounds O(L^-2) give O(1) for their coarse Gram sum; one fine difference yields O(L^-3), and the Gram sum of lifted S is L^4 L^-6=O(L^-2).
- Modified inverses are Btilde=B+zeta B d2*d2 B. The identity d2 B Btilde^-1=(I+zeta d2 B d2*)^-1d2 gives precisely the D_c factors in `ch05:positive-defect`.
- C0+zeta_c I−zeta_f S*S>=I under zeta_c>=C0'+2 and L²>=zeta_f C1. Uniform boundedness of D_c^-1 transfers this to strict positivity on all three-forms. No projection onto a momentum-dependent subspace is used.
- Source-specific transport-column bounds are compressed in the exposition. Their explicit principal cancellation plus the earlier alias estimates make a credible route, but this review did not independently rederive every entry of the nonprincipal transport bound from original manuscript component formulas.

## Chapter6 checks

### Scalar energy implication

- Summing the six defined terms cancels every cross term and every transported square exactly. Localizing before cancellation correctly leaves E_L,E_D as signed terms.
- The coarse path term cancels in E_c because the relaxed test is an indicator: chi_rel²=chi_rel. This would fail if it were silently replaced by a smooth function between0 and1; the current Chapter4 definition is an indicator.
- The intermediate coarse range contributes c_dir,c t_c r/4. Since t_f<=2t_c and a<=c_dir,c/64, this is at least4a t_f² per plaquette, enough for at most four assigned coarse sites.
- Fine and mismatch energy reserves can support one a t_f² charge per test, the additional a t_f t_hi charge for D, and the signed linear excess after choosing L and then W large. The displayed bounds leave this slack.
- Remaining D-losses have ratio O(B^4 t_f/t_hi) to the reserved energy, tending to0. Small coarse losses have ratio O(B^4 t_c^4/t_f²), also tending to0. The final a/2 constant follows.
- These conclusions remain conditional on the explicit local signed comparison. The chapter does not incorrectly derive the actual nonabelian path comparison from the flat Fourier algebra.

### Actual Gaussian and windows

- A principal compression preserves the gap and weighted Schur bound, so the inverse column comparison is uniform. Its residual is zero inside the column window and exponentially small outside because the window contains a fixed multiple of B around the root. Row/column summation after reducing the exponent preserves the small factor.
- Symmetrizing P makes Gamma positive for large B by closeness to A^-1, not by symmetry alone.
- m=−P*f has residual A m+f=A(A^-1−P*)f, so the stated mean/forcing estimates have the correct orientation.
- In the exact change u=m+g z, the scalar is (2pi g²)^(n/2)(det Gamma)^(1/2)exp(−beta Q(m)); the linear residual is −g^-1(A m+f); the quadratic residual is (Gamma^-1−A)/2. Signs and powers agree.
- The Gaussian used is conditional on frozen Haar variables. The derivative density uses the inverse of the marginal covariance block, not a block of the full precision. Those distinctions are correct.

### Correlated tails and common majorant

- For a distinct witness set J, summing sign choices and using exponential Markov at parameter1 gives2^|J| exp((M/2−T)|J|). Since r/Q<=|J|<=r, T>=M/2+HQ gives2^r exp(−Hr). The N^r witness assignments produce(2N exp(−H))^r. No independence is used or needed.
- T proportional to exp((log log beta)^2) dominates Q H when Q is polynomial in B and H=O(log beta)+O(log N), at fixed L. Thus beta^(-2tau r) is available for distinct addresses. Repetitions are rightly counted once.
- For the doubled majorant, the covariance tilt is2K. The bound||Gamma^(1/2)K Gamma^(1/2)||<=1/8 leaves norm<=1/4 and bounds the inverse tilt. The determinant logarithm and linear shift cost O(tr Ktilde+|Gamma^(1/2)eta|²), hence exp(C sum lambda_i).
- Cauchy–Schwarz then takes the square root of beta^(-2tau r), yielding exactly beta^(-tau r). Polynomial moments under the tilted laws are explicit assumptions; they are not inferred from separate factor estimates. The common quadratic bound applies to the sum of all corrections, which is essential.
- Per-selected-test energy beta t_f² is comparable to (M_f^cut)². Both stated loss classes are little-o of it: logarithmic polynomials are dominated by exp(2(log log beta)^2), while the cubic-action loss ratio is B^d t_f→0. No unexplained global volume normalization is absorbed.

## Overall conclusion

The reviewed algebraic implications and scale factors are consistent. Correct the false continuity statement. For self-contained exposition, expand the two-sided lift by the short chain above. The source-specific sector gap, common coordinate change, mask-vanishing, and aggregate quadratic bound remain explicit hypotheses, as they should; this review does not close those model-specific interfaces.
