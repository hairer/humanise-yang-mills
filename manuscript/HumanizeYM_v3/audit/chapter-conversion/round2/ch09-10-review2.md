# Second review r5: chapters/09-renormalization.tex (9), 09-forest-average.tex (9f), 10-common-trajectory.tex (10)

Worktree /Users/mgubi/ym-terminology, manuscript/HumanizeYM_v3. Diffs read: `git diff --word-diff 4f462ac5 HEAD` for the three files (9: 184 changed lines, 9f: 65, 10: 160; 409 in all), each changed line read against the present file around it, before the first-round reports (ch09-apply/review, ch10-apply/review) were read. Nothing staged, committed or reverted.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 9:283–284 | ERROR | "…unrelated event indicators or a seeded and / an unseeded law has been made. The actual interpolation estimates" | "…unrelated event indicators, or between a sector with nonempty index triple / and the law with empty index triple, has been made. The interpolation estimates" | False: the unseeded law keeps `A_c` (the coarse large-field set), so it is not "the law with empty index triple". Chapter 6 (6:1544) has been restored to "seeded sector … unseeded law". | "…unrelated event indicators or a seeded and / an unseeded law has been made. The interpolation estimates" (4f462ac5 words; "actual" stays deleted) |
| 9f:274–275 | LEFTOVER | "A label which contains exactly one incoming regular / activity records its index $i$" | unchanged | *regular activity* (sense 1, the incoming `(X_i,o_i,E_i)`) is *localized term* everywhere else in 9 and 9f (e.g. 9f:546, 586). Inside Assumption ch09:forest-assumption; the word only changes, the object is the same. | "…incoming localized / term records its index $i$" |
| 9f:346–348 | LEFTOVER | "…computed from data in its dependence / region: local windows of the quadratic form, their inverses, block / averages and link words." | unchanged | "dependence region" is "dependence set" everywhere else (9:82–93; 9f:230, 329, 682, 716, 933); "block averages" (the values `Q_e(U)`) is a table word; 9s:141 now says "the values of the averaging operation". | "…dependence / set: local windows of the quadratic form, their inverses, values / of the averaging operation and link words." |
| 9f:633 | TERM | "the missing symmetry is restored / by an averaging operation." | unchanged | After the conversion "averaging operation" is the name of the nonlinear block average (9:913; 9f:125, 348); here it is the average over `H_4`. One name, two meanings. | "…restored / by averaging." |
| 9f:964–965 | LEFTOVER | "…which fix one forest: their marked / activities must be averaged" | unchanged | *mark* sense 1: "with insertions"; chapter 11 now has "expansions with insertions", "coefficient with insertions". | "…their activities / with insertions must be averaged" |
| 9:153 | DICTIONARY | "for ordinary polymers excluded by a selected large-field region." | "…by a chosen large-field region." | The dictionary files 9:153 under *selected* sense 1 (belonging to the index triple); the editor took sense 4. "chosen" is neutral and not false. | left for the author |
| 9:921 (10:921) | DICTIONARY | "One must use the same block bridge, clipping data and" | "…the same linearization of the critical configuration, clipping data and" | Book-wide table asks for the representative where `W` is unqualified; *block bridge* gives `W_a`, but with basis I for the representative, so no symbol may be inserted. | left for the author |
| 9f:865 | MINOR | "transports the quadratic expression $a_dP_d$ with its channel." | "…$a_dP_d$ together with its quadratic term." | Reads slightly circularly (`a_dP_d` is the expression of the quadratic term `d`, 9:545), but true. | left |
| 10:432, 439, 447, 781, 861 | LEFTOVER (kept) | "zero terminal arrays", "Wilson terminal arrays", "zero-terminal-array history", "terminal activity", "zero terminal array" | unchanged | *terminal* sense 1 is "at the ultraviolet cutoff", but the auxiliary histories start at a scale `k>m`, not at `N` (10:824), so the word is ambiguous here; the first editor left them for that reason. | left for the author |

All other changed lines were found correct in meaning, word and grammar. Points checked in particular:

