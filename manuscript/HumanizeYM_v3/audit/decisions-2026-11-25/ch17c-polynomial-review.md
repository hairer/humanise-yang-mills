# Review of the rewrite of 17c:55–69

Independent agent, 25 November 2026, as handed back (condensed). Read: 17c:1–140, 200–389; 17m:150–279; 5:440–609, 1060–1170; 17t:1–80. The author's report was read last.

## Verdict

The rewritten proof holds; no mathematical error was found. One small gap was closed inside a line. Two points are left unstated in the text. The later passages that still referred to the alias argument were brought into agreement with the new proof.

| Point | Verdict |
|---|---|
| (a) (ch17:defect-four) is equivalent to vanishing of `B` on pairs of polynomial fields of total degree at most 3 | correct: the symbol is analytic by the exponential locality assumed at 17c:14–15; the Taylor coefficients are the polynomial moments of the kernel |
| (b) Ward identity for bounded potentials and fields of polynomial growth | correct (truncation argument). Unstated: the computation is on the covering lattice, with the period-independent kernels of 5:445–446, 586–601; polynomial fields do not exist on the periodic lattice |
| (c) `W_a − W_s` and `W_F − W_a` are gradients of bounded potentials | correct for the first (5:1106, 1108, 1124–1126). For the second chapter 5 says only that the potential vanishes at the block roots (5:1139–1143); boundedness follows because each spanning tree lies in its block (5:917). Added at 17c:62 |
| (d) `D²G(0)[a,a'] = B(W_F a, W_F a')` | correct |
| (e) use of (ch17:polynomial-response) | correct and not circular: 17m:216–226 was re-derived from (ch05:transport-formula) and uses only chapter 5. Unstated: 17m speaks of vector polynomials; fields with values in the Lie algebra need `W_s` to act componentwise |
| (f) `j ≥ 5` | correct ((ch05:actual-bridge) for `r ≤ j−2`, used with `r ≤ 3` at 17c:116); the present argument needs only `j ≥ 4` |
| (g) rescaling `L^{-n-2}` | correct; for `n = 4` it gives `L^{-6}·L^5 = L^{-1}`, consistent with (ch17:quadratic-current-contraction) |
| (h) the base-point average `K_0` | correct |
| (i) the conclusion is what the chapter uses (17c:92, 103, 208) | correct |

## Edits (within lines; 396 and 480 lines unchanged)

- **17c:62**: the potential of `W_F a − W_a a` is bounded, being a sum of values of `W_a a` along the spanning tree of one block.
- **17c:71–72**: grammar.
- **17c:76–78, 80–87**: the alias cases, "transverse coefficient", "projected coefficients" are replaced by a statement of what the new proof establishes; the double zero of `K_0` (73–75) is kept as a true remark, said not to be used.
- **17c:323–330**: the argument with `N_0(0) = L^{-1}I` and nonzero aliases is replaced by the exact rescaling with `n = 2`: `B` vanishes for `r + r' < 2` because a constant field is the gradient of a linear potential; for `r + r' = 2` the factor `L^{-4}` is compensated by `L^4` in `J'`; `K_a` has coefficient sum one.
- **17m:232–234**: the reference to "the order-two transverse estimate" is replaced.

Inference added by the reviewer, to be checked by the author: the vanishing on constant legs (17c:324–325), the extension of the Ward identity to linear potentials, the boundedness of the tree potential (17c:62). The new 17c:323–330 assumes, as the old text did, that `J_ab` is gauge invariant with zero first field derivative; neither was verified.

## The text's route against Lean's (source read; no Lean command run)

Same skeleton: `YM.Trace.Perfect.crossing_step` (`Lean/YM/TraceExtension/Perfect/Zinnia.lean`, read in full): Hessian of the composite on images of probes (`YM.Stationary.pay_second`), images approximated by `inflateA` (`Pulp.lean:32`), lower terms killed, result `L^{-b}B`. Polynomial moments: `YM.Trace.Perfect.Ether` (`Ether.lean:34`, read), proved in `Ether.witty` via `Carrier.pure_moment` (not read).

Differences:

1. Lean removes the gradients by an exact nonlinear gauge transformation of the critical configuration (`YM.Stationary.liftedUp`, `Next/STATIONARY/Joint/Regulator.lean:567`, read; `YM.Trace.Perfect.smooth_plan`, `Equate.lean`, read), not by linear Ward identities. The text's route is valid given (b) and (c).
2. Lean works on tori with the period tending to infinity; the text computes on the covering lattice and does not state that passage.
3. Lean's probes have degree at most 2, plus a constant probe in a second slot pairing the vector field with the test; the text tests degrees up to 3 and has no such slot. Pairs of degree (3, 0) are automatic by the constant-leg argument.
4. Lean's `W` (`installed ratio k`) has exact polynomial moments, which points to `W_s`; the definitions were not traced to the formula of chapter 5.
5. `YM.Trace.Perfect.Sheaf.top` (`Fossa.lean`, read) handles finite combinations of translates; that its consumer is `K_0` was not checked.

## Disagreements with the author's report

`Sheaf.top` is Lean's analogue of the `K_0` step, at least in form (the report said each base point is treated separately). The vanishing of the stress Hessian below degree two is automatic and is now in the text. (ch17:polynomial-response) does follow from chapter 5 alone (checked).

## Not checked

The build and the rendered pages; the proofs of `Carrier.pure_moment`, `orbit_gain`, `amongL`, `breeze`, `sprout`; `dot_predict`, `colors`, `port` beyond their statements; the consumers of `Tour.be` and `Sheaf.top`; 7:812–816 and 7:1135–1148, which carry their own alias arguments; whether `J_ab` has zero linear part.
