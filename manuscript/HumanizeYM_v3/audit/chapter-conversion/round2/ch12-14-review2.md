# Second review r8: 12, 13, 13sb, 13ba, 14, 14lc

Worktree `/Users/mgubi/ym-terminology`. I read the word diffs `4f462ac5..HEAD` of the six files first, then the reports `ch12-13-apply.md` and `ch12-14-review.md`, and the dictionary entries concerned. All changed lines were examined (12: 111, 13: 38, 13sb: 37, 13ba: 82, 14: 116, 14lc: 20; 404 in all). Every edit is within one line, and every file keeps its line count.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 13:163–165 | LEFTOVER (coordinator) | `comparison depth increases`; `comparison depths`; `At each fixed depth` | unchanged | *comparison level* entry: one word, *comparison scale `k`* (as in 11:734, 1149) | `comparison scale increases`; `comparison scales`; `At each fixed comparison scale` |
| 14:227 | LEFTOVER | `the numerical comparison level` | unchanged | same entry (it lists 14:226–227) | `the numerical comparison scale` |
| 14lc:23 | LEFTOVER | `At an admissible comparison depth $k$` | `At a comparison depth $k$ whose comparison window lies in a single stage` | "depth" should be "scale". The condition clause is the dictionary's S-basis proposal; I kept it | `At a comparison scale $k$ whose …` |
| 12:391 | TERM / MISMATCH | `The averaging weights sum to one` | unchanged | *averaging weight* is defined in chapter 4 (4:186) as the convolution weight `w^av`. Here the words mean the weights of a finite stencil average | `The weights of this average sum to one` |
| 12:143 | LEFTOVER | `distance from the actual graphs` | unchanged | *actual* 6. The graphs meant are the "selected graphs" of 12:134, 139 | `distance from the selected graphs` |
| 12:293 | LEFTOVER | `the actual cutoff moment` | `the actual lattice correlation at the cutoff` | "actual" left standing. Both sides of the contrast are now named (*actual* 6) | `the lattice correlation at the cutoff` |
| 12:286 | LEFTOVER | `its vacuum denominator` | unchanged | *vacuum* 2 / *vacuum normalization bound*: `Z⁰`, the normalization without insertions. "Vacuum" is kept for `Ω` in chapters 14–16 | `its denominator without insertions` |
| 13ba:32 | LEFTOVER | `the actual cutoff $N$` | unchanged | *actual* 6 (13ba:32); the word carries nothing | `the cutoff $N$` |
| 13:231 | LEFTOVER | `for a physical lattice difference` | unchanged | *physical* 2: the difference carries the inverse step `a_N^{-1}` (13:235–236) | `for a dimensionful lattice difference` |
| 14:530–531 | LANGUAGE | `because its temporal residual response and all its transverse profiles are nonnegative` | `because the Laplace transform of its temporal residual profile and all its transverse profiles are nonnegative` | Ambiguous attachment: "the Laplace transform of" seems to govern the transverse profiles as well. Those profiles are themselves nonnegative | `because all its transverse profiles and the Laplace transform of its temporal residual profile are nonnegative` |
| 12:40, 370 vs 12:13, 133, 298; 13ba:17 | MINOR | `common construction`; `common selected trajectory` | `cutoff-independent construction` | The same object has two phrasings, both dictionary proposals (*common* 3, *trajectory* 2) | left for the author |
| 13ba:258, 261 | DICTIONARY | `coupling-threshold requirement / conditions` | unchanged | The condition is on the minimum starting scale `b_q` (10:122–126), not on `β̂` (first reviewer's finding, confirmed). It stands next to "lower bounds on the reference coupling" elsewhere in the file | left for the author (suggested: "lower bound on the starting scale") |
| 14:519, 579, 611 | LEFTOVER (basis I) | `collision orders` | unchanged | The proposal "order of the singularity at coincident points" has basis I | left |
| 14:34 | LEFTOVER (kept) | `unit vacuum $\Omega_\mu$` | unchanged | *unit* 2 proposes "unit vector" (basis I); "vacuum" is the kept word for `Ω` | left |

The following were checked and found correct, with no change:

- 12:22–29: *total large-field activity* is defined before its first use and used with one meaning.
- 12:31, 41, 175: *action data*.
- 12:178: the reference to (ch04:weighted-sums) follows *rooted* 1(a).
- 12:236: "incidence bounds" follows *rooted* 1(c).
- 12:247: the reference to (ch11:replicated-bound) is the dictionary's request, and the formula matches (11:808–812).
- 12:37–38: the forward reference to Section ch12:graphs is true; the admissible graph is defined at 12:82.
- 12:187: "regularity condition at scale `m`" (*cutoff* 3).
- *Source degree* (defined 11:134) is used throughout.
- 13:120: *correlation functional* agrees with 3:482.
- 13:206, 211: "limit point" (*cluster* 1).
- 13:239: "backward comparison" (*trial descent*).
- 13:394: reference labels (*trial encoding*).
- 13sb:26: "coupling constant renormalization" (*scalar* 3).
- 13sb:27, 36: *admissible* 7 (basis S).
- 13sb:73: *mode*.
- 13ba:36, 165: "small-field indicator" (App. D 13ba:36; the guard is an indicator, *regularity condition* entry).
- 13ba:229–270: local gauge transformation, transporter, auxiliary random variables (*primitive* 4, *shared frame seed*).
- 13ba:283: *replicate*.
- 13ba:194: *room*.
- 14:12: "undecomposed" is glossed at its first use, 18lp:8, which is input in chapter 13.
- 14:99: *buffer* (13:335).
- 14:308: "the sign of the chosen tensor".
- 14:410: the title follows *angular boundary*.
- 14:448, 464: *frequency profile* and *residual profile* are defined at first use.
- 14:465 ff.: "Laplace transform" (*response* 9).
- 14:776, 796: "left side of (ch14:line-ward)" (*angular boundary*).
- 14:946: the first reviewer's correction.

No sentence about Bałaban's or Dimock's papers occurs in these files. "Lowest scale" and "bottom" do not occur in them.

## Corrections applied

14 phrases on 13 lines:

| class | phrases |
|---|---|
| LEFTOVER | 12 (comparison depth/level → comparison scale: 5; actual: 3; vacuum: 1; physical: 1; averaging weights: 1, also counted as TERM) |
| LANGUAGE | 1 (14:530–531) |
| ERROR | 0 |

## Cross-chapter mismatches not fixed

- **Remaining "comparison level" / "comparison depth" outside my files:**
  - 11R:7, 70;
  - 11:1343, 1361, 1401, 2032, 2035, 2064;
  - 15:253.
- **13ba:258, 261 against 13ba:39, 50, 83, 101.** "Coupling-threshold" there is a condition on the starting scale, not on `β̂` (see the table).
- **12:40, 370 against 12:13, 133, 298.** The construction of Chapter 10 is named in two ways.

## Leftover house words

**Kept on purpose:**

- *label*: polynomial label, sense 1, throughout chapters 12–13.
- *selected*: senses 2 and 6 at 12:123, 134, 139; 13:172, 307, 395; 13sb:50; 13ba:30, 50, 195, 200, 304. The dictionary proposes deletion or "fixed"; it was not applied by the conversion, and I did not apply it.
- *unit*: "unit forward differences" (12:391) and "units" (13ba:148) are ordinary uses. "Unit vacuum" (14:34) is basis I.
- *weight*: source weights; `ω^res`.
- *profile*: chapter 14's defined sense.
- *mixed*: only in the labels `ch14:mixed-sign` and `ch18:mixed-bound`.
- *physical Hilbert space* (14:1026): standard.
- *collision orders*: basis I.

**Replaced:** see the table.

## Assessment of the first review's corrections

All ten were checked, and none is wrong:

- 12:48, 62, 126: "width".
- 12:131: title restored.
- 12:219.
- 13:120, 138, 237.
- 13ba:124: "full transfer".
- 14:308.
- 14:406, 992: "response" restored for values.
- 14:946.

The first review missed "comparison depth/level" in 13 and 14, and the "averaging weights" clash at 12:391.

## For the author

- **12:40, 370.** Choose one name for the construction of Chapter 10.
- **13ba:258, 261.** Reword as a lower bound on the starting scale.
- **14lc:23.** The single-stage condition on the comparison window is still not stated anywhere in the book (*admissible comparison depth*, basis S).
- **12:131.** The title "Forgetting the terminal graph" is left as the first reviewer restored it. "Terminal graph" names no object.
- **13:367.** "lie in at most `2n` classes" lost "those of `w` and `θw`" before the conversion (*residue patterns*).

## Checks

- **Line counts** equal `git show HEAD:<path> | wc -l` for all six files: 405, 403, 177, 337, 1028, 110.
- **`python3 tools/check_draft.py`:** "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- **`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r8 monograph.tex`:** exit 0. The log has "undefined" 0, "Citation" 0, "Overfull" 0.
- **Rendered text:** extracted with `mutool draw -F txt`. Each corrected phrase appears once, and the text has no "??".
- Nothing was staged or committed. Other files show as modified in the worktree; those are other reviewers' edits.

## Not checked

- Page images were not viewed.
- Sources and Lean were not opened.
- The remaining "selected" (sense 2) uses were not converted.
- 18-graded-quotient and 18-lattice-products belong to other reviewers.
