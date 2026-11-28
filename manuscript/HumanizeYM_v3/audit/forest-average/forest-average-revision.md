# Forest average: revision after the independent review

Worktree /Users/mgubi/ym-terminology (branch claude/v3-terminology-dictionary). Nothing committed, staged, pushed or
reverted. Date 24 November 2026. "FA" = manuscript/HumanizeYM_v3/chapters/09-forest-average.tex (new, untracked, now
973 lines; rewritten in full); "09", "10", "17" = 09-renormalization.tex, 10-common-trajectory.tex,
17-current-contraction.tex in the same directory (edited within lines only; 979 / 935 / 396 lines, equal to HEAD).
"Martin" = manuscript/existence. "Before" below means the text of the draft as I found it.

## 1. Changes C1-C9

**C1 (mask form, unmasked terms).** Applied; this is how Martin obtains it (forest-average-log.tex:187-210:
"the integrated construction gives a measurable local extension f_i ... w_i = 1_{X_i cap Flags = empty} f_i", then
eq:forest-cluster-mask). Martin does not argue the equivariance of the extension, so it is assumed, not proved.
- FA Assumption (a), end: new sentence and equation (ch09:mask-form) `a_M^F = h_{X_M} f_M^F` for labels with
  I_M empty, f_M^F real Borel gauge-invariant local on X_M; "Parts (b)-(d) hold for the functions f_M^F as well as for
  the a_M^F."
- FA eq. (ch09:averaged-activity): adds `\bar f_M = E_F f_M^F`. Proposition ch09:forest-average-prop (ii), (iii) and
  their proofs now also cover \bar f_M and state `\bar a_M = h_{X_M} \bar f_M`.
