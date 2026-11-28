# Corrections applied after the review of chapters 4 and 5 (`ch04-review.md`)

Worktree `/Users/mgubi/ym-terminology`. Files edited: `chapters/04-blocking.tex` (29 lines, still 677), `chapters/05-gaussian.tex` (32 lines, still 1388), `figures/block-paths.tex` (caption, 4 lines, still 44), `references.bib` (3 entries appended, 21 lines). Nothing staged, committed, pushed or reverted. All edits are within lines; no symbol, label or display was renamed (one word inside `\text{…}` at 5:1028 changed, see mismatch 4).

## 1. The three ERRORs

- **4:16 (A1).** Now `unlike in~\cite{Balaban1984Propagators}, a step is not followed by a rescaling to the unit lattice`. The reviewer proposed "some of Bałaban's papers (for instance [B84a])". Altered: the *Literature* line of *step* names B84a, B95, D1; only B84a has a key and is about gauge fields, so the sentence now speaks of that paper alone and generalises to nothing.
- **4:452 (A2).** Both done: the sentence reads "The word regular has two technical uses, as in his papers: …" (reviewer's text), AND the third use at 532 and 584 was removed, so the sentence is true of the chapter. Basis: the entry *regular* (adopted decision: "The book then has the two uses of 'regular' that Bałaban has") and the renaming in *regular activity*. The entry *regular expression* (basis I) proposes "the smooth expression with the indicators held fixed"; I did not write "smooth", which the chapter does not support (`E_i^reg` has "the required number" of derivatives, 4:437–438). 532: "the regular expressions" → "the local expressions" (the sentence itself continues "with the event indicators held fixed"; "local … expressions" is the chapter's word at 504). 584: "the regular local expression" → "the local expression $E_i^{\rm reg}$ itself" (the clause "no derivative of $h_{X_i}$ is included" follows). After this, "regular" occurs in chapter 4 only in "regular part of the action", "regularity condition", "regular configurations" (428, of Bałaban's spaces) and the symbol `E^reg`.
- **5:1007 (B1).** Reviewer's text used: "estimate for the local gauge transformations in the proof of Lemma~\ref{ch04:predictor-comparison}, linear in the plaquette sum, controls the discrepancies at the two roots;". That proof treats both branches (4:357–365). In addition (not in the review's corrected text, but the review notes the same narrowing there) **5:1019**: "are bounded by the sum in \eqref{ch04:frame-first-power}" → "are bounded by the sum over the patch estimated in the proof of Lemma~\ref{ch04:predictor-comparison} on either branch"; the sum meant is the unlabelled display 4:371–374, valid on both branches by 4:364–365.

## 2. Citations added and bib entries

| line | statement | citation | dictionary evidence |
|---|---|---|---|
| 4:16 | rescaling after a step | `Balaban1984Propagators` | *step*: B84a |
| 4:226 | delta function in place of `q_{bβ}` | `Balaban1984Propagators,Balaban1985Averaging,Balaban1987RG`; subject changed from "Bałaban's renormalization transformations for gauge fields" to "The renormalization transformations for gauge fields in [these]" | *penalty parameter*: B84a (1.12), B85a (10), B87 (0.17) |
| 4:428 | regularity condition; spaces of regular configurations | `Balaban1985Spaces`; "The term regularity condition is that of [B85b], where the spaces of regular configurations carry bounds on the plaquette variables, depending on the scale, on a nested sequence of domains, and a second condition" | *`Bad_m(U)`*: B85b pp. 75, 77, incl. the second condition (1.9) |
| 4:452 | localized term, localization domain, regular part of the action | `Balaban1987RG,Balaban1988Expansions` | *regular activity*: B87 pp. 256–257, B88b p. 259 |
| 4:452 | "activity" | `Balaban1988Cluster`; "Bałaban uses the word activity for polymer activities only" → "… for the activities of a polymer expansion [B88a]" (positive statement, one paper) | *activity*: B88a p. 14 |
| 4:591 | linear size | `Balaban1987RG`; "in Bałaban's papers" → "in [B87]" | *connected covering number*: B87 p. 257 |

