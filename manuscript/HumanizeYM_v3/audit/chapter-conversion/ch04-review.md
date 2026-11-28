# Independent review: chapter 4 (uncommitted) and chapter 5 second pass (`ece3310d`)

Repository `/Users/mgubi/ym-terminology`. Read-only review; nothing edited, staged or committed.
Line numbers are those of the files as they stand (`04-blocking.tex` working tree, 677 lines; `05-gaussian.tex` at `ece3310d` = working tree, 1388 lines).
Every corrected text below fits on the line it replaces.

## Verdicts

- **Part A (04-blocking.tex, uncommitted): ACCEPT WITH THE LISTED CORRECTIONS.** The mathematics is unchanged on all 172 lines; two added sentences say more than the evidence or the chapter supports, four short terms need a better defining sentence, and four first-use sentences about Bałaban carry no reference.
- **Part B (05-gaussian.tex, `ece3310d`): ACCEPT WITH THE LISTED CORRECTIONS.** One replacement (5:1007) narrows an estimate to an equation that covers one branch only; the five short terms are defined before use and used consistently.

| class | Part A | Part B | between chapters |
|---|---|---|---|
| ERROR | 2 | 1 | |
| LANGUAGE | 6 | 2 | |
| DICTIONARY | 3 | 1 | |
| TERM | 6 | 2 | |
| MISMATCH | | | 11 |
| MINOR | 10 | 3 | |

## Mechanical checks run

- `git diff --stat -- .../04-blocking.tex`: 172 insertions, 172 deletions; 677 lines before and after.
- Script comparing old and new files (inline math, display math, `\label`, `\ref`, `\eqref`, `\cite`):
  - Chapter 4: no label, reference, citation or math segment removed or altered; all display environments identical. Added: `\ref{ch04:kernel-section}`, `\ref{ch04:frame-lemma}`, `\eqref{ch05:nonlinear-tree}`, `\ref{ch05:gaussian}`, `\eqref{ch04:relaxed-test}`, `\ref{ch10:choices}`, `\cite{Balaban1987RG}`, and 30 inline math segments that restate existing symbols (listed under item 7).
  - Chapter 5: display environments identical; three `$\ZZ^4$` removed (735, 751, 828); added `\ref{ch05:histories}`, `\ref{ch05:transports}`, `\eqref{ch04:frame-first-power}`, `\eqref{ch05:tree-comparison}`, `$r_A$`.
- All added labels exist (`ch05:nonlinear-tree` at 5:1014, `ch10:choices` at 10:23). `Balaban1987RG` exists in `references.bib`.
- Brace and `$` balance of both files: balanced. No doubled words.
- `references.bib` contains four Bałaban papers only: `Balaban1984Propagators` (B84a), `Balaban1985Variational`, `Balaban1987RG` (B87), `Balaban1988Expansions` (B88b). B85a, B85b, B88a, B89b, B95 and Dimock's papers have no key.

---

## PART A: 04-blocking.tex

### ERROR

**A1. Line 16: "several of Bałaban's papers".**
- Old: `$m+1\to m$. Write $L=L_m$, fix a positive integer smoothing order $j$,`
- New: `$m+1\to m$; unlike in several of Ba\l{}aban's papers, a step is not followed by a rescaling to the unit lattice. Write ...`
- The *Literature* line of *step* names B84a, B95 and D1 for the rescaling. D1 is Dimock's; that leaves two papers of Bałaban, of which only B84a is about gauge fields. "Several" exceeds the evidence, and no reference is given.
- Corrected (rest of the line unchanged): `$m+1\to m$; unlike in some of Ba\l{}aban's papers (for instance~\cite{Balaban1984Propagators}), a step is not followed by a rescaling to the unit lattice. Write $L=L_m$, ...`

**A2. Line 452: "The word regular thus has two uses".**
- New: `... The word regular thus has two uses, as in his papers: the regular part of the action, and the regularity condition. ...`
- False for the chapter as it stands: line 532 has "the regular expressions" and line 584 "the regular local expression", a third use (the editor left them, basis I, and says so in the report). The statement about Bałaban is supported by the *Literature* line of *regular*.
- Corrected clause: `The word regular has two technical uses, as in his papers: the regular part of the action, and the regularity condition.` The author must also decide lines 532 and 584; I cannot propose a replacement because the dictionary does not determine what "regular expression" means there.

