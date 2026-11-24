# Vocabulary applied to main-theorem.tex (MT), reading-guide.tex (RG) and chapters/01-lattice.tex (1)

Worktree /Users/mgubi/ym-terminology, branch `claude/v3-terminology-dictionary`. 72 lines changed (MT 6, RG 16, chapter 1: 50). Nothing committed or staged. All edits were made by a script that replaces a substring inside one numbered line and refuses unless the substring occurs exactly once in that line (scratchpad/decisions/b1a_edit.py and b1a_edit2.py).

## Changes

### main-theorem.tex

| line | before | after | decision or entry |
|---|---|---|---|
| 12 | `penalty parameter for the block transformation,` | `penalty parameter for the renormalization transformation,` | table: step / renormalization transformation |
| 27 | `They contain the identity and` | `They contain the identity field and` | table: identity field (Appendix B row lists MT:27) |
| 50 | `within each phase. Uniqueness of` | `within each phase, a phase being a character of a commutative operator algebra (Section~\ref{ch15:characters}). Uniqueness of` | *phase* 1 (D): pointer to chapter 15 at first use; wording of 15:8–9. Placed outside the statement of the theorem |
| 63 | `renormalization group trajectory` | `renormalization-group trajectory` | *trajectory* 1 (R); spelling of 4:20 |
| 88–89 | `extension across the / collision diagonals is` | `extension across / coincident points is` | *collision* (R); the wording of MT:46 |

### reading-guide.tex

| line | before | after | decision or entry |
|---|---|---|---|
| 5 | `while the physical volume is held fixed` | `while the volume in continuum units is held fixed` | *physical* 1 (R) |
| 17 | `by transporting all coefficients together` | `by transferring all coefficients together` | table: transfer (*transport* 3; basis I at this line, see Inconsistencies) |
| 18 | `by equality of all separated correlation responses.` | `by equality of all their separated correlations with all other fields.` | *one-slot response*, *spectator responses* (R): the wording proposed for RG:18 |
| 22 | `is the block step. Its` | `is the renormalization transformation, or \emph{step}, of Chapter~\ref{ch04:blocking}. Its` | table: step; forward reference only (first-use sentence stands at 4:5, 4:16) |
| 23 | `and a stationary background.` | `and a background field (the critical configuration of Chapter~\ref{ch05:gaussian}).` | *stationary background* (adopted 24 Nov.: background field); table: critical configuration; forward reference (sentence stands at 5:20) |
| 29 | `local gauge choices` | `local gauge transformations` | *frame* (R), as chapters 4–5 |
| 32 | `Once the block estimates are available, one scale schedule must satisfy` | `Once the estimates for one step are available, the choices of Chapter~\ref{ch10:trajectory} must satisfy` | table: step; *schedule* 2 (R) |
| 33 | `It is chosen slowly enough that each` | `The stages (lists of orders, exponents, widths and bounds, Section~\ref{ch10:choices}) are introduced slowly enough that each` | *schedule* 2; table: stage, with a pointer to its definition (10:25) |
| 35 | `A common trajectory then determines the couplings,` | `The resulting construction, the same for all ultraviolet cutoffs, then determines the couplings,` | *trajectory* 2 (R), *common* 3 (R) |
| 36 | `for the entire Wilson family.` | `for the entire family of Wilson measures.` | *common family*, *same-family* (R) |
| 55 | `local labels` | `polynomial labels` | *polynomial label* (D), explicit for RG:55 |
| 60 | `at fixed physical volume.` | `at fixed volume in continuum units.` | *physical* 1 (R) |
| 64 | `specified contact extensions,` | `specified extensions to coincident points,` | *contact* 1 (R) |
| 73–74 | `needs a signed / replacement estimate for a whole cluster, uniform under repeated copies.` | `needs an estimate of the / replacement error of a whole cluster of nearby fields, with its sign kept and with a constant independent of the number of reflected copies.` | *signed* 2 (R), *replacement* (keep), *cluster* 2 (keep, glossed), *uniform in the number of reflected copies* (R) |
| 76 | `across collision diagonals,` | `across coincident points,` | *collision* (R) |