Appended to `references.bib` (format of `Balaban1984Propagators`):
- `Balaban1985Averaging` (CMP 98 (1985) 17–51, doi 10.1007/BF01211042) and `Balaban1985Spaces` (CMP 99 (1985) 75–102, doi 10.1007/BF01466594), data as given.
- `Balaban1988Cluster`: T. Bałaban, Renormalization group approach to lattice gauge field theories. II. Cluster expansions, CMP 116 (1988) 1–22. NOT in the brief: added because the "activity" sentence rests on this paper only; data copied from Appendix L of the dictionary (B88a); **no DOI entered, not verified** (no external services). Remove the cite and entry if unwanted.
- `Balaban1988Convergent` not created: the paper exists as `Balaban1988Expansions` (CMP 119, 243–285), which is used.

## 3. Reviewer corrections altered, and additions

- A1 (4:16): see above.
- A4 (4:189–190): the reviewer's sentence ("The value of the … averaging operation, obtained on the first of two branches by projecting …, minimizes") still says the value minimizes on both branches. Written: "On the first of its two branches, the value of the gauge-covariant \emph{averaging operation} is obtained by projecting the weighted / average of the transporters to the group; it then minimizes".
- A5 (4:65): reviewer's text with "strictly below" (as at 4:57).
- A11 (4:161): "sections, one in each dimension" would introduce a second word beside "hyperplane" of 147–151; written "hyperplanes of the successive slices, one in each dimension, specify an initial point". 147 as proposed.
- 4:428: reviewer's text, but "is that of [B85b], where …" instead of "is Bałaban's; his …", and the second condition mentioned (the entry records it).
- 4:591, 4:226: paper named instead of "Bałaban's papers / Bałaban's" (brief, point 3).
- MINOR 4:605: the reviewer's "localization domain or exclusion support" does not fit: the anchored sum is over localized terms only. Written "the terms whose localization domain contains $x$, a \emph{containing-site} sum like the second".
- MINORs on unchanged lines, applied: 121 "Coordinatewise minimization" → "Minimization over the value at one point"; 127 "old coordinate" → "old value"; 150 "its transported link on the" → "its translate, along the last coordinate, in the"; 358, 367 "gauge $H$" → "gauge transformation $H$"; 379 "middle straight path" → "middle straight contour". NOT changed: 362 "pure gauge" (standard), 349–356 "coordinate-path gauge", "path counting" (paths that are counted; rewriting 349 needs the author), 26 (reviewer: acceptable), 505–506 "support" of an expression.
- B3 (5:1302–1303): the proposed line 1303 "and the quadratic hypothesis leading to" left "…, the / and the …"; written 1302 "… \eqref{ch05:path-budget} and the", 1303 "quadratic hypothesis leading to". Same wording at 5:1382 ("the quadratic hypothesis leading to / \eqref{ch05:actual-hessian}"), since B4 notes that the equation is the Hessian formula, not the hypothesis.
- B MINOR: `$\ZZ^4$` restored at 735, 751, 828; "of the block kernel" restored at 1283; 760 "the centered-box factors and the link multipliers used in (history-filter)" → "the link multipliers and the centered-box factors of (history-filter)".
- All other corrections (A3, A6, A7, A-L3, A-L4, A-L5, A-L6, 456, B2, B4, B5, B6) use the reviewer's text.

## 4. The 11 mismatches

