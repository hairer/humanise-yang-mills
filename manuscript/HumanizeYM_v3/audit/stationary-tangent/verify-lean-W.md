# Verification of Lean claims about W_s / W_a / W_F

Lean repository: /Users/mgubi/OpenAI-YM, HEAD `1dba696` ("Add GitHub Actions workflow ..."), toolchain `leanprover/lean4:v4.32.0`.
Paths below are relative to that repository. Nothing was edited there; no build was run.
Manuscript read: v3 `chapters/05-gaussian.tex` 454-560, 1070-1165, 1220-1245; `17-current-contraction.tex` 30-125;
`17-marked-trace-rates.tex` 232-270. `audit/terminology.md` was not read.

## Commands run

- `lake env lean leanscratch/A.lean` (imports `YM.Work.F04`, `YM.UVNext.PRICED_KERNELS.Trees`, `YM.Push.LOOP_COEFFICIENT.Column`): exit 0, about 20 s. Output in `leanscratch/A.out`.
- `lake env lean leanscratch/B.lean` (imports `YM.TraceExtension.Perfect.Gist`, `...Perfect.Zinnia`, `YM.Next.FREE_KERNELS.Primal`): exit 0, about 5 s. Output in `leanscratch/B.out`.
- `#print axioms YM.Precision.stationed` and `YM.Work.F04.tangent`: `[propext, Classical.choice, Quot.sound]` only.
- Text searches with `grep` over `YM/` (all occurrences of `fixRoot`, `extracted`, `straighten`, `Guessed`, `fleece`, `gaugePad`, `rootAt`, `sitesCopy`, `duplicateM`, products `probe _ * _`, matrices of type `Body 0 f x Body 0 c`).

Elaborated (`#print` / `#check`), all names fully qualified as returned by Lean:
`YM.Precision.extracted`, `.straighten`, `.stays`, `.Inputs`, `.stationed`, `.action`, `.probe`, `.Guessed`, `.relative`, `.linearCopy`,
`YM.Work.F04.tangent`, `YM.Work.F04.answer`, `YM.Bid.F04`, `YM.Tree.Forest`,
`YM.UVNext.PricedKernels.factor_tree`, `.extract_price`, `YM.Push.Loops.sampled_stationary`, `.centered_graph`, `.graft`,
`YM.Trace.Perfect.inheritJ`, `YM.Stationary.encamp`, `.abode`, `.liftedUp`, `.salute`,
`YM.Trace.Perfect.smooth_plan`, `.first_fresh`, `.colors`, `.fleece`, `.gaugePad`, `.Slide`, `.Lot`, `.Ether`, `.crossing_step`, `.Slide.smooth_cost`,
`YM.Next.Free.Flight.genuine_alias`, `.scaled_tri`, `.tangent`, `.duo`.

## Dictionary established by formulas (not by names)

| v3 object | Lean | formula used for the match |
|---|---|---|
| `M` (straight block average, coarse links <- fine links) | `YM.Precision.mean S` (YM/PREC/FrameResponse.lean:65) | weighted sum over patch points of line integrals along the straight coarse-step path `S.repath` |
| `R` (root row) | `YM.Precision.fixRoot S` (:63) | `probe = mean + d 0 c * fixRoot` (:68), i.e. v3 `Q = M + d_{0,c} R` |
| `Q` (rooted average) | `YM.Precision.probe S` (:68) | same; `root_gradient` (:92): `probe (d_{0,f} v) = d_{0,c}(v restricted to block roots)` = v3 (ch05:actual-Q) |
| `K_f`, `K_c` | `YM.Precision.K H = (d 1 n)^T * H * d 1 n` (YM/PREC/TreeMatch.lean:68) | `H` an arbitrary 2-form metric matrix |
| `b` (penalty) | `S.kernel.penalty` | |
| `W_s` | the matrix argument `W`; in every application `YM.Bloch.installed S.ratio T.A0` (YM/CellFourier/Shuttle.lean:35), `T : YM.Precision.Towers` | `Inputs` equations; stencil form `(W p)(x) = sum_z A0(residue x; z) p(parent x + z)` = v3 (ch17:polynomial-response) |
| `W_F` | `YM.Precision.extracted S F W` | vanishes on tree links (`stays`), both stationarity identities (`stationed`), derivative of the germ (`Guessed`) |
| `rep` (linear) | `YM.Precision.linearCopy` (YM/PCalc/Chart.lean:38) | 0 on links internal to a block, coarse value on block-crossing links |
| `W_a = W_s - d_f E R W_s` | no counterpart (see claim 5) | |

