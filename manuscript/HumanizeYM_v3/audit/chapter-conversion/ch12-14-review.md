# Review of the vocabulary conversion of chapters 12–14 (c5: 12, 13, 13sb, 13ba; c6: 14, 14lc)

Worktree `/Users/mgubi/ym-terminology`, uncommitted. I read the word diffs of all six files first, then the editors' reports `c5-apply.md`, `c6-apply.md`, the dictionary entries concerned, and the converted text of chapters 4–11 where the same objects occur. My corrections are within lines only; every file keeps its line count.

## Review findings

| file:line | class | committed text | edited text | what was wrong | corrected text |
|---|---|---|---|---|---|
| 12:131 | ERROR | `[Forgetting the terminal graph]` | `[Independence of the graph at the cutoff]` (App. D repair) | The proposition (12:133–136) says that the selected graphs and coefficients at a fixed scale are **Cauchy** in the cutoff. The proof (12:139–145) replaces the graph at scale `m+h` by one fixed admissible graph that does not depend on the cutoff, and shows that the scale-`m` graph moves by at most `2^{1−h}`. Nothing is independent of the cutoff, and the graph that is replaced lies at `m+h`, not "at the cutoff". The new title states a stronger claim than the one proved, so it is restored. | `[Forgetting the terminal graph]` (committed; for the author) |
| 12:48, 62, 126 | MISMATCH | `at width`; `smaller width $v$. A strict width reserve`; `at a strict width reserve` | `at decay rate`; `smaller decay rate $v$. A strict margin in the decay rate`; `at a strict margin in the decay rate` | Chapter 7 defines *width* as the exponential decay rate of the path coefficients (7:360), and chapter 10 writes "strict width margin" (10:375, 442, 703). Lesson 11(c) says to use that word. "Decay rate" also gave chapter 12 a second name for the same object. | `at width`; `smaller width $v$. A strict width margin makes`; `at a strict width margin and` |
| 12:219 | MINOR | `grouped profiles` | `grouped total large-field activities` | "Grouped" repeats what "total" already says. | `total large-field activities` |
| 13:120 | DICTIONARY | `define the one-slot response` | unchanged | *response* 8 / *one-slot response* (basis D, 13:119–122) proposes *correlation functional* for `L_{v,f}`, with "response" for its value. The job note `"one-slot response" (correlation functional)` gave the new word, but the editor kept the old one. | `define the correlation functional`; "response(s)" stays for the values (13:9–10, 151–152, 161, 177, 183, 210–211, 265), as the entry says |
| 13:138 | LANGUAGE | `after a coefficient refinement` | `after a further subsequence for the coefficients` | "After a subsequence" is elliptical. | `after passing to a further subsequence for the coefficients` |
| 13:236–237 | LANGUAGE | `translated-stencil cost is bounded by the coupling-threshold requirements` | `the factor contributed by the fixed translated stencil is bounded by the lower bounds on the reference coupling` | As edited, a factor is "bounded by lower bounds on a coupling", which does not parse as mathematics. The requirements control the factor; they are not its bound. | `… is controlled by the lower bounds on the reference coupling` |
| 13ba:124 | TERM | `its complete push to $h$` | `its full image under the block maps down to $h$` | This is a seven-word description where the table word *transfer* exists. The same file uses it at 158, 170 and 185 ("transferred"). It breaks rule 7. | `its full transfer to $h$` |
| 14:308 | TERM | `This fixes an orientation of the physical line.` | `This fixes the sign of the generator of the line.` | "Generator" now also names the local charges `p_b`, `Y_d(K)` ("the local generators", title 14:312; "both generators", 14:408) and the plane generators (14:946). The App. D repair "the sign of `J`" cannot be applied as written, because `J` is not on the line (lesson 11a). | `This fixes the sign of the chosen tensor on the line.` (the `J` chosen at 14:296; words only) |
| 14:406, 991–992 | MISMATCH, LANGUAGE | `these response identities`; `have zero responses against every spectator` | `these identities between values of the correlation functionals`; `have zero values of the correlation functionals against every spectator` | Chapter 13 keeps "response" for the value of `L_{v,f}` (13:211 "all response identities"), so chapter 14 should say the same. Line 992 had also become a noun pile. | committed wording restored at both lines: "these response identities", "have zero responses against every spectator" |
| 14:946 | ERROR | `their transported mixed matrices as $B_{k,i}$` | `their conjugates by the comparison maps as $B_{k,i}$` | "Their" refers to the free matrices `C_i`, so the edit says that `B_{k,i}` is a conjugate of `C_i`. In fact `B_{k,i}` is the matrix of the generator on the undecomposed spaces, pulled back by `U_{k,d}` (it converges to `C_i` by (ch14:charge-limits)). | `the conjugates of their undecomposed matrices by the comparison maps as $B_{k,i}$` |

