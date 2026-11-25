# Second review r6: chapters/11-marked-insertions.tex, lines 1–1180

Worktree `/Users/mgubi/ym-terminology`, file `manuscript/HumanizeYM_v3/chapters/11-marked-insertions.tex`. I read the word diff `4f462ac5..HEAD` for lines 1–1180 (about 265 changed lines) and the present text of 1–1180 in full. Only after that did I read `ch11-c3a-apply.md`/`ch11-c3a-review.md`. Dictionary entries checked: the table, *physical*, *actual*, *selected slot*, *slot*, *rebasing contraction*, *warning*, *preselection bound*, *row*, *coarse forecast*, *frame*, *supplies*, *full dependence region*, *stencil*, *complementary*, *cutoff failure*, *remote*, *counting norm*, *forest*, *terminal map*, *history*, *localization*, *extraction*, *graph*, *comparison level*, *coarse kernel level*, *dictionary*, *weight*, *transport*, *noise*, *threshold*, *inverse terminal coordinates*, *gap*, *word*, *level*, *schedule*, *normalized local insertion*, *bottom*, *endpoint*, *trial encoding*, *threshold for the starting scale*, *tour length*, *inputs*, *common Gaussian*, *mark*, *tag*, *reserve*, *occupancy*, *menu*.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 11:896, 909 | ERROR (TERM) | "so the bottom residual coefficient"; "starts at the bottom with zero coefficient" | "residual coefficient at the lowest scale"; "starts at the lowest scale with" | "Bottom" is the coarsest end (smallest scale index). The book's table makes *scale* mean the lattice spacing `a_m`, so "the lowest scale" reads as the finest spacing, which is the cutoff end and the opposite of what is meant. The induction runs from small `i` (coarse) to `i+1`. | "at the coarsest scale" (both lines) |
| 11:1059 | MISMATCH | "corresponding selected schedule inequalities." | "corresponding inequalities on the sequence of scales." | Chapter 10 defines the short term *schedule* (10:121, `\emph{schedule}`) and uses it at 10:808. Here the same object was given another name. | "corresponding inequalities on the schedule." |
| 11:734, 737 | LEFTOVER | "Restarting below a comparison level"; "comparison level while" | unchanged | *level* → *scale*, from the table and the entry *comparison level* (proposed: *comparison scale `k`*). 17m:136 already says "comparison scale". | "comparison scale" (title and 737) |
| 11:1149 | LEFTOVER / TERM | "At comparison depth $k$ put" | unchanged | The same index as 734–737 under a third name (*comparison level*, variants: "comparison depth"). | "At the comparison scale $k$ put" |
| 11:258, 265 | TERM | "at a fixed mark"; "at a specified mark" | "at a fixed insertion"; "at a specified insertion" | Under *mark*, sense 2, a mark is an insertion point. In the neighbouring lines (260, 268, 272) the conversion wrote "insertion points". "At a fixed insertion" is vaguer. | "insertion point" |
| 11:345 | MINOR | "the stated occupancy $g$" | "the stated bound $g$ on the number of insertions per coarse site" | `g` is defined at 260 as the number of *insertion points* projecting to a coarse site | "…number of insertion points per coarse site" |
| 11:382 | LANGUAGE | "above the preselection bound $C_d/L+o_x(1)$, which may be chosen as $L^{-2/5}$ after the stage choices" | "above $C_d/L+o_x(1)$, the bound valid before $L$ and the lower bound on the reference coupling are chosen ($\epsilon$ may be …)" | The meaning is that of *preselection bound* (S). The appositive "the bound valid before … are chosen" is hard to parse: it can be read as "the bound [is] valid before L and the lower bound … are chosen". | "above the bound $C_d/L+o_x(1)$, which is valid before $L$ and the lower bound on the reference coupling are chosen ($\epsilon$ may be taken to be $L^{-2/5}$ after those choices), it satisfies" (math unchanged, one "the bound" moved) |
| 11:279, 297, 319, 339 | DICTIONARY (minor) | "nonleading" | "nonprincipal" | *nonleading* has no dictionary entry, so this replacement has no D/R/S basis. It is harmless: the committed text already had "nonprincipal" at 425 and "principal" at 179 and 289–331. | left; listed |
| 11:937 | MINOR | "$u_N>0$ the terminal attachment reserve" | "$u_N>0$ the strict margin for attachments at the ultraviolet cutoff" | "Strict" comes from the *reserve* proposal and is already implied by `u_N>0`. Not wrong. | left |
| 11:672 | MINOR | "and actual background" | "and the non-flat background" | Sense 2 of *actual* (I, but it lists 11:672) proposes "non-flat". The contrast is with "At zero background" (668), and a general background could be flat. "Non-flat" slightly sharpens this. | left for the author |
| 11:668 | MINOR | "the actual row Gram" | "the Gram matrix of the components" | "Components" of what is not stated (it is the components of the linearized action vector, *row* 1). | left |

