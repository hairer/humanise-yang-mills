# Second review r7: chapter 11, lines 1181–2355; 11-restarted-history.tex; 11-equation-calibration.tex

Worktree: `/Users/mgubi/ym-terminology`. Files: `manuscript/HumanizeYM_v3/chapters/11-marked-insertions.tex` (lines 1181–2355 only), `11-restarted-history.tex` (11R) and `11-equation-calibration.tex` (11E).

Method:
- I read the word diff `4f462ac5..HEAD` for each file: about 175 changed lines in 11:1181–2355, 110 in 11R and 30 in 11E. I also read the present text of all three ranges in full.
- Only after that did I read `ch11-c3b-apply.md`, `ch11-c3b-review.md` and `ch11-c4-apply.md`. 11R and 11E are covered by c4, which has no first-round review.
- Dictionary entries checked: the table, *delay*, *threshold for the starting scale*, *block floor*, *floor*, *restoration levels*, *leading*, *top level*, *bottom*, *comparison level*, *weight restoration*, *endpoint*, *re-expression of the endpoint*, *recording scale*, *genuine*, *neutral*, *clip*, *value cost*, *expense*, *envelope*, *corrected body product estimate*, *coupling band*, *deletion-of-support identities*, *front-column*, *rooted*, *same-data restart conditions*, *site conversion*, *tolerance exponent*, *trial descent*, *protected trial*, *protected*, *alphabet*, *exterior row*, *determinant-word series*, *finite decorations*, *transport*, *mesh threshold*, *plant*, *stencil*, *sliced-integrand level*, Appendix D B5.
- Line 1238 reads exactly `$\|Au\|\le H^{bd+c_d}$, choose $D>bd+c_d+v$ before the stage` (not touched).
- 11E:25–30 is stated as part of "the stage-$j$ lower bound on the block ratio", which is correct for a floor on `L`.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 11:1410; 11:1930, 2085, 2092; 11R:68 (title), 89, 384, 387 | TERM (ambiguity; same kind as r6's "lowest scale") | "leading step"; "endpoint re-expression"; "top level $k$"; "endpoint"; "Re-expression of the endpoint"; "selected trajectory's endpoint bounds" | "from the top scale to the middle scale"; "change of representation at the top scale"; "at the top scale $k$"; "density at the top scale"; "top-scale bounds" | `k` has the largest scale index of the window (`S=a_\ell/a_k\ge H^{b+2}`, 11:1754, 1763; `D_i=\mathcal B D_{i+1}`, 11R:233). It is therefore the *finest* lattice spacing. The book's "scale" means lattice spacing, so "top scale" reads as the coarsest. The index `k` already has a name in the chapter, *comparison scale* (r6 at 734–737, 1149). | "comparison scale" in each place (11R:89: "the bounds at the comparison scale of the construction of Chapter 10") |
| 11R:218 | TERM | "window with top level $k$, reference inverse coupling $s=x_k$" | "window with top scale $k$, reference inverse coupling" | The "top" ambiguity, as above. *Reference coupling* is the book's name for `β̂` (10:38–157; 11R:10). | "window with finest scale $k$, reference coupling $s=x_k$" |
| 11R:7, 70; 11:1343, 1361, 1401, 2032, 2035, 2064, 2180, 2209 | LEFTOVER | comparison level / depth | unchanged | *comparison level* entry (proposed *comparison scale `k`*). r6 already changed 734, 737 and 1149. c3b kept these "per assignment". | "comparison scale(s)"; 2209 "at that scale" |
| 11R:47, 50, 65, 115, 245; 11:1211, 1355 | MISMATCH | "actual (inverse coupling) band"; "reference-inverse-coupling band" | "inverse coupling band" | Chapter 10 defines "the coupling band" (10:212), and chapter 6 uses it (6:623, 878, 1155). | "coupling band" |
| 11R:246 | MISMATCH | "the reference inverse couplings" | unchanged | Same object as the *reference coupling* `β̂` | "the reference couplings" |
| 11E:113 | LEFTOVER | "These are post-length threshold conditions." | unchanged | *threshold for the starting scale* (R): "post-length" means imposed after the block ratio is fixed. 11E:106 already says "conditions on the starting scale". | "They are imposed after the block length is fixed." |
| 11:1343 | MINOR (accepted) | "the inverse front-column bounds" | "the front-column bounds" | The word "inverse" was dropped. This changes the words, but entry *front-column* (S) and App. D call "inverse" misleading. | left |
| 11R:239 | MINOR (accepted) | "all deletion-of-support identities supply" | "all deletion identities \eqref{ch08:deletion-identity} give" | A reference was added. This is the dictionary's own proposal (S), and the label exists. | left |
| 11R:300–301 | MINOR (accepted) | "…components with an actual selected prescribed set of large-field sites, and to a selected component within each such component" | "…connected components that contain large-field sites, and within each such component to one constituent carrying the selected component bound above" | The meaning is newly worded. It is App. D B5 applied without its parenthesis, and B5 is based on S. | left; see "For the author" |
| 11:1662–1663, 1666, 1673, 1911, 2306; 1589 | MINOR (accepted) | "corrected body product estimate"; "same-data restart conditions"; "tolerance exponent"; "original marked alphabet"; "protected trial"; "ordinary bound by one" | proposals of the respective entries (S); 1589 adds `\eqref{ch11:higher-induction}` | Each follows its entry's *Proposed* field. The added references exist and say what the text claims: 1892 uses the same `\eqref` for the same bound; 1602 for `ch11:integrated-component`. | left |
| 11R:266 | MINOR (accepted) | "exterior row, determinant and Haar bounds" | "remote action-term, local determinant and Haar bounds" | "Local" was added. The *exterior row* entry (S) supports it: these are the local determinants outside the selected components. | left |
| 11:2014 | LEFTOVER | "A genuine additive value error $\delta$" | unchanged | *genuine* (D) means full density; *value cost* (R) means sup-norm bound per site. A short wording is not clear. | left for the author |
| 11:1788, 1813 | MINOR | "transported" | "conjugated" | *transport* sense 4 proposes "image under / conjugation by". `\mathcal L\kappa\mathcal L^T` is a congruence, but the term is acceptable. | left |
| 11R:142 vs 281, 320–321 | MINOR | "support conversions" (142, unchanged) | 281, 321: "change of cover radius" | 142 covers both senses of *site conversion*, while 281 and 321 cover only sense 2. The difference is consistent with the entry. | left |

All other changed lines: I accepted the meaning, the word and the language. This includes the following:
- *delay* → "lower bound on the starting scale" (12 places), with the sentences still parsing;
- *frame* → "basis";
- *leading* → "upper"/"principal";
- *rooted activity norm* → "incidence bound" (proposal);
- failed-cutoff factors → "large-field factors" (these are `(1-\chi)R` for the restarted small-field indicator, 1495–1496, so they are not large fluctuation-field events);
- *genuine/neutral* → "full density" / "reduced density" (defined at 11R:197 before use);
- *clip* → "piecewise quadratic--linear function";
- *recording scale* → "auxiliary reference parameter" (defined at 11R:25/33);
- 11E's *stencil* → "link support(s)", *ordinary/complementary* → "small-field"/"large-field part", *trial descent* → "backward comparison";
- *plant* → "place … in distinct cells" (supported at 2341);
- *mesh threshold* → "lower bound on $N$" (`N` is the cutoff throughout chapter 11).

"Upper interval" is defined at its first use (1410). *Averaging operation* at 11R:247 is used for the nonlinear average.

## Corrections applied

37 replacements on 28 lines. Line counts are unchanged: 2355, 393, 185.

| class | lines | count |
|---|---|---|
| TERM | 11:1410, 1930, 2085, 2092; 11R:68, 89, 218, 384, 387 | 9 lines |
| LEFTOVER | 11R:7, 70; 11:1343, 1361, 1401, 2032, 2035, 2064, 2180, 2209; 11E:113 | 11 lines |
| MISMATCH | 11R:47, 50, 65, 115, 245, 246; 11:1211, 1355; plus "reference coupling" at 11R:218 | 8 lines + 1 |

No ERROR (meaning change) was found in the converted lines of my range.

## Cross-chapter mismatches not fixed

- "inverse coupling band" remains at 11:693 (r6's range), 9:386, 9:429 ("reference-inverse-coupling bands"), 10:676, and 17m:312. Chapter 10 (10:212) and chapter 6 say "coupling band".
- "reference inverse coupling" remains at 10:524 and 11:743 (r6's range). Elsewhere the text says "reference coupling".
- "comparison level" remains at 13:163–165, 14:226–227, 14lc:23 ("comparison depth") and 15:253.
- 11R:89 cites "the construction of Chapter 10" (c4's choice under *trajectory* 2). 11:2176 and 2294 still say "the selected trajectory".

## Leftover house words

Kept on purpose:
- *physical*: 11R:60 ("physical covariance factors", sense 6, I), 11:2305 ("exact physical difference identity", I), 11E:185 ("physical convention", I).
- *actual*: "the actual probability of a large fluctuation-field event" (11:1613), listed under *large fluctuation-field event*.
- *endpoint*:
  - 11E:124 (sense 4, I);
  - "All endpoints" (11:2287, sense 6, ordinary).
- *reserved mass*: 11E:104, 117 (basis I).
- "sliced-integrand level" (11R:358): *sliced-integrand level*, basis I.
- *label*: "polynomial label space", "equation labels" and "free label" are defined objects. "Label choices" (11R:304) is the dictionary's own proposal.
- *weight*: "averaging weight" (11R:112) is the coined term. "Probability weights" and "support weight(s)" are standard or defined.
- *floor*: "metric floors" (11R:247), sense 2, I.
- *unit*: "extra unit" / "one additional unit in the exponent" means one unit of the support exponent.
- *tree*: "The tree uses …" (11:1985) is a spanning tree in the graph sense.
- *marked*: "marked" / "unmarked" occur only inside math (`\rho_{\rm marked}`, `\text{unmarked exponent}`, 11:1581–1582).

Replaced: comparison level/depth (10 lines), post-length threshold conditions (1).

Left for the author: "genuine additive value error" (11:2014).

## Assessment of the first review's corrections

c3b-review (11:1181–2355): its corrections at 1410 (defining "upper interval" at its first use), 2092 ("density at the top scale") and the others are right in substance. Its choice of "top scale" for `k` carries the ambiguity, and I corrected it to "comparison scale".

c4 (11R, 11E) had no first review. Its changes are correct apart from the following:
- the "top scale" wording;
- "inverse coupling band" / "reference inverse coupling", which it left;
- the "comparison level" leftovers.

## For the author

- 11R:218: I wrote "finest scale $k$". "comparison window below the comparison scale $k$" would also do.
- 11R:300–301 (B5): check whether "constituent carrying the selected component bound above" reads as intended. The source's "to each, if there are several" was not added.
- 11:2014: "A genuine additive value error $\delta$". Possible wording: "an additive term of the full density with sup-norm bound $\delta$ per site".
- 11E:124: "endpoint estimate" (sense 4, I). The proposal is "estimate at the last step".
- 11R:89: either "selected trajectory" (as 11:2176, 2294) or "the construction of Chapter 10". One name should be chosen.

## Checks

- Line counts equal HEAD for all three files (2355 / 393 / 185). No line outside 1181–2355 of the main file was changed.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r7 monograph.tex`: exit 0. The log has 0 "undefined", 0 "Citation" and 0 "Overfull".
- I found the corrected passages in the extracted PDF text (Proposition 11.3 title, 11R:218, 11E:113, 11:1410).

## Not checked

- I did not visually inspect the rendered pages beyond text extraction.
- I did not read the source manuscripts or Bałaban's papers. I relied on the dictionary's *Source* lines.
- I did not grep every name of the brief's point 4 in every chapter. I checked: comparison level/scale, top/finest scale, coupling band, reference coupling, upper/lower interval, larger source weight, reduced density, auxiliary reference parameter, link support, selected trajectory, dependence set, averaging operation, large fluctuation-field event, margin/support reserve.
