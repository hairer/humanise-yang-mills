# Audit: the forest average and the steps with insertions (chapters 9, 10, 11)

Report of a read-only agent, 26 November 2026, as handed back (condensed). Worktree at `e53484a2`. Nothing was changed. `9f` = `chapters/09-forest-average.tex`, `9` = `09-renormalization.tex`, `10` = `10-common-trajectory.tex`, `11` = `11-marked-insertions.tex`, `11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`. "Martin" = `manuscript/existence/`, "Scott" = `manuscript/HumanizeYM_v2/`. Lean paths under `Lean/YM/`; IR = `PhysicalNext/AFTERNOON_INTERACTING_RANK_COMPARISON/`. No Lean command was run; no Lean chain was traced to the final theorem.

| Point | Verdict |
|---|---|
| A1 Assumption `ch09:forest-assumption` (a)–(f) | persists |
| A2 Hypothesis (H) at 11:335 | persists |
| A3 Restarted steps | persists |
| A4 Proposition `ch10:stability-assumption` | persists (narrower) |
| A5 9:362 and 9:521 | not a gap beyond the Assumption |
| A6 9:949–951 | not a gap (already corrected) |
| A7 Symmetrization on the label space in chapter 11 | persists at 11:389–390, 463, 474–475, 1330–1341 |
| A8 Chapter 6 forest and 17:164–165 | no inconsistency; one unproved claim persists |

## A1. Assumption ch09:forest-assumption (a)–(f) has no proof in v3

**v3.** 9f:221–310 states the six parts; 9f:923–925: "The six parts … none of which is proved in this monograph at present."

**Martin, part by part.**
- (a), the identity: derived for one fixed forest at `gaussian-reassembly.tex:240–307` (eq:reassembly-block-gas).
- (a), forest independence of the normalization: proved at `forest-average-log.tex:15–79`.
- (a), the mask form: asserted only, `forest-average-log.tex:188–193` ("the integrated construction gives a measurable local extension f_i").
- (b): a three-sentence argument at `forest-average-log.tex:93–101`, comparing the Haar factors as pullbacks of one product Haar measure.
- (c): asserted, 112–113 ("The bounds on a_M^F are uniform in F").
- (d): asserted, 117–121 ("The covariance of the individual sector formulas consequently gives…").
- (e): argued at `selected-nonlinear-offering.tex:182–272` by replication to a product period.
- (f): equivariance is a hypothesis of the reset, `physical-reset-reorganization.tex:22–24`; no proof found for the large-field family.

**Scott.** No forest average. `part2/D-section.tex:131` (Lemma D-connected (a)) and `:441` assert "equivariant" for the expansion with one axial tree per block, which 9f:12–18 argues has no reason to hold. Scott marks these conclusions as conditional on sector inputs (D:125).

**Lean** (source read).
- `YM.PhysicalNext.InteractingRank.Orchard`, `Orchard.grow`, `Streak` (IR/`Orchards.lean:39–118`, definitions read): independent tree tags per coarse site. `Orchard.transportable` (`:92`, statement and proof read): signed transport of the tags.
- `glance` (IR/`Layout.lean:124`, definition read): the average over tags of the integral.
- Factorization over disjoint supports: `inter_spec` (`Layout.lean:147`, statement and proof read), derived from the predicate `Sees` (IR/`Sight.lean:57`, definition read) through `integrate_beam` (`Sight.lean:94`, statement read). `Sees` is a structure field of each integrand (`PaintCan.sees`, `Flake.script`); not traced whether it is established for the actual integrands.
- Transport: structure `Voyage` (IR/`Voyage.lean:61`, definition read); `Soft.husks` (IR/`Soft/Shipment.lean:27`, proof read in part); `Voyage.tribute` (`Voyage.lean:96`).
- (f)-type: `YM.RG.Activities.Moves` (`RG/Activities.lean:87–96`, definition read), the field `moves` of `Valid`; not traced where it is discharged.
- Nothing searched for (c) or (e).

**Missing in v3.** All six parts. Martin supplies arguments for (a) in part, (b) and (e), and assertions for (c), (d), (f). Lean proves locality and transport for its own construction, given `Sees`; that construction is not v3's chapter 6.

**A fix would need.** Martin's reassembly, its argument for (b) and its replication argument for (e), carried into chapters 6 and 9; proofs of (c), (d), (f) against the choices of chapter 6 (cutoffs, covariances, assignment rules, regrouping).

**Inference of the auditor.** None of (a)–(f) looks false. (c) needs the local form of the constants, not only "finitely many tree shapes".

