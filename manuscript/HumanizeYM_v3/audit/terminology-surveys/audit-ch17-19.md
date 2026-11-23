# Audit D: `audit/terminology-surveys/ch17-19.md` (chapters 17–19, main theorem, reading guide)

> **Status.** Independent check of `ch17-19.md` by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in `../terminology-book-overview.md`, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only check against the worktree `manuscript/HumanizeYM_v3/` (HEAD `16317fd1`). No repository file was edited.

**Overall verdict.** The survey's line references and counts are mostly accurate (three or four wrong lines, a few counts off by one or two). Its main weakness is the "undetermined" list: at least twelve terms it calls undetermined or inferred are settled elsewhere under `chapters/`, mostly in chapter 11. It also contains one wrong meaning (`equation calibration floor`), one claimed inconsistency that does not exist (`W`, `W_a`, `W_s`), two merged senses that the text keeps apart (`response`; `ordinary` against `regular`), and a few "terms" that are the survey's own coinages.

Method: I read all ten assigned files in full, blanked `\label`, `\ref`, `\eqref`, `\pageref`, `\input`, `\cite` arguments, and re-ran `grep -n` for every multi-sense word. Cross-chapter claims were checked by reading the cited lines with context. File abbreviations are the survey's; `11`, `11E`, `11R`, `14lc`, `18lp`, `18gq` are the chapter 11, 14 and 18 fragment files.

---

## Definite errors

1. **`equation calibration floor` (§1.1, 19:30): wrong meaning.** The survey says "A lower bound on `β̂_N`". The cited passage is a lower bound on the block ratio `L`: 11E:25–29 "`L^{1/8} ≥ max_{d≤j} 2(1+C_j)Q_{dj}δ_d^{-1}`" (label `ch11:calibration-floor`) "in the stage-`j` block floor". The `β̂_N` condition at 11E:30 is a separate "adjacent stage condition on the starting scale". The proposed equivalent should be "the lower bound on the block ratio in (11.calibration-floor)".

2. **`W` / `W_a` / `W_s` "inconsistency" (§1.2 row "stationary tangent", §6, §7 item 1): there is none in the chapters.**
   - 5:1084 defines `W_s` as "the straight-average transport"; 5:1108 defines `W_a=W_s-d_{0,f}ERW_s`.
   - 5:1151 "The smooth representative `W_a` and the forest representative `W_F` are distinct"; 7:574 "The actual stationary tangent is `W_a` … its forest representative is `W_F`".
   - So 17c:112 ("may be replaced by the smooth representative `W_a`") and 17m:263 ("The actual tangent is `W_a=W_s−d_fERW_s`") agree: `W_a` is the actual tangent in its smooth representative.
   - `notation.md`:242 agrees with 17m:263; the survey's "says the opposite again" is wrong. Only its word "forest-coordinate" conflicts with 5:1151.

3. **`ordinary` and `regular` are not synonyms (§5 cluster "small-field part", §7 item 7; copied into overview §5).** 17m:106–115: "`Z_ord=𝒞 exp[−βS−𝓛−E_reg]`" and "The regular term is estimated using its already proved differentiated regular norm". `ordinary` is the whole small-field part; `regular` is one term of it, the remainder `E_reg`. Replacing both by "small-field" changes 17m:114 and 17w:78.

4. **`response`, first sense (§3.11): two different operators merged.** 17w:11, 60, 67, 68 concern the curvature response `Ψ_i` (17w:62 displays `Ψ_{n-1}⋯Ψ_ℓ`; 11:647 "`J=H_{0,f}^{-1}TH_{0,c}` is the curvature response"; 11:1729 "the actual installed curvature response `Ψ_i`"). 17m:193, 202 and 19:159 concern the link tangent `W` (11:642 "the actual stationary forest response `W`"). These need separate rows.

5. **Survey coinages listed as house terms.** These phrases do not occur in the text:
   - "component average `K_a`" and "difference primitive `K_a^t`" (§1.2). The text has "finite Laurent polynomial `K_a^t`" (17t:34); "difference-primitive" (17c:309) refers to `q_a`, `t_abc`.
   - "trace stability amplification `e_i`" and "stable functional" (§1.2). The second is only the label `ch17:stable-functional`; "amplification" occurs at 17w:78–79 for the product (17.window-product).

