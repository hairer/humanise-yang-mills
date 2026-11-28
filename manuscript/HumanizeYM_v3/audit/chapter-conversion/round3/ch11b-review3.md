# Third review t7: chapter 11, lines 1181–2355; 11-restarted-history.tex (11R); 11-equation-calibration.tex (11E)

Worktree `/Users/mgubi/ym-terminology`. I read the word diff `4f462ac5..HEAD` for 11:1181–2355 (about 175 changed lines), 11R (about 110) and 11E (about 30). I compared each against the present text around it. Only then did I read `ch11-c3b-apply.md`, `round2/ch11b-review2.md`, `round3/ch11a-review3.md` and the leads. Dictionary entries read: *cutoff failure*, *large-field factor*, *large fluctuation-field event*, *delay*, *floor*, *block floor*, *leading*, *top level*, *mesh threshold*, *plant*, *descent*, *trial descent*, *frame*, *endpoint*, *moving*, *protected*, *stencil*, *rooted*, *incidence*, *coupling band*, *front-column*, *corrected body product estimate*, *same-data restart conditions*, *tolerance exponent*, *alphabet*, *exterior row*, *row*, *history*, *normalization index*, *window*, *presentation*, *remote*, *site conversion*, *detection*, *extraction*, *transport*, *physical*, *common Gaussian*. I also read the book-wide table. Other text checked: 5:148–212 (alias formula, "centered box multiplier"), 5:281–319 (blocking sequence), 6:1166–1182, 8:300–330 (`ch08:reassembly`), and Martin `existence/restarted-rank-history.tex:630–680` for 11R:300–301.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 11:1476, 1487, 1500, 1523, 1932 | TERM / MISMATCH (point a) | "failed-cutoff factor(s)"; 1932 "Every nonzero failed cutoff" | "large-field factor(s)" | The object is `1−(1−χ)Rz_I`, with `χ` the restarted small-field indicator (1309). It is nonzero only where its support "contains a large-field indicator covered by an original prescribed large-field set" (1495–1496). At 1932 the same factors meet new large-field sites, and they are suppressed by the large-field site factor `e^{-2u}` (1933–1935; 11R:114–116). They are not suppressed by a joint Gaussian tail. So this is a failure of the regularity condition at the new threshold, a large-field site. It is **not** a large fluctuation-field event (sense 1 of *cutoff failure*). The second reviewer said the same. The name "large-field factor" collides with the incoming large-field factors of 11:245, 250, 332, 424, 923 and 10:654. As the assignment directs, I restored the old wording. | "failed-cutoff factor(s)" (1476, 1487, 1500, 1523); "failed cutoff" (1932) |
| 11:1325–1326 | MISMATCH (lead b) | "coefficient extraction $T$" | unchanged | `T` is called the "common localization map" at 1307, 1330, 1836, 2057, 2214, in the section title at 1141, and at 14lc:30 and 17w:100. | "common localization map $T$" |
| 11:2092 | MISMATCH (lead b) | "unchanged top map and endpoint" | "unchanged top map and density at the comparison scale" | "Top map" is the map `T` constructed "at the comparison scale `k`" (2085). The word "top" is the ambiguity that round 2 removed elsewhere. | "unchanged localization map and density at the comparison scale" |
| 11:2307 | MISMATCH (lead b) | "in its normalization index" | unchanged | Chapter 2 calls the index `d` of `V_d` the *filtration index* (2:96, 402). Note that the factor `a_N^{|l|}` is part of the normalization at that index; it is not part of the index. | "in the normalization at its filtration index" |
| 11:1731 | MISMATCH (lead b) | "box-filter identities" | unchanged | Chapter 5 calls the symbol of the box average the "centered box multiplier" (5:209; "centered-box factors" 5:760, 817). "Box filter" occurs only here. | "box-multiplier identities" |
| 11:2078, 2149 | MISMATCH (lead b) | "compact configuration window"; "the compact window" | unchanged | The same set is the "compact configuration set" at 2048 and the "compact separated configuration set" at 2124, and a "compact set of separated configurations" in chapter 14. "Window" has other senses in the chapter (the comparison window). | "compact configuration set" (both) |
| 11R:71, 196, 222, 251, 339 | MISMATCH (lead c) | "presentation(s)" | unchanged | This is one object under two names in the same file: "The new representation at scale index $i$" (11R:18) and the proposition title "Change of representation …" (11R:68). Chapter 11 says "local representation" (11:122). | "representation(s)" |
| 11R:269–270 | ERROR (attachment; lead c) | "The two determinant-word series and inverse correction are exponentially small" | "The two Neumann series of the determinant and inverse correction are exponentially small" | The old sentence lists three items: two series and the inverse correction. Martin's actual-corrected-body-compiler lists separately "the quadratic inverse correction", "the relative logarithmic determinant series" and "its inverse-correction logarithmic series". The new wording reads naturally as two series, one of the determinant and one of the inverse correction, so the inverse correction is lost as a third item. | "The inverse correction and the two Neumann series of the determinant are exponentially small" |
| 11R:266 | LEFTOVER (lead c) | "the corresponding exterior row, determinant and Haar bounds" | "the corresponding remote action-term, local determinant and Haar bounds" | "Remote" is replaced elsewhere by "far from the large-field set" (*remote* sense 1, R: 6:1008, 1249; 9:280; 11:709). "Remote action-term … bounds" is also a pile of nouns. | "the bounds for the corresponding action terms far from the large-field set, and the local determinant and Haar bounds" |
| 11R:300–301 | ERROR-risk (scope; lead c) | "Apply the factor $m$ only to components with an actual selected prescribed set of large-field sites" | "…only to connected components that contain large-field sites" | The old text, the source ("Each forced body component contains an owner. Charge its factor $m$ to such an owner", restarted-rank-history.tex:640–641) and the inflation rule at 11:277 all refer to a **nonempty prescribed large-field set**. "Contain large-field sites" is a condition on the support. It agrees with the old text only through the exact-coverage conditions, and it is not stated as such. The second half ("within each such component to one constituent carrying the selected component bound above") agrees with the source and stays. | "…only to connected components with a nonempty prescribed large-field set, and within each such component …" |
| 11E:113 | LANGUAGE | "These are post-length threshold conditions." | "They are imposed after the block length is fixed." | "They" has no plural antecedent in the previous sentence ("Then $|D|\le q_d$ bounds …"). It refers back to the conditions displayed at 106–110. | "These conditions are imposed after the block length is fixed." |
| 11E:171 | MISMATCH (lead d) | "free nondegeneracy and detection estimates" | unchanged | "Detection" is the old name of the separating property. The same estimate is "the bound from the separating family \eqref{ch11:detector-bound}" at 11E:183. | "free nondegeneracy and separating-family estimates" (plural kept) |
| 11:1699 | MISMATCH (lead b) | "uniform in the kernel history" | unchanged | Two readings are possible. The dictionary (*history* sense 1) reads it as the blocking sequence (5:303), which fits the uniformity over blocking sequences proved in chapter 5 (5:281, 298, 319). Reviewer t6 reads it as the sequence of quadratic kernels. The words do not settle which is meant. | left for the author ("uniform in the blocking sequence" if that is meant) |
| 11R:142 | MINOR (lead c) | "These are the support conversions of Section ch06:primitive-bounds" | unchanged apart from "they lose factors" | The phrase covers both the change of cover radius and the passage from anchored to site bounds (*site conversion*, senses 1 and 2). Section 6 (1166–1182) defines the containing-site bound but does not use the word "conversion". | left for the author |
| 11R:376 | MINOR (lead c) | "exact factorization and reassembly" | unchanged | Chapter 8 calls `\eqref{ch08:reassembly}` an "exact factorization" (8:310) and a "factorization identity" (8:279, 355). Here "factorization" may instead mean the Gaussian factorization of the step, so I could not tell whether "reassembly" is redundant. | left for the author |
| 11R:351, 365 | — (lead c) | "regular logarithm(s) (with holes)" | unchanged | Correct as it stands. This is the logarithm of the regular part of the action (the regular family `E`, 11R:197, 339–340). "Regular" is kept for the regular part by the book-wide table, so it is not the polymer gas of chapter 8. | no change |
| 11:1788, 1813 | MINOR | "transported" | "conjugated" | `B_0=\mathcal L\kappa_\ell\mathcal L^T` is a congruence, not `\mathcal L\kappa\mathcal L^{-1}`. "Conjugated" is the dictionary's proposal (*transport* sense 4) and is common loose usage. Round 2 accepted it. | left for the author ("image under $\mathcal L$" or "transferred" would be exact) |
| 11:1765, 1787 | MINOR | "closed background" | "closed background field" | "Field" was added. The table defines *background field* as a configuration about which one expands, and `u` is the conditioning curvature cochain, so the word is acceptable. Note that 1:452 and 5:7 use "background field" for the critical configuration. | left |
| 11:1343 | MINOR (accepted) | "inverse front-column bounds" | "front-column bounds" | "Inverse" was dropped on purpose (Appendix D; second review). The bound given, `‖u‖≤D_k‖Au‖`, is unchanged. | left |
| 11R:239 | MINOR | "all deletion-of-support identities supply" | "all deletion identities \eqref{ch08:deletion-identity} give" | A plural cited by one equation. Here "all" means all instances of that one identity, so the claim is not widened. | left |

