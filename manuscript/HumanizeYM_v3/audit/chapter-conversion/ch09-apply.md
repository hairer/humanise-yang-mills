# Chapter 9: vocabulary applied (job c1)

Files: `chapters/09-renormalization.tex` (`9`, 182 lines changed of 979) and `chapters/09-forest-average.tex` (`9f`, the new subsection of 24 November, 65 lines changed of 973), in the worktree `/Users/mgubi/ym-terminology`. Nothing committed or staged. Every edit is inside one line; no line was added, removed, joined or split. In `9f` only leftover house words were changed; the Assumption, the statements and the proofs are otherwise untouched (words inside them, such as "anchor" → "base point" and "regular activity" → "localized term", were changed as words only). In `9` the lines edited on 24 November (75, 148, 161, 234, 239–240, 313, 331, 351, 362, 367, 398, 521, 525, 867, 903, 919, 924–926, 955) keep their mathematical content; only words were replaced in 148, 234, 239, 367, 867, 919, 924, 926.

The edits were applied by a script that checks that each "before" string occurs exactly once in the named line (scripts and logs: `c1_edit9.py`, `c1_e9.py`, `c1_e9b.py`, `c1_ef.py`, `c1_log9*.json`, `c1_logf.json` in this directory).

## Changes

The columns give the changed words only; the rest of each line is unchanged. Two rows with the same line number are two edits in that line.

### `9` (09-renormalization.tex)

