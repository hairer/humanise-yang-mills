# Audit B: `audit/terminology-surveys/ch10-11.md` and the overview claims for chapters 10–11

> **Status.** Independent check of `ch10-11.md` by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in `../terminology-book-overview.md`, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only audit. All four chapter files were read in full (`10` = `10-common-trajectory.tex`, `11` = `11-marked-insertions.tex`, `11R` = `11-restarted-history.tex`, `11E` = `11-equation-calibration.tex`), plus sections 1, 8, 9 of `terminology-ch03-06.md`, the whole overview, and the passages of chapters 5, 8, 9, 12, 13, 18 cited below. No repository file was edited.

**The worktree changed during the audit.** Commit `ac15effb` ("Repair thirteen sentences broken by mechanical term replacement") landed while I was reading. It rewrote 11:247, 296, 365, 1312, 1595, 1868–1869 and 11R:302; line numbers are preserved. The survey and overview were written against the earlier text. Where this matters I say "pre-repair" or "at HEAD". The commit message names the replaced source words: *inventory*, *unmasked*, *guarded*, *entry-controlled*.

Occurrence counts were re-done with `grep -noiE` after stripping `\label`, `\ref`, `\eqref`, `\input`, `\cite`.

---

## Definite errors

1. **`row` at 10:354 is assigned to the wrong sense.** The survey (section 3) and the overview (2.2) put "actual quadratic rows" under "component of the action vector". The sentence cites Proposition `ch05:horizon-limit`, whose title is "Convergence of the selected Gaussian rows" and which is introduced by "Write a translation-invariant row as $K_{ab}(z)$" (5:711–712); its conclusion is "All limits are for the actual chosen rows on the cover" (5:752). This is the chapter 5 sense, kernel of a translation-invariant operator. 10:356 ("direct row coefficient") is correctly the component sense (5:749 "the fixed direct coefficient $c$").

2. **"Selected component and selected trajectory alternate within single paragraphs" is false.** Survey section 7 item 3 cites "11:1045 vs 11:1933", which are about 900 lines apart; overview 2.3 repeats the claim. Using the survey's own line lists for senses (a) and (b), no blank-line-delimited paragraph in any of the four files contains both. The nearest cases are adjacent paragraphs (11:1933 vs 11:1965) and one proof (11R:89 vs 11R:159).

3. **"the stopping level `k`" is quoted but does not occur.** Survey section 5 lists it, in quotation marks, as a name for the top of the restart interval. `grep "stopping level"` finds nothing in chapters 10–11 (only "stopping pair", "stopping scale", "stopping representation", "stopped at"). The identification is also doubtful: in the restart argument the chessboard normalisation is done at the output level ("At the output $V=q_0$", 11:2019), not at the top level `k`.

4. **`hot` is not a word for the large-field event.** Survey section 5 lists `"hot" (symbol)` among names of the large-field event. `hot(s)` is a function: "$u=a_*\,\mathrm{hot}(s)^2$" (11:1934) against "put $u=a_*h(s)^2$" (11R:114), so `hot(s) = h(s) = e^{(\log\log s)^{3/2}}`. The survey's own section 4 says this; the cluster entry reads meaning off the name.

5. **`mesh threshold` is not a synonym of `delay`.** Survey 1.1 files "mesh threshold" (11:1119, 1815) under "Same thing as delay: requirement `τ_m ≥ b_j log 3`". The text makes it a lower bound on the cutoff `N`: "once the mesh is sufficiently fine relative to the fixed physical cell" (11:1123–1124), "one mesh threshold ensures the required nonwrapping and separation for every period" (11:1129–1131).

6. **`backward comparison / descent` is not "downward induction in the level from N".** The induction on the cone condition runs upward: "The induction starts at the bottom with zero coefficient" (11:909), concluding "$A_{i+1}|x_{i+1}|\le c_{i+1}$" (11:908). "Descent" is the propagation of the terminal trial down the block steps, which gives the decay $e^{-(\tau_N-\tau_i)/8}$ (11:915).

