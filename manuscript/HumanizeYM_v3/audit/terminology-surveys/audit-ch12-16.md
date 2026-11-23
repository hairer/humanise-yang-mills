# Independent audit of `audit/terminology-surveys/ch12-16.md` (survey C)

> **Status.** Independent check of `ch12-16.md` by a fresh agent (Claude Fable 5.2 subagent) that did not write the survey, reproduced as returned. Where this audit and the survey disagree, the audit was verified against the text at the points listed in `../terminology-book-overview.md`, section 9; elsewhere it is one more agent reading, not a mathematician's review.


Read-only audit; no repository file was edited. All eleven chapter files (3869 lines) were read in full, then every row of the survey's sections 1, 2.2, 2.3 and 4 was checked against the cited lines, and the multi-sense words were re-classified from `grep -n` output with `\label/\ref/\eqref/\input/\cite` arguments stripped. Abbreviations are the survey's (`12`, `13`, `13sb`, `13ba`, `18gq`, `18lp`, `14`, `14lc`, `15`, `15sp`, `16`); other chapters are cited as `1:`, `2:`, `9:`, `10:`, `11:`, `11R:`.

**The worktree changed during the audit.** HEAD moved to `ac15effb` ("Repair thirteen sentences broken by mechanical term replacement"). In my files it rewrote 14:832, 18lp:43 and 18lp:136; line numbers are preserved. Quotations of those three lines in the survey and overview were verbatim before that commit and no longer match the text.

Overall: the survey is mostly reliable on line references and quotations (I found no misquotation inside my chapters). Its weak points are (i) several terms declared undetermined or inferred that other chapters define, (ii) four wrong or shifted meanings (`terminal graph`, `normalized local insertion`, `probe`, `stopping` in 13sb), (iii) three occurrence counts that are off by much more than "a few" (`spectator`, `source`, `physical`), and (iv) a handful of proposed equivalents that collide with existing or standard usage.

---

## 1. Definite errors

1. **`terminal graph` "is at the intermediate level m+h, not at N" (§2.2, basis R, cited 12:131, 139).** Not supported. The word "terminal" occurs only in the title 12:131 ("Forgetting the terminal graph"); 12:139 says "Replace the selected graph at $m+h$ by one fixed admissible graph" and does not contain the word. Every other "terminal" in these files means "at the cutoff N": 13ba:123 "its terminal source satisfies the joint attachment bound at $N$"; 13:217 "inverse terminal coordinates"; 11:895 "the terminal trial". The natural reading is that the dependence on the graph at the cutoff level is what is forgotten; the replacement at m+h is the proof device. The R code is an inference, and probably a wrong one.

2. **`normalized local insertion` = "the source multiplied by ω_k" (§1.1, basis R).** Wrong object. ω_k is the *weight* attached to the insertion: 18lp:243 "The weights of normalized local insertions in \eqref{ch13:weight-size}". The normalized local insertion is the canonical insertion of a label, which is subtracted from a trial: 11:895 "Subtract one normalized local insertion density from the terminal trial, choosing its reference coefficient"; 13ba:119 "the negative normalized local insertion used in the subtraction". notation.md:158 agrees ("primary source | Normalized local insertion, with its local polynomial coefficient"). 13sb:65 ("multiplication of the complete source by $\omega_k$") describes the weighting, not the definition.

3. **`spectator` "49×" (§2.1).** The count is 33 (13: 10, 18gq: 2, 18lp: 3, 14: 15, 14lc: 1, 16: 2).

4. **`source` "≈60" with sense (a) "≈38" (§3).** The count is 49. Senses (b)–(e) are 7 + 4 + 6 + 1 as stated, so sense (a) is 31, not ≈38 (12: 14, 13sb: 3, 13ba: 9, 18lp: 3, 14lc: 2).

5. **`physical` "(37)" (§3).** The count is 31; the survey's own sub-counts (≈17 + 7 + 7 + 1) also give 32, not 37. Sense (i) is 16.

