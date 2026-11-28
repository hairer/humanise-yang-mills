# `M_core`, `M_act`, rooted and centered coordinates (7:521–565)

Report of a read-only agent, 25 November 2026, as handed back (condensed; nothing in the text was changed). Issue 1 of the fork, item 28. Worktree at `d5e3deda`. "Martin" = `manuscript/existence/`, "Scott" = `manuscript/HumanizeYM_v2/part2/`, Lean paths under `Lean/`.

## Result

`M_act` is the full gauge-completed Hessian of path action plus penalty term in the fluctuation coordinates. `M_core` is the same matrix with the penalty Hessian replaced by its pullback through the derivative of the averaging operation. "Rooted" and "centered" are two normalizations of the per-block local gauge transformation. Both matrices act on the full joint fluctuation space (fine field and one local gauge transformation per block) and are completed by `F*F`. They are not matrices of the block axial gauge, and no source assumes a translated reference tree for this calculation.

## Definitions, with what was read

**Joint space.** Martin `stationary-determinant-prices.tex:161–163` ("Let `b` project the joint space onto its fine one-form part, and let `e` project it onto its coarse scalar part"); Scott `B-section.tex:553–556`; Lean `YM.Stationary.Joint := Config G f × Coats G c` (`YM/Next/STATIONARY/Joint/Chart.lean:229`, definition read), `YM.Stationary.shield` (`:336`, definition read).

**Rooted coordinates.** The block coordinate is the local gauge transformation at the block root, extended over the block by the minimizing transformation normalized there (`h_o = 1`). Martin `predictor-branch.tex:169–170, 214–223, 270`; `selected-stationary-linear-data.tex:88–89`. Scott `B-section.tex:553, 625`. Lean `YM.Stationary.enroll` (`Chart.lean:367`, definition read; comment "to rooted"), `YM.Stationary.fedora` (`Regulator.lean:379`). In v3 the normalization is at 4:43, 58, 87 and 5:997; the rooted scalar coordinate `r_root` at 7:693–696.

**Centered coordinates.** The block coordinate is multiplied by the nearest group element to the weighted mean (weights: the smoothing probability) of the block's transformations. Martin `weighted-frame-penalty.tex:95–98, 125–128`. Scott `B-section.tex:645` ("Its tangent is triangular with identity diagonal, so it preserves determinants"). Lean `YM.Stationary.prospect` (`Chart.lean:364`), `bears` (`:365`), `recruit` (`:368`, "to centered"), all definitions read. The change of coordinates: Martin `selected-stationary-linear-data.tex:119–126`; Lean `YM.Stationary.shear` (`Regulator.lean:413`, definition read), `shear_det` (`:457`, statement read). Full Hessians transform by congruence only on the critical configuration, the core matrix also off it: Martin `thermal-contact-cancellation.tex:117–121`; Lean `abides` (`Completion.lean:79`), `fields` (`:96`), statements read. In v3: 7:642–658, 688–700; the triangular change at 7:674–676, 699–700.

**`M_act`.** Martin `stationary-determinant-prices.tex:172`: "`M_act = b*Kb + B + F*F`", `K` the fine kinetic Hessian, `B` "the actual penalty Hessian" (`:83`), `F = X + T` the gauge-fixing map (`:166`). Scott `B-section.tex:629`: `C_μ = J + F_μ*F_μ`. Lean `YM.Stationary.medals` (`YM/Next/STATIONARY/Joint/Completion.lean:59`, definition read).

**`M_core`.** Martin `stationary-determinant-prices.tex:173`: "`M_core = b*Kb + Q*HQ + F*F`", `Q(U)` "the block constraint derivative", `H(U)` "its coarse penalty form" (`:81–82`); `thermal-contact-cancellation.tex:130`: "Write `A(x) = M_core(x)` in rooted coordinates". Scott `B-section.tex:633`: "`C^rem_μ` for `C_μ` with the contact term of (B-contact) removed". Lean `YM.Stationary.legion` (`Completion.lean:61`, definition read).

**The identity `M_act = A + Z`.** Lean `YM.Stationary.Teller.contact` (`Completion.lean:116`, statement and proof read); Martin `thermal-contact-cancellation.tex:136–138`; Scott `B-section.tex:618–623`. The calculation (ch07:contact-exact): Lean `YM.Stationary.lean_drift` (`Joint/Drift.lean:498`, statement read); `Y` is `rind` (`:102`, definition read); the Ward identity `DY(0) d_{0,c} = 0` is `guard_y` (`:265`, statement read, proof skimmed).

