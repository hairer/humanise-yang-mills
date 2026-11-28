# Review of the vocabulary conversion: chapter 11, lines 1181–2355, and the fragments 11R and 11E (reviewer c3b-review)

Worktree `/Users/mgubi/ym-terminology`, files in `manuscript/HumanizeYM_v3/chapters/`:
- `11-marked-insertions.tex`, lines 1181–2355 only (abbreviated "11").
- `11-restarted-history.tex` (abbreviated "11R").
- `11-equation-calibration.tex` (abbreviated "11E").

Method:
- I read the word diffs against `HEAD` first: 148 lines in 11 (1181–2355), 121 lines in 11R and 31 lines in 11E.
- Only after that did I read the editors' reports, `c3b-apply.md` and `c4-apply.md`.
- I checked each change against:
  - its dictionary entry and the dictionary's Appendix D;
  - the committed chapters 1–10;
  - the reviewed first half of chapter 11 (lines 1–1180), which I did not change.

## Review findings

| file:line | class | old (committed) | edited | what was wrong | corrected |
|---|---|---|---|---|---|
| 11:1613 | ERROR | "the actual cutoff-failure probability absorbs the complementary / principal cutoff" | "the actual probability of a large fluctuation-field event absorbs the large-field part of the / principal cutoff" | The first replacement is right: *cutoff failure* sense 1 (failure of a smooth cutoff), with 11:1613 in that sense's line list. The second is wrong. The entry *complementary* puts 11:1613 under sense 2, "the factor `(1−γ)W` left by a smooth local cutoff `γ`", not under sense 1 (large-field part). The edit named the other kind of failure (a large-field indicator). The proposal for sense 2 inserts a formula, so the committed word must stay. | "…absorbs the complementary / principal cutoff." |
| 11:1410, 1540 | TERM | 1410 "At an earlier leading step"; 1540 "For the same leading expansion let" | 1410 "At an earlier step of the upper interval"; 1540 "For the same expansion on the \emph{upper interval}, from the comparison scale to the middle scale, let" | There are two problems. (1) The term is used at 1410, 130 lines before it is defined. (2) The definition is wrong: in this chapter the "comparison scale" is `H` (1668–1669: "`H` measures the slowly growing comparison scale"). The upper interval runs from the top scale `k` to the middle scale `ℓ` (*leading* 2; `m=k−ℓ`, 1754). "Top scale" is the word used at 11R:218 (which comes earlier in the book: 11R is input at 11:765) and at 11:1930 and 2085. | 1410: "At an earlier step of the \emph{upper interval}, from the top scale to the middle scale, a nonzero connected principal component"; 1540: "For the same expansion on the upper interval let its regular remainder satisfy" |
| 11:1288 | LANGUAGE | "The low-weight coefficient extraction of $\mathscr Pu$" | "The extraction of the coefficients of low scaling dimension of $\mathscr Pu$" | Stacked "of … of": it can be read as "low scaling dimension of `𝒫u`". | "The extraction from $\mathscr Pu$ of the coefficients of low scaling dimension belongs to this basis:" |
| 11:1384 | LANGUAGE | "For a marked activity with support $X$" | "For an activity with insertions with support $X$" | "with insertions with support" | "For an activity with insertions, with support $X$ and source variable set $I$, its" |
| 11:1812 | LANGUAGE | "the transported mean contributes" | "the image of the mean contributes" | The mean `μ=𝓛u` (1788) is itself the image under `𝓛`. "Image of the mean" names `𝓛μ`, which is a different quantity. | "the mean contributes" |
| 11:1965 | MISMATCH | "The selected plateau must include" | "The selected interval of scales on which the stage is constant must include" | Chapter 10 (committed) defines the short term at 10:123: "a \emph{stage plateau}, a maximal interval of scales on which the stage is constant". It uses "plateau" again at 10:139 and 189. The long description violates the length rule. | "The selected stage plateau must include" |
| 11:2118 | MISMATCH (from c3a-review) | "The coefficient tails and physical covariance errors are" | unchanged | In the first half, "physical" means *in continuum units* or *dimensionful*, so this use misreads. The sense here is *physical* 9(b), the block on the retained jet coordinates. Evidence: 2116–2120 repeat, for `n` insertions, the pair argument of 1862–1865 ("the common coordinate estimate and the coefficient tail … `CH^{-2}`"). That common coordinate estimate is 1831–1833 ("their [physical →] retained jet block differs from the free one by at most `H^{-2}`"). The editor already converted 1832 to "retained jet block". | "The coefficient tails and the covariance errors on the retained jet block are" |
| 11:2276 | LANGUAGE | "For the tested correlation assertions," | "For the assertions on these values," | "These values" has no antecedent in this paragraph: the preceding paragraph ends with `Z`. | "For the assertions on the values of the averaged functionals," (the wording of 2255; 2288 "the bound on these values" now refers back to it) |
| 11:2092 | MINOR | "with unchanged top map and endpoint." | "with unchanged top map and top scale." | *Endpoint* 3 here is the re-expressed density at the top scale. An unchanged top *scale* says nothing. 11R:384 and 387 render the same word as "density at the top scale". | "with unchanged top map and density at the top scale." |
| 11R:184 | LANGUAGE | "Absolute convergence justifies countable labels and coalescing." | "…justifies countably many terms and collecting them by support." | "justifies countably many terms" does not parse as intended. "By support" also disagrees with 11R:147, which now says "by dependence set" for the same collection. | "Absolute convergence justifies the sums over countably many terms and collecting them by dependence set." |
| 11R:239 | MINOR | "all deletion-of-support identities supply" | "all identities \eqref{ch08:deletion-identity} give" | The reference is right: (8.11) deletes the labels whose supports meet `Y` (8:206–216), which is the source's "hole-deletion identity". But "all identities (8.11)" reads oddly. | "all deletion identities \eqref{ch08:deletion-identity} give" (as at 9:152 and 9:354) |
| 11R:247 | MISMATCH | "forest charts" | "charts of the block axial gauge" | Chapter 5 defines the short term "block axial chart" (5:930, "the chart of the block axial gauge"). | "block axial charts" |
| 11E:171 | DICTIONARY | "free nondegeneracy and detection estimates" | "…and separation estimates" | The entry *detection* has basis I. It also says that "separation" cannot be reserved for this property. c3a-review restored "detection" in the title at 11:960 for the same reason. | committed "detection" restored |
| 11E:104 | MISMATCH | "bounds this / normalized mass." | "bounds this / normalized weighted norm." | The reviewed first half keeps "normalized mass" for the same object (11:424, "the incoming normalized mass is $m/\kappa_f$"; the entry *normalized mass* groups the two lines). In the very next sentence 11E:104–105 also keeps "reserved mass". | committed "normalized mass" restored; listed for the author |