6. **`test`, 14:207 assigned to "pair with all spectators / exterior words" (§3 (b)).** 14:207 is "Testing against each fixed $f$ separately would be weaker" where f is a test function (14:203–204). It is integration against a test function. The overview repeats the misassignment (§2.4).

7. **`macro-box radius` listed as occurring at 13ba:229–248 (§2.1).** The word "macro" does not occur in any of the eleven files. The text is "each endpoint frame reads a box of fine-lattice radius $(j_i+3)L_i$" (13ba:244–245).

8. **`the source construction` (§1.1, §4): "the parameters there are M_k while 14lc uses H_k".** This is not a mismatch. M_k is the generic sequence of 14:171 ("let $M_k\to\infty$, $r_k\to0$"), and 14lc instantiates it as H_k term by term: 14:187 "$r_k=a_kM_k^{\alpha_0}$, $s_k=M_k^{-\alpha_0}$" against 14lc:26 "$r_k=a_kH_k^{\alpha_0},\qquad s_k=H_k^{-\alpha_0}$"; 14:188–189 against 14lc:85–86. So the phrase refers to the construction given in 14lc (or to its counterpart in the formal source). Which of the two is still not stated.

9. **`admissible`: "undefined: remainder graph 12:37".** 12:37–38 "any fixed admissible remainder graph" is the admissible graph defined at 12:82, used 45 lines early. It is a forward reference, not an undefined term.

10. **`row` "(7)".** There are 8 occurrences, and the survey's own sub-counts add to 8.

---

## 2. Basis codes that overstate or understate

**Overstated (R or D for what is inferred)**

- `terminal graph` (§2.2): R → I at best; see 1.1.
- `normalized local insertion`: R → wrong; see 1.2.
- `graph` (§1.1): "A linear map" is given under D, but 12:82 does not say "linear". Linearity comes from 11:379 "Let $G$ be an incoming linear graph". D for the bound `‖Gx‖ ≤ s_m‖x‖_1`; "linear" is R from chapter 11.
- `probe` (§2.2, R): see section 3 below; the stated meaning is not what 18lp:332 shows.
- `separated` (§1.2, R, cited 14:17–18): the cited lines do not contain the word ("evaluated at distinct points or against test functions supported away from collisions").
- `subpower` (§2.3): "13:159, 217 use 'subpower in a_N^{-1}'". Those lines say only "subpower inverse terminal coordinates"; "in $a_h^{-1}$" is at 13ba:18 and 11:1101.

**Understated (I, ? or "not defined" for what the text settles)**

- `section` (§1.1, "no", I): defined at 2:138–146, "A local polynomial section is a complex-linear map $P_d^{\mathrm{loc}}:V_d\longrightarrow$ {polynomial functions of finitely many link entries …}" and "The term section simply means a right inverse of the Taylor map". 11:15 recalls it and 13ba:217 uses the symbol. D (ch. 2).
- `history` (§2.3, I): defined at 11:18–19, "A history means one fixed choice of these kernels, inverse couplings, adjacent path pairs, and local representations." The survey's gloss ("the sequence of renormalisation steps started at a given cutoff") is close but is not the definition.
- `separated` test function (§1.2, "no"): defined at 1:359, "A separated test function is an element of $C_c^\infty(\Conf_n)$, extended by zero".
- `complementary profile` (13ba:165, I): 13ba:16 gives the sense explicitly, "its complete bound, including the complementary large-field part". R.
- `bounded rows` (13:159, I): 11:2253 "The rows $(I-\Pi_i)u_{j,i}$ are bounded, hence admissible." R (ch. 11).
- `centered` sense (iv), 18lp:224 (I): 1:217 "Odd block ratios give centered blocks". R (ch. 1).
- `marker amplitude` = source weight (14lc:61, I): notation.md:216 "R_I, G_I, omega | Corrected subset source, free subset moment, and source amplitude". Supported, though only by the blueprint.
- The §4 terms listed in section 8 below.

---