## Claim 1. CONFIRMED (read and elaborated)

`YM.Precision.extracted S F W = W + Exterior.d 0 f * straighten S F W` (YM/PREC/TreeMatch.lean:26-27; `#print` reproduces it).
`straighten S F W` (:21-24) is the 0-form-valued matrix whose row at fine site `i` is
`integralLink i (F.hike i) o W  -  (row of fixRoot S at parent(i)) o W`, i.e. (line integral of `W a` along the tree path from `i` to its block root) minus `(R W a)(parent i)`.
`YM.Precision.stays` (:40): `marked F (extracted S F W *v a)` for every coarse 1-form `a`, where `marked F a := forall i in F.trunks, a(i.1, coord i.2) = 0` (:18).
Additional facts read: `centers` (:35): the potential restricted to block roots equals `-(fixRoot S *v (W *v a))`; `YM.UVNext.PricedKernels.factor_tree` (YM/UVNext/PRICED_KERNELS/Trees.lean:53): `straighten S F A = (hiker S F - rootAt S.ratio * fixRoot S) * A`, with `rootAt` the block-constant extension (value at the parent block). Hence
`extracted = W - d_f E_0 R W + d_f (tree-path potential of W)`, `E_0` block-constant, not v3's smooth `E`.

## Claim 2. CONFIRMED (read and elaborated)

`structure YM.Precision.Inputs S W H H' : Prop` (YM/PREC/TreeMatch.lean:76-79) has exactly two fields:
`primal : K H * W = (mean S).transpose * K H'` and `dual : mean S * W = 1 - S.kernel.penalty^-1 . K H'`.
`YM.Precision.stationed` (:81): under `Inputs`, `probe S * extracted S F W = 1 - penalty^-1 . K H'` and `K H * extracted S F W = (probe S).transpose * K H'`.
`YM.Precision.action` (:93): with `T = extracted S F W`, `P = 1 - probe S * T`: `T^T * K H * T + penalty . (P^T * P) = K H'`.
Precision: `Inputs` is a hypothesis on an arbitrary matrix `W`; it does not say `W` is a stencil. It is supplied for `installed S.ratio K.A0` by `YM.Precision.Towers.Diagonal.trial` (YM/PREC/Stacks.lean:82-84) and proved for the Fourier-defined stencil in `YM.Next.Free.Flight.tangent` (YM/Next/FREE_KERNELS/Primal.lean:63), which also gives `T^T d_{1,f} = d_{1,c} mean` and `T H_c d_{1,c} = H_f d_{1,f} A` = v3 (ch05:physical-transports).

## Claim 3. CONFIRMED, with one precision

