# Audit: flagged statements outside chapters 7, 9–11 (forest) and 17

Report of a read-only agent, 26 November 2026, as handed back (condensed). Worktree at `e53484a2`. Nothing was changed; no Lean command was run. The points come from the lists of noticed statements in `audit/dictionary-verification/part1–6.md`. "Martin" = `manuscript/existence/`, "Scott" = `manuscript/HumanizeYM_v2/`.

| Point | Verdict |
|---|---|
| C1 "Admissible periods" | resolved by sources; wording |
| C2 Three axial gauges | not a gap (as far as read) |
| C3 `B_m²` at 13ba:127 | resolved by sources; wording |
| C4 Single-stage condition at 14lc:23 | resolved by sources; missing reference |
| C5 Order of the bidegree | not a gap |
| C6 Failed-cutoff factor | not a gap; one ambiguous antecedent |
| C7 One symbol, several objects | no wrong formula; but see `b` under "New" |
| C8 "Wrapping around the torus" | resolved by sources; definition missing in v3 |
| C9 5:1019 | not a gap |
| C10 Formulas not added | not a gap, except a missing reference at 9s:258 |
| C11 Forest prescription 18:398–421 | resolved by sources; "not used" needs precision |
| C12 `C_st`, principal/complementary bounds, 10:622–626 | resolved by sources; undefined in v3 |

## C1. "Admissible periods" in the main theorem

**v3.** MT:14–15 "admissible periods in continuum units tending to infinity"; MT:19–20 "At each fixed admissible period the correlations converge along the full sequence"; 19:20–21; 10:193–197 chooses `M` "large enough that the lattice side `R_p/a_m` meets the required lower bound at every step of this plateau", `R_p = 4(M+p+1)`; 1:359–361: a test function "is admissible at volume `p` if its support is contained in `((-R_p/2,R_p/2)^4)^n`".

**Martin.** `common-scale-selection.tex:115–119`: "Choose an integer `M` at least … the required minimum physical period. Use periods `P_p=4(M+p+1)`." The periods are not called admissible.

**Scott.** `part1/02-definitions.tex:90`: a separated test "is *p-admissible*, or supported inside volume `p`, if its support lies in `((-L_p/2,L_p/2)^4)^n`". The main theorem (`part1/03-main-theorem.tex:9`) asks only `L_p ↑ ∞`.

**Lean.** `YangMills.WilsonFamily` (`PublicWilson.lean:35–46`, definition read): `period : ℕ → ℕ+` with `periodStrict`, no other condition. `YangMills.WilsonFamily.suitable` (`:75–77`, definition read): the support of the test lies in the box of side `period`. `YangMills.WilsonFamily.Converges` (`:85–90`, definition read). `YangMills.JointExistence` (`ChallengeSpec.lean:186–188`, statement read): the family is chosen existentially. `YangMills.wilsonFamily` (`WilsonBridge.lean:20–22`, definition read).

**Finding.** "Admissible" merges membership in the chosen sequence `R_p` with admissibility of a test function at volume `p`. Since the theorem asserts that a choice exists, no hypothesis is missing. MT:19 should say "for every period of the chosen sequence, for test functions admissible at that period".

**Not checked.** Martin's "required minimum physical period"; Lean's internal `C.S.period`.

## C2. Three axial gauges

5:937 and 5:1005 distinguish the block axial gauge from the axial gauge of chapter 4. 9s:173–176 uses a coordinate axial gauge on the cube, needing only that the holonomy of a full coordinate cycle is one for reflected periodic extensions (Scott `part2/D-section.tex:417`, same argument). 6:339–340, 969–971 use a coarse axial gauge on a box for link bounds polynomial in `B`. No step found that applies a property of one gauge to another. Weak point: 6:970 "The local axial gauge construction bounds `‖h‖_∞ ≤ CB^a t_f`" names no lemma; Lemma `ch04:frame-lemma` gives a summed bound (4:74–76). Not checked: 11:1208, 1766; Lean; Martin.

## C3. `B_m²` at 13ba:127

