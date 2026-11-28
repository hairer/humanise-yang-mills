# Review of the vocabulary conversion of chapters/11-marked-insertions.tex, lines 1–1180 (reviewer c3a-review)

Worktree `/Users/mgubi/ym-terminology`, file `manuscript/HumanizeYM_v3/chapters/11-marked-insertions.tex`. I read the word diff of all 265 changed lines in 1–1180 against `HEAD` before reading the editor's report `c3a-apply.md`. I checked each change against its dictionary entry (`audit/terminology.md`), the table "Book-wide word choices", Appendix D, and the committed chapters 1–10. I read lines 1181–2355 for context only and did not change them: they are byte-identical to the state before my edits.

## Review findings

| line | class | old (committed) | edited | what was wrong | corrected |
|---|---|---|---|---|---|
| 70 | LANGUAGE | "be the unmarked density with $Z_N=\dots$" | "be the density without insertions with $Z_N=\dots$" | "without insertions with" reads as one phrase | "be the density without insertions, with $Z_N=\dots$" |
| 166 | MINOR (flagged by the editor) | "At a Wilson terminal scale every new component" | "At the ultraviolet cutoff, where the action is Wilson's, every new component" | The meaning is right (entry *terminal* 1; *Wilson initialization*: the flow starts at `N` with the Wilson action). The clause "where the action is Wilson's" is colloquial. | "At the ultraviolet cutoff, with the Wilson action, every new component" |
| 244, 679 | TERM | "In one sector and tag"; "one forest, tag, coarse gauge" | "…for one value of the auxiliary index $\alpha$, …"; "…one value of the auxiliary index $\alpha$, …" | The edit inserts the symbol `$\alpha$`, which this chapter already uses for other things: a lattice direction at 405 (`e_\alpha`) and 1065–1066 (`\Delta_\alpha`), and the number `\alpha=1/(4(D+2))` at 1264–1265 and 1294. Chapter 6 also writes "values of the auxiliary index" without the symbol (6:1108, 1344). | Kept "auxiliary index" and dropped `$\alpha$`: "for one value of the auxiliary index," and "one value of the auxiliary index, one coarse gauge" |
| 479 | LANGUAGE | `\subsection{Propagating the already formed terms involving at least two insertions}` | `\subsection{Propagating the terms of source degree at least two already formed}` | The word order of the title is awkward | `\subsection{Propagating the already formed terms of source degree at least two}` |
| 642 | MISMATCH (minor) | "For the actual stationary forest response $W$, the adjacent" | "For the linearization $W$ of the critical configuration, in its block axial representative $W_F$, the adjacent" | Naming `W_F` is correct: the table says `W_F` at 11:642, and the forest gauge is the block axial gauge. "Block axial representative" is a new compound; 5:1151, 5:1234 and 7:574 say "representative … in the block axial gauge/chart". The identities `KW=Q^*K'`, `AW=bQ^*`, `DW=JD'` (645) and 655 are untouched, and no new property is attributed. | "For the linearization $W$ of the critical configuration, taken in its representative $W_F$ in the block axial gauge, the adjacent" |
| 689 (line not edited by the editor) | LANGUAGE | "its physical evaluation in a different local / frame" | "…in a different local / gauge transformation" (690 edited) | "Evaluation in a gauge transformation" does not read well once "frame" (*frame* 1, R) becomes "local gauge transformation" | "its physical evaluation with a different local / gauge transformation" |
| 960 | TERM / DICTIONARY | `\section{Finite-dimensional detection before taking limits}` | `\section{Finite-dimensional separation before taking limits}` | The entry *detection* has basis I and warns that "'Separated' also means 'at pairwise distinct points' … so 'separation' cannot be reserved for this property". In this chapter "separations" now names the exponents `h_i` (850, 861–862, from *gap* 6), and "separated" names positions at 840 and 1017. The title therefore reads as being about separated points. The edit at 976 ("used to separate the quotient") is correct and stays. | Committed title restored; listed for the author |