### References missing from added sentences (counted under MINOR)

All four statements are supported by the dictionary's *Literature* lines, but none gives a reference, and the project standard asks for one.

- **Line 226** (delta function; "the coarse field equals the average exactly"). Supported by *penalty parameter* (B87 (0.17), B85a (10), B84a (1.12)) and *mismatch* ("the new field equals the average exactly"). Add `~\cite{Balaban1984Propagators,Balaban1987RG}` after "gauge fields".
- **Line 428** (regularity conditions "on a nested sequence of domains with scale-dependent bounds"). The evidence is one paper, B85b p. 77 (entry *`Bad_m(U)`*), which has no key in `references.bib`; the same entry quotes B87 p. 254 with a single bound `|U(∂p) − 1| < ε_0`, so "who imposes" generalises. The entry also records a second condition on `D*∂U`, omitted here. Corrected (rest of line unchanged): `... The term regularity condition is Ba\l{}aban's; his spaces of regular configurations carry bounds on the plaquette variables on a nested sequence of domains, depending on the scale; here the condition is a single inequality at one scale, and the large-field set is neither enlarged nor summed over. This definition is`, with a new bib entry for B85b (Commun. Math. Phys. 99, 75–102 (1985)).
- **Line 452** (localized terms; "activity for polymer activities only"). Sources per the dictionary: B87 pp. 256–257 and B88b p. 259 (keys `Balaban1987RG`, `Balaban1988Expansions` exist); "activity" rests on B88a p. 14 and B89b (no keys). Add `~\cite{Balaban1987RG,Balaban1988Expansions}` after "are Ba\l{}aban's".
- **Line 591** (linear size). Source: B87 p. 257. See A-L2 for the corrected text with the citation.

Line 213 is the only added sentence with a citation; the key exists and the *Literature* line of *block average* supports it (B87 (0.4), (0.12); the formula itself is quoted there from B85a (15)). The statement about the chapter ("on the minimizing branch it is the nearest group point to a weighted mean") agrees with line 201.

The other first-use sentences are true of the chapter: line 5 (table); line 16, smoothing order (line 186: `j`-fold convolution); line 36 (contour, contour variable); line 43 (`g_x^{z,o}=T_U(z\to x;o)` makes the links along the contours from `z` equal to one; the normalized `h` differs by a constant conjugation, line 47); line 431 (see item 7); line 651 (the parenthesis repeats 10:25–26 word for word).

### TERM

**A3. Line 132: "Normalize two minimizers".**
- Old: `Center two minimizers $h,k$ in this way and set`. New: `Normalize two minimizers $h,k$ in this way and set`.
- "Normalized" already means `h_0=1` in this chapter (43, 46, 58, 111, 174), and line 111 is in the same proof. "In this way" refers to lines 119–120 (left multiplication so that `1` is nearest to the centroid), which the proof needs at line 138. The dictionary proposal (*centered* 3, R) collides here.
- Corrected: `Multiply two minimizers $h,k$ on the left in this way, so that $1$ is nearest to each centroid, and set`

**A4. Line 189: the averaging operation "minimizes".**
- New: `... The gauge-covariant \emph{averaging operation}, obtained by projecting the weighted` / `average of the transporters to the group, minimizes`
- An operation (the map `U ↦ Q_e^pred`, line 213) does not minimize `P_e(u)`; its value does. Lines 205, 383, 395 say "the value of the averaging operation". The defining sentence also covers one branch only.
- Corrected line 189: `Put $\bar Y_e=\sum_z w_z^{\rm av}Y_{e,z}$. The value of the gauge-covariant \emph{averaging operation}, obtained on the first of two branches by projecting the weighted`

**A5. Line 65: "This condition, the loop condition".**
- The sentence follows the display of the energy (59–64); "this condition" can be read as the minimization or as `h_0=1`. The condition meant is at line 57.
- Corrected: `The condition that all these distances be below $\delta_{\rm fr}$, the \emph{loop condition}, includes every order $o_0$, so it does not privilege a preliminary`

