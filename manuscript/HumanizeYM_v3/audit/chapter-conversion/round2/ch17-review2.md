# Second review r10: 17-trace-law, 17-variable-windows, 17-trace-transfer, 17-current-contraction, 17-marked-trace-rates

Worktree /Users/mgubi/ym-terminology, files under manuscript/HumanizeYM_v3/chapters/. I read the word diffs `4f462ac5..HEAD` of all five files in full before the reports ch17-review.md, ch17-17w-17t-apply.md and ch17c-17m-18-19-apply.md. Every changed line (47 + 46 + 48 + 109 + 132 = 382 lines) was checked against the present text around it, the dictionary entries, and the committed chapters 5, 6, 7, 10, 11, 14 and 15 where they define a term or a label.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 17w:97 | ERROR | imposed at the actual bottom stage, | imposed at the stage of the lowest scale of the interval of scales, | "Lowest scale" is ambiguous: scale indices increase towards the fine lattice. *bottom* says the end meant is the coarsest level of the interval (the last backward stop from `n`, 17w:31–33). | imposed at the stage of the coarsest scale of the interval of scales, |
| 17w:35 | TERM | The schedule bound $L_i\le\log\widehat\beta_i$ makes each | The bound $L_i\le\log\widehat\beta_i$ of the sequence of scales makes each | Chapter 10 defines the *schedule* (10:121); "sequence of scales" is a second name for it, introduced only here. | The schedule bound $L_i\le\log\widehat\beta_i$ makes each |
| 17c:75 | LEFTOVER | two factors of the block average $M_a$ there. | (unchanged; first review restored it) | `M_a = L^{-1}Σ_v s_a^v` (17t:20) is a plain mean of `L` translates acting on base points. It is neither the averaging operation nor the linear averaging operator `M` of chapter 5 (5:993). After the conversion "block average" occurs nowhere else in the book except the title 17t:12, so here it would read as the old house term. | two factors of the average $M_a$ there. |
| 17c:265 | TERM | At coarse anchor zero the displaced coarse current is | At coarse base point zero the transferred coarse current is | `Y'_b` in (17.actual-current-map) is the coarse vector field (the old "displaced" pointed at the displacement `Y`). "Transferred coarse current" reads as `J'`, the transferred current of 17t:64. The section speaks of the "map on vector fields" (247) and "the coarse vector field $R_fY$" (290–291). | At coarse base point zero the transferred coarse vector field is |
| 17m:87 | TERM | Fix the full dependence region of a rooted connected component | Fix the full dependence set of … (first review restored "full") | The term defined in chapter 4 (4:459) is *dependence set*. That set already consists of all the links on which the term depends; the contrast with the score stencil is made at 17m:118. | Fix the dependence set of a rooted connected component |
| 17m:92 | MINOR | For finite ordinary selections, | For finite small-field subfamilies, | "selections" → "subfamilies" is not a dictionary replacement (*ordinary* covers only the adjective). It changes a word whose meaning the text does not fix. | For finite small-field selections, |
| 17t:145 | LEFTOVER | must be retained as marked remainders. | (unchanged) | *mark* sense 3 (R) lists 17t:145; elsewhere in 17m that sense was rendered as "with insertions". | must be retained as remainders with insertions. |
| 17:33 | LEFTOVER | The fact that inserting the identity leaves | (unchanged) | The text says bare "identity". Two lines earlier it says "identity field", and *unit* says never to write bare "identity". | The fact that inserting the identity field leaves |
| 17c:284 | LEFTOVER | differentiation adds only finite path-length factors. | (unchanged) | The previous line (283) now says "Their fixed contours". The table reserves "path" for path action, path coefficients and paths that are merely counted. | finite contour-length factors. |
| 17m:34 | LEFTOVER | a fixed power of the path length. | (unchanged) | Line 32 now says "contour-variable representative". The same reason as 17c:284. | a fixed power of the contour length. |
| 17m:251 | DICTIONARY | Choose $j$ above the fixed probe order. | Choose $j$ above the order of the coefficient evaluations. | *fixed probe order* has basis I (one occurrence, read from context). The replacement is vague but not false. Restoring "probe" would clash with the defined probe of chapter 3. | left for the author: suggest "Choose $j$ larger than the degrees of the finitely many polynomial fields used." |
| 17m:409 | DICTIONARY | For an actual exponentially local spectator, | For an exponentially local spectator that need not have finite range, | This applies *actual* sense 6, which has basis I. The qualifier is plausible from 17m:408–410. (The first review listed this too.) | left for the author |
| 17t:405; 17c:241, 391 | MINOR | at the fixed output level / At a fixed output level | at a fixed scale | "output" (the end of the run of transfers, *output level* sense 2) is dropped. The new wording is consistent across the three lines and avoids the chapter 11 "output scale" `w`. | left (acceptable); see "For the author" |
| 17c:359–360 | LANGUAGE | within the gauge-covariant block average and averaging patches | within the patches of the averaging operation and the averaging patches | The juxtaposition reads oddly. The meaning of the second patches is inferred (basis I, App. D). | left for the author |
| 17c:373–374 | LANGUAGE | transform its output frame and the differential … | transform the local gauge transformation at its output and the differential … | Clumsy but correct. | left |
| 17t:125–126 | LANGUAGE | same one-loop normalization … using the actual action | … using the same action | Repeats "same". Correct (17t:84). | left |
| 17w:11 / 17m:428 | MISMATCH | linear marked-column constants / accumulated pre-ratio column costs | linear column constants with insertions / accumulated ratio-independent coefficient-map factors | One group of constants `C_j` (multiplied along the interval of scales) now has "column" in 17w and "coefficient-map" in 17m. In 17w "with insertions" also attaches ambiguously. The book itself mixes "column bound" (11, 11E, 13ba, 18gq, 18lp) and "coefficient-map bound" (10:83). | left for the author |
| 17w:97 / 17m:433 | MISMATCH | positive partition estimate / actual positive-density estimate | positive partition estimate / lower bound on the partition function in (11.replicated-bound) | *positive partition estimate* asks for one name. That 17w:97 means the same bound has basis I. | left for the author |
| 17w:54–56 vs prose | MISMATCH | `\text{ in window}` in (17.window-product) | unchanged (math) | The prose says "interval of scales" but the display still prints "window". Math may not be edited under the rules. | left for the author |
| 17c:138 (title) | DICTIONARY | The nonlinear terms need fixed-ratio bounds | unchanged | This is the last "fixed-ratio" in the file. 17w:72 and 17m:429 now say "ratio-dependent". It is a title. | left for the author |
| 17t:12 (title) | LEFTOVER | Difference-preserving block averages | unchanged | The averages `M_a`, `K_0`, … are plain means. This is the last "block average" in the book. It is a title. | left for the author (suggest "Difference-preserving averages") |
| 17m:26, 163; 17c:55 | LEFTOVER | stationary kernels; exact stationary identity | unchanged | "stationary" in phrases whose object the dictionary does not settle (kernels of the critical-configuration map? the identity `K_fW = …` of chapter 5?). | left for the author |

