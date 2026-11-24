# Chapter 5 (05-gaussian.tex): long replacements shortened

File: /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/05-gaussian.tex. 51 lines edited, in place; line count 1388 (unchanged). Nothing staged or committed. Edit list as data: ch05-shorten-edits.py in this directory.

## Short terms introduced (defining sentence, line)

- **blocking sequence** — l. 303: "A finite \emph{blocking sequence} consists of odd ratios $L_1,\ldots,L_n\ge3$ and smoothing orders ...". Gloss at first use, l. 10: "blocking sequence (the list of block ratios and smoothing orders, defined in Section~\ref{ch05:histories})". Used at 281, 298 (title), 319, 449, 450, 695, 700, 703, 707, 757, 775, 783, 1368. No "sequence(s) of blocking parameters" remains.
- **link multipliers** — l. 335: "the multipliers $r_A$ of the averages along the links, the \emph{link multipliers}, compose by $r_A(Bt)r_B(t)=r_{AB}(t)$". Used at 760, 762.
- **periodization criterion** — l. 730-731: "agreement of the matrices of the subsequential limits on tori of unbounded side length suffices (the \emph{periodization criterion})". Used at 828, 849.
- **block axial chart** — l. 930: "The \emph{block axial chart}, the chart of the block axial gauge (the gauge in which the links of the chosen spanning tree of each block equal the identity), is" (eq. ch05:forest-chart). Used at 912 (title), 1061, 1078, 1153, 1234, 1289, 1304; replaces both "chart of the block axial gauge" and "coordinates of the block axial gauge".
- **quadratic hypothesis** — l. 1057-1058: "Identifying their sum with a chosen metric $H_f$ is an exact coefficient condition on the incoming path action, called the \emph{quadratic hypothesis} below." Used at 1303, 1374, 1382.

## Tighter phrasings without a new term

- zero-alias compounds: 425 "The zero-alias bounds give", 571 "zero-alias denominator", 796 "zero-alias summand", 817 "zero-alias centered-box factor".
- "noise estimate": 418 ("the noise estimate above"), 779 ("The noise estimate in Proposition ...") for "estimate of the accumulated/propagated noise".
- "infinite-lattice coefficients / kernels / limits": 735, 751, 820, 828, 849 (the phrase "infinite lattice coefficients" already stood at l. 634). The explicit "$\ZZ^4$" is dropped at 735 and 751; l. 711 still says $z\in\ZZ^4$.
- 656, 660: "such positions", "position" after "a fixed position within the block" at 654.
- 859: "operator $W$ of Section~\ref{ch05:transports}" (l. 535 already identifies it as $W_s$).
- 1007: "estimate \eqref{ch04:frame-first-power} for the local gauge transformations controls the discrepancies at the two roots" — the equation reference replaces "linear in the plaquette sum" (l. 1019 cites the same estimate).
- 1283: "Penalty terms and" (full name stands at 20 and 1163).
- 1290, 1375: "Poincar\'e-type inequality" with the equation reference instead of "in that gauge" / "in the block axial gauge".

## Long forms deliberately left

- 453 section title "The linearization of the critical configuration, the induced map on curvatures, and the curvature defect", 1081 subsection title, 1234, 1310: "linearization of the critical configuration" is the agreed name of $W$; no other section title in the manuscript contains math, so "the linearization $W$" was not put into titles. The 453 title is still long; author's decision.
- 967 "every condition on the minimum of the objective": once only; chapter 4 is not yet converted and has no name for this condition, so a shorter form ("minimum condition") could not be checked for exactness.
- 328 "accumulated symbol of the averaging operators": first, defining occurrence; later lines say "accumulated symbol".
- 654, 713 "position(s) within the block": first occurrence and one distant one.
- 805, 837 "criterion for subsequential limits" (four words).
- 976, 977, 986, 1005, 1018, 1020, 1045, 1163, 1214, 1339: once each, clear; 1005 is an intended disambiguation.
- 968, 1293, 1336 "local value(s) of the index $\alpha$".
- 740, 1378 "nested (selected) choice of parameters": already short in the current text.

Pre-existing, not touched: l. 1302-1304 reads "satisfying \eqref{ch05:path-budget}, the quadratic hypothesis in \eqref{ch05:actual-hessian}" with no "and" (it was so before the conversion as well).

## Checks (run)

