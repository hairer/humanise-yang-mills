# Third review: chapters 4 (04-blocking.tex) and 5 (05-gaussian.tex)

Worktree `/Users/mgubi/ym-terminology`, branch `claude/v3-terminology-dictionary`, HEAD `23c008c2`. I read `git diff --word-diff 4f462ac5 HEAD` for both files first: 177 changed lines in chapter 4 and 227 in chapter 5. Each changed line was compared with the old text and checked against the present file. After that I read the earlier reports (`round2/ch04-05-review2.md` and the first-round files) and the leads. Line numbers are those of the present files. Nothing was staged or committed.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 4:209 | TERM | `assign uniform mass to redundant block average labels $z\in\mathbb B_R$.` | `assign uniform probability weight to the redundant values $z\in\mathbb B_R$ of an index.` | Lead (a). "an index" is used here before the auxiliary index is introduced (4:217), and the text does not say which index is meant. The old "block average labels" means the index of the averaging operation, which is the name 4:316 uses ("the indices of the local gauge transformations and of the averaging operation"). | `… the redundant values $z\in\mathbb B_R$ of the index of the averaging operation.` (4:210 "let the index take the value $z$" now has its antecedent.) |
| 5:1234 | MISMATCH | `whereas $W_F$ is its representative in the forest coordinates.` | `… in the block axial chart.` | Lead (b). Everywhere else `W_F` is "the representative in the block axial gauge": 5:1151, 5:1311; 6:947; 7:574; 9s:189 (this line has since been harmonised); 11:642. The chart is the map `(v,ψ) ↦ U(v,ψ)`. `W_F` lies in the gauge slice (5:1144). | `… in the block axial gauge.` |
| 5:1293 | ERROR (symbol inserted) | `and all its redundant local labels agree there as functions of the full field.` | `… local values of the index $\alpha$ specify the same operation there, …` | The conversion inserted `$\alpha$` after "index", but in chapter 5 `α` is the scalar `Σ_l|m_l|² tr D_l` (5:495–496, 572, 577, 815) and a summation index (5:232). The chapter's own wording is "auxiliary index" (5:948, 968). | `… local values of the auxiliary index specify the same operation there, …` |
| 5:1336 | ERROR (symbol inserted) | `All local tag descriptions define the same action and stationary graph` | `All local descriptions by a value of the index $\alpha$ define …` | Same problem as 5:1293. | `All local descriptions by a value of the auxiliary index define …` |
| 4:505–506 | MINOR (two words for one set) | `the small-field indicator of its declared footprint. The footprint contains …` | `the indicator of the regularity condition on its declared support. The support of the expression contains …` | Lead (d). Two phrases, "declared support" and "support of the expression", name the same set two lines apart. The set is not chapter 6's "link support": that set also contains the links read by the averaging operation (6:459), and nothing in the text identifies the two. | left for the author (e.g. "This support contains …"). Not identified with "link support". |
| 5:1019 | (first-round correction) | `are bounded by the sum in \eqref{ch04:frame-first-power}` | `are bounded by the sum over the patch estimated in the proof of Lemma~\ref{ch04:predictor-comparison} on either branch` | Lead (e). I checked it again. The sum meant is the per-patch display at 4:371–374, and 4:361–365 shows that it holds on both branches. `(ch04:frame-first-power)` is stated only for a minimizing local gauge transformation. The present wording is correct, but it changes a reference and adds a claim. | left for the author (keep it, or restore the equation reference) |
| 5:719 | MINOR (untouched line) | `by diagonal extraction` | unchanged | Lead (c). Other chapters say "diagonal subsequence" (10:846; 14:225; 17m:446; 17t:139; 19:89) or "diagonal argument" (13:31, 139). The line was not touched, and no house word from the table stands on it, so rule (f) applies. | left for the author (listed) |
| 4:189 | MINOR | `The gauge-covariant block average, obtained by projecting …, minimizes` | `On the first of its two branches, the value of …` | The text speaks of "the first of its two branches" before the branches are introduced (4:202–212), where they are called the "minimizing" and "alternative" branches. The statement is true. | left for the author ("On its minimizing branch" would match 4:212) |
| 5:1378 | LANGUAGE (minor) | `For the nested selected schedule,` | `For the nested selected choice of parameters,` | "selected choice" is redundant. The sentence parses. | left |

