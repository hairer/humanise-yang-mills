# Third review: chapters 12, 13 (13, 13sb, 13ba), 14 (14, 14lc)

Worktree /Users/mgubi/ym-terminology, files under manuscript/HumanizeYM_v3/chapters/. Every line changed between 4f462ac5 and HEAD (12: 113; 13: 42; 13sb: 37; 13ba: 82; 14: 117; 14lc: 20; 411 lines in total) was read old against new, with the surrounding lines of the present file. Line numbers are the present (unchanged) ones.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 13:206, 211 | ERROR (minor) | `A common cluster point $(b,z)$` / `at the same cluster point` | `A common limit point` / `at the same limit point` | The argument is about a filter (13:211 "hold along the filter", 13:213). For a filter, "limit point" reads as a limit, i.e. convergence, which is not proved; only compactness of a finite-dimensional set is used, which gives a cluster point. "Cluster point" is the standard term, not house vocabulary (the dictionary's "subsequential limit" fits chapter 5's sequences, not this filter). | `A common cluster point`, `at the same cluster point` (4f462ac5 restored) |
| 13:394 | TERM | `admissible trial encoding,` | `the reference labels of admissible trials,` | "Admissible" is defined for comparison coefficients / coefficient families (11:883–885, 11:1101–1102), and the reference label `v_{N,p}` has subpower cutoff-scale coordinates (11:1074–1075), i.e. is admissible. The conversion moved the adjective onto "trials", for which it is undefined. | `the admissible reference labels of the trials,` |
| 13ba:307 | ERROR | `approximation thresholds may depend on each fixed pair.` | `the lower bounds on $N$ for the approximation may depend on each fixed pair.` | The approximation holds "on the ordered cutoff and volume tails" (13ba:207; proof 13ba:333–335 intersects ordered tails, which have thresholds in both `p=P(k)` and `N=n(j)`, 13:213–214). Restricting the thresholds to `N` narrows the statement. | `approximation thresholds may depend on each fixed pair.` (4f462ac5 restored) |
| 13ba:247 | ERROR (minor) | `every shared frame seed for an output` | `every auxiliary random variable for an output` | "Shared" dropped: the claim was about the shared frame seeds (the random variables choosing the local gauge transformation, which several output links share), and is now stated for all auxiliary random variables, including the coarse-link samples of 13ba:231. Scope widened. | `every shared auxiliary random variable for an output` |
| 13ba:37 | LANGUAGE | `so its ordinary derivative` | `so its small-field derivative` | After "the small-field indicator" (13ba:36) "its" reads as the indicator, which would give an indicator a derivative constant (lead). The constant is that of the normalized small-field polynomial (cf. 10:95–99, "their small-field chart bound"). | `so the polynomial's small-field derivative` |
| 12:271 | LANGUAGE | `higher regular entries ... and only those entries` | `Multiply every term of source degree at least two, and only those / entries,` | Old noun "entries" left behind after "terms" (lead). | `... and only those / terms,` |
| 14:776–777, 796 | LANGUAGE | `express the total raw / angular response as`; `whereas the total shell response is independent` | `express the left side of / \eqref{ch14:line-ward} as`; `whereas the left side of \eqref{ch14:line-ward} is independent` | Correct in substance (the left side of (ch14:line-ward) is the sum over insertions of the local fluxes of `V=Ky`), but it points ahead to the equation displayed at 14:798, whose `=0` is the conclusion being proved (lead). The quantity has a book name: "Ward sum" (3:915), and 14:842 calls its normalized version "the normalized angular Ward sum". | `express the angular Ward sum, the left side of / \eqref{ch14:line-ward} below, as`; `whereas the angular Ward sum is independent` |
| 13ba:36, 165 | (checked, right) | `the local smooth cutoff`; `multiplied by the smooth cutoff has zero complementary profile` | `the small-field indicator`; `multiplied by the small-field indicator has no large-field part,` | Lead (a). Not an error. The factor is an indicator in the chapter's own formula: the coarse trial is `V_h = a_h^{-d}(v_0 + 1_{small-field stencil} P_d^loc[...])` (13ba:215–217), and 10:98 says "the indicator of the relaxed regularity condition is one" for the same trials. "Smooth cutoff" was a mechanical replacement of the earlier word "guard" (commit 4ebb64ea, recorded in the dictionary, *relaxed* / Appendix H). Kept; only "its" at 13ba:37 fixed (above). | — |
| 13ba:258, 261 | DICTIONARY / for the author | `coupling-threshold requirement`; `coupling-threshold conditions` | unchanged (261 untouched) | Lead (d). Chapter 10 settles it: the condition `b_q log3 ≥ 2 log(ȷ_q+7)` is imposed on `b_q`, "the minimum starting scale" (10:122–126: "Let `b_j, c_j` be nonnegative integers specifying respectively the minimum starting scale and a requested length for a stage plateau. … include `b_j log 3 ≥ 2 log(ȷ_j+7)`"). It is not a lower bound `d_j` on `β̂` (10:157–159). So "lower bound on the reference coupling" would misstate it. "Coupling-threshold" was already inaccurate at 4f462ac5 (the condition is on the starting scale, though both are enforced by starting stages late). Replacing the word changes the stated claim, so left. Correct wording would be "a permitted finite lower bound on the starting scale" (258) and "among the lower bounds on the starting scales of Section ch10:schedule" (261), as at 10:63, 606, 692 and 12:123. | left for the author |
| 12:203 | for the author (scope rule) | `$H_X$, and large-field factors` | unchanged (untouched line) | Lead (f). Here the "large-field factor" of `Q` is `K_Q + Σ_i z_i k_{i,Q} + K_Q^{≥2}`, the total large-field activity of the density with insertions at support and prescribed large-field set `Q` (12:26–27, 162), expanded by source degree 0, 1, ≥2; it is a "factor" of the exact-cover gas. That is the same use as in chapter 11 (11:1476, 1487, 1500, 1523: a large-field factor carrying a source monomial). 10:654 ("one required large-field factor") is a different object. Not renamed (untouched line, not a table word). | left; suggest "total large-field activities" if the author wants one name in chapter 12 |
| 12:279 | (checked, right) | `If a source monomial contains $q$ origins,` | `contains $q$ insertions,` | Elsewhere in chapter 12 "origins" became "insertion points". Here the monomial `z_S`, `|S|=q`, has `q` insertions; "insertions" reads better than "contains q insertion points". Kept. | — |

