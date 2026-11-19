# Chapter18: operator products and contact extensions

## Draft and mathematical scope

`chapters/18-operator-products.tex` supplies a compatible finite-degree probe prescription, symmetric graded coefficients, the exact same-history marked replacement obligation, and its conditional phase-uniform finite-order OPE consequence. It separately proves a concrete finite-order distribution extension for every collision pattern directly from the already established phase-uniform polynomial separated bounds. It does not assert infinite truncation convergence, coincident-point lattice limits, contact positivity, or contact Ward identities.

## Source map

- Compatible probes and finite-dimensional splittings: Martin `ope-prescription.tex`, `ope-homogeneous.tex`; Scott J definitions D31--D33 and lemma J1.1. The old probes remain the same finite correlation combinations when new quotient degrees are added. Rotation/reality averaging is followed by the graded recursion built from those averaged readouts.
- Marked input: Scott J `lem:J-signed-local`, `lem:J-graded-quotient`, `lem:J-marked-costs`, `lem:J-lattice`, `lem:J-power-separated`; Martin `ope-filtration.tex`, `ope-grouping.tex`, `ope-cutoff.tex`, `ope-estimates.tex` input `ope-raw-estimates`, and `ope-phase-prices.tex`.
- OPE consequence: Martin `ope-estimates.tex` averaged-readout comparison and finite-truncation theorem. The error measured by a probe is obtained by rotating the whole correlation, not only the cluster's labels. Compactness of O(4) gives a common clearance and uniform bounds for the finite probe list.
- Contact comparison: Scott J D36--D38 and contact recursion. The source uses degree-dependent normal orders L_h-1-q, with L_h=max(0,d_h+1-4(|h|-1)), and nested parent Taylor operators act before child operators. Its sharper order (W+2)n depends on a complete signed multiscale estimate, not just the single-shell power count.

## Explicit remaining OPE obligation

Assumption `ch18:replacement-input` retains both raw coefficient bounds and all-copy signed replacement moments on the same selected history. The power constants and radius threshold must precede the copy count; cutoff thresholds can depend on a fixed count. The full higher marked family, original inventories/masks, physical inclusion maps and common coefficient readout must be retained. A mean error or ordinary one-insertion contraction alone does not imply this assumption. The graded quotient estimate is stated with the correct a_m^(-(t-i)) and subpower factor. UV author has been asked for exact suppliers; none is silently imported as proved.

## Conservative contact prescription: fully checked

Instead of claiming the source's sharper forest order without its signed multiscale supplier, the chapter fixes an elementary conservative normal Taylor prescription.

For n>=2, m=n(n-1)/2 and delta=min pair distance, define rho=(sum pair-distance^-2)^-1/2, so delta/sqrt(m)<=rho<=delta. Smooth nonnegative pair weights sum to one and select only pairs with distance<=4sqrt(m)rho. For each selected pair use its orthogonal centroid projection pi_h and normal displacement z_h. Subtract the weighted normal Taylor jets through order k with one cutoff chi(rho/s), where k+1>P and P is the common separated growth exponent. Near the collision set, the remainder is bounded by C rho^(k+1)||f||_(C^(k+1)); multiplying by the kernel bound gives rho^(k+1-P), bounded and locally integrable. This handles arbitrary simultaneous collision rates because selected pairs are always comparable to the minimum separation.

A subtracted term can be nonzero only when pi_hx lies in the test support and |z_h|<=C_n s; hence every integral lies in a fixed compact enlargement. The formula is linear, has distribution order at most k+1, and agrees with separated tests because every jet on a pair diagonal then vanishes. The same dominated bound proves phase continuity and barycenter compatibility. Its choices are translation/rotation/permutation invariant. A single common k is fixed on each bounded degree menu before extending multilinearly in labels. No compatibility across independently changed degree-menu subtraction orders is claimed.

This changes the contact prescription and gives a weaker order than the sharp source formula. It is an explicitly documented alternative, not an assertion that the two distributions agree. Their difference is supported on the union of diagonals. This conservative contact theorem requires no OPE input and closes finite-order extension existence even while the marked replacement estimate remains open.

## Literature checked before drafting

- Wilson, *Non-Lagrangian Models of Current Algebra*, Physical Review179 (1969),1499--1512, DOI10.1103/PhysRev.179.1499: publisher record verified. Used only for the original OPE context.
- Fröb--Holland, arXiv1603.08012, submitted2016, revised2021: author arXiv abstract checked. Its all-order existence statement is perturbative and is described as such, never used as a substitute for the nonperturbative input.
- Brunetti--Fredenhagen, CMP208 (2000),623--661, DOI10.1007/s002200050004, arXiv math-ph/9903028: original full PDF examined at Section5.2, Theorems5.2 and5.3, printed pp23--25 (PDF indices22--24), especially formula38 and the Taylor-jet subtraction. The draft cites the standard extension mechanism and proves only the elementary multiple-diagonal choice above. It does not attribute the particular pair-weighted formula or an optimal scaling-degree statement to that paper.

Bibliography entries are in `audit/ope-bibliography.bib`, using the existing Scott keys Wilson1969, FrobHolland2016 and BrunettiFredenhagen2000. No global bibliography edited.

## Validation

Checked label uniqueness and theorem/proof/equation environment balance. No global build run; parent owns compilation and integration. Suggested independent check: the contact extension is deliberately an integral of the complete Taylor remainder, never separately integrals of its divergent summands.

## Local replacement integrated before Ward identities

The graded quotient and exact grouped lattice estimate now appear at the end of Chapter13, including their mixed spectator consequence. The source filenames retain prefix18 for continuity. Chapter18's former replacement assumption is now a proposition, with proof in `18-raw-replacement.tex`: arbitrary replicated chessboard bounds pass to compression-algebra norm using the moment formula, before phase characters are evaluated. Its OPE remains dependent on the earlier phase construction, but no longer introduces an independent cluster-replacement assumption. See `chapter-18-lattice-products.md` for the numerical weight inequalities and checks. The conservative contact extension and its limitations are unchanged.