## Corrections applied

28 line edits: 12 in 11:1181–2355, 14 in 11R, 2 in 11E. Line counts are unchanged at 2355 / 393 / 185.
- TERM / MISMATCH: 22 lines (11:1325, 1326, 1476, 1487, 1500, 1523, 1932, 1731, 2078, 2092, 2149, 2307; 11R:71, 196, 222, 251, 339; 11E:171; 11R:300–301 counted under ERROR)
- ERROR (scope, attachment): 4 lines (11R:269, 270, 300, 301)
- LEFTOVER: 1 (11R:266)
- LANGUAGE: 1 (11E:113)

## Cross-chapter mismatches not fixed

- "Kernel history" (11:1699) against "blocking sequence" (5:303; 10:373) and "block history" (11:92).
- "Comparison window" (11, 11R) against "interval of scales" (10:185; 17w). The dictionary chose not to apply "interval of scales" in chapter 11.
- "Coefficient map 𝖹" (11E:184; 11:1136) against `M_G`, "coefficient map" (11:381). See t6.
- "Support conversions" (11R:142) against "change of cover radius" (11R:281, 321; 18lp:112).
- "Reassembly" (11R:376; 9:57) against "factorization identity" (8:279).
- "Selected history" (11:2183) and "selecting the common history" (11E:34) against "common trajectory" (11:2176, 2294).
- "Detection" in the section title 11:960 (outside my range; t6 left it for the author).

