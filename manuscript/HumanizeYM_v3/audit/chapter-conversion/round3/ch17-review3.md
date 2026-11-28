# Third review, chapter 17 fragments (t10)

Files (under /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/): 17-trace-law (17), 17-variable-windows (17w), 17-trace-transfer (17t), 17-current-contraction (17c), 17-marked-trace-rates (17m). Changed lines 4f462ac5..HEAD examined: 48 + 45 + 49 + 111 + 135 = 388, each against the old line and the present context. The diff was read before the earlier reports and the leads.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 17m:68 | TERM | identity for the full source | identity for the full insertion | The object is the differentiated kernel `𝒟_Y k` of (17.kernel-divergence), the factor whose integral against every spectator is zero; "insertion" is the book's word for a local observable (1:331; 3:92) | identity for the full differentiated kernel |
| 17m:72 | TERM | an admissible marked conditional integral | an admissible conditional integral with insertions | The inserted factor is `𝒟_Y k` (the next line: "a finite sum of smooth local kernel scores times `Y`"), not observables | an admissible conditional integral with the differentiated kernel inserted |
| 17m:84 | TERM | that marked integral | that integral with insertions | Same integral as 17m:72 | that conditional integral |
| 17m:120, 122 | TERM | the marked component / the marked connected component | the component of the insertion | Component containing the kernel score | the component of the differentiated kernel |
| 17m:121–123, 127, 129 | ERROR | failure anywhere in the marked connected component … distant failure … complementary marked sum … this new failure … exponential failure probability | violation of a regularity condition … distant violation … large-field sum with insertions … this new violation … exponentially small probability of the violation | "Regularity condition" is reserved for the plaquette condition; the failures here are failures of smooth chart cutoffs ("their derivatives are supported where at least one enlarged chart condition fails"), bounded by a Gaussian or energy estimate, while the incoming large-field sets are retained separately. Whether every "failure" in 121–122 is only a cutoff failure (large fluctuation-field event) or also includes incoming large-field sites is not settled by the text, so the old word is restored | Every term with a failure anywhere in the connected component of the differentiated kernel, including a distant failure joined to the score, is kept in the complementary sum. … bounds this new failure … where the exponentially small failure probability absorbs |
| 17m:128, 321 | ERROR | these complementary terms / the complementary part | these large-field terms / the large-field part | Same terms as above; "large-field" names the large-field set proper (6:7–11) | these complementary terms / the complementary part |
| 17m:131 | ERROR | the ordinary cancellation and the complementary large-field estimate | the small-field cancellation and the large-field estimate | "complementary" dropped (the estimate is the one for the complementary terms just described) | the small-field cancellation and the complementary large-field estimate |
| 17m:87 | ERROR (dropped word) | Fix the full dependence region | Fix the dependence set | "full" dropped by the second review; it contrasts with the score stencil (17m:118), and the harmonisation kept "full dependence set" book-wide (6:1179, 1324; 9:93) and recorded 17m:87 as "full" | Fix the full dependence set |
| 17m:155 | TERM | the full zero-exterior-moment source | the full insertion with zero exterior moments | `𝒟_Y k` (its coefficient is `Σ_k − βj_k`) | the full differentiated kernel, with zero exterior moments, |
| 17m:391 | ERROR (dropped word) | The source is carried as a density-valued kernel insertion | The insertion is carried as a differentiated kernel | "density-valued" lost; that is the point of the sentence (not divided by `F`) | The differentiated kernel is carried as a density-valued factor |
| 17m:412 | TERM | the source to a spectator | the insertion to a spectator | `𝒟_Y k` | the differentiated kernel to a spectator |
| 17m:441 | DICTIONARY | The physical mark normalization | The normalization of the insertion in continuum units | Sense 2 of *physical* (the factor `a^{-d}`), whose book-wide word is "dimensionful" (11:86 "the dimensionful normalization"); "in continuum units" is sense 1 | The dimensionful normalization of the insertion |
| 17m:443 | TERM | the full zero-moment source | the full insertion with zero exterior moments | `𝒟_Y k` | the full differentiated kernel with zero exterior moments |
| 17m:459 | TERM | The same source identity | The same identity for the insertion | `𝒟_Y k` | The same identity for the differentiated kernel |
| 17w:71 | MISMATCH | uniform in the actual free history | uniform in the free history | "free history" defined nowhere; the very statement in chapter 11 (11:1699, proof of (11.finite-covariance)) says "uniform in the kernel history" | uniform in the kernel history |
| 17w:78 | ERROR (narrowed) | The regular and large-field source recurrences | The step estimates (ch11:lower-weighted-step) in the regular and large-field norms | Cites only the lower recurrence; chapter 11 has an upper recurrence too (11:1541–1544, 1643) and calls the pair "the upper and lower recurrences" (11:2135) | restored: The regular and large-field source recurrences |
| 17w:120 | MISMATCH | The full-copy estimates | The estimates uniform in the number of reflected copies | 17:130 (same chapter) and chapters 15, 18 say "with constants independent of the number of reflected copies" | The estimates with constants independent of the number of reflected copies |
| 17c:359–360 | ERROR | within the predictor (later: gauge-covariant block average) and averaging patches | within the patches of the averaging operation and the averaging patches | Names the averaging operation's patch twice. In the bound just displayed the two kernels are `M_{ef}` (differential of the averaging operation) and `K_0`, whose multiplier 17c:76 calls the "averaging multiplier"; the original draft (89c513b3) reads "predictor and averaging patches" | within the patches of the averaging operation and of the base-point average |
| 17m:2 (title) | TERM | marked coefficient estimates | coefficient estimates with insertions | The coefficients are those of the expansion with `𝒟_Y k` inserted. A title: | left for the author (suggest "… to coefficient estimates for the differentiated kernel") |
| 17m:150, 176, 381 | TERM | exact marked step; marked remainder; marked error bounds | exact step with insertions; remainder with insertions; error bounds with insertions | These name the chapter 11 operation (step with insertions), its remainder `E_mark` and its error bounds, applied with `𝒟_Y k` as inserted factor. The machinery is the chapter 11 one, so "with insertions" is defensible; 381 reads awkwardly | left for the author |
| 17m:193, 265, 291, 303, 307 | TERM | regular local sources; coefficient source; regular source | regular local insertions; insertion coefficient; regular insertion(s) | These are the local regular terms of the score (`div_Haar Y − D𝓛[Y]`, …) whose coefficient is extracted, not `𝒟_Y k` itself and not observables. No short book word exists | left for the author |
| 17t:145 | TERM | retained as marked remainders | retained as remainders with insertions | Sense 3 of *mark* (the differentiated terms of smooth truncations, carried with the kernel score); "differentiated kernel" is introduced only later (17m) in book order | left for the author |
| 17:281, 295 | MISMATCH | the common family; same-family | the same family of measures | 17:100 (same chapter) says "lattice family" | left for the author (one name) |
| 17w:97 / 17m:433 | MISMATCH | positive partition estimate / actual positive-density estimate | unchanged / lower bound on the partition function | Two names; identity of the two has basis I | left for the author |
| 17c:71 | MINOR | the actual anchor average `K_0` | the base-point average `K_0`, the average over translates of the base point | Added gloss; `K_0 = ∏M_aN_a` has signed coefficients (`c_2 < 0`) with sum one (17c:324), so "average" is loose | left for the author |
| 17m:409 | MINOR | an actual exponentially local spectator | an exponentially local spectator that need not have finite range | Added qualifier (basis I); implied by "first truncate" | left (as the second review) |
| 17c:46 (title) | MINOR | Preservation of the low moments | Preservation of the order of vanishing | Title reworded although no house word was in it; the new title is accurate (order four retained) | left for the author |

