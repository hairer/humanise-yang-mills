# Independent review: retained stationary integral and centered change

Reviewed `chapters/09-stationary-remainder.tex` as supplied by root; no Chapter9 edits made.

## Confirmed

- The scalar identity is exact. With gamma0=N(0,A(0)^-1), the exponent s(x)-s(0) converts the reference Gaussian determinant to det A(x)^(1/2). Thus `Omega exp(-Phi(x)) R(g,x)` has precisely the original Haar/chart Jacobian and g^n multiplier. No determinant or extra tag count is missing.
- `R(0,x)` is the actual truncated N(0,A(x)^-1) mass. The symmetric Euclidean ball gives exact evenness in g. The g² gain, after retaining the superpolynomially small mass error, is valid. Polynomially many coordinates and D=d0 M are compatible with the tail estimate because M outruns every power of log z.
- Fixed-order derivative costs are subpower on the parameter ball h=z^-7/16, including derivatives of rho and the moving Hessian. Higher derivative orders must be selected with the stated reserve. The finite-difference interpolation step can use steps smaller than the radius-z^-1 microscopic ball, so arbitrary inverse powers are available from a superpolynomial value error.
- The direct fine-cutoff proof does not need an empty-sector lower bound. For the explicit coordinate-fold pullback pi_w, coordinate loops retrace and have identity holonomy. An axial gauge on the original cube, pulled back, gives the required polynomial-in-side coarse link bound. This would be false for an arbitrary small-curvature torus with torons, but the text correctly restricts the argument to folded fields and their microscopic neighborhoods.
- The operator `H_f^-1 T H_c` uses the fine-output ROW norm of T, which is O_j(L^-2); its large opposite column norm is irrelevant here. The two H factors have fixed-stage convolution Schur bounds. The actual corrected transport has the same curl as the straight transport. Consequently the leading fine curvature bound is C_j L^-2 t_c, with constant fixed before L; nonlinear coordinate/stationary/plaquette errors are P_j,L(B)t_c² and can be made small after L. The gD displacement is O(d0 t_f) uniformly in the actual coupling band. The z^-1 microscopic perturbation is negligible. The strict cutoff margin is valid.
- Geometric chart recognition can use the actual tree inequality from Chapter5, uniformly over live tags. On the convex safe coordinate ball the Hessian gap yields the exponent loss Delta=gamma D²/4; outside it, a healthy field has a mismatch bounded below by fixed delta. Since beta delta² dominates both beta phi_stat=o(beta) and M², the exterior estimate is consistent. The polynomial-in-log normalization loss is o(M²).
- Centering the final logarithm gives the stated three powers: beta^-1 h=z^-23/16, beta h^5=z^-19/16, h³=z^-21/16. The largest is -19/16, strictly below -23/20. The first derivative cancellation is properly applied to the full corrected logarithm, not assumed for each determinant contribution.

## Corrections sent to root

1. Define the pure integrand explicitly with the indicator that all fine plaquettes obey the fine cutoff. Merely saying 'incoming activities omitted' is insufficient: the exterior proof bounds negative path/loop contributions on healthy fields only. Martin `stationary-exterior-receipt.tex`, `eq:exterior-tag-integrand`, includes this indicator. The prescribed path and kernel otherwise remain unchanged.
2. The physical stationary field in the forest chart has tangent W_F, not W_a. Its **curvature** tangent agrees with d_f W_a. Replace that sentence; the subsequent estimate remains valid.
3. Replace the literal comma before dgamma in the R integral by normal differential spacing.
4. Remove the stale attribution of the direct exterior argument to an 'unrefined sector expansion'. The written proof uses actual chart recognition, the Hessian gap and direct cutoff verification, not that expansion.

## Centered scalar change in Chapter7

Independently checked `r=r_root-Ru` and its gauge law in `07-matching.tex` around the centered quotient estimate. With Chapter5's exact frame derivative H and R=-sum w H, the centered frame derivative is H+R. Hence `r_root+H = (r_root-R)+(H+R)` and `Q u-d_c r_root = M u-d_c(r_root-Ru)`. Also `R d_f phi=phi at roots-sum w phi`, so the centered scalar transforms by the smoothed scalar mean. In unitary block Fourier coordinates that mean has coefficient mu² m_l, whose principal real alias is bounded below after dividing by mu². The internal linear triangular coordinate change has determinant one. These signs and normalizations agree with the actual predictor, and were confirmed to the Chapter7 author.

No independent verification of all subsequent ratio-uniform weighted nonlinear vertex estimates is claimed by this short review.