All other changed lines were checked and are right. Points examined in detail and accepted: 12:31/41/175 "action data" (defined 12:31–34); 12:178–179 reference (ch04:weighted-sums) and 12:247 reference (ch11:replicated-bound) (both labels give the objects meant, 4:593–601, 11:806–812); 12:236–237 "incidence bounds" (= the bound `H_f` of 11:506); 12:133, 298 "common trajectory of Chapter 10" for "selected trajectory"; 12:143 "selected graphs" (= 12:139); 12:187 "regularity condition at scale m" (a plaquette condition, as it should be); 13:236–237 "lower bounds on the reference coupling" (matches 11:1070–1071, a condition `2^{ϖq} ≤ β̂_N`); 13:239 "backward comparison" (11:890 section title); 13:159, 217 "cutoff-scale coordinates" (11:884); 13sb:26 "coupling constant renormalization" (cf. 10:421); 13sb:27, 36 (Appendix D, basis S); 13ba:194 "provided the cones lie inside the cells, as verified below" (13ba:269–271); 13ba:283 "Place a copy of the discrepancy in each reflected cell" (dictionary *replicate*, product over cells 13ba:285–286); 14:99 "with buffer r" (defined 13:335; covers both separation and slab margins); 14:238, 250 "convergent sequences of free fields"; 14:448 gloss of *frequency profile* (true: the factors `g_k(p_k)` of 14:504); 14:464 *residual profile* defined at first use; 14:465, 688, 697, 740, 761 "Laplace transform" for the map 𝓛 of 14:450; 14:946 "conjugates of their undecomposed matrices by the comparison maps" (as in 14:830); 14lc:23 "a comparison scale k whose comparison window lies in a single stage" (dictionary *admissible comparison depth*, basis S); 14lc:95–96 strips for the coordinate hybrids.

## Corrections applied

ERROR 3 (13:206+211 counted once; 13ba:307; 13ba:247), TERM 1 (13:394), LANGUAGE 3 (12:271; 13ba:37; 14:776–777+796). Total 7 findings corrected, on 10 lines; no line added or removed.

## Cross-chapter mismatches not fixed

- "Coupling-threshold" (13ba:258, 261) against "lower bound on the reference coupling" (13ba:39, 50, 83, 101; 13sb:16, 41, 45) and "lower bound on the starting scale" (10:63, 606, 692; 12:123). See the findings: the 13ba lines mean the starting scale.
- "Large-field factor": 12:203 and chapter 11 (11:1476–1523) mean a factor of the exact-cover gas with its source expansion; 10:654 a required factor of an array with a prescribed large-field set.
- Field spaces `F_d` of chapter 14: "undecomposed field spaces" (14:263) and "interacting inclusion" `j_d` (14:212); 18gq:8 / 18:43 "interacting field spaces". Two adjectives for one space (inherited from the old "mixed" / "physical").
- "Comparison window" (14lc:23; 11, 11R) against "interval of scales" (10, 17).
- First-scale choices: "the first scale with `a_m < cr`" (13sb:147), "first such scale" (13:358, 362), "first-crossing scales" (18lp:21).
- `T`: "common localization map" (14lc:30; 11:1307) also used for the one-step map (11:373).
- "Ward sum": defined for the free hierarchy at 3:915; chapter 14 uses "angular Ward sum" (now 14:776, 796, and 14:842 "normalized angular Ward sum") and "translation Ward sum" (14:812) without restating the definition for the interacting hierarchy. Fine as a reuse, but the author may want a one-line definition in chapter 14.