## 3. Sense misassignments, with my per-sense counts

Counts are mine, from stripped `grep -o -i`.

**actual (20; survey 20, correct).** (a) of this construction 14, (b) produced against substituted 2, (c) belonging to cutoff N 2, (d) true function against the model Q 2. I agree with the assignment. Borderline, judgement only:
- 18lp:229 "on the actual histories" sits in (c) by analogy with 13ba:32; it reads equally as (a).
- 12:118 "actual inserted density" contrasts with "only … the regular part" (complete against partial).
- 13:162 and 14lc:53 contrast the interacting object with the free one.

The dictionary senses "nonlinear" and "running coupling" do not occur, as the survey says.

**row (8; survey "7").** 12:55 displacement-indexed quadratic path coefficient 1; literal matrix row 3 (13:168, 182; 14:277); 13:159 1; 15:275 (two), 278 3. Two merges are suggested:
- 15:275–278 "reference rows" are the rows of the matrix of correlation pairings of 15:288–289, so survey senses (d) and (b) are one sense.
- 13:159 is the usage of 11:2253 (rows of a finite list of coefficient vectors), which the overview files separately as "vector in a finite list".

**selected / select / selection (23; survey 22 + "Selecting", correct).** (a) 11, (b) 3, (c) 3, (d) 2, (e) 3, plus 15:301. Assignment accepted, with two doubts:
- 13:395 "all refer to the same selected family" is put under "continuum family". The items listed there are lattice estimates, and parallel passages say "the same lattice family" (15:250–251; title of 14lc:2). It could be sense (a).
- 13ba:30 "selected level-$h$ polynomial coordinates" is most simply "on the selected history" (sense (a)), since J_h is a map along that history (13ba:274–276).

**test (47; survey ≈47, correct).** Mine: test function 30, paired with spectators or words 7, "tested" as smeared or evaluated 10. Two moves:
- 14:207 goes from (b) to (c); see 1.6.
- 16:215 "the tested function and all its derivatives decay exponentially" is the test function itself (the argument of the distribution), so it belongs in (a), not (c).

The chapter 4–6 senses do not occur.

**label (59; survey ≈60, correct); tag 0.** (a) ≈30, (b) ≈26, (c) 3, (d) 1 accepted. Not decidable from the text: 13:282–285 (labels of a "word", stated after the quotient is defined), 18lp:295, 14lc:7, 13sb:176. The claim that notation.md requires (a) and (b) to be kept apart is correct (notation.md:150 "distinguish from quotient field").

**mark / marked / marker (53; survey 53, correct).** 34 / 12 / 3 / 2 symbols / 2 "unmarked". No misassignment.

**window (6), history (7).** Correct, one sense each. For `history` see section 2.

**source (49; survey "≈60").** Variable 31, inserted observable 7, weight 4, "source attachment / constants / corrected-source" 6, 14:186 1. The assignment of lines is accepted; only the totals are wrong. In sense (d), "corrected-source estimate" (14lc:45) is not undetermined: 14lc:49–54 defines the corrected coefficients R_I and says "These are precisely the coefficients of the actual squarefree source polynomial divided by the free moment polynomial".

**response (25; correct).** One-slot 15, spectral 8, flux 2. The "spectral" sense holds two different objects:
- a function of E, the Laplace transform of a profile: 14:465, 531, 688, 697, 740, 761 (6);
- the number obtained by evaluating a functional on a product of profiles: 14:654 "the transverse responses of $Q_0,Q_1,Q_2$", 14:672 (2), and the displayed `Resp_i(g)` at 14:503.

**transport (14; correct).** RG transfer 8, comparison maps 5, "carries over" 1. In the second group 14:281–282 ("Center the componentwise map $U_{k,4}$ after transport … its inverse transports back") is application of U_{k,d} to a field array, not conjugation. "Conjugation" fits only 14:229, 302, 946.

**Words given a "new sense" in §2.2**

