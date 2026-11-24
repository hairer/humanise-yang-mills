# Review and correction: main theorem, reading guide, chapters 1, 2 (with 2e), 3

Files (worktree /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/): `main-theorem.tex` (MT), `reading-guide.tex` (RG), `chapters/01-lattice.tex` (1), `chapters/02-observables.tex` (2), `chapters/02-equation-section.tex` (2e), `chapters/03-maxwell.tex` (3). Every changed line of the six word-diffs was read before the editors' reports. Line numbers are those of the files (unchanged by the edit).

## Review findings

Classes: ERROR, LANGUAGE, DICTIONARY, TERM, MISMATCH, MINOR. "Committed" = HEAD.

### The main theorem: statement compared word by word (MT:10–48)

The statement differs from the committed one in exactly two places; everything else in lines 10–48 is identical.

| line | committed | edited | judgment |
|---|---|---|---|
| MT:12 | "a positive penalty parameter for the block transformation," | "… for the renormalization transformation," | same object (table: one block transformation = renormalization transformation / step). Mathematically identical. Kept. |
| MT:27 | "They contain the identity and" | "They contain the identity field and" | same object (the constant field); the term *identity field* is defined only at 2:80, so it is used here before its definition. Mathematically identical. Kept; see "Left for the author". |

Not changed inside the statement, although other files now differ: MT:14 "admissible physical periods" (chapter 1 now says "periods … in continuum units"). Outside the statement: MT:50 (pointer for "phase", correct: 15:8–9, 15:136, label `ch15:characters` exists), MT:63 (hyphen), MT:88–89 ("across coincident points", as MT:46 already said). No problem found.

### Problems