No other error of meaning was found. I checked and accept the following:
- The first-use and gloss sentences at 4:5, 16, 43, 174, 213, 226, 428, 431, 452, 489, 591 and 651, and at 5:10, 20, 335, 731, 930, 937 and 1058. For the literature I checked them against the *Literature* lines of *step*, *block average*, *penalty parameter*, *large-field set*, *regular activity*, *connected covering number*, *tree slice* and *stationary graph*.
- The formulas and symbols added by the conversion: 4:19 (`ZZ^4`), 4:78 (`(z,o)`), 4:361 (`f`), 4:397, 4:428, 4:525; 5:351, 379, 535, 626, 859 and 976. All are true and consistent with the surrounding lines.
- 4:160–161 "one in each dimension": one hyperplane is chosen per induction step `r = 1,…,4`.
- 5:689 "pair of stages of one step": this is sense 2 of *adjacent pair*, the *stage pair* of 10:30.
- 5:1045 "β-independent quadratic term of the path action" for "inherited loop action". It is the same object `ℒ = Σ A_i^{(2)}` (7:237 defines both names).
- 5:296 → `ch05:nonlinear-tree`, which does use both branches (5:1019).
- 5:1289, 1375 "Poincaré-type inequality" for the tree comparison `ch05:tree-comparison`.

## Corrections applied

| class | count | lines |
|---|---|---|
| ERROR | 2 | 5:1293, 5:1336 |
| TERM | 1 | 4:209 |
| MISMATCH | 1 | 5:1234 |
| LANGUAGE, LEFTOVER, DICTIONARY, MINOR | 0 | |

Four lines were edited in all, each in place: one in chapter 4 and three in chapter 5.

## Cross-chapter mismatches not fixed