## Leftover house words

Kept on purpose:
- *actual*:
  - 11:1613, "the actual probability of a large fluctuation-field event". This is ordinary use and contrasts with the bound.
- *physical*:
  - 11:2305, "exact physical difference identity" (I);
  - 11R:60, "physical covariance factors" (sense 6, I);
  - 11E:185, "physical convention" (I).
- *marked* / *unmarked*: only inside math (`\rho_{\rm marked}`, `\text{unmarked exponent}`, 11:1581–1582).
- *weight*: these are source weights, support weights, probability weights, the "averaging weight" at 11R:112 (unchanged from the old text) and "weighted" norms. All are defined or ordinary.
- *label*: "polynomial label space", "equation labels", "free label" and "labels of bounded degree" are defined objects. "Label choices" (11R:304) is the dictionary's proposal.
- *unit*: "one additional unit of the support exponent" (11:1446) and "extra unit" (11R:141) are ordinary use.
- *tree*: "The tree uses …" (11:1985) is a spanning tree in the graph sense. "Tree gauge" was already replaced by "Axial gauge" at 1975, which is correct, since the tree is the comb tree `(x−e_{p(x)},p(x))`.
- *failed*: the restored "failed-cutoff factor" / "failed cutoff" (11:1476–1932), as the assignment directs.

Missed: none found. None of the following occurs in my ranges: tag, block average, predictor, stationary, noise, frame, level, block transformation, reset, heat, mixed, ground, kill.

## Leads

