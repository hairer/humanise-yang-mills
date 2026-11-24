# Forest average: draft repair of v3 chapter 9

Worktree /Users/mgubi/ym-terminology (branch claude/v3-terminology-dictionary). Nothing committed. Date 24 November 2026.
"Martin" = manuscript/existence, "v3" = manuscript/HumanizeYM_v3/chapters (NN:line).

## 1. What Martin's construction is

Source: forest-average-log.tex (read in full), with gaussian-reassembly.tex (full), selected-nonlinear-offering.tex
(1-507 except 430-460 skimmed), five-period-localization.tex (full), physical-reset-reorganization.tex (1-60, 120-175,
255-280), forced-exclusion.tex (95-125), marked-block-integral.tex (140-190).

- What is averaged: the integrated activities a_M^F of the connected components of the exact block gas
  (eq:reassembly-block-gas, B R = O * sum over compatible families with exact flag coverage of prod a_M), i.e. the gas
  BEFORE the logarithm (forest-average-log.tex:9-11, 112-116).
- Over what: an independent uniform forest F_x at each coarse site x, of which only the restriction to the block rooted
  at x is used (81-91). The measure is a product over coarse sites.
- What it proves:
  1. Scalar unchanged (15-79): all forests have the same number of tree bonds; an integer unimodular change of basis
     T_FH with M_H T_FH = M_F and T^T D_H^0 T = D_F^0 gives det A_F^0 = det A_H^0. Uses only: flat rows annihilate
     gradients of functions vanishing at block roots.
  2. Factorisation E_F prod a_M^F = prod E_F a_M^F for compatible (disjoint-support) families (93-110). Uses: a_M^F
     depends on the forest only at coarse sites of its assigned support X_M ("local reads of the rows, inverse windows,
     tags and chart factors"; Haar factors compared as pullbacks of one product Haar measure). Martin's remark: false for
     an average over one global forest.
  3. The average bar a_M has the same bounds (uniform in F), the gas identity holds with bar a_M, O factors out (112-116).
  4. Covariance of bar a_M under signed lattice transformations, from "the covariance of the individual sector formulas"
     and invariance of the product uniform measure (117-121). The fixed-forest covariance is asserted, not proved there.
  5. Locality, gauge invariance, measurability, derivative bounds survive (187-196).
- What else Martin does, outside that file, to get an equivariant family:
  - selected-nonlinear-offering.tex:160-165, 418: allocation weights and the regular output (truncated array and folded
    counterterms) are followed by a "fixed symmetry average" over signed lattice symmetries, cost C_turn;
    five-period-localization.tex end: "A fixed signed-orientation average and its local allocation multiply this bound".
  - forced-exclusion.tex:113-117: labels and cluster tuples are permuted by signed lattice transformations.
  - physical-reset-reorganization.tex:22-24 takes equivariance of all entries as a hypothesis; 139-146 is the reindexing
    argument for Delta delta.
  - selected-nonlinear-offering.tex:255-265: consistency of the forest average between tori (constant-size fibres).
  - marked-block-integral.tex:150-158: the marked expansion uses the same forest average.

## 2. Where each piece went in v3

New file chapters/09-forest-average.tex = subsection 9.1.1 "Lattice symmetries and the average over forests", input at
the end of Section 9.1 (ch09:integral), i.e. after the first component expansion and before the logarithm is used in 9.2.

| Martin | v3 new text | status |
|---|---|---|
| lattice group, equivariance of entries (reset:22-24) | group G, Definition ch09:equivariant | definition |
| flat determinant forest independent (15-79) | Lemma ch09:forest-determinant | proved in full; stated for any symmetric A^0 killing root-zero gradients; hypothesis checked for d_1^* H_f d_1 + b Q^*Q via (ch05:actual-Q) |
| block gas with fixed forest (reassembly:281-303), locality in forest, uniform bounds, sector covariance | Assumption ch09:forest-assumption (a)-(d), eq. ch09:fixed-forest-gas | ASSUMED (see 4) |
| product average, bar a_M, same scalar, bounds, covariance (81-121) | Proposition ch09:forest-average-prop (i)-(iii) | proved from the Assumption |
| consistency between tori (offering:255-265) | paragraph after the proposition | proved given one-forest agreement, which v3's "the same local formula" presupposes |
| labels/cluster tuples permuted (exclusion:113-117) | Proposition ch09:family-equivariance | proved from the Assumption; F_{gx}(U)=F_x(g^*U), F_x(1) constant |
| fixed symmetry average of folded counterterms (offering:418) | Lemma ch09:symmetric-localization (average of G_x, L_x over H_4) | proved in full |
| reindexing for Delta delta (reset:139-146) | Lemma ch09:isotropy (transformation law of q_f and of the clover curvature; three symmetries named) | proved in full |
| output entries equivariant (reset hypothesis is also needed for the next step) | Proposition ch09:output-equivariance; closing paragraph on the Wilson start | proved from formulas of 9.4-9.6 |

## 3. Edits to existing files (all within one line; line counts unchanged)

- `09-renormalization.tex:75`
  - before: `sector. It is extracted once, not separately for every eventual`
  - after: `sector; by Lemma~\ref{ch09:forest-determinant} its value does not depend on that forest. It is extracted once, not separately for every eventual`
- `09-renormalization.tex:148`
  - before: `additional exponential support decay. The first component expansion`
  - after: `additional exponential support decay. The first component expansion, the average over forests of Proposition~\ref{ch09:forest-average-prop},`
- `09-renormalization.tex:161`
  - before: `rather than an asymptotic expansion for its logarithm.`
  - after: `rather than an asymptotic expansion for its logarithm. \input{chapters/09-forest-average}`
- `09-renormalization.tex:239`
  - before: `For the comparison with the actual integral use the same forest`
  - after: `For the comparison with the actual integral use, for each forest separately, the same forest`
- `09-renormalization.tex:240`
  - before: `and physical local coordinates on both sides. The estimates of`
  - after: `and physical local coordinates on both sides; the resulting bounds are uniform in the forest by Assumption~\ref{ch09:forest-assumption}(c) and pass to the average \eqref{ch09:averaged-activity}. The estimates of`
- `09-renormalization.tex:313`
  - before: `low-order formula, retaining a weighted tail`
  - after: `low-order formula to a finite set of labels which is mapped to itself by the lattice symmetries of Section~\ref{ch09:forest-average}, retaining a weighted tail`
- `09-renormalization.tex:331`
  - before: `Let $F_y^{(i)}$ denote the same local formula on $\Lambda_i$`
  - after: `Let $F_y^{(i)}$ denote the same local formula on $\Lambda_i$, formed with the average over the forests of $\Lambda_i$ (see the remark on tori after Proposition~\ref{ch09:forest-average-prop}),`
- `09-renormalization.tex:351`
  - before: `the local expression in each class is independent of $i$.`
  - after: `the local expression in each class is independent of $i$ and of the branch of $\pi_{w+i}$ on which each coordinate of the site lies. The first assertion uses the covariance of the family $F^{(i)}$ under the translations of $\Lambda_i$ and the agreement between tori; the second uses its covariance under the axis reflections $q_c\mapsto-q_c$ of $\Lambda_i$, which leave $U_{i,z}$ unchanged because $\pi_{w+i}(-q)=\pi_{w+i}(q)$ (Proposition~\ref{ch09:family-equivariance}).`
- `09-renormalization.tex:362`
  - before: `Translation covariance makes $F_x(1)=F_0(1)$, giving exactly`
  - after: `Covariance under translations, \eqref{ch09:share-equivariance}, makes $F_x(1)=F_0(1)$, giving exactly`
- `09-renormalization.tex:367`
  - before: `Thus $G_x$ is the small-field local activity and $L_x$ is a`
  - after: `From here on $G_x$ and $L_x$ denote their averages over $H_4$ defined in Lemma~\ref{ch09:symmetric-localization}, which satisfy the same identity and form equivariant families. Thus $G_x$ is the small-field local activity and $L_x$ is a`
- `09-renormalization.tex:398`
  - before: `hold, give local functions $f_i$, preliminary large-field`
  - after: `hold, give equivariant families (Definition~\ref{ch09:equivariant}; see Proposition~\ref{ch09:family-equivariance} and the paragraph following it) of local functions $f_i$ and preliminary large-field`
- `09-renormalization.tex:521`
  - before: `By translation and hypercubic covariance,`
  - after: `By Lemma~\ref{ch09:isotropy}, which uses the equivariance of the family $(f_i)$ under translations, axis reflections and coordinate permutations,`
- `09-renormalization.tex:525`
  - before: `An axis reflection kills off-diagonal orientation pairs;`
  - after: `Translations make the sum independent of $o$; the reflection about $o$ of an axis lying in exactly one of two distinct orientations $q,r$ changes the sign of the corresponding entry, which therefore vanishes;`
- `09-renormalization.tex:526`
  - before: `permutations identify the diagonal pairs.`
  - after: `coordinate permutations without signs identify the diagonal entries.`
- `09-renormalization.tex:867`
  - before: `Use $\beta(1-c_{\rm dir})R(U_p)$ as a regular activity.`
  - after: `Use $\beta(1-c_{\rm dir})R(U_p)$ as a regular activity, divided into four equal shares anchored at the vertices of $p$ so that the family is equivariant (Section~\ref{ch09:forest-average}).`
- `09-renormalization.tex:903`
  - before: `The resulting full Wilson curve is continuous, and its`
  - after: `The resulting full Wilson curve is continuous, its activity families are equivariant in the sense of Definition~\ref{ch09:equivariant}, and its`
- `09-renormalization.tex:919`
  - before: `Chapter~\ref{ch04:blocking}, with the support reserve used above.`
  - after: `Chapter~\ref{ch04:blocking}, with the support reserve used above, and both incoming activity families are equivariant under translations and signed coordinate permutations in the sense of Definition~\ref{ch09:equivariant}.`
- `09-renormalization.tex:924`
  - before: `Use the same forest, path realization, clipped frozen source and`
  - after: `For each forest use the same forest, path realization, clipped frozen source and`
- `09-renormalization.tex:926`
  - before: `Chapter~\ref{ch06:large-fields}. Construct the outgoing path by the`
  - after: `Chapter~\ref{ch06:large-fields}, and average over the forests as in Section~\ref{ch09:forest-average}; assume that this construction satisfies Assumption~\ref{ch09:forest-assumption}, on the actual torus and on the auxiliary tori, that selected sets of terms and anchors are chosen by rules commuting with the lattice symmetries, and that the preliminary large-field activities are regrouped as described after Proposition~\ref{ch09:family-equivariance}. Construct the outgoing path by the`
- `09-renormalization.tex:939`
  - before: `continuous output representation with fixed labels,`
  - after: `continuous output representation with fixed labels and equivariant activity families,`
- `09-renormalization.tex:955`
  - before: `The proof consists of the convergent local expansion,`
  - after: `The proof consists of the convergent local expansion, the average over forests (Proposition~\ref{ch09:forest-average-prop}), the equivariance statements of Section~\ref{ch09:forest-average},`
- `17-current-contraction.tex:164`
  - before: `fixed smaller coarse Fourier strip. To check the width statement, take the forest of`
  - after: `fixed smaller coarse Fourier strip. To check the width statement in this zero-background computation, take the forest of`
- `17-current-contraction.tex:165`
  - before: `Section~\ref{ch05:actual-coordinates} to consist of the coarse translates of one reference tree; this restricts only a free choice. Let $\Pi_F$ be projection onto the forest slice along the joint gauge`
  - after: `Section~\ref{ch05:actual-coordinates} to consist of the coarse translates of one reference tree. This fixes a free choice for the present computation only; the average over forests of Section~\ref{ch09:forest-average} is not used here, and independence of the forest is not claimed for the forest-dependent jets $z_2,z_3$ themselves. Let $\Pi_F$ be projection onto the forest slice along the joint gauge`
New file: chapters/09-forest-average.tex (699 lines), first line `% Draft repair, 24 November 2026; not independently reviewed`.
Input pattern: existing fragments are input on their own line (09:307, 02-observables:395, 14:194); to keep line numbers the
new `\input{chapters/09-forest-average}` is appended to the end of 09:161 (last text line of Section 9.1).

## 4. Hypotheses stated without proof, and why

Assumption ch09:forest-assumption (cited as a hypothesis in Theorem ch09:step-theorem, line 926):
- (a) Form. The fixed-forest output is the identity Z_blk = N_F e^{-S} sum_A prod a_M^F with F-independent labels,
  supports (containing the complete dependence region), prescribed sets, compatibility = disjoint supports, and
  N_F = c m^{N_free} det(iota_F^* A^0 iota_F)^{-1/2}. Why assumed: v3 never displays this identity; 09:56-96 and
  06:1561-1568 describe it in prose and 06 says the reconstruction identities "are distinct from the analytic bounds
  proved here". F-independence of the label set is obtained by a convention (absent factor = value zero), stated in the
  text. That the factor outside the gas depends on F only through N_free and the flat determinant is my reading of
  09:56-79; v3 gives no formula for "the flat reference determinant".
- (b) Locality in the forest: a_M^F depends only on the trees of blocks in X_M. Martin proves it from his detailed
  local reads; v3's chapter 6 was not read in full and has no such statement.
- (c) Bounds uniform in F. Supported by 05:964-966 and 05:1041 (quoted in the text); not checked for every estimate of
  chapter 6 (06:348 says "a constant depending on the fixed tree family and L").
- (d) Transport: a^{gF}_{g.M}(U) = a^F_M(g^*U), S invariant, classification of labels invariant. Needs every auxiliary
  choice of chapter 6 (cutoff functions, finite-range covariances, component assignment, labels) to be made by a rule
  commuting with the lattice group. v3 proves this only for the block kernel (04:262-264) and has the H_4-averaged
  path action (04:518-520). Martin also only asserts it.
Further hypotheses added to the step theorem (09:926): the Assumption also on the auxiliary tori; selected sets and
anchors chosen by rules commuting with the symmetries (anchors: equal shares over the support); the preliminary
large-field activities k_i regrouped by connected unions (v3 09:150-155 gives no formula for k_i; Martin's
forced-exclusion.tex does).
Equivariance of both incoming families is now a hypothesis (09:919) and a conclusion (09:939) of the step theorem.

## 5. Points found while doing this that the audit note did not have

- The family (G_x) of (ch09:localization) is not transported by axis reflections even when F is: the fold image
  x + {0..w+i}^4 is one-sided and a reflection shifts the base point by (w+i)e_c, which depends on i. So equivariance
  of the forest-averaged terms does not by itself give equivariance of the f_i entering 09:521. Martin handles this by
  his "fixed symmetry average" of the folded counterterms. The draft adds the H_4 average of G_x and L_x
  (Lemma ch09:symmetric-localization; 09:367 now says G_x, L_x denote the averages). This changes the objects defined in
  v3, minimally; exact because the localization identity is linear in G_x, L_x.
- After the average, a cluster term with two or more polymers is a product of independent averages, not the average of
  the fixed-forest cluster term. The text notes that 9.2.x estimates the logarithm of the complete pure integral
  (forest free); the statement that the comparison with the selected terms is unchanged is made conditional
  ("provided the remaining terms are removed through their majorants") because v3 does not display that comparison.
- At the Wilson start a plaquette term has no equivariant single anchor; 09:867 now gives it four equal shares.
- The seminorm (ch04:local-seminorm) uses left derivatives; a reflection turns them into right derivatives on reversed
  links, so ||E_{g.i}||_m = ||E_i||_m is not claimed anywhere. The Delta argument needs only absolute convergence at each
  anchor.

## 6. Not transplanted / open

- No proof of Assumption (a)-(d) from v3's chapters 5-6 (Martin's proofs rest on his own local constructions).
- Martin's sections "cost of excluding regular activities" and "local regular functions" (forest-average-log.tex:123-241)
  were not transplanted: v3 covers them by Chapter 8 and 09:148-155.
