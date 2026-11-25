# Third review: main theorem, reading guide, chapters 1, 2 (with 2e), 3

Worktree `/Users/mgubi/ym-terminology`, files under `manuscript/HumanizeYM_v3/`: `main-theorem.tex` (MT), `reading-guide.tex` (RG), `chapters/01-lattice.tex` (1), `chapters/02-observables.tex` (2), `chapters/02-equation-section.tex` (2e), `chapters/03-maxwell.tex` (3). I read every word-diff `4f462ac5..HEAD` (6 + 15 + 51 + 36 + 38 + 68 = 214 changed lines) and judged it before opening the reports of rounds 1 and 2, the harmonisation report and the leads. Line numbers are HEAD's (unchanged by my edits).

## (a) Main theorem: statement compared word by word with 4f462ac5 (MT:9–48)

There are exactly two differences. Every other word of MT:9–48 is identical.

| line | 4f462ac5 | HEAD | judgement |
|---|---|---|---|
| MT:12 | "a positive penalty parameter for the block transformation," | "a positive penalty parameter for the renormalization transformation," | Same object. The table row "one block transformation" says: *step*, at first use "renormalization transformation"; 4:226 states the difference from Bałaban (penalty density instead of a delta function). Mathematically identical. |
| MT:27 | "They contain the identity and" | "They contain the identity field and" | Same object, the constant field `𝟏` (table row "unit" → *identity field*; defined at 2:80). Mathematically identical. |

I restored nothing. "admissible physical periods" (MT:14) is unchanged inside the statement; see Cross-chapter mismatches. Outside the statement, MT:50 adds the gloss "a phase being a character of a commutative operator algebra (Section ch15:characters)". It is true (15:8) and repeats the gloss at 1:415. MT:63 gains a hyphen, and MT:88–89 has "coincident points".

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| RG:18 | ERROR | "Fields are finally defined by equality of all separated correlation responses." | "…by equality of all their responses, the values of the correlation functionals." | The harmonisation (its §15) dropped **separated**. Round 2 had kept it ("all their separated correlations with all other fields"). The restriction to separated points is the point of the sentence. "Correlation functional" is defined only at 13:119–122, and the RG reader does not have that definition. 3:482 also uses the phrase with point evaluations. | "…by equality of their responses in all separated correlations." This is chapter 13's own wording (13:8–9: "Local fields are then defined by their responses in all separated correlations"). |
| RG:32 | MISMATCH | "one scale schedule must satisfy" | "one scale schedule (the choices of Chapter ch10:trajectory) must satisfy" | Point (d). This is the only "scale schedule" in the book. Chapter 10 defines the object as *the schedule* (10:121, D), and 10:5 says "a single schedule". The gloss already says which choices are meant. | "one schedule (the choices of Chapter ch10:trajectory) must satisfy" |
| 2e:254 | TERM | "for all labels and all spectators." | unchanged | Point (e). This is the first use of "spectators" in book order, before its definition at 3:705. The line is untouched, but a word from the table ("spectators, defined once") stands there. The sense is that of 11E:74 ("The same map works for every spectator") and 11E:163 ("every bounded spectator outside its microscopic stencil, by (ch02:microscopic-null)"): the other insertions of a correlation, which at lattice level include the exterior functions `S`. | "for all labels and all other insertions of the correlations." These are the words of the definition at 3:705 ("the remaining insertions … of the correlation"), so no second definition is needed. |
| MT:42; 19:78, 96 | MISMATCH | MT:42 "whose local charges generate translations and rotations"; 19:96 "its local charges" | unchanged | Point (b). See the next section. Chapter 14 now calls these objects "the local generators" (title 14:312, "both generators" 14:408), but MT:42 and 19:96 still say "local charges". | left for the author (no rename, as instructed) |
| 3:409 | MISMATCH | "the curvature response obtained by contracting …" | unchanged | Point (e). Here the term is the two-point function with a linear source (*response* sense 1). Chapter 11 uses the same name for the unrelated `J = H_{0,f}^{-1}TH_{0,c}` and `Ψ_i` (11:647, 1729–1750; 17w:67–68). One name, two objects. The line is untouched and the word is not in the table. | left for the author (the dictionary proposes "two-point function with source ℓ_P" for 3:409) |
| 3:146, 147, 832, 879, 914, 1016 | MISMATCH | "collision(s)", "collision diagonals" | unchanged | Point (c). See the section after the next. The lines are untouched and the word is not in the table. | left for the author |
| 1:371 | MINOR | "A lattice family converges" | "A lattice family (the measures μ_{N,p} and the insertions I_{N,p} above) converges" | Symbols added inside a definition. The gloss is correct by 1:331–350 and agrees with 1:398 ("The lattice family, including its normalizations"). The dictionary basis for this composition is I. | kept; noted |
| 1:365 | MINOR | "from the collision diagonals." | "from the diagonals $x_i=x_j$, $i\ne j$." | A formula was added. It is exactly the complement of `Conf_n` (1:357). | kept |
| 2:339 | MINOR | "has distance from the identity at most $t$," | "satisfies $\chi(U_\square)\le t$," | A formula was added in a proposition. It is equivalent: χ is defined at 1:90–94 as "the normalized Hilbert–Schmidt distance from the identity". | kept |
| 3:482 | MINOR | (no sentence) | "A family of correlation functionals, each the correlation with fixed insertions at fixed points, is a separating family …" | The definition was added. It matches the dictionary (R, 3:484–495, 797–809) and the source (one- or two-point tests at generic configurations). Later chapters also call families of smeared or pairing functionals "separating" (14:386, 832), and 13:120 defines "correlation functional" as a smeared one (`L_{v,f}`). The noun is used in two ways, point evaluation and smeared, but the property is the same. | kept; listed |
| RG:35 | MINOR | "A common trajectory then determines … for the entire Wilson family." | "The resulting common trajectory, the same for all ultraviolet cutoffs, then determines … for the entire family of Wilson measures." | "The same for all ultraviolet cutoffs" is the dictionary's gloss of "common" (*trajectory* 2, R, 10:4–9: the schedule and coefficient arrays used at every cutoff). Read as the sequence of couplings at one cutoff (*trajectory* 1), it would be false: chapter 10 proves convergence in N. The surrounding sentence (schedule, choices) points to sense 2. | kept; for the author |
| 1:473 | MINOR | "A transfer matrix records this mixing" | "The matrix of one step records this mixing" | The text now says "one step" and the definite article. It agrees with chapter 11, where the step with insertions gives a per-step coefficient map `M_G` together with a remainder map (11:381), matching "Bounds for this matrix and for the remainder" (1:474). | kept |
| 2e:88, 135 | MINOR | "base point $z$ of the plaquette" | "initial point $z$" | Correct, but 2:170 and 2:222 (untouched) still say "plaquette based at $z$". | left for the author |

