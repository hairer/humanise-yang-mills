# Chapter 5 (05-gaussian.tex): corrections applied from ch05-review.md

File: `/Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/05-gaussian.tex`. 29 lines edited in place, no line added, removed, joined or split. Nothing staged, committed or reverted.

Items applied: E1 (351); L1 (412), L2 (857), L3 (1293); D1 (7, 14, 1156), D2 (312); m1 (20), m2 (937), m3 (352, 360), m4 (379), m5 (611), m6 (689), m7 (712), m8 (730, 731, 848), m9 (828, 849), m10 (740, 1378), m11 (920), m12 (968), m13 (1007), m14 (1313, 1314), m15 (105).

## Reviewer corrections changed, and why

- **m8, lines 730-731.** The reviewer's text for 730 ends "...the matrices of the subsequential limits", but line 731 begins "matrices on an unbounded sequence", which would give "limits matrices on". Line 730 now ends "agreement of the matrices of the subsequential" and line 731 begins "limits on an unbounded sequence" (one word replaced on 731, a line the review did not list).
- **m14, lines 1313-1314.** The reviewer left 1313 ("...only on a") unchanged, giving "only on a graph of one previously selected ... map". A map has one graph, so 1313 now ends "only on the"; 1314 is the reviewer's text.

## Reviewer corrections applied as given but resting on the reviewer's own reading

- **m4, line 379**: "with accumulated symbol $f_{\rm suffix}$" is the reviewer's interpretation of 388-392 (the file does not define `f_suffix` elsewhere; it occurs only in the display at 384). Consistent with "The symbol composition identities above identify the summands" (390-391), but the author should confirm.
- **m13, line 1007**: reviewer marked "author to confirm the intended object"; applied verbatim.
- **m11, line 920**: "parent map" is defined at 01-lattice.tex:220 and is the map used in the display at 923; applied.

## Not applied / left as is

- **Line 2 (chapter title)**: the review gives no corrected text ("leave as edited ..., or restore; author's choice"). Left as the conversion made it: `\chapter{Gaussian kernels and background fields}`. The body now says "critical configuration" at 7, 14, 1156, so the title and the section title use different words; author's decision.
- **m2, optional `\cite{Balaban1984Propagators}` at 937**: not added (marked optional; the reviewer did not open the paper).
- **m12**: the review gives corrected text only for 968; 1293 is covered by L3; 1336 ("a value of the index $\alpha$") unchanged.
- **Point 5 survivors** (581, 582, 599 "principal columns"; 945, 1306, 1319; macro-box; 320; 1222, 1287): not classed as corrections ("needs the author's decision"); unchanged.

## Checks (run after the edits)

- `wc -l`: 1388.
- `git -C /Users/mgubi/ym-terminology diff --stat`: only `manuscript/HumanizeYM_v3/chapters/05-gaussian.tex` (216 insertions, 216 deletions); `git status --short` shows only that file modified.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1170 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.../scratchpad/v3build-ch05 monograph.tex`: exit 0, PDF written. In `monograph.log`: "undefined" (case-insensitive) 0 lines, "Overfull" 0 lines.
- Rendered pages were not inspected.

## Before and after, by line

**Line 7**

- before: `it supplies the inverse needed to construct a background field for`
- after: `it supplies the inverse needed to construct the critical configuration, the background field for`

**Line 14**

- before: `background field. The general block transformation algebra is`
- after: `critical configuration. The general block transformation algebra is`

**Line 20**

- before: `different averaging operation without checking its hypotheses. In particular, Ba{\l}aban's background field is a minimum of the action at fixed averages (his ``minimal configuration''), for $k$ steps at once; the critical configuration constructed in Section~\ref{ch05:stationary} is a stationary point of the fine action plus the penalty term of the block kernel, for one step.`
- after: `different averaging operation without checking its hypotheses. Moreover, Ba{\l}aban's background field is a minimum of the action at fixed averages (his ``minimal configuration''), for several steps at once; the critical configuration constructed in Section~\ref{ch05:stationary} is a stationary point of the fine action plus the penalty term of the block kernel, for one step.`

**Line 105**

- before: `The map $W$ sends a coarse field to the critical fine configuration. The`
- after: `The map $W$ sends a coarse field to the fine critical configuration. The`

**Line 312**

- before: `Fix the final smoothing order $j=j_n\ge4$ and the penalty $b>0$.`
- after: `Fix the final smoothing order $j=j_n\ge4$ and the penalty parameter $b>0$.`

**Line 351**

- before: `$c(1+|z_\mu|)$ for $z_\mu\ne0$; the case of the zero alias is bounded`
- after: `$c(1+|z_\mu|)$ for $z_\mu\ne0$; the case $z_\mu=0$ is bounded`

**Line 352**

- before: `directly by the finite sum. At the real zero alias the`
- after: `directly by the finite sum. At the zero alias with real momentum the`

