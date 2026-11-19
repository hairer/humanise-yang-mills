# Independent mathematical review of Chapter 17

Reviewed `chapters/17-trace-law.tex` (draft seen2026-11-19). No edits to author file.

## Correction applied

Root replaced the arity occurrences by fixed $N_*$ in both hypotheses and error displays.

In prescribed-radius comparison, n denotes the lattice level tending to infinity, but the powers `(alpha0-alpha1) D n+c` and `(alpha0-alpha2) D n-alpha0-c` must use FIXED arity, not that level. Fixed exponents cannot satisfy the first negative inequality for n→∞. Rename this occurrence to a fixed arity bound N_* (in hypotheses AND strip/grid error displays). Parent notified.

## Checked implications

- Stability lemma is sound under its stated hypotheses. Although convergence s_i→s is not initially assumed, the bases (t_i,k_i) converge to (t,v), with k_i=v_i−t_is_iv_i→v, and s_it_i=I,s_ik_i=0. This proves convergence/boundedness of s_i and the claimed uniformly bounded coordinate functional c_i. The error e_i rho(k_i) tends to zero from both assumed rates and bounded rho t_i.
- Trace cancellation uses the SAME lambda_i for all three tensors. f_i inverse remains bounded by independence of free divergences. Coefficients c_i can grow q_i, but error products vanish because q_i/e_i→0. Formula4c_D=lambda(beta KB_L)+c_Xlambda(KB_X)+c_D(lambda(KB_D)+4) has the correct signs. It gives c_D→−kappa/4.
- Amplification is handled correctly: with A_i=beta_i r_i^4 U_i^-1, beta_i r_i^4 U_i^-1 Z_i=beta_i A_iB_L+c_X A_iB_X+c_D A_iB_D. Faster-than-power trace cancellation on L/X suppresses the first two terms; D contributes−kappa O. Qualitative convergence alone would not suffice; the draft explicitly requests stronger rates.
- Conserved-line comparison/flux fixes nu_i→1. This uses centered conserved tensors, exact inclusion/symmetry transport, and same-family shell comparison; all should remain in the stated interface. The flux argument cannot be replaced by a bare subsequential free stress limit from an unrelated comparison map.
- Subtracting selected phase expectation costs beta_i r_i^4→0. Units must be preserved by U_i, as required.
- All-radius subsequence logic is valid: from EVERY prescribed null sequence a comparison subsequence is required. If the full limit failed, the violating null sequence would have no subsequence with the target limit. Monotonicity only of G(r), not of r8log²G, is used correctly; fixed t<1 and t>1 sandwich normalized target, then t→1.
- Free ordered-pair normalization yields2*24/16=3 per colour, consistent with O=1/4Σordered F².
- Regulator argument correctly avoids differentiating O(1). MVT for logmu over a FIXED interval requires uniform bounded remainder for that current/period family, and the Haar coefficient is independent of selected mu. With the stated uniform current-period limit on each compact regulator interval, then u→−∞ and interval length A→∞, the claim follows. Keep this order explicit.
- Finite mass-shell profiles have only nonnegative integer log powers at any finite asymptotic order; sufficient expansion before multiplication supplies the bounded remainder. The exclusion is appropriately restricted and does not assert absence of generalized free representations or a mass gap.

## Boundaries not discharged by this review

This is a review of finite-dimensional, spectral and limiting deductions, not verification of actual regulator/current transfer estimates. In particular same-family rho(Sigma_k), equation direction errors after backward matching/replication, exact forward-difference preservation, uniform all-radius marked windows and moving-label comparison are explicit additional inputs. Their qualitative counterparts do not imply the required rates. No new hidden algebraic gap identified beyond the arity/level notation collision above.
