# Chapter 5 (05-gaussian.tex): independent review of the vocabulary edit

Reviewed: the uncommitted diff of `manuscript/HumanizeYM_v3/chapters/05-gaussian.tex` in `/Users/mgubi/ym-terminology` against `HEAD` (4f462ac5), all 213 changed lines (the 214th line of `git diff --stat` is an unchanged blank line inside the last hunk). The diff was read and judged before the editor's report `ch05-apply.md` was opened. Nothing was edited, staged or committed.

**Verdict: ACCEPT WITH THE LISTED CORRECTIONS.**
Counts: ERROR 1, LANGUAGE 3, DICTIONARY 2, MINOR 15.

## Mechanical checks (run)

- Line-by-line comparison with `HEAD`: 1388 lines before and after, 213 lines differ, each in place.
- Math mode, `\ref`, `\eqref`, `\label`, `\cite` on every changed line, old against new: nothing removed or altered. Only additions: `$k$`, `\ref{ch05:stationary}` (20); `$\ell^2$` (40, 528, 944); `$W$`, `$T$`, `$W_s$`, `$W_F$`, `$M$`, `$D$`, `$W_0$`, `$N$`, `$\ZZ^4$`, `$\mathcal Q$`, `$\beta$`, `$\alpha$`, `$v=0$`, `$\Gamma_{y,x}$` in prose; `\ref{ch05:actual-tangent}` (535), `\ref{ch10:choices}` (689), `\ref{ch04:blocking}` (937, 1005). All four target labels exist. No label, macro argument or quotation was reworded.
- Dollar parity and brace balance unchanged on every changed line; no doubled words, also across line ends; no a/an fault.
- No proposal with basis `?` was applied.

## ERROR (1)

**E1. Line 351.**
Old: `$c(1+|z_\mu|)$ for $z_\mu\ne0$; the principal case is bounded`
New: `$c(1+|z_\mu|)$ for $z_\mu\ne0$; the case of the zero alias is bounded`
The estimate is per coordinate: the display bounds `|r_M((p_μ+2πz_μ)/M)|` by `C/(1+|z_μ|)`, and the sentence splits into `z_μ ≠ 0` and "the principal case", which is `z_μ = 0`. "Zero alias" is the alias `z = 0` (all four components). With the new wording the aliases with `z ≠ 0` but `z_μ = 0` are covered by neither clause, so the proof of the displayed bound has a gap that the old text did not have. The dictionary lists 5:351–353 under *principal* sense 1, so the source of the slip is the entry, but the result is wrong here.
Corrected: `$c(1+|z_\mu|)$ for $z_\mu\ne0$; the case $z_\mu=0$ is bounded`
(Line 352, "At the real zero alias the centered factor has a positive lower bound", is acceptable: the zero alias has `z_μ = 0`, and this is what line 425 uses.)

## LANGUAGE (3)

**L1. Line 412.**
Old: `For a nonprincipal real alias the denominator is bounded below`
New: `For a nonzero real alias the denominator is bounded below`
Ambiguous in a way that matters. For real `p ≠ 0` the zero alias `p/M` is itself a nonzero real momentum, and line 811 uses "nonzero real momentum" in exactly that sense. The lower bound `c(1+max|z_μ|)²` holds only for alias index `z ≠ 0`.
Corrected: `For a real alias with $z\ne0$ the denominator is bounded below`

**L2. Line 857.**
Old: `actual block average correction introduced below is a fixed finite-range`
New: `gradient correction for the averaging operation introduced below is a fixed finite-range`
"introduced below" now attaches to "the averaging operation", which was introduced in Chapter 4, not below; what is introduced below is the correction `d_{0,f}ER` of (ch05:corrected-transport). The word "gradient" is the editor's addition; it is true (1092, 1108) and I accept it.
Corrected: `gradient correction introduced below for the averaging operation is a fixed finite-range`