### chapters/01-lattice.tex

| line | before | after | decision or entry |
|---|---|---|---|
| 11 | `At a fixed physical volume,` | `At a fixed volume in continuum units,` | *physical* 1 (R) |
| 68 | `\section{Links, holonomies and the Wilson measure}` | `\section{Links, contour variables and the Wilson measure}` | table: contour variable; holonomy for closed contours only |
| 78–80 | `A path holonomy is the ordered / product of its link variables, with this inverse convention on backward / steps. We use` | `A \emph{contour} is a lattice path along which the link variables are multiplied; its \emph{contour variable} is the ordered / product … convention on links traversed / backward; for a closed contour it is called a \emph{holonomy}. We use` | table: contour, contour variable, holonomy; *holonomy* names this line. "backward steps" removed because *step* is now a term |
| 126 | `is a path from $y$ to $z$, its holonomy transforms as` | `is a contour from $y$ to $z$, its contour variable transforms as` | table (open contour) |
| 127 | `Thus a closed holonomy transforms by` | `Thus a holonomy transforms by` | table (a holonomy is closed by definition) |
| 149 | `will be specified by bounds on the gauge-invariant` | `will be specified by a regularity condition (Section~\ref{ch04:density-coordinates}), a bound on the gauge-invariant` | table: regularity condition; forward reference (sentence stands at 4:428) |
| 174 | `distinct from physical distances.` | `distinct from distances in continuum units.` | *physical* 1 |
| 202 | `increasing physical periods $R_p$, each` | `increasing periods $R_p$ (the side lengths of the tori in continuum units), each` | *physical* 1; *period* ("saying once that it is the side length of the torus") |
| 203 | `At scale $m$ and` | `At scale index $m$ and` | table: scale index |
| 204 | `and physical spacing $a_m$.` | `and spacing $a_m$ in continuum units.` | *physical* 1 |
| 206 | `Its physical side is exactly $a_ms_{m,p}=R_p$. Increasing` | `Its side in continuum units is exactly $a_ms_{m,p}=R_p$. We call $a_m$ the \emph{scale} and $m$ the \emph{scale index}; in~\cite{Balaban1987RG} the index runs the other way, from zero on the finest lattice. Increasing` | *physical* 1; table: scale, scale index, first-use sentence |
| 207 | `integrating out one scale goes from` | `integrating out one scale, in one \emph{step} of the construction (Chapter~\ref{ch04:blocking}), goes from` | table: step; forward reference |
| 208 | `the finest scale in a finite renormalization trajectory.` | `the finest scale index in a finite renormalization-group trajectory.` | table: scale index; *trajectory* 1 |
| 209 | `At cutoff $N$, a lattice site has physical placement` | `At ultraviolet cutoff $N$, a lattice site has the position in continuum units` | *cutoff* 1 (R); *placement* 1 (D) |
| 222 | `the same physical position.` | `the same position in continuum units.` | *physical* 1 |
| 224–225 | `its physical / support has diameter at most $a_N\operatorname{diam}(\Sigma)$. Such an` | `its / support has diameter at most $a_N\operatorname{diam}(\Sigma)$ in continuum units. Such an` | *physical* 1 |
| 227 | `of fixed physical size,` | `of fixed size in continuum units,` | *physical* 1 |
| 244, 247 | `positive sectors`; `in the indicated sector.` | `positive halves`; `in the indicated half.` | *positive sector*, *sector* 2 (D) |
| 284 | `without observables on seams.` | `without observables on the reflection planes of the tiling.` | *seam* (R/S) |
| 287 | `reads no seam links.` | `reads no link meeting a reflection plane.` | *seam* |
| 317 | `across the strip seams.` | `across the reflection planes bounding the strips.` | *seam* |
| 323 | `seams and divisibility.` | `reflection planes and divisibility.` | *seam* |
| 329–330 | `the physical side of the / torus, as in` | `the side of the / torus, both in continuum units, as in` | *physical* 1 (the form of 4:13–14) |
| 350 | `is the physical volume element` | `is the volume element in continuum units` | *physical* 1 |
| 365 | `from the collision diagonals.` | `from the diagonals $x_i=x_j$, $i\ne j$.` | *collision* (R): "the diagonals" for the set |
| 371 | `A lattice family converges` | `A lattice family (the measures $\mu_{N,p}$ and the insertions $I_{N,p}$ above) converges` | *lattice family* (R): define once; the content is what (ch01:lattice-smear) uses |
| 379 | `and the retained volumes satisfy` | `and the volumes $P(k)$ satisfy` | *retained volumes* (R) |
| 387 | `uses every cutoff $N$` | `uses every ultraviolet cutoff $N$` | *cutoff* 1 (R) |
| 393 | `extract one refinement that` | `extract one subsequence that` | *refinement* (R) |
| 408 | `a hypothesis that supplies the` | `a hypothesis that gives the` | *supplies* (R) |
| 409 | `parameter $b>0$ specifies the soft constraint in the block transformation;` | `\emph{penalty parameter} $b>0$ specifies the penalty term in the renormalization transformation (Section~\ref{ch04:kernel-section});` | table: penalty parameter `b`, step; *soft constraint* (R); forward reference (sentence stands at 4:226) |
| 415 | `decomposition into phases,` | `decomposition into phases (characters of a commutative operator algebra, Section~\ref{ch15:characters}),` | *phase* 1 (D): pointer at first use in chapter 1 |
| 420 | `the block parameter $b$` | `the penalty parameter $b$` | table |
| 426 | `at collisions.` | `at coincident points.` | *collision* (R) |
| 440 | `An exact block transformation integrates` | `An exact renormalization transformation integrates` | table |
| 452–453 | `a stationary background and its Gaussian / fluctuations organize` | `a background field and the Gaussian / fluctuation field about it (Chapter~\ref{ch05:gaussian}) organize` | *stationary background*; table: fluctuation field; forward reference |
| 456–457 | `positive action supplies an exponential / penalty. Connected` | `positive action gives an exponentially / small factor. Connected` | *supplies* (R); "penalty" removed because *penalty term / parameter* is now a different, technical object ("small factor" is the word of the *Literature* line of *gain*) |
| 473 | `A transfer matrix records` | `The matrix of one step records` | *transfer matrix* (R): "matrix of the block step" |
| 477 | `their collision diagonals.` | `the diagonals.` | *collision* |
| 488 | `At a fixed physical volume, stability of the renormalization` | `At a fixed volume in continuum units, stability of the renormalization-group` | *physical* 1; *trajectory* 1 |
| 490–491 | `Uniform estimates in the physical volume then permit one common / infinite-volume subsequence, as` | `Estimates uniform in this volume then permit one / infinite-volume subsequence for all correlations, as` | *physical* 1; *common* 2 (R: "one … for all") |
| 503 | `common family,` | `single lattice family,` | *common* 2, *lattice family* |

