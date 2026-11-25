# Review of job c1 (chapter 9: 09-renormalization.tex, 09-forest-average.tex)

Worktree `/Users/mgubi/ym-terminology`, files under `manuscript/HumanizeYM_v3/chapters/`. `9` = 09-renormalization.tex, `9f` = 09-forest-average.tex. Line numbers are those of the files (unchanged by the edit). Nothing committed or staged. 10-common-trajectory.tex and 11-marked-insertions.tex (modified by other agents) were not touched.

## Review findings

| file:line | class | committed text | edited text | what was wrong | corrected text |
|---|---|---|---|---|---|
| 9:547 | ERROR | "and $L_d$ its actual clipped or tested expression." | "its clipped expression, restricted by its event indicators." | In (ch04:path-action) a plaquette term is clipped (`clip_t(χ)`) and a row-square term carries the indicator `χ^rel`; "clipped **or** tested" is a disjunction by kind of term. The edit made both properties hold for every `L_d`. | "its clipped expression or expression restricted by its event indicator." |
| 9f:125 | ERROR (draft must stay identical) | "for the derivative of the block average" | "for the linearization of the averaging operation" | "derivative" is not a house word; only "block average" was to change. | "for the derivative of the averaging operation" |
| 9:687 | DICTIONARY | "bounds the number of attachments" | "bounds the number of supports meeting a given support" | *attachment* sense 2 has basis I at 9:687 (only S for the source statement); the replacement is also stronger than what one unit of decay gives (a weighted sum, not a number). Only the norm sense (9:697 "attachment norm" → site norm, which is the norm of 9:659/602) and the margin of that norm bound (9:794) were legitimately converted. | "bounds the number of attachments" (restored; the change "exponential support decay" → "the decay rate of the support weight" in the same line kept) |
| 9:83 | TERM | "tag variable" | "auxiliary index $\alpha$" | Inserts the symbol `α`, which in this chapter is the matched determinant coefficient (`β = β′+α+Δ`, 9:409–410, 719). Symbol clash created by a vocabulary change. | "auxiliary index" |
| 9:26 | MISMATCH | "the quadratic loop correction" | "the $\beta$-independent quadratic term" | Chapter 7 (7:237) defines this object's short term, *inherited loop action*; brief §11(c) lists it. Also, "quadratic term" is now the short term for a channel `d` (9:544), so the edit created a collision within chapter 9. | "is the inherited loop action." |
| 9:723 (first use) | DICTIONARY | — | — | *reset*: the Literature line states "The difference is stated at first use: Bałaban defines `g_{k+1}` by the β-function, v3 defines `β = β′+α+Δ` …"; 9:717 is the first use in the book of *coupling constant renormalization* / *vacuum energy renormalization* (grep over ch. 1–8, MT, RG: none). The editor added no sentence. | Sentence prepended to line 723 (see Corrections). |
| 9:17 | LANGUAGE | "The actual incoming inverse coupling is" | "The incoming inverse coupling, unlike the reference value $\mathfrak b$, is $\beta'\in[\mathfrak b/2,2\mathfrak b]$" | "unlike 𝔟, is in [𝔟/2,2𝔟]" reads as if 𝔟 were not in that interval. | "…, which need not equal the reference value $\mathfrak b$, is" |
| 9f:865 | LANGUAGE | "transports the quadratic expression $a_dP_d$ with its channel." | "… with its term." | "with its term" is empty after the channel was renamed; ambiguous. | "… together with its quadratic term." |
| 9:176 | MINOR (consistency) | "before performing either expansion." | unchanged | With "first expansion"/"second cluster expansion" gone, "either" has no antecedent pair until 9:192. | "before performing the Mayer expansion and its exponentiation." |
| 9:190 | LANGUAGE | "The gap $19/16-23/20=3/80$ absorbs" | "The difference $19/16-23/20=3/80$ of the exponents absorbs" | Postposed "of the exponents" after a formula. | "The difference of the exponents, $19/16-23/20=3/80$, absorbs" |
| 9:234 | LANGUAGE | "an inherited term is anchored at the coarse site" | "an inherited term has as base point the coarse site" | Awkward construction. Words only. | "an inherited term has its base point at the coarse site" |
| 9:442 | LANGUAGE | "its bounds are the concrete interface for" | "its bounds are the statement used in" | Plural subject with "are the statement". | "its bounds form the statement" |