- `probe` (6): one sense, but not the survey's. The survey reads it as "finite linear combination of separated correlations used as a coordinate functional". 18lp:332 has "using fixed cells for exterior probes and shrinking cells only for cluster factors", and 14:354 "chosen by fixed probes before the exterior spectator". Probes occupy cells, so they are the fixed exterior insertions (words) whose correlations realise the coordinates. That is the sense the overview reports from 18:36–38 ("a fixed word v …").
- `stopping` (11 with "stopped"; survey 10): two senses merged.
  - Chapter 12: stop at level m *and* delete the terms of source degree ≥ 2 (12:207–216).
  - 13sb:85, 102, 137; 13ba:193; 18lp:159: the level k at which the transfer is halted and the normalized chessboard bound applied, with nothing deleted. 13sb:9–11: "We keep all incoming joint marked components; replacing them … would invalidate the estimate."
- `request` (12): three uses merged.
  - A finite tuple of data (14:224–227; 14lc:9, 79, 108).
  - A requirement placed on the schedule (13ba:100 "countably many finite degree requests to the single schedule of coupling thresholds"; 18lp:103, 151).
  - A prescribed lower bound on a level (13:96; 13ba:336; 15:207).
- `cutoff`: the survey lists three senses and omits the most frequent one in chapters 14–16, a smooth cutoff function (≈17 uses: 13ba:36, 165; 14:252, 324, 328, 347, 396, 614, 620, 625, 736; 16:205, 232, 235, 283, 459, 539). 14:324 "independent of the cutoff" is the function χ, not N.
- `cost`, 18lp:85 ("The incidence norm has a second cost") is filed under "error term". It is a combinatorial factor, "at most $(1+\mathfrak N)n$ assignments per representative" (18lp:88).
- `anchor`, `lift`, `representative`, `charge`, `centered`, `word`: accepted. "Center … centers" as verbs at 14:281, 283 belong to the zero-expectation sense and are not listed.

**Multi-sense words the survey does not treat as such**

- `scalar`: besides the constant term of the exponent, "strictly ordered scalar heights" (16:218) and "positive scalar imaginary gaps" (16:248) mean purely time-directed imaginary parts; also "scalar operators" (16:481) and "the two scalar corrections" (14:283–284).
- `gap`: time separation (14:731 "a genuine temporal gap", 15:76), difference of heights (16, 15×), spectral (15:340; 16:383).
- `corrected`: with free moments subtracted (14lc:45; 15:17, 253, 258) against "corrected projection / inclusions" (18gq:8, 110, 114).
- `signed`: signed coordinate permutations and reflections (14:26; 14lc:8; 13ba:60 "signed symmetry orbit") against "with its sign kept" (18lp:24 "Signed local transport", 18lp:65) against 13sb:35 "Signed regular costs".

---

## 4. Wrong line references and misquotations

No misquotation found in my chapters (subject to the `ac15effb` note above).

Lines that do not contain the cited term:
- 12:139 for "terminal" (§2.2).
- 14:17–18 for "separated" (§1.2).
- 14:354 for "exterior word" (the text is "exterior spectator", continuing on 355).
- 13ba:229–248 for "macro-box" (absent from all files).
- 13:159, 217 for "subpower in a_N^{-1}".

Cross-chapter references off by a few lines (outside my files):
- "11:808 'absolute action cost per site'" is at 11:789.
- "11:1094" for the equation space is 11:1089–1093.
- "11:258" for the incidence sum is 11:257.

Missed occurrence: `subpower` also at 13:235.

---

## 5. Omitted terms

House usages in my files with no entry in the survey:

- **origins** ("physical origins", "insertion origins": 12:22, 208, 230, 239, 279). Position of an insertion; a synonym of `anchor` that the synonym table does not list.
- **background convergence / background limits** (12:31, 41, 175). R at 12:31–34: Cauchy convergence of β, the path coefficients and the activity arrays.
- **normalized null condition / estimate / representative argument** (13:192, 215, 240; 18gq:9, 108). D by formula at 13:198–203.
- **microscopic** (18gq:10, 76, 84, 94, 97–98) = at the cutoff level N.
- **unit** ("the distinguished unit" 13:58; "the unit" 14:220, 283, 408, 974; "unit vacuum" 14:34, 15:25) = identity field.
- **grid** (14:177–200; 14lc:29, 75; 18lp:225, 300, 327–342; 15:178, 207; 13ba:305–336): "grid word", "grid error", "grid restriction", "grid target", alongside "lattice".
- **target** ("derivative target" 13:252, 260; "grid target" 18lp:341; "target exponent" 18lp:344).
- **raw** ("raw representatives" 13sb:173; "raw coordinate", "raw replacement error" 18lp:318, 324–325; "total raw angular response" 14:777).
- **ordinary** = small-field ("ordinary norm bound", "ordinary chart", "ordinary derivative constant", 13ba:15, 37).
- **signed**, **corrected**, **scalar** (ch. 16), **gap**: see section 3.
- **replacement** ("local replacement", "replacement field" 14:353; titles 18lp:4, 220, 282) and **reconstruction** $\mathcal P_D$ (18lp:266–279, "finite correlation reconstruction maps").
- **collision orders** (14:519, 579, 611); **Ward sum** (14:812, 841, 901, 917); **vector-map space**, **defect space** (14:817, 820, 937).
- **endpoint estimate / endpoint comparison** (13ba:18, 34); **fine end** (18lp:46, 63).
- **vacuum normalization bound**, **vacuum denominator** (12:247, 286): "vacuum" for the insertion-free lattice integral.
- **exceptional phases** (15:325–340; 16:380).
- **positional** ("positional modulus" 14lc:92; "positional derivatives" 14:813–814, 841; 18lp:296).
- **reference label / coefficient / insertion / rows** (18gq:12, 85, 106; 13ba:200, 275; 15:278).
- **transitions** between stages (13sb:49; 13ba:81); **degree ceiling** (13ba:56).
- Forward uses not noted: "slab" at 13:335, 391 before its definition at 14:86; "phase" at 13:393, 13ba:5, 304, 18lp:7, 14:351, 371 before 15:8; "mixed" at 18lp:8 (input into chapter 13) and 14:12 before 15:5.

---

## 6. Questionable equivalents

- **stopping → "truncated correlation `C_{N,p,m}`".** Misleading. "Truncated correlation function" is, to my knowledge, the standard name for connected (Ursell) functions in this literature. It is also wrong for 13sb/13ba/18lp, where nothing is deleted. I would write "correlation with the terms of source degree ≥ 2 deleted at level m" for chapter 12 and "the level k(m) at which the bound is applied" for 13sb.
- **graph → "remainder map".** Collides with the text's own "unreparametrized remainder map" J_G (12:91) and "raw remainder map $R_G$" (11:381). I would write "the linear map G from coefficients to remainders".
- **unmarked gas → "partition function without insertions".** Changes the meaning. The gas is a function of the configuration U (12:180–183 "a finite polynomial in the latter profiles and fixed eligibility indicators"); the partition function is its integral (12:173).
- **heat semigroup → "(Osterwalder–Schrader) transfer semigroup".** I do not know "transfer semigroup" as a standard term ("transfer matrix" is the discrete-time lattice object). "The contraction semigroup $e^{-tH}$ of time translations" is safe. The remark "nothing to do with a heat equation" is a judgement; I am unsure how unusual "heat semigroup" for $e^{-tH}$ is.
- **profile → "one-variable multiplier".** "Multiplier" suggests a Fourier multiplier operator. I would write "one-variable factor of the product test function in momentum space".
- **moment → "correlation".** Acceptable at 12:293, 14lc:47, 14:898. Wrong at 15:213 "compressed product moments": these are $\langle\Omega,M(w_1)\cdots M(w_k)\Omega\rangle$, and 15:123 says "Compression is not multiplication of finite-separation words", so they are not correlations of a word.
- **remainder with vanishing extracted coefficient → "term with vanishing Taylor polynomial of degree t".** Fits only the regular part (18lp:38). The large-field part has no Taylor characterisation there (18lp:39–40 "the large-field term retains half the suppression").
- **low plane → "subspace of dimension < i".** Ambiguous between linear and scaling dimension. Write "span of the basis polynomials of scaling dimension below i".
- **recentering → "renormalisation of the remainder".** The survey flags it as unsure; I agree it should not be used. 18lp:40–43 is the subtraction of the output coefficient.
- **ancestor cone → "domain of dependence".** Usable, but the cone also contains the auxiliary random variables (13ba:232–233), and the dictionary already has "dependence region". Judgement.
- **`ker H` → "zero-energy subspace; vacuum"** (§5). "Vacuum" must not replace "ground space" in chapter 15: 15:47–48 "it does not say that this space is one dimensional".
- **cell → "tile"**, **buffer → "margin"**: neither is an improvement. "Cell" is ordinary in chessboard estimates, and "margin" already names a different length (3a_k at 13:88). Judgement.
- **mixed measures → "polarised measures"**: I am not sure "polarised" is standard; "the complex measures $\nu^{AB}$ obtained by polarization" is.