7. **`common localization / extraction`: "two words for one map" merges two maps.** 11:372–377 is the one-step map: "Localization by Taylor expansion of the fine local section … gives a triangular change of basis $T$", leading map $TS_L$. The common localization map is a different `T`, built at the comparison level: "Define $Tu$ to be precisely these frame coefficients" (11:1292–1293), with $\|Au-Tu\|_1\le\tfrac12\|Au\|_1$. 11:1180 and 1203 ("localization by radial Taylor expansion") give `Au`, a third object. The survey's own section 6 lists the two `T`s separately.

8. **`hard` / `soft`: the proposed "small-field corrections" is wrong.** 10:656–666 is an instance of Proposition `ch09:fusion-prop` (9:652–666): hypotheses "$|k_i|\le e^{-\kappa}v_i$, $|e^{\ell_a}-1|\le v_a$", conclusion "$\mathcal K_m(K)\le e^{-\kappa}(e^\gamma-1)$", matching "$e^{-\zeta}(e^I-1)\le\phi$" (10:664). So hard = bound on the preliminary large-field activities; soft = bound on the logarithmic correction factors $e^{\ell_a}-1$. These are not small-field: "with $\ell_a=0$ when $Z_a$ is small-field" (9:634–635).

9. **`ch10:shooting` is listed as jargon "surviving only in labels"** (survey section 4 last paragraph; overview section 7), but the word is in prose: "uniqueness of the shooting parameter" (10:273), "the choices made in shooting" (10:818). The survey's own row 1.1 cites both lines. The same list contains other labels whose words are in prose: `drift-floor`, `equation-floor`, `calibration-floor` ("floor", 10:55, 90), `ch11:mass` (11:423), `ch11:root-bound` (11:817), `ch11:replicated` ("replication costs", 10:172).

---

## Basis codes that overstate or understate

**Overstated**

- **fusion — "D (ch. 9)", "defined in ch. 9".** The word occurs in chapter 9 only inside labels (`ch09:fusion`, `ch09:before-fusion`, `ch09:fusion-prop`). The section is titled "Absorbing logarithmic corrections into large-field activities" and the proposition "Exact regrouping". The stated meaning is right; the basis is I (identified through label names).
- **dictionary — R.** No sentence says what a dictionary is; "coefficients $c_N(\gamma)$ on a common dictionary" (10:375–376) supports "index set" only by inference. R / I.
- **path coefficient `α_{N,m}` — R at the cited lines.** 10:422–423 says only "the one already used in the exact step". The meaning is settled in chapter 9: "The coefficient $\alpha$ is the matched determinant coefficient, not an adjustable trial inverse coupling" (9:409–411), "$\alpha=-\kappa_G\log L+O_j(1)$" (9:739). R, but by chapter 9.
- **complementary part — R.** "One minus the small-field indicator" is not in 11:147–151; it is explicit only at 11:1490–1494 ("factors $1-(1-\chi)Rz_I$"). R / I.

**Understated**

- **mark / marked — I, resting on `notation.md`.** The text gives it: "let $\rho_N\ge0$ be the unmarked density" (11:70) and $q_N=\rho_N\prod(1+z_iF_i)$ (11:75), so unmarked = coefficient of $z_\varnothing$, marked = carrying $z_S$, $S\ne\varnothing$. R.
- **eligible (2.2) — I, "neither dictionary sense is clearly meant".** Settled by 8:286–295: families of large-field labels with disjoint supports and $\bigcup I_\eta=D$; "The exact rules for eligibility are part of the definition of an effective density". The overview section 3 already records this; the survey row does not.
- **cone inequality — I, "presumably".** 11E:125–128 uses "$|e_j-u_j|\le4K_{N-1}L_{N-1}^{-3/8}c_N$", which is 11:905–906 ("If $A_i|x_i|\le c_i$, substitution gives $y_i\le4K_ie_ic_{i+1}$") with $e_i=s_i^{-3}=L_i^{-3/8}$ (11:893). R.
- **residual scalar correction `q_m`.** D is right; add that it is `Δ` of `(ch09:reset)`: "$\beta=\beta'+\alpha+\Delta$" (9:719), bound "$|\Delta|\le C_jH_{\rm pre}/t_m^2$" (9:733), matching "$f_m=C\varepsilon x^{-11/10}/t(x)^2$" (10:648).