No occurrence of "actual" in the three files. Appendix D proposes no sentence repair for them.

## First-use sentences added

1. 1:206 (*scale*, *scale index*; table row 1): "We call $a_m$ the \emph{scale} and $m$ the \emph{scale index}; in~\cite{Balaban1987RG} the index runs the other way, from zero on the finest lattice." Rests on the table ("Bałaban, B87 p. 256. His index `k` runs the other way: `k = 0` is the finest lattice"); B87 is `Balaban1987RG` in references.bib. Chapter 1 did not cite this paper before: brief item 5 forbids a new key, item 10 requires one; item 10 was followed. Remove the clause after the semicolon if item 5 is to prevail. (The chapter 4 report had left this sentence to chapter 1.)
2. 1:78–80 (*contour*, *contour variable*, *holonomy*): "A \emph{contour} is a lattice path along which the link variables are multiplied; its \emph{contour variable} is the ordered product of its link variables, with this inverse convention on links traversed backward; for a closed contour it is called a \emph{holonomy}." This is the text's own definition of "path holonomy" reworded, no claim about the literature. It duplicates the clause at 4:36; one of the two can now be shortened to a reference.

Forward references only (no sentence about Bałaban): RG:22 (step, Chapter 4), RG:23 (critical configuration, Chapter 5), RG:32–33 (choices and stages, Chapter 10), MT:50 and 1:415 (phase, Section ch15:characters), 1:149 (regularity condition), 1:207 (step), 1:409 (penalty parameter and penalty term, Section ch04:kernel-section), 1:453 (Chapter 5).