Checked and found correct (no change), by topic:

- **9f, all 65 lines** compared one by one: apart from 9f:125 (restored above) every change is a house word only: scalar (factor) → normalization constant / constant (28, 104, 235, 244, 449, 927); regular activities → localized terms (71, 546, 548, 586, 842, 888); anchor(s)/anchored → base point(s)/with base point(s) (88, 97–100, 298, 303, 491, 495, 512, 518, 543, 547–550, 580–592, 607–612, 660, 864, 896, 960); channel(s) → term(s) (287, 488 title, 491, 503, 591, 863, 889) and "quadratic term" at 866; dependence region → set (230, 329, 682, 716, 933); first expansion / first polymer activities → Mayer expansion (207, 446); selections → index triples (341, sense 1, as 6:85); rows → components (133); folding map → reflection map (627, 681, 710; as 9s:175); logarithmic → large-field / correction (871, 875); selection → family (874–875, sense 4); support reserve → margin in the decay rate of the support weight (615, 960); "costs … a polynomial" → "contributes … a polynomial factor" (614, 960); regrouping → exact regrouping (918, which is the operation of Proposition ch09:fusion-prop covered by Prop. ch09:output-equivariance). 9f:543 ("with base points there. The resulting family") is the same statement. Assumption (a)–(f), lemmas, propositions and proofs are otherwise identical.
- **Theorem ch09:step-theorem (9:909–952)**: hypotheses and conclusion unchanged in content: "the free quadratic forms of two consecutive scales" (as 6:946), "the gauge-covariant averaging operation", "path action", "eligibility conditions", "margin in the decay rate of the support weight", "inhomogeneous term" (6:1558), "base points", "lower bounds on the ratio / on the reference coupling / on the period", "original" torus/period (actual sense 9), "ultraviolet cutoff", "commutes with restriction of the parameter interval", 949 repair words only. The forest-average lines of 24 November (75, 148, 161, 234, 239–240, 313, 331, 351, 362, 367, 398, 521, 525, 867, 903, 919, 924–926, 955) keep their content; 239 "actual integral" → "block integral" names the same integral (𝒵_blk).
- **attachment**: 9:150 "Components attached to" unchanged (correct, sense 1/ordinary verb); 9:697 → "site norm" (norm sense; the norm of 9:659 = 9:602/607); 9:794 "strict margin in the site-norm bound" (the slack in `(2B+1)^4γ ≤ 1/2` of 9:701–702, γ being the site-norm bound): kept; 9:687 restored.
- **seeded/unseeded (9:283–284)**: matches 6:1544 as committed ("a sector with nonempty index triple … the law with empty index triple"). Note for the author: the unseeded law has `A_f = A_n = ∅` but `A_c` equal to the coarse large-field set (dictionary *seeded sector*), so "empty index triple" is exact only if `A_c = ∅`; the same wording stands in 6:1544, so chapter 9 follows it.
- **reset**: 9:717 names both (coupling constant renormalization ↔ `β = β′+α+Δ`, vacuum energy renormalization ↔ `v_sc`) in the order of the display: correct. 9:748 "the coupling constant renormalization $\Delta$": the dictionary's proposal for this line, with `Δ` (the quantity identified, 9:763); kept although it inserts `$\Delta$` (it is a vocabulary proposal, not a sentence repair). `C_reset` and labels untouched.
- **Mayer / exponentiated cluster expansion**: 9:44, 89, 148, 173; 9f:207, 446 Mayer; 9:192 "exponentiated cluster expansion"; 9:176 now "the Mayer expansion and its exponentiation". Consistent with the table (*exponentiation* (*exponentiated cluster expansion*)). No difference from Bałaban is recorded for these (Literature: same object), so no first-use sentence.
- **regular activity**: every replaced occurrence in `9` and `9f` is sense 1 (incoming/outgoing local terms `(X_i,o_i,E_i)`, `G_x`, `R(U_p)` at the Wilson start, Definition ch09:equivariant): *localized term* correct. The chapter-8 polymer activities (sense 2) appear in ch. 9 only as "ordinary gas/polymers/factor" → "polymer gas" (9:150), "small-field polymers" (9:153), "elementary small-field factor" (9:172) and as "polymer activities of the Mayer expansion": correct.
- **threshold**: changed occurrences 9:145, 202, 430, 709, 901, 929 are all coupling thresholds (9:901: smallness of `e^{-cβt²}` needs `β̂_N` large). The small-field threshold `t` and "reference thresholds" (9:19) unchanged.
- **cutoff failure**: 9:111 "event labels" (6:835), 9:133 "large fluctuation-field event at a distinct event label", 9:280 "a large fluctuation-field event far from the index triple" (remote sense 1; cf. 6:1008 "far from the location of A"): all sense 1. No sense-2 occurrence in these files.
- **short terms**: *large-field correction* (9:367–369) is defined once, with "a term of the exponent" (true: the `ℓ_a` of 9:633 include `L_x`); used consistently at 9:432, 607–608, 630, 633, 638 ("correction labels"), 671, 677, 698; 9f:871, 875; agrees with 10:570 ("large-field correction terms in the exponent"). Not a first-use sentence about Bałaban (his *boundary terms* are only suggested by the dictionary, not adopted). *quadratic term* `d` (9:543–544) used consistently; collision with 9:26 removed. *auxiliary standard Gaussian coordinates* (9:59) / "auxiliary Gaussian integral" (9:72): fine. *margin in the decay rate of the support weight*: chapter 8's phrase (8:150, 331, 362).
- **selected**: sense 5 kept everywhere because of `{\rm selected}` in 9:319–320; consistent. Senses 1/4 converted (index triple; family, subfamilies, chosen).
- **Appendix D repairs** at 81–82 (allocation weights), 124 (table header), 140 (resolvent identity), 220 (support with its adjacent plaquettes), 231 (coarse image of the support), 283–284, 949 (words only, no `\eqref{ch10:drift-floor}`): words only, nothing inserted. The repairs of 9:77 and 9:147 (formulas) and 9:893–894 were rightly not applied.
- **Symbols inserted by the edit** (all checked): 9:17 `𝔟` (already on the line); 9:108 "belonging to $M$" (`A_M` on the line); 9:517 `ζ_f` (dictionary *discrepancy* 1, R, proposes "the indicator corrections `ζ_f`"); 9:748 `Δ` (see above); 9:970 `\eqref{ch07:classical-budget}`, `\eqref{ch07:inherited}` (dictionary entries *classical bound contraction*, *inherited-loop contraction*, R, propose exactly these; verified 7:1055, 7:1084). 9:83 `α` removed (TERM above).
- **Agreement with chapters 1–8**: step, consecutive scales, representation data, averaging operation, dependence set, auxiliary index, index triple, sector, event label, large fluctuation-field event, eligibility/additional conditions (4:448–450, 6:83), prescribed large-field set (8:288), zero-mean (6:851), inhomogeneous term (6), lower bound on the reference coupling (6:322, 411, 432), rescaled activities (8:170), base point / anchored (4:603, 8:76), scaling dimension: all as committed. "attributed" (9:280, 672, 877, 885, 889) follows 8:288; chapter 6 still says "assigned" for action terms (6:1329 ff.) — not a conflict of object names, noted only.

