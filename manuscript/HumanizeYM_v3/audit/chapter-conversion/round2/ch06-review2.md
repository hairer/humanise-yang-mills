# Second review: chapters/06-large-fields.tex

Worktree /Users/mgubi/ym-terminology, file manuscript/HumanizeYM_v3/chapters/06-large-fields.tex. I read the diff 4f462ac5..HEAD first: 398 changed lines, compared old against new line by line, with the present text for context. Only after that did I read audit/chapter-conversion/ch06-apply.md (in part) and ch06-review.md. 15 lines corrected, all within lines. The file has 1568 lines, as at HEAD. Nothing staged or committed.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 6:63 | TERM | "Every chosen frame tag must have positive" | "Every chosen value of the auxiliary index `$\alpha$` of Chapter~\ref{ch04:blocking} for a local gauge transformation …" | Inserts the symbol `α` after "auxiliary index". In this chapter `α` already has two other meanings: `α_p` (109–120, 260) and the decay rate of the support weight (1170, 1177, 1232, 1311, 1465, 1475). This is the pattern the brief warns about. | "Every chosen value of the auxiliary index of Chapter~\ref{ch04:blocking} for a local gauge transformation …" |
| 6:87 | TERM | "and all frame and block average tags." | "and the value of the auxiliary index `$\alpha$`." | Same as 63 | "and the value of the auxiliary index." |
| 6:362–363 | TERM | "all selected frame and block average branches / … the redundant tags" | "… chosen by the index `$\alpha$` / the redundant values of `$\alpha$`" | Same as 63 | "chosen by the auxiliary index" / "the redundant values of the auxiliary index" |
| 6:486 | TERM | "same trees and tags." | "same trees and the same index `$\alpha$`." | Same as 63 | "same trees and the same values of the auxiliary index." |
| 6:671 | TERM | "the branch masses," | "the probability weights `$\lambda(U,\alpha)$` of the auxiliary index," | Adds a formula. `α` clashes as at 63, and `λ` indexes amplitudes `a_λ`, `S_λ` at 1173–1177. | "the probability weights of the auxiliary index," |
| 6:920, 1016 | TERM | "likelihood tests are then on their plateaux" / "All corresponding likelihood factors" | "the normalized weights of the index `$\alpha$`" | Same as 63 | "the normalized weights of the auxiliary index" |
| 6:172, 175 | ERROR | "At Wilson initialization the direct" / "the terminal fine metric is unmodified" | "(the Wilson density at the cutoff scale `$N$`)" / "fine metric at the ultraviolet cutoff `$N$`" | Introduces `N`, which in this same passage is the complement map `N` (126–128, 154, 948). Later in the chapter `N` is also a number of coordinates (852, 877). | "(the Wilson density at the ultraviolet cutoff)" / "fine metric at the ultraviolet cutoff is unmodified" |
| 6:846 | DICTIONARY | "the actual mean, block average response, and event indicators." | "the mean `$m_Y$`, the derivative of the averaging operation, and cutoff factors." | "Event indicators" was replaced by "cutoff factors". No dictionary entry supports this (*event indicator*: keep, say which event), and line 1022 still says "these event indicators" for the same objects. | "… derivative of the averaging operation, and event indicators." |
| 6:946 | ERROR (minor) | "Use the same adjacent quadratic pair in" | "Use the free quadratic forms of the two consecutive scales as in" | Adds the qualifier "free". The old line does not have it, and elsewhere in the chapter "free" was the house word for non-tree links. | "Use the quadratic forms of the two consecutive scales as in" |
| 6:1404 | LANGUAGE | "the squared group distance" | "the term in `$\chi(\cdot)^2$`" | Clumsy, and it names a formula fragment rather than a quantity. The book's word is "distance from the identity". | "the squared distance from the identity" |
| 6:1406 | LANGUAGE | "so only its nonnegative residual remains." | "so only this nonnegative square remains." | "this" has no clear antecedent: the previous sentence has two squares. | "so only its nonnegative square remains." |
| 6:1544 | ERROR | "compare a seeded sector to an unseeded law," | "compare a sector with nonempty index triple to the law with empty index triple," | The unseeded law has `A_f = A_n = ∅` but `A_c` equal to the coarse large-field set of the configuration (dictionary *seeded sector*, basis S). That set need not be empty, so "empty index triple" is false. Conversely, a sector with only `A_c ≠ ∅` is not seeded. | 4f462ac5 wording restored: "compare a seeded sector to an unseeded law,". Better wording is left for the author. |
| 6:1557 | DICTIONARY | "selecting a scale schedule" | "choosing a sequence of scales" | What is chosen is the schedule of Chapter 10 (stage and block ratio at each scale). The dictionary proposes "fixed parameter sequence"; the reading guide (RG:32) keeps "scale schedule". "Sequence of scales" is weaker than the old phrase but not false. | left for the author |
| 6:1018 | TERM | "compulsory component region" | unchanged | Now the only use of "compulsory" in the chapter, and it is undefined. Line 1461 was converted to "cutoff factor kept inside the component". | left for the author (radius `300B` identification is basis I) |
| 6:694 / 733 | TERM | — | "protected logarithmic chart" (694); definition "Call a factor protected …" (733) | The word is used 39 lines before the definition the conversion added. | left (moving the definition would need a line change) |
| 6:13 | MINOR | "one adjacent pair of scales" | "two consecutive scales, the fine scale `$m+1$` and the coarse scale `$m$`" | Adds symbols. They agree with `t_f=t_{m+1}`, `t_c=t_m` at 26. | kept |
| 6:1493 | MINOR | "the tree-straightened linear relative response" | "the linear relative field `$W_Fh-\operatorname{rep}h$` of the proof of Proposition~…" | Adds a formula. It matches 976 ("relative candidate `v=W_Fh-\operatorname{rep}h`"). | kept |
| 6:1403 | MINOR | "The fine and block average energies" | "The energies `$E_f$` and `$E_n$`" | Adds symbols. I checked the identification: `E_f = ½|X_f−Φv_c|² + (K_f − ½|X_f|²)`, and similarly for `E_n`. It holds. | kept |