- Bounds for the symmetrized G_x: asserted to follow from the same derivation as for G_x (v3 gives that derivation in one
  sentence, 09:371-372); not re-derived.
- Chapter 11 (marked expansions, 11-marked-insertions.tex:679 "one forest") and chapter 10 (10:256-257 "forests" as part of
  a history) were not changed. Martin applies the same average to the marked gas; v3 chapter 11 would need the
  corresponding statement. Not examined.
- 17:164-165: the translated reference tree is now said to be a choice "for the present computation only"; the sentence
  no longer says "this restricts only a free choice", and states that forest independence of z_2, z_3 is not claimed.
  Whether the gauge-invariant outputs of that computation are forest independent is not proved in v3.
- Equal-share anchoring of cluster terms: its effect on the anchored bound (ch09:early-bounds) (direction weights are
  measured from the anchor) was not checked.
- No bibliography entry was added (Martin cites Creutz for maximal-tree gauge; references.bib has none).
- Blueprint records / check_blueprint.py: not touched, not run (no blueprint change).

## 7. Commands run and results

- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 677 labels; 1104 references. All explicit
  cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build monograph.tex`: exit 0, 287 pages,
  0 lines containing "Warning" in monograph.log, 0 "Overfull". New subsection is 9.1.1, printed pages 108-115
  (PDF pages 119-126); pages 121 and 126 rendered with mutool and inspected.
- `git diff --stat`: 09-renormalization.tex 42 lines changed (21+/21-), 17-current-contraction.tex 4 (2+/2-);
  "2 files changed, 23 insertions(+), 23 deletions(-)". `wc -l` of every existing chapter file identical before and
  after (09-renormalization 979, 17-current-contraction 396). `git status`: two modified files, one untracked new file.
- No Lean command, no lake build, no git state change.

## 8. Not read

- v3: chapters 1-3, 7, 10-16, 18-19; chapter 4 only 190-290 and 420-677; chapter 5 only 900-1156; chapter 6 only
  40-125, 425-470, 655-700, 880-925, 955-970, 1400-1430, 1535-1568 and greps; chapter 11 only 612-640; chapter 17 only
  140-185. Chapters 8, 09-renormalization and 09-stationary-remainder were read in full.
- Audit notes: ch9-covariance.md and forest-invariance.md in full; 09-renormalization-audit.md first 120 lines;
  ch09-independent-review.md not read.
- Scott (HumanizeYM_v2): not read (only the quotations in the two audit notes).
- Lean (/Users/mgubi/OpenAI-YM): not opened; only the quotations in the audit notes.
- Martin: files other than those listed in section 1.