## Corrections applied

`9`:
- 17: "The incoming inverse coupling, which need not equal the reference value $\mathfrak b$, is"
- 26: "$\mathcal L$ is the inherited loop action."
- 83: "every Haar coordinate, auxiliary index and Gaussian covariance"
- 176: "$h=\mathfrak b^{3/8}$ before performing the Mayer expansion and its exponentiation."
- 190: "The difference of the exponents, $19/16-23/20=3/80$, absorbs the remaining subpower factor."
- 234: "an inherited term has its base point at the coarse site whose block contains its incoming base point and is not divided into shares"
- 442: "Equation \eqref{ch09:early} and its bounds form the statement"
- 547: "clipped expression or expression restricted by its event indicator. Its support $Y_d$"
- 687: "… One additional unit of the decay rate of the support weight bounds the number of attachments, since a support has at most"
- 723 (first-use sentence, prepended): "These are Ba{\l}aban's names~\cite{Balaban1987RG,Balaban1988Expansions}; he defines the next coupling through the beta function~\cite{Balaban1987RG}, whereas here the increment of the inverse coupling is the coefficient $\alpha$ fixed by the matching plus the coefficient $\Delta$ of the local quadratic subtraction." Basis: dictionary *reset*, Literature line (B87 p. 268 "coupling constant renormalization", (0.18); B87 p. 258 and B88b p. 279 "vacuum energy renormalization"; keys `Balaban1987RG` = B87, `Balaban1988Expansions` = B88b, both already in references.bib). It claims only that the names are his and that he defines the next coupling by the beta function. `α` and `Δ` are those of the display 9:719 just above.