Accepted as standard: iterated limit; argument (slot); n-point (arity); coincident coordinates; with pairwise distinct coordinates in every direction; imaginary parts; coefficient vector / coefficient map (the text itself says "coefficient map" at 12:90).

---

## 7. Overview claims concerning these chapters

**Errors**

- **§2.1 `actual`, column "ch. 12–16": 14 and 4.** These sum to 18 of 20. The two uses "the true function against the model solution Q" (14:868, 869) appear in no row. They fit the first row, which should then read 16.
- **§2.2 `row`: 12:55 placed under "component of the stacked vector whose half-square is the action".** At 12:53–55 the object is indexed by a displacement and summed over $x\in\ZZ^4$ ("The canonical indices enumerate displacement vectors … For a row their length is $|x|_1+4$"). That is the kernel sense (cf. 10:354 "quadratic rows"). Judgement, but the survey itself wrote "kernel/component sense, I".
- **§2.2 `row`: "bounded coefficient family 13:159" and "vector in a finite list 11:2253" as separate senses.** 13:159 restates 11:2253; they are one sense.
- **§2.4 `test`: 14:207 under "paired with all spectators or words".** It is a test function; see 1.6.
- **§2.6: "In 14:186, 18:411 and RG:82 'the source' is the formalisation the book was written from."** Stated as fact. It is clear for RG:82 ("source locations") and probable for 18:411 ("the source prescription and its proposed sharper local-order bound"; notation.md:206). For 14:186 the survey itself marks "?", and the parameters quoted there are those of 14lc (see 1.8). Should read "probably".
- **§2.7: heading "ten senses"; the table has nine rows.**
- **§2.11 `probe`: the 18lp:268 sense ("a finite combination of separated correlations") listed apart from the 18:36 sense ("a fixed word v").** 18lp:332 and 14:354 indicate one sense; see section 3.
- **§4, chapters 12–16.** Of the seven listed terms, three are settled elsewhere (`trial encoding`, `site conversion`, `corrected inclusions`) and `attachment` is largely settled; see section 8. `sparse stopping` can be inferred. Only `coordinate hybrids` and `protected trial` stay open.
- **§6 broken sentences.**
  - 18lp:43 and 18lp:136 were broken as quoted and are repaired in `ac15effb`.
  - 18lp:185 ("Each term is assigned the union of its supports and original prescribed set of large-field sites") and 13sb:63 ("its counterpart constrained to cover the prescribed large-field sites, as well as the source attachment bound") parse. They are awkward, not broken, and the repair commit left them alone.
  - Further candidates in my files: 18lp:27 "a remainder with vanishing extracted coefficient of norm $r_l$" and 18lp:36 "… of size $q$" (the norm or size belongs to the remainder, not the coefficient); 16:380 "by \ref{ch15:ae-ground}", a bare `\ref` where `\eqref` is meant.
  - 14:832 "justify" (survey §7) is fixed in `ac15effb`.

