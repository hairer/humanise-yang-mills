# Third review t5: chapters/09-renormalization.tex (9), 09-forest-average.tex (9f), 10-common-trajectory.tex (10)

Worktree /Users/mgubi/ym-terminology, manuscript/HumanizeYM_v3. Line numbers are those of the present files (the same as at HEAD). I read `git diff --word-diff 4f462ac5 HEAD` for all three files: about 185 changed lines in 9, 65 in 9f and 160 in 10, roughly 410 in all. I checked each one against the present text around it, and against chapters 4, 6, 7 and 8 and the dictionary where needed. I read the reports of the earlier rounds (ch09-review, ch09-apply, round2/ch09-10-review2, round2/harmonise, round3/ch06 and ch07-08-9s) and the leads only after forming my own reading. Nothing was staged, committed or reverted. All edits stay within their lines, and the line counts are unchanged.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 9:94 | ERROR | "The large-field indicators in their eligibility criteria can read outside $Y_i$." | "…in their additional conditions can read…" | The meaning is narrowed. The eligibility criteria are the whole event (ch04:eligibility): $\{\operatorname{Bad}_m\cap Y_i=I_i\}\cap\mathcal E_i^{\rm extra}$. "Additional condition" is the name of $\mathcal E^{\rm extra}$ alone (4:441–450). The large-field indicators sit mainly in the first factor. The same chapter says "eligibility conditions" at 9:902 and 9:918. | "…in their eligibility conditions can read outside $Y_i$." |
| 10:530–531 | ERROR | "the Gaussian coordinate is rescaled / by $\ell(t)$ while its fluctuation coefficient is divided by" | "the fluctuation field is rescaled / by $\ell(t)$ while its coefficient is divided by" | False. The fine read is $\mu+gz$, and the fluctuation field is $gz$ ("components $gz_i$ of the fluctuation field", 6:908). The rescaling keeps $gz$ fixed: $z$ is rescaled and $g$ is divided. Chapter 9 calls $z$ the "Gaussian coordinates" (9:59, 138–139). | 4f462ac5 wording restored: "the Gaussian coordinate is rescaled / by $\ell(t)$ while its fluctuation coefficient is divided by" |
| 10:123 | ERROR (minor) | "…a requested length for a stage plateau." | "…a prescribed length for a \emph{stage plateau}, a maximal interval of scales on which the stage is constant." | The meaning is sharpened. Under the definition now given, the plateau of stage $j$ is $[A_j,A_{j+1})$, whose length $b_{j+1}+2k_j+1$ exceeds $c_j$. $c_j$ is only a minimum ($k\ge c_j$, 10:186–188), but "prescribed length" reads as the exact length. The new definition of the plateau is correct and is kept. | "a requested length for a \emph{stage plateau}, …" (4f462ac5 word) |
| 9:748 | TERM | "There is a second, intrinsic way to identify the reset." | "…to identify the coupling constant renormalization $\Delta$." | One name is used for two objects 25 lines apart. 9:717–723 introduces the coupling constant renormalization as the operation $\beta=\beta'+\alpha+\Delta$ and says explicitly that "the increment of the inverse coupling is the coefficient $\alpha$ … plus the coefficient $\Delta$". 9:748 then gives the same name to $\Delta$ alone. What the passage identifies is $\Delta$ (the zero of $f(d)$). | "…to identify the coefficient $\Delta$." ($\Delta$ already stood on the HEAD line; the wording is that of 9:723.) |
| 10:422 | TERM (lead b) | "It is not the vacuum normalization." | unchanged; the preceding sentence was converted | Within chapter 10 the "vacuum normalization" is the additive normalization constant (10:265–266 "including the additive normalization constant. That constant is not asserted to converge"; 10:818–819 "additive vacuum normalizations"). The dictionary instead reads it as $Z^0$ (sense 2 of *vacuum*), on basis I. The sentence contrasts $q_m$ with that constant. Chapter 9 now names the pair (9:717) "the coupling constant renormalization and the vacuum energy renormalization". | "It is not the vacuum energy renormalization." |
| 10:422–423, 855 | MISMATCH | "The path coefficient $\alpha_{N,m}$ …"; "The limits of the common path corrections $\alpha_{N,i}$ cancel." | "The explicit coupling increment $\alpha_{N,m}$ …"; "…common explicit coupling increments $\alpha_{N,i}$…" | Chapter 9 calls the same coefficient "the determinant coefficient fixed by the matching" (9:410, 723, 738). The identity $\beta_m-\beta_{m+1}-\alpha_{N,m}=q_m$ is (ch09:reset). Round 2 listed this pair and did not fix it. | "The coefficient $\alpha_{N,m}$ fixed by the matching is the one already used…"; "The limits of the common coefficients $\alpha_{N,i}$ fixed by the matching cancel." |
| 10:775–776 | MISMATCH | "…preserves it by its convergent product expansion with a strict attachment / margin." | unchanged | This is the same margin $(2B+1)^4\gamma\le1/2$ of the exact regrouping (9:701–702). Chapter 9 now calls it "the strict margin in the site-norm bound" (9:794) and the norm "the site norm" (9:697). The dictionary files 10:775 under *attachment* sense 1 (merging insertions); that is wrong, because the sentence concerns the exact regrouping. | "…with a strict margin in the / site-norm bound." |
| 10:83 | MISMATCH | "Fix the stage column bound" | "Fix the stage coefficient-map bound" | The same $C_j$ is "the column bound" at 11E:19 ("$C_j$ the column bound") and "the already selected stage column bound" at 11:1200. The dictionary records *column* sense 1 as "not applied". In chapter 11 "coefficient map" names $M_G$ and $\mathsf Z$, and that $C_j$ bounds either one has basis I. So the new name both splits $C_j$ in two and makes a claim. | 4f462ac5 wording restored: "Fix the stage column bound" |
| 10:109 | MISMATCH | "fixed-stencil support and occupancy conditions" | "…the conditions on the number of insertions per coarse site" | Chapter 11 (11:345) says "number of insertion points per coarse site", in agreement with the definition at 11:260 ("insertion points project to a coarse site"). | "…the conditions on the number of insertion points per coarse site." |
| 10:166 | LEFTOVER / MISMATCH | "its per-site normalization cost" | unchanged | $q^{\rm site}_{m+1}$ is "the per-site normalization exponent of (ch11:replicated-bound)" (13sb:24–25; 12:247; 17m:439). The dictionary lists "per-site normalization cost" as no longer in the text, but it stands here. "cost" was replaced everywhere else in chapters 9–10. | "its per-site normalization exponent," |
| 9f:604 | LEFTOVER / MISMATCH | "property of the physical torus that $\Lambda_i$ does not share" | unchanged | Chapter 9 calls this torus, as opposed to the auxiliary tori, the "original torus" (9:325, 936; "original coarse period", 9:931). | "property of the original torus that…" |
| 9:81–82 | TERM (lead e) | "retain all sector / allocation indicators." | "retain all sector / allocation weights." | "Sector allocation weights" is used here only and defined nowhere. The object is the weights of 6:67–79 (the partition-of-unity products for $A_f$, $A_n$), the condition on $A_c$ and the probability weights of the auxiliary index. Chapter 6 calls each of these a "weight" and defines a sector by them (6:85). "Weights" rather than "indicators" (Appendix D) is correct, because the $\vartheta$ factors are smooth. | "retain all the / weights defining the sectors." |
| 9:432 | LANGUAGE | "…and the small logarithmic corrections." | "…and the small large-field corrections." | The phrase "small large-field" is hard to parse. | "…and the smallness of the large-field corrections." |
| 10:570 | LANGUAGE | "Small logarithmic factors require a different estimate." | "Small large-field correction terms in the exponent require…" | "Small large-field" is hard to parse, and "terms in the exponent" repeats the definition of a large-field correction (9:368). | "The large-field corrections, which are small, require a different estimate." |
| 9:6 | LANGUAGE | "express its exact output in the coordinates" | "express its exact output by the representation data" | "Express … by" is unidiomatic. | "express its exact output in terms of the representation data" |
| 9:893–894 | LANGUAGE (lead c; Appendix D B1) | "A connected prescribed set of $r$ large-field sites is bounded in number by a rooted spanning-walk count." | "A connected prescribed large-field set of $r$ sites is bounded in number…" | The sentence was damaged before the conversion: the number of such sets is bounded, not a set. The repair only reorders words and adds no content. | "The number of connected prescribed large-field sets of $r$ sites is bounded / by a rooted spanning-walk count." |
| 9:949–951 | — (lead c; Appendix D B2) | "Output inverse coupling-band membership additionally requires the numerical band margin in the choice of scales." | "That the output inverse coupling lies in its band additionally requires…" | The meaning is identical to 4f462ac5, so the conversion did not damage it. Whether the theorem should rather say that output membership is not asserted (Scott D:847), and what "numerical band margin" is, are questions about substance. | left for the author |
| 10:421–422 | — (lead b) | "$q_m$ is the residual scalar inverse coupling correction." | "$q_m$ is the coupling constant renormalization of the step." | $q_m=\beta_m-\beta_{m+1}-\alpha_{N,m}$ is $\Delta$ of (ch09:reset) exactly, by direct comparison (basis R, not I as the dictionary says). However, after my edit at 9:748, chapter 9 uses "coupling constant renormalization" for the whole operation with increment $\alpha+\Delta$, while chapter 10 uses it for $\Delta$ alone (10:421, 446, 651, 772, 816, 842, 902; also 13sb:26). This is the author's choice; see *For the author*. | left for the author |
| 9:77, 130 | TERM | "stationary residual" | "residual of the mean equation", "mean-equation residual" | "Mean equation" is defined nowhere in the book. Chapter 6 does not name the equation $\mathsf A m+f_Y=0$. The phrase is understandable and not false. | left for the author |
| 10:249 (also 10:393–395, 709, 757, 895, 905) | MISMATCH | "labels", "dictionaries" | "indices", "index sets" | Chapter 10 now says "indices" for the labels of terms. Chapter 9 keeps "labels" in the same statements (9:385, 771, 816 "retains the construction and all its labels", 9:939 "fixed labels"), and 9f defines "labels" (Assumption (a), 9f:229). Chapter 10 is consistent within itself, and the dictionary adopted "index" for 10:249. | left (listed) |