- FA Proposition ch09:family-equivariance (i): defines `c^0_\Gamma = (1/n!) \varphi^T(\Gamma) \prod_r \bar f_{M_r}`,
  states and proves `c_\Gamma = h_{X_\Gamma} c^0_\Gamma` (Martin's two-case argument) and the transport of c^0_\Gamma.
  (ii) says that the f_a^0 of 09:319 are these c^0_\Gamma and the selected path terms.
- Deviation from the review's text: the review writes F_\Gamma; I used c^0_\Gamma because F_\Gamma would clash with
  F_x (the clash C6 is about).
- A comment after the Assumption says the extension off the small-field set is a choice and why (b)-(d) are required
  of it separately.

**C2 (agreement between tori, selected sets).** Applied as a new part (e) of the Assumption (text in section 4).
v3 has no statement comparing two tori (grep "replicat", "between tori", "auxiliary tor" over chapters/: only the
phrase "the same local formula on \Lambda_i", 09:331). Martin proves it by replication,
selected-nonlinear-offering.tex:190-272 ("Under replication to a larger period, each short cluster meeting the
designated anchor has a unique lift ... For each polymer choose matching forests on the two periods ... The forests
used by the expansion are averaged, so equality for one matching pair must be lifted to equality of those averages
... constant-size fibers ... Passing two tori to their product period"). That proof rests on Martin's own local
constructions; it was not transplanted, the statement is assumed.
- Differences from the review's wording: (1) I define a "local identification" (restriction of a translation between
  two nonwrapping cubes) before the Assumption instead of "identified isometrically"; reflections are supplied by
  the equivariance on each torus (09:351). (2) "Shape modulo translation" is not defined in v3, so (e) states
  directly: the selected set is finite, is mapped to itself by the group of its torus, and corresponds under local
  identifications. (3) (e) also states that the pure small-field construction is carried out on each \Lambda_i with
  (a)-(d) holding there, and that the selected path terms are channels of an H_4-averaged path action and correspond
  between tori. (3) was implicit in the draft (Proposition family-equivariance (iii) had "provided the Assumption
  holds for that construction"; "path terms are transported because the path action is invariant").
- FA remark on tori (after Proposition forest-average-prop) rewritten to cite (e) and to prove what follows from it:
  equality of the averaged \bar f, of the Ursell coefficients and of the shares.
- FA old paragraph "A finite set of labels which is mapped to itself ... always exists" deleted; (ii) cites (e).
- 09:313 before: `low-order formula to a finite set of labels which is mapped to itself by the lattice symmetries of Section~\ref{ch09:forest-average}, retaining a weighted tail`
  after: `low-order formula to the finite selected set of Assumption~\ref{ch09:forest-assumption}(e), which is mapped to itself by the lattice symmetries of Section~\ref{ch09:forest-average} and corresponds between the tori used below, retaining a weighted tail`
- 09:331 before: `..., formed with the average over the forests of $\Lambda_i$ (see the remark on tori after Proposition~\ref{ch09:forest-average-prop}),`
  after: `..., formed with the average over the forests of $\Lambda_i$ (that it is the same formula is Assumption~\ref{ch09:forest-assumption}(e) together with the remark on tori after Proposition~\ref{ch09:forest-average-prop}),`
- 09:351 before: `... and the agreement between tori; the second uses ...`
  after: `... and the agreement between tori (Assumption~\ref{ch09:forest-assumption}(e)); the second uses ...`

**C3 (wording).** Applied. FA Assumption, first sentence: "Under the hypotheses of Theorem~\ref{ch09:step-theorem}
other than the present assumption, with an equivariant incoming density coordinate tuple, the construction of this
section has the following six properties."

**C4 (anchors of inherited terms).** Applied, with one addition the review's text needs. The rule "keep the coarse
anchor y of the block containing the incoming anchor" commutes with the group only if the transported label contains
the transported incoming activity; that was not in the Assumption. Added to (d): "A label which contains exactly one
incoming regular activity records its index i; the label \varsigma.M then records the index \varsigma.i given by the
equivariance of the incoming family, and the coarse site y with o_i in B(y) belongs to X_M."
- FA Proposition family-equivariance (ii): equal shares now only for the terms of degree at least three and the
  selected low-order cluster terms and their tail; "The terms linear in an incoming regular activity are not divided:
  such a term keeps the single coarse anchor y for which B(y) contains the anchor of the incoming activity"; proof
  added (o_{\varsigma.i} = \varsigma o_i in \varsigma B(y) = B(\varsigma y)).
- FA paragraph after the proposition records the open point (polynomial cost of anchoring equal shares at arbitrary
  sites of a support, to be absorbed by the support reserve of (ch09:early-bounds); "used and has not been checked").
- 09:234 before: `There are $L^4$ fine anchors above each coarse anchor.`
  after: `There are $L^4$ fine anchors above each coarse anchor; an inherited term is anchored at the coarse site whose block contains its incoming anchor and is not divided into shares (Proposition~\ref{ch09:family-equivariance}(ii)).`

**C5 (09:75).** Applied with a changed formula. The review's text prints `b\mathcal Q^*\mathcal Q` in chapter 9, where
\mathcal Q is the quadratic part of the path action (09:403) - the clash the review itself lists under C6. I refer to
the equation instead.
- before: `sector; by Lemma~\ref{ch09:forest-determinant} its value does not depend on that forest. It is extracted once, ...`
- after: `sector; when the flat matrix annihilates the gradients of site functions vanishing at the block roots, as the restriction of the quadratic form \eqref{ch05:actual-hessian} to the fine variables does, its value does not depend on that forest (Lemma~\ref{ch09:forest-determinant}; that the flat reference determinant has this form is Assumption~\ref{ch09:forest-assumption}(a)). It is extracted once, ...`
- FA: new short paragraph after the proof of Lemma forest-determinant: the lemma is unconditional, its application to
  the flat reference determinant is part (a).

**C6 (notation).** All renames are in FA only; no existing symbol was changed.

| draft | now | reason |
|---|---|---|
| tree F_y of block y | F(y) | F_x, F_y^{(i)} of 09:319-336 |
| \mathfrak F (set of forests) | \mathfrak T | \mathfrak F_m(U), 04:543 |
| \mathcal Q (block-average derivative) | \mathcal Q_{\rm av}, with a sentence saying it is the \mathcal Q of (ch05:actual-Q) | \mathcal Q of 09:403 |
| h in H_4 (also k, h') | \varrho, \varrho', \varrho'' | h_X; h of 09:176; k_i |
| g in \mathfrak G | \varsigma | g = (\beta')^{-1/2}, 09:60 |
| translation vector b | z (as in 01:187, y -> hy+z) | penalty b |
| \tau_b (translation) | \varsigma_z | scalar \tau |
| \sigma (permutation) | a -> \varrho(a), the permutation of axes induced by \varrho | support exponent \sigma |
| \varepsilon_a (signs of h) | \omega_a | loop signs \varepsilon, \eta of 09:451 |
| \theta (edge bijection) | \Xi | \theta of H_pre |
| \mathcal P (label set) | \mathcal M | P of Section fusion |
| c (scalar in \mathscr N_F) | \mathscr N_0 | c(X), 09:419 (not in the review's list) |
| w, \tilde w (curls) | (dA)_q, (d\tilde A)_q | w = 4R+100(1+B) (not in the review's list) |
| S_o(q,r) | \Delta_o(q,r) | S(0), 09:568 (not in the review's list) |

Not renamed: the label letter M. Chapter 9 already uses M for a connected product at 09:99-108 (G_M, s_M, A_M,
a in M), so M is the existing symbol for these objects; its coincidence with M_x is pre-existing. FA says in the text
why \varrho, \varsigma replace the h, g of chapter 1. The draft's edited lines of chapter 9 contain none of the
renamed symbols (checked), so no chapter 9 line needed a rename.

**C7 (09:398).** Applied.
- before: `hold, give equivariant families (Definition~\ref{ch09:equivariant}; see Proposition~\ref{ch09:family-equivariance} and the paragraph following it) of local functions $f_i$ and preliminary large-field`
- after: `hold, give, under Assumption~\ref{ch09:forest-assumption} (its part (f) for the $k_i$, which is not proved), equivariant families (Definition~\ref{ch09:equivariant}; Proposition~\ref{ch09:family-equivariance} and Lemma~\ref{ch09:symmetric-localization}) of local functions $f_i$ and preliminary large-field`
  (The review's "regrouping hypothesis stated after Proposition family-equivariance" no longer exists as such: it is
  part (f).)

**C8 (09:924-926; FA "fails").** Applied. Line 924 unchanged from the draft.
- 09:926 before: `..., and average over the forests as in Section~\ref{ch09:forest-average}; assume that this construction satisfies Assumption~\ref{ch09:forest-assumption}, on the actual torus and on the auxiliary tori, that selected sets of terms and anchors are chosen by rules commuting with the lattice symmetries, and that the preliminary large-field activities are regrouped as described after Proposition~\ref{ch09:family-equivariance}. Construct the outgoing path by the`
- after: `..., and average over the forests as in Section~\ref{ch09:forest-average}. Assume that this construction satisfies all six parts of Assumption~\ref{ch09:forest-assumption}. Its part (e) concerns the auxiliary tori and the selected sets of terms, and its part (f) the preliminary families. Assign anchors as in Proposition~\ref{ch09:family-equivariance}(ii). Construct the outgoing path by the`
- FA: "It fails for a general probability measure ...; in particular it fails for ..." -> "It is not available for a
  general probability measure on \mathfrak T, for instance for the uniform measure on the translates and signed images
  of one reference forest."

**C9 (17:165).** Applied as written. Appended after "... jets $z_2,z_3$ themselves.":
`The bounds are used below only for pullbacks of gauge-invariant functions along the stationary branch; that these do not depend on the forest (two forest slices differ by a gauge transformation equal to one at the block roots) is used here and is not proved in this chapter.`
I did not verify the review's claim (17:185-213) that the bounds are used only in that way.

## 2. The four gaps beyond the Assumption

1. Unmasked terms f_a^0: closed by assumption, C1 above ((a) mask form; (b)-(d) for f_M^F). Mask form restored from
   Martin.
2. Tori: closed by assumption, part (e), C2 above. Martin's replication proof located (file and lines above), not
   transplanted.
3. Preliminary large-field family: new part (f): "The preliminary large-field activities (Y_i, I_i^bad,
   E_i^extra, k_i) of (ch09:early) form an equivariant family." The draft's sentence that "the argument of
   Proposition output-equivariance shows" this was removed (v3 has no formula for k_i). Part (f) also assumes the
   list of the regular functions f_i of (ch09:early) (non-selected terms incl. the tail, anchored as in (ii), and the
   symmetrized G_x): the draft derived equivariance of (f_i) without v3 ever saying what the f_i are. This is an
   addition of mine, not in the review.
4. Anchors: resolved as in C4 (inherited terms keep one coarse anchor; 09:234 states the convention).

Also from the review, not in C1-C9:
- 1.6 "the forward reference should become a short lemma placed before both uses": done, FA Lemma
  ch09:path-channels (channels of the H_4-averaged path action are permuted by the group), with the computation
  moved from the proof of Proposition output-equivariance; both propositions cite it.
- 1.7 / item 5 (bound for the symmetrized G_x): the paragraph now says the statement "is not proved in detail here".
- item 4 (L_x = 0, identity (ch09:localization-sum)): the lemma now says "Suppose, as is derived in
  Section improvement, that ..." and the Status paragraph lists it as used and not proved.

## 3. Chapter 10 (three within-line edits)

- 10:233 before: `Fix the common numerical choices above and the compatible finite`
  after: `Assume that every block step used below satisfies Assumption~\ref{ch09:forest-assumption}, which is not proved in this monograph. Fix the common numerical choices above and the compatible finite`
- 10:257 before: `forests, local integral choices and output representations. The`
  after: `local integral choices (made for every forest and averaged over the forests as in Section~\ref{ch09:forest-average}) and output representations. The`
- 10:431 before: `sequence and every allowed activity array of norm at most $1/8$,`
  after: `sequence and every allowed activity array of norm at most $1/8$ (here an allowed array is in particular equivariant in the sense of Definition~\ref{ch09:equivariant}, a linear condition with fixed bijections of labels; the maps are those of Theorem~\ref{ch09:step-theorem} and are therefore subject to Assumption~\ref{ch09:forest-assumption}),`
Not checked: whether every array to which the proof of Proposition ch10:stability-assumption applies the maps
(10:456-801) is equivariant; only the statement was restricted.

## 4. Final wording of the Assumption (FA, verbatim)

    \begin{assumption}[Fixed-forest expansion]
    \label{ch09:forest-assumption}
    Under the hypotheses of Theorem~\ref{ch09:step-theorem} other than the
    present assumption, with an equivariant incoming density coordinate
    tuple, the construction of this section has the following six
    properties.
    \begin{enumerate}[label=\textup{(\alph*)}]
    \item \emph{Form.} For every forest $F\in\mathfrak T$ there are a
     countable set $\mathcal M$ of labels, each with a nonempty support
     $X_M\subset\Lambda$ containing its complete dependence region and a
     prescribed set $I_M\subset X_M$ of large-field sites, possibly empty,
     all independent of $F$; real Borel gauge-invariant functions $a_M^F$
     of the coarse field, with $a_M^F$ local on $X_M$ and
     $\sum_M\sup_U|a_M^F(U)|<\infty$; a Borel function $\mathscr S$
     independent of $F$; and a scalar $\mathscr N_F>0$, such that at every
     coarse field
     \begin{equation}
      \mathscr Z_{\rm blk}(U)=\mathscr N_Fe^{-\mathscr S(U)}
       \sum_{\mathcal A}\prod_{M\in\mathcal A}a_M^F(U).
      \label{ch09:fixed-forest-gas}
     \end{equation}
     The sum is over the finite sets $\mathcal A\subset\mathcal M$ whose
     supports are pairwise disjoint and for which
     $\bigcup_{M\in\mathcal A}I_M=\operatorname{Bad}_m(U)$. The scalar is
     that of the bookkeeping at the beginning of this section:
     $\mathscr N_F=\mathscr N_0\,\mathfrak m^{N_{\rm free}(F)}
     \det(\iota_F^*\mathsf A^0\iota_F)^{-1/2}$, where $\mathscr N_0$ does
     not depend on $F$ and $\mathsf A^0$ is a matrix independent of $F$
     which satisfies the hypothesis of Lemma~\ref{ch09:forest-determinant}.
     For a label with $I_M=\varnothing$ there is a real Borel
     gauge-invariant function $f_M^F$, local on $X_M$, with
     \begin{equation}
      a_M^F=h_{X_M}f_M^F .
      \label{ch09:mask-form}
     \end{equation}
     Parts \textup{(b)}--\textup{(d)} hold for the functions $f_M^F$ as
     well as for the $a_M^F$.
    \item \emph{Locality in the forest.} If $F(y)=F'(y)$ for every
     $y\in X_M$, then $a_M^F=a_M^{F'}$.
    \item \emph{Uniform bounds.} The estimate \eqref{ch09:joint-input}, the
     majorants of the table following it, and the comparison estimates of
     Section~\ref{ch09:improvement} hold for every $F$ with right sides
     that do not depend on $F$.
    \item \emph{Transport.} For every $\varsigma\in\mathfrak G$ there is a
     bijection $M\mapsto\varsigma\cdot M$ of $\mathcal M$ with
     \[
      X_{\varsigma\cdot M}=\varsigma X_M,\qquad
      I_{\varsigma\cdot M}=\varsigma I_M,\qquad
      a^{\varsigma F}_{\varsigma\cdot M}(U)=a^F_M(\varsigma^*U),
     \]
     and $\mathscr S(\varsigma^*U)=\mathscr S(U)$. The classification of
     labels used below (the number and kind of elementary factors, the
     presence of an incoming activity, and path lengths) is preserved by
     these bijections. A label which contains exactly one incoming regular
     activity records its index $i$; the label $\varsigma\cdot M$ then
     records the index $\varsigma\cdot i$ given by the equivariance of the
     incoming family, and the coarse site $y$ with $o_i\in\mathbb B(y)$
     belongs to $X_M$.
    \item \emph{Selected terms and agreement between tori.} The pure
     small-field construction, without incoming activities, is carried out
     with the same choices on each auxiliary torus $\Lambda_i$,
     $0\le i\le4$, of Section~\ref{ch09:improvement}, and parts
     \textup{(a)}--\textup{(d)} hold there with the group
     $\mathfrak G(\Lambda_i)$. On each torus $\Lambda'$ among
     $\Lambda,\Lambda_0,\ldots,\Lambda_4$ the selected low-order terms form
     a finite set. Its elements are tuples of labels with empty prescribed
     sets, and path terms which are channels of a path action averaged over
     $H_4$ as in Lemma~\ref{ch09:path-channels}. This set is mapped to
     itself by $\mathfrak G(\Lambda')$. For every local identification
     $\jmath$ between two of these tori, the labels occurring in selected
     tuples supported in $S'$ correspond bijectively to those supported in
     $S''$, with supports mapped by $\jmath$ and the classification of
     part~\textup{(d)} preserved; a tuple is selected exactly when the
     corresponding tuple is; and
     $f^{F''}_{\jmath M}(U'')=f^{F'}_M(U')$ whenever $U''$ corresponds to
     $U'$ and $F''(\jmath y)$ corresponds to $F'(y)$ for every $y\in X_M$.
     The selected path terms supported in $S'$ and in $S''$ correspond in
     the same way, with anchors mapped by $\jmath$ and equal values at
     corresponding fields.
    \item \emph{Preliminary families.} The regular functions $f_i$ of
     \eqref{ch09:early} are the terms of the logarithm of the averaged
     regular gas other than the selected ones, the tail of the truncation
     included, with the supports and anchors of
     Proposition~\ref{ch09:family-equivariance}\textup{(ii)}, together
     with the localized terms $G_x$ of \eqref{ch09:localization} after the
     symmetrization of Lemma~\ref{ch09:symmetric-localization}. The preliminary large-field activities
     $(Y_i,I_i^{\rm bad},\mathcal E_i^{\rm extra},k_i)$ of
     \eqref{ch09:early} form an equivariant family.
    \end{enumerate}
    \end{assumption}

Preceding definition (FA): "A local identification between two tori Lambda' and Lambda'' is a bijection j between a set S' in Lambda' and a set S'' in Lambda'', each contained in a cube of side smaller than the period of its torus, which is the restriction of a translation between these two cubes. It carries the blocks of S', their fine sites and links, their trees, and the link variables read there to the corresponding objects for S''."

## 5. The "Status" paragraph (FA, verbatim)

    \paragraph{Status of this subsection.}
    \emph{Proved here, with complete proofs.}
    Lemma~\ref{ch09:forest-determinant}: the number of free edges and the
    flat determinant are the same for all forests.
    Lemma~\ref{ch09:path-channels}: the lattice symmetries permute the
    terms of the averaged path action.
    Lemma~\ref{ch09:symmetric-localization}: the localization identity
    survives the average of $G_x$ and $L_x$ over $H_4$, and the averaged
    families are equivariant.
    Lemma~\ref{ch09:isotropy}: for an equivariant family the summed
    quadratic coefficient is a multiple of the identity.
    Proposition~\ref{ch09:output-equivariance}: subtraction, path
    replacement and regrouping preserve equivariance.
    Propositions~\ref{ch09:forest-average-prop}
    and~\ref{ch09:family-equivariance} are proved from
    Assumption~\ref{ch09:forest-assumption} and are no stronger than it.
    
    \emph{Assumed.} The six parts of
    Assumption~\ref{ch09:forest-assumption}, none of which is proved in
    this monograph at present.
    Part~(a): the exact identity for the block integral with one forest,
    the formula for its scalar factor, and the form
    \eqref{ch09:mask-form} of the activities without large-field sites;
    the beginning of this section and the last section of
    Chapter~\ref{ch06:large-fields} describe this reassembly in words and
    state that its identities are separate from the bounds proved there.
    Part~(b): an activity reads the forest only in the blocks of its
    support; Chapter~\ref{ch06:large-fields} defines the dependence region
    of a factor as containing every window entry and frozen coordinate
    which it reads, but does not state the consequence.
    Part~(c): bounds uniform in the forest; Chapter~\ref{ch05:gaussian}
    takes common constants over the finitely many tree shapes and states
    \eqref{ch05:tree-comparison} uniformly in the allowed trees, while the
    uniformity of \eqref{ch09:joint-input} and of the comparison estimates
    is not stated.
    Part~(d): transport of the activities by the lattice symmetries
    together with the forest; proved for the block kernel
    (Proposition~\ref{ch04:kernel-properties}) and built into the path
    action \eqref{ch04:path-action}, not examined for the cutoffs,
    covariances and assignment rules of Chapter~\ref{ch06:large-fields}.
    Part~(e): the same construction on the auxiliary tori, selected sets
    which are mapped to themselves and correspond between tori, and equal
    fixed-forest values under local identifications; supported only by the
    locality of the constructions of Chapters~\ref{ch05:gaussian}
    and~\ref{ch06:large-fields}, which contain no comparison of two tori.
    Part~(f): the list of the preliminary regular functions and the
    equivariance of the preliminary large-field activities;
    the regrouping which produces them is not displayed in this chapter.
    
    \emph{Used and not proved, apart from the assumption.} The vanishing
    of $L_x$ on small-field neighborhoods and the identity
    \eqref{ch09:localization-sum}, which Section~\ref{ch09:improvement}
    derives by a classification of sites that is only sketched there; the
    derivative bound for the localized terms after the average over $H_4$;
    and the absorption, by the support reserve, of the cost of anchoring
    equal shares at all sites of a support.
    
    \emph{Not yet adapted.} The expansions with insertions of
    Chapter~\ref{ch11:insertions}, which fix one forest: their marked
    activities must be averaged over the forests in the same way, so that
    at zero source they reduce to the representation constructed here; no
    such statement has been written. The histories of
    Chapter~\ref{ch10:trajectory} depend on the assumption through
    Theorem~\ref{ch09:step-theorem}. Chapter~\ref{ch06:large-fields} does
    not yet say that its forest is averaged afterwards. The zero-background
    computation of Section~\ref{ch17:quadratic-current} uses one translated
    forest and relies on an unproved independence of the forest for
    gauge-invariant quantities.

## 6. Review items found wrong or not applicable as written

- C5: its replacement text would put `\mathcal Q` (block-average derivative) into chapter 9, against C6. Used
  `\eqref{ch05:actual-hessian}` instead.
- C1: symbol F_\Gamma would clash with F_x. Used c^0_\Gamma.
- C4: the proposed rule needs the transported label to carry the transported incoming index; added to (d).
- C6: "h", "\mathcal Q" are not new symbols of the draft: h in H_4 is the notation of 01:187, 02:195, 04:519, and
  \mathcal Q that of (ch05:actual-Q). They were still replaced inside FA (the clashes within chapter 9 are real);
  the existing chapters keep them.
- C6: label letter M left as is (existing usage 09:99-108), see above.
- C2: "shape modulo translation" is undefined in v3; replaced by direct statements.
- Three label names I first wrote for the Status paragraph did not exist (ch11:marked, ch10:common,
  ch17:contraction); corrected to ch11:insertions, ch10:trajectory, ch17:quadratic-current before the checks.
- No line number or label of the review was found mis-stated in the items applied.

## 7. Commands run and results

- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1164 references. All
  explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build monograph.tex`: exit 0, 290 pages.
  In monograph.log: 0 lines containing "undefined", 0 "Overfull", 0 "Warning", 0 lines starting with "!".
  The aux file has the new labels (ch09:mask-form = (9.4), ch09:path-channels = Lemma 9.5). New subsection 9.1.1 is
  printed pages 108-118; Section 9.2 now starts on page 119.
- `mutool draw -r 70` on PDF pages 122, 129, 130; pages 122 (Assumption (a)-(f)) and 129 (Status paragraph)
  inspected: render correctly. Page 130 rendered, not inspected.
- Line counts, `wc -l` against `git show HEAD:<path> | wc -l`: 09-renormalization.tex 979 / 979;
  10-common-trajectory.tex 935 / 935; 17-current-contraction.tex 396 / 396.
- `git diff --stat`: 09-renormalization.tex 44 (22+/22-), 10-common-trajectory.tex 6, 17-current-contraction.tex 4;
  "3 files changed, 27 insertions(+), 27 deletions(-)". `git status --short`: three modified files, one untracked.
- Existing files were edited by a script that replaces an exact substring on a given line and aborts otherwise:
  /private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/apply_rev.py
- Not run: Lean, lake, check_blueprint.py (no blueprint change), any git state change.

## 8. Remaining uncertainties

- The Assumption now has six parts and none is proved; Theorems ch09:step-theorem and ch10:finite-history are
  conditional on it and say so.
- Part (e) is my formulation; whether "restriction of a translation between nonwrapping cubes" is the identification
  the localization of 09:343-357 needs at every class of sites was not checked against a written proof (v3 has only
  the sketch).
- Part (f)'s list of the f_i is my reading of 09:395-400 and 09:383; v3 does not display it.
- That the selected "path terms" of 09:315 are channels of an H_4-averaged path action is assumed in (e); v3 does not
  say what they are.
- The new text is a draft: the review covered the previous version, not this one. Line 1 of FA says so.
- Chapter 11 and chapter 6 were not touched (outside the permitted files); the Status paragraph records both.
- Not read by me: chapters 6, 11 beyond greps; Martin beyond forest-average-log.tex:80-241 and
  selected-nonlinear-offering.tex:185-275.
