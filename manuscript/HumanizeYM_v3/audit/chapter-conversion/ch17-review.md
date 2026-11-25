# Review of the chapter 17 conversion (c8: 17, 17w, 17t; c9: 17c, 17m)

Files (worktree /Users/mgubi/ym-terminology, manuscript/HumanizeYM_v3/): chapters/17-trace-law.tex (17), chapters/17-variable-windows.tex (17w), chapters/17-trace-transfer.tex (17t), chapters/17-current-contraction.tex (17c), chapters/17-marked-trace-rates.tex (17m), and the caption of figures/radius-windows.tex. The word diffs were read in full before the reports c8-apply.md and c9-apply.md. Every changed line was checked against the committed text, the dictionary entries (displacement, stationary substitution, stationary tangent, tangent, actual stationary tangent, response, current defect, pre-ratio constants, fixed-ratio jet errors, window, radius window, comparison level, comparison window, output level, coupling threshold, threshold, alias, principal, amplitude, anchor, anchored, anchor average, exterior, low moments, mark, marked replacement, moving, label, ordinary, regular, complementary, failure, bottom, frame, transport, block average, block-average patch, box-filter identity, unit, unit endpoints, density-valued insertion, equation direction, terminal norm bounds, positive partition estimate, physical mark normalization, exterior discrepancy, coupling band, raw, tail, stage plateau, schedule, common localization, amplification, actual) and Appendix D, and against the committed chapters 5, 7, 11, 14, 15.

## Review findings

