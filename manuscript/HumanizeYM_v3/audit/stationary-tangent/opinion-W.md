# Opinion: which operator is the unnamed `W` (ch. 17) and `\mathcal U_F` (ch. 6)?

Paths: v3 = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/; Martin = /Users/mgubi/ym-terminology/manuscript/existence/; Scott = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v2/part2/.
Read-only; nothing edited. "States" = quoted from the text; "Inferred" = my own deduction.

## 0. What chapter 5 defines (stated)

- `W_s` (05:1084-1088): "the straight-average transport already constructed in Section ch05:transports", with
  `K_f W_s = M^* K_c`, `M W_s = I - b^{-1}K_c` (M = straight average). In ch05:transports itself the same operator is
  written as a bare `W` (05:527-535: "Denote the resulting operators by W and T ... QW=I-b^{-1}d^*Hd ... Here Q is the
  straight averaging operator").
- `W_a = W_s - d_{0,f} E R W_s` (05:1107-1109), with `\mathcal Q W_a = I - b^{-1}K_c`, `K_f W_a = \mathcal Q^* K_c`,
  `d_1 W_a = d_1 W_s` (05:1112-1116) and the fine-difference bound `|∇^r W_a| <= C L^{-1-r} e^{-c d}` (05:1128-1133).
- `W_F` (05:1139-1149): `W_a v` minus "the unique gradient d_{0,f}φ whose site potential is zero at every block root
  and makes all tree edges vanish"; "the unique minimizer in the forest slice"; and
  `rep v + ι_F Dρ(0) v = W_F v` (ch05:stationary-tangent). "The smooth representative W_a and the forest representative
  W_F are distinct. Estimate (actual-bridge) is asserted for W_a, not for tree coordinates" (05:1151-1153).

Inferred properties (short proofs):
- `K_f W = \mathcal Q^* K_c` holds for all three (K_f kills gradients; `\mathcal Q^*K_c = M^*K_c` since `K_c d_{0,c}=0`,
  as 05:1090-1092 says).
- `\mathcal Q W = I - b^{-1}K_c` (rooted/gauge-covariant average) holds for `W_a` and `W_F`, NOT for `W_s`
  (`\mathcal Q W_s = I - b^{-1}K_c + d_{0,c} R W_s`).
- "Derivative of the nonlinear stationary graph in the forest chart": `W_F` only (05:1146-1149; also 09:188-191).
- Fine-difference bounds `L^{-1-r}`: `W_s` and `W_a` (05:1128-1136). Explicitly not asserted for `W_F`.
- Exact polynomial preservation: proved in v3 only for `W_s` (17-marked-trace-rates:242, eq. ch17:polynomial-response).
  Not claimed for `W_a`; I see no reason it holds beyond constants (the cardinal extension `E` reproduces constants,
  05:1118-1120, not higher polynomials). `W_F` certainly does not (it vanishes on tree edges).
- Coarse-translation covariance (needed for "alias amplitudes N_l"): `W_s`, `W_a` yes. `W_F` only if the block trees are
  translates of one tree. v3 does not impose this (05:911-913 "in each centered block ... a spanning tree"; 05:1041,
  1327 "uniform in the allowed trees"); Scott does (D-section:1197 "Choose one reference tree and translate it").
- Exponential locality: `W_s`, `W_a` stated. `W_F`: true at fixed L (bounded-range tree sums of `W_a`; this is what
  06:971-974 says) but not recorded in ch. 5.
- Principal amplitude `N_0(0)=L^{-1}I`: true for all three (for `W_F` with translated trees: on constant v, `W_F v = rep v`,
  block mean `L^{-1}v`).

## 1. The `W` of 17-current-contraction.tex:46-53

Text: "Let W be the actual stationary tangent from coarse link variables to fine link variables ... The first derivative
of the nonlinear stationary substitution is this W ... Fine gauge changes of W have no effect on this quadratic
calculation by the Ward identities of E_b" (17c:48-53); "The actual tangent may be replaced by the smooth representative
W_a because the quadratic Ward identities kill its gradient correction" (17c:112-113).

Conclusion: the text is not determinate as a symbol, but the only reading under which every sentence of that file is
literally true is **W = the gauge class of the stationary tangent, with W_F as the literal derivative** — i.e. `W_F`,
immediately traded for `W_a`. It is not `W_s`.

Property by property:
- "first derivative of the nonlinear stationary substitution is this W" (17c:49-50): literally `W_F` (05:1148, 09:188-189
  "Its tangent is the forest-coordinate lift W_F"). For `W_a` or `W_s` it is true only modulo a fine gradient
  (which 17c:51-53 says is irrelevant).
- Alias identity `K_f N_l = A_l K_c` with `A_l` from "the adjoint of the gauge-covariant block average" (17c:55-60): all three.
- "N_l is the alias amplitude of W", "principal amplitude is analytic by the exponential locality of W" (17c:59, 66):
  fine for `W_a`/`W_s`; for `W_F` needs translated trees and a locality statement ch. 5 does not make.
- "may be replaced by the smooth representative W_a" (17c:112): presupposes W != W_a. With W = W_F it is correct
  (difference `d_0 φ`). With W = W_a it is vacuous.
- Bounds (17c:114-117, 189, 339, 364) are all explicitly attached to `W_a`, never to bare `W`. Correct per ch. 5.
- Polynomial preservation is not invoked in 17c (only Taylor order of transverse amplitudes); it is invoked in
  17-marked-trace-rates, for `W_s`.

Consistency across v3 — the phrase "actual (stationary) tangent" is used in two incompatible senses:
- Sense A (a specific operator, `W_a`): 07:574 "The actual stationary tangent is W_a ...; its forest representative is
  W_F"; 17-marked-trace-rates:263-264 "The actual tangent is W_a=W_s-d_fERW_s".
- Sense B (the tangent of the graph / its gauge class, of which `W_a` is one representative): 05:1081 title, 05:1234
  "W_a is the smooth representative of the actual stationary tangent, whereas W_F is its representative in the forest
  coordinates"; 17c:112; 09:188-191; 07:1114-1117 ("the tangent of the actual block average differs from this
  representative by a fine gradient ... even if the tree-gauge representative itself has poor difference bounds").
- If Sense A is imposed on 17c:48 (W = W_a), then 17c:49-50 is false as an equality (true only up to fine gauge) and
  17c:112 says "W_a may be replaced by W_a". No estimate breaks; the mathematics is unaffected because every use is
  gauge-invariant or explicitly through `W_a`.
- 17-marked-trace-rates:190-205, 260-266: "actual response" is unnamed in the proposition; the proof uses `W_s`
  (polynomial response) then `W_a` via gauge invariance. Mathematically sound; it never mentions `W_F`, though the same
  gauge argument covers it.

Earlier texts: Scott has the same three objects under other names: `W_s` centred (B-section:367-372), `W_r = W_0 =
W_s - d_f I_ℓ(F_m W_s)` rooted (B:388-390) = v3 `W_a`, and the axial tangent `W_ax` = "the tree representative of W_r"
(B:529, B:781) = v3 `W_F`. Scott C-section:237 does the folding with `W_r`, noting it differs from `W_s` by a fine
gradient. WARNING: Scott's own symbol `W_F` (B:365, `C_f M^* C_c^{-1}`) is a different operator from v3's `W_F`.
Martin (selected-stationary-linear-data.tex:44-93) has `W` = installed smooth matrix and `E = W + d_0 K` = tree tangent
("Its fine tangent is not W itself"); I found no Martin counterpart of the 17c subsection by phrase search.

## 2. `\mathcal U_F` in 06-large-fields.tex:951-955, 970-978

Conclusion: `\mathcal U_F = W_F`, linear. High confidence.
- v3: "Let a=\mathcal U_F h be the stationary fine response to a coarse logarithmic field h" (06:953); the statement
  calls it "its stationary tree response" (06:947); "The tree-straightened response has a bounded row norm at fixed L:
  the exponentially decaying stationary kernel is summed absolutely, and its straightening correction is a sum along
  finitely many tree edges per block. Thus ... v=\mathcal U_Fh-rep h is zero on the tree" (06:971-977).
  Linear rows `X_f^lin(a)`, a row-norm bound, and "zero on the tree" single out `W_F`: `W_F v - rep v = ι_F Dρ(0)v`
  (05:1148), and neither `W_a` nor `W_s` vanishes on tree edges.
- The norm equality `|p|^2=|w|^2` (06:956-957) uses `Z^lin = sqrt(b)(v - Qa)` with `T^*d_1 = d_1 \mathcal Q` (06:131, 159),
  i.e. the rooted average; that identity holds for `W_F` and `W_a`, not `W_s`.
- Martin, local-mean.tex:12-19: "Write \mathcal U_F b for the fine stationary field in tree coordinates with coarse
  input b. It is the tree-straightened installed linear response. ... v_F(b)=\mathcal U_F b-\bar b ... On every forest
  bond this difference is zero"; eq. (mean-diagonal) with "Q the rooted linear predictor" (local-mean:20-27);
  actual-reader-guarded-curvature.tex:198-199 "The stationary linear fine response is ℓ=\mathcal U_F v".
  So Martin says explicitly it is linear. It equals Martin's `E`, by inference (same description), not by a stated equation.
- Residual doubt: only that v3 never writes the equation `\mathcal U_F = W_F`. Note v3 09:188 uses `\mathcal U(x)` for the
  NONLINEAR stationary field, so the undefined `\mathcal U_F` invites a wrong (nonlinear) reading.

## 3. 09:188-195 and 11:642-650

- 09:188-191: "Let \mathcal U(x)=D_x(ρ(x)) be the physical stationary fine field. Its tangent is the forest-coordinate
  lift W_F ... Its curl agrees with that of the smooth actual lift W_a", then uses `d_1 W_a = H_f^{-1}TH_c d_1`.
  Correct and consistent with ch. 5 (Sense B). 09:230 "the actual stationary tangent" is generic.
- 11:642-646: "For the actual stationary forest response W ... KW=Q^*K', AW=bQ^*, DW=JD'", `A=K+bQ^*Q`, Q "the rooted
  gauge-covariant block average derivative" (11:626-628). `AW=bQ^*` requires `QW=I-b^{-1}K'` with the rooted Q: true for
  `W_F` and `W_a`, FALSE for `W_s`. The words "forest response" give `W_F`; indeed (inferred) `bXQ^* = \mathcal P W = W_F`
  exactly. Only `DXbQ^*=DW` is used, so `W_F` or `W_a` both work. This `W` is a third bare-`W` usage (ch. 5 transports:
  `W_s`; ch. 11: `W_F`; ch. 17c: gauge class).

## 4. Minimal changes

(a) Ch. 6: define the symbol. E.g. at 06:953: "Let `a = W_F h` be the stationary fine response (ch05:stationary-tangent)"
    and replace `\mathcal U_F` by `W_F` at 06:976. Safe: every statement in that proof (linear rows, rooted norm
    identity, zero on tree, row norm bounded at fixed L — also directly from `‖Dρ‖<=C_ρ`, 05:1329-1331) holds for `W_F`.
    No further change needed there.
(b) 17c:48. Do NOT write `W_s`. Writing `W_a` or `W_F` alone each needs a second edit:
    - `W = W_F`: 17c:49-53 and 112 become exactly right, but 17c:59 ("alias amplitude of W") and 17c:66 ("exponential
      locality of W") then rely on translated trees and on locality of `W_F`, neither stated in ch. 5; and 07:574 /
      17mtr:263 ("The actual tangent is W_a") would contradict it.
    - `W = W_a`: aliases, locality, bounds all covered by 05:1112-1133, but 17c:49-50 must say "up to a fine gauge
      change" and 17c:112 must lose "may be replaced by".
    Recommended wording (two-step, removes the ambiguity): at 17c:48-53, "The first derivative of the nonlinear
    stationary substitution is the forest representative `W_F` of (ch05:stationary-tangent). It differs from the smooth
    representative `W_a` by a fine gradient, which the Ward identities of `E_b` annihilate; we therefore compute with
    `W=W_a`." Then 17c:112-113 becomes "Recall `W=W_a`; its fine-difference bounds are". Nothing else in 17c changes
    (17c:189, 339, 364 already say `W_a`).
(c) For global consistency fix the phrase once: either reword 07:574 and 17mtr:263 to "the smooth representative of the
    actual stationary tangent is `W_a`" (Sense B, matching 05:1234), or adopt Sense A everywhere and reword 17c:112.
    Sense B needs fewer edits. Optionally name `W_F` at 11:642.

## Not read / limits

- Not read: the forbidden audit/terminology files and blueprint/notation.md; the Lean tree (not needed); most of Martin
  (only local-mean, actual-reader-guarded-curvature:190-210, selected-stationary-linear-data:1-140,
  inherited-loop-transport:150-245); Scott outside the quoted B/C/D lines; v3 chapters other than the cited ranges.
- Not verified: the full derivation of ch05:transports (that the bare `W` there has exactly the `W_s` identities — taken
  from 05:1084-1088); that `R` and `E` are coarse-translation covariant (assumed from their stencil definitions).
- Side observation, not pursued: 07:882 calls `(u, W_a u, r_u)` "the smooth centered representative"; in Scott the
  centred tangent is `(v, W_s v, 0)` and the rooted one is `(v, W_r v, -F_m W_r v)` (C-section:161). Worth a separate check.
