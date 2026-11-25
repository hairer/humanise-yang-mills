# Second review: chapters 4 (04-blocking.tex) and 5 (05-gaussian.tex)

Worktree `/Users/mgubi/ym-terminology`, branch `claude/v3-terminology-dictionary`. Diff read: `git diff --word-diff 4f462ac5 HEAD` for both files: 177 changed lines in chapter 4, 227 in chapter 5 (404 in all), each read against the present file. The diff was judged first; then the first-round reports (`ch04-apply/review/fixes.md`, `ch05-apply/review/fixes/shorten.md`) were read. Line numbers are those of the present files (unchanged in number). Nothing staged or committed.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 4:36 | TERM | `in order $o$. For a root $z$` | `in order $o$; a \emph{contour} is a lattice path along which the link variables are multiplied, and its \emph{contour variable} is their ordered product. For an initial point` | Duplicate definition: *contour* and *contour variable* are already defined (with emph) at 1:78–80, and holonomy at 1:80. Chapter 4 says at 4:12–13 that the conventions are those of Chapter 1. | `in order $o$. For an initial point` |
| 4:497 | MISMATCH | `combination of transported curvatures,` | `combination of parallel-transported curvatures,` | The book's term is *transported curvature*, defined in chapter 2 (equation `ch02:transported-curvature`, cited on 4:503) and used in 2:201, 282, 314, 370; 2e:37, 62, 216; 7:147; 10:313. Chapter 4 alone said "parallel-transported". | `combination of transported curvatures,` |
| 4:502 | MISMATCH | `plaquette curvature transported to` | `plaquette curvature parallel-transported to` | Same. | `plaquette curvature transported to` |
| 5:20 | MINOR (citation) | (sentence added) | `… (his ``minimal configuration''), for several steps at once; …` | First-use statement about Bałaban without a reference. The *Literature* line of *stationary graph* rests on B85d (p. 277: "This minimal configuration is called a background field"), key `Balaban1985Variational`. | `(his ``minimal configuration''~\cite{Balaban1985Variational}), for several` |
| 5:937 | MINOR (citation) | (sentence added) | `… where Ba{\l}aban has the tree of his contours $\Gamma_{y,x}$ rooted at a block corner; …` | No reference; the *Literature* line of *tree slice* gives B84a p. 19 (axial gauge in blocks with the contours `Γ_{y,x}`), key `Balaban1984Propagators`. (The first reviewer suggested it as optional.) | `… $\Gamma_{y,x}$~\cite{Balaban1984Propagators} rooted at a block corner; …` |
| 5:861 | LEFTOVER / MISMATCH | `or of marked integral maps` | unchanged | "marked" is a table word (*with / without insertions*). The maps are those of one step on densities with insertions (entry *mark* 1); chapter 12, which treats their cutoff dependence, now says "the cutoff-dependent step with insertions" (12:37) and "one step with insertions" (12:90). The entry gives basis I for 5:861 only because chapter 5 does not say so itself; the object is not in doubt. | `or of the integral maps of a step with insertions` |
| 5:986 | TERM | `Differentiating the actual connector and then its block average` | `Differentiating the gauge-transformed parallel transporter and then the averaging operation applied to it` | The long name was replaced at 4:174 by the short term *transporter* ("for short the transporter"); chapter 6 (6:368) uses the short term. Repeating the long description is what the rules forbid. | `Differentiating the transporter of Chapter~\ref{ch04:blocking} and then the averaging operation applied to it` |
| 5:581, 582, 599 | LEFTOVER | `bounded principal columns`; `both nonprincipal columns`; `the principal columns are $I$` | unchanged | *principal* sense 1 (basis R) is "zero alias", and the chapter now says "zero alias" / "nonzero aliases" everywhere else (250, 279, 351, 360, 402, 412, 425, 548, 571, 579, 796, 817): one object, two names within the chapter. "columns" (basis I) kept. | 581 `bounded columns at the zero alias and bounds`; 582 `for both columns at each nonzero alias on a smaller cube.`; 599 `the columns at the zero alias are $I$ and the other` |
| 5:1019 | (first-round correction; left, see For the author) | `are bounded by the sum in \eqref{ch04:frame-first-power}, so this step` | `are bounded by the sum over the patch estimated in the proof of Lemma~\ref{ch04:predictor-comparison} on either branch, so this step` | Not a vocabulary change: the line had no house word; the first-round fixer replaced an equation reference by a lemma reference and added "on either branch". I checked it: the sum meant is the per-patch display 4:371–374, which holds on both branches by 4:361–365, whereas (4.frame-first-power) is stated for a minimizing local gauge transformation only. So the new wording is correct and more exact, but it changes a reference and a claim. | left for the author |
| 4:189 | MINOR | `The gauge-covariant block average, obtained by projecting …, minimizes` | `On the first of its two branches, the value of the gauge-covariant \emph{averaging operation} is obtained by projecting …; it then minimizes` | Adds a qualifier (true: the minimizing branch is defined at 4:202–210) with a forward reference to the branches. Correct. | left |
| 4:397, 4:428, 4:525, 5:351, 5:379, 5:859, 5:976 | MINOR | words | formulas `$\chi(V_eQ_e(U)^{-1})$, $e\in\partial p$`; `$\chi(U_\square)\le t_m$`; `$\sum_{x,i}A_i^{(2)}(U,x)$`; `$z_\mu=0$`; `accumulated symbol $f_{\rm suffix}$`; `$W=W_s$`; `at $Ly$` → `at $y$` | Mathematics written where the old line had words. Each checked: 397 matches (4.macro-comparison); 428 is equivalent to `X ∩ Bad_m(U) = ∅`; 525 is the β-free term of 4:517; 351 repairs the per-coordinate case split; 379 names the symbol already used undefined in the display 384; 859 agrees with 5:535; 976 agrees with the definition of the patch at 4:173. All true. | left for the author (whether to keep formulas) |
| 4:431 | MINOR | `We keep two kinds of local corrections.` | `… the localized terms, whose sum is the \emph{regular part of the action}, …` | With `V_ρ` (4:555) the regular part is `Σ_i h_{X_i}E_i^{reg}`, the sum with indicators; "sum" is slightly loose. | left for the author |
| 4:36, 89, 106, 161, 279 | DICTIONARY | `root` | `initial point` | *root* 1 (R) proposes "base point" for the contour system; the editor used the *Literature* word "initial point" (B85a "axial gauge with the initial point y"; the entry says it is equally good) because "base point" is the word for `o_i`. Sound; the dictionary should record it. | left |
| 4:298, 367, 398; 5:1005, 1028, 1031–1032 | DICTIONARY | `macro-box`, `macro-patch` | `macro-box` | *macro-box* (R) proposes "enlarged block"; first round kept "macro-box" (also chapter 6). Consistent book-wide; deviation from the dictionary. | left for the author |

