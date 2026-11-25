# Third review t6: chapters/11-marked-insertions.tex, lines 1–1180

Worktree `/Users/mgubi/ym-terminology`, file `manuscript/HumanizeYM_v3/chapters/11-marked-insertions.tex`. I read the word diff `4f462ac5..HEAD` for lines 1–1180 in full (about 265 changed lines), with the surrounding present text, and formed a judgement before reading `ch11-c3a-review.md`, `round2/ch11a-review2.md`, the relevant parts of `round2/harmonise.md` and the leads. Dictionary entries read: *empty coefficient*, *large-field factor*, *cutoff failure*, *selected slot*, *slot*, *detection*, *separating family*, *history*, *free history*, *push*, *transfer*, *supplies*, *coefficient map*, *terminal map*, *trial encoding*, *endpoint*, *physical*, *complementary*, *coarse forecast*, *row*, *warning*, *coarse kernel order*, *dictionary*, *weight*, *reserve*, *actual*, *cutoff*, *coupling band*, *lower bound on the starting scale*. I also checked the claims against 4:547, 5:302–306, 6:1324, 6:1440–1466, 10:648–656, 12:85–113. Line numbers are those of the present file.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 11:424–425 | ERROR (TERM) | "Its selected slot has no purely principal component." | "The large-field factor carrying it gives no purely principal term." | "Component" became "term". In this chapter a *component* is a connected union of terms (330: "Purely principal connected components"; 608: "the purely principal components"). The source (Martin heading-history-handoff.tex:313–321, quoted in *selected slot*) says "no ordinary principal cluster", that is, no component. "No purely principal term" is a different claim and does not read clearly. "It" could also refer to "the incoming normalized mass" of the previous clause. | "The large-field factor carrying this input lies in no purely principal component." |
| 11:725 | TERM | "A common Gaussian sample and coarse forecast are used for all subsets." | "One joint Gaussian vector and one linear prediction … are used for all subsets." | The same object is "one … Gaussian sample" at 679–680 in the same subsection ("one coarse gauge and one Gaussian sample for all coordinates read by the polynomial family"). "Sample" was replaced without a dictionary basis (the glossary row "common Gaussian sample" only glosses it). | "One joint Gaussian sample and one linear prediction …" |
| 11:604 | DICTIONARY (lead a) | "The empty coefficient is exactly one" | unchanged | The text is right. Here the empty coefficient is `M_∅ = M_∅^* = 1` of Proposition ch11:joint-gaussian (571): the coefficient of the empty index set in the generating function of product moments, not the density without insertions. The entry *empty coefficient* says under "Meaning" that 11:604 is the density without insertions. That is wrong for this line. Both 604 and 773 ("coefficient of `z_∅`") name the coefficient of the empty index set, which is right at both places. | left; the dictionary entry needs correcting |
| 11:773 | MINOR | "Its empty coefficient remains the original unmarked density." | "Its coefficient of `$z_\varnothing$` remains the original density without insertions." | A symbol was inserted. It is correct (`z_S` at 37 with `S=∅`), and the first reviewer accepted it. | left |
| 11:960 | TERM (lead a) | `\section{Finite-dimensional detection before taking limits}` | unchanged (restored by the first review) | "Detection" is the old name for the separating property. Everywhere else the chapter says "separating family" (29, 1078, 1141) and 976 says "used to separate the quotient". "Separation" in a title would collide with "separations" `h_i` (850, 861–862) and "separated" positions (840, 1017). | left for the author (for example "A finite separating family before taking limits") |
| 11:92 | DICTIONARY / MISMATCH (lead b) | `[Changing the block history]` | unchanged | The proposition replaces the block *kernels* below scale `k` by arbitrary other normalized positive kernels (94–95). That is part of a history in the sense of 18–19 (kernels, couplings, path pairs, representations). It is not a *blocking sequence* (5:302–305: ratios `L_h` and smoothing orders `j_h`, a list of parameters). So "blocking sequence" would be wrong here. The entry *history* puts 11:92 in sense 1 (= blocking sequence), and that classification is doubtful. "Kernel history" (11:1699, outside my range) is the sequence of quadratic kernels, a third object. | left for the author (for example "Changing the block kernels") |
| 11:424, 245, 250, 332, 923 against 11:1476–1932, 10:654 | MISMATCH (lead c) | — | "large-field factor" | In 1–1180, "large-field factor" is always an incoming factor carrying a prescribed large-field set (245 "incoming large-field factors", 250, 332, 923 "original selected large-field factors", 424). 10:654 ("one required large-field factor", for arrays with a prescribed large-field set) is the same kind of object. At 11:1476, 1487, 1500, 1523 and 1932 (outside my range) the same words name the former "failed-cutoff factor" `1−(1−χ)Rz_I`, a factor made from the large-field part of an insertion. That is a different object. | not fixed (lines outside my range) |
| 11:321–325, 444; 647–651; 845–878; 1141 | — (lead a, two `T`) | — | — | Lines 1–1180 contain four objects written `T`: the one-step localization map (373, named there; 377, 444), the induced map on curvatures (647–651, named there), the positive transfer operator (845–878, "transfer operators"), and the common localization map (subsection 1141; the symbol appears after 1180). The words distinguish each one at its introduction. At 444 ("half the inverse bound of `T`") the nearest named `T` is the one-step map, which is correct. | no change |
| 11:642 | MINOR | "For the actual stationary forest response $W$" | "For the linearization $W$ of the critical configuration, taken in its representative $W_F$ in the block axial gauge" | The symbol `W_F` was inserted, and the identities that follow use `W`. It is correct (second review: 5:1113–1151) and it matches 5:1151 and 7:574. | left |
| 11:1074; 1116, 1129–1130 | MINOR | "the trial encoding"; "mesh threshold" | "the reference label `$v_{N,p}$` of the trial"; "lower bound on `$N$`" | Symbols were inserted. Both are correct: `v_{N,p}` is at 946, and `N_0` is at 1086. | left |
| 11:351–352 | MISMATCH | "fine kernel order …, coarse kernel level" | "fine kernel order …, coarse kernel order" | Chapter 5 calls this parameter the *smoothing order* (5:303–305). "Kernel order" occurs only here. Whether it is the same parameter is basis S. | not fixed; listed |
| 11:479 | TERM | `\subsection{Propagating the already formed terms involving …}` | "…of source degree at least two" | "Propagating" is one of the synonyms of *transfer*. | title, left for the author |
| 11:558 against 588 | LEFTOVER / MISMATCH | "actual normalized local curvature coordinates"; "physical coordinates" | unchanged | One object has two names, both inherited (*actual* 2, *physical* 8, basis I). | left |
| 11:1136 against 381 | TERM | "the terminal map `𝖹`" | "the coefficient map `𝖹`" | `M_G` is "a linear coefficient map" (381), and `𝖹` is the composition of these maps (1047). The dictionary adopted the shared word. | left for the author (for example "the composed coefficient map") |
| 11:380 | — | (new sentence) | "As in the graph transform … halves the distance between two of them." | Verified. Lemma ch12:contraction (12:94–106) gives `d_m(ΦG,ΦH) ≤ a/2` under `4δ s ≤ 1`, which is imposed at 11:464. The analogy is stated without a citation. | left |
| 11:221 | MINOR | "One marked step with the actual local factors" | "One step with insertions" | "The local factors" was dropped from the title. | title, left for the author (already listed by round 2) |