**L3. Line 1293.**
Old: `local labels agree there as functions of the full field.`
New: `local values of the index $\alpha$ agree there as functions of the full field.`
Values of an index do not agree "as functions". The old metonymy (label for the choice it labels) does not survive the replacement.
Corrected: `local values of the index $\alpha$ select the same operation there, as a function of the full field.` (the wording of 968–969)

## DICTIONARY (2)

**D1. Lines 2, 7, 14, 1156: "stationary background" → "background field".**
Old / new: `Gaussian kernels and stationary backgrounds` / `... and background fields`; `construct a stationary background for` / `construct a background field for`; `stationary background. The general` / `background field. The general`; `\section{A stationary background on a uniform neighborhood}` / `\section{A background field on a uniform neighborhood}`.
Two problems. (a) The entry *stationary background* has basis I; it was applied on the strength of "Adopted (24 November 2026)" and the table. (b) The sense: at 7, 14 and 1156 the object is the specific stationary field `ρ(v)` that the chapter constructs, for which the table word is *critical configuration*; "background field" is the table word for any configuration about which one expands. The replacement drops "stationary" and so weakens 7 and 14, and the chapter now has two names for one object: the new sentence at line 20 speaks of "the critical configuration constructed in Section~\ref{ch05:stationary}", and that section is titled "A background field on a uniform neighborhood". The editor's report raises the same doubt for 1156.
Corrected (keeps the adopted word for the role, names the object):
- 2: leave as edited (`Gaussian kernels and background fields`), or restore; author's choice.
- 7: `it supplies the inverse needed to construct the critical configuration, the background field for`
- 14: `critical configuration. The general block transformation algebra is`
- 1156: `\section{A critical configuration on a uniform neighborhood}`
Minimal alternative if the 24 November decision is to be kept literally: "a stationary background field" at 7, 14, 1156.

**D2. Line 312: survivor with basis D.**
Text (unchanged): `Fix the final smoothing order $j=j_n\ge4$ and the penalty $b>0$.`
*block penalty* sense 1 (D) lists 5:312; lines 88, 102, 1089 were changed and this one was not.
Corrected: `Fix the final smoothing order $j=j_n\ge4$ and the penalty parameter $b>0$.`

### Basis-I applications that I checked and accept (no correction; for the author's information)

- *actual* (basis I, senses 1 and 3) deleted or absorbed at 302, 751, 782, 857, 912, 930, 986, 1000, 1078, 1118, 1289, 1304, 1311, 1321, 1324, 1379, 1380. I read each sentence: no object, hypothesis or claim changes. At 1118 "the actual quadratic energy" became "the quadratic energy built with $\mathcal Q$", which agrees with (ch05:actual-transport-identities). At 1078 the contrast with the flat Fourier calculation is still stated in the same sentence. The editor cites a separate rule of the brief for this word; I did not see the brief.
- *tree slice* (I) → *block axial gauge*; *route*, *walk* (I) → *contour* (995, 1003, 1016): table decisions.
- No dictionary entry exists for "block transformation" (6), "fluctuations" (6), "averaging map" (20), "block map" (88, 206, 306), "stationary fine field" (105). They were replaced from the table. Sense identified correctly in each: 88 abstract linear `Q`, 306 the linear `M` of the recurrence, 206 the nonlinear gauge-equivariant average.

## Point 1: meaning, line by line

Apart from E1, L1 and D1 I found no change of object, hypothesis, quantifier or claim. Specific checks:

- **`W_s`, `W_a`, `W_F`.** 528/535 (`W` of Section 5.6 is `W_s`: true by 1084); 859 ("the operator $W$ built with the linear averaging operator" = old "straight transport"); 1084; 1118 (`W_a`, energy with `𝒬`); 1144 (`W_F`, unchanged claim); 1151–1153; 1234 (`W_a` smooth representative, `W_F` its representative in the gauge coordinates); 1310–1311 (the derivative is identified with `W_F`, representative of `W_a`, as in (ch05:stationary-tangent)). No property moved to the wrong operator.
- **"minimizer" / "minimal".** Not introduced anywhere; 958, 1118, 1144 are original wording.
- **"axial gauge" against the spanning trees.** Combinatorial uses kept as "tree" (917–919, 964, 1002, 1041, 1140, 1327); "block axial gauge" only where the slice, chart or coordinates are meant. 1005 states which axial gauge is meant.
- **"averaging operation" against "linear averaging operator".** Checked at 20, 88, 154, 206, 241, 306, 328, 535, 536, 857, 912, 950, 954, 969, 986, 993, 1008, 1017, 1071, 1084, 1292, 1304, 1376, 1381. Linear where the text has `M`/`Q`, nonlinear where it has the average of Chapter 4. At 536 `𝒬 = M + d_{0,c}R` is called "an averaging operator containing a gradient correction": correct (it is linear).
- **"fluctuation field".** Used once (6), for the integration variable; "noise" (the Gaussian term of the block kernel) was left alone.
- **penalty parameter / penalty term.** Parameter at 88, 102, 1089; term at 146, 1163, 1283. Correct.
- **scale / step / stage / cutoff.** 379 (steps `h+1,…,n` are the later, coarser ones: consistent with 705–707 and 776–777); 705–706 ("terminal scale `N+1`" → "ultraviolet cutoff `N+1`": same integer); 757; 689 (stages). No integer changed.
- **"regularity condition".** Does not occur.
- **subsequential limit, kernel, preimage, position within the block, site, base point.** Same objects as cluster, row (sense 2), lift, fine residue, anchor. "residue" at 389–390 (momentum classes) correctly left.

## Point 4: first-use sentences

- **Line 20.** "In particular, Bałaban's background field is a minimum of the action at fixed averages (his ``minimal configuration''), for $k$ steps at once; the critical configuration constructed in Section~\ref{ch05:stationary} is a stationary point of the fine action plus the penalty term of the block kernel, for one step." Supported: the first half by the *Literature* line of *stationary graph* (B85d p. 277 abstract, p. 278; B87 p. 256), the second by (ch05:actual-action) and Proposition (ch05:stationary-prop) (`F = D_y f = 0`, `y` the non-tree coordinates). It follows the wording the entry prescribes. It claims nothing beyond that. Two style points under MINOR (m1).
- **Line 930.** "the gauge in which the links of the chosen spanning tree of each block equal the identity". True: in (ch05:forest-chart) `ι_Fψ` vanishes and `rep` equals one on tree edges. It is the definition the entry *tree slice* asks for.
- **Line 937.** "Any spanning tree rooted at the block center is allowed here" is true (916–918, 1041, 1327). "the gauge is used here as a chart" is true (936). "a different construction from the axial gauge ... of Chapter 4" follows the entry. "Bałaban has the tree of his contours $\Gamma_{y,x}$ rooted at a block corner": the *Literature* line gives the contours (B84a (1.7), B85a p. 24) and the corner, and says that the contours form a tree "is an inference from the definition of the contours". The statement is therefore supported only up to that declared inference; it is mathematically harmless (the comb contours do form a tree), and the entry itself orders this sentence. No citation is attached; `Balaban1984Propagators` (B84a) is already in the bibliography. See m2 for "patch frames".
- **Unreported in the list of three but present, and true:** 154 (names `M`), 528 (names `W`, `T`), 535 (`W` is `W_s`; ordered by the table), 1005 (which axial gauge). The editor lists them as item 4 of his report.

## Point 6: changes that are more than a word swap

All faithful; listed so that the author sees them.
- 195: `The particular smoothing in the supplied construction uses` → `The smoothing used in this construction is` (Appendix D repair, verbatim).
- 689: `\ref{ch10:choices}` added (Appendix D, 5:689).
- 498: `The rescaled one-form and two-form transports are` → `The rescaled alias components of the operators $W$ and $T$ introduced below are` (forward reference; "one-form and two-form" dropped).
- 450: `a prescribed sequence of growing histories` → `prescribed growing sequences of blocking parameters`; 707: "sequence of ... histories" → "succession of ... sequences".
- 772: `the directional filter squares converge` → `the squared moduli of the directional symbols converge` (more exact; `u` is defined as a squared modulus at 758).
- 857 "gradient" added; 1118 `$\mathcal Q$` and 1311 `$W_F$` written out; 1339 "with its value at $v=0$ subtracted" (basis S).
- 453: "Exact" dropped from the section title.

