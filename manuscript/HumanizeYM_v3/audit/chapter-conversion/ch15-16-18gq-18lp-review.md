# c7 review: chapters 15, 15sp, 16, 18gq, 18lp

Reviewed the uncommitted edit in /Users/mgubi/ym-terminology (word diff read first, editor's report c7-apply.md afterwards), against the dictionary manuscript/HumanizeYM_v3/audit/terminology.md and the committed text of the main theorem, the reading guide and chapters 1–14. Corrections were applied within lines; no other file was touched.

## Review findings

| file:line | class | old (committed) | edited | what was wrong | corrected |
|---|---|---|---|---|---|
| 15:262 | ERROR | "only the cutoff and translation thresholds depend on" | "only the lower bounds on $N$ and on the translations depend on" | inserts the symbol `$N$`, absent from the committed line (rule 11a) | "only the lower bounds on the cutoff and on the translations depend on" |
| 15:275 | MINOR (content lost) | "a fixed finite-row constant if necessary" | "a fixed finite constant if necessary" | the dependence of the constant on the finitely many rows (now "tests") was dropped | "a fixed constant depending on the finitely many free tests, if necessary" |
| 15:276 | LANGUAGE | "These are estimates uniform in the number of reflected copies, stronger than a bound on the mixed mean." | "These estimates have constants independent of the number of reflected copies, stronger than …" | the apposition "stronger than a bound on the undecomposed mean" no longer has a noun to attach to | "These are estimates with a constant independent of the number of reflected copies, stronger than …" (the dictionary's phrase) |
| 16:260–261 | LANGUAGE | "with its entire finite-dimensional label action" | "with the entire finite-dimensional action on fields" | "finite-dimensional action" is not what is meant (the field spaces are finite-dimensional); differs from 16:153 | "with its entire action on the finite-dimensional field spaces" (as 16:153) |
| 16:87, 117, 150 | MINOR (consistency) | "when tested", "after testing", "Testing" | "when paired with test functions", "after pairing with a test function", "Pairing with test functions" | integration against test functions; the same edit says "smeared" at 16:151 and 16:300, and keeps "paired with" for exterior words (16:46) | "when smeared with test functions", "after smearing with a test function", "Smearing with test functions" |
| 18lp:27 | ERROR (sharpened) | "a remainder with vanishing extracted coefficient of norm $r_l$" | "a remainder of norm at most $r_l$ whose extracted coefficient vanishes" | "at most" added; the repair was to be word order only | "a remainder of norm $r_l$ whose extracted coefficient vanishes" |
| 18lp:36–37 | ERROR (sharpened) | "In detail a remainder with vanishing extracted coefficient of size $q$ has / output coefficient and remainder at most $L_l^{-2/5}q$." | "In detail, if a remainder … has norm at most $q$, then its / output coefficient and output remainder have norm at most …" | "of size q" became "norm at most q"; more than word order | "In detail, a remainder of size $q$ with vanishing extracted coefficient has / output coefficient and remainder at most $L_l^{-2/5}q$." (line 37 is back to the committed wording) |
| 18lp:210 | MINOR (content lost) | "the required source monomial in the marked sum costs $\varpi^{-1}$" | "the required source monomial contributes the factor $\varpi^{-1}$" | "in the marked sum" dropped | "the required source monomial in the sum with insertions contributes the factor $\varpi^{-1}$" |
| 18lp:216 | not a vocabulary change | "All the terms involving at least two insertions" | "All the terms of source degree at least two" | equivalent, but it is not a house word and the original was plain | restored "involving at least two insertions" (the change "transport → transfer" on the same line is kept) |

Checked and found correct (no change):
- Phase, compression, `𝔄`: 15:8–10 (definition of a phase untouched; "compressions of concatenated words" is the *whole word* proposal), 15:91 (title "The compression algebra" was committed), 15:155 "characters of the compression algebra" (App. D repair, words only). 15:129 and 15sp:10 "concatenated" correct.
- Zero-energy subspace: 15:47 ("the zero-energy subspace of the mixture; it does not say that this space is one dimensional" kept), 15:305 "zero-energy projection", 16:379 "zero-energy subspace is a line". No sentence says "the vacuum" where the committed text had the subspace. 15:301 title "Selecting a phase with a unique vacuum" (house word "ground vector" replaced; the section proves `ker H_ξ = ℂΩ_ξ` a.e., i.e. vacuum uniqueness, as 15:156 already says) does not claim more than the section. 15:167, 213, 15sp:15 "vacuum expectations" are expectations in `Ω`, correct (*moment* 3).
- "label → field": 15:109, 119, 178, 316 and 16:19–20, 36, 83, 132, 153, 260–261, 369, 373, 515, 520 are elements of `F_d`/`F` (sense 2), as chapter 14 (committed) already writes the entries of words as "fields" (14:23–26). 16:345 "the map from F to the field operators is injective" is sense 9 (the map `A ↦ Φ_ξ(A,·)`); its proof (16:369–373) shows exactly this. Polynomial labels kept where meant: 15:278 "fixed free labels", 18gq:13, 48, 96, 106; 18lp:17, 228, 295, 303.
- "undecomposed": gloss at 18lp:8 ("the undecomposed correlations, before any decomposition into phases") agrees with *mixed* 1 and 15:5–6, and chapter 14 (committed) uses the adjective the same way (14:12, 165, 263, 349, 820, 946). 15:24 "undecomposed reflection Hilbert space" follows 14's attributive use.
- "paired with" for correlations with exterior words/probes (15:243, 248; 16:46; 18lp:307, 310, 320–321, 330); "smeared" for test functions (16:151, 300).
- In-place definitions: 16:48 "heights (imaginary parts)", 16:53 "the smallest gap between heights" (meaning of *gap* 2 unchanged), 15:325 *exceptional phases* (exactly the dictionary's sense: not shown that uniqueness fails), 16:291 "a word is a finite ordered list of letters" (App. D repair, words only).
- 16:64, 16:118: `\eqref{ch16:slabs}` / `\eqref{ch15:mixture}` replace the names "padding" / "barycenter identity" (App. D, cited by number; no new symbol).
- 18lp: "unmarked gas" → "exact-cover gas of the density without insertions": the same name as 12:180 and 9:593 (committed); the gas is a polynomial in the *total large-field activities* (12:180–181), so the two names denote different objects and are used consistently. "probe" kept for the word (18lp:269, 293, 321, 332). "finest scale" (18lp:46, 63) is the fine end `m`. "cost" → adds / contributes the factor / exponent / bound / loses: each fits its line. "lower bound on the block ratio" (18gq:25; 18lp:41), "lower bound(s) on the reference coupling" (18lp:101, 116, 148, 151) agree with chapters 6, 9, 11R, 14lc. "transfer" only for moving coefficients through the steps (18gq:13, 76, 84; 18lp:24, 47, 197, 216). "stopping scale" (18lp:159) as 13sb:102. "change of cover radius" (18lp:112) as 11:515, 11R:281. "backward comparison" (18gq:105; 18lp:34) as the section title 11:890. "link support" (18gq:102) as chapter 11. "reference scale", "cutoff scale" as 11–12.
- 18gq "responses" (111, 113, 130) are values of correlation functionals; chapter 13 (committed) says "correlation functional" for the map (13:120) and "responses"/"separated responses" for values (13:9–10, 151, 161, 177, 183). 18gq agrees; nothing to change.

## Corrections applied

1. 15:262 symbol `$N$` removed: "lower bounds on the cutoff and on the translations".
2. 15:275 "a fixed constant depending on the finitely many free tests, if necessary".
3. 15:276 "These are estimates with a constant independent of the number of reflected copies,".
4. 16:87, 117, 150 "smeared / smearing with test function(s)".
5. 16:260–261 "with its entire action on the finite-dimensional / field spaces, therefore".
6. 18lp:27 "a remainder of norm $r_l$ whose extracted coefficient vanishes".
7. 18lp:36–37 "In detail, a remainder of size $q$ with vanishing extracted coefficient has / output coefficient and remainder at most $L_l^{-2/5}q$."
8. 18lp:210 "in the sum with insertions contributes the factor".
9. 18lp:216 "involving at least two insertions" restored.

## Left for the author

- 18lp:27, 36: App. D B6 (and the source, Scott J:45, "r_l is its remainder bound") reads "norm at most"; I applied word order only, as instructed. Whether to write "at most" is the author's decision.
- 15:275, 278 "test(s)" for the reference rows (*row* 8: basis I for the reading, S for the object) collides with the reservation of *test* for test functions (*test* 1). Kept the editor's word; alternative: "member of the separating family".
- 15sp:6, 24 "loss in the exponent" vs 13sb:6–7 (committed) "the loss … can be reduced to an arbitrarily small excess": the same quantity is "excess" in 13sb and "loss" in 15sp and 18lp:334. Harmonise one way or the other.
- 18lp:73 vs 74, 184, 245: "the coefficient of every source monomial" next to "partial modes" (basis I, kept): the reader meets "modes" without the word "mode" being introduced.
- 18lp:86 "attributed" vs 18lp:88 "assignments" (dictionary proposal applied at 86 only).
- 18lp:134 "loses at most the factor $L_l^{-4n}$": the direction of "at most" with a factor below one was already unclear in the committed text.
- 18lp:226 "full dependence supports" → "dependence sets" drops "full"; acceptable if the dependence set of chapter 4 is meant (I believe so).
- The editor's own "not changed" list (c7-apply.md) stands.

## Words this file introduces that other chapters may also define

- *undecomposed* (gloss at 18lp:8; chapters 14, 17-trace-law, 18-operator-products and 19 use it).
- *height*, *gap* (16:48, 53), *exceptional phases* (15:325; 19:107 "exceptional vacua" refers to it).
- *word* of letters (16:291; 17:34, 44 and 19:105 use it).
- *free tests* (15:275–278).
- *exact-cover gas of the density without insertions* (18lp:186; 12:180, 9:593).
- *stress flux*, *flux identity* (15:245; 16:538, 558; chapter 17 "shell" uses, 17:99, 17w:122).

## Checks

- Line counts (`wc -l` vs `git show HEAD:<path> | wc -l`): 15-phases 342/342, 15-sharp-phase-bounds 26/26, 16-reconstruction 558/558, 18-graded-quotient 131/131, 18-lattice-products 352/352.
- `git diff --numstat` for my files: 47, 8, 63, 26, 92 changed lines (18lp:37 is back to the committed text). Chapter 17 files are modified by other agents; untouched by me.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1242 references. All explicit cross-references resolve; no duplicate labels." exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-c7 monograph.tex`: exit 0. In monograph.log: "undefined" 0, "Citation" 0, "Overfull" 0. (The build includes the other agents' uncommitted chapter 17 files.)
- Rendered text (pdftotext) checked at 18lp:36 and 18lp:210 and 15:262.

## Not checked

- The Lean and source manuscripts (only the dictionary's Source lines were used).
- Rendered pages were not inspected visually beyond the text extraction above.
- Whether "free tests" (15:275–278) are the same family as the rows of 13:168, 182 and 14:277 (the dictionary also leaves this open).