Everything else in 1–1180 was checked line by line and accepted: source degree (134 and its later uses), dependence set / link support, large-field part (*complementary* 1), the failure of the regularity condition at 151 (the plaquette indicator, exact cover 4:547), "covered by" at 248 (exact covers of large-field sites, 4:547), lower bound on the reference coupling, coupling band, margin in the support exponent, the margin in the decay exponent at 521 (the retained positive energy of 6:1440–1466), Taylor localization and the one-step localization map, scaling dimension at 407 and 411, identity field, dimensionful / in continuum units, normalized local insertion, cutoff-scale coordinates, restarted history, "coarsest scale" at 896 and 909 (the induction runs from small `i` to `N`), the joint tail bound for cutoff remainders, modified metrics, "image under the block maps" and "transfer" (*push*), and "integrated inequalities for the normalized products" (877).

## Corrections applied

Two edits, on three lines (424, 425, 725). The line count is unchanged at 2355, and lines 1181–2355 are untouched.
- ERROR (TERM): 1 (424–425)
- TERM: 1 (725)

## Cross-chapter mismatches not fixed

- "Large-field factor": 11:245, 250, 332, 424, 923 and 10:654 (incoming factor with a prescribed large-field set) against 11:1476, 1487, 1500, 1523, 1932 (the former failed-cutoff factor `1−(1−χ)Rz_I`).
- "Kernel order" (11:351–352) against "smoothing order" (5:303–305).
- "Block history" (11:92) against "blocking sequence" (ch. 5, 10) against "kernel history" (11:1699). These are three different objects, so no single replacement is right.
- "Coefficient map" for both `M_G` (11:381) and `𝖹` (11:1136). `M_G` against `I_G` (12:90) is an inherited two-symbol issue.
- "Curvature response" `J` (11:647) against response sense 1 at 3:409 (lead, part 5). Not examined beyond the line.