**Points of the assignment, checked and found correct (no change):**

- **mixed / physical across chapters 12–14.**
  - The chapter 12–13 files contain no occurrence of *mixed* in sense 1 (undecomposed mixture) and none of *physical* in sense 3 (interacting, against free). The chapter 12–13 editor therefore made no choice for either.
  - Chapter 14 uses one word for each contrast, the dictionary's: *undecomposed* for *mixed* 1 (14:12, 165, 263, 349, 820, 946) and *interacting* for *physical* 3 (14:212, 291; at 308 the word was dropped).
  - The two contrasts are kept apart, so chapters 12–14 now agree. Chosen: **undecomposed** (mixed 1), **interacting** (physical 3). In chapters 12–13, *physical* 1 → *in continuum units* and *physical* 2 → *dimensionful*, the same as chapter 11.
- **12:178.** "Summing the norms of \eqref{ch04:weighted-sums} over the finitely many sites" is the App. D repair. It names exactly the norms of chapter 4: `𝓔_m` (each regular activity counted at its anchor) and `𝓚_m` (each large-field activity counted at every site of its support). This is reading (a) of *rooted* 1, not the incidence norm of reading (c). The edit is correct.
- **12:236–237.** "Incidence bounds … at support exponent `σ_m`" is the object of *rooted* 1(c), basis S: the sums pinned at an insertion, i.e. the incidence bound with source weight and support exponent. Chapter 11 (converted in the worktree) uses the same words at 11:1437–1440. The edit is correct.
- **total large-field activity.**
  - Defined at 12:26–27 with the dictionary's meaning (the sum of the activities with one support and one prescribed large-field set).
  - Used consistently at 12:78, 161, 180–181, 219, 223, 248, 288. 13ba:165 has "no large-field part" (App. D).
  - Chapter 14's *profile* (frequency profile, residual profile, 14:448, 464 …) was not touched in the wrong sense.
- **stopping.** The edit keeps the word in both senses, exactly where it stood. Nothing new is merged.
  - Chapter 12 (sense 1, terms deleted): 12:10, 225, 302. The lemma title "Removal of terms of source degree at least two" says what is deleted.
  - Chapter 13 (sense 2, nothing deleted): 13sb:85, 102, 137; 13ba:8, 193.
- **ordered tail.** Kept. The definition is at 13:213–214; 13:143 now reads "the ordered tails of these subsequences".
- **buffer.** Kept at 13:335. 14:99 "with buffer `r`" is the entry's own proposal and is correct: the buffer covers both the pairwise separation and the slab margins.
- **selected.**
  - "Fixed by the construction" → "the construction of Chapter 10" at 12:13, 133, 298 and 13ba:17.
  - Ordinary "chosen" at 13sb:136.
  - Subsequence senses kept (13:172 and others).
- **label.** Each chapter 14 occurrence was checked against the entry *label*.
  - Sense 2 (element of `F_d`) → *field* at 14:26, 98, 101, 147, 658, 842, 864, 879, 980, 991, 1025.
  - Sense 3 → *free fields* at 14:238, 250.
  - 14lc:7 is left; the entry calls that line undecided.
  - Chapters 12–13 keep *label* = polynomial label (sense 1): 12:22, 147 and chapter 13.
  - For 14:26, 98, 101 the entry notes that the formal objects are polynomial labels, but either reading leaves the statements unchanged.
- **heat → translation semigroup** (14:80, 435, 855, 858; 414 deleted). `E_μ(t)` is built from the translations `T_t` by `te_μ` (14:39–56), so the name is accurate. It is not defined by name.
- **window → compact set (of separated configurations).** Applied at 14:173, 197, 226, 237 and 14lc:6, 97.
- **14:776–777, 796.** The left side of (ch14:line-ward) is `Σ_i {S(…,Y(K)A_i,…) + (Kx_i)_b S(…,p_bA_i,…)}`. By Proposition ch14:charges this is the sum, over the insertions, of the local linear and constant fluxes of the field `V = Ky`. Conservation turns that sum into `−∫∂_μV_c S(J_{μc},A)`. So that left side is exactly the quantity meant, the total angular flux.
  - The equation is displayed after these lines (a forward reference). The argument is not circular: it shows that the left side is independent of `λ` and tends to zero, hence vanishes.
- **14:186, 903.** These are word-only repairs and correct. 14:186 still relies on the unstated `M_k = H_k`, as before.
- **"corrected coefficients"** is kept (14lc:45).
- **12:247.** `q` in (ch11:replicated-bound) (11:810–812) is the per-site normalization exponent. The symbol `r` was already on the line.

## Corrections applied