### Points named in the assignment

- **11:1238.** Unchanged against `HEAD`: `$\|Au\|\le H^{bd+c_d}$, choose $D>bd+c_d+v$ before the stage`.
- **"Larger source weight" for "restored weight" and "weight restoration" (1436, 1471, 1552, 1554, 1569, 2130, 2131, 2200).** Same lemma and same meaning. The entry *weight restoration* defines the passage from `(ω_−, e+2)` to the larger weight `ω` at exponent `e`, which is exactly what each lemma states. The phrase reuses the committed subsection title "Absorbing the larger source weight" (1374). `\ref{ch11:restore-regular}` at 2131 points to the lemma at 1436, which is the old "Regular weight restoration". At 1554, "the two preceding lemmas" are 1436 and 1471.
- **Rooted activity norm replaced by incidence bound (1437, 1440, 1552).** This follows *rooted* 1(c) (S) and *incidence*: the supremum over insertions of the weighted sum over the terms containing that insertion, at source weight `ω` and support exponent `e`. The lemma still states the same thing: the hypothesis is at `(ω_−, e+2)` and the conclusion at `(ω, e)`.
- **Failed-cutoff replaced by large-field (1476, 1487, 1500, 1523, 1562, 1932).** All of these are *cutoff failure* sense 2: the factors `1−(1−χ)Rz_I`, whose support contains a large-field indicator (1487–1497). The replacement names the right kind. 1613 is sense 1 and correctly became "large fluctuation-field event"; only its second phrase was wrong (see above). 11R:283, 308 and 311 (sense 1, "large fluctuation-field events") and 11R:378 (sense 2, "regularity condition fails") are also right.
- **Frame replaced by basis (1286, 1288, 1293).** Sense 2, correct.
- **Weight replaced by scaling dimension (1288, 1335, 1848).** Correct. "Source weight" (1370–1371) is a different sense and was rightly kept.
- **Level replaced by scale (1405, 1551, 1646, 1886, 1889, 2085, 2088).** Correct. "Comparison level" was kept, as in the first half.
- **Stage delay replaced by lower bound on, or increase of, the starting scale (12 places).** Correct, and the same words as 10:63, 107, 158.
- **Reserve replaced by margin or "kept aside".** Right in each place: "kept aside" for a factor that is set aside (1596, 1658, 1662, 1935; 11R:170, 180), "margin" for slack (1601, 1748, 2089; 11R:9, 274, 371).
- **Cost replaced by factor or bound.** Right in each place: 1514, 1830, 1918, 2163 are sense 1 (a factor); 2309 is sense 3 (a bound).
- **"Upper interval".** Now defined at its first use (1410), with the correct ends.
- **Stencil (settled).** The meaning depends on the place:
  - At 2308, "its stencil" is the set of links of the difference trial, made of `2^{|l|}` translates. That is the *stencil* entry's sense, which the first half calls "link support" (919, 938, 957). "Link support" is right there.
  - At 1783 and 1824–1829 ("interior stencil", "stencil point", "stencil value", "stencil radius"), "stencil" is the finite point set on which the residual coordinates and finite differences are evaluated. That is the ordinary finite-difference stencil, as in "finite stencil" at 1:138 and 2:188. It is correctly kept.
  - 11E:15, 80–81 and 95 ("union of the link supports") follow the first half (11:922). Committed 10:80 still says "union stencil" for the same `q_d` (listed below).