Every other changed line I checked was correct. The list:
- contour / contour variable / holonomy (1:78–80, 126–127; 2:171, 216, 285, 367; 2e:67, 78, 80, 127, 209)
- scale / scale index and the Bałaban sentence (1:206; key `Balaban1987RG` exists; supported by the table row and the *level* Literature line, B87 p. 256)
- "in continuum units" (RG:5, 60; 1:11, 174, 202–227, 329–330, 350, 488)
- "dimensionful" (2:401)
- penalty parameter / penalty term (1:408–409, 420, matching 4:226 and 5:1163)
- regularity condition (1:149; defined at 4:426)
- background field, critical configuration and fluctuation field (RG:23; 1:452–453)
- positive halves and reflection planes (1:244–247, 284, 287, 317, 323)
- "subsequence", "the volumes P(k)" (1:379, 393)
- "single lattice family" (1:503)
- the bidegree gloss, identity field and filtration index (2:79–80, 96–99, 192, 259–260, 281, 400–402)
- test link variables (2:118, 150)
- "infinite lattice", "links of ℤ⁴" (2:291–295, 366, 381–382)
- exterior function (2e:41, 195, 205–206, 213, 221)
- base point for the anchor (2e:39, 83, 126, 212, 216)
- automorphism `R_d` (2e:52; defined at 2e:25)
- layer → (homogeneous) component / degree index (2e:91–185)
- the history forward reference (2e:253)
- on-shell polynomial space (3:194–224, 784)
- "argument" for slot (3:292–293, 1003)
- direct sum for tower (3:431, 462, 470; matches (ch03:triangular) and 3:391)
- flux convention reference (3:546–547)
- spectators definition (3:705)
- jet functional (3:751, 883, 939–995; at 3:751 `f` is the scalar curvature component)
- weighted Euler operator and "eigenspace of 𝓔" (3:689, 1009)
- zero-mean (3:580–603)
- annihilate for kill (3:925, 999, 1032, 1069)
- scaling dimension for weight (3:168–170, 786–1068)
- RG:73–74 (cluster of nearby fields, sign kept and constant independent of the number of reflected copies, consistent with 15:276, 17:130, 18:159, 185 and *signed* 2)
- RG:22, 26, 29, 55, 64, 76.

## Corrections applied