1. 12:48, 62, 126: *width* and *strict width margin* (chapters 7 and 10).
2. 12:131: committed title restored.
3. 12:219: "grouped" removed.
4. 13:120: "correlation functional".
5. 13:138: "after passing to a further subsequence for the coefficients".
6. 13:237: "is controlled by".
7. 13ba:124: "its full transfer to $h$".
8. 14:308: "the sign of the chosen tensor on the line".
9. 14:406, 992: committed "response" wording restored.
10. 14:946: "the conjugates of their undecomposed matrices by the comparison maps".

## Left for the author

- **12:131.** The title "Forgetting the terminal graph" is restored. "Terminal graph" names no object; the graph forgotten is the one at `m+h`. Words-only titles that do not overclaim, for the author's choice:
  - "Loss of memory of the graph at finer scales";
  - "Convergence of the graphs at a fixed scale".
  The App. D entry (no. 4, group 3) should be corrected: its repair asserts independence.
- **13ba:258, 261.** Confirmed: the condition `b_q log3 ≥ 2 log(ȷ_q+7)` is on `b_q`, the *minimum starting scale* of the stage (10:122–126). It is not a lower bound on `β̂`.
  - The dictionary needs this correction: remove 13ba:258, 261 from the *Where* of *coupling threshold*, and record them as a lower bound on the starting scale (as at 10:171 and 12:123).
  - Suggested wording, not applied: "This is a permitted finite lower bound on the starting scale:" and "among the conditions on the minimum starting scales of Section~\ref{ch10:schedule}".
- **14lc:23.** "a comparison depth `k` whose comparison window lies in a single stage" follows App. D (suggestion no. 9).
  - It uses "window" outside the book-wide sense `Ω_i`, as chapter 11 does (11:1675, 11R:215).
  - The condition itself is still not stated anywhere in the book.
- **14:12 and later.** "Undecomposed" is not glossed in chapter 14. Its first use in the book is 18lp:8, in chapter 13, which belongs to another agent. A one-line gloss belongs there, not here.
- **13sb:9.** "Gaussian comparison used for the separating families", for "rank detection" (*detection* has basis I). It is acceptable, but it rests on the table row and not on a D/R entry.
- **Chapter 12, two phrasings for one object.** 12:13, 133, 298 say "the construction of Chapter 10"; 12:40, 370 say "the cutoff-independent construction". Both are dictionary proposals (*trajectory* 2, *common* 3).
- **Other remaining points:**
  - 14:1016: "the values of the correlation functionals on all positional derivatives" was left; it is correct.
  - 14:757: "adds to the exponent" has the same sign ambiguity as the committed "costs exponent".
  - 13:231: "physical lattice difference" (*physical* 2) was left by the editor.
- **Other points left by the editors** (listed in their reports): "excess", "stencil", "cone", "terminal", "fixed-input continuity", "request", "comparison depth", and the basis-I words. I agree with leaving them.

## Words this file introduces that other chapters may also define

- *total large-field activity* (defined 12:26).
- *action data* (12:31, by enumeration).
- *correlation functional* (13:120). Chapter 3 already has "vector / internal-defect correlation functionals"; 18gq:111, 113, 130 and RG:18 still say "response" in the functional sense.
- *undecomposed* (14; also needed in 18lp, 15, 15sp, 16, 17, 18, 19).
- *interacting* (14; 18gq, 18).
- *translation semigroup* (14:80).
- *frequency profile*, *residual profile* (14:448, 464).
- *coincident-coordinate strips* (14:179).
- *compact set of separated configurations* (14:173; chapter 11 and 17:140 have "window" in this sense).
- *local generators* / *generators* for `p_b`, `Y_d(K)` (14:312, 408; chapter 16 uses "charge" for a different object).
- *incidence bound* (chapter 11).
- *with buffer `r`* (13:335; 14:99).

## Checks

- Line counts equal HEAD: 12-ultraviolet-limit.tex 405/405; 13-continuum-fields.tex 403/403; 13-sharp-bounds.tex 177/177; 13-bounded-approximations.tex 337/337; 14-reflection-ward.tex 1028/1028; 14-lattice-comparison.tex 110/110.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1236 references. All explicit cross-references resolve; no duplicate labels." Exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-c56 monograph.tex`: exit 0. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0.
- Rendered text (`mutool draw -F txt` of the PDF):
  - Each corrected phrase appears and reads correctly ("define the correlation functional L_{v,f}(c) = …", "after passing to a further subsequence for the coefficients", "Forgetting the terminal graph", "strict width margin", "chosen tensor on the line", "undecomposed matrices", "zero responses against").
  - No "??" anywhere.
- No other file was edited. Nothing was staged or committed.

## Not checked

- Page images were not viewed; only text was extracted.
- The original sources and the Lean code were not opened. Literature claims rest on the dictionary's *Source* and *Literature* lines.
- 18-graded-quotient.tex and 18-lattice-products.tex are input in chapter 13 but belong to another agent; I did not review them.
- Chapter 11 (under review by another agent) was read only for the words it uses.