## Is the block axial gauge needed?

From the sources: no, for the matrices. The forest enters in three places only: the construction of the critical configuration (Martin `selected-stationary-linear-data.tex:45–96`); the determinant factorization relating the Hessian in the axial chart to `det M_act` (Martin `thermal-contact-cancellation.tex:45–79`; v3 7:241–259); and the proof of the Ward identity, which restores the axial gauge and uses uniqueness there (Martin `:195–204`; v3 7:549–555). `DY(0)` does not depend on the forest: Lean `y_stems` (`Drift.lean:478`, statement read); Martin `:202–203` ("Replacing the branch by its linear tangent does not alter `DY(0)`"). Lean's `YM.Tree.Forest` (`YM/Tree/Pines.lean:24`, definition read) is an arbitrary structure per coarse site, and `lean_drift` has no translation hypothesis.

Inference of the agent, not stated in a source: the hypothesis "one reference tree translated over the blocks" is not needed for 7:521–568.

## Where v3 has these objects under other names

- `M_act` is the completed matrix `C = J + F*F` of 7:251–252 (at zero background `𝒞 = ℋ + F*F`, 7:876–879).
- `M_core` is the "blocked completed matrix `C_0`", taken "after removing the contact term of the averaging operation" (7:772–774). The match with Martin is by role (`Θ = C_0 − Ã_μ` at 7:480 against `M_core − M_rank`), not by a shared symbol.

## Discrepancies and clashes found

- Martin (`thermal-contact-cancellation.tex:94`) and Scott (`B-section.tex:645`) give the centered tangent as `(Wx, 0)`; v3 gives `(Wx, r_x)` with a possibly nonzero `r_x` (7:506, 580–582).
- `Z` is the "coarse-frame projection" at 7:477 and the contact term at 7:527.
- `r_x` is the coarse scalar component at 7:506, `r` the scalar coordinate at 7:695, `r(x)` the penalty gradient at 7:523 (Martin writes `b(x)`, Scott `d`).
- `A` is the fine kinetic Hessian at 7:275 and `M_core` at 7:527.

## Proposed wording (not applied; replaces text inside lines 521, 523, 524)

Line 521: "The fluctuation coordinates are the fine field and one local gauge transformation per block, extended over the block by the minimizing local gauge transformation of Chapter 4 normalized by `h_0 = 1` at the block center. In *rooted coordinates* the block coordinate is this transformation at the block center; in *centered coordinates* it is multiplied by the nearest group element to the `ω`-weighted mean of the normalized transformation over the block, and the transformation on the block by its inverse, which gives the centering `Σ_x ω(x) Π F_x = Π 1` of Section (ch07:weighted). Use rooted coordinates for the following exact calculation. Let `w_x(v)`"

Line 523: "`v`, with `w_x(0) = 0`. Let `r(x)` be the derivative of the penalty term with respect to that increment of the averaging operation. Let `M_act(x)` be the completed matrix `C = J + F*F` of Section (ch07:completion) at the critical configuration over `x`: the Hessian of the path action plus penalty term in the fluctuation coordinates, plus the square of the gauge condition."

Line 524: "Let `M_core(x)` be the same matrix with the Hessian of the penalty term replaced by its pullback `H*BH` through the derivative `H` of the averaging operation, as in (ch07:theta); this is the matrix `C_0` of Proposition (ch07:comparison-input). Set"

Stated in the sources: both matrices, the rooted normalization, the centering, `A = M_core` in rooted coordinates. Inference of the agent: "and the transformation on the block by its inverse" (from the Lean docstring `Chart.lean:299` with Scott `:645`); the identification with `C_0` (from 7:773 and Scott `:633`); "path action" (Lean `mainTerm`, Scott "leading action", Martin "fine kinetic" match by role). The label names in the proposal were not checked against the file.

## Not checked

That `Lean/` is at the pinned revision; the proofs of `lean_drift`, `guard_y`, `y_stems`, `abides`, `fields` (statements read); the definitions of `Critical`, `Guessed`, `PriceGap`, `Inputs`, `mainTerm`; `HaarJac.lean` and `Completion.lean:441ff`; Scott's Def. D20b and Lemma B6; Martin `inherited-loop-transport.tex`; other uses of "rooted" in chapters 6, 9, 11. No build was run.