1. One block transformation: table → "renormalization transformation"/"step". 5:14 "The general algebra of renormalization transformations", 5:84 section title "The exact Gaussian renormalization transformation" (label unchanged), 5:114 "the identities for renormalization transformations".
2. Weight of the index: *branch masses* → "probability weights". 5:970 "The uniform probability weights of its redundant values are constant there."
3. `w^av`: chapter 4 "averaging weight". 5:153–154 "averaging weight … with sum one"; 5:993 "with the averaging / weights".
4. Box of radius `(j+7)L`: "macro-box" in both (5:1028 inside `\text{}`, 1031, 1032). The dictionary proposes "enlarged block"; not used, as in the chapter 4 conversion (`ch04-apply.md`: the entry *block-average patch* warns against "block" for overlapping boxes, and chapter 6, outside this task, says macro-box). **Deviation from the dictionary; needs the author's decision.**
5. 5:206 "gauge-covariant".
6. Patch `Ly + 𝔹_R`: dictionary (*block-average patch*) → "patch of the averaging operation", in 4:173 (definition), 4:369, 5:976 ("at $y$", as in chapter 4). This also settles A10.
7. Site `Ly`, normalization: 5:995 "at the coarse endpoints" (4:181); 5:997 "the normalization of the local gauge transformation at the patch center" (4:43, 51). "Block roots"/"the two roots" at 5:1002–1018 kept: there they are roots of the spanning trees of 5:917, which *root* 1 keeps.
8. 4:210 no longer says "choose" (A-L4); 5:968, 1293 "specifies", "specify" (the verb of 4:77).
9. 5:861 "localized terms and large-field activities of the nonlinear step" (*array*, *activity*).
10. 4:234 "the block kernel of the step" (A6).
11. 5:902 "at every real point $x$"; "base point" is left to the localized terms.

## 5. Figure caption (`figures/block-paths.tex` 38–41)

Short title "Fine contours and local gauge transformations in the averaging operation"; "Two transporters in the weighted average $\bar Y_e$"; "Each solid contour"; "the factors of the local gauge transformations"; "the transporter $Y_{e,z}$". Compiles in the monograph build.

## 6. To record in the dictionary

- *root* 1: chapter 4 says **"initial point"** (36, 89, 106, 161, 279), the *Literature* word (B85a p. 24), not the *Proposed* "base point", because *anchor* 1 also proposes "base point" (435, 573, 606, 657). The dictionary should adopt "initial point (of the axial gauge)". Nothing edited.
- *macro-box*: kept (mismatch 4). *regular expression*: resolved as "local expression" (ERROR 2). *block-average patch*: applied.

## 7. Checks run

- `wc -l`: 677, 1388, 44.
- `git diff --stat`: 04-blocking.tex 354 (includes the earlier uncommitted conversion), 05-gaussian.tex 64, block-paths.tex 8, references.bib 21; 4 files, 234 insertions, 213 deletions.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1179 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf … -outdir=…/v3build-ch04 monograph.tex`: exit 0, run to completion (bibtex included; the three new keys are in `monograph.bbl`). In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. BibTeX: one warning, "empty year in LeblSCV" (older).
- Diff reread line by line; one defect found and repaired during rereading (5:1302–1303, above). Rendered pages not inspected visually.

## 8. Every changed line (before / after)

### 04-blocking.tex

**16**
- before: `$m+1\to m$; unlike in several of Ba\l{}aban's papers, a step is not followed by a rescaling to the unit lattice. Write $L=L_m$, fix a positive integer \emph{smoothing order} $j$ (the number of convolution factors in the averaging weight $w^{\rm av}$ of Section~\ref{ch04:kernel-section}),`
- after: `$m+1\to m$; unlike in~\cite{Balaban1984Propagators}, a step is not followed by a rescaling to the unit lattice. Write $L=L_m$, fix a positive integer \emph{smoothing order} $j$ (the number of convolution factors in the averaging weight $w^{\rm av}$ of Section~\ref{ch04:kernel-section}),`

**65**
- before: `This condition, the \emph{loop condition}, includes every order $o_0$, so it does not privilege a preliminary`
- after: `The condition that all these distances be strictly below $\delta_{\rm fr}$, the \emph{loop condition}, includes every order $o_0$, so it does not privilege a preliminary`