## MINOR (15)

- **m1. Line 20.** "In particular" does not follow from the preceding sentence (a different averaging operation); `$k$` is Bałaban's index and is not defined in the chapter. Suggested: `... without checking its hypotheses. Moreover, Ba{\l}aban's background field is ... for several steps at once; the critical configuration ...` (rest unchanged).
- **m2. Line 937.** "the axial gauge of the patch frames of Chapter 4" keeps the house word "frame", which lines 950–1020 replace by "local gauge transformation". Suggested: `... a different construction from the axial gauge of the local gauge transformations of Chapter~\ref{ch04:blocking}.` Optionally add `\cite{Balaban1984Propagators}` after `$\Gamma_{y,x}$`.
- **m3. Lines 352, 360.** "the real zero alias" reads oddly. Suggested: 352 `directly by the finite sum. At the zero alias with real momentum the`; 360 `At the zero alias with real momentum the same factors have product bounded`.
- **m4. Lines 379, 384.** The prose no longer contains "suffix", but `f_{\rm suffix}` stays in the display at 384 and is now unexplained. Suggested for 379: `through the subsequent, coarser steps $h+1,\ldots,n$, with accumulated symbol $f_{\rm suffix}$. If these steps have total scaling factor` (that `f_suffix` is the accumulated symbol of those steps is my reading of 388–392; the old text did not define it either).
- **m5. Line 611.** `with the norm multiplied by a fixed factor` states an equality where a bound is meant. Suggested: `written $A=Vd_{r+1}$ on a smaller strip, with the norm increased by at most a fixed factor.`
- **m6. Line 689.** `pair of consecutive stages`: the entry's meaning is the pair `(J(m+1),J(m))` of one step, which may be `(j,j)`; "consecutive" suggests `j, j+1` only. (The entry also offers "two consecutive stages", so the editor followed it.) Suggested: `For each pair of stages of one step (Section~\ref{ch10:choices}) choose the coarse modification`.
- **m7. Line 712.** `two-scale kernel` loses "adjacent". Suggested: `range over fixed finite coordinate sets. For a kernel between adjacent scales,`.
- **m8. Lines 730, 848.** Noun pile "subsequential limit matrices". Suggested: 730 `then identifies every coefficient. Alternatively, agreement of the matrices of the subsequential limits`; 848 `theorem. Thus the matrices of the subsequential limits agree on every torus, and the`.
- **m9. Lines 828, 849.** "the limit of the periodized kernels ... identify their limit on the infinite lattice": two different limits (period, cutoff) under one word. Suggested: 828 `and the recovery of a kernel on $\ZZ^4$ from its periodizations along unbounded periods identify their limit on the infinite lattice.`; 849 `recovery from the periodizations identifies the kernel on the infinite lattice. This proves convergence for the`.
- **m10. Lines 740, 1378.** "schedule" → "sequences of blocking parameters". By the definition at 303–305 that term covers ratios and smoothing orders only, while the nested data of 703–705 also contain the modification coefficients, on which the modified metrics in the proposition depend. "just described" saves the statement. Suggested: 740 `Fix a scale and the nested choice of parameters just described. The unmodified`; 1378 `For the nested selected choice of parameters, Proposition~\ref{ch05:horizon-limit}` (770 already says "the parameters").
- **m11. Line 920.** "pull-back under the block projection": "block projection" is not defined; the text's defined word is the parent map (1:218–220; used in the display at 923). Suggested: `links $V$, their pull-back under the parent map is`.
- **m12. Lines 968, 1293, 1336.** `the index $\alpha$` is not introduced in this chapter (it is the `α` of 4:217) and the letter is also the scalar `α` of 495, 572, 815 and a summation index at 232. Suggested for 968: `strictly on its minimizing branch. Every local value of the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking} then selects the`.
- **m13. Line 1007.** `the two discrepancies between root and local gauge transformation` is as obscure as the old "root-to-frame discrepancies" and less idiomatic. Suggested: `estimate for the local gauge transformations, linear in the plaquette sum, controls the discrepancy at each of the two roots from its local gauge transformation;` (author to confirm the intended object).
- **m14. Line 1314.** "Equality of actions only on a / previously selected critical-configuration map": equality holds on the graph of the map, as line 972 now says. Line 1313 ends with "only on a" and is unchanged, so the suggested line 1314 is `graph of one previously selected critical-configuration map would not suffice for this argument.`
- **m15. Line 105.** `the critical fine configuration` splits the adopted term. Suggested: `The map $W$ sends a coarse field to the fine critical configuration. The`.

## Point 5: consistency and survivors

One name per object now holds for: sequence of blocking parameters, symbol, zero/nonzero alias, kernel, subsequential limit, preimage, position within the block, averaging operation, linear averaging operator `M`, local gauge transformation, block axial gauge, contour, critical-configuration map, auxiliary index. Titles agree with the body except for D1 (2, 1156).

Old house words still in prose:
- 312 "the penalty" (D): see D2.
- 581, 582, 599 "principal columns", "nonprincipal columns": left because "columns" is basis I; but the same objects are "alias components" at 498 and the same alias is "zero alias" everywhere else. Needs the author's decision; a consistent form would be 581–582 `These formulas give bounded components at the zero alias and bounds` / `$C\Gamma(l)^{-j}$ for the components at nonzero aliases on a smaller cube.`, 599 `At zero momentum the components at the zero alias are $I$ and the other`, 600 `components vanish, ...`.
- 609, 624 "matrix row", "two-form row" (row sense 3, basis I): correctly left; "row" is otherwise gone except the literal row sums (882, 996, 1346).
- 945 "the tree inequality", 1306 "the deterministic comparison \eqref{ch05:tree-comparison}", 1319 "the Euclidean tree gap": the same inequality is "Poincar\'e-type inequality in the block axial gauge" at 1290 and 1375. No entry lists these three lines.
- 1005–1006, 1028, 1031–1032 "macro-box", "macro-patch" (R: "enlarged block"): left because 1028 is inside math mode; consistent within the chapter.
- 320 "torus period": the entries *period* (keep) and *torus period* (side length) disagree; left.
- 1222, 1287 "the background" for `ρ`: basis I, left; consistent with D1 only if the role sense is intended.
- 14, 84, 114 "block transformation" against "one step" at 6: the editor's reason (general algebra of the cited literature) is sound.
- 700 "observation scale", 738/858/1378 "selected", 861 "activity arrays", "marked integral maps", 970 "uniform branch masses", 973 "uncut", "plateaux", 1362 "determinant margin", "incoming", "vertical", "physical", "nonlinear step": basis I or no replacement proposed; correctly left.
- Pre-existing, not introduced by the edit: 1301–1304 "satisfying \eqref{ch05:path-budget}, the hypothesis ..." lacks "and".

## Not checked

- No LaTeX build and no rendered pages (read-only review); the editor reports a clean `latexmk` run and `tools/check_draft.py`, which I did not repeat.
- Bałaban's papers were not opened; statements about them were checked only against the *Literature* lines of the dictionary.
- The dictionary's own basis assignments and line lists were taken as given, except where the chapter text contradicts them (E1).
- The editor's brief (in particular its "rule 3" for *actual*) was not available to me.
- Other chapters: in this worktree chapters 1–4 still use the old words ("frame", "block average", "tag"), and no chapter contains "called a step"; the first-use sentences that chapter 5 now relies on for *step*, *averaging operation*, *local gauge transformation*, *contour*, *auxiliary index*, *penalty parameter* do not exist yet. Citations of chapter 5 titles or phrases from other chapters were not searched.
- The mathematics of unchanged lines, the Lean correspondence and the blueprint were not reviewed.