---

## Sense misassignments (with my per-sense counts)

Total counts per file agree with the survey for every word below.

**row** (2 / 10 / 4 / 0). Mine: kernel of a translation-invariant operator 1 (10:354; missed sense, see Definite errors 1); component of the action vector 6 (10:356; 11:668, 710; 11R:101, 102, 122); literal matrix row 7; vector in a list 1 (11:2253); undetermined 1 (11R:266).

**actual** (18 / 58 / 15 / 0). The survey's six senses and counts hold to within three. Borderline lines:
- 11R:45 "these actual thresholds" is under (b) running coupling; the thresholds are $\vartheta(x_i)$, functions of the reference coupling. Belongs to (a).
- 11:676 (section title "Actual local coordinate and cutoff estimates") is under (a); the section is the actual-to-flat comparison (11:681). Belongs to (c).
- 11:1216 "the Taylor polynomial of the actual function is unique; it does not require a linear choice of its separate activity representatives" is under (c); the contrast is function against representation, sense (d).
- 11:1325, 1950, 2097 ("actual density", "actual pushed density", "actual source") are under (a) and fit (d) equally.
- My counts: (a) about 54, (b) 16, (c) 10, (d) 3 to 6, (e) 3, (f) 3.
- I agree that the chapter 5 "gauge-covariant block average" sense does not occur.

**selected / selection** (5 / 30 / 12 / 3, excluding "preselection" and counting "unselected" separately). Mine: (a) large-field 25, (b) fixed by the construction 15, (c) ordinary "choose" 10. Four lines the survey puts in (b) are ordinary: 10:892 "A new selection of equally bounded coefficients", 11:219 "before the history thresholds are selected", 11:2084 "before selecting the stage orders", 11E:30 "the selection order". No sense missed.

**test** (1 / 11 / 1 / 0). All 13 assignments confirmed: standard 2, tested correlation 5, tested links 3, evaluate/check 3.

**label / tag** (6 / 27 / 5 / 2). All 40 confirmed: polynomial label 13, insertion label 13, index of a term 8, random index 4, not prose 2.

**mark / marked** (11: 67 hits including 17 "unmarked", so 50; 11R: 6). The survey's four groups sum to 56 and the examples are correctly placed. (a) "mark" and (b) "marked point / site / ancestor" are one sense, noun and adjective, and should be merged.

**window** (3 / 13 / 4 / 0). All 20 confirmed: index neighbourhood 5, interval of levels 12, range of distances 1, compact configuration set 2.

**history** (22 / 14 / 3 / 4 by my count; survey says 23 for chapter 10).
- 11:92 "Changing the block history" is under (b); the proposition replaces kernels only ("Replace any kernels below a fixed level $k$"), so it is (c), the kernel sequence.
- Senses (a) and (b) are close to one sense: chapter 10 already attaches the choices to the trajectory ("Choose one such history for each $N,p$, retaining its path arrays, forests, local integral choices and output representations", 10:256–257). Judgement.

**source** (3 / 36 / 1 / 2). 11:1632 ("Reassigning a principal source term") is in no list. Otherwise confirmed.

**response** (1 / 7 / 0 / 0) and **transport** (2 / 9 / 0 / 0). Lists complete and correctly assigned. That `W` of 11:642 is the chapter 5 transport checks out: $AW=bQ^*$ and $KW=Q^*K'$ with $A=K+bQ^*Q$ give $QW=I-b^{-1}K'$.

