# Chapter 11 adapted to the average over forests

Report of the adapting agent, 25 November 2026, as handed back (condensed). Issue 2 of the fork; issue 1, items 27 and 30. "Martin" = `manuscript/existence/`; Lean paths under `Lean/YM/`. Nine lines changed (7 in `11-marked-insertions.tex`, 2 in `11-restarted-history.tex`), all within lines.

## What the sources show

The density with insertions is averaged over the forests by the same average as the density without insertions.

- Martin `marked-block-integral.tex:140–156` (read 1–200): the activities with insertions read the forest only in the blocks of their support ("The marked value has the same locality in the forest as the ordinary one"); independent forest choices are averaged as in `sec:forest-average-log` ("`a_C = E_F a_C^F`, `b_C = E_F b_C^F`"); one identity covers both densities. Also `marked-activity-jets.tex:172`, `marked-kernel-convergence.tex:213`, `restarted-rank-history.tex:67–68`.
- Lean (source read; not traced to the final theorem): `YM.PhysicalNext.InteractingRank.Orchard`, `Streak` (`PhysicalNext/AFTERNOON_INTERACTING_RANK_COMPARISON/Orchards.lean:1–110`): one independent tree tag per coarse site, with `transportable`. `YM.PhysicalNext.InteractingRank.glance` (`Layout.lean:124`) is the average over the tags of the integral; the integrands with insertions `Display.pages`, `Display.tucked` (`Curated.lean:34, 66`) are integrated by the same `glance`.
- v3: the right side of (ch11:conditional-curvature), 11:656–659, contains no forest (read; agrees with `audit/forest-average/forest-invariance.md:131–135`).

Classification of the statements of chapter 11:

- need the forest-averaged form: the normalization at 11:334–335; reduction to chapter 9's representation at zero source; equivariance of `Z_{N,p,d}` (11:1049); the signed symmetry at 11R:191;
- need only bounds uniform in the forest: the fixed-sector bounds of 11:244–345; the local estimates of 11:679–732;
- need nothing: the source algebra (11:31–118), the support bounds (11:120–219), the chessboard and transfer arguments (11:827–881), the finite-dimensional detection (11:960–1032).

## Hypothesis (H), stated at 11:335

For every forest `F`, the exact identity for the block integral of the incoming representation with insertions (ch11:local-source) has the form (ch09:fixed-forest-gas), with the same constant `N_F` and function `S`; labels, supports `X_M` (containing the dependence sets of the insertions carried by `M`) and prescribed large-field sets `I_M` independent of `F`; and activities `a_M^F(z,U)` in `A_I` with `Σ_M sup_U ‖a_M^F(·,U)‖_ω < ∞`, whose coefficient of `z_∅` is the activity of (ch09:fixed-forest-gas), or zero for a label carrying an insertion factor. Moreover every coefficient `[z_S] a_M^F` satisfies part (b) of Assumption ch09:forest-assumption; the bounds of the section hold for every `F` with right sides independent of `F`; and for every `ς` in `𝔊` there is a bijection of labels as in part (d) transporting the activities with insertions.

The Assumption (a)–(f) does not cover this: it is stated for the insertion-free construction, with real-valued activities. Martin proves forest locality for one insertion; v3 does not.

## Changed lines

| Line | Change | Support |
|---|---|---|
| 11:19 | adds that the local representations are those of chapter 9, averaged over the forests, and that the chapter assumes Assumption ch09:forest-assumption and Hypothesis (H), neither proved | 09-forest-average.tex:446; 10:233, 257 (read) |
| 11:244 | "In one sector, which includes one forest (one rooted spanning tree in every block), …" | 09-forest-average.tex:6–9; 9:74 (read) |
| 11:293 | "… formed with its forest; by Hypothesis (H) below the bounds `b_j` and the factors `t_C` do not depend on the forest" | pointer to (H) |
| 11:335 | the normalization is the forest-averaged one; statement of (H); under (H) the proof of Proposition ch09:forest-average-prop (i)–(ii) applies coefficient by coefficient | sources above (read); the coefficientwise argument is the agent's own check of the cited proof (inference) |
| 11:679 | "(a forest; the identity (ch11:conditional-curvature) holds for every forest and its right side does not depend on the forest, and the estimates below are used, by Hypothesis (H), with bounds independent of the forest …)" | 11:656–659 (read); uniformity of the chapter 6 estimates is assumed through (H) |
| 11:726 | "The normalization constant, which does not depend on the forest (Proposition ch09:forest-average-prop (i)), …" | Lemma ch09:forest-determinant and Assumption (a) |
| 11:1049 | records that the equivariance of `Z_{N,p,d}` rests on the Assumption and the transport part of (H) | inference: a dependency is recorded, not proved |
| 11R:192 | the signed symmetry requires the forest-averaged incoming activities | 09-forest-average.tex:13–18 |
| 11R:247 | "(for every forest; the local integrals are formed for each forest and averaged …, under Assumption … and Hypothesis (H), neither of which is proved)" | Martin `restarted-rank-history.tex:67–68` (read) |

## Not adapted

- 11:389–390, 463, 474–475 ("finite symmetry averaging"); 11:1096, 1330–1341 (equivariant projections, localization map); 11:2063 ("real and equivariant"); 11E:59, 136–141: these symmetrize maps on the label space; whether they presuppose equivariant activities was not determined.
- Chapter 6 does not say that its forest is averaged afterwards; 17:164–165 uses one translated forest.
- The status paragraph at the end of `09-forest-average.tex` (lines 963–967) still says chapter 11 is not adapted. The agent's edit of it was refused by the permission classifier and was not made.

## Not read or checked

Chapter 11 beyond about line 1110, except grep hits, 1318–1345 and 2050–2070; 11E except 1–70 and 130–141; the chain from `glance` to the final Lean theorem. Checks run: line counts unchanged (2355, 393, 185, 973); `python3 tools/check_draft.py`: all cross-references resolve.