## Leftover house words

Kept on purpose:
- "label(s)" in 12:22, 147; 13 passim; 13sb:176; 13ba:312: polynomial labels in `V_d` (defined term, 2:58–65; 13:117) and the "prescribed label" (coefficient). Correct.
- "weight(s)": "source weights" (defined), 12:391 "the weights of this average" (ordinary).
- "unit": 12:391 "unit forward differences", 13ba:144, 148 "units" of an exponent, "continuum units", "lattice units" (ordinary).
- "physical": 14:1026 "physical Hilbert space" (ordinary, untouched).
- "mixed", "heat": only in labels (`ch14:mixed-sign`, `ch14:heat`, `ch18:mixed-bound`).
No "actual", "tag", "block average", "predictor", "stationary", "noise", "cutoff failure", "frame", "tree gauge", "level", "block transformation", "reset", "marked", "unmarked", "ground", "kill" remain in the prose of these files.

Not replaced because of the scope rule (lines identical at 4f462ac5 and HEAD, not table words):
- 14:34 "unit vacuum `Ω_μ = [∅]`" (ordinary: the vacuum vector; "unit" is in the table, but here it is not the identity field, so no change needed).
- 14lc:7 "the finite label list": in chapter 14 the converted lines call these "fields"; untouched line, listed.
- 14:519, 611 "collision orders" (chapter 14 otherwise says "coincident points").
- 14:406 "response identities", 14:992 "zero responses" (response in the sense of correlation functional values; elsewhere in chapter 14 the conversion wrote "values of the correlation functionals").
- 13ba:258, 261 "coupling-threshold" (above).
- 12:203 "large-field factors" (above).

## Leads

- 13ba:36, 165 (a): verified; not an error (indicator in the formula 13ba:216 and at 10:98); the ambiguous "its" at 13ba:37 fixed.
- 13:394 (b): verified; adjective misplaced; fixed.
- 14:776–777, 796 (c): verified correct in substance; reworded to "the angular Ward sum, the left side of (ch14:line-ward) below".
- 13ba:258, 261 (d): verified from 10:122–126; the condition is on the minimum starting scale `b_q`; left, reported (replacing would change the stated claim; "coupling-threshold" was already inaccurate).
- 12:271 (e): fixed ("entries" → "terms").
- 12:203 (f): which factor: `K_Q + Σ z_i k_{i,Q} + K_Q^{≥2}`, the total large-field activity of the density with insertions at `Q`, by source degree; untouched line, left.
- "first-scale choice" (13sb, 13:358, 18lp:21): two names, not fixed (13:358 untouched; 18lp not mine).
- "comparison window" / "interval of scales" (14lc:23): listed.
- `T` for two maps (14lc:30 uses the common localization map, correctly).
- "large-field factor" in several senses (12:203): listed.

## Assessment of earlier corrections

- First round / apply: 13:206, 211 "limit point" (from the dictionary's *cluster* sense 1) is wrong for a filter; restored. 13ba:307 "lower bounds on N" narrowed the thresholds; restored. 13ba:247 dropped "shared". 13:394 moved "admissible" to the trials. None of these was caught in round 2 (round2/ch12-14-review2.md:35, 37 accepted them).
- The first reviewer's correction 13:236–237 ("controlled by") is right. The second reviewer's and the harmonisation's changes in these files were checked and contain no further error.

## For the author

1. 13ba:258, 261: say "lower bound on the starting scale" (the condition is on `b_q`, 10:122–126), or keep "coupling-threshold" and explain that starting scales are raised to enforce it.
2. 12:203: name the factor ("total large-field activities with insertions") or leave "large-field factors" (consistent with chapter 11).
3. Chapter 14: one adjective for the field spaces `F_d` ("undecomposed" 14:263 against "interacting" 14:212).
4. 14:519, 611 "collision orders", 14lc:7 "label list": untouched lines with old wording.
5. The condition behind "comparison window lies in a single stage" (14lc:23) is not stated anywhere in v3 (dictionary *admissible comparison depth*, basis S).

## Checks

- Line counts: 12 405/405, 13 403/403, 13sb 177/177, 13ba 337/337, 14 1028/1028, 14lc 110/110 (working tree / HEAD).
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build-t8 monograph.tex`: exit 0. In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0.
- The working tree also contains other reviewers' uncommitted edits (09, 10 and others); the build includes them.

## Not checked

- Rendered pages were not inspected: no pdftotext or PDF library on this machine. The build succeeded with no overfull boxes.
- 13-continuum-fields.tex lines 333–390 and 18gq / 18lp (input in chapter 13) were not part of the assignment beyond the changed lines; their own changes belong to another reviewer.
- Unchanged lines were read only as context.
