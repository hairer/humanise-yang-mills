# Review of the adaptation of chapter 11 to the forest average

Independent agent, 25 November 2026, as handed back (condensed). Read: `09-forest-average.tex` in full; 11:1–750, 1000–1116 and grep hits; 11R in full. Issue 2 of the fork.

## Verdict

Hypothesis (H) at 11:335 was close to correct but not a precise statement. Four defects were corrected inside the line; one remains open. The claim that the proof of Proposition ch09:forest-average-prop applies coefficient by coefficient is correct after the amendment. That the density with insertions is averaged by the same forest average is confirmed by the text of Martin (`marked-block-integral.tex:140–171`) and by the Lean source (`YM.PhysicalNext.InteractingRank.glance`, `Layout.lean:124`; `Display.pages`, `Curated.lean:66, 69`; product formula for disjoint supports, `Layout.lean:109–111`; source read, not built, not traced to the final theorem).

## Corrected

- **11:335.** (1) (H) now says the activities are Borel and gauge-invariant in `U` and local on `X_M`, and that the labels comprise those of (ch09:fixed-forest-gas), with the same supports and prescribed large-field sets and with coefficient of `z_∅` equal to the activity there, and further labels, which carry an insertion factor and whose coefficient of `z_∅` is zero. Without the identification of the labels the reduction at zero source did not follow. (2) The uniformity clause now covers "every other estimate of this chapter which is made for one forest, in particular those of Section ch11:actual-reader", which 11:679 cites (H) for. (3) The transport clause now has a bijection from the labels for the insertions `F_•` onto those for `F_•∘ς^*`.
- **11:19, 11R:247.** The Assumption and (H) are stated for the original steps; the restarted steps use a different construction (11R:48–49). Both lines now say that the analogues for the restarted steps are assumed. That the restarted steps fall outside the hypotheses of Theorem ch09:step-theorem is the reviewer's inference; those hypotheses were not read.

## Open

- **Transport clause of (H).** `F_i∘ς^*` needs the action of `ς` on the cutoff lattice, which is not defined (chapter 9 defines it one scale finer), and the clause refers to cutoff insertions inside a one-step hypothesis. A cleaner formulation would transport the coefficients `(h_S, K_Y, k_{Y,S})` of the incoming representation.
- **11R:192.** What needs the forest-averaged activities is the symmetry of the incoming representation at the comparison scale, not the reindexing. Wording only; not edited.

## Per line

11:244 correct (6:85–86). 11:293 correct; the factors `t_C` are forest-free by definition. 11:679: the identity part is correct (11:617–660 read: `P_f − J P_c J^*` involves no forest); the appeal to (H) is now covered. 11:726 correct: Proposition (i) states that `N_F` does not depend on `F`. 11:1049 correct as a statement of dependence.

## Other places in chapters 11, 11R, 11E

- Need the forest-averaged form and the Assumption with (H): 11:1096 and 969–970; 11E:59, 136–141; 11R:374–375 ("invariant sum" of the regular pieces, not noticed by the adapting agent); 11:2063 (probably at the level of the density only; inference).
- Need only uniformity in the forest: 11:244–345 with 383–388, 457–462, 512; 11:676–732; 11:1374ff, 1494–1506, 1592ff; 11R:261–337.
- Need nothing: 11:31–219, 537–606, 617–674; 11:1208, 1766, 1975–1990 (axial gauges for gauge-invariant evaluation, not block forests); 11:1330–1341, 389–390, 463, 474–475; 11R:111–112, 360–362.

## The status paragraph of `09-forest-average.tex` (lines 963–967), not edited

Replacement proposed by the reviewer, five lines:

    \emph{Adapted under a further hypothesis.} The expansions with insertions of
    Chapter~\ref{ch11:insertions} average their activities with insertions over
    the forests by the same average, under Hypothesis~(H) of Section~\ref{ch11:marked-step},
    which extends parts~(a)--(d) to activities with insertions and is not proved; under it the
    coefficient of $z_\varnothing$ is \eqref{ch09:averaged-gas}. The histories of

## Not read or checked

11:750–1000, 1116–1200 and most of 1212–2355 (grep hits only); 11E beyond 15–25, 50–70, 128–145; the hypotheses of Theorem ch09:step-theorem; chapter 6 beyond grep hits; the Lean chain beyond the files named. No build. Checks run: line counts 2355 and 393 unchanged; `python3 tools/check_draft.py` passes.
