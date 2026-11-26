# Audit: chapter 7 (determinant, contact term) and chapter 17 (current contraction)

Report of a read-only agent, 26 November 2026, as handed back (condensed). Worktree at `e53484a2`. Nothing was changed; no Lean or LaTeX command was run. Paths of the manuscripts are under `manuscript/`; Lean paths under `Lean/YM/`. "Martin" = `existence/`, "Scott" = `HumanizeYM_v2/`. The agent could not confirm that `Lean/` in the worktree is at the pinned revision `3456e5e7` (no file in `Lean/` names it).

| Point | Verdict |
|---|---|
| B1 Centered tangent `(Wx,0)` or `(Wx,r_x)` | resolved by sources; wording |
| B2 `M_core`, `M_act` | resolved by sources; definitions missing |
| B3 Alias arguments 7:812–818, 1135–1148 | resolved by sources; wording |
| B4 17c:55–68, 71–87, 323–330 | persists: torus against covering lattice; `j ≥ 5` |
| B5 17m:104 | persists |
| B6 17:128–129 strip argument | resolved by sources; wording |
| B7 7:578–579 reference | wrong reference only |
| B8 Polynomial preservation 17m:216–249 | resolved by sources; sketch |
| B9 `W_F` and translated forests | persists at 17c:164–165; chapter 6 not a gap |

## B1. The centered tangent

**v3.** 7:505–507 "tangent `(Wx,r_x)`, where `r_x` is its coarse scalar component after recentering" (`W` not named there); 7:574 "The smooth representative of the linearization `W` … is `W_a`"; 7:580–582; 7:882 "`Tu=(u,W_a u,r_u)`"; 7:693–698.

**Martin.** `thermal-contact-cancellation.tex:93–94`: "`Dζ(0)x=(Wx,0)`"; `selected-stationary-linear-data.tex:44–93`: there `W = A_0`, v3's `W_s`.

**Scott.** `part2/C-section.tex:161`: "the smooth representative of its tangent is `(v,W_s v,0)`. Its rooted representative uses `W_0=W_r` and has the accompanying centred frame component `−𝓕_m W_r v`; the joint gauge transformation … relates the two." `B-section.tex:388–390`: `W_r = W_s − d_f I_ℓ(𝓕_m W_s)`, v3's `W_a`.

**Lean.** `YM.Push.Loops.graft` (`Push/LOOP_COEFFICIENT/Column.lean:50`, definition read); `YM.Push.Loops.centered_graph` (`:117`, statement read, proof skimmed). Lean has no `W_a`.

**Finding.** Both are correct: they are tangents of two gauge-equivalent representatives. The earlier texts use the one with fine part `W_s`, with zero scalar part; v3 uses `W_a`, whose centered scalar part is `r_x = −R W_a x`, in general nonzero (this is Scott C:161). The chain rule 7:513–516 holds for either. v3 does not assume `r = 0` later (7:915). At 7:537–539 the identity `QW = I − b^{-1}K_c` with the rooted `Q` holds for `W_a` and not for `W_s`, so the unnamed `W` must be `W_a`.

**Fix.** At 7:506 write `W = W_a` and `r_x = −R W_a x`; say that the rooted tangent is `(W_a x, 0)`.

**Inference of the auditor.** The formula for `r_x` (from 5:1104–1109, 7:693–698); the rooted tangent `(W_a,0)` (from 5:1139–1143).

## B2. `M_core` and `M_act` (7:521–565)

**Lean** (`Next/STATIONARY/Joint/Completion.lean`): `YM.Stationary.medals` (`:59`, definition read) is the Hessian of main term plus penalty in joint increments plus `F*F`; `YM.Stationary.legion` (`:61`, definition read) is `b*Kb + H*BH + F*F`; `YM.Stationary.Teller.contact` (`:116`, statement and proof read): `medals = legion + contact`; `abides` (`:66`) and `fields` (`:91`), statements and proofs read: congruence under the change of coordinates, for `medals` only at the critical configuration; `YM.Stationary.lean_drift` (`Joint/Drift.lean:498`, statement read); `guard_y` (`:265`, statement read).

**Martin.** `stationary-determinant-prices.tex:172–173`; the full derivation at `thermal-contact-cancellation.tex:127–204`.
**Scott.** `B-section.tex:618–633`.