All other changed lines check out: same objects, quantifiers and connectives, and the dictionary word for the sense at that line. I checked these in particular: the two Bałaban sentences (11, 442) against the *cutoff failure* and *frozen* Literature lines (B88b = Balaban1988Expansions, B88a = Balaban1988Cluster, both keys exist); 919–920 and 1015–1016 against *likelihood* 2 (basis S, which says the allocation weights also equal one); 834 and 1018 against *warning*; 845 *response* 4; 1170 (`hB`-neighbourhood); 1296 ("connected covering number", ch04:587); 1540 (`T_V`, defined at 728); and 303/317/344 macro-box and axial gauge against 4:298, 4:367 and 5:1005.

## Corrections applied

15 lines: 63, 87, 172, 175, 362, 363, 486, 671, 846, 920, 946, 1016, 1404, 1406, 1544.
- TERM: 8 lines (63, 87, 362, 363, 486, 671, 920, 1016), all the auxiliary-index `α`.
- ERROR: 4 lines (172, 175, 946, 1544).
- DICTIONARY: 1 line (846).
- LANGUAGE: 2 lines (1404, 1406).

## Cross-chapter mismatches not fixed

- **Link support.** 6:453 and 11:134–164 / 11E:15, 81, 95 say "link support"; 4:506 says "support of the expression". Chapter 6 links the two names, but one should be chosen.
- **Decay rate of the support weight.** 6:1170 and 1556 (with chapters 8 and 9) say "decay rate of the support weight"; 4:651 says "support exponents", and 11R:125, 179 say "support exponent".
- **Auxiliary index.** Chapter 6 now names the auxiliary index without its symbol. Chapters 4 and 5, 9s:127–242 and 11 write "auxiliary index `α`". That is consistent with chapter 4, but within chapter 6 `α` is taken.
- **Schedule.** 6:1557 "sequence of scales" against Chapter 10's defined "schedule" (10:121) and RG:32 "scale schedule".

## Leftover house words

- **Kept on purpose.**
  - "physical" at 691, 693, 735, 1079, 1458, 1466, 1512, 1534: senses 4 and 8, basis I.
  - "event label" (835–877, 1106): basis D, keep.
  - "weight(s)": ordinary use or a defined probability weight.
  - "actually assigned" (1162): ordinary emphasis.
  - "Gaussian units" (1504): ordinary.
  - "mismatch" at 1379 ("frozen mismatch") and 1410 ("two signed mismatch terms", *mismatch* 2, basis I): no D/R/S proposal.
  - "compulsory" (1018): see Findings.
- **Missed, now replaced.** None among the listed house words. The remaining "tag" senses were already gone, and "actual", "block average", "stationary", "noise", "frame", "tree gauge", "label" (in the tag sense) and "level" no longer occur in the prose.

## Assessment of the first review's corrections

- **α kept before line 1170.** The first reviewer kept the symbol `α` for the auxiliary index before 1170, arguing that `α` is the decay rate only from 1170 on. That misses `α_p` at 109–120 and 260, and it leaves two meanings of `α` in one chapter. I removed it at all eight places.
- **Keyword collision at 1544.** The first review accepted "nonempty / empty index triple" at 1544 as an Appendix D repair. It is not correct for `A_c`; see Findings.
- **Symbol `N` at 172/175.** The first review listed the clash with `N` (852, 877) but did not notice the clash with the complement map `N` in the same paragraph. I fixed it.
- **Correct corrections.** Its other corrections (63 wording, 164, 259, 442 attribution, 453, 469, 494, 694–695, 733, 739, 992, 1006, 1018, 1108, 1170, 1344, 1397, 1408, 1422, 1449, 1461, 1558) I found correct.

## For the author

1. **1544.** A wording for "seeded sector / unseeded law" without the house word. For example: "a sector in which `$A_f$` or `$A_n$` is nonempty to the law of the sector with `$A_f=A_n=\emptyset$`" (adds symbols).
2. **1557.** "choosing a sequence of scales" against "choosing the schedule" (Chapter 10) or "a scale schedule" (reading guide).
3. **1018.** "compulsory component region" (undefined) against "the retained `$300B$` region of its component" (identification basis I).
4. **694 / 733.** "Protected" is used before its definition. Consider moving the definition to 694 in a later edit that may change lines.
5. **Basis-I applications** listed by the first review (direct → plaquette; selected → fixed/this; mass/likelihood → probability weight; path word → contour variable; stored → prescribed; physical counting → unnormalized `ℓ²`; actual sense 2 → non-flat): I found none of them wrong at its line.

## Checks

- **Line count.** `wc -l chapters/06-large-fields.tex`: 1568, equal to `git show HEAD:… | wc -l`. `git diff --stat`: 15 insertions, 15 deletions, this file only.
- **check_draft.** `python3 tools/check_draft.py`: "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels." Exit 0.
- **Build.** `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-r3 monograph.tex`: exit 0. In monograph.log, "undefined" 0, "Citation" 0, "Overfull" 0. The build used the other chapters in their current state, which other reviewers are editing.

## Not checked

- Rendered PDF pages were not inspected (pdftotext is not installed).
- Bałaban's papers were not opened; the citation sentences were checked against the dictionary Literature lines only.
- Of the first-round reports, ch06-apply.md was not read in full.
- Other chapters were checked by grep only, for the terms named above.