- (a) "Large-field factor" (11:1476–1932). I checked the text at 4f462ac5. The object is `1−(1−χ)Rz_I` for the restarted small-field indicator. It is suppressed by large-field site factors, not by a Gaussian tail, so it is not a large fluctuation-field event. I **restored** the old wording at 1476, 1487, 1500, 1523 and 1932. 1562 ("Its large-field part …") and 1636 ("Its large-field part retains the original prescribed large-field set") stay. Both are the chapter's *large-field part* of an insertion, the complement of the small-field indicator (as at 11:150, 941), which is correct.
- (b) Results:
  - "extraction `T`" (1326): replaced by "common localization map".
  - "top map" (2092): replaced by "localization map".
  - "kernel history" (1699): left for the author, since two readings are possible.
  - "normalization index" (2307): replaced by "filtration index", with the normalization stated.
  - "box-filter identities" (1731): replaced by "box-multiplier identities", the wording of chapter 5.
  - "compact configuration window" (2078, 2149): replaced by "compact configuration set".
- (c) Results:
  - "presentation": replaced by "representation" at all 5 places.
  - 11R:266 "remote": replaced.
  - 11R:270: rewritten, because the inverse correction had become ambiguous as a third item.
  - 11R:300–301: the first half has been restored to "nonempty prescribed large-field set" (old text and source), and the second half was kept.
  - 11R:351, 365 "regular logarithm": correct as it stands.
  - 11R:142 "support conversions": left.
  - 11R:376 "reassembly": left.
- (d) 11E:171 "detection": replaced by "separating-family estimates".
- (e) 11:1238: not touched.
- Other leads touching my files:
  - 17w:78 (the "step estimates" plural) is outside my files.
  - "comparison window" against "interval of scales" is listed above.
  - 11R:218 "finest scale `k`" was checked: `k` has the largest scale index, so it is the finest scale, which is right.

## Assessment of earlier corrections

- Harmonisation / c3b: "large-field factor" for the failed-cutoff factor at 1476–1932. This introduced a second sense of an existing term and has been reverted. Round 2 noted that the object is not a large fluctuation-field event, but it did not flag the name collision.
- Appendix D B5, applied by c4 and accepted by round 2 (11R:300–301): "contain large-field sites" loosened "nonempty prescribed large-field set". Corrected.
- Harmonisation (11R:270): "determinant-word series" became "Neumann series of the determinant", and the inverse correction ended up attached as though to a second Neumann series. Corrected.
- Round 2 (11E:113): "They" replaced "These" and lost the antecedent. Corrected.
- The other corrections of rounds 1 and 2 in my ranges are right:
  - "comparison scale" for `k`, "finest scale" (11R:218), "coupling band", "reference coupling";
  - "upper interval" defined at 1410;
  - "lower bound on the starting scale";
  - the added references at 1589, 1662–1663, 1666, 11R:89, 11R:239. All exist, and the claims agree with them.

## For the author

- 11:1476–1932: "failed-cutoff factor" was restored as the assignment directs, but "failed cutoff" is itself a house word. A non-house name for this object would be "factor of the failure of the (relaxed) regularity condition at the restarted threshold", or simply "factor of the large-field part `(1−χ)R`". It must not be "large-field factor", which names the incoming factors at 11:245–923 and 10:654, and it must not be "large fluctuation-field event".
- 11:1699 "kernel history": should this read "blocking sequence"?
- 11:1788, 1813: "conjugated" for a congruence `\mathcal L\kappa\mathcal L^T`.
- 11R:142 "support conversions"; 11R:376 "reassembly".
- 11:1514 "its factor is at most $H^{Un+2^n}$". "Its" refers to the power of `H` in `w_o`, which is clear but loose.
- 11:2014 "A genuine additive value error" (round 2 already listed this).

## Checks

- `wc -l`: 2355 / 393 / 185, equal to `git show HEAD:… | wc -l`. No line of 11:1–1180 was touched; the edits in that file are only at 1325–2307.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-t7 monograph.tex`: exit 0. `monograph.log` has "undefined" 0, "Citation" 0 and "Overfull" 0.

## Not checked

- I did not inspect the rendered pages; `pdftotext` is not available.
- Apart from restarted-rank-history.tex:630–680, I did not read Martin's sources or Bałaban's papers.
- I did not grep every pair in brief point 4 across all chapters. I checked these: large-field factor, large fluctuation-field event, localization map, filtration index, box multiplier, compact configuration set, representation/presentation, remote, separating family, blocking sequence/kernel history, background field, coupling band and common trajectory.