**New senses claimed in 2.2.** stage, history, lift, frozen, envelope, mass, target, window confirmed. Missed: `extraction` has a further sense at 11:2037, "The estimates are before extraction", which is not the coefficient-extraction map (compare 11:2214 "a comparison before any cutoff limit"); I could not determine it. `leading` has three uses the survey does not separate: leading-order map ("the leading map is $TS_L$", 11:370–377), the upper interval `k→ℓ` ("leading interval", "leading recurrence", 11:1643, 1952), and the principal coefficients ("corrected leading coefficients", 11:1551, 1886).

**physical.** 11:588 "replace the physical coordinates by $a+\eta_t$" is under (e) "before division by `g`"; those coordinates are the "normalized local curvature coordinates" $\xi_{t,I}$ (11:558–560), contrasted with the Gaussian model.

---

## Wrong line references and misquotations

- raw: 11:901 should be 900 ("the raw inequalities give"); 11:1014 should be 1013.
- presentation: 11R:250 should be 251 ("incoming presentation").
- stationary graph / jets (2.1): 10:336 has "stationary formula"; "jets" is only in the `\eqref` label there. "Stationary jets" is at 10:717.
- inherited (2.1): 10:761 "multiplicities inherited from the input arrays" is the ordinary word.
- occupancy: 11:260 defines `g` but the word is at 11:345 and 10:109 only.
- principal row: "Purely principal connected components … contain neither" alters the text, which reads "since it contains neither an unmarked correction nor an incoming large-field factor" (11:331–332).
- "the stopping level `k`": not in the text (Definite errors 3).
- Overview 2.7: "`J = H₀⁻¹ T H₀`" drops the subscripts; the text has "$J=H_{0,f}^{-1}T H_{0,c}$" (11:647), two different operators.
- Overview 2.10: the history sentence is at 11:18–19, not 17–18.
- All other quotations I checked are verbatim up to line breaks and TeX markup (about 60, including every quotation in sections 1.1, 2.3, 3 and 4).

---

## Omitted terms

House terms in these chapters with no row in the survey:

- **prescribed set of large-field sites / prescribed large-field set** (about 20 uses). Only in the garbled-sentence list and section 7. It is defined: sets $I_\eta\subset D\cap Y_\eta$, "The set $I_\eta$ records the large-field sites assigned to that activity" (8:286–288), with exact cover $\bigcup I_\eta=D$.
- **normalized local insertion** (14 uses, e.g. 11:353, 895, 2191). `notation.md` gives it as the replacement of "primary source"; presumably $O_{N,p}(d,c)$ of 11:1051–1054, which the text calls "the physical insertion".
- **ordinary** as "small-field / regular part": "ordinary remainder" (11:940), "ordinary norm bound" (11E:83), "ordinary contribution" (11E:111), "ordinary chart bound" (10:97).
- **block length / length** for the block ratio `L`: "fixed before the block length" (11E:20), "then the length, then the inverse coupling threshold" (11E:31–32). 11:1873 "Choose the block length after $A_{2D}$" may instead mean the number of steps `m`; not determined.
- **pre-threshold constants** (11:1396), the counterpart of "post-length".
- **energy / suppression** of a large-field component: "whose suppression is $\exp(-c\beta_Nt_N^2 n)$" (11:167–168), "selected-component energy" (11R:63), "energy reserve" (11:521).
- **value** against derivative: "weighted derivative and value norm" (10:391), "terminal value norms" (10:106), "global value" (11:925), "value tails" (10:765). Only "value cost" has a row.
- **bottom**: "common bottom endpoint" (10:850), "bottom residual coefficient" (11:896).
- **fit(s)** in the accounting sense: "its site bound fits $\omega_n$ … The other components fit $\delta_n-\omega_n$" (11R:330–332), "fit inside the remaining margin" (11R:305–306).
- **kill**: "Each conjugate kills $E_i$" (11:970), "killed by $X$" (11:1691). The overview has it; the survey does not.
- Program-style words: **returned** ("the actual returned arrays", 10:777–778; "the returned inverse coupling", 10:785); **reported** ("the reported bound $G(x)$", 11:1597); **declared / declaration** (11:441, 534); **encoded** ("encoded coefficients of a normalized lattice difference", 11:991).
- **coefficient functionals** ("fixed common coefficient functionals", 10:373, 813, 889) and **curl-division and path-placement operations** (10:314): undefined here.
- Smaller: **attenuation** ("polynomial attenuation", 11:1657), **true-length** (11R:102, 133, 274), **consume** ("consume one box factor", 11:1740), **weaken** (11R:275, 279), **discarded-support** (11:1201, 1235), **tolerance exponent** (11:1673), **arity** (11:343, 2041–2047), **exchange term** (10:337; the survey's section 8 says it was looked up but there is no row).

---

## Questionable equivalents

- **moment norm → "norm of the functional on `c_0`".** Wrong space. $\sup_n|\sum_ia_i(t_i/q)^n|$ is the sup norm of the moment sequence, an element of $c_0$ (10:476–477); equivalently the norm of $f\mapsto\sum a_if(t_i)$ on power series with norm $\sum|f_n|q^n$ (the norm $|f|_R$ of 10:535–536). I would write "sup norm of the moment sequence". The duality is standard; the name "moment norm" is the text's.
- **principal → "leading part".** Collides with "leading interval / step / recurrence" (11:1410, 1643, 1952) and "leading map" (11:377). Keep "principal", defined once.
- **stage → "regularity level `j`".** Collides with "level `m`", which the survey's own section 5 proposes for the scale index. The overview's "regularity class" is safer.
- **hard / soft → "large-field factor / small-field corrections".** Changes the mathematics (Definite errors 8). Use "preliminary large-field activity" and "logarithmic correction factor $e^{\ell_a}-1$".
- **backward comparison, descent → "downward induction".** See Definite errors 6. I would use "propagation of the terminal trial down the block steps".
- **corrected coefficients `R_I` → "truncated (connected) coefficients"** (the survey marks this unsure). It would be wrong: $R_I$ is the coefficient of the source polynomial multiplied by the inverse of $\sum_IG_Iz_I$ (11:2096–2098); only its logarithm differs from the connected coefficients by the free ones. Keep "corrected".
- **reset → "redefinition of the coupling".** `(ch09:reset)` fixes the output coupling and the scalar together ("The output inverse coupling and scalar are now fixed", 9:716). "Definition of the output coupling" is closer.
- **moving → "cutoff-dependent".** Right at 11:1083, 2218; at 10:730–731 the expression "would move with the mean or precision".
- **delay → "after increasing the starting scale of the stage".** Fits 11:1192–1200. The terminal delays of 10:107–112 are conditions at the cutoff level `N` ("$\widehat\beta_N\ge a_{d,J(N)}$").
- **Section 5 cluster "large-field event: … tail event".** "Tail events" (11R:43) and "tail-event factors" (11R:284) may be Gaussian tail events of the chapter 6 chart; the merge is an inference.
- Sound, as far as I know the standard usage: "graph transform" for $G\mapsto R_GM_G^{-1}$; "column bound" as the $\ell^1\to\ell^1$ operator norm; "identity insertion" for unit; "modulus of continuity in the insertion point"; "cyclic product of transfer operators"; "majorant" for envelope; "extended by zero"; "index set" for dictionary. I am unsure whether "chessboard seminorm" (as opposed to "chessboard estimate") is established usage.

---

## Overview claims (errors / confirmed)

**Errors**

- 2.2 `row`: 10:354 is in the wrong row (kernel sense).
- 2.3: the "alternate within single paragraphs" sentence is unsupported.
- 2.1 table, chapters 10–11 column: the survey's sense (f), "under the law in force" (11:280, 293, 1613), has no row, so the column sums to 87 against 91 uses. The other entries match the survey (55 / 10 / — / 17 / — / 3 / 2) and my recount to within three.
- 2.7: heading says "ten senses", the table has nine rows; `J` formula misquoted; "response bound" (10:626) is not placed.
- 2.9: the survey's sense "range of distances" (11:1726) is omitted.
- Section 4 lists as undetermined, under other chapter groups, terms that chapters 10–11 or 13 settle:
  - `attachment`: mechanism at 11:147–156 ("Join each complementary stencil to every selected large-field support it meets").
  - `site conversion`: 11:266–272.
  - `weight restoration`: 11:1374–1454.
  - `trial encoding`: the reference label $v_{N,p}$ of 11:945–951 (11:1074–1076).
  - `root estimate`: "Taking the number-of-cells root" (11:817–822).
  - `sparse stopping`: 13sb:102–110.
- Section 7: `ch10:shooting` and several others are not label-only (Definite errors 9).
- Section 6, further broken text in these chapters at HEAD:
  - 11:1636–1637 "retains the original large-field prescribed set of large-field sites" (not repaired by `ac15effb`).
  - 10:922–923 "identifies a / auxiliary graph" (article).
  - 11:938 "has cover at most81;" (missing space).
  - 11:1589 "The ordinary bound for terms involving at least two insertions by one has neither …" (parses with difficulty).
  - 10:98 "the relaxed small-field smooth cutoff is one": `notation.md` line 93 says of the same object "Relaxed small-field test … not a smooth cutoff", and the repair commit names "guarded" as a replaced word, so this is probably the same kind of artefact. Conjecture, not verified.

**Confirmed**

- Section 1 bullet for chapters 10–11: none of `price`, `pay`, `budget`, `receipt`, `readout`, `table`, `probe`, `detector`, `purchase`, `ledger`, `fund`, `share`, `spent`, `excess` occurs in the prose of the four files.
- 2.4, 2.5, 2.6 as far as they cite these chapters; 2.9 lists; 2.10 quotations for history and stage, and `J(m)`; 2.11 "transfer word", "difference word".
- Section 3 rows: regularity-stage index (10:25–31, 129–134), coupling band (10:212, verbatim), width (10:375–381), envelope (11:1581), Warnings (11:319–320 verbatim; correctly "still inferred"; the word occurs only at 6:1476 and 11:319), compulsory (10:654; 11R:161), eligible (8:294–295, verbatim).
- Section 4: `hot(s)` against `h(s)` (11:1934; 11R:114).
- Section 6 reread:
  - 11:247 and 11:1312 were verbatim pre-repair.
  - 11:365, 1595, 1868 and 11R:302 were broken pre-repair as reported.
  - 11:296 parsed, as a noun stack.
  - 11:2133 parses.
  - All except 11:1637 are repaired at HEAD, so the overview's quotations no longer match the files.
- Section 7 labels for chapters 10–11 all exist.

---

## Terms the survey calls undetermined that the text settles

- **sparse stopping scale** (10:172). 13sb:104–109: "Choose $k=k(m)$ as the first level $k\ge m$ with $B_k^2\le a_m/a_k$", then "$(a_m/a_k)^4q_k^{\rm site}\le(L_{k-1}B_{k-1}^2)^4q_k^{\rm site}=o(\tau_k)$", which is the condition imposed at 10:167. Also 18lp:156–160. The word "sparse" itself is still unexplained.
- **Haar-ball normalization argument; replication costs** (10:169–172). 13sb:36–37 "The Haar-ball argument of Section `ch11:replicated`", i.e. 11:795–805; the cost is the factor $e^{(a_m/a_k)^4q_k}$ of 11:819. The survey's guess is right and can be R.
- **"n copies"** (11:781). `n` is the number of reflected cells: the bound $e^{Vq+n(x+y+2)}$ (11:809) becomes $e^{(a_m/a_k)^4q_k+x+y+2}$ on "Taking the number-of-cells root" (11:817–819), which requires $V=n(a_m/a_k)^4$.
- **restoration levels** (11:1405). The middle levels `ℓ`: "the corrected leading coefficients at the middle level … their rooted contribution at the restored weight" (11:1551–1553); "On the lower interval … at the restored weight" (11:1564–1569); 11:1405–1407 contrasts them with "the separated opening sites". Strong inference, not a definition.
- **deletion-of-support identities** (11R:239). Probably `(ch08:deletion-identity)`: "delete all labels whose supports meet $Y$", $Z_{\rm pol}(z^Y)/Z_{\rm pol}(z)=e^{-\mathcal L_Y(z)}$ (8:208–215). Inferred from the name and the reference at 11R:367.
- **regular logarithms with holes; raised hole correction** (11R:365–368). 11R:367 refers to `(ch08:reassembly)`, $Z_D=e^{\mathcal L(z)}\sum_B(\prod K_\eta)e^{-\mathcal L_{Y(B)}(z)}$ (8:311–315). The "hole" would be the deleted set $Y(B)$ and the "raised hole correction" $e^{-\mathcal L_Y}-1$, consistent with "using $|e^{-c}-1|\le e^{|c|}|c|$" (11R:369). Probable reading only; "hole" does not occur in chapter 8.

I agree these remain undetermined: Hilbert encoding, block bridge, response bound `ε` (no "response" anywhere in chapter 9), preselection bound, selected slot, coarse kernel level, front-column, exposure, alphabet, coarse forecast, corrected body product estimate, same-data restart conditions, finite decorations, exterior row (no "exterior" in chapter 6), protected local representative / protected trial (13:229 reuses the phrase without explaining it).

---

## Confirmed rows

Meaning, basis and references as stated, apart from the points above.

- **1.1:** stage; plateau; schedule; floor; delay; request; inner barriers; shooting; tuned; coarse target; comparison level and its family (except restoration levels); comparison window; stopping pair; restart; recording scale; re-expression of the endpoint.
- **1.2:** history (both rows); pad by zero; prescribed-site rules; finite parameter evaluation (meaning); narrow / reserved band; compensation; held fine reads; real nodes; reset (meaning); low-order collection; residual scalar correction; stationary branch; moving expression.
- **1.3:** source algebra; source weight and restoration; insertion label; push; unit; principal (meaning, I); inflation factors; incidence; site bound; occupancy; menu; join / attach; graph `G`; raw; rebasing contraction; column; vanishing-jet remainder; screened; mass; common Gaussian; corrected source; near part; lift; magnification; measurement; trial; terminal map; calibration; admissible; equation subspace; positional modulus; transfer word; difference word; plant; spans; chessboard seminorm; replica cell; envelope; expense.
- **1.4:** all rows except the two settled above.
- **1.5:** counts for cost (10/22/10/0), reserve (19/18/5/2), retain (9/31/18/2), supplies (3/13/1/0), subpower (2/11/1/4) exact; absorb, margin, input within three.
- **2.2:** history, stage, response, transport, mass, lift, window, frozen, target, envelope, weight.
- **2.3:** all rows.
- **Section 4:** all rows except those listed in the previous section. The garbled-sentence list was accurate pre-repair.

---

## Not checked

- Survey section 2.1 was spot-checked (about 25 of 35 rows), not checked row by row.
- Survey section 6 (overloaded symbols): about 30 entries spot-checked, all correct; not audited systematically.
- Per-occurrence classification of `scalar`, `unit`, `endpoint`, `weight`, `cutoff`, `root`, `frame`, `anchor`: totals checked, assignments only sampled. `physical` was checked for senses (a)–(e) only.
- "powered-curvature-factor estimate" (11E:14) was not traced in chapter 2.
- `figures/cutoff-histories` was not read.
- No Lean source and no literature were consulted; the judgements on proposed equivalents are from my own knowledge.