- **Assumption ch09:forest-assumption (9f:221–310), its statements and proofs, Propositions ch09:forest-average-prop, ch09:family-equivariance, ch09:output-equivariance, Lemmas ch09:forest-determinant, ch09:path-channels, ch09:symmetric-localization, ch09:isotropy**: compared with 4f462ac5 line by line; only words for the same objects change (scalar → (normalization) constant, regular activities → localized terms, anchor(s) → base point(s), dependence region → set, channels → terms, rows → components, selections → index triples / families, folding → reflection map, logarithmic → large-field / correction, first → Mayer). No hypothesis, quantifier or conclusion changed. My two edits inside the assumption (274–275) and the comment after it (347–348) are words only.
- **Theorem ch09:step-theorem (9:909–952)**: hypotheses and conclusion identical in content. "the free quadratic forms of two consecutive scales" is the dictionary's own reading of "adjacent quadratic pair" (*adjacent pair* 1, R, citing 9:912); "clipped frozen inhomogeneous term" (*source* 5, R, 9:924); "lower bounds on the ratio / the reference coupling / the period" (*floor*, *threshold*); "original" torus/period (*actual*, sense for 9:931, 936); "uniformly in volume, ultraviolet cutoff and curve parameter"; "commutes with restriction of the parameter interval" (= "restriction compatibility", cf. 9:391, 815–816); "That the output inverse coupling lies in its band additionally requires…" (Appendix D wording, no formula).
- **Added sentence 9:723** (Bałaban's names): checked against *reset*, `*Literature:*`: "coupling constant renormalization" (B87 p. 268; B88b p. 279), "vacuum energy renormalization" (B88b p. 279; B87 p. 258 has "vacuum energy counterterm"); "Bałaban defines `g_{k+1}` by the β-function [B87 (0.18), (2.15)], v3 defines `β = β′+α+Δ` by the matched coefficient plus a projected remainder `Δ`". The sentence claims exactly this; `α` (9:410, "fixed by the matching") and `Δ` (9:523, the coefficient of the local quadratic subtraction) are those of the display on 9:719. Keys `Balaban1987RG` (CMP 109, 1987, 249–301 = B87) and `Balaban1988Expansions` (CMP 119, 1988, 243–285 = B88b) exist in references.bib. 9:717 is the first use of both names in the book (grep of main-theorem, reading-guide, ch. 1–8: none); the sentence occurs nowhere else (chapter 10 and 13sb:26 use the term without repeating it). Correct; kept.
- **Short terms of these files**: *large-field correction* (defined 9:367–368, "a term of the exponent"; used 9:432, 607, 630, 633, 638, 671, 677, 698; 9f:871, 875; 10:570 "large-field correction terms in the exponent"); *quadratic term* `d` (9:543–544; 9:571, 612, 770, 861; 9f:865–866); *auxiliary standard Gaussian coordinates* (9:59); *stage pairs* (10:30, used 10:125); *schedule* (defined 10:121; used before at 10:12, 67, 114 and in ch. 4–7 in the same sense); *stage plateau* (10:123); *coarse endpoint* (10:153; 10:268 and 10:850 consistent, 19:21–23); *activity array* (glossed 10:421); *finite parameter evaluation* (glossed 10:457). All defined at or before their first use in book order, with one meaning.
- **Cross-chapter names**: step, two consecutive scales, representation data, averaging operation, dependence set, auxiliary index (9:83, 85; no `α` inserted), index triple, event label, large fluctuation-field event, additional conditions / eligibility conditions, joint law, lower bound on the reference coupling (as 6:322, 411, 432, 919, 1161; 11:382; 17m:185), inherited loop action (7), coordinate contours (7:146), implicit-differentiation formula (7:938), blocking sequence (5), critical configuration / critical-configuration map, penalty parameter `b`, Mayer expansion / exponentiation, exact regrouping (Proposition ch09:fusion-prop) — consistent.

## Corrections applied

ERROR 1 (9:283–284); LEFTOVER 3 (9f:274–275, 9f:347–348, 9f:964–965); TERM 1 (9f:633). Total 5 corrections, 9 lines, all within lines. 10-common-trajectory.tex unchanged.

## Cross-chapter mismatches not fixed

- "reserve" for the support-weight margin: chapter 9 (and 8) say "margin in the decay rate of the support weight" (9:148, 230, 267, 282, 438, 919; 9f:615, 960); chapter 10 still says "support reserves" (10:37, 507), "support-exponent reserve" (10:594), "support reserve" (10:603–604, 913), "support and attachment reserves" (10:760), "comparison reserves" (10:813), "numerical reserves" (10:426). The dictionary's basis for these lines is I (not tied to a displayed inequality), so not changed.
- "inverse coupling band" (9:386; 10:676), "reference-inverse-coupling bands" (9:429) against "coupling band" (6:623, 878, 1155; 10:212) and "reference coupling" for `β̂` (6, 9, 10). Also "reference inverse coupling `β_0`" (10:524, a local value, correctly different). The book still uses "inverse coupling" for `β` some 40 times in chapter 10 against "the coupling β" of chapter 4 and of 10:153, 808: a book-wide choice.
- `α`: "the determinant coefficient fixed by the matching" (9:410, 723, 738) and "explicit coupling increment `α_{N,m}`" (10:423, 855): two descriptions of the same coefficient, both dictionary proposals (*matched*, *path coefficient*); compatible but not one name.
- "spatial exponents" (9:30) against "spatial weights" (10:79) for what appear to be the same stage data `ϖ_j` (not verified).

## Leftover house words

Kept on purpose:
- "label(s)": labels of Assumption 9f (a)–(f) (index of a term, *label* 6, kept as defined there; the assumption must stay identical), "event label(s)" (defined term), "correction labels", "fixed labels", and LaTeX labels.
- "stationary" 9:136 ("the stationary mean"), 293 ("finite stationary region"), 305 ("sector and stationary estimates"): they refer to the section "The stationary integral with its cutoff retained" of 9s, which keeps the word; changing them alone would break the reference.
- "physical": 9:240, 257, 773; 10:711, 725, 732, 880, 896–898 (*physical* sense 4 and 10:880, basis I); 9f:604 "physical torus" (ordinary contrast with the auxiliary tori); 10:28 ordinary.
- "weight(s)": support weight (sense 2, kept), "weighted", "allocation weights" (App. D), 9:182 "original weights", 10:79, 382, 465, 605, 617 (ordinary or basis I).
- "unit": 9:465 (a unit vector `T_*`), 9:687 ("one additional unit"), 10:153 ("unit scale"): ordinary.
- "level": only "level set" (10:229), ordinary. "reset": only `C_{\rm reset}` and labels (math, labels). "actual": only label names `ch05:actual-*`, `ch06:actual-jet-integral`. "marked": 9:263 "marking one changed factor" is ordinary (*mark*, Across chapters). "scalar": 9:764 "the two scalars" (numbers), 10:443, 515, 645, 684, 826, 849, 868, 870 (scalar coordinates / projection / recursion / bound; left by the first round, *scalar* senses 3–4).
- None of "tag", "block transformation", "predictor", "noise", "cutoff failure", "frame", "tree gauge", "heat", "mixed", "ground", "kill" remain in prose.

Replaced: 9f:274–275 (regular activity), 9f:347–348 (dependence region, block averages), 9f:964–965 (marked).

## Assessment of the first review's corrections

- ch09-review left 9:283–284 as "a sector with nonempty index triple … the law with empty index triple" while noting that the unseeded law keeps `A_c`; that wording was false and is now restored (see Findings).
- All its other corrections hold: 9:17 ("which need not equal the reference value"), 9:26 (inherited loop action), 9:83 (`α` removed), 9:176, 9:190, 9:234, 9:442, 9:547 ("clipped expression or expression restricted by its event indicator", the disjunction restored), 9:687 ("number of attachments" restored), 9:723 (sentence correct, see above), 9f:125 ("derivative" restored), 9f:865.
- ch10-review corrections (107, 111 starting scales; 123 stage plateau; 356 direct coefficient; 656, 658, 666 hard/soft restored; 676 sectors restored) are correct.

## For the author

- 9:153 "chosen large-field region" against the dictionary's *selected* sense 1.
- 10:921 representative of the linearization (`W_a` by the dictionary, basis I).
- 10:432, 439, 447, 781, 861 "terminal" (auxiliary histories do not start at `N`).
- 10:655, 666, 774, 914: "the exact regrouping" without `\ref{ch09:fusion-prop}`.
- The cross-chapter pairs above (support reserve / margin; inverse coupling / coupling; names of `α`).
- 9:283–284 and 6:1544 now both read "seeded … unseeded"; "seeded" itself is not defined in the book (the dictionary's repair "the law of a nonempty selection and that of the empty selection" would need `A_f = A_n = ∅`, not an empty triple).

## Checks

- Line counts: 09-renormalization.tex 979 = HEAD 979; 09-forest-average.tex 973 = 973; 10-common-trajectory.tex 935 = 935. `git diff --stat` against HEAD: 9f 7/7 lines, 9 2/2 lines, 10 none.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r5 monograph.tex`: exit 0. monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0 (the build included other reviewers' concurrent edits).
- Rendered text (pypdf): the corrected phrases found on PDF pages 126 ("localized term records"), 127 ("averaging operation and link"), 130 ("restored by averaging"), 133 ("with insertions must"), 135 ("seeded and").

## Not checked

- Pages were not inspected as images.
- Bałaban's papers were not reread; the 9:723 check rests on the dictionary's `*Literature:*` line.
- 09-stationary-remainder.tex and chapters other than mine were only grepped for consistency.
- Whether 10:79 "spatial weights" and 9:30 "spatial exponents" are the same data was not verified.