6. **`replicate`, "ch11:780".** That line is `\label{ch11:replicated}`. The verb does not occur in chapter 11 prose (it does at 13ba:283). The supporting text is 11:815–817 "A reflected tiling at scale `a_m`, stopped at `a_k` … Taking the number-of-cells root".

7. **§6, `τ`: "`τ_m=log D_m` (17m:423)".** 17m:423 reads "`τ_{k(n)}−τ_n ≥ T_n`"; there is no `log D_m`. `τ` is defined at 10:145–146: "`τ_{m+1}=τ_m+log L_m`, `a_m=e^{−τ_m}`". This also settles what "crosses" in "first crossing" (see below).

---

## Basis codes that overstate or understate

**Overstated (given D or R, really I or weaker).**
- `level`, `k_i` (R): `k_i=k(n_i)` is never written. 17:85–87 only names "insertion level `k_i`"; the identification rests on 17:108, 139–142 and 17m:386, 420.
- `request` (R): no sentence defines it; the meaning is read from usage. I.
- `field order` (D, "17c:222"): that line defines `e_r`, not the term. R.
- `exterior` / `interior` (R): 18r:9–11 uses "interior lattice difference", "exterior factors", "interior seminorms" undefined; 18lp:154, 207, 238 use them, also undefined. I.
- `resolution heights` (R "via that file", "defined in 18lp:223–341"): the phrase occurs only at 18r:54–55 and nowhere in 18lp. That two of `θ_−<θ<θ_+` are meant is an inference. Since `Z_0=Wθ_++4n_cl(θ_+−θ)` (18r:32) must tend to `W`, the two are `θ` and `θ_+`, not `θ_−`.
- `anchor average`, "mass" (D/R) is fine; the two invented names in the same row are not (see error 5).

**Understated (given I or ?, the text settles it).** See the section "Terms the survey calls undetermined that the text settles". In brief: `history`, `conserved line`, `ordered tails`, `replicate`, `physical inclusions`, `spectator responses`, `vacuum bound q_n`, `root estimate`, `weight restoration`, `top polynomial extraction`, `strip removal`, `derivative-transport argument`, `centered … tensors`, `admissible periods`, `restarted representation`, `exceptional vacua`.

---

## Sense misassignments (with my per-sense counts)

**`actual` — 41 (grep agrees).**
| Sense | Mine | Survey |
|---|---|---|
| of this construction | 23–24 | 25 |
| the tangent `W_a` / gauge-covariant block average | 7 | 6 |
| true object against an idealised or substituted one | 4–5 | 4 |
| emphatic | 4 | 4 |
| running coupling | 2 | 2 |
- 17t:157 "the actual stationary pullback of the current defect, with the gauge-covariant block average frame correction" belongs with the tangent sense (it is contrasted with "the usual smooth transport bound", 17t:161), not "of this construction".
- 17w:68 "product of the subsequent actual responses. It uses no replacement by a common stage's quadratic form" is true-against-substituted; borderline.
- No missed sense. Counts are right to within two.

**`row` — 10 (agrees).** The split into "kernel of an operator" (6) and "literal matrix row" (4) should be merged. Every use is a row of a matrix or kernel at a fixed output index:
- `Ψ` row sums: 17w:12 (11:1735 "`sup_x Σ_y|Q_{i,w}(x,y)| ≤ R L_i^{−|w|−2}`", the `R_{J_i}` of 17w:63).
- `M_{ef}`: 17c:336, 349, 367. `R_0`: 17c:280. `W_s`: 17m:237, 245, 249, 260. The 3×3 recursion matrix: 17c:237.
- "Kernel of a translation-invariant operator" (overview §2.2) is wrong for 17m:237: "`A_x^{ab}(z)` … from coarse direction `b` at `⌊x/L⌋+z` to fine direction `a` at `x`" depends on `x`.

**`selected` / `selection` / `selects` — 19 (agrees); all six sense assignments confirmed.** `chosen` — 18 (agrees). "All ordinary" contradicts the survey's own table: 17:15 "the phase `ξ_*` chosen in Section…" is the phase sense.

**`test` — 16 (agrees): 12 test function, 4 pairing.** Confirmed.