## Short terms introduced

| term | defining sentence | line |
|---|---|---|
| *reflection planes* (of the tiling), for "seams"; the proposal for "seam links", "links meeting a reflection plane", is used once | "without observables on the reflection planes of the tiling"; the planes are those "at multiples of $\ell$" of 1:288 | 1:284; used 287, 317, 323 |
| *lattice family* (kept, now glossed; the proposal is a ten-word description) | "A lattice family (the measures $\mu_{N,p}$ and the insertions $I_{N,p}$ above) converges to kernels …" | 1:371; used 391, 398, 503 |
| *stage* (table word; gloss at first use in the book) | "The stages (lists of orders, exponents, widths and bounds, Section~\ref{ch10:choices}) are introduced slowly enough …" | RG:33 |

## Dictionary words applied that are not in the table of word choices

| word replaced | word used | occurrences |
|---|---|---|
| physical (volume, distance, period, spacing, side, position, support, size, volume element) (*physical* 1, R) | in continuum units | 16: RG:5, 60; 1:11, 174, 202, 204, 206, 222, 224–225, 227, 329–330, 350, 488, 490 ("this volume"); with *placement* at 209 |
| physical placement (*placement* 1, D) | position in continuum units | 1 (1:209) |
| collision diagonals, collisions (*collision*, R) | coincident points; the diagonals | 6 (MT:89; RG:76; 1:365, 426, 477) |
| contact extensions (*contact* 1, R) | extensions to coincident points | 1 (RG:64) |
| seam, seam links, strip seams (*seam*, R/S) | reflection planes; link meeting a reflection plane | 4 (1:284, 287, 317, 323) |
| positive sector, sector (*positive sector*, D) | positive half, half | 2 (1:244, 247) |
| retained volumes (R) | the volumes `P(k)` | 1 (1:379) |
| refinement (R) | subsequence | 1 (1:393) |
| supplies (R) | gives | 2 (1:408, 456) |
| cutoff `N` (*cutoff* 1, R) | ultraviolet cutoff `N` | 2 (1:209, 387) |
| transfer matrix (R) | the matrix of one step | 1 (1:473) |
| common (sense 2, R) | one … for all; single | 2 (1:490–491, 503) |
| common trajectory, scale schedule (*trajectory* 2, *common* 3, *schedule* 2, R) | the choices of Chapter 10; the resulting construction, the same for all ultraviolet cutoffs | 2 (RG:32, 35) |
| Wilson family (*common family*, R) | family of Wilson measures | 1 (RG:36) |
| renormalization (group) trajectory (*trajectory* 1, R) | renormalization-group trajectory | 3 (MT:63; 1:208, 488) |
| correlation responses (*one-slot response*, *spectator responses*, R) | correlations with all other fields | 1 (RG:18) |
| signed; uniform under repeated copies (*signed* 2, *uniform in the number of reflected copies*, R) | with its sign kept; with a constant independent of the number of reflected copies | 1 each (RG:73–74) |
| local labels (*polynomial label*, D) | polynomial labels | 1 (RG:55) |
| local gauge choices (*frame*, R, as chapters 4–5) | local gauge transformations | 1 (RG:29) |
| exponential penalty (no entry; clash with the table word *penalty*) | exponentially small factor | 1 (1:456–457) |
| period (*period*: say once that it is the side length) | "periods $R_p$ (the side lengths of the tori in continuum units)" | 1 (1:202) |