13ba:127–129: "Open the centered cells at `m` with spacing at least `B_m^2`. This spacing persists because `L_i ≥ 3` and the adjacent support radii satisfy the schedule". The use at 13ba:131–132 needs spacing `B_{i+1}^2` at scale `i+1` (11:482–486); the schedule gives `B_{i+1}^2 ≤ 2B_i^2` (13sb:20, 10:166). Martin `centered-geometry-producer.tex:7, 21–33` and `fullmesh-correlation-cauchy.tex:165, 195`; Scott `part1/04-strategy.tex:126`. Both forms are right; what persists is "spacing at least `B_i^2` at scale `i`", by induction, not the number `B_m^2` as the sentence says.

## C4. 14lc:23 and 13ba:258–261

14lc:23: "At a comparison scale `k` whose comparison window lies in a single stage", with no reference. The condition is at 10:185–189 ("For comparison estimates requiring an interval of scales `w_j(s)=o(s)` around one scale of stage `j`, increase `c_j` … At `k=k_j` the whole prescribed interval stays on the same plateau"); the windows are those of 11R:216–218 and 11:1965–1968. Martin `common-scale-selection.tex:100–113`. The condition of 10:122–126 and 13ba:257–262 is a different one (minimum starting scale) and is stated and used correctly. Fix: at 14lc:23 take `k = k_j`, cite 10:185–189, name the window. Not checked: whether every window used in chapter 14 is among these.

## C5. Order of the bidegree

2:79 defines the bidegree as the pair `(w_i,f_i)`, a label. 2e:34–36 orders "(factor count, scaling dimension) … in lexicographic order". The one later use (11E:174, "`R_d−I` never lowers factor count") needs factor count first, as does Scott `part2/A-section.tex:169`. No formula depends on the written order of the pair.

## C6. Failed-cutoff factor

Under the definition at 11:1476 (the term `−(1−χ)Rz_I`), 11:1491, 11:1500 (`p_f ≤ H^{1/8}C_*R_{e+1}`), 11:1523–1526 and 11:1932 are correct; 11:1500 would be false for the whole factor. Martin `allarity-marked-propagation.tex:2313–2330` uses the same sense. The antecedent of "such a factor" at 11:1491 is the whole factor of 11:1490; write "such a failed-cutoff factor `−(1−χ)Rz_I`".

## C7. One symbol, several objects

- `c_d`: a norm constant (11:1286–1287, 1298) and an exponent (11:1238, 1363, 1842–1843, 1925–1926), in the same section; no formula combines them.
- `T`: the one-step localization map (11:373–385), the common localization map (11:1292–1352), a number at 11:1605; also the induced curvature map at 9s:189.
- `𝓡_m`: the chessboard seminorm (11:822, 949; 11E:67) and the space of remainder arrays (12:70).
- `M_G/R_G` (11:381, 447) and `I_G/J_G` (12:90–92) are the same objects under two names.

No wrong formula found.

## C8. "Wrapping around the torus"

Used undefined at 4:627, 642; 9:220, 463, 472, 497; 11:399, 441, 1130; 13ba:272; 17m:324, 331. The bound at 17m:331 ("covering number at least `N_per/[10(2B_k+1)] − 1`") can be derived only from the criterion with the factor 10.

**Martin.** `local-splitting.tex:46–47`: "a support `X` is nonwrapping at `o` precisely when `10 dist(x,o) < n` for every `x ∈ X`, where `n` is the lattice side".
**Scott.** `part2/D-section.tex:19`.
**Lean.** `YM.Lattice.Nonwrapping` (`YM/Lattice/Support.lean:80`, definition read): `∀ x ∈ X, 10 * separation x o < n.val`; `YM.Lattice.separation` (`YM/Lattice/Site.lean:81`, definition read); `YM.Trace.Physicalv2.wraps` (`YM/Trace/Physicalv2/Germ.lean:50`, definition read), matching 17m:331.

Fix: state the definition once, near 4:627, and refer to it.

## C9. 5:1019

The sentence is correct: the proof at 4:361–365 covers both branches of the local gauge transformation ("Thus both branches … obey the same bound"); Scott `part2/B-section.tex:996` says "on either branch". Inference of the auditor: the discrepancy at the root is a single term of the sum (from 4:43, 5:917).