| line | before | after | decision or entry |
|---|---|---|---|
| 5 | `A block transformation acts on the density` | `A step acts on the density` | table: step |
| 6 | `of local terms. Our task is to express its exact output in the` | `of local terms. Our task is to express its exact output by the` | density coordinates (D): representation data |
| 7 | `coordinates of Chapter~\ref{ch04:blocking}, while` | `representation data of Chapter~\ref{ch04:blocking}, while` | density coordinates (D): representation data |
| 15 | `Fix one adjacent pair of scales, with fine scale` | `Fix two consecutive scales, with fine scale` | adjacent pair 1 (R) |
| 17 | `The actual incoming inverse coupling is` | `The incoming inverse coupling, unlike the reference value $\mathfrak b$, is` | actual 4 (R): contrast with the reference coupling |
| 26 | `$\mathcal L$ is the quadratic loop correction.` | `$\mathcal L$ is the $\beta$-independent quadratic term.` | inherited loop action / separate quadratic correction (R), as 6:170, 7:237 |
| 41 | `one Gaussian law, a local low-order matching estimate, and a` | `one Gaussian law, a local low-order matching estimate, and an` | grammar after 42 |
| 42 | `one-loop drift estimate are different inputs.` | `estimate of the one-loop shift of the coupling are different inputs.` | one-loop drift (R) |
| 44 | `The exact local integral and its first expansion` | `The exact local integral and its Mayer expansion` | table: Mayer expansion |
| 56 | `Here is the scalar bookkeeping in a form useful for checking` | `Here is the bookkeeping of the normalization constants in a form useful for checking` | scalar 1 (D) |
| 57 | `Suppose there are $N_{\rm free}$ free tree-gauge` | `Suppose there are $N_{\rm free}$ non-tree` | free (R), as ch. 6; table: block axial gauge (tree gauge) |
| 59 | `let $D$ be the dimension after dummy Gaussian coordinates have` | `let $D$ be the dimension after auxiliary standard Gaussian coordinates have` | dummy Gaussian coordinates (R) |
| 63 | `With $a=\mu+gz$, the measure multiplier before the Haar` | `With $a=\mu+gz$, the constant factor of the change of variables before the Haar` | measure multiplier (R) |
| 72 | `The dummy Gaussian integral equals one` | `The auxiliary Gaussian integral equals one` | dummy Gaussian coordinates (R) |
| 77 | `logarithm, missing-coordinate factor and stationary residual` | `logarithm, missing-coordinate factor and residual of the mean equation` | stationary residual (R) |
| 82 | `allocation indicators. A complete dependence region contains` | `allocation weights. A complete dependence set contains` | App. D 9:81-82; dependence region (D), as ch. 4, 6 |
| 83 | `every Haar coordinate, tag variable and Gaussian covariance` | `every Haar coordinate, auxiliary index $\alpha$ and Gaussian covariance` | tag 1 (D) |
| 84 | `halo read by its factor.` | `neighborhood read by its factor.` | halo (R) |
| 85 | `the Haar and tag coordinates are independent;` | `the Haar coordinates and auxiliary indices are independent;` | tag 1 (D) |
| 88 | `Connected components of intersecting dependence regions define` | `Connected components of intersecting dependence sets define` | dependence region (D) |
| 89 | `the first polymer activities.` | `the polymer activities of the Mayer expansion.` | table: Mayer expansion (first polymer activities) |
| 91 | `This factorization concerns dependence regions.` | `This factorization concerns dependence sets.` | dependence region (D) |
| 93 | `have disjoint full dependence regions.` | `have disjoint full dependence sets.` | dependence region (D), as 6:1179 |
| 94 | `The large-field indicators in their eligibility criteria can read outside $Y_i$.` | `The large-field indicators in their additional conditions can read outside $Y_i$.` | eligible 2 (D), ch. 4 word |
| 105 | `Here $\nu$ is the one sector Gaussian/Haar law,` | `Here $\nu$ is the joint Gaussian/Haar law of one sector,` | one sector Gaussian/Haar law, common law (R) |
| 107 | `derivatives, $s_M$ counts the full dependence region in` | `derivatives, $s_M$ counts the full dependence set in` | dependence region (D) |
| 108 | `radius-$B$ blocks, and $A_M$ is its selected large-field condition set.` | `radius-$B$ blocks, and $A_M$ is the part of the index triple belonging to $M$.` | selected 1 (D), ch. 6 word index triple |
| 111 | `ratio. Distinct cutoff-failure labels each contribute their` | `ratio. Distinct event labels each contribute their` | cutoff-failure label, label 8 (D), ch. 6 word |
| 114 | `proves this joint` | `proves this` | joint bound (R): avoid 'joint bound under their joint law' |
| 115 | `bound on their common law.` | `bound under their joint law.` | common law, joint bound (R) |
| 115 | `The alternative quadratic-tilt criterion` | `The alternative hypothesis on tilted Gaussians` | quadratic-tilt criterion (R) |
| 124 | `\text{factor after deterministic subtraction}&\text{majorant}\\ \hline` | `\text{factor}&\text{integrated majorant}\\ \hline` | App. D 9:124 |
| 125 | `\text{stationary cubic remainder}` | `\text{cubic remainder at the critical configuration}` | table: critical configuration |
| 130 | `\text{covariance and stationary residual}` | `\text{covariance and mean-equation residual}` | stationary residual (R) |
| 132 | `\text{incoming regular activity}` | `\text{incoming localized term}` | table: localized term |
| 133 | `\text{cutoff failure at a distinct label}` | `\text{large fluctuation-field event at a distinct event label}` | table: large fluctuation-field event; event label |
| 139 | `coordinates. The latter is estimated inside the common integral.` | `coordinates. The latter is estimated inside the joint integral.` | common 2 (R) |
| 140 | `The other rows follow from the determinant inverse identity,` | `The other rows follow from the resolvent identity for the determinant,` | App. D 9:140 |
| 145 | `After increasing the inverse coupling threshold these rows are bounded` | `After increasing the lower bound on the reference coupling these rows are bounded` | coupling threshold (R), as ch. 6 |
| 148 | `additional exponential support decay. The first component expansion,` | `a margin in the decay rate of the support weight. The Mayer expansion,` | support-weight reserve (R), as ch. 8; table: Mayer expansion |
| 150 | `logarithm of the ordinary gas without large-field sites.` | `logarithm of the polymer gas without large-field sites.` | ordinary 1 (R); regular activity 2 |
| 151 | `a prescribed large-field site set remain` | `a prescribed large-field set remain` | prescribed set of large-field sites (D), ch. 4 word |
| 153 | `for ordinary polymers excluded by a selected large-field region.` | `for small-field polymers excluded by a chosen large-field region.` | ordinary 1 (R); selected 4 (R) |
| 157 | `All rearrangements can first be made for finite selections.` | `All rearrangements can first be made for finite subfamilies.` | selected 4 (R) |
| 159 | `the absolute envelopes allow passage` | `the absolute majorants allow passage` | envelope (R) |
| 172 | `Give every elementary ordinary factor a degree one, and give` | `Give every elementary small-field factor a degree one, and give` | ordinary 1 (R) |
| 173 | `a first-expansion polymer the sum of its factors' degrees.` | `a polymer of the Mayer expansion the sum of its factors' degrees.` | table: Mayer expansion |
| 180 | `applied with these inflated activities,` | `applied with these rescaled activities,` | inflated activities (D/R), as ch. 8 |
| 190 | `The gap $19/16-23/20=3/80$ absorbs` | `The difference $19/16-23/20=3/80$ of the exponents absorbs` | gap 5 (R) |
| 192 | `second cluster expansion; a single polymer may already have` | `exponentiated cluster expansion; a single polymer may already have` | table: exponentiation |
| 196 | `An incoming regular activity accompanied by a further factor` | `An incoming localized term accompanied by a further factor` | table: localized term |
| 197 | `with that incoming activity` | `with that incoming term` | table: localized term |
| 201 | `Both fit the right side of` | `Both are bounded by the right side of` | fits (R) |
| 202 | `increasing the threshold.` | `increasing the lower bound on the reference coupling.` | threshold 1 (R) |
| 206 | `The component linear in an incoming regular activity must use` | `The component linear in an incoming localized term must use` | table: localized term |
| 208 | `lifted potential splits into parts with inverse-ratio sizes` | `lifted potential splits into parts with sizes` | inverse-ratio sizes (R): the powers of L^{-1} follow on 209 |
| 211 | `Curvature therefore begins at weight` | `Curvature therefore begins at scaling dimension` | weight 1 (D): scaling dimension |
| 214 | `quadratic curvature term of weight four. Every surviving` | `quadratic curvature term of scaling dimension four. Every surviving` | weight 1 (D) |
| 215 | `selection in the ordered Taylor expansion has weight at least` | `term in the ordered Taylor expansion has scaling dimension at least` | selected 4 (R); weight 1 (D) |
| 220 | `For $d^3<L$ the inspected support admits a nonwrapping` | `For $d^3<L$ the support with its adjacent plaquettes admits a nonwrapping` | App. D 9:220 |
| 221 | `radial gauge and the per-label gain is $L^{-5}$.` | `radial gauge and the gain per term is $L^{-5}$.` | label 6 (R) |
| 230 | `Choose the scale ratio and incoming support exponent so that, after` | `Choose the scale ratio and the incoming decay rate of the support weight so that, after` | support exponent (R), as ch. 6 |
| 231 | `support compression, the outgoing weight uses at most half of the` | `passing to the coarse image of the support, the outgoing weight uses at most half of the` | App. D 9:230-232 |
| 234 | `There are $L^4$ fine anchors above each coarse anchor; an inherited term is anchored at the coarse site whose block contains its incoming anchor and is not divided` | `There are $L^4$ fine base points above each coarse base point; an inherited term has as base point the coarse site whose block contains its incoming base point and is not divided` | anchor 1 (D): base point, ch. 4 word |
| 239 | `For the comparison with the actual integral use,` | `For the comparison with the block integral use,` | actual 1: contrast named |
| 257 | `Hold the physical links in the incoming activity fixed by the` | `Hold the physical links in the incoming localized term fixed by the` | table: localized term |
| 261 | `one extra derivative of the incoming activity` | `one extra derivative of the incoming localized term` | table: localized term |
| 262 | `when adjacent levels have equal derivative orders.` | `when consecutive scales have equal derivative orders.` | level (R): scale |
| 264 | `nonquadratic local weights contribute a gain of order $g$ with` | `nonquadratic local factors contribute a gain of order $g$ up to` | weight 6 (R); loss 2 (R) |
| 265 | `subpower losses; a second incoming activity contributes` | `subpower factors; a second incoming localized term contributes` | loss 2 (R); table: localized term |
| 266 | `$O((\epsilon_{m+1}^{\rm reg})^2)$ instead. Common Gaussian moments` | `$O((\epsilon_{m+1}^{\rm reg})^2)$ instead. Joint Gaussian moments` | common Gaussian (R) |
| 267 | `and the unused support exponent sum the resulting polynomial costs.` | `and the margin in the decay rate of the support weight sum the resulting polynomial factors.` | support-weight reserve (R); cost 1 (R) |
| 278 | `For this comparison the local windows and their dependence halos` | `For this comparison the local windows and their dependence sets` | halo (R) |
| 279 | `must be clean. A window meeting a selected large-field component is` | `must be clean. A window meeting a large-field component of the index triple is` | selected 1 (D) |
| 280 | `assigned to that component; a failed remote cutoff has the joint` | `attributed to that component; a large fluctuation-field event far from the index triple has the joint` | assigned (R); table: large fluctuation-field event; remote (R), as ch. 6 |
| 282 | `remaining supports gain $e^{-cB}$ from the unused incoming support` | `remaining supports gain $e^{-cB}$ from the margin in the decay rate of the incoming support` | support-weight reserve (R) |
| 283 | `weight. Thus no comparison between unrelated event indicators or a seeded and` | `weight. Thus no comparison between unrelated event indicators, or between a sector with nonempty index triple` | App. D 6:1544 and 9:283-284, in ch. 6's applied wording |
| 284 | `an unseeded law has been made. The actual interpolation estimates` | `and the law with empty index triple, has been made. The interpolation estimates` | App. D 9:283-284; actual 5 (R): delete |
| 292 | `must apply to the same integral and stationary branch.` | `must apply to the same integral and critical configuration.` | branch 2 (R) |
| 304 | `$\mathfrak b^{-23/20}$. The argument below specifies the actual` | `$\mathfrak b^{-23/20}$. The argument below specifies the` | actual 1: delete |
| 355 | `The fourth-difference weights therefore give` | `The fourth-difference coefficients therefore give` | weight 6 (R) |
| 367 | `Thus $G_x$ is the small-field local activity and $L_x$ is a` | `Thus $G_x$ is the small-field localized term and $L_x$ is a` | table: localized term |
| 368 | `logarithmic correction supported where its enlarged` | `\emph{large-field correction}, a term of the exponent supported where its enlarged` | logarithmic correction (R): short term defined |
| 378 | `The first fits an arbitrarily small fraction of` | `The first is at most an arbitrarily small fraction of` | fits (R) |
| 383 | `The selected low-order terms contain no incoming regular or` | `The selected low-order terms contain no incoming localized term or` | table: localized term |
| 385 | `prescribed path, actual inverse coupling and fixed labels.` | `prescribed path action, the inverse coupling and fixed labels.` | path 2 (R); actual 4: deleted, the band follows |
| 394 | `\section{A precise preparatory output}` | `\section{A precise intermediate representation}` | preparatory output (R) |
| 399 | `activities $k_i$, and a scalar $\tau$ satisfying` | `activities $k_i$, and a constant $\tau$ satisfying` | scalar 1 (D) |
| 410 | `the matched determinant coefficient, not an adjustable` | `the determinant coefficient fixed by the matching, not an adjustable` | matched (R) |
| 426 | `$V_jL^{-1}\epsilon_{m+1}^{\rm reg}$ fits the desired fraction of` | `$V_jL^{-1}\epsilon_{m+1}^{\rm reg}$ is at most the desired fraction of` | fits (R) |
| 430 | `Then choose the inverse coupling threshold for the inherited` | `Then choose the lower bound on the reference coupling for the inherited` | coupling threshold (R) |
| 432 | `and the small logarithmic corrections.` | `and the small large-field corrections.` | logarithmic correction (R) |
| 434 | `localization costs have been specified.` | `localization factors have been specified.` | cost 1 (R) |
| 437 | `normalization losses, and the final large-field bound.` | `normalization factors, and the final large-field bound.` | loss 2 (R) |
| 438 | `Polynomial support costs use support-weight reserves.` | `Polynomial support factors use margins in the decay rate of the support weight.` | cost 1 (R); support-weight reserve (R) |
| 440 | `a single selected large-field condition.` | `a single large-field condition of the index triple.` | selected 1 (D) |
| 442 | `Equation \eqref{ch09:early} and its bounds are the concrete` | `Equation \eqref{ch09:early} and its bounds are the statement` | interface (R) |
| 443 | `interface for the rest of the chapter.` | `used in the rest of the chapter.` | interface (R) |
| 462 | `For a preliminary $f$ on $X$ anchored at $o$, put` | `For a preliminary $f$ on $X$ with base point $o$, put` | anchor 1 (D) |
| 476 | `It can be extended periodically using a cutoff outside` | `It can be extended periodically using a cutoff function outside` | cutoff 2 (R) |
| 477 | `the dependence region. Therefore` | `the dependence set. Therefore` | dependence region (D) |
| 500 | `dependence region; no derivative` | `dependence set; no derivative` | dependence region (D) |
| 510 | `own small-field conditions. Enlarging $X$ to $Z$ costs a bounded` | `own small-field conditions. Enlarging $X$ to $Z$ adds a bounded` | cost 1 (R) |
| 514 | `is explicit. If $x\in Z$ and $c(Z)=n$, its anchor lies` | `is explicit. If $x\in Z$ and $c(Z)=n$, its base point lies` | anchor 1 (D) |
| 517 | `absorbs this polynomial. Consequently the discrepancy` | `absorbs this polynomial. Consequently the series of the indicator corrections $\zeta_f$` | discrepancy 1 (R) |
| 518 | `series has containing-site norm` | `has containing-site norm` | discrepancy 1 (R) |
| 541 | `The path action is the tested and clipped density of \eqref{ch04:path-action}. Its path and cutoff data remain fixed during this replacement, as do the frame choices defining the actual probability kernel` | `The path action is the clipped density of \eqref{ch04:path-action}, restricted by its event indicators. Its path and cutoff data remain fixed during this replacement, as do the choices of local gauge transformations defining the probability kernel` | test 4 (D): event indicator; frame 1 (R); actual 1: delete |
| 543 | `Expand the quadratic part into plaquette channels and ordered` | `Expand the quadratic part into plaquette terms and ordered` | channel 2, plaquette channel (R) |
| 544 | `pairs of entries in each row square. For a channel $d$ let` | `pairs of entries in the square of each component. For a quadratic term $d$ let` | row 1 (R): component; channel 2 (R) |
| 547 | `actual clipped or tested expression.` | `clipped expression, restricted by its event indicators.` | actual 8: contrast named; test 4 (D) |
| 548 | `every plaquette whose relaxed small-field condition is not automatic.` | `every plaquette whose relaxed regularity condition is not automatic.` | table: regularity condition; ch. 4 word |
| 568 | `where $S(0)$ is the row` | `where $S(0)$ is the component` | row 1 (R) |
| 571 | `$\mathcal C$, while the raw channels restricted by their event indicators sum to` | `$\mathcal C$, while the raw quadratic terms restricted by their event indicators sum to` | channel 2 (R) |
| 607 | `Here the site norm sums supremum majorants of logarithmic` | `Here the site norm sums supremum majorants of the large-field` | logarithmic 2 (R) |
| 608 | `terms over supports containing a site.` | `corrections over supports containing a site.` | logarithmic 2 (R) |
| 609 | `The low regular channels contain two curvatures, the high` | `The low regular terms contain two curvatures, the high` | channel 2 (R) |
| 610 | `channels at least three; each derivative costs a polynomial` | `ones at least three; each derivative contributes a polynomial factor` | channel 2 (R); cost 1 (R) |
| 612 | `The actual clipped channel can have size $O(t)$ on a` | `The clipped quadratic term can have size $O(t)$ on a` | actual 8: contrast named; channel 2 (R) |
| 630 | `\section{Absorbing logarithmic corrections into large-field activities}` | `\section{Absorbing large-field corrections into large-field activities}` | logarithmic correction (R) |
| 633 | `Write the logarithmic corrections in` | `Write the large-field corrections in` | logarithmic correction (R) |
| 636 | `Their extra large-field indicator dependence regions are retained.` | `Their extra large-field indicator dependence sets are retained.` | dependence region (D) |
| 637 | `For each finite connected selection $P$ of preliminary` | `For each finite connected family $P$ of preliminary` | selected 4 (R) |
| 638 | `large-field labels and logarithmic labels, require a` | `large-field labels and correction labels, require a` | logarithmic 2 (R) |
| 643 | `of the preliminary prescribed large-field site sets.` | `of the preliminary prescribed large-field sets.` | prescribed set of large-field sites (D) |
| 671 | `In a nonzero term each selected logarithmic label contains` | `In a nonzero term each chosen correction label contains` | selected 4 (R); logarithmic 2 (R) |
| 672 | `a large-field site. Exact coverage assigns that site to a preliminary` | `a large-field site. Exact coverage attributes that site to a preliminary` | assigned (R) |
| 673 | `prescribed large-field site set, so its connected component contains` | `prescribed large-field set, so its connected component contains` | prescribed set of large-field sites (D) |
| 677 | `recovers the old exact cover and the logarithmic selection.` | `recovers the old exact cover and the chosen correction labels.` | selected 4 (R); logarithmic 2 (R) |
| 687 | `connected selections through a fixed site. One additional unit of exponential support decay bounds the number of attachments, since a support has at most` | `connected families through a fixed site. One additional unit of the decay rate of the support weight bounds the number of supports meeting a given support, since a support has at most` | selected 4 (R); support-weight reserve (R); attachment 2 (S) |
| 690 | `The resulting absolute envelope justifies the countable` | `The resulting absolute majorant justifies the countable` | envelope (R) |
| 697 | `majorants small in the attachment norm.` | `majorants small in the site norm.` | attachment 2: the site norm (9:659) |
| 698 | `For the logarithmic terms use` | `For the large-field corrections use` | logarithmic 2 (R) |
| 709 | `for a sufficiently large inverse coupling threshold, provided the` | `for a sufficiently large lower bound on the reference coupling, provided the` | coupling threshold (R) |
| 712 | `the exponent $1/5$ and all polynomial logarithmic costs.` | `the exponent $1/5$ and all polynomial logarithmic factors.` | cost 1 (R) |
| 717 | `The output inverse coupling and scalar are now fixed:` | `The output inverse coupling and the constant per site are now fixed by the coupling constant renormalization and the vacuum energy renormalization:` | table: reset; scalar 1 (D) |
| 738 | `If the matched coefficient has` | `If the coefficient fixed by the matching has` | matched (R) |
| 748 | `There is a second, intrinsic way to identify the reset.` | `There is a second, intrinsic way to identify the coupling constant renormalization $\Delta$.` | table: reset (entry: at 9:748 the correction itself) |
| 756 | `Hold the constructed activities fixed and vary only a trial` | `Hold the constructed activities fixed and vary only a shift` | trial inverse coupling correction (R) |
| 757 | `inverse coupling correction $d$. The scalar discrepancy is` | `$d$ of the inverse coupling, and define` | trial inverse coupling correction (R); discrepancy 2 (R) |
| 770 | `Projection, subtraction and channel replacement are bounded` | `Projection, subtraction and replacement of the quadratic terms are bounded` | channel 2 (R) |
| 774 | `fixed; for a centered Gaussian of precision $\beta A$,` | `fixed; for a zero-mean Gaussian of precision $\beta A$,` | centered 1 (D), as ch. 6 |
| 785 | `Gaussian scores. Apply the common-law estimate to these` | `Gaussian scores. Apply the estimate under the joint law to these` | common law (R) |
| 792 | `discrepancies have sum at most $\varepsilon$.` | `differences have sum at most $\varepsilon$.` | discrepancy 3 (R) |
| 794 | `summable envelope. The strict attachment margin allows` | `summable majorant. The strict margin in the site-norm bound allows` | envelope (R); attachment 2 |
| 796 | `The rooted estimate then gives one summable output envelope;` | `The rooted estimate then gives one summable output majorant;` | envelope (R) |
| 814 | `The scalar formula and projection show continuity of` | `The formula for the constant per site and projection show continuity of` | scalar 1 (D) |
| 835 | `Choose the finest row` | `Choose the finest-scale component` | row 1 (R) |
| 840 | `vertices, $\chi_p^{\rm rel}$ for its row cutoff condition, and` | `vertices, $\chi_p^{\rm rel}$ for the indicator of its relaxed regularity condition, and` | row 1 (R); cutoff 3 (R); ch. 4 word |
| 853 | `$t^2/4$. The relaxed small-field condition implies that the plaquette` | `$t^2/4$. The relaxed regularity condition implies that the plaquette` | table: regularity condition |
| 861 | `where $L_p$ is the actual clipped quadratic channel.` | `where $L_p$ is the clipped quadratic term.` | actual 8: contrast named; channel 2 (R) |
| 862 | `If the relaxed small-field condition inspects a larger neighborhood, its` | `If the relaxed regularity condition inspects a larger neighborhood, its` | table: regularity condition |
| 867 | `as a regular activity, divided into four equal shares anchored at the vertices of $p$` | `as a localized term, divided into four equal shares with base points at the vertices of $p$` | table: localized term; anchor 1 (D) |
| 870 | `differentiation are supplied by Taylor's formula; for` | `differentiation are given by Taylor's formula; for` | supplies (R) |
| 877 | `Assign the nonnegative residual energies to connected` | `Attribute the nonnegative residual energies to connected` | assigned (R) |
| 885 | `where $d_I$ is the sum of assigned residual energies with` | `where $d_I$ is the sum of attributed residual energies with` | assigned (R) |
| 889 | `Every residual term is assigned exactly once; its relaxed small-field condition has` | `Every residual term is attributed exactly once; its relaxed regularity condition has` | assigned (R); table: regularity condition |
| 890 | `The only nonzero exact-cover selection is the actual set` | `The only nonzero exact-cover family is the set` | selected 4 (R); actual 7 (R) |
| 891 | `of these components, so the density identity is exact.` | `of these components of the configuration, so the density identity is exact.` | actual 7 (R): determined by the configuration |
| 900 | `Since $\beta t^2\ge(M_N^{\rm cut})^2/2$, this fits` | `Since $\beta t^2\ge(M_N^{\rm cut})^2/2$, this is at most` | fits (R) |
| 901 | `$\epsilon_N^{\rm lf}$ for a sufficiently large threshold.` | `$\epsilon_N^{\rm lf}$ for a sufficiently large lower bound on the reference coupling.` | threshold 1 (R) |
| 902 | `The activity labels and eligibility criteria are independent of $\beta$.` | `The activity labels and eligibility conditions are independent of $\beta$.` | eligible 2 (D), ch. 4 word |
| 904 | `scalar normalization is zero.` | `normalization constant is zero.` | scalar 1 (D) |
| 912 | `the start of the chapter. Fix an adjacent quadratic pair with the` | `the start of the chapter. Fix the free quadratic forms of two consecutive scales, with the` | adjacent pair 1 (R) |
| 913 | `positive metrics, exact transport identities and actual gauge-covariant block average` | `positive metrics, exact transport identities and gauge-covariant averaging operation` | actual 3; table: averaging operation |
| 913 | `identities and gauge-covariant averaging operation` | `identities and the gauge-covariant averaging operation` | grammar after table word |
| 914 | `of Chapter~\ref{ch05:gaussian}. Let the incoming path have the` | `of Chapter~\ref{ch05:gaussian}. Let the incoming path action have the` | path 2 (R) |
| 918 | `cancellations, large-field eligibility rules and weighted bounds of` | `cancellations, large-field eligibility conditions and weighted bounds of` | eligible 2 (D), ch. 4 word |
| 919 | `with the support reserve used above,` | `with the margin in the decay rate of the support weight used above,` | support-weight reserve (R) |
| 924 | `path realization, clipped frozen source and` | `path realization, clipped frozen inhomogeneous term and` | source 5 (R), as ch. 6 |
| 926 | `Assign anchors as in Proposition~\ref{ch09:family-equivariance}(ii). Construct the outgoing path by the` | `Assign base points as in Proposition~\ref{ch09:family-equivariance}(ii). Construct the outgoing path action by the` | anchor 1 (D); path 2 (R) |
| 928 | `Choose the stage constants, ratio floors, minimum` | `Choose the stage constants, lower bounds on the ratio, minimum` | floor 2 (R) |
| 929 | `auxiliary periods and inverse coupling thresholds in the order` | `auxiliary periods and lower bounds on the reference coupling in the order` | coupling threshold (R) |
| 931 | `Require also that the actual coarse period exceeds the largest` | `Require also that the original coarse period exceeds the largest` | actual 9: original |
| 935 | `the stage-dependent period floor ensures that every localization` | `the stage-dependent lower bound on the period ensures that every localization` | floor 2 (R) |
| 936 | `cube and its dependence neighborhood embeds in the actual torus.` | `cube and its dependence neighborhood embeds in the original torus.` | actual 9: original |
| 947 | `volume, cutoff and curve parameter. The construction` | `volume, ultraviolet cutoff and curve parameter. The construction` | cutoff 1 (R) |
| 948 | `retains restriction compatibility and all exact-cover` | `commutes with restriction of the parameter interval and retains all exact-cover` | restriction compatibility (R) |
| 949 | `cutoff conditions. Output inverse coupling-band membership additionally` | `cutoff conditions. That the output inverse coupling lies in its band additionally` | App. D 9:949-950 (words only) |
| 960 | `normalization refer to the actual block integral.` | `normalization refer to the block integral.` | actual 1: delete |
| 963 | `This is a theorem for one compatible adjacent pair. Its premises` | `This is a theorem for one compatible pair of consecutive scales. Its premises` | adjacent pair 1 (R) |
| 964 | `include the actual quadratic coefficient and fixed path coefficient bounds;` | `include the quadratic coefficient and fixed path coefficient bounds;` | actual 1: delete |
| 966 | `size. The common Gaussian estimate is supplied by the complete` | `size. The joint Gaussian estimate is given by the complete` | common Gaussian (R); supplies (R) |
| 970 | `classical bound contraction and inherited-loop contraction of` | `bounds \eqref{ch07:classical-budget} and \eqref{ch07:inherited} of` | classical bound contraction, inherited-loop contraction (R) |
| 974 | `What remains for a whole trajectory is to make those choices` | `What remains for a whole renormalization-group trajectory is to make those choices` | trajectory 1 (R), as ch. 8 |