Everything else checked and accepted:

- **18–19, *history*.** The words are exactly those of the committed definition. The only change is `\emph{history}`. 7:1202 refers to this place as the definition ("a \emph{history} is defined in Chapter~\ref{ch11:insertions}").
- **372–373, localization.** "Taylor localization, the extraction of the local polynomial part by Taylor expansion of … coarse jet, gives the one-step localization map $T$, a triangular change of basis with diagonal …". This is the table row "extraction of the local polynomial part … *the localization operator* (*Taylor localization*)" together with *localization* 1 (D, "one-step localization map"). It says no more than the chapter: 438 has "its extracted polynomial and a bounded Taylor remainder". The symbol `T` is unchanged. No other words were added. The Bałaban half of the first-use sentence was not added (see "Left for the author").
- **380, graph transform.** "As in the graph transform for invariant manifolds, the step with insertions maps coefficient graphs at the fine scale to graphs at the coarse scale and halves the distance between two of them."
  - It follows the source sentence word for word (Scott `part2/E-section.tex:242`). "Marked step" becomes "step with insertions". "Level `m+1`" and "level `m`" become "fine scale" and "coarse scale", as Appendix D 11:380 allows.
  - The direction is right: `q_m=\mathcal B_m q_{m+1}` (76), so the fine end is `m+1`, and the outgoing graph is `G'=R_GM_G^{-1}` (447).
  - The sentence adds no formula, and it does not mention `M_G` or `R_G`. Those are introduced on the next line (381), unchanged.
  - It claims no more than the source. The halving is the content of the contraction estimate prepared at 453–468, as the entry *rebasing contraction* says. Like its source, it does not repeat the condition `4\delta s_f\le1`.
