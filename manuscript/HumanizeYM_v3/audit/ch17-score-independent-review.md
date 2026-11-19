# Independent review: kernel score and marked trace rates

Reviewed the initial and revised `17-marked-trace-rates.tex` against the exact kernel in Chapter4, bounded pointwise-jet conditional estimate in Chapter6, and the marked graph/moment bounds in Chapter11.

## Checked portions

- q_gamma=Z_gamma^-1 exp(-gamma w), with u-independent normalization and smooth compact-group w, gives |D^r q_gamma|<=C_r(1+gamma)^r q_gamma. The original fine density and Borel frame eligibility tests are untouched by coarse differentiation.
- The exact identity div_V(FY)=integral (divY k + D_Vk[Y]) f is valid. It is a density-valued source; dividing by F does not show locality. Original fine spectator coefficients can be retained as f_A(U), since the V integral of div_V(Yk) vanishes pointwise in U. All generated joint modes must remain in its subsequent expansion.
- Absolute score bounds are suitable for failed-test contributions with retained exponential energy/Gaussian suppression; they do not preserve a small ordinary regular bound by themselves.
- Author added the necessary ordinary normalized-integral cancellation: include determinants, Jacobians, and V-dependent normalizations before differentiation; use the already differentiated smooth regular action norm. One extra derivative reserve is required. The dependence region must be the full rooted connected component, including any connected distant failures.
- Author added bounded coefficientwise covariant completion before truncation, rather than assuming uniform bounds for a growing-dimensional jet section. Controlled field jets through order four imply that cancelling the complete classical current identity leaves a fifth-field-order remainder with normalized cost beta t^5/t²=beta^-1/2 H³. This supplies the desired power gain for that particular remainder.

## Still requiring a precise supplier at this review checkpoint

Vanishing radial/engineering jets through degree five does not by itself increase field degree or supply another factor t. A bilinear term with sufficiently many spatial differences has zero such jet but is still O(t²) on arbitrary small-field links. Chapter11's screened polynomial-moment attenuation yields C_d/L+o_beta(1) for a general such remainder, not beta^-1/10. Consequently the low-field-order spatial remainder in the loop/Jacobian source cannot yet be assigned the displayed beta^-1/10 H^C bound solely by the quoted radial cancellation.

Possible resolutions need to be proved on the same actual source: exact low-moment preservation under its linear transfer; a controlled longer attenuation window with coefficient drift bounded; or a direct estimate identifying these low-field spatial terms as already multiplied by a negative coupling power. The ordinary score identity and the classical fifth-order estimate alone do not establish this last step.

This is a review checkpoint, not an assertion that the supplied manuscripts lack a repair. Parent and author were notified of the exact missing implication.

Potential refinement discussed with author: a bilinear fine scalar remainder R of total momentum order>=4, transported exactly as I(K0R), retains zero degree<=3 momentum jet. Principal/principal aliases preserve order; mixed aliases have transverse order2, the other Ward factor order1, and K0 order2; two nonprincipal aliases have order4 even when cancelling. Thus such a term could be retained in Sigma with rho=0 instead of falsely estimated as norm-small. The remaining source-match is essential: derivatives of the predictor/frame maps and stationary substitution, and internal Gaussian contractions in the kernel score, must first be separated from this exact bilinear transport. Averaging the original current anchor alone does not establish the required scalar-source decomposition.

## Stronger source supplier found and matched

The previous checkpoint's missing polynomial-response condition has a source-specific repair. `heading-history-handoff.tex`10–90 proves exact polynomial transport for degree<j. This is stronger than the O(p²) nonprincipal alias estimate previously used for the current defect.

The exact matching is:

- Chapter5 `actual-tangent` defines W_s to be its already constructed straight-average transport.
- Chapter5 defines m_l=w_L(theta_l)^j.
- Martin `kernel-transport-identities.tex`155–193 rewrites the nonprincipal one-form alias as A_l=B_l+diag(g_l)x_l sigma. Both B_l and g_l contain conjugate m_l, while the remaining factors are analytic at p=0 with nonzero denominators. Thus all derivatives below j of every nonprincipal alias vanish.
- `heading-history-handoff.tex`10–90 then proves (W_s p)(x)=sum_z A_0(z)p(x/L+z), so it is globally polynomial of no larger degree. It includes centered block carries and points outside the central block.
- Actual W_a=W_s−d_f E R W_s. Gauge invariance permits comparison of its exponential field to the gauge transform of exp(W_s v); the BCH discrepancy is O(poly(B)t²). In normalized field units this is O(poly(B)t), not a new uncontrolled alias error.
- `trace-row-jet-estimates.tex`161–278 gives screened multilinear jet comparison and the exponentially small crop tail. The polynomial-moment implication is already proved in Chapter11. These now match the actual response modulo the controlled gauge conversion.
- `trace-regular-atom.tex`274–379 performs actual principal integral → Gaussian reference → deterministic reference. `trace-local-rate-selection.tex`173–207 displays the complete response-plus-crop cost. Its dominant normalized fluctuation term is g/t=H^-1; other terms have a negative coupling power times fixed support polynomials. With B=O(log² beta), those polynomial factors are H^{o(1)}. Hence the relevant coefficient-probe error is H^-1+o(1), or H^-1+theta+o(1) for source norm H^theta, rather than the incorrectly asserted universal beta^-1/10 rate.

For the trace source, the already cancelled classical fifth-field-order contribution has negative coupling power. The remaining normalized loop/Jacobian spatial remainder has the fixed-order derivative cost bounded by H^theta times logarithmic factors; choose theta<1/6. Its screened-probe error is then o(H^-1/5), which is sufficient for the trace functional stability rate. One additional source derivative is required for the Gaussian/deterministic Taylor comparison. Large-field contributions still use the score bound and retained exponential suppression.

This route does not rely on proving that the full differentiated scalar source is an exact K0-averaged bilinear pullback. It applies the actual regular-insertion comparison with its stronger polynomial-preserving reference row. Author and parent received these exact source matches for integration; final approval is contingent on the fragment stating this corrected rate and its normalized source-cost premise explicitly.

## Final reread of integrated repair

The revised `ch17:spatial-moments` proposition now states and proves the actual H^-1/2 coefficient bound, with the alias formula, polynomial row identity, gauge correction, normalized conditional comparison, source bound N_k<=H^(theta_j+o(1)), and one extra derivative reserve explicit. The error formula retains this H^-1/2 contribution separately from the genuinely negative-coupling high-field remainder. This resolves the checkpoint's unsupported radial-vanishing implication.

The revised source proof also uses the exact pointwise-U zero integral with every incoming f_A, retaining all original fine spectator modes. Coarse smooth spectator truncation is a separate identity, and its distance at k(n) is specified as at least c exp(T_n), so the tail is negligible on the stated long comparison window. No quotient-by-density locality claim is used.

No further obstruction was found in the revised kernel-score, ordinary cancellation, coefficient-smallness and original-law spectator join. This is not an independent audit of the separate regulated Ward identity.