### `9f` (09-forest-average.tex)

| line | before | after | decision or entry |
|---|---|---|---|
| 28 | `proved here, namely that the scalar factor does not depend on the` | `proved here, namely that the normalization constant does not depend on the` | scalar 1 (D) |
| 71 | `A family of regular activities $(X_i,o_i,E_i)_{i\in I}$ is` | `A family of localized terms $(X_i,o_i,E_i)_{i\in I}$ is` | table: localized term |
| 88 | `for any family of functions labelled with supports, and with anchors` | `for any family of functions labelled with supports, and with base points` | anchor 1 (D), ch. 4 word |
| 97 | `definition constrains the choice of anchors.` | `definition constrains the choice of base points.` | anchor 1 (D) |
| 98 | `so one anchor per` | `so one base point per` | anchor 1 (D) |
| 100 | `equal shares $f/\|X\|$, one anchored at each` | `equal shares $f/\|X\|$, one with base point at each` | anchor 1 (D) |
| 104 | `\subsubsection*{The scalar factor does not depend on the forest}` | `\subsubsection*{The normalization constant does not depend on the forest}` | scalar 1 (D) |
| 125 | `for the derivative of the block average, which is` | `for the linearization of the averaging operation, which is` | table: averaging operation, its linearization (ch. 5) |
| 133 | `The hypothesis persists when further flat rows` | `The hypothesis persists when further flat components` | row 1 (R), as ch. 6 |
| 207 | `The first expansion of this section was described for one forest.` | `The Mayer expansion of this section was described for one forest.` | table: Mayer expansion |
| 230 | `containing its complete dependence region and a` | `containing its complete dependence set and a` | dependence region (D) |
| 235 | `and a scalar $\mathscr N_F>0$, such that at every` | `and a constant $\mathscr N_F>0$, such that at every` | scalar 1 (D) |
| 244 | `The scalar is` | `The constant is` | scalar 1 (D) |
| 287 | `sets, and path terms which are channels of a path action averaged over` | `sets, and path terms which are terms of a path action averaged over` | channel 2 (R) |
| 298 | `the same way, with anchors mapped by` | `the same way, with base points mapped by` | anchor 1 (D) |
| 303 | `included, with the supports and anchors of` | `included, with the supports and base points of` | anchor 1 (D) |
| 329 | `factor reads a tree only in the blocks which meet its dependence region.` | `factor reads a tree only in the blocks which meet its dependence set.` | dependence region (D) |
| 341 | `the assignment of selections to components` | `the assignment of index triples to components` | selected 1 (D), ch. 6 word |
| 446 | `From here on the first polymer activities are the averaged activities` | `From here on the polymer activities of the Mayer expansion are the averaged activities` | table: Mayer expansion |
| 449 | `sets, majorants and scalar factor.` | `sets, majorants and normalization constant.` | scalar 1 (D) |
| 488 | `\begin{lemma}[Channels of the path action]` | `\begin{lemma}[Terms of the path action]` | channel 2 (R) |
| 491 | `by channels $d$, with supports $Y_d$, anchors $o_d$ and values` | `by $d$, with supports $Y_d$, base points $o_d$ and values` | channel 2 (R); anchor 1 (D) |
| 495 | `and anchor $\varrho'o_d$.` | `and base point $\varrho'o_d$.` | anchor 1 (D) |
| 503 | `channel $d$ by $z$ is a channel $d+z$,` | `term $d$ by $z$ is a term $d+z$,` | channel 2 (R) |
| 512 | `supports and anchors by $\varrho''$.` | `supports and base points by $\varrho''$.` | anchor 1 (D) |
| 518 | `anchor. Translations and $H_4$` | `base point. Translations and $H_4$` | anchor 1 (D) |
| 543 | `the sites of its support. The resulting anchored family is` | `the sites of its support, with base points there. The resulting family is` | anchor 1 (D) |
| 546 | `linear in an incoming regular activity are not divided: such a term` | `linear in an incoming localized term are not divided: such a term` | table: localized term |
| 547 | `keeps the single coarse anchor $y$ for which` | `keeps the single coarse base point $y$ for which` | anchor 1 (D) |
| 548 | `the anchor of the incoming activity, and with these anchors they form` | `the base point of the incoming term, and with these base points they form` | anchor 1 (D); table: localized term |
| 550 | `anchors, form an equivariant family.` | `base points, form an equivariant family.` | anchor 1 (D) |
| 580 | `the share $c_\Gamma/\|X_\Gamma\|$ anchored at` | `the share $c_\Gamma/\|X_\Gamma\|$ with base point` | anchor 1 (D) |
| 581 | `is sent to the share of $\varsigma\cdot\Gamma$ anchored at` | `is sent to the share of $\varsigma\cdot\Gamma$ with base point` | anchor 1 (D) |
| 586 | `incoming regular activity with index $i$,` | `incoming localized term with index $i$,` | table: localized term |
| 587 | `Its incoming anchor is` | `Its incoming base point is` | anchor 1 (D) |
| 590 | `So the coarse anchor of the transported term is` | `So the coarse base point of the transported term is` | anchor 1 (D) |
| 591 | `selected path terms are channels of an averaged path action by` | `selected path terms are terms of an averaged path action by` | channel 2 (R) |
| 592 | `they are permuted with their anchors by` | `they are permuted with their base points by` | anchor 1 (D) |
| 607 | `The anchors in (ii) are those counted in` | `The base points in (ii) are those counted in` | anchor 1 (D) |
| 609 | `counts the $L^4$ fine anchors above one coarse anchor, which is the` | `counts the $L^4$ fine base points above one coarse base point, which is the` | anchor 1 (D) |
| 610 | `anchor kept here.` | `base point kept here.` | anchor 1 (D) |
| 612 | `derivatives from the anchor, and placing a share` | `derivatives from the base point, and placing a share` | anchor 1 (D) |
| 614 | `site, costs at most a polynomial in the diameter of the support.` | `site, contributes at most a polynomial factor in the diameter of the support.` | cost 1 (R) |
| 615 | `this polynomial is absorbed by the support reserve of` | `this polynomial is absorbed by the margin in the decay rate of the support weight in` | support-weight reserve (R) |
| 627 | `with the folding map $q\mapsto x+\pi_{w+i}(q)$,` | `with the reflection map $q\mapsto x+\pi_{w+i}(q)$,` | fold 2 (R), as 9s:175 |
| 660 | `$(\widehat L_x)_x$, anchored at $x$, are` | `$(\widehat L_x)_x$, with base point $x$, are` | anchor 1 (D) |
| 681 | `$G_x$ with the folding map` | `$G_x$ with the reflection map` | fold 2 (R) |
| 682 | `which gives the dependence region.` | `which gives the dependence set.` | dependence region (D) |
| 710 | `folding map, of which it uses only` | `reflection map, of which it uses only` | fold 2 (R) |
| 716 | `dependence region of $\widehat G_x$ extends` | `dependence set of $\widehat G_x$ extends` | dependence region (D) |
| 842 | `Then the regular activities and the large-field activities of the` | `Then the localized terms and the large-field activities of the` | table: localized term |
| 863 | `$\mathfrak G$ permutes the channels` | `$\mathfrak G$ permutes the terms` | channel 2 (R) |
| 864 | `with their supports and anchors, and transports` | `with their supports and base points, and transports` | anchor 1 (D) |
| 865 | `the quadratic expression $a_dP_d$ with its channel. The clover` | `the quadratic expression $a_dP_d$ with its term. The clover` | channel 2 (R) |
| 866 | `substitute of a channel is transported by` | `substitute of a quadratic term is transported by` | channel 2 (R) |
| 871 | `Hence the logarithmic corrections $\ell_a$ of` | `Hence the large-field corrections $\ell_a$ of` | logarithmic correction (R), short term of 9:368 |
| 874 | `A finite connected selection $P$ of preliminary large-field labels and` | `A finite connected family $P$ of preliminary large-field labels and` | selected 4 (R) |
| 875 | `logarithmic labels is mapped by $\varsigma$ to the selection` | `correction labels is mapped by $\varsigma$ to the family` | logarithmic 2 (R); selected 4 (R) |
| 888 | `regular activities of the output are the functions` | `localized terms of the output are the functions` | table: localized term |
| 889 | `and the regular channel terms composing $F$, which` | `and the regular terms composing $F$, which` | channel 2 (R) |
| 896 | `Divided into four equal shares anchored at the` | `Divided into four equal shares with base points at the` | anchor 1 (D) |
| 918 | `replacement and regrouping preserve equivariance.` | `replacement and exact regrouping preserve equivariance.` | table: exact regrouping |
| 927 | `the formula for its scalar factor, and the form` | `the formula for its normalization constant, and the form` | scalar 1 (D) |
| 933 | `defines the dependence region` | `defines the dependence set` | dependence region (D) |
| 960 | `and the absorption, by the support reserve, of the cost of anchoring` | `and the absorption, by the margin in the decay rate of the support weight, of the polynomial factor from placing the base points of` | support-weight reserve (R); cost 1 (R); anchor 1 (D) |