No ERROR (meaning changed or false statement) was found in either file. In particular I checked and accept: the eleven first-use and gloss sentences of chapter 4 (4:5, 13–16, 43, 213, 226, 428, 431, 452, 489, 587–591, 651) against the *Literature* lines of *step*, *block average*, *penalty parameter*, *`Bad_m(U)`*, *regular*, *regular activity*, *activity*, *connected covering number*, *stage*; their keys exist in `references.bib` (`Balaban1984Propagators`, `Balaban1985Averaging`, `Balaban1985Spaces`, `Balaban1987RG`, `Balaban1988Expansions`, `Balaban1988Cluster`); 5:20 and 5:930–937 against *stationary graph* and *tree slice*; 5:1045 ("the β-independent quadratic term of the path action" for "inherited loop action", entry R: `ℒ = Σ A_i^{(2)}`); 5:1289, 1375 ("Poincaré-type inequality" = *tree comparison* 2, eq. `ch05:tree-comparison`) and 4:296 (`ch05:nonlinear-tree` = *tree comparison* 1); 5:689 (`pair of stages of one step`, entry *adjacent pair* 2 and Appendix D); 5:1339 (`log det A(x) − log det A(0)`, entry *centered log determinant*); 5:1385 ("standing hypotheses", entry *interface*).

## Corrections applied

| class | count | lines |
|---|---|---|
| TERM | 2 | 4:36; 5:986 |
| MISMATCH | 2 | 4:497, 4:502 |
| LEFTOVER | 4 | 5:861; 5:581, 582, 599 |
| MINOR (missing citation) | 2 | 5:20, 5:937 |
| ERROR, LANGUAGE, DICTIONARY | 0 | |

Ten lines edited in all (3 in chapter 4, 7 in chapter 5); every edit within its line; line counts 677 and 1388, equal to HEAD.

## Cross-chapter mismatches not fixed (other files)

| object | my files | elsewhere |
|---|---|---|
| dependence set | 4:459 (definition, "dependence set"), 461, 493–494, 539, 607 | "full dependence set": reading-guide:28; 6:1117, 1179, 1324; 9:93, 107; 10:127 ("full dependence radius"); 17m:87 |
| quadratic hypothesis | 5:1058 (definition), 1303, 1374, 1382 | "quadratic coefficient condition": 6:140, 6:380 |
| representation data | 4:550 (definition) | "density coordinate tuple", "density coordinate": 09-forest-average:86, 224 |
| regularity condition | 4:426 | "small-field conditions": 9:510 |
| prescribed large-field set | 4:440 | "prescribed set (of large-field sites)": 09-forest-average:231; 9:893 |
| linear averaging operator | 5:88, 154, 306, 993 | "block average $M_a$": 17c:75; title "Difference-preserving block averages": 17t:12 |
| step | 4:5 "A renormalization transformation, called a \emph{step}" | reading-guide:22 already defines "the renormalization transformation, or \emph{step}" (emph). Two defining sentences; harmless, author to choose |
| penalty parameter | 4:226 `\emph{penalty parameter}` | already introduced at 1:409 (and MT:12); the emph at 4:226 is a second definition |