3 in-line replacements; line counts unchanged:
- ERROR 1: RG:18.
- MISMATCH 1: RG:32.
- TERM 1: 2e:254.
- LANGUAGE 0, LEFTOVER 0, DICTIONARY 0, MINOR 0.

## (b) "local charges"

- **MT:42** ("a … stress tensor whose local charges generate translations and rotations through the Ward identities") and **19:96** ("the conserved tensor, its local charges, Euclidean rotations and Ward normalization in Chapter 14") both mean the linear maps `p_b : F_d → F_{d+1}` and `Y_d(K) : F_d → F_d` of Proposition ch14:charges ("Representation of the local flux", 14:373–380). These maps represent the constant and linear fluxes (ch14:flux) of the stress tensor through a shrinking shell. Their commutation relations are (ch14:charge-commute), and their limits (ch14:charge-limits) identify `p_b = c_*∂_b`. At 4f462ac5, chapter 14 called them "local charge fields" (section title) and "both charges" (14:408). Chapter 14 now says "Shrinking shells and the local generators" (14:312) and "both generators annihilate the identity field" (14:408). MT:42 and 19:96 therefore name the same object differently from chapter 14.
- **19:78** ("Its relativistic continuation gives the local charge law (ch16:charge-law)") means the commutator identity `i[Q_K(f,c), Φ_ξ(A,g)] = Φ_ξ(Σ_K A, g) − Σ_a Φ_ξ(A, ∂_a(K^a g))` for the smeared charge `Q_K(f,c) = Σ_b T^M_{4b}(K^b(c⊗f))` (16:521–533). Chapter 16 calls it "a smeared charge identity" (16:535) in the section "The weak commutant and smeared stress charges" (16:464).

## (c) chapter 3 "collision"

- 3:146 ("support avoids collisions"), 3:147 ("supports meet collision diagonals"), 3:914 ("distributions defined on collision sets") and 3:1016 ("without collisions", that is, no two points coinciding along the path) mean the same object as "coincident points" / "the diagonals $x_i=x_j$" of chapter 1 (1:365, 424–426, 477), MT:46, 89 and chapters 12–18.
- 3:832 ("we use a collision that lowers the highest jet order") and 3:879 ("the unmodified rescaled collision limit") are not the set. They mean the process of bringing a quadratic spectator to the point of `P` and its short-distance limit (3:836–879). The dictionary also proposes *short-distance limit* for 3:879.
- All six lines are untouched, and "collision" is not in the table. Per (f) I did not rename them. Suggested words: "coincident points" / "the diagonals" at 146, 147, 914, 1016; "a short-distance limit" at 832 and 879.

## Cross-chapter mismatches not fixed

- MT:14 "admissible physical periods" against 19:20–21 "admissible periods $R_p$ in continuum units" and 1:202. This is inside the main theorem; (a) forbids changing it.
- MT:42, 19:96 "local charges" against 14:312, 408 "local generators" (see (b)).
- 3:409 "curvature response" (sense 1) against 11:647, 1729–1750 and 17w:67–68 (the unrelated `J`, `Ψ_i`).
- Chapter 3 "collision" (six lines) against "coincident points" / "the diagonals" (see (c)).
- 2:170, 222 "plaquette based at $z$" against 2e:88, 135 "initial point $z$ of the plaquette".
- "Correlation functional" is point-evaluated at 3:482 (and RG:42) but smeared at 13:120 (`L_{v,f}`). "Separating family" covers both.
- "Lattice family" (1:371, 391, 398, 503) against "family of Wilson measures" (RG:36; MT:58) and "the same family of measures" (17–19). The dictionary adopts the latter in 17–19.
- The filtration index `d` (2:96–402) is still called "normalization index" at 11-marked-insertions.tex:2307 (not my file).
- The phase gloss is repeated at MT:50 and 1:415. Both glosses are true.
- "Step" is emphasized at RG:22, and contour is defined at 1:78–80 (4:36 status not rechecked by me).

## Leftover house words

Replaced: none of the listed house words needed replacing in the six files. "spectators" (a defined term from the table) at 2e:254 was replaced because it is used before its definition (see Findings).