All other changed lines I found correct in meaning, word and grammar. Points checked in particular:
- The table at 9:124–133, whose heading "factor | integrated majorant" came from Appendix D.
- 9:140 ("resolvent identity for the determinant", Appendix D; it is the identity of 6:1285–1289).
- 9:17 (gloss on "actual").
- 9:57 ("non-tree bonds", as in 5:1161 and 6:442).
- 9:105 ("joint law").
- 9:108 ("part of the index triple belonging to $M$").
- 9:220 and 9:230–231 (Appendix D).
- 9:367–368 (definition of *large-field correction*).
- The Bałaban sentence at 9:723: it is consistent with the *Literature* line of *reset*, and the keys `Balaban1987RG` and `Balaban1988Expansions` exist.
- 9:912 ("free quadratic forms of two consecutive scales").
- 9:946–948.
- 9:970 and 10:35–36 (the bounds (ch07:classical-budget) and (ch07:inherited) are the two former "contractions", 7:1055 and 7:1084).
- 10:30 (*stage pairs*), 10:121 (*schedule*), 10:153 (*coarse endpoint*; $a_0=1$, so "unit scale" is right).
- 10:265 ("not merely of their representations").
- 10:313–316 (Appendix D) and 10:336 (7:938 name).
- 10:353–356 ("kernels", "direct coefficient", as in 5:749–751).
- 10:421 (*activity array* gloss) and 10:457 (*finite parameter evaluation* gloss).
- 10:616 ("connected covering number", 4:587).
- 10:727 (Appendix D).
- 10:921–923.