- **11:2305 ("exact physical difference identity").** Not settled: left. It is either *physical* 1 (a difference quotient with step in continuum units; compare 2282 and the factor `a_N^{|l|}` at 2307) or *physical* 2 (carrying the power of `a_N`). The line is not in the entry's lists.
- **11:1324 ("every higher source variable coefficient").** Left. The text does not decide whether "higher" means source degree at least two or nonconstant. "Higher coefficients" at 1672 and 1950 has the same doubt, and the dictionary has no entry. Writing "source degree at least two" could weaken the claim.
- **Fragments.**
  - 11R:197: "reduced density" is defined once at its first use. It occurs nowhere else in the book, so there is no collision.
  - 11R:25: "auxiliary reference parameter" is the dictionary's word (D). It agrees with "changing the reference parameter" (11R:49, 275).
  - "Small-field" for "ordinary" (11E:83, 93, 111, 118) is sense 1, correct.
  - "Top scale" (11R:68, 89, 218, 384, 387) is correct.
  - Appendix D repairs, checked:
    - 11R:238–239: right identity; "deletion" restored.
    - 11R:266: as given.
    - 11R:300–302 (B5): without the parenthesis. This agrees with the committed singular "to a selected component".
    - 11R:304: as given.
  - 11E:25–30: the calibration floor is still a lower bound on the block ratio `L`, with the formula untouched.
- **Appendix D repairs in the second half.** All are words only, or words plus a reference to an existing label: 1343, 1405 (without `$\ell$`), 1551, 1632, 1662–1663 (`\eqref{ch11:integrated-component}` exists, 291), 1666 (`\ref{ch11:restart-construction}` exists), 1673 ("of the initial remainder bound" in place of "$H^{-q}$"; correct, since `z_0≤H^{-q}`, 1542, 1929), 1886, 1911, 2037, 2207 and 2306 (`\eqref{ch11:trial-error}` exists, 951). No formula, symbol, radius or constant was inserted.