## C10. Formulas not added

- 9s:258–259 ("`d_c` the prescribed coarse quantum contribution, including the renormalization terms"): the claim that quadratic matching bounds `D²W(0)` needs `d_c` to be the matched term of chapter 7; no reference says so (nor does Martin `pure-action-small-field.tex:104–107`). Missing reference.
- 11:1343; 9:147; 7:427; 7:599: complete.
- 7:195: exchange symmetry is a hypothesis of Lemma `ch07:unique`; at its application (7:1162) it is not verified in the text. Inference of the auditor: it holds because the symbol comes from a quadratic action.
- 6:1018 ("is zero by definition"): the convention is at 6:1340–1346, later; Martin `gaussian-warnings.tex:206–208` states it. A forward reference would do.

## C11. The forest prescription, 18:398–421

**Lean formalizes the recursion** (`YM/Contacts/Score/Formula.lean`, definitions read): `YM.Contacts.Normal.System.depth`, `subtractAt`, `cumulant`. Not opened: `receding`, `reshape`, `taylor`, `instructionScore`. `YM.Contacts.Solstice.MultipleLight` (structure read), `YM.Contacts.Solstice.celestial` (statement read), `provided` (proof read), `global_charge` (not read).

**Dependence of the final theorem.** `YangMills.JointExistence` (`ChallengeSpec.lean:186–188`) has no contact clause. `YangMills.jointExistence` (`Solution.lean`, proof read) calls `YangMills.constructed` and discards the remaining components. `constructed` (`Construction.lean:31–40`, proof read) calls `YM.Nonperturbative.existence` (`Headlines.lean:19–25`), which calls `continuum_with_position_tests` (`Continuum.lean:27–48`, proof read); the contacts come separately from `contacts_on` (`:13–23`), which calls `Contacts.Solstice.provided`. So the four public conclusions are derived without the forest prescription, but it lies in the dependency closure of the proof term, and `YangMills.constructed` proves a contact extension by the forest prescription. v3 proves its contact clause (main theorem, iii) by the different pair-weighted subtraction.

**Fix.** "formalized, and used in the formal contact theorem, but not needed for the conclusions of the public formal statement nor for this book's proof".

## C12. `C_st` and the principal and complementary regular bounds, 10:622–626

10:621–630: "`𝒩(H(t)) ≤ 3ε C_st x^{-11/10} + O(x^{-23/20+o(1)})` … the fixed fraction `ε ≤ 1/16` … allotted to the principal regular bound (and `2ε` to the complementary one) … This is the small remainder estimate of Chapter 9". `C_st` occurs nowhere else in v3; "complementary" does not occur in chapter 9.

**Martin.** `selected-nonlinear-offering.tex:21–33` ("The regular principal bound is at most `E/16`, the complementary regular bound at most `2E/16` … `E=c_st δ_E(x_0)`"); `background-test-prices.tex:84–105` ("`C_st>0` is the fixed stage conversion constant"; the proof "uses the principal and complementary bounds only through their sum").

**Missing in v3.** The definitions of `C_st` and of the two bounds in terms of chapter 9's quantities, and Martin's remark that the one-step proof uses the two bounds only through their sum. Inference of the auditor: in v3's normalization `C_st = 1`; "principal" is the inherited part of 9:235; "complementary" presumably the new terms of 9:374–379.

## New

1. **`b` in Section ch11:common-extraction** is the patch radius `b = 8B`, growing with the scale (11:1152, 1210, 1222), and the fixed magnification exponent (11:1238, 1352 `ρ = H^b`, 1363, 1843 "Choose `b` larger than `c_d+3`", 1920). With `b = 8B`, "choose `D > bd + c_d + v` before the stage orders" (11:1238) would be impossible, so the two must be separated.
2. Lean proves the contact extension by the forest prescription; v3 by the pair-weighted one (C11).
3. 1:202 requires periods to be multiples of four; Lean's public `WilsonFamily` does not. Harmless.

## Not examined

11:283–291 (single `t_C` against the product cited at 11:1662); 9s:140; 9:230–232; 11R:358–360.
