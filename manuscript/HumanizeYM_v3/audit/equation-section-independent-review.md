# Independent review: microscopic equations and calibration

Reviewed `chapters/02-equation-section.tex` and `chapters/11-equation-calibration.tex`, with the ordinary/forced charge distinction checked against Martin `marked-field-local-estimates.tex`, `marked-portfolio-calibration.tex`, `actual-marked-portfolio-calibration.tex`, and `actual-equation-kernel-relay.tex`.

## Verified

- The avoiding-link curvature coordinates span the finite radial-jet dual: sampled curl is polynomial on the integer lattice; removing finitely many plaquettes does not affect polynomial uniqueness; radial closed polynomial potentials vanish by Euler's identity. Paths avoiding the distinguished link give exact link independence, not merely linearized independence.
- The force span only needs the top layer of its common kernel to solve Maxwell. It does not incorrectly identify the entire discrete-force kernel with continuum solution jets. Finite-dimensional annihilator duality gives the required one-layer equation functional.
- Curvature representatives for the remaining factors are chosen on the full jet space. Consequently force errors at equal factor count raise engineering weight; nonlinear errors raise factor count. The stated lexicographic triangular order and finite inverse are valid.
- Integration by parts freezes all links except the differentiated link. The transport, multiplicative factors, and bounded exterior spectator are independent of that link. Thus no derivative of the spectator is taken. Finite stencil and period-fit requirements prevent periodization from identifying that link with a nominally exterior one.
- Symmetry and real-structure averaging preserve exact nullity and both filtrations. One fixed section is selected before all derivative requests.
- The same-history endpoint follows from the last cone step and is independent of spectators. Finite symmetry averaging costs the stated orbit bound twice. The map acts on factor-normalized coefficients, so the equation space is correctly `Z P S_t R I`, not `Z P R I` or an unproved fixed Maxwell subspace.

## Resolved repair: ordinary terminal attachment cost

The initial calibration proof replaced the general trial charge containing `2|D| r` by `2 q_d` without displaying the additional estimate that permits this replacement. This is material because the block floor must be independent of the later coupling and global value norm.

Martin `marked-field-local-estimates.tex:139,162–186,375–387` supplies the sharper bound: in the remainder norm weighted by `sqrt(w_N)`, the attachment costs at most

`2 |D| sqrt(w_N) exp(81 sigma_N) Z_N^val`.

Impose `sqrt(w_N) Z_N^val <= 1` on the adjacent-stage coupling delay, together with the finite regional-mass/stencil conditions needed for the original attachment. Then coefficient plus remainder is bounded by the displayed `Q_dj`, while the unweighted reserved mass remains in `E_N`. These are different norms/costs; the large global-value term must not simply be omitted from both.

The payment is available before history selection: `Z_N^val <= A_d M_d beta_N^k` for a fixed degree, whereas `sqrt(w(beta)) beta^k -> 0` for every fixed k. At each stage take the finite maximum over degrees through that stage and its adjacent profiles. Martin lines13–65 give the elementary proof; `actual-marked-portfolio-calibration.tex:476–533` then separates Q (cone endpoint) from E (root error) explicitly. The author added the normalized attachment formula, the separate unweighted reserved mass, all three entry conditions, and the adjacent-stage threshold explanation. Independently reread these additions; the issue is resolved. No further obstruction found in this review.