Particular points of the assignment, checked and accepted:
- **18–19, history.** The defining sentence is word for word the committed one, now in `\emph`. 2e:253 and 7:1202 refer forward to it, and no earlier chapter defines "history". Chapter 5 no longer uses it in sense 1. Chapter 10 uses it (sense 3) without a forward reference, which is outside my range.
- **372–373, Taylor localization.** This is the table row ("extraction of the local polynomial part … *Taylor localization*") together with *localization* 1 (D: "one-step localization map", its own symbol `T`). It says no more than the chapter (438: "its extracted polynomial and a bounded Taylor remainder"). It is the first use of the Taylor sense in the book. Chapters 4 and 9 use "localization" only in Bałaban's compounds. The Bałaban half of the table's sentence is not there; see "For the author".
- **380, graph transform.** The sentence is Scott E-section.tex:242 as quoted in the entry *graph* 1 (S), with "marked step"/"level m+1, m" changed to "step with insertions"/"fine, coarse scale". The direction is right (`q_m=\mathcal B_mq_{m+1}`, `G'=R_GM_G^{-1}` at 447). The halving is the contraction prepared at 453–468 under `4\delta s_f\le1` (*rebasing contraction*). It adds no formula. The name is used again at 468.
- **636–666, `W_F` and the identities.** Chapter 5 (5:1113–1115, 1141–1148) gives `K_fW_a=\mathcal Q^*K_c`, `\mathcal QW_a=I-b^{-1}K_c`. Hence `AW_a=K W_a+bQ^*QW_a=bQ^*`. `W_F` differs from `W_a` by a gradient that `D` and `K` annihilate and that leaves `\mathcal QW_a` unchanged (5:1141–1142). So `KW=Q^*K'`, `AW=bQ^*` and `DW=JD'` hold for `W_F`, and 655 (`DXbQ^*=DXAW=DW`) is correct. The wording "taken in its representative $W_F$ in the block axial gauge" matches 5:1151, 1234, 1311. Q as "rooted linearization of the averaging operation" matches 7:694. "Induced map on curvatures" (648, 651) matches 5:453, 528. "Unnormalized `\ell^2` scalar products" (621) matches 5:528 (*counting norm*). "Modified" metrics (627, 649, 662) are *actual* 10.
- **1051, 1109.** "normalized local insertion" for "physical insertion" follows the entry *normalized local insertion* ("keep, define once at 11:1051"). It is consistent with 11:2323 and 13sb:53.

## Corrections applied

Ten lines (line count unchanged, 2355): ERROR/TERM 2 lines (896, 909), MISMATCH 1 (1059), LEFTOVER 3 (734, 737, 1149), TERM 2 (258, 265), LANGUAGE 1 (382), MINOR 1 (345).

## Cross-chapter mismatches not fixed