| object | my files | elsewhere |
|---|---|---|
| set of links an expression is built from | 4:505–506 "declared support" / "support of the expression" | "link support" (6:453 ff., 11, 11E, 13sb, 18gq). This may be a different set (6:459 includes the averaging operation's links); do not merge without the author. "stencil" remains at 10:80, 11E:163, 17m:119 |
| diagonal subsequence | 5:719 "diagonal extraction" | 10:846, 14:225, 17m:446, 17t:139, 19:89 "diagonal subsequence" |
| `W_F` | 5:1151, 1234, 1311 "in the block axial gauge" | 17c:49 "forest representative"; 6:953 "linearized critical configuration" (from the leads, not rechecked) |
| pull-back | 5:920 "pull-back under the parent map" (`rep V`) | 7:1083–1151 and chapter 17 use "pull-back" for composition with the critical configuration (lead, dictionary part 4) |
| dependence set | 4:459 (definition) | "full dependence set" at reading-guide:28, 6, 9, 10, 17m (from round 2) |
| quadratic hypothesis | 5:1058 (definition) | "quadratic coefficient condition" at 6:140, 380 (from round 2) |
| step, penalty parameter | 4:5 "called a step"; 4:226 `\emph{penalty parameter}` | defined earlier at reading-guide:22 and 1:409 / MT:12. The book has two defining sentences for each |
| block axial chart | 5:930 (defined), 1061, 1078, 1289, 1304 for the chart itself (correct) | 11R:247 "block axial charts" (correct use) |

## Leftover house words

Grep of both files, with labels, references and citations removed:
- "physical" at 5:97 ("physical quadratic exponent"), 5:520 ("physical kernels") and 5:1085 ("physical coordinates"). These lines are untouched, "physical" is not in the "Book-wide word choices" table, and the senses are position-space or unscaled. Listed under rule (f), not changed.
- "noise" at 5:377–399, 418, 549, 775–783: the entries *noise* and *accumulated noise* say "unchanged"/acceptable.
- "unit" at 4:16 ("unit lattice", Bałaban's) and 5:768–769 ("unit complex numbers", "unit phase"): ordinary use.
- "weight": defined terms (*averaging weight*, *probability weight*) or weighted norms. Ordinary use.
- "mixed coordinates" at 4:354: ordinary use.
- "row" at 5:609, 624, 882, 996, 1346: matrix rows and row sums. Ordinary use.
- "transport(ed)" at 4:497, 502: *transported curvature*, the chapter 2 term.
- "lift(s)" at 4:300, 399, 628, 641; 5:1042: periodic or coordinate lifts. Ordinary use.
- "suffix" at 5:379, 384 occurs only in `f_{\rm suffix}`, which is math.
- "the background" at 5:1222, 1287: ordinary use.
- "frame", "tag", "predictor", "actual", "stationary", "connector" occur only in labels. "stationary" also stands at 5:20 ("a stationary point"), which is ordinary use.

Not found in prose: "block average", "cutoff failure", "tree gauge", "level", "block transformation", "reset", "marked", "unmarked", "heat", "ground", "label", "kill", "history".

Replaced in this round: none. The leftovers were already handled in rounds 1 and 2.

## Leads

- (a) 4:209 "of an index": verified and corrected (see Findings).
- (b) 5:1234 "block axial chart" against "block axial gauge": verified and corrected. 9s:189 now also reads "gauge".
- (c) 5:719 "diagonal extraction": the line is untouched and has no table word, so I listed it and did not change it.
- (d) 4:506 "support of the expression" against "link support": I did not identify the two; listed.
- (e) 5:1019: the present wording is mathematically correct (the per-patch sum at 4:371–374, which holds on both branches). Left for the author.
- Dictionary-part-3 lead on "ℒ: β-independent quadratic term (4:525; 6:170) / inherited loop action (9:26)": these are not two names. 7:237 defines "the β-independent quadratic term of the path action, called the inherited loop action". At 4:525 the term is written `Σ A_i^{(2)}`, the same object. Nothing to do.
- Dictionary-part-4 lead on "pull-back" with two senses (5:920): listed above.
- Dictionary-part-4 lead on "representation data (ch. 4) / local representation (ch. 11) / presentation (11R)": it concerns other files. 4:550 is the definition.

## Assessment of earlier corrections

- Round-1 fixer, 5:1019: an equation reference was replaced and "on either branch" added. It is correct but it was not a vocabulary change; see (e).
- Round 1/2: `$\alpha$` was inserted after "index" at 5:1293 and 5:1336 by the conversion, and neither review caught it. It conflicts with the chapter's scalar `α` (5:495, 815). Corrected now.
- Round 2, 5:986 "transporter of Chapter 4": correct.
- Round 2, 5:581/582/599 "zero alias": correct.
- Round 2, 5:861 "integral maps of a step with insertions": correct.
- Round 2, 4:36 duplicate definition removed and 4:497/502 "transported curvature" restored: correct.
- Round 2, 5:20 and 5:937 citations added: the keys exist and render.
- Harmonisation: no wrong change was found in these files.

## For the author

1. 5:1019: keep the lemma reference with "on either branch", or restore `\eqref{ch04:frame-first-power}`.
2. 4:505–506: choose one name for the set an expression is built from, and decide whether it is chapter 6's "link support" (probably not: 6:459 is larger).
3. 5:719 "diagonal extraction" against "diagonal subsequence" elsewhere.
4. 4:189 "the first of its two branches": consider "its minimizing branch".
5. "physical" at 5:97, 520, 1085, on untouched lines.
6. The duplicate defining sentences for *step* (reading-guide:22, 4:5) and *penalty parameter* (1:409, 4:226).
7. Items 2–4 of the round-2 "For the author" still stand: whether to keep the formulas added by the conversion; "macro-box" against the dictionary's "enlarged block"; four names for `ch05:tree-comparison` on unchanged lines (945, 1290, 1306, 1319).

## Checks

- Line counts: `git show HEAD:<path> | wc -l` gives 677 and 1388; the working files have 677 and 1388.
- `git diff --stat` against HEAD: 04-blocking.tex 1 line, 05-gaussian.tex 3 lines.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-t2 monograph.tex`: completed with exit 0. The log has 0 "undefined", 0 "Citation" and 0 "Overfull".
- Rendered text (pypdf extraction): the four edited sentences appear as intended. The chapter 5 sentence reads "…whereas W_F is its representative in the block axial gauge."

## Not checked

- Bałaban's papers themselves: statements about them were compared with the dictionary's *Literature* lines only.
- Rendered pages were checked by text extraction only, not visually.
- Other chapters were searched by keyword only and not edited. The 17c and 6:953 names for `W_F` were taken from the leads.
- The mathematics of unchanged lines, and `figures/block-paths.tex`.