In 9f, every converted term agrees with chapters 4–9: localized term, representation data, base point, dependence set, Mayer expansion, normalization constant, values of the averaging operation, reflection map, terms of the path action, correction labels, exact regrouping. The mathematics of 9f is untouched.

## Corrections applied

- ERROR: 3 (9:94; 10:530–531; 10:123)
- TERM: 3 (9:748; 10:422; 9:81–82)
- MISMATCH: 5 (10:422–423 and 855, counted once; 10:775–776; 10:83; 10:109; 9f:604)
- LEFTOVER: 1 (10:166)
- LANGUAGE: 4 (9:6; 9:432; 10:570; 9:893)

That is 16 corrections on 20 lines: 9 has 7 lines, 9f has 1 and 10 has 12. All are word changes within lines. No formula, symbol or reference was added; $\Delta$ (9:748) and $\alpha_{N,m}$ (10:423, 855) already stood on those lines.

## Cross-chapter mismatches not fixed

- **Coupling constant renormalization.** In 9:717–723 it is the operation with increment $\alpha+\Delta$. In 10:421, 446, 651, 772, 816, 842, 902 and 13sb:26 it is $q_m=\Delta$ alone. The dictionary adopts both senses (entry *reset*).
- **Labels and indices.** 9:385, 771, 816, 939 and 9f (Assumption (a)) say "labels"; 10:249, 393–395, 709, 757, 895, 905 say "indices" or "index sets".
- **Large-field set allowed to be empty.** "Prescribed large-field set $I_M\subset X_M$, possibly empty" (9f:231) against 8:288 and 4:440, where the prescribed large-field set is nonempty. 9f's labels include small-field ones, so the term is extended there. Lead (d) is otherwise confirmed: chapters 9 and 10 use the name for $I_\eta$ (9:151, 643, 673, 893; 10:577, 654).
- **The function $f_i$.** "Regular functions $f_i$" (9f:300) against "local functions $f_i$" (9:398).
- **Coarse endpoint.** At 10:153 it is defined as the value $\bar\beta$; 1:465 uses it for the end of the trajectory, which "has a prescribed coupling".
- **"Far from the index triple"** (9:280) against "far from the large-field set" (chapter 6; 11:709). Both are correct in place.