- "comparison level" remains at 11R:7, 11R:70 (`11-restarted-history.tex`) and 15:253. Now that 11:734, 737 and 1149 say "comparison scale", those should be changed to match (as 17m:136 already is).
- "history" (sense 3) in chapter 10 (10:209–256) is used before the definition at 11:18 without a forward reference. 2e:253 and 7:1202 have one.
- Chapter 13 (13:159) still has "inverse terminal coordinates" (noted by the first reviewer). Chapter 11 says *cutoff-scale coordinates* (885).
- "Lowest scale" may occur elsewhere as the rendering of "bottom" (entry *bottom*: 10:850, 17w:97). It has the same ambiguity there, and I did not check those lines.

## Leftover house words

Kept on purpose:
- *physical* at 423, 696 (sense 6, I), 472 (sense 4, I), 588 (sense 8, I) and 689 (not in the entry). All have basis I.
- *actual* at 415, 558 (sense 2, I) and 1158 (sense 1, I).
- *terminal* at 110, 147, 157, 171, 525, 923, 955, 1076: not on the table's list.
- *weight*:
  - support weights (198, 204, 217, 503) and source weights (43–49, 192, 496, 817, 823, 953): senses 2 and 4, kept;
  - "fine spatial weight" (351) and "derivative-weight origin" (1068): sense 6. The proposal "coefficients; factors" does not fit an integer exponent;
  - "probability weights" (563, 602): correct.
- *label*: "polynomial label space" (15, 29) and "label space" (965) are the defined objects of chapter 2. "Reference label(s)" (946, 958, 1074) is the defined term.
- *unit*: "two unit bounds" (792) means bounds equal to one, ordinary use. "One retained unit" (396) and "cover units" (495, 502, 528, 533) are units of support exponent.
- *cost* (241–242, 397, 421, 492, 534, 596, 789, 806, 910): not on the list.
- "common tagged partitions" (871): the standard Riemann-sum term.

Replaced: comparison level (734, 737), comparison depth (1149).

No remaining occurrence in 1–1180 of: tag (house sense), block average, predictor, stationary, noise, cutoff failure, frame, tree gauge, block transformation, reset, marked/unmarked, heat, mixed, ground, kill.

## Assessment of the first review's corrections

All seven corrections in `ch11-c3a-review.md` are right:
- 70: comma;
- 166: "with the Wilson action";
- 244, 679: `$\alpha$` removed;
- 479: title order;
- 642: `W_F` wording;
- 689: "with a different local gauge transformation";
- 960: title restored.

The first reviewer accepted "lowest scale" at 896 and 909 and "sequence of scales" at 1059. I correct both above.

## For the author

- 372: the second half of the table's first-use sentence ("which Bałaban calls imposing renormalization conditions") is still missing. Its *Literature* sources (B95 p. 118; D1) have no key in `references.bib`; the keys present are Balaban1984Propagators, 1985Variational, 1985Averaging, 1985Spaces, 1987RG, 1988Expansions, 1988Cluster, BFKT2016. A bibliography entry is needed first.
- 221: title "One step with insertions" (formerly "…with the actual local factors").
- 672: "non-flat background" or "a general background".
- 1136: "the coefficient map $\mathsf Z$" shares its words with `M_G` (381).
- 842: "cyclic product of transfer operators" also contains the slab kernels `B_i`.
- 279 ff.: "nonleading" → "nonprincipal" was made without a dictionary entry. I find it correct.

## Checks

- `wc -l` of the file: 2355; `git show HEAD:… | wc -l`: 2355. Lines 1181–2355 not touched (all edits at 258–1149).
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r6 monograph.tex`: exit 0. `monograph.log`: 0 "undefined", 0 "Citation", 0 "Overfull".

## Not checked

- I did not inspect the rendered pages visually.
- I did not consult the source manuscripts (Scott/Martin) or the papers. I relied on the dictionary's *Source* and *Literature* lines.
- I did not grep every other chapter for every name in the brief's point 4. I checked: history, schedule, comparison level/scale, reference coupling, auxiliary index, link support, exact cover, connected covering number, prescribed large-field set, dependence set, block axial gauge, linearization of the averaging operation, induced map, fluctuation field/variables, identity field, dimensionful, normalized local insertion, source degree, restarted history, cutoff-scale coordinates, modulus of continuity in the insertion points.