**A6. Lines 226, 232, 234: one kernel, three names.** "the block kernel" (226), "Exact block map" (232, unchanged), "the kernel of the step" (234, new). Chapter 5 says "block kernel" (5:103, 1163, 1376).
- Corrected line 234: `For $\beta\ge0$, define the block kernel of the step and its action on fine densities by`

**A7. Line 489: relaxed regularity condition.** Defined at first use and not used again in the chapter (it is for chapters 6, 9). "The regularity condition with the exponentially weighted threshold" does not say on which set; the regularity condition of line 426 is relative to a set `X`.
- Corrected sentence: `We call the condition in \eqref{ch04:relaxed-test} the \emph{relaxed regularity condition} at $x$: the regularity condition on the whole lattice, with $t_m$ replaced by the threshold $t_m e^{\operatorname{dist}(x,y)/R^{\rm rel}}$ growing exponentially with the distance from $x$.`

**A8. Figure caption, `figures/block-paths.tex:38–41`** (input at line 215, cited at 182): still "connectors", "frame factors", "framed transport", "block average". It prints inside chapter 4 beside the new words. The editor reports this; it is outside the edited file and must be fixed with it.

Other defining sentences checked and found correct, defined at or before first use, and used consistently: *transporter* (174; used 183, 190, 206, 378, 393); *axial* gauge transformation (43; used 68, 106, 145, 361); *averaging weight* (186; announced at 16 with a section reference; 375); *auxiliary index* and *probability weight* (217–218); *representation data* (550; plural agreement correct at 550, 567, 625, 656, 670–671, 676); *dependence set* (459; used 461, 493–494, 539, 607); *anchored* / *containing-site* sum (603–605); *eligible pair* (68–69, unchanged; 76, 224); *exact cover* (547, unchanged; forward use at 462 says "below"); *initial point* (36, 43); *large-field set* (425); *localized term*, *localization domain*, *large-field activity*, *exclusion support*, *prescribed large-field set* (435–441); *connected covering number* (587); *stage* (651). No collision with chapter 5 except those listed under MISMATCH.

Traps checked: "averaging operation" is the nonlinear map throughout chapter 4 (no linear operator occurs); "localized term" replaces "regular activity" only where `E_i^reg` is meant (9, 435, 573, 603, 627, 637–638, 642), and both kinds are named where the old text said "activities" (452, 539, 659, 673); the proof-internal index `α` of 322, 330 is "contour index", not "auxiliary index"; "holonomy" is used only for the closed contour of 50–54 and 277; "path" survives only in "path coefficients" and for counted paths; "critical configuration" (166) and "scale index" (15, 652) follow the table.

### DICTIONARY

**A9. Lines 36, 89, 106, 161, 279: "initial point" for *root*.** The *Proposed* word of *root* 1 (R) is "base point"; the editor used the *Literature* word because *anchor* 1 (D) also proposes "base point" (435, 506, 573, 606, 657). The choice is sound, and the dictionary needs the decision recorded. Chapter 5 has a third "base point" (5:902, the real base point of an analytic continuation).

**A10. Line 173 (and 369): "patch of the local gauge transformation".** The entry *block-average patch* (R) proposes "the patch `Ly + 𝔹_R` of the averaging operation, defined once in chapter 4". The editor followed chapter 5 (5:976) instead. The two chapters agree with each other and not with the dictionary; one of the two must change.

**A11. Lines 147–151, 161: "hyperplane" for *layer* (R).** Applied as proposed, but the argument is an induction over slices with `r` varying coordinates: for `r<4` the layer is a section of the slice, and the "chosen hyperplanes" of 161 are four nested sections ending in a point.
- Corrected line 147: `hyperplane of the slice perpendicular to the last coordinate whose internal plaquette sum`
- Corrected line 160–161: `... the chosen` / `sections, one in each dimension, specify an initial point. At $r=4$ the bound is \eqref{ch04:axial-eligible}`

