# Independent review of `forest-and-insertions.md`

Report of a reviewing agent (not the auditor), 26 November 2026, as handed back (condensed). Read at `7d23f9e2`; chapters and `Lean/` unchanged since `e53484a2`. Nothing was edited; no Lean command was run. IR = `Lean/YM/PhysicalNext/AFTERNOON_INTERACTING_RANK_COMPARISON/`.

| Point | Auditor | Review |
|---|---|---|
| A1 | persists | confirmed with corrections |
| A2 | persists | confirmed with corrections |
| A3 | persists | confirmed with corrections |
| A4 | persists (narrower) | confirmed with corrections |
| A5 | not a gap beyond the Assumption | weakened: 9:521 depends on further unproved items, which v3 lists |
| A6 | not a gap | confirmed |
| A7 | persists | confirmed |
| A8 | one unproved claim persists | confirmed |

## Errors of fact in the audit report

1. A4: "has not been identified with a positive density" is at 10:513–518, not 498–501; it continues "Positivity is required for the histories of densities, not for this algebraic extension of their local comparison formulas."
2. A4: 9:920 states positivity only; the narrow band (17/20–23/20) is defined at 10:403–404.
3. A3: 11R:246 says only "Only the inverse coupling is held constant"; "no reset" is the auditor's paraphrase.
4. A3: "we do not claim that the larger q_n meets that derivative bound" is at 11R:257–258; `h_α` is defined at 11R:204–206.
5. A2: v3 does define the action of lattice isometries on configurations of any lattice (1:186–190).
6. A2: Martin also treats several insertions (`allarity-marked-propagation.tex`), with the matching of the forest measure as a hypothesis.
7. A1: `Sees` is established for the actual integrands in Lean.
8. A5: 9:521 depends on items beyond the Assumption (9f:955–961).

## A2. Hypothesis (H) at 11:335

Quotations accurate. **Found in addition:**
- 1:186–190 defines the action of every affine lattice isometry on configurations ("pulling back oriented paths"); 9f:46–49 gives the lift by one step; 4:256–264 (Proposition `ch04:kernel-properties`) states covariance of the block kernel. So the lift to the cutoff lattice is the iterate of the stated one-step lift. Missing is only the statement that `F_•∘ς^*` means pullback by this iterated lift.
- Martin `allarity-marked-propagation.tex:565–582`: for several insertions the matching of the forest measure for every product is hypothesis (CI)(a); `:1020–1027`: "A singleton identity alone does not establish that property for a product". No equivariance statement in that file.
- Lean: `Voyage` (IR/`Voyage.lean:61`, definition read) maps a family to itself, not to transported insertions; in `Stocking.lean:59` the family of flakes is `Empty`; no instance with insertions found (grep only).

The other two parts of the finding stand: the clause contains a claim about the whole finer history, and locality in the forest for several insertions is assumed. Not checked: where Martin discharges (CI); `Display.inspected`, `Display.impression`.

## A3. Restarted steps

**Found in addition:**
- 11R:191–192 already says that the signed symmetry at the endpoint "requires that the incoming activities be the ones averaged over the forests … and it rests on Assumption ch09:forest-assumption".
- Scott does not have the restart: `part2/E-fixed-level.tex:110` ("the coefficientwise marked attachment induction restarted at level m … Its anchored higher-mode bound and this restart are not yet established in this draft"); `PROOF-STATUS.md:15`.
- Lean covers the endpoint of the restart, not the restarted steps: `Lean/YM/Next/RANK/Rifle.lean` (docstring: "Does not assert that another vStep picks up this representation and produces later ones"; lines 140–160, proof read in part); `YM.Next.Rank.Paint.Path` (`Next/RANK/Stepped.lean:98–104`, definition read, headed "Awaiting restarted trajectory") takes the restarted trajectory as a predicate; `Next/RANK/Happen.lean` docstring: "Does NOT give the necessary step-W or restored raw kernel estimate". No Lean proof of the restarted steps found.