All other changed lines were found correct. In particular:
- 17:128 (Proposition 14.smooth-comparison, "Derivative transport and smooth comparison", exists at 14:230).
- 17:309 (Proposition 17.spatial-moments, "Low-moment estimate for spatial remainders").
- 17:341 ((14.conserved-line) is `dim ker(div|_𝒦) = 1`).
- 17w:78 ((11.lower-weighted-step) at 11:1566).
- 17w:93 (Lemma 11.restore-regular, "Regular remainders at the larger source weight"; (11.n-mark-root)).
- 17m:440 (the weights `ω_i` are in (11.replicated-bound)).
- 17m:439 ("per-site normalization exponent", as at 12:247 and 13sb:25).
- 17:130 ("reflected copies", from *uniform in the number of reflected copies*, R).
- 17:370 ("free", from *label* sense 3, R; the same wording as 14:238).
- 17:32 ("undecomposed hierarchy", 14:12).
- 17c:147–149 ("joint classical action", "fluctuation coordinates", 7:872–877).
- 17c:144, 170, 176 ("gauge-fixed inverse", 7:877).
- 17m:380 ("a multiple of the identity field", *unit endpoints*, R/S).
- 17m:356 (the gloss agrees with 17:164–172).

## Corrections applied

10 in all, within lines; line counts unchanged.
- ERROR 1: 17w:97.
- TERM 3: 17w:35, 17c:265, 17m:87.
- LEFTOVER 5: 17c:75, 17t:145, 17:33, 17c:284, 17m:34.
- MINOR 1: 17m:92.

## Cross-chapter mismatches not fixed