**Finding.** Both identifications are verified from the definitions: `M_act` is `C = J + F*F` of 7:251–252 at the critical configuration; `M_core` is the same with the penalty Hessian replaced by `H*BH`, and equals `C_0` of 7:773 (`Θ = C_0 − Ã_μ` at 7:480 contains `H*BH` and no contact term), up to the change between rooted and centered coordinates, which has determinant one. With these definitions and the rooted tangent of B1 the proof of (ch07:contact-exact) is complete. v3 compresses two steps that Martin writes out (`QW = I − b^{-1}K_c` gives `Dr(0) = −K_c`; the expansion `tr(A^{-1}Z) − ½ tr(A^{-1}ZA^{-1}Z)`), and 7:530–531 does not say that the congruence for `M_act` holds only at the critical configuration.

**Not checked.** Proofs of `lean_drift`, `guard_y`.

## B3. The alias arguments at 7:812–818 and 7:1135–1148

**Martin.** `inherited-loop-transport.tex:130–252` has the same argument with the translation-covariant matrix (v3's `W_s`); `quadratic-pole-transport.tex:120–137` derives `N_0(0) = μI`.
**Lean.** `YM.Push.Loops.GaugeAlias` (`Push/LOOP_COEFFICIENT/GaugeAlias.lean:18`, definition read), `GaugeAlias.probe` (`:29`, statement and proof read); Lean does this calculation only with the translation-covariant tangent.

**Finding.** Valid for `W_s` or `W_a`; not meaningful for `W_F` with a forest that is not translated. v3 does not say which is meant (7:1112–1118 has just chosen `W_s`). 7:813 uses `N_l`, `A_l` before their definition at 7:1135. The count at 7:817 presumes `N_0(0) = L^{-1}I`, which v3 has only implicitly (5:522, 5:599–601).

**Fix.** Name `W_s` in both places; define `N_l`, `A_l` at first use; cite 5:522 and 5:599–601.

## B4. 17c:55–68, 71–87, 323–330

No counterpart of this subsection found in Martin or Scott (searched "current defect", "polynomial fields", "polynomial moment"). Lean: `YM.Trace.Perfect.Stoke` (`TraceExtension/Perfect/Spurs.lean`, definition read) works on tori with the period tending to infinity; `YM.Trace.Perfect.crossing_step` (`Perfect/Zinnia.lean:56`, statement read) requires `fderiv (H w) 0 = 0` and `4 ≤ d`.

- **(i) Vanishing on a constant leg (17c:324–325), (ii) Ward identity for bounded or linear potentials (17c:56), (iii) the potential of `W_F − W_a` is bounded (17c:62), (iv) `J_ab` gauge invariant with zero first derivative (17c:323–330).** True by the auditor's argument (truncation under joint exponential decay of the kernel in both legs; trees inside their blocks, 5:917–918; `Ad`-covariance of the plaquette fields, 17t:185–190, preserved by the transfer). None is stated in a source. Not checked: that the reference stress subtracted at 17c:319–320 is gauge invariant.
- **(v) Covering lattice. Persists.** Chapter 5 constructs the critical configuration and `W_F` on a torus of coarse period `s` (5:915–917; 5:1103–1104). 17c:62–63 evaluates `D²G(0)` on polynomial fields, which exist only on the covering lattice; no sentence connects the two. Needed: independence of the kernels from the period (5:448–450, 5:599–601) and that the kernel of `D²G` on the torus is the periodization of the one used. (ch17:polynomial-response) is stated for a "vector polynomial" (17m:240); for fields with values in the Lie algebra one needs `W_s` to act as the identity on the Lie-algebra factor, which Martin states (`selected-stationary-linear-data.tex:30`) and v3 does not.
- **(vi) `j ≥ 5`. Persists.** 17c:64 asserts "`j ≥ 5`, since (ch05:actual-bridge) is used below with three fine differences"; the standing hypothesis is `j ≥ 4` (5:304, 5:312). 17c:116 uses `r ≤ 3` and (ch05:actual-bridge) gives `r ≤ j − 2`. Martin's degree-four argument asks `j ≥ 6` (`principal-reference-attenuation.tex:14`).

**Fix.** A hypothesis `j ≥ 5` in the schedule or at (ch17:quadratic-current-contraction); a paragraph passing from the torus to the covering lattice; a sentence on the action of `W_s` on Lie-algebra values; optionally a lemma for (i)–(iii).

## B5. 17m:104 "By its definition in Chapter 9"

17m:104–108: "By its definition in Chapter 9, `Z_ord = 𝒞 exp[−βS − 𝓛 − E_reg]`, `D_V log 𝒞 = 0`." `Z_ord` is defined only at 17m:91–92 (the integral of the normalized conditional integrand of one rooted component). `E_reg` occurs nowhere else; the closest objects are `E_i^reg` of (ch04:effective-density) (4:552–562) and `P^path = β𝒦 + 𝓛` (9:22–24). Not found in Martin or Scott (searched `Z_{\rm ord}`, `E_{\rm reg}`, "small-field score", `D_V`); Lean not searched.

**Finding.** The reference is wrong and the identity is asserted, not derived. No statement of chapters 4 or 9 gives the form for one component with a constant `𝒞` independent of `V`. "If an intermediate local normalization depends on `V`, it is included in `𝓛 + E_reg`" is a stipulation.

**Fix.** Cite (ch04:effective-density) and 9:22–24, define `E_reg`, and derive the identity for one component from the step theorem and the expansion of chapter 9 (9:89–96), or state it as an input. **Not checked:** chapters 8 and 11.

## B6. 17:128–129

The cited argument is at `14-reflection-ward.tex:166–205` and Proposition (ch14:smooth-comparison) (`:229–258`). It applies uniformly in `u` if the inputs are uniform, as `17-trace-law.tex:118–121` asserts. Two things are left unsaid (auditor's inference): the proposition, stated for sequences, gives uniformity by applying it along arbitrary sequences `u_n`; and the `α_j` must move with `u` (differences fixed), which 17-trace-law.tex:118 permits.

## B7. 7:578–579

Wrong reference only: `W_a` is defined in (ch05:actual-tangent) (5:1082; (ch05:corrected-transport) at 5:1107), not in (ch05:transports).

## B8. Polynomial preservation (17m:216–249)

**Lean.** `YM.Trace.Perfect.Ether` (`TraceExtension/Perfect/Ether.lean:34`, definition read); `Ether.witty` (`:38`, proof read in full); `YM.Planned.PrimaryIntegral295.Carrier.pure_moment` (`Planned/PRIMARY_INTEGRAL_295/Bijets.lean:99`, statement and proof read), through `status`, `resonate`, `vanish_message`; `pilot_vanish` (`Headroom.lean:120`, statement read); `origin_money` (proof read); `pilot_origin`, `pilot_none` (`Next/FREE_KERNELS/ZeroAlias.lean:25, 46`, statements read); `pilot` (`Next/FREE_KERNELS/Pilot.lean:46`, definition read).

**Finding.** v3 follows the same route as Lean (vanishing to order `j` at nonzero aliases, identity at the zero alias) but as a sketch: the alias-sum step is compressed and the value `I` of the zero-alias column is asserted (also at 5:599–601). **Not checked:** proofs of `pilot_vanish`, `pilot_components`; that Lean's rows are v3's `W_s`.

## B9. `W_F` and translated forests

Chapter 6 (6:944–977, Proposition (ch06:mean-cancellation)) uses `W_F` only through pointwise identities and holds for every forest. 17c:164–165 takes the translates of one reference tree and says that the independence of pullbacks of gauge-invariant functions from the forest "is used here and is not proved in this chapter". The result is usable for the forest-averaged construction of chapter 9 only with that independence.

**Lean.** `YM.Bid.F05` (`Bid/Station.lean:94`, definition read): for two forests the `tested` functions agree near 0; `YM.Work.F05.answer : YM.Bid.F05` (`Work/F05.lean:60`, statement only). The definition of `tested` was not read.

**Fix.** A lemma that two forests give critical configurations differing by a fine gauge transformation equal to one at the block roots (Scott `B-section.tex:599` gives the invariance of the kernel under such transformations).

## New

1. 7:813 uses `N_l`, `A_l` long before 7:1135.
2. The standing smoothing order is `j ≥ 4`; 17c needs `j ≥ 5`.
3. 17m:104 writes `βS` where chapter 9 writes `β𝒦`.
4. 7:530–531 omits that the congruence of `M_act` holds only at the critical configuration.
