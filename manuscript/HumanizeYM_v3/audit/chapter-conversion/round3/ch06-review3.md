# Third review: chapters/06-large-fields.tex

Worktree /Users/mgubi/ym-terminology, file manuscript/HumanizeYM_v3/chapters/06-large-fields.tex. I paired the old lines (4f462ac5) with the HEAD lines, 396 changed lines, and read every pair against the present file, which I read from line 1 to line 1568. I formed my judgement before reading ch06-apply.md, ch06-review.md, round2/ch06-review2.md, round2/harmonise.md and the leads. I corrected 25 lines, all within lines. The file has 1568 lines, as at HEAD. Nothing is staged or committed.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 6:919 | ERROR (minor) | "The curvature, block average, / and likelihood tests are then on their plateaux." | "The two partition-of-unity weights / and the normalized weights of the auxiliary index are then equal to one." | Lead (b). Each of the three items has a counterpart: curvature test = `ϑ_f` factor, block-average test = `ϑ_n` factor, likelihood test = normalized weight of the auxiliary index (*likelihood* 2, basis S). "Equal to one" is right for these factors: the place is far from `A`, so the factor is `1−ϑ` with `ϑ=0` below `t_f/4` or `Wt_f`, and the normalized weight is one on the minimizing branch. But the weights of 6:70–76 are products over all plaquettes or all edges, so saying that "the two partition-of-unity weights" equal one claims too much. | "The local factors of the two partition-of-unity weights / and the normalized weights of the auxiliary index are then equal to one." |
| 6:1015 | ERROR (minor) | "All corresponding / likelihood factors are on their plateaux." | "The partition-of-unity weights and the / normalized weights of the auxiliary index there are equal to one." | Same over-claim as 919, though "there" limits it. HEAD also adds the partition-of-unity weights to what was "likelihood factors". The source (Martin, quoted under *likelihood*) says both kinds equal one, and the thresholds `t_f/4` and `Wt_f` on line 1014 are those of `ϑ_f` and `ϑ_n`, so I kept the addition. | "The corresponding factors of the partition-of-unity weights and the" |
| 6:947 | TERM / MISMATCH | "its stationary tree response" | "the linearization $W_F$ of their critical configuration in the block axial gauge" | Lead (c). In the book `W_F` is the *representative* in the block axial gauge of the linearization `W` (5:1151, 5:1311, 7:574). It is not itself "the linearization in the block axial gauge". | "the representative $W_F$, in the block axial gauge, of the linearization of their critical configuration" ("their" = of the quadratic forms of the two consecutive scales, as in 5:528 "of the quadratic problem") |
| 6:953 | TERM / MISMATCH | "Let $a=W_F h$ be the stationary fine response to a coarse" | "Let $a=W_F h$ be the linearized critical configuration, with $W_F$ as in \eqref{ch05:stationary-tangent}, for a coarse" | Lead (c). "Linearized critical configuration" is a third name, found nowhere else. The added reference is correct (5:1149 defines `W_Fv`), so I kept it. | "Let $a=W_F h$ be the fine field that the linearization of the critical configuration, in its representative $W_F$ of \eqref{ch05:stationary-tangent}, assigns to a coarse" |
| 6:1545 | TERM | "does not replace the tree response by a different gauge response," | "does not replace $W_F$ by the linearization in a different gauge," | Same naming. The other object is the representative of `W` in another gauge, for example `W_a`. | "does not replace $W_F$ by the representative in a different gauge," |
| 6:282 | ERROR (minor) | "kernels, with their coefficients aligned with the curvature rows used" | "kernels, with their quadratic coefficients satisfying the factorization hypothesis for the curvature components used" | The qualifier "quadratic" is new. It narrows the hypothesis of Proposition ch06:signed-input. It is plausible from 6:140 but not stated by the old line. | "kernels, with their coefficients satisfying the factorization hypothesis for the curvature components used" |
| 6:1278 | ERROR | "multiplying by the base affine row, of size $O(t_f)$ on the protected" | "multiplying by the affine component at the base point, of size $O(t_f)$ on the protected" | "Base point" is a defined notion in this chapter (the base point of a local term, and `V_0`, 694, 809). The factor here is the affine approximation itself, evaluated on the protected chart (the half-square difference is affine × Taylor remainder + ½ remainder²), not its value at a base point. | "multiplying by the base affine component, of size …" (old wording, new noun) |
| 6:1374 | LANGUAGE | "the full signal and add its replica value." | "the full displacement field and add its value at $\operatorname{rep}V$." | "its" now reads as "the displacement field's". What is added is the value `b(V)` of the components at `rep V` (6:587). | "the full displacement field and add the value of the components at $\operatorname{rep}V$." |
| 6:427, 630, 772, 813, 985, 996, 1070, 1181, 1226, 1284, 1313, 1314, 1407, 1450, 1457, 1474, 1504 | LEFTOVER | "cost(s)" (unchanged lines) | unchanged | Point (a). This is *cost* sense 1 (basis R): a factor contributed to a bound. Outside chapters 6, 9s, 10 and 11 the book now says "contributes", "factor" or "loses", and the conversion reports give no reason for leaving chapter 6 out. | "contributes" (630, 772, 813 "contributes a factor $|I|$", 985, 996, 1226 "contribute an additional polynomial factor", 1313, 1314, 1407); "factors" (1070, 1181, 1457, 1474 "derivative factors polynomial in…"; 1284 "with the fixed factors from the path bounds"); "contributions" (1450); "amount to at most" (427); "satisfies" (1504, before the displayed inequality) |
| 6:1317 | LEFTOVER (kept) | "For path labels the analogous cost is their true length" | "For path terms the analogous cost is …" | "Cost" is used for the counting-and-derivative factor of 1313–1314, measured by the true length. Neither "factor" nor "contribution" fits without adding a word such as "a power of". | left for the author |
| 6:1018 | TERM | "compulsory component region" | unchanged | Undefined. It is now the only "compulsory" in the chapter: 1461 says "cutoff factor kept inside the component". | left for the author (identification with the `300B` region is basis I) |
| 6:1557 | — | "selecting a scale schedule" | "choosing the schedule of Chapter~\ref{ch10:trajectory}" | Harmonisation change, never reviewed. It is correct: "schedule" is Chapter 10's word (10:5, Section ch10:schedule), and the label exists. | kept |
| 6:85 | MINOR | "An allocation sector fixes the selection, …" | "A \emph{sector} is a term of this decomposition with fixed discrete data: it fixes …" | A new definition. It is loose: the spanning trees and the auxiliary index are not part of the partition of unity just introduced (the index comes from the kernel sum 4:237). It is not false. | left for the author |
| 6:834 | MINOR | "A cutoff remainder is bounded …" | "A cutoff remainder, a cutoff factor minus one, is bounded …" | The gloss reads "cutoff factor" broadly. The remainders also include the normalized weights of the auxiliary index minus one (*cutoff remainder*, basis S; 6:1107 lists "cutoff factors or probability weights of the branches"). | left for the author |
| 6:920, 1016 | TERM | "likelihood tests/factors" | "normalized weights of the auxiliary index" | The normalization (number of values times probability weight, equal to one on the minimizing branch) is stated nowhere in the book. | left for the author |