## Leftover house words

Kept on purpose:
- **"stationary"** at 9:136 ("stationary mean"), 293 ("finite stationary region") and 305 ("stationary estimates"): these refer to 9s, which keeps the word.
- **"physical"** at 9:240, 257, 773 and 10:711, 725, 732, 880, 896–898: sense 4, basis I.
- **"scalar"** at 9:764 (numbers) and 10:443, 515, 645, 684, 826, 849, 868, 870: scalar senses 3–4 as recorded in the dictionary. 10:645 "scalar projection" is the projection defining $\Delta$; it is left for the author.
- **"reserve"** at 9:34 and 10:112, 426, 491, 529, 676, 760, 813: basis I.
- **"label(s)"**: event label (defined at 6:835), correction labels, the labels of 9f's Assumption, and fixed labels.
- **"weight(s)"**: ordinary uses, support weight, the probability weight, and 9:182 "original weights".
- **"unit"** at 9:465 (unit vector) and 9:687.
- **"level"**: only "level set" at 10:229.
- **"reset"**: only $C_{\rm reset}$ and labels.
- **"actual"**: only labels.
- **"marked"**: 9:263 "marking one changed factor", ordinary.
- **"ordinary"**: 9:314 (sense 2, basis I) and ordinary uses at 10:16, 536, 718.
- **"cost"** at 10:172 ("replication costs subpower"): an Appendix D damaged sentence, left for the author.
- **"stencil"** at 10:80, 103, 109: finite stencils of chapter 2, as the dictionary records.
- **"terminal"** at 10:432, 439, 447, 781, 861: left for the author (round 2).
- **"attachment reserves"** at 10:760: basis I.
- **None remain** of "tag", "block average", "predictor", "noise", "cutoff failure", "frame", "tree gauge", "block transformation", "unmarked", "heat", "mixed", "ground" or "kill".

Replaced: 10:166 ("cost") and 9f:604 ("physical").

## Leads

- **(a) 9f vocabulary.** Checked as above, and the mathematics is unchanged. One fix was made (9f:604). 9f:865 ("$a_dP_d$ together with its quadratic term", slightly circular) is left as round 2 left it.
- **(b) 10:421–422.** Verified. $q_m$ is exactly $\Delta$ of (ch09:reset). "Vacuum normalization" there means the additive normalization constant, not $Z^0$, so the dictionary's sense 2 is wrong for this line. I corrected it to "vacuum energy renormalization", the name chapter 9 gives that constant. The letter $q$ also names the per-site normalization exponent in chapters 11–13 and 17; that is a symbol clash present before the conversion, and I did not change it.
- **(c) 9:949–951.** The meaning is unchanged from 4f462ac5, so no conversion error; the substance is left for the author. **9:893–894**: repaired by word order only.
- **(d) "Prescribed large-field set".** Chapters 9 and 10 use it for $I_\eta$ or its unions, which is correct. The exception, a possibly empty set in 9f:231, is listed above.
- **(e) "Sector allocation weights".** Replaced by "the weights defining the sectors", in chapter 6's words. These are more than the partition of unity of 6:67 (they include the auxiliary-index weights and the $A_c$ condition), so "partition of unity" would be too narrow. **"Reassembly"** (9:57; also 9f:312, 930) is not the factorization identity of 8:279. It is the recombination of the local factors and normalization constants into the block integral for one forest (9f:927–930). It was kept, and the dictionary's *exact reassembly* entry is wrong to list 9:57.
- **9:913 "transport"** (leads, part 6). At 9:913 the phrase is "exact transport identities" of chapter 5, which is not a transfer through the steps. Left unchanged.
- **10:654 "large-field factor"** (appendix agent). Here it is the factor $k_i$ retained once per component in the exact regrouping (the old "compulsory large-field factor"). It is correct in place; other chapters were not compared.
- **9:147** (Appendix D, damaged). Not touched, as instructed.