| # | where | class | committed | edited | problem | corrected text |
|---|---|---|---|---|---|---|
| 1 | RG:32–35 | ERROR (meaning shifted) | "one scale schedule must satisfy all fixed finite requirements. It is chosen slowly enough that each stage's constants can be controlled before the next set of requirements is introduced." | "the choices of Chapter 10 must satisfy all fixed finite requirements. The stages (lists of orders, exponents, widths and bounds, Section …) are introduced slowly enough that each stage's constants …" | "one" was lost (the point of the sentence is that a single schedule serves all requirements); the subject of "slowly" changed from the schedule to the stages. The edited sentence is compatible with 10:118–134 (`J(m)` increases by at most one, minimum starting scales `b_j`), but it is not the committed statement. | "one scale schedule (the choices of Chapter~\ref{ch10:trajectory}) must satisfy all fixed finite requirements. It is chosen slowly enough that each stage's constants can be controlled before the next set of requirements is introduced (a stage specifies finitely many orders, exponents, widths and bounds, Section~\ref{ch10:choices})." The gloss of *stage* repeats 10:25–26 and is now a parenthesis after the sentence. "scale schedule" (house word, *schedule* 2) therefore stays once: see "Left for the author". |
| 2 | 1:452–453 | MISMATCH / weakened | "a stationary background and its Gaussian fluctuations organize the local integral" | "a background field and the Gaussian fluctuation field about it (Chapter 5) organize …" | "stationary" dropped: the background is the critical configuration (table), as RG:23 says ("a background field (the critical configuration of Chapter 5)"). | "a background field (a critical configuration, Chapter~\ref{ch05:gaussian}) and the Gaussian fluctuation field about it organize the local integral." |
| 3 | 1:490 | LANGUAGE | "Uniform estimates in the physical volume then permit" | "Estimates uniform in this volume then permit" | "this volume" points back to "a fixed volume" of 1:488; uniformity is in the volume as a parameter. | "Estimates uniform in the volume then permit one" |
| 4 | 2:50–51 | MISMATCH / DICTIONARY | "we also call its scaling dimension its \emph{weight}." | unchanged | *weight* 1 (D) is replaced by *scaling dimension*; chapter 3 no longer uses or repeats the word (3:168–169), and chapter 2 never uses it again, so the definition defined a word with no use in chapters 1–3. | "For a homogeneous polynomial in jet coordinates, its scaling dimension is the common scaling dimension of its monomials." (the name is removed; the sentence keeps what the committed one presupposed). Chapters 7, 9, 11 still use "weight" in this sense (7:350–357, 609, 1026; 9:211–215; 11:407, 411, 1288, 1848) and must convert it. |
| 5 | 2:171 | TERM (repeated definition) | "If $\gamma$ is a lattice path from the origin to $z$, its transported" | "… is a contour from the origin to $z$, that is, a lattice path along which the link variables are multiplied, with contour variable $U_\gamma$, its transported" | repeats the definition now standing at 1:78–80 (and at 4:36). | "If $\gamma$ is a contour (Section~\ref{ch01:wilson-section}) from the origin to $z$, its transported" |
| 6 | 1:207 | TERM (second definition-style emphasis) | "integrating out one scale goes from $m+1$ to $m$" | "integrating out one scale, in one \emph{step} of the construction (Chapter 4), goes …" | *step* is defined at 4:5 with its first-use sentence; an emphasized "step" here reads as a second definition. | "in one step (the renormalization transformation of Chapter~\ref{ch04:blocking})," |
| 7 | 1:409 | TERM (same) | "A fixed parameter $b>0$ specifies the soft constraint in the block transformation;" | "A fixed \emph{penalty parameter} $b>0$ specifies the penalty term in the renormalization transformation (Section …);" | the term is already used at MT:12 and has its first-use sentence at 4:226; emphasis removed, forward reference kept. | "A fixed penalty parameter $b>0$ specifies …" |
| 8 | 2e:253 | TERM (same) | "along the actual renormalization history," | "… history (a \emph{history} is defined in Chapter 11)," | forward reference, not a definition; emphasis removed. Deleting "actual" is prescribed (*actual* 1). | "(a history is defined in Chapter~\ref{ch11:insertions})," |
| 9 | 3:830 | DICTIONARY (noted, kept) | "This proves detection at bounded jet order." | "This proves the separating property at bounded jet order." | *detection* has basis I at this line; but the entry *separating family* (basis R) names 3:830 for this replacement, and the sentence says what the paragraph proves (`𝒩_{b_j}` contains no nonzero invariant polynomial of jet order ≤ j). Kept. | — |
| 10 | 3:146–147, 832, 879, 914, 1016 | MISMATCH (not corrected) | "collisions", "collision diagonals" | unchanged | MT, RG and chapter 1 now say "coincident points" / "the diagonals"; chapter 3 keeps "collision" because the entry gives basis I for the chapter 3 lines. 146–147 and 914 are plainly the chapter 1 sense. Not changed (rule: no basis-I proposal); for the author. | — |
| 11 | 2e:88, 135 against 2:167, 222 | MINOR (not corrected) | "base point $z$ of the plaquette", "integer base points" | "initial point $z$", "integer initial points" | correct and consistent with chapter 4 (*initial point* of a contour) and with 2e:124 ("initial vertex of $e$"); 2:167, 222 still say "plaquette based at $z$". For the author. | — |
| 12 | 2e:131–132 | MINOR (kept) | "Fix a layer $j$. … restricted to jets through layer $j$" | "Fix a degree index $j$. … restricted to jets through the component of degree index $j$" | parses; heavier than the original. "degree index" is the word of 2:236–237. Kept. | — |
| 13 | RG:73–74 | MINOR (kept) | "needs a signed replacement estimate for a whole cluster, uniform under repeated copies." | "needs an estimate of the replacement error of a whole cluster of nearby fields, with its sign kept and with a constant independent of the number of reflected copies." | every piece is a dictionary phrase (*signed* 2, *replacement*, *cluster* 2, *uniform in the number of reflected copies*, all R); "with its sign kept" could attach to "estimate" or to "error". The longest rewording after RG:32–35. Kept; for the author. | — |

### Checked and found correct (the points of the assignment)