`9f`:
- 125: "for the derivative of the averaging operation" (restored "derivative").
- 865: "the quadratic expression $a_dP_d$ together with its quadratic term."

## Left for the author

- 9:283–284 (and 6:1544): "the law with empty index triple" — the unseeded law keeps `A_c` = coarse large-field set; the dictionary's "the law of the sector with empty selection" (or "with `A_f = A_n = ∅`") would be exact. Changed in neither chapter; a chapter-6 decision.
- 9:748: "the coupling constant renormalization $\Delta$" — `Δ` is only the projected part of the coupling increment `α + Δ` named so at 9:717; the dictionary proposes this wording. Alternative: "identify the coefficient $\Delta$".
- 9:717: "are now fixed by the coupling constant renormalization and the vacuum energy renormalization:" — acceptable; the author may prefer "are now fixed; these are the …".
- 9:153 "a chosen large-field region": the dictionary files 9:153 under *selected* sense 1 (index triple); the editor took sense 4. "chosen" is neutral and not false; left.
- 9:547: my repair keeps "clipped … or … restricted by its event indicator" as two kinds of term; if the author prefers, name them ("the clipped plaquette term or the row-square term with its indicator").
- All items in the editor's "Not changed, for the author" list stand (selected sense 5 vs `{\rm selected}`; shares; labels; 9:77/9:147/9:893 repairs with formulas; 9:913 transport identities and the representative of `W`; etc.).

## Words this file introduces that other chapters may also define

- *coupling constant renormalization*, *vacuum energy renormalization* (first use in the book, 9:717; first-use sentence 9:723). Chapter 10 (being converted now) uses "coupling constant renormalization" at 10:446, 651, 772, 816, 902 — it must not repeat the first-use sentence.
- *Mayer expansion*, *exponentiated cluster expansion* / *exponentiation* (first use, 9:44, 192).
- *large-field correction* (defined 9:367–369; 10:570, 658 use "large-field correction terms/factors").
- *quadratic term* `d` of the path action (9:543–544); *correction labels* (9:638).
- *auxiliary standard Gaussian coordinates* (9:59); *indicator corrections* `ζ_f` (9:517); *residual of the mean equation* (9:77, 130).
- *inherited loop action* is used here as defined in 7:237.

## Checks

- `wc -l` 09-renormalization.tex → 979 = `git show HEAD:… | wc -l` 979; 09-forest-average.tex → 973 = 973.
- `git diff --numstat`: 09-forest-average.tex 65/65; 09-renormalization.tex 184/184 (182 from the editor plus 176 and 723 here; 190, 442 were already changed). Also listed: 10-common-trajectory.tex 160/160 and 11-marked-insertions.tex 463/463 — other agents' files, not touched.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3) → "51 files; 679 labels; 1223 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build-c1 monograph.tex` → exit 0. In monograph.log: `grep -ci undefined` 0; `grep -c Citation` 0; `grep -c Overfull` 0. The build included the other agents' current edits to chapters 10 and 11.

## Not checked

- Rendered PDF pages were not inspected visually (no pdftotext used).
- The Bałaban citations rest only on the dictionary's *Literature* line; the papers were not reread.
- Chapter 9s (09-stationary-remainder.tex) and chapter 10 were not reviewed, only grepped for consistency of terms.