| file:line | class | committed text | edited text | what was wrong | corrected text |
|---|---|---|---|---|---|
| 17c:370 | ERROR | Derivatives of the gauge-covariant block average or its frame correction multiply lower | Derivatives of the averaging operation or of its local gauge transformation multiply lower | "frame correction" (the root correction `d_V R_0`) became the gauge transformation itself: the derivatives are those of the correction, not of the transformation. c8 rendered the same phrase at 17t:157 as "the correction from the local gauge transformation". | Derivatives of the averaging operation or of the correction from its local gauge transformation multiply lower |
| 17:128–129 | ERROR | Thus the strip removal and derivative-transport / argument of Section~\ref{ch14:comparison} applies to these windows. | Thus the bound on the coincident-coordinate strips and Proposition~\ref{ch14:smooth-comparison} / of Section~\ref{ch14:comparison} apply to these intervals of radii. | The committed line says the *argument* applies to the intervals of radii; the edit says the *Proposition* applies, but Proposition 14.smooth-comparison is stated on compact sets of separated configurations (14:229–239). Claim sharpened. | Thus the bound on the coincident-coordinate strips and the argument of Proposition~\ref{ch14:smooth-comparison} / of Section~\ref{ch14:comparison} apply to these intervals of radii. |
| 17c:75 | MISMATCH | two factors of the block average $M_a$ there. | two factors of the linear averaging operator $M_a$ there. | `M_a = L^{-1}Σ_v s_a^v` is a Laurent polynomial in shifts acting on base points (17t:19–21), not the linear averaging operator `M` on link fields (5:993, 5:1084). c8 kept "block averages" for these `M_a` (17t:12 title, reason stated in c8). The dictionary's *block average* sense 2 does not list 17c:75. | committed wording restored: two factors of the block average $M_a$ there. |
| 17c:241, 391 | MISMATCH | At a fixed output level / at each fixed output level. At that level | At a fixed output scale / at each fixed output scale. At that scale | "output scale" is the chapter 11 name of the lowest scale `w` (11:2088 "middle or output scale"); here the level is the scale `k` at which the current is evaluated (*output level* sense 2, which says it is not `w`). c8 wrote "a fixed scale" for the same level at 17t:405 for this reason. | At a fixed scale / at each fixed scale. At that scale |
| 17m:249, 428, 429 | MISMATCH | the same pre-ratio row bounds. / accumulated pre-ratio column costs / Fixed-ratio nonlinear jet constants | the same row bounds, independent of $L$. / pre-ratio coefficient-map factors / Fixed-ratio nonlinear (unchanged) | The two editors rendered *pre-ratio constants* (basis R; 17m:249, 428, 429 are in its *Where*) differently: c8 "ratio-independent / ratio-dependent" (17w:24, 72, 75, 76), c9 "independent of $L$" at 249 (a symbol added after a word) and the house words kept at 428–429 (c9 cited basis I, but the *pre-ratio constants* entry is R for these lines; only *fixed-ratio jet errors* at 17w:72 is I, and that is about the identification of the errors, not the word). | 249: obey the same ratio-independent row bounds. 428: ratio-independent coefficient-map factors. 429: Ratio-dependent nonlinear |
| 17t:297 | MISMATCH | Let $Z_b$ be any anchored gauge-covariant displacement, | Let $Z_b$ be any anchored gauge-covariant vector field, | c9 rendered the same chapter 17 "anchored" (a local function with a distinguished site, *anchor* sense 1, D, which lists ch. 17) as "with a base point" (17c:13, 185, 186); c8 kept "anchored" here (and at 17:224, where *response* 11 is basis I, rightly left). | Let $Z_b$ be any gauge-covariant vector field with a base point, |
| 17c:324 | MISMATCH | the mass-one anchor average | the base-point average with total sum one | 17t:42 (c8) renders the same "mass" of the same kernels as "coefficient sums are one". | the base-point average with coefficient sum one |
| 17m:70 | TERM | has zero exterior moments. | has zero exterior moments, that is, zero integral against every function independent of the varied links. | The new gloss (a defined short term, used at 155 and 443) says "every function"; the identity it glosses (17m:66–67) is stated for "every spectator independent of the varied coarse links", which is also *exterior* sense 2. Broader than the text. | … that is, zero integral against every spectator independent of the varied links. |
| 17m:400 | TERM | The same score source is used for every $A$ | The same score insertion is used for every $A$ | New phrase "score insertion"; the entry *density-valued insertion* (variants: score source) proposes "the differentiated kernel", which c9 itself used at 17m:391 two sentences earlier. | The same differentiated kernel is used for every $A$ |
| 17m:87 | MINOR | Fix the full dependence region of a rooted connected component | Fix the dependence set of a rooted … | "full" dropped; it carries the contrast with the score stencil (17m:119 "the full rooted component, not just the score stencil"). | Fix the full dependence set of a rooted connected component |
| 17w:97 | MINOR | imposed at the actual bottom stage, | imposed at the stage of the lowest scale of the interval, | Rendering correct (a stage, the one containing the lowest scale of the window, as *bottom* says), but "the interval" has no near antecedent (the paragraph speaks of cells and the chessboard bound). | … at the stage of the lowest scale of the interval of scales, |
| figures/radius-windows.tex:19–23 (caption) | DICTIONARY | Overlapping comparison windows … At level $n$ … two neighbouring levels. Successive windows | (not edited) | Caption still used "comparison windows", "level", British "neighbouring", against "intervals of radii" and "scale" now in 17:129–146. | Overlapping intervals of radii for the trace law … At scale $n$ … two neighboring scales. Successive intervals |
| 17c:373–374 | LANGUAGE (not changed) | transform its output frame and the differential … | transform the local gauge / transformation at its output and the differential … | "transform the local gauge transformation" is clumsy but correct (the output frame is changed together with the differential). Left; see below. | — |
| 17t:126 | LANGUAGE (not changed) | already calculated using the actual action | already calculated using the same action | "same normalization … using the same action": repetition, but correct (17t:84 "the same admissible path action"). Left. | — |

No other problems found. In particular:

- **24 November lines, content intact.** 17c:48–53: only "stationary substitution" → "critical-configuration map" (48); the statements that the derivative is the forest representative `W_F` of (5.stationary-tangent), that `W_F − W_a` is a fine gradient and that the computation uses `W = W_a` are word for word as committed. The derivative "from coarse to fine link variables" is the derivative of `V ↦ U_stat(V)`, which chapters 5 and 7 call the critical-configuration map (5:1145, 7:1150), so the rename does not change the object. 17c:112–113: "kill" → "annihilate" only. 17c:164–166: the reference-tree sentence is unchanged; "stationary branch" → "critical-configuration map", "two forest slices" → "the slices of the block axial gauge for two forests" (7:891 wording), "forest slice" → "slice of the block axial gauge"; same content. 17m:263–264: "the actual tangent" → "the linearization of the critical configuration"; `W_a = W_s − d_fERW_s` and "Its difference from `W_s` is a fine gradient" unchanged. No restoration needed.
- **Representatives of `W`.** No representative is newly named where the committed text leaves `W` unqualified. 17c:8, 187, 210, 323 and 17m:193, 202 say "the linearization (of the critical configuration)" without a letter; 17c:61 "of `W`" keeps the committed `W` (fixed as `W_a` at 17c:53); 17t:161 "the bound for the smooth representative" stands before the printed `∇_f^rW_a`; 17m:221 "the linearization built with the linear averaging operator" is `W_s` by 5:1084 and 7:1112 and agrees with the `W_s p` of 17m:241. This agrees with 5:1145–1152 and 7:883 ("the full linearization of the critical configuration in the smooth centered representative").
- **displacement.** The defining passage 17:191–193 now reads "Here $Y$ is a left vector field on the links": `Y_b^x` assigns a Lie-algebra element to each link and generates `U ↦ e^{sY}U` (17t:182–184), which is what the entry (basis D) records. Both editors use "vector field" (17:193; 17t:182, 297, 298, 340, 355; 17c:247–373; 17m:27, 57); 17c:187 "fine displacement $x$" (a position offset) correctly kept. "Vector field" also occurs at 17:387 for a vector field on R^4; "on the links" keeps them apart.
- **stationary substitution.** 17t:28 and 17c:72–73 both "composition with the critical configuration" (7:1083 glosses "pulled back" the same way); 17c:48, 165 "critical-configuration map" for the map itself. Consistent.
- **current defect** (17:194): kept, glossed once as "the defect of the lattice Ward identity", which is the entry's sense (D, 17:194–195). Not repeated elsewhere.
- **window**: interval of scales (17w:2, 7, 37, 43, 49, 102, 107, 124; 17m:429), interval of radii (17:129, 131, 146; 17w:6), compact set (17:140), averaging length (17m:476): each as its sense in *window*.
- **comparison level → comparison scale** (17m:136): words only; see "Left for the author".
- **coupling threshold** → "lower bound(s) on the reference coupling" in all five files; the small-field threshold `t` remains "threshold" (17c:316; 17m:153, 272, 304, 378), as *threshold* sense 2 asks.
- **alias**: zero / nonzero alias, Fourier coefficient at the alias, as chapter 7; 17c:56–87, 322–335; 17m:215, 227, 232.
- **anchor → base point**; *base-point average* (17c:71) defined once with the entry's gloss and used at 82, 85, 120, 324.
- **ordinary / regular**: "ordinary" → "small-field" for `Z_ord` and its expansion (17m:86–131, 185); `E_reg` and "regular" untouched (17m:113–115; 17w:78 "regular and large-field norms"); "complementary" → "large-field", "failure" → "violation (of a regularity condition)" as their entries say. 17m:461 "ordinary backward comparison" is the everyday sense 4.
- **marked → with insertions** (17m title, 72, 81, 84, 120–123, 150, 176, 381, 393, 411; 17c:316, 396; 17:119, 132; 17w:11, 124). The inserted factor `𝒟_Yk` is called "insertion" throughout 17m (*source* 2, *density-valued insertion*), so *mark* sense 3 is rendered by the same words. "Marked replacement" is in chapter 18, not reviewed here.
- **Repairs (words only):** 17t:157–160 (App. D group 4 no. 3, with table words; "its order-two term must satisfy its … conditions" mends the damaged "annihilate … conditions"); 17c:161 (group 4 no. 1); 17c:359–360 (group 4 no. 2; see below); 17w:78–79 (second round, label `ch11:lower-weighted-step` exists at 11:1566); 17w:122 ("comparison isomorphisms", the name of `U_{i,d}` at 17:81–84; no symbol inserted); 17t:405 ("a fixed scale", no `k` inserted); 17:307–309 (only the confirmed half); 17c:66; 17m:251, 361, 440–442, 474. None inserts a formula, symbol, radius or constant; the added `\ref`/`\eqref` replace nicknames of existing results.
- **moving labels** (17:97, 370) → "convergent sequences of free fields": the committed phrase already had "convergent"; "moving" (varying with the index) and "free labels" (elements of `𝓜_d^Max`, *label* sense 3, R) make exactly a convergent sequence of free fields. The wording is that of the committed 14:238, 250 ("also for convergent sequences of free fields"); "also" adds nothing, since fixed fields are constant sequences. No change.
- **actual**: every deletion checked sense by sense; 17:84 (sense 4) is safe because the sentence names the reference value `b_i`; 17m:312 "inverse coupling band" is the 11R/11 term.