Inference of the reviewer: invariance of the total at 11R:375 needs covariance of the exact restarted densities, available from 1:188 and 4:256 without forests; the single pieces need not be covariant since they are symmetrized afterwards. Not checked: `Candle`; `Bag.lean`, `Patchable.lean`.

## A4. Proposition ch10:stability-assumption

10:560–935 read: 10:783–794 treats the histories with zero terminal data ("positivity is retained … it does not assume that every abstract element of a completed norm ball represents a positive density"); nothing there extends the Assumption.

**Found in addition:**
- Martin gives no proof: `background-ray-estimates.tex:69–74` makes the same assertion as 10:431; `background-path-convergence.tex:313`: "The extrapolated parameter need not lie in [0,1]; the extended input domain is essential for this proof".
- Lean makes the fixed bijections a hypothesis: `YM.FullVolume.Urns.Home` (`Lean/YM/FullVolume/Table/Vars.lean:27–33`, definition read) is the submodule of arrays transported by one fixed choice of permutations; `corresponds` (`:39`, statement read) puts an actual representation in it only under a hypothesis that its transport agrees with that choice.

The fix should name two items: output equivariance on extrapolated inputs and the wider band; and that the step maps preserve one fixed bijection of labels. The auditor's remark that the identity "is linear in the activities" is misleading: `a_M^F` is not linear in the incoming activities; the averaging argument of 9f:403–421 is pointwise and needs no positivity, which is a different point. Not checked: Scott.

## A7. Symmetrization in chapter 11

Confirmed. 11:1100–1330 read, 1345–2050 searched: no other symmetry step. 11:1285–1300 proves only compatibility of `T` with the adjoint action and conjugation; equivariance under the lattice group comes entirely from the averaging at 11:1330–1335. No definition of the "finite symmetry averaging" of 11:389 in any chapter; v3 defines only the average of 9f:635–662 and the conjugation average of 11E:136. Caveat: the proof of kernel covariance at 4:274–280 is a sketch. Not checked: 11:2050–2355.

## A8. Chapter 6 forest and 17c:164–165

Confirmed. No proof of independence from the forest in any chapter. A related claim is unproved at 11:679: "(ch11:conditional-curvature) holds for every forest and its right side does not depend on the forest".

## A1. The Assumption (a)–(f)

Quotations accurate. **Found in addition:**
- `Sees` is proved for the actual integrands: `YM.PhysicalNext.InteractingRank.forage` (IR/`Wings.lean:72`, statement and proof read), from `UsesFinal`, measurability and `GaugeInvariant`; used for the large-field integrands (`highTone`, IR/`Pictures.lean:69`) and the insertions (`Docking.bead`, IR/`Snap.lean:26`; `shade_sees`, `Wings.lean:98`, proof read). For `Zest` it is discharged in IR/`Opacity/Vegetal.lean:100` (`Pulled.versed` not read).
- Counterpart of (c): `Display.Docking.Spot` (IR/`Payout.lean:49–53`, definition read) bounds every factor by constants uniform in the tree tags; `Docking.bead_worth` (`Snap.lean:31`, statement read).
- Counterpart of (e): none found (limited search).
- (f): `YM.RG.Activities.Valid.moves` (`RG/Activities.lean:109`, field read); not traced where it is discharged for the ordinary step.

The verdict stands for v3: none of this is for the objects of v3's chapter 6. Not checked: whether these declarations lie on the chain to the final theorem.

## A5. 9:362 and 9:521

9:362 is conditional only on the Assumption. 9:521 uses Lemma `ch09:isotropy`, which needs Lemma `ch09:symmetric-localization`; its hypotheses and the absorption of the base point (9f:610–616) are listed at 9f:955–961 as "Used and not proved, apart from the assumption". A disclosed gap.

## A6. 9:949–951

Confirmed. Not checked: 10:212–254; Lean.
