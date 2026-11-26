# Independent review of `statements-elsewhere.md`

Report of a reviewing agent (not the auditor), 26 November 2026, as handed back (condensed). Read at `7d23f9e2`. Nothing was edited; no Lean command was run.

| Point | Auditor | Review |
|---|---|---|
| `b` in chapter 11 (new) | two meanings; 11:1238 impossible with `b = 8B` | strengthened |
| C1 | wording | confirmed (also 1:373, 12:375) |
| C2 | not a gap | confirmed with corrections: a fourth axial gauge in chapter 11 uses an unstated lemma |
| C3 | wording | confirmed |
| C4 | missing reference | confirmed |
| C5 | not a gap | confirmed |
| C6 | not a gap | confirmed |
| C7 | no wrong formula | confirmed; `B` is overloaded too |
| C8 | definition missing | confirmed with corrections |
| C9 | not a gap | confirmed |
| C10 | not a gap except 9s:258 | confirmed with a correction at 6:1018 |
| C11 | "not used" needs precision | confirmed, strengthened |
| C12 | undefined in v3 | confirmed; the auditor's `C_st = 1` is wrong |

## Errors of fact in the audit report

- C12: "`C_st = 1` in v3's normalization" is wrong; and "complementary = the new terms of 9:374–379" contradicts Martin.
- C10: the convention "zero by definition" is not at 6:1340–1346; v3 has none.
- C8: Lean's `wraps` does not literally match 17m:331–336; 9f:756 is missing from the list of uses.
- C2: 6:970 is not a weak point (a supremum is bounded by the sum, 6:340).
- C11: the forest prescription is in the *statement* of `YangMills.constructed`, not only in a proof term.
- `b`: `ρ = H^b` is at 11:1350; the late use is at 11:1921. C6: the definition is at 11:1475.

## `b` in Section ch11:common-extraction

Patch radius `b = 8B` (with `B = M²`, `M = ⌈(log s)²⌉`): 11:1152, 1163, 1177, 1184, 1196, 1199, 1210, 1222, 1262–1263. Fixed exponent: 11:1238 ("choose `D > bd + c_d + v` before the stage orders"), 1350, 1363, 1760 ("`b ≥ 6`"), 1806, 1812, 1843, 1850, 1921, 1953, 1955. `D` is fixed before `s`, so with `b = 8B → ∞` the condition at 11:1238 cannot hold. The section never separates the two.

**Found in addition.** Martin `existence/actual-rank-purchases.tex:1029–1031`: "Here the amplification exponent `b` is the one in the calibration equation, not the patch radius. It is chosen before `D` and before the stage's derivative order." v3 dropped this sentence. Proposition `ch11:n-mark-comparison` (11:2054–2059) fixes "finitely many magnification exponents `b_1,…,b_t`". A defect of notation that makes 11:1238 false as written, not a missing argument. Lean not checked.

## C11. The forest prescription, 18:398–421

The Lean definitions (`YM.Contacts.Normal.System.depth`, `subtractAt`, `cumulant`, `Lean/YM/Contacts/Score/Formula.lean`, read) agree with 18:399–403. `YangMills.jointExistence` (`Lean/Solution.lean`, proof read) keeps only `core` from `YangMills.constructed` (`Lean/Construction.lean`, statement and proof read).

**Found in addition.** `Lean/verification/declaration-usage.tsv` gives the chain `subtractAt` → `cumulant` → `punctured` → `candidate` → `vote` → `election` → `YM.Contacts.Harvest.Route.windings` → `Solstice.Resolution` → `Solstice.MultipleLight` → `celestial`. The prescription enters through the type `MultipleLight`, which occurs in the statements of `continuum_with_position_tests` and `YangMills.constructed`. The roots explored before `celestial` (`YM.Independent.Core.point` and others) do not reach `subtractAt`.

So "not used in the main result" (18:419) is false for the contact clause as Lean proves it, and true only for the conclusions of the public statement `JointExistence`. Not checked: `Core.of_receipts`; `global_charge`.

## C12. `C_st` and the two regular bounds, 10:621–630

In Martin `c_st` is `c^reset` (`selected-nonlinear-offering.tex:30–31`), defined at `physical-reset-reorganization.tex:420–424` as `1/(64(1+B^reset))`. v3's analogue is the stage constant `c_j^pre` in `H_pre = θ c_j^pre ε_m^reg` (9:420–423; chosen at 9:614–616 "small enough to absorb the terms linear in `H_pre`") — inference of the reviewer. Martin `selected-nonlinear-offering.tex:274–276`: "terms retained from the incoming regular array remain in the complementary part"; the identification of "principal" and "complementary" in v3's terms is unresolved. No mathematical gap: 10:644 needs only that `C_st` is fixed before the bound on the reference coupling.

## C8. "Wrapping"

Confirmed that v3 has no definition. `YM.Trace.Physicalv2.wraps` (`Lean/YM/Trace/Physicalv2/Germ.lean:50`, definition read) is `exp(2e − e·n/(10(4B+2)))`, which agrees with 17m:331–336 (`N/[10(2B+1)] − 1`) only up to a convention. 2:352 and 11:1982–2004 use "wrap" in other senses.

## C1, C3, C4, C5, C6, C7, C9

Confirmed. C1: the same conflation at 1:373 ("admissible fixed volume `p`") and 12:375 ("admissible period cell"). C4: 14lc:107–112 takes `k → ∞` along one sequence, so `k = k_j` suffices. C7: `B` is `M²` at 11:1152, a bound on means at 11:1854, and `H^λ` at 11:1862. C9 not checked: whether the constant rotations of 4:369ff cancel between the two roots of a crossing edge.

## C2. Axial gauges

11:1208–1225 and 11:1766–1786 use a patch axial gauge and rely on two facts v3 states nowhere as a lemma: each link is a product of at most `4b` plaquette holonomies, and `|x−y| ≤ C_G a²/θ`. 4:145–151 gives only a summed form. Martin states and proves both (`actual-rank-purchases.tex:951–971`). No property is transferred between gauges.

## C10

6:1018: v3 has no convention that the cutoff remainders are zero there; 6:1340–1346 imposes conditions on the factor. Martin `gaussian-warnings.tex:206–207` ("Factors inside their compulsory seed region are defined to be zero") supplies it.

## The four items the audit left unexamined

- **11:283–293 against 11:1604, 1662.** Not a gap. 11:276–281 states inflation of each amplitude; the single `t_C` is derived. 11:1604 and 11:1662 cite the label for a product hypothesis that is not stated there; Martin `actual-mixed-marked-compiler.tex:103–113` states it. Only one factor `1/m` per component is used later (11:1625; 11R:371–372).
- **9s:139–147.** Not a gap; the norm of the "fixed closed coordinate ball" is unstated. Martin `stationary-exterior-receipt.tex:88–92`: the supremum ball, whose convexity is used. Not checked: where v3 discharges the Hessian assumption on the ball (9s:141).
- **9:230–232.** Not a gap; the inequality is proved at 6:1295–1311 and should be cited.
- **11R:358–360.** Not a gap; "the finite factor counting the values of the auxiliary index" is the number of index values (Martin `warning-safety.tex:114–118`); v3 defines the weights at 4:217–223 but not the count or "normalized weight" (6:920, 1016).
