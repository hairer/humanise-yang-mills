# Independent review of `chapters-7-and-17.md`

Report of a reviewing agent (not the auditor), 26 November 2026, as handed back (condensed). Read at `7d23f9e2`. Nothing was edited; no LaTeX or Lean build was run. 17c = `17-current-contraction.tex`, 17m = `17-marked-trace-rates.tex`, 17t = `17-trace-transfer.tex`, 17w = `17-variable-windows.tex`, 9s = `09-stationary-remainder.tex`, 9f = `09-forest-average.tex`.

**The Lean pin is confirmed.** `source/upstream.json` records revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464` with `project_root: "Lean"` (also `README.md:20`, `source/audit.md:5`); `git diff --quiet 9865613f HEAD -- Lean` reports no change since the import; `cd Lean && shasum -a 256 -c SOURCES.sha256` gives 9,497 OK, failing only for the 10 `verification/*.log` files, which were never imported.

| Point | Auditor | Review |
|---|---|---|
| B1 | wording | confirmed with corrections: `W` need not be `W_a` |
| B2 | definitions missing | confirmed with corrections |
| B3 | wording | confirmed with corrections: `A_l` is never defined |
| B4 | persists | confirmed with corrections: (v) narrower; (vi) persists |
| B5 | persists | weakened: chapter 9 has the form for related objects |
| B6, B7, B8 | wording / reference / sketch | confirmed (light check for B6, B8) |
| B9 | persists at 17c:164–165 | weakened: Lean supplies the missing lemma |

## Errors of fact in the audit report

1. B4: counterparts exist: Scott `part2/I-section.tex:349–355`; Martin `quadratic-pole-transport.tex:68–117`.
2. B4(v): v3 does state that the covariance acts as the identity on the Lie-algebra factor (5:172).
3. B4(i) is not independent of (v): on a torus a constant one-form is not a gradient.
4. B5: 9s:117–133, 9:56–79 and 9f:236–249 give the form with a constant normalization for related objects.
5. B9: Scott's invariance of the kernel is at `B-section.tex:583`, not 599.
6. B9: the needed lemma is in Lean.
7. B1: `QW = I − b^{-1}K_c` holds also for `W_F` (5:1142).
8. B2: the congruence sentence is at 7:533–534.
9. B3: `A_l` is not defined at 7:1135 nor anywhere in chapter 7.
10. Martin's `j ≥ 6` concerns a different statement.

## B4. 17c:55–68, 71–87, 323–330

Quotations accurate. Steps (i)–(iv) re-derived by the reviewer:
- (ii) holds under joint exponential decay of the kernel in both legs; 17c:55 asserts that decay for "a gauge-invariant local function"; for the transferred functions it must come from the transfer bounds (not checked).
- (i) is true on `ℤ⁴` and false as stated on a torus, so 17c:324–325 depends on the passage of (v).
- (iii) true (5:1139–1141; 5:1104–1108; 5:1124–1126).
- (iv) true initially (`17-trace-law.tex:185–191`) and preserved by the transfer; the preservation is the reviewer's inference, not stated in v3.

**Reference stress (17c:319–320)** is nowhere said to be gauge invariant. It matters at 17c:345–347: the division by two curls of the remainder uses the Ward identities on each leg.

**(v) Torus against `ℤ⁴`: narrower than reported.** v3 has the machinery: 5:445–446 ("The same Fourier symbol works on every finite-period grid"); 5:710–754 (the periodization criterion; "All limits are for the chosen kernels on the infinite lattice `ℤ⁴` and their periodizations"); 5:1101; 7:169; 7:557–560, 778–779, 990–995; 17c:163, 199, 396. Missing is one sentence: the Hessian of the pulled-back function on the torus is the periodization of `B∘(W_s⊗W_s)` on `ℤ⁴`. Martin does the step (`quadratic-pole-transport.tex:68–69`, 98–108); Lean by limits along tori (`YM.Trace.Perfect.Stoke`, `Lean/YM/TraceExtension/Perfect/Spurs.lean:57`, definition read).

**(vi) `j ≥ 5` persists.** The only occurrence in all chapters is 17c:64, stated as a requirement. Standing hypothesis `j_h ≥ 4` (5:304, 5:312). Chapter 10's schedule (10:25–31, 66–70, 124–126) allows "countably many finite numerical requirements on the schedule" but none is entered. Other requirements on the smoothing order, also not entered: 11:350–352 (at least `d+3`), 17m:251. Scott's counterpart works "after stage `j ≥ 7`".

Not checked: the joint decay for the transferred functions; proofs of the Lean lemmas.

## B5. 17m:104

Quotation accurate; `E_reg` occurs only in 17m (107, 111, 113, 161).

**Found in addition.** 9s:111–133: the pure small-field block integral equals `Ω e^{−Φ(x)} R(g,x)` with `Ω` independent of `x`, which has the form `𝒞 exp[−βS − 𝓛 − E_reg]`. 9:56–79: the constant factor of the change of variables; the flat determinant "is extracted once, not separately for every eventual connected component". 9f:236–249 (Assumption (a)): the block integral with a constant `𝒩_F`, unproved. Nothing in chapters 4, 6, 8, 11. Scott `B-section.tex:597` has the corresponding remark.

**What remains missing:** the form for one rooted component of the conditional integrand; since 9:75–76 extracts the constant globally, a constant for one component needs an argument. If it rests on 9f (a), it rests on an unproved assumption. The reference "Chapter 9" is right in part; `βS` against `β𝒦` confirmed. Lean not read.

## B9. `W_F` and translated forests

17t and 17w do not mention forests or trees. `YM.Bid.F05` (`Lean/YM/Bid/Station.lean:94`, definition read) with `YM.Precision.tested` (`Lean/YM/PCalc/Chart.lean:81`, definition read: path action plus penalty at the lifted configuration) is independence from the forest of the value of the action and of the thermal term, not of arbitrary pullbacks. `YM.Work.F05.answer` (`Lean/YM/Work/F05.lean:60`, proof read) is proved from:
- `YM.Work.F05.graph_switch` (`Work/F05/Graphs.lean:37`, statement read): `switch B T x (ρ x) = u x` near 0;
- `YM.Work.F05.fine_switch` (`Work/F05/Actions.lean:81`, statement read);
- `YM.Precision.Profiles.wiped F U = Lattice.gauge (F.foldAt U) U` (`PCalc/Profiles.lean:19`, definition read);
- `Forest.fold_root` (`Lean/YM/Tree/Cut.lean:23`, statement read): the gauge transformation is 1 at the block roots.

Together: the critical configurations for two forests differ by a fine gauge transformation equal to one at every block root — the lemma the audit asks for — at least near 0. v3 has only the linear analogue (9f:114–136; 9:75); 11:679 asserts independence from the forest without proof. Not checked: proofs of `graph_switch`, `fine_switch`; that Lean's critical point is v3's; the hypotheses `PriceGap`, `W.Bounds`.

## B1. Centered tangent

Verified from the definitions: with `u = W_a x`, `r_root = 0`, 5:1113–1114 make both stationarity equations vanish, so `(W_a x, 0)` is a rooted critical tangent; `r_x = −R W_a x` follows from 7:695. The same holds with `W_F` (5:1142), which is the tangent of v3's actual critical configuration in the block axial gauge (5:1148; 9s:188–190). So the unnamed `W` at 7:506, 537 is not forced to be `W_a`; the text must say which representative is meant.

Further: the second derivative along the tangent is independent of the representative only if the function is invariant under the fine gauge transformation relating the representatives; 7:508–511 states invariance only under constant gauge transformations. One sentence is needed (covariance of the Hessians, 7:533–534).

## B2. `M_core`, `M_act`

Confirmed that neither is defined (only 7:527, 529, 542). Lean definitions as reported. With rooted scalar tangent zero, `Dr(0) = b(QW − I) = −K_c`: the zero rooted scalar of B1 is used. `M_core = C_0` is consistent with 7:773, 7:480, 7:801–803, but v3 defines `C_0` only by a phrase, so the identification is plausible, not verified from a definition. Not checked: `Shell`, `lean_drift`, `guard_y`.

## B3. Alias arguments

Confirmed. `A_l` is undefined throughout chapter 7 (7:813, 1140); chapter 5's `𝒜_l` (5:500, 523) is the alias symbol of `W` itself, a different object, so a new symbol is needed for the alias symbol of the adjoint averaging operator. 7:1136 says "the linearization of the critical configuration" just after 7:1112–1118 chose `W_s`.

## B6, B7, B8

Confirmed. 17m:251 adds another requirement on the smoothing order.

## New

- 17c:319–320: gauge invariance of the reference stress is unstated and used at 17c:345–347.
- Three requirements on the smoothing order (17c:64; 17m:251; 11:352) are not entered into the schedule of chapter 10.
- 7:508–511 gives invariance only under constant gauge transformations.