All other changed lines check out: same objects, connectives and quantifiers, and the dictionary word for the sense at that line. In particular I checked these: 8–11, 13 (`m+1`, `m` agree with 26); 49 (definitions of deviation and index triple); 63, 87, 362–363 (auxiliary index as at 4:217–218, which covers both the local gauge transformations and the averaging operation; no `α`); 90 (`H` as coarse plaquettes, consistent with 295); 109 (`α_p`); 135 (5:533 holds three identities, so the plural is right); 161–165; 170 (as 4:525, 5:1045); 172, 175; 303 (as 4:298); 317, 344 (axial gauge on the macro-box, as 4:367, 5:1005); 326, 355–356 (*excess* 1); 368 (on the minimizing branch the averaging operation is the nearest-point projection, 4:189–201, so dropping "nearest-point" loses nothing); 442 (B88a = Balaban1988Cluster, B88b = Balaban1988Expansions, as in Appendix L and the *frozen* Literature line); 453, 459, 491 (link support, averaging components); 488, 514 ("Poincaré-type" as 5:1290, 1375); 638, 1282 ("directions of size $O(t_f)$" = the dimensionless parameters of 627–629); 733, 739; 897, 908; 1080; 1296 (`c_B` at 1172); 1332; 1403–1406; 1408; 1493 (`v` as at 976); 1540–1541.

## Corrections applied

25 lines: 282, 427, 630, 772, 813, 919, 947, 953, 985, 996, 1015, 1070, 1181, 1226, 1278, 1284, 1313, 1314, 1374, 1407, 1450, 1457, 1474, 1504, 1545.
- ERROR: 4 lines (282, 919, 1015, 1278)
- TERM / MISMATCH: 3 lines (947, 953, 1545)
- LANGUAGE: 1 line (1374)
- LEFTOVER: 17 lines ("cost")

## Cross-chapter mismatches not fixed

- Partition of unity / partition-of-unity weights (6:67, 919, 1015) against "sector allocation weights" (9:81–82).
- `β`-independent quadratic term (4:525; 5:1045; 6:170, 1261, 1270) against "inherited loop action" (7:237, defined there as this term) and "loop term" (9:836; 9s:38, 151; 17t:148; 11R:343 "quadratic-loop terms"). Chapter 6 agrees with chapters 4–5.
- `W_F`: "block axial gauge" (5:1151; 6:470, 947, 974; 7:574) against "block axial chart" (5:1234; 9s:189; 6:1512 uses "chart" in the coordinate sense) and "forest representative" (17c:49).
- Link support (6:453 on; 11) against "support of the expression" (4:506). Harmonisation found these to be different objects, so a single name would be wrong.
- "Pull-back" is `rep V` (5:920; 6:180, 445, 489) but means composition with the critical configuration in 7:1083–1151 and chapter 17.

