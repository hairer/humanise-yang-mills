# Second review: main theorem, reading guide, chapters 1, 2 (with 2e), 3

Worktree `/Users/mgubi/ym-terminology`, files under `manuscript/HumanizeYM_v3/`: `main-theorem.tex` (MT), `reading-guide.tex` (RG), `chapters/01-lattice.tex` (1), `chapters/02-observables.tex` (2), `chapters/02-equation-section.tex` (2e), `chapters/03-maxwell.tex` (3). All word-diffs `4f462ac5..HEAD` (6+15+50+34+38+68 changed lines, 211 in all) were read and judged before the first-round report `audit/chapter-conversion/front-ch01-03-review.md` and the apply reports were opened.

## Main theorem: statement compared word by word with 4f462ac5 (MT:9–48)

Exactly two differences inside the statement; every other word of MT:9–48 is identical.

| line | 4f462ac5 | HEAD | judgement |
|---|---|---|---|
| MT:12 | "a positive penalty parameter for the block transformation," | "a positive penalty parameter for the renormalization transformation," | same object (table: one block transformation = renormalization transformation, a step). Mathematically identical. |
| MT:27 | "They contain the identity and" | "They contain the identity field and" | same object (the constant field `𝟏`, *unit* 1 → *identity field*). Mathematically identical; the term is defined later, at 2:80 (MT is informal and comes first). |

Unchanged inside the statement: MT:14 "admissible physical periods". Now 19-assembly.tex:20–21 says "admissible periods $R_p$ in continuum units", and 1:202 "periods $R_p$ (the side lengths of the tori in continuum units)". Listed below, not decided.