No proposal of basis I or ? was applied. Where an entry of basis I was involved the editor either left the word (*branch*, *read*, *rotation*, *declared*, *regular expression*) or used the manuscript's own phrase ("alternative branch", already at 4:211, for *fallback*). "actual" in the title 293 was deleted, which the table's definition of "averaging operation" as the nonlinear map covers. Line 421 "sequence of scales" for "scale schedule" agrees with the entry *trajectory* ("scale schedule (the sequence of scales only)"). Line 296 follows *tree comparison* 1 (R).

### LANGUAGE

**A-L1. Line 428: "The term is Ba\l{}aban's".** The antecedent is three sentences back. See the corrected text under line 428 above ("The term regularity condition is ...").

**A-L2. Line 591: "it plays the role".** "It" can be the weight or the covering number.
- Corrected end of line: `supports without requiring a support itself to be connected; the covering number plays the role of the linear size of a localization domain in Ba\l{}aban's papers~\cite{Balaban1987RG}.`

**A-L3. Lines 651–652: "that index".** After "regularity-stage index" became "the stage", "that index" has no antecedent.
- Corrected end of line 651: `...; see Section~\ref{ch10:choices}); the stage index` (652 unchanged).

**A-L4. Lines 209–210: "let the value $z$ of the index choose".**
- Corrected line 210: `let the index take the value $z$, and set $Q_e^{\rm pred}=Y_{e,z}$, with probability`

**A-L5. Lines 315–316: "every choice, of positive probability weight, of the indices ...".** Parses, but heavily.
- Corrected 315: `averaging operation of \eqref{ch04:predictor-cost}, every value of positive probability weight` (316 unchanged).

**A-L6. Line 539: "Their dependence sets".** After "the exclusion supports of the latter", "Their" is ambiguous.
- Corrected: `... are those of Definition~\ref{ch04:activities}. The dependence sets of the large-field activities also contain the links needed for every condition; ...`

### MINOR

- Line 456: "will be disjoint" → "will be pairwise disjoint" (as at 544).
- Lines 505–506 and 605: "support" now also stands for the footprint of an expression and for the localization domain, beside the two meanings discussed at 455–464. At 605 write `whose localization domain or exclusion support contains $x$`.
- Lines 358, 362, 367 (unchanged): "comparison gauge $H$", "pure gauge $fH^{-1}$", "an axial gauge $H$" are gauge transformations of the same kind as `f`, now called "local gauge transformation". Not converted.
- Lines 121, 127 (unchanged): "Coordinatewise minimization", "the old coordinate $h_x$" beside line 334, where "frame coordinate" became "the gauge transformation at one point".
- Lines 349–362, 379 (unchanged): "coordinate-path gauge", "path count", "middle straight path" are contours in the table's sense (links are multiplied along them); the editor flags 379 as borderline.
- Line 26: "transformed by common local gauge transformations" reads less clearly than the old "expressed in common gauge frames"; acceptable.
- Line 150 (unchanged): "its transported link" beside the new "transporter".
- The four missing references and the generalisation at line 428, above.

### Item 7: changes in Part A that are not vocabulary

All were checked against the chapter and are mathematically faithful.

- Cross-references added: 16 (`ch04:kernel-section`), 224 (`ch04:frame-lemma` for "the frame lemma"), 296 (`ch05:nonlinear-tree`, `ch05:gaussian` for "the later tree comparison"), 489, 651 (`ch10:choices`).
- Symbols or formulas written where the old text had words: 128 (`F_x(h)`), 203 (`ε_pred`), 309 (`𝒫_y(U)`), 361 (`f`), 383 (`Q∈G`), 397 (`χ(V_eQ_e(U)^{-1})`, `e∈∂p`, matching (4.macro-comparison)), 407, 418, 533 (`β`), 428 (`χ(U_□) ≤ t_m`, equivalent to `X ∩ Bad_m(U) = ∅`), 525 (`Σ_{x,i}A_i^{(2)}(U,x)`, the term of line 517 without the factor `β`), 528 ("quadratic below `t` and linear above", true by (4.clip)), 658 (`v_sc`).
- Sharpened: 438 "small-field configurations" → "configurations satisfying the regularity condition on $X_i$" (the set is that of line 580); 657 "supports" → "localization domains, exclusion supports".
- New content: 431 "whose sum is the regular part of the action". With `V_ρ` of line 555 the regular part is `Σ_i h_{X_i}E_i^reg`, the sum of the terms multiplied by their indicators; "sum" is slightly loose but agrees with the entry *regular* 1.
- The eleven first-use sentences.