## A2. Hypothesis (H) at 11:335

**v3.** 11:335: "a bijection M↦ς·M from the labels for the insertions F_• onto those for the insertions F_•∘ς^*, … with a^{ςF}_{ς·M}[F_•∘ς^*](z,U)=a^F_M[F_•](z,ς^*U)". The insertions are functions on the cutoff lattice (11:65–75); 9f:46–47 lets ς act only on the coarse torus and one scale finer.

**Martin.** One insertion only: `marked-block-integral.tex:117–160` ("If it contains ⋆, exactly one component C contains that letter … a_C=E_F a_C^F, b_C=E_F b_C^F"). Symmetry transport of the terms with insertions appears only as a required property, `actual-marked-portfolio-calibration.tex:455–457`.

**Scott.** No forest average; not searched for transport of insertions.

**Lean.** `Display.Flake` (IR/`Pictures.lean:73`, definition read) carries a set of markers and a field `script : Sees …`. `Display.observer` (IR/`Slate.lean:56`, proof read) gives `Sees` for products of several flakes. `Display.inspected` (IR/`Tableau.lean:65`, statement read) and `Display.impression` (IR/`Curated.lean`, statement read) state the forest-averaged product formula for several disjoint clusters with insertions. No symmetry transport for flakes found.

**Missing or wrong in v3.**
- `F_•∘ς^*` needs an action of ς on configurations of the cutoff lattice, which v3 does not define.
- The clause compares two incoming representations built from different insertions, so it contains a claim about every finer step of the history; a one-step hypothesis should not.
- Forest locality of the coefficients `[z_S]a_M^F` for activities with several insertions is part of (H) and is not proved; Martin treats one insertion.

**A fix would need.** Either state transport for the incoming coefficients `(h_S, K_Y, k_{Y,S})` of (ch11:local-source) in the form "if incoming then outgoing", or define the action of ς on the cutoff lattice and make the transport over all steps an explicit induction.

**Inference of the auditor.** The natural action is `x ↦ ϱx + (L_m⋯L_{N−1})z`; odd, centered, nested blocks would make it compatible with every intermediate step. No source says so.

## A3. Restarted steps (11R:48–49, 11:19, 11R:247)

The restarted steps do not satisfy the hypotheses of Theorem `ch09:step-theorem`, so an analogue is needed; it is not stated.

**v3.** 11R:247 cites "the analogues for these restarted steps of Assumption … and of Hypothesis (H) …, which are stated for the original steps and are not proved". The restarted steps differ: radius `B_i = b(x_i)²`, threshold `ϑ(x_i)`, auxiliary reference parameter `r(x_i)` (11R:12–48); inverse coupling held constant, no reset by (ch09:reset) (11R:246); the incoming regular family deleted and reinserted as local factors `h_α` (11R:252–254: "we do not claim that the larger q_n meets that derivative bound"). The step theorem requires incoming activities with the weighted bounds of chapter 4, a positive density and the band (9:906–926). Output symmetry: 11R:374–375 "Averaging the regular pieces over the finite signed motion group retains their anchored bound and invariant sum".

**Martin.** `restarted-rank-history.tex:47–68` reuses the reassembly and forest average "with this enlarged alphabet"; at 125–145 it symmetrizes the additive family afterwards, asserting without proof "The newly obtained sum E_c is invariant under signed lattice motions".

**Scott, Lean.** Not checked.

**A fix would need.** The restarted analogue stated explicitly (parameters, local factors `h_α`, the same forest average, invariance of the total), or a proof that the conclusions of the Assumption persist under the changes of parameters.

## A4. Proposition ch10:stability-assumption

**v3.** 10:431: an allowed array "is in particular equivariant … a linear condition with fixed bijections of labels". 10:349: "The extrapolation preserves all linear symmetry and moment conditions". 10:498–501: "the array and local scalar outputs there even when an extrapolated array has not been identified with a positive density". 10:491–493 uses a widened range of inverse couplings.

**Missing.** Equivariance is preserved by the operations used (affine lines, extrapolation, limits). But the Assumption is stated "Under the hypotheses of Theorem ch09:step-theorem" (9f:223), which require a strictly positive input density and the narrow band (9:920). The proof evaluates the step maps on extrapolated arrays that need not represent positive densities, and on a wider band; there the equivariance of the outputs (Propositions `ch09:family-equivariance`, `ch09:output-equivariance`) is not covered by the Assumption as scoped. That fixed bijections serve all arrays on a line is asserted, not derived from part (d).