## First-use sentences added

None. The table words used here (step, scale, critical configuration, averaging operation and its linearization, regularity condition / relaxed regularity condition, localized term, base point, large fluctuation-field event, auxiliary index `α`, index triple, sector) have their first-use sentences in chapters 4–6. *Mayer expansion*, *exponentiated cluster expansion*, *coupling constant renormalization* and *vacuum energy renormalization* occur here for the first time in the book (grep over chapters 1–8, `main-theorem.tex`, `reading-guide.tex`: no match), but the table does not say that v3's construction differs from Bałaban's for these objects, so no sentence was added and no citation inserted.

## Short terms introduced

| term | defining sentence | line |
|---|---|---|
| *large-field correction* (for "logarithmic correction", "logarithmic term", "logarithmic label" → "correction label"; the proposal "large-field correction terms in the exponent" is five words) | "Thus $G_x$ is the small-field localized term and $L_x$ is a \emph{large-field correction}, a term of the exponent supported where its enlarged neighborhood contains a large-field site." | 9:367–369; used at 9:432, 607–608, 630 (section title), 633, 638, 671, 677, 698; 9f:871, 875 |
| *auxiliary standard Gaussian coordinates* (for "dummy Gaussian coordinates") | "let $D$ be the dimension after auxiliary standard Gaussian coordinates have been added" | 9:59; "auxiliary Gaussian integral" at 9:72 |
| *margin in the decay rate of the support weight* (for "support reserve", "support-weight reserve", "additional exponential support decay", "unused support exponent"; the wording of chapter 8, 8:150, 330, 362) | no new definition; chapter 8's phrase | 9:148, 267, 282, 438, 687, 919; 9f:615, 960 |
| *quadratic term* `d` of the path action (for "channel", "plaquette channel"; the entry's proposal is "term") | "Expand the quadratic part into plaquette terms and ordered pairs of entries in the square of each component. For a quadratic term $d$ let …" | 9:543–544; used at 571, 609–612, 770, 861; 9f:287, 488 (lemma title "Terms of the path action"), 491, 503, 591, 863–866, 889 |

## Dictionary words applied that are not in the table of word choices

| word replaced | word used | occurrences |
|---|---|---|
| density coordinates (D) | representation data (ch. 4) | 1 (9:6–7) |
| adjacent pair, adjacent quadratic pair (R) | two consecutive scales; the free quadratic forms of two consecutive scales; pair of consecutive scales | 3 (9:15, 912, 963) |
| actual (sense by sense, as the brief requires) | deleted (senses 1, 5: 9:239 → "block integral", 284, 304, 541, 960, 964); "unlike the reference value 𝔟" (4: 9:17); deleted with the band following (4: 9:385); "the gauge-covariant averaging operation" (3: 9:913); "clipped …, restricted by its event indicators" / "clipped quadratic term" (8: 9:547, 612, 861); "of the configuration" (7: 9:890–891); "original" (9: 9:931, 936) | 15 |
| loop correction (R) | `β`-independent quadratic term (as 6:170, 7:237) | 1 (9:26) |
| one-loop drift (R) | one-loop shift of the coupling | 1 (9:42) |
| scalar, scalar bookkeeping, scalar factor, scalar normalization (scalar 1, D) | normalization constant(s); constant; constant per site | 9 (9:56, 399, 717, 814, 904; 9f:28, 104, 235, 244, 449, 927) |
| free tree-gauge bonds (free, R; table) | non-tree bonds | 1 (9:57) |
| dummy Gaussian coordinates / integral (R) | auxiliary standard Gaussian coordinates; auxiliary Gaussian integral | 2 (9:59, 72) |
| measure multiplier (R) | constant factor of the change of variables | 1 (9:63) |
| stationary residual (R) | residual of the mean equation; mean-equation residual | 2 (9:77, 130) |
| sector allocation indicators (App. D) | sector allocation weights | 1 (9:82) |
| (complete, full) dependence region (D; ch. 4, 6 word) | dependence set | 14 (9:82, 88, 91, 93, 107, 477, 500, 636; 9f:230, 329, 682, 716, 933) |
| tag variable, tag coordinates (tag 1, D) | auxiliary index `α`; auxiliary indices | 2 (9:83, 85) |
| halo, dependence halos (R) | neighborhood; dependence sets | 2 (9:84, 278) |
| eligibility criteria / rules (eligible 2, D) | additional conditions; eligibility conditions (ch. 4, 6) | 3 (9:94, 902, 918) |
| one sector Gaussian/Haar law; common law; common-law estimate; joint bound on their common law (R) | joint Gaussian/Haar law of one sector; bound under their joint law; estimate under the joint law | 3 (9:105, 114–115, 785) |
| common Gaussian, common integral (common 2, R) | joint | 3 (9:139, 266, 966) |
| selected large-field condition set / component / condition (selected 1, D) | part of the index triple belonging to `M`; component of the index triple; condition of the index triple (ch. 6 word) | 4 (9:108, 279, 440; 9f:341 "index triples") |
| selected 4, selection(s) (R) | chosen; subfamilies; term; family, families; chosen correction labels | 9 (9:153, 157, 215, 637, 671, 677, 687, 890; 9f:874–875) |
| cutoff-failure label; cutoff failure; failed remote cutoff (D, R; table) | event label; large fluctuation-field event; … far from the index triple | 4 (9:111, 133, 280) |
| quadratic-tilt criterion (R) | hypothesis on tilted Gaussians | 1 (9:115) |
| table heading (App. D 9:124) | factor / integrated majorant | 1 |
| determinant inverse identity (App. D 9:140) | resolvent identity for the determinant | 1 |
| inverse coupling threshold, the threshold, coupling thresholds (R) | lower bound on the reference coupling (ch. 6 wording) | 7 (9:145, 202, 430, 709, 901, 929) |
| ordinary gas, ordinary polymers, elementary ordinary factor (ordinary 1, R) | polymer gas; small-field polymers; elementary small-field factor | 3 (9:150, 153, 172) |
| prescribed large-field site set(s) (D) | prescribed large-field set(s) (ch. 4) | 3 (9:151, 643, 673) |
| envelope (R) | majorant | 4 (9:159, 690, 794, 796) |
| inflated activities (D/R) | rescaled activities (ch. 8) | 1 (9:180) |
| gap 5 (R) | difference of the exponents | 1 (9:190) |
| fits (R) | are bounded by; is at most | 4 (9:201, 378, 426, 900) |
| inverse-ratio sizes (R) | sizes (the powers `L^{-1},L^{-2},L^{-3}` follow on 9:209) | 1 (9:208) |
| weight 1 (D) | scaling dimension (brief 11(d)) | 3 (9:211, 214, 215) |
| inspected support (App. D 9:220) | the support with its adjacent plaquettes | 1 |
| per-label gain (label 6, R) | gain per term | 1 (9:221) |
| incoming support exponent (R); support compression (App. D 9:230–232) | incoming decay rate of the support weight; passing to the coarse image of the support | 2 (9:230, 231) |
| anchor, anchored (anchor 1, D; ch. 4 word) | base point; with base point | 5 lines in `9` (234, 462, 514, 867, 926), 27 lines in `9f` |
| level (R) | scale | 1 (9:262) |
| weights 6 (R) | factors; coefficients | 2 (9:264, 355) |
| losses, costs (loss 2, cost 1, R) | factors; adds; contributes a polynomial factor | 9 (9:265, 267, 434, 437, 438, 510, 610, 712; 9f:614) |
| assigned, assigns, assign (R) | attributed, attributes, attribute | 5 (9:280, 672, 877, 885, 889) |
| seeded / unseeded (App. D 9:283–284, in ch. 6's applied wording 6:1544) | a sector with nonempty index triple and the law with empty index triple | 1 |
| stationary branch (branch 2, R) | critical configuration | 1 (9:292) |
| preparatory output (R) | intermediate representation (section title) | 1 (9:394) |
| matched (R) | fixed by the matching | 2 (9:410, 738) |
| concrete interface (R) | the statement used in the rest of the chapter | 1 (9:442–443) |
| cutoff 2 (R) | cutoff function | 1 (9:476) |
| discrepancy series / scalar discrepancy / input discrepancies (discrepancy 1–3, R) | the series of the indicator corrections `ζ_f`; "define `f(d)`"; differences | 3 (9:517–518, 757, 792) |
| tested (test 4, D) | restricted by its event indicators (the chapter's own phrase, 9:408) | 2 (9:541, 547) |
| frame choices (frame 1, R) | choices of local gauge transformations | 1 (9:541) |
| row (row 1, R) | component (square of each component; component coefficient matrix; finest-scale component; 9f "flat components") | 4 (9:544, 568, 835, 840; 9f:133) |
| channel, plaquette channel (R) | (quadratic) term | see "Short terms" |
| row cutoff condition (row 1; cutoff 3, R) | indicator of its relaxed regularity condition | 1 (9:840) |
| attachment norm, number of attachments, attachment margin (attachment 2) | site norm; number of supports meeting a given support; strict margin in the site-norm bound | 3 (9:687, 697, 794) |
| trial inverse coupling correction (R) | shift `d` of the inverse coupling | 1 (9:756–757) |
| centered Gaussian (centered 1, D) | zero-mean Gaussian (ch. 6) | 1 (9:774) |
| supplied, supplies (R) | given | 2 (9:870, 966) |
| floors (floor 2, R) | lower bounds on the ratio; lower bound on the period | 2 (9:928, 935) |
| cutoff 1 (R) | ultraviolet cutoff | 1 (9:947) |
| restriction compatibility (R) | commutes with restriction of the parameter interval | 1 (9:948) |
| output inverse coupling-band membership (App. D 9:949, words only) | that the output inverse coupling lies in its band | 1 |
| classical bound contraction, inherited-loop contraction (R) | the bounds (ch07:classical-budget) and (ch07:inherited), cited by number | 1 (9:970) |
| trajectory 1 (R) | renormalization-group trajectory (ch. 8) | 1 (9:974) |
| source 5 (R) | inhomogeneous term (ch. 6) | 1 (9:924) |
| path 2 (R) | path action | 3 (9:385, 914, 926) |
| derivative of the block average (9f:125) | linearization of the averaging operation (table; ch. 5) | 1 |
| folding map (fold 2, R) | reflection map (as 9s:175) | 3 (9f:627, 681, 710) |
| regrouping (9f:918, the operation of Proposition 9:651) | exact regrouping | 1 |

Table words applied: step (9:5); scale / consecutive scales (9:15, 262, 912, 963); Mayer expansion (9:44, 89, 148, 173; 9f:207, 446); exponentiated cluster expansion (9:192); coupling constant renormalization and vacuum energy renormalization (9:717, 748); localized term (9:132, 196–197, 206, 257, 261, 265, 367, 383, 867; 9f:71, 546, 548, 586, 842, 888); critical configuration (9:125, 292); large fluctuation-field event (9:133, 280); regularity condition / relaxed regularity condition (9:548, 840, 853, 862, 889); averaging operation (9:913; 9f:125); exact regrouping (9:628, 651 unchanged; 9f:918). American spelling: no British spelling found in either file.

## Not changed, for the author

`9`:
- "selected" in sense 5 (*the low-order terms retained*, R) at 9:312, 313, 314, 383 and throughout `9f` (Assumption (e), Propositions, 24 occurrences): left, because the defining formulas 9:319–320 write `\sum_{a\ {\rm selected}}` in math mode, which the brief forbids touching; replacing the prose word would make text and formula disagree. If the author renames the subscript, "selected" → "retained" can be applied uniformly (and "retaining a weighted tail" at 9:313 should then become "with a weighted tail").
- "shares" (9:234, 315–316, 323, 867; `9f` throughout): the entry (D) proposes "weights", which fits `p_{xa}` but not the functions `f/|X|` that `9f` also calls shares. Left.
- "label(s)" (sense 6, R: "index; term") at 9:385, 638, 671–684, 771, 816, 902, 939 and in `9f`: kept, as chapter 8 keeps "labels" for the polymer and large-field labels on which the proof of the exact regrouping rests (sense 5, "keep"). Only "cutoff-failure label" → "event label" and "per-label" were changed.
- "logarithmic" sense 6 at 9:712 ("polynomial logarithmic factors", I) and sense 3 at 9:247 ("logarithmic density derivative", keep).
- 9:34 "derivative reserves" (*derivative reserve*, I at 9:34).
- 9:35, 502 "normalized affine directions": the proposal "directions of size `t_m`" would fix which threshold (fine or coarse) is meant; not determined at 9:35. Left.
- 9:49 "the exact kernel": the entry *exact* proposes "normalized block-spin kernel", but chapter 4 keeps "exact kernel" (4:169).
- 9:56–57, 9f:312, 930 "reassembly": the entry *exact reassembly* (R) is chapter 8's factorization identity; here the word means reassembling the Haar integral from the local factors. Sense differs; left.
- 9:63, 76–77 "Haar logarithm" (I; kept by ch. 6), "missing-coordinate factor": the Appendix D repair of 9:77 inserts `\mathfrak m^{-(N_{\rm free}-n_{\rm act})}`, a formula not in the line (brief 11(a)); not applied.
- 9:72–73 "inactive Haar variables have been frozen": chapter 6 keeps "active"/"frozen" (6:442–443); left.
- 9:74–75 and passim "forest": kept; `9f` defines it (9f:6–7, 106) and builds on it.
- 9:110, 421, 427, 928, 935 "stage": kept (table).
- 9:113 "primitive factors", 9:112 "bounded-jet estimate": kept as chapter 6 keeps them (6:1025, 1165).
- 9:126 "centered determinant variation" (centered 6, S/I/?): proposal is a formula inside `\text{}`; left.
- 9:127, 141 "Haar remainder", "Haar correction"; 9:128 "inherited quadratic-loop variation": no definite replacement.
- 9:136 "the stationary mean", 9:293 "a finite stationary region", 9:305 "sector and stationary estimates": "stationary" here is not the field `ρ(v)` itself; left.
- 9:147 "Read-count polynomials": the Appendix D repair inserts `(1+s_M)^{d_j}` (not in the line); not applied.
- 9:208 "lifted potential" (*lift* 4): not clear that the potential is `W` applied to a coarse field; left.
- 9:219, 235, 268 "principal" (I, keep); 9:220, 463, 472 "nonwrapping", "wraps" (none proposed); 9:221, 245, 260, 264, 282 "gain" (I).
- 9:240, 257, 773 "physical" (physical 4, I).
- 9:242 "in Gaussian units" (I; *unit* 4: keep).
- 9:279 "clean" (I).
- 9:294–295 "centered auxiliary bound" (centered 6, ?).
- 9:311, 367 "local activities": the generic phrase at 9:311 left.
- 9:314 "ordinary selected term" (ordinary 2, I).
- 9:457, 681, 862, 932 "reads", "read", "inspects", "local read diameter" (I).
- 9:563, 839 "health domains", "health event indicator" (I).
- 9:567 "The selected free metric" (selected 2, I); "metric" kept (ch. 7 keeps it).
- 9:571 "raw" (I).
- 9:573, 837 "atoms" (I).
- 9:593, 802 "exact-cover gas", "exact-cover sums": kept (entry allows "keep, define once"; ch. 4 keeps "exact cover").
- 9:597–605 `C_{\rm reset}` and the label `ch09:reset-cost`: symbols and labels.
- 9:676 "flattening" (I).
- 9:701–702 "strict margin": the inequality is printed, as the entry asks; kept.
- 9:726 "Flat normalization": *flat* is "standard"; kept.
- 9:731, 746, 770, 814 "projection", "local projection" (I).
- 9:752 "The direct positive plaquette term" (*direct*, I).
- 9:764 "the two scalars": which two quantities is not clear (`d` and `Δ`?); left.
- 9:893–894: Appendix D repair B1 inserts `2(r-1)` and `C(1+B)^4`, not in the lines (brief 11(a)); not applied. The damaged sentence stands.
- 9:913 "exact transport identities" (*transport* 2, R): the replacement names the linearization `W`, and the sentence does not say which representative (brief 11(b)); left.
- 9:938 "admissible continuous input curve" (admissible 7, I/S).
- 9:949–951: Appendix D repair applied only as words; its reference `\eqref{ch10:drift-floor}` for "the numerical band margin" was not inserted (the entry's basis at 9:950 is "?").
- 9:964 "fixed path coefficient bounds": *path coefficient* (R) proposes "explicit coupling increment `α`", which is a different object from the coefficients of the path action meant here; left.
- 9:966 "complete factor construction", 9:969 "pure integral" (kept: 9s defines *pure*).
- Section titles 9:163 "Improving the regular remainder", 9:204 "The linear inherited regular term", 9:288 "Low-order terms and localization", 9:818 "Wilson initialization": no replaced house word (the entry *Wilson initialization* says keep); "localization" is chapter 9's operation, not chapter 11's localization operator.

`9f`:
- "selected" (sense 5): see above.
- "gas" (13): kept, as chapter 8 keeps it.
- "reads", "read" (9f:219, 329, 658, 935): basis I.
- "sector data" (9f:212): *sector* kept (ch. 6 defines it).
- "physical torus" (9f:604): physical, I.
- "assignment of index triples to components", "assignment rules" (9f:341, 945): ch. 6 keeps "assignment".
- "the regrouping which leads from the gas to (ch09:early)" (9f:351, 953): this is not the exact regrouping of Proposition 9:651 but the unnamed passage to the preliminary representation; left.
- "coordinate lifts" (9f:758): a different sense of *lift*; left.
- "local windows" (9f:347), "window entry" (9f:934): sense 1, kept.
- The comment line 9f:1 and the labels `ch09:path-channels`, `ch09:channel`, `ch09:fusion`, `ch09:before-fusion`, `ch09:fusion-prop`, `ch09:reset`, `ch09:path-reset` are unchanged.

## Inconsistencies noticed

- *selected* sense 5 against the math-mode subscript `{\rm selected}` (9:319–320): see above.
- *shares* (D) proposes "weights", but `9f` uses "shares" for the functions `f/|X|` as well as for the weights `p_{xa}`.
- *label*: the dictionary files 9:638–684 under sense 6 (index, R), while chapter 8 keeps "labels" for the same polymer and large-field labels (sense 5, "keep"). Chapter 8 was followed.
- *exact reassembly* lists 9:57, but the word there is the reassembly of the Haar integral, not the factorization identity of chapter 8.
- *logarithmic correction* and *logarithmic* 2 propose "large-field correction terms in the exponent"; at 9:432 this gives "the small large-field corrections", grammatical but awkward.
- *relaxed* proposes "exponentially weighted regularity condition"; chapter 4 (4:489) fixed "relaxed regularity condition", which was used.
- *channel* proposes "term"; in this chapter "term" also names the cubic and quartic terms and the regular terms, so "quadratic term" was written where the channel must be distinguished (9:544, 571, 612, 770, 861; 9f:866).
- *exact* proposes "normalized block-spin kernel", chapter 4 keeps "exact kernel".
- *gas* proposes "polymer sum" / "small-field polymer gas"; chapter 8 keeps "gas". At 9:150 "the ordinary gas without large-field sites" became "the polymer gas without large-field sites".
- *seeded sector*: Appendix D's repair ("the law of a nonempty selection and that of the empty selection") and chapter 6's applied wording ("a sector with nonempty index triple … the law with empty index triple", 6:1544) differ; chapter 6 was followed.
- The ch. 9 entry *missing-coordinate factor* and Appendix D's repair of 9:77 both give a formula for a word-only repair.

## Checks

Run after the edits (the last two edits, 9:114 and 9:913, were followed by a second run of all checks):

- `wc -l manuscript/HumanizeYM_v3/chapters/09-renormalization.tex` → 979; `git show HEAD:manuscript/HumanizeYM_v3/chapters/09-renormalization.tex | wc -l` → 979.
- `wc -l manuscript/HumanizeYM_v3/chapters/09-forest-average.tex` → 973; `git show HEAD:… | wc -l` → 973.
- `git diff --numstat`: `09-renormalization.tex` 182/182, `09-forest-average.tex` 65/65. `git status --short` also shows `10-common-trajectory.tex`, which another agent is converting; I did not touch it.
- `python3 tools/check_draft.py` (from `manuscript/HumanizeYM_v3`) → exit 0: "51 files; 679 labels; 1218 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build-c1 monograph.tex` → exit 0; `grep -ci undefined monograph.log` → 0; `grep -c "multiply defined" monograph.log` → 0. The build included the other agent's edits to chapter 10 present in the worktree.
- The whole word diff of both files was reread after the edits; two sentences were then corrected (9:114 "this joint bound under their joint law" → "this bound under their joint law"; 9:913 article "the" added).
- Not done: the rendered PDF pages were not inspected (no `pdftotext` on this machine, and no visual check).