**Confirmed**

- §1: the description of chapters 12–16; no accounting words `price, pay, purchase, budget, receipt, ledger, fund` in prose (grep: 0).
- §2.3: 13:172, 15:257 as "continuum family along the chosen subsequence" (13:395 doubtful, section 3).
- §2.5: the label split and the notation.md requirement.
- §2.6: "marked" at 12:200–206.
- §2.7: the three chapter 13–14 rows.
- §2.8: 14:229–302, 946 (with the nuance on 14:281–282).
- §2.9: 14:173–237; 14lc:6.
- §2.10: 10:25 and 10:129–134 quotations (verified); 11:17–18 definition of history (verified at 11:18–19).
- §2.11: phase at 15:6–10 and 16:15; word at 13:282 and 16:291.
- §3: `subpower` at 18lp:18 agrees with 6:822; regularity stage at 10:25–29, 129–134.
- §5: the chessboard-seminorm notations (13:74, 13:302, 13sb:79, 13ba:24, 14lc:64).
- §7: all labels named from chapters 12–16 and 18 exist.

---

## 8. Terms the survey calls undetermined that the text settles

- **trial encoding** (13:394; §4). 11:943–951: "a reference label $v_{N,p}$ with inverse terminal coordinates bounded by $2E_{N,p}$ and $\mathcal R_m\{F-O_{N,p}(e,v_{N,p})\}\le\ldots$"; 11:1074 "now supplies the trial encoding with subpower inverse terminal coordinates and a vanishing chessboard-seminorm error". The encoding of a trial F is that reference label.
- **site conversion; support conversion cost `T_l`** (13ba:145; 18lp:112–113).
  - 9:513 "The conversion of anchored bounds to containing-site bounds is explicit."
  - 11R:141–142 "the extra unit used to turn an anchored bound into a site bound. These are the support conversions".
  - 11:267 and 11:1918 "Root-to-site conversion costs only $\mathcal W(B)$".
  - $T_e$ is defined by formula at 11:233–237 (`ch11:cover-transfer`).
- **admissible period cell** (12:375). 1:359–361: a separated test function "is admissible at volume $p$ if its support is contained in $((-R_p/2,R_p/2)^4)^n$".
- **equation remainder; corrected projection; corrected (physical) inclusions** (18gq:8, 110, 114).
  - 18gq:108–110 applies the argument of 13:198–205; there the "corrected projection" is $\Pi_ux_u$ and the remainder is $(x_u-\Pi_ux_u)/(1+\|\Pi_ux_u\|)$, of which 13:220 says "Their difference lies in the exact finite equation kernel."
  - The inclusions are $\iota_{d,e}$ of 13:263–264.
  - "Corrected relative to what" *is* said: 18gq:94–95 "it is not the naive inclusion of unnormalized polynomials" (cf. 13:117–118).
- **attachment** (11 uses). Not defined in one sentence, but usage elsewhere fixes it as the joining of an insertion stencil or a complementary (large-field) part to an existing support in the polymer expansion, and the sum over the places where this can happen.
  - 9:687 "One additional unit of exponential support decay bounds the number of attachments, since a support has at most $(2B+1)^4c(Z)$ sites."
  - 11:924–925 "Attach the latter to the original selected large-field factors".
  - 11:937 "$u_N>0$ the terminal attachment reserve"; 11:941 "the complementary attachment".
  - So the "attachment bound" $u_i$ of 13ba:62, 77 is that reserve. Basis I rather than ?.