- **contour / contour variable / holonomy.** Defined once at 1:78–80 (the committed "A path holonomy is the ordered product …" reworded; no claim about the literature). 1:126–127, 142, 148, 448 use the three words in the defined senses ("holonomy" only for closed contours). Gloss at 2:171 removed (finding 5). The clause at 4:36 is now the repetition: see "Left for the author".
- **identity field.** Defined at 2:79–80. Used earlier at MT:27 only (inside the statement); not in RG, not in chapter 1. Later uses (2:192, 259–260, 281, 400; 2e:227, 236; 3:126, 190, 925, 943, 1032) agree.
- **scale / scale index, the reversed index.** Stated once, at 1:206. Committed chapter 4 does not state the reversal (4:13–16 says only that a step is not followed by a rescaling to the unit lattice; 4:652 uses "scale index"). Nothing to remove anywhere.
- **`\cite{Balaban1987RG}` at 1:206.** The key exists (references.bib:29; CMP 109, 249–301, the dictionary's B87). The sentence "in [B87] the index runs the other way, from zero on the finest lattice" is covered by the *Literature* line of *level* ("Bałaban's and Dimock's `k = 0` is the finest (bare) lattice and `k` increases towards the unit lattice", B87 p. 256) and by the table row. It claims no more. Chapter 1 did not cite the paper before (editors' rule 5 against rule 10); kept.
- **weight.** See finding 4. 3:168–169 ("As in Definition ch02:labels, scaling dimensions add in products of these coordinates") restates 3:96–97 and 2:49; correct. No "weight" in sense 1 remains in chapters 1–3 (3:311 "weighted by" is ordinary; label `ch03:weight` untouched).
- **"test link variables"** (2:103, 118, 150). Defined at 2:118; correct for `U(h,J)(y,μ)` (one matrix per link; "holonomy" is now reserved for closed contours); no other use of the phrase in the book. Kept; for the author.
- **"moves"** for "transfers" (2e:220): ordinary verb, avoids the table word *transfer*. Kept.
- **"exponentially small factor"** (1:456–457): same meaning as "exponential penalty"; avoids the table word *penalty*; "small factor" is the papers' usage (*Literature* of *gain*). Kept.
- **"jet functional"** (3:751; 883, 939, 956, 966, 973–974, 985, 995): defined at first use, the short form of the proposal "linear functional on jets" (*probe* 1, R); no other use in the book. At 939 it is said of scalar solution jets ("scalar order-$j$ jet functionals"), which the wording carries. Kept.
- **"separating family" without "finite"** (3:482): correct. The definition covers both statements that carry the name: Corollary 3:484–495 (a finite family, the title says "finite separating families") and Proposition 3:806–809 (the family of all separated words with `P_i ∈ M_D^Max`, not finite). With "finite" the definition would exclude the second. The dictionary's *Meaning* ("A finite family …") should be amended.
- **"supplies" → "gives"** (3:6, 303, 711) and **"slot" → "argument"** (3:292, 293, 1003): the three "supplies" are the entry's general sense ("gives"); the three "slot" are argument positions (*slot* 2). Correct although chapter 3 is missing from the two line lists; the lists should be completed.
- **"physical" → "in continuum units", 16 places** (RG:5, 60; 1:11, 174, 202, 204, 206, 209, 222, 224–225, 227, 329–330, 350, 488, 490): each is sense 1 of *physical* (volume, distance, period, spacing, side, position, support diameter, loop size, volume element). None is sense 2 (factor `a_N^{-d}`), 3 (interacting) or 4–9. Left unconverted: MT:14 (statement), 1:171 (section title "Physical scales and lattice symmetries"), 2:11 "physical scale", 2:401 "physical normalization" (sense 2, not sense 1; correctly not touched).
- **Sentence repairs in chapter 3** (non-vocabulary changes): 3:546–547 "flux convention \eqref{ch03:flux} used below" (label exists, 3:666); 3:576 "quantitative convergence of the rescaled interacting fields to free fields" (entry *moving comparison fields*, basis S, proposal "… to their free limits"); 3:431–432, 462, 470 direct sums written out (consistent with (ch03:triangular) and Proposition ch03:jet-positive). Correct.
- **Other non-vocabulary additions**, all correct: 1:202 gloss of "periods" inside Definition ch01:scales; 1:365 "the diagonals $x_i=x_j$, $i\ne j$"; 1:371 gloss of "lattice family" inside Definition ch01:ordered-limit (`μ_{N,p}` 1:339, `I_{N,p}` 1:333); 2:339 "$\chi(U_\square)\le t$" for "has distance from the identity at most $t$" (2:310–312); 2e:41 the name "exterior function" inside Theorem ch02:equation-adapted; 3:705 definition of "spectators" inside Proposition ch03:free-ward.
- Forward references resolve: `ch04:blocking`, `ch04:kernel-section`, `ch04:density-coordinates`, `ch05:gaussian`, `ch10:trajectory`, `ch10:choices`, `ch11:insertions`, `ch15:characters`, `ch01:wilson-section`.

Counts: ERROR 1, LANGUAGE 1, DICTIONARY 1 (kept), TERM 4, MISMATCH 3 (two corrected, one left), MINOR 3 (kept).

## Corrections applied

Twelve lines, all within lines:

- RG:32, 33, 35 (finding 1).
- 1:207 (6), 1:409 (7), 1:452–453 (2), 1:490 (3).
- 2:50–51 (4), 2:171 (5).
- 2e:253 (8).
- MT and chapter 3: none.