---

## PART B: 05-gaussian.tex, commit `ece3310d`

### ERROR

**B1. Line 1007: the estimate for the local gauge transformations.**
- Old: `estimate for the local gauge transformations, linear in the plaquette sum, controls the discrepancy at each of the two roots from its local gauge transformation;`
- New: `estimate \eqref{ch04:frame-first-power} for the local gauge transformations controls the discrepancies at the two roots;`
- (4.frame-first-power) is stated for a minimizing local gauge transformation (4:320–329). The estimate (5.nonlinear-tree) is claimed for every configuration and needs both branches (4:296–297); the alternative branch is handled at 4:361–365. The old sentence named the estimate generically; the new one pins it to an equation that covers one branch. It also drops "linear in the plaquette sum" and what the discrepancy is measured from. Mitigation: 5:1019 (unchanged) already cites the same equation, so the narrowing repeats an existing imprecision.
- Corrected: `estimate for the local gauge transformations in the proof of Lemma~\ref{ch04:predictor-comparison}, linear in the plaquette sum, controls the discrepancies at the two roots;`

### LANGUAGE

**B2. Line 731: "tori of unbounded side length".** A torus has a side length; the sequence is unbounded.
- Corrected: `limits on a sequence of tori with unbounded side lengths suffices (the \emph{periodization criterion}): for fixed $z$,`

**B3. Line 1303: missing conjunction** (older than this commit, but on a changed line): "satisfying \eqref{ch05:path-budget}, the quadratic hypothesis in".
- Corrected: `and the quadratic hypothesis leading to`

### TERM

**B4. Line 1058: quadratic hypothesis.** Defined before its three uses (1303, 1374, 1382) and used consistently. The definition is attached to "Identifying their sum with a chosen metric $H_f$", so it is not said whether `H_f ≥ εI` (line 1053) is part of it; the dictionary's meaning (*quadratic coefficient condition*, D) includes it. The uses cite (5.actual-hessian), which is the resulting Hessian formula, not the hypothesis; the dictionary notes that this identification was not checked.
- Corrected: `condition on the incoming path action; with $H_f\ge\varepsilon I$ it is called the \emph{quadratic hypothesis} below.`

**B5. Lines 1151, 1153, 1234, 1311: chart or gauge.** `W_F` is "the representative in the block axial gauge" (1151, 1311) and "its representative in the block axial chart" (1234). Line 1153 says an estimate is "asserted for $W_a$, not for the block axial chart", an operator against a chart.
- Corrected line 1153: `for the representative $W_F$. Gauge-invariant quadratic insertions see the same`

The other terms: *blocking sequence* is defined at 303, announced at 10 with a reference to the section, and no "sequence of blocking parameters" remains; *link multipliers* is defined at 335 (the symbol `r_L` is introduced unnamed at 163) and used at 760, 762; *periodization criterion* is defined at 731 and used at 828, 849, where it replaces the same description; *block axial chart* is defined at 930 (the title 912 precedes it) and used at 1061, 1078, 1153, 1234, 1289, 1304. None collides with a dictionary headword of another meaning or with a word of chapter 4.

### DICTIONARY

**B6. Line 859: "operator $W$ of Section~\ref{ch05:transports}".** Old: "operator $W$ built with the linear averaging operator". The table asks for the representative to be named wherever `W` is unqualified. The reference is correct (5:535 identifies that `W` as `W_s`), but the name is lost.
- Corrected: `operator $W=W_s$ of Section~\ref{ch05:transports} also preserves convergence. These are statements`

### MINOR

- Lines 735, 751, 828: `$\ZZ^4$` removed three times ("infinite lattice $\ZZ^4$" → "infinite-lattice"). No information is lost (5:711 has `z∈ℤ^4`), but the editors were told not to touch math.
- Line 1283: "Penalty terms of the block kernel" → "Penalty terms". The entry *block penalty* 2 asks for the qualified phrase; it occurs at 5:1163.
- Lines 760–761: "the link multipliers used in \eqref{ch05:history-filter}"; that display contains only centered-box factors, the link multiplier enters at 335. Older than this commit.