**`label` — 15 in prose, not 14** (the survey's own lists sum to 15). Missed sense: at 17:97 and 17:370 "moving (free) labels" are elements of the free Maxwell spaces `𝓜_d^Max`. 17:81 "`U_{i,d}:𝓜_d^Max→F_d`"; 17:320 "`β_i r_i^4U_{i,4}^{-1}Θ → −κ_G𝒪`". So three senses: polynomial label (7; 19:29 is uncertain), field entry of a word (6), free Maxwell field (2).

**`tag` — 0.** Confirmed.

**`mark` / `marked` / `marker` — 32 in prose plus the file name at 17:311 (agrees with 33).** The "new use" (the inserted factor is `𝒟_Yk`, not an observable) is not confined to 17t:145 and 17m:120–122. It covers most of 17m: 72 "an admissible marked conditional integral. Its extra factor is a finite sum of smooth local kernel scores", and 81, 84, 150, 176, 381, 393, 411. Judgement on where to draw the line, not an error.

**`window` — 18 in prose plus two file names (agrees with 20).**
| Sense | Mine | Survey |
|---|---|---|
| interval of radii | 4: 17:129, 131, 146; 17w:6 | 6 |
| range of scales | 11–12: 17w:2, (7), 37, 43, 49, 54, 55, 56, 102, 107, 124; 17m:429 | 10 |
| compact set of separated configurations | 1: 17:140 | 0 (called undetermined) |
| length of an average | 1: 17m:476 | 1 |
- 17w:2 "Comparison windows crossing changes of stage" is assigned to radii, while the same phrase at 17w:124 is assigned to scales. Both are scales.
- 17w:7 "requiring every window to lie inside a plateau" is ambiguous (a plateau is a set of scales).
- 17:140 "Diagonalize finite degree, arity, window and derivative requests" parallels 14:225–226 "explicitly diagonalizing arity, degree, compact windows and errors". This is the chapter 14 sense, which the survey says is absent from these chapters.

**`history` — 9 (agrees).** The sense is right, but "none of the files defines it" overlooks 11:18–19: "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations". 17w:103 and 19:49 are the restarted history of 11:736–741.

**`source` — 21 (agrees).** Five senses confirmed, with one unsupported assignment: 17w:12 "polynomial-source propagation constants" and 17w:78 "regular and large-field source recurrences" are put under "source variables / weights of ch. 11". Neither phrase occurs anywhere else in `chapters/`; they should be listed as undetermined. That leaves 2 (18:125; 17m:440) in that sense.

**`response` — 13 (agrees).** See error 4. My split: `W` 3; curvature response `Ψ_i` 4; nonlinear stationary field 1 (17m:278); quadratic coefficient of `Γ_μ` 2; "anchored vector response" 1 (I); correlation with spectators 2. The last (18:182; RG:18) is the "one-slot response" defined at 13:120–122, not a new sense.

**`transport` — 13, not 12.** RG:17 "transporting all coefficients together" is in §1.4 but missing from §3.12. 17:128 "derivative-transport argument" is not undetermined (see below). 17w:68 "each conditional covariance is transported by the product of the subsequent actual responses" is conjugation by linear maps; assigning it to "RG transfer" is a stretch.

**`transfer` — 15 in prose, not 17.** The survey's list has 15; a sixteenth hit, 17c:2, is a TeX comment.

**`probe` — 22 (agrees).** 17m:251 "fixed probe order" is probably not a third sense. Context: 17m:240 "every vector polynomial `p` of degree less than `j`", 17m:252 "tuples of potential polynomials". This matches chapter 3 (3:939 "the scalar order-`j` probes"). Inference, not settled.

**Other counts.** `stage` 23, `phase` 46, `word` 12, `anchor` 20, `supplies` 16, `raw` 7, `physical` 11, `regular` 11, `ordinary` 13 all agree. `mixed` is 11, not 12. `leg` is 15, not 16. `coupling threshold` is 19, not 17 (two occurrences are split across lines: 17m:142–143, 346–347).

---

## Wrong line references and misquotations

- `leg`, "17c:373": the line reads "gauge is legitimate for this covariant displacement". Substring artefact.
- `gain`, "17c:375": the line reads "frame derivatives again occur only below the field-order diagonal". Substring artefact. 18:256 "residual gain `(ρ/R)^{D+1}`" is missing from the list.
- `shooting`, "ch10:210": that line is `\label{ch10:shooting}`. The word is in prose at 10:273 and 10:818; the section title (10:209) is "Tuning a finite history to the coarse endpoint".
- `replicate`, "ch11:780": a label line (error 6).
- `stopping levels`, "17w:101": the words are on 17w:102.
- Overview §2.11, probe "(18:36–38 ✓)": the definition is at 18:38–39; 18:36 is a label.
- No misquotation found. Every quotation I checked is verbatim up to marked ellipses and TeX markup (about 40 checked, including all those in §§1.1–1.4, 2.3, 3.1–3.6).

---

## Omitted terms

House terms in these files that the survey does not list:

- **`graph`**: 18:124 "the one-insertion graph contraction" (cf. 11:347 "The one-insertion graph estimates", 11:911 "the graph of normalized local insertions"). 17m:444 "descending graph" is listed, but "graph" is not glossed.
- **`Diagonalize … requests`** (17:139): "take a diagonal subsequence over", an unusual use; also "diagonal radius selection" (17m:446).
- **`empty coefficient` / `empty density` / `denominator`**: 17w:88 "the empty coefficient, and hence the denominator, is unchanged"; 17m:418 "Every spectator subset uses the same empty density". This is the coefficient of the empty source monomial, i.e. the density without insertions (11:604, 773, 2101).
- **`squarefree polynomial`** (17w:86): polynomial in the nilpotent source variables (11:23 "squarefree source algebra").
- **`cross-modes`** (17m:401 "all pushed spectator cross-modes"): coined; `notation.md` has "higher modes".
- **`microscopic sections`** (19:28); cf. 11E:36 "normalized microscopic section".
- **`correlation-null fields`** (18:40) and **`field-null spaces`** (19:68).
- **`endpoint constants` / `endpoint factors`** (17w:23, 26); only "endpoint error" is listed.
- **`bottom stage`, `middle` and `output` stopping levels, `top` extraction** (17w:97–102): positional words for the comparison window. "Bottom stage" may use `stage` for a level, which would be the only such use in these files (I could not determine this).
- **`division`**: "analytic division argument" (17c:99), "homotopy divisions" (17c:102), "Coordinatewise Taylor division" (17c:104), "Two-leg curl division" (17c:346).
- **`box-filter identity`** (17c:365; 11:1731).
- **`units` of the support exponent**: "Retaining two units of the exponential support exponent" (17m:332, 413).
- **`admissible` (path) action** (17t:84; 17c:12): only "admissible periods" and "admissible marked conditional integral" are listed.
- **`attach`** (17m:125 "Attach this condition to its actual dependence support").
- **`tail`** as a multi-sense word: for all large indices ("fixed-stage tail" 17c:135; "ordered tails" 19:38) against the far part of a kernel ("exponential row tail" 17m:260; "crop tail" 17m:313).
- **`compression`** (18:19–20; 18r:14, 36; 19:98): standard operator theory, but used as a noun for an element; borderline.
- **`twelve-plane coefficient convention`** (17t:120; 17:236).

---

## Questionable equivalents

- **`ordinary`, `regular` → "small-field"**: changes the meaning (error 3). Keep "small-field part" for `ordinary`; for `regular` say "the remainder `E_reg`" or "small-field remainder".
- **`primitive` → "discrete potential"**: I do not know "discrete potential" as a standard term for `q` with `tr J=Σ_aδ_aq_a`. "Primitive" (antiderivative for the forward difference) is closer to standard; better to state the identity.
- **`current defect` → "conservation error of the lattice current"**: `𝓔_b=Σ_a∇_aJ_{ab}−D𝖲[Y_b]` (17:195) is the failure of the Ward identity, i.e. conservation up to the equation-of-motion term. "Defect of the lattice Ward identity" is safer.
- **`field reconstruction H_d(w)` → "projection of the cluster onto `F_d`"**: a cluster word is not an element of a space containing `F_d`. More exact: "the field in `F_d` with the same values of the functionals `b_α`, `|α|≤d`".
- **`contact identity` → "chart identity for `div_Haar Y`"**: not standard either; keep the proposition number.
- **`exceptional vacua` → "further invariant vectors"**: loses the measure-theoretic point (see below). Use "non-uniqueness of the vacuum on the `ν`-null set of phases".
- **`mixed ground space` → "space of invariant vectors of the mixed theory"**: the text's own phrase is "zero-energy subspace of its reflection Hilbert space" (15:7); use that.
- **`row` → "kernel"**: in chapter 17 "row" is a literal matrix row; "row of the kernel" or "for fixed output index" is right, "kernel" alone is not.
- **`replicate` → "apply the chessboard estimate at the scale…"**: acceptable given 11:815–822, but that text should be cited.
- **`stage` → "parameter regime `j`"**: not standard; "stage `j`" defined once is better (the survey's first option).
- Fine as proposed, to my knowledge standard: "inhomogeneous term", "annihilate", "vertices", "truncation to a ball", "downward induction", "arguments" for slots, "identity" for unit. I did not check any of these against the literature.

---

## Overview claims (errors / confirmed)

**Errors or inconsistencies.**
- **§2.1 table, column ch. 17–19.** The numbers 25 / 4 / 6 / 2 / 4 sum to 41 and reproduce the survey. But the "4" is entered in the row "nonlinear / at the non-flat background, against flat or linearised", whereas the survey's four lines (17m:276, 284, 294, 409) are "true object versus an idealised model". 17m:409 "an actual exponentially local spectator" has nothing to do with nonlinearity. The row label does not fit.
- **§2.2**, "kernel of a translation-invariant operator … 17w:12; 17c:280; 17m:237–260": not translation-invariant (see `row` above).
- **§2.7**, row "stationary fine field / the map `W` … 17w, 17m; 19:159": the 17w uses are the curvature response `Ψ_i` and belong in the next row (11:647, 1729). Row "correlation with other fields … 18:182; RG:18" duplicates the row "one-slot response … (defined 13:120)". 17:224 "anchored vector response" is missing. The heading says ten senses; the table has nine rows.
- **§2.3**: 17m:446, 19:38 and 19:112 (subsequence choice) and 17t:419, 454 (picked out by a formula) are not represented.
- **§2.4**: 18r:36 is missing from the pairing row.
- **§2.9**: 17:140 belongs in the row "compact set of separated configurations".
- **§2.11**: line reference 18:36–38 should be 18:38–39.
- **§4, chapters 17–19.** Of the seven named terms, five are settled in other chapters: `strip removal`, `derivative-transport argument`, `weight restoration`, `root estimate`, `exceptional vacua`. The overview's own §2.8 cites 14:229 for "conjugation by comparison maps", which is the derivative-transport proposition. `fixed probe order` and `unit endpoints` remain open.
- **§5**, "small-field part: ordinary, regular, small-field": not synonyms (error 3).
- **§6**: no cited line lies in my files. Further sentences in my files that look damaged by replacement or do not parse:
  - 17m:303 "There are no invariant constant spacetime-vector or terms linear in the `𝔤`-valued field." (a noun is missing).
  - 17t:159–160 "the order-two pullback must annihilate its affine--affine and affine--quadratic polynomial moment conditions" (one annihilates moments, not conditions).
  - 17c:359–360 "Only a bounded number of coarse output edges are within the gauge-covariant block average and averaging patches".
  - 17t:157–158 "with the gauge-covariant block average frame correction"; 17c:161 "all mixed gauge-covariant block average and frame terms included" (noun piles after replacement).
  - 19:152–154 "Positivity at contacts, contact Ward identities, the fact that inserting the identity leaves correlations unchanged, and uniqueness of contact terms require…" (18:430 still has "unit removal" in the same list).
  - 17m:284–285 "the difference … are bounded"; 17w:76 "an coupling-threshold-controlled"; 17m:144 "let `f` be curvature-factor count".

**Confirmed.**
- §1: chapters 17–19 reuse `window`, `source`, `probe`, `response`, `transport`; front matter uses `phase` without "character" (MT:32–35) and "admissible periods" without definition (MT:14, 19).
- §1: none of `price`, `pay`, `purchase`, `budget`, `receipt`, `ledger`, `fund`, `readout`, `detector`, `share`, `spent`, `excess` occurs in the prose of my ten files.
- §2.3: the phase row (17:15, 31, 351; 19:117; MT:91, 93) and the pair-weight row (18:297, 352, 358).
- §2.5: polynomial labels in MT, RG, ch. 19; 18:140–222 "probably" fields.
- §2.6: `marker` 18:123 / 18:124; the inserted factor in 17m is a differentiated block kernel; "the source" at 18:411 and RG:82 (supported by `notation.md`:206 "the unverified sharper source forest prescription" and 14:186 "the source construction uses").
- §2.9: rows for 17w, 17m:429, 17m:476.
- §3: 17w:14 for `J(m)`; 17m:283 for `envelope`; 17c:301 for `matching`.
- §4: `v_eom` occurs only at 17m:385–386 and is never introduced.
- §7: `ch17:current-suppliers` (17t:4), `ch18:raw-replacement` (18r:3), `ch19:conditional` (19:57).

---

## Terms the survey calls undetermined that the text settles

| Term (survey place) | Settled by | Meaning |
|---|---|---|
| `history` (§3.5, I) | 11:18–19 | "one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations" |
| `restarted representation`, `B_n` (§1.1, ?) | 11:736–741; 11R:18 | History with the inverse coupling held constant below a comparison level; "The new representation at level `i` has radius `B_i=b(x_i)^2`" |
| `root estimate` (§3.14, §4) | 11:817–822; 11:2072–2079 | "Taking the number-of-cells root … `𝓡_m` denotes that chessboard seminorm"; the bound is (11.n-mark-root) "`‖R_I‖_root ≤ H^{−1/(16n)}`", with "cell side … at most `a_kH^{b_j+5}`", matching 17w:96 |
| `weight restoration`, `regular-restoration bounds` (§4) | 11:1374–1375, 1436, 1471, 2131 | Named lemmas "Regular weight restoration" and "Large-field weight restoration": passage to the larger source weight; "Regular weight restoration therefore gives `H^{-1}`" |
| `top polynomial extraction T` (§4) | 11:1142 ff.; 11:2085–2088 | "Construct `T` at the top level `k` from the actual insertion and its original same-insertion covariance"; "top" is the top level of the comparison window |
| `vacuum bound q_n`, `positive-density estimate` (§1.2, §4) | 11:801–812, 819 | `q` is the per-site exponent in the lower bound for the partition function ("positivity gives `Z ≥ …`"); `(a_m/a_k)^4q_k` in (11.root-bound) is the `L_*^4B_n^8q_n` of 17m:436 |
| `replicate` (§1.1, I) | 11:815–817 | Take a reflected tiling at scale `a_m` |
| `strip removal`, `strip width`, `scaled mesh`, `grid errors` (§3.14, §4) | 14:174–200 | "coordinate-equality strips of width `4δ_k`", `δ_k=M_k^c`; grid spacing `s_k=M_k^{−α_0}`; `ε_k` on the grid; the strips "have volume `O(δ_k)`" |
| `derivative-transport argument` (§3.12, §4) | 14:229–238 | Proposition "Derivative transport and smooth comparison": `r_kU_{k,d+1}^{-1}∂_aU_{k,d} → ∂_a^0` |
| `centered … tensors` at 17:163 (§3.14) | 3:580–584; 14:261–264 | "Centered means that each component has zero expectation"; the same sense as the other uses |
| `conserved line` (§1.2, I) | 3:591–596 | Proposition "Conserved tensor line": `{J∈𝒯_{≤4}: div J=0}=ℝT^Max` |
| `ordered tails` (§1.4, I) | 13:213–214 | "the filter is generated by ordered tails: `p=P(k)` with `k≥k_0`, and `N=n(j)` with `j≥j_0(k)`" |
| `admissible periods` (§1.4, ? in MT) | 10:193–197 | `R_p=4(M+p+1)`, `p≥0`, with `M` large enough for the first plateau |
| `exceptional vacua` (§1.4, I, "no other occurrence") | 16:379–381; 15:324–328 | "the zero-energy space is a line for almost every phase … To remove the exceptional set requires a bound uniform in `ξ`". "Exceptional" refers to the null set of phases, not to a kind of vector |
| `physical inclusions` (§1.3, I) | 14:210–212 | "`i_d` … for the free inclusion, `j_d` for the physical inclusion": physical means interacting, against free |
| `spectator responses` (§3.11, I) | 13:120–122 | "one-slot response `L_{v,f}(c)=∫f(x_0,x)S_{n+1}(c(x_0),v(x))`" |
| "what crosses" in `first crossing` (§1.1) | 10:145–146; 17m:422–425, 433 | `τ_m=log(1/a_m)`; "`τ_{k(n)}−τ_n ≥ T_n` is the first crossing"; "`B_n^2 ≤ a_m/a_n ≤ L_*B_n^2`" |
| `window … requests` at 17:140 (§3.4) | 14:225–226 | "diagonalizing arity, degree, compact windows and errors": strongly indicated, not explicit |
| "the kernel identities" at 17:308 (§3.14, §4) | 17m:10–66, 396–398 | "The next section proves them using the kernel identities": the next section is 17m, on the block kernel `k`. Likely, not explicit |

Partly settled: `corrected free-subset polynomial` (11:2064–2071: free moments `G_I`, corrected coefficients `R_I`); `eligibility condition` (8:294–295 and 9:94 use it without stating the rule); `finite incidence costs` ("incidence" bounds at 11:208–342).

Still undetermined, as the survey says: `v_eom`; `actual free history`; `protected-path errors`; `fixed-ratio jet errors`; `with these same frames`; `unit endpoints`; `normalized large-field majorants`; `finite momentum approximation`; `E_stat`, `E_tail`, `E_mark`; `polynomial-source propagation constants`; `source recurrences`; why "contact" in "contact identity".

---

## Confirmed rows

Meaning, line references and basis as stated (apart from the points above):

- **§1.1**: stage; plateau; level (except `k_i`); radius window; stop backwards / overshoot; pre-ratio / post-ratio / fixed-ratio; coupling threshold; schedule; floor (17t:107); shooting (meaning); current depth; restart (pointer).
- **§1.2**: current defect (definition); "order at least four"; low moments (both senses); stationary substitution; stationary tangent (meaning); anchor average `K_0` and mass; primitive `q_a`, `t_abc` (meaning); displacement; leg; channel; diagonal / below the diagonal; source / forcing; completed; covariant completion; infinitesimal gauge insertion and background insertions; regulated current / regulator; contact identity; chart velocity; action-gradient terms; Haar coefficient and coefficient functionals; trace functional and raw divergence; equation direction; same-family; density identity; density-valued insertion; complementary; ordinary; threshold coordinates; crop; jet menu; coefficient evaluation; reserve; cost / gain / loss; trial descent.
- **§1.3**: probe; field reconstruction (definition); measurement; mixed table; cluster; clearance; replacement and `Z_D`; signed; same-history; nilpotent marker; source weights; raw; moving field; normalized-null lemma; uniform in the number of copies; derivative descent; subtraction convention; slots; contact projection / shell; source prescription; unit removal.
- **§1.4**: phase; polynomial labels; penalty parameter; normalizations; correlation responses; transporting; positive action cost; slab; hierarchy; nickname pointers 19:47–52, 89–105; low-energy estimate; finite-list senses; rate-sensitive cancellation / squeeze; source locations.
- **§2.2**: amplitude, mass, and the list of new senses (subject to the §3 corrections).
- **§2.3**: all nine rows.
- **§4**: the rows listed above as still undetermined.
- **§5**: the three symbol rows (`M_n`/`H_n`/`H`; `w_0`/`W`; `spare`) and the `kill` list.

---

## Not checked

- **§6 (overloaded symbols)**: only the `W` row and the `τ` entry were checked (both wrong); the other rows were not.
- **§2.1 (same-sense list)**: spot-checked by count and by about half the cited lines; no errors found, not exhaustive.
- **§5**: checked only for meaning-changing merges and for the rows with line references.
- **Figures** (`figures/radius-windows.tex`, `figures/pair-subtraction.tex`): not read.
- **Other chapters**: read only at the cited passages, a few lines each. `18-lattice-products.tex` and `18-graded-quotient.tex` were searched, not read in full.
- **`blueprint/notation.md`**: only the lines the survey quotes; all were found as quoted.
- **Literature**: no proposed equivalent was checked against it; my judgements on what is standard are from my own knowledge.
- **Overview**: only statements citing my ten files.
- **One mathematical point noticed, not pursued**: 17m:438 has "`B_n=O((log β̂_n)^2)`", whereas 11R:15–18 gives `B_i=b(x_i)^2` with `b(x)=⌈(log x)^2⌉`. I could not determine whether these are the same `B`.