## Corrections applied

All within lines; line counts unchanged.

1. 17c:75 "linear averaging operator $M_a$" → "block average $M_a$" (committed wording).
2. 17c:241 "At a fixed output scale" → "At a fixed scale".
3. 17c:324 "with total sum one" → "with coefficient sum one".
4. 17c:370 "or of its local gauge transformation" → "or of the correction from its local gauge transformation".
5. 17c:391 "at each fixed output scale." → "at each fixed scale.".
6. 17m:70 "against every function independent" → "against every spectator independent".
7. 17m:87 "Fix the dependence set" → "Fix the full dependence set".
8. 17m:249 "obey the same row bounds, independent of $L$." → "obey the same ratio-independent row bounds.".
9. 17m:400 "The same score insertion is used" → "The same differentiated kernel is used".
10. 17m:428 "pre-ratio coefficient-map factors" → "ratio-independent coefficient-map factors".
11. 17m:429 "Fixed-ratio nonlinear" → "Ratio-dependent nonlinear".
12. 17t:297 "any anchored gauge-covariant vector field," → "any gauge-covariant vector field with a base point,".
13. 17w:97 "lowest scale of the interval," → "lowest scale of the interval of scales,".
14. 17:128 "strips and Proposition~" → "strips and the argument of Proposition~".
15. figures/radius-windows.tex:19, 22, 23 (caption only): "Overlapping comparison windows" → "Overlapping intervals of radii"; "At level $n$" → "At scale $n$"; "two neighbouring levels" → "two neighboring scales"; "Successive windows" → "Successive intervals".

The edits were made by /private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/c89/fix.py, which requires each old string to occur exactly once on its line.

## Left for the author