Outside the statement: MT:50 adds "a phase being a character of a commutative operator algebra (Section~\ref{ch15:characters})" — true (15:8 "A phase will be a character of a commutative operator algebra"; 15:136 characters of 𝔄); repeated at 1:416. MT:63 hyphen; MT:88–89 "coincident points" as MT:46 already says.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 2:401 | LEFTOVER | "Its eventual physical normalization" | unchanged | *physical* sense 2 (factor `a_N^{-d}`, R): the sentence is about the dimensionful normalization of the identity field, the object of 11:86–89 ("the dimensionful normalization … reference-scale coefficient of the dimensionful identity field … `a_{r(d)}^d e_0`"). The editor called it ordinary. | "Its eventual dimensionful normalization" |
| 2:11 | LEFTOVER | "normalize the representatives at a fixed physical scale." | unchanged | *physical* sense 1 (R): a scale fixed in continuum units (the reference scale `a_{r(d)}` of 11:88). With *scale* now defined at 1:206 as `a_m`, "physical scale" is the old word. | "normalize the representatives at a fixed scale in continuum units." |
| 1:460 | LEFTOVER | "It does not supply those estimates by itself." | unchanged | *supplies* (R, proposal "gives", Where lists 1:456 for this sentence); all other "supply" in chapters 1–3 were converted. | "It does not give those estimates by itself." |
| 2:118 | LANGUAGE | "The solution remains in $G$." | "…; we call the $U(h,J)(y,\mu)$ the \emph{test link variables} of the jet $J$." | "the" directly before a formula with no noun. | "we call the matrices $U(h,J)(y,\mu)$ the \emph{test link variables} …" |
| RG:18 | DICTIONARY | "by equality of all separated correlation responses." | "by equality of all their separated correlations with all other fields." | Entry *correlation responses* (R) proposes "the correlation functionals `L_{v,f}`" and says explicitly "Not *correlations with all other fields*"; entries *one-slot response* / *spectator responses* propose the phrase used. Meaning is preserved (labels identified when all their separated correlations against spectators agree), so not wrong. | left for the author |
| RG:35 | MINOR (author's choice) | "A common trajectory then determines the couplings, activities and observable normalizations for the entire Wilson family." | "The resulting construction, the same for all ultraviolet cutoffs, then determines … for the entire family of Wilson measures." | Subject changed from "trajectory" (a defined object of ch. 10, whose title is still "A common trajectory and fixed-scale stability", and RG:59 still "One common trajectory") to the vaguer "construction"; "resulting" is new. Not false (the trajectory results from the schedule of RG:32), but RG:35 and RG:59 now name the object differently. | left for the author |
| RG:32 | LEFTOVER (kept) | "one scale schedule must satisfy" | "one scale schedule (the choices of Chapter~\ref{ch10:trajectory}) must satisfy" | *schedule* 2 proposal "the choices of Chapter 10"; the first reviewer restored the word to keep "one" and the subject of "It is chosen slowly enough". Agree. | left for the author |
| 2e:254 | TERM / DICTIONARY | "for all labels and all spectators." | unchanged | First use of "spectators" in book order, before its definition at 3:705. The dictionary (*spectator* 2, *exterior spectator* 1, R) assigns this line to *exterior function*; but in a sentence about continuum null fields it can equally mean the other insertions (sense 1). Both editors left it; I agree the sense is the author's to fix. | left for the author ("all exterior functions" if sense 2) |
| 2:339 | MINOR | "If every plaquette used by the translated section has distance from the identity at most $t$," | "If every plaquette $\square$ used by the translated section satisfies $\chi(U_\square)\le t$," | Formula inserted into a theorem statement. Equivalent: 1:90–94 defines χ as "the normalized Hilbert–Schmidt distance from the identity"; 2:310–312 already says "a bound $\chi(U_\square)\le t$". Proposed by the dictionary (*distance from the identity*, D). Not wrong. | kept; noted |
| 1:371 | MINOR | "A lattice family converges" | "A lattice family (the measures $\mu_{N,p}$ and the insertions $I_{N,p}$ above) converges" | Gloss with symbols added inside Definition ch01:ordered-limit. Correct by 1:331–345 (`I_{N,p}`, `μ_{N,p}` enter `C^lat`), but the dictionary gives the composition basis I. | kept; noted |
| 1:365, 477 | MINOR | "from the collision diagonals"; "their collision diagonals" | "from the diagonals $x_i=x_j$, $i\ne j$"; "the diagonals" | Formula added; it is exactly the set meant (*collision*, R). Correct. | kept |
| 3:431–432, 462, 470 | MINOR | "a finite tower", "full tower", "whole tower" | "an element $\Sigma_zP$ of $\bigoplus_{k\le j}\mathcal S_k$", "direct sum $\bigoplus_{j<m}\mathcal S_j$", "direct sum" | Formulas added; checked against (ch03:triangular) (`0≤k≤j`) and 3:391 (`⊕_{j<m}`). Correct; dictionary *tower* (D/R). | kept |
| 3:168–170 | MINOR | "As in Definition ch02:labels, we also call `weight' the scaling dimension of a homogeneous jet polynomial." | "As in Definition ch02:labels, scaling dimensions add in products of these coordinates." | A definition of a removed word became a (true) statement restating 2:49. Fine; the additivity sentence is in the paragraph before the Definition, not in it (as the old reference already was). | kept |
| 3:546–547 | MINOR | "match the shell-flux convention in the supplied construction." | "match the flux convention \eqref{ch03:flux} used below." | Reference added; (ch03:flux) at 3:666 is the outward flux (3:705), dictionary *supplies* (S). Correct. | kept |
| 3:577 | MINOR | "quantitative estimates on moving comparison fields." | "quantitative convergence of the rescaled interacting fields to free fields." | Dictionary *moving comparison fields* (S) proposes "…to their free limits". Correct. | kept |
| 3:591 | MINOR (title) | "Conserved tensor line" | "One-dimensionality of the space of conserved tensors" | Title matches the statement (`{div J = 0} = ℝT^Max`). | left for the author (titles) |
| 2e:88, 135 | MINOR | "base point $z$ of the plaquette", "integer base points" | "initial point $z$", "integer initial points" | Correct; but 2:167, 222 still say "plaquette based at $z$". | left for the author |

Everything else checked and found correct (independently of the first round): contour / contour variable / holonomy (1:78–80, 125–127, 2:171, 217, 285, 367, 2e:67, 78, 80, 127, 210); scale / scale index with the Bałaban reversal (1:206; key `Balaban1987RG` exists, claim within the *level* Literature line); all "physical" → "in continuum units" (sense 1) in RG and chapter 1; "positive halves" (1:245–247), "reflection planes" (1:284, 287, 318, 324); "subsequence", "the volumes $P(k)$"; penalty parameter / penalty term (1:409, consistent with 4:226, 5:20, 5:88, 19:17); "regularity condition … a bound on χ" (1:150, consistent with 4:426–428); "background field (a critical configuration)" and "fluctuation field" (1:452–453; RG:23); "The matrix of one step" (*transfer matrix*, R); identity field (2:80, 192, 260, 281, 399; 2e:227, 236; 3:127, 190, 925, 943, 1033); filtration index (2:96–99, 402); bidegree gloss (2:79; `w_i, f_i` defined at 2:66–67); exterior function and base point (2e:39–41, 83, 126, 194–221); "automorphism $R_d$" (2e:52, defined at 2e:25); layer → (homogeneous) component / degree index (2e:91–184, 3:185); history forward reference (2e:253; label resolves); separating family definition (3:482; covers Corollary 3:484 and Proposition 3:806; no other definition in the book); spectators (3:705; `P_1,…,P_n` as in (ch03:ward-identity)); jet functional (3:751; consistent with `U_j=(𝒮_j^sc)^*` at 3:939); weighted Euler operator and "eigenspace of $\mathscr E$" (3:689–692, 1009; `\mathscr E` is (ch03:weight)); zero-mean (3:580–603; same word in 14:261–263, 1004, 1019); on-shell polynomial space (3:194–224, 784; *free image*, D); annihilate (*kill*, R); argument (*slot* 2).

## Corrections applied

4 in-line replacements, line counts unchanged:
- LEFTOVER 3: 2:11, 2:401, 1:460.
- LANGUAGE 1: 2:118.
- ERROR 0, TERM 0, MISMATCH 0, DICTIONARY 0, MINOR 0.

## Cross-chapter mismatches not fixed

- Admissible periods: MT:14 "admissible physical periods" against 19-assembly.tex:20–21 "admissible periods $R_p$ in continuum units" (and 1:202 "periods $R_p$ (the side lengths of the tori in continuum units)"). Listed, not decided, as instructed.
- Contour defined twice: 1:78–80 and 4:36 ("a \emph{contour} is a lattice path along which the link variables are multiplied, and its \emph{contour variable} is their ordered product"). 4:36 should become a use or a back reference.
- Step emphasized twice: RG:22 ("the renormalization transformation, or \emph{step}, of Chapter~\ref{ch04:blocking}") and 4:5 ("A renormalization transformation, called a \emph{step}").
- Common trajectory: RG:35 "The resulting construction, the same for all ultraviolet cutoffs" against RG:59 "One common trajectory" and the chapter 10 title.
- Collision: 3:146–147, 832, 879, 914, 1016 still "collision(s)", "collision diagonals"; MT, RG and chapter 1 say "coincident points" / "the diagonals". Dictionary basis I for chapter 3 lines; not changed.
- "normalization index" for the filtration index survives at 11-marked-insertions.tex:2307 (not my file).
- Plaquette base: "plaquette based at $z$" (2:167, 222) against "initial point $z$ of the plaquette" (2e:88, 135).
- Phase gloss repeated: MT:50 and 1:416 both gloss "phase" (true; duplicate).

## Leftover house words

Replaced: "physical" at 2:11 (sense 1) and 2:401 (sense 2, → dimensionful); "supply" at 1:460.

Kept on purpose:
- MT:14 "admissible physical periods" — inside the main theorem statement (see above).
- 1:171 section title "Physical scales and lattice symmetries" — sense 1; a title, author's choice.
- 1:314 "The slots are the $2q$ strips" — *slot* 1, positions of the cyclic product of the cited chessboard theorem; the dictionary doubts a standard word exists.
- 3:146–147, 832, 879, 914, 1016 "collision" — basis I for chapter 3.
- RG:32 "scale schedule" — with gloss; see Findings.
- "unit" at 2e:81, 92 ("unit plaquette", "unit square"), 3:323, 525, 733, 847, 953 — ordinary (unit square/sphere/direction/mass).
- "mixed" at 3:406, 943, 947 — ordinary ("mixed jet orders", "mixed quadratics").
- "weighted" at 3:311, "weighted norms"/"support weights" at RG:28 — ordinary / *weight* 2.
- "centered" at 1:183, 217, 3:699 — *centered* 2, ordinary geometric sense.
- "label" — the defined *polynomial labels* (2:58) and LaTeX labels.
- "transport", "transported curvature", "parallel transport" — kept by the table (parallel transport for the action).
- No "actual", "tag", "block average", "predictor", "stationary", "noise", "cutoff failure", "frame" (2:181 "the frame at" is ordinary: the Lie-algebra frame at a point), "tree gauge", "level", "block transformation", "reset", "marked", "heat", "ground", "kill" remain in prose of the six files.

## Assessment of the first review's corrections

All twelve corrected lines re-read: RG:32–35 (restores "one scale schedule … It is chosen slowly enough", correct; gloss of *stage* matches 10:25 and the label resolves), 1:207, 1:409, 1:452–453, 1:490, 2:50–51, 2:171, 2e:253. None is wrong. Two remarks:
- 2:50–51: the reviewer's sentence "its scaling dimension is the common scaling dimension of its monomials" is correct (homogeneity is in scaling dimension).
- 1:452–453: "(a critical configuration, Chapter~\ref{ch05:gaussian})" restores the dropped "stationary"; correct.
The first reviewer's "Checked and found correct" list matches my own reading, except that it called 2:401 "sense 2, correctly not touched" and 2:11 ordinary; I replaced both (sense 2 has the proposal *dimensionful*, used at 11:86–89).

## For the author

1. MT:14 "admissible physical periods" vs 19:20–21 "admissible periods $R_p$ in continuum units".
2. RG:18: "correlations with all other fields" vs the dictionary's "correlation functionals".
3. RG:35 "The resulting construction, the same for all ultraviolet cutoffs" vs "common trajectory" (RG:59, chapter 10 title).
4. 2e:254 "all spectators": sense 1 (other insertions; then used before 3:705) or sense 2 (exterior functions).
5. Titles: 1:68 "Links, contour variables and the Wilson measure"; 1:171 "Physical scales and lattice symmetries"; 2:102 "Test link variables and Taylor normalization"; 3:591 "One-dimensionality of the space of conserved tensors".
6. Chapter 3 "collision" (five places).
7. Duplicate definitions: contour (1:78–80, 4:36); step (RG:22, 4:5).
8. "initial point" vs "based at" for plaquettes (2e:88, 135 vs 2:167, 222).

## Checks

- Line counts (working tree / `git show HEAD:… | wc -l`): main-theorem.tex 102/102; reading-guide.tex 84/84; 01-lattice.tex 503/503; 02-observables.tex 452/452; 02-equation-section.tex 254/254; 03-maxwell.tex 1088/1088.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-r1 monograph.tex`: exit 0. In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0. The build included other reviewers' concurrent edits (e.g. 06-large-fields.tex).
- Only 01-lattice.tex and 02-observables.tex edited (4 lines); nothing committed, staged, pushed or reverted.

## Not checked

- Rendered PDF pages not inspected.
- Bałaban's paper itself (the 1:206 sentence checked against the dictionary's Literature line only).
- Unchanged lines of chapter 3 beyond the leftover greps; chapters 4–19 only where grepped for the named objects.
