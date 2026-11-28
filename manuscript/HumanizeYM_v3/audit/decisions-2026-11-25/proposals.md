# Proposals for approval: titles, defining sentences, coined terms

Report of a read-only agent, 25 November 2026, as handed back. Issue 1 of the fork, items 37, 39, 43. Nothing in the text was changed.

- **Line numbers** are those of the worktree `/Users/mgubi/ym-terminology`, read on 25 Nov. Files 09, 11 and 11R had uncommitted edits by other agents while I read.
- **Dictionary** means `manuscript/HumanizeYM_v3/audit/terminology.md`. I parsed all 1417 entries with a script and treated an entry as a house word when its *Now* line begins "replaced", "partly replaced" or "not applied" (559 entries).
- **Counts** are case-insensitive regular-expression matches in prose, plural forms included. I took the files in reading order, following the `\input` tree from `monograph.tex`, with comments and `\label`/`\ref` arguments removed.
- **"Inference"** marks my own reading.

---

## List 1 — new titles (item 37)

No title in the book contains mathematics. Titles are noun phrases, for example "Cauchy convergence on common lattice points" (12:296) and "Uniform logarithmic running" (10:275).

### A. The titles you named

| Location | Present title | What the unit states | Proposed | Alternative | Note |
|---|---|---|---|---|---|
| 4:2 (chapter) | Exact blocking and effective densities | One step is defined as an integral operator with a normalized block kernel built from the gauge-covariant averaging operation. The resulting density is represented by a leading path action, a normalization constant, localized terms and large-field activities, and these representations are given norms. | Block kernels and effective densities | The renormalization transformation and the effective density | The house word is "exact". Its entry says "not applied (4:2, 232, …)" and proposes "normalized block-spin kernel"; the meaning is a probability kernel, so the step preserves the partition function. "Effective density" is ordinary RG usage, and "blocking" has no entry. The same word should go from 4:169 ("…and the exact kernel" → "…and the block kernel") and from 4:232 (Definition "[Exact block map]" → "[Block kernel]"; the definition defines `k` and its operator `𝓑`, 4:234–243). |
| 5:2 (chapter) | Gaussian kernels and background fields | Schur-complement formulas for the covariance of the fluctuation field and for the coarse quadratic form. Then uniform estimates over blocking sequences, the linearization `W`, convergence at a fixed scale, the block axial chart, and the construction of the critical configuration. | Covariances and critical configurations | The quadratic approximation and the critical configuration | "Gaussian kernels" has no dictionary entry and is never defined; its only other occurrence is the title at 5:738. The chapter's own first sentences (5:5–7) say what it does: it identifies the covariance and constructs the critical configuration. "Background field" is adopted vocabulary, but the chapter builds one particular background field, the critical configuration. By your criterion this title is not a house-word case; I propose the change for clarity only. |
| 10:2 (chapter) | A common trajectory and fixed-scale stability (short form: Common trajectories and stability) | The schedule, then tuning of the finite histories (Thm 10:232). Prop. 10:428 compares the step maps at different cutoffs. Thm 10:810 "Fixed-scale convergence": at every fixed scale, the inverse couplings, activity arrays and `q_m` converge as `N→∞`. | A common trajectory and convergence at fixed scales; short form "Common trajectories and convergence" | A common trajectory and its limit at each scale | In chapter 10, "stability" occurs only in label names (`ch10:path-stability`, `ch10:stability-assumption`). What is proved is convergence (10:810). In Bałaban "stability bound" is a lower bound on the action (dictionary line 4827), so "stability" here would clash with the literature. "Common trajectory" is kept as you confirmed. |
| 12:131 (Proposition) | Independence of the graph at the ultraviolet cutoff (formerly "Forgetting the terminal graph") | Graph contraction plus fixed-input cutoff continuity imply that the graphs and the normalized coefficients at every fixed scale are Cauchy as `N→∞`. The proof replaces the graph at scale `m+h` by a fixed one, at a cost of `2^{1−h}`. | Cauchy convergence of the graphs at a fixed scale | Forgetting the graph at the ultraviolet cutoff (the reviewer's suggestion) | The present title claims independence, which is not proved. The reviewer's version keeps "forgetting", whose entry says "not applied", and it names the method of proof rather than the result. The proposed form follows 12:296. |
| 11:960 (section) | Finite-dimensional detection before taking limits | At fixed cutoff: bounded equivariant projections `Π_i` whose kernel is the equation space `E_i`, and the bound `|Π_i v| ≤ Z|L_iΠ_i v|` for the separating family `L_i`, obtained by perturbing an injective free matrix. | A finite-dimensional separating bound before taking limits | Uniform separating bounds at finite cutoff | The entry *detection* says the word remains only in this title. Avoid "separation": "separated" means "at distinct points" (1:359). |
| 17c:138 (subsection) | The nonlinear terms need fixed-ratio bounds | The jets of the critical configuration enter below the diagonal and their constants may depend on `L`. Only the coarse coefficient width must be uniform in `L`, and it comes from the gauge-fixed inverse of Ch. 7. Formulas for `z_2`, `z_3` follow by implicit differentiation. | Ratio-dependent bounds for the nonlinear terms | Bounds on the nonlinear terms that may depend on the block ratio | The entry *fixed-ratio constants* says the word remains only here. "Ratio-dependent" is the adopted replacement (17w:24, 72, 76; 17m:429). The present title is a sentence; the book's titles are not. |
| 17t:12 (subsection) | Difference-preserving block averages | Defines the Laurent polynomials `M_a, G_a, N_a, K_0, K_a, K_a^e` in the shifts, acting on the base point before composition with the critical configuration. Lemma 17t:32 proves `K_0∇_a = L^{-1}∇_a^c K_a`, `K_0δ_a = L^{-1}δ_a^c K_a^e`, `K_a − K_0 = δ_a^c K_a^t`. | Base-point averages and fine and coarse differences | Linear averages intertwining fine and coarse differences | "Block average" is replaced throughout the book (*averaging operation*, *linear averaging operator*). These objects are neither of those: they are averages over translates of the base point. `K_0` receives the name "base-point average" only later, at 17c:71. |
| 11:92 (Proposition) | Changing the block history | Replacing the kernels below scale `k` by other normalized positive block kernels and transferring `q_k` through them leaves every coefficient integral unchanged. Field-independent polynomials commute with the transfer. | Changing the block kernels | Independence of the coefficient integrals from the block kernels | The entry *history* says "block history" remains at 11:92. A history also fixes couplings, path pairs and representations (11:18–19); the statement concerns the kernels only. |
| 17m:2 (section) | From the current identity to coefficient estimates with insertions | Integration by parts in the block kernel (`𝒟_Y k`, the density identity), the degree-five coefficient `Σ_k`, the low-moment estimate (Prop. 17m:191), and the rates for the kernel vector. | From the current identity to coefficient estimates | From the current identity to estimates with the differentiated kernel | "With insertions" here is sense 3 of *mark*: the inserted factor is `𝒟_Y k`, not an observable. Dropping the phrase also shortens the title. |
| 18:119 (section) | The replacement estimate with insertions | Replacing a cluster of nearby insertions by one field, with moment bounds for `Z_D` that are uniform in phases. | Replacing a cluster of insertions by one field | The replacement estimate for clusters | Here "insertion" is sense 1, an observable, and "with insertions" is the adopted wording. The real defect is that the title does not say "cluster". Low priority. |
| 18:146 (Proposition) | Replacement with insertions on the same history | The estimate itself: `|b_α| ≤ C r^{|α|−w_0−ε}` and `⟨Ω,(Z_D^*Z_D)^kΩ⟩ ≤ (C r^{D+1−w_0−ε})^{2k}`. | Cluster replacement on the same history | Replacement of a cluster on the same history | "Replacement with insertions" is a conversion headword (formerly *marked replacement*), defined at 18:154–157. The proposal matches 18lp:220 "Lattice cluster replacement". |

There is no title containing "with insertions" in 18-lattice-products.tex or 18-graded-quotient.tex; the two above, both in 18-operator-products.tex, are the only ones.

### B. Further titles found by the scan

I matched every house headword against all 379 title lines. Matches where the title uses a sense the dictionary keeps were dropped: on-shell, path action, sector, window sense 1, scaling-dimension uses, the inherited loop action, the ordinary "selecting a phase", and others.

| Location | Present title | House word (entry, *Now*) | Proposed | Alternative / note |
|---|---|---|---|---|
| 1:171 | Physical scales and lattice symmetries | physical, sense 1 ("remains … at 1:171 (section title)") | Scales in continuum units and lattice symmetries | Continuum scales and lattice symmetries |
| 4:536 | The exact-cover representation and its norms | exact cover (not applied; proposed "compatible family covering the large-field set") | Representations by disjoint large-field families, and their norms | The large-field covering and the norms of a representation |
| 5:453 | The linearization of the critical configuration, the induced map on curvatures, and the curvature defect | curvature defect (not applied; no standard name) | The linearization of the critical configuration and the induced map on curvatures | Also shorter. 5:603 "A positive factorization of the defect" needs a name for `Z_0` first. The dictionary proposes "positive remainder in the recursion for `H^{-1}`"; this is still open. |
| 5:310 | [Uniform curvature metric] | curvature metric / metric (not applied; proposed "quadratic form on two-forms") | [Uniform bounds on the quadratic form on two-forms] | This is longer and would need a book-wide decision on "metric"; it could be left. |
| 5:738 | [Convergence of the selected Gaussian kernels] | selected, sense 2 (proposed: delete, or "fixed") | [Convergence of the Gaussian kernels at a fixed scale] | [Convergence along nested blocking sequences] |
| 6:832 | Simultaneous tail estimates | tail, sense 5 (replaced by *large fluctuation-field event*) | Simultaneous estimates for large fluctuation-field events | Joint bounds for several cutoff remainders |
| 6:1025 | The bounded-jet route for local activities | route, sense 2 ("remains at … 6:1025 (subsection title …)"); jet (not applied, remains at 6:1025) | Derivatives of products of local factors | Local activities with bounded derivatives |
| 6:1165 | Weighted bounds for the primitive local factors | primitive, sense 1 (proposed "elementary") | Weighted bounds for the elementary local factors | — |
| 7:282 | The auxiliary lattice determinant | auxiliary, sense 1 (not applied at 7:282; proposed "regulated") | The regulated lattice determinant | — |
| 10:883 | Identifying the analytic comparison on the selected family | selected, sense 2 | Identifying the analytic comparison on the common trajectory | …on the fixed family |
| 11E:2 | Calibrating the microscopic equations on the same history | calibration (not applied; proposed "normalization"); microscopic (sense 1 replaced by "at the cutoff scale"; "microscopic equations" is not covered by the entry) | Normalizing the equations at the cutoff scale on the same history | — |
| 11:1034 | Collected estimates and local calibration | calibration | Collected estimates and local normalization | — |
| 11:890; 13ba:48 | Backward comparison of a local trial; [The coarse-trial residual on reflected tilings] | trial (not applied; proposed "candidate local observable") | Backward comparison of a candidate local observable | Only if "trial" is replaced book-wide; otherwise keep. |
| 11:1675; 11R:215 | The covariance on a comparison window; [One restarted history on the comparison window] | comparison window (not applied; proposed "interval of scales `[w,k]`") | The covariance on an interval of scales; [A restarted history on an interval of scales] | — |
| 11:2041; 11:2050; 13sb:3 | Finite-arity comparison on a common finite set of scales; [Common finite-arity Gaussian comparison]; Sharp fixed-arity short-distance bounds | arity (not applied; proposed "number of insertions") | Comparison for boundedly many insertions on a finite set of scales; [Joint Gaussian comparison for boundedly many insertions]; Sharp short-distance bounds for a fixed number of insertions | "Common" in 11:2050 is sense 2 (joint). |
| 12:225 | A stopping estimate uniform in the stopping scale | stopping, sense 1 (not applied at 12:225) | An estimate uniform in the scale at which higher source degrees are deleted | Removal of higher source degrees, uniformly in the scale (compare 12:257) |
| 14:229 | [Derivative transport and smooth comparison] | transport, sense 4 (conjugation) | [Conjugated derivatives and smooth comparison] | — |
| 17:385 (paragraph) | The dilation current at short separation. | separation, sense 4 (proposed "distance") | The dilation current at short distance. | — |
| 17c:97 | A homogeneous bound for the quadratic channel | channel, sense 3 (remains at 17c:97; proposed "order-two component") | A homogeneous bound for the order-two component | — |
| 17t:3; 17t:82 | Exact current transfer and the scalar regulator; What scalar mass regularization changes | scalar, sense 9 (proposed "regulator mass for the gauge-parameter component") | Exact current transfer and the regulator mass; What the regulator mass changes | — |
| 17t:175 | The group-coordinate contact identity | contact, sense 3 (Appendix G: the reason for "contact" is not given) | An integration-by-parts identity in group coordinates | Inference from 17t:229–235: the identity relates `½ tr(R D²(DS[Y]))` to `div_Haar Y`. |
| 17t:286 | Cancellation of the action-gradient terms | action-gradient terms (not applied; proposed "the terms `DS[Z]`, `DΓ[Y]`") | Cancellation of the derivatives of the actions | — |
| 19:56 | [Assembly of the common Wilson family] | common family (replaced except at 19:56) | [Assembly for the lattice family] | [Assembly for the family of Wilson measures] |
| MT:91 (paragraph) | A further conclusion in one selected phase. | selected phase (not applied; sense 7 → "the fixed phase `ξ_*`") | A further conclusion in one fixed phase. | — |

I flagged these but made no proposal, because the dictionary proposes no replacement or the sense in the title is unclear:
- "comparison", whose entry says to name the two objects each time: 3:2, 10:310, 10:386, 10:428, 11:2, 11:537/544, 11R:68, 14lc:2, 17:78.
- "centered", sense not determined: 7:572, 7:626, 9s:236, 13sb:102, 13sb:121.
- "signed comparison": 6:215, 6:278.
- 14:312 "Shrinking shells" (shell, sense 2).
- 3:1027 "internal rotation defect": the dictionary has no proposal.

---

## List 2 — defining sentences (item 43)

**1. "free tests"**
- **Occurrences:** 15:275 and 15:278, nowhere else.
- **What it is:** the finitely many one- or two-point free (Maxwell) correlation functionals of the finite free separating family. Each has a label `u` and an optional spectator label `v` at fixed configurations. Scott `part2/H-section.tex:160`: "Each row of trial ℓ consists of a singleton u and optional spectator v … Write 𝒢_I^ℓ for the Maxwell moment of the row labels"; Scott `E-section.tex:490–499` has the lemma "finitely many one- or two-point tests at generic configurations … for which the matrix has rank dim 𝓜_d". In v3 the family is Corollary `ch03:detectors` (3:484–492, two-point functionals `P ↦ S_2^Max(P,P_j;x,y)`), the "free separating family" of 11:1348 (`v_1,…,v_r`), and "the separating family" of 15:256.
- **Proposed sentence:** inside 15:275, after "free tests": ", the free correlations of the separating family, each of one label with at most one further label at fixed points (Corollary~\ref{ch03:detectors})".
- **Symbols checked:** none new. `ch03:detectors` is at 3:485.
- **Uncertain:** the one-point tests, for example `Δ_1 = M(u) − s1` at 15:281, are not in Corollary 3:484, which is two-point; they appear only through Scott's "optional spectator". I did not check whether 11:1348's `v_j` include them.

**2. "compulsory component region"**
- **Occurrences:** none left. 6:1018 now reads "A cutoff remainder assigned within distance $300B$ of its component of the index triple $A$ is zero by definition".
- **Is it self-explanatory?** No, in my reading. In chapter 6, "component" more often means a curvature or averaging component (6:101–109, 453, 491). No sentence says how a cutoff remainder is "assigned" to a component of `A`; 6:86 only says that a sector fixes the assignment of the index triple to connected components of its neighborhoods.
- **Sources:** Lean `YM.ConnectedActivityE6.Coat.mandatory` (as cited in the entry, which I did not reopen) uses `A.dome (300·B)`, the `300B`-neighborhood of the whole selection, not of one component. Martin `gaussian-warnings.tex:206–208` says "Factors inside their compulsory seed region are defined to be zero", and `:225` "radius R_c ≥ R_p + B".
- **Proposed wording** inside 6:1018: "A cutoff remainder at a plaquette, edge or site within distance $300B$ of $A$ is zero by definition: there the cutoff factor itself is kept as a factor of the component." This drops "its component", following Lean. If "its component" is intended, a sentence is needed saying that each remainder is attached to the connected component of `A^{[300B]}` that it meets.
- **Symbols:** `B` (6:38 region), `A` (6:49).
- **Uncertain:** whether "component" means the connected component of `A` or of its neighborhood (inference).

**3. "protected" at 6:694, before its definition at 6:733**
- **What it is:** the definition at 6:733 reads "Call a factor \emph{protected} when it is cut off inside this logarithmic chart." The chart is fixed at 6:704–705 by the radius `d_*`. Martin `compensated-variation.tex:151–158`: "On the protected support all fine reads are consequently fixed".
- **Proposed change** at 6:694: replace "Within a protected logarithmic chart define" by "Within the logarithmic chart of the active bonds, where these logarithms are defined (its radius $d_*$ is fixed below), define". The word then first appears at its definition.
- **Symbols:** `u_e`, `rep V` (6:693), `m_Y`, `g` (earlier in chapter 6); `d_*` is a forward reference within 11 lines.
- **Uncertain:** nothing in the meaning.

**4. "reflected seminorm directions" at 9s:295–296**
- **Present text:** "Original small-field logarithmic coordinates and the normalized affine directions of the activity seminorm, restricted to the microscopic neighborhood and carried to the reflected periodic extension, are bounded by a polynomial in $B$ times $t_m$". The coined phrase is gone, but the sentence is neither self-contained nor matched to the source.
- **Source:** Scott `D-section.tex:425`: "A direction of that definition, restricted to $N_{\bar w}(x)$ and reflected, is bounded by $2t(1+\bar w)^{\varpi_{J_m}}$". These are all directions admitted by the activity seminorm, `|A_e| ≤ t_m(1+dist(e^-,o))^ϖ` (v3 4:574–581), not only affine ones. They are restricted to the spatial cube `N_{w̄}(x)`, whereas in 9s:223, 233, 254 the "microscopic neighborhood" is a neighborhood in field space (dictionary *microscopic*, sense 2).
- **Proposed sentence** for 9s:295–296: "The directions admitted by the activity seminorm \eqref{ch04:local-seminorm}, restricted to the cube about $x$ used for localization and carried to the reflected periodic extension, are bounded by $2t_m$ times a polynomial in $B$, which is $o(h)$."
- **Symbols:** the seminorm is at 4:578; `B`, `t_m`, `h` are in 9s. `N_{w̄}(x)`, `w̄` and `π_v` are defined at 9:318–330, and 9s is read before that point (it is input at 9:307). So the sentence must not use those symbols, or it must cite them forward.
- **Uncertain (inference):** whether the current "normalized affine directions" was intended.

**5. "partition-of-unity weights"**
- **Occurrences:** 6:919–920 ("The local factors of the two partition-of-unity weights") and 6:1015.
- **What it is:** the products `∏_{p∈A_f}ϑ_f(r_p^f)∏_{p∉A_f}(1−ϑ_f(r_p^f))` and the analogous product with `ϑ_n(n_e)` over coarse edges (6:67–76). The entry *allocation*, sense 1, says the same.
- **Proposed sentence** inside 6:919, after "weights": "(the weights given to the sets $A_f$ and $A_n$ by the global partition of unity of the first section, with local factors $\vartheta_f(r_p^f)$ or $1-\vartheta_f(r_p^f)$ and $\vartheta_n(n_e)$ or $1-\vartheta_n(n_e)$)".
- **Symbols:** `ϑ_f`, `ϑ_n` (6:68–70), `r_p^f` (6:46), `n_e` (6:47), `A_f`, `A_n` (6:49–50). The section at 6:19 has no label, so the sentence refers to it in words.
- **Uncertain:** nothing in the meaning.

**6. "kernel history"**
- **Occurrences:** 11:1699 and 17w:71.
- **What it is:** the sequence of quadratic kernels, the metric symbols `H` at the successive scales of the history. 11:1699 reads "All constants are uniform in the kernel history within the already fixed quadratic bounds". The entry *free history* reads it this way; one reviewer reads it as the blocking sequence instead. No source sentence has the phrase.
- **Proposed sentence** inside 11:1699: "uniform in the sequence of quadratic kernels (the symbols $H$ at the successive scales of the history)".
- **Symbols:** `H(p)` at 11:1681.
- **Uncertain:** the two readings differ only in whether the ratios `L_m` also vary. The source does not settle it.

**7. "numerical band margin"**
- **Occurrences:** none. 9:949–951 now cites "the barrier inequalities of Section~\ref{ch10:shooting}, which rest on \eqref{ch10:step-drift} and the condition \eqref{ch10:drift-floor} on the choice of scales".
- **Is it self-explanatory?** Yes. The inner barriers are defined at 10:213.
- **Proposed:** nothing more is needed.

**8. "kernel identities"**
- **Occurrence:** 17:308.
- **What it is:** the bound `\eqref{ch17:kernel-score}` (17m:17) and the density identity `\eqref{ch17:kernel-divergence}` (17m:63), with its integrated forms at 17m:396–398. It is not the block identities of 17t:32 (entry *kernel identities*; Scott uses the same phrase for those). There is no source for the sentence.
- **Proposed change** at 17:308: replace "the kernel identities" by "the bound \eqref{ch17:kernel-score} and the density identity \eqref{ch17:kernel-divergence} for the differentiated block kernel".
- **Symbols:** none.
- **Uncertain:** nothing.

**9. "front-column bounds" / "one-step coefficient bounds in the direction of the transfer"**
- **Occurrence:** 11:1342–1343.
- **What it is:**
  - Martin `actual-rank-purchases.tex:178–188`: `D_k = a_k^d∏_{u<k} C_{u+1}L_u^d`, "where $C_{u+1}\ge1$ is the purchased front-column bound". That is the only occurrence of the phrase in either source.
  - Lean `YM/Source/Insertion.lean`, structure `TransferData.Based` (read): `front : F.coeffSize (T.entries m v).x ≤ (H.levels.params (m+1)).columns * (block m)^d * F.coeffSize (T.entries (m+1) v).x`. The companion field `back` is the bound in the other direction, without the factor `L^d`.
  - `columns` is a field of `YM.RG.Stage` (`YM/RG/History.lean`, with `columns_ge : 1 ≤ columns`).
  - So a "front-column bound" bounds the coefficient one step further along the transfer, at the coarser scale `m`, by `C L_m^d` times the coefficient at `m+1`. `C` is the stage constant `columns`, which is v3's "stage column bound `C_j`" (10:83). Inference: "front" is the direction of the transfer and "column" is the name of the stage constant.
- **Proposed sentence** inside 11:1342: "the one-step bounds $\|x_m\|_1\le C_{J(m+1)}L_m^d\|x_{m+1}\|_1$ for the coefficient of one transferred insertion, with the stage column bound $C_j\ge1$ of Section~\ref{ch10:choices}, applied successively from the reference scale to $k$". If `x_m` is to be avoided, because it is the activity array in ch. 10, use words: "the $\ell^1$ norm of the coefficient at scale $m$ is at most $C_{J(m+1)}L_m^d$ times that at scale $m+1$".
- **Symbols:** `C_j` (10:83–84, which never says what it bounds); `J(m)` (10:807); `L_m` (4:13).
- **Uncertain:** v3 never states the one-step bound, so 10:83 should also say what `C_j` bounds.

**10. `C_st` and the "principal" and "complementary" regular bounds**
- **Occurrence:** 10:622–626.
- **What it is:**
  - Martin `background-test-prices.tex:84–105`: `b(x) = 3tC_st x^{-11/10} + R(x)`, "where … $C_{\rm st}>0$ is the fixed stage conversion constant". `:170–173` sets `C_st = 1/(64(1+C_0))`, "the allocation $c^{\rm reset}$ of (eq:reset-stage-constants)".
  - Martin `physical-reset-reorganization.tex:420–424`: `B^reset = C_reset + C_turn(L_0+L_1)`, `c^reset = 1/(64(1+B^reset))`.
  - Martin `selected-nonlinear-offering.tex:21–29`: "The regular principal bound is at most $E/16$, the complementary regular bound at most $2E/16$ … These are the principal and complementary bounds of the preceding local expansion", with `E = c_st x_0^{-11/10}`. The proof uses only their sum, `3E/16` (`:153–158`).
- **Proposed sentence** inside 10:626: "here $C_{\rm st}=1/(64(1+B))$, with $B$ a constant depending only on the stage, built from $C_{\rm reset},L_0,L_1$ of \eqref{ch09:reset-cost}, and the regular bound of the step is the sum of a bound $\varepsilon C_{\rm st}x^{-11/10}$ and a bound $2\varepsilon C_{\rm st}x^{-11/10}$ for two parts of the regular remainder, of which only the sum is used".
- **Symbols:** `C_reset`, `L_0`, `L_1` (9:597–599).
- **Uncertain:** `C_turn` has no v3 counterpart that I found. What the "principal" and "complementary" parts are is not determined by what I read; the proof needs only the sum, so dropping the split is the safe alternative.

**11. "stationary kernels" and "exact stationary identity"**
- **Occurrences:** 17m:26 ("its stationary kernels") and 17m:163 ("stationary and loop kernels are truncated"). "Exact stationary identity" no longer occurs: 17c:55 now reads "For the exact Taylor-order statement …".
- **What it is:** the kernels of the critical-configuration map, that is, its Taylor coefficients in the coarse field, which are exponentially local. Scott `I-section.tex:358–362`: "The errors are stationary substitution, omitted loop paths, … truncate stationary kernels and loop paths at `C_j(log β̂_k)²`".
- **Proposed sentences:**
  - 17m:26: "…and the kernels of the critical-configuration map (the coefficients of its Taylor expansion in the coarse field)".
  - 17m:163: "Here the kernels of the critical-configuration map and the loop paths are truncated at…". This also lets `E_stat` be read as the error from truncating the first and `E_tail` from truncating the second.
- **Symbols:** "critical-configuration map" (5:972, 1166).
- **Uncertain:** nothing in the meaning.

**12. "large-field event" (17m:330) and "the common large-field estimate" (17m:322)**
- **What they are:** the large-field set proper, not the large fluctuation-field event. Scott `I-section.tex:366`: "For the forced term, Lemma E2.2 leaves $(\epsilon_k^{\rm for})^{1/2}=e^{-M_k^{1/5}/2}$, and Lemma E2.2a retains the original eligibility event." So:
  - the common large-field estimate is the bound on the large-field activities, `𝒦 ≤ exp(−(M^cut)^{1/5})` (4:646–647), with `H = M_k^cut`;
  - the event is (ch04:eligibility), `{Bad_m(U)∩Y_i = I_i^bad} ∩ 𝓔_i^extra` (4:446–448).
  - 17m:127 confirms that "all incoming prescribed large-field sets are retained".
- **Proposed sentences:**
  - 17m:322: "The bound \eqref{ch04:activity-bounds} on the large-field activities retains the square-root bound".
  - 17m:330: "not the eligibility event \eqref{ch04:eligibility} of a large-field activity or its exponential gain".
- **Symbols:** `H` (17m, `= exp((log log β̂_k)²) = M_k^cut`, 4:411).
- **Uncertain:** nothing; this is a source plus v3 reading.

**13. 9s:259, "renormalization terms" (formerly the source's "reset" contribution)**
- **Source:** Martin `pure-action-small-field.tex:103–108` says only "$d_{\rm coarse}(x)$ for the prescribed coarse quantum and reset contribution", with no further definition.
- **Inference from v3 9s:264–268:** the fine and coarse classical terms carry the same `β'`, in `log 𝒵 + β'a_c + d_c`. So `d_c` must contain the coupling shift `(α+Δ)a_c`, which is the coupling constant renormalization, with `α` being the "quantum" part fixed by the matching. The constant per site, the vacuum energy renormalization, can sit in `d_c` or in `Ω`, and it disappears in `W − W(0)` anyway.
- **Answer:** at least the coupling constant renormalization; probably both. The sources do not determine it.
- **Proposed replacement** at 9:258–259: "the prescribed coarse quantum contribution, including the terms of the coupling constant renormalization and of the vacuum energy renormalization (\eqref{ch09:reset})". Here `ch09:reset` is the display at 9:717–721.
- **Uncertain:** as stated.

**14. Terms Appendix G still lists as undetermined**
- **"anchored marked support bound" (18:174):** still in the text and unreferenced. Proposed: "the bound \eqref{ch11:higher-induction} for coefficients with several insertions". The dictionary's identification is S/I.
- **"centered" at 9:294** ("The resulting centered auxiliary bound"): take sense 6 of *centered*. Proposed: "the resulting bound for the auxiliary functional minus its value at the flat configuration". Inference.
- **"group-coordinate contact identity" (17t:175, title):** the reason for "contact" is not given, and Martin's "contact identity" (`thermal-contact-cancellation.tex:126`) is the chapter 7 object. I propose a new title (List 1B) and no defining sentence.
- **"numerical band margin":** gone (item 7).

---

## List 3 — coined short terms (item 39)

Columns: definition (book line and exact quotation) | former house word | count | literature | remark. "No entry" means the dictionary has no *Literature* line; all the entries listed here except those quoted say nothing about the literature.

### A. The terms you listed

| Term | Definition (exact quotation) | Former | Count | Literature | Remark |
|---|---|---|---|---|---|
| blocking sequence | 5:303–305: "A finite \emph{blocking sequence} consists of odd ratios $L_1,\ldots,L_n\ge3$ and smoothing orders $j_0,\ldots,j_n\ge4$, with $j_{h-1}-j_h\in\{0,1\}$." | history, sense 1 | 17 | no entry | First use at 5:10 is a forward reference with a gloss. |
| link multipliers | 5:335: "the multipliers $r_A$ of the averages along the links, the \emph{link multipliers}, compose by" | link factor | 3 | no entry | — |
| periodization criterion | 5:731: "agreement of the matrices of the subsequential limits on a sequence of tori with unbounded side lengths suffices (the \emph{periodization criterion})" | period recovery | 3 | no entry | — |
| block axial chart | 5:930: "The \emph{block axial chart}, the chart of the block axial gauge (the gauge in which the links of the chosen spanning tree of each block equal the identity), is …" | forest; tree slice | 8 | the *tree slice* entry cites Bałaban's "axial gauge in blocks" (B84a p. 19) | "Block axial gauge" (28 occurrences) is first used at 4:296, before its gloss at 5:930. |
| quadratic hypothesis | 5:1057–1058: "Identifying their sum with a chosen metric $H_f$ is an exact coefficient condition on the incoming path action; with $H_f\ge\varepsilon I$ it is called the \emph{quadratic hypothesis} below." | quadratic coefficient condition | 4 | no entry | Uses "metric", a house word not applied. |
| transporter | 4:174: "define the \emph{gauge-transformed parallel transporter}, for short the \emph{transporter}," (followed by the formula) | connector | 16 | the *connector* entry says "no noun"; the object is Bałaban's contour `Γ_{c,x}` with `U(Γ_{c,x})` | — |
| loop condition | 4:65: "The condition that all these distances be strictly below $\delta_{\rm fr}$, the \emph{loop condition}, includes every order $o_0$" | test, sense 3 | 6 | — | — |
| averaging weight | 4:186: "Let the \emph{averaging weight} $w^{\rm av}$ be the $j$-fold convolution of the uniform probability on $\mathbb B_{(L-1)/2}$." | averaging kernel (5:153) | 7 | the *smoothing order* entry: all papers read use the uniform weight `L^{-d}` | First used at 4:16 with a forward reference. |
| dependence set | 4:457–460: "The \emph{dependence set} includes those links as well as the internal links and any links read by other conditions." | full dependence region | 54 | "no separate notion; the localization property (B88b p. 252)" | The definition says what the set includes, not what it is. |
| representation data | 4:550–552: "\emph{Representation data} $\rho$ consist of $\beta$, a real constant $v_{\rm sc}$ per site, the localized terms and the large-field activities, with the fixed action \eqref{ch04:path-action}." | coordinate tuple; density coordinates | 10 | the *density coordinates* entry: Bałaban's "inductive description of the effective actions" (B87 p. 260) | — |
| index triple | 6:49: "A \emph{large-field index triple}, for short an \emph{index triple}, $A=(A_f,A_n,A_c)$ consists of fine plaquettes, coarse edges, and coarse sites." | large-field selection; selected | 18 | "no word; the index sets of the decompositions of unity" (B85e p. 257, B88b) | First used at 6:8, before the definition. |
| deviation | 6:47–49: "$n_e$ is called the \emph{deviation} of the coarse link $V_e$ from its average $Q_e(U)$" | mismatch | 13, including ordinary "large deviations" (6:8) | the *mismatch* entry: "no noun"; Dimock's condition `|Φ_{k+1} − QΦ_k| ≤ p_k` | Clashes with "large deviations" in the probabilistic sense. |
| link support | 6:453: "A component is retained when its \emph{link support}, the fixed set of links from which its expression is built, meets an active edge." | stencil; footprint | 27 | no entry | — |
| background derivative | 7:332: "$b(p;k)$ its first derivative in the background field, for short its first \emph{background derivative}" | background insertion; insertion, sense 2 | 31 | *background insertion* entry: no name; only Bałaban's vacuum polarization tensor for the second derivative | — |
| source degree | 11:133–134: "terms linear in the source variables, that is, of \emph{source degree} one" | terms linear in the sources; higher entries | 57 | — | Defined only through degree one; the general sense (number of source variables) is implicit. |
| cutoff-scale coordinates | 11:884–885: "its inverse coordinates under $\mathsf Z_{N,p,d}$, its \emph{cutoff-scale coordinates}" | inverse terminal coordinates | 6 | no entry | — |
| total large-field activity | 12:26: "A \emph{total large-field activity} is the sum of activities having one particular support and prescribed large-field set" | large-field profile; profile | 8 | no entry | — |
| upper interval | 11:1410: "the \emph{upper interval}, from the comparison scale to the middle scale" | leading, sense 2 | 4 | no entry | The dictionary proposes symbols instead. |
| larger source weight | not \emph-defined. The object is `ω = H^{1/16}` against `ω_- = H^{1/16−U}` (11:1380–1382) | weight restoration (title) | 10 | no entry | First used at 11:29, about 1350 lines before the weights appear; never named at that point. |
| reduced density | 11R:197: "where the \emph{reduced density} $R^0$ is obtained by deleting only the regular additive family $E=\sum_\alpha E_\alpha$" | genuine; neutral | 6 | no entry | — |
| base-point average | 17c:71: "The base-point average $K_0$, the average over translates of the base point" (not \emph) | anchor average | 3 | no entry | `K_0` is introduced unnamed at 17t:22, earlier in reading order. |
| exterior moments | 17m:70: "…zero exterior moments, that is, zero integral against every spectator independent of the varied links." | zero-exterior-moment source (no longer used) | 4 | — | Clashes with exterior forms, and "moment" here is an integral against a function, not a power moment. |
| failed-cutoff factor | 11:1476: "\emph{failed-cutoff factors} (the terms $-(1-\chi)Rz_I$ of the factors $1-(1-\chi)Rz_I$ in the proof below, which vanish where the cutoff $\chi$ equals one)" | cutoff failure, sense 2 | 4 | the *cutoff failure* entry: Bałaban's large fluctuation field characteristic function | Defined by a forward reference to the proof. |
| differentiated kernel | the name is never \emph-defined. The symbol is defined at 17m:58: "$\mathcal D_Y k=(\operatorname{div}_{\rm Haar}Y)k+D_Vk[Y]$"; the subsection title at 17m:10 is "A differentiated block kernel" | score source | 14 | no entry | Add "the \emph{differentiated kernel} $\mathcal D_Yk$" at 17m:58. |
| activity array | 10:421: "Here $x_m$ is the activity array, the family of localized terms and large-field activities" | array; coefficient arrays (10:6) | 11 | — | First used at 10:6, about 415 lines before the gloss. Still uses "activity", whose sense 1 the book otherwise moved to "localized term". |
| local generators | 14:408: "The maps $p_b$ and $Y_d(K)$ are the \emph{local generators} of translations and rotations; they are the local charges of the stress tensor in the main theorem." | local charge | 2 | no entry | Used in the title at 14:312 before the definition. MT:42 and 19:96 still say "local charges", so the object has two names. |
| smoothing order | 4:16: "fix a positive integer \emph{smoothing order} $j$ (the number of convolution factors in the averaging weight $w^{\rm av}$ …)" | averaging order; kernel level | 20 | "name clash; … in Bałaban the order … is the number of composed" steps | — |
| stage | 4:651 ("the \emph{stage} $J_m$ in force at scale $m$ (a stage specifies finitely many derivative orders, support exponents, path widths and coefficient bounds…)") and again 10:25 ("A stage $j\ge1$ specifies …") | regularity class; regularity-stage index | 152, including ordinary uses | "name clash … in Dimock 'stage' means a step" | Defined twice. First used at RG:34, with a gloss. |
| safe chart | 9s:140: "a fixed closed coordinate ball of the chart, the \emph{safe chart}" | (unchanged) | 1 | "no name"; analogues in B85b | Used only at its definition; the name could be dropped. |
| corrected coefficients | 11:2066: "Define the corrected coefficients, the Wick products of the $F_i$ with respect to the free field, by the recursion" | (unchanged) | 7 | — | Used at 11:2027 before the definition. 17t:389 "The corrected coefficient" is a different object, `𝖼(F)`; this is a clash. |
| separating family | 3:482: "A family of correlation functionals, each the correlation with fixed insertions at fixed points, is a \emph{separating family} for a space of fields if no nonzero field of that space lies in the kernel of all of them." | detecting family; detection | 23 | no entry | Standard meaning; adequate. |
| spectators | 3:705: "lists of \emph{spectators}, the remaining insertions $P_1,\ldots,P_n$ of the correlation" | (kept) | 73 | "name clash. In D2 spectator variables are the fields left in holes" | First used at 2e:254, before the definition (round-3 review). |
| restarted history | 11:736: "A useful auxiliary history, the \emph{restarted history}, keeps the inverse coupling constant below a comparison scale while retaining the paths, adjacent quadratic identities, and block geometry." | auxiliary history | 8 | see the *history* entry (name clash with D2's "history") | First used at 11:26, before the definition. |
| comparison window | used without definition. First use 11R:215 (title); 11R:217 "the comparison window with finest scale $k$" | window, sense 2 | 4 | — | Not applied; the dictionary proposes "interval of scales `[w,k]`". Chapters 10 and 17 already say "interval of scales" for the same notion, so the book has two names. |
| common trajectory | used without definition in chapter 10. RG:35: "The resulting common trajectory, the same for all ultraviolet cutoffs, then determines the couplings, activities and observable normalizations"; 10:812 "Use the common trajectory above" | trajectory; selected trajectory; common construction | 15 | the *trajectory* entry: Bałaban's "renormalization group flow" | Chapter 10 itself has no defining sentence; a gloss should go near 10:5 or 10:810. |
| filtration index | 2:96: "it also belongs to a chosen space $V_d$ with $w_i\le d$, whose index $d$ we call the \emph{filtration index}." | normalization index; tag; observable label | 5 | — | The entry *degree* says chapters 12–16 still write "degree" for `d`, so the index has two names. |

### B. Further coined terms

These come from the round-2 list in `audit/chapter-conversion/round2/harmonise.md:164` and from the dictionary's conversion headwords, keeping only technical names. Standard words such as "subsequence" or "side length" are left out. Unless marked otherwise, there is no literature counterpart (no *Literature* line).

| Term | Definition | Former | Count | Remark |
|---|---|---|---|---|
| relaxed regularity condition | 4:488: "We call the condition in \eqref{ch04:relaxed-test} the \emph{relaxed regularity condition} at $x$" | relaxed small-field condition | 12 | — |
| eligible pair | 4:68–69: "call a pair $(z,o)$ eligible when" (formula) | (house) | 2 | — |
| auxiliary index | 4:217: "Collect all choices … in a finite \emph{auxiliary index} $\alpha$" | random index; tag | 26 | — |
| patch of the averaging operation | 4:173: "the \emph{patch of the averaging operation} at $y$" | block-average patch | 5 | Literature: "no name; … locality of the average (B85a p. 24)". |
| averaging component | 6:491: "the retained components containing the averaging operation, for short \emph{averaging components}" | — | 6 | — |
| sector | 6:85: "A \emph{sector} is a term of this decomposition with fixed discrete data" | allocation sector | 29 | First used at 6:15, before the definition. |
| large fluctuation-field event | apposition at 6:9: "Large fluctuation-field events, the failures of smooth local cutoffs in the remaining coordinates" | cutoff failure; tail events | 17 | Literature: Bałaban's large fluctuation field characteristic function (B88b). 17m:330 uses "large-field event" for a different object (List 2, item 12). |
| event label | first use 6:835, no definition sentence ("An event label specifies one particular cutoff and its base point") | cutoff-failure label | 11 | — |
| stage pairs | 10:30: "\emph{stage pairs} (the stages of the two scales of one step)" | adjacent pair | 4 | — |
| stage plateau | 10:123: "a \emph{stage plateau}, a maximal interval of scales on which the stage is constant" | — | 3 | — |
| schedule | 10:121: "the \emph{schedule}: the stage and the block ratio at every scale" | (kept) | 25 | RG:32 says "scale schedule". |
| coarse endpoint | 10:153: "a prescribed value $\bar\beta>0$ of the coupling at unit scale, the \emph{coarse endpoint}" | coarse target | 10 | First used at 1:465, before the definition. |
| finite parameter evaluation | 10:457: gloss "(finite linear combinations of values along a real line)" | — | 4 | — |
| width margin | not \emph-defined; first use 10:375 "the strict width margin" | width reserve | 7 | — |
| Taylor localization / one-step localization map | 11:372–373: "Taylor localization, the extraction of the local polynomial part by Taylor expansion … gives the one-step localization map $T$" | extraction | 4 / 1 | — |
| common localization map | title 11:1141; no definition sentence found; first use 11:28 | extraction | 12 | First used 1100 lines before its construction. |
| normalized local insertion | 11:1051: "The normalized local insertion is therefore" (formula) | (kept) | 23 | First used at 11:353, before the definition. |
| comparison scale | no definition; first use 11:734 (title) | comparison depth; endpoint, sense 3 | 29 | Possibly self-explanatory; given only as "the comparison scale $k$". |
| auxiliary reference parameter | 11R:25 (paragraph title), then "There is a unique sufficiently large $r(x)$ …" | recording scale | 5 | — |
| chessboard bound | no definition sentence; first use 11:867 | root estimate | 14 | — |
| large-field correction | 9:368: "$L_x$ is a \emph{large-field correction}, a term of the exponent supported where …" | logarithmic correction | 8 | First used at 9f:871, before the definition (9f is input at 9:161). |
| exact regrouping | Proposition title 9:651 | fusion | 7 | Literature: "no single word … Mayer expansion … polymer expansion (B89b)". First used at 9f:918, before the proposition. |
| critical-configuration map | no definition sentence; first use 5:972; Proposition title 5:1166 | branch; stationary graph; stationary substitution | 21 | — |
| jet functional | 3:751: "every \emph{jet functional}, that is, every linear functional on the jets of the curvature at $x_0$" | probe | 9 | — |
| current defect | 17:194: "define its \emph{current defect}, the defect of the lattice Ward identity" | (kept) | 6 | — |
| ratio-dependent / ratio-independent constants | no definition; first use 17w:24 | post-ratio / pre-ratio constants | 4 / 3 | 17c:138 still has "fixed-ratio". |
| compression algebra | Proposition title 15:90 | ground algebra | 4 | — |
| identity field | 2:80 (\emph) | unit | 34 | First used at MT:27. |
| alternative branch | no definition; first use 4:211 | fallback | 4 | — |
| per-site normalization exponent | no definition; first use 10:165 | vacuum bound | 4 | — |
| reflected periodic extension | no definition; first use 9s:169, before the map at 9:322–330 | folded | 4 | The round-3 review noted the same. |
| comparison identity for the mean | no definition; 6:924 | local transfer identity | 2 | — |
| growth factor | no definition; 11:1365 | amplification | 4 | — |
| kernel vector | title 17m:375 | equation direction | 2 | — |
| kernel history | — | free history | 2 | List 2, item 6. |
| free test | — | reference rows | 2 | List 2, item 1. |
| factorization hypothesis | no definition; first use 6:136 | aligned | 4 | — |
| flat map for the penalty term / untruncated flat maps | 6:125–126 / 6:948 | penalty map / full maps | 3 / 2 | — |
| hypothesis on tilted Gaussians | 9:115 | quadratic-tilt criterion | 1 | — |
| mesh estimate | 7:461 | recording estimate | 2 | — |
| coincident-coordinate strip | first use 14:179 | coordinate-equality strips | 6 | — |
| inclusions of the field spaces | 18gq:8 | corrected inclusions | 2 | — |
| subpower cutoff-scale coordinates | 11:1075 | subpower inverse terminal coordinates | 3 | — |
| weighted Euler operator | 3:689 | weight operator | 1 | — |
| convergence of the action data | 12:31 | background convergence | 2 | — |
| intermediate representation | 9:394 | preparatory output | 1 | — |
| localized approximate inverse | title 6:520 | local inverse columns | 2 | Literature: Bałaban's localized inverses (see *window*). |
| six local terms | 6:190 | six anchored quantities | 1 | — |
| number of transfers | 17m:361 | current depth | 1 | — |
| pair of positive weight | 18:352 | selected pair | 2 | — |
| distinguished identity field | 13:58 | distinguished unit | 1 | — |
| graph of the backward comparison | 17m:444 | descending graph | 1 | — |
| admissible conditional integral (with insertions / with the differentiated kernel inserted) | 17m:72 | admissible marked conditional integral | 1 | — |
| large-field part | first use 9:639 | complementary profile | 20 | — |
| margin in the support exponent | first use 8:150 | support-weight reserve | 20 | — |
| replacement with insertions | 18:154–157 (formula for `Z_D`) | marked replacement | — | List 1A. |

For the 1:1 conversion headwords with ordinary-English successors (for example "is at most" from "fits", "subsequence" from "refinement"), I judged them not coined and left them out.

**Same object, two names:**
- local generators / local charges (14:408 against MT:42, 19:96);
- filtration index / degree;
- comparison window / interval of scales;
- the coefficient `α_{N,m}`: "determinant coefficient fixed by the matching" against "explicit coupling increment" (the harmonise note says so; I counted 0 occurrences of the latter, so it may already be gone).

**Defined after first use:** index triple, averaging weight (forward reference), block axial gauge, activity array, larger source weight (never defined by name), corrected coefficients, restarted history, spectators, sector, coarse endpoint, local generators, large-field correction, exact regrouping, common localization map, normalized local insertion, reflected periodic extension.

**Clashes with standard or literature meanings:** stage (Dimock), spectators (Dimock), smoothing order (Bałaban's "order"), history (D2), deviation (large deviations), exterior moments (exterior forms; also not power moments), corrected coefficient (two objects).

---

## What I did not read or check

- **Lean:** I read only `Lean/YM/Source/Insertion.lean` lines 75–105 and `Lean/YM/RG/History.lean` lines 45–65. All other Lean citations come from the dictionary.
- **Literature:** I did not open the Bałaban or Dimock papers; the literature columns repeat the dictionary's *Literature* lines.
- **Sources read myself:**
  - Scott: `D-section.tex:410–427`, `I-section.tex:366–373`.
  - Martin: `actual-rank-purchases.tex:150–190`, `background-test-prices.tex:60–180`, `selected-nonlinear-offering.tex:1–40` and `148–160`, `physical-reset-reorganization.tex:415–430`, `pure-action-small-field.tex:1–175`, `thermal-contact-cancellation.tex:1–20` and `120–135`, `leaf-expansion.tex:1–12` and `176–200`.
  - Everything else under *Source* is taken from the dictionary, including the Martin `gaussian-warnings` passages for "compulsory".
- **Not resolved:**
  - what "principal" and "complementary" regular bounds are (List 2, item 10);
  - whether `d_c` contains the vacuum constant (item 13);
  - whether the one-point free tests belong to Corollary 3:484 (item 1);
  - the senses of "centered" in the titles at 7:572, 7:626, 9s:236 and 13sb:102/121;
  - the second "kernel history" reading.
- **Counts:** these are regular-expression counts. Some include unrelated ordinary uses (stage, deviation, window, history, transfer), and I did not hand-check them.
- **Definition search:** I looked for definitions as `\emph{…}` occurrences plus the contexts I opened. Where I say "no definition sentence found", a definition phrased without `\emph` might exist elsewhere; I checked only the first-use context.
- **Not done:** I did not build LaTeX or run `check_blueprint.py`, since nothing was edited. I did not read `08-polymers.tex` or the reading guide beyond the matched lines.