- **"Open the centered cells at m"** (13ba:127). Chapter 11 uses "opening" for the starting level of an estimate: 11:1889 "already present at the opening level"; 11:1919 "At the opening all distinct sites … are separated". By that usage, 13ba:127 means "start with the centered cells at level m". I, not ?.
- **sparse stopping** (18lp:159). 10:167–172 imposes the last condition of `ch13:sharp-schedule` and says "It will keep replication costs subpower at a nearby sparse stopping scale"; 13sb:85–86 has the anchors at the stopping level with "spacing at least $B_k^2$". "Sparse" = widely spaced anchors at that level. I.
- **common** (§4, cited 12:13, 40, 370). The cited lines are "common trajectory / construction"; 10:4–9 says what is common ("a single sequence of scales and a consistent choice of coefficient arrays … compare theories with different ultraviolet cutoffs"). "One common lattice" is at 12:230, 296, 299 and is clear in place: one of the nested lattices containing all the points (12:352).
- **corrected-source estimate** (§3 `source` (d)): 14lc:46–55; see section 3.

Remain open after my search of `chapters/`:
- `coordinate hybrids` (14lc:95; no other occurrence of "hybrid").
- `admissible comparison depth` (14lc:23; 11:884 defines an admissible comparison *coefficient*, not a depth).
- `protected trial` (13:229; 11:2306 uses it without definition).
- Whether "the source construction" (14:186) names the formal source.
- Why a linear map is called a "graph".

---

## 9. Confirmed rows (meaning, basis and lines as stated)

- **§1.1:** fixed-input continuity; I_G / J_G; forgetting (the R gloss, apart from "terminal"); dictionary; inventory; large-field profile; complete; terms linear in the sources / modes; source weights; column; inverse terminal coordinates; admissible coefficient family (quotation verified at 11:1101–1102); trial; equation space; incidence; rooted; reserve; block floors (10:55 verified); first-below scale; comparison depth; lift; ancestor cone; frame seed; group / merger / live; recentering (meaning only); low plane; cell census; inspected.
- **§1.2:** ordered limits / tails; slot; arity (17); cell / centered; buffer; exterior word; slab; heat (meaning); damping; coordinate spectral measures; profile (meaning); annular correction; conserved stress line; line axis; shell factor; Ward kernel / normalization / spin operators (all I, as stated); phase (including the notation.md warning, verified at notation.md:169); compression; whole word; cluster; generic; coordinate ties; height / gap / tied; padding identity; letter; barycenter identity; partial boundary; local charge.
- **§2.2:** response (three rows); transport; anchor; label; word; window; lift; representative; charge; centered; cutoff (incomplete, see section 3).
- **§2.3:** regularity stage (10:25, 133, 808 verified); subpower (18lp:18); schedule; moving; marked; event indicator.
- **§3 counts verified:** actual 20, select 23, test 47, label 59, mark 53, window 6, history 7, response 25, transport 14, cost 25, mixed 23, column 22, cone 17, centered 24, probe 6, anchor 6, frame 4, phase 52, word 96, cluster 23, heat 18, level 77; price / pay / readout / table / tag 0.
- **§7 label list:** all present.

---

## 10. Not checked

- Survey §5 (synonym clusters) and §6 (overloaded symbols): only spot-checked (`χ` at 13sb:30; `r_d` at 13:146 and 13ba:251; `R_d` at 14:972 and 13:137; the seminorm notations). Not verified row by row.
- Survey §2.1 (same-sense rows): cited lines were checked for the presence of the term; "same as the dictionary" was not re-derived against chapters 3–6.
- `label`: the split between V_d and F_d was checked at the lines listed, not for all 59 occurrences one by one.
- Sub-counts within `threshold`, `comparison`, `stage`, `margin`, `admissible` were not recounted.
- Chapters 10 and 11 were consulted by grep and excerpts only (10:4–22, 23–29, 53–56, 129–134, 165–176, 350–383, 806–809; 11:14–19, 160–172, 208–270, 374–382, 440–448, 496–504, 806–822, 880–960, 1056–1108, 1398–1410, 1880–1930, 2248–2256, 2296–2310); chapters 17–19 only for 18:405–413.
- Figures were not opened. No Lean declaration was consulted. No equivalent was checked against the literature; the judgements in section 6 are from my own knowledge.