- **17c:138 title** "The nonlinear terms need fixed-ratio bounds": the only remaining "fixed-ratio". "Ratio-dependent bounds" would read as if dependence on `L` were required; the meaning is "bounds at a fixed ratio, whose constants may depend on `L`". A title wording choice; left.
- **17c:359–360** "within the patches of the averaging operation and the averaging patches": App. D group 4 no. 2 in words, with the chapter 4 term "patch of the averaging operation". The second round of App. D and *block-average patch* say the reading (supports of `M_{ef}` and `K_0`) is inferred (basis I) and propose no repair. The juxtaposition with "the averaging patches" reads oddly.
- **17m:136** "At the comparison scale $k$": a level→scale substitution. *comparison level* sense 2 (S; I from the text) proposes "insertion scale `k_i`" for this line, and notes that the chapter 11 "comparison scale" is the top level of a window. Kept as edited (words only, no claim changed).
- **17w:78–79**: the repair cites only (11.lower-weighted-step), while *regular* says the plural "recurrences" also covers the upper-part estimate 11:1541–1544 (inferred). As App. D gives it.
- **figures/radius-windows.tex:7–8**: the TikZ node labels still print "level $n$", "level $n+1$" in the figure, against "At scale $n$" in the caption. I was allowed to edit only the caption.
- **17m:409** "an exponentially local spectator that need not have finite range": *actual* sense 6 (basis I) names the contrast (finite-range against exponentially local); the editor wrote it out. Plausible from 17m:408–410; please confirm.
- **17m:278** "The nonlinear critical configuration": *response* sense 5 is basis I; the replacement is the table word for "stationary" fine field.
- **17c:62, 332** "the linearized averaging operation": the committed text said "the gauge-covariant block average"; an adjoint and a column sum require the linear map, which 6:376 and 7:694 call by this name. A small addition of precision; not changed.
- **17:224** "anchored vector response" (*response* 11, I) and **17t:482** "anchored correction" kept "anchored": they now stand beside "with a base point" for the same idea elsewhere in chapter 17.
- **17c:373–374** "transform the local gauge transformation at its output": correct but clumsy.
- **17w:12, 52** "propagation constants" keep the word "propagation" (basis S; c8's reason stands), while "propagation" elsewhere became "transfer".

## Words this file introduces that other chapters may also define

- *current defect*, "the defect of the lattice Ward identity" (17:194).
- *vector field (on the links)* for "displacement" (17:193); clashes with no defined term, but "vector field" also names `v` on R^4 at 17:387.
- *base-point average* `K_0` (17c:71).
- *exterior moments* (17m:70, now glossed with "spectator").
- *ratio-independent / ratio-dependent* (17w; 17m:249, 428, 429). Chapters 5–7 and 11E have the same idea as "pre-`L`", "chosen before `L`", "post-length" (*pre-ratio constants*).
- *lower bound(s) on the reference coupling* (already in chapters 10–16).
- *mass regularization*, *mass-regularized current* (17:152, 227; 17m:354, 362).
- *inhomogeneous term* for "source"/"forcing" (17c), *gauge-covariant extension* (17m:28–34), *kernel vector* (17m:375 title), *number of transfers* (17m:361), *zero-mean trace* (17:23 and passim).
- *critical-configuration map*, *composition with the critical configuration* (chapters 5, 7 terms, reused).
- Chapter 18 (other reviewer) uses *insertion*, *with insertions*, *differentiated kernel* in the same senses as 17m.

## Checks

- Line counts (`wc -l` against `git show HEAD:<path> | wc -l`): 17-trace-law 458 = 458; 17-variable-windows 125 = 125; 17-trace-transfer 500 = 500; 17-current-contraction 396 = 396; 17-marked-trace-rates 480 = 480; figures/radius-windows 26 = 26. `git diff --numstat`: 47/47, 46/46, 48/48, 109/109, 132/132, 3/3.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-c89a monograph.tex`: exit 0, run to completion (rerun with `-g` also exit 0). In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0. The build includes the other reviewer's files (18-operator-products, 18-raw-replacement, 19-assembly) in their state at that moment; I did not touch them.
- Rendered text checked with `mutool draw -F txt`: figure 17.1 caption and list-of-figures entry ("Overlapping intervals of radii for the trace law"), 17c:241, 324 and 17m:249 render as edited.
- Nothing staged, committed or pushed. No other file edited; references.bib untouched.

## Not checked

- Rendered pages were not inspected visually (text extraction only).
- The source manuscripts (Scott, Martin) and the Lean files were not consulted; the readings rest on the dictionary entries and the committed chapters.
- Chapter 18 and 19 changes in c9's report (outside this assignment) were not reviewed, including its treatment of *marked replacement*.
