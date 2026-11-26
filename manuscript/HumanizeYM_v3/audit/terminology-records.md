# Terminology of the v3 manuscript: records

Companion to [terminology.md](terminology.md), which holds the dictionary and Appendices A to G and I. This file holds the appendices that record how the entries were decided: the open questions, the decisions, the findings from the source manuscripts and the formal proof, and the names used in the papers of Bałaban and Dimock (with the abbreviations of those papers used in the *Literature* lines of the dictionary). The appendices keep their letters. References `chapter:line` and the file abbreviations are those of terminology.md.

## Contents

- [Appendix H](#appendix-h). Open questions.
- [Appendix J](#appendix-j). Record of decisions.
- [Appendix K](#appendix-k). Findings from the source manuscripts and the Lean formalisation.
- [Appendix L](#appendix-l). Names in the papers of Bałaban and Dimock.

---

<a id="appendix-h"></a>

## Appendix H. Open questions

Points the agents could not decide from the text, by letter range. They were written during the merge; "the note" and "Part I–VI" refer to the previous, chapter-by-chapter version of this file (commit `75bb0840`). Each point is marked **Open** (the current text still does not decide it), **Settled** (how, with the line) or **No longer applicable** (the wording it was about is gone). Open points come first in each group.

### Letters A, B, D

- **Open. actual free history** (17w:71, now "uniform in the kernel history", the words of 11:1699): the object is that of 11:1699, read as the sequence of quadratic kernels; whether the blocking sequence is meant instead is open (see *history*).
- **Open. admissible** without stated conditions at 18lp:103 ("a finite admissible request") and 17m:72 ("an admissible conditional integral with the differentiated kernel inserted"). 13:394 now has "the admissible reference labels of the trials", which is sense 1 (11:1074–1075).
- **Open. admissible periods**: MT:14–15, 19 and 19:20–21 still use the adjective; 1:202 and 10:193–197 give conditions without it. Since 25 November 2026 MT:14–15 reads "admissible periods in continuum units" (decision 36), as 19:20–21; "admissible" is still not defined for periods.
- **Open. affine** and **reflected** in "normalized affine directions" (9:35, 502) and "the reflected seminorm directions" (9s:295–296).
- **Open. block length at 11:1873**: block ratio `L` (probable) or number of steps `m`.
- **Open. amplitude** in the sense "bound on a local factor" (6:1076, 1173, 1208, 1451; 11:256, 276, 280): read from use only.
- **Open. annular estimates** (19:51, 95): which results are meant.
- **Open. anchored marked support bound** (18:174): which result is meant (see Appendix G).
- **Open. block root** (5:1002, 1140; 6:342; 9:75; 11:633; 17c:165): no gloss recorded.
- **Settled. defect Ward identity** (17c:66): the sentence was removed on 25 November 2026 with the alias argument; the Ward identity is now written on each leg at 17c:56.
- **Open. bridge legs** (7:597): `W_a` is inferred from the label `ch05:actual-bridge`.
- **Settled. admissible** at 12:80 ("majorant admitted in the infimum"), 13sb:36 (now "satisfy the bounds (ch04:activity-bounds)") and 14lc:23 (now "a comparison scale `k` whose comparison window lies in a single stage").
- **Settled. alphabet** (11:1911): now "for each term of the original expansion with insertions".
- **Settled. bounded approximations** (19:50): now "proves Proposition (ch13:bounded-singleton), Corollary (ch13:bounded-word)".
- **Settled. block bridge** (10:921): now "the same linearization of the critical configuration"; the representative is not named.
- **Settled. actual stationary tangent** at 17c:48: 17c:48–53 says the derivative is `W_F` and the computation uses `W=W_a`.
- **Settled. output anchors** (6:90): now "the coarse plaquettes based at distance at most `4B/5` from `D`".
- **Settled. adjacent pairs** at 10:30: now "permitted stage pairs (the stages of the two scales of one step)".
- **Settled. exterior discrepancy** (17m:426–442): the phrase is gone; 17m:442 now reads "the normalized residual of (ch11:descent-error)". Whether that identification is right was not checked.
- **No longer applicable. bottom stage** (17w:97): now "the stage of the coarsest scale of the interval of scales".
- **No longer applicable. direction selectors** (7:427): now "The four constant maps `J_a` in the vector regulator `M_μ=Σ_aJ_a^*m_μJ_a`, where `J_a` takes a one-form to its component in direction `a`" (since 25 November 2026 with the symbol and formula).

### Letters C

- **Open.** `cross-modes` (17m:401, "all pushed spectator cross-modes"): the text does not determine the meaning. "Front-column" (11:1343) was replaced on 25 November 2026 by "the one-step coefficient bounds in the direction of the transfer" (whether this renders the source is open, review).
- **Settled.** `compulsory component region` (6:1018): since 25 November 2026 "within distance `300B` of its component of the index triple `A`". `compulsory cutoff factor` (6:1461) is settled: "a cutoff factor kept inside the component".
- **Open.** `centered` at 9:294; settled at 9s:283–284 (see Appendix G).
- **Open.** `comparison level` in chapter 17: 17m:136 now "the comparison scale `k`"; that it is the insertion scale `k_i` is still inferred.
- **Open.** `C_0` ("the blocked completed matrix `C_0`", 7:773): gauge or block completion not determined in the text (the trace of 25 November 2026, `decisions-2026-11-25/contact-matrices-trace.md`, identifies it with Martin's `M_core` by role). The `completed fine kinetic matrix` (17c:64) was removed on 25 November 2026.
- **Open.** `contact identity` (17t:175): the reason for the name is not given.
- **Decided** (25 November 2026, decision 5). `corrected coefficients R_I`: the text calls them the Wick products with respect to the free field (11:2066; 14lc:53) and keeps the recursion; the identification rests on general knowledge, not on a source, and was not checked by a mathematician.
- **Open.** `chessboard seminorm`: that `‖O‖_k` (13:302) and `‖·‖_𝒯` (13:74) are `𝓡_m` is inferred.
- **Open.** `cover paths` (10:81): assignment to the covering-lattice sense is inferred.
- **Open.** `cost` in chapters 17–19: now one use (17w:73); not classified.
- **Open.** `cubic momentum functional` (17m:351, 356): identification with `𝔥` inferred.
- **Open.** `chosen`: the chapter 4–6 lines were not split between the ordinary sense and the auxiliary-index sense.
- **Open.** `conserved line` at 17:341: now "The one-dimensionality of the space of conserved tensors, (ch14:conserved-line)"; the interacting statement of chapter 14 has still not been read in full.
- **Settled.** `admissible comparison depth` (14lc:23): see letters A. `corrected body product estimate` (11:1662–1663): now "the inflated product bound (ch11:integrated-component)". `coordinate hybrids` (14lc:95–96): now "each configuration taking every coordinate from the point or from its rounding". `coarse forecast` (11:725–726): now "one linear prediction of the fine curvature from the coarse field". `coarse kernel level` (11:352): now "coarse kernel order".
- **No longer applicable.** `coordinatewise splice` (7:637): the word is gone (see Appendix D, group 1).
- **Settled.** `compensating map` (6:1540): now "the change of variables `T_V`".
- **Settled.** `path-placement operations` (10:314–315): now "the choice of coordinate contours of Chapter 7".
- **Settled.** `q_r` (12:247) = `q` of (ch11:replicated-bound): 12:247 now says so; `q^site` likewise (13sb:24–25).

### Letters E–H

- **Open. exterior identity** (7:408, 686; 11:1692): never displayed; 5:839 uses the phrase for another identity.
- **Open. finite momentum approximation** (17m:362): no gloss. **front-column** (11:1343) and **Hilbert encoding** (10:381–382) were replaced on 25 November 2026 (the one-step coefficient bounds; the weighted `ℓ²` norm and the summability condition written out).
- **Settled in the text, open for the author. forgetting the terminal graph** (12:131): the title is "Independence of the graph at the ultraviolet cutoff" since 25 November 2026; the review thinks it claims too much and suggests "Forgetting the graph at the ultraviolet cutoff".
- **Open. history**: whether senses 2 and 3 should be counted as one; what "kernel history" (11:1699; 17w:71) means; the title "Changing the block history" (11:92), which replaces the block kernels.
- **Open. equation calibration floor**: 19:29–31 now reads "such as the lower bound (ch11:calibration-floor) on the block ratio"; whether it also covers the condition on `β̂_N` is not said.
- **Settled. equation direction**: `v_eom` was replaced by `v`, introduced at 17m:383 (25 November 2026).
- **Settled. gauge completion**: "completed fine kinetic matrix" (17c:64) was removed on 25 November 2026.
- **Open. group-coordinate contact identity** (17t:175): why "contact".
- **Settled. frame** at 17w:122: since 25 November 2026 "the same diagonal subsequence and the same comparison isomorphisms `U_{i,d}`", the maps being named at 17:139–140.
- **Open. `E_stat`, `E_tail`, `E_mark`** (17m:161–176): only bounds are given.
- **Open. forest prescription** (18:419): known only through `notation.md`; since 25 November 2026 18:419 says it "is formalized but not used in the main result" (decision 9).
- **Open. failure** (17m:121–131): "failure" and "complementary" are restored (17m:121–131, 321), after a period as "violation of a regularity condition" and "large-field terms"; the failures are attached to the supports of the derivatives of smooth chart cutoffs ("their derivatives are supported where at least one enlarged chart condition fails", 17m:124–125). Whether they are all large fluctuation-field events of chapter 6 or also include incoming large-field sites was not said. **Decided** on 25 November 2026 (decision 50): they are large fluctuation-field events, and 17m:121, 122, 127, 129 now say so.
- **Settled. extraction** at 11:2037: now "The estimates hold before any subsequence is chosen".
- **Settled. endpoint** at 11:877: now "the integrated inequalities for the normalized products".
- **Settled. exterior row** (11R:266): now "the bounds for the corresponding action terms far from the large-field set". **finite decorations** (11R:304): now "the finitely many label choices of each selected component".
- **Settled. factor after deterministic subtraction** (9:124): gone.
- **Settled. fixed probe order** (17m:251): now "the order of the coefficient evaluations".
- **Settled. graph** as the graph transform: 11:380 (see Appendix F); "descending graph" is gone (17m:444 "the graph of the backward comparison").
- **Settled. unmarked gas** (18lp:186): now "the exact-cover gas of the density without insertions".
- **Settled. ground algebra** (15:155): now "compression algebra".
- **Settled. exterior discrepancy** (17m:442): now cites (ch11:descent-error).
- **No longer applicable. endpoint error** (17m:444–470): the phrase does not occur at those lines (17m:469, 474 have "endpoint" in other phrases; not reread).

### Letters I–M

- **Open. inverse terminal coordinates**: the phrase is gone, but whether the `X_i` of 11:1101–1102 is the terminal map `𝖹_{N,p,d}` of 11:1047–1049 is still not said.
- **Open. label** between polynomial and field at 13:282–285, 18lp:295, 14lc:7, 13sb:176, 19:36 and in chapter 18 (18:140, 141, 205, 222; 18r:61, 64).
- **Open. infinitesimal gauge insertion**: the phrase no longer occurs; whether `ℛ` (chapter 7) and `d` (chapter 17) are one operator was not rechecked.
- **Settled. macro-box** against **padded block** (7:628): since 25 November 2026 7:628 names the patch `Ly+𝔹_R`, `R=(j+3)L`; see letters N–Q.
- **Open. level**: whether `k_i = k(n_i)`; 17:139–141 still does not write it.
- **Open. left frame** (17t:194–195): unchanged.
- **Open. middle and output stopping scales** (17w:101–102): identification with `ℓ`, `w` of chapter 11 inferred.
- **Open.** **support moments** (10:603; at 18lp:177 now "polynomial factors in the support size"); **inhomogeneous graph estimate** (11:892); **"polynomial logarithmic factors"** (9:712): no gloss found. **missing-coordinate factor** (9:77) and **numerical band margin** (9:950) were settled on 25 November 2026 (formula at 9:77; the sentence at 9:949–951 rewritten).
- **Settled. moving comparison fields** (3:576): now "quantitative convergence of the rescaled interacting fields to free fields".
- **Settled. likelihood tests** (6:920): now "the local factors of the two partition-of-unity weights and the normalized weights of the auxiliary index" (6:919–920).
- **Settled. leading**, sense 3 (11:1551, 1886): now "corrected principal coefficients".
- **Settled. moving labels** (14:238, 250): now "convergent sequences of free fields".
- **Settled. live tag actions; tag-coincidence radius** (9s:127, 221): now "the actions for all values of the auxiliary index with positive probability weight" (9s:127) and "the ball on which the actions for all values of the auxiliary index with positive probability weight coincide" (9s:221).
- **Settled. inspected support** (9:220): now "the support with its adjacent plaquettes".
- **Settled. live group** (18lp:110): now "a single group loses at most the factor `6L_l`".
- **Settled. inverse source-weight bounds** (17m:440): now "The inverse source weights in (ch11:replicated-bound)".
- **Settled. link factor** (5:328–336, 759–763): now *link multipliers* (5:335, D).
- **Settled. moving complement** (11:1083, 2218): now "cutoff-dependent equation space / kernel".
- **No longer applicable. level**: the "output level" of 17t:405, 17c:241, 391 is now "a fixed scale".

### Letters N–Q

- **Open. protected** (sense 2) and **protected-path errors** (17w:72); **protected local representative** (11:1063): no definition.
- **Settled. padded block** (7:628): the patch of radius `(j+3)L`, which 7:628 names since 25 November 2026; 7:599 now says "padded box of radius `(j+5)L` around the patches of the averaging operation".
- **Open. normalized local insertion**: whether the one-step uses (11:353–355, 438) and `O_{N,p}(d,c)` are one notion.
- **Open. opening**: no definition (11:1406, 1889 "opening scale", 1919, 1949, 2151, 2200).
- **Open. one-step integral identity** (7:859): three candidates.
- **Settled. positive partition estimate** at 17w:97: now "the lower bound on the partition function" (25 November 2026, decision 45), as at 17m:433–434, which cites (ch11:replicated-bound); 17w:97 still cites nothing.
- **Open, undetermined in every part:** *normalized large-field majorants* (17m:414); "affine" in *normalized directions* (9:35; 9s:295, where it now stands for the admitted directions of the seminorm); *polynomial-source propagation constants* (17w:12); *powered-curvature-factor estimate* (11E:14); *principal* sense 5; *physical* sense 9; the criterion for *nonwrapping*; formulas for `a_c`, `d_c` (9s:258–259; not added on 25 November 2026, the source has none). Settled among them: *preselection* (gone from 11:382), "path-placement" (10:314–315, see letters C), and on 25 November 2026 *numerical band margin* (9:950), "reflected" (9s:296) and `r_pred` (defined at 6:460).
- **Open. physical support-weighted mass** (11:423), in *normalized mass*: unchanged.
- **Settled (in part). protected** (sense 1): 6:733 now defines "Call a factor protected when it is cut off inside this logarithmic chart", the cutoff reading. 9:258 ("protected coordinate change"), 10:720–721 ("The protected change of variables") and 17m:74 ("a protected dependence set") still apply the word to other things.
- **Settled. probe** at 17m:251: now "the order of the coefficient evaluations".
- **Settled. ordinary** at 10:327 (now "unenlarged output bounds") and at 11:1589 (now "The bound by one of (ch11:higher-induction)").
- **Settled. regular** at 17w:78: reading A ("The regular and large-field source recurrences", the regular and large-field norms; the line was briefly reworded and has been restored).
- **Settled. orientation of the line** (14:308): now "This fixes the sign of the chosen tensor on the line." **physical mark normalization** (17m:441): now "The dimensionful normalization of the insertion".
- **No longer applicable. output level** (chapter 17): now "a fixed scale" (17t:405; 17c:241, 391).

### Letters R

- **Open. row** (7:1059): "the prescribed coarse quadratic row", unchanged.
- **Open. response**: "the anchored vector response" (17:224) is still an inferred reading.
- **Open. protected local representative** (11:1063): object identified, word not explained.
- **Open. `𝒫_D` and `H_d`**: that the reconstruction of 18lp:266–279 and the field reconstruction of chapter 18 are one map is the note's reading (not rechecked).
- **Open. raised hole correction / regular logarithms with holes** (11R:365–369): unchanged; "hole" still does not occur in chapter 8.
- **Settled. read-count polynomials** (9:147): now "the polynomial factors `(1+s_M)^{d_j}` in the number of blocks read" (25 November 2026).
- **Open. residual**: the sense list was not rechecked.
- **Open. reflected seminorm directions** (9s:296): "reflected" is not explained.
- **Open. reflection cubes, faces** (9:325, 350): unchanged.
- **Settled. relaxed** (10:98; 13ba:36–40): 10:98 now "the indicator of the relaxed regularity condition is one"; 13ba:36 "the small-field indicator".
- **Settled. regular** (17w:78): see letters N–Q.
- **Settled. reference rows** (15:275, 278): now "the finitely many free tests".
- **Settled. response** at 6:846 (now "derivative of the averaging operation") and 19:159 (now "the linearization of the critical configuration").
- **Settled. response bound `ε`** (10:626): now "the fixed fraction `ε`" (of what is not said). **recording** (7:461, 742): now "mesh estimate", "finite-volume coefficients". **replicate** (the verb): gone (17m:432 "Place a copy in each reflected cell").
- **Settled. `𝒰_F` and `W`**: 6:953, 976 write `W_F`.
- **Settled. restoration levels** (11:1405): now "the middle scales". **rebasing contraction** (11:467): now "the contraction estimate of the graph transform".
- **Settled. residue patterns** (13:367; 15sp:11): now "classes modulo the (side-`a_m`) tiling". **replica census** (15:261): now "an arbitrary finite set of reflected copies".

### Letters S

- **Settled. seeded sector / unseeded law** (6:1544; 9:283–284): replaced by the index triple on 25 November 2026 (the review notes that the source's seeds also include coarse sites).
- **Open. "source"** at 17w:12 ("polynomial-source propagation constants") and 18:411 ("the source prescription"): not classified.
- **Open. "sparse"** in "sparse stopping scale" (10:172): inferred reading only. (18lp:159 no longer has the word.)
- **Open. selected** at 13:395 ("the same selected family of measures") and at 13ba:30 ("their selected scale-`h` polynomial").
- **Open. site norm**: whether the "support norm" (8:196) is the site norm; "attachment norm" and "rooted activity norm" are gone (9:697, 12:178).
- **Open. slab** in 11:844–876 and **strip** in 13:84, 368: not rechecked.
- **Open. spin operators** (14:903): now "the infinitesimal rotation operators"; identification with the generators `L(K)` still inferred.
- **Open. stationary tangent**: `W^rad` (17c:191) is not glossed.
- **Settled. selected slot** (11:424): now "The large-field factor carrying this input". **same-data restart conditions** (11:1666): now stated. **support compression** (9:231): gone.
- **Settled. "source"** at 14:186 ("the construction below"), 17w:78 ("source recurrences", sense 8) and 11:1632 ("a principal term").
- **Settled. stage** at 5:689 ("each pair of stages of one step (Section ch10:choices)") and 6:21, 96 (stage now defined at 4:651); **bottom stage** gone.
- **Settled. stationary tangent**: which representative the `W` of 17c:48 is (17c:48–53).
- **Settled. signed local transport** (18:174): now the reference (ch18:signed-transport).
- **No longer applicable.** "source" at RG:82: the line now reads "accompanying chapter audits provide source locations", the ordinary sense.

### Letters T–Z

- **Settled in the text. terminal**: the title at 12:131 no longer says "terminal graph" (25 November 2026; now "Independence of the graph at the ultraviolet cutoff").
- **Open. threshold**: 17m:197 "stage orders and thresholds" is not assigned to a sense.
- **Open. target**: "the finite target list" (11:1364) is not identified. "Normalized target columns" (11:1237) was replaced on 25 November 2026 by "the solutions `u=u_{j,N,p}` of the lift equations".
- **Settled. weight**: "encoding weights" (10:382) was replaced on 25 November 2026 by the condition `Σ_γ e^{−2(δ−w)ℓ(γ)}<∞`.
- **Settled. `v_eom`**: replaced by `v` (17m:383–386, 25 November 2026).
- **Open. with these same comparison isomorphisms** (17w:122): the noun has no antecedent in 17w; `U_{i,d}` is a guess.
- **Open. unreparametrized remainder map** (12:91): the reading "before composing with `I_G⁻¹`" is inferred.
- **Settled. tangent**: 17c:48–53 says the derivative is `W_F` and the computation uses `W=W_a`.
- **Settled. target** at 11:2207: now "limit configurations".
- **Settled. vacuum normalization bound**: 12:247 now "the per-site normalization exponent of (ch11:replicated-bound) at scale `r`".
- **Settled. Four phrases of 17m:426–442**: 17m:426 now "multiplication by its constants"; 17m:440–442 cite (ch11:replicated-bound) and (ch11:descent-error), and 17m:441 reads "The dimensionful normalization of the insertion".
- **Settled. tag-coincidence radius** (9s:221): see letters I–M.
- **Settled. Trace norms and recording** (7:742): now "Trace norms and finite-volume coefficients".
- **No longer applicable. warning**: the word is gone; 6:1476 now "Cutoff remainders carry the joint-event factors", 11:319 "the joint tail bound for cutoff remainders".

### Concepts with several names

- **Settled.** The padded block (7:628) is the patch of radius `(j+3)L`; 7:628 says so since 25 November 2026.
- **Open.** Whether the site norm, containing-site norm, support norm and activity norm are one norm (8:69; 9:513–518; 8:196; 10:445).
- **Open.** Whether `‖O‖_k` (13:302) and `‖·‖_𝒯` (13:74) are the chessboard seminorm `𝓡_m`.
- **Decided** (25 November 2026, decision 5). `corrected coefficients R_I`: called Wick products with respect to the free field in the text (11:2066; 14lc:53); general knowledge only.
- **Open.** "Comparison scale" in 17w and 17m against ch. 11: which scale is meant (I).
- **Settled.** "Warning" (6:1476; 11:319–320): now "cutoff remainders".
- **Settled.** "Likelihood tests" at 6:920: now both weights are named (6:919–920).
- **Settled.** "Bottom stage" (17w:97): gone.
- **Settled.** "Corrected leading coefficients" (11:1551, 1886): now "corrected principal coefficients".
- **Settled.** "Ground algebra" (15:155): now "compression algebra".
- **Settled.** The one word for the operator `W` (linearization of the critical configuration), for the critical-point map (critical-configuration map), for the constant `b` (penalty parameter), for the index `d` (filtration index), for the algebra `𝔄` (compression algebra), for the restarted history and for the identity of Proposition 9:651 (exact regrouping): decided on 23 November 2026 and now in the text (Appendix B).

### Symbols

- **Open.** `a_*` (6:733–736), `λ_i` (6:1112, 1132), `π o_X` (6:1301), `E_stat` / `E_tail` / `E_mark` (17m:161–176): no definition in the text. `r_pred` (6:460) is defined there since 25 November 2026.
- **Open.** `K_ax` (4:364) = `a_ax` (4:68–72, 90): inferred.
- **Open.** The meanings of `u`, `X`, `c`, `p`, `V`, `ν`, `δ`, `μ` in ch. 17–18 that Part VI counts but does not cite (not rechecked).
- **Open.** About 30 entries of Part III's table without a line reference (e.g. "partition functions", "`H_4`", "bounds `B_H`, `B_loop`") were not located (not rechecked).
- **Open.** Whether `‖O‖_k` (13:302) and `‖·‖_𝒯` (13:74) denote the chessboard seminorm.
- **Settled.** `q_r` (12:247) = `q^site` (13sb:24): 12:247 now says that `q_r` is the per-site normalization exponent of (ch11:replicated-bound).
- **No longer applicable.** `𝒰_F` (6:953, 976) and `𝒰_F` = `W` or `W_F`: the symbol is gone; both lines write `W_F`.
- **Open** (trace of `M_core`, `M_act`, 25 November 2026, `decisions-2026-11-25/contact-matrices-trace.md`). In chapter 7: `Z` is the "coarse-frame projection" at 7:477 and the contact term at 7:527; `r_x` is the coarse scalar component at 7:506, `r` the scalar coordinate at 7:695, `r(x)` the penalty gradient at 7:523 (Martin writes `b(x)`, Scott `d`); `A` is the fine kinetic Hessian at 7:275 and `M_core` at 7:527. The centered tangent is `(Wx, r_x)` with possibly nonzero `r_x` in v3 (7:506, 580–582), `(Wx, 0)` in both sources (Martin `thermal-contact-cancellation.tex:94`; Scott `B-section.tex:645`). The trace's proposed wording for 7:521, 523, 524 was not applied.
- **Open.** `C_st` and the "principal" and "complementary regular bound" (10:622–626): defined nowhere in v3; 10:626 has used them since the repair of 25 November 2026 (review of the repairs).
- **Open.** The transport clause of Hypothesis (H) (11:335): `F_i∘ς^*` needs an action of `ς` on the cutoff lattice, which is not defined (chapter 9 defines it one scale finer), and the clause refers to cutoff insertions inside a one-step hypothesis (review of the chapter 11 adaptation, 25 November 2026). Also open from that review: the wording of 11R:192 (what needs the averaged activities is the symmetry of the incoming representation at the comparison scale); the status paragraph of `chapters/09-forest-average.tex`:963–967, which still says chapter 11 is not adapted.
- **Open.** "Reference coupling" for `β̂`: decision 33 of 25 November 2026 calls it the defined short name of `β̂`, but no defining sentence was found by grep (4:408 has "the reference values"; 9:17 and 17:86 "reference value").



**The two sections that follow are a record.** They list corrections to entries of this dictionary as it stood before the regeneration of 25 November 2026, and they quote the manuscript at commit `4f462ac5`. They were not brought up to date; the entries above take precedence.

### Corrections proposed by the sample check and not yet applied

Each block is the note of one agent that rewrote the sampled entries. "The report" is the sample-check report it worked from.

#### From sample check 1

All corrections were confirmed against the chapter lines (checkout `/Users/mgubi/ym-terminology`, grep with `\label`, `\ref`, `\eqref` arguments stripped) before being applied. 27 entries rewritten (26 MINOR, 1 WRONG).

#### Corrections not applied, or applied differently

- *chosen*, sense 2: the proposed equivalent *every frame tag of positive probability* was not taken over. The sentence is "Every chosen frame tag must have positive mass" (6:63), so that equivalent would make it circular. The entry keeps *chosen* with the reading "assigned by the random index" marked as inferred (basis I).
- *chosen*: RG:33 ("It is chosen slowly enough") added to sense 1; the main theorem has no "chosen".
- *low-energy estimate*: 16:439 not added to *Where*; the line contains only `\eqref{ch16:low-energy}` and "the estimate", not the phrase.
- *logarithmic*:
  - 9s:176 corrected to 9s:175 (the word is on line 175); 6:953 written as 6:953–954.
  - 10:514, 570, 605 were not left "to be checked" under sense 2. 10:570 ("Small logarithmic factors", estimated through "their exponential minus one") is sense 2. 10:514 ("convergent logarithmic series") and 10:605 ("the logarithmic expansion") are put with the new sense of 8:228 (logarithm of the partition function), basis I.
  - 17t:90 ("the same logarithmic coefficient as the regulated response") was not added to sense 4 (log-determinant); only 17t:97 ("logarithmic Hessian") is clear. 17t:90 is listed as not classified.
  - 10:61 ("fixed logarithmic size bound `K_j`") was not put in the "power of `log β̂`" sense: `K_j` is compared with `log ℒ_j`. Listed as not classified.
  - Added by grep, beyond the report: 6:1075 (sense 3); 11:750 and 17m:173 (sense 6). Nine lines (17c ×4, 17t:90, 387; 17w:42; 17:137; 10:61) are listed as not classified. The count is 60 exactly.
  - The new senses are numbered 7 (logarithmic scale) and 8 (logarithm of the partition function); sense 6 is rewritten as proposed.
- *period*: the *Where* list was rebuilt by grep; counts are 108 lines in 26 chapter files plus 3 in the main theorem ("about 110", not "about 120"); chapter 11 has 25 lines, not 26; chapters 13–19 have 25, not "about 30". "10:196–199" is given as 10:199 (lines 196–198 are a label and a formula).
- *trace functional*: `ρ` lines given as 17:266–278 (the symbol does not occur at 262–265).
- *suppression*: 13ba:77 ("the original large-field suppression") added by grep; "Across chapters" therefore includes 13ba.
- *curvature family*: 7:1168–1169 ("the cubic/quartic families of Proposition (ch07:classical-match)") added as further support for the identification with `S_3`, `S_4`; basis kept at I as proposed.
- *scalar*: the new sense is numbered 9 (after the ordinary sense 8) so that the references "scalar (sense N)" elsewhere stay valid. Chapter 3 has 14 lines with the word (not 15).
- *reconstruction*: 3:761, 6:1561, 7:142 are listed as not classified (not in the report).
- *descent*: 17m:470 removed from sense 1 (the word is at 17m:469 only).

#### Found wrong or unverified in the report

- Nothing in the report was contradicted by the text, apart from the small line and count differences listed above.
- Not flagged by the report but found while checking *exterior*: in sense 1 *Where*, 18lp:207 and 18lp:238 contain "interior", not "exterior". The list was left as it stands, since the report does not correct it; these two lines should be removed or marked "(interior)". Uncited sense-1 lines found by grep: 13:366, 373, 377, 380, 382; 14:354; 16:66, 245; 18lp:323, 332.
- *normalized directions*: 6:1282 ("normalized small-field directions") is not in *Where*; it was added to *Variants* only.

#### Corrections for other entries (not in the sample), not made here

- plateau: sense 1 *Where* should read "5:973; 6:917–920, 1011–1016, 1023; 11:712–713" (5:1044, 5:1241 and 6:281 have "uncut" and no "plateau"; confirmed by grep. The report gives "6:1014–1016"; the word is at 6:1011, 1012, 1016, 1023).
- selected: its "Across chapters" line and the new *chosen* entry now agree on 4:456, 4:616; no change needed there. Sense 9 of *selected* should mention 6:63 ("chosen frame tag") as the one "chosen" among the random-index lines.
- clean: carries the shared list 11:679, 709, 721 with *remote*; 11:709 has "remote", 11:679 "clean", 11:721 "clearance". The list should be split by word.
- backward comparison: 11:27, 890 and 11E:121 belong to this entry (they have "Backward comparison", not "descent"); check that they are listed there.
- second cluster expansion / first expansion: both carry 9:44, 88–89, 148, 173, 192; the phrase "second cluster expansion" occurs only at 9:192. Split the list by word.
- source weight: carries the same chapter 12–18 list as *available weight*; say that "available weight" occurs only at 18lp:128, 168, 175.
- stationary graph: 17c:147 ("stationary internal coordinates") and 17t:28 ("stationary substitution") have neither "branch" nor (to be checked) "graph"; removed from *branch*, to be checked in *stationary graph*.
- mass (sense 2): already lists 11E:104–105 and 18lp:115–116; now consistent with *normalized mass*. No change needed.
- discrepancy (sense 5): "exterior discrepancy" (17m:426–442) is marked `?`/"not identified"; 17m:67–70 explains "exterior" (integrals against spectators independent of the varied coarse links). Replace the `?` by a pointer to *exterior* (sense 2).
- replacement: says, like the old *reconstruction*, that 18lp:266–279 has no formula and concludes basis R; 18:67–70 defines `H_d` by a formula (and 18:82–85 the symmetrised `A_d`, `B_d`). Same correction needed.
- soft constraint: omits 5:146 and 17c:288–290 (the penalty term), as *block penalty* did; add them.
- torus period, physical (sense 1), admissible periods, volume: *period* now proposes to keep "period" and to use *side length* only for "torus side" / "torus size"; check that these entries do not propose *side length* for "period".
- expense: basis R is too strong (nearer I), 11:2137–2138.
- core: 6:1359, 1389, 1438 could be added to *Where*.
- group: uses continue to 18lp:167, 183, 246.
- General (section 3 of the report): entries whose *Where* list was copied from a source row covering two words can be found mechanically (does the headword or a variant occur within the cited line ±1?); entries still scoped to one chapter group can be found by comparing the files in *Where* with the files where `grep -w` finds the word; "only in chapter X" statements should each be checked by one grep.
- Proposed equivalents not checked against the literature or `blueprint/notation.md`: *Mayer expansion* (first expansion), *holonomy* for "path word" (6:630; an open path, so *parallel transport along the path* may be safer), *critical-point map*, *threshold ratio* for `M^cut`.

#### From sample check 2

All 31 MINOR and WRONG entries of the report were opened against the chapter text (worktree `/Users/mgubi/ym-terminology`, which differs from commit `7bec3925` in 24 line-preserving edits) and every correction was confirmed, with the adjustments below. 32 blocks are given: the 31 entries plus *containing-site bound*, which becomes the full entry for the duplicate *site norm*.

#### Corrections applied differently from the report

- **comparison level**: the report lists `11R:217–218` in *Where*; those lines have "comparison window with top level `k`", not the term. They are cited in the meaning and basis only, as are 11:1753–1754 (`m = k − ℓ` is at 1754, not 1753) and 11:2085–2088.
- **complete**: the report corrects "chapters 12–15" to "12–18". Grep shows the same use throughout chapter 11 (11:95, 507, 775, 899, 1038, 1159, 1498, 1916, 1949, 2114; 11E:84; 11:775 states the inclusion explicitly), so the entry now says chapters 11–18. 12:208 and 13ba:153 are removed from *Where* (ordinary "whole") and the count "16 in all" is dropped. The assignment of the individual chapter 11 lines was made from the line alone, except 11:775, 1038–1039, 1159–1160, which were opened.
- **coordinate half-space spectrum**: the report keeps `14:69–77, 413–414` in *Where*; only 14:76 (headword) and 14:410 (variant, section title) contain the term, so the other lines are cited in the basis.
- **exact unit rule**, **joint bound**: *Where* gives the single occurrence (11:1049–1050; 9:114–115); the passages that state the content are cited in meaning and basis.
- **quotient estimate**: 7:719 is the formula and does not contain the term; it is cited in meaning and basis, not in *Where*.
- **site conversion**, sense 1: the report lists `11:266–272`; the word "conversion" is at 11:267 only. The lines 11:257, 300, 1473; 11R:74, 125, 170–181 of the old list are "site bound" lines and moved to *containing-site bound*.
- **kernel**, sense 3: the report gives `4:240` (the label line); the definition is at 4:234–240 and the word also at 4:169, 249, 257, 282. Block-kernel uses found by grep and added: 9:49, 810; 9s:13, 125; 10:127. Chapter 7 lines of sense 2 are listed (10 lines; the report says 11 uses). Senses 1 and 4 were not rechecked beyond the report; the null-space sense has many uncited occurrences (2e:20, 147, 153; 3:161, 192, 644, 931, 1021; 11:967–969, 1096, 2222, 2320; 13:185, 220; 14:279, 817–821, 955), mentioned in *Across chapters* only by chapter.
- **auxiliary**: sense 1 has 7 lines, not 8 (7:108 removed). 10:782 and 10:923 could not be assigned and are listed as not classified; 11:8 is placed with *auxiliary history*.
- **array**: the meaning was widened by "or tensor indices" to cover 14:262; 10:321, 507–516, 654 ff., 11:453, 471, 13:141, 17w:109 also contain the word and stay under "passim" / uncited.
- **site norm / containing-site bound**: the two entries duplicate each other; *containing-site bound* is made the full entry (it is the chapter 4 notion and already had "site norm", "site bound", "site sum" as variants) and *site norm* a pointer. Its *Where* list was rebuilt by grep for "containing-site", "site norm", "support norm", "site bound", "site sum" (11:1896 "separated-site bound" excluded). The proposal follows the report (*site norm*, kept, against *anchored norm*).
- **unselected**: variants "unselected tests" (6:336) and "unselected rows" (6:1437) added; "unselected plaquette" kept.

#### Corrections not applied

- **low plane** (classified CORRECT, note only): not rewritten. Suggested change, confirmed at 18gq:76, 94–95: *Proposed* should read "*span of the basis polynomials of scaling dimension below `i`* at the microscopic level; elsewhere *its image under the transfer*".
- **ordered tail**: 18gq:39–40 ("converges on an ordered cutoff and volume refinement … on that tail") was not added; the phrase is not "ordered tail".

#### Found wrong or imprecise in the report

- comparison level: "11:1753 (`m = k − ℓ`)" is line 1754.
- complete: "one sense in chapters 12–18" overlooks chapter 11 (see above).
- kernel: "7 (11 uses)" is 10 lines; "defined at 4:240" is the label line of the display beginning at 4:234.
- stationary graph: 7:949, 1152 and 9s:39 have "branch" alone (kept, as in the present entry).
- Nothing else in the report was found unsupported by the text.

#### Changes needed in other entries and in the appendices (not made)

- uncut: *Where* is the list shared with *plateau*; it should be `5:973, 1044, 1241, 1286, 1302, 1325; 6:281` (the report gives the first four and 6:281; 5:1286, 1302, 1325 found by grep). Remove "6:917 ff.".
- common law: *Where* should be `9:115, 139 ("common integral"), 785 ("common-law estimate")`; *Proposed* should be *the joint law `ν`* alone, since *joint estimate under one measure* is the proposal of *joint bound*. 11:510 also has "common integral".
- incoming: the counts "ch. 7, 22 lines; ch. 9, 27 lines" are for incoming / inherited / outgoing together; the lines 13sb:10, 72; 13ba (6); 18lp (4); 14lc:60 contain no "outgoing". The variant "outgoing" should point to the entry *outgoing*.
- site bound (pointer): should read "See *containing-site bound*." instead of "See *site conversion*.".
- support norm (pointer): should read "See *containing-site bound*." instead of "See *site norm*.".
- support conversion cost (pointer), root-to-site conversion (pointer): still valid; could say "See *site conversion* (sense 2)" and "(sense 1)".
- weighted quotient (pointer, line 6140): could say "See *quotient estimate* (sense 1)".
- See-also lines naming *site norm* (attachment, support-weight reserve and others, lines 372, 5498, 5508): now reach the pointer; could be retargeted to *containing-site bound*.
- selected: no change needed; the new *unselected* agrees with its sense 1.
- candidate field / trial: the proposals cross (*candidate field* → *trial field*, *trial* → *candidate local observable*); one of the two must be changed.
- reserve: 8:150–151 does not contain the word (the label is at 8:146).
- ordered limit: 11:1031 could be added to *Where*.
- tuned: the verb also occurs at 1:464, 4:407, 9:975, MT:62 in the same sense.
- vacuum normalization bound: 10:422 does not belong to it; "vacuum normalization" there was the additive normalization constant, and the line now says "vacuum energy renormalization" (see *vacuum*, sense 3).
- forward-difference primitive: 13ba:230 "primitive random variables" is a further ordinary use.
- *block-completed form* (line 489) and *completion* (sense 2, line 1028) quote "The block-completed form needs a quotient estimate": should refer to *quotient estimate*, sense 1.
- Appendix G (line 6594): remove *powered-curvature-factor estimate* (now basis I); add *kernel identities* (now basis `?`).
- Appendix H (line 6698): remove *powered-curvature-factor estimate* from "Undetermined in every part"; add an item for *kernel identities* (which of (ch17:kernel-divergence) with 17m:396–398 or (ch17:block-algebra) is meant at 17:308); lines 6728 and 6753 (*site norm*) should name *containing-site bound*.
- Appendix B (line 6329, polymer-activity norms): add "support norm" at 11:217 and 11R:7; "Not synonyms" could add site conversion against support conversion ((ch11:cover-transfer)), and unselected against small-field (6:54–60, 1340–1342).
- Appendix J (line 7058, kernel identities "basis I kept"; line 7323, site conversion "Parts I, IV, V agree"; line 7393, unselected): superseded by the entries above.
- Contents line: the counts change (one more pointer, *site norm*; two more entries with several senses, *quotient estimate* and *site conversion*).
- General: several entries list in *Where* lines that explain the term without containing it; a separate "cf." list would remove the ambiguity (done here for the rewritten entries by moving such lines to meaning or basis).

#### From sample check 3

All 26 MINOR entries of the report have a block above (the report has no WRONG entry). Line numbers were checked against the working tree of `/Users/mgubi/ym-terminology` (HEAD `e533a10a`, not `7bec3925`; the report's line numbers agree with this tree).

#### Corrections not applied, or applied differently

- **post-length threshold conditions.** The report says that "length = block ratio `L`" is a bare inference. The text is more explicit than that: 11E:20 "These quantities are fixed before the block length" and 11E:31–32 "the section and its derivative constants are fixed first, then the length, then the inverse coupling threshold". The basis line now gives R for "conditions on the starting scale", cites 11E:20, 31–32 for "post-length = after the block length is fixed", and keeps I only for "block length = block ratio `L`" (11E:25–29).
- **shell, sense 2.** The report says the word is at 14:328. It is not in the prose there: line 328 has only `\ref{ch14:fig-ward-shell}` and line 330 `\input{figures/ward-shell}`. Both are left out of *Where* and mentioned as a figure name. The report's "14:312–313" is 14:312 (the title is one line).
- **shell, sense 6.** The report gives no basis; I put R (17:424–426, where the kernels `K_{m,k,h}` are displayed). I did not read the display beyond its first line, so whether it is a definition of "mass shell" is not checked.
- **shell, sense 4.** The report adds 16:415 to this sense; the headline was widened from "comparable radius" to "comparable size" so that the energy range fits, with basis R for that line.
- **threshold, sense 2.** The report's corrected list omits 17m:304, 378, 427 without giving a reason. All three lines contain "threshold" ("threshold ball", "threshold coordinates", "threshold costs"), so they are kept. The report cites 11:748 and 11R:18; the word is at 11:749 and 11R:19. Lines 4:420, 534, 572; 10:734, 899; 11:795, 1313; 11R:20–23, 45–46, 71, 187; 11E:115 were added after reading the context (not in the report). Sense 1 received 10:104–105, 11:278, 443, 711, 11R:10, 11E:32 in addition to the report's four lines ("inverse coupling threshold" is explicit in each). The remaining chapter 10–11 lines are listed as unclassified in *Across chapters*; sense 4 points to the five lines that say "threshold(s) for the starting scale(s)".
- **zero-energy subspace.** The defining sentence is at 15:27–28, not 15:26–27.
- **joining bound.** The report gives the role as 18lp:79–86, 94–96; the sentence about retained representatives starts at 18lp:93, so 93–96 is cited.
- **replicate.** The report's "place one copy in each cell of a reflected tiling" for 13ba:283 is itself a reading: the sentence does not mention a tiling (the reflected cells are at 13ba:269–271). The basis is therefore I for the verb, R for the estimate.
- **averaged measurements.** The report's formula `L_i((I − Π_i)u_{j,i})` is not printed in the text; the entry says in words "the values of `L_i` on the rows `(I − Π_i)u_{j,i}`" (11:2253–2255).
- **coefficient recovery.** Of the report's two options the second sense was chosen, because a pointer entry *coefficient conversions* → *coefficient recovery* exists (dictionary line 818) and would otherwise point to nothing.
- **width, sense 1.** In addition to the report's lines, 10:34, 442, 712, 758 were added (grep; "path widths", "width reserve").
- **random index.** The headword is kept (no RENAME): the report asks only for a line saying it is the dictionary's own name. The bare "9s" in *Where* was replaced by the four lines found by grep (9s:127, 134, 221, 242).
- **field reconstruction.** Which of `A_d`, `B_d` the text means by "symmetric reconstruction" (18:212) is not said in the text; the entry says so instead of naming `B_d` alone as the report does.
- **nilpotent marker.** 18:128 is removed from *Where* (it has "marks") but still quoted in the meaning; "*insertion* at 18:124, 128" in *Proposed* became "at 18:124".

#### Not verified

- **refinement.** The lines were confirmed by grep; 17:21 was read (ordinary sense), 13:53, 15:257, 18gq:40, 47, 19:36, 60 were seen only as single grep lines. The variant "volume refinement" was removed: it does not occur in the manuscript (grep).
- **fine residue.** The meaning "class modulo `L`" rests on the count `L^4` and on 17t:55; no line defines the term.
- 18lp:266–279 (the basis of *reconstruction* sense 2) was not read.

#### Changes needed in other entries (not made here)

- reconstruction (sense 2, line 4322): replace the proposal "projection onto `F_D` along the fixed probes" by "the field of `F_D` with the same fixed probe coordinates"; it contradicts "not a projection" in *field reconstruction*. Its variant "field reconstruction" should point to that entry.
- defect (sense 2, line 1462): the formula should read `Z₀ = B_c − T*B_fT − b⁻¹ d_{1,c} d_{1,c}*`; add 5:453, 603, 1371 to *Where*.
- branch (sense 1, line 556): same meaning, basis and *Where* as the new *minimizing branch* (remove 5:948, which is a branch of an analytic function; add 6:496; "chapters 4–6", so the *Across chapters* sentence "sense 1 in chapters 4–5 only" is false); variant "minimising branch" should be spelt "minimizing branch".
- fallback (line 2011): its pointer to *branch* sense 1 says "the smallness test fails"; add that equality belongs to this case (4:211–212).
- inflation (line 2595): the pointer gives the formula of 8:171 for "chapters 8–9"; chapter 9 inflates by `h = 𝔟^{3/8}` per unit of degree (9:174–180).
- source prescription (line 5212): duplicate of *forest prescription*; make it a pointer (`See *forest prescription*.`) or give it the same meaning (the one-shell rule of 18:398–410 is stated in the book).
- mark (sense 4, line 3172 ff.): consistent with the new *nilpotent marker*; no change needed except that 13sb:72 ("mark weights") is not a "marker" line.
- integral shear (line 2684), interpolated link fields (line 2716): delete "one reader only" from *Across chapters* (unexplained process note).
- "(note 2749): new entry" and similar notes: not explained in "How to read an entry".
- Entries that use "the random index" as if it were the text's term (lines 566, 707, 713, 2833, 2945, 2979, 3198, 4945, 5121, 5528, 5535, 5547, 5905, 6109; Appendix B lines 6283, 6285; Appendix C lines 6415, 6484; line 6642): say "the index `α`" or "the label `α` (4:217)".
- block floor (line 497) and Appendix B (line 6267): "stage-`j` block floor" (11E:29) is correctly a variant there; "calibration floor" in the Appendix B row is one member of the block floor, not a synonym for it.
- comparison coefficient (line 958): the variant "comparison family" does not occur in the chapters; the text has "coefficient family" (11:1101) (not checked by me).
- free (line 2276): the across-chapters note places the Gaussian sense of "free" in chapter 3 only; it runs through chapters 11–19 as well (11:2065, 15:275) (not checked by me).
- `hot(s)` (line 2544): basis I in the entry, R in Appendix C (line 6515) for the same comparison (not checked by me).
- cutoff: should cover 4:203, 211, 406 (the small-field cutoff of chapter 4), now removed from *threshold* sense 2 (whether the *cutoff* entry already lists them was not checked).
- replicate: "replicated coarse field" (6:180, 341, 445, 587) is a further use of the word in chapter 6 that the entry does not mention; whether it has its own entry was not checked.

### Corrections implied by the source and Lean findings and not yet applied

Appendix K settles many of the questions listed above in this appendix; where they conflict, Appendix K and the entries are right. The lists below name further statements in this file that the findings contradict.

#### From the source and Lean findings, set 1

- `terminology.md` *anchor*, Variants line: "output anchors (6:90, undetermined)" → "output anchors (6:90: coarse plaquettes, see *output anchors*)"; sense 1 lists 6:90 under "site of a support", which does not fit (the output anchors are plaquettes addressed by base site).
- *response*, senses other than 4: 6:846 "block average response" was not traced and stays as it is.
- *moving*, *Across chapters* / *See also*: add that 3:576 is sense 1.
- *shared frame seed*, *Across chapters*: "Whether it is related to 'seeded / unseeded' … is not determined" → not related: the seeds of chapters 6 and 9 are the selected large-field elements.
- *sector* / *selected* entries (See also at 4928): the selection `A` is what the sources call the seeds; add the cross-reference.
- *uniform mass*, *Across chapters*: "'Likelihood tests / factors' (6:920, 1016) are probably other weights and are not merged here" → they are the same weights taken per site and per bond and normalised by the number of tags.
- *mandatory factor* (3169): "This does not settle 'compulsory component region' (6:1018) and 'compulsory cutoff factor' (6:1461)" → those are settled in *compulsory*, sense 2, and are a different object.
- *cutoff remainder* (1428): "The remainder itself is not defined; that it is the difference produced by a smooth cutoff being different from one is inferred" → it is `γ·a − 1` (bounded cutoff times an allocation, tag or contraction factor, minus one) or a chart cutoff minus one; add the *Source* line of *warning* and "warning" as a variant.
- *cutoff failure* / *cutoff-failure event* (1408–1423): the "cutoff-failure indicator" of 6:1018 is a cutoff remainder (source: "warning"), not an event indicator.
- *tail events* (5580): cross-reference to *warning* stays; add that the warning estimate is the joint bound for these events.
- *fixed-position read* (2169): "'Coordinatewise splice' in the same sentence is not explained" → see *coordinatewise splice*; the meaning there ("averaged over offsets") should be checked against Martin `weighted-frame-penalty.tex:78–83`, where the read is the link at a fixed position along one straight piece of a coordinate path between two patch points.
- *block-average patch* (480) and *macro-box* (3156): "for the 'padded block' of 7:599, 628 the text does not decide between the two" → 7:599 is a third box of radius `(j+5)L`, 7:628 the block-average patch (the latter inferred).
- *margin* (3176) and *inner barriers* (2633): "The 'numerical band margin' of 9:950 is not determined / possibly these barriers" → it is the condition (ch10:drift-floor), `C^drift_j/log 𝓛_j ≤ κ_G/4`, which makes the barriers work.
- *compression* (1039): "'Support compression' (9:231) … unrelated" stays correct; add the pointer.
- *tag* (5546): "'Live tag actions' (9s:127) is not determined by the text" → see *live tag actions*. *live group* (2978): "a separate, undetermined use" → "a separate use (tags of positive weight)".
- *chart* (676–677): the "tag-coincidence radius" cross-reference now points to a determined term.
- *affine* (202–203): "'reflected normalized directions' … the word is not explained" applies to "affine" only; "reflected" is settled.
- *stage* is referred to from *step* and *smoothing order*: the statement "the reading 'step' is not excluded at 5:689" is removed in the entry; any copy elsewhere should go.
- Appendix B, "Fields and gauges", row "The weights of the random index" (6297): "'Likelihood tests / factors' must not be merged: 6:1016 probably the allocation weights `ϑ`; 6:920 open" → both are the tag weights `λ`, normalised per site and bond; they are to be merged with this row, and are not the allocation weights.
- Appendix B, "Operators and maps", row on `W` (6321): "`𝒰_F` (6:953, 976) is not identified with `W` by the text" → `𝒰_F = W_F` (source and Lean); add `𝒰_F` to the names.
- Appendix B, row "The mesh-mean error bound of ch. 7" (6328): add that "recording" is the source word for the agreement of finite-volume coefficients with the common coefficient function.
- Appendix B, row "Failure of a smooth local cutoff …" (6334) and "Not synonyms" items 6400 (`padded block`), 6425 (`likelihood`): update as above (6400: two boxes, radii `(j+5)L` and `(j+3)L`; 6425: same weights, normalised).
- Appendix C, row `U` (6485): "`𝒰_F` (6:953, 976; undefined …)" → "`𝒰_F` = `W_F` (6:953, 976)". Row `H` (6462): "output anchors (6:90)" → "set of coarse plaquettes near `D` (6:90)". "Symbols used without definition", row `𝒰_F` (6522): replace "Probably one of the operators `W`, `W_F` of ch. 5; the text does not identify it. I" by "`W_F` of 5:1143; S".
- Appendix D: the item "9:949" can be moved to the repairable ones with the wording above.
- Appendix F, row "cutoff failure, warning | large-field event" (6589): unchanged, still correct.
- Appendix G (6606): remove from the list of terms the text does not determine, or mark as resolved from the sources: compulsory; coordinatewise splice; direction selectors; inspected; likelihood; live tag actions; missing-coordinate factor; moving comparison fields; numerical band margin; protected (sense 1 only; sense 3 stays); recording estimate; reflected normalized directions; seeded sector; support compression; tag-coincidence radius; Trace norms and recording.
- Appendix H: close the items at 6629 (output anchors), 6635 (direction selectors), 6639 (coordinatewise splice only), 6640 (compulsory), 6683 (likelihood tests), 6687 (moving comparison fields), 6688 (live tag actions, tag-coincidence radius, missing-coordinate factor, numerical band margin only), 6690 and 6703 and 6764 (padded block), 6692 (inspected support), 6710 (numerical band margin and "reflected" only), 6722 (recording only), 6723 and 6778 and 6781 (`𝒰_F`), 6726 (read-count polynomials only), 6728, 6734 (seeded sector and support compression only), 6750 and 6766 (warning), 6758, 6759, 6767.
- "How to read an entry": add the basis code **S** and the *Source* line to the description of the format.
- `blueprint/notation.md`: no line on any of these terms was found by a keyword search (seed, warning, likelihood, padded, selector, splice, inspected, compulsory, protected, `U_F`); line 213 ("recording-scale change") concerns chapter 11 and is unaffected. Nothing to change; `𝒰_F = W_F` could be added.

**Notes.**

- All twenty items of the report were entered. No finding was rejected; the cited source lines and Lean declarations were opened and say what the report says, with the qualifications below.
- **Not verified, and therefore not cited as read:** `noteAt` and `glyph` (item 12); the definition of the constant `toll r` used in `Release.compressed` (item 14; a grep for `def toll` found only unrelated declarations, and `collapse` in `YM/Corona/Spend.lean` gives the constant `((s+6)+(s+6)+1)^4 = (2s+13)^4`); `flare`, `mail`, `enforce`, `cone`, `Contract.charges`; the headers of `Stencils.lean` quoted in item 13. The `namespace` lines of the cited files were read; the report's short name `Protected` is `YM.PhysicalNext.JointLoad.Psalm.Pitch.Protected`, and `collapse` is `YM.Lattice.Corona.collapse`.
- **Small differences from the report.** (a) Item 5: the report says v3 states no radius at 6:1018; v3 does state "the retained `300B` region" at 6:1341–1350, which agrees with the Lean constant, and the entry uses it (as an inference). (b) Item 2: `YM.Push.SectorMeasure.Seeded` does not contain the positivity of the frame-tag weight; that condition is in the local form `Stores.Plot` (field `list`), read. Also, the Lean abbreviation named `seeded` in `…/RG_NEXT_COMPLETE_REPEATABLE_NONLINEAR_STEP/Islet.lean` is the *empty* selection with the actual flags, i.e. Martin's "seed-free store"; the name was not used as evidence. (c) Item 6: the threshold `ξ τ √β` in the description of `lem:warning-vanishes` was not checked and is not in the entry; the lemma is quoted only as "vanishes on the event `𝒲_{2B}(i)`". (d) Item 11: `panelSwap` takes a list of axes, not a set; immaterial. (e) Item 13: Martin's "uniform measure on `𝓑`" is at lines 96–97, not 95. (f) Item 3: Martin's "output anchor" (`actual-global-row-prices.tex:30–33`) is a coarse site, Scott's and Lean's objects for 6:90 are coarse plaquettes addressed by base site; the entry records both.
- **Observation not in the report:** in the Lean step `Calendar.op m p` the patch order (the smoothing order `j` of chapter 4, radius `(J+3)L`) is `J (m+1)`, the stage index. This is recorded in *stage* under *Across chapters*; it bears on the remark "The letter `j` is shared with the smoothing order" and on the entries *smoothing order* and *stage index `j`*, which were not rewritten.
- `𝒰_F` has no headword; it is treated inside *response*, sense 4, whose full entry is given with only that sense changed. `Inputs.primal`/`dual` were compared with (ch05:actual-transport-identities), 5:1113–1116: `K_f W = Q^* K_c` and `Q W = 1 − b^{-1} K_c` agree. The Lean matrices act on scalar one-forms; the colour-valued extension was not traced.
- *protected*, senses 2 and 3, and "normalized affine directions" were outside the report and are unchanged.
- No `lake` command was run; all Lean evidence is from reading source text at checkout `1dba6965d734bac06951579601b90e985033ee45`.

#### From the source and Lean findings, set 2

- "How to read an entry", **Basis**: add the code **S** ("not determined by the v3 text; taken from the source manuscripts or the Lean definition cited under *Source*") and describe the *Source* line.
- Book-wide word choices, row "graph": the remark "not 'remainder map'" stands; add that *graph transform* for `G ↦ ΦG` is the source's own comparison (Scott part2/E-section.tex:242).
- Appendix F, table row "graph (ch. 11, 12)": keep; the "see below" item **graph** in the list of "three identifications … suggested by a checking agent from general knowledge. No sentence of the manuscript states them and no source was consulted" is no longer of that kind: Scott's source text states the comparison with the graph transform for invariant manifolds. Move it out of the list (two identifications then remain) and cite E-section.tex:242.
- Appendix G: remove *alphabet*, *coarse forecast*, *coarse kernel level*, *corrected body product estimate*, *exterior row*, *finite decorations*, *front-column*, *Hilbert encoding*, *preselection bound*, *response bound `ε`*, *same-data restart conditions*, *selected slot*; *column* stays only if another sense of it has basis `?` (its sense 4 is now settled); *protected* stays (sense 3, protected-path errors).
- Appendix H, Letters A, B, D: remove the items **alphabet** (11:1911) and **block bridge** (10:921); **bridge legs** (7:597) keeps its question, but the object named by the label is now known to be `W` (see *block bridge*).
- Appendix H, Letters C: remove `coarse forecast`, `coarse kernel level`, `corrected body product estimate` from the list at line 6639.
- Appendix H, Letters E–H: remove **exterior row**, **finite decorations**, **front-column**, **Hilbert encoding** from the "no gloss anywhere" item (exterior row and finite decorations remain partly open: link to chapter 6 inferred; no count); replace the item **graph** ("whether the name refers to the graph transform (general knowledge, needs a mathematician)") by "'descending graph' (17m:444) inferred"; the item **forgetting the terminal graph** is answered as far as the source goes (see *graph*, Across chapters).
- Appendix H, Letters I–M: **inhomogeneous graph estimate** (11:892) remains open.
- Appendix H, Letters R: in the item "response bound `ε` (10:626), recording, replicate, 'protected' local representative: the object is identified in each case, the word is not explained", remove *response bound `ε`* (source word "response parameter", no further content) and reword for *protected* (the word names the two bounds, "protected local bounds"; why "protected" is still not stated).
- Appendix H, Letters S: remove **selected slot** and **same-data restart conditions** from the "meaning not determined" item; replace the item **site norm** by: "whether the 'rooted activity norm' of 12:178 is the anchored norm or the incidence bound; whether 'support norm' at 8:196 is the site norm (inferred)".
- Appendix H, Letters T–Z: remove "target: … not identified" (now: right-hand sides of the lift equations; limit configurations), "weight: 'encoding weights' (10:382)"; the item "terminal: whether 'the terminal graph' … is the graph at the cutoff `N` or the graph replaced at level `m+h`" should say: the graph `G_{m,N}` belongs to the history with terminal index `N`, and the one replaced is at `m+h` (Martin fixed-rung-convergence.tex:92–94, 114–121); the title itself is not glossed.
- Appendix H, Concepts with several names: replace "Whether site norm, containing-site norm, support norm, attachment norm and rooted activity norm are one norm" by the statement that they are three normalisations (see *containing-site bound*), with 12:178 open.
- Appendix B, Large-field and polymer vocabulary, row "Polymer-activity norms": "none; name each normalisation once / I. That these are one norm is not stated" should become: three normalisations, *containing-site norm* (site norm 8:69; support norm 8:196; attachment norm 9:697 at exponent `σ+1`), *anchored norm* (regular activities; remainder norm 11:362), *incidence bound* (rooted activity norm at `(ω,e)`, 11:1437); evidence Lean `YM.RG.Activities.KBound`, `EBound`. The reference "rooted activity norm (11:265–272)" in that row should be 11:1437–1440.
- Appendix B, same table, row "Sum over the terms containing a site": add that the incidence sum carries the source weight `ω^{|I|}` in addition.
- Appendix B, Operators and maps, row "The operator `W`": add "block bridge (10:921); bridge (label `ch05:actual-bridge`; 7:597)" to the words in use.
- Appendix C, Symbols used without definition, row `hot(s)`: add the formula `exp((log log s)^{3/2})` and the evidence (Lean `YM.Next.Rank.Perch.hot`); basis there R, in the entry I: unify (the line 6938 note already records this).
- Entry *column*, sense 4 ("Front-column … not determined", basis `?`): replace by a pointer to *front-column* with the inequality `‖x_m‖_1 ≤ C_{m+1}L_m^d‖x_{m+1}‖_1`, basis S; in its Variants "inverse front-column bound" stays. In sense 2, "target columns" at 11:1237 is now explained under *target* (sense 3).
- Entry *encoding weights* (pointer): unchanged. Entry *weight*: the variant "encoding weights" is now explained under *Hilbert encoding*.
- Entry *support norm* (pointer): should read "See *containing-site bound*." (already proposed at line 6877).
- Entry *site norm* (pointer): unchanged.
- Entry *attachment*, sense 2: no change of content; its *See also* could name *containing-site bound* instead of *site norm*.
- Entry *site conversion*, last sentence of *Across chapters*: add that the incidence bound of 11:1437–1440 is called "rooted activity norm" there.
- Entry *finite incidence costs*: "constants of the 'incidence' bounds of 11:208–342" can now refer to the formula in *incidence*; basis stays I.
- Entry *bridge legs* (lines 571–576) and entry *actual* (See also, line 135): "the same label underlies 'block bridge'" can now say that the object is the map `W_a`.
- Entry *forgetting* and entry *terminal*, sense 2 (not rewritten here; they belong to the chapters 12–16 report): "does not say which graph is terminal" should be replaced by the reading recorded under *graph* (Martin fixed-rung-convergence.tex:92–94, 114–121; Lean `YM.MergeProof.Matric.Gear`), keeping that the title is not glossed.
- Entry *response*, last sentence of *Across chapters* ("The phrase 'response bound' (10:626) fits none of the senses"): keep, and add "it is the source's 'response parameter', a free constant".
- Entry *kernel*, sense 3: add that the integer `J` ("kernel order", "kernel level", 11:351–352) is the averaging order of this kernel.
- `blueprint/notation.md`, table "Source wording" (lines 148–167): nothing there is contradicted; the row "primary source → Normalized local insertion" is confirmed by Lean `YM.Source.TransferData.cylinder`. Rows could be added for: bridge → the coarse-to-fine map `W`; forecast → linear prediction of the fine curvature; exposure → the map `V_d → 𝒫_d`; alphabet / letter → index set of the factors / factor; body → factors without insertions; slot → index of a large-field activity; hot → `h(s)`; front-column bound → the one-step coefficient bound; response parameter → the fraction `ε`; graph → kept, with the graph-transform sentence.

**Notes.**

- **`graph`: the two reports reconciled.** L3 states that neither source describes the object as a graph transform. That holds for Martin (existence/fixed-rung-convergence.tex:10–125, read) but not for Scott: part2/E-section.tex:242 reads "As in the graph transform for invariant manifolds, the marked step maps coefficient graphs at level `m+1` to graphs at level `m` and halves the distance between two of them" (read). The entries follow L2 on this point and take the Lean declarations (`Gram`, `Gram.step`, `Gram.Within`, `Gram.revenue`, `Gear`) from L3, each read. L3's proposed equivalent "remainder map `G`" was not adopted: it contradicts the book-wide word choice and the text's own use of "remainder map" for `R_G`, `J_G`.
- L3 cites Scott E-section.tex:137 for "common complete graph class"; that phrase is not at line 137 and a search of E-section.tex for "graph class" found nothing. Not entered.
- L3 gives `Gram.revenue` at Booths.lean:77; it is at line 74. L2 gives "the single joint warning event" at restarted-rank-history.tex:655; it is at :698–699. L2's Lean name `PhysicalGuard7f546 {sampled,forecast,wind}` is, fully qualified, `YM.PhysicalNext.PhysicalGuard7f546.Curved.*`. These are corrected in the entries.
- L2 item 1 cites Martin background-path-convergence.tex:15–47; not opened, not cited.
- L2 item 2: the Lean hit `ζ * x^(-(11/10))` in `LogQuote.lean:182` is a name-level match in the report and was not entered.
- L2 item 8: the formula `𝓔v = Σ_i v_i b_i` is not in the source and there is no Lean declaration for `𝓔`; entered as inferred. The source supports domain, codomain, injectivity and `c_d`.
- L2 item 14 (Lean "not located") is superseded by L3 (`RawProtected`, read). L3's citation "ope-filtration.tex 300–330" was checked only at :354 (title of the proposition) and :332.
- L2 item 17 (`tail events`): the mention of "failed-mask" factors in actual-local-compiler-handoff.tex was not verified and not entered; the entry keeps basis R.
- L2 item 18: that "normalized target columns" (11:1237) are the vectors `Au_j` is the report's reading; the source only says "All columns are therefore normalized simultaneously" and "on a fixed bounded target set". Entered as inferred. The correspondence of Lean `Ship.targets` with 11:2207 is likewise inferred.
- L2 item 20: the quotation from Scott E-one-mark.tex, Step 1 (`1+z(x_0 + 1_small P_d[t^{-k}x°] + …)`) and the source words "primary insertion / primary mark" were not checked and not entered.
- L2 item 21: that the "support norm" of 8:196 and the "attachment norm" of 9:697 are the containing-site norm rests on the v3 text only (no source or Lean evidence is cited for these two); kept at basis I. The identification of the "rooted activity norm" at 12:178 is not treated by the report and stays open; the entry *attachment* was therefore not rewritten.
- L2 item 7: "`d W = ψ d`" is the statement of `flow_spins` (read); the matrix `psi` and `low` were not unfolded.
- L2 item 4: `Rosin.lean:79` and `Primary.lean:183` were read at the cited lines only; which level is "coarse" in `Rosin` was taken from the neighbouring hypotheses (`rep N n m` and `rep N n (m+1)`).
- No Lean declaration was elaborated; all "read" marks refer to the source text of the `.lean` files.
- Entries added beyond the report's headwords, because the findings change them: *slot* (new sense 3), *common Gaussian*, *protected* (sense 2), *trial*, *anchored*, *containing-site bound*, *rooted*. No new headword was needed and no rename is proposed.

#### From the source and Lean findings, set 3

- "How to read an entry", bullet **Basis**: add the code **S** ("not determined by the v3 text; taken from the source manuscripts or the Lean definition cited under *Source*") and mention the *Source* line.
- Entry `comparison level`: in *Across chapters*, the sentence "'Admissible comparison depth' (14lc:23) is undefined … probably a depth allowed by the schedule (`?`)" should read: it is a comparison level whose window lies in a single stage (see *admissible comparison depth*, basis S).
- Entry `cost`, *Across chapters*: "The `q_r` of 12:247 …, the `q^site` of 13sb:24–25 and the `q` of (ch11:replicated-bound) … are one quantity by the form of the bounds (inferred)" → one quantity, basis S (Martin fullmesh-correlation-cauchy.tex:208–218; Lean `YM.Vac.treasury`).
- Entry `vacuum`, sense 2: "vacuum normalization bound" is the per-site exponent `q_m`, not a bound on `Z⁰` alone; add a pointer to *vacuum normalization bound* and note that the sources' name is "vacuum treasury per site".
- Entries `residual scalar inverse coupling correction q_m` and `rates e_i, q_i`, *Across chapters*: add `q_r` to "(`q_k`, `q^site`)".
- Entry `moment`: the variant "free row moments" (15:275, sense 1) is now explained: the free moments `G_{u}`, `G_{v}`, `G_{u,v}` of the labels of one test (see *row*, sense 8).
- Entry `compression`, *Across chapters*: "'Ground algebra' (15:155) is read as the same algebra `𝔄` …; this is R / I, not a definition" → confirmed by the sources (basis S; see *ground algebra*).
- Entry `zero-energy subspace`: may receive a *Source* line: Lean `ground := ⨅ t, ker (E t − id)`, YM/OS/Core.lean (definition read), the vectors fixed by every `E t`; Scott part2/H-section.tex:41 "the full ground space `ker H_4^OS` of the mixture, which need not be a line".
- Entry `cell census`: "in some uses the number of copies" and "I for the count" should go; at 15:261 "replica census" is the finite set of reflected copies with its allowed subsets (see *replica census*).
- Entry `source`, sense 7: delete "probably" before "the source construction" (14:186); and in *Across chapters* "sense 7 in three places" is now certain for 14:186.
- Entry `reference label`: its *See also* "reference rows; row" is misleading only if "reference" is read as "reference level"; in "reference rows" the word means free (Maxwell). A half sentence would prevent the confusion.
- Entry `graph` (other writer): its variant "terminal graph" is now explained under *forgetting* and *terminal* (sense 1). The blocks here keep the word "graph", following the book-wide table (line 47); the report's proposal "remainder map" was not used. `selected` (sense 2) says "also the graph produced by the trajectory (12:134, 139)"; this is Martin's "selected graph `G_{m,N}`" (fixed-rung-convergence.tex:93). I read `YM.MergeProof.Matric.Gram` (YM/FullVolume/Mark/Hinge.lean:12: `g : F.Coeff →ₗ[ℂ] Coin F Y c`, `toll v : ‖g v‖ ≤ a * F.coeffSize (F.core v)`) and `Gram.Within` (Booths.lean:40); both agree with the report. `Gram.index`, `Gram.recorded`, `Gram.step`, `Gram.revenue` were not reopened by me.
- Entry `protected trial` (other writer): nothing in the report's section 10 on "protected trial" was checked here. The headword `protected` is in the list of Appendix G.
- Appendix B, "Operators and maps" (line 6310): "R / I that 'ground algebra' at 15:154–156 is `𝔄`" → S (Martin phases.tex:229; phase-selection.tex:4; Lean `YM.OS.Spread.algebra`).
- Appendix B (line 6325): "That this is Wick ordering with respect to the free moments is general knowledge" → add that the sources reserve "Wick ordering" for the internal contractions of one insertion (Scott part2/E-Gaussian-sources.tex:105, 113), so the wording, if used, must be "Wick product of the insertions relative to the free moments".
- Appendix B, "Insertions and correlations" (line 6356): "reference rows" is listed as a name of the separating family; a row is one member (test) of the family, and the family is that of Scott's Lemma "Free tests".
- Appendix B, "Scales and steps" (line 6276, "selected family"): basis may be raised to S (Lean `YM.Family.Makes`, field `wilson : C.path.Selected`).
- Appendix C, row `q` (line 6476): "`q_r`=`q^site`: I, from the formulas" → S; the three names are one function of the level.
- Appendix F, table row and paragraph "corrected coefficients `R_I`" (lines 6584, 6595): "is the definition of Wick ordering with respect to the free moments" → "is the defining relation of the Wick product of the insertions relative to the free moments (identification from the formula; neither source says so, and both use 'Wick ordering' for something else)". It remains one of the items that need a mathematician.
- Appendix F, "heat semigroup" (lines 6578, 6596): add that "heat" is the sources' and the formalisation's name (Scott part2/G-section.tex:475; Lean file YM/OS/Flow.lean "Heat operators on actual GNS spaces").
- Appendix G (line 6606): remove `admissible comparison depth`, `coordinate hybrids`, `source construction` from the list of terms whose meaning the text does not determine, or move them to a list "determined from the sources (S)".
- Appendix H: close or reword the items at lines 6639 (`coordinate hybrids`), 6642 (`admissible comparison depth`), 6655 and 6779 (`q_r` = `q^site` = `q`), 6666 and 6749 (terminal graph: closed up to the remark that the source body does not use the phrase), 6673 (unmarked gas), 6675 and 6771 (ground algebra), 6719 (reference rows), 6729 (residue patterns closed; replica census closed up to its use at 15:261), 6735 ("source" at 14:186 closed; 17w:12, 78 and 11:1632 stay open), 6738 (selected at 13:395 and 13ba:30: sense 2), 6743 (spin operators), 6754 (vacuum normalization bound). Items 6648 and 6773 (Wick) stay open, with the sharper statement above.
- `blueprint/notation.md` (the file is `manuscript/HumanizeYM_v3/blueprint/notation.md`), line 150 "token, label → polynomial label with specified filtration index; distinguish from quotient field": consistent with the Lean types; a row "tag → field (element of `F_d`) with its degree" could be added, and rows for "treasury → per-site normalization exponent `q_m`", "census → finite marker set with its allowed subsets", "heat semigroup → translation semigroup `e^{−tH_μ}`".

**Notes.**

- **Quotations of the report not found as cited.** (a) "per-cell site cost" is at Scott part2/E-section.tex:362, not :117; line :44 has the relation `(a_m/a_{k(m)})⁴ q_{k(m)} = o(s_{k(m)})`. (b) The quotation "the treasury receipt … bounds the extensive bracket … by `M_m(a_m/a_k)⁴ t_k`" was not found in Martin centered-construction.tex:86–110; that range has eq. `ex-centered-sail`; the file has "`t_k` is the vacuum treasury per site at that depth" (:42) and "the treasury is the cost of all `M_m(a_m/a_k)⁴` scale-`k` cells" (:123). The entry cites what was found. (c) "`𝒯_m` is the vacuum treasury" is at actual-phase-grid-approximants.tex:126, not :124. (d) The Scott passage on the source parameters is at G-section.tex:240–243 (the report gives 234–243, which also covers the preceding inequalities).
- **`History.Selected.running`.** The Lean bound is `ε * A.S.scale m`, not "`ε·τ_m`"; entered as in Lean, `S.scale` not opened.
- **`Family.Makes`.** Read: fields `wilson`, `sections`, `stages`, `places` and the beginning of `priced`. The report's "calibrated coefficient transfers" was not confirmed and is not in the entry.
- **Terminal graph.** The report states that "terminal" means "belonging to the terminal index `N`". The source supports "terminal index `N`" = cutoff, but its body, like v3, never says "terminal graph"; the entry records the last step as inferred. The report's proposed titles with "remainder map" were not adopted (book-wide choice "graph").
- **Wick product.** Entered only as an identification from the formula, as the report itself marks it. Scott part2/E-section.tex:565 adds a formulation not in the report: "multiplication by `e^{𝖢^Max}` shows that `𝔠_I` is exactly `R_I`", which matches 11:2099 ("subtract its finite connected logarithm").
- **Labels: which chapters use which type.** The report's assignment of v3 passages (14:26, 98, 101 and chapter 15 on polynomial labels; 14:146–147 and 14:799 ff. on fields) is entered in *Across chapters* as a correspondence by the types of the Lean declarations read (`YM.OS.Future`, `YM.OS.Spread.atom`, `YM.DiffPlan`, `YM.Ward.SpinRows`, `YM.Ward.angular`, `YM.Ward.tags`), not as a line-by-line check; the *Where* list of sense 2 was left unchanged. Chapter 16 was not checked on the Lean side.
- **Not entered.** `Tiling.residue` (YM/Cells/Margins.lean): name match only. `YM.Vac.treasury_stage` as the Lean form of the bound `q_i^site ≤ C_{J(i)}(1 + log β̂_i)` of 13sb: the statement was read but not compared with 13sb. The count "`2^{4n}` coordinate hybrids" is arithmetic from Scott's definition and is entered as "at most `2^{4n}`".
- **Entries not rewritten.** `corrected coefficients`, `reference rows`, `ground space`, `cell census`, `comparison level`, `cost`, `moment`, `vacuum`, `compression`, `source` keep their text; the changes they need are listed under "Corrections elsewhere".
- **Line numbers of v3.** The lines quoted under "Damaged sentences" were read in the working copy of `/Users/mgubi/ym-terminology` and agree with the dictionary's numbering at every place checked.

#### From the source and Lean findings, set 4

- Book-wide word choices (terminology.md:41): the row "the operator `W` | *the stationary tangent*, naming the representative (`W_a` or `W_F`)" should say: *the stationary tangent* is the derivative of the stationary map, which is `W_F` in forest coordinates; `W_a` is *its smooth representative* and `W_s` *the straight-average operator*; name which of the three is meant, and do not call `W_a` "the actual tangent".
- Appendix B, "Operators and maps" (terminology.md:6321): the remark "`𝒰_F` (6:953, 976) is not identified with `W` by the text" should become "`𝒰_F` (6:953, 976) is `W_F` (Martin `local-mean.tex:11–27`; Lean `YM.Precision.extracted`); the text does not say so". The proposed single word should name three versions (`W_F` the derivative, `W_a`, `W_s`).
- Appendix C, row `W_s`, `W_a`, `W_F` (terminology.md:6489): "`W`, the derivative of the stationary substitution (17c:48–50)" is `W_F`; the remark "`notation.md`:242 … agrees on which is actual" should be withdrawn: the operator that is the derivative of the stationary map is `W_F`, so `notation.md`:242 is wrong both in "forest-coordinate" and in attaching "actual" to `W_a`.
- Appendix C, "Symbols used without definition": row `𝒰_F` (terminology.md:6522): best reading becomes "`W_F` of chapter 5", basis S; row `v_eom` (6529): basis S (Scott I:133); row `E_stat`, `E_tail`, `E_mark` (6530): replace "only bounds are given" by the four definitions of the new entry, basis S.
- Appendix C, row `E_reg` (terminology.md:6456): "Same symbol for a term and for an error bound" → "for a term (17m:107) and for the degree-five coefficient of its derivative along `Y` (17m:161; Scott's `ε_cl`, the classical defect)".
- Entry *tail*, sense 5 (terminology.md:5574): "The symbol `E_tail` (17m:161, 165) belongs here by its name" is wrong; `E_tail` is the contribution of the loop paths omitted by the truncation at `C_j(log β̂_k)²` (Scott I:362), not a Gaussian tail. Move it to a sense "omitted part of a truncated sum" or to the new entry.
- Entry *mark* (terminology.md:3180): the variant `E_mark` should point to the new entry "`E_stat`, `E_tail`, `E_mark`".
- Entry *regular*, sense 1 and Appendix H lines 6709, 6718 (regular at 17w:78): the "regular and large-field source recurrences" are Scott's (E-source-step) in the regular norm and in the normalised forced (large-field) norm; this confirms Reading A.
- Entry *stage*, *Across chapters* (terminology.md:5315): delete "'Bottom stage' (17w:97 …) may use the word for a level; not determined"; "stage" there is the regularity stage `J_k` of the lowest level `k`.
- Entry *history*, *Across chapters* (terminology.md:2536): delete "Undetermined: 'the actual free history' (17w:71)"; refer to the entry.
- Entry *threshold*, *Across chapters* (terminology.md:5677): "17m:197 'stage orders and thresholds' is not assigned to a sense" → sense 1 (lower bound on `β̂` of the stage); the proof ends "after increasing the coupling threshold" (17m:315) and "Increasing its coupling threshold makes the bounds uniform on that stage" (17m:346–347).
- Entry *`Q^pred`* (terminology.md:4162): "The superscript is never explained" can be completed: "predictor" is the source's name for the gauge-covariant block average (Scott I:162 "`Q^pred(U)` … for the predictor in that frame"; Martin `local-mean.tex:22` "`𝒬` is the rooted linear predictor"); at the linear level it is `𝒬 = M + d_{0,c}R` (Lean `YM.Precision.probe`, `YM/PREC/FrameResponse.lean`, definition read).
- Appendix D (terminology.md:6544, 6551): add the original wordings and the repairs of *Damaged sentences* items 1–3; add 17c:62 as checked and sound.
- Appendix G list (terminology.md:6606): remove *actual free history*, *admissible marked conditional integral*, *bottom*, *cross-modes*, *exterior discrepancy*, *finite momentum approximation*, *inverse source-weight bounds*, *normalized large-field majorants*, *physical mark normalization*, *polynomial-source propagation constants*, *tangent*, *with these same frames*; keep *kernel identities*; *protected* and *representative* stay only for their other senses.
- Appendix H: lines 6674 (`E_stat`, `E_tail`, `E_mark`), 6723 and 6781 (`𝒰_F` and `W`), 6739 (stationary tangent), 6748 (tangent), 6669 (equation direction), 6778 (`𝒰_F`, `E_stat` …) are answered; remove or mark as resolved from the sources.
- `blueprint/notation.md` line 242: "the actual forest-coordinate response `W_a`" → "the smooth representative `W_a`; the forest-coordinate operator is `W_F`, the derivative of the stationary map". Line 240: "`v_i^eq` … the approximate equation direction" should add that its limit `v_eom` is the kernel vector `v = (0,0,1)` of 17:171–172.
- v3 chapters (for the author, not edited): 7:574 and 17m:263 "The actual (stationary) tangent is `W_a`" → "The smooth representative of the stationary tangent is `W_a`"; 17c:48 name `W_F`; 6:953, 976 `𝒰_F` → `W_F`.

**Notes.**

- **What is established and what is inferred for `W` (17c:48) and `𝒰_F`.** Read and confirmed: the Lean definitions `mean`, `tau`, `adjusted`, `fixRoot`, `probe`, lemma `root_gradient` (FrameResponse.lean); `marked`, `straighten`, `extracted`, `books`, `centers`, `stays`, `K`, `Inputs`, `stationed`, `action` (TreeMatch.lean, with proofs); `lifting`, `tested`, `Critical`, `relative`, `Guessed` (Chart.lean); statement of `Work.F04.tangent`; `abode`, `encamp`, `camp_claim`, `encamp_zero` (Joint/Gauge.lean); `inheritJ` (Desktop.lean); statement of the private lemma `trials` (Native.lean), which concludes `Guessed F (installed …) (stationary N m p F)`; `salute`, `liftedUp`, `soldier`, `endorse`, statement of `soldier_known` (Regulator.lean). v3's `R` of (5.frame-linearization) equals `fixRoot` term by term, and `probe` is (5.actual-Q). Not read: the proof of `F04.tangent`, `Comptroller`, `PriceGap`'s use, `Forest`, `linearCopy`, `installed`, `Carrier.linesOf`, `content`, `uniformM`. The following are inferences from agreement of formulas, and the entries say so: Lean `W` (any matrix satisfying `Inputs`) = v3 `W_s`; `extracted S F W_s` = v3 `W_F`; Martin's `𝒰_F` = both; `inheritJ` = the `𝓘` of 17t:28. No declaration or sentence states any of these identities by name. Independently of Lean, v3 itself says that the derivative of the stationary graph in forest coordinates is `W_F` (5:1147–1150; 9s:188–190), so the only thing taken from the sources for 17c:48 is that the `U_stat` of chapter 17 is that forest-coordinate map (Scott I:162 with B:483 says so for its Lemma B3).
- **`protected` and `stage`** are also treated by report L1 (items 7 and 9). The block for `protected` above changes sense 3 only; whoever enters L1 item 7 changes sense 1, and the two blocks must be merged. `stage` is left to that editor; my one change to it is listed under *Corrections elsewhere*.
- **Scott line numbers differing from the report** (content confirmed in every case): stationary substitution I:162 (report: 159); (I-five-pieces) and its sentence I:358–362 (report: 354–358), `ε_mark` at I:366; "its stage constant is at most" I:98 (report: 101); second "kernel identities" I:349 (report: 334); `v_i^eq` display I:390–391 (report: 389–391); "width level `k`" E-Gaussian-sources:201.
- **Not entered or weakened.** (a) The report's repair "within the patches of `Q` and of the anchor average" for 17c:359–360: "anchor average" is not in the original or in a source line I could open; I kept "averaging patches". (b) The report's Lean citation `S.prediction U r e` (Chart.lean:78) for the group-level predictor: only a use inside `noiseTaylor` was read, not the definition, so it is not cited. (c) `YM/TraceExtension/Terrace/Base.lean` (`Gate`, `summit`, `PostT`): read and consistent with the report (`PostT.bloom`: block ≤ log β̂; `share`: columns ≤ log β̂; `purse`: `Vac.fiat ≤ (log β̂)²`), but it concerns the inputs of Step 3, not the meaning of `B_n`; not cited in the entry. (d) The report's side observation that in Lean the restarted radius is `radiusB (retime x)` and not obviously `b(x)²` (11R:18) was not checked and is not entered. (e) For *cross-modes* no source sentence has the compound; "cross" and "pushed" stay inferred. (f) For *polynomial-source propagation constants* I looked for the chapter 11 counterpart and found two candidate recurrences (11:513, 11:1643), neither in the source's form; the equation is left unpinned.
- **Nothing in the report was found wrong in substance.** One wrong line number: the display `T u = (u, Dz(0)u)` "On the forest slice" is at 17c:149–150, not 17c:109. It has the form of Scott's `W_ax v = (v, Dψ(0)v)` (B:473); I entered it in *stationary tangent* as a remark on form only, since the surrounding v3 passage was not read beyond those two lines.

- **Basis codes.** Where the v3 text alone settles the point (unit endpoints, 17m:379–380 with 467–475; the bound in *exterior discrepancy*; protected-path errors; `W_F` as derivative in forest coordinates) the code is R, with S only for what is taken from the sources.

#### From the source and Lean findings, set 5

- Entry *admissible*, sense 6 (line 163–164): remove "periods" from the list of nouns "not stated at the place of use" and from "see the separate entries for path action, periods, comparison depth" as an undetermined case; *admissible periods* now has two determined senses (basis S and D).
- Entry *anchored* (line 296): no change of meaning; add to *See also* "anchored marked support bound", whose "anchored" is this sense applied to the insertion sites (Scott `part2/E-section.tex:233`).
- Entry *block floor* (line 496): basis "I at 18gq:25 and 18lp:41" can become S for 18lp:41: the inequality `(1+2C_j) L^{−2/5} ≤ L^{−3/8}` used there is part of the same threshold as (11.calibration-floor) in Martin `marked-portfolio-calibration.tex:210–219` and in Lean `YM.PhysicalNext.Repeat.Legato.paper` (definition read).
- Entry *exceptional vacua* (pointer, line 1883): unchanged.
- Entry *height*, sense 2 (line 2495–2496): add the source line of *resolution heights* (Scott `part2/J-section.tex:222`; Lean `YM.OPE.Height`) and the general definition "height of a sequence of levels `m(T)` = `lim τ_{m(T)}/T`".
- Entry *inner barriers* (line 2633): replace "The 'numerical band margin' of 9:950 is possibly these barriers (10:212–222); the text does not say so" by "The 'numerical band margin' of 9:950 is the condition (10.drift-floor) that makes these barriers work (10:218–222); see *numerical band margin*".
- Entry *physical inclusion* (line 3825): replace "'Graded quotient comparison' (18:175) belongs with it and is not glossed separately" by a pointer to the entry *graded quotient comparison* (Proposition (18.graded-estimate), 18gq:35–48).
- Entry *prescribed set of large-field sites* (line 4033): "(11:1595–1596, where 'decay of the prescribed set' is loose; 11R:300–301)": both sentences now have a recovered meaning (Appendix D, B4 and B5).
- Entry *rate-sensitive tensor cancellation* (line 4242): no new evidence; its *See also* partner *prescribed-radius squeeze* now names two steps, not only the monotonicity argument.
- Entry *reconstruction*, sense 2 (line 4333–4334): replace the proposal "keep, define once (*projection onto `F_D` along the fixed probes*)" by "*the field of `F_D` with the same fixed probe coordinates*"; the maps are left inverses of `A ↦ A(0)`, not projections (Scott `def:D31`: "a fixed left inverse of field evaluation"; Lean `YM.OPE.Orbits.old_fixes`). This is also the correction already listed at line 6925.
- Entry *relaxed* (line 4463) and Appendix H line 6717: the conflict at 10:98 is explained as far as the wording goes: the pre-replacement text had "the relaxed small-field guard is one" (commit `4ebb64ea`), and the guard is the factor `1_{Σ_d healthy}` of Scott `part2/E-bounded-real.tex:13–17`, which tests the relaxed threshold on the stencil of the trial; it is not `χ^rel` of 4:483–487. Whether v3 intends an indicator or a smooth cutoff remains open (13ba:37 says "smooth cutoff").
- Entry *remainder with vanishing extracted coefficient* (line 4475–4478): add that "of norm `r_l`" / "of size `q`" (18lp:27, 36) is the remainder norm `𝔯 = 𝓔 + (ε^{for})^{-1/2} 𝓚` of Scott `part2/J-section.tex:24` (regular part plus large-field part divided by the square root of the large-field bound; cf. 18lp:31–32), and that the object is Scott's "`R_l` has coefficient zero" (J:45).
- Entry *source*, sense 7 (line 5198–5199): "the text the book was written from" can be named: the manuscripts of Martin (`existence/`) and Scott (`HumanizeYM_v2/`) (and Trish); for 18:411 the place is Scott Part II §J.2. 14:186 was not examined.
- Entry *unit removal* (line 5948–5952): the meaning "the property that inserting the identity field leaves the correlations unchanged" names the proved separated-point fact (Scott E1), whereas 18:430 lists unit removal among properties *not* established for the contact extension. Change the meaning to "compatibility of the extended distributions with deletion of an identity-field insertion: the extension of `S_{n+1}(1, A; x_0, x)` across the diagonals `x_0 = x_i` equals `1 ⊗` the extension of `S_n(A; x)`", basis S (Scott `part1/02-definitions.tex:190`, `part2/J-section.tex:862`; Lean `YangMills.Hierarchy.Contacts`, definition read, has no such clause), proposed *compatibility with deletion of an identity-field insertion*.
- Appendix A, line 6255: "'admissible physical periods' without definition … the identification is inferred": now two senses, the first from the sources (S), the second defined at 1:359–361.
- Appendix B, line 6279 (row "Lower bound on the block ratio"): unchanged in substance; "calibration floor" is one member of the block floor (already noted at line 6935), and the same threshold contains `(1+2C_j) L^{−2/5} ≤ L^{−3/8}`.
- Appendix D, lines 6545–6552: the items 9:893–894, 9:949, 18lp:27/36, 19:152–154, 11:1595–1596, 11R:300–301 and 10:98 now have recovered source wording and suggested repairs (section "Damaged sentences" above); 10:98 is no longer a bare conjecture as to its origin ("guard" was replaced by "smooth cutoff").
- Appendix F, line 6587 (row "exceptional vacua"): add the sentence-level equivalent "extend uniqueness of the vacuum from almost every phase to every phase" for 19:105–107.
- Appendix G, line 6606: remove "anchored marked support bound" (now S; I), "annular estimates", "bounded approximations", "forest prescription" (nested case now S), "numerical band margin", "signed local transport" from the list of terms with basis ?; keep "admissible" (other senses remain ?). "anchored marked support bound" and "numerical band margin" keep a ? for the v3 text at the place of use but have a determined meaning from the sources.
- Appendix H: line 6620 (admissible periods: what the adjective requires), line 6623 (anchored marked support bound: which result), line 6632 (annular estimates, bounded approximations), line 6678 (forest prescription "known only through `notation.md`"), line 6688 and 6710 (numerical band margin), line 6742 (signed local transport) are answered; line 6623 remains open in one respect (whether the author meant (11.higher-induction) or its use in 18lp). Line 6668 (whether 19:29–31 also covers the condition on `β̂_N`) remains open. Line 6724 (`𝒫_D` and `H_d` one map) is not settled by these findings: Lean `shadow` and Scott `P_j^raw` identify `H_d`, and 18lp:276–279 was not compared with them beyond the text.
- Appendix H, line 6914 (which of `A_d`, `B_d` is "the symmetric reconstruction" at 18:212): still open; Scott calls the pair `A_j`, `B_j` together "Symmetric projection" (`def:D32`).
- `blueprint/notation.md:206` ("the unverified sharper source forest prescription"): the Lean tree contains a formal statement of this prescription with order `(2+Σd_j)n` (`YM.Contacts.Solstice.celestial`, `MultipleLight.distribution`, `totalTestOrder`); the note should say so and say that the proof's dependencies have not been audited. It should not be changed to "verified" on the present evidence.
- `blueprint/notation.md:156` ("higher modes … Terms involving two or more insertions"): consistent with the entry *anchored marked support bound*; no change.

**Notes.**

- All source lines and Lean declarations cited in the entries were opened and agree with the report, with these corrections:
  - (10.drift-floor) reads `C_j^{drift}/log 𝓛_j ≤ min{κ_G/4, j^{−2}}` (10:57–60), not `≤ κ_G/4` as the reports L5 (B2) and L1 (item 16) write; the entry gives the full inequality and names the part used.
  - Lean lemma `found` in `YM/OPE/Height.lean:58` stands after `end Height` (line 40), so its name is `YM.OPE.found`, not `Height.found`.
  - Lean annulus is open: `e/4 < ‖x‖ < 2e`; the v3 and Scott displays use the closed annulus `1/4 ≤ |z| ≤ 2`. Not a discrepancy of substance.
  - `YM.Bid.G09` contains only the first inequality of (18.signed-transport); the second (`cost o ≤ 2(1+C_o) w`) is the separate theorem `YM.Work.G09.cost_finest`. Entered so.
  - Report B4 cites `gas ξ.era.coast τ = exp(−trib(coast.a, τ))` at `YM/MergeProof/West/Laurel.lean:51`; that line is a rewriting step inside a proof, not a definition, and `Perch.gas` was not opened. Not cited. `Opacity/Offers.lean:84` does carry the same two hypotheses (line read) but is not needed.
  - Report A11: `Doors.rate` (said to be `L^{−2/5}`) and `Bid.Credit` were not found/opened; the entry says so and takes `L^{−2/5}` from Martin only.
  - Report A13: "Only `audit/foundations-literature.md` and `audit/chapters-01-02.md` mention Lean" was confirmed by a whole-word search (the third hit is `terminology.md` itself).
  - Report A12: the pre-replacement sentence "The onto reflection comparison and the phase-uniform low-energy estimate remove exceptional vacua" is confirmed by the diff of `4ebb64ea` (the words "onto reflection comparison" were replaced; "exceptional vacua" was not touched). It concerns the words before the term and was not entered in the entry.
- v3 itself settles more than the report says in three cases, and the basis codes reflect that: *signed local transport* is the title of the subsection 18lp:24 (basis R, not S); *bounded approximations* is the title of Proposition (13.bounded-singleton) in the chapter that 19:50 names (R); the second sense of *admissible periods* is defined at 1:359–361 (D).
- *graded quotient comparison*: the report treats it only in a parenthesis (Lean not searched); both the v3 proposition (18gq:35–48) and Scott's lemma were opened, and the pointer entry was replaced by a full entry.
- *rate-sensitive tensor cancellation*: the report asserts "= Proposition `ch17:coefficient`" without new evidence; the existing entry already says this with basis I. No entry written. (Scott's proof of the trace theorem, `part2/I-section.tex:514`, does cite `prop:I-coefficient` next to the monotonicity argument, which supports the pairing but does not explain the words "rate-sensitive tensor cancellation".)
- *anchored marked support bound*: the Lean lines `YM/MergeProof/Wicket.lean:18` and `YM/OPE/Replicas/Thunder.lean:40` do contain `supportExponent − 4` on the fine side (read), but their statements were not examined and they are not cited in the entry. The correspondence of `YM.Bid.I01` with (11.separated-cover) is exact (`B·|F| ≤ 64·coverNumber`, `B ≥ 8`, separation `B²`); that of `radius_change` with 11:495–503 is by content.
- *forest prescription*: as instructed, the entry records what the Lean definitions and statements say and that the proof's dependencies were not checked; it does not say the prescription is verified. `YM/Contacts/Solstice/Result.lean` ends with the command `#print axioms YM.Contacts.Solstice.celestial`, whose output was not obtained (no build). The Scott sentence "expanding it gives forests … position-space forest formula" is at `part2/J-section.tex:677` (read), not within 665–670.
- *admissible periods*: "at least the required minimum physical period" is Martin's wording; in Lean it is `B.minLength ≤ M`, read in the proof of `Wait.engine`, while the report's separate proof obligation "`B.minLength ≤ 4(M+i+1)`" was not located as such.
- Part B: entered entirely under "Damaged sentences". The consequences for the entries *unit removal*, *relaxed*, *remainder with vanishing extracted coefficient*, *prescribed set of large-field sites* are listed under "Corrections elsewhere" and not written as entries. For B4 the form of the chapter 6 decay was taken from 11R:286–290 and Martin; chapter 6 was not opened. For B1, B3 Lean was not searched (as in the report).
- Not examined: the "Trish" manuscript; `source` sense 7 at 14:186; Lean counterparts of A4, A5, A6 (argument), A12 and of the graded quotient bound.

#### Second round, chapters 1–6

- *compensating map* (pointer entry, line 1011): "See *compensation*" → "See *compensation* (sense 2)".
- *core energy* (pointer entry, line 1230): unchanged pointer; the target now states the meaning.
- *Haar logarithm* (line 2536): basis I → R (6:1290–1291: "The fourth line follows from `log J(u) = O(|u|²)` for the Haar density in exponential coordinates"), with Source Martin `existence/actual-corrected-body-compiler.tex:162–163`; add that "frozen Haar logarithm" (6:598) is not this object but the coordinate of a frozen link.
- *padded block* (line 3787), sense 2: Martin `weighted-frame-penalty.tex:77` → `:78` (the line reads "Apply this on the enlarged block `𝓑` of radius `(J+3)L`"); `:96–97` is correct.
- *coordinatewise splice* (line 1211): the quotation is at `weighted-frame-penalty.tex:79–83` (line 78 is the sentence about the enlarged block).
- *output anchors* (line 3751): consistent with the new *anchor* entry; no change.
- *path-placement operations* (pointer, line 3865): unchanged pointer; the target sense is no longer "undetermined".
- *likelihood* (line 3041), sense 1: add Scott `part2/B-section.tex:100` ("The product of frame and predictor masses is `λ^tag(U, α_tag)`") and `:1193` ("Reference tags are independent uniform tags; their actual likelihoods are included among the factors") as source sentences for the normalisation.
- *warning* (line 6260): add Scott `part2/B-section.tex:1173` and `part2/D-section.tex:96` as the Scott form of the definition; "contraction factor" there is Scott's "inventory test".
- *cutoff failure* / *cutoff-failure event*: as already listed in Appendix H (set 1); the new *cutoff remainder* entry carries the definition.
- *row*, sense 8, and *reference rows*: add Scott `part2/E-section.tex:493–499` (the free test matrix `𝒢_{ij}` and Lemma "Free tests") as the definition of the matrix whose rows are meant.
- *residue patterns* (line 4726) and any entry citing "residue" at 5:389–390 as a position in the block: at 5:388–390 the residues are alias classes of momenta.
- Appendix B, "Not synonyms", line 6574 (`padded block`, `macro-box`): "the wording fits the patch of radius `(j+3)L`" → 7:599 is the box of radius `(j+5)L`, 7:628 the patch of radius `(j+3)L`; neither is the macro-box.
- Appendix C, "Symbols used without definition", row `r_pred` (line 6697): "A radius … ?" → "the largest coarse distance read by the block average of a coarse edge (Scott `B-section.tex:1051`); S".
- Appendix D, "Left for the author", item 10:98: move to the repairable items with the wording above; add 13ba:36 and 13ba:165 (same replacement of "guard").
- Appendix G: mark as resolved from the sources: compensating map; core energy; cutoff remainder; determinant inverse identity; fixed-position read; full maps; path-placement operations; `r_pred`; safe chart; stationary residual; sector allocation indicators; seam.
- Appendix H: close the items at 6959 (output anchors), 6975 (compensating map: the identification with the rescaling of 10:529–531 is wrong; it is the map `T_V`), 6982 (path-placement operations), 7020, 7033 and 7094 (padded block against macro-box), and in 7108 the symbol `r_pred`; in set 1 of the corrections not yet applied, the items on *anchor*, *response* (6:846), *uniform mass*, *cutoff remainder*, *fixed-position read*, *block-average patch* / *macro-box* are carried out by the entries above.
- Appendix J (record of decisions), lines 7630, 7636, 7660, 7861–7862, 7873, 7900, 7903, 8031, 8181: the statements "nothing new", "still I", "undetermined" for compensating map, path-placement, core energy, output anchors, padded block, safe chart and block-average patch are superseded.
- `blueprint/notation.md:83` (`Q_e^pred`): add that "pred" abbreviates "predictor" and that `r_pred` (6:460) is the coarse radius read by it; `:93`: the remark "clip has a jump, not a smooth cutoff" could add that `χ^rel` is an indicator, since "smooth cutoff" now stands for it at 10:98.

**Notes.**

- **unchanged: moving comparison fields** (line 3467). The entry already has a *Source* line; the one open point is the Lean statement for the particular trace label `a_i = U_i^{-1}(B_i r_i^4 Θ) → 4 d_2 O`. Searched: identifiers containing `movingLabel` / `moving_label` in `YM/` (one hit, `YM.Work.A14.movingLabels`, `YM/Work/A14.lean:137`, a private theorem; statement read: the derivative of a moment along a differentiable path of labels is the sum of the moments with one label replaced by its derivative. This is a product rule used for rotations, not the trace comparison; name match only, not entered); `Tendsto` statements with `4 * d₂` in `YM/`; users of `YM.OPE.Cards.variation` (only its own file). The directories `YM/Trace`, `YM/TraceExtension` (50 entries) were listed but not read. The point stays open as the entry says.
- **Not elaborated.** No `lake env lean` run was made; all Lean citations are of source text read (`YM/Lattice/Site.lean`, `YM/RG/Patch.lean`, `YM/Pressure/Cost.lean`, `YM/Work/A14.lean`, `YM/CellFourier/Mesh.lean` for the use of `wrap`/`lift`). No scratch Lean file was created.
- **Points settled from the v3 text alone, with the sources only confirming:** link factor (5:160–164); determinant inverse identity (6:1285–1289 against 9:126, 140–142); full maps (6:125–131, 179–182); path-placement operations (7:146–160); residual sense 4 (11:894–902); residual Gaussian density (6:659–668, 1090); "the linear response" of 19:159 (17m:190–202, 263); 5:388–390 "residue" = alias class.
- **Doubt kept in the entries.** (a) *block-average patch*: the reading of 17c:359–360 is inferred. (b) *response*: that "block average response" at 6:846 is the derivative of the block average at the actual field is inferred from the pre-replacement wording and one Martin sentence at zero background. (c) *determinant inverse identity*: which form of the "inverse identity" (difference or derivative of an inverse) Scott intends at D:162 is not displayed. (d) *padded block* at 7:628 (radius `(j+3)L`) remains inferred, as in the first round. (e) *source locations*: the Trish files are not in the checkout. (f) *anchor*: whether "output anchors" comprises only anchors of coarse terms or all anchors after projection to coarse sites is not decided by Scott's sentence; the entry *output anchors* (first round, Lean `Stores.outs`, not reread here) takes them to be coarse plaquettes by base site. (g) *cutoff remainder*: the identification of Scott's "inventory tests" with Martin's "fine site contractions" rests on the matching address (fine sites) only. (h) *fine residue*: v3 does not say which representative it uses; the centred one is the sources' choice.
- **Correction to the present dictionary found on the way.** *compensation*: the identification of the "compensating map" of 6:1540 with the rescaling of 10:529–531 (basis I) is wrong; the two are different maps. *determinant inverse identity*: the pointer to 6:1192–1203 is wrong; the right place is 6:1285–1289. *fine residue*: 5:389–390 was listed under the position sense. *full maps*: `N` was missing. *first-power*: "linear in the distance `χ`" should be "linear in the plaquette sum".
- **Citations of the first round checked and found off by one or two lines:** *padded block* sense 2 (`weighted-frame-penalty.tex:77` → `:78`); *coordinatewise splice* (`:78–83` → `:79–83` for the quoted sentences). The quotations themselves are correct.
- **Commands run (kinds):** `sed -n` on v3 chapters, Scott and Martin files around the cited lines; `grep -n -i` for the v3 words and the pre-replacement words (predictor, guard, warning, compensat, residue, seam, safe chart, regrad, spectator, likelihood, mass, padded, splice, placement, allocation, inverse identity) in `manuscript/existence/*.tex` and `manuscript/HumanizeYM_v2/part*/*.tex`; `git log -S` and `git show 4ebb64ea` on three chapter files (read-only); `grep -rn` in `/Users/mgubi/OpenAI-YM/YM` for `wrap`/`lift`, `macroR`, `frameMass`, `predictorMass`, `movingLabel`, `safeChart`, `residue`. Not checked: the Trish manuscript; Lean statements for the first-power axial bound, the safe chart, the compensated change of variables, the stationary residual bound and the free test matrix (none was looked for beyond one identifier search for "safe chart", which found nothing).

#### Second round, chapters 7–9

- Entry *inner barriers*, *Across chapters*: "The 'numerical band margin' of 9:950 is possibly these barriers (10:212–222); the text does not say so" → "is the condition (10.drift-floor) that makes these barriers work; see *numerical band margin*" (already listed in Appendix H, "Corrections implied by the source and Lean findings"; the *margin* entry is rewritten above).
- Entry *placement*, sense 4: basis `?` and "Not found under that name in chapter 7" → the placement of the curvature factors on chosen coordinate paths, 7:146–161 with (ch07:slot); basis R (7:146–161), S for the identification; *Source:* Scott `part2/C-section.tex:139` ("Fourier inversion and the placement on paths are linear too"). *Across chapters* there: "one undetermined compound in chapter 10" → "one compound in chapter 10, referring to 7:146–161".
- Entry *reflected normalized directions*, *Across chapters*: delete "'normalized affine directions' (9:35, 502) was not examined in the sources"; they are Scott's "diagonal tests `tA^{q,T_*}` and their half-sum" (D:516); see *affine*.
- Entry *normalized directions*: add to *Source* Scott `part2/D-section.tex:516` for the normalized affine directions.
- Entry *Gaussian units*: for "stationary units" add the pointer to the rewritten entry and its source (Martin `existence/stationary-exterior-receipt.tex:156–165`).
- Entry *tag average*: basis I can become "I; confirmed by S", with *Source:* Martin `existence/actual-corrected-body-compiler.tex:79–81` and `existence/gaussian-reassembly.tex:194–199` ("a single factor `|𝒯|^{-1}` … remains outside the product. This is the uniform tag average").
- Entry *exterior* and entry *exterior discrepancy*: no change; *discrepancy* sense 5 now agrees with them.
- Entry *matching*: "Quantum matching … refers to the determinant matching" is confirmed by Martin `existence/pure-action-small-field.tex:157–169` ("The finite-volume quadratic matching estimate supplies a further bound `‖D²W(0)‖ ≤ q` … This quadratic matching is a separate input from classical matching through degree four"); a *Source* line may be added.
- Entry *missing-coordinate factor*, *See also*: add *measure multiplier*, *dummy Gaussian coordinates*.
- Entry *live tag actions*, *Variants*: "tag-count factor" has its own entry (rewritten above); the remark "In 11R:358–360 'tag-count factor' is the number of values of `α`" stands.
- Appendix B (Concepts with several names): "centered log determinant" = "relative log determinant" (source) = `s(x) − s(0)` up to the factor ½; "discrepancy series" = "mask discrepancy" (Scott) = "supported discrepancy" (Martin); "thermal term" = "Gaussian contribution `T(v)`"; "reset" = "coupling correction `Δ`" at 9:748 and 10:651.
- Appendix G: remove *affine*, *centered*, *completion*, *discrepancy*, *placement*, *representative* from the list (no sense with basis `?` remains, given the rewritten entries and the correction to *placement*); *factor after deterministic subtraction* and *support compression* stay (a `?` remains for the v3 wording).
- Appendix H, open questions answered: "**affine** … in 'normalized affine directions'" (≈ line 6951; "reflected" was answered in the first round); "**adjacent pairs** at 10:30 … what is paired is not said" (≈ 6961: the stages of the two levels; "permitted" still unexplained); "`completed fine kinetic matrix` (17c:64) … likewise the content of `C_0` at 7:773" (≈ 6974 and 7000: `C_0` answered, 17c:64 gauge completion by inference); "`path-placement operations` (10:314–315)" (≈ 6982 and 7040); "**factor after deterministic subtraction** (9:124): which subtraction" (≈ 6994: answered row by row; the word "deterministic" stays open); "**infinitesimal gauge insertion**: whether `ℛ` and `d` are one operator" (≈ 7019: they are not; `d` is the fine component of `ℛ`); "**one-step integral identity** (7:859): three candidates" (≈ 7038: narrowed to the identity of the step theorem with (ch09:reset)); "formulas for `a_c`, `d_c`" (≈ 7040: `a_c = 𝒦`; `d_c = 𝓛 + α𝒬` inferred, to be confirmed).
- Entry *reset* as it stands attributes the quotation "There is a second, intrinsic way to identify the reset" to 9:597; it is at 9:748 (corrected in the block above).
- `blueprint/notation.md`: no line was found to contradict these findings beyond the one already recorded under *representative* (line 242).

**Notes.**

- Every entry of the list (29) was treated and has a block; none is "unchanged".
- Points still open after this round: (1) *adjacent pair*: what "permitted" excludes at 10:30; (2) *attachment*: whether the reserve `u_N` of 11:937 is Scott's attachment threshold `η^att` (inferred from the form of the conditions); sense 3 (17m:125) stays I; (3) *completion*: the source passage of 17c:64 was not found, so "gauge completion" there rests on the neighbouring v3 sentences; (4) *factor after deterministic subtraction*: the phrase is in neither source and "deterministic" is unexplained; (5) *one-step integral identity*: identified by inference, the phrase is in neither source; (6) *plaquette filling bounds*: the v3 passage 9s:167–180 was written for v3, the bound is not displayed anywhere; (7) *prescribed coarse classical action*: no source displays `d_c`; `d_c = 𝓛 + α𝒬` is obtained by comparing two v3 displays and Martin's quadratic matching statement, and what "reset" adds in Martin's "quantum and reset contribution" is not determined; (8) *flattening* is fixed by the source's proof, not by a defining sentence.
- "Trish" (third source manuscript) is listed in `blueprint/source-index.md` but its files are not in the checkout; it was not consulted. If "after deterministic subtraction" or "one-step integral identity" come from it, points (4) and (5) could be closed there.
- Lean was opened for one point only (the constant of *support compression*). Files read: `YM/PhysicalNext/V9_JOINT_ENDPOINT_LOAD/Heir/Fusion.lean:1–75`, `YM/Corona/Spend.lean:70–78`, `YM/Planned/ATOM_REGULAR_ESTIMATE/Geometry.lean` (line 50 and the namespace lines). No `lake env lean` run; the resolution of the name `toll` in `Fusion.lean` to `YM.Planned.AtomRegular.toll` is by reading the `open` line and by a grep showing no other `toll` with a single `ℕ` argument and `ℕ` value. A grep for `exchange` in declaration names (457 files contain the word) gave only unrelated declarations; no Lean counterpart of the lemma at 7:193–197 was sought further, since Martin states the symmetry as a formula.
- First-round evidence cited by reference and not re-opened: the Lean declarations under *numerical band margin*, *live tag actions*, *protected trial*, *representative* (sense 1). Re-read in this round: Scott D:847; Martin stationary-exterior-receipt.tex:48–61; v3 10:55–60, 212–222.
- Line numbers of v3 are those of the checkout `/Users/mgubi/ym-terminology` (commit `1a2474b3`); they agreed with the dictionary's references at every place checked except the quotation under *reset* noted above.
- Searches made (all read-only `grep`/`sed` on the three trees): the v3 words and their source variants in `manuscript/existence/*.tex` and `manuscript/HumanizeYM_v2/part2/*.tex` ("dummy", "multiplier", "deterministic", "flatten", "reset", "discrepanc", "filling", "stationary units", "tag count / tag-count / tag multiplicity", "thermal", "exchange", "fold", "completed", "adjacent", "attachment", "corrected logarithm", "coarse classical", "hole-deletion", "placement", "one-step integral"); the audit notes `09-renormalization-audit.md`, `ch07-matching.md`, `chapter-10.md`, `ch17-marked-rates.md` for the source packets; `git log -S'deterministic subtraction'` on chapter 9 (present since the first v3 commit `89c513b3`).

#### Second round, chapters 10–11

- Appendix G (terminology.md:6936): remove *column*, *leading*, *physical*, *principal*, *source*, *weight*: with the entries above none of them has a sense of basis `?` left. *numerical band margin* stays (its basis is `?` for the v3 text at the place of use, by the rule on basis codes).
- Appendix B, row "Main part of a single-insertion factor on the small-field event" (terminology.md:6535): replace the remark that "Leading" in "corrected leading coefficients" "may be the same or 'produced on the leading interval'" by: "leading" is the source's word for "principal" (Martin allarity-marked-propagation.tex:103–104, 340–341, 1878–1881); S.
- Appendix H (terminology.md:6948): "**actual free history** (17w:71): object not identified" is superseded by the entry *actual free history*.
- Appendix H (terminology.md:6969): remove `cross-modes` and "front-column" from the list of terms whose meaning the text does not determine (both have entries with basis S).
- Appendix H (terminology.md:6991): remove "**endpoint** at 11:877" (now *endpoint*, sense 6).
- Appendix H (terminology.md:6993): remove **front-column** and **Hilbert encoding**; **exterior row** now rests on the definition of the charge (see the entry), **finite decorations** stays open for the count.
- Appendix H (terminology.md:6997): "**history**: 'the actual free history'" can go; the question whether senses 2 and 3 are one stays.
- Appendix H (terminology.md:7015): remove "**inverse terminal coordinates**: whether the `X_i` of 11:1101–1102 is the terminal map": 11:1089 says `X_i = 𝖹_{N,p,e}`.
- Appendix H (terminology.md:7026): remove **moving complement** (defined by 11:1096–1099 with 11:2224–2232); **link factor** stays.
- Appendix H (terminology.md:7035): remove "**ordinary** at 10:327 … and at 11:1589".
- Appendix H (terminology.md:7056): remove **restoration levels** and **rebasing contraction** from "inferred readings, no defining sentence" (both now S); **read-count polynomials** was not treated here.
- Appendix H (terminology.md:7083): remove "weight: 'encoding weights' (10:382)".
- Appendix H (terminology.md:7099): remove "'Corrected leading coefficients' (11:1551, 1886): principal coefficients, or coefficients produced on the leading interval".
- Appendix J (terminology.md:7765, 7840): the decision "basis I, both readings stated" for *inverse terminal coordinates* is overtaken by 11:1089; (terminology.md:7688) the decision for *fixed common coefficient functionals* ("text not opened") is overtaken: 10:313–339 was opened.
- Appendix K (terminology.md:8291): row *exterior row*, Status "partly (link to the chapter 6 table inferred)" → "partly: the charge of a row is defined in the source as in v3 6:1426–1437; the numerical bound was not compared". Row *front-column* (terminology.md:8285): add that the companion bound `back` is the inverse-column bound of 11:445–446.
- Entry *front-column*: its sentence "The word 'inverse' in v3 is not in the source and is misleading" is confirmed by the Lean fields `front` / `back`; it could say that `back` is the bound of 11:445–446.
- Entry *target*, sense 3 and *Across chapters*: replaced above (the exponent is settled: 11:1363 is right, 11:1238 lacks `bd`).
- Entry *held fine reads*: "Noun use of 'reads' of chapters 3–6 … *Basis:* I" → add the source definition `I(S)` given under *local read set*.
- Entry *counting norm*: "'Counting coordinates' (11:621) is read as the same convention (inferred)" → S (Martin actual-reader-tree-covariance.tex:11–23).
- Entry *level*: "I … for the middle level" → S (Martin allarity-marked-propagation.tex:248–254); the middle level is where the source weight changes and the corrected principal terms are introduced.
- Entry *weight restoration*: add that the change of weight is made once, at the middle level `ℓ` (Martin allarity-marked-propagation.tex:263–265).
- Entry *cutoff-failure catalogue* (pointer): unchanged; its target now has a Source line.
- Entry *normalized large-field majorants*: its *See also* pointed to itself; replaced above.
- `blueprint/notation.md`: nothing contradicted. Rows could be added for: leading → principal; opening level → level `k`; middle / restoration level → level `ℓ`; tolerance exponent → exponent of the initial remainder bound; warning → cutoff-failure factor; read set → variables on which a factor depends; fusion → exact regrouping.

**Notes.**

**The three open points of the first round.**

1. *Exterior row* (11R:266). The match with chapter 6 was by position and exponent only. It now rests on a definition: the source's "ceiling charge" of an "oriented energy address" is the term `levy_j`, defined (existence/actual-harvested-owner-energy.tex:203–231) by exactly the rule that v3 6:1434–1437 gives for the energy assigned to a selected component: each action row counted once, the affine square subtracted at selected rows, nothing subtracted at unselected rows, the extracted mean squares kept with positive sign. The identity `eq:owner-ceiling-identity` is v3 (ch06:component-extracted-energy), with the same four terms. "Exterior" charges are those of the rows not assigned to an owner (selected component), i.e. chapter 6's "remote nonlinear action remainders" and "remote extracted mean squares". Still open: the two other items of 11R:266 (determinant, Haar) are matched to the table of 6:1253–1256 by name; and I did not check that `y^{-1/4+o(1)}` is the chapter 6 bound at the recording parameter `y`. The updated entry *exterior row* is among the blocks above.
2. *Finite decorations* (11R:304). No formula for the count was found: the only quantitative statement is "their logarithms per seed are `O((log log s)² + log B)`" (Martin existence/restarted-rank-history.tex:657–660), the same in v3. What can be added: the neighbouring "local counting costs" of 11R:304 is the source's "packet count `H_B D_B^{2r}`", with `H_B = (2(ℓB+1)+1)^4 T_L`, `D_B = (4(ℓB+1)+1)^4 T_L` and "at most `H_B D_B^{2n}` packets of size `n` containing a fixed site" (existence/mixed-activity-prices.tex:33–55), so that the decoration cost is a separate factor; and the one passage that says what a decoration of an owner is (existence/actual-corrected-body-compiler.tex:346–351: "Each owner decoration is required to equal the fine flags in its assigned region, so exactly one decoration survives for each owner") gives multiplicity one on the configurations considered. The Lean tree has about 30 lines containing "decorat" in 17 files; none was opened. The entry *finite decorations* is left as it is.
3. *Exponents `H^{c_d}` (11:1238) and `H^{bd+c_d}` (11:1363)*. Source and Lean agree on `bd + q_* + 2`, with `q_*` the largest factor ("connection") degree of a basis element of the frame: Martin existence/allarity-coordinate-calibration.tex:232–243 derives it (`|Tu|_1 ≤ (2H)^{q_*} r^d |v|_1`, `r = H^b`), existence/actual-rank-purchases.tex:1027–1029 uses it for the Taylor order (`D > bd + q_* + 2 + v`), and Lean `YM.Next.Rank.Atlas.income` states `H · ‖Au‖ ≤ H^{b·d + saves}` with `saves = leash + 2`. v3 11:1363, 1842–1843 ("Choose `b` larger than `c_d+3`"; the source has `b ≥ (q_*+2)+3`, allarity-coordinate-calibration.tex:259) and 11:1925 are consistent with this; 11:1238–1239 dropped `bd`, which also makes its Taylor order `D > c_d + v` too small as written. The Lean lemma was read as a statement; `Price.Solves`, `Tested` and `coeffSize` were not unfolded. Entered in *target* (block above) and noted in *column*.

**Unchanged entries.**

- *reserve* (terminology.md:4683): unchanged. What it leaves open is only that the word has no definition and that the reading of 9:34 through 10:737–739 is inferred. Searched Martin for a defining sentence ("a reserve", "reserve means", "called … reserve"): none; the source uses the word in the same loose way ("Choose a target support exponent `a ≥ 0` and a reserve `η > 0`", existence/high-degree-cluster-prices.tex:188). Scott part2/D-section.tex has 25 occurrences, not opened one by one.
- *same-data restart conditions* (terminology.md:4936): unchanged. The remaining "I for the identification with 11R:19–23, 43–45" could only be removed by a v3 sentence naming the conditions; none exists, and no Lean declaration was sought.

**Points still open inside rewritten entries.**

- *column*: whether the bound of sense 1 is always an `ℓ¹` operator-norm bound (the Lean `coeffSize` was not unfolded); the uses at 17w:11 and 17m:428.
- *fixed common coefficient functionals*: no sentence defines the phrase; the identification with the maps of 10:313–316 rests on the audit note and on the sources.
- *opening*: `B_m²` (13ba:127) against `B_j²` in the source lemma.
- *physical*, sense 9: 6:957 by inference; 6:1372 not reread.
- *principal*, sense 5: "principal resolvent identity" (6:1494) and "principal real cube" (7:704) remain inferences from the v3 text; the sources were not searched for these two (chapters 6–7 are outside this list).
- *protected trial*: why "protected"; the field `scale` behind `Slow`.
- *restoration levels*: the plural.
- *row*: 7:1059 "the prescribed coarse quadratic row" (searched Scott part2/C-section.tex and Martin for "quadratic row", "coarse quadratic": no matching sentence); whether the matrices of 13:168, 182 and 14:277 use the family of tests of sense 8. Not treated further.
- *incidence*, *rooted*: no Lean declaration for the sum over the terms containing a given insertion was located (not searched beyond the first round).
- *label*: the undecided places between senses 1 and 2 (13:282–285, 18lp:295, 14lc:7, 13sb:176, chapter 18) were not reopened; only 14:238, 250 was settled.
- *request*, senses 2 and 3: no source definition sought; Martin existence/trace-firesky-gallery.tex:1668 ("Fix a finite request: grades and arities at most `d`, a compact …") has the sense-2 use.

**A correction to my own first reading.** I first took the "front-column bound" for the bound on the inverse of the one-step coefficient map (the `s_f` of 11:445–446). The Lean structure `YM.Source.TransferData.Based` has both: `back` is that inverse bound and `front` the forward one with the extra factor `L_m^d`; the first-round entry *front-column* is right, and *column* sense 4 was written accordingly.

**Commands run.** `grep`/`sed`/`awk` on the v3 chapters, on `manuscript/existence/*.tex`, `manuscript/HumanizeYM_v2/part{1,2}/*.tex`, the audit notes and `blueprint/notation.md`; `git log -S'restoration levels'` on chapter 11 (first v3 commit only); in the Lean tree, `grep -rn` for identifiers and reading of YM/RG/Activities.lean:1–101, YM/Shoot/Reach.lean:55–92, YM/Shoot/Criteria.lean:60–66, YM/Next/SCHEDULE/Dues.lean:90–104, YM/Push/RELAY_DIFFERENCE/RawTop.lean:1–40 and Rates.lean:37–69, YM/Lane/Lease.lean:1–40, YM/Next/RANK/Matrices.lean:20–62, 100–135, YM/Next/RANK/ParticleGate.lean:20–60, YM/Next/RANK/Reign.lean:20–26, YM/Source/Insertion.lean:88–100. No `lake env lean` run, nothing built or elaborated; no scratch Lean file was needed. Lean checkout `1dba696` (pinned revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464` plus CI files).

#### Second round, chapters 12–16

- `#### complementary` (line 1025), *Across chapters*: "'Complementary profile' (13ba:165, undefined) is the large-field part of a term" should read: "… is the large-field profile of the term linear in the sources of an inserted trial; it vanishes for a trial defined as cutoff times polynomial (13ba:165–166)".
- `#### complementary profile` (line 1036): pointer unchanged.
- `#### total response` (line 5905): "The text says 'response', not 'flux'" is true of v3 but the source calls the same quantity "the total angular flux of the raw charges" (Scott part2/G-section.tex:661). The meaning should be stated as "the angular sum `Ang_K` (left side of (ch14:line-ward)), written as the integral `−∫∂_μV_c S(J_{μc},A)`"; add a *Source* line with Scott G-section.tex:656–663, 677 and Lean `YM.Ward.angular`.
- `#### response`, sense 10 (line 4739 ff.): "Not *flux integral*: the text calls it a response, and 'flux' is not its word" should be weakened: in the source both words are used for it ("total angular flux", "angular and positional shell responses", G-section.tex:661, 677). Proposed: *the angular sum (ch14:line-ward)*.
- `#### flux` (line 2277), last sentence of *Across chapters*: same remark; add that the title 14:708 "Vanishing angular flux at infinity" uses "flux" for this integral.
- `#### physical line` (line 3938): add `*Source:*` Martin existence/actual-stress-normalization.tex:138 ("The physical conserved line"; "reference and physical tables"), Lean `YM.Next.UVStress.differential_rank`; *Where* should not list 14:258 and 14:1019 as occurrences of "physical line" (the phrase is at 14:306 only; 14:258 is "conserved stress line", 14:1019 "centered conserved line").
- `#### orientation of the line`, *Where*: the phrase occurs only at 14:306; the list "14:258, 293–294, 308, 1019" is that of the group "conserved stress line".
- `#### angular boundary`, *Where*: 14:358 does not contain the term (it is in the proof of the flux representation); the occurrences are the titles 14:410 and 14:708.
- `#### terminal` (line 5769), sense 1: add after "(see *forgetting*)" that no object named "terminal graph" exists in the formal source: `Gear.shawls` replaces the graph at level `i+d'` by one independent of the cutoff index.
- `#### graph` (line 2479), *Across chapters*: "`TwoFold` not unfolded" can be replaced by "`TwoFold` (definition read): the Cauchy property in the relation `Within`"; and "The remainder space `Coin` … not unfolded" by "`Coin` (definition read, YM/FullVolume/Mark/Purse.lean): the space of arrays with a finite bound, with the seminorm `ticket f = sInf {v | Pay f v}`"; `F.core` remains unopened.
- `#### stopping` (line 5569): add to sense 2 a *Source* line: Scott part2/E-several-mark.tex:188, "A stopping pair is a pair of levels `m ≤ k` with `B_k² ≤ a_m/a_k`".
- `#### admissible path action` (line 189): remove the variant "admissible path-action representation (13sb:27)"; it is sense 7 of *admissible* (a representation of the density, not an action).
- `#### seeded sector` (line 5074), last sentence: "(auxiliary random variables)" can be made precise: "(the random variable choosing the frame at a coarse site)".
- Appendix B, row "Correlation function" (line 6531): "'support moments' (18lp:177)" is no longer unexplained; and `M_{N,p}` is `M^lat_{N,p}` of 1:341–343.
- Appendix C, "Symbols used without definition": `M_{N,p}` (12:262) is defined at 1:341–343 as `M^lat_{N,p}`; the entry should say "superscript dropped".
- Appendix G / Appendix H (line 7018): remove "support moments (18lp:177)" from the list of terms without gloss; remove "orientation of the line" and "barycenter identity" if listed.
- Appendix F ("three that need a mathematician"): the item on `R_I` should carry the two qualifications stated in *corrected*: the reference moments are the free ones, so `R_I` is not centred under the lattice measure; and none of Scott, Martin, v3 or the formal source uses "Wick" for it.
- `blueprint/notation.md` line 153–154 ("flag / inventory", "forced activity"): add "forced profile → large-field profile" (source: Martin existence/fixed-rung-convergence.tex:20, 219).

**Notes.**

Formal source: checkout `1dba696` of /Users/mgubi/OpenAI-YM, i.e. revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464` plus CI files. Declarations were read as source text; nothing was elaborated (`lake env lean` was not run) and nothing was built.

The four open points of the first round.

1. *Corrected coefficients and Wick products.* Treated in *corrected*. What the Lean definition computes: for a finite set `I` of slots and a lattice configuration `U`, `corrected I U = ∏_{i∈I} X_i(U) − G_I − Σ_{∅≠t⊊I} G_{I∖t} · corrected t U`, where `X_i` is the lattice insertion in slot `i` and `G_s` is the correlation of the free ("Maxwell") fields with the given labels in the slots `s` at the rescaled points (identity fields elsewhere, so `G_∅ = 1`). Names: Scott "relative errors" (E-section.tex:508) and no name in G-section.tex:279–285; Martin "invoice" for the density after "subtraction of its prescribed free connected coefficients" and "corrected coefficient" (actual-rank-purchases.tex:152–154, 281); v3 "corrected coefficients" (11:2065). "Wick" is used by all three texts for (i) the ordering `:π:_C = e^{−Δ_C/2}π` of one insertion with respect to its internal contractions (Scott E-Gaussian-sources.tex:105, 113; E-section.tex:521; v3 3:101) and (ii) Gaussian expectation by pairings (Martin "Wick evaluation `𝒲_{Q,μ}`", allarity-cumulant-comparison.tex:17–22; v3 "Wick's rule"). No text and no Lean docstring calls `R_I` a Wick product. The decision left to a mathematician is only one of naming: the formula is the squarefree case of `:e^{Σ z_iX_i}: = e^{Σ z_iX_i}/E e^{Σ z_iX_i}` with `E` replaced by the free moment functional; the caveat is that the moments are those of the limit, not of the lattice measure.
2. *"Forgetting the terminal graph".* Treated in *forgetting*. Martin: the phrase is only the title (fixed-rung-convergence.tex:92); the body has "the selected graph at scale `m` in the history with terminal index `N`" and replaces `G_{m+h,N}`. Lean: `Gear`, `Gear.shawls`, `Gear.voyages`, now with `Club.flow`, `TwoFold`, `Ritzy` opened. The other "terminal graph" in Martin (terminal-normalization-transfer.tex:211, "The new terminal graph need not have the old graph's complete analytic expansion") is the stationary graph at the terminal step of a different construction and is unrelated.
3. *"Conserved line" at 17:341.* Treated in the new block *conserved line* and in *orientation of the line*. What is proved at 14:258–308 is surjectivity of the divergence `𝒦 → 𝒱` and `dim ker = 1`, then the choice of sign of a generator. The statement is conditional on the comparison maps and on the free rank computation (explicit hypotheses `FreeDiv`, `Approaches`, `Stable` in Lean `differential_rank`).
4. *"Rooted activity norm" at 12:178.* Treated in the new block *rooted*: it is the pair of norms of (ch04:weighted-sums). There is one occurrence at 12:178; the neighbouring "rooted majorant sums" (12:236) is the insertion-rooted normalisation.

Entries of the list not rewritten.

- *spin operators* (line 5432): unchanged. The entry has its source; I re-read `YM.Ward.SpinRows` and `YM.Ward.angular` (YM/Ward/Sum.lean) and they say what the entry says. Nothing remains open except that v3 does not use the name before 14:903, which the entry records.

Limits of what was done.

- *comparison*: only the comparison maps were given a definite referent; the bare word stays generic. `Spin.change` was read (`(comparator L).Field d ≃ₗ[ℂ] S.Field d`); `Approaches` was not opened, so the precise mode of convergence in Lean is not quoted; the entry takes it from 14:201–204.
- *admissible majorant*: the Lean predicate `Pay` and the subspace `tent` were not opened; their content is inferred from the proof of `posture`.
- *shared frame seed*: no source-manuscript sentence and no Lean declaration; the reading rests on 13ba:229–248, 4:217–219 and the v3 audit note. The 780 Lean files containing "seed" were not searched (the word there names large-field selections and other things).
- *support moments*: the Martin passage gives the estimate and the phrase "polynomial moment"; that 10:603 and 18lp:177 descend from it was not established (Scott J-section.tex:280, the source of 18lp:170–180, lacks the phrase).
- *sparse stopping scale*, *Haar-ball normalization argument*: Lean was not searched; both are settled by Scott's text and v3 chapters 11 and 13.
- *complementary profile*: reading from the v3 context and `audit/ch13-bounded-residual-supplier.md:25`; Scott part2/E-bounded-real.tex has no corresponding sentence and Martin existence/selected-centered-service.tex was searched only for "forced profile" (lines 101, 2056–2074), where the forced part is a component of a coefficient family.
- *rooted* (c): `YM.Extra.Multi.Rooted` matches the formula of the insertion-rooted sums; I did not trace a theorem connecting it to the statement at 12:236–240.
- *angular boundary*: `M4.move` was not opened.
- A name collision to keep out of the dictionary: Lean `DiffPlan.Orientation` (compatibility of derivative maps with conjugation and reflections) has nothing to do with "orientation of the line".

Commands run: `grep`/`sed`/`awk` on terminology.md, the v3 chapters, `manuscript/existence/*.tex`, `manuscript/HumanizeYM_v2/part1,part2/*.tex`, the v3 audit notes and `blueprint/notation.md`; `grep -rn` on /Users/mgubi/OpenAI-YM/YM for definitions (`Rooted`, `SumBudget`, `EBound`, `Coin`, `ticket`, `TwoFold`, `Club`, `Gear`, `KernelSpace`, `currentDiv`, `differential_rank`, `produce_current`, `Scaling`, `ground`, `barycenter`, `angular`, `corrected`) followed by reading the files cited; one `git log -S'complementary profile'` on the v3 chapter (only the initial commit). No scratch Lean file was needed.

#### Second round, chapters 17–19

- Entry *rebasing contraction* (terminology.md:4427–4431): replace "Presumably the contraction property …", basis I, by the statement with basis S and the source Scott `part2/E-one-mark.tex:102` (quoted in *contraction*, sense 1). Appendix H line 7056 lists it as an inferred reading; remove it there.
- Entry *safe chart* (4929–4934): "The phrase itself is not defined" holds for v3 only; add the definition of Martin `existence/stationary-exterior-receipt.tex:88–91, 111–118` (closed ball of radius `r_s` in the combined coordinates), basis S for the set, and "common safe chart" (`:81`).
- Entry *live group* (3075) and entry *tag* (5700): the sentences calling "live tag actions" undetermined are contradicted by the entry *live tag actions* (3078–3082); already listed at 7292. In addition, the meaning "not yet merged" for "live" in *live group* and *group* (2511) is replaced by "of positive weight" (Scott J:224); Appendix H line 7023 can be closed.
- Entry *forest prescription* (2322): "Not opened: `majorKernel` (so the link between `distribution` and the recursion `full` was not traced)" can be replaced by the finding in Notes, point 2: `majorKernel` is the correlation reading of `(waySystem P M o d t).full P s` on the trivial partition, so `distribution` is a statement about the recursion; and the sentence on dependencies can be completed by the import facts given there. Entry *source prescription* (5378–5380): no change of meaning.
- `blueprint/notation.md:206` ("the unverified sharper source forest prescription") and v3 18:418–421: "unverified" is true of the v3 text; the formal source states the corresponding theorem and derives the public clause `YangMills.Hierarchy.Contacts` from it (Notes, point 2). Whether v3 wants to say so is an editorial decision; the dictionary should not repeat "unverified" as a fact about the construction.
- Entries *actual stationary tangent* (134) and *stationary tangent* (5539): "No Lean declaration corresponding to `W_a` was found (not searched exhaustively)" can be made precise as in Notes, point 4: the identities (5.actual-transport-identities) are proved in Lean for the forest representative (`YM.Precision.stationed`), and no smooth extension operator was found among the declarations that use `fixRoot`, `probe` or the words searched.
- Entry *propagation constants* (4040–4042): "citing the chapter 11 recurrence by number" can now name it: (11.lower-weighted-step), 11:1566, and the leading recurrence 11:1541–1544 (proved 11:1643); see *regular*. Appendix H line 7048 (regular at 17w:78) and the pending item at 7414 are settled in the same sense, with the equation identified.
- Entry *comparison level* is rewritten above; the pending correction at 7370 is thereby applied.
- Appendix G (line 6936): remove *anchored marked support bound* and *kernel identities* from the terms the text does not determine (now S / I); *contact* and *group-coordinate contact identity* stay only for the reason for the word.
- Appendix H: close 6953 (anchored marked support bound), 6964 (defect Ward identity: v3 17c:16, 52–53), 6989 and 7087 (frames at 17w:122: the maps `U_{i,d}`, Scott I:109, 111), 6995 and 7034 (fixed probe order: a third sense, Martin trace-row-jet-estimates), 7021 and 7041 (`k_i = k(n_i)`: Scott I:109; output level of chapter 17: the fixed level `k` of Scott I:213, not `w`), 7054 (`𝒫_D = H_D`: v3 18r:4–7, 60–61), and the item for *kernel identities* announced at 7220.
- Appendix B, "Not synonyms" (6561 ff.), if "exterior word" and "spectator word" are listed there as one concept: exterior points may approach the cluster (Scott J:400, 730; v3 18:250–253), spectators are at fixed distance.
- Appendix C (symbols with several meanings): add `k` (volume index in the ordered limit of 13:46; level in chapters 11 and 17) if not present; the two meet in 17m:338.
- Entry *first-below scale* / *overshoot* (not opened): if they repeat that the crossing quantity at 17w:31 is unnamed, the quantity is `log(a_m/a_n)` (Scott I:91).

**Notes.**

**Unchanged entries.**
- *low-coordinate errors* (3206): unchanged. Nothing is open; the entry already determines the term from 18r:36–39 with 18lp:318–322 (text reread, it says what the entry says). It was listed because of the word "undetermined" in "Not undetermined".
- *prescribed-radius squeeze* (4135): unchanged. The one open point is the Lean form of the monotonicity argument. Searched: uses of `YM.TraceExtension.EuclideanAsymptotic` (it appears as hypothesis `ht` in `YM/TraceExtension/LogScaling.lean`, `Dyadic.lean`, `Wick/Palette.lean`, and as a structure field `shortDistance` / `at_length` in `YM/Integration/ManuscriptTraceTests.lean:70`, `YM/TraceExtension/Endpoint.lean:118`, `YM/TraceExtension/Belfry.lean:23`); the declaration that proves the field was not located, so the argument remains unlocated in Lean.

**Point 1, kernel identities.** Decided for the block-kernel identities of 17m, on three grounds from the v3 files: 17m proves (17.transfer) by (17.kernel-divergence) and its integrated forms (17m:150, 396–398, 443, 459); `grep` for `block-algebra` in the chapter 17 files gives only 17t:39, 68 and 17c:293, none in 17m; the labels and the chapter note call the 17m identities "kernel" identities. Scott's use of the phrase for the Laurent identities (I:184, 349) is real but belongs to the passage rendered in 17t. A third family, Martin's "exact identities of the original transport kernels" (`existence/kernel-transport-identities.tex:1`), supplies the polynomial response used in the proof of the low-moment proposition (17m:201–249, per `audit/ch17-marked-rates.md:69`); it sits inside the "separate low-moment estimate" and is not what the sentence lists first. Residual doubt: the sentence gives no number, so this is a reading (basis I), not a citation.

**Point 2, the forest prescription in Lean** (revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; files read as text, nothing elaborated or built).
- What is defined. `YM.Contacts.Normal.System` (`YM/Contacts/Score/Formula.lean:31–53`): for a subset `g` of the `k` slots, `degree g = Σ deg`, `relative g = 4(|g| − 1)`, `depth g = degree g + 1 − relative g` in ℕ (so `max(0, ·)`, Scott's `L_h`); `subtractAt g F = −Σ_{w < depth g} reshape(reader g w) F · taylor (normalOn P g) s (depth g − 1 − w)`; `cumulant g` = the field with trivial test operator if `|g| < 2`, else `subtractAt g` of the sum over proper partitions of products of cumulants (`receding`); `punctured`, `full = totalForm cumulant` (sum over all partitions), `full_formula : full g = punctured g + cumulant g`. `taylor K s m = mask (window K s) ∘ jet K m` (`YM/Contacts/Normal/Subtractions.lean`): cutoff in the normal variable at length `s` times the Taylor polynomial of order `m` in the normal variables. This is Scott's (`eq:J-contact-recursion`) and (`eq:J-normal-Taylor`) term by term.
- What is stated. `YM.Contacts.Solstice.MultipleLight.distribution` (`YM/Contacts/Solstice/Result.lean:60–62`): for an isometric parametrisation `P` whose range contains the plane of `g`, a configuration `o` collapsed on `g`, degrees `d`, labels `t`, a state `α`, `B ∈ (0,1]` with `B ≤ M.clearance(Σ d_i)` and `0 < s`, `2s ≤ B`: `Charge (majorKernel P g M t α o s) ⊤ (totalTestOrder d g)`. Here `majorKernel … x = (readExpr M.basis (spectator Z α)) ∘ (Normal.under x (parcel ((waySystem P M o d t).full P s) (root g)))` (`YM/Contacts/Solstice/Venue.lean:59`; definition read): the correlation, in the state `α`, of the fully subtracted expression `full` of the system `waySystem` (degrees `d`, fields `insertField` at the points `P x + o`, reader `M.insertRow` at the centroid; `YM/Contacts/Harvest/Yield.lean:39–40`), applied to a test function at the point `x`. `Charge P U n` (`Venue.lean:30–31`): for every compact `K ⊆ U` there is `C > 0` such that for every smooth `p` supported in `K` whose derivatives up to order `n` are bounded by `m` (`Jet`, `YM/Contacts/Normal/TestRates.lean:18–20`), `x ↦ P x p` is integrable with `∫‖P x p‖ ≤ C m` (`Dust`, `YM/Contacts/Harvest/Absolute.lean:20–22`). `totalTestOrder d g = (2 + Σ_j d_j)·|g|` (`YM/Contacts/Solstice/Skies.lean:48`), Scott's local order `(2 + |A|_deg) n`. So the statement is: the forest-subtracted expression is absolutely integrable against test functions on all of configuration space, including the diagonals, with local order `(2+Σd)·n`. `MultipleLight` has two further fields, `slope` and `moment` (shell and partial-collision estimates; their structures `Sunshine`, `Resolution` were read only as statements).
- How it is proved and used. `provided` (`Result.lean:65–69`) derives `MultipleLight Z M` from `M.rotation = Z.sector.turns` and `H : OPE.Services C F S`, the `distribution` field by `global_charge` (`Venue.lean:62–63`, which calls `glues_total`, `Skies.lean`). `celestial` (`Result.lean:78–79`) states the existence of a family with `MultipleLight`, a real basis and thresholds. `YM.Nonperturbative.contacts_on` (`YM/Nonperturbative/Continuum.lean:14–24`) builds the devices `M` from the OPE reader `Q` (`M.basis = Q.port`) and applies `provided` to the same `OPE.Services` that the operator product expansion uses. `YangMills.contactDistribution` (`ContactBridge.lean:14–45`; statement and proof text read) applies `distribution` with `g` = all slots, `o = 0`, `B = min 1 (M.clearance(Σ d_i))`, `s = B/4` (Scott's `r_* = min(1, δ_W^pres)`, `s_* = r_*/4`) and shows that the resulting continuous functional equals `∫ f · S` on test functions supported in the separated configurations; this is `YangMills.Hierarchy.Contacts` (`ContactSpec.lean:12–14`), one of the clauses of `YangMills.constructed` (`Construction.lean:16–41`).
- Does the main result depend on it. The comparator statement `YangMills.JointExistence` (`ChallengeSpec.lean`, end of file) asks for `WilsonRegularity` and `Hierarchy.Properties` = convergence, reconstruction, operator product expansion, trace test; it has no contact clause. `Solution.lean` proves it from `YangMills.constructed` and discards the contact clause (`obtain ⟨q,S,F,L,Q,M,X,core,_⟩`). The modules under `YM/Contacts` and `YM/MultipleContact` are imported, outside those two directories, only by `ContactBridge.lean`, `YM/Nonperturbative/HeadlineSpec.lean` and `YM/Nonperturbative/Continuum.lean` (grep on `^import`); `YM/Independent/Core.lean`, which carries reconstruction, trace and OPE, imports none of them. So the four conclusions of the main theorem do not use the forest prescription; the proof term of `jointExistence` passes through `constructed`, which also proves the contact clause, but nothing in the four conclusions is derived from it. In the other direction, the contact theorem depends on the OPE hypotheses (`OPE.Services`).
- Not established. No `#print axioms` was run (the file `Result.lean` ends with `#print axioms YM.Contacts.Solstice.celestial`, whose output I did not see); a text search finds no `sorry` and no `axiom` line under `YM/Contacts`, `YM/MultipleContact`, which says nothing about their imports. The proofs of `glues_total`, `patch_need`, `any_power`, `summers`, `collars` were not read. `M.row` (hence the identification of `insertRow` with Scott's `P_{=q}^ct`), `readExpr`, `spectator`, `insertField`, `Normal.under`'s helper `action` beyond its formula, and the hypotheses `Run`, `Given`, `Authority`, `Eligible` were not opened. Whether Scott's hypotheses of Lemma `lem:J2.2` and the Lean hypotheses coincide in detail was not compared. So: Lean contains the forest recursion as a definition and a theorem about it that is used to prove a public clause; that this theorem is free of unproved assumptions is unverified here.
- Consequence for v3. The sentences 18:418–421 ("A one-shell estimate alone does not verify that stronger forest prescription. We have therefore used the fully specified pair-weighted subtraction"; since 25 November 2026 "It is formalized but not used in the main result: we use the fully specified pair-weighted subtraction") describe the v3 text correctly, and the v3 main theorem, like the Lean `JointExistence`, does not need the contact extension. The statement in `notation.md:206` that the source prescription is "unverified" does not describe the formal source.

**Point 3, the "source recurrence" of 17w:78.** It is (11.lower-weighted-step), 11:1566, together with the leading recurrence 11:1541–1544 (proved at 11:1643), not (11.higher-induction), 11:513. Evidence: Scott I:98 cites (`eq:E-source-step`), whose form `S_i ≤ K S_{i+1} + 𝓜^{1/2} S_{i+1}²` is that of 11:1566 with `𝓜 = H`; 11:513 has neither the quadratic term nor a power of `H`. Entered under *regular*. The candidate "11:1643" of the first round is the sentence that closes the proof of the upper recurrence; the display itself is at 11:1541–1544.

**Point 4, Lean counterpart of `W_a = W_s − d_f E R W_s`.** None found. What exists (namespace `YM.Precision`, definitions and statements read): `fixRoot S` (`YM/PREC/FrameResponse.lean:63`) is `R` (`adjusted S x center`, with `tau` the negative averaged path integral, lines 57–61); `probe S = mean S + d 0 c * fixRoot S` (line 68) is `𝒬 = M + d_{0,c}R`; `root_gradient` (line 92) is `𝒬 d_{0,f} v = d_{0,c}(v at block roots)`; `straighten S F W` (`YM/PREC/TreeMatch.lean:21–24`) is the fine site potential `x ↦ ∫` of `W a` along the forest path from `x` to its root, minus `(R W a)` at the block of `x`; `extracted S F W = W + d 0 f * straighten S F W` (lines 26–27) vanishes on tree links (`stays`) and has potential `−R W a` at the roots (`centers`); `stationed` proves `probe * extracted = 1 − b⁻¹K_c` and `K_f * extracted = probeᵀ K_c` from `Inputs` (`K_f W = meanᵀ K_c`, `mean W = 1 − b⁻¹K_c`). So Lean corrects `W_s` by the gradient of a potential that extends `−R W_s` from the block roots to the block along the forest (piecewise, through `parent`), which is v3's forest representative `W_F`, and proves for it the first two identities that v3 states for `W_a` in (5.actual-transport-identities). A smooth cardinal extension `E` (5:1093–1106) was not found: no definition among the 32 files using `fixRoot` was seen to interpolate (file list read, the files `PREC/*`, `Push/LOOP_COEFFICIENT/Column.lean`, `Push/FREE_RESOLVENT/GaugeProjection.lean` opened), and searches for `cardinal`, `interpolat`, `partitionOfUnity`, `smoothRep`, definitions named after `Rooted`, `tangent`, `extension` gave no candidate. Not checked: the other 28 files using `fixRoot`; `YM/RG08/Line/Hikes.lean` (`gaugePin = 1 + d 0 f * hikeMap`, `gaugeFrame = d 0 f * padMap`, names seen, bodies not read), which may contain a variant. The chapter note `audit/chapter-05-actual-matching.md:15` records `W_a` as introduced in the v3 chapter ("Identified a smooth actual-predictor transport"), on the model of Scott's `W_r` (B-section:386–390).

**Other remarks.**
- *contact projection*: the present entry's reading ("operators attached to nested subsets" for child / parent) was right for the Taylor operators but the projection itself was not identified; it is a defined object in Scott (`def:D36`–`def:D38`).
- *exterior*: the proposal of the present entry (replace by "spectator word") is withdrawn in the rewritten entry, because the source distinguishes the two and v3 18:250–253 uses the distinction.
- *corrected free-subset polynomial*, *kernel identities*, *probe* (sense 3), *the supplied construction*, *mark* (5:861): the readings are supported but no source sentence states them; the bases say so.
- *chart*: the domain of the "small-field / ordinary chart" (e) relative to the logarithmic chart (b) is still not stated anywhere I read (v3 10:97–98, 17m:41–42; Scott D-section:208).
- Reason for the word "contact" in chapters 7 and 17: not found in v3, Scott or Martin.
- Line numbers of Scott `part2/I-section.tex` used here: 59, 91 (comparison windows), 98, 105, 109, 111, 184, 213, 228, 331, 349, 373, 381; each line was opened.

**Commands run.** `grep`/`sed`/`awk` on the v3 chapters, `audit/*.md`, `blueprint/notation.md`, Scott `part1`, `part2`, `macros.tex`, Martin `existence/*.tex`; `git log --oneline -S…` on two chapters (read-only); in the Lean tree `grep -rn`/`-rl` for declaration names and imports, and `sed`/`cat` of `ChallengeSpec.lean`, `ContactSpec.lean`, `ContactBridge.lean`, `Construction.lean`, `Solution.lean`, `Challenge.lean`, `YM/Contacts/Solstice/Result.lean`, parts of `Venue.lean`, `Skies.lean`, `YM/Contacts/Score/Formula.lean`, `Tape.lean`, `Subdivide.lean`, `YM/Contacts/Normal/Subtractions.lean`, `YM/Contacts/Coherent.lean` (lines 117–141), `YM/Contacts/Tomography.lean` (lines 12–40), `YM/Nonperturbative/Continuum.lean`, `YM/PREC/FrameResponse.lean` (lines 57–95), `YM/PREC/TreeMatch.lean`, `YM/Push/LOOP_COEFFICIENT/Column.lean` (lines 1–80), `YM/Push/FREE_RESOLVENT/GaugeProjection.lean` (lines 1–70). No `lake env lean` run, no build; the scratch directory `a5` was created and is empty.

---

<a id="appendix-j"></a>

## Appendix J. Record of decisions

What was decided for each term where the chapter-group dictionaries disagreed or a check proposed a correction, and on what evidence. "Note NNN" is a line of the previous, chapter-by-chapter version of this file (commit `75bb0840`); "A2"–"A6" are the round 3 check reports for its Parts II–VI.

### Letters A, B, D

- **actual.** Eleven senses kept, with the chapters of each. Counts for chapters 1, 2, 7–9 taken from the per-line lists (23 and 5), not from the overview ("about 24", "about 6"), following the third audit. Chapters 12–16 senses (b), (c), (d) merged into sense 6, as the overview does. Not opened beyond the lines quoted in the note.
- **actual stationary tangent.** Row 2672 kept as its own entry because the phrase has two uses (`W_a`; the operator `W`); the note's reconciliation through 5:1234 is recorded. Lines not reopened (the note records them as verified in the last fold).
- **adjacent pair.** Basis disagreement (chapter 9: D; chapter 6: R / I) decided as R; text read at 6:13, 9:15, 9:912. The compound "adjacent quadratic pair" occurs at 9:912 only (audit correction applied).
- **admissible.** Count for chapters 12–16 corrected from 15 to 16 and "graph" from 7 to 6 (audit correction; not recounted). Coupling band: place of definition 4:418–419 added beside 10:212 (text read: 4:418–419).
- **admissible path action.** Chapters 17–19 had basis ? and "cite the ch. 7 definition"; replaced by the chapter 5 reading (5:1241–1252, 1378–1387), basis R / I. Text read: 5:1241–1252, 1378–1387; 17t:83–85; 17c:11–13. The statement that "admissible" does not occur in chapter 7 is the audit's grep, not repeated.
- **admissible periods.** Overview (inferred) against Parts I §3 and VI (R): split into R for the identification with `R_p` and the formula, I for the meaning of "admissible". Text read: MT:11–20; 19:16–21; 10:193–197; 1:200–203.
- **alias.** The overview's statement that "alias" is new in chapters 17–19 corrected: same term as in chapters 5, 7, 11. Text read: 5:350–353; 11:1731–1737; 17c:55–57. Basis raised from R / I to R on 17c:56.
- **amplification.** Cluster equivalent *loses a factor* rejected (audit); text read: 11:1365–1366, 1963; 17w:77–79.
- **anchor.** Sense 1 raised from R to D (text read: 4:435–436). The merge "anchor, root → base point" restricted to "anchor" (audit; 5:917, 6:86, 5:1242–1246, 6:1462 not opened).
- **anchor average.** First occurrence corrected from 17c:120 to 17c:71 (text read).
- **attachment.** Chapters 10–11 (narrow, R) against chapters 12–16 (wide, I): decided by the text as two senses, the narrow one R at 11:148–149 and 11:922–923, the counting use of 9:687 separate (I). Part I's reference 11:924–941 replaced by 11:922–923, 937, 941. Text read: 9:685–688, 696–698; 11:145–156, 921–924, 936–941. Row 2701 ("attach a condition", 17m:125) added as sense 3 (text read: 17m:124–126).
- **backward comparison / descent.** Basis for "trial descent" unified to R (chapters 10–11 had I; chapters 17–19 R via chapter 11). Sense "passage to a quotient" and 18lp:342 added from the third audit. Text read: 13:263; 14:51; 13ba:170; 18lp:342; 17m:444, 461, 469; 7:1187. One verb chosen for sense 1 (*transfer*), the alternative *propagation* recorded.
- **block length.** 11:1873 moved from ? to I (block ratio `L`) on the audit's argument; text read at 11:1870–1874, 11E:28–32, 19:18–21; the supporting lines 11:1760, 1953, 1957–1958 not opened, so the alternative reading is kept in the entry.
- **block penalty.** "Same sense" in chapter 7 rejected; two senses (constant in chapters 4–6, MT, 19; penalty term in chapters 7, 9s). Text read: 4:226; 5:87–88; 6:21; 7:475–477, 523–524, 573–575, 873–875; 1:408–410, 419–421; MT:12; 19:17. Synonym cluster for the constant `b` to be restricted to "soft constraint (coefficient)", "block parameter", "penalty parameter", "soft-block penalty". 17m:14 (cited by the note's symbol table for "block penalty") has `q_{bβ}`, not the phrase (text read).
- **`B_n`.** "Not determined" resolved: two radii under one letter (4:413 at 17m:432–438; restarted radius at 17w:33). Text read: 4:410–414; 17m:432–438; 17w:31–34.
- **bottom.** "Bottom stage" kept as ? for the word "stage"; reading "lowest level" supported by 11:896, 909 (note) and the audit; text read: 17w:96–98.
- **branch.** Chapters 10–11 ("stationary branch" undefined, I) against chapters 7–9 (R, 9s:36): chapters 7–9 followed, on the audit's reading of 9s:36 (not opened here).
- **buffer.** "Slab margins = the same thing" corrected to "a component of the buffer"; cluster equivalent *margin* rejected. Text read: 13:332–336; 14:98–100.
- **delay.** "Of another kind" for 10:107–112 and "inferred" for the mechanism both replaced; one sense, basis R. Text read: 10:105–112, 157–159; 11:1397–1402; 11E:28–32.
- **density coordinates.** Equivalent *representation* chosen over *parametrisation*; 9:7 reworded (text read: 9:6–7).
- **detection.** *separating family* chosen over *nondegeneracy*; the reservation of "separation" dropped; cluster "value of a correlation functional" not followed (audits A2, A4; chapter 3 lines not opened).
- **dictionary.** Chapter 12 meaning widened to include the indicators (text read: 12:22–27).
- **discrepancy.** Senses 3 and 4 added from audits A3 and A2 (text read: 9:791–792; 11:1870–1872; chapter 6 lines not opened).
- **distance from the identity.** Basis moved from D (4:56) to D (1:90–95); text read: 1:90–95. The chapter 6 count is 13, or 14 with "the squared group distance".
- **division.** Chapters 17–19 ("not defined", paraphrase) and chapters 10–11 (curl-division, ?) overridden by chapters 7–9 (D, 7:89–91). Text read: 7:89–91; 17c:98–105.
- **denominator.** Second sense imported from the rows "vacuum denominator" (12:286) and "empty coefficient; empty density; denominator" (17w:88; 17m:418), which belong to other writers.
- **Dropped:** note 392 ("**D** — the text defines the term; the line is given") and note 2630 ("**Basis codes** …"): legend lines of the note, not terms.
- **Folded into another entry:** 2390 and 2407 (→ *admissible*, with a separate entry for *admissible comparison depth*); 2155, 1576 (→ *admissible*, sense 1); 2701 (→ *attachment*, sense 3); 2745, 2971, 1572 (→ *descent* and *backward comparison*); 1169, 1800, 2334 (→ *detector*, *detection*); 1087, 494 (→ *allocation*); 3027, 2662 (→ *bottom*); 2682, 1681 (→ *box-filter identity*, *alias*); 1045, 1046, 1177, 1809, 2283, 2344, 2787, 484 (→ *anchor*); 1680, 720, 1725 (→ *anchored*).

- **Integration of handed-over material (letters A, B, D).**
- absorb (note 2710): nothing new; the entry already records chapters 17–19 without a line list.
- active / inactive (note 1073): nothing new (9:51, 58, 72–73 already in *active coordinates*).
- accumulated noise (note 524): new entry, pointing to *noise* (sense 1).
- activity arrays; array (note 2252): stub *activity arrays*; variant added to *array*; references already present.
- additive multipliers (note 1594): new entry.
- adjacent stage pair; adjacent-stage cases (notes 1490, 2644): added to *adjacent pair* as variants with 10:28–31, 45 (text read: 10:24–32, 44–46; the sentence does not say what is paired).
- allocation sector (note 595): stub to *sector* (sense 1); removed from the variants of *allocation*.
- amplification (note 1569): nothing new; relation to "magnification" added to the coherence line.
- anchored correction (note 2692): new entry.
- angular boundary (note 2217): new entry.
- annular estimates; bounded approximations (notes 2768, 3038): new entries, basis ?.
- arity (note 1645): basis contradiction (I in chapters 10–11, R at 13:39 in the entry) decided by the text at 11:2044 and 13:39 (text read: 11:342–344, 2040–2048; 13:37–41): no sentence states the meaning, so I.
- attach; attachment; attachment reserve; attachment margin (note 1553): agrees with the entry; variant "attachment margin" added.
- auxiliary history (note 1514): new entry with two senses (text read: 10:822–828, 916–919; 11:734–738; 11R:3–7), basis R for both; pointer left in *auxiliary*.
- available weight (note 2151): new entry; cross-reference added in *amplitude* (sense 4).
- averaged measurements (note 1570): new entry.
- background insertions `b`, `c` (note 2685): agrees with the entry; equivalent written *vertices*.
- block root (note 1660): new entry without gloss.
- bounded coarse polynomial trials (note 1571): stub to *trial*.
- branch masses (note 538): new entry.
- budget (note 2978): stub to *path budget*; label names only.
- detector (note 2978): nothing new; the stub already says labels only.
- declared / declaration (note 1641): nothing new.
- deep transferred current (note 2657): new entry (text read: 17m:27–30).
- defect; defect Ward identity (note 2668, with 573): entry *defects* rewritten as *defect* with four senses; current defect added with the corrected count (21 uses); stub *defect Ward identity* (text read: 17:192–196; 17c:64–67; 14:930–938).
- defect space (note 2238): new entry (text read: 14:930–938).
- degree ceiling (note 2196): new entry.
- degree-`d` section (note 2158): stub to *section*.
- degree menu (note 1551): new entry.
- denominator (note 2715): agrees with sense 2; 17w:88 put under the same basis.
- descendants (note 2748): new entry.
- descending graph (note 2711): stub to *descent* (sense 1); 17m:470 added there; "graph" kept.
- dimensionless directions (note 716): stub to *normalized directions*.
- direction selectors (note 257): basis contradiction (I in the entry, undetermined in the bullet) not decided by the text (text read: 7:272–278, 424–429); basis set to ? with the reading as I.
- discarded-support (note 1645): new entry.
- distant part (note 1565): new entry.
- distinguished unit (note 2232): stub to *unit* (sense 1).
- division, compound forms (note 922, 2681): nothing new; already variants of the entry.
- downward blocking (note 954): new entry.
- Book-wide decisions applied: *level* for the scale index in *adjacent pair*, *delay*, *downward blocking*; *the penalty parameter `b`* in *block penalty*; *transfer* in *backward comparison* and *descent*; *the stationary tangent* (with the representative) in *actual stationary tangent*; *history* kept in *auxiliary history*.

### Letters C

- `centered`: six senses assembled from Parts II, III, V, VI; Part II's "(iii) normalised, 4:132" made precise from 4:119–120, and 5:127, 6:851 added to the zero-mean sense (audit A2 D15; not reopened). Sense 4 confirmed at 13:85–89 (text opened).
- `centered log determinant`: Part II (`log det H(v) − log det H(0)`) against Part III (`s(x) − s(0)`, `s = ½ log det A`). Decided for the vertical Hessian `A` by 5:1338–1339 and 9s:47, 59 (text opened); the subtraction stays inferred.
- `cell`: "copy" removed from the synonyms of "cell" (audit A4 U16, 11:836, 846, 1122; not reopened); 11:846 dropped from the range 835–846; count 57 kept with the recount 58 (audit A5).
- `charge`: Part II (generator, 3:780) and Part V (maps on `F_d`; smeared operator, 16:523) kept as two senses (3:779–781 opened).
- `chessboard seminorm`: line 11:820 corrected to 11:819, 822; statement that the notations are one seminorm limited to three of them (audit A5; not reopened).
- `clearance`: Part II *distance* against Part VI *separation*; *distance* chosen (6:495–497, 602–604; 18:75–80 opened). The joint line list of Part II split between clean (6:925–997), clearance (6:496, 603) and remote (6:1008, 1249).
- `cluster`: three house senses plus the standard "cluster expansion"; Part VI's "third meaning in the book" not adopted (audit A6 D8; 15:32–34, 76–84 opened).
- `coarse forecast`: Part IV basis I against Part I "undetermined"; `?` kept (11:724–727 opened).
- `column`: Part IV (image of a basis vector) against Parts I and V (coefficient vector and map). Both uses occur (11:443–446; 18lp:25–27; 13ba:274–278 opened); recorded as two senses, not as a change between chapters (audit A5).
- `comparison level`: second sense for 17m:136 added from audit A6 (4b-2), basis I (17m:135–137 opened, which only shows the phrase).
- `compensation`: Part IV's identification of 6:1540 with 10:529–531 lowered to I (6:1539–1541 opened).
- `complementary`: sense 2 (`(1−γ)W`, 11:1613) separated and the explicit formula 11:1316–1321 added (audit A4 U11; 11:1611–1614 opened).
- `completion`: Part VI's "`𝒞⁻¹` its inverse (ch. 7)" corrected: the completed inverse of chapter 7 is `(ℋ + F*F)⁻¹` (7:877–879), another operator (audit A6 D4; 17t:85–88, 17c:63–65 opened; 7:877–879 not reopened). 17c:64 left unassigned.
- `compression`: "ground algebra = `𝔄`" lowered from D to R / I (audit A5; not reopened).
- `compulsory`: chapter 6 uses kept apart from 10:654 (6:1014–1019, 1458–1462 opened); "mandatory" marked as a different object in the same role (audit A4 U15).
- `cone`: chapter 16 count corrected to six; 16:202 is a cone of imaginary parts (audit A5; not reopened).
- `connected covering number`: symbol reference 6:1296 → 6:1297; two notations and "boxes"/"balls" recorded (audits A2, A5; not reopened).
- `conserved line`: Part I, Part V and Part VI agree; basis R for the two statements, I for which is used at 17:341.
- `contact`: possible common origin of the chapter 7 and chapter 17 uses recorded as an inference (audit A6 D7).
- `contraction`: 17:256 removed (an `\input` line; audit A6 E8).
- `corrected`: Part IV ("no standard name") against Parts I and V (Wick ordering, general knowledge); the Wick reading kept as a flagged possibility. "Corrected projection" lowered from R to I (audit A5).
- `correlation-null`: definition at 13:125–132 added (audit A6; 13:125–132 opened).
- `correlation responses`: three proposed equivalents in the note (*correlations with all other fields*; *value of the functional*; *correlation functional*); *correlation functionals `L_{v,f}`* chosen.
- `cost`: five senses merged from five parts; 5:967 added (audit A2); the 24 uses of chapters 17–19 were not split by sense in the note.
- `counting norm`: "counting coordinates" (11:621) kept as inferred, since Part II has no row for the phrase (audit A4).
- `coupling band`: definition moved from 10:212 to 4:418–419 (audit A2; 4:417–420 opened).
- `coupling threshold`: one equivalent (*lower bound on `β̂`*) for the wordings of Parts II, III, V, VI; caveat on bare "threshold" from audit A3 D11 and Part I.
- `cover`: second sense (connected cover) separated from the covering lattice, because both occur in chapter 11 (11:494–496 opened).
- `crude and grid constants`: `?` raised to R (18lp:320–341; 18r:28–30, 37–40, 50–55 opened; audit A6).
- `curl-division`: `?` raised to R (10:313–316; 7:67, 88–91 opened; audit A4 E7). "Path-placement" stays open.
- `current defect`: count 22 → 21 (audit A6 E11).
- `curvature defect`: "`Z`" marked as the note's notation; 6:176 dropped (audit A2 D12).
- `curvature measurement / coordinate / insertion`: kept as three related objects, against Part III's synonym cluster (audit A3 D6).
- `cutoff`: four senses; Part IV's fifth item ("cutoff failure = large-field event") moved to `cutoff failure`.
- `cutoff failure`: Part IV ("= large-field event") against Parts I and II ("not a large-field event"). Two uses found in the text (6:1014–1019; 10:530–533; 11:147–152, 1486–1492, 1611–1614, 1931–1934 opened); written as two senses (audit A4 E4). "Tail events" assigned to sense 1 (audit A4 E3; not reopened).
- `cutoff remainder`: 6:1018 added (audit A2).
- Dropped: note line 386 ("Companion parts.", a pointer sentence of Part II, no term); note line 877 ("Conventions." of Part III, no term). Note lines 256–260 (Part I §4, bullets by chapter group) are not terms: their items beginning with C are in the entries *coarse forecast*, *corrected body product estimate*, *coordinate hybrids*, *column* (front-column) and *comparison level*; the others are in "Material for other letters".
- Rows saying only that terms do not occur (note 1126, 1689, 1719, 2308) are folded into the "Across chapters" lines of *centered log determinant*, *cluster* and *compulsory*.
- Integration of handed-over material (round 3):
  - `coordinate tuple`: new entry (pointer to *density coordinates*).
  - `containing-site sum`: added to *containing-site bound* (conversion 11:266–272; see also *anchored*).
  - `comparison coefficient / family`: stub to *admissible* (sense 1).
  - `cones; disjoint-cone identity`: added to *cone* (variant and gloss, 13ba:181–270).
  - `coefficient recovery; coefficient conversions`: new entry and stub; cross-reference to *deterministic coefficient evaluation*.
  - `coefficient functional; cubic momentum functional`: new entry and stub; the cubic momentum functional identified with `𝔥` by inference from 17m:353–357 (text opened: 17:211–226; 17m:348–357).
  - `cofinal grids`: new entry, basis R (13ba:303–307, 335–337 opened); kept out of "subsequence".
  - `compensating map`: nothing new; "not glossed" recorded in *compensation*.
  - `completed`: already in *completion* (17c:64 unassigned); nothing added.
  - `coordinatewise splice`: "question for the author" added.
  - `corrected projection; corrected inclusions`: lines 13:195–203, 220, 263–264 added to *corrected* (sense 2); stub *corrected inclusions*.
  - `cost` (chapters 17–19 and 12–16): already in *cost*; the identification `q_r` = `q^site` = `q` marked as inferred (the entry had stated it without a basis); neighbouring word counts added. Contradiction on 9:712 ("fits none of the senses" against sense 1): decided by text at 9:712, a polynomial-logarithmic factor, sense 1. "Margin" belongs to M.
  - `coverage`: stub to *exact cover*; third use noted in *cover*.
  - `curl-division; path-placement operations`: entry unchanged in substance; "path-placement" recorded as open inside the entry.
  - `charge fields`: already in *charge*; nothing added.
  - `coefficient graph`: stub to *linear graph*, with the rejected equivalent *remainder map*.
  - `comparison level` (with output, stopping, radius level): chapter 17 lines and the remark on the output level added to *comparison level*.
  - `complementary profile`: stub; remark added to *complementary*.
  - `centered` (9s:283): already sense 6; nothing added.
  - `channel; clover substitute`: *channel* extended; stub *clover substitute* (9:541–548 opened).
  - `cleared by`: new entry.
  - `coefficient normalizations`: new entry.
  - `compulsory` (non-occurrence in chapters 1, 2, 7–9; 12–16): chapters 1, 2 added to the non-occurrence statement.
  - `consume`: new entry.
  - `correlation responses`: already present; see-also to *one-slot response* and *spectators* added; rejected equivalent kept in neutral form.
  - `cutoff tail`: stub; lines 12:190, 249; 13sb:84 added to *cutoff* (sense 1).
  - `cutoff-failure catalogue; clipping rule / clipping data`: stubs; reading and lines 10:393, 727, 921 added to *cutoff failure* and *clip* (10:391–394 opened).
  - `centered coordinates`: stub; opposition to rooted coordinates added to *centered* (sense 3).
  - `comparison cell; copies`: stub *comparison cell*; new entry *copy* (image, not cell; neither *copies* nor *cell* adopted for both).
  - `centered log determinant; compulsory` (no occurrence in chapters 12–16): recorded in *centered log determinant*; *compulsory* already said so.
  - `change of stage`: stub to *stage*.
  - `chart recognition`: new entry.
  - `chosen`: new entry, four senses.
  - `coarse endpoint`: stub already present (to *coarse target*); "trajectory ends" of the bullet rendered as "history" there, as before.
  - `common family`: new entry.
  - `common trajectory`: stub already present; nothing added.
  - `connector`: remark on 13ba:244–245 added.
  - `core energy`: stub; proposal and 6:1429 added to *core*.
  - `corrected body product estimate`: "question for the author" added.
  - `candidate field`: new entry (basis I, the row had none).
  - `choice of sufficiently large starting scale; condition(s) on the starting scale`: two stubs to *threshold for the starting scale*.
  - `clean` (9:279): already present.
  - `coarse trial`: stub to *trial*.
  - `contact` in "contact identity": already present (sense 3 and the inferred common origin).
  - `counting`: already in *counting norm*.
  - `cover units`: stub to *connected covering number* and *unit* (sense 3).
  - Bare symbols in the bullets (`p_b`, `Y_d(K)`, `𝗾`, `𝗹`, `𝗵`, `𝖼`, `V_h`): skipped as symbols, mentioned inside entries only.
  - Tidying: references to parts of the note and to audit reports removed from inside entries; rejected equivalents kept in the form "Not *…*".

### Letters E–H

- **eligible**: three senses kept. The overview (one sense), chapters 10–11 (11:153 undecided) and chapters 12–16 (basis I) disagreed; decided by the text, opened at 4:438–450, 4:68–75, 8:286–295, 11:123–132, 11:150–154, 11R:78–81, 11R:166–168, 10:668–670, 18:122–128: the later uses attach eligibility to a term or label (per-activity), 11:125 is the family rule.
- **envelope**: one sense (majorant). 6:1187 opened; fits, basis I there. Synonymy with "majorant" refused on the audit's reading of 9:793–794 (opened).
- **equation calibration floor**: parts agree; 11E:23–30 opened.
- **equation space**: one object, two notations; equivalent of chapters 12–16 kept, that of chapters 10–11 recorded. Text not opened.
- **equation remainder**: no equivalent in the note for this term alone; "none proposed". Text not opened.
- **event indicator**: 11R count 8 → 9 and the caveat on `h_X` in chapter 9, from the audits. Text not opened.
- **exceptional phases / vacua**: three different equivalents (overview, chapters 12–16, chapters 17–19); decided by the text (15:324–328, 16:379–381, 19:105–108 opened): the non-uniqueness is never shown, so the chapter 17–19 wording is rejected.
- **excess**: three senses; removed from "slack" on the audits' quotations (6:326–329; 13sb:6–7). Text not opened.
- **exchange term**: "undetermined" in chapters 10–11 against R in chapters 1, 2, 7–9; decided by the text (7:933–947, 10:335–338 opened): R.
- **exterior identity**: reference 5:840 → 5:839 (opened).
- **extraction**: three senses; 11:2037 opened, not decisive; assigned to sense 3 with basis I on the audit's argument.
- **elementary division / curl-division / division (ch. 17)**: audit corrections applied (defined 7:67–97); text not reopened.
- **factor count**: basis for the chapter 11 use raised to D via chapter 2 and the gloss widened to "degree in jet coordinates" (2:51–54, 11:368–369, 11:1134–1136 opened).
- **fine end**: direction corrected (fine end = `m`, not `k_*`); 18lp:44–53, 62–65 opened.
- **fixed common coefficient functionals**: basis ? → I on the audit's reading of 10:313–321, 339; text not opened.
- **fixed-input continuity / convergence**: the chapter 19 nickname attached to the chapter 12 definition as an inference (12:36–39 opened).
- **fixed-ratio jet errors**: overview "undetermined" against a partial gloss in chapters 17–19; the gloss kept with basis I. Text not opened.
- **flattening**: basis R → I (9:675–678 opened).
- **floor**: two senses; 11R:247 assigned to the operator sense (11R:246–248 opened; 7:685 and 17t:107 taken from the note's quotations).
- **flux**: equivalent of chapters 3–6 ("smeared charge") replaced by the wording of `notation.md` line 165 (3:664–673 and `notation.md` 165 opened).
- **frame**: three senses plus one undetermined use (17w:120–123 opened; no antecedent).
- **free image**: "five names" → six, and the proposed equivalent is the text's own name (audit; text not opened).
- **frozen**: two senses; 6:441–444, 7:733–736, 11R:246–248 opened.
- **gap**: senses 4 and 5 added and the cluster "lower bound: floor, gap, margin" split, from the audit of chapters 1, 2, 7–9; text not opened.
- **gauge completion**: chapter 17 use separated from the chapter 7 inverse `𝒞^{-1}` (audit; text not opened).
- **graph**: "?" of chapters 17–19 overridden and "remainder map" of chapters 10–11 rejected; 11:379–382, 11:446–448, 11:910–912, 12:82–94, 17m:443–445, 18:122–128 opened.
- **Haar logarithm**: basis R → I; "local Haar logarithms" (6:1255) moved here from the chapter 3–6 row "logarithm" (9:62–64, 76–77, 9s:37–40, 6:1254–1256 opened).
- **hard**: reference 9:656 → 9:657–658 (audit); 10:653–667 opened.
- **heat**: first use 14:80, not 14:41 (14:79–81, 15:26 opened).
- **height**: "resolution heights" added as a separate sense with the audit's settlement from 18lp:223–224, 347–348; text not opened.
- **history**: three senses; 5:302–306, 10:254–257, 11:16–20 opened. Equivalent "RG trajectory" not adopted for sense 2 (audits: trajectory and schedule are other objects).
- **grid / generic**: "cofinal" removed from the meaning "subsequence" (audit; text not opened).
- **Dropped:** note 2627 "File abbreviations" (a list of file abbreviations, not a term).
- **Passed on, not given entries:** note 241 (`E_reg`) and note 3040 (`E_stat`, `E_tail`, `E_mark`), bare symbols, placed under "Material for other letters".
- **Entries added without an owned row:** *forced*, *gas*, *event indicator*, *fine end* (from rows 1727, 2307, 2148, 2189 and the note lines 281, 973, 986, 1897).

- **Integration of handed-over material (letters E–H):**
- **fine residue** (note 1050): added to entry (7:585, 595, 599; 7:585 opened).
- **`E_stat`, `E_tail`, `E_mark`, `E_reg`** (note 260, 241, 3040): skipped as symbols.
- **excess** (note 2267, 2332): added to entry *excess* (count for sense 3; relation to *reserve*, *margin*, *loss*); no contradiction.
- **failure** (note 2700): new entry.
- **field-null spaces** (note 2727): new entry (definition at 13:125–132 as handed over, not opened).
- **finite decorations** (note 258): entry exists; nothing new.
- **fits** (note 1167): line list added to entry *fits*.
- **fixed-ratio jet errors** (note 260): entry exists; sense of "fixed-ratio" and cross-reference added.
- **fixed-ratio constants** (note 2651): stub to *pre-ratio constants* ("post-ratio constants" belongs to P).
- **gain** (note 1167): line list added to entry *gain*.
- **grid configurations** (note 2744, 3037): added to entry *grid* (18r:29 via 18lp:223–226, basis R).
- **grid errors** (note 220, 2998): already in entry *grid*; nothing new.
- **ground algebra** (note 2220): new entry. Contradiction on the basis (D in the note, R / I handed over) decided by text at 15:150–156: the sentence does not define the phrase, basis I.
- **ground space / ground vector / ground projection** (note 2234): stubs to *zero-energy subspace*.
- **halo** (note 605): entry exists; nothing new.
- **Hilbert encoding** (note 258): entry exists; nothing new.
- **entry; lower / higher entry** (note 1606) and **higher (regular) entries** (note 2150): new entry *entry* with two senses; stub *higher entries*.
- **external** (note 944): new entry.
- **field word** (note 2227): new entry.
- **finite local / auxiliary projection; projected scalar** (note 1527): new entry *finite local projection*.
- **geometric magnification** (note 1569): stub to *magnification* ("measurement magnification" belongs to M).
- **high coordinates** (note 2173): new entry.
- **exact-cover gas** (note 986): added to entry (chapter 9 identification is inferred; *constrained sum `ℱ⁰`* recorded as not adopted book-wide).
- **graded quotient comparison** (note 2738): stub to *physical inclusion* (the reference is 18:175, not 18:174).
- **Haar-ball normalization argument** (note 1534, 1863): new entry ("sparse stopping scale" belongs to S).
- **encoded** (note 1641): new entry ("declared" belongs to D).
- **endpoint re-expression** (note 1507): stub to *re-expression of the endpoint*; it remains a variant in *endpoint*, sense 3.
- **exact pulled-back defect** (note 2671): new entry.
- **first (backward) crossing** (note 2648, 3008): new entry *first crossing* ("overshoot" glossed inside it; its own entry belongs to O).
- **forcing** (note 2680): new entry.
- **forest prescription** (note 2749): new entry.
- **frame seed** (note 2169): stub to *shared frame seed*.
- **endpoint error** (note 2711): stub to *trial descent*; mentioned in *endpoint*.
- **envelope** (note 1585): already in entry *envelope* (variant "weighted output envelope"); nothing new.
- **event label** (note 1127): entry exists; the row has no text. Entry reworded for *cutoff-failure event*.
- **exact unit rule** (note 1545): new entry; equivalent changed from *identity insertion* to *identity field*.
- **exterior discrepancy** (note 2714, 3032): new entry, basis ?.
- **field reconstruction** (note 2724): new entry.
- **"with these same frames"** (note 3028, 2951): already in entry *frame* and under Unresolved.
- **full-copy estimates** (note 2741): stub to *uniform in the number of reflected copies*.
- **gaps** (note 1579): added to entry *gap* as sense 6.
- **graph, why so called** (note 2393): already in entry *graph* and under Unresolved.
- **horizon** (note 508): new entry.
- **Book-wide decisions applied:** *history* kept for senses 2 and 3 (the equivalents "finite renormalisation trajectory" and "trajectory started from zero activities" withdrawn); *cutoff-failure event* in *event label*; *transfer* in *fine end* and as the reason against "transfer semigroup" in *heat*; *identity field* in *exact unit rule*; *level* in *first crossing* and *horizon*.

### Letters I–M

- **incidence**: basis I (Part IV) against R (Part V) on the same quotation; decided I after reading 11:256–259, as audit A5 (2.3, 4a.4) asks. Text opened.
- **incoming / inherited / outgoing**: five parts agree; merged into one entry. Not opened.
- **infinitesimal gauge insertion**: Part III (`ℛ`, *infinitesimal gauge action*) and Part VI (`d`, *infinitesimal gauge map*) merged; one equivalent chosen (the text's phrase at 7:877, as quoted by the note). Not opened.
- **inflation factors**: synonym cluster "loss in an estimate … inflation" not followed, on audit A4 U14 (11:274–292). Not opened.
- **inherited loop action**: Parts I, II, III, IV, VI agree; audit A3 E7 concerns the path-action row and is consistent. Not opened.
- **insertion**: Part I (three senses) against Part III (four); four kept plus the definition at 3:92 (audit A2 4c) and the 17m use. 3:91–93 and 1:330–334 opened.
- **interface**: Part III "same sense" as Part II; 5:1383–1386 and 9:441–444 opened: hypotheses in chapter 5, an established statement in chapter 9; one entry with two wordings, basis raised to R.
- **inverse terminal coordinates**: Part IV (`𝖹^{-1}c`, D) against Part V (`‖X_i^{-1}z_i‖_1`, R at 11:1101–1102); 11:1047–1049 and 11:1099–1103 opened: neither defines the phrase; basis I, both readings stated.
- **join / attach**: Part IV (R, narrow) against Part V (I, wide); narrow kept on audit A5 (11:145–152, 922–923). Not opened.
- **kernel identities**: basis I kept; audit A6 (section 3) notes the row was misfiled under "determined by another chapter". 17:306–309 opened.
- **kinetic**: Part III (new term, *quadratic curvature form*) against Part II (*kinetic operator*, D 5:44–46); same object by audit A3 D1 and by 5:44–46, 7:183–190, 7:611–613 (opened); Part II equivalent kept; lines 7:904, 1161 added.
- **label**: Part II (element of `V_d`) against Parts I, III (pair `(d,c)`): both in the text (audits A2 4a.4, A3 4b.6); recorded together. Chapter 18 use: Part I "probably `F_d`", Part VI "not stated"; 18:139–141 opened, names no space; basis I. Count for chapter 13 corrected to 15 (audit A5). "Moving labels" of 14:238, 250 not filed as free fields (14:236–239, 249–251 opened). Part IV and Part VI label paragraphs (note 1763–1768, 2913–2917), not in the assignment, were folded in.
- **layer**: basis I and *degree* (Part II) changed to R and *homogeneous component* after reading 3:184–186, 2e:90–92, 4:146–148; third sense (7:454–455) from Part III.
- **leading**: sense 3 given two readings, on audit A4 U12. Not opened.
- **leg**: Part VI "new sense" corrected to the chapter 7 sense, on audit A6 4c.12; 3:825–827, 7:60–62, 17c:14–17 opened.
- **level**: proposed word *level* (Parts I, IV, V) against *scale* (Part VI; audit A6 4a.7); *level* kept. Different attachments of "comparison level" and "output level" recorded from audit A6 4b. Not opened.
- **lift**: chapter 7 use no longer "same sense" as chapter 5 without qualification (audit A3 D10); 5:626–633 and 7:131–135 opened. Two equivalents for the coefficient lift merged.
- **likelihood**: basis I for both lines (Part II) against "undetermined" (Part I) and audit A2 D1; 6:918–921, 1013–1017, 1105–1108 opened: I at 6:1016, ? at 6:920.
- **line**: entry added for the two objects called "line" in chapter 14, on audit A5 4b.8. Not opened.
- **linear graph**: proposed *remainder map `G`* (Part IV) rejected by Part I section 8, Part V and audits A4 E1, A5, A6 E1; 11:379 opened for the phrase only.
- **localization**: not in the assignment (the row is "common localization", note 1566); entry written because the headword is in range.
- **logarithm / logarithmic**: "local Haar logarithms" (6:1255) removed from the examples of *logarithm* (audit A3 4a.7; 6:1254–1256 opened); "in `log β`" corrected (audit A3 E8; 1:49–51, 1:461–463 opened).
- **margin**: "lower bound" cluster (Part III) rejected in favour of "slack" (Part I), on audit A3 E5 and the lines found by grep (9:701, 794, 950; 9s:221; 6:737, 917–918, 1020; 10:615, 776, 915; 11R:261, 278, 306); spatial sense for file 11 (audit A4 E8; 11:2339, 2351); *margin* not to replace *buffer* (audit A5 1.7).
- **mark**: Parts I, III, IV, V, VI agree; merged. 7:377–379 opened for sense 5.
- **mass**: Parts II, IV, V, VI list different senses; merged as five senses. 11:422–425 and 17t:41–43 opened.
- **matching**: Parts I, II, III, VI agree. 1:461–463 opened (occurrence only).
- **measurement**: equivalents *value of the functional* (Part I) against *correlation functional* (Part V; audit A5 4a.10); the first kept. 18:72–73 opened.
- **metric**: audit A4 (4a) says Part II has no row for "metric"; note line 572 is that row, so the "same sense" rows of Parts III and IV stand.
- **microscopic sections**: note's meaning and basis replaced on audit A6 E10; 19:27–29, 11E:4–7, 36–39 opened.
- **mixed**: first use 18lp:8 (Part V, audit A5 4a.9) against 14:12 (Part I); chapter 3 sense added from audit A2 4b (3:405–407, 943–947 opened); 16:359–361 opened.
- **moment**: extended from one sense to four or five on audit A5 2.10; 15:212–214, 18lp:176–178 opened (the latter gives no gloss).
- **moment norm**: not in the assignment; entry from note 344 and 1519; 10:464–471, 10:630, 633 opened.
- **moving**: Part I (one sense) against Parts III, IV (second sense, audit A3 4b.8); two senses kept; reference "17t:97" corrected to 17:97 (audit A6 4a.12; 17:96–98 opened); 14:250 confirmed (opened).
- **Dropped:** note line 394 (the definition of basis code I in the header of Part II; not a term).
- **Stubs and merged rows:** 205, 1115, 2819, 1670, 570 → *inherited loop action* / *incoming*; 112–120, 459–461, 1040, 1153, 2285, 2322 → *label*; 1222, 1001 → *live tag actions*; 978, 1224 → *missing-coordinate factor*; 2146 → *inventory*; 2182 → *insertion origins*; 2731 → *marked replacement*.
- **Integration of handed-over material (letters I–M).**
- **inactive coordinates** (note 556, 1073): new entry.
- **minimising branch** (note 537): new entry, pointing to *branch*.
- **mismatch distance** (note 555): added to *mismatch* (4:397 quotation, `χ` at 1:90–95, the three unconnected names); stub. 4:395–397 and 1:90–95 opened.
- **inputs** (note 646): added to *inputs* (the group of program words of chapters 3–6; no basis for those lines).
- **marked** (note 709): added to *mark*, sense 1.
- **length** (note 1635): new entry.
- **marked ancestors** (note 2168): added to *mark*, sense 2.
- **middle and output stopping levels** (note 2662) and **middle level `ℓ`** (note 1502): added to *level*; stub *middle level*. 17w:29–34, 99–103 opened.
- **mass (of a kernel)** (note 2673): already in *mass*, sense 3; nothing added. **kernels `K_a`, `K_a^e`, `K_a^t`**: skipped as symbols.
- **inherited-loop contraction** (note 962, 1242): new entry.
- **inspected support** (note 257, 1226): entry *inspected* had basis I, the bullets "undetermined"; 9:216–222 opened: the sentence does not say what is inspected; basis I for the word, ? for the phrase, both stated.
- **interior** (note 2206, 2742): new entry with two senses; 13:66–90 opened for sense 1.
- **joint bound** (note 981): new entry.
- **large-coordinate event** (note 606): new entry.
- **leading interval; lower interval** (note 1502): contradiction on the basis (entry R, bullet I) decided by text at 11:1952–1962: the lines give step counts only, so R for those and I for the identification with `k → ℓ`, `ℓ → w`; added to *leading*, sense 2; stub *lower interval*.
- **left frame** (note 2690): new entry; 17t:186–197 opened.
- **likelihood tests; likelihood factors; likelihood (of tags)** (note 256, 538, 1126, 1719, 2308): agree with *likelihood*; 5:970 added.
- **live tag actions** (note 257): agrees with the entry; nothing added.
- **localization onto `T`; low-weight coefficient extraction** (note 1566): already in *localization*; cross-reference to *common localization* added.
- **loss; lose** (note 1167, 1620, 2267, 2710, 2784): counts added to *loss*; the line list of sense 2 corrected by text: 10:597 and 11:502 have "gain", the loss lines are 11:270, 724 and 11R:57, 143, 178, 269, 277 (grep of files 10, 11, 11R).
- **low-coordinate errors** (note 2744, 3037): new entry; contradiction on the basis (? against R) decided by text at 18r:36–39 and 18lp:316–322: R.
- **mandatory** (note 246): agrees with *mandatory factor*; reference 11R:96–116 and cross-reference to *compulsory* added.
- **margin** (note 2206, 2267, 2784) and **margin `3t`** (note 1582): agree with *margin*; 11:2337 added.
- **metric modification** (note 572): stub; 5:227–235 added to *metric*.
- **missing-coordinate factor** (note 257): agrees with the entry; nothing added.
- **mixed measures** (note 2212): already in *mixed*, sense 2; nothing added.
- **interior (difference, seminorms)** (note 2742): see *interior*.
- **joining bound `h_l`; merger; live group** (note 2170): three new entries; 18lp:65–136 opened.
- **link factor** (note 526): new entry.
- **local read set** (note 1522): new entry.
- **Maxwell solution potential** (note 913): new entry; 2e:10–21 opened.
- **moment norm `M_q`** (note 1519): added to *moment norm* (the space `c₀`, the equivalent norm).
- **moving complement; moving / varying equation space** (note 1577): added to *moving*.
- **inverse coupling reserve** (note 1520): new entry.
- **jet (chapter 6 sense)** (note 1080): agrees with *jet*; nothing added.
- **label basis elements; local labels** (note 2757): already in *label*, sense 1; nothing added.
- **markers; marks** (note 2734): already in *mark*, senses 2 and 4; quotation 18:128 and cross-reference to *nilpotent marker* added.
- **measurement cell** (note 1584): added to *measurement* as sense 3, with the distinction between cell and copy.
- **large-field activities** (note 2252): new entry, from 4:440–450 as quoted in the note.
- **lattice shell sum** (note 708): new entry; 5:1209–1214 opened, basis D.
- **large-field selection** (note 435): new entry.
- **lift; lift equations; lifted vectors** (note 1568, 1127): agree with *lift*, sense 5; nothing added.
- **local energy `𝓔_A`** (note 581): new entry.
- **measure multiplier** (note 976): new entry; 9:63 opened.
- **inclusion trial** (note 2156): new entry pointing to *trial*. **local trial** (note 1571, 2156): stub.
- **inverse source-weight bounds** (note 2714, 3032): new entry.
- **inverse terminal coordinates** (note 1574): the bullet has basis D; the entry had already decided I by text at 11:1047–1049, 1101–1102; cross-reference to *terminal map* added.
- **level; levels** (note 724, 1127): agrees with *level*; nothing added.
- **local inverse columns** (note 601): new entry.
- **local polynomial section** (note 908): new entry.
- **modes** (note 2150): new entry *mode*.
- **Book-wide decisions applied:** *level* for the index in *level*, *moving*, *mesh threshold* (*level `n_i`*, *level `k_i`* instead of *scale*); *the stationary tangent* in *lift*, sense 4; *identity field* in *kill*; *cutoff-failure event* in *large-coordinate event*; *graph* kept in *linear graph*. Process remarks removed from the *Across chapters* lines; rejected equivalents kept in neutral form.

### Letters N–Q

- **noise**: Part II rows 524 and 525 and Part IV row 1667 merged into two senses (chapter 5 block noise; chapter 6 fluctuation coordinates). No disagreement. Text not opened.
- **nonwrapping**: Parts II, III, VI agree that no criterion is given; the partial consequence 17m:331–332 and the chapter 11 use (11:1129–1131, from note 1496) added. Text not opened.
- **normalized directions**: Part II 716 (unglossed), Part III 1027, 1247 and 1229 merged; scaling settled by 4:580–581 and 6:626–638 (Part III), "affine" / "reflected" left `?`. Text not opened.
- **normalized local insertion**: basis I (Part IV) against R (Part V). Decided: R for the identification with `O_{N,p}` (11:2323 with 11:1051–1054), I for the unity with the one-step uses, R for "the weight is not part of it" (audit A5 item 4, A4 U6). Text opened (11:351–356, 1047–1055, 2322–2325).
- **normalized-null lemma**: reference "13:202–240" replaced by the statement 13:195–216 (audit A6). Text not opened beyond 13:210–215.
- **numerical band margin**: audit A3 (margin = slack in an inequality) added. Remains `?`.
- **observable label / polynomial label**: Part II (element of `V_d`) against Parts I, III (pair `(d,c)`): both are in the text (2:58–65; 2:96–97; audit A2 item 4). Two entries kept. Text not opened.
- **one-step integral identity**: Part III singled out 9:44 ff.; audit A3 D16 gives two further candidates. No candidate singled out. Text not opened.
- **opening**: Part IV (note 1502, owned by another letter) and Part V (2176, 2406) compatible; text opened (11:1887–1890, 1917–1920, 1404–1407; 13ba:125–129). Basis I kept.
- **ordered limit / ordered convergence / ordered period limit**: merged into one entry; Part VI basis I supported by 13:44–50 (audit A6 D5). Text opened (13:44–50).
- **ordered tail**: Parts I, V, VI agree; rejected equivalent "for all sufficiently large `N`" recorded. Text opened (13:210–215).
- **ordinary**: Part I 192 put 11:1589 under "small-field part", Part IV 1633 glossed it "without source weight"; audit A4 U10 says neither. Text opened (11:1586–1591): separate sense 3, basis I. Sense 2 (9:314) added from audit A3 D12; text opened (9:312–316). Part V's reading from 13ba:15–16 supplemented by 13ba:36–40 = 10:95–99 (audit A5; text opened). Proposed equivalent: *small-field* chosen (Parts III, V, VI); Part IV's *regular (small-field)* rejected because "regular" names `E_reg` in chapter 17 and the chapter 8 gas.
- **output anchors**: Part II 678 and Part VI 2823 merged; still I.
- **padded block**: Parts I, III agree on two candidates and the preference; text opened (7:597–600, 626–629); basis I kept, not raised.
- **parent**: Part III's "used undefined" is a stale quotation (audit A2 item 13); D at 1:218–220. Second sense (18:404–418) added from note 2748. Text not opened.
- **path**: "7:789" corrected to 7:786, 790 (audit A3).
- **path action**: Part III 1063 "here defined as `β𝒦 + 𝓛`" corrected: chapter 9 splits the path action defined in chapter 4 (audit A3 E7). Text not opened (the quotation of 9:21–28 is in the note and the audit).
- **path coefficient**: remark on the plural at 11:471 added (line seen while reading 11:470–474).
- **penalty parameter**: audit A3 E1 applied in the coherence line (in chapters 7, 9s "block penalty" is the penalty term, not the constant). The single phrase is left to the *block penalty* entry.
- **period**: audit A2 E1 applied (`volume` is not a synonym).
- **permitted direction**: audit A3 D11 (threshold `t` is the small-field threshold) applied.
- **phase**: Part III 1179, 1230 ("undefined", "deferred") against Part I 174 and Part V 2219 (defined 15:8–9): decided for the definition, text opened (15:7–10; 1:414–418). Paraphrase of `notation.md` corrected (audit A6 D9); 17w:121 and 18r:5 added to the list (audit A6). Complex phase factor kept as sense 2.
- **physical**: the lists of Parts II (489, 725), III (1076, 1077), IV (1704, 1822), V (2273, 2355), VI (2962) merged into nine senses; Part II (iii) and Part IV (b) identified after opening 6:692–700, 9:256–260, 11:470–474; chapter 6 uses from audit A2 D3 added under senses 8 and 9.
- **physical inclusion**: Parts I 222, VI 2738, 3005 and V 2180 merged; pointer 18gq:2, 43–45 for "physical quotient" added and "18:174" corrected to 18:175 (audit A6). Text not opened.
- **placement**: Part III 888, 889, 1202 merged; "path-placement" (10:314–315) added from audit A4 E7 as undetermined.
- **plateau**: Part II 576, Part IV 1491, 1664, Part VI 2645 merged into two senses; two wordings of the equivalent for sense 2 reduced to one.
- **pole**: Part II 623 replaced by the two uses found by audit A2 D13. Text opened (3:863–877, 962–965).
- **polynomial attenuation**: row 1645 lists seven words with seven line groups; only 11:1657 belongs to this word. The other six are in "Material for other letters".
- **pre-ratio constants**: Part II 690 ("pre-`L`"), Part VI 2651, and the remarks at notes 1149, 1495, 3023 merged; one equivalent.
- **prescribed set of large-field sites**: Parts III 987, IV 1631 and the Part I / V lists merged; one equivalent chosen (*prescribed large-field set `I_η`*).
- **primitive**: Part II 714, III 1080, 1102, IV 1677, V 2169, VI 2674 merged into four senses.
- **principal**: Part II 527, 727, Part III 943, 993, 1194, 1221, Part IV 1546 merged into five senses (audit A3 item 9 counts three across the book; the principal submatrix and the undetermined uses are added). Part III's *leading term* for 9:235, 268 not adopted because Part I section 8 rejects "leading" (audit A3 D14); text opened (9:233–236, 266–269). Audit A4 U12, U13 applied in the coherence line.
- **probe**: Part II 615 (functional on jets) against Parts V 2284 and VI 2723 (fixed word, D 18:38–39): two senses; text opened (3:937–941; 18:37–40; 17m:249–252). "Probe" removed from the synonym row "pairing with spectators" (audit A5 item 6). *Test configuration* not adopted (audit A6 D10).
- **profile**: Part I 188 and Part V 2366 merged with rows 2147, 2213; remark on 14:513 from audit A5.
- **protected**: Part II 604, Part IV 1657, 1851, Part V 2270, 2391, Part VI 2820, 3022. Part V's "presumably same (with cutoff)" for 13:229 rejected; text opened (6:692–700, 804–808; 9:256–260; 10:503–507, 719–722; 11:1061–1068, 2303–2309, 470–474, 1771–1775; 13:226–233; 17m:72–77; 17w:70–73). Three senses; senses 1 and 2 basis I, sense 3 `?`.
- **pulled back / push**: cluster equivalent *transfer* (Parts I, VI) recorded beside the row equivalents.
- **Dropped:** note 388 ("Purpose." paragraph of Part II) and note 879 ("Overall." paragraph of Part III) are not terms; the vocabulary counts of 879 are passed on under "Material for other letters". Note 1205 ("Occurrences fitting none of the senses") is a list of four leftovers of other words (row, cost, recording, centered); passed on. Notes 1798, 2332 (first clause), 2978 (`price / pay`: no occurrence) are represented by the entry *price / pay*; the rest of 2332 is passed on. Note 541 (`Q^pred`) is kept as an entry although it is a symbol, because the row is about the unexplained superscript.
- **Integration of handed-over material (letters N, O, P, Q).**
- **path budget** (note 568): new entry.
- **quadratic path square** (note 569): new entry.
- **ownership; ownership components** (notes 641, 602): new entry *ownership* and stub *ownership components*; the two rows (attribution / components) are two aspects of one definition; text read at 6:1327–1336 ("selected sets", not "large-field sets").
- **number of attachments** (note 1018): stub to *attachment* (sense 2).
- **principal / nonprincipal** (notes 1050, 1681, 2790): added to entry *principal* (17m:204, "principal column"); stub *nonprincipal*.
- **partition-of-unity weights** (note 1087): stub to *allocation* (sense 1).
- **probe** (notes 1169, 1800): non-occurrence in chapters 1, 2, 7–11 added to entry *probe*.
- **normalized (affine) directions** (note 1229): already in entry *normalized directions*; nothing new.
- **omitted degrees** (notes 2744, 3037): new entry; basis `?` against R decided by text at 18lp:321–323 (R).
- **one sector Gaussian/Haar law** (note 981): new entry, pointing to *common law*.
- **one-shell estimate** (note 2748): new entry.
- **opening** (note 1502): added to entry *opening* (support at 11:1928–1930, read; reference 11:1405–1407).
- **orientation of the line** (note 2215): new entry, basis `?`.
- **output anchors** (notes 256, 1126, 1719, 2308): added to entry (non-occurrence in chapters 1, 2, 7–16); "undetermined" against I: text read at 6:87–92, which does not decide; basis I with "probably" kept.
- **output (level) `w`** (note 1502): new entry *output level*, two senses (text read at 17t:403–406, 17c:240–242).
- **parent operators** (note 2748): stub to *parent* (sense 2), already there.
- **path-placement operations** (note 1643): stub to *placement* (sense 4), already there.
- **penalty map** (note 719): new entry.
- **physical line** (note 2215): new entry (text read at 14:292–295).
- **plaquette measurement** (note 909): new entry.
- **polynomial-source propagation constants** (note 260): already an entry; nothing new.
- **positive completion** (note 572): new entry.
- **positive-defect identity** (note 573): new entry (text read at 6:143–149; formula taken from the display).
- **preselection bound** (note 258): already an entry; nothing new.
- **protected trial; protected; protected-path errors** (notes 258, 260, 1071, 2156): already in entry *protected*; stubs *protected trial*, *protected-path errors*.
- **quadratic defect** (note 2668): stub to *quadratic defect has order at least four* and *current defect*.
- **neutral** (note 1593): new entry.
- **polynomial image** (note 625): stub to *free image*.
- **primitive** (note 2674): already sense 3 of *primitive*; nothing new.
- **profile** (note 2213): already in entry *profile*; nothing new.
- **normalized mass** (note 1561): new entry; basis I of the row raised to R for the value after reading 11:423–424; "reserved mass" belongs to letter R.
- **origins; physical origins** (note 2182): new entry *origins*, stub *physical origins*.
- **outgoing** (notes 1052, 2258): new entry.
- **polynomial moment conditions** (note 2670): new entry pointing to *low moments*.
- **projection** (note 1015): new entry.
- **original variables** (note 1076): stub to *physical* (sense 4).
- **prescribed-radius squeeze** (note 2775): new entry.
- **node sign** (note 1523): new entry.
- **parent** (note 549): agrees with entry *parent* (sense 1); nothing new.
- **nonlinear step** (note 511): new entry; equivalent *step* by the book-wide decision.
- **normal Taylor polynomial; pair weights `a_h`** (note 2746): new entry and stub.
- **numerical schedule** (note 1492): stub to *schedule* (sense 1).
- **one-slot response** (note 2204): agrees with entry; nothing new.
- **order-`r` zero** (note 918): new entry.
- **plateau (of a stage)** (note 1491) and **plateau** (note 576): already senses 2 and 1 of *plateau*; nothing new.
- **primitive random variables** (note 2169): stub to *primitive* (sense 4).
- **physical mark normalization** (notes 2714, 3032): new entry, basis `?`.
- **positive mass** (note 538): stub to *uniform mass*.
- **positive-density estimate; positive partition estimate** (notes 2713, 2996): entry *positive partition estimate* extended; its basis I against R of the bullet decided by text at 17m:433–434 and 11:799–812 (R for "positive-density estimate", I for 17w:97); stub *positive-density estimate*.
- **post-length threshold conditions** (note 1495): new entry.
- **principal compression** (note 601): added to *principal* (sense 2), range 6:520–574.
- **Book-wide decisions applied:** *level `m`* in *observation scale*, *one-loop drift*, *nested histories*, *plateau* (sense 2), *quantitative descent*; *the penalty parameter `b`* in *penalty parameter*; *history* kept in *nested histories*; *transfer* in *pulled back*, *push*; *cutoff-failure events* in *prescribed-site rules*; *step* in *nonlinear step*.
- Section "Material for other letters" removed (routed).

### Letters R

- **reference label**: Part V (note 2186, "fixed label … independent of the cutoff", basis I) against Part IV (note 1574, defined 11:1047–1049) and the audit of Part V. Decided for "coefficient at the fixed reference level `r(d)`, possibly cutoff-dependent", basis R; *fixed label* rejected. Text opened: 11:881–886, 1045–1050; 12:134–136, 146–148; 13ba:199–201; 18gq:10–14, 111–113.
- **regular (17w:78)**: Parts I and VI (notes 192, 2703, 2804, 2964) give a wider sense "the whole non-large-field part"; the audit of Part VI (D1) disputes it. Text opened (17w:74–96): the sentence only pairs regular with large-field. Wider sense not recorded as a sense; basis I for 17w:78; see Unresolved for "source recurrences".
- **regular activity**: chapter 8 sense (polymer activity `z_γ`) against chapters 4, 9 (additive term). Real change of meaning; text opened at 8:284–287. Name reserved for the chapter 4 sense.
- **request**: Part IV (one meaning) against Parts I and V (three uses). Three senses kept; 11:2057 moved to "finite set of data". Text opened: 10:65–70; 11:2052–2058. Part VI basis I raised to R via 10:66–69, 11:2052–2057, 14:224–227 (audit of Part VI, item 13).
- **reserve**: 11:495 removed from the references (it reads "Retain two cover units", opened); 11:507, 521, 528 added from the audit of Part IV. "Room" removed (next item). Cluster members `excess`, `loss` not treated as synonyms (audit of Part V).
- **room**: moved from "slack in an exponent" to a geometric statement (audit of Part V, item 3); text opened at 13ba:192–195 (13ba:269–271 quoted from the audit, not opened).
- **representative**: Part III's cluster (a name of the operator `W`) rejected in favour of Parts I, II, VI (gauge representative), following the audit of Part III (E4), which read 7:574, 579, 883, 929. Not opened by me.
- **restart / `B_n`**: Part VI's "open point" closed following the audit of Part VI (E2). Text opened: 11:1152–1156; 17w:31–34; 11R:16–19. 4:413 quoted from the audit, not opened.
- **recording estimate**: object determined, word unexplained; equivalent *Fourier mesh estimate* from the text. Text opened: 7:455–462, 760–764. Notes 237, 936, 1217, 1245 merged.
- **resolution heights**: Part I ("undetermined") and Part VI (basis I) against the audit of Part VI (E6). Decided: `θ` and `θ_+`, basis R. Text opened: 18r:52–56; 18lp:221–226, 346–349.
- **response**: senses of Parts I, II, III, IV, V, VI merged into eleven. 6:953 read as the image field, 6:972 as the operator (opened 6:951–954, 970–977); 11:642–648 opened for the curvature response (D); for the one-slot response *correlation functional* chosen over *value of the functional* (Part I) and *correlations with all other fields* (Part VI). 17t:90–91 placed with the chapter 7 sense as in Part I. Pointer row note 933 ("see section 3") merged, no content.
- **response bound `ε`**: hint from 9:167, 374–379 added from the audit of Part IV (U19), marked I; 10:624–627 opened; chapter 9 not opened.
- **replacement / reconstruction**: basis "D by formula in 18lp:266–279" changed to R (audit of Part V, item 6); 14:352–356 opened; 18lp:266–279 quoted from the audit.
- **reflected replica cell**: cell and copy separated (audit of Part IV, U16); the conflicting cluster equivalents (*copies*, Part I; *cell*, Part IV) recorded.
- **relaxed**: 9:840 removed from the word's occurrences (audit of Part III); the pointer "Part II (section 9)" corrected to Part II sections 1.4 and 2.3 (audit of Part IV, E6); 10:95–99 opened; conflict left open (Unresolved).
- **root**: Part II's equivalent *base point* for the tree root and its cluster "anchor, root" not adopted (audit of Part II, D7); text opened at 4:35–37, 5:916–918, 17c:257–260.
- **rooted activity norm**: Part IV ("pinned at a marked site") and Part V ("containing a fixed site") reconciled by 11:265–272 (quoted from the audit of Part IV, not opened).
- **row**: placement of 13:168, 182 and 14:277 (Part I: reference rows; Part V: literal matrix rows) decided for literal matrix rows; 15:274–279 and 7:1058–1060 opened, neither decides its doubtful reading.
- **regularity-stage index `J_m`**: six rows merged (notes 204, 676, 1123, 1715, 2301, 2815); no disagreement left. The stale remarks elsewhere in the note that Part II reads "stage" as a renormalisation step (notes 1098, 1490) are not owned here.
- **regrouping**: chapter 9 reading (9:651–667) preferred to Part II's gloss "the cluster expansion step".
- **raw**: count in chapter 11 given as "11 or 12" (note 11, audit of Part IV 12).
- **replica**: cross-reference added between the chapter 5 field `rep V` and the chessboard "replica cells / replicate" of chapters 11–17; not in the note.
- **retain**: note 436 ("retained", Part II, not in the assignment) folded into the entry so that the R-range is complete.
- **Dropped:** note 393 (headword "R"): it is the legend of the basis code R ("the meaning is read off an explicit sentence or formula, though the term is not formally defined"), not a term. Notes 1882 and 1892 (headwords "R:302–303", "R:300–301"): these are rows of Part IV's table of damaged sentences, for 11R:302–303 ("Coverage of the original prescribed set of large-field sites ensures that an incoming large-field factor cannot occur without such a component"; marked as repaired) and 11R:300–301 ("Apply the factor `m` only to components with an actual selected prescribed set of large-field sites, and to a selected component within each such component"; "a selected component within each such component" and "actual selected prescribed set" unclear, not touched by the repair). They are sentences, not vocabulary, and belong to the list of doubtful sentences rather than to the dictionary.
- **Integration of handed-over material (letter R).**
- reflection cubes, faces; reflected tori (note 1009): new entry *reflection cubes*; 9:322–329 opened to quote the definition.
- reflected normalized directions (note 1229): new entry, basis ?; 9s:294–297 opened.
- residual (profile, response) (note 2214): added to *residual* sense 5 with references. Contradiction decided by text at 14:456–471: `𝓡_{m,ρ} f` is the Laplace transform of the residual profile `f − 𝒞_{m,ρ} f`, not of the annular correction.
- row sum (note 2679): stub to *row* sense 6; 17c:216, 237, 349 added there.
- read-count polynomials (note 257): already in the entry; nothing new.
- regrouping (notes 722, 1678): general use and its references added to the entry; the chapter 9 reading kept for chapter 9.
- relaxed (note 1066): already in the entry; nothing new.
- remote (notes 603, 1663, 1071): new entry, two senses.
- replica census; replica cells (note 2174): new entry *replica census* (13ba:171–175 and 15:258–264 opened); "replica cells" added to *reflected replica cell* with 13ba:53, 18lp:91.
- residue patterns (note 2206): new entry, basis I; 13:363–369 and 15sp:9–12 opened, since the note gives no gloss.
- resolution heights (note 260): already in the entry; nothing new.
- response bound (note 258): already in the entry; nothing new.
- restoration levels (note 1502): already in the entry; nothing new.
- root bound (note 1583): stub to *root estimate*; variants and 11:2027, 2140 added there.
- regular; `E_reg` (notes 241, 192): already in *regular*; nothing new.
- random index (notes 118, 119, 460): new entry ("tag" itself belongs to T).
- replacement error / estimate; `Z_D` (note 2731): added to *replacement* (formula, basis D at 18:154–157, references); 18:152–158 opened.
- retained energy (note 638): new entry, basis I; 6:1453–1456 opened.
- recording (note 1205): stub to *recording estimate* and *recording scale*.
- refinement (coefficient, volume) (note 2202): variants and the chapters 12–16 use added to *refinement*.
- row, 7:1059 (note 1205): already recorded in *row* and under Unresolved.
- recognizes (notes 1002, 1243): new short entry pointing to *chart recognition*.
- reflected slab word `w^♯` (note 2209): new short entry pointing to *slab*.
- replication costs (notes 1863, 1534): 11:795–819 and the stopping level `k(m)` added to the entry.
- retained (note 436; 19:117, note 2861): already in *retain*; "retained phase" named there.
- root-to-site conversion (notes 1549, 2181): stub to *site conversion*.
- raw divergence `div_raw`; raw vector coordinates (note 2693): already *raw* sense 2; reference 17:179–183 and a stub added.
- reconstruction identity / comparison (note 2724): added to *reconstruction* sense 2 as variants.
- reference level / label / coefficient (note 1574): added to *reference label* (variant, equivalent for the map `𝖹_{N,p,d}` with "level" for "scale"). Basis difference (D against R) decided by text at 11:1047–1049: D for the map, R for the label and level.
- regular-restoration bounds (note 2994): stub to *weight restoration*.
- repeated-word identity / bound; repeated copies; replica number (note 2741): three stubs to *uniform in the number of reflected copies*.
- representative (note 1127): no content; nothing added.
- Book-wide decisions applied: *regularity-stage index* ("stage `j`" kept for the regularity class only); *restart* (*restarted history* kept, defined through *history*); *reference label* (*transfer*, "level"); *remote* (*distance* for "clearance"); *row transport* (*parallel transport*). Remarks about the parts of the note and the audits removed from the entries or rephrased as rejected equivalents.

### Letters S

- **selected**: Part II (note 437) filed 4:456, 4:616 and 4:160 under "chosen by the random index, or fixed by the construction"; Part I (note 88) has "finite subfamily" for 4:616. Decided for Part I and the audit of Part II: 4:456 and 4:616 are finite subfamilies of activities, 4:160 a choice inside a proof (text opened: 4:146–148, 158–161, 454–457, 614–617; also 4:209–211, 382–384, 392–394 for the random-index uses). Chapter 6 count 44 replaced by 48 with "unselected" (audit; not recounted).
- **selected, 13:395 and 13ba:30**: Part V doubts its own assignment; Part I omits 13:395; 13ba:29–31 opened, not decisive; left undecided.
- **stage**: Parts III (note 1092, 1098, 1339), IV (1490, 1696), I section 5 (271) and VI section 5 (3049) say or imply that Part II reads "stage" as a step; Part II (512, 656) and Part I 2.10 (167) read the regularity stage. One sense written; text opened at 4:650–652, 5:687–691, 6:20–22, 95–97, 949–951. Basis for chapters 5–6 left at I. Count for chapters 12–16 changed from 22 to 25 = 23 + 2 idiomatic (audit of Part V). Proposed equivalent: *stage `j`* kept; *regularity class* (Parts IV, V) rejected.
- **stationary branch / graph**: Part III (R, same object as the stationary graph) against Part IV (I, "presumably the chosen stationary solution"). Decided for Part III on 9s:34–40 and 10:918–924 (opened). One entry *stationary graph*; proposed *critical-point map*; Part IV's *stationary solution* rejected.
- **stationary chart**: Part III's synonym cluster makes it a name of the critical-point map; the audit of Part III (5:1321–1335; 7:867–869) shows it is the neighbourhood. Separate entry written; text not reopened.
- **stationary tangent**: "representative" removed from the names of `W` (audit of Part III, E4); text not reopened.
- **shooting**: basis I (Part IV) against R (Part VI); R, on 19:21–23 (opened). Equivalent: *tuning of the bare coupling* chosen over "keep".
- **source weight**: basis "? here" (Part VI) against D (Part IV); D at 11:43–49 (opened). Reference 11:812 corrected to 11:808–811 (audit of Part V; not reopened).
- **source locations**: basis R (Part VI) lowered to I; RG:81–83 opened; Part VI's *locations in the formalisation* not adopted (audit of Part VI, D3).
- **source construction**: Part V's two readings kept; the audit's preference for "the text the book was written from" recorded as inferred; 14:184–189 opened.
- **source**: eight senses written from Part I 2.6 and the classifications of Parts II–VI; "an insertion" (Part IV (e)) and the differentiated-kernel "source" of 17m merged into sense 4; "forcing" merged into sense 5.
- **stopping**: Part V's sense (2) gloss "the level `k = k(m)`" widened and the chapter 11 lines added (audit of Part V); opened 11:780–782, 815–817, 944–946; 12:207–213, 249–252, 300–305; 13ba:8–9, 192–195, 211–213; 13sb:9–11, 84–87, 102–106; 18lp:154–160. The chapter 17 "stopping levels" filed under sense 2 (audit of Part VI, 4c-9, 4c-10).
- **sparse**: basis ? (Part IV) against I (Part V); I adopted; 13sb:84–87 and 10:169–173 opened; the text does not state the reading.
- **signed**: Part V's third use (13sb:35) merged into "with its sign kept" (13sb:35–37 opened; I); sense "of either sign" added from 14:520, 681 (audit of Part V; opened).
- **section / microscopic sections**: Part VI basis I and reference 11E:31–38 replaced by R via 2:138–146 and 11E:4–7, 36–39 (audit of Part VI, E10; 11E:4–7, 36–39 opened).
- **schedule**: Part II *fixed parameter sequence `(L_m, j_m, ζ_m)`*, Part IV *scale sequence `(J(m), L_m, a_m)`*, Part VI *fixed parameter sequence* for the wider use at 19:18–21. Two senses written (19:17–32 opened); *fixed parameter sequence `(J(m), L_m, a_m)`* for sense 1; Part VI's equivalent rejected for sense 2 as too weak. "Defined 10:118" corrected to 10:121–147 (audit of Part VI).
- **scale (index)**: Parts I and V *level `m`*, Part VI *scale*; *level* chosen (no text decides; reason given in the entry).
- **same-family / same-history**: Part I and Part V cluster them with the selected trajectory, schedule and histories as one phrase; Part VI and the audit of Part V keep them apart; kept apart on the definition 11:18–19 (quoted in the note; 18:128–131 and 19:17–32 opened). Part VI's *along the same sequence of block transformations* not adopted.
- **spectator**: Part II *the remaining insertions; auxiliary insertion* against Parts I, V *spectators, defined once*; the latter chosen. Sense 2 (2e) from Part III; 2e:39–41 opened.
- **separation**: sense "mutual distance / pairwise distinct" added (audit of Part II, D6); for the separating property the text's "separating family" kept, Part II's *nondegeneracy* rejected. Part VI's *separation* for `clearance` conflicts with Part II's *distance*; *distance* recommended.
- **separated**: count 67 replaced by 63 (audit of Part V).
- **shell**: multi-sense entry assembled from rows of Parts II, V, VI and the audit of Part II (4b); for the shell flux Part II's *smeared charge* rejected (audit E4, citing notation.md line 165); text opened only at 14:356–359 and 11:264–272.
- **score**: Part I lists it as new in chapters 17–19; Parts II, III, IV, VI have it from chapter 6; one sense (6:1528–1531 opened).
- **subpower**: Part V files it under "open items of Part II clarified"; it is defined at 6:822–823 (Parts I, II); 18lp:15–18 opened.
- **supplies**: count for chapters 12–16 changed from 20 to 19 (audit of Part V).
- **step**: reference 6:171 added for "update" (audit of Part II, E6; 6:170–172 opened).
- **soft constraint**: entry created from Part I (note 275) and Part III (1061, 1265), with the restriction of the audit of Part III (E1): "block penalty" in chapters 7, 9s is the penalty term, not the constant; 1:408–410, 419–421, 7:573–575, 19:17 opened.
- **safe chart**: the "tree comparison" is the nonlinear estimate 5:1009–1015 (Part III and its audit) and not Part II's linear inequality; text not reopened.
- **site conversion**: Parts I, IV, V agree; 11:264–272 opened to confirm basis R.
- **site norm**: Part III's "support norm" kept as inferred; Part I's warning that the attachment and rooted norms are not verified to be the same norm kept.
- **slab**: the chapter 11 uses (11:844–846, 876) added from a grep of the text; relation to the chapter 14 definition marked inferred.
- **strip**: third sense (chessboard strips, 1:315–318) and the chapter 13 uses (13:84, 368; 13ba:247) added from the text; the note has only two senses (Part VI) and "strip count" inside the row `cell` (Part V).
- **stop backwards**: "middle and output stopping levels" identified with the two stops of 17w:31–33 (audit of Part VI, inferred); 17w:31–33, 17m:431–433 opened.
- Dropped: note 384 ("**Status:**" line of Part II) and note 875 ("**Scope.**" line of Part III): headers, not terms. Note 1163 ("**stage**: see 2.2 …") is a cross-reference, absorbed in *stage*.
- Integration of handed-over material (letter S). Book-wide decisions applied: *level `m`* / *step* / *stage `j`* (entries *scale*, *stage*, *step*); *the penalty parameter `b`* (MT:12) replaces *penalty coefficient `b`* in *soft constraint*; *the stationary tangent* replaces *derivative of the stationary map* as the proposed name in *stationary tangent*; *distance* for `clearance` and *separating family* (entry *separation*); *spectators*, *history* kept; *cutoff-failure event* used in *small-coordinate event*; the "graph" of 11:379–382 and 12:82–94 (both read) distinguished from the *stationary graph*. Remarks naming Parts and audits inside entries rephrased neutrally.
- **squared group distance** (note 555): new entry.
- **scalar discrepancy** (note 1016): stub to *discrepancy* (sense 2); the handed-over basis R against the note's I decided by the text, which prints `f(d)` at 9:757–759 (read); line added to *scalar*.
- **scalar `v_sc`** (note 1074): added to entry *scalar* (variant; references already present).
- **slab margins** (note 2207): added to entry *slab*; stub.
- **stationary tangent `W`; smooth representative `W_a`; `W_s`; forest representative `W_F`** (note 2672): added to entry *stationary tangent* (5:1151, 17m:263–264, split basis D / R / I, `W^rad`); stub *smooth representative `W_a`*; bare symbols skipped.
- **score source** (note 2699): already in *source* (sense 4) and *score*; stub.
- **signed local transport** (note 3036): new entry, basis ? (18:172–175 read; "signed local transport" is at 18:174).
- **same-data restart conditions** (note 258): entry exists, nothing new.
- **scalar principal alias** (note 942): already in *scalar* (sense 2); stub.
- **schedule; scale schedule; common schedule; nested schedule** (notes 507, 2303, 2653): entry *schedule* already has both senses and all references; nothing new.
- **seeded sector / unseeded law** (notes 256, 1719, 2308): entry exists, nothing new.
- **selected slot** (note 258): entry exists, nothing new.
- **shell** (notes 2263, 2748, 2799): entry *shell* already has these senses and references; distribution over chapters added.
- **small-coordinate event** (note 606): new entry.
- **spectator responses** (note 2762): entry exists; see-also to *correlation responses* added.
- **straight** (note 1048): entry exists with 7:1112, 1154; nothing new.
- **strip count** (note 2206): stub to *strip* (sense 3) and *cell*.
- **support compression** (notes 257, 1226): entry exists; quotation 9:230–232 added (read).
- **support exponent** (notes 605, 2800): new entry (17m:330–332, 9:230 read).
- **second cluster expansion** (note 975): new entry.
- **soft correction `a_s`** (note 1524): new entry.
- **squarefree polynomial** (note 3009): stub and entry *squarefree source algebra* already have 17w:86; nothing new.
- **stationary units** (note 994): new entry (9s:163–166 read).
- **stencil** (note 599): entry exists, nothing new.
- **suppression** (note 1637): new entry.
- **selected site factor `X_z`** (note 1595): new entry; pointer in *selected* (sense 1).
- **separate quadratic correction** (note 570): new entry, pointing to *inherited loop action*.
- **source variable incidence** (note 1548): stub to *incidence*; line added to *site conversion*.
- **split-field definition** (note 945): new entry.
- **subpower inverse terminal coordinates** (note 2154): stub to *inverse terminal coordinates*; variable named in *subpower*.
- **selected / retained / chosen phase** (note 2756): already *selected* (sense 7); stub *selected phase*.
- **soft-block penalty `b`** (note 2758): already in *soft constraint*; stub; proposed equivalent changed to *the penalty parameter `b`*.
- **spatial exponent `p_0`** (note 912): new entry.
- **sparse stopping scale** (note 1534): entry exists; references to the two companion phrases of 10:169–172 added.
- **scalar correction** (note 1528): already *scalar* (sense 3); stub.
- **slab kernel** (note 1579): added to entry *slab* (11:842–845 read); stub.
- **spin operators** (note 2218): new entry (14:900–904 read).
- **stage entrance** (note 1495): stub to *threshold for the starting scale*; line added to *stage*.
- **Symbols** (`𝒰_F`, `𝓡_m`, `𝓘`, `I_G`, `J_G`, …): skipped as symbols.
- Section "Material for other letters" deleted (routed).

### Letters T–Z

- terminal: Part I (note 190) says chapters 5–6 use the word differently; Part II (508, 689), Part IV (1655) and two audits say the sense is the same. Text opened (5:703–707): same sense, the finest scale `N`. A second sense (fine end of a comparison not starting at `N`) is recorded for 17m:426 on the audit of Part VI and 11:910–916; 12:131 kept at I after opening 12:129–140.
- terminal norm bounds: basis `?` (notes 2714, 3032) raised to "R via 11:910–916, partly settled" on the audit of Part VI; text opened (17m:422–442). The other four phrases of that row stay `?` and are in the material for A, E, I, P.
- tail: audit correction applied, 17c:259 is the initial vertex of a link (text opened, 17c:257–260); "tail `U`" (note 528) merged as sense 4.
- tail events: Part IV (1853, 1915–1916) undetermined or filed with the large-field part; audit of Part IV says chapter 6's events. Text opened (11R:42–46, 281–285, 307–312): decided, basis R.
- tangent: note 248 kept; text opened (17c:46–53, 110–113); the `W` of 17c:48 remains unidentified (see Unresolved). "Representative" removed from the names of `W` (audit of Part III).
- test: audit of Part II applied, 4:483–493, 6:83, 6:687, 6:1340 moved from "indicator" to "condition" (text opened). Equivalent for the pairing sense: Part I "value of the functional" against Part V "correlation functional"; the first chosen, since the phrase names a value. Senses of Parts I–VI merged into nine.
- thermal: three rows (236, 934, 1250) agree; text opened (7:229–234, 763–766); basis kept at I.
- threshold: audit of Part III applied (senses `t` and period threshold in chapters 2, 2e, 9; text opened at 2:326, 9:19, 2e:210). "Mesh threshold" filed as sense 3. 17m:197 left unassigned (text opened: "the stage orders and thresholds have been chosen").
- threshold for the starting scale: audit of Part IV applied, the terminal delays of 10:107–112 are conditions of the same kind (11E:29–30, 106–113; not opened by me, quoted from the audit).
- top polynomial extraction: Part I (229) "probably, inferred" against Part VI (2995) "R"; text opened (17w:96–103, 11:2083–2089): R for the identification with the `T` of 11:2085–2088; the further identification with the common localization map rests on a label and `notation.md`.
- tower: audit of Part II applied, second sense "the direct sum itself" and basis D for the first (text opened, 3:429–433, 460–470).
- trajectory: no owned row; entry compiled from Part I (166, 272), Part III (1268), Part V (2409, 2420) and the audits of Parts II and III (4:20 opened). The cluster "sequence of scales and couplings" is not one object (audit of Part III, not reopened).
- transfer: no owned row; entry compiled from Part I 2.8 and Part VI 3.12.
- transport: rows of Parts II–VI merged into six senses; 4:35 added as the place where parallel transport is introduced (audit of Part II; not opened). Note 2763 ("transporting all coefficients together", RG:17) merged into sense 3; its equivalent "by propagating … through the block steps" replaced by Part I's *transfer*. Notes 1042–1044 merged into senses 1 and 2.
- tree comparison: Part II (548) attaches all references to the linear inequality; Part III (1002) and its audit read 4:296 and 9s:139 as the nonlinear estimate. Text opened (4:294–298; 5:998–1016, 1034–1041; 9s:137–142): two senses.
- trial: Part IV "local observable (to be approximated)" and Part V "candidate observable" combined. Protected trial: Part V's guess "with small-field cutoff" rejected, the audits' reading adopted with basis I (text opened, 11:1062–1068, 2304–2309; 13:228–233).
- trial descent: basis I (Part IV, 1571) against R (Part VI, 2711); R on the audit of Part VI (11:890–917, not reopened). Equivalent: the section's own "backward comparison" kept, Part IV's paraphrase recorded.
- trace functional: the row's equivalent ("coordinates before passing to the quotient by the equation of motion") describes the raw coordinates, not `ρ`; it is passed to R, and `ρ` is "keep, define once".
- unit: equivalents of Parts I, III, IV, V for the identity field unified as *identity field*. Notes 1624, 2709 merged as sense 3 (stub *units of support exponent*). The audit of Part IV notes that 11:495 has "cover units" and not "reserve"; the reference is kept under sense 3.
- unmarked gas: no owned row; entry from note 2148 and the rejected-equivalents table (341); text opened (12:178–184; 18lp:184–187).
- unselected: chapter 6 occurrences added from the audit of Part II (6:1339–1341 opened).
- vacuum bound / vacuum normalization bound: notes 2190, 2713, 2996 merged into one entry on the audit of Part V (same form of bound at 12:243 and 11:808–809; 13sb:24–25); the identity of `q_r` with `q^site` stays inferred. Part V's equivalent replaced because it loses "per site".
- volume: no owned row; entry from the audit of Part II against the cluster at note 657; text opened (5:189–191; 6:503–505): number of sites, not side length.
- warning: Part II (680) cutoff remainders; Parts I (244) and IV (1716) cutoff-failure events, Part IV with basis R / I. Text opened (6:1474–1477; 11:317–321): not decided; basis I, both readings stated.
- weight: place of definition corrected to 2:50–51 (Part III against Part II; audit of Part II; 3:168–170 quoted from the audit). Senses of chapters 4–6 added from that audit. Source weight: basis `?` of Part VI replaced by D (11:43–49) on the audit of Part VI.
- weight restoration: notes 227, 2994 and row 1541 agree.
- width: notes 212, 706, 1720, 2249, 2361, 2801 and the width part of 1127 merged; the precise statement is 10:375–381 (audit of Part V).
- window: nine groups of rows merged into five senses. Audit of Part VI applied: four new senses in chapters 17–19, not three; the basis for 17:140 is I. Note 3010 ("window … requests") merged into sense 3.
- word: audit of Part VI applied, 17:34, 17:44, 19:105 are field words and the general definition is 13:282, not 14:23 (text opened). Part II's sense (i) (3:234) and Part V's Euclidean word (13:282) are one sense.
- Wilson initialization: notes 724, 1120, 1684 agree; no equivalent is proposed by the note.
- Owned entries not given an entry of their own: note 3008 ("what crosses in first crossing"), 3039 ("why contact"), 2393 ("why the map `G` is called a graph"), 3028 ("with these same frames"): their headwords are questions about terms of other letters, and their content is in the material for F, C, G, F. Note 1585 (envelope) and 2724 (field reconstruction) have entries here under the first word as written and are repeated in the material for E and F.
- Integration of handed-over terms (one line per term):
- unit column (M1, note 911): added to *unit*, sense 1. The hand-over reads it as a basis column `P_d^loc[b_{d,i}]`, the entry had it under the identity field; decided by text at 2:259–260 ("The unit column is one"): the basis column at the basis element `𝟏`. "Column by column" belongs to C.
- undamped measure (M1, note 2211): new entry (text read at 14:416–422).
- top (M1, note 2662) and top level (M2, note 1502): new entry *top level*; cross-reference added to *top polynomial extraction*.
- unreparametrized remainder map `J_G` (M2, note 2142): new entry (text read at 12:89–92); the graph `G` is not renamed.
- vector-map space (M2, note 2238): new entry with the corrected reading (14:816–822); cross-references added to *Ward kernel* and *Ward sum*.
- Ward sum (M2, note 2238): already in entry *Ward sum*; nothing new.
- Warnings (M2, notes 1126, 1719, 2308): added "ch. 1, 2" to the non-occurrence remark of *warning*.
- with these same frames (M2, note 260; own notes 2951, 3028): new entry, basis `?`.
- word measures (M2, note 2212): new entry (text read at 14:422–423).
- tied (M3, note 2225): new entry; weakly / strictly ordered heights: new entry *weakly ordered heights* (strictly ordered as variant).
- tree gauge (M3, note 1049): stub to *tree slice*; variant, references of chapters 7, 9, 9s and the "forest" remark added there.
- unmarked gas (M3, note 2148): already in entry; nothing new.
- tag-count factor (M4, notes 1001, 1222; M7, note 1604): new entry; the hand-overs say "undefined" (9s) and "number of values of `α`, basis I" (11R); one entry with basis I for both places (text read at 9s:134–135, 11R:357–359).
- tag-coincidence radius (M4): new entry, basis `?` (9s:221–222 read).
- tag average (M7, note 1604): new entry.
- transverse-to-line axes (M4, note 2216): new entry ("line time axis" belongs to L).
- uninflated (M4, note 1547): new entry.
- unmarked (M4, note 1543): new entry.
- tag `d` (M5, note 900): already sense 2 of *tag*; nothing new.
- tolerance exponent (M5, note 1645): new entry.
- torus side; torus size (M5, note 515): stubs to *torus period*; *See also* period added there.
- true-length (M5, note 1645): new entry.
- weaken (M5, note 1645): new entry.
- weighted quotient (M5, note 949): stub to *quotient estimate*.
- word (M5, note 1811): already senses 4 and 5 of *word*; nothing new.
- wrapping; wraps (M5, notes 518, 1059, 2821): stub to *nonwrapping*.
- window (M6, note 2647): compared with *window*, no contradiction (17:140 is I in both); the remark on the two attachments of "comparison level" (17w:31–33, 100–103; 17m:136) added.
- walk (M6, note 542): already in entry; nothing new ("route matrices" belongs to R).
- Trace norms and recording (M6, note 936): new entry, basis `?`, pointing to *recording estimate*.
- total (raw angular, shell) response (M7, note 2217): new entry *total response* (text read at 14:776–777, 796).
- weight restoration; restored weight (M7, note 1541): already in entry; lemma lines 11:1436, 1471 made explicit.
- "will be spent" (M7, note 967): new entry.
- Book-wide decisions applied: *the stationary tangent* as equivalent in *tangent* (sense 1), *transport* (sense 2) and *Ward sum*; *level* for the scale index in *terminal*, *terminal map*, *threshold for the starting scale*, *Wilson initialization*, *window*; *identity field* in *unit removal*; *transfer* against *propagation* in *transport* and *trial descent*; `b` named the penalty parameter in *transport*; *cutoff-failure event* in the cross-reference of *warning*. Remarks about the parts of the note and the audits removed from the entries, rejected equivalents and unresolved readings kept in neutral wording.

### Letters gaps

Opened in the text (repository /Users/mgubi/ym-terminology, chapters/):
- 3:480–496, 773–781, 786–816, 828–831 (separating family: the term stands in two titles, basis R not D; `𝒩_D` at 3:797–803).
- 4:14–19, 170–175, 200–211 (block average, block-average patch); 4:30–33, 74–77, 361, 390, 393 (fallback); 4:432–443 and 8:284–287 (activity); 4:672–678 (reachable).
- 5:928–937, 986–995 (forest chart; linearisation `𝒬 = M + d_{0,c}R`; straight average).
- 6:41–47, 169–173, 457–460, 693–697, 1016–1019, 1341–1346, 1543 (block average, update, patch, chart, stored, export).
- 9s:220–222; 10:749–751; 11R:282–284; 17m:39–43, 88–90 (chart).
- 11:284–290, 351–353, 376–382; 12:80–84, 113–116 (remainder; the three classes `t_C = m, l, 1`).
- 13sb:148–155; 17:136–143; 17w:30–37 (overshoot); 17c:89–93, 338–342, 358–361 (update, averaging patches).
- Occurrence counts by grep over chapters/*.tex for: readout (0), export (1), stored (1), reachable (1), update (3), overshoot (3), fallback (3), parallel transport (3), local representation (4), remainder (about 110 lines), block average (per chapter).

Audit corrections applied: A2 E6 (update: 6:171, not 5:1380 / 6:950); A2 D6 and cross-chapter item 6 (separating family kept, not *nondegeneracy*; "separated" is another word); A2 D9 (letters `Q`, `M`, `𝒜` in *block average*); A3 E6 (stationary chart is the domain, not the map, in *chart*); A4 U13 (remainder is not a synonym of nonprincipal) and U14 (inflation is not a loss), A4 E1 / A5 item 1 (remainder map is `R_G`, `J_G`, not the graph).

Found beyond the list given:
- Further dangling See-also items, all retargeted above: spectators, origin, defects, copies, atoms, "mass (of a kernel)", "row (factorisation sense)", the two "lift (…)" items, "response (Laplace transform …)". Items of the form "X (sense n)" were left alone when the headword X exists.
- `export` had no entry although the entries `declared` and `inputs` name it; a short entry is added.
- `overshoot` also occurs at 13sb:154 (first-below scale), which the old note does not list; recorded in the stub.
- `local representation` occurs at 11:740 and 13ba:162 besides the note's 11:19, 122.

Terms reported as possibly without a home:
- column by column: has a home (variant of `basis column`). No action.
- route matrices: has a home (variant of `route`, sense 1). No action.
- strictly ordered heights: has a home (variant of `weakly ordered heights` and of `height`). No action.
- strict attachment margin: has a home (variant of `attachment` and of `margin`). No action.
- declared / declaration: has a home (`declared`); its See-also items stored and reachable now exist.
- post-ratio constants: variant of `pre-ratio constants`; a stub is added because "fixed-ratio constants" has a heading and this one had none.
- measurement magnification: has a home (variant of `magnification`). No action.
- first crossing / overshoot: `first crossing` exists; stub `overshoot` added.
- non-occurrence remarks: `detector` already carries its remark (labels only); `readout` gets an entry stating that it does not occur; `table` has an entry for its single occurrence (18:72) but says nothing about chapters 1–11. Suggested addition to the *Across chapters* line of `table` (I did not edit the file): "No occurrence in the prose of chapters 7–11; the table at 9:123–134 is referred to through its 'rows'."

Unresolved:
- chart: whether the "small-field chart" / "ordinary chart" (10:97–98, 750; 13ba:37; 17m:89, 173) is the domain of the logarithmic chart or a smaller set, and what "the common chart" of 9s:221 is common to, is not decided by the text; basis I.
- block-average patch: that "block average patch" (6:459; 7:599) and "averaging patches" (17c:360) name the patch `Ly + 𝔹_R` of 4:172–173 is an inference; the "padded block" question stays open as in the entry `padded block`.
- remainder: only the uses treated by the old note are classified; the remaining occurrences (chapters 1, 5, 7, 9, 10, 14, 17, 19) were not surveyed.
- stopping levels: retargeted to `level`, which glosses them (basis I); the entry `stop backwards` also lists "stopping levels (chapter 17)" as a variant, so two entries claim the variant. The two glosses do not contradict each other.
- small-field condition: there is no entry for the unqualified phrase and the old note has no row for it; the See-also item of `relaxed` is retargeted to the only entry that treats the condition. If an entry is wanted, the nearest note material is the row "indicator" (note line 448) and the cluster "small-field indicator `h_X`" (note line 1275).
- holonomy and parallel transport are standard terms that the text itself uses; they are given stubs to `transport` (sense 1) rather than full entries.

### Concepts with several names

Decisions where parts disagreed or an audit correction was applied; "read" = chapter lines opened for this merge.

- Scale index: *level* chosen (Parts I, IV, V) over *scale* (Part VI). `stage` removed from three rows (note 271, 2418, 3049) on 4:651–652 and 10:25–26 (read).
- "The fixed construction of chapter 10" (note 272, 1268, 2420) split into schedule, history, trajectory and "same family" on 10:5–9, 10:118, 11:18–19, 13sb:50–51, 13ba:50, 5:303–305, 1:465–467 (read). Part V's phrase kept for the schedule only.
- Constant `b` (note 275, 1265): "block penalty" restricted to ch. 4–6 and 19:17 and "penalty Hessian" removed, on 7:475–477, 523–524, 873–875, 4:226, 6:21, 1:409, 1:420, 5:102 (read). *Block parameter* chosen because "block penalty" changes meaning in ch. 7.
- Operator `W` (note 274, 1263, 1928): "representative" removed on 7:574, 5:1151 (read); Part I's "not synonyms" confirmed against Part III.
- Critical-point map (note 1264): "stationary chart" removed on 7:867–869, 5:1321–1335 (read); Part III's reading of "stationary branch" (9s:36) preferred to Part IV's "undefined".
- Lower bounds (note 289, 1270, 1271, 1905, 1907): split into starting scale / `β̂` / block ratio / operator; "margin" moved to slack on 9:701–702, 794, 950, 9s:220–221 (read); terminal delays identified with starting-scale conditions on 10:107–112, 157–159, 11E:29–30 (read).
- Large-field event (note 280, 1916): split into two uses on 6:7–11, 6:1018, 10:532, 595–597, 11:1613, 11:150–151, 1487–1497, 1932–1933, 11R:283–284, 308–311 (read). Part IV's proposal *large-field event* rejected for the first use; Part I's blanket rejection does not cover the second.
- Tail event (note 1915, 1916): moved from "large-field part of an insertion" to the cutoff-failure row on 11R:43–45, 283–284 (read).
- Restart sequence (note 1911): "auxiliary history" restricted to 11:736, 11R:5 on 10:824–827, 918 (read).
- Loss / factor (note 288, 1909): "inflation" removed on 11:274–292 (read).
- Slack (note 287, 2424, 3062, 1908): "excess", "loss", "room" removed on 6:326–329, 13sb:6–7, 13ba:193–195, 269–271 (read); example 11:495 dropped (audit A4 E8, not reopened).
- Distance from a boundary (note 2423): not merged; Part V §1.2 preferred to Part V §5 on 13:88, 13:334–335, 14:99 (read).
- Side length (note 657): "volume" removed on 5:190, 6:504, 5:879 (read).
- Base point (note 663): merge of anchor and root undone on 4:435, 4:36, 5:917, 5:1242–1246, 6:1462 (read).
- Enlarged block (note 659, 1280): "padded block" removed (I) on 7:599–600, 628, 4:16–17, 4:298–299 (read).
- Transported curvature (note 1267): reduced to one object on 2:171–175, 2e:60–65, 2:362, 7:147 (read).
- Majorant (note 1284): "envelope" removed on 9:793–794 (read).
- `h_X` (note 1275): generic "event indicator" and "small-field conditions" removed on 9:19, 283, 837, 510 (read).
- Activities with prescribed sites (note 281, 1917): compulsory and mandatory factors separated on 10:654, 11R:159–161 (read).
- Value of a functional (note 279, 1920, 2431): "probe" removed on 18:38, "detection" on 11:960, 976 (read); functional and value separated on 13:120–122 (read); three different proposals reconciled.
- Cell and copies (note 1921, 284, 2425, 3054): "copy" removed from cell and "replica cells" from copies on 11:836, 846, 1122 (read).
- Correlation function (note 2422): "response", "hierarchy / family" removed (13:120–122 read).
- Subsequence (note 2426): "cofinal" removed on 13ba:305–306 (read).
- Its complement (note 1914): "remainder" removed on 11:379–380, 286–290 (read).
- Spectators (note 276, 2421, 3053; Part II row 613): *spectators* chosen over "the remaining insertions"; 2e sense excluded on 2e:39–41 (read).
- Separating family (note 278, 2432): text's own word at 3:484 (read); Part II's "nondegeneracy" rejected.
- On-shell polynomial space (note 665): the proposed name is already the text's (3:149 read).
- Small-field part (note 1276, 3056): `regular` kept as a member for ch. 8 only on 8:285–286, 9:150, 17m:106–115 (read).
- `exp((log log β̂)²)` (note 3059): `M^cut` of 4:411 chosen as the one symbol; names of 11:746, 11R:14, 14lc:24 added (4:411, 17:104, 17w:29, 17m:138, 11R:14 read; 11:746 and 14lc:24 taken from the note's symbol rows).
- Chessboard seminorm (note 283, 2437): reference 11:820 corrected to 11:819; `‖·‖_{𝒞_k(y)}` (13ba:205) added (read).
- Step (note 656, 271): reference for "update" corrected to 6:171 (read).
- "For all large `N`" (note 286, 2427) and "lower bound on the cutoff" (note 1906) merged: same condition (11:1123–1131 read).
- "Unused extra regularity" (note 3062) merged into slack; "bound" (note 3063) merged into factor; "RG transfer of a function or current" (note 3050) merged into the block-map transfer row.
- No owned row was dropped. All 122 rows of `M9-SYN.tsv` are cited in the last column of a table row (tally at the end of the merge; several note lines are cited in two rows where the cluster was split).

### Symbols

- `χ` (note 745): basis moved from "4:56" to D at 1:90–95; 4:56 does not contain the symbol, 4:71 is the first use in ch. 4, 6:49 a reminder (read).
- `w` (note 746): "penalty function (5:1048)" dropped as a separate meaning (it is `w` of 1:92; read); five ch. 5–6 meanings added.
- `B` (note 3087, with 1296, 1937, 2452): the "open mismatch" of Part VI closed: 4:413 (`B_m=⌈(log β̂_m)²⌉`), 11:1152–1156, 11R:15–18, 17w:29–33, 17m:432–438 read; 17m uses the ch. 4 radius, 17w the restarted one.
- `K` (note 1298): `𝒦` corrected to "the `β`-coefficient of the path action" (9:21–28 read); (note 2455) 14:549 corrected to a bound on exponents (read).
- `R` (note 2457): `𝓡_m` reference 11:820 → 11:819 (read).
- `T` (note 2459): `T=log(1/r)` reference 18lp:15 → 18lp:300 (read).
- `Q` (note 2461): `Q_{A,B}` reference 14:860 → 14:861 (read).
- Off-by-one references of Part VI corrected from the text: `ρ` 18:284, `Z_D` 18:156, `B_dw` 18:85, `W^rad` 17c:191, `τ` 17c:256–257 (read).
- `W_a` (note 1294 against 3074): Part III says `notation.md`:242 "contradicts" the text; Part VI says it agrees on which representative is "actual" and conflicts only in "forest-coordinate". Part VI's statement adopted (5:1151, 7:574 read; `notation.md` not reopened).
- One operator under `M`, `𝒜`, `Q` (5:156, 535, 989, 993; 6:370–374 read) and one quantity under `q`, `q^site`, `q_r` (11:808–811; 13sb:24–28; 12:243–247 read) recorded in the rows `M` and `q`; `cov_B` / `c_B` (4:587–589; 9:419; 6:1297; 11:1368; 12:229; 13ba:132; 18lp:78 read) in the row `c`.
- Rows added that are not in the note's tables: `d`, `p`, `s`, `Y`, `Γ`, `Δ`, `π`, `φ`, and separate rows for `u`, `X`, `I`, `G`, `U`, `V`, `η`, `δ`, `ν`, `μ` that the note had only inside its two "each has at least three uses" rows (note 1957, 3098).
- Additions reported by the audits and not entered, because I did not confirm them at a line: `d` "trial correction" (9:756); `d_I`, `d_c`; `A_M`, `A_d`; `V` as "volume" beyond the form of 11:809; `p_o`; `k` "level" compounds; the Part VI list "three or more meanings across 17–18" for `c`, `h`, `u`, `p`, `N`, `G`, `V`, `E`, `I`, `J`, `λ`, `ν`, `δ`, `η`, `μ`, `ω`, `α`, `θ` (no lines in the note; only the lines shown in the rows were found).
- Rows of the note merged: all 109 rows of `M9-SYM.tsv` are cited in a "Note" entry (the two collective rows 1957 and 3098 are cited in each row they contribute to). No owned row was dropped.

### Decisions of 25 November 2026

The author's decisions behind the text changes of commits `c5bd232d`, `d869e433` and `080d934e` (issue 1 of the fork; issue 2 for decision 27). Reports in `decisions-2026-11-25/`. The dictionary entries named in brackets were updated on the same day.

- **5.** `R_I` is called a Wick product with respect to the free field, and the recursion stays (11:2066; 14lc:47, 53). [*corrected*; *Wick product*]
- **9.** The forest prescription (18:398–421) is described as "formalized but not used in the main result" (18:419). [*forest prescription*]
- **11, 12, 34.** The remaining sentence repairs of Appendix D applied, with formulas from the sources (`repairs-apply.md`; corrected by `repairs-review.md`). [Appendix D]
- **24.** 17c:55–68 rewritten along the route of the formal proof (`W_s` and polynomial fields); label `ch17:current-alias` replaced by `ch17:polynomial-four`; the alias argument removed there and, after review, at 17c:71–87, 323–330 and 17m:232–234 (`ch17c-polynomial-route.md`, `ch17c-polynomial-review.md`). [*polynomial field*; *alias*; *base-point average*]
- **27.** Assumption `ch09:forest-assumption` kept as a stated hypothesis; chapter 11 adapted, with a new unproved Hypothesis (H) at 11:335; issue 2 of the fork (`ch11-forest-adaptation.md`, `ch11-forest-review.md`). [*Hypothesis (H)*; *average over the forests*; *forest*]
- **28.** `M_core`, `M_act`, rooted and centered coordinates traced; report only, text not changed (`contact-matrices-trace.md`). [*`M_core`, `M_act`*; *rooted coordinates*; *centered coordinates*]
- **33.** "Inverse coupling" for `β` (4:407, 418, 533; 11:1670); "reference coupling" stays as the short name of `β̂`; "bare coupling" stays. [*inverse coupling*]
- **36.** "Admissible periods in continuum units" in the main theorem (MT:14–15). [*admissible periods*; *physical*]
- **42.** "Common trajectory" confirmed. [no change]
- **45.** "Smoothing order" (11:351–352, was "kernel order"); "activity arrays" (10:6, was "coefficient arrays"); "lower bound on the partition function" (17w:97, was "positive partition estimate"). [*smoothing order*; *array*; *lower bound on the partition function*]
- **47.** "Failed-cutoff factor" kept and defined at 11:1476. [*failed-cutoff factor*; *cutoff failure*]
- **48.** "Requirement on the starting scale" / "conditions on the starting scales" (13ba:258, 261, was "coupling-threshold"). [*requirement on the starting scale*; *coupling threshold*; *threshold*]
- **49.** "Local charges" kept in the theorem; 14:408 says that the local generators `p_b`, `Y_d(K)` are those charges. [*local charge*; *local generators*]
- **50.** The "failures" of 17m:121–129 are large fluctuation-field events. [*failure*; *complementary*]
- **51.** 17m:193, 265, 291, 303, 307 say "regular terms of the differentiated kernel". [*differentiated kernel*; *regular terms of the differentiated kernel*]
- **52.** "Coupling constant renormalization" is the operation; `q_m` is "the coefficient `Δ` of the coupling constant renormalization" (10:421, 816). Not adapted: 10:446, 651, 772, 842–843, 902; 13sb:26. [*coupling constant renormalization*; *reset*]
- **15c.** The record appendices (H, J, K, L) were moved to this file.
- **15d.** No upstream pull request yet.

---

<a id="appendix-k"></a>

## Appendix K. Findings from the source manuscripts and the Lean formalisation

One row per term traced beyond the v3 text. The entries carry the detail. "Lean definition read" means the declaration was read as source text and matched on its formulas; nothing was elaborated or built.

### First round: terms the v3 text left undetermined

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| moving comparison fields | 3:576 | Rescaled interacting fields whose labels depend on the scale index and converge to a fixed free-field label (here the trace field converging to a multiple of the free curvature square); the estimate is convergence of their correlations to the free ones. | Martin `trace-asymptotic.tex:192–195`, `trace-scribe-producer.tex:1456–1459`; Lean `YM.OPE.Cards.variation` (general statement only) | partly |
| seeded sector / unseeded law | 6:1544; 9:283–284 | A seed is a selected large-field element. A seeded sector has non-empty selection; the unseeded law is the Gaussian law of the sector with empty selection of plaquettes and edges, on the same forest. | Lean `YM.Pressure.Stores`, `YM.Push.SectorMeasure.Seeded`; Martin `gaussian-reassembly.tex:14–17`, `actual-reader-dawn-selection.tex:175–177` | partly |
| output anchors | 6:90 | Coarse plaquettes, addressed by base site, at which the coarse-side energies `E_L`, `E_D` are counted; `H` is those within `4B/5` of `D`. | Scott `B-section.tex:918`; Lean `Stores.outs`, `Stores.hit`, `talll` | Lean definition read |
| likelihood tests, likelihood factors | 6:920, 1016 | The tag weights per coarse site and per coarse bond, multiplied by the number of tags; equal to 1 on the minimising branch. Not the allocation weights `ϑ`. | Martin `gaussian-warnings.tex:116–118, 199–201`; Lean `Tags.siteMass`, `Tags.pinMass`, `Patch.frameMass`, `Patch.predictorMass` | Lean definition read |
| compulsory component region, compulsory cutoff factor | 6:1018, 1461 | Positions within a fixed multiple of `B` (300B in Lean) of the selected component; there the allocation or tag weight is kept as a factor of the component and its cutoff remainder is zero by definition. | Martin `gaussian-warnings.tex:206–208, 225, 281–282`, `gaussian-reassembly.tex:187–192`; Lean `Coat.mandatory`, `Coat.mayor`, `Mask.profiles`, `Mask.tickets` | Lean definition read |
| warning, warning estimate | 6:1476; 11:319 | A cutoff remainder `γ·a − 1` at one address, zero unless a Gaussian coordinate nearby is large; the warning estimate is the joint probability bound `E^n` for `n` distinct remainders to be nonzero together. | Martin `gaussian-warnings.tex:4–8, 131–133, 206–207, 242–246`; Lean `WarningAt`, `Coat.detect` (probability bound not located) | partly |
| protected | 6:694–737 and later | Multiplied by smooth cutoffs in the logarithmic coordinates of the bonds read; on that support the change of variables is exact and the fine links read are fixed. | Martin `compensated-variation.tex:6–9, 151–158`; Lean `Protected`, `protects`, `openedPatch` | partly |
| `𝒰_F` | 6:953, 976 | The operator `W_F` of chapter 5: the stationary tangent in the representative that vanishes on all tree edges. | Martin `local-mean.tex:11–27`; Lean `YM.Precision.extracted`, `stays`, `Inputs` | Lean definition read |
| stage | 5:689; 6:21, 96 | The regularity stage `j` of 10:25: a finite record of derivative order, power, support exponent, path constants, drift bound; level `m` uses stage `J(m)`. Not a step. | Lean `YM.RG.Stage`, `Calendar`, `YM.Pressure.Teller` | Lean definition read |
| direction selectors | 7:427 | The four constant maps `J_a` taking a one-form to its `a`-th component; `M_μ = Σ_a J_a^* m_μ J_a`. | Scott `C-section.tex:259, 348`; Lean `copiesV`, `brigadeM`, `rankAux` | Lean definition read |
| coordinatewise splice | 7:637 | The point with the coordinates of `y` on the axes already traversed and those of `x` on the others; exchanging these coordinates between the endpoints preserves the uniform measure on pairs. | Martin `weighted-frame-penalty.tex:78–83`; Lean `panelSwap`, `swapPanel`, `stopPanel` | Lean definition read |
| recording estimate; "Trace norms and recording" | 7:461, 742 | Bound for the difference between finite-torus Taylor coefficients (mesh means) and the infinite-volume coefficient function (integrals), exponentially small in the side length. | Martin `stationary-output-construction.tex:14–27`, `annulus-recording-yield.tex:65–75`; Lean `YM.Stationary.Recorded` (`noteAt` not read) | partly |
| padded block | 7:599, 628 | Two boxes: at 7:599 the box of radius `(j+5)L` containing both endpoint patches of a coarse bond; at 7:628 the block-average patch of radius `(j+3)L`. Not the macro-box. | Martin `weighted-frame-penalty.tex:77, 96–97, 168–170, 238–243`; Lean `Patch.radius`, `playhouse`, `rent_fit`, `rent_pay` | Lean definition read |
| support compression | 9:231 | The inequality `t·cov(Y) ≤ t T_r + (σ/2)·cov(X)` for a coarse support `Y` in the `rB`-neighbourhood of the coarse image of `X`, valid when `20 t T_r ≤ Lσ`. | Martin `nonlinear-singleton-inheritance.tex:216–219`; Scott `D-section.tex:291–300`; Lean `Release.compressed`, `Walled`, `collapse` | Lean definition read |
| inspected support | 9:220 | The support together with the sites of all plaquettes touching it: what the activity and its small-field test read. | Lean `YM.RG.inspected`, `flags_agree`, `inspected_radius`; Martin `principal-reference-attenuation.tex:175–177` | Lean definition read |
| numerical band margin | 9:950 | The condition `C^drift_j / log 𝓛_j ≤ κ_G/4` on the block ratios (ch10:drift-floor), which makes the inner barriers of 10:212–222 work. | Scott `D-section.tex:847`; Lean `Shoot.band`, `Drifting`, `gates`, `limits`, `Issues.advances` | Lean definition read |
| missing-coordinate factor | 9:77 | `𝔪^{−(N_free − n_act)}`: one factor `𝔪^{-1}` per free bond that is not active. | Martin `gaussian-reassembly.tex:57–63, 105–109` | source text read |
| read-count polynomials | 9:147 | The factors `(1 + s_M)^{d_j}`, `s_M` the number of radius-`B` blocks covering everything the product reads. | Scott `D-section.tex:105, 148, 212`; Martin `high-degree-cluster-prices.tex:98–99` | source text read |
| live tag actions | 9s:127 | For each value `α` of the random index with positive weight, the fine action plus the block penalty computed with the block average of `α`. | Martin `stationary-exterior-receipt.tex:38–61`; Lean `Alive`, `StepData.density`, `Patch.predict` | Lean definition read |
| tag-coincidence radius | 9s:221 | A fixed radius around the stationary point within which all these actions are equal (the block average does not depend on `α`). | Martin `stationary-exterior-receipt.tex:259–262, 282–283` | source text read |
| reflected normalized directions | 9s:296 | The derivative directions of the activity seminorm, restricted to the reflection cube and extended to the auxiliary torus by the coordinatewise fold; bounded by `2t(1+w̄)^ϖ`. | Scott `D-section.tex:417, 425`; Lean `BudgetPoint.dirBound` (fold not sought) | partly |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| Hilbert encoding, encoding weights | 10:381–382 | The path coefficients `c(γ)` are taken in the weighted `ℓ²` space with weight `e^{2δℓ(γ)}`, i.e. `c(γ) = e^{-δℓ(γ)}z(γ)` with `z ∈ ℓ²`. The "summability of the encoding weights" is the condition `Σ_γ e^{-2(δ−w)ℓ(γ)} < ∞` needed to pass to the `ℓ¹` bound at width `w < δ`. | Martin path-attachment-producer.tex:852–871; selected-history-limits.tex:21–23, 94–97; Lean `YM.UVExtension.Projection.Ortho`, `yard`, `via`, `yard_gain`, `pilot` | Lean definition read |
| response bound `ε` | 10:626 | A free constant `ε ≤ 1/16`: the fraction of `C_st β̂^{-11/10}` allowed to the principal regular bound of the one-step output, fixed before the inverse coupling threshold. No response function is involved. | Martin background-test-prices.tex:83–99, 129–131 | source text read |
| block bridge | 10:921 | The linear coarse-to-fine map `W` of one block step, solution of `K_f W = 𝒬^*K_c`, `𝒬W = I − b^{-1}K_c`, with the bound `L^{-1-r}` on `r` fine differences; in v3 notation `W_a`. | Martin selected-history-limits.tex:378–383; quadratic-pole-transport.tex:33–37; inherited-loop-transport.tex:162–165; Lean `YM.Stationary.Bridge`, `Cruise`, `primalV`, `secondV` | Lean definition read (choice of `W_a` over `W_s` inferred) |
| coarse kernel level | 11:352 | The averaging order `J` of the block kernel at the coarse level; "kernel level" and "kernel order" are the same parameter at two adjacent levels. | Martin heading-history-handoff.tex:10–12, 347; Lean `YM.RG.Patch.J`, `YM.RG.Calendar.J`, `Calendar.op` | Lean definition read |
| preselection bound | 11:382 | The one-step error bound `C_d/L + o(1)` as it stands before the block ratio `L` and the inverse coupling threshold are chosen; afterwards it is at most `L^{-2/5}`. | Scott part2/E-one-mark.tex:71; part2/E-section.tex:128 | source text read |
| selected slot | 11:424 | The index (support with prescribed large-field sites) of the large-field activity that carries the large-field remainder of an insertion. The sentence says the expansion around it has no term made of small-field factors only. | Martin heading-history-handoff.tex:313–321; Lean `YM.Source.Coefficient.forced`, `marked`, `Format` | Lean definition read (for the indexing) |
| coarse forecast | 11:725–726 | The deterministic vector `g^{-1}·(fixed matrix)·(curvature of the coarse field)`: the linear prediction of the normalised fine curvature coordinates, about which they fluctuate. | Martin actual-reader-guarded-curvature.tex:5–8, 44–48; Lean `…PhysicalGuard7f546.Curved.forecast`, `flow`, `look`, `flow_spins` | Lean definition read |
| common Gaussian sample | 11:725 | The single joint Gaussian vector from which all fine curvature coordinates, for all subsets of insertions, are computed. | Martin actual-reader-guarded-curvature.tex:5–8, 53–56; Lean `…Curved.wind` | Lean definition read |
| exposure `𝓔` | 11:1285–1293 | The injective linear map from the coefficient space `V_d` to the polynomials of weighted degree `≤ d` in the radial jet variables, sending a coefficient vector to its polynomial; `c_d` bounds its inverse in `ℓ¹` norms. | Martin actual-rank-purchases.tex:545–555; Lean constituents `YM.Labels.Pol`, `Label`, `Frame.coords` | partly (formula `Σ v_i b_i` inferred; no Lean declaration for `𝓔`) |
| front-column | 11:1343 | The one-step coefficient bound `‖x_m‖_1 ≤ C_{m+1}L_m^d‖x_{m+1}‖_1` with the stage column constant `C`; its product gives `D_k = a_k^d∏_{i<k}C_{i+1}L_i^d`. | Lean `YM.Source.TransferData.Based.front`, `YM.Next.Rank.Price.outward`, `reference_size`; Martin actual-rank-purchases.tex:176–188 | Lean definition read |
| corrected body product estimate | 11:1662–1663 | The bound `(∏μ_a)∫∏\|X_a\|dν ≤ ∏z_a` for collections of factors without insertions of a restarted step, with inflation factors `m` (factors with prescribed large-field sites) and `l` (others). | Martin actual-mixed-marked-compiler.tex:102–112; restarted-rank-history.tex:640–662, 698 | source text read |
| same-data restart conditions | 11:1666 | The requirement that the local estimates of a restarted step be proved for the data of its density identity: original path and clipping coefficients, block kernel and Gaussian law. A set of hypotheses, not an estimate. | Martin restarted-rank-history.tex:603–612; actual-local-compiler-handoff.tex:4–7 | source text read |
| alphabet | 11:1911 | The index family of the factors of the connected expansion, with their supports and prescribed large-field sets; "term by term on the original marked alphabet" = for each factor of the original expansion. | Martin actual-corrected-body-compiler.tex:4–9; actual-mixed-marked-compiler.tex:314–322 | source text read |
| `hot(s)` | 11:1934 | The function `h(s) = exp((log log s)^{3/2})` of 11R:14. | Lean `YM.Next.Rank.Perch.hot`; Martin actual-reader-guarded-curvature.tex:527–528 | Lean definition read |
| protected trial | 11:1063, 2306; 13:229 | A local trial on a fixed finite stencil with two bounds growing slower than every power of `a_N^{-1}`: one for its derivatives on small fields, one for its supremum on all configurations. Finite differences written at higher degree are examples. | Martin actual-insertion-derivative-relay.tex:24–35; Lean `YM.Push.RelayDifference.RawProtected`, `clothed` | Lean definition read |
| exterior row | 11R:266 | The capped action terms not assigned to a selected large-field component, one of eight contributions to the unselected exponent. | Martin actual-corrected-body-compiler.tex:93–100, 137–139 | partly (link to the chapter 6 table inferred) |
| finite decorations | 11R:304 | The finitely many label choices (fine large-field sites, attached insertions) of a selected component, entering as a counting factor. | Martin restarted-rank-history.tex:657–660; actual-corrected-body-compiler.tex:346–349, 488 | partly (no formula for the count) |
| tail events | 11R:43, 284 | The Gaussian large-coordinate events of chapter 6, retained as factors where cutoff conditions fail. | v3 6:837–843; Martin restarted-rank-history.tex:698–700 ("warning event") | source text read (entry unchanged) |
| target list, target columns | 11:1237, 1364 | The list `v_1,…,v_r` of right-hand sides of the lift equations `S_{g/θ}Tu_j = W_ρv_j`; the "target columns" are the vectors of the solutions `u_j`. | Lean `YM.Next.Rank.Price.Solves`, `solve`; Martin actual-rank-purchases.tex:208–217, 1026–1028 | Lean definition read ("target columns" inferred) |
| targets | 11:2207 | The fixed configurations of separated points approached by the rounded, rescaled lattice configurations. | v3 11:2205–2207; Lean `YM.Next.Rank.Ship.targets` | partly |
| incidence | 11:258 and 16 further lines | `sup_j Σ_{a: j∈I(a)} ω^{\|I(a)\|}e^{e c_B(X_a)}p_a`: the weighted sum over the terms whose insertion set contains a given insertion. | Martin allarity-marked-propagation.tex:78–96, 1953–1978 | source text read |
| normalized local insertion | 11:353, 895, 1051 | `O_{N,p}(d,c;x) = a_N^{-d}P_d^loc[S_{1/t_N}𝖹^{-1}c](x)`; at an intermediate level, the local section of that level's coefficient on small fields. | Lean `YM.Source.initial`, `TransferData.cylinder`, `Coefficient.exponentialEntry` | Lean definition read |
| site / support / containing-site norm | 8:69–74; 6:1172; 9:518 | `sup_x Σ_{γ: x∈X_γ}e^{αc(X_γ)}\|z_γ\|`: each term counted at every site of its support; used for large-field activities. | Lean `YM.RG.Activities.KBound`, `BudgetPoint.mass`, `YM.Lattice.coverNumber` | Lean definition read |
| anchored norm; remainder norm | 8:75–79; 11:362–366 | The same weighted sum with each term counted at one designated site; used for regular activities. The remainder norm is its version with a single anchor. | Lean `YM.RG.Activities.EBound`, `YM.Source.Coefficient.remBound` | Lean definition read |
| rooted activity norm at `(ω,e)` | 11:1437–1440 | The incidence bound at source weight `ω` and support exponent `e`. | Martin allarity-marked-propagation.tex:1953–1978 | source text read (12:178 still open) |
| graph `G` | 11:379–382; 12:82–94 | A linear map from the coefficient space `V_d` to the remainder arrays at one level with `‖Gx‖ ≤ s_m‖x‖_1`; the density with one insertion is the set of pairs `(x,Gx)`. One step maps `G` to `ΦG = J_GI_G^{-1}` and halves distances, as in the graph transform for invariant manifolds. | Scott part2/E-section.tex:242; Martin fixed-rung-convergence.tex:33–50, 88; Lean `YM.MergeProof.Matric.Gram`, `Gram.step`, `Gram.Within`, `Gram.revenue` | Lean definition read |
| linear graph, coefficient graph | 11:347–911 | The same map in chapter 11, with the supports of the remainders fixed. | Scott part2/E-section.tex:242; Lean `YM.Source.TransferData.entries`, `Based.linear`, `Based.cap` | Lean definition read |
| terminal graph | 12:131 | The selected graph `G_{m,N}` of the history with terminal index `N`; the proposition says its dependence on the graph put in at the fine end `m+h` decays like `2^{1−h}`, so `G_{m,N}` is Cauchy in `N`. | Martin fixed-rung-convergence.tex:92–94, 114–121; Lean `YM.MergeProof.Matric.Gear`, `Gear.voyages` | partly (title not glossed by the source) |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| terminal graph ("Forgetting the terminal graph") | 12:131 | The graph at the fine end of the history with cutoff ("terminal index") `N`. The proposition says that the level-`m` graph depends on the graph supplied `h` levels higher by at most `2^{1−h}`, so the graphs at a fixed level are Cauchy in `N`. | Martin fixed-rung-convergence.tex:92–125; Lean `YM.MergeProof.Matric.Gear` (definition read), `Gear.voyages` (statement read) | partly (the phrase itself is not defined in the source either) |
| exact-cover gas | 12:180–183; 9:593 | The large-field factor of the density: the sum over finite families of large-field activities with pairwise disjoint supports whose prescribed large-field sets cover exactly the large-field sites of `U`, of the product of the activities; equal to 1 without large-field sites. | Lean `YM.RG.Activities.gas`, `Activities.admissible`, `YM.RG.Rep.eval` (definitions read); Martin fixed-rung-convergence.tex:221–233 | Lean definition read |
| unmarked gas | 18lp:186 | The same factor for the density without source variables (activities of degree zero in the sources). | Martin terminal-marked-construction.tex:127–142; Scott part2/G-section.tex:289; Lean `YM.RG.Activities.gas` (definition read; the density with sources of 18lp not located) | partly |
| `q_r`, `q^site`, `q`, `q_k` (vacuum normalization bound, per-site normalization cost) | 11:808–811, 819; 12:247; 13sb:24 | One function of the level: `q_m = 2b_act + κ_m + β b_loc(ρ) + 4D_G log(16/ρ)` with `ρ = β̂_m^{-1/2}`, the exponent per lattice site lost when a coefficient integral is divided by the lower bound on the partition function. | Lean `YM.Vac.treasury` (definition read), `YM.RG.Rep.denominator`, `YM.Vac.suffices_bill`, `YM.Vac.treasury_stage` (statements read); Martin centered-construction.tex:86–110, fullmesh-correlation-cauchy.tex:208–218 | Lean definition read |
| corrected coefficients `R_I` | 14lc:49–57; 11:2066–2070 | `R_∅ = 1`, `R_I = ∏_{i∈I} I_i − Σ_{∅≠J⊆I} G_J R_{I∖J}`: the product of the insertions with the free moments subtracted on every subset; `R_{12} = (I_1−G_1)(I_2−G_2) − (G_{12}−G_1G_2)`. For Gaussian variables its expectation vanishes for `I ≠ ∅`. Whether to call it a Wick product relative to the free moments is an identification from the formula, not in the sources. | Lean `YM.Extra.WeakScaling.corrected` (definition read), `multiply_back`, `finite_comparison` (statements read); Scott part2/E-section.tex:508–521, G-section.tex:279–285 | Lean definition read |
| heat semigroup, heat analyticity | 14:39–56, 80; 15:26 | `E_μ(t) = e^{−tH_μ}`: the self-adjoint contraction semigroup on the reflection Hilbert space induced by translating positive-time words by `t e_μ`; "heat analyticity" is its holomorphy in `Re z > 0`. No heat equation is involved. | Lean `YM.OS.Semigroup`, `YM.OS.Chamber`, `YM.OS.travel` (definitions read); Scott part2/G-section.tex:475 | Lean definition read |
| the source construction | 14:186 | The construction of the source manuscript (Scott, eq. `eq:G-balance`), i.e. that of `14-lattice-comparison.tex`, with `M_k = H_k`; not "construction with source variables". | Scott part2/G-section.tex:240–243; git history of `14-reflection-ward.tex` | source text read |
| admissible comparison depth | 14lc:23 | A level `k` such that the window of levels `[k − h_k(α) − v_k, k]`, `h_k(α) = ⌈(α+2) log H_k / log L⌉`, `v_k = ⌈10 log B_k / log L⌉`, lies in `{0,…,k}` and inside one stage of the schedule. Arbitrarily large such `k` exist. | Lean `YM.Next.Rank.Station.Allowed` (definition read); Scott part2/E-section.tex:48–53, 119; Martin actual-rank-purchases.tex:244–246 | Lean definition read (existence of infinitely many such levels: source text only) |
| coordinate hybrids | 14lc:95 | For two configurations `x, y` of `n` points, any configuration each of whose `4n` coordinates is taken from `x` or from `y`; the intermediate points when `x` is moved to its rounding one coordinate at a time. | Scott part2/E-section.tex:583, 590, 614; I-section.tex:105 | source text read |
| reference rows; free row moments | 15:275, 278 | A row is one test of the finite family separating the free fields: a one- or two-point configuration with fixed free labels (a singleton `u`, an optional spectator `v`). The free row moments are the free moments `G_{u}`, `G_{v}`, `G_{u,v}` of one row. | Scott part2/H-section.tex:160; E-section.tex:490–499; Lean `YM.Push.Corrected.Row` (abbreviation read, `Columns` not opened) | partly |
| selected (history, family; 13:395, 13ba:30) | 13:395; 13ba:30 and the lines of sense 2 | Belonging to the one history fixed by the construction: for each cutoff `N`, the densities obtained from the Wilson density by the block steps, with level-0 coupling `β̄` and the bounds of the schedule at every level. 13:395 and 13ba:30 are this sense, not "along a subsequence". | Lean `YM.RG.History.Selected` (definition read), `YM.Family.Makes` (read in part); Martin actual-phase-grid-approximants.tex:11–46, 136–146 | Lean definition read |
| residue patterns | 13:367; 15sp:11 | The classes of the main insertion points modulo `a_mℤ⁴`; translates by multiples of `s ∈ a_mℤ` give only the `2n` classes of `w` and `θw`. | Scott part2/F-infinite-volume.tex:213–215; Martin actual-slab-copy-bounds.tex:103–128 | source text read |
| replica census | 15:261; 13ba:173 | A census is a finite set of markers with a subset-closed family of allowed subsets containing `∅` and the singletons; here the markers are the reflected copies. "With arbitrary replica census" = for any finite set of reflected copies. | Lean `YM.Marker.Census`, `YM.Stock.census` (definitions read); Martin centered-birth-receipt.tex:5 | Lean definition read (its use at 15:261 inferred) |
| label (polynomial label against field) | chapters 13–16 | Two different objects: the pair `(d,c)` with `c ∈ V_d`, and the pair `(d,A)` with `A ∈ F_d = V_d/N_d(S)`, related by the quotient map. In the formalisation the words of the reflection Hilbert space and the compressions are built from the first; inclusion, derivative, spin operators and Ward identities act on the second. | Lean `YM.Register.Token`, `YM.Register.Word`, `YM.Table.Field`, `YM.Table.Tag`, `YM.DiffPlan`, `YM.Ward.SpinRows` (definitions read); Scott part1/02-definitions.tex:216–226 | Lean definition read (chapter 16 not checked) |
| spin operators | 14:903 | The maps `L_d(K) = c_*^{-1}Y_d(K)` on `F_d`, `K ∈ so(4)`: the part of the infinitesimal rotation acting on the field components. Only the exponential of one `L(K)` at a time is used. | Lean `YM.Ward.SpinRows`, `YM.Ward.angular` (definitions read); Martin physical-ward-analytic-continuation.tex:8–9 | Lean definition read |
| ground algebra | 15:155 | The compression algebra `𝔄`: the norm-closed unital `*`-algebra on `𝓗_0 = ker H` generated by the compressions `M(w)`. | Lean `YM.OS.Spread.algebra`, `YM.OS.Spread.atom`, `ground` (definitions read); Martin phases.tex:229–231 | Lean definition read |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| actual stationary tangent `W` | 17c:48–50, 112–113 | The derivative at zero of the stationary map `V ↦ U_stat(V)`. In the forest coordinates, in which that map is constructed, it is `W_F` (zero on tree links); 17c uses it modulo fine gradients and replaces it by the smooth `W_a`. | v3 5:1147–1150, 9s:188–190; Scott B:473, 483, I:162; Lean `YM.Precision.extracted`, `Guessed`, `Critical`, `Inputs` (definitions read), `stays`, `stationed`, `Work.F04.tangent` (statements read) | Lean definition read (identification of `extracted S F W_s` with `W_F` by agreement of formulas) |
| `W_s`, `W_a`, `W_F` (stationary tangent, tangent, representative, transport, lift) | ch. 5, 7, 9s, 17 | Three linear maps from coarse to fine one-forms differing by fine gradients: straight-average (`W_s`), smooth (`W_a = W_s − d ERW_s`), zero on the forest (`W_F`). Only `W_F` is the derivative of the stationary graph. | as above; Scott B:386–389, 529; Lean `soldier_known` (statement read) | Lean definition read for `W_s`, `W_F`; source text read for `W_a` (no Lean counterpart found) |
| `𝒰_F` | 6:953, 976 | The map from a coarse field to the fine stationary field in tree coordinates: the same operator as `W_F`. | Martin `local-mean.tex:11–27`; Lean `YM.Precision.extracted`, `stays`, `action` | Lean definition read (identity `𝒰_F = W_F` inferred from equal defining properties) |
| `v_eom` | 17m:385–386 | The vector `(0,0,1)` spanning the kernel of the free quotient map; the `v` of 17:171–172. | Scott I:133, 390–391 | source text read |
| `E_stat`, `E_tail`, `E_mark`, second `E_reg` | 17m:161–176 | Errors of the degree-five coefficient: truncation of stationary kernels; omitted long loop paths; remainder of the marked step after Taylor cancellation; coefficient of the derivative of the regular term along `Y` (Scott's "classical defect"). | Scott I:358–366 | source text read (last identification inferred) |
| polynomial-source / linear propagation constants; source recurrences | 17w:12, 52, 78 | The linear coefficient `K_j^src` of the one-step recurrence for the single- and multi-mark source terms, fixed before the block ratio and included in `C_j`; the recurrence holds in the regular and the normalised large-field norm. | Scott E-Gaussian-sources:159, 167–173; E-section:123–126 | partly (chapter 11 equation not pinned) |
| actual free history | 17w:71 | The sequence of quadratic kernels along the constructed history; the covariance estimate is uniform in it within the fixed quadratic bounds. | v3 11:1699–1700 | partly ("free" = "quadratic" inferred) |
| protected-path errors | 17w:72 | Errors from discarding response paths that leave the patch of radius `B`. | v3 11:1773–1776 | partly (v3 text only; identification inferred) |
| fixed-ratio jet errors | 17w:72 | Local errors whose constants bound higher derivatives of the stationary map and depend on `L`; added along a window, not multiplied. | v3 17w:21–25, 17c:138–141, 17m:429–430 | partly (no source sentence) |
| with these same frames | 17w:122 | With the same comparison maps `U_{i,d}` and the same diagonal sequence `(n_i,k_i)`. | Scott I:109, 111 | source text read |
| bottom stage | 17w:97 | The positive-density ratio bound is applied once at the lowest level `k` of the window, with the constant of that level's regularity stage `J_k`. | Scott E-Gaussian-sources:81, 201; I:98 | source text read |
| kernel identities | 17:308 | Either the identities for the block kernel `k` in 17m or the Laurent block identities of 17t; the source uses the phrase for the latter. | Scott I:184, 349 | still open |
| admissible marked conditional integral | 17m:72 | A conditional integral meeting the pointwise derivative hypothesis of chapter 6, so that the bound (6.actual-jet-integral) applies. | v3 17m:72–81, 6:1037–1051 | partly (no source counterpart) |
| finite momentum approximation | 17m:362 | The error of replacing the finite local Taylor coefficient by the momentum-space Taylor coefficient defining `𝔥(Y)`. | Scott I:381 | source text read |
| cross-modes | 17m:401 | Coefficients of the joint marked expansion indexed by the score source together with at least one spectator mark. | Scott usage of "mode"; v3 context | partly |
| normalized large-field majorants | 17m:414 | The majorants of the large-field marked activities divided by their normalisation; they satisfy the same tail bound as the regular ones. | Scott I:402; E-Gaussian-sources:167 | source text read (v3 normalisation `κ_i^{-1}` inferred) |
| inverse source-weight bounds | 17m:440 | The factor `𝗐^{-1}` of the replicated bound, `𝗐` a multiple of the source tolerance `β̂^{-(q+4)}`; logarithm `O(log β̂_n)`. | Scott I:409; E-several-mark:218–221 | source text read |
| physical mark normalization | 17m:441 | The factor `a_n^5` normalising a degree-five insertion in physical units. | Scott I:409 | source text read |
| exterior discrepancy | 17m:442 | The matched residual of backward matching for the source `Σ − βj` with vanishing exterior moments, after replication. | Scott I:395, 404; v3 17m:425 | source text read |
| fixed probe order | 17m:251 | The largest degree of the polynomial fields on which the response is evaluated; the smoothing order `j` is chosen above it. | v3 17m:236–255 | partly (no source sentence) |
| `B_n` at 17m:438 | 17m:332, 413, 432–438 | The chapter 4 support radius `⌈(log β̂_n)²⌉`, not the restarted radius of 17w:33. | Scott I:409, part1/05:17–21; Lean `YM.Pressure.radiusB` | Lean definition read |
| unit endpoints | 17m:474 | The identity-field parts of the two endpoint values of a telescoped sum; they are equal and cancel. | Scott I:447, 451 | source text read |
| "predictor" phrases | 17c:62, 161, 359–360; 17t:157–158 | "Predictor" was the source's word for the gauge-covariant block average `Q^pred`; its "frame correction" is the term from the dependence of that average on the coarse frame. | git `89c513b3`; Scott I:162, 182 | source text read |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| signed local transport | 18:174; 18lp:24–65 | The estimate (18.signed-transport): a local marked density whose extracted coefficient is made to vanish at the coarse end `k_*` of an interval of levels has coefficient plus remainder norm at level `l` at most `4(1+C_m) q_fin (a_m/a_l)^{1/8}`. "Signed": the column is subtracted before norms are taken. | Scott `part2/J-section.tex:45–56` (`lem:J-signed-local`); Lean `YM.Bid.G09`, `YM.Work.G09.cost_finest` (statements read) | Lean definition read |
| anchored marked support bound | 18:174 | The bound, by induction over the levels, for the sum over supports based at the insertions of all coefficients with two or more insertions, in a norm with larger support exponent; in v3 (11.separated-cover) and (11.higher-induction). The identification with these displays is inferred. | Scott `part2/J-section.tex:19`, `E-several-mark.tex:176–181`; Lean `YM.Bid.I01`, `YM.Multi.radius_change` (statements read); the induction not located in Lean | partly |
| graded quotient comparison | 18:175 | Proposition (18.graded-estimate): a label of size `ε` at level `m` is within `C_{t,i}(m) a_m^{−(t−i)} ε` of the fields of degree below `i` in the field space `F_t`. | 18gq:35–48; Scott `part2/J-section.tex:95–103` (`lem:J-graded-quotient`) | source text read |
| annular estimates | 14:971; 19:51, 95 | The estimate (14.annular-input): on the annulus `ρ/4 ≤ \|x − x_0\| ≤ 2ρ` the stress tensor times a field `A`, multiplied by `ρ^{3+ϰ}`, is a field of degree `D = d+1−ϰ` up to an error tending to zero, uniformly over finitely many spectators. | 14:332–370; Scott `part2/G-section.tex:316–321`; Lean `YM.Next.UVStress.ShellBound`, `annular_field` (read) | Lean definition read |
| bounded approximations; real approximation | 19:50, 99 | Real lattice observables, bounded uniformly in cutoff, period and position, that approximate a normalized local insertion within `δ` in the chessboard seminorm of a fixed tiling (Proposition (13.bounded-singleton)); for word differences, Corollary (13.bounded-word). | 13ba:198–210, 302–307; Scott `part2/E-bounded-real.tex:4–10` | source text read |
| fixed-input convergence | 19:47 | If the step maps of different cutoffs are applied at a fixed level to inputs with common limits, the outputs have a common limit; hence couplings and activity arrays converge at each fixed level as `N → ∞` (Proposition (10.stability-assumption), last assertion; Theorem (10.convergence)). That 19:47 means these and not the chapter 12 statement is inferred. | 10:442–447, 810–820; Scott `part2/D-section.tex:1077, 1202`; phrase at Scott `E-section.tex:685` | source text read |
| prescribed-radius squeeze | 19:126–127 | Two steps: the comparison with Maxwell correlations along a subsequence of any prescribed null sequence of radii, and the monotonicity argument (limits at separations `t < 1` and `t > 1` bound the upper and lower limits at `t = 1`) ending the proof of Theorem (17.all-radii). | 17:78–100, 373–383; Scott `part2/I-section.tex:56–60, 503, 514`; Lean `YM.TraceExtension.EuclideanAsymptotic` (conclusion only) | source text read |
| forest prescription; source prescription | 18:398–421 | The recursive subtraction over collision subsets `h`: for each field degree `q < L_h` extracted from the cluster, the normal Taylor polynomial of the test function of order `L_h − 1 − q` at the diagonal `Δ_h` is subtracted, with `L_h = max(0, d_h + 1 − 4(\|h\|−1))`; nested subsets give forests. v3 does not use it and calls it unverified; Lean contains the recursion and a theorem statement of local order `(2+Σd_j)n`, whose proof dependencies were not checked. | Scott `part2/J-section.tex:647–670, 788–797`; Lean `YM.Contacts.Normal.System.cumulant`, `depth`, `YM.Contacts.Solstice.totalTestOrder` (definitions read), `celestial` (statement read) | Lean definition read |
| field reconstruction `H_d`, `A_d`, `B_d` | 18:67–87 | The linear map from clusters `w` of nearby insertions to `F_d`, `H_d(w) = Σ_{\|α\|≤d} b_α(w) u_α`, with `b_α(w)` the fixed probe functional evaluated on the cluster; `A_d` is its `O(4)` average and `B_d` the real part of `A_d`. It is a left inverse of the insertion `A ↦ A(0)` of a single field, not a projection of a space onto itself. | Scott `part2/J-section.tex:153–176` (`def:D31`, `def:D32`); Lean `YM.OPE.shadow`, `YM.OPE.Orbits.averageV`, `checkReal` (definitions read), `old_fixes` (statement read) | Lean definition read |
| resolution heights | 18r:54–55 | The height of a sequence of levels `m(T)` is `lim τ_{m(T)}/T`, `τ_m = log(1/a_m)`, `T = log(1/r)`; the two heights sent to one are `θ` (extraction level) and `θ_+` (grid level). | 18lp:223–224, 347–348; Scott `part2/J-section.tex:222, 304`; Lean `YM.OPE.Height` (definition read) | Lean definition read |
| admissible (physical) periods | MT:14–15, 19; 19:20–21 | Two notions: (1) the selected periods `R_p = 4(M+p+1)`, multiples of four, at least the minimum period and with lattice side `R_p/a_m` at least the stage requirement at every level; (2) at MT:19, a period whose box contains the support of the test function (1:359–361). | Martin `common-scale-selection.tex:116–126`; Scott `part1/02-definitions.tex:90–96`; Lean `YM.RG.Supply.Program.book`, `YM.RG.Calendar.Fits`, `YangMills.WilsonFamily.suitable` (definitions read) | Lean definition read |
| equation calibration floor | 11E:23–30; 19:30 | The lower bound `L^{1/8} ≥ max_{d≤j} 2(1+C_j) Q_{dj} δ_d^{-1}` on the block ratio of stage `j`, one of finitely many lower bounds on that ratio. | Martin `marked-portfolio-calibration.tex:186–221`; Lean `YM.MergeProof.sphere`, `sliver`, `YM.PhysicalNext.Repeat.Legato.paper` (definitions read) | Lean definition read |
| exceptional vacua | 19:107 | Not a kind of vector: the possibility that `ker H_ξ` is larger than `ℂΩ_ξ` for `ξ` in the `ν`-null set left by (15.ae-ground); "remove exceptional vacua" means proving `ker H_ξ = ℂΩ_ξ` for every phase. | 15:314–326; 16:379–381; Scott `part2/H-section.tex:211` | source text read |
| source locations | RG:82 | References by file, label and line into the earlier manuscripts (Martin, Scott, Trish) from which each chapter was written; not locations in the Lean formalisation. | `audit/chapter-18-lattice-products.md:15`; `audit/chapter-18.md:10`; `README.md:5` | source text read |
| numerical band margin | 9:950 | The condition `C_j^{drift} ≤ (κ_G/4) log 𝓛_j` on the block ratios, part of (10.drift-floor). The step theorem does not assert that the output inverse coupling lies in `[β̂_m/2, 2β̂_m]`; with this condition the barriers `ℓ_m`, `u_m` of 10:212–222 keep the tuned couplings in the band. The identification with (10.drift-floor) is inferred from 10:218–222 and the constant `κ_G/4`. | Scott `part2/D-section.tex:847`; Lean `YM.RG.Shoot.band`, `Drifting` (definitions read), `gates`, `limits` (statements read) | Lean definition read |

### Second round: entries that still recorded an ambiguity

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| anchor (output anchors; anchors of the energy terms) | 6:90, 210–212, 1329 | In chapter 6 the anchors are the addresses at which the six local energy terms are summed, fine ones being counted at their coarse projection; "output" means the coarse level. | Scott `B-section.tex:915, 918`; v3 6:210–212 | source text read |
| block-average patch | 4:17, 172; 6:459; 7:599; 17c:359 | The patch `Ly + 𝔹_R`, `R = (j+3)L`. At 6:459 the set of links read by the block average of a coarse edge (coarse radius `r_pred`); at 7:599 a different box of radius `(j+5)L`; at 17c:359 the supports of `M_{ef}` and `K_0` (inferred). | Scott `B-section.tex:17, 81, 1051`; Martin `weighted-frame-penalty.tex:168`; Lean `YM.RG.Patch.radius` | partly (17c:359 inferred) |
| compensation / compensating map | 10:529–531; 6:1540 | Two changes of variables that keep the fine field fixed: the rescaling `z ↦ ℓ(t)z` when the coupling varies (ch. 10), and the map `T_V` of (ch06:protected-change) when the coarse field varies (ch. 6). The map of 6:1540 is the second, not the first. | Martin `compensated-variation.tex:3–9, 130–134, 147–150`; `local-parameter-comparison.tex:51–55`; v3 6:695–729 | source text read |
| core, core energy | 6:80, 1327–1333 | Core: the energy terms within `2B` of a component; core energy: their sum, which is the local energy `𝓔_A`. | Martin `packet-estimates.tex:23–33`; Scott `B-section.tex:915`; v3 6:210–212 | source text read |
| cutoff remainder | 6:739, 834–843, 1018, 1040 | A cutoff factor minus one, `W_w = F_w − 1`, for the plaquette and discrepancy cutoffs, the normalised tag weights, the inventory tests and the chart cutoffs; nonzero only on a Gaussian tail event near its address. | Scott `B-section.tex:1173`, `D-section.tex:96`; Martin `gaussian-warnings.tex:206–207` | source text read |
| determinant inverse identity | 9:140 | The resolvent identity applied to the integral formula for the local log-determinant, giving the determinant row `P_j(t_{m+1}+g)`; the argument of 6:1285–1289. Not the series of 6:1192–1203. | v3 6:1253, 1285–1289, 9:126, 140–142; Scott `D-section.tex:162` | source text read (exact form of Scott's "inverse identity" not displayed) |
| fine residue | 5:654–660, 713; 7:585–599; 11:271; 17c:337 | The class of a fine site modulo `L`, with a chosen (centred) representative: `z = z̄ + L r(z)`. At 5:388–390 "residue" is instead an alias class of momenta. | Martin `weighted-frame-penalty.tex:238–239`, `rg-horizon-geometry.tex:266–270`; Lean `YM.Lattice.wrap`, `YM.Lattice.lift` | Lean definition read |
| first-power | 4:293, 308–312; 5:1007 | A bound linear in the plaquette sum `𝒫_y(U)`, as opposed to a bound by its square root obtained from an energy comparison. | Martin `seed-geometry.tex:4–7, 20–24, 89–91`; v3 4:301–310 | source text read |
| fixed-position read | 7:637, 710 | The link at a fixed position of a straight piece of a coordinate path, as a function of the two endpoints (7:637); the averaged link at a fixed position of the straight connector of the block average (7:710). | Martin `weighted-frame-penalty.tex:78–83`, `weighted-stationary-inverses.tex:179–182` | source text read |
| free (links) | 5:918, 1161; 6:442–443, 489, 588, 1376 | The links outside the block trees; they carry Haar measure and split into active ones (Gaussian variables) and frozen ones. | Scott `B-section.tex:583, 1047, 1171` | source text read |
| full maps | 6:948, 987, 1006 | The untruncated flat maps `M_f`, `M_n`, `N`; `Φ`, `Φ_n`, `𝒩` are their transported truncations. | v3 6:125–131, 179–182; Scott `B-section.tex:854–871` | source text read |
| link factor | 5:335, 762 | The multiplier `r_L(t) = L^{-1} Σ_{r<L} e^{irt}` of the average along a straight path of `L` links. | v3 5:160–164, 334–336, 759–763 | v3 text (source text read for confirmation) |
| logarithm | chapters 4–6, 9s | Lie-algebra coordinate of a link; for active fine links relative to the replicated coarse field, `U_e = exp(u_e)(rep V)_e`. "Local Haar logarithm" is `log J(u)`, the logarithm of the Haar density; "frozen Haar logarithm" (6:598) is the coordinate of a frozen link. | v3 6:693, 1290–1291; Scott `B-section.tex:583, 1121, 1127, 1171`; Martin `actual-corrected-body-compiler.tex:162–163` | source text read |
| macro-box | 4:298; 5:1005–1032; 6:303–325 | The box of radius `(j+7)L` about `Ly`, in the covering lattice. The padded block of chapter 7 is not this box. | Scott `B-section.tex:991`; Lean `YM.Pressure.macroR` | Lean definition read |
| placement, sense 4 (path-placement operations) | 10:314–315 | The choice of coordinate paths along which the curvature factors are transported in (ch07:slot); with the curl division it makes the path representation a linear function of the coefficient. | v3 7:67–143, 146–160, 10:313–319; `audit/chapter-10.md` | v3 text (no source uses the phrase) |
| `Q^pred`, `r_pred` | 4:202–210; 6:460, 501 | "pred" = predictor, the source name of the gauge-covariant block average; `r_pred` is the largest coarse distance read by it. | Scott `B-section.tex:3, 68, 100, 1051`; Lean `YM.RG.Patch.predictorMass` | source text read |
| regrading | 2e:27–36, 52 | A unipotent change of labels with respect to the grading by (factor count, scaling dimension). | Scott `A-section.tex:169` | source text read |
| relaxed (10:98 "smooth cutoff") | 10:98; 13ba:36, 165 | The factor is the indicator of the relaxed small-field condition on the stencil of the bounded coarse trial; "smooth cutoff" replaced "guard" mechanically. | git commit `4ebb64ea`; Scott `E-bounded-real.tex:14–17`; v3 13ba:213–220 | source text read |
| residual, senses 1, 3, 4 | 6:1080, 1090, 1404; 9:77, 130; 11:894–902 | Stationary residual: `η = −g^{-1}(𝖠 m_Y + f_Y)`. Residual Gaussian density: `exp{η·z + ½ z^*(Γ^{-1} − 𝖠)z}`. Nonlinear residual: actual row minus its comparison term. Trial residual: terminal trial minus one normalised local insertion. | v3 6:659–668, 1090, 11:894–902; Scott `B-section.tex:1277, 1308`; Martin `packet-annulus.tex:209–246` | source text read |
| response (6:846; 19:159) | 6:846; 19:159 | 6:846: the first-order variation of the block average in the fine fluctuation (source: "predictor response"). 19:159: `W_s`. | git commit `4ebb64ea`; Martin `actual-reader-tree-covariance.tex:63–65`; v3 17m:190–202, 263 | partly (6:846 inferred) |
| safe chart | 9s:139–141, 232 | The inverse image, under the stationary chart, of the closed coordinate ball `max(‖x‖_∞, ‖y‖_∞) ≤ r_s`; convex in the coordinates. | Martin `stationary-exterior-receipt.tex:22–23, 81–91, 111–118` | source text read |
| seam | 1:284, 287, 316, 323 | A reflection hyperplane of the chessboard tiling (here through sites, `x_a ∈ ℓℤ`); seam links are links with an endpoint on one. | Martin `centered-estimates.tex:32–37, 56–60, 125–126`; v3 1:242–247, 284–289 | source text read |
| sector allocation indicators | 9:81–82 | The factors selecting an allocation sector (allocation weights of the selection, the condition on `A_c`, the tag weights), kept unexpanded. | Scott `D-section.tex:105`, `B-section.tex:908–915`; v3 6:67–89 | source text read |
| separating family (reference rows) | 3:484–495; 15:278 | A finite family of one- or two-point tests whose matrix of free correlations with a basis has full rank; the reference rows are these tests. | Scott `E-section.tex:493–499`, `H-section.tex:160` | source text read |
| source locations | RG:82 | References into Martin, Scott and Trish; Trish is a variant of Scott with the same files, not present in the checkout. | `blueprint/scott-trish-comparison.md:1–3`; `blueprint/source-index.md` | partly (Trish not read) |
| spectator | chapters 3–19; 2e | The list `B` of other insertions, at separated points, in a correlation `S(A,x;B,y)`; in 2e a bounded measurable function of the links outside a ball. | Scott `part1/02-definitions.tex:216, 293`; `A-section.tex:180` | source text read |
| stationary residual | 9:77, 130 | `η = −g^{-1}(𝖠 m_Y + f_Y)`, the failure of the window mean to solve the mean equation of the sector quadratic form; exponentially small in `B`. | Scott `B-section.tex:1087–1096, 1269, 1277`, `D-section.tex:154, 162`; v3 6:615–623, 659–668 | source text read |
| uniform mass | 4:77, 209; 6:63, 1344 | Mass = probability weight of a tag; uniform mass = `1/(number of tags)` on the minimising branch; likelihood = the same weight relative to the uniform law. | Scott `B-section.tex:90, 95, 100, 1182, 1193`; Lean `YM.RG.Patch.frameMass`, `YM.RG.Patch.predictorMass` | Lean definition read |
| moving comparison fields | 3:576 | Unchanged (see Notes). | — | still open (Lean statement for the trace label) |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| adjacent pair (permitted adjacent pairs; adjacent quadratic pair) | 10:30, 125; 5:689; 6:946; 9:912 | At 10:30 the pairs are the stage pairs `(J(m+1), J(m))` of the fine and coarse level of a step; there are finitely many for each stage. The "adjacent quadratic pair" is the pair of free quadratic forms of two consecutive levels with the transport identities of chapter 5. | Martin restarted-rank-history.tex:464–466, 497–500, 734; Scott E:142, C:83; v3 6:946–947, 1553–1554 | source text read ("permitted" not explained) |
| affine (normalized affine directions) | 9:35, 502 | The affine link fields `A^{q,T_*}_c(y) = 1_{c=b}ξ_o(y)^a T_*` and their half-sums, multiplied by the threshold `t`; they are admitted directions of the activity seminorm. | Scott D:22, D:516; Martin physical-reset-reorganization.tex:104–107; v3 9:458–467 | source text read |
| attachment (sense 2; attachment norm) | 9:687, 697, 794 | In a rooted tree sum a child support is attached to its parent by meeting it; `(2B+1)^4` times the site norm of the weights bounds the supports attachable to one support. | Scott D:109, 111–116, 214 | source text read; `u_N` = Scott's `η^att` only inferred |
| centered (sense 6) | 5:1338; 9:126, 294; 9s:283 | Value at zero subtracted: `log det A(x) − log det A(0)`; the determinant minus its flat value and the quadratic term assigned to `α𝒬`; `G − G(0)` for the corrected logarithm `G`. | Martin uniform-stationary-chart.tex:193–198, pure-action-small-field.tex:187–197; Scott D:162 | source text read |
| centered log determinant | 5:1338 | `log det A(x) − log det A(0)`, `A` the vertical Hessian on the stationary graph (the source's "relative log determinant"). | Martin uniform-stationary-chart.tex:193–198, 231; truncated-stationary-log.tex:40–41 | source text read |
| completion (blocked completed matrix `C_0`; completed fine kinetic matrix) | 7:773; 17c:64 | `C_0` is the matrix of fine kinetic form + block penalty (constraint pullback, contact term removed) + gauge term `F*F`; it is compared with the gauge-completed auxiliary fine matrix. At 17c:64 the completion is the gauge completion of the fine kinetic symbol. | Martin stationary-determinant-prices.tex:171–186; Scott C:237; v3 7:728–739 | partly (17c:64 inferred; its own source passage not found) |
| corrected logarithm; centered expression | 9s:264, 274, 283 | `G = log 𝒵 + β′a_c + d_c`; the centered expression is `G − G(0)`. | Martin pure-action-small-field.tex:115–123, 194–197 | source text read |
| curl-division (path-placement operations) | 10:314–315 | Path placement: choosing once coordinate paths from the origin to the displacements and placing the curvature factors at their ends (ch07:slot); linear, like the division. | Scott C:139; Martin multileg-curvature-lift.tex:306–309; v3 7:146–161 | source text read |
| deletion-of-support identities | 11R:239 | The identities `Z_pol(z^Y)/Z_pol(z) = e^{−𝓛_Y(z)}` (ch08:deletion-identity), one for each deleted set `Y` ("hole"). | Martin restarted-rank-history.tex:707–710; actual-corrected-body-compiler.tex:380–396 | source text read |
| discrepancy (discrepancy series; exterior discrepancy) | 9:517; 17m:442 | The functions `ζ_f = (1−h_Z){f(1) + h_{{o}}Q_f − h_X f}`, the correction for the different event indicators in the local subtraction. The exterior discrepancy is the normalized residual of backward matching for a source with vanishing exterior moments. | Scott D:491–495, 322; Martin physical-reset-reorganization.tex:193–198; Scott I:395, 404 | source text read |
| dummy Gaussian coordinates | 9:59, 72 | The `D − n_act q` coordinates (tree coordinates and coordinates of inactive free bonds) on which the precision is the identity; each gets an independent standard Gaussian variable of integral one. | Martin gaussian-reassembly.tex:14–27, 46–50, 65–71 | source text read |
| exchange symmetry | 7:195 | `f_{ab}^{uv}(p) = f_{ba}^{vu}(−p)`: symmetry of a two-leg symbol under exchange of the legs. | Martin stationary-output-construction.tex:192–199, 228–230 | source text read |
| factor after deterministic subtraction | 9:124 | Table heading; each row is a term of the exponent after removal of its leading part (stationary quadratic part of the action; flat value and assigned quadratic term of the determinant; value and first derivative of the Haar density). The source heading is "factor". | Scott D:149–162 | partly (the phrase is in no source; "deterministic" unexplained) |
| flattening | 9:676 | Replacing each new label (a connected component) by its constituent old large-field and logarithmic labels; inverse of taking components. | Martin soft-log-fusion.tex:94–105; forced-exclusion.tex:84–94 | source text read |
| fold (sense 1) | 7:810 | Pullback of a fine quadratic kernel to coarse momentum: `L⁴ Σ_z N_{−z}(−ξ)^T Y(k_z) N_z(ξ)`, a sum over aliases. | Scott C:234, 237–240 | source text read |
| infinitesimal gauge insertion | 7:243; 17t:85 | Differential of the gauge action; `ℛ` (ch. 7) acts into the joint space (fine links and frame coordinates) and has fine component `d_U`; `d` (ch. 17) is that fine component. Not the same operator. | v3 7:679–681, 876–877; 17t:182 | settled from the v3 text |
| margin (numerical band margin) | 9:950 | Slack `κ_G/4` in the condition (10.drift-floor) on the block ratios. | entry *numerical band margin* (Scott D:847; Lean `YM.RG.Shoot.Drifting`, read in the first round); v3 10:55–60, 212–222 re-read | source text read (first-round Lean evidence not re-opened) |
| measure multiplier | 9:63 | `(2π)^{-(D−n_act q)/2} g^{n_act q} c_H^{n_act}`: Gaussian normalisation of the dummy coordinates, Jacobian of `a = μ + gz`, Haar density at zero; without the field-dependent Haar correction. | Martin gaussian-reassembly.tex:49–62, 67 | source text read |
| one-step integral identity | 7:859 | The identity `dens(ρ) = 𝓑_m^{β′} dens(ρ′)` of the step theorem with `β = β′ + α + Δ`. | v3 7:856–859, 9:716–722, 941–945; Scott D:663, 671–676 | partly (inferred; the phrase is in no source) |
| plaquette filling bounds | 9s:175 | Axial-gauge bound of a link by the number of plaquettes filling the loop to the gauge tree times the largest plaquette distance. | Martin stationary-exterior-receipt.tex:96–108 (same estimate elsewhere); audit/09-renormalization-audit.md (passage new in v3) | partly (v3 passage has no source) |
| prescribed coarse classical action `a_c`, `d_c` | 9s:258–259 | `a_c` = coarse classical action `𝒦`; `d_c` = "prescribed coarse quantum and reset contribution", by comparison with (ch09:early) `𝓛 + α𝒬`. | Martin pure-action-small-field.tex:104–112; stationary-output-construction.tex:410–420 | partly (formula for `d_c` inferred) |
| representative (sense 3, "protected") | 11:1063 | Finite difference written as a trial of degree `d+1`; "protected" = satisfying the two subpower bounds of a protected trial. | entry *protected trial* (Martin actual-insertion-derivative-relay.tex:24–35) | source text read (first round) |
| reset | 9:748; 10:651 | Passage to the output coupling `β = β′ + α + Δ` and scalar; at 9:748 and 10:651 the correction `Δ`. | Scott D:574, 663, 671–676; Martin coupling-reset-selection.tex:1–8, physical-reset-reorganization.tex:1, 322–326 | source text read |
| stationary identification | 7:578, 829 | The identity `rep v + ι_F Dρ(0)v = W_F v` (ch05:stationary-tangent), with `W_F`, `W_a`, `W_s` equal up to fine gradients. | v3 5:1139–1155; Scott B:483, D:1197 | settled from the v3 text |
| stationary units | 9s:165 | Divided by `Ω e^{−Φ(x)}`. | Martin stationary-exterior-receipt.tex:156–165 | source text read |
| support compression (constant) | 9:231 | `T_r = (2r+13)^4` is the Lean constant `toll r`. | Lean `YM.Planned.AtomRegular.toll`, YM/Planned/ATOM_REGULAR_ESTIMATE/Geometry.lean:50 | Lean definition read (name resolution not elaborated) |
| tag (live tag actions) | 9s:127 | Tags of positive weight; action = fine action plus penalty for that tag. | entry *live tag actions*; Martin stationary-exterior-receipt.tex:48–61 re-read | source text read |
| tag-count factor | 9s:134; 11R:357 | Number of tag arrays; arises from writing the tag weight as (number of tags) × probability, with a uniform tag average outside. | Martin actual-corrected-body-compiler.tex:70–81; gaussian-reassembly.tex:194–199; warning-safety.tex:115–118 | source text read |
| thermal (thermal coefficient) | 7:765 | Thermal term = `T(v)` (ch07:thermal), the part of the stationary integral without `β`; thermal coefficient = its quadratic coefficient `α(T)`. | Martin thermal-contact-cancellation.tex:83–88, 268–287; stationary-output-construction.tex:410–413 | source text read |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| front-column (in *column*, sense 4) | 11:1343 | The one-step bound `‖x_m‖_1 ≤ C_{m+1}L_m^d‖x_{m+1}‖_1` in the direction of the transfer; its product is `D_k`. The bound of 11:445–446 is the one in the opposite direction, with the same constant. | Martin actual-rank-purchases.tex:176–188; Lean `YM.Source.TransferData.Based` (fields `front`, `back`), `YM.Next.Rank.Price.outward`, `.at_current`, `.reference_size` | Lean definition read |
| exponent of the target columns | 11:1238 against 11:1363, 1842, 1925 | `‖Au‖ ≤ H^{bd+c_d}` with `c_d = q_*+2`, `q_*` the largest factor degree of a basis element; 11:1238 has lost `bd`. | Martin allarity-coordinate-calibration.tex:232–243, actual-rank-purchases.tex:1027–1029; Lean `YM.Next.Rank.Atlas.income`, `saves`, `leash` | Lean definition read |
| rooted activity norm | 12:178 | Anchored norm for regular activities, containing-site norm for large-field ones; either, summed over the sites of the torus, bounds the unweighted total. | Martin parameter-comparison-suppliers.tex:31–35; Lean `YM.RG.Activities.EBound` (with `KBound` of the entry) | partly (link of 12:178 to the source passage inferred) |
| cutoff-failure catalogue; Warnings | 10:727; 6:1476, 11:319 | The finite list of cutoff-failure factors of a step on the fixed torus; "warning" is the source's word for such a factor. | Martin gaussian-warnings.tex:4–7, parameter-comparison-suppliers.tex:30, selected-history-limits.tex:454–457 | source text read |
| eligibility test `𝓔_i^extra` | 4:440–450 and later | A free datum of a large-field activity (a Borel, gauge-invariant, local event); no rule defines it. | Scott D-section.tex:34, 05-renormalization.tex:62–65; Lean `YM.RG.ForcedAddress`, `.eligible`, `YM.RG.Activities.ForcedFamily` | Lean definition read |
| normalized endpoint inequalities | 11:877 | The bounds `A^q l/R` on the difference of the normalized word between displacement `0` and displacement `l`, from Cauchy's estimate integrated over `[0,l]`. | v3 11:862–877; Martin centered-estimates.tex:438 | source text read |
| before extraction | 11:2037 | Before the countable choice of subsequences in the mesh and period limits. | Martin fullmesh-fixedbounds-producer.tex:410–413, actual-rank-purchases.tex:285–289 | source text read |
| fixed common coefficient functionals | 10:339, 373, 813, 889 | The fixed linear maps (curl division, path placement) that assign to an action its array of path coefficients, the same at every cutoff. | v3 10:313–316; audit/chapter-10.md:10; Martin background-path-convergence.tex:24–37 | partly (no defining sentence for the phrase; no Lean) |
| fusion | 10:655, 666, 774, 914 | The exact regrouping of large-field activities with logarithmic corrections, Proposition ch09:fusion-prop. | Scott D-section.tex:536, 554–557; Martin soft-log-fusion.tex:1–6 | source text read |
| inverse terminal coordinates | 11:946, 958, 1075; 13:159, 217 | `𝖹_{N,p,d}^{-1}z`, the coordinates at the cutoff level; `X_i = 𝖹_{N,p,e}` by 11:1089, so the two former readings coincide. | v3 11:883–886, 1089, 1101–1102; Martin actual-insertion-derivative-relay.tex:38–40 | source text read |
| convergent moving labels | 14:238, 250 | Convergent sequences in the free field space `F_d^0`. | v3 14:210–250 | source text read (v3 text alone) |
| corrected leading coefficients; leading / lower interval | 11:1551, 1886; 11:1410, 1643, 1952 | "Leading" is the source's word for the principal terms and for the interval `k → ℓ` on which they are tracked; the corrected ones are the coefficients of `D_Q − D_R` at level `ℓ`. | Martin allarity-marked-propagation.tex:103–104, 248–254, 305–306, 1876–1881, 1892–1896 | source text read |
| local read set, held fine reads | 10:508–765; 11:696–720 | The set `I(S)` of fine links on which a local factor with coarse support `S` depends; "held" = kept fixed while the parameter varies. | Martin sector-analytic-prices.tex:99–100, 108–114, 125 | source text read |
| moving complement | 11:2224 | The range of the projection `Π_i` with kernel the equation space `K_i`. | v3 11:1089–1099, 2218–2232 | source text read (v3 text alone) |
| normalized large-field majorants | 17m:414 | Large-field majorants divided by `κ = (ε^for)^{1/2}`. | Scott E-one-mark.tex:37, 71; v3 11:360–361, 886–888 | source text read |
| opening, opening level | 11:1405–1407, 1889, 1919; 13ba:127 | Level `k`, to which the marked density `q_k` is transferred and where the sites are separated; at 13ba:127 the embedding of level-`m` sites in finer levels with separation `B_j²`. | Martin allarity-marked-propagation.tex:193, 2609–2612; centered-geometry-producer.tex:5–23 | partly (`B_m²` against `B_j²` at 13ba:127 open) |
| ordinary bound by one; ordinary output bounds | 11:1589; 10:327 | The bound by one of (ch11:higher-induction); the stage bound without the enlargement factor 64. | v3 11:1892, 10:341–343; Martin allarity-marked-propagation.tex:2636–2638, background-path-convergence.tex:52–56 | source text read |
| physical counting coordinates; physical jet block | 6:957, 11:621; 11:1832 | Cochains with the counting scalar product (no volume factor); the covariance block on the retained jet coordinates as opposed to the residual ones. | Martin actual-reader-tree-covariance.tex:11–23; allarity-coordinate-calibration.tex:4–6, 163–166 | source text read |
| principal source term; nonleading | 11:1632; 11:319 | A prescribed principal term `F_{c,I}` (cell `c`, set `I` of insertions) with prescribed support; "nonleading" = "nonprincipal". | Martin allarity-marked-propagation.tex:54–56, 103–115, 202–204, 340–341 | source text read |
| protected trial ("subpower", "trial") | 11:1063, 2306; 13:229 | `Slow`: for every `ε > 0` eventually `≤ exp(ε·scale N)`; a trial is a family of functions of the configuration indexed by cutoff, period and site. | Lean `YM.Push.RelayDifference.Slow`, `flight`, `YM.Extraction.Lease.Trial` | Lean definition read (`scale` not unfolded; "protected" unexplained) |
| rebasing contraction | 11:467 | The contraction of the graph map `G ↦ R_GM_G^{-1}`; "rebasing" = rewriting the remainder in the outgoing coefficient by the inverse bound. | Scott E-one-mark.tex:102 | source text read |
| request (sense 1) | 10:66–69 and later | A real number of a countable family fixed in advance, which the stage constants are made to dominate from some stage on. | Martin common-scale-selection.tex:141–159 | source text read |
| restoration levels | 11:1405 | The middle levels `ℓ`, where the source weight is raised from `ω_−` to `ω`. | Martin allarity-marked-propagation.tex:248–265, 1876–1879; audit/chapter-11-weight-restoration-review.md:23 | source text read |
| selected large-field condition set `A_M` | 9:108, 440 | The selection `(A_f, A_n, A_c)` of the large-field component in the connected product `M`. | Scott D-section.tex:170 | source text read |
| tolerance exponent `q` | 11:1673 | The exponent of the initial regular-remainder bound `d_0 = H^{−q}` of the recurrence on `k → ℓ`. | Martin allarity-marked-propagation.tex:197–200, 207–209, 289–291 | source text read |
| exterior row | 11R:266 | The action rows (energy minus subtracted affine square plus mean square) not assigned to a selected component; chapter 6's "remote" action lines. | Martin actual-corrected-body-compiler.tex:93–100, 137–139, 298–299; actual-harvested-owner-energy.tex:203–231 against v3 6:1426–1437 | partly (the numerical bound not compared; determinant and Haar lines by name) |
| finite decorations | 11R:304 | No change: the choices of fine large-field sites attached to a selected component; no count is given. "Local counting costs" beside it is the packet count `H_B D_B^{2r}`. | Martin restarted-rank-history.tex:657–660; mixed-activity-prices.tex:33–55; actual-corrected-body-compiler.tex:346–351 | still open (count) |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| admissible majorant | 12:80 | Any family of bounds for the entries of a remainder array with finite weighted sum, i.e. a competitor in the infimum that defines the seminorm of `𝓡_m`; the phrase introduces an `ε`-argument. | Martin fixed-rung-convergence.tex:11–14, 27–29; Lean `YM.MergeProof.Matric.ticket` | Lean definition read |
| admissible trial encoding | 13:394 | The trial encoding whose coefficients have subpolynomially growing inverse terminal coordinates (the defined sense of 11:1101). | v3 11:1074–1075, 13:239 | source text read (v3 alone) |
| admissible path-action representation; admissible bounds | 13sb:27, 36 | The representation of the density of the trajectory (path action, regular and large-field activities) in the class to which the one-step theorem applies; its bounds are (ch04:activity-bounds). | Scott E-section.tex:25–27; part1/05-renormalization.tex:191; v3 10:237 | source text read |
| finite admissible request | 18lp:103 | A numerical requirement on the schedule of the kind allowed at 10:66–70, met by raising the stage coupling threshold. | v3 10:66–70, 13ba:258 | source text read (v3 alone) |
| angular boundary; angular flux at infinity | 14:410, 708 | The integral `−∫ ∂_μV_c S(J_{μc}, A)` of the conserved tensor against the derivative of a vector field equal to `Ky` on a large box; it equals the angular sum of the Ward identity and is shown to vanish for collinear configurations. | Scott G-section.tex:656–663, 677; Martin physical-ward-propagation.tex:23–34; Lean `YM.Ward.angular`, `Collinear` | Lean definition read |
| barycenter identity | 16:118 | `S(w) = ∫_Ξ S^ξ(w) dν(ξ)`, eq. (ch15:mixture), and its extension to the boundary distributions. | Martin phase-selection.tex:68–72; assembly.tex:85–96; Lean `YM.OS.Spread.Resolution.barycenter`, `YM.EveryPhase.barycenter` | Lean definition read (statements) |
| comparison maps `U_{k,d}` | 14:210–231 | Linear isomorphisms from the free to the interacting field space of degree `d`, with scales `r_k ↓ 0`, under which rescaled interacting correlations converge to free ones. | v3 14:201–222; Lean `YM.Climb.Scaling`, `YM.Next.UVStress.Stable` | Lean definition read |
| comparison (bare word) | ch. 11–17 | Generic; no single object. | — | still open (nothing to settle) |
| corrected coefficients `R_I` | 11:2066–2070; 14lc:49–57 | `Σ_I R_I z_I = ∏(1 + z_iI_i)/Σ_J G_J z_J` in squarefree variables, `I_i` the lattice insertions, `G_J` the free correlations; not centred on the lattice; not the Wick ordering of single insertions. Whether to call it a Wick product is left to a mathematician. | Lean `YM.Extra.WeakScaling.corrected`, `multiply_back`; Scott E-section.tex:506–521, G-section.tex:279–285; Martin actual-rank-purchases.tex:152–154 | Lean definition read; name still open |
| field word; letter; word (ch. 16) | 16:291–293 | A word is a finite ordered list of letters `(A,f)`; `𝒫` is the free algebra on the letters; fields act on its quotient by the null space. | Martin reconstruction.tex:4–5, 18–23, 37–38 | source text read |
| Haar-ball normalization argument | 10:169–172; 13sb:36 | Lower bound for the partition function by restricting all links to a ball of small Haar measure `(ρ/16)^{4D_GV}`; gives the per-site cost `q = O(1 + log β̂)`. | v3 11:795–811; Scott E-section.tex:26–42 | source text read |
| large-field profile; complementary profile | 12:26; 13ba:165 | Sum of the large-field activities with given support and large-field set; "complementary profile" is the large-field part of the term linear in the sources of an inserted trial. | Martin fixed-rung-convergence.tex:19–20, 218–222; Lean `YM.RG.ForcedAddress`; v3 13ba:16, 160–166 | partly (13ba:165 from v3 context and audit note) |
| moment (lattice correlation) | 12:262, 293 | `M_{N,p} = M^lat_{N,p}`, the expectation of a product of lattice insertions (1:341–343). | Scott part1/02-definitions.tex:66–74; E-section.tex:672 | source text read |
| compressed product moments | 15:213 | `⟨Ω, M(w_1)⋯M(w_k)Ω⟩`, cluster limits of correlations (ch15:cluster). | v3 15:80–83; Scott H-section.tex:111–113 | source text read |
| support moments | 18lp:177; 10:603 | Polynomial factors `(1+S)^k` in the size of a support, summed against the weighted activities and absorbed by part of the exponential support weight. | Martin high-degree-cluster-prices.tex:123–151; v3 10:603, 11:420 | partly (correspondence of passage inferred) |
| orientation of the line | 14:306 | The sign of the generator `J` of `ker(div\|_𝒦)`, chosen so that `U_{k,4}^{-1}(c_k^{-1}r_k^4J) → +T^0`. | v3 14:296–308; Martin actual-stress-normalization.tex:182–233; Lean `YM.Next.UVStress.produce_current` | Lean definition read (statement) |
| conserved line (interacting) | 14:258–308; 17:341 | `div : 𝒦 → 𝒱` is onto and `dim ker = 1`, `𝒦` the centred real symmetric covariant degree-four tensors of the interacting theory; plus the choice of `J` with pull-backs tending to `T^0`. | Martin actual-stress-normalization.tex:138–180; Lean `YM.Next.UVStress.differential_rank`, `KernelSpace`, `currentDiv` | Lean definition read |
| phase (ch. 1, MT) | 1:415, 418, 499 | The chapter 15 notion: a character of the compression algebra, i.e. a point of the compact metrizable space carrying the measure of MT:33–36. | v3 MT:33–36, 19:66–68; Martin phase-selection.tex:60–73; Lean `YM.OS.Spread.Resolution` | Lean definition read |
| shared frame seed | 13ba:231, 247, 270 | The random variable choosing the gauge frame at a coarse site in a block step; shared by the coarse links at that site. | v3 13ba:229–241, 4:217–219; audit/bounded-coarse-approximation-review.md item 1 | partly (v3 text and audit note; no source manuscript, no Lean) |
| sparse stopping scale | 10:172; 18lp:159 | The level `k(m)`, first `k ≥ m` with `B_k² ≤ a_m/a_k`; "sparse": the reflected insertions are `a_m/a_k ≥ B_k²` sites apart at that level. | v3 13sb:85–86, 104–117; Scott E-section.tex:111–117, E-several-mark.tex:188, 208 | source text read; "sparse" partly |
| zero-energy subspace | 15:27–28 | `ker H`, the vectors fixed by the semigroup; not asserted one-dimensional for the undecomposed family. | Lean `YM.OS.Semigroup.ground`, `Chamber.UniqueHeat` | Lean definition read |
| forgetting the terminal graph | 12:131 | The level-`m` graph of the history depends on the graph at level `m+h` by at most `2^{1−h}`; with fixed-input continuity the graphs are Cauchy in the cutoff. No object called "terminal graph" exists in the source body or in Lean. | Martin fixed-rung-convergence.tex:92–125; Lean `Gear`, `Gear.shawls`, `Gear.voyages`, `TwoFold`, `Club`, `Ritzy` | Lean definition read |
| rooted activity norm | 12:178 | The norms `𝓔_m` (anchored, regular) and `𝓚_m` (containing-site, large-field) of (ch04:weighted-sums). | v3 12:31–34, 4:596–614; Martin fixed-rung-convergence.tex:193–196, 212–219; Lean `YM.RG.Activities.EBound`, `KBound` | Lean definition read |
| rooted majorant sums | 12:236 | Insertion-rooted weighted sums `sup_s Σ_{i: s ∈ mode i} e^{a·cov(X_i)} f_i`. | Lean `YM.Extra.Multi.Rooted` (formula match) | partly |
| spin operators | 14:903 | Unchanged (entry already carries its source). | — | Lean definition read (first round; `YM.Ward.SpinRows`, `angular` re-read) |

| Term | Where in v3 | What it is | Evidence | Status |
|---|---|---|---|---|
| anchored marked support bound | 18:174 | The chapter 11 induction (11.higher-induction) for coefficients with at least two insertions, in the norm with larger support exponent; 18lp:67–136 is where it is used, not a second candidate. | Scott J-section:19 (the estimate belongs to Lemma `lem:E-source-attachments`); identification with (11.higher-induction) by content | source text read |
| available weight | 18lp:128, 168, 175 | The product `ω` of the weights of the source variables of one group that are still positive. | Scott J-section:236, 280; G-section:334 | source text read |
| chart (safe chart, common chart) | 9s:139–141, 221 | The set of fine configurations `exp(y_i) V(x)^rep_i` with `max(‖x‖_∞, ‖y‖_∞) ≤ r_s`; "the common chart" of 9s:221 is this set. Domain of the "small-field / ordinary chart" still not stated. | Martin stationary-exterior-receipt:14–23, 81, 88–91, 111–118, 259–262 | partly |
| comparison level (17m) | 17m:136 | The fixed level `k` at which the transferred current is evaluated, later `k = k_i`. | Scott I-section:213, 331 | source text read |
| contact (chapter 17), group-coordinate contact identity | 17t:175–237 | Identity (17.contact); the name is the chapter 7 one: a gradient paired with the second derivative of a nonlinear coordinate map. The reason for the word "contact" is nowhere given. | Martin thermal-contact-cancellation:1, 126–141; Scott I-section:228 | partly |
| contact projection; child / parent operators | 18:404–418 | The map sending a cluster near a centre to its field of exact degree `q` at the centre, defined by finitely many separated correlations and a fixed left inverse; child and parent operators are the normal Taylor operators of nested collision subsets. | Scott J-section:591–619, 673; Lean `System.reader`, `waySystem`, `insertRow` (definitions read; `M.row` not opened) | source text read |
| rebasing contraction | 11:467 | The contraction by 1/2 of `G ↦ R_G M_G⁻¹`; "rebasing" is the composition with `M_G⁻¹`. | Scott E-one-mark:102 | source text read |
| corrected free-subset polynomial | 17w:87 | The polynomial `Σ_I G_I z_I` of free moments of the subsets, by whose inverse the source is multiplied (11:2096–2098). | v3 11:2064–2071, 2096–2099; wording in Martin actual-rank-purchases:300–302 | partly |
| current depth | 17m:29, 361 | The number `N − k` of block transfers of the current down to the fixed level `k`; a threshold chosen before the ordered limit, not a further limit. | Scott I-section:213, 331, 381 ("transfer depth") | source text read |
| defect Ward identity | 17c:66 | Gauge invariance of the current defect: its Hessian symbol vanishes on gradients in each argument. | v3 17c:16, 52–53 | source text read |
| exterior (word, points) | ch. 13–16, 18 | Insertions outside the cluster, at a distance from it that may tend to zero more slowly than the cluster size; spectators are the fixed-distance case. | Scott J-section:400, 730; part1/02-definitions:293 | source text read |
| first crossing | 17:138; 17w:31; 17m:425, 432 | First level at which `log(a_m/a_n)` reaches a target (17w:31: `(b+2) log H_n`, then a further `10 log B_n`); at 17:138 the first `n` with `r(n, α_0)` below the prescribed radius. | Scott I-section:91, 109 | source text read |
| forcing | 17c:380–386 | Inhomogeneous term of `X_m ≤ ½X_{m+1} + ¼`: the term `L⁴𝓘(K_a^t J_aa)` entering the primitive, and the reference-function constant. | v3 17c:380–389; 17t:62–66 | source text read |
| frame (17w:122) | 17w:122 | The comparison isomorphisms `U_{i,d} : 𝓜_d^Max → F_d` of 17:81. | Scott macros.tex:46; I-section:59, 109, 111 | source text read |
| group, live group | 18lp:71, 110 | Group: marks with a common representative. Live: of positive weight. | Scott J-section:224, 236 | source text read |
| kernel identities | 17:308 | The identities for the differentiated block kernel of 17m: (17.kernel-score), (17.kernel-divergence), `∫𝒟_Y k dV = 0`. Not the Laurent block identities (17.block-algebra). | v3 17m:10–66, 150, 396–398, 443, 459; 17m does not cite (17.block-algebra); audit/ch17-marked-rates.md:61 | partly |
| level (`k_i = k(n_i)`; stopping levels) | 17:84–108; 17w:101–102 | `k_i = k(n_i)`; the middle and output stopping levels are the `ℓ`, `w` of chapter 11 with `n` as top. | Scott I-section:91, 109; E-Gaussian-sources:77–81 | source text read |
| mark (5:861; marker) | 5:861; 18:123–124 | "Marked integral maps": the maps of one block step on densities with insertions (12:37, 90). Marker: one group of insertions with one nilpotent variable and one weight. | v3 12:37, 90; Scott J-section:224 | partly |
| ordered limit (17m) | 17m:338, 365 | Period to infinity along the volume sequence, after the cutoff, at a fixed level `k` (a level, not the volume index of 13:46). | Scott I-section:331, 373 | source text read |
| output level (chapter 17) | 17t:405; 17c:241, 391 | The fixed level `k` to which the current is transferred and where the regulator identity is evaluated; later `k_i`. Not the `w` of chapter 11. | Scott I-section:213, 331 | source text read |
| probe (17m:251) | 17m:251 | A coefficient evaluation: derivative of fixed total order of a local function along a polynomial test path of link fields. | Martin trace-row-jet-estimates:160–161, 226–233, 282–285; attribution via audit/ch17-marked-rates.md:69 | partly |
| reconstruction (`𝒫_D`, `H_D`) | 18lp:266–279; 18:67–70 | One map: the low-degree component in the fixed biorthogonal system of probe coordinates. | v3 18r:4–7, 41, 60–61; 18lp:289, 293; Scott J-section:151–161 | source text read |
| regular (17w:78), source recurrences | 17w:78 | The step estimates 11:1541–1544 and (11.lower-weighted-step), 11:1566, in the regular and the large-field norm. Not (11.higher-induction), 11:513. | Scott I-section:98; E-Gaussian-sources:167–171; v3 11:1566, 2135 | source text read |
| remainder with vanishing extracted coefficient | 18lp:27–40 | The remainder of Section `ch11:one-graph`: regular part with vanishing Taylor polynomial plus large-field part with the `κ^{-1}` normalisation. | v3 18lp:26–32; 11:360–366, 379–380 | source text read |
| replicate | 13ba:283; 17m:432 | Put one copy of the observable in every cell of a reflected tiling and take the product; at 17m:432 with the tiling at the first level `m<n` with `a_m/a_n ≥ B_n²`. | Scott E-several-mark:188–195 | source text read |
| the supplied construction | 3:547; 5:195 | The construction of the source manuscripts, i.e. the one the book presents. | Scott G-section:120–128; B-section:194–196; no source sentence has the phrase | partly |
| forest prescription (Notes, point 2) | 18:398–421 | The recursive subtraction of normal Taylor jets over nested collision subsets. Lean defines it and states and uses a theorem for it; the main theorem does not include the contact clause. | Lean definitions and statements read (see Notes) | Lean definition read |
| smooth representative `W_a` (Notes, point 4) | 5:1108; 17m:264 | `W_s − d_f E R W_s`; Lean has `R`, `𝒬` and the forest representative, with the identities of (5.actual-transport-identities) proved for the latter; no smooth extension `E` found. | Lean `YM.Precision.fixRoot`, `probe`, `straighten`, `extracted`, `centers`, `stays`, `stationed` (read) | still open |

---

<a id="appendix-l"></a>

## Appendix L. Names in the papers of Bałaban and Dimock

Fifteen papers were compared with the dictionary by five agents; a sixth merged their reports. Each match is recorded in the entry concerned under *Literature*. Matches were made on the mathematics as described in the papers, not on similar words. No finding here has had a second reader, and the coordinating agent did not open the papers.

### Papers read

Page numbers are journal pages (for D1, D2 the article number followed by the page). All papers except D1–D3 are scans with an OCR text layer: prose is reliable, displayed formulas and Greek, script or Fraktur letters are not. "Image" means the page was rendered and read as a picture; a formula quoted from any other page comes from the text layer and its symbols and constants were not verified. Bracketed numbers inside quotations ("[15]", "[I]", "[5]") are the quoted paper's own reference keys.

| Abbr. | Reference | Read in full | Skimmed only, or not read |
|---|---|---|---|
| B84a | T. Bałaban, Propagators and renormalization transformations for lattice gauge theories. I, Commun. Math. Phys. 95, 17–40 (1984) | All prose pp. 17–40 (text layer); pp. 19, 23, 29, 34 as images | The Fourier formulas of pp. 24–33 and the proof of Proposition 1.2 (pp. 36–40) were not checked symbol by symbol |
| B84b | T. Bałaban, Propagators and renormalization transformations for lattice gauge theories. II, Commun. Math. Phys. 96, 223–250 (1984) | Prose pp. 223–245 (text layer); pp. 224, 245 as images | pp. 246–250 at the level of proposition statements only; (2.154)–(2.155) not seen; the formula for `𝒢_j` on p. 246 is garbled and was not used |
| B85a | T. Bałaban, Averaging operations for lattice gauge theories, Commun. Math. Phys. 98, 17–51 (1985) | pp. 17–30 and the opening of §F, pp. 43–45 (text layer); pp. 19, 24, 31, 36, 43, 44 as images; the whole text layer was searched by keyword | pp. 30–42 (algebra of §C after (81), proofs of Propositions 3–5) and pp. 45–51 (Propositions 9–10, end of §F): statements read in the text layer, displayed conditions mostly not; (176)–(177), (207), (213) not reconstructed. The quotation of Proposition 1 (p. 26) is from the text layer |
| B85b | T. Bałaban, Spaces of regular gauge field configurations on a lattice and gauge fixing conditions, Commun. Math. Phys. 99, 75–102 (1985) | pp. 75–86 (text layer); pp. 77, 78 as images; the whole text layer was searched by keyword | pp. 86–102 (proofs of Proposition 3, Theorem 4, Proposition 5, §§E–H): statements only; (1.61), (1.62), (1.66), (1.139)–(1.146) not reconstructed. The quotations of Lemma 1 (p. 79) and of (1.35)–(1.37) (p. 82) are from the text layer |
| B85c | T. Bałaban, Propagators for lattice gauge theories in a background field, Commun. Math. Phys. 99, 389–434 (1985) | pp. 389–397 (text layer); pp. 417, 428 as images | Sect. B (pp. 398–407) and Sect. C (pp. 408–416): headings, theorem statements and keyword search only; Sect. D (pp. 419–427): theorem headings only; Sect. E pp. 429–431 skimmed; the appendix on chiral models (pp. 432–433) not used |
| B85d | T. Bałaban, The variational problem and background fields in renormalization group method for lattice gauge theories, Commun. Math. Phys. 102, 277–309 (1985) | pp. 277–281 (text layer); pp. 278, 279, 285 as images | Sect. B (pp. 281–285): first lines only; Sects. D–E: proposition statements only; Sect. F (pp. 300–304): not read; Sect. G (pp. 305–309): first and last paragraphs. The text layer of this file renders Greek and script letters badly; symbols were checked only on the three images |
| B85e | T. Bałaban, Ultraviolet stability of three-dimensional lattice pure gauge field theories, Commun. Math. Phys. 102, 255–275 (1985) | pp. 255–275, all; pp. 257, 266 as images | Nothing omitted; formulas (62), (70)–(71) quoted from the text layer |
| BIJ85 | T. Bałaban, J. Imbrie, A. Jaffe, Renormalization of the Higgs model: minimizers, propagators and the stability of mean field theory, Commun. Math. Phys. 97, 299–329 (1985) | §1–§4.1 and the opening of §4.4 (pp. 299–312) | §5–§7 and the Appendix: keyword search only |
| B87 | T. Bałaban, Renormalization group approach to lattice gauge field theories. I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions, Commun. Math. Phys. 109, 249–301 (1987) | pp. 249–277 (Sects. 0–2 and Sect. 3 to (3.35)), pp. 280–281, 291–292, 298; pp. 254, 255, 259, 260, 264, 266 as images | pp. 277–280 (rest of Sect. 3), pp. 281–291 (Sect. 4, Ward–Takahashi identities), pp. 292–297 (Sect. 5, analysis of `Π`): keyword search only. Statements about Sects. 4–5 rest on the introduction and on pp. 264, 292. Formulas (0.24)–(0.29), (2.3), (2.15) are from the text layer |
| B88a | T. Bałaban, Renormalization group approach to lattice gauge field theories. II. Cluster expansions, Commun. Math. Phys. 116, 1–22 (1988) | pp. 1–22, all; pp. 12, 14 as images | Nothing omitted; formulas (1.26), (1.31), (2.30), (2.31) are from the text layer |
| B88b | T. Bałaban, Convergent renormalization expansions for lattice gauge theories, Commun. Math. Phys. 119, 243–285 (1988) | The text layer of the whole paper, restricted to lines of at least five words; pp. 246, 252, 255, 257, 258 as images | Displayed formulas on the other pages were not seen: (2.26)–(2.27) and (2.40)–(2.42) on pp. 259–261 are quoted from the text layer. §3 from p. 272 on (cluster expansion details, proof of Theorem 2, Ward–Takahashi argument) was skimmed for names only |
| B89a | T. Bałaban, Large field renormalization. I. The basic step of the R operation, Commun. Math. Phys. 122, 175–202 (1989) | pp. 175–190, complete text layer; pp. 188, 201 as images | pp. 191–202: text layer restricted to lines of at least five words. (0.1)–(0.6) on pp. 175–176 and (1.24) were not rendered; the exponents `p_0` against `p_0²` in (0.1) could not be decided |
| B89b | T. Bałaban, Large field renormalization. II. Localization, exponentiation, and bounds for the R operation, Commun. Math. Phys. 122, 355–392 (1989) | The text layer of the whole paper, restricted to lines of at least five words; pp. 379, 380, 381, 384, 387, 388, 390, 391 as images | pp. 356–376 (cancellation of the Wilson terms, localization of the background field) skimmed for names only; (1.79), p. 383, not rendered |
| B95 | T. Bałaban, A low temperature expansion for classical N-vector models. I, Commun. Math. Phys. 167, 103–154 (1995) | §1–§2 (pp. 103–121) | §3–§4: keyword search only |
| B96 | T. Bałaban, The variational problems for classical N-vector models, Commun. Math. Phys. 175, 607–642 (1996) | §1 (pp. 607–611) | The rest was not read; the text layer loses most Greek letters |
| D1 | J. Dimock, The renormalization group according to Balaban, I. Small fields, Rev. Math. Phys. 25, 1330010 (2013) | Introduction, §2.1–2.5, §3, §4.1–4.2; §4.4–4.8 (statements and definitions); §5 (statements); pp. 1330010-19, -22 as images | Proofs in §4.3, §4.9 and Appendices A–E: keyword search only |
| D2 | J. Dimock, The renormalization group according to Balaban, II. Large fields, J. Math. Phys. 54, 092301 (2013) | §I; §II.A–C (definitions); §III.A–E; §III.J; headings and opening paragraphs of §III.F–R; pp. 092301-26, -27, -31, -42, -43 as images | §II.D–E, the proofs of §III.K–R and Appendices A–E: keyword search only; Appendix F: opening only. The text layer drops the capitals Ω, Λ, Π, Φ |
| D3 | J. Dimock, The renormalization group according to Balaban, III. Convergence, Ann. Henri Poincaré 15, 2133–2175 (2014) | §1 (Theorem 1); the openings of §2, §3, §3.5, §3.6; Appendix B | The rest: keyword search only |

On the v3 side only parts of chapters 4–10 were opened (4:1–677; 5:30–200, 905–1160; 6:1–125, 516–540, 826–846, 1325–1350, 1455–1482, 1538–1548; 7:1–26, 177–232, 825–860, 988–1000; 8:21–80, 275–350; 9:1–96, 392–412, 626–765; 10:209–260, 650–670); every other statement about v3 is taken from the dictionary entries. Identifications marked as inferences in the literature lines were not checked against the v3 formulas.

### House terms with no counterpart in the papers read

A term is listed only if none of the eighteen papers gave a counterpart, by name or by object. Terms whose object has a counterpart but whose word has none (for example *predictor*, *gas*, *fusion*, *reset*, *shooting*, *thermal*, *noise*, *replica*, *warning*, *inventory*, *trajectory*) have a literature line in the other file.

**Frames and random choice.** *fallback* (frame, connector, branch); *frame seed*, *shared frame seed*; *likelihood* (tests, factors); *live group*, *live tag actions*; *minimizing branch* (and the minimising frame and frame energy `𝓔_U(h)`); *random index*; *tag*, *tag average*, the weights `λ(U,α)`; *uniform mass*; eligibility as a selection rule (*eligible*, sense 1, has only the underlying axial estimate). Nothing in the papers read is randomised, and no gauge is chosen by minimisation: Bałaban's averaging operation is one deterministic formula, defined through the principal logarithm and controlled only on regular configurations ("Formally, it is defined for all configurations, but we have good control over it for configurations U satisfying the regularity condition (52)", B85a p. 42); the random choice of frame and the two-branch definition are v3's own construction. The only discrete averaging in the papers is over gauge-fixing graphs with constant weights `N_i = 1/(2^d d!)` (B89a p. 201). In role, the minimizing branch corresponds to the domain on which the averaging operation is regular (B85a pp. 42–43), and the nearest construction to the frame normalisation is the averaging operation for gauge transformations, B85a (61), (78).

**Large-field bookkeeping.** *allocation* (sense 2, core/annulus); *channel*; *clip*; *cutoff* (sense 2, smooth cutoff); *large-field profile*; *new-small-field*; *number of attachments* and the attachment reserve; *plaquette whose relaxed small-field condition is not automatic*; *plateau* (sense 1); *relaxed* (small-field condition); *restart* (restarted threshold, restarted representation); *seeded sector* and the unseeded law; the "sector Gaussian"; "mask" (not a headword). All cutoffs in the papers read are sharp characteristic functions with one threshold, and there is one operation `T_k(X)` per component of the large field region, so the vocabulary that v3 needs for smooth overlapping cutoffs and for families of activities sharing a support has nothing to correspond to. Where v3 distinguishes a seeded sector from the unseeded law, Bałaban states the opposite fact positively: the small-field integral in the presence of large-field regions "is equal to the corresponding conditional integral in the case analyzed in [I], i.e. where there are no large field regions, but with a different background field" (B88b pp. 252–253). The nearest thing to a relaxed condition is "tighter restrictions near the boundaries relative to the bulk" (D2 Def. 3.4, p. 092301-26), which is not an exponentially weighted threshold.

**Scheduling.** *block floor*, *floor*; *change of stage*; *delay*; *horizon*; *plateau* (sense 2), *stage plateau*; *regularity-stage index `J_m`*; *request*; *schedule*, *scale schedule*, *numerical schedule*; *stage* as a regularity class (the word occurs with another meaning: see Name clashes). In every paper read `L`, `M` and one set of constants are fixed once for all steps ("an odd, positive integer > 11", B87 p. 251; Theorem 3, B87 p. 264; D1 p. 1330010-28), and no regularity class varies with the scale; the only step-dependent discrete parameter is the length `R_j`, "the smallest number of the form `L^r` such that `R_j ≥ (log g_j^{-2})^r`" (B88b p. 255). The level-dependent schedule is v3's own.

**Accounting words.** *budget*; *loss*; *margin*; the nouns *cost* and *gain* as a system (the verb "gain" and "small factor" are in D1, D3: see *gain*); the pair *hard* / *soft* as a pair. The papers describe these operations by verbs ("We extract the expression … from each factor", B88a p. 18; "controls", "is suppressed by") and write the splitting `exp(−κd) = exp(−δκd)·exp(−(1−δ)κd)` explicitly; the accounting nouns are v3's.

**Insertions and correlations.** *background insertion* (the first insertion); *chessboard seminorm*; *copy*; *normalization index*; *replica* in the chapter 11 sense; *squarefree source algebra*; *spectator* in v3's sense. The papers read treat partition functions and effective actions; correlation functions appear only as a remark (B95 p. 108; D3 p. 2171), and chessboard bounds only as other authors' methods (B95 p. 105), so this vocabulary has no source in them; for *source*, *marked* and *unmarked* only an ordinary source `g` occurs (see *source*).

**Other.** *discrepancy* (senses 1–3, 5); *fine residue*; *mismatch* (sense 2); *rooted* (only sums over domains containing a cube or a point occur; for the anchor see *anchor*); *row* (sense 5, the factorisation `C^*C = H`); "covariant" as a house term (used only in the ordinary sense: covariant derivative `D_U`, covariant Laplace operator `Δ_U`). These are either unnamed auxiliary objects of v3 or consequences of the differences listed below.

### Name clashes

| Word | Meaning in v3 (headword) | Meaning in the literature |
|---|---|---|
| stage | regularity class `j` (*stage*, 10:25–31) | a step of the iteration (D2 p. 092301-19: "At the kth stage of the iteration"; D3 p. 2133) |
| history | one fixed choice of kernels, couplings and path pairs (*history*, sense 2); the sequence of densities at one cutoff (sense 3) | the sequence of small-field regions `Π = (Ω_1, Λ_1, …, Ω_k, Λ_k)` (D2 p. 092301-29: "the history dependent parts of R_{k,Π}") |
| order (of an averaging operator, of a block) | the number `j` of box convolutions in the averaging weight (*smoothing order*, *coarse kernel level*) | the number of composed steps: "block of an order j", "k-th order averaging" (B85a pp. 17, 24); "averaging operators of different orders" (B84b p. 223) |
| random walk, walk | a lattice path (*walk*) | a sequence of cubes or localization domains in the expansion of a propagator (B85c pp. 409, 413; B88a pp. 1–3; D1 p. 1330010-12); a lattice path is a "contour" |
| regular | the regular term `E_reg`, regular activities (*regular*, sense 1) | "regular configuration", "regularity condition": a small-field bound on plaquette variables (B85a p. 26; B85b pp. 75, 77; B85d pp. 277–278; B87 p. 254). "The regular part of the action" (B88b p. 259) agrees with v3 |
| localization | Taylor extraction of a local polynomial, the map `T` (*localization*, *common localization*) | writing a functional as a sum over polymers by a decoupling expansion (D1 p. 1330010-36; B95 p. 118); "localization domain" (B87 p. 257) |
| buffer | margin of a word in a slab (*buffer*, 13:332–335) | nested enlargement `Ω(X)` of a polymer (D2 p. 092301-21, Fig. 2) |
| spectator | the other insertions of a correlation (*spectator*) | "spectator variables": fields left in holes from earlier stages (D2 p. 092301-61) |
| activity | any local term of a density, regular or large-field (*activity*, sense 1) | only the activity of a polymer expansion, `H(Z)` (B88a p. 14), `F(X')` (B89b (1.91)); a regular activity is a "localized term", "potential" (B88a p. 15) |
| `W` | the stationary tangent (*stationary tangent*) | the unit-covariance fluctuation variable `W_k`, `Z = C_k^{1/2}W` (D1, D2); "auxiliary variables" `W_{k,Π}` (D2 pp. 092301-20, -27) |
| level index | `m`: `0` coarsest, `N` finest; a step goes from `m+1` to `m` (*level*) | `k`: `0` finest (bare), increasing towards the unit lattice, with rescaling after each step (B87 p. 256; D1); for fixed `L`, `k = N − m` (an inference) |
| scale | the index `m` (*scale*) | also the lattice spacing `η = L^{−k}`, `L^{-j}` of a region; "unit scale" `K` (B87 p. 256) |
| axial | the patch frames of chapter 4 only; the block gauge is called tree gauge or forest (*frame*, *tree slice*) | both are "axial gauge" at different sizes (B84a p. 19; B85a pp. 24, 27; B85b p. 98) |
| partition of unity | the weights over large-field selections (*allocation*) | "decomposition of unity" for field sizes (B85e p. 257; B88b p. 246); "partition of unity" for the spatial `Σ ζ_□ = 1` (B87 p. 270) and `{h_□}` (B84b p. 235; D1 p. 1330010-14) |
| normalization (conditions) | conditions on regular activities (*affine Hessian*); *normalization index* | D1: removal of relevant terms ("normalized" functional, p. 1330010-22), which is v3's extraction; B87 pp. 294–295: a Laurent decomposition in the analysis of `Π`, unrelated |
| remainder | the part of a term that is not its local polynomial part (*remainder*) | "tiny remainder" `R_{k,Π}`, bounded by `λ_k^{n_0}` (D2 p. 092301-28) |
| new small field | re-thresholded small-field condition (*new-small-field*) | the next step's region, "new small field region Ω_{k+1}" (D2 p. 092301-31) |
| weaken | ordinary verb (*weaken*) | "weakening parameters `s_□`", "weakened" propagator (D1 p. 1330010-16) |
| admissible | several senses (*admissible*); for index families v3 says "eligible" | allowed sequences of domains and index sets (B88b pp. 248, 257; B89b p. 390; B85e p. 258); this is the sense of v3's sources |
| soft | the Gaussian block constraint (*soft constraint*); the bound on `e^{ℓ_a} − 1` (*soft correction `a_s`*) | no such word; the only exponential factor is the "exponential gauge fixing functions" (B87 (0.14)), a different object |
| extract | take out a polynomial coefficient (*extraction*, sense 2) | take a small factor out of a bound (B88a p. 18; B89b p. 389) |
| `χ` | distance from the identity `χ(u)` (*distance from the identity*) | characteristic function `χ`, `χ_k`, with `ζ = 1 − χ` (all papers) |
| `β` | inverse coupling `1/g²` | the β-function `β_{j+1}(g_j)` (B87 p. 264); constants `β`, `β′` in B87 (0.31); a small number in B88b p. 262 |
| `R` | linearised frame average (5:985) | projection defining the Landau-type gauge (B84a p. 24, (1.38)); adjoint action `R(U)X = UXU^{-1}` (B85c p. 390); the R operation (B89a); the set `R_j`, `R_{k+1}` of large fluctuation fields (B88b, D2); the length `R_j` (B88b p. 255) |
| `C` | the factor in `C^*C = H` (*row*, sense 5) | parametrisation of the constraint surface, `B = CB̃` (B85c p. 428); unit lattice propagator `C^{(k)}`; remainder `C_j(U,A)` of the average (B85d p. 285) |
| `H` | metric on two-forms; "block average derivative" | the minimiser operator `H_k` (B84a p. 26); polymer activity `H(Z)` (B88a p. 14) |
| `Δ` | remainder of the coupling update, `β = β′ + α + Δ` | Laplacian `∂*∂ + ∂∂*` and Wilson-action Hessian `Δ^η(U)`; action `Δ_k`; cubes `Δ(y)` (B84a, B85c) |
| `B` | range parameter of chapter 6, `B_m` | the coarse field (B84a); the boundary terms `B_k` (B88b p. 259); blocks `B(y)` |
| `A` | the completed matrix `K_f + bQ^*Q`; a large-field selection | the fine field (B84a); the Wilson action `A(U)` and effective action `A_k` (B87) |
| `a` | — (v3's constant is `b`) | the constant of the Gaussian block kernel (D1, B95) and of the auxiliary operator `Δ_a` (B84a p. 25) |
| `P`, `Q` (sets) | — | in B88b `P` = large plaquette of the new field, `Q` = large approximate fluctuation field; in D2 `P` = large deviation from the block average, `Q` = large new field. In B84a `P = I − R` is a projection, and `Q` is the averaging operator |
| `T` | the localization map (*common localization*) | the renormalization transformation `T` (B84a p. 19; B87 p. 254); the integral operation `T_k(X)` (B88b) |
| `ρ` | the stationary graph `ρ(v)` | the density `ρ_k` (B85e p. 256; D1) |
| `Γ` | the finite-range covariance of 6:534 | contours `Γ_{y,x}` (B84a p. 18) |
| `Ω` | index neighbourhoods `Ω_i^sec`, `Ω_i^loc` (*window*) | small-field regions `Ω_j`, sequences `Ω_1 ⊃ … ⊃ Ω_k` (B84b, B85b, B88b, D2) |
| `M` | the straight average (*straight*) | the side of the cubes of the cluster expansion; the group average `M({U_j})` (B87 p. 253) |
| `S` | actions `S_0`, `S_3`, `S_4` | the rescaling `S` (B84a p. 20); the operation `S(Z) = Z'^{~10}` (B89b p. 384) |

The rows from `χ` to `β` and the last six rows are read off the formulas quoted in the literature lines; the other letters are listed as clashes in the comparison of B84a–B85d.

### Differences between v3 and the literature that affect naming

1. **Soft constraint against delta function.** In all of Bałaban's gauge-field papers the block transformation is `δ(B − QA)` or `δ(VŪ^{-1})` with a delta-function axial gauge fixing (B84a (1.12); B85a (10); B87 (0.17); B88b (2.21)); v3 has the weight `exp(−(b/2)‖Qa − v‖²)`, in the group the kernel `q_{bβ}`. A Gaussian kernel with constant `a` is the choice of the scalar papers D1 and B95, and BIJ85 has an "approximate delta function" for the scalar field only. Consequences: `W` is not `H_k` (`QW ≠ I`); `(K_f + bQ^*Q)^{-1}` is v3's fluctuation covariance but only an auxiliary Green's function `G` for Bałaban; "block penalty", "mismatch", "discrepancy" have no gauge-theory counterpart; the stationary field is a critical point of action plus penalty, not of the action at fixed averages. Bałaban's "exponential gauge fixing" (B87 (0.14)) must not be cited for the soft constraint.
2. **One step against `k` steps.** `Q_k`, `H_k`, `G_k`, `U_k(V)` connect the unit lattice with the `L^{-k}` lattice at once, and the effective action is a function of the background field `U_k(V)`, the minimiser of the Wilson action on the finest lattice (B87 (1.3), (2.3)). v3's `M`, `W`, `K_c`, `ρ` are one-step objects with separately tracked recursions, and the effective density is an explicit function of the coarse links (path action, 4:496–521). Hence v3 needs a classical matching through order four (7:988–998), which has no counterpart; and calling `ρ(v)` "the background field" without qualification would mislead.
3. **No R operation in v3** (an inference from the v3 text read, not a statement found in v3). In Bałaban a large-field region persists: its variables stay unintegrated inside `T_k`, the region grows by `S(Z) = Z'^{~10}` at each step, and its one-time factor "controls a large number of steps, but this number is a small fraction of the total number of steps" (B88b p. 244); the R operation replaces such a component by a small-field expression, dividing by a normalising integral (B89a (1.100)). In v3 every link is integrated at every step (the frozen links by Haar measure, 9:48–52), a large-field activity is a function of the current field, and the activities are re-estimated at each step. v3's representation is the one Bałaban reaches only at the end, B89b (1.104). No v3 term should be glossed as "the R operation" or "R-terms". Whether the per-step re-estimation achieves what R achieves was not checked. Dimock's φ⁴ model also omits the R operation (D2 p. 092301-29).
4. **Exact identities against "equivalent" densities.** v3's step acts on the density exactly (9:5–8). Bałaban's `Rρ_k` is only "equivalent" to `ρ_k`: "the equivalence means that both sides have equal integrals over the space of fields `V_k`" (B89a p. 193; B89b p. 378, "equivalent, but not equal"). B87, B88a represent only the small-field part of the density, and B85e gives an upper bound (41) with a separate lower bound (47). A v3 identity called by a name from these papers would import the weaker meaning.
5. **Smooth against sharp decompositions of unity.** All papers read use characteristic functions with one threshold. v3 uses smooth weights with overlapping thresholds (`t_f/4`, `t_f/2`), `clip`, the relaxed condition and cutoff remainders. A reader of Bałaban or Dimock will recognise `1 = Π(ζ + χ)` but not the words; "decomposition of unity" fits v3's allocation only with "smooth" added.
6. **What counts as large field.** In B88b, B89a, B89b and D2 every failed condition (plaquette, approximate fluctuation field, fluctuation field) creates large field region. v3 treats fluctuation failures as cutoff remainders that do not enter `Bad_m(U)`. See the next section.
7. **Random frames.** Bałaban's average uses one fixed axial contour system from the block base point, one coordinate order, hence is not invariant under lattice symmetries, and is defined by one formula with no control off the regular configurations. v3 uses a symmetric minimising frame when all loop transports are small and otherwise a uniformly random eligible axial pair, with estimates valid for all configurations. The symmetric and the random parts, eligibility and the first-power bounds have no antecedent.
8. **Definition and weight of the average.** Bałaban: exponential of the uniform block mean of logarithms about `U(c)`, uniform weight `L^{-d}` on one corner-based block, `L > 1` any integer in B84a, B85a. v3: Hilbert–Schmidt-nearest group point to a weighted Euclidean mean, `j`-fold convolution weight on centred blocks, `L` odd, overlapping patches of radius `(j+3)L`. Bałaban's regularity and decay come from the Landau gauge and Green's function estimates, not from smoothing the weight.
9. **Gauge.** Bałaban ends in a Landau gauge relative to a background, with a uniqueness theorem (B85b Theorem 2), reached from the axial gauge by the Faddeev–Popov procedure; the axial gauge is his "preliminary gauge condition". v3's chapters 4–6 stay in the tree gauge, used as a chart. Bałaban's `H` satisfies `R∂^*H_kB = 0`; v3's smooth representative `W_a` is built by a gradient correction with a cardinal partition of unity (5:1100–1108). The two play the same role and are different representatives.
10. **One support against two.** Bałaban enlarges regions by layers of cubes until every characteristic function depends only on fields in its own component ("the desired localization property", B88b p. 252), and his polymer is the dependence set (B88a p. 14). v3 keeps the exclusion support and the full dependence region distinct (4:455–464), and allows any disjoint family rather than the connected components of one region. "Component of the large field region" suggests more locality than `Y_i` has.
11. **Exponentiation.** After the polymer expansion of the large-field factors Bałaban exponentiates (B89b (1.98)) and returns the result to the action as R-terms and boundary terms. v3 keeps the exact-cover sum as a separate factor and never takes its logarithm (9:651–666). Dimock sums over nested sequences `Π` with boundary terms tracked through the steps and a final resummation onto the connected components of `Λ^c` (D3); his names (boundary term, history, buffer) do not transfer.
12. **Regularity class and norms.** The literature's terms are analytic on complex neighbourhoods (`U^c_j(X, α_0, α_1)`, B87 p. 262, B88b p. 261; Dimock's analyticity domains), bounded by Cauchy integrals, one sup bound `E_0 e^{−κ d_j(X)}` per connected localization domain. v3's are real Borel functions with finitely many derivatives, with arbitrary supports, in summed containing-site or anchored norms with a covering number, and with a regularity stage. "Localized term" transfers; "analytic" and "localization domain" do not transfer literally; v3's "derivative reserve" has no counterpart.
13. **Renormalisation of the coupling.** Bałaban defines `1/g_{k+1}² = 1/g_k² − β_{k+1}(g_k)` with the full β-function read off the vacuum polarization tensor; the one-loop value and the proof of B87 Theorem 2 are deferred. v3 splits the change into a matched determinant coefficient `α = −κ_G log L + O(1)` and a remainder `Δ` fixed by the exact density identity (9:716–762) and proves the tuning by an intermediate-value argument (10:232–251). "β-function" names `α + Δ`, not `α`. In B88b the coupling is a function `g_k(x)` near large-field regions; v3 has one number. In D1 `λ_k` is pure scaling and only `ε_k`, `μ_k` are dynamical; v3's reference coupling is closer to Bałaban's "ideal flow / actual flow" (B95 p. 112).
14. **Thresholds.** Bałaban's small-field threshold uses the running coupling itself (`g_k p(g_k)`, B85e, B88b) or a fixed small constant (`ε_0`, B87; `α_0`, B85a, B85b); v3's uses a reference `β̂_m` that does not move when `β` is varied (4:414–421).
15. **Indexing and rescaling.** Bałaban's and Dimock's `k` increases towards the coarse lattice with fixed `L`, and both rescale to the unit lattice after each step; v3's `m` increases towards the fine lattice with level-dependent `L_m` and no rescaling step.
16. **Normalisations.** Bałaban: `U = e^{iηA}` with hermitian `A`, `tr 1 = 1`, the average `Q` normalised by `L^{-(d+1)}` (line average); v3: `U = exp(u)`, `M` sums along the line, counting scalar products. The symbol `|X|` is the operator norm in B85a, B85b and the Hilbert–Schmidt norm in B85c, B85d; v3's `χ` is the normalised Hilbert–Schmidt norm.
17. **Minimiser.** Linear and explicit in D1; nonlinear, unique in a small-field space, analytic, constructed by contraction in B95, B96 and in B85d. v3's stationary graph is of the second kind. BIJ85's `H_{k,Ax}`, `H_k` are linear minimisers under a delta constraint in a fixed gauge.

### "Large field" for failures of fluctuation bounds

In B88b, B89a, B89b and D2 the region where a bound on the fluctuation field fails is called large field and is added to the large field region. B88b p. 255: "a large fluctuation field characteristic function associated with the set `R_j`"; after the decomposition of unity in the fluctuation variable the cubes `R_1` (resp. `R_{k+1}`) are surrounded by a layer and removed from the small field domain, "This domain `Λ_1` is the final small field domain" (B88b pp. 250–251, 268–269, text layer), and `Λ_1^c` is "the large field domain" (p. 252). B89a p. 188, (1.55): "We exclude from `Z` the components with the large field function `1 − χ'^{(j)}`", where `χ'^{(j)} = χ({|B_j(b)| < δ'_j …})` restricts the Gaussian integration variable `B_j`; p. 181: "In components with the function `1 − χ` we have introduced new large fields". B89b p. 380: "Take the cover of the large field region `P_j ∪ Q_j ∪ R_j`", `R_j` being the fluctuation-field set. D2 p. 092301-43: "Anticipating that the factor exp(−½‖W_k‖²) suppresses large W_k we define χ^w_k(□, W_k) = Π χ(|W_k(x)| ≤ p_{0,k})" and "The new large field regions Q_{k+1}, R_{k+1} generate a new small field region Λ_{k+1}". Bałaban does separate the two mechanisms, but in the estimate and not in the name: `χ^c_j(P_j)` gives its factor "in the usual way, using Theorem 1 [15]" (from the Wilson action of the large plaquette), whereas `χ'^c(Q_j)` and `χ^c(R_j)` give theirs "by expanding the Wilson action locally in the approximate fluctuation field, and using the positivity bound for the resulting quadratic form" (B89b p. 380). v3 chapter 6 (6:7–11) separates "selected large plaquette fields and large block average discrepancies", which retain a deterministic positive energy, from "failures of smooth local cutoffs", which are "controlled by simultaneous Gaussian tail estimates"; a cutoff failure does not enlarge `Bad_m(U)`, and its remainders are organised as a polymer of cutoff remainders rather than as an enlargement of a region. So the literature includes both kinds of failure in the "large field region" under one name and distinguishes them only by the estimate, while v3 keeps two names for them. The dictionary's rule "cutoff-failure event, never large-field event" is thus a v3 convention that departs from the naming of B88b, B89a, B89b and D2; if it is kept, the entries *cutoff failure*, *large-coordinate event*, *tail events* and *warning* need the explicit statement that these events are what the literature calls large fluctuation field events, and the distinction is best stated in mathematical terms (large integration variable against large plaquette field).

### Names in the literature with no dictionary entry

**Transformations and gauges.**
- **Rescaling `S`**, "scaling transformation" back to the unit lattice after each step (B84a p. 20; B95 pp. 106–107; D1 p. 1330010-5). v3 seems to keep the lattices fixed and vary the spacing (inferred from the *scale* entry only).
- **Faddeev–Popov procedure** (B84a p. 20; B84b p. 227; B85c p. 417; B87 p. 255); **Feynman gauge**, **Landau gauge condition**, "generalized Landau conditions" (B85b pp. 76, 80, (1.27)); **exponential gauge fixing** (B87 (0.14)); **preliminary gauge condition** (B85b p. 81); the "transformation from the axial gauge to the Landau gauge" (B85b §C, Theorem 2, p. 83).
- **Projection `R`** onto `ΔN(Q'_k)` (B84a p. 24, (1.38)), `P = I − R`; **projection `𝒫`** on `{QA = 0, R∂^*A = 0}` (B84a pp. 34–35, (1.104)–(1.107)); v3's unnamed soft analogue is the splitting `a ↦ a − WQa` in (5.completion).
- **Scalar averaging operator `Q'`, `Q'_k`** on gauge functions (B84a pp. 19–20; B85c p. 393); **operators `G'`, `G'_k`, `H'`** (B84b p. 241); **averaging operations for gauge transformations** `\overline{R_0 u}^j` and the class `A_k(U_0, α_3)` (B85a §F, pp. 43–44).
- **One-step / k-th order averaging operation**, composition of averaging operations (B85a §B, p. 23); the **new averaging operation** `Ũ_1^k` of the relative field (B85a p. 31), whose logarithm is `Q_k(U_0,ηA)`; in v3 the corresponding object is the block average in forest-chart coordinates about `rep V`, unnamed (an inference).
- **Linearizing transformation** `A = A' − H𝒟(A')`, "change of variables linearizing the function Q" (B85d p. 285; B87 p. 267; B88a p. 2; B85b §E, p. 95); **remainder `C_j(U,A)`** of the average (B85d p. 285, (44)), possibly related to v3's *contact term* (not examined).
- **Orbit**; a gauge condition as a **surface** "intersecting each orbit at exactly one point" (B85b p. 78; v3 says "slice"); the subgroup `u(y) = 1 for y ∈ 𝔅_k` (B85b p. 78, (1.14)), which is v3's unnamed "root normalization" (gauge transformations acting on the coarse field through block roots only, 4:262–263); the fibre `𝔅_k(𝔅_k, V)` of configurations with `Ū^j = V` (B85b p. 78).
- **The constants `a_j`**, `a_{j+1} = a a_j/(aL^{-2} + a_j)` (B84b p. 225; B85c p. 393): the recursion of the constant term of v3's covariance recursion (5:172–177).
- **Bond**, **bond variables**, **plaquette variable** `U(∂p) = (∂U)(p)`, `f(p) = (∂A)(p)` (B84a p. 18, (1.2); B85a pp. 18, 33; B85b p. 77), **gauge function**, **covariant derivative** `D_U` (B85b p. 76): v3 says link, edge, plaquette field.

**Fields and the variational problem.**
- **Background field**, **fluctuation field**, **approximate fluctuation field** (B88b p. 247), **minimal / critical configuration**, **minimal orbit**, **critical orbit**, **minimizer**, **approximate minimizer** (D2 §III.F), **classical field** (BIJ85 p. 301), **mean field theory** = the quadratic approximation `S_Q^{(k)}` (BIJ85 p. 299). The dictionary has only the house words (*stationary …*, *noise*).
- **Saddle point method / steepest descent** (B87 pp. 256, 265).
- **Regularity conditions**, **spaces of regular field configurations** `𝔘_k({Ω_j}, α_0)`, the **second regularity condition** (1.9) on `D*∂U` (B85b pp. 77, 101; B85c p. 396; B85d pp. 277–278); the domain of regularity of the averaging operation (B85a pp. 42–43).
- **Fundamental fields** `Φ_{k,Ω}`, **auxiliary variables** `W_{k,Π}` (D2).
- **Propagator**, **unit lattice propagator** `C^{(k)}` (B85c p. 427); **(generalized) random walk expansion** (B84a p. 36; B85c p. 408; B88a pp. 1–3; B88b p. 275; D1 §2.4); **weighted distance `d(y,y')`** over admissible contours (B84b p. 231).

**Domains and large fields.**
- **Small field region / domain**, **large field region** `Z_j = Λ_j^c`, **large field domain**; **admissible sequence of domains** `{Ω_j}`, `{Λ_j}`, `{S_j}`; **determining set** (B88b p. 255); **generating set** (B89a p. 179; B96 p. 608); **separation condition** (D2 p. 092301-19); **big blocks** of size `M_1` (B84b p. 224; B85b p. 77; B85e p. 257); boundary conditions "obtained by building an effective mass on the domain" and Dirichlet conditions on `Ω_0^c` (B84b p. 229; B85c p. 394). The dictionary has `Bad_m(U)` but no headword *small-field* or *large-field region*.
- **Characteristic functions**: small field, large field, large fluctuation field; "large field function `1 − χ`"; **redundant characteristic functions** (D2 p. 092301-46); **decomposition of unity**.
- **Integral operation `T_k`**, one-step operations `T^{(j)}`, **factorization properties** (B88b pp. 257–258).
- **R operation** (`R`, preliminary form `R'`), "renormalization of the expressions connected with the large field regions" (B89a p. 175); the operations `RT` (B88b p. 243); **R-terms** `R_k` (B88b p. 259); **equivalent densities** and "the fundamental normalization property" (B89a pp. 193, 201); conditions (i), (ii) selecting the components to which R is applied, **preliminary integrations** (B89a pp. 177, 190; B89b p. 381); the operation `S(Z) = Z'^{~10}` and "The factor `exp(−κ_j(Z))` controls `K` renormalization steps" (B89b p. 384). Dimock reports the R-operation without using it (D2 p. 092301-29).
- **Boundary terms** `B_k` (B88b p. 259); **active / inactive boundary term** (D2 p. 092301-28; D3 p. 2136); **tiny remainder** `R_{k,Π}` (D2 p. 092301-28); **bare action** `S_k^+`, **unrenormalized action / potential** (D2 pp. 092301-28/29).
- **Stability bound** (B85e (70)–(71); D1 Theorem 1; D3 Theorem 2); **ultraviolet stability** (B85e p. 256; B87 p. 259; B88b p. 264; B89b pp. 355–356): v3's uniform activity bounds are this property.
- **Layer of cubes**, the operation `~`, **buffer** `Ω(X)` (D2).

**Expansions.**
- **Localization domain** `X ∈ D_j`; **linear size** `d_j(X)`, **relative linear size**, **tree size**; the **scaling inequality** for the linear size (B88a p. 9, (1.31)), whose v3 analogue would be the comparison of `cov_B` at adjacent levels; **reblocking** (D1 §3.4).
- **Localization expansion**, **decoupling expansion**, **decoupling / weakening parameters** `s(Δ)`, `s_□` (B88a pp. 3–4; D1 §2.5; D2 p. 092301-53; B95 p. 118).
- **Mayer expansion**, **polymer expansion**, **exponentiated cluster expansion**, **exponentiation**, **cluster expansion with holes**, **polymer with holes**, **M-polymer**, **multiscale polymers**, **small / large polymers**, **ultralocal** measure (B88a; B89b; D1; D2); **conditioning** (B88a p. 12); **cumulant expansion**, **loop variables** (B85e pp. 262, 264).
- **Analytic extension to complex field configurations**, the spaces `U^c_j(X, α_0, α_1)`, `U_k^{(n)c}` (B87 pp. 251, 262; B88b p. 261; B89a p. 190); Dimock's **analyticity domains** `R_k`, `P_k(□, δ)` (D1 Def. 2; D2 Defs. 3.2–3.5); B95's spaces `Φ_j`, `Ξ_j`, `Ψ_j`. v3 uses finitely many real derivatives instead.

**Renormalisation.**
- **Effective action**, **effective density**, **density** `ρ_k`; **bare coupling constant**, **effective / running coupling constant**; **β-function**; **renormalization group equations (Callan–Symanzik equations)**; **renormalization group flow**, **ideal flow / actual flow**; **unit lattice / unit scale**.
- **Relevant / marginal / irrelevant** terms (B87 p. 259; B85e pp. 264, 267; B88b pp. 260, 281; B95 p. 119); v3 says "marginal quadratic coefficient" (7:177) with no entry.
- **Vacuum polarization tensor** `Π` (B87 pp. 264, 291); **Ward–Takahashi identities** (B87 pp. 251, 258, Sects. 4–5; B88b p. 280); **Euclidean covariance**.
- **Vacuum energy (renormalization) counterterm**, **normalization factor**, **energy density**; **coupling constant renormalization**; **renormalization conditions / operations**; **normalized** functional.
- **Tuning**, "non-perturbative renormalization" (D1 p. 1330010-42).
- BIJ85: **surface bonds**, **edge plaquettes**, **edge average** `Q^e` (pp. 304–305).

## Unmatched

House terms used in the comparisons that are not `#### ` headwords of terminology.md; their findings were attached to the headword named.

- **small-field** (set, condition, `h_X`), **regular configuration**: under `Bad_m(U)` and *regular*.
- **effective density**, **density**: under *density coordinates* (a new headword is suggested there).
- **running coupling `β`**, **reference coupling `β̂_m`**: under *coupling band*.
- **polymer**, **incompatibility / hard-core**: under *activity* (sense 2).
- **cluster expansion** (chapter 8 logarithm): under *gas* and *second cluster expansion*.
- **support `X_i`** of a regular activity: under *regular activity* (localization domain).
- **plaquette field**, `χ(U_□)`: Bałaban's **plaquette variable** `U(∂p)`, `(∂U)(p)` (B84a p. 18, (1.2): "then we define a plaquette variable"; B85b p. 77); the same object; v3's *curvature coordinate* (a transported, paired version) has no counterpart. **plaquette energy `w(u)`**: under *distance from the identity*.
- **link** (fine and coarse links): Bałaban's **bond**, **bond variables** `U_b` (B85a p. 18); the same object; v3 mixes "link", "edge", "bond".
- **axial** (axial gauge, axial frames): under *frame*, *tree slice* and *macro-box*.
- **covariant** (gauge-covariant average): "the averaging preserves gauge transformations", `\overline{U^u} = (Ū)^u` (B85a p. 19, (11)); the same property; "covariant" is used in B85b, B85c only for the covariant derivative.
- **fluctuation covariance** on the tree slice (`Γ` of 6:534): under *window* (unit lattice propagator). The headword *common Gaussian* names a different object and was not used.
- **root normalization** (gauge transformations trivial at block roots): the subgroup of B85b (1.14); listed above under names with no dictionary entry.
- **Ward identity / lemma "Removal of the kinetic coefficient"** (chapter 7): under *one-loop drift*; the headword *Ward kernel* (14:820–822) names a different object and was not used.
- **coarse quadratic form `K_c`**: under *kinetic*.
- **level reversal `k = N − m`**, **block length `L`**: under *level*.
- **mask**: not a headword; no counterpart beyond "characteristic function".