- **467–468.** "the contraction estimate / of the graph transform on the coefficient graphs". This is the Appendix D repair "the contraction estimate", with "of the graph transform on" added. Those are words only, giving the dictionary's name for `G\mapsto G'` (*graph* 1). The other repair (`G\mapsto R_GM_G^{-1}`) inserts a formula and was correctly not used (lesson 11a).
- **382.** The Appendix D repair was applied as given. `\epsilon`, `L` and `L^{-2/5}` were already in the committed line. "Inverse coupling threshold" was replaced by "lower bound on the reference coupling", the chapter 6 word. "After those choices" in place of "after the stage choices" follows the repair and its source (*preselection bound*: choose `L`, then the threshold).
- **Other Appendix D repairs, words only.** 319 (*warning*, with "nonprincipal" from the second repair of the same line), 352, 424–425, 725–726 and 877 ("normalized products", consistent with 842).
- **Source degree (134 and the 12 replaced lines).** The entry *terms linear in the sources* (R): the terms are the coefficients of `z_S` with `|S|=1`, respectively `|S|\ge2`. Because `z_i^2=0`, the degree of `z_S` is `|S|`, the number of insertion indices. So "linear in the sources" is exactly source degree one, and "involving at least two / several insertions" is exactly source degree at least two. This holds at every replaced line: 479, 502, 503, 507, 509, 517, 519, 775, 792, 1039. "Source variables" is in use from 49. Chapter 12 already says "source degree" (12:270).
- **With / without insertions, insertion point, insertion index.** The replacements follow *mark* 1–2, *unmarked*, *insertion label* (D) and *anchor*. "Insertion-free" is used as a prenominal variant of "without insertions". "Index set" replaces "label set". The second half uses "without insertions" only, which is compatible.
- **885, cutoff-scale coordinates.** "when its inverse coordinates under $\mathsf Z_{N,p,d}$, its \emph{cutoff-scale coordinates}, have a uniform subpower bound".
  - The committed phrase "inverse coordinates under `𝖹`" stays. The new words only name it.
  - That these are coordinates at the cutoff scale follows from 883 ("transfers a cutoff coefficient to its fixed reference scale").
  - The entry is basis R, not I (*inverse terminal coordinates*; the earlier basis-I decision is overtaken, Appendix D line 926).
  - Nothing more is asserted, so I kept it. The term is used at 946, 958 and 1075.
- **1051, 1109, normalized local insertion.** The entry *normalized local insertion* says: keep it, defined once at 11:1051 under this name (R, 11:2323). "Dimensionful" is used for *physical* 2 at 72, 86, 88, 920, 1077 and 1158, and "in continuum units" for *physical* 1 at 866, 981, 998, 1030, 1124 and 1129.
- **Lower bound on the reference coupling** (278, 382, 443, 464, 711, 723). This matches chapters 6, 9 and 10. At 464 and 723 the dictionary leaves bare "threshold" unclassified, but the context fixes the sense: 464 pairs it with the block ratio exactly as 443 does, and 723 follows 711. "Reference scale" matches 2:402. "Nonprincipal" for "nonleading" follows Appendix B and the display at 288.
- **Other passages.**
  - 617–672: block axial gauge, spanning trees, non-tree coordinates, the induced map on curvatures (as 5:453, 528), "rooted linearization of the averaging operation" (as 7:694), and unnormalized `\ell^2` scalar products (as 5:528).
  - 627, 649, 662: "modified" metrics (*actual* 10).
  - 736: "restarted history", defined once. 741 already used it.
  - 773: `$z_\varnothing$` is inserted, the notation of 37 and 76. *Mark* 1 gives "the coefficient of `z_∅`". I kept it.
  - 1074: `$v_{N,p}$` is inserted, as the *trial encoding* proposal says.
  - 1119 and 1130: `$N$` is inserted ("lower bound on $N$", *mesh threshold*).
  - 621: `$\ell^2$`, the chapter 5 phrase.

## Corrections applied

These are in-line replacements only. The file still has 2355 lines, and lines 1181–2355 are unchanged.

1. 70: comma added after "without insertions".
2. 166: "where the action is Wilson's," became "with the Wilson action,".
3. 244 and 679: `$\alpha$` deleted after "auxiliary index".
4. 479: subsection title reordered to "Propagating the already formed terms of source degree at least two".
5. 642: "in its block axial representative $W_F$" became "taken in its representative $W_F$ in the block axial gauge".
6. 689: "evaluation in a different local" became "evaluation with a different local".
7. 960: committed title restored ("Finite-dimensional detection before taking limits").

## Left for the author

- **960, title.** I restored "detection" (see the findings). A possible title is "A finite separating family before taking limits"; the author should choose.
- **221, title.** "One marked step with the actual local factors" became "One step with insertions". Deleting "actual" (sense 1) also removed "with the … local factors". The edited title is not wrong, so I left it, but the author may want "One step with insertions and its local factors".
- **372, first use of the localization operator.** The sentence now says that Taylor localization is "the extraction of the local polynomial part". The second half of the table row ("which Bałaban calls imposing renormalization conditions") is not there. Its sources are B95 and D1, and neither has a key in `references.bib`; chapter 11 cites no Bałaban paper. This needs the author and a bibliography entry.
- **474.** "The strict path-width reserve and the strong support reserve" became "The strict margins in the path width and in the support exponent". The adjective "strong" was dropped. It refers to the "same strong norm" of 471, so probably nothing is lost, but this is unconfirmed.
- **648.** "the installed two-form transport" became "the induced map on curvatures". "Installed" (I; "fixed along the history") was dropped with the phrase. At 651, "raw" (I) was dropped in the same way.
- **842.** "Cyclic product of transfer operators" is the dictionary's word for "transfer word", but the product `\tr\prod B_iT^{H_i}` also contains the slab kernels `B_i`.
- **1136.** "the coefficient map $\mathsf Z$", for "terminal map", shares its words with "linear coefficient map $M_G$" (381) and "single-insertion coefficient maps" (1047). The symbol removes the ambiguity, so I left it.
- **Editor's open list.** The points in `c3a-apply.md`, "Not changed, for the author", still stand. They include *actual* at 415, 558, 1158; *selected* 1; *terminal* left at 110, 147, 157, 171, 525, 923, 955, 1076; *inflation*; *attachment*; *residual coefficient*.

## Mismatches seen between the halves (listed, not fixed)

- 2118 ("physical covariance errors") and 2305 ("The exact physical difference identity") keep "physical". The first half uses "dimensionful" or "in continuum units" by sense; these two lines are not in the *physical* entry's lists.
- 1324 ("every higher source variable coefficient") does not use the first half's "source degree at least two".
- 1783 ("On the interior stencil") and 1824–1829 ("stencil point", "stencil value", "stencil radius") keep "stencil". If this is the stencil of a trial, the first half calls it "link support" (919, 938, 957). If it is a finite-difference stencil, "stencil" is ordinary usage. The reviewer of 1181–2355 should decide.
- Consistent between the halves:
  - "common localization map" (29; 1141, 1307)
  - "Taylor localization" (372, 474; 1203, 1333)
  - "restarted history" (736; 2058)
  - "lower bound on $N$" (1119, 1130; 1815)
  - "normalized local insertion"
  - "prescribed large-field set"
  - "large-field part"
  - "insertion indices" (1371)
  - "with insertions" / "without insertions"
- The second half never uses "inverse terminal coordinates", so "cutoff-scale coordinates" needs no change there.

## Words this file introduces that other chapters may also define

- *source degree* (134). Already used at 12:270. Chapters 12–16 have "linear in the sources" 19 times.
- *cutoff-scale coordinates* (885). Chapter 13 still says "inverse terminal coordinates" (13:159, 217).
- *restarted history* (736). Also in 11R, which another agent is editing (11R:215 title).
- *normalized local insertion* (1051). Also 13sb:53, 13ba:119, 174, and 18lp:243.
- *graph transform* (380, 468). Chapter 12 (12:82–94, "Graph contraction") should use the same name.
- *Taylor localization* and *one-step localization map*.
- *dimensionful*.
- *insertion-free*.
- *insertion point*. Chapters 14 and 18lp use "mark" in this sense.
- *modulus of continuity in the insertion points*. "Positional" also occurs at 14lc:92, 14:813–814, 841 and 18lp:296.
- *lowest scale*.
- *lower bound on $N$*.
- *large-field part (of an insertion)*. Chapter 9 uses "large-field part" of a family of labels (9:639), a different object.
- *separations* (the exponents `H_i`). Chapter 16 has "gap" in another sense.
- *coefficient map* `𝖹` (11E, 13).

## Checks

- `git show HEAD:manuscript/HumanizeYM_v3/chapters/11-marked-insertions.tex | wc -l`: 2355. `wc -l` of the edited file: 2355.
- Changed lines against `HEAD`: 265 in 1–1180 (960 restored, 689 newly changed) and 198 in 1181–2355. Lines 1181–2355 compared with `cmp` against the copy taken before my edits: identical.
- `python3 tools/check_draft.py` (from `manuscript/HumanizeYM_v3`): "51 files; 679 labels; 1225 references. All explicit cross-references resolve; no duplicate labels." Exit status 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-c3a monograph.tex`: exit status 0.
- `monograph.log`: 0 lines matching "undefined" (case-insensitive), 0 matching "Citation", 0 matching "Overfull".

## Not checked

- I did not check the rendered PDF pages visually: neither `pdftotext` nor PyMuPDF is installed. I checked only that the build succeeded, with no warnings of the kinds counted.
- I did not consult the Bałaban and Dimock papers or the Scott/Martin sources. I relied on the dictionary's *Literature* and *Source* lines, as instructed.
- I did not recheck the editor's unchanged ("Not changed") occurrences, beyond those named above.
- I did not review lines 1181–2355 as such. I read them only for the mismatch list above.