## Leftover house words

Kept on purpose:
- *actual*: 415, 558 (sense 2, I) and 1158 (not classified; I). The contrast at 1158 is not clear enough to delete it safely.
- *physical*: 423, 696 (sense 6, I); 472 (sense 4, I); 588 (sense 8, I); 689 (unclassified, I).
- *weight*: source weights (43–49, 192–204, 496, 817, 823, 938, 953), support weights (204, 503), probability weights (563, 602), "derivative-weight origin" (1068, sense 6; no fitting replacement).
- *label*: "polynomial label space", "label space" (15, 29, 965, defined objects); "reference label(s)" (946, 958, 1074, defined term).
- *unit*: "unit of exponential support decay", "cover units" (396, 495, 502, 528, 533), "two unit bounds" (792, bounds equal to one). All are ordinary use.
- "tagged partitions" (871): the standard Riemann-sum term.

Replaced: "Gaussian vector" back to "Gaussian sample" (725).

None of the following occurs in 1–1180: tag (house sense), block average, predictor, stationary, noise, cutoff failure, frame, tree gauge, level, block transformation, reset, marked/unmarked, heat, mixed, ground, kill.

## Leads

- (a) "empty coefficient" (11:604): verified correct as it stands. It is `M_∅`, not the density, and the dictionary's reading is wrong (see Findings). "Detection" (11:960): left for the author with a suggestion. The two `T`: the words distinguish them; no change.
- (b) "block history" (11:92): it is not the blocking sequence. Left for the author, with the dictionary classification flagged.
- (c) "Large-field factor" (11:424): it is the incoming large-field factor of 245/332, the same kind of object as 10:654, but not the factor of 11:1487 ff. I also corrected "term" to "component" in that sentence.
- "common localization map `T` / extraction `T`" (11:1326) and "kernel history" (11:1699): outside my range.
- `W_F` at 11:642: consistent with 5:1151 and 7:574. Kept.
- "Coefficient map `M_G`/`I_G`" (leads part 1): inherited; listed.

## Assessment of earlier corrections

- The Appendix D repair at 424–425 ("…gives no purely principal term"), accepted by the first review under "Other Appendix D repairs", changed "component" to "term". Corrected above.
- The other corrections of rounds 1 and 2 in 1–1180 are right: the comma at 70, 166, the `$\alpha$` removals at 244 and 679, the order of the title at 479, the `W_F` wording at 642, 689, the title at 960, "coarsest scale" at 896 and 909, "schedule" at 1059, "comparison scale" at 734, 737 and 1149, "insertion point" at 258 and 265, and the occupancy at 345.

## For the author

- The title at 960 ("detection").
- The title at 92 ("block history"; perhaps "Changing the block kernels").
- The title at 479 ("Propagating").
- The title at 221 (the lost "local factors").
- "Coefficient map `𝖹`" (1136) against `M_G` (381).
- "Kernel order" (351–352) against "smoothing order".
- "Large-field factor" has two senses in chapter 11 (see the mismatches).
- The entry *empty coefficient* should not equate 11:604 with the density without insertions.

## Checks

- `wc -l chapters/11-marked-insertions.tex`: 2355, equal to `git show HEAD:… | wc -l` (2355). The diff against HEAD touches only lines 424–425 and 725.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-t6 monograph.tex`: exit 0. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0.

## Not checked

- I did not inspect the rendered pages visually.
- I did not consult the source manuscripts or Bałaban's papers directly. For those I relied on the dictionary's *Source* lines.
- I did not grep every name of brief point 4 in all chapters. I checked: large-field factor, history / blocking sequence, separating family, coefficient map, kernel / smoothing order, transfer, coupling band, lower bound on the reference coupling, `W_F`, dependence set, exact cover.
