# Chapter 6 (06-large-fields.tex): review of the vocabulary conversion, and corrections

File: /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/06-large-fields.tex. The whole word diff against HEAD was read before the editor's report; the current text of the file was then read from line 1 to line 1568. 26 corrections were applied on 26 lines, all within lines. Nothing staged, committed or reverted; no other file edited; `references.bib` not touched (both keys exist).

Counts: ERROR 1, LANGUAGE 5, DICTIONARY 3 corrected (+ 1 class of basis-I applications left and listed), TERM 4, MISMATCH 5, MINOR 4.

## Review findings

Line numbers are those of the file (unchanged by the edit). "Committed" is HEAD.

### ERROR

- **1018** (Appendix D repair 6:1018–1019). Committed: "A cutoff-failure indicator assigned within the compulsory component region is". Edited: "A cutoff remainder assigned within the retained $300B$ region of its component is". The radius `300B` is not in the committed line; the dictionary (*compulsory*, sense 2, and the repair itself) says the identification of the compulsory region with the `300B` region of 1341–1350 is inferred (basis I). Corrected: "A cutoff remainder assigned within the compulsory component region is" ("cutoff remainder" for "cutoff-failure indicator" is the source's "warning" and stands; line 1019 "every other such remainder" stands). The proposal with the radius is listed for the author.

### LANGUAGE

- **63**. Committed: "Every chosen frame tag must have positive". Edited: "Every value chosen by the auxiliary index $\alpha$ for a local gauge transformation must have positive". An index does not choose a value. Corrected: "Every chosen value of the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking} for a local gauge transformation must have positive" (the chapter reference moved here from line 87, since this is the first use).
- **87**. Edited: "and the auxiliary index $\alpha$ of Chapter~\ref{ch04:blocking}." Corrected: "and the value of the auxiliary index $\alpha$." (a sector fixes the value; reference now at 63).
- **164**. Committed: "hold for the same aligned action rows and". Edited: "hold for the same factorized action components and". The components are not factorized; the metric is. Corrected: "hold for the same action components satisfying the factorization hypothesis and".
- **469–470**. Committed: "a local inequality on the / specified block-tree slice:". Edited: "a local inequality on the / specified block axial gauge:". Corrected 469: "a local inequality in the".
- **1170**. Committed: "a halo multiplier $h$ / large enough to contain every window". Edited: "a multiplier $h$ of the neighborhood radius $hB$, / large enough to contain"; the multiplier does not contain anything. Corrected: "and a multiplier $h$ such that the $hB$-neighborhoods are / large enough to contain".
- **1006** (also LANGUAGE). Edited: "uses the factorized path realization of the untruncated flat maps". Corrected: "uses the path realization, with its factorization, of the untruncated flat maps" (as line 399).
- **1461**. Edited: "where a / cutoff factor kept inside the component vanishes the full component factor is zero." Comma of the Appendix D repair restored: "vanishes, the full component factor is zero."

### DICTIONARY

- **1408**. Left by the editor as unclear: "The null-row linear term vanishes". The entry *row*, sense 1 (basis R), names this line: "complement-row", "null-row" (6:203, 1408) are the components of `N`; line 203 was converted to "complement-component". Corrected: "The linear term of the complement component vanishes" (the cancellation cited is `Nw = 0` of Proposition ch06:mean-cancellation).
- **133**. Left by the editor as the one remaining "block average": "with the linear block average appropriate to the". Chapter 5 as committed calls this `Q` "the linear averaging operator" (5:88, 5:535 "Here $Q$ is the linear averaging operator of this construction"). Corrected: "with the linear averaging operator appropriate to the".
- **694–695**. Committed: "Within a protected logarithmic / chart define". Edited: "Within a logarithmic / chart at $V_0$ define". *protected* has basis I and is agreed as kept-with-definition; deleting it here leaves "protected chart" (1279, 1292, 1518) without antecedent, and "at $V_0$" is an addition not in the committed text. Corrected: committed wording restored on both lines.
- **Basis-I proposals applied by the editor, left as they are and listed for the author** (the wording is not wrong; see "Left for the author"): *direct* → "plaquette" (225, 507, 1009, 1362; the compound "direct row" is covered by *row* 1, basis R); *selected* sense 2 → "fixed", "used here", "this" (134, 165, 177); *mass* 1 and *likelihood* 1 → "probability weight" (63–64, 1107, 1345); *word* 3 → "contour variable" (630, 632, 634); *stored* → "prescribed" (1343); *physical* 9(a) deleted (957); *frozen* and *protected* (kept, defined once, as agreed).

### TERM

- **733**. Edited: "Call a factor \emph{protected} when it is cut off inside this chart." "This chart" was forty lines from its antecedent. Corrected: "inside this logarithmic chart." (with "protected logarithmic chart" restored at 694).
- **739 / 834**. The gloss "a cutoff factor minus one" stood twice (739 in parentheses, 834 by the Appendix D repair). Corrected 739: "Cutoff remainders (defined in the next section) must likewise".
- **1108, 1344, 1422, 1449, 1558**. The edit wrote "the index $\alpha$" where the committed text had "tags". From line 1170 on `α` is the decay rate of the support weight (`e^{\alpha c_B(S)}`, 1177, 1232, 1311, 1465, 1475), so the prose named two different `α` within a few lines (e.g. 1449 against 1465). Corrected: "auxiliary index" without the symbol at these five lines ("local values of the auxiliary index"; "The retained values of the auxiliary index for the local gauge transformations"; "spanning trees, auxiliary index, index triple,"; "Haar, auxiliary-index, and frozen-coordinate"; "values of the auxiliary index,"). Before 1170 the symbol stays (63, 87, 362–363, 486, 920, 1016).
- **1396–1397**. Edited: "about each / annular component. The nonlinear component minus". In this subsection "component" is the large-field component `O`, and the editor's own rule there is "action term" for the rows that carry energy terms. Corrected: "annular action term. Its nonlinear component minus".

### MISMATCH

- **259**. "The direct part is" was left while 1009 has "The plaquette part". Corrected: "The plaquette part is" (the formula on the next line is the `c_{\rm dir,c}` plaquette term).
- **494**. "macro-patch" left on an unedited line, against "macro-box" everywhere else and in chapters 4–5. Corrected: "macro-box, from".
- **453** (with chapter 4). Chapter 4 as committed renders the same object as "the support of the expression" (4:506). The new short term *link support* is now tied to it in its defining sentence: "its \emph{link support}, the fixed set of links from which its expression is built (the support of the expression, in the words of Chapter~\ref{ch04:blocking}), meets an active".
- **992**. Edited: "evaluated at the pulled-back coarse field"; elsewhere "at $\operatorname{rep}V$" (587, 1374, 1400). Corrected: "is evaluated at $\operatorname{rep}V$,".
- **442** (see next section).

### First-use sentences (point 4)

- **11**. "Ba{\l}aban makes the same split, into large plaquette fields and large fluctuation fields~\cite{Balaban1988Expansions}; he adds the location of a large fluctuation field to the large-field region, whereas here the large-field set is not enlarged and these events are bounded by a joint Gaussian tail estimate." Agrees with the Literature line of *cutoff failure* (B88b pp. 252, 255; "add its location to the large field region"; "v3 does not … bounded by a joint Gaussian tail estimate") and with the table row. B88b is `Balaban1988Expansions` (Appendix L; key present). The phrase "large fluctuation" occurs in no other chapter file of the worktree, so nothing is repeated. Not changed.
- **442**. Edited: "(The word conditioning is Ba{\l}aban's~\cite{Balaban1988Cluster}; he does not integrate such variables in the same step.)" The word is from B88a p. 12 (`Balaban1988Cluster`, correct), but the second clause rests on B88b p. 256 ("integrations with respect to variables on large field regions left"), not on the paper cited. Class MISMATCH/ERROR of attribution. Corrected: "(The word conditioning is Ba{\l}aban's~\cite{Balaban1988Cluster}; in~\cite{Balaban1988Expansions} the integrations over such variables are left to later steps, whereas here they are carried out in the same step.)" The last clause is the Literature line's "v3 integrates the frozen links in the same step" and the chapter's own 673–674.

### Points examined and found correct (no change)

- **The two mechanisms.** Every occurrence of "fluctuation" and "large-field" was checked (9, 11, 835, 897, 908, 992, 1014, 1137 against 8, 19, 49, 78, 326, 421, 611, 643, 648, 687, 689, 1078, 1284, 1343–1344, 1480). "Large fluctuation-field event" is used only for the events `ℰ_w` of (ch06:tail-event) (835, 897, 1137); "large-field" only for the index triple, `Δ_p` (326), the coarse sites and the indicators. No sentence calls an element of `A` a fluctuation event or the reverse. "Large fluctuation-field region" is not used in the chapter.
- **Appendix D repairs.** 80 ("the bound on the local energy $\mathcal E_A$ defined below": `𝓔_A` is defined at 210–212), 90, 459, 834, 846, 919–920, 1015–1016, 1460–1461, 1476, 1544 say what the repair texts say with the agreed words substituted. 1540–1541 uses the symbol `T_V`: it is defined at 728 and the source wording ("the compensated change of variables … a global bijection") describes that map, so it is kept, and noted below. 1018 corrected (above). 845 "the mean $m_Y$" for "the actual mean": `m_Y` is the mean in `v = m_Y + gz` (897); kept.
- **row.** Sense 1 → component / plaquette component / path component / affine component (and "vectors" for `Φv_c`, `Φ_n v_c`, 186–188, which the entry calls the comparison vectors); sense 4 → "operator $K$" (145); sense 5 → factorization (125, 136, 164, 377); sense 6 (row and column sums, row norm, row bound: 217, 240, 280, 330, 554, 636, 812, 828, 907, 942, 972, 994, 1501) kept. Correct at every line.
- **selected / selection** (index triple, "of $A$", "$A^{[10B]}$", "location of $A$"; "retained" for sense 3), **allocation** (partition of unity 67–81, 1340; assignment 1327, 1460), **sector** (defined 85–87), **test** (conditions 83, 687, 1324, 1340; indicator 108, 1416; variables 320, 336, 604; plaquettes and edges 54, 79, 89, 323), **tag**, **likelihood** 2 ("normalized weights of the index $\alpha$" at 920, 1016, distinct from the partition-of-unity weights), **noise** (only sense 2 occurs: 908, 1014), **frozen**, **warning** (1476), **window** (only `Ω_i` and "local window" 1287): correct.
- **"element of $A$"** (416–417, 1157, 1162, 1329, 1349): the editor's reasoning holds. `|A|` is the sum of the three cardinalities (51) and Proposition ch06:energy is in `|A|`, and `n` at 1329 is the `n` of `𝓔_O^{rem} ≥ κ t_f² n` (1443), so "plaquettes and edges" would have dropped the sites of `A_c`. At 416 the split "per plaquette of $A_f$ or edge of $A_n$ … per element of $D$" is right (`D ⊂ A_f ∪ A_n`).
- **Lines left by the editor as unclear.** 133 and 1408: resolved (above). 215 (title "Direct bounds and the signed comparison"), 1379 ("frozen mismatch"), 1410 ("the two signed mismatch terms", *mismatch* 2 basis I), 1455 ("retained energy coefficient"): rightly left.
- **Short terms.** *index triple* (49), *deviation* (49; agrees with 9s:141, 149, 163 as committed; chapter 4 no longer has "mismatch" and does not use another word), *averaging component* (491), *merged components* (1332), *displacement field* (1374): defined at first use, used consistently, and found in no other chapter file. *sector*, *frozen*, *active*, *cutoff remainder*, *residual Gaussian density*, *core* / *annulus*: defined where the editor says.
- **953, 976.** Both read `W_F`; 953 now "Let $a=W_F h$ be the linearized critical configuration, with $W_F$ as in \eqref{ch05:stationary-tangent}, for a coarse" (the label is at 5:1149 and defines `W_Fv`); 976 untouched. Meaning unchanged. 947, 966–967, 972–974, 1493, 1545 name `W_F` as chapter 5 does ("the representative $W_F$ in the block axial gauge").
- **Non-vocabulary changes.** None that alters a formula. Additions of symbols already in the text (`m_y(q)` 305, `\Delta_p` 326, 356, `A^{[10B]}`, `E_f`, `E_n` 1403, `\mathsf Am_Y+f_Y` 639, `u\mapsto\mathsf Du+b_Y` 446, `\lambda(U,\alpha)` 671 as at 4:218) and of cross-references ((ch05:physical-transports), (ch05:positive-defect) 135; (ch06:flat-identities) 164; (ch06:macro-comparison) 338; (ch06:protected-change) 1031, 1535; Section ch06:sector 1356) were each checked against the text.

## Corrections applied

26 lines: 63, 87, 133, 164, 259, 442, 453, 469, 494, 694, 695, 733, 739, 992, 1006, 1018, 1108, 1170, 1344, 1397, 1408, 1422, 1449, 1461, 1558 (25 changed; the script also touched 470 with an identical string). The script is /private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/b1d-fix.py (old and new text of every correction).

## Left for the author

1. **1018**: whether to write the radius: "within the retained $300B$ region of its component" (Appendix D proposal; identification inferred) in place of "the compulsory component region", which is now the only use of "compulsory" in the chapter and is not defined.
2. **920, 1016** "the normalized weights of the index $\alpha$": the normalization (weight times the number of values of the index, so that it equals one on the minimizing branch; *likelihood* 2, basis S) is not stated in the chapter. A gloss would add a sentence the committed text does not have.
3. **Basis-I words applied** (list under DICTIONARY above): confirm or revert *direct* → plaquette (225, 259, 507, 1009, 1362), *selected* 2 (134, 165, 177), "probability weight" for mass / likelihood 1 (63–64, 1107, 1345), "contour variable" for "path word" (630–634), "prescribed" for "stored" (1343; the same adjective as chapter 4's "prescribed large-field set"), "unnormalized $\ell^2$ norms" for "physical counting norms" (957).
4. **442**: the parenthesis on conditioning rests on an entry of basis I; delete it if not wanted. The gloss "non-tree links that are held fixed in the Gaussian integral and integrated afterwards" is the entry's reading.
5. **1332** "repeatedly merging subsets of $A$" for "merging selected sets": probably the components of `A` (1329), but the text does not say so.
6. **1553–1554** "the compatible untruncated quadratic identities": "full" was read as "for the untruncated maps"; the line is not in the entry *full maps*.
7. **172, 175**: the glosses "(the Wilson density at the cutoff scale $N$)" and "at the ultraviolet cutoff $N$" are the dictionary's (basis R), but `N` is also a number of coordinates later in the chapter (852, 877, 1060).
8. **1404** "the term in $\chi(\cdot)^2$" (dictionary proposal) against the book's usual "squared distance from the identity".
9. **1493** "the linear relative field $W_Fh-\operatorname{rep}h$ of the proof of Proposition …": the formula is that of 976 ("relative candidate"); the identification of the two `v` is the editor's, supported by 939 and 1498.
10. **1540–1541** `T_V` (Appendix D repair): a symbol where the committed line had "the compensating map".
11. **13** "the fine scale $m+1$ and the coarse scale $m$" (dictionary wording, as 9:15); the table would say "scale index".
12. Title **215** and lines **1379, 1410, 1455** remain as committed.
13. **453**: *link support* (chapter 6) and "support of the expression" (4:506) name the same notion; one of the two should be chosen for the book.

## Words this file introduces that other chapters may also define

index triple (large-field index triple); deviation `n_e`; sector; frozen / conditioning variables; active coordinates; link support (chapter 4: "support of the expression"; chapters 11–13 have "stencil"); averaging component; plaquette component, path component, action term; protected (factor, chart); cutoff remainder; large fluctuation-field event (chapters 9–11 have "cutoff failure", "tail events", "warning"); residual Gaussian density; core, annulus; merged components; displacement field; partition of unity / partition-of-unity weights (chapter 9 "sector allocation indicators"); inhomogeneous term; non-tree links; pull-back `rep V`; decay rate of the support weight (chapters 7, 8, 9, 17); `hB`-neighborhood; lower bound on the reference coupling (chapters 7, 10, 11 "coupling threshold"); localized approximate inverse; comparison identity for the mean; factorization hypothesis; two consecutive scales (chapters 7, 9).

## Checks

- `git show HEAD:manuscript/HumanizeYM_v3/chapters/06-large-fields.tex | wc -l`: 1568; `wc -l` of the file: 1568. `git diff --numstat`: 400 / 400.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1216 references. All explicit cross-references resolve; no duplicate labels." Exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-b1d monograph.tex`: exit 0 after 3 pdflatex runs; in monograph.log "undefined" 0, "Citation" 0, "Overfull" 0. Both `Balaban1988Cluster` and `Balaban1988Expansions` are in the .bbl. The build used the other chapters in the state they had at that moment (HEAD moved to 8b1d5324 during the review; 07-matching.tex was still uncommitted).
- `git status --short`: of this assignment only chapters/06-large-fields.tex is modified; nothing staged.

## Not checked

- The papers of Bałaban were not opened; the two citation sentences were checked only against the dictionary's Literature lines.
- The rendered PDF pages were not inspected.
- The mathematics behind the editor's identifications (e.g. `E_f`, `E_n` at 1403, `v` at 1493, `T_V` at 1540) was checked against the formulas of this chapter only, not against the source manuscripts or Lean.
- Dictionary entries were read for the words named in the assignment and for the bases of the other entries applied; the full text of every entry applied (about 90) was not reread.
- Chapters 7–11 were not compared word by word; only greps for the new terms were run.
