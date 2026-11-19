# Chapter 16: relativistic reconstruction

File: `chapters/16-reconstruction.tex`. Standalone compile: 8 pages, no overfull/underfull boxes, 2026-11-19. Global bibliography/build/render left to parent.

## Exact hypotheses retained

The chapter assumes the actual separated phase correlations, uniform phase slab bounds, common label/null-space identification, full-support phase measure, orthogonal covariance, and normalized stress/annular identities from Chapters14–15. These conclusions retain their Chapter11 marked lattice/calibration and Chapter14 common-grid/annular analytic prerequisites. Chapter16 proves the reconstruction from that interface, and does NOT claim to close those upstream microscopic suppliers.

No collision extension of the Euclidean hierarchy is postulated. No analyticity is inferred from mere continuity: heat spectral calculus and polynomial slab bounds supply it. No uniform bound in arity is asserted or required. No mass gap follows from the low-energy estimate.

## Checked proof units and sources

- Centered slabs, width independence, polynomial time-gap bound: Scott `part2/H-section.tex`187–217; Martin `existence/complex-heat.tex` and `analytic-boundary.tex`1–120. Only spatial strong continuity needed.
- Joint boundary, arbitrary independent height ratios, common Schwartz seminorm and phase continuity/barycenter: Martin `analytic-boundary.tex`121–231; ScottH218–238. Exact backwards Taylor formula has integrand bounded by cancellation of s^m against gap s^-m; all weakly ordered heights allowed.
- Lorentz covariance, exponential compact-frequency test identity, suffix spectral cones: Martin `fourier-support.tex`1–142; ScottH224–242. Coordinate Fourier pairing is Euclidean; momentum transforms by inverse transpose, still preserves forward cone.
- Full spacetime tube and closed-cone partial boundaries: Martin `full-tube.tex`1–274. Smooth cutoff equals one near support; distance-three neighborhood gives bounded exponential multiplier on closed imaginary cone. Bare exponential off support is not used as a Schwartz multiplier.
- Adjacent locality: Martin `locality.tex`1–239; ScottH243–274. Small imaginary boosts produce both germs, Euclidean smoothness at the spatially separated tie identifies all jets on a totally real slice, finite chain of germs reaches arbitrary real times. Tied-height partial boundaries are taken only after germ identity.
- Word fields: Martin `reconstruction.tex`1–224; ScottH275–291. Standard Wightman quotient is cited, only domain/null invariance check retained. Independent Gram limits yield positive form and actual vectors, not just scalar limits.
- Onto OS comparison: ScottH282–291. Compact-frequency damping identifies positive-height vectors with images; closed-range density supplies surjectivity before vacuum transfer.
- Low energy and every-character vacuum: Martin `phase-selection.tex` low-energy/vacuum portions; ScottH293–337. Full zero-energy projection Q is retained until uniform heat decay+phase continuity+full support prove Q=vacuum projection everywhere. Odd time average gives SUM of two positive measures. Momentum bump volume u^3 divided by energy u gives u². Compact word density checked.
- Weak commutant: ScottH339–350. Pasting upper/lower half-plane heat functions uses bounded B without assuming domain invariance.
- Stress continuation and local charges: ScottH352–365. Derivative conversion and zeta factors recorded; spacelike support of cutoff derivative is essential to bounded holomorphic jump continuation. This assertion retains the upstream normalized shell identity, not just conservation.

## Stable exports

`ch16:boundary`, `ch16:cone-support`, `ch16:locality`, `ch16:fields` (faithful fields, joint spectrum, onto heat-intertwining OS comparison), `ch16:vacuum` with `ch16:low-energy` and `ch16:heat-decay`, `ch16:irreducible`, `ch16:charge-law`.

## Original literature

Wightman, Physical Review101(1956),860–866, DOI10.1103/PhysRev.101.860, original APS publisher record checked2026-11-19. New sidecar `blueprint/ch16-bibliography.bib`, keyWightman1956. The standard word construction is attributed rather than presented as a new source result. Existing OS1973/OS1975 entries retained; original OS1975 ProjectEuclid paper checked again. Their abstract reconstruction theorem is not invoked without its hypotheses: actual slab-based boundary construction is given here. The source-specific uniform every-phase conclusion and local stress jump argument remain explicitly proved adaptations of the supplied manuscripts.

## Limits

No separate global PDF build, bibliography mutation, or rendered-page review was performed by this agent. Parent handles integration. No additional missing mathematical input identified within the Chapter16 reconstruction once its stated14/15 inputs hold. The substantive upstream unclosed conditions remain visible rather than being hidden inside an OS citation.