`YM.Precision.Guessed B W rho := forall x, HasDerivAt (fun t => rho (t . x)) (relative B W x) 0` (YM/PCalc/Chart.lean:97), and
`relative B W b` (:93) is, on each free (non-tree) link `x` and colour `i`, `(extracted S B W *v parts b i)(x) - linearCopy S.ratio b x i`.
So the statement is about directional derivatives along rays, in chart coordinates indexed by free links only, which is v3 (ch05:stationary-tangent) read on free links (on tree links both sides vanish: `YM.Work.F04.parts_stretch`, YM/Work/F04/Pairing.lean:17).
`Guessed` is a definition (a Prop), not a theorem. The theorem is `YM.Work.F04.tangent` (YM/Work/F04.lean:88): from `0 < a`, `PriceGap H p W a` (vertical Hessian gap), `Inputs S U (B.metric.acts f) (C.metric.acts c)`, `YM.Bid.Comptroller H B p W` (the Hessian of the tested action at 0 is the quadratic form of v3 (ch05:actual-hessian)), `Critical H p W rho`, it concludes `fderiv R rho 0 x = relative H U x`. `YM.Work.F04.answer : YM.Bid.F04` (:150) packages existence of `rho` with `Critical`, `Guessed H (installed S.ratio T.A0) rho` and the quadratic value. Axioms: standard three only.
Related: `YM.Push.Loops.sampled_stationary` (YM/Push/LOOP_COEFFICIENT/Column.lean:73) states the derivative of the full fine configuration as `graph G (extracted S F A) 0`.

## Claim 4. CONFIRMED (read and elaborated), with detail

`YM.Trace.Perfect.inheritJ F r f V = f ((YM.Stationary.encamp F r (YM.Stationary.content V)).1)` (YM/TraceExtension/Perfect/Desktop.lean:71), where
`encamp F rho z = abode S F (input z) (rho (arm z)) = (lifting F (input z) (rho ..), 1)` (YM/Next/STATIONARY/Joint/Gauge.lean:219, :22), and `lifting` (YM/PCalc/Chart.lean:60) puts `exp(a_i) * replica V i` on free links and 1 on tree links. So `inheritJ` substitutes the stationary fine field in the forest chart (tangent `extracted` = `W_F`), with `content` the logarithmic chart of `V`. `inheritY` (:73) is the vector-field analogue with an extra transport `shuttle`.
Identification with chapter 17 is by structure: `YM.Trace.Perfect.Dart` (Perfect/Badge.lean:22) has fields `J : Axis -> Axis -> Site -> (Config -> R)`, `Y : Axis -> Site -> (Config -> Link)`, `E`, and `dust` (Perfect/Blunt.lean) is `sum_b (difference_b J_{b a}) - aroma p R (Y_a)`, the shape of v3's `sum_a nabla_a J_ab - DS[Y_b]`. I did not trace `inheritJ` to a final theorem.

## Claim 5. CONFIRMED: no Lean counterpart of `W_a = W_s - d_f E R W_s`

Searched: every occurrence of `fixRoot` (32 files; every matching line was read, not every file in full), every use of `extracted` and `straighten`, all matrices typed fine sites x coarse sites, all products `probe _ * X`, and comment words (cardinal / partition of unity / interpolation).
- All coarse-site -> fine-site extensions are block-constant: `YM.UVNext.PricedKernels.rootAt` (Trees.lean:47), `YM.RG08.duplicateM` (YM/RG08/Gaussian/TreeProjection.lean:55), `sitesCopy` (YM/WilsonBulk/Trees/Map.lean:44), `padMap` (YM/RG08/Line/Hikes.lean:18). No smooth cardinal extension `E` exists.
- No declaration isolates `W - d * E * R * W`. The combination occurs only inside `straighten` / `extracted` together with the tree-path potential.
- The only matrix proved to satisfy the rooted identity `probe * X = 1 - b^-1 K_c` is `extracted` (`stationed`). For the input `W` only `mean * W = ...` is stated.
- What Lean does instead of `W_a`:
  (a) Joint variables (fine configuration, coarse-site gauge), `YM.Stationary.Joint G c f = Config G f x Coats G c` (YM/Next/STATIONARY/Joint/Chart.lean:229). `YM.Push.Loops.graft G S W = graph G W (fixRoot S * W)` (Column.lean:50) is the pair (`W_s v`, `R W_s v`); `centered_graph` (:117) proves `graft = graph (extracted) 0 + (joint gauge generator of straighten)`. The `R W_s` part is carried as a coarse gauge variable, not subtracted from the fine field.
  (b) `YM.Stationary.liftedUp F W rho x = wages S (salute F W x) 1 (encamp F rho x)` (YM/Next/STATIONARY/Joint/Regulator.lean:566-568), a fine gauge transform of the forest-chart field by `exp(straighten W x)`; `YM.Trace.Perfect.smooth_plan` (Perfect/Equate.lean:15): its fine part has derivative `uniformM W`, i.e. the input `W` itself.
  (c) `YM.Trace.Perfect.fleece W D x = W - d_{0,f}(gaugePad W x D)` (Perfect/GaugeFoot.lean:85-86), a fine-gradient modification of `W` by a clamped linear potential with slope `W(x, .)` centred at a fine site `x` (removes the value of `W` at `x`); `first_fresh` (Equate.lean:31). It is not `d E R W`.
