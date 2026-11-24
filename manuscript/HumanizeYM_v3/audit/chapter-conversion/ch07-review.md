# Chapter 7 (`chapters/07-matching.tex`): review of the vocabulary conversion, and corrections

File: /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/07-matching.tex. The whole word diff (289 changed lines) was read before the editor's report. 25 lines were corrected, all within their lines; the file still has 1206 lines. "Committed" below means `HEAD`.

Counts: ERROR 0; inserted mathematical content (class 7, treated as ERROR-level and removed) 3; LANGUAGE 12; TERM 3; MISMATCH 3; DICTIONARY 1; MINOR 3.

## Review findings

### Inserted formulas (not vocabulary)

| line | class | committed | edited | what was wrong | now |
|---|---|---|---|---|---|
| 195 | non-vocabulary | "exchange symmetry and signed-coordinate symmetry, has" | "exchange symmetry $f_{ab}^{uv}(p)=f_{ba}^{vu}(-p)$ and signed-coordinate symmetry, has" | The formula is in the source (`existence/stationary-output-construction.tex:196–199`, read: identical formula, with `a,b` coordinate and `u,v` colour indices, momenta `(−p,p)`), but the committed line states the symmetry in words only and does not determine the index placement. Inside a lemma statement this adds a hypothesis in formula form. | committed wording restored |
| 599 | non-vocabulary | "padded block average patch only changes constants" | "box of radius $(j+5)L$ only changes constants" | The radius is from `existence/weighted-frame-penalty.tex:168` (read: "a padded box of radius `(J+5)L`"), nowhere in v3; the dictionary itself classes it S and says the committed phrase "names a larger box" than the patch of chapter 4. | "padded patch of the averaging operation only changes constants" (committed phrase, with chapter 4's word for "block average patch") |
| 427 | non-vocabulary / TERM | "The four constant direction selectors in the vector regulator do not" | "The four constant component maps $J_a$ in $M_\mu=\sum_aJ_a^*m_\mu J_a$ do not" | The source sentence at this place (Scott `part2/C-section.tex:348`, as quoted in Appendix D) is the committed sentence; the formula comes from another source line (259). It introduces a symbol `J_a` that v3 never defines and that collides with `J=Dr(0)=-K_c` (539), the action `J(v)` (976), `J_0` (648) and `\mathsf J` (242). | "The four constant maps in the vector regulator that take a one-form to its components do not" (words only; this is what 7:276 says of `M_μ`) |

### Other Appendix D repairs

- 461 "this last mesh estimate": agrees with the text's own "The Fourier mesh estimate at the end of Proposition …" (762, committed). Correct.
- 742 title "Trace norms and finite-volume coefficients": acceptable (the paragraph ends with the infinite-lattice representation of the finite-torus coefficients and the finite-volume error); a title, see "Left for the author".
- 636–637 "For the coordinate contours of the transporters, / the link read at a fixed position is a translate of a point having some coordinates of each endpoint.": says what the source says (`weighted-frame-penalty.tex:78–83`, as quoted in Appendix D: "the link read is a translate of the coordinatewise splice of the two endpoints"), no more. Left.
- 764–765 "identifies the coefficient $\alpha$ of / the Gaussian contribution \eqref{ch07:thermal}": `T(v)` is called "The Gaussian contribution" at 231; the sentence claims no more than the source ("the thermal term and the core determinant term have the same leading quadratic coefficient") and less than the committed one only by the deleted "actual stationary" (the critical configuration is already in the definition of `T`). Correct; better than the Appendix D text, which kept "actual".

### `W_s`, `W_a`, `W_F`

Checked against 05-gaussian.tex:1081–1153 and 1234.

- 574: says that `W_a` (ch05:corrected-transport) is the smooth representative of the linearization `W` and `W_F` (ch05:stationary-tangent) its representative in the block axial gauge. Agrees with 5:1149–1153 and 5:1234. Correct.
- 1043 "bounds on the smooth representative $W_a$ through order two": `T u=(u,W_au,r_u)` (882) and (ch05:actual-bridge) is asserted for `W_a` (5:1151–1152). Correct.
- 1118 "the representative $W_F$ in the block axial gauge itself has poor difference bounds": 5:1151–1152 ("asserted for `W_a`, not for the representative `W_F`"). Correct.
- 1112 "The representative $W_s$, built with the linear averaging operator": 5:1084; the committed 1115 already calls it "this representative". Correct; adjective order fixed (LANGUAGE).
- 1201 "the infinite-lattice bounds on $W_s$" (committed "the common transport bounds"): the operator is determined by 1112–1119 (the bounds `∇_f^rW_s=O(L^{-1-r})`). Kept, but "infinite-lattice bounds" is not a defined thing (TERM): now "the bounds on the infinite-lattice kernels of $W_s$".
- 1154 (MISMATCH with 1114) committed "once the actual and straight stationary tangents have been identified up to gauge"; edited "once the linearization of the critical configuration and its representative $W_s$ have been identified up to gauge". If `W_s` is "its representative" the identification is tautological; 1114 calls the first object "the linearization built with the averaging operation". Now "once the linearization built with the averaging operation and the representative $W_s$ have been identified up to gauge as above".
- 1088 (MINOR, meaning) committed "from the transports of Chapter 5"; edited "from the bounds on the linearization of the critical configuration in Chapter 5". "the bounds on" was added and the plural lost. Now "from the representatives of the linearization of the critical configuration in Chapter 5".
- 780, 1114, 1136, 1140–1141: representative left unnamed, as in the committed text. Correct (the identities used hold for `W_s`, `W_a` and `W_F` up to the change `M`/`𝒬`).

### "background field" / "critical configuration"

All uses checked. "critical configuration" stands only where the committed text had "stationary" (5, 231, 250, 499, 505, 517, 552–553, 766, 770–771, 780, 863, 867, 882, 938, 949, 953, 965, 971, 985, 1072, 1136, 1150–1154, 1159, 1200–1204); "background" only for "external" / "background" (332–333 and the background derivatives, 366, 597–630, 671, 676, 750, 899–909, 1033–1042). No confusion found. Two readings are the editor's and are listed for the author (499/770 and 1200).

- 1150 (LANGUAGE/TERM) "the pullback by the nonlinear critical configuration": a configuration is not linear or nonlinear; now "the nonlinear critical-configuration map" (the word of 517, 949, 953, 1152 and of 5:1145).
- 899 (LANGUAGE) "the background cubic and quartic vertices": now "the cubic and quartic vertices with background legs" (cf. 1033).
- 597 (MISMATCH) "External smooth bridge legs" was left while every other "external" direction or leg became "background" (the entry *external*, basis R, lists 595–630): now "Background smooth bridge legs". "bridge legs" (basis I) is untouched.

### "gauge-fixing term" / "gauge-fixed"

Applied only to `F^*F`, `d_Ud_U^*`, `d_0d_0^*` and the operators containing them (229, 314, 371, 877, 935, 1025: `C=\mathsf J+F^*F`, `a_{\rm loc}`, `\mathscr C^{-1}=(\mathscr H+F^*F)^{-1}`). The block-completed form is "The kinetic form with the penalty term added, the form $\mathcal G$ below" (687–688); "blocked completed matrix $C_0$" (773) is unchanged. Correct.

### Short terms

- 332 *background derivative*: defined at first use; correct; no collision (the only other occurrence in the book, 17-trace-transfer.tex:370, has the same sense).
- 36 *infinite-lattice symbol*: the text's own definition with the headword changed; agrees with chapter 5's "infinite-lattice kernels". Word order corrected at 558 and 1112 (LANGUAGE: "holomorphic infinite-lattice kernels", "exponentially local infinite-lattice kernels").
- 237 *inherited loop action*: "the $\beta$-independent quadratic term of the path action" is the phrase of 04-blocking.tex:525. Correct.
- 529 *contact term* (`Z`) and *contact correction* (the difference in (ch07:contact-exact)): consistent with all uses (501, 504, 568, 773, 807); 773 "After removing the contact term …" can only mean the matrix `Z`, which supports the reading independently of the source. The source (`existence/thermal-contact-cancellation.tex:1, 126–141`, read) has the title "The thermal determinant and its contact term" and `M_act = A + Z`, but no sentence "Z is the contact term". Left; listed for the author. The words collide with the coincident-point "contact terms" of chapters 18–19 (already so in the committed text); the qualifier "of the averaging operation" is kept.
- 506, 521 *centered* / *rooted coordinates*: glosses agree with the entries *centered* 3 and *rooted coordinates* (basis R). Left.
- 360 *width* (LANGUAGE): "a smaller \emph{width}, that is, exponential decay rate of the path coefficients" lacked the article and the comparative; now "that is, a smaller exponential decay rate of the path coefficients". Sense confirmed by 1177–1180.
- 61 *leg* (LANGUAGE): "the indicated \emph{leg}, that is, argument of the symbol" → "the indicated \emph{leg} (field argument of the symbol)" (cf. line 34).

### Remaining findings

| line | class | edited | problem | now |
|---|---|---|---|---|
| 25 | LANGUAGE | "They do not differentiate a threshold boundary." | noun pile; a threshold has no boundary | "They do not differentiate at the boundary of the small-field region." (chapter 4's term) |
| 323 | LANGUAGE | "depend on the fixed path bounds, lower bound on the metric and group," | reads "lower bound on (the metric and group)" | "…, on the lower bound for the metric and on the group," |
| 352 | DICTIONARY | "the four edge exponentials and their contour variables" (committed "their transports") | the entry *transport* 1 keeps *parallel transport* for the action; "their contour variables" is not what is expanded | "and their parallel transports" |
| 407 | LANGUAGE | "The lower bound on the real inverse propagators" (committed "The real denominator floor") | "real" qualifies the momenta (cf. 453–454) | "The lower bound on the inverse propagators at real momenta" |
| 414 | LANGUAGE | "both channel inverse propagators" | noun pile | "the inverse propagators of both channels" |
| 618 | LANGUAGE | "H\"older … contributes $O(\mu^4)$" | | "gives" |
| 749–750 | LANGUAGE | "These factors occur in different terms; the same factor is not used to compensate for both." | "factors" (the losses `L^2`, `μ^{-2}`) and "factor" (`μ^2`) confused after "costs" was replaced | "These large factors … the same small factor …" |
| 752 | LANGUAGE | "The norms of their first two background derivatives" | "their" = "Positive background derivatives of $d_U$": derivatives of derivatives | "The norms of these first two background derivatives" |
| 828 | LANGUAGE | "with the normalized path action, lower bound on the metric and / identity …" | lost articles | "…, the lower bound on the metric and the / identity …" |
| 869 | LANGUAGE | "The fixed-$L$ chart … but its inverse in the block axial chart alone" | "chart … in the … chart" | "its inverse in the block axial gauge alone" |
| 889 | LANGUAGE | "with the / identification of the averaging operation in Chapter 5" (committed "actual block average identification") | says the averaging operation is identified | "identification for the averaging operation" |

No sentence about Bałaban's or Dimock's papers was added by the edit; no bibliography key was added. No change inside math mode, labels or `\ref` targets, other than the three formulas above; references added by the edit (`\eqref{ch05:stationary-tangent}` at 578 and 829, `\eqref{ch07:thermal}` at 765, `\eqref{ch07:contact-exact}` at 529, `\ref{ch10:choices}`, `\ref{ch11:insertions}`, `\ref{ch07:weighted}`) all resolve.

Agreement with chapters 4–5 checked for: transporter (4:174), averaging operation / linear averaging operator `M` (5:1084), "position within the block" (5:654, 713), "β-independent quadratic term" (4:525), block axial gauge / chart, critical-configuration map (5:1145), "(Section ch10:choices)" for stage (5:689), penalty term of the block kernel. No mismatch.

## Corrections applied

25 lines: 25, 61, 195, 323, 352, 360, 407, 414, 427, 558, 597, 599, 618, 749, 750, 752, 828, 869, 889, 899, 1088, 1112, 1150, 1154, 1201. Script: /private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-b1e/review_fix.py (each old string required to occur exactly once on its line).

## Left for the author

1. **195**: whether to print the exchange symmetry, `$f_{ab}^{uv}(p)=f_{ba}^{vu}(-p)$` (source `existence/stationary-output-construction.tex:198`).
2. **599**: whether to write "box of radius $(j+5)L$" (source `existence/weighted-frame-penalty.tex:168`); likewise 628 "padded block" (radius `(j+3)L`, inferred), untouched.
3. **427 / 276**: whether to define `J_a` with `M_\mu=\sum_aJ_a^*m_\mu J_a` at 276; the letter `J` is already used three ways in the chapter.
4. **529**: the names *contact term* for `Z` and *contact correction* for the difference in (ch07:contact-exact), and the clash with the coincident-point "contact terms" of chapters 18–19.
5. **1200**: committed "actual stationary block average" is now "averaging operation at the critical configuration", a literal conversion; the parallel sentence 765–766 suggests "the averaging operation and the critical configuration" was meant. Not found in the sources.
6. **499, 770–771**: "stationary (background) insertions" is now "the background derivatives at the critical configuration"; literal, no dictionary entry, not found in the sources.
7. **578–579** (pre-existing): "the identity \eqref{ch05:stationary-tangent} and smooth representative of Section~\ref{ch05:transports}" — both are in Subsection `ch05:actual-tangent` (5:1081), which lies in a different section; the reference should probably be `\ref{ch05:actual-tangent}`. Not changed (a reference).
8. **636**: "coordinate connector paths" became "the coordinate contours of the transporters"; in the source the coordinate paths join pairs of points of the patch (construction of the local gauge transformation), and the transporters come afterwards (640).
9. Titles changed by the edit: 229, 501, 572, 603, 626, 742 ("Trace norms and finite-volume coefficients"), 825/827 ("One-loop shift of the coupling"), 863.
10. **913** "the same or higher scaling dimension" and **365**: the entry *weight* 1 does not list these lines; kept because 365 states the same thing (a coordinate-change term raises the scaling dimension).
11. **313** the gloss "(the Hessian in left increments of the proof below)" inside the statement of a proposition; **22** and **1202** forward references for *stage* and *history*.
12. Kept house words with basis I (as in the editor's list): "coarse-frame projection / directions" (477, 892) beside "local gauge transformation" elsewhere; "bridge legs" (597); "common strip / width / bound", title "Common comparison estimates" (136, 456, 769, 806, 820, 958, 1013, 1159, 1169); "blocked completed matrix $C_0$" (773); "quotient estimate"; "selected"; "response".
13. **522** "a fluctuation left increment", **924–925** "fluctuation / vectors": correct but heavy; the display at 886 still has "internal".

## Words this file introduces that other chapters may also define

*background derivative* (332); *infinite-lattice symbol* (36); *inherited loop action* (237; chapters 9, 10, 17 use `ℒ`); *contact term*, *contact correction* (529; chapter 17 has a "contact identity", chapters 18–19 "contact terms"); *width* (360; chapters 5, 10, 11, 12, 17); *leg* (61; chapters 3, 17); *centered* / *rooted coordinates* (506, 521); *transported curvature* (147; chapters 1, 2); *inverse propagator* (331; 17t:107); *scaling dimension* for "weight" (chapters 2, 3, 9, 11); *zero / nonzero alias* (chapters 5, 11, 17); *position within the block* (chapters 5, 11, 17); *base point* in the sense of a real momentum (733); *norm comparison* (498, 751, 917); *one-loop shift of the coupling* (825); *lower bound on the inverse coupling* (1190; "coupling threshold" elsewhere); forward glosses of *stage* (22) and *history* (1202).

## Checks

- `wc -l chapters/07-matching.tex` → 1206; `git show HEAD:manuscript/HumanizeYM_v3/chapters/07-matching.tex | wc -l` → 1206; `git diff --numstat` → `290 290`.
- `python3 tools/check_draft.py` → "51 files; 679 labels; 1215 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-b1e monograph.tex` → exit 0 (pdflatex ran, PDF written 18:36); in `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build included the uncommitted state of 06-large-fields.tex present at that moment.
- Nothing staged, committed or reverted; only 07-matching.tex edited.

## Not checked

- The rendered pages were not inspected.
- Bałaban's and Dimock's papers were not opened (no sentence about them was added).
- Sources read: only `existence/stationary-output-construction.tex:190–202`, `existence/thermal-contact-cancellation.tex:1, 120–142`, `existence/weighted-frame-penalty.tex:160–172`; the Scott source for 427 and the source lines for 637 and 764 were taken from the quotations in Appendix D.
- Dictionary entries were read for the terms in question, not for every one of the 289 lines; the routine substitutions (cost, floor, denominator, principal, frame, internal/external, insertion) were checked against the entry once and then for sense and grammar line by line.
- The mathematics of the chapter itself (e.g. whether the rooted coordinates are indeed normalized at the root) was not re-derived; the glosses at 506 and 521 rest on the dictionary's basis R.