## Leftover house words

- Kept on purpose. "physical" at 691, 693, 735, 1079, 1458, 1466, 1512, 1534 (*physical* senses 4/8, basis I). "event label" (835–877, 1106; defined at 835). "weight(s)": ordinary use, or a defined probability weight or partition-of-unity weight. "actually assigned" (1162): ordinary. "Gaussian units" (1504): ordinary. "mismatch" at 1379 ("each frozen mismatch") and 1410 ("the two signed mismatch terms", *mismatch* 2, basis I). "envelopes" (1187, *envelope*, basis I at this line). "compulsory" (1018). "seeded / unseeded" (1544, as restored in round 2). "cost" (1317). Every other "actual", "predictor", "frame" or "stationary" stands only inside a label.
- Replaced: "cost(s)" on 17 lines (see Findings).

## Leads

- **6:947** ("their critical configuration"). Verified: "their" refers correctly to the quadratic forms of the two consecutive scales, but `W_F` was called the linearization rather than its representative. Corrected.
- **6:919–920** (three items became two plus one; "on their plateaux" became "equal to one"). Verified. The count matches: the two partition-of-unity weights stand for the curvature and block-average tests, and the normalized weights for the likelihood tests. "Equal to one" is correct for the relevant factors, because the place is far from `A`, so `1−ϑ = 1` and the minimizing-branch weight is 1. The phrase over-claimed for the global products, and I corrected it to "local factors" (919) and "corresponding factors" (1015).
- **partition-of-unity weights (6:919, 1015)**. These are new phrases for the `ϑ` products of 6:67–76 and are used consistently in the chapter. For the mismatch with 9:81–82 see above.
- **6:953** ("linearized critical configuration"). Corrected (see Findings).
- **6:1018** ("compulsory component region" undefined). Confirmed and left for the author.
- **6:1410** ("two signed mismatch terms" against 6:212). Probably `E_L`, `E_D`, but this is basis I. Left for the author.
- **6:1187** ("derivative envelopes" against "majorant"). Ordinary use here (*envelope* basis I at this line). Left.
- **6:1437**. Already found right in the leads, and I agree.

## Assessment of earlier corrections

- Round 1, 453 (link support tied to "support of the expression"): wrong, as harmonisation found, and it has been removed.
- Round 1, 63/87 kept `α` before 1170: wrong, and round 2 removed it. I agree with round 2.
- Round 2, 946 (removed "free") and 1544 (restored seeded/unseeded): correct.
- Harmonisation 1074, 1170, 1475, 1556, 1557: correct. 1170 and 1556 are back to the 4f462ac5 wording "support exponent".
- None of these rounds noticed the issues at 282, 947/953/1545, 1278, 1374 or 919/1015.

## For the author

1. 6:1018: define "compulsory component region" or replace it (the `300B` identification is basis I).
2. 6:920, 1016: say once what "normalized weights of the auxiliary index" are (the number of values times the probability weight, equal to one on the minimizing branch).
3. 6:1317: "the analogous cost is their true length". Choose a wording, for example "the analogous factor is a power of their true length".
4. 6:1278: "the base affine component" is the old wording. Consider "the affine component itself".
5. 6:85: the definition of *sector* names discrete data that the partition of unity alone does not supply.
6. 6:834: the gloss "a cutoff factor minus one" leaves out the weights of the auxiliary index, unless "cutoff factor" is read broadly.
7. 6:1410: "the two signed mismatch terms". Write `E_L`, `E_D` if that is what is meant.
8. 6:694/733: "protected" is used before its definition. This needs a change that moves lines.
9. "Cost" remains on 37 − 17 = 20 lines in chapters 9s, 10, 11 and elsewhere. Chapter 6 now follows the rest of the book.

## Checks

- Line count: `wc -l` gives 1568, equal to `git show HEAD:…/06-large-fields.tex | wc -l` (1568). `git diff --stat`: 25 insertions, 25 deletions, this file only.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1250 references. All explicit cross-references resolve; no duplicate labels." Exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-t3 monograph.tex`: exit 0. In monograph.log, "undefined" 0, "Citation" 0, "Overfull" 0. The build used the other chapters in their current state.

## Not checked

- Rendered PDF pages were not inspected.
- Bałaban's papers were not opened. The sentences at 11 and 442 were checked only against the Literature lines of *cutoff failure*, *large-field set* and *frozen*, and against Appendix L.
- Source manuscripts and Lean were not opened. Basis-S readings (likelihood 2, cutoff remainder) were taken from the dictionary.
- ch06-apply.md was read only for "cost". Other chapters were checked by grep only.