- Decay bounds: `YM.UVNext.PricedKernels.extract_price` (Trees.lean:116): if `A` has weighted row bound `C/L` then `extracted S F A` has bound `(1 + dC*hikeC) * C` at the same weight, for every forest (order 1, no `L^-1`, no difference bounds). Difference bounds `C / L^(1+r)` are stated for the stencil `A0` itself: `YM.Precision.Towers.Deep` (Stacks.lean:111), `Carrier.priced` (YM/Planned/PRIMARY_INTEGRAL_295/Carrier.lean:131, orders `<= j-2`), `Slide.shade` (orders `<= 3`).

## Claim 6. Lean counterpart located; operator is the input `W` (= `W_s`), reached from `W_F` by a gauge transformation

Location: `YM/TraceExtension/Perfect/` (Desktop, Equate, Gist, Zinnia, Ether, Eureka, GaugeFoot, Badge, Blunt).
- Substitution: `inheritJ` / `inheritY` use the forest-chart field (tangent `extracted` = `W_F`).
- Replacement: `YM.Trace.Perfect.colors` (Equate.lean:68): for `J` with `Cleric J` (analytic and invariant under fine gauge families, `Dresses`), `inheritJ F rho J o input = J o input o content o (fresh F rho W m).1` near 0, where `fresh` has first derivative `fleece W (L+1) m` (`first_fresh`). `port` (:79) is the vector version. So gauge invariance is what permits the replacement, as v3 says, but the replacement operator is `W_s` (or `W_s` minus a local linear gauge), not `W_a`.
- Moment preservation: `YM.Trace.Perfect.crossing_step` (Zinnia.lean:56) and `Slide.smooth_cost` (Gist.lean:44). Hypotheses on the operator, all on the stencil `A` with `U` a joint germ whose fine part has derivative `uniformM (installed ratio A)`:
  1. translation covariance: built in, `installed` of a `Cross L` stencil (depends on residue and offset only);
  2. exponential decay: `(A w).strip eta C` (`YM.Bloch.Row.strip`, weight `exp(eta * size z)`, YM/CellFourier/Circulant.lean:26);
  3. polynomial preservation: `YM.Trace.Perfect.Ether A` (Perfect/Ether.lean:34): `sum_z A(0,i) j z = delta_ij / L`, and for the test polynomials `1`, `x_i`, `(x_i + x_j)^2` the row at residue `x` applied to the polynomial equals the residue-0 row applied to the polynomial shifted by `x/L`; this is v3 (ch17:polynomial-response) in `17-marked-trace-rates.tex`;
  4. in `Slide` (Gist.lean:9): difference bounds `advanceC k l` with `strip alpha (V / L^(1+|l|))` for `|l| <= 3`, = v3 `|nabla_f^r W| <= C L^(-1-r), r <= 3`, but stated for the stencil `W_s`;
  5. the tested functional has `fderiv (H w) 0 = 0` (v3: "the defect has zero first field derivative").
  Conclusion: `Stoke ... (L^-b * B) b` from `Stoke ... B b` (vanishing of polynomial-probe coefficients of total degree below `b`, with gain `L^-b`). `Stoke` was not read.
