# 17c:55–68 rewritten along the route of the formal proof

Report of the rewriting agent, 25 November 2026, as handed back (condensed). Issue 1 of the fork, items 24 and 26. The agent's run was interrupted once and resumed. Lean paths under `Lean/YM/TraceExtension/` unless stated.

## What changed

Lines 55–56, 58–59 and 61–68 of `17-current-contraction.tex`; lines 57, 60, 69 and the lead-in 48–53 are unchanged. The proof now computes with `W_s` and tests the Hessians on polynomial fields; the alias argument is gone. The label `ch17:current-alias` is removed (nothing else referred to it) and `ch17:polynomial-four` is new. The lead-in still names `W_a`, which lines 112–117 need for the fine-difference bounds; the new text passes from `W_a` to `W_s` by `W_a − W_s = −d_{0,f} E R W_s` (ch05:corrected-transport).

## Each step and what supports it

1. **Pullback Hessian.** Lean `YM.Stationary.pay_second` (`Next/STATIONARY/Joint/Completion.lean:23`, statement read), used in `YM.Trace.Perfect.crossing_step` (`Perfect/Zinnia.lean:56`, proof read); v3 17c:48–52.
2. **Replacing `W_F` by `W_s`.** Lean does it nonlinearly: `YM.Trace.Perfect.colors` (`Perfect/Equate.lean:77`, statement read) composes with a fine gauge transform of the critical configuration; `smooth_plan` (`Equate.lean:15`, proof read); `YM.Precision.extracted` (`PREC/TreeMatch.lean:26`, definition read); the theorem using it is `YM.Trace.Perfect.Tour.be` (`Perfect/Tael.lean`, proof read). The text uses instead the linear Ward identity of 17c:16 and (ch05:corrected-transport), with bounded potentials from 5:1104–1106 and 5:1123–1126.
3. **Taylor coefficients of the symbol are values on polynomial fields.** Lean `YM.Trace.Perfect.Stoke` (`Perfect/Spurs.lean:57`, definition read): convergence of the Hessian on polynomial probes of type `RowGrade` (1, `x_i`, `(x_i+x_j)²`). The hypothesis `Tip … 0 5` (`Perfect/Fossa.lean:31`) is vanishing for total degree at most 3. The equivalence with the symbol condition is the agent's own elementary step; Lean has no symbol.
4. **`K_0 E_b` inherits the condition from the translates of `E_b`.** Inference of the agent. Lean applies `Tour.be` to each fine base point separately.
5. **`D²G(0)[P,P'] = B(W_s P, W_s P')` for polynomial `P, P'`.** Lean `trough` (`Perfect/Dune.lean:18`, proof read), `Crossed.eval` (`Spurs.lean`, proof read). v3: decay of `W_s` at 5:586–601. Absolute convergence is the agent's step.
6. **`W_s` maps polynomials of degree `r` to polynomials of degree at most `r`, leading part `L^{-r-1} P`.** Lean `YM.Trace.Perfect.Ether` (`Perfect/Ether.lean:34`, definition read), `Ether.witty` (`:38`, proof read down to the call of `Carrier.pure_moment`, not read). v3: (ch17:polynomial-response), 17m:237–249.
7. **Vanishing and the exact rescaling `L^{-n-2}`.** Lean `crossing_step`; wrappers `Slide.smooth_cost` (`Perfect/Gist.lean:51`, proof read) and `Tour.be`.

## Inference, not inspected evidence

The symbol–moment equivalence; the truncation argument extending the Ward identity to bounded potentials; that the tree potential is bounded; that `K_0` preserves the condition; that the derivation of (ch17:polynomial-response) uses only chapter 5; that `j ≥ 5` (deduced from the use of (ch05:actual-bridge) at 17c:116).

## Asserted in the text, not stated outright by Lean or v3

1. (ch17:polynomial-response) is applied to fields with values in the Lie algebra; 17m speaks of a "vector polynomial". Lean acts componentwise.
2. Lean's probes have degree at most 2 on each leg; the text also covers pairs of degree (3, 0).
3. Lean works on tori with a limit of large period; the text works on the covering lattice, as 17m does.
4. Lean's functional has a second component encoding the vector field `Y`, not reflected in v3's `E_b`.
5. v3 has no statement "`j ≥ 5`".

## Later lines that referred to the old argument

- 17c:71–87 ("transverse coefficient has order two", "projected coefficients").
- 17c:323–331 (`N_0(0)`, "transverse coefficients at nonzero aliases").
- 17m:232–234 ("stronger than the order-two transverse estimate sufficient for the current contraction").
- 7:812–816 and 7:1135–1148 carry their own alias arguments, independent of 17c.

Not checked by the agent: that the stress Hessian vanishes below degree two for the transferred functions.

## Not checked

The proofs of `Carrier.pure_moment`, `origin_money`, `orbit_gain`, `amongL`; `dot_predict` beyond its statement; the consumers of `Tour.be` and `Tour.boar`; how the per-base-point Lean statement is combined with `K_0`; the derivation of order-`j` vanishing in 17m; the two earlier manuscripts. No Lean command was run.

## Checks run

Line count 396 before and after; `python3 tools/check_draft.py` passes; `latexmk` exit 0, passage on pages 256–257, new equation (17.15).