## Left for the author

1. **RG:32 "scale schedule"** stays, with the dictionary phrase in parentheses. If the house word is to go, the two sentences need the author's wording (the subject of "It is chosen slowly enough").
2. **RG:22 "\emph{step}"** and the definition at 4:5 both emphasize the word; the reading guide comes first. RG:58 still has "One common trajectory" and "the nonlinear step" (chapter titles).
3. **MT:27 "identity field"** is used before 2:80. **MT:14 "admissible physical periods"** differs from chapter 1's "periods … in continuum units" (the editor left the statement alone).
4. **Titles**: 1:68 "Links, contour variables and the Wilson measure" (committed: "holonomies"); 1:171 "Physical scales and lattice symmetries" (unchanged); 2:103 "Test link variables and Taylor normalization"; 3:591 "One-dimensionality of the space of conserved tensors" (committed: "Conserved tensor line").
5. **"test link variables"**, **"initial point" of a plaquette** (2e:88, 135, against "plaquette based at $z$" at 2:167, 222), **"jet functional"**, **"exterior function"**: the editors' own short terms, all correct; the choice of words is the author's.
6. **2:50–51**: the name "weight" was removed (finding 4); the replacement sentence is mine.
7. **2e:254 "all spectators"**: used before the definition of *spectators* at 3:705; the dictionary assigns it to *exterior function* (sense 2, R), the chapter 2 editor doubted this. Not changed.
8. **collision** in chapter 3 (finding 10).
9. **RG:73–74** (finding 13).
10. **For chapters 4–5 (not edited)**: 4:36 "a \emph{contour} is a lattice path along which the link variables are multiplied, and its \emph{contour variable} is their ordered product" repeats 1:78–80 and should become a plain use or a back reference to Section `ch01:wilson-section`. 4:13–16 needs no change for the scale index (the reversal is at 1:206 only). 4:226 remains the place of the first-use sentence for the penalty parameter; MT:12 and 1:409 use the word before it.
11. **Dictionary**: *separating family* should not say "finite"; the line lists of *supplies* and *slot* 2 lack chapter 3; *detection* gives basis I at 3:830 while *separating family* prescribes the replacement there.

## Words this file introduces that other chapters may also define

- 1: *contour*, *contour variable*, *holonomy* (1:78–80; also 4:36); *scale*, *scale index* with the reversal (1:206); *lattice family* (1:371); *reflection planes of the tiling* (1:284; "reflection plane" also at 13:293, 14:855 in the ordinary sense); "the diagonals" (1:365); *position in continuum units* (1:209).
- 2: *identity field* (2:80; used from chapter 3 to 19 for "unit"); *filtration index* (2:96; "tag"/"normalization index" at 11:2307); *bidegree* (2:79); *factor count* (2:53); *test link variables* (2:118).
- 2e: *exterior function* (2e:41); *base point* `o` of a local function (2e:39; chapter 4 has *base point* of a localized term); *history*, forward reference only (2e:253; defined 11:18–19).
- 3: *separating family* (3:482; chapters 11, 11E, 13, 14, 15, 19 use it); *spectators* (3:705; chapters 11–19); *jet functional* (3:751; "probe" has other senses in 17m and 18); *on-shell polynomial space*; *zero-mean*; *weighted Euler operator* (3:689).
- Removed and to be converted elsewhere: *weight* = scaling dimension (chapters 7, 9, 11).

## Checks

- Line counts (file / HEAD): main-theorem.tex 102/102; reading-guide.tex 84/84; 01-lattice.tex 503/503; 02-observables.tex 452/452; 02-equation-section.tex 254/254; 03-maxwell.tex 1088/1088.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1215 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-b1abc monograph.tex`: exit 0, run to completion. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build included the other editors' files (chapters 8, 9s) as they were at that moment.
- Edited only the six files; nothing committed, staged or reverted; references.bib not touched.

## Not checked

- The rendered PDF pages were not inspected.
- The papers themselves: the sentence at 1:206 was checked against the dictionary's *Literature* lines only.
- Unchanged lines of the six files were not reviewed for house words the editors missed, beyond the greps for "physical", "collision", "sector", "seam", "supply", "weight", "probe", "tower", "spectator".
- Whether "scale schedule … chosen slowly enough" (RG:32–33) is the author's intended sense of 10:118–134; the committed wording was restored, not interpreted.
- Chapters 6–9 as converted in parallel were not compared with these files.
