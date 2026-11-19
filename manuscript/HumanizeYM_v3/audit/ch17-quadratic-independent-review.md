# Independent review of the quadratic current contraction

Reviewed `17-current-contraction.tex` against Chapter5 actual transport identities and Chapter7 curl division, plus the exact Laurent-polynomial kernels in `17-trace-transfer.tex`.

The stated quadratic argument is internally consistent:

1. The actual smooth stationary representative satisfies K_f W_a=Q* K_c. At a nonprincipal alias k_l(0)≠0, its transverse component is analytic and O(p²), since K_c=O(p²). The forest-gauge correction is killed by each Ward identity. Individual inverses need not be uniform in L for this exact order statement.
2. The anchor average K0 has factors M_a² G_a(s_a^L), so has a double zero whenever the total alias is nonprincipal. The principal/principal, mixed, and nonprincipal/nonprincipal cases give total momentum order at least four; the final case covers cancelling alias indices.
3. The independent two-leg Ward identities allow bounded curl division at a strict width reserve. The resulting coefficient has Taylor order two and factors two further differences. Difference allocations are (1,3), (2,2), or (3,1).
4. The actual W_a derivative bound L^(-1-r) gives L^-6 for the two differentiated legs. K0 has bounded absolute mass, so there is no extra volume L^4. The current normalization L^5 gives the homogeneous C_j/L estimate.
5. The leading continuum quadratic identity has the displayed sign and uses the linear Bianchi identity. Thus the initial order-four cancellation follows for the stated normalized leading action/current pair.

Scope retained: this proves the exact pulled-back quadratic defect channel. It does not establish higher stationary jets, nor permit an additive action-matching error to replace equality of the quadratic pullback. The draft explicitly preserves these limitations. No correction requested.

## Follow-up: full triangular contraction and current bounds

Reviewed the subsequently added sections against Chapter7's actual completed inverse and Scott/part2/I-section.tex 150–180, 329–345.

- The forest-slice inverse Π_F C^-1 Π_F* is valid: Π_F* extends a slice covector to annihilate gauge directions, the completed inverse solves the Hessian modulo gauge, and Π_F selects its slice representative. The finite block-tree projections have bounded coarse range; their L-dependent norm does not shrink the common spatial Fourier strip.
- The z2,z3 implicit derivative equations include the three D3S[z2,T] terms. Fixed-L bounds on these jets suffice. The radial gauge is applied to the complete invariant function: raw higher field jets are not incorrectly assumed to satisfy homogeneous Ward identities. Its nonlinear derivatives multiply strictly lower field-order inputs.
- Diagonal orders (2,3,4) are C/L,C/L,C/L^3; every off-diagonal coefficient C_(j,L,r,s) is multiplied by (log β_f)^s/(log β_c)^r for s<r. Ratio first, entry second makes all row sums small without a claim of pre-ratio nonlinear jet bounds.
- Requested explicit definitions of R_f,R_0 and the Y transfer. Author added them. The source plus sign is correct: R_f|0=M+d0R and d_V|0=−d0, while R_0|0=R, hence the corrected differential is exactly M. There is no rough root-gradient term in the diagonal Y channel.
- Requested the output-link convolution estimate. Author added K0 infinity norm O(L^-4), M row mass O(L), yielding O(L^-3) for the full local displacement norm, with exponentially weighted coefficient tails. The linear remainder's extra output-index difference moves onto M and uses its finite-difference row sum O(1); an extra field difference uses the smooth tangent. Both supply the claimed L^-1 gain.
- The exact column sum L^-3 follows from the box-filter alias cancellation and row mass L. Together with the tangent curvature factor L^-2 and normalization L^5 it preserves the leading covariant curvature displacement. The stress weight-four quadratic jet is likewise preserved. Covariance fixes the associated commutator term.
- Primitive old terms contract; equal-order J forcing is one-way and bounded before L, so a smaller fixed primitive weight absorbs it. Remaining fixed-L reference forcing is suppressed by logarithmic normalization. Matching through order four introduces no defect source because Y'(0)=0.

With these explicit definitions and convolution details, no further correction was found in the new full current contraction argument. This review does not cover the later scalar regulated Ward identity or its marked finite-coefficient transfer; those are separate arguments.