**Line 360**

- before: `On the real zero alias the same factors have product bounded`
- after: `At the zero alias with real momentum the same factors have product bounded`

**Line 379**

- before: `through the subsequent, coarser steps $h+1,\ldots,n$. If these steps have total scaling factor`
- after: `through the subsequent, coarser steps $h+1,\ldots,n$, with accumulated symbol $f_{\rm suffix}$. If these steps have total scaling factor`

**Line 412**

- before: `For a nonzero real alias the denominator is bounded below`
- after: `For a real alias with $z\ne0$ the denominator is bounded below`

**Line 611**

- before: `written $A=Vd_{r+1}$ on a smaller strip, with the norm multiplied by a fixed factor.`
- after: `written $A=Vd_{r+1}$ on a smaller strip, with the norm increased by at most a fixed factor.`

**Line 689**

- before: `For each pair of consecutive stages (Section~\ref{ch10:choices}) choose the coarse modification`
- after: `For each pair of stages of one step (Section~\ref{ch10:choices}) choose the coarse modification`

**Line 712**

- before: `range over fixed finite coordinate sets. For a two-scale kernel,`
- after: `range over fixed finite coordinate sets. For a kernel between adjacent scales,`

**Line 730**

- before: `then identifies every coefficient. Alternatively, agreement of the subsequential limit`
- after: `then identifies every coefficient. Alternatively, agreement of the matrices of the subsequential`

**Line 731**

- before: `matrices on an unbounded sequence of side lengths of the torus suffices: for fixed $z$,`
- after: `limits on an unbounded sequence of side lengths of the torus suffices: for fixed $z$,`

**Line 740**

- before: `Fix a scale and the nested sequences of blocking parameters just described. The unmodified`
- after: `Fix a scale and the nested choice of parameters just described. The unmodified`

**Line 828**

- before: `and the limit of the periodized kernels along unbounded periods identify their limit on the infinite lattice.`
- after: `and the recovery of a kernel on $\ZZ^4$ from its periodizations along unbounded periods identify their limit on the infinite lattice.`

**Line 848**

- before: `theorem. Thus the subsequential limit matrices agree on every torus, and the`
- after: `theorem. Thus the matrices of the subsequential limits agree on every torus, and the`

**Line 849**

- before: `limit of the periodized kernels identifies the kernel on the infinite lattice. This proves convergence for the`
- after: `recovery from the periodizations identifies the kernel on the infinite lattice. This proves convergence for the`

**Line 857**

- before: `gradient correction for the averaging operation introduced below is a fixed finite-range`
- after: `gradient correction introduced below for the averaging operation is a fixed finite-range`

**Line 920**

- before: `links $V$, their pull-back under the block projection is`
- after: `links $V$, their pull-back under the parent map is`

**Line 937**

- before: `tree edges. Any spanning tree rooted at the block center is allowed here, where Ba{\l}aban has the tree of his contours $\Gamma_{y,x}$ rooted at a block corner; the gauge is used here as a chart, and it is a different construction from the axial gauge of the patch frames of Chapter~\ref{ch04:blocking}. The derivative of the chart at the identity is exactly`
- after: `tree edges. Any spanning tree rooted at the block center is allowed here, where Ba{\l}aban has the tree of his contours $\Gamma_{y,x}$ rooted at a block corner; the gauge is used here as a chart, and it is a different construction from the axial gauge of the local gauge transformations of Chapter~\ref{ch04:blocking}. The derivative of the chart at the identity is exactly`

**Line 968**

- before: `strictly on its minimizing branch. Every local value of the index $\alpha$ then selects the`
- after: `strictly on its minimizing branch. Every local value of the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking} then selects the`

**Line 1007**

- before: `estimate for the local gauge transformations, linear in the plaquette sum, controls the two discrepancies between root and local gauge transformation;`
- after: `estimate for the local gauge transformations, linear in the plaquette sum, controls the discrepancy at each of the two roots from its local gauge transformation;`

**Line 1156**

- before: `\section{A background field on a uniform neighborhood}`
- after: `\section{A critical configuration on a uniform neighborhood}`

**Line 1293**

- before: `local values of the index $\alpha$ agree there as functions of the full field.`
- after: `local values of the index $\alpha$ select the same operation there, as a function of the full field.`

**Line 1313**

- before: `give the coarse quadratic form as the Hessian of the reduced action. Equality of actions only on a`
- after: `give the coarse quadratic form as the Hessian of the reduced action. Equality of actions only on the`

**Line 1314**

- before: `previously selected critical-configuration map would not suffice for this argument.`
- after: `graph of one previously selected critical-configuration map would not suffice for this argument.`

**Line 1378**

- before: `For the nested selected sequences of blocking parameters, Proposition~\ref{ch05:horizon-limit}`
- after: `For the nested selected choice of parameters, Proposition~\ref{ch05:horizon-limit}`