**121**
- before: `Then $\|\bar h-1\|_{\mathrm F}\le2d$. Coordinatewise minimization shows`
- after: `Then $\|\bar h-1\|_{\mathrm F}\le2d$. Minimization over the value at one point shows`

**127**
- before: `it adds a term whose maximum is attained at the old coordinate $h_x$.`
- after: `it adds a term whose maximum is attained at the old value $h_x$.`

**132**
- before: `Normalize two minimizers $h,k$ in this way and set`
- after: `Multiply two minimizers $h,k$ on the left in this way, so that $1$ is nearest to each centroid, and set`

**147**
- before: `hyperplane perpendicular to the last coordinate whose internal plaquette sum`
- after: `hyperplane of the slice perpendicular to the last coordinate whose internal plaquette sum`

**150**
- before: `to one. Every remaining link differs from its transported link on the`
- after: `to one. Every remaining link differs from its translate, along the last coordinate, in the`

**161**
- before: `hyperplanes specify an initial point. At $r=4$ the bound is \eqref{ch04:axial-eligible}`
- after: `hyperplanes of the successive slices, one in each dimension, specify an initial point. At $r=4$ the bound is \eqref{ch04:axial-eligible}`

**173**
- before: `$Ly+\mathbb B_R$ centered at a coarse site $y$, the \emph{patch of the local gauge transformation} at $y$. Write $h_{y,z}$ for the value of its`
- after: `$Ly+\mathbb B_R$ centered at a coarse site $y$, the \emph{patch of the averaging operation} at $y$. Write $h_{y,z}$ for the value of its`

**189**
- before: `Put $\bar Y_e=\sum_z w_z^{\rm av}Y_{e,z}$. The gauge-covariant \emph{averaging operation}, obtained by projecting the weighted`
- after: `Put $\bar Y_e=\sum_z w_z^{\rm av}Y_{e,z}$. On the first of its two branches, the value of the gauge-covariant \emph{averaging operation} is obtained by projecting the weighted`

**190**
- before: `average of the transporters to the group, minimizes`
- after: `average of the transporters to the group; it then minimizes`

**210**
- before: `let the value $z$ of the index choose $Q_e^{\rm pred}=Y_{e,z}$ with probability`
- after: `let the index take the value $z$, and set $Q_e^{\rm pred}=Y_{e,z}$, with probability`

**226**
- before: `Fix the \emph{penalty parameter} $b>0$ of the block kernel. Ba\l{}aban's renormalization transformations for gauge fields have a delta function in place of the densities $q_{b\beta}$ used below, so that there the coarse field equals the average exactly. For $\gamma\ge0$, let`
- after: `Fix the \emph{penalty parameter} $b>0$ of the block kernel. The renormalization transformations for gauge fields in~\cite{Balaban1984Propagators,Balaban1985Averaging,Balaban1987RG} have a delta function in place of the densities $q_{b\beta}$ used below, so that there the coarse field equals the average exactly. For $\gamma\ge0$, let`

**234**
- before: `For $\beta\ge0$, define the kernel of the step and its action on fine densities by`
- after: `For $\beta\ge0$, define the block kernel of the step and its action on fine densities by`

**315**
- before: `averaging operation of \eqref{ch04:predictor-cost}, every choice, of positive probability weight,`
- after: `averaging operation of \eqref{ch04:predictor-cost}, every value of positive probability weight`

**358**
- before: `any comparison gauge $H$. For a minimizing local gauge transformation $f$, this gives a`
- after: `any comparison gauge transformation $H$. For a minimizing local gauge transformation $f$, this gives a`

**367**
- before: `Choose an axial gauge $H$ on the macro-box of radius $(j+7)L$. The`
- after: `Choose an axial gauge transformation $H$ on the macro-box of radius $(j+7)L$. The`

**369**
- before: `$E(H\cdot U)\le C_jL\mathcal P_y(U)$. On each translated patch of a local gauge transformation,`
- after: `$E(H\cdot U)\le C_jL\mathcal P_y(U)$. On each translated patch of the averaging operation,`