## Leftover house words

Grep over both files for the words of the brief.

Kept on purpose:
- "unit" (4:16 "unit lattice", Bałaban's term; 5:768–769 "unit complex numbers", "unit phase"): ordinary.
- "weight(s)": *averaging weight* (4:16, 186, 375; 5:153, 994) and *probability weight* (4:77, 209, 218, 315; 5:970) are defined terms; "support-weight exponent", "exponential weight" (4:572, 590, 608; 5:1271, 1273) are *weight* 2 (keep); 4:206 "the weights" = averaging weights; 5:900, 909 "weights" of weighted Fourier norms (entry *weight* 6 proposes "factors", but "weighted Fourier spaces" in the same sentence makes "weights" the standard word; left).
- "physical" 5:97, 520, 1085: senses 6 and 5, basis I, not applicable.
- "noise" 5:251, 280, 377–399, 418, 549, 775–782: entry *noise* 1 says "acceptable".
- "mixed coordinates" 4:354: ordinary (coordinates other than the varying one).
- "frame", "tag", "predictor", "actual", "stationary", "connector" occur only inside labels (`ch04:frame-lemma`, `ch04:tag-law`, `ch04:predictor-cost`, `ch05:actual-*`, `ch05:stationary*`, `ch04:connector`).
- 5:609, 624 "matrix row", "two-form row" (*row* 3, basis I); 5:882, 996, 1346 "row (and column) sums" (*row* 6, keep).
- 5:1222, 1287 "the background" for `ρ` (basis I).

Replaced: 5:861 "marked"; 5:581, 582, 599 "principal"/"nonprincipal" (see Findings).

None of "block average", "cutoff failure", "tree gauge", "level", "block transformation", "reset", "unmarked", "heat", "ground", "label", "kill" occurs in the prose of either file.

## Assessment of the first review's corrections

All first-round corrections in these two files were rechecked (the 29 + 32 lines of `ch04-fixes.md`, the corrections of `ch05-review.md`). None is wrong. Remarks:
- 5:1019 (added by the fixer, not proposed by the reviewer): see Findings; correct, but it replaces an equation reference and adds a claim on a line that needed no vocabulary change.
- 4:532, 4:584 ("regular expressions" → "local expressions", "the local expression $E_i^{\rm reg}$ itself"): made to keep the new sentence of 4:452 ("two technical uses") true; basis of *regular expression* is I. Faithful to the chapter.
- 4:121, 127, 150, 358, 367, 379 (unchanged lines changed on the reviewer's MINORs): faithful.
- `Balaban1988Cluster` was added to `references.bib` without a DOI (the fixer says so); the entry exists and resolves.
- The first reviewer's MINOR on 5:581–600 ("principal columns") was not applied; applied now (keeping "columns").

## For the author

1. 5:1019: keep the first round's lemma reference ("the sum over the patch estimated in the proof of Lemma 4.predictor-comparison on either branch") or restore `the sum in \eqref{ch04:frame-first-power}`. The new text is the correct one mathematically (the alternative branch is needed).
2. Formulas introduced by the conversion (4:397, 428, 525; 5:351, 379, 859, 976): all true; decide whether they stay.
3. "macro-box" against the dictionary's "enlarged block"; "initial point" against "base point" for the contour root: record the decision in the dictionary.
4. Within chapter 5 the inequality `ch05:tree-comparison` has four names on unchanged lines: "the tree inequality" (945), "Poincaré-type inequality" (1290, 1375), "the deterministic comparison" (1306), "the Euclidean tree gap" (1319, the gap it implies). Not changed (unchanged lines, no dictionary entry for 945, 1306, 1319).
5. The cross-chapter list above; the chapters named there are outside this assignment.
6. 4:431 "whose sum is the regular part of the action" (sum with indicators).

## Checks

- Line counts: `git show HEAD:<path> | wc -l` = 677 and 1388; working files 677 and 1388.
- `git diff --stat` against HEAD: 04-blocking.tex 3 lines, 05-gaussian.tex 7 lines, each in place.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r2 monograph.tex`: completed, exit 0, after the last edit. Log counts: "undefined" 0, "Citation" 0, "Overfull" 0.
- Rendered text (extracted from the PDF with pypdf): the changed sentences appear on pp. 45, 52, 56, 67, 68, 69 with the citations resolved ([Bał85c], [Bał84]) and "Chapter 4" for the new reference.

## Not checked

- Bałaban's and Dimock's papers themselves: statements about them were compared with the dictionary's *Literature* lines only.
- The rendered pages were checked by text extraction, not visually.
- Other chapters were searched by keyword only, for the mismatches listed; they were not edited.
- The mathematics of unchanged lines, the figure `figures/block-paths.tex`, and `references.bib` entries (beyond existence of the keys).