- "full dependence set": 6:1117, 1179, 1324; 9:93, 107. The defined term is "dependence set" (4:459), and 17m:87 now uses it.
- "column bound / column constant" (11:446, 1200; 11E:19; 13ba:14; 18gq:25, 92; 18lp:64, 305; 17w:11) against "coefficient-map bound / factors" (10:83; 17m:428).
- "positive partition estimate" (17w:97) against "lower bound on the partition function" (17m:433).
- The `\text{ in window}` of (17.window-product), 17w:54–56, against "interval of scales" in the prose.
- "signed path average" (17c:257) follows 5:976 "coordinate path", while 17c:255, 258 say "contour". Chapter 5 is not mine.
- "anchored" kept at 17:224 ("anchored vector response", basis I) and 17t:482 ("anchored correction"). Elsewhere chapter 17 says "with a base point".

## Leftover house words

Kept on purpose:
- 17w:12, 52 "propagation constants" (the first review's reason, basis S).
- 17w:72 "protected-path errors".
- 17t:8, 84; 17c:42; 17:194 "path action" (a kept term); 17c:178 "path vertices"; 17c:257 "signed path average" (chapter 5 wording).
- 17t:90–91 "normalized quadratic response", "regulated response": *response* sense 7, basis I; chapter 7 no longer uses "regulated response", so the pointer may need the author.
- 17t:195 "left frame" (*frame* sense 3, basis I).
- 17:224 "anchored vector response" (I); 17t:482 "anchored correction".
- 17c:64 "completed fine kinetic matrix" (*completion* at 17c:64, basis I).
- 17m:237 "physical row" (*physical* sense 5, basis I).
- 17c:287 "stationary value" (envelope theorem, ordinary).
- "threshold" for the small-field threshold `t` (17c:316; 17m:153, 197, 272, 304, 378, 427).
- 17t:14, 29, 205, 392 "unit" (unit translation, unit vector: ordinary).
- 17m:332, 413 "two units of the exponential support exponent" (*unit* sense 3, R; no short replacement).
- 17m:331, 416 "scale-`k` units", 17m:441, 476 "continuum units" (ordinary).
- 17c:122, 381 "weights" (ordinary); 17m:316 "spare exponential support weight".
- 17m:246 "mixed polynomial moments", 17c:161 "mixed derivatives" (ordinary).
- Labels and equation names (`actual-current-map`, `actual-Q`, `actual-coordinates`, `actual-jet-integral`, `frame-linearization`, `stationary-tangent`, `stationary-higher-jets`, `window-product`, `marked-rates`) are labels.

Replaced: 17c:75, 17t:145, 17:33, 17c:284, 17m:34.

Not settled, listed for the author: 17t:12; 17c:138; 17m:26, 163; 17c:55.

## Assessment of the first review's corrections

- 17c:75 (restored "block average $M_a$"): right that `M_a` is not the linear averaging operator `M`. But "block average" is now an otherwise eliminated house term, so I replaced it with "average".
- 17m:87 (restored "full"): superseded. The defined term is "dependence set".
- 17w:97 ("lowest scale of the interval of scales"): the addition of "of scales" was right, but "lowest" stayed ambiguous. Now "coarsest".
- The other 12 corrections (17c:241, 324, 370, 391; 17m:70, 249, 400, 428, 429; 17t:297; 17:128; figure caption) are correct. I checked all of them except the caption, which is not in my files.

## For the author

- 17c:138 title "need fixed-ratio bounds" and 17t:12 title "Difference-preserving block averages". These are the last "fixed-ratio" and the last "block average" in the book.
- 17m:251 "order of the coefficient evaluations" (from a basis-I proposal) and 17m:409 "that need not have finite range" (basis I): please confirm.
- 17t:405 and 17c:241, 391 "a fixed scale": the word "output" (the scale at which the transferred current is evaluated) was dropped. If wanted, write "the fixed scale at which the current is evaluated".
- 17c:359–360: the wording "patches of the averaging operation and the averaging patches".
- 17w:11 / 17m:428: one name for the constants `C_j`.
- 17w:97 / 17m:433: one name for the lower bound on the partition function.
- The display (17.window-product) prints "window".
- 17t:90–91: "regulated response in Chapter 7" no longer matches the wording of chapter 7.

## Checks

- Line counts against `git show HEAD:<path> | wc -l`: 458/458, 125/125, 500/500, 396/396, 480/480.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r10 monograph.tex`: exit 0. In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0. The build includes the other reviewers' working-tree files as they were at that moment.
- Text extracted from the built PDF (pdftotext): every corrected sentence renders as edited.
- Nothing staged, committed, pushed or reverted.

## Not checked

- Rendered pages were not inspected visually.
- The source manuscripts and the Lean files were not consulted.
- The figure caption figures/radius-windows.tex was not checked: not in my files.
- The literature lines of the entries were not re-checked. No sentence about Bałaban's or Dimock's papers was added in these files.