**A fix would need.** The scope of the Assumption extended to the algebraic extension used in Step 2, or a proof that output equivariance and the forest-average identity hold coefficientwise without positivity.

**Inference of the auditor.** The forest-average identity is linear in the activities and plausibly needs no positivity. **Not checked:** Martin, Scott, Lean for this proposition; 10:560–935.

## A5. 9:362 and 9:521 — not a gap beyond the Assumption

9:161 inputs 9f. 9:362 now cites (ch09:share-equivariance), which is Proposition `ch09:family-equivariance` (ii) (9f:554–559). 9:521 cites Lemma `ch09:isotropy`, whose equivariance comes from 9:398 "under Assumption … (its part (f) …)". Both are conditional on the Assumption, and 9:398, 9:926 say so.

## A6. 9:949–951 — not a gap

9:949: "The theorem does not assert that the output inverse coupling lies in its band [β̂_m/2,2β̂_m]; along the tuned histories of Theorem ch10:finite-history it does…". Scott `part2/D-section.tex:847`: "no output-band condition is imposed". 10:212–254 supports the second clause. Lean not re-read.

## A7. Symmetrization of maps on the label space in chapter 11

**v3.** 11:389: "Finite symmetry averaging only enlarges C_d,ε"; the averaging is not defined in chapter 11; 463 and 474–475 refer back to it. 11:1330–1335: "Average the raw polynomial construction on domain and range … The insertion, covariance and radial Taylor localization have the corresponding covariance identities, so this preserves … the exact density comparison". The dependence is stated or harmless at 11:968–970 ("assuming E_i is invariant"), 1049, 1096, and in 11E:59, 136–141.

**Martin.** `marked-block-integral.tex:268–272` presupposes equivariant activities: "The original and remaining regular sums are invariant under this average: their label permutations preserve values and masks".

**Missing.** The one-step symmetrization (11:389) and the averaged localization map (11:1330) preserve exactness only if the representation with insertions is covariant; at the level of activities this is the Assumption plus the transport part of (H), and the text does not say so at those lines. The "corresponding covariance identities" of 11:1330 are asserted without proof.

**Inference of the auditor.** Statements about integrated correlations or exact densities only (11E, possibly 11:2063) need only covariance of the exact densities, which follows from invariance of `ρ_N` and covariance of the block kernels (Proposition `ch04:kernel-properties`), without forests, once ς acts on the cutoff lattice (A2). No source states this split. **Not checked:** 11:1100–1250, 1345–2050; 11E beyond 50–65, 128–145.

## A8. Chapter 6 forest and 17:164–165

06:86 fixes "a rooted spanning tree in every block" per sector; chapter 6 does not say that the forest is averaged afterwards (9f:969–970 records this). 17:164–165 takes "the coarse translates of one reference tree … the average over forests of Section 9 is not used here … that these do not depend on the forest (…) is used here and is not proved in this chapter". Scott uses the same device (`part2/D-section.tex:1197`).

The translated forest is one element of the product set of forests, so there is no contradiction. The bounds of chapter 17 transfer to the averaged construction only through the unproved independence of gauge-invariant pullbacks from the forest; "Π_F commutes with coarse translations" (17:166) does not give them for forests that are not translation invariant.

**A fix would need.** A proof that two forests give critical configurations differing by a gauge transformation equal to one at the block roots, or the bounds of chapter 17 uniformly in the forest.

## New findings

1. The status paragraph 9f:963–967 still says chapter 11 is "Not yet adapted … no such statement has been written", although 11:19 and 11:335 now state (H).
2. The Assumption is scoped to positive input densities on the narrow band; chapter 10 Step 2 uses the step outside that scope (A4).
3. Scott's Lemma D-connected (D:131) asserts equivariance for one fixed axial tree per block.
4. Martin's averaging with insertions handles one insertion; Lean (`Display.inspected`, `Display.impression`) several; (H) needs several.
5. Martin's restart symmetrizes afterwards but asserts invariance of the total without proof; 11R:374–375 copies this.
6. 11:389 refers to a "finite symmetry averaging" defined nowhere in chapter 11.

## Not read or checked

Chapter 6 beyond grep hits; chapter 11 lines 480–960, 1100–1260, 1345–2355 except grep hits; chapter 10 beyond 205–262, 330–360, 395–560; chapter 17 beyond 150–215. Lean: no build; nothing searched for (c), (e) or the restart. Martin: files beyond those cited. Scott: beyond D-section 125–135, 353, 441, 840–850, 1197. Audit notes `forest-average-revision.md`, `ch9-covariance.md`, `forest-invariance.md` not read.