- `wc -l`: 1388.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1174 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf ... -outdir=.../scratchpad/v3build-ch05 monograph.tex`: exit 0, PDF written; in monograph.log "undefined" 0, "Overfull" 0.
- Diff reread line by line for sentences that parse; rendered pages were not inspected visually.

## Lines changed (before / after)

### 10
- before: `which survive changes of the lattice size and of the sequence of blocking parameters.`
- after: `which survive changes of the lattice size and of the blocking sequence (the list of block ratios and smoothing orders, defined in Section~\ref{ch05:histories}).`

### 281
- before: `over every admitted sequence of blocking parameters. These are precisely the`
- after: `over every admitted blocking sequence. These are precisely the`

### 298
- before: `\section{Uniform estimates over finite sequences of blocking parameters}`
- after: `\section{Uniform estimates over finite blocking sequences}`

### 303
- before: `A finite sequence of blocking parameters consists of odd ratios $L_1,\ldots,L_n\ge3$ and`
- after: `A finite \emph{blocking sequence} consists of odd ratios $L_1,\ldots,L_n\ge3$ and`

### 319
- before: `The constants depend on $j,b$, but not on the length of the sequence,`
- after: `The constants depend on $j,b$, but not on the length of the blocking sequence,`

### 335
- before: `$f(\theta)r_{M_n}(\theta_\mu)$: the multipliers of the averages along the links compose by`
- after: `$f(\theta)r_{M_n}(\theta_\mu)$: the multipliers $r_A$ of the averages along the links, the \emph{link multipliers}, compose by`

### 418
- before: `Together with the estimate of the accumulated noise it proves a uniform`
- after: `Together with the noise estimate above it proves a uniform`

### 425
- before: `The bounds for the symbol at the zero alias give positive real lower bounds for`
- after: `The zero-alias bounds give positive real lower bounds for`

### 449
- before: `This proves uniform bounds for arbitrary finite sequences of blocking parameters.`
- after: `This proves uniform bounds for arbitrary finite blocking sequences.`

### 450
- before: `Convergence for prescribed growing sequences of blocking parameters is`
- after: `Convergence for prescribed growing blocking sequences is`

### 571
- before: `corresponding denominator at the zero alias is`
- after: `corresponding zero-alias denominator is`

### 656
- before: `has bound $CL^{-3}$. A Gram product sums over $L^4$ positions within the block.`
- after: `has bound $CL^{-3}$. A Gram product sums over $L^4$ such positions.`

### 660
- before: `position within the block, so it introduces no further sum over positions.`
- after: `position, so it introduces no further sum over positions.`

### 695
- before: `sequences of blocking parameters ending at a fixed order.`
- after: `blocking sequences ending at a fixed order.`

### 700
- before: `The curvature metrics and the operators $W$, $T$ in this section are those of Sections~\ref{ch05:curvature} and~\ref{ch05:transports}; their sequences of blocking parameters now vary while the observation scale stays fixed.`
- after: `The curvature metrics and the operators $W$, $T$ in this section are those of Sections~\ref{ch05:curvature} and~\ref{ch05:transports}; their blocking sequences now vary while the observation scale stays fixed.`

### 703
- before: `nested sequences of blocking parameters used in the construction. The nesting is essential:`
- after: `nested blocking sequences used in the construction. The nesting is essential:`

### 707
- before: `$N$ at its fine end. An arbitrary succession of bounded sequences of blocking parameters need`
- after: `$N$ at its fine end. An arbitrary succession of bounded blocking sequences need`

### 731
- before: `limits on an unbounded sequence of side lengths of the torus suffices: for fixed $z$,`
- after: `limits on tori of unbounded side length suffices (the \emph{periodization criterion}): for fixed $z$,`

### 735
- before: `This argument identifies the coefficients on the infinite lattice $\ZZ^4$, not merely a`
- after: `This argument identifies the infinite-lattice coefficients, not merely a`

### 751
- before: `All limits are for the chosen kernels on the infinite lattice $\ZZ^4$ and their`
- after: `All limits are for the chosen infinite-lattice kernels and their`

### 757
- before: `Let $d=N-m$ be the depth of the sequence of blocking parameters and $M_{d,m}$ its total scaling factor.`
- after: `Let $d=N-m$ be the depth of the blocking sequence and $M_{d,m}$ its total scaling factor.`

### 760
- before: `product of the centered-box factors and the multipliers of the averages along the links used in`
- after: `product of the centered-box factors and the link multipliers used in`

### 762
- before: `single-step directional symbol at scale $m$, including the multiplier`
- after: `single-step directional symbol at scale $m$, including the link multiplier`

### 763
- before: `$r_{L_m}(\theta_\mu)$ of the average along the link. Composition gives`
- after: `$r_{L_m}(\theta_\mu)$. Composition gives`

### 775
- before: `The accumulated noise is also convergent. Extending the sequence of blocking parameters adds one`
- after: `The accumulated noise is also convergent. Extending the blocking sequence adds one`

### 779
- before: `therefore increases with depth. The estimate of the propagated noise in`
- after: `therefore increases with depth. The noise estimate in`

### 783
- before: `not a monotonicity assertion for arbitrary sequences of blocking parameters of the same length.`
- after: `not a monotonicity assertion for arbitrary blocking sequences of the same length.`

### 796
- before: `summand at the zero alias converges by the same argument without an alias sum.`
- after: `zero-alias summand converges by the same argument without an alias sum.`

### 817
- before: `the centered-box factor at the zero alias is nonzero on the real base cube and`
- after: `the zero-alias centered-box factor is nonzero on the real base cube and`

### 820
- before: `uniform exponential bounds identify unique limits on the infinite lattice for $W,T$.`
- after: `uniform exponential bounds identify unique infinite-lattice limits for $W,T$.`

### 828
- before: `and the recovery of a kernel on $\ZZ^4$ from its periodizations along unbounded periods identify their limit on the infinite lattice.`
- after: `and the periodization criterion identify their infinite-lattice limit.`

### 849
- before: `recovery from the periodizations identifies the kernel on the infinite lattice. This proves convergence for the`
- after: `periodization criterion identifies the infinite-lattice kernel. This proves convergence for the`

### 859
- before: `operator $W$ built with the linear averaging operator also preserves convergence. These are statements`
- after: `operator $W$ of Section~\ref{ch05:transports} also preserves convergence. These are statements`

### 912
- before: `\section{The averaging operation and the coordinates of the block axial gauge}`
- after: `\section{The averaging operation and the block axial chart}`

### 930
- before: `is one on every tree edge. The chart of the block axial gauge, the gauge in which the links of the chosen spanning tree of each block equal the identity, is`
- after: `is one on every tree edge. The \emph{block axial chart}, the chart of the block axial gauge (the gauge in which the links of the chosen spanning tree of each block equal the identity), is`

### 1007
- before: `estimate for the local gauge transformations, linear in the plaquette sum, controls the discrepancy at each of the two roots from its local gauge transformation;`
- after: `estimate \eqref{ch04:frame-first-power} for the local gauge transformations controls the discrepancies at the two roots;`

### 1058
- before: `condition on the incoming path action.`
- after: `condition on the incoming path action, called the \emph{quadratic hypothesis} below.`

### 1061
- before: `at the identity. Therefore the second derivative of the chart of the block axial gauge does`
- after: `at the identity. Therefore the second derivative of the block axial chart does`

### 1078
- before: `This proves the vertical gap for the chart of the block axial gauge, rather than`
- after: `This proves the vertical gap for the block axial chart, rather than`

### 1153
- before: `for the coordinates of the block axial gauge. Gauge-invariant quadratic insertions see the same`
- after: `for the block axial chart. Gauge-invariant quadratic insertions see the same`

### 1234
- before: `We retain the distinction from Section~\ref{ch05:actual-tangent}: $W_a$ is the smooth representative of the linearization $W$ of the critical configuration, whereas $W_F$ is its representative in the coordinates of the block axial gauge. They have the same curvature, but the fine-difference bounds apply to $W_a$.`
- after: `We retain the distinction from Section~\ref{ch05:actual-tangent}: $W_a$ is the smooth representative of the linearization $W$ of the critical configuration, whereas $W_F$ is its representative in the block axial chart. They have the same curvature, but the fine-difference bounds apply to $W_a$.`

### 1283
- before: `on a common complex ball. Penalty terms of the block kernel and`
- after: `on a common complex ball. Penalty terms and`

### 1289
- before: `For the chart \eqref{ch05:forest-chart} of the block axial gauge, the deterministic`
- after: `For the block axial chart \eqref{ch05:forest-chart}, the deterministic`

### 1290
- before: `Poincar\'e-type inequality in that gauge and the Hessian identification have already been proved`
- after: `Poincar\'e-type inequality and the Hessian identification have already been proved`

### 1303
- before: `hypothesis on the quadratic part of the incoming action in`
- after: `quadratic hypothesis in`

### 1304
- before: `\eqref{ch05:actual-hessian}. The averaging operation and the coordinates of the block axial gauge`
- after: `\eqref{ch05:actual-hessian}. The averaging operation and the block axial chart`

### 1368
- before: `For each fixed smoothing order, the construction for finite sequences of blocking parameters`
- after: `For each fixed smoothing order, the construction for finite blocking sequences`

### 1374
- before: `path action with the explicit local bound and the hypothesis on the quadratic`
- after: `path action with the explicit local bound and the quadratic hypothesis`

### 1375
- before: `part just stated; its Poincar\'e-type inequality in the block axial gauge and the`
- after: `just stated; its Poincar\'e-type inequality \eqref{ch05:tree-comparison} and the`

### 1382
- before: `checked against \eqref{ch05:path-budget} and the hypothesis on the quadratic`
- after: `checked against \eqref{ch05:path-budget} and the quadratic hypothesis`

### 1383
- before: `part \eqref{ch05:actual-hessian}. The common minimizing`
- after: `\eqref{ch05:actual-hessian}. The common minimizing`