Table words applied: renormalization transformation / step (MT:12; RG:22, 32; 1:207, 409, 440, 473); scale, scale index (1:203, 206, 208); penalty parameter `b`, penalty term (1:409, 420); contour, contour variable, holonomy (1:68, 78–80, 126, 127); background field, critical configuration, fluctuation field (RG:23; 1:452–453); regularity condition (1:149); identity field (MT:27); transfer (RG:17); stage (RG:33).

## Not changed, for the author

- **admissible physical periods** (MT:14–15), **admissible period** (MT:19): left exactly, as instructed. The dictionary records two notions (sense 1, the chosen periods `R_p = 4(M+p+1)` of 10:193–197, basis R/S; sense 2, a period whose box contains the support of the test function, 1:359–361, basis D/S) and the main theorem uses one adjective for both. For the same reason "physical" was not turned into "in continuum units" at MT:14, although it was everywhere else. 1:359–361 and 1:373, 385 ("admissible" for test functions) keep the defined word (*admissible* 3, "keep").
- **phase** (MT:34, 35, 41, 45, 50, 73–95; RG:47, 62; 1:415, 418, 499): kept (defined 15:8–9); pointers added at MT:50 and 1:415 only. The statement of the theorem (MT:32–36) itself has no pointer.
- **selected phase** (MT:91, 93): *selected* 7 proposes "the fixed phase `ξ_*`"; the symbol is not available in the front matter and "selected in Section …" is plain English. Left.
- **normalizations of local observables**, "normalized quantum field", "observable normalizations" (MT:15; RG:13, 16, 36): basis I, "keep … add a pointer to chapter 11". No pointer added inside the theorem; MT:64–65 already names Chapter 11.
- **positive action cost** (RG:26; *cost* 5 and *positive action cost*, basis I); **gain** (1:454, basis I); **defects** (1:457, basis I: "large-field regions"); **placements** (1:322, *placement* 2, basis I: "positions"); **reads** (1:287, basis I; kept as in chapter 4); **source locations** (RG:82, basis I); **local integral** (1:453, 459, basis I): not applied.
- **slot** (1:314): proposal "factors of the cyclic product", with the remark that a standard word is not certain. Left.
- **activity**, **activities** (RG:27, 29, 36): RG:27 "polymer activities" is the standard sense (keep). RG:29 and RG:36 may be sense 1 (localized terms and large-field activities, the "activity array" of 10:421) or sense 2; the sense cannot be told from the reading guide, so the word stays.
- **cutoffs** (RG:29, "the cutoffs and local gauge transformations used to define it"): smooth cutoffs or thresholds, sense unclear; left. "full cutoff limit" (MT:66), "cutoff-dependent" (1:336), "finite-cutoff" (1:464, 484), "the cutoffs" (1:488) are ordinary uses of sense 1; left.
- **regions of small curvature** (RG:24), **small curvature**, **small-curvature part** (1:445–452): descriptive, and 1:447–449 says what is meant; not replaced by "small-field region" (which 1:149 already uses, now with a pointer to the regularity condition).
- **nonlinear step** (RG:58): proposal *step* (basis I); the phrase already contains the agreed word and "nonlinear" marks a real contrast. Left. "Exact blocking" (RG:57, the title of chapter 4) and "exact" (1:440) left, as in chapter 4.
- **blocking** (RG:39; 1:473 "mix under blocking"), **block ratio** (1:217, 455, 463): no entry; the words of chapters 4–5.
- **centered blocks**, **centered-cell boundary** (1:183, 217; *centered* 2, R: "centered at `x₀`; symmetric"): ordinary geometric use, no single replacement fits; left.
- **transport**, **parallel transport**, **row transport** (1:80–81, 153–154): kept (standard; *row transport* "keep, defined").
- **oriented paths** (1:188), **loop** (1:143, 227): paths that are pulled back or described, not contours of a definition; left.
- **trajectory** alone (1:465, 467): short for the renormalization-group trajectory of 1:208; left.
- **steps** in the ordinary sense: MT:59 ("main steps of its proof"), 1:499 ("after these steps"). Left; the author may prefer "parts" now that *step* is a term.
- **label**, **local-observable labels**, **label list**, **field labels** (1:331, 393, 481; MT:26; RG:15, 43, 56): kept (*label* 1, *polynomial label*: keep).
- **insertion**, **separated**, **ordered convergence**, **parent map**, **stencil** (defined at 1:138), **strips**, **positive algebra**, **lift**, **mass-shell**, **reconstruction**, **slab operators**, **matching**, **logarithmic**: "keep".
- Symbols: `C_{\gLie}` against `C_G` of 7:15 (Appendix C) not touched.