## Assessment of earlier corrections

- **Harmonisation, 10:760.** The change ("the margins in the support exponent and the attachment reserves") is correct. But harmonisation did not carry 9:794's "margin in the site-norm bound" over to 10:775; this is now done.
- **Second review and harmonisation, 10:83 "spatial exponents" and 9:94.** Neither caught the narrowing at 9:94 ("additional conditions"), which goes back to the first conversion. Round 2 explicitly accepted it under "additional conditions / eligibility conditions … consistent".
- **10:530–531.** All earlier rounds passed the "fluctuation field" error.
- Round 2's other corrections (9:283–284 restored, 9f:274–275, 347–348, 633, 964–965) are correct.

## For the author

1. **Coupling constant renormalization**: is it the operation with increment $\alpha+\Delta$ (9:717–723) or the correction $\Delta=q_m$ (10:421 ff., 13sb:26)? One way to settle it is to call $\Delta$ and $q_m$ "the remainder" or "the projected part" of the coupling constant renormalization.
2. **9:949–951**: whether the output band membership is asserted, and what the "numerical band margin" is (Scott D:847).
3. **Labels and indices** in chapters 9, 9f and 10.
4. **"Mean equation"** (9:77, 130) is undefined; one could name $\mathsf A m+f_Y=0$ in chapter 6.
5. **"Scalar"** at 10:645, 684, 826, 849, 868, 870 (scalar projection, cumulative scalar bound, scalar recursion and so on).
6. **Undefined "prescribed" words**: "prescribed interval" (10:189) and "requested length" (10:123) both refer to requirements from later comparison estimates. Saying "minimum length" would be more precise, but it adds a qualifier.
7. **Representative of the linearization** at 10:921 (round 2) and **"terminal arrays"** at 10:432, 439, 447, 781, 861 (round 2).
8. **Dictionary corrections**:
   - *vacuum*, sense 2: 10:422 is not $Z^0$.
   - *exact reassembly*: drop 9:57.
   - *attachment*: 10:775 belongs to sense 2.
   - *coupling constant renormalization*: the identification with $\Delta$ is R, not I.
   - *column*: it was applied at 10:83 and is now restored.
   - *per-site normalization cost*: it remained at 10:166 and is now replaced.

## Checks

- **Line counts**: 09-renormalization.tex 979 = HEAD 979; 09-forest-average.tex 973 = 973; 10-common-trajectory.tex 935 = 935. `git diff --stat` against HEAD shows 9 with 7 lines, 9f with 1 and 10 with 12, all replaced in place.
- **`python3 tools/check_draft.py`**: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- **Build**: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-t5 monograph.tex` exited 0. In monograph.log, "undefined" 0, "Citation" 0, "Overfull" 0. The build included other reviewers' concurrent edits.
- **Rendered text** (pypdf): every corrected phrase was found in the PDF, on pages 121–160 (for example "weights defining the sectors" p. 122, "identify the coefficient" p. 145, "vacuum energy renormalization. The" p. 153, "Gaussian coordinate is rescaled" p. 155, "site-norm bound. The finite" p. 159).

## Not checked

- Pages were not inspected as images.
- Bałaban's papers were not reread; the check of 9:723 rests on the dictionary's *Literature* line.
- The Scott and Martin sources behind the Appendix D repairs at 9:124, 140, 220 and 10:98 were not reopened. I accepted them as recorded.
- I only grepped other chapters for consistency and edited none of them.