Everything else in the three diffs I checked and accepted. That covers the remaining *actual* deletions and replacements, *mark*/*unmarked*, source degree, prescribed large-field set, transfer, conjugation, majorant, growth factor, cell sides, placing, the values of the correlation functionals, cutoff-dependent, backward comparison, lower bound on `N`, under the joint law, clipping and the piecewise quadratic–linear function, sup-norm bound per site, dependence set, decay exponent and change of cover radius. No first-use sentence about Bałaban or Dimock was added in these files.

## Corrections applied

These are in-line replacements only. Line counts are unchanged, and lines 1–1180 of 11 are byte-identical to their state before my edits.

1. 11:1288: "The extraction from $\mathscr Pu$ of the coefficients of low scaling dimension belongs to this basis:"
2. 11:1384: comma after "insertions".
3. 11:1410: `\emph{upper interval}` is defined here, "from the top scale to the middle scale".
4. 11:1540: definition removed, "for the same expansion on the upper interval".
5. 11:1613: committed "complementary principal cutoff" restored.
6. 11:1812: "the mean contributes".
7. 11:1965: "The selected stage plateau must include".
8. 11:2092: "unchanged top map and density at the top scale".
9. 11:2118: "the covariance errors on the retained jet block".
10. 11:2276: "For the assertions on the values of the averaged functionals,".
11. 11R:184: "justifies the sums over countably many terms and collecting them by dependence set."
12. 11R:239: "all deletion identities \eqref{ch08:deletion-identity} give".
13. 11R:247: "block axial charts".
14. 11E:104: committed "normalized mass" restored.
15. 11E:171: committed "detection" restored.

## Left for the author

- **11:2305**, "physical difference identity": sense 1 or sense 2 (see above).
- **11:1324**, "higher source variable coefficient", together with 1672 and 1950 ("higher coefficients"): it is not decided whether this means source degree at least two.
- **11:2118**: corrected by inference from 1831–1833 and 1862–1865. The line is not in the entry's lists; please confirm.
- **11E:104**: "normalized mass" restored for agreement with 11:424. The dictionary (R) proposes "weighted norm (divided by `κ_f`)". If the author wants it, it should be applied at 11:424, 11E:104 and 18lp:116 together, with "reserved mass" (11E:104–105, 117) decided at the same time.
- **"Large-field factor"** (1476–1523, 1932) for the failed-cutoff factors `1−(1−χ)Rz_I`. The same words also name the incoming large-field factors (old large-field activities) at 11:245, 250 and 332. Inside the lemma at 1471 the qualifiers "new"/"additional" and "old" keep them apart. A distinct name, for example "new large-field factor", is a choice for the author.
- **11:1199**, "the first is a lower bound on the starting scale for the already selected stage column bound". This is grammatical but loose: the inequality is *imposed by* such a bound. It was left, because the committed "is a delay for" was equally loose.
- **10:80** (committed) still says "union stencil" for the `q_d` that 11E:15 now calls "the fixed union of the link supports". Chapter 10 is outside my files.
- **11R:89** now cites `Chapter~\ref{ch10:trajectory}` for "the selected trajectory", and 11:1666 cites `Section~\ref{ch11:restart-construction}`. These are new references, not formulas. I kept them.
- **The editors' "Not changed" lists** in `c3b-apply.md` and `c4-apply.md` still stand. They cover "actual" at 1613; *selected* 2; "inflation"; "installed"; "metric floors"; "reserved mass"; "physical covariance factors" (11R:60, sense 6); "its physical convention" (11E:185); and the half-square.

## Words this file introduces that other chapters may also define

- *upper interval* (11:1410). Chapter 11 also uses "lower interval" (1564, 1960), undefined as in the committed text.
- *larger source weight* (from the title at 1374). 17w:89 and 93 cite the lemmas formerly titled "weight restoration".
- *incidence bound* at `(ω, e)` for the rooted activity norm. 12:236 has the same reading (*rooted* 1(c)).
- *large-field factor* (sense 2 of *cutoff failure*). Chapter 12 (12:203) and 17m:300 use "large-field factors" for incoming factors.
- *reduced density* and *full density* (11R:195–197).
- *auxiliary reference parameter* (11R:25).
- *top scale*, *density at the top scale*, *change of representation at the top scale* (11R:68; 11:1930).
- *sup-norm bound per site* (11R:225). The same `q_n` is the vacuum normalization bound in chapters 12, 13sb and 18lp.
- *piecewise quadratic–linear function* (11R), *clipping coefficients*.
- *growth factor*, *majorant* (for envelope), *cell sides*, *placing in distinct cells*, *backward comparison*, *cutoff-dependent*, *under the joint law*, *strict margin in the decay width*.
- *link support* versus *stencil*: chapters 12 and 13 use both (13:138 "fixed link support"; the entry notes a finite-difference stencil in chapter 12).

## Checks

- Line counts:
  - 11-marked-insertions.tex: 2355, same as `HEAD`.
  - 11-restarted-history.tex: 393, same as `HEAD`.
  - 11-equation-calibration.tex: 185, same as `HEAD`.
- Lines 1–1180 of 11 were compared with `cmp` against the copy taken before my edits: identical. 10 lines of 11 changed relative to the editor's version.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1234 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-c3b monograph.tex`: exit 0.
- `monograph.log`: 0 lines matching "undefined" (case-insensitive), 0 matching "Citation", 0 matching "Overfull".
- I extracted the rendered text with `mutool draw -F txt` and found each corrected passage in it ("upper interval, from the top scale to the middle scale", "stage plateau", "deletion identities (8.11)", "detection estimates", "complementary principal cutoff", "values of the averaged functionals").

## Not checked

- I did not look at the rendered pages visually, beyond the text extraction above.
- I did not consult the Bałaban, Dimock, Scott or Martin sources. I relied on the dictionary's *Literature* and *Source* lines.
- I did not recheck the editors' "Not changed" occurrences, except those named above.
- Chapters 12–14 are being edited by others in this worktree. I did not touch or review them, and they did not break the build.
