# Independent review: spatial remainder coefficient

Reviewed the revised `ch17:spatial-moments` proof, focusing on the previously unproved low-field-order/high-spatial-order remainder. This is a focused check of this supplier, not a new certification of the full monograph.

## Corrections requested and incorporated

1. Vanishing deterministic moments are restricted to polarized polynomial-link tuples with summed engineering weight at most five. Vanishing on all polynomial fields below the smoothing order would be false. Chapter11's screened-moment statement gives exactly the restricted assertion, and the straight response preserves or lowers every polynomial degree.
2. The nonprincipal alias formula now defines its pole-cancelled factors. From F1_l^* x = bar(m_l) diag(|r_L|^2) x_l and pi=s^{-1}sigma, direct substitution gives the stated g_l expression. The denominators s alpha and B_a are regular and nonzero; D_l is regular at a nonprincipal alias. Both resulting summands contain bar(m_l), so their derivatives below smoothing order vanish. There is no silently discarded coarse pole.
3. The gauge comparison uses an invariant color-scalar, spacetime-vector source, rather than equivariance alone. Haar divergence of equivariant Y is invariant, as are action and loop variations. The actual tangent correction is a gradient; applying its gauge transformation leaves source evaluation invariant, with only the controlled nonlinear BCH error in exponential coordinates.
4. N_k explicitly bounds the already t^{-2}-normalized source and its normalized-link derivatives. The source starts at field order two after invariant projection and cancellation of the classical part, so no further inverse threshold factor is introduced.

## Rate check

With g=beta^{-1/2}, t=beta_hat^{-1/2} H and the actual coupling band, g/t <= C H^{-1}. Polynomial support/crop losses are H^{o(1)}. The stationary and BCH coordinate errors divided by t are polynomial(B)t, which is smaller than every fixed inverse power of H. Hence the one-extra-derivative estimate has size H^{-1+theta_j+o(1)}, sufficient for H^{-1/2}. This also suffices for the later H^{1/5} rho-error multiplier, while the coefficient norm allowance H^{1/6} remains below that multiplier.

The Gaussian comparison should be read as subtracting the deterministic (zero) reading inside the same actual conditional expectation and estimating the evaluation difference with its joint polynomial moment bound. I requested this clarification: no O(t) total-variation comparison of nonlinear and Gaussian densities is needed or justified by the coordinate argument alone. In particular the density's possible beta t^3 scale must not be confused with the source evaluation's g/t gain.

No remaining concrete obstruction was identified in this restricted coefficient argument after the above corrections. The full zero-exterior-moment source and all its higher marked modes must still be retained in subsequent descent, as the text explicitly does; the projected coefficient by itself is not a zero-moment insertion.
