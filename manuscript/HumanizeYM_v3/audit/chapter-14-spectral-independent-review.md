# Independent review: coordinate spectral and angular-flux argument

Reviewed Chapter 14 coordinate measures, mixed-sign transfer, symmetric contact normalization, diagonal response chain and anisotropic flux against Martin `physical-ward-packet-prices.tex`, `physical-ward-stress-cone.tex`, and `physical-ward-propagation.tex`. Also checked the new mixed replacement application to the annulus.

## Verified

- Undamping is independent of placement; only finite-energy mass and sufficiently damped moments are used. Moment bounds follow from positive difference multipliers and further heat damping. Word offsets require the stated hyperplane restrictions, except in the separately handled line-time case.
- The Lagrange annular correction reproduces the moments through order 2m−1. Its rational response identity and low-energy lower bound have the correct signs and retain E=0.
- The two-residual sign-transfer identity discards a nonnegative response with a minus sign. Corrections are majorized only as transverse profiles. The backward induction visits and removes all shrinking axes; its choice of next width, transverse moment, energy moment exponent and final subtraction order is consistent.
- The product Taylor extension is integrable and preserves signed tensor symmetries. The contact constant q has the correct divergence sign. Reflection parity and the paired index patterns give within-pair/pair-exchange symmetry. After subtraction the divergence contact polynomial starts at degree3.
- Conservation gives Q1=p_mu²Q0+D1 and Q2=p_mu²Q1+D2 with defect degrees4 and6. The normalized width identities give d0=A−B,d1=A−4B,d2=A−16B up to the stated errors, hence 4d0=5d1−d2. Corrected Laplace signs are +,−,+.
- Angular test fields equal the required rotation near the insertions; the two off-diagonal columns cancel exactly. The four final exponents are negative and agree with the source after the lambda^100 prefactor. The diagonal low-energy region includes E=0, whose mass cannot be bounded using the vanishing E-weighted diagonal estimate.
- Chapter 13 mixed replacement gives the annular rate rho^(1−epsilon), with the same correction for every spectator and no phase input. Its power uses W=d+4 and D=d+1−kappa exactly.

## Repairs applied with parent authorization

1. Extended the residual *upper* moment estimate to all widths whose support lies inside the correction radius, including growing widths. Kept the low-energy *lower* bound in its narrower regime. Stated that the energy moment exponent is chosen before the subtraction order.
2. Proved positivity of the signed dyadic corrected profile by monotonicity of its positive rational kernel below the radius8 correction nodes. Positivity for a nonnegative original profile alone would not justify this signed difference. Included the resolvent-difference lower bound.
3. Constructed the line-axis temporal gap with c=sigma0*sigma0 and nonnegative Fourier transform, a fixed time cutoff covering offsets, its uniformly bounded correction, and the positive residual floor. Added the two-term sign-transfer/moment argument. Merely removing an interval from an arbitrary Fourier profile would not ensure positivity.
4. Restricted the ordinary mixed-sign stress bound to mu!=b. The diagonal component uses its separate weighted estimate, as the subsequent table already did.

No further concrete error found in this packet. No global compilation performed; parent controls integration and rendering.
