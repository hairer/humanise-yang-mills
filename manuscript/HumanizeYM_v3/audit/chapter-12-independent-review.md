# Independent review of Chapter12

Reviewed the fixed-level graph, scalar normalization, stopping argument and smooth passage against Martin `existence/fixed-rung-convergence.tex`, `fullmesh-correlation-cauchy.tex` and `smooth-limits.tex`.

## Required clarification

The graph-contraction lemma uses the bound `||Phi H|| <= s_m` in its proof. State explicitly that the marked step maps admissible graphs to admissible graphs. The displayed difference bounds and inverse bound by themselves do not imply this. This is the existing admissibility supplier, not a new convergence estimate.

## Checks passed

- The graph includes both ordinary and forced singleton remainder data and uses common fixed dictionaries. No quotient by equality of evaluated functions is used. Terminal forgetting is valid only together with the explicitly stated fixed-input cutoff continuity; the chapter keeps that distinction.
- The scalar is the extensive scalar, stripped from numerator and denominator identically. Uniform positivity of the stripped partition function follows by restricting the positive full density to the fixed small-link ball. Positivity of each separate partition function alone would not suffice; the text supplies the uniform lower bound.
- The stopped density retains full singleton data, including forced singletons, and removes only higher marked terms. The fixed-base constant uses coefficient bounds and positive weights at one fixed base level, so it does not depend on the stopping level. The stronger separated support estimate pays per-marker weight changes. The disk argument gives the stated factor 2 exp(-B_m/64).
- The fixed-level convergence plus the stopping bound proves full cutoff Cauchy convergence, with the order of choices stopping level first, cutoff second. It does not falsely infer convergence of a sequence of changing maps merely from contraction of each map.
- The discrete smoothness proof uses uniform bounds on every finite difference order on enlarged separated compacts, identifies derivative limits by secants and discrete Taylor expansion, and allows equal coordinate projections. The physical Riemann sum normalization a_N^(4n) is correct.

## Scope

This review validates the stated conditional ultraviolet passage. Production of fixed-level background convergence and marked fixed-input cutoff continuity for the selected history is still a separate interface. Uniform finite-history Gaussian bounds alone do not supply those convergence inputs. The review does not certify coincident-point extensions or reconstruction.

## Resolution

The graph-contraction lemma now explicitly assumes that the marked step maps admissible graphs into admissible graphs. The sole requested local clarification is resolved.