**379**
- before: `For the middle straight path, each of its $L$ translations is injective,`
- after: `For the middle straight contour, each of its $L$ translations is injective,`

**428**
- before: `Thus every plaquette meeting $X$ must have $\chi(U_\square)\le t_m$. The term is Ba\l{}aban's, who imposes regularity conditions on the plaquette variables on a nested sequence of domains with scale-dependent bounds; here the condition is a single inequality at one scale, and the large-field set is neither enlarged nor summed over. This definition is`
- after: `Thus every plaquette meeting $X$ must have $\chi(U_\square)\le t_m$. The term regularity condition is that of~\cite{Balaban1985Spaces}, where the spaces of regular configurations carry bounds on the plaquette variables, depending on the scale, on a nested sequence of domains, and a second condition; here the condition is a single inequality at one scale, and the large-field set is neither enlarged nor summed over. This definition is`

**452**
- before: `The names localized term, localization domain and regular part of the action are Ba\l{}aban's. His localized terms are analytic, one for each connected localization domain, and bounded term by term; those used here are real Borel functions with finitely many derivatives, have a base point and an arbitrary localization domain, and are summed in a weighted $\ell^1$ norm. The word regular thus has two uses, as in his papers: the regular part of the action, and the regularity condition. Ba\l{}aban uses the word activity for polymer activities only; its use for the large-field terms is particular to this book. Neither a localized term nor a large-field activity is assumed nonnegative. Both may be indexed by a`
- after: `The names localized term, localization domain and regular part of the action are Ba\l{}aban's~\cite{Balaban1987RG,Balaban1988Expansions}. His localized terms are analytic, one for each connected localization domain, and bounded term by term; those used here are real Borel functions with finitely many derivatives, have a base point and an arbitrary localization domain, and are summed in a weighted $\ell^1$ norm. The word regular has two technical uses, as in his papers: the regular part of the action, and the regularity condition. Ba\l{}aban uses the word activity for the activities of a polymer expansion~\cite{Balaban1988Cluster}; its use for the large-field terms is particular to this book. Neither a localized term nor a large-field activity is assumed nonnegative. Both may be indexed by a`

**456**
- before: `$Y_i$ determines exclusion and coverage: the $Y_i$ of each subfamily in the sum below will be disjoint.`
- after: `$Y_i$ determines exclusion and coverage: the $Y_i$ of each subfamily in the sum below will be pairwise disjoint.`

**489**
- before: `The distance is periodic and measured in lattice units. We call the condition in \eqref{ch04:relaxed-test} the \emph{relaxed regularity condition} at $x$: the regularity condition with the exponentially weighted threshold $t_m e^{\operatorname{dist}(x,y)/R^{\rm rel}}$. Although written`
- after: `The distance is periodic and measured in lattice units. We call the condition in \eqref{ch04:relaxed-test} the \emph{relaxed regularity condition} at $x$: the regularity condition on the whole lattice, with $t_m$ replaced by the threshold $t_m e^{\operatorname{dist}(x,y)/R^{\rm rel}}$ growing exponentially with the distance from $x$. Although written`

**532**
- before: `refer to the regular expressions on the domains where the regularity condition holds, with the event indicators`
- after: `refer to the local expressions on the domains where the regularity condition holds, with the event indicators`

**539**
- before: `The indices of the localized terms and of the large-field activities, and the exclusion supports of the latter, are those of Definition~\ref{ch04:activities}. Their dependence sets also contain the links needed for every condition; the two sorts of support must remain distinct in the sums below.`
- after: `The indices of the localized terms and of the large-field activities, and the exclusion supports of the latter, are those of Definition~\ref{ch04:activities}. The dependence sets of the large-field activities also contain the links needed for every condition; the two sorts of support must remain distinct in the sums below.`

**584**
- before: `domain defined by the regularity condition, interpreted through the regular local expression;`
- after: `domain defined by the regularity condition, interpreted through the local expression $E_i^{\rm reg}$ itself;`