All other changed lines were found correct, including: 17m:13, 56 (local gauge transformations), 27–34, 70 (gloss of "exterior moments", true by 17m:67–68), 136–144, 202–232 (zero/nonzero alias), 249, 251, 263–264 (not touched, assignment c), 276–301, 354–362 (mass regularization; 17:227–232), 375, 380, 426–444, 461, 469, 474, 476; 17:23–44, 84–86, 97, 119–146, 194 (gloss "defect of the lattice Ward identity", consistent with (17.regulator-input) and 17t:411), 227, 235, 246, 308–309, 341 ((14.conserved-line) exists, 14:293), 370; 17w:6–7, 11, 22–24, 36–43, 59–68 ("conjugated" matches 11:1788 "the conjugated coarse covariance `B_0 = 𝓛κ𝓛^T`"), 84–103, 115–118, 122, 124; 17t:3–43, 85–126, 157–163, 178–226, 291–360, 404–498; 17c:8–13, 43, 48–53, 61–68, 72–87, 112–113, 132–216 (148: "joint classical action" is 7:872's name), 164–166 (not touched), 225–300 (288–290 "penalty term" = 7:874), 312–396.

## Corrections applied
- TERM: 8 (17m:68, 72, 84, 120, 122 [kernel part], 155, 412, 443, 459 — counted as 9 lines, 8 findings)
- ERROR: 6 (17m:121–123/127/129 failure; 17m:128/321; 17m:131; 17m:87; 17m:391; 17w:78; 17c:360)
- DICTIONARY: 1 (17m:441)
- MISMATCH: 2 (17w:71, 17w:120)
- Total lines edited: 17m 19 lines, 17w 3 lines, 17c 1 line. Line counts unchanged (480, 125, 396; 17 and 17t not edited).

## Cross-chapter mismatches not fixed
- "the same family of measures" (17:281, 295; 18:172; 19:46) / "lattice family" (17:100; 1:371–503; 14lc:2; 15:251).
- "positive partition estimate" (17w:97) / "lower bound on the partition function" (17m:433).
- "interval of scales" (17w:2, 7, 37, 49, 97, 102, 107, 124; 17m:429) / "comparison window" (chapter 11, 11R, 14lc:23); also `\text{ in window}` in (17.window-product), 17w:54–56 (math, not editable).
- "column constants with insertions" (17w:11) / "ratio-independent coefficient-map factors" (17m:428) for the same constants `C_j`.
- "large-field event" (17m:330, unchanged) / "large fluctuation-field event" (6, 9, 10, 11, 11R): whether the large-field event or a cutoff failure is meant is not settled; together with "The common large-field estimate" (17m:322).
- "anchored" kept at 17:224 and 17t:482; elsewhere chapter 17 says "with a base point".

## Leftover house words
Kept on purpose: 17t:195 "left frame" (*frame* sense 3, basis I); 17m:237 "physical row" (sense 5, position space, basis I); 17c:287 "stationary value" (envelope theorem, ordinary); 17t:14, 29, 205, 392 "unit" (unit vector/translation, ordinary); 17m:331–332, 413, 416 "units" (ordinary); 17c:122, 197, 381 and 17w:89, 17m:440 "weight(s)" (ordinary exponential weights; source weight is a kept term); 17m:246 and 17c:161 "mixed" (ordinary).
Not settled, left for the author: 17t:12 title "Difference-preserving block averages" (`M_a` are plain means, not the averaging operation); 17m:26, 163 "stationary kernels" and 17c:55 "exact stationary identity" (object not fixed by the dictionary; `E_stat` depends on the first).
Replaced: none beyond the corrections above (the leftovers "marked", "source" in sense of the kernel were all handled under TERM).

## Leads
- 17c:359–360 (part 1 lead 1; appendix agent): verified; corrected to "of the base-point average" (see Findings).
- 17w:71 "free history" (part 1 lead 4): verified; corrected to "kernel history" (11:1699).
- "comparison window" / "interval of scales": verified; left (title and author's choice).
- 17m:121–131, 321 (part 2 lead 2; appendix): verified; "violation of a regularity condition" and "large-field sum/terms/part" were wrong; old words "failure", "complementary" restored (whether the failures are all large fluctuation-field events is left open).
- "insertion" for `𝒟_Y k` (part 2; part 3 lead 4; part 4 lead 2): verified line by line; at 68, 72, 84, 120, 122, 155, 391, 412, 443, 459 replaced by "differentiated kernel"; at 2, 81, 150, 176, 381, 393, 411, 418 the phrase names the chapter 11 step/expansion or genuine observable insertions (393: incoming coefficients `f_A`; 418: density without insertions) and is kept; 193, 265, 291, 303, 307 listed.
- 17w:68 "conjugated" (part 3 lead 3): verified correct; chapter 11 calls `𝓛κ𝓛^T` "the conjugated coarse covariance" (11:1788).
- 17m:441 (part 4 lead 1): verified; now "dimensionful normalization".
- 17w:97 / 17m:433 (part 4): verified two names; left.
- 17w:78 (part 5): verified narrowing; old wording restored.
- 17w:120 / "reflected copies" (part 6): fixed to the 17:130 form.
- 17w:122 "these same comparison isomorphisms": in book order 17w is input at 17:150, after 17:81–82 ("Let `U_{i,d}` … be real comparison isomorphisms"), so the antecedent exists 40 lines earlier in the same section. Left as is.
- "stencil" at 17m:119: "score stencil", contrasted with the full component; left.
- 17:281/295 "same family of measures" vs "lattice family": left (above).
- "transfer: still transport…": no "transport" remains in the prose of my files (17t:3 title now "transfer").

## Assessment of earlier corrections
- Second review, 17m:87: removing "full" was wrong in my view (old word dropped; the harmonisation kept "full dependence set" and recorded 17m:87 with "full"); restored.
- Second review, 17c:75 "average `M_a`": acceptable.
- Second review, 17w:97 "coarsest scale": correct.
- Second review, 17t:145 "remainders with insertions": transfers the kernel sense of *mark* into "insertion"; listed for the author.
- Harmonisation did not touch chapter 17; its report items for 17m:312, 316, 332, 413 are in the text and correct.
- 17w:78 (reference to a single equation for "recurrences") was passed by both reviews; corrected now.

## For the author
1. Title 17m:2 and the phrases "step/remainder/error bounds with insertions" (17m:150, 176, 381): with "differentiated kernel" now used for `𝒟_Y k`, decide whether these should read "with the differentiated kernel inserted".
2. 17m:193, 265, 291, 303, 307 "regular local insertions", "insertion coefficient": the local regular score terms; a name is needed if "insertion" is to keep one meaning.
3. 17m:121–122: is every "failure" in the connected component a cutoff failure (then "large fluctuation-field event"), or also an incoming large-field site?
4. 17t:12 title, 17c:46 title, 17w:2 title.
5. 17m:26, 163 "stationary kernels"; 17c:55 "stationary identity".
6. One name each: lattice family / same family of measures; positive partition estimate / lower bound on the partition function; `C_j` constants (17w:11 vs 17m:428).
7. 17c:71 gloss "average over translates" for a combination with signed coefficients.

## Checks
- Line counts equal to HEAD: 17-trace-law 458, 17-variable-windows 125, 17-trace-transfer 500, 17-current-contraction 396, 17-marked-trace-rates 480 (wc -l, identical to `git show HEAD:… | wc -l`).
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/v3build-t10 monograph.tex`: completed (exit 0, 5 runs). Log: "undefined" 0, "Citation" 0, "Overfull" 0. (The working tree also contains other reviewers' concurrent edits to chapters 6–9.)

## Not checked
- Rendered pages: pdftotext and pdftoppm are not installed, so the PDF pages were not inspected visually.
- Literature claims: none added or changed in my files.
- Lines of 24 November (17c:48–53, 112–113, 164–166; 17m:263–264) were not changed, per assignment.