### Item 7: changes in Part B that are not vocabulary

- Cross-references in place of descriptions: 10, 859, 1007 (B1), 1375 (`ch05:tree-comparison` for "in the block axial gauge"; correct, it is the inequality of 1036–1040 and agrees with 1289–1291).
- 418 and 779: "the estimate of the accumulated / propagated noise" → "the noise estimate"; the estimate is at 399, inside the proof of the proposition cited at 780.
- 656, 660: "positions within the block" → "such positions", "every position"; the antecedent is at 654.
- 1290, 1375: "in that gauge", "in the block axial gauge" dropped.

All other lines of the commit were read and say what they said before.

---

## MISMATCH: chapters 4 and 5 as they stand

| # | object | chapter 4 | chapter 5 |
|---|---|---|---|
| 1 | one block transformation | 4:5, 30 "renormalization transformation", "step" | 5:14, 84 (title), 114 "block transformation" |
| 2 | weight of the auxiliary index | 4:77, 209, 218 "probability weight" | 5:970 "Redundant uniform branch masses" |
| 3 | the weight `w^av` | 4:186, 375 "averaging weight(s)" | 5:993–994 "the convolution weights"; 5:153–154 "averaging kernel of total mass one" |
| 4 | box of radius `(j+7)L` | 4:298, 367, 398 "macro-box" | 5:1028, 1031, 1032 "macro-patch" (5:1005–1006 "macro-box") |
| 5 | covariance of the averaging operation | 4:189 "gauge-covariant" | 5:206 "gauge-equivariant averaging operation" |
| 6 | the patch `Ly + 𝔹_R` | 4:173 "patch of the local gauge transformation at $y$" | 5:976 "... at $Ly$" |
| 7 | the site `Ly` and the normalization `h_0=1` | 4:51 "patch center", 4:181 "coarse endpoints", 4:43, 58 "normalized" | 5:995, 1002, 1007 "block roots", "the two roots"; 5:997 "root normalization" |
| 8 | action of the index | 4:210 "choose" (was "select") | 5:968, 1293 "selects", "select" |
| 9 | the terms of the representation | 4:431–452 "localized terms", "large-field activities" | 5:861 "nonlinear activity arrays" |
| 10 | the kernel `k_β` | 4:234 "kernel of the step" (4:226 "block kernel") | 5:103, 1163, 1376 "block kernel" |
| 11 | "base point" | 4:435 base point `o_i` of a localized term | 5:902 "real base point $x$" of an analytic continuation |

Agreeing: local gauge transformation (4:43; 5:950, 977, 1007); auxiliary index (4:217; 5:948, 968); averaging operation; smoothing order (4:16; 5:202, 304); contour and contour variable (4:36; 5:995, 1003, 1008); loop condition and the condition on the minimum (4:65, 209; 5:967); gauge-transformed parallel transporter (4:174; 5:986); the axial gauge of chapter 4 against the block axial gauge of chapter 5 (4:43, 296; 5:937, 1005); penalty parameter (4:226; 5:88, 312); stage (4:651; 5:689); "initial point" does not occur in chapter 5, and "root" there is the root of a spanning tree, which the dictionary keeps.

## Not checked

- Bałaban's and Dimock's papers themselves: every statement about them was compared with the dictionary's *Literature* lines only, which record partial reading from OCR.
- The build and the rendered pages: I did not run LaTeX (the editor reports a clean `latexmk` run); long lines such as 4:16, 4:452 were not inspected for overfull boxes.
- Whether the first-use sentences of chapter 4 duplicate or contradict chapters 1–2, the main theorem or the reading guide.
- Chapter 5 outside the 51 lines of `ece3310d`, except by keyword search for the comparison table; the first pass `114af230` was not reviewed.
- The correctness of the dictionary's own meanings and proposals, the Lean sources, and `audit/chapter-conversion/ch05-shorten.md`.
- Chapters other than 4 and 5 that use the renamed terms (6, 7, 9, 13ba, 17c).