**591**
- before: `supports without requiring a support itself to be connected; it plays the role of the linear size of a localization domain in Ba\l{}aban's papers.`
- after: `supports without requiring a support itself to be connected; the covering number plays the role of the linear size of a localization domain in~\cite{Balaban1987RG}.`

**605**
- before: `exclusion support. Replacing an anchored sum by a sum over the terms whose support contains $x$, a \emph{containing-site} sum,`
- after: `exclusion support. Replacing an anchored sum by a sum over the terms whose localization domain contains $x$, a \emph{containing-site} sum like the second,`

**651**
- before: `$q,\varpi,\sigma$ may depend on the \emph{stage} $J_m$ in force at scale $m$ (a stage specifies finitely many derivative orders, support exponents, path widths and coefficient bounds; see Section~\ref{ch10:choices}); that index`
- after: `$q,\varpi,\sigma$ may depend on the \emph{stage} $J_m$ in force at scale $m$ (a stage specifies finitely many derivative orders, support exponents, path widths and coefficient bounds; see Section~\ref{ch10:choices}); the stage index`

(29 lines changed)


### 05-gaussian.tex

**14**
- before: `critical configuration. The general block transformation algebra is`
- after: `critical configuration. The general algebra of renormalization transformations is`

**84**
- before: `\section{The exact Gaussian block transformation}`
- after: `\section{The exact Gaussian renormalization transformation}`

**114**
- before: `real quadratic specialization of the block transformation identities in`
- after: `real quadratic specialization of the identities for renormalization transformations in`

**153**
- before: `odd $L\ge3$. Let $w(z)$ be a finitely supported real averaging kernel`
- after: `odd $L\ge3$. Let $w(z)$ be a finitely supported real averaging weight`

**154**
- before: `of total mass one, periodized on the fine lattice, and use the linear averaging operator`
- after: `with sum one, periodized on the fine lattice, and use the linear averaging operator`

**206**
- before: `quadratic form of a particular gauge-equivariant averaging operation additionally`
- after: `quadratic form of a particular gauge-covariant averaging operation additionally`

**731**
- before: `limits on tori of unbounded side length suffices (the \emph{periodization criterion}): for fixed $z$,`
- after: `limits on a sequence of tori with unbounded side lengths suffices (the \emph{periodization criterion}): for fixed $z$,`

**735**
- before: `This argument identifies the infinite-lattice coefficients, not merely a`
- after: `This argument identifies the coefficients on the infinite lattice $\ZZ^4$, not merely a`

**751**
- before: `All limits are for the chosen infinite-lattice kernels and their`
- after: `All limits are for the chosen kernels on the infinite lattice $\ZZ^4$ and their`

**760**
- before: `product of the centered-box factors and the link multipliers used in`
- after: `product of the link multipliers and the centered-box factors of`

**828**
- before: `and the periodization criterion identify their infinite-lattice limit.`
- after: `and the periodization criterion identify their limit on the infinite lattice $\ZZ^4$.`

**859**
- before: `operator $W$ of Section~\ref{ch05:transports} also preserves convergence. These are statements`
- after: `operator $W=W_s$ of Section~\ref{ch05:transports} also preserves convergence. These are statements`

**861**
- before: `nonlinear activity arrays or of marked integral maps; those require`
- after: `localized terms and large-field activities of the nonlinear step, or of marked integral maps; those require`

**902**
- before: `argument is justified if, at every real base point $x$, the matrices`
- after: `argument is justified if, at every real point $x$, the matrices`

**968**
- before: `strictly on its minimizing branch. Every local value of the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking} then selects the`
- after: `strictly on its minimizing branch. Every local value of the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking} then specifies the`

**970**
- before: `whole common ball. Redundant uniform branch masses are constant there.`
- after: `whole common ball. The uniform probability weights of its redundant values are constant there.`

**976**
- before: `signed sum along a coordinate path in the patch of the local gauge transformation at $Ly$. The`
- after: `signed sum along a coordinate path in the patch of the averaging operation at $y$. The`