Kept on purpose:
- MT:14 "physical periods": inside the main-theorem statement.
- 1:171 section title "Physical scales and lattice symmetries": untouched title, not a table word; author's choice.
- "unit" at 2:222, 2e:81, 92, 3:323, 525, 733, 847, 953: ordinary (unit square, plaquette, sphere, direction, mass).
- "mixed" at 1:434, 3:406, 944, 947: ordinary.
- "weighted" / "support weights" at RG:28: ordinary / support weight proper.
- "label(s)": the defined polynomial labels, and LaTeX `label=`.
- "frame" at 2:181 ("the frame at the origin"): ordinary geometric use.
- "response(s)" at 3:409, 423, 444, 899, 975 (sense 1), 3:657, 1084, 1086 (sense 2) and 3:964 (sense 3): untouched lines (444's change was only tower → element) and not table words; listed under *response* in the dictionary for the author.
- "collision(s)": see (c).
- "transport" (1:80 "row transport", "transported curvature"): kept by the table (parallel transport).

None of these remain in the prose of the six files: actual, tag, block average, predictor, stationary, noise, cutoff failure, tree gauge, level, block transformation, reset, marked, unmarked, heat, ground, kill, supply/supplied, seam, slot, layer, anchor, probe, tower, regrading.

## Leads

- chapter 3 "collision" against "coincident points": verified; left (see (c)).
- "scale schedule" (RG:32) against "schedule": verified; corrected to "one schedule".
- "curvature response" names two objects (3:409; chapter 11): verified; left (untouched line, not a table word).
- normalization index (11:2307) against filtration index (2:96–402): verified that chapter 2 uniformly says filtration index. 11:2307 is not my file.
- "microscopic" (RG) against "at the cutoff scale" (18gq, 18lp): RG:55 "exact microscopic equations" is untouched and refers to the lattice equations of motion of 2e (exact at every cutoff). It is not the cutoff-scale coordinates. No change.
- "lattice family" (1:371–503) against "the same family of measures": verified; listed. The 1:371 gloss is correct.
- "uniform in the number of reflected copies" (17w:120) against "with constants independent of …" (RG:74): RG:74 uses the majority form. No change in my files.

## Assessment of earlier corrections

- **Harmonisation §15, RG:18: wrong.** It replaced round 2's "by equality of all their separated correlations with all other fields" with "by equality of all their responses, the values of the correlation functionals", dropping "separated" and introducing a term defined only in chapter 13. Corrected (see Findings).
- Harmonisation §10, RG:35 ("The resulting common trajectory, the same for all ultraviolet cutoffs"): acceptable under *trajectory* sense 2. "Same for all ultraviolet cutoffs" was added by round 1 and is the dictionary's reading. Noted for the author.
- Round 2's corrections (2:11, 2:401, 1:460, 2:118): all correct.
- Round 1's corrections (RG:32–35, 1:207, 1:409, 1:452–453, 1:490, 2:50–51, 2:171, 2e:253): correct. RG:32 kept "scale schedule", which I have now shortened to "schedule" (the gloss already carries the content).

## For the author

1. MT:14 "admissible physical periods" (theorem statement) against "admissible periods $R_p$ in continuum units" (19:20–21).
2. MT:42 and 19:96 "local charges" against chapter 14's "local generators" `p_b`, `Y_d(K)`; decide one name.
3. 3:409 "curvature response" (the chapter 3 two-point function) against chapter 11's curvature response `J`.
4. Chapter 3 "collision" (six lines): "coincident points" / "the diagonals" for 146, 147, 914, 1016; "short-distance limit" for 832, 879.
5. RG:35 "the same for all ultraviolet cutoffs": correct only in the sense "the construction of Chapter 10"; consider "the common trajectory of Chapter 10" without the gloss.
6. 2e:254: I wrote "all other insertions of the correlations". If you meant only the exterior functions `S`, write "all exterior functions".
7. "Correlation functional": point-evaluated (3:482, RG:42) or smeared (13:120).
8. "plaquette based at $z$" (2:170, 222) against "initial point $z$" (2e:88, 135).
9. Titles: 1:68, 1:171, 2:102, 2e:60, 3:591 (as listed by round 2).

## Checks

- Line counts (working tree / `git show HEAD:… | wc -l`): main-theorem.tex 102/102; reading-guide.tex 84/84; 01-lattice.tex 503/503; 02-observables.tex 452/452; 02-equation-section.tex 254/254; 03-maxwell.tex 1088/1088.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-t1 monograph.tex`: exit 0. monograph.pdf and monograph.log are dated 11:34, after my edits. In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0. The build included other reviewers' concurrent working-tree edits (chapters 4, 5, 12, 13, 14).
- Edited only reading-guide.tex (2 lines) and 02-equation-section.tex (1 line). Nothing committed, staged, pushed or reverted.

## Not checked

- Rendered PDF pages were not inspected; no pdftotext or PyMuPDF is available.
- Bałaban's paper itself (1:206 checked only against the table and the Literature line).
- Untouched lines of chapter 3 beyond the leftover greps. Chapters 4–19 only where grepped for the named objects.