## Inconsistencies noticed

- RG:18: three entries give two proposals for the same words: *correlation responses* and *response* 8 propose "the correlation functionals `L_{v,f}`", *one-slot response* and *spectator responses* propose "correlations with all other fields" (the first names RG:18 explicitly). The second was used; the symbol `L_{v,f}` is not available in the reading guide.
- RG:17: *transport* 3 gives basis I for this line, while the table row "transfer" covers it. The table was followed.
- RG:32–36: *schedule* 2 ("the choices of Chapter 10"), *trajectory* 2 ("the construction of Chapter 10") and *common* 3 ("cutoff-independent; the parameter sequence of Chapter 10") name overlapping things in one paragraph. "The choices of Chapter 10" was used at 32 and "the resulting construction, the same for all ultraviolet cutoffs" at 35. At 33 "It [the schedule] is chosen slowly enough" could not survive the loss of its subject; it became "The stages … are introduced slowly enough" (supported by the title of Section 10.2, "A slowly increasing stage schedule", and 10:133–134). This is the one place where a sentence was reworded beyond a word; please check it.
- *stationary background*: the table gives *critical configuration* for `ρ(v)` and the entry (24 Nov.) *background field*; both are now in RG:23 ("a background field (the critical configuration of Chapter 5)"), as at 5:7.
- *holonomy*: the entry says the product along an open contour is the contour variable "also where the text has 'holonomy'", and cites 1:78–79; applied. The definition of contour now stands at 1:78 and at 4:36.
- *step* and *penalty parameter*: the table asks for "renormalization transformation, called a step" and the delta-function remark at first use; the first uses in the book are RG:22 / 1:207 and MT:12 / 1:409, but the sentences stand in chapter 4 (4:5, 4:16, 4:226), as the brief prescribes. Here only forward references were added.
- *scale*: 1:203 uses "scale index" inside Definition ch01:scales, three lines before the term is introduced at 1:206 (a line could not be added inside the definition).
- *physical* 1 lists MT:14 among the lines to change; not done (see Not changed), so the main theorem says "physical periods" where chapter 1 now says "periods … in continuum units".
- *lattice family* proposes "measures, couplings and normalized observables"; the gloss at 1:371 names the measures `μ_{N,p}` (which contain the couplings) and the insertions `I_{N,p}`.

## Checks

- `wc -l`: main-theorem.tex 102 (HEAD 102); reading-guide.tex 84 (HEAD 84); chapters/01-lattice.tex 503 (HEAD 503).
- `git diff --stat` for the three files: 01-lattice.tex 100 (+50/−50), main-theorem.tex 12, reading-guide.tex 32; 72 insertions, 72 deletions. `git status --short` also shows 02-equation-section, 02-observables, 03-maxwell, 08-polymers, 09-stationary-remainder (other agents); I touched none of them. The main checkout /Users/mgubi/humanise-yang-mills was not modified.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1196 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-b1a monograph.tex`: exit 0; `grep -c undefined monograph.log` → 0; no Overfull boxes reported. The build includes the other agents' files as they were at that moment.
- The whole diff was reread once. The rendered PDF pages were not inspected (no pdftotext on this machine; not opened visually).
- No `lake build`, no external service, no commit.