**993**
- before: `Here $M$ is exactly the linear averaging operator, the straight length-$L$ average with the convolution`
- after: `Here $M$ is exactly the linear averaging operator, the straight length-$L$ average with the averaging`

**995**
- before: `also by differentiating gauge covariance at block roots. Each contour has`
- after: `also by differentiating gauge covariance at the coarse endpoints. Each contour has`

**997**
- before: `at most $C_jL$. These statements include the root normalization. Dropping`
- after: `at most $C_jL$. These statements include the normalization of the local gauge transformation at the patch center. Dropping`

**1007**
- before: `estimate \eqref{ch04:frame-first-power} for the local gauge transformations controls the discrepancies at the two roots;`
- after: `estimate for the local gauge transformations in the proof of Lemma~\ref{ch04:predictor-comparison}, linear in the plaquette sum, controls the discrepancies at the two roots;`

**1019**
- before: `are bounded by the sum in \eqref{ch04:frame-first-power}, so this step`
- after: `are bounded by the sum over the patch estimated in the proof of Lemma~\ref{ch04:predictor-comparison} on either branch, so this step`

**1028**
- before: ` |a_e|\le C_{j,L}\sum_{p\text{ in the macro-patch at }y}|(d_{1,f}a)_p|`
- after: ` |a_e|\le C_{j,L}\sum_{p\text{ in the macro-box at }y}|(d_{1,f}a)_p|`

**1031**
- before: `Square, use the finite macro-patch cardinality, and sum over edges. A fine`
- after: `Square, use the finite cardinality of the macro-box, and sum over edges. A fine`

**1032**
- before: `plaquette belongs to a bounded number of macro-patches, and each coarse`
- after: `plaquette belongs to a bounded number of macro-boxes, and each coarse`

**1058**
- before: `condition on the incoming path action, called the \emph{quadratic hypothesis} below.`
- after: `condition on the incoming path action; with $H_f\ge\varepsilon I$ it is called the \emph{quadratic hypothesis} below.`

**1153**
- before: `for the block axial chart. Gauge-invariant quadratic insertions see the same`
- after: `for the representative $W_F$. Gauge-invariant quadratic insertions see the same`

**1283**
- before: `on a common complex ball. Penalty terms and`
- after: `on a common complex ball. Penalty terms of the block kernel and`

**1293**
- before: `local values of the index $\alpha$ select the same operation there, as a function of the full field.`
- after: `local values of the index $\alpha$ specify the same operation there, as a function of the full field.`

**1302**
- before: `uncut path actions satisfying \eqref{ch05:path-budget}, the`
- after: `uncut path actions satisfying \eqref{ch05:path-budget} and the`

**1303**
- before: `quadratic hypothesis in`
- after: `quadratic hypothesis leading to`

**1382**
- before: `checked against \eqref{ch05:path-budget} and the quadratic hypothesis`
- after: `checked against \eqref{ch05:path-budget} and the quadratic hypothesis leading to`

(32 lines changed)


### figures/block-paths.tex

**38**
- before: `\caption[Fine paths and endpoint frames in the block average]{Two connectors in the matrix average $\bar Y_e$ for $e=(y,\mu)$,`
- after: `\caption[Fine contours and local gauge transformations in the averaging operation]{Two transporters in the weighted average $\bar Y_e$ for $e=(y,\mu)$,`

**39**
- before: `shown in a coordinate plane. Each solid path traverses $L$ fine links.`
- after: `shown in a coordinate plane. Each solid contour traverses $L$ fine links.`

**40**
- before: `The dashed arrows are frame factors, which can depend on the whole`
- after: `The dashed arrows are the factors of the local gauge transformations, which can depend on the whole`

**41**
- before: `patch. They give the framed transport $Y_{e,z}$ the same coarse`
- after: `patch. They give the transporter $Y_{e,z}$ the same coarse`

(4 lines changed)