- Alias amplitudes: the identity `K_f(k_l(p)) N_l(p) = A_l(p) K_c(p)` exists as `YM.Next.Free.Flight.genuine_alias` (YM/Next/FREE_KERNELS/ZeroAlias.lean:53) and normalised as `Flight.scaled_tri` (Primal.lean:32): `rotor 1 k wing q * (L^-1 pilot k P p l) = (L^-3 flux P 1 q) * rotor 1 k land p`, `q = aliasAt p l = p/L + mon l`, `rotor = mirage 1 * pulse * signal 1` (symbol of `d_1^* H d_1`), `pilot` the alias amplitude of `A0` (`Flight.duo`, `A0 := meshBook (pilot k) 1 [] P`). It is used to prove `Inputs` for `installed A0` (`Flight.tangent`). In `TraceExtension/Perfect` no alias amplitude is used (the only match for "alias" is the header of Eureka.lean: "Reproduction replaces aliases before reading polynomial probes"); the v3 argument "project `N_l` off the gradient, order `|p|^2` at non-principal aliases, double zero of `K_0`" has no located counterpart there. `Ether` is derived from Fourier data at `Ether.witty` (Ether.lean:38) via `Carrier.origin_money` and `Carrier.pure_moment` (YM/Planned/PRIMARY_INTEGRAL_295/Bijets.lean:37, :99; moments of degree `< j`); those proofs were not read.
- `pilot = ahead + mask 1 (gains) * signal L 0 (alias) * sluice` (YM/Next/FREE_KERNELS/Pilot.lean:46): a principal part plus a fine-gradient part, the shape of v3's `A_l = D_l F_{1,l}^* R + e_l x_l pi`. Term-by-term equality with v3 was not checked (`gains` is per-axis, v3's `e_l` is scalar).

## Claim 7. Lean does not require a translation-invariant forest

`YM.Tree.Forest g` (YM/Tree/Pines.lean:24): `up : Site f -> Step`, `height : Site f -> N`, `bound`, `rise`, `stays` (the step from a non-root site stays in its block and lowers height). No periodicity field. File header: "Chosen independently per physical coarse site in applications."
`extracted`, `stays`, `stationed`, `action`, `Guessed`, `YM.Bid.F04`, `extract_price`, `Lot.wood` all take an arbitrary `F : Forest S.ratio`; the kinetic data require `Critical` and `Guessed` for all forests (YM/PCalc/Loop.lean:103-107). `YM.Bid.F05` (YM/Bid/Station.lean:94) states independence of the stationary value from the forest.
Translation-invariant forests exist as special constructions: `YM.RG08.Repeated L` with `Repeated.forest` (YM/RG08/Gaussian/Repeated.lean:16, :25; `up` depends on the residue only), `Line.green` (YM/RG08/Line/Pine.lean:53), `spreadForest` (YM/WilsonBulk/Trees/Repeat.lean:24), used in RG08 / WilsonBulk Gaussian computations. Which theorems need `Repeated` was not determined.

## Not checked

- `Stoke`, `stampA`, `Teller`, `Cleric`-side lemmas beyond their statements; the end theorem consuming `crossing_step`.
- Whether every `Slide` is instantiated with `k = A0` of the kinetic towers (seen: `Native.lean:27` `Guessed F (installed K.ratio E!) ...` via `Work.F04.tangent`; not expanded).
- Proofs (only statements) of `genuine_alias`, `pure_moment`, `origin_money`, `Carrier.priced`, `extract_price`.
- Equality of Lean's `pilot` with v3's `A_l` term by term; equality of Lean's `mean` weights with v3's `M`.
- The 57 files mentioning `Precision.probe`-like patterns were only scanned through the product grep, not opened.
- Martin and Scott texts were not consulted.
