# Sentence repairs, formulas and restored sentences

Applied by one agent on 25 November 2026 (issue 1 of the fork, items 11, 12, 34), before review. Every item of Appendix D of `terminology.md` not plainly "applied" was compared with the suggestion recorded at commit `4f462ac5` and with the source passage itself. All edits are within lines. "Scott" = `manuscript/HumanizeYM_v2/part2/`, "Martin" = `manuscript/existence/`.

## Sources read, by line

6:1018 Martin `gaussian-warnings.tex:195–285`, `selected-centered-service.tex:834–844`; 6:1544, 9:283–284 Martin `gaussian-reassembly.tex:14–17`; 6:846 Martin `gaussian-warnings.tex:199–208`; 6:459–460 Scott `B-section.tex:1050`; 7:195 Martin `stationary-output-construction.tex:190–202`; 7:427 Scott `C-section.tex:259, 348`; 7:599 Martin `weighted-frame-penalty.tex:165–172, 238–246`; 7:628 Martin `weighted-frame-penalty.tex:78–100`; 9:77 Martin `gaussian-reassembly.tex:50–63`; 9:147 Scott `D-section.tex:212`; 9:949–950 Scott `D-section.tex:847`; 9s:258–259 Martin `pure-action-small-field.tex:103–124`; 9s:295–296 Scott `D-section.tex:425`; 10:98–99 Scott `E-bounded-real.tex:10–17`; 10:169–172 Scott `E-section.tex:42, 362`; 10:381–382 Martin `path-attachment-producer.tex:840–865`; 10:626 Martin `background-test-prices.tex:80–100`; 11:1237 Martin `actual-rank-purchases.tex:1015–1032`; 11:1285–1286 Martin `actual-rank-purchases.tex:544–556`; 11:1343 Martin `actual-rank-purchases.tex:165–188`; 11:1595–1597 Martin `actual-local-compiler-handoff.tex:12–28, 338–346`; 11:1934 v3 11R:14, 114; 12:131 Martin `fixed-rung-convergence.tex:88–100`; 14:186 Scott `G-section.tex:240`; 14:903–904 Martin `physical-ward-analytic-continuation.tex:1–14`; 17:138–140 Scott `I-section.tex:109`; 17w:31–32 Scott `I-section.tex:91`; 17w:87 v3 11:2063–2098 (no source sentence); 17w:122 Scott `I-section.tex:111`; 17m:383–386 Scott `I-section.tex:133`; 18:404 Scott `J-section.tex:589–626`; 18lp:27, 36 Scott `J-section.tex:45, 61`.

## Inferred by the agent, not read in a source

The clause "along the tuned histories … this follows from the condition (ch10:drift-floor)" at 9:950 (the non-assertion itself is the source's); "renormalization terms" for the source's "reset" at 9s:259; "around the patches" at 7:599; the patch `Ly + 𝔹_R`, `R = (j+3)L`, at 7:628; the identification at 17w:87; the gloss of the contact projection at 18:404 (condensed from the source's definitions D36–D37). The new title at 12:131 is the dictionary's proposal; the source has the old title.

## Skipped

- 6:21: the stage is defined at 4:651 and 10:25.
- 10:921: the representative is not named; whether the source's "block mean" is `M` (giving `W_s`) or the averaging operation (giving `W_a`) was not determined.
- 11:2306: applied already; stating the hypotheses of 11:919–924 would need new lines.
- 13:395–396, 13ba:30: "selected" is right (13:172; the source has the same words).
- 17:307–309: no source sentence.
- 17c:66: the file was being rewritten.
- Item 12, "word": defined at first use, 3:234; restated at 13:282 and 16:291. Nothing added.
- Item 12, `W_F`: defined at 5:1139–1149; 6:953 has the source's defining sentence. `𝒰_F` no longer occurs. Nothing added.

## Formulas not added

- 9s:258–259, a formula for `d_c`: neither the source nor v3 displays one.
- 11:1343, `D_k = a_k^d ∏ C_{u+1} L_u^d`: the constants `C_{u+1}` are not defined in chapter 11.
- 9:147, the bound `C_{j,η} e^{η s_M}`: `C_{j,η}` and `η` are not defined in chapter 9.

## Not checked by the agent

Rendered pages; the Lean source. Checks run: per-file line counts equal; `python3 tools/check_draft.py` passes; full build 298 pages, no errors, no undefined references, no overfull boxes.

## Changed lines

**6:460**

- was: `path. Its coarse radius is at most $R_*+5+r_{\rm pred}\le B/50$ for large`
- now: `path; here $r_{\rm pred}$ is the largest coarse distance at which the averaging operation reads a link. Its coarse radius is at most $R_*+5+r_{\rm pred}\le B/50$ for large`

**6:846**

- was: `derivative of the averaging operation, and event indicators. A covariance estimate by itself cannot`
- now: `derivative of the averaging operation, and the cutoff factors. A covariance estimate by itself cannot`

**6:1018**

- was: `also one. A cutoff remainder assigned within the compulsory component region is`
- now: `also one. A cutoff remainder assigned within distance $300B$ of its component of the index triple $A$ is`

**6:1544**

- was: `are clean. It does not compare a seeded sector to an unseeded law,`
- now: `are clean. It does not compare the Gaussian law of a sector whose index triple has nonempty $A_f$ or $A_n$ with the law of the sector with $A_f=A_n=\emptyset$,`

**7:195**

- was: `exchange symmetry and signed-coordinate symmetry, has`
- now: `exchange symmetry $f_{ab}^{uv}(p)=f_{ba}^{vu}(-p)$ and signed-coordinate symmetry, has`

**7:427**

- was: `The four constant maps in the vector regulator that take a one-form to its components do not`
- now: `The four constant maps $J_a$ in the vector regulator $M_\mu=\sum_aJ_a^*m_\mu J_a$, where $J_a$ takes a one-form to its component in direction $a$, do not`

**7:599**

- was: `padded patch of the averaging operation only changes constants: its number of residue`
- now: `padded box of radius $(j+5)L$ around the patches of the averaging operation only changes constants: its number of residue`

**7:628**

- was: `Use normalized probability measure on the padded block and the three`
- now: `Use the uniform probability measure on the patch $Ly+\mathbb B_R$, $R=(j+3)L$, of the averaging operation and the three`

**9:77**

- was: `logarithm, missing-coordinate factor and residual of the mean equation`
- now: `logarithm, missing-coordinate factor $\mathfrak m^{-(N_{\rm free}-n_{\rm act})}$ and residual of the mean equation`

**9:147**

- was: `by $\mathfrak b^{1/16}$. Read-count polynomials are absorbed by`
- now: `by $\mathfrak b^{1/16}$. The polynomial factors $(1+s_M)^{d_j}$ in the number of blocks read are absorbed by`

**9:283**

- was: `exponent. Thus no comparison between unrelated event indicators or a seeded and`
- now: `exponent. Thus no comparison has been made between unrelated event indicators, or between the Gaussian law for an index triple with nonempty $A_f$ or $A_n$ and`

**9:284**

- was: `an unseeded law has been made. The interpolation estimates`
- now: `the law for $A_f=A_n=\emptyset$. The interpolation estimates`

**9:949**

- was: `cutoff conditions. That the output inverse coupling lies in its band additionally`
- now: `cutoff conditions. The theorem does not assert that the output inverse coupling lies in its band`

**9:950**

- was: `requires the numerical band margin in the choice of`
- now: `$[\widehat\beta_m/2,2\widehat\beta_m]$; along the tuned histories of Section~\ref{ch10:shooting} this follows from the condition \eqref{ch10:drift-floor} on the choice of`

**9s:258**

- was: `Let $a_c$ be the prescribed coarse classical action and $d_c$ its`
- now: `Let $a_c$ be the coarse classical action and $d_c$ the prescribed coarse`

**9s:259**

- was: `quantum contribution. Define`
- now: `quantum contribution, including the renormalization terms. Define`

**9s:295**

- was: `Original small-field logarithmic coordinates and the reflected`
- now: `Original small-field logarithmic coordinates and the normalized affine directions of the activity`

**9s:296**

- was: `seminorm directions are bounded by a polynomial in $B$ times`
- now: `seminorm, restricted to the microscopic neighborhood and carried to the reflected periodic extension, are bounded by a polynomial in $B$ times`

**10:98**

- was: `the ratio. On that chart the indicator of the relaxed regularity condition is one. Its`
- now: `the ratio. On that chart the indicator of the relaxed regularity condition is one. The`

**10:99**

- was: `complementary global value is controlled by the same later`
- now: `value of the trial outside that chart is controlled by the same later`

**10:169**

- was: `$C_j(1+\log\widehat\beta_{m+1})$ using the Haar-ball normalization`
- now: `$C_j(1+\log\widehat\beta_{m+1})$ by the lower bound on the partition function from the Haar measure of a small ball`

**10:170**

- was: `argument. At a fixed stage the numerator is a fixed polynomial in`
- now: `about the identity on every link, as in \eqref{ch11:replicated-bound}. At a fixed stage the numerator is a fixed polynomial in`

**10:171**

- was: `$\log(2+\tau_m)$, so this is a finite lower bound on the starting scale. It will keep`
- now: `$\log(2+\tau_m)$, so this is a finite lower bound on the starting scale. It will make`

**10:172**

- was: `replication costs subpower at a nearby sparse stopping scale. For the`
- now: `the per-cell normalization cost $o(\tau_k)$ at the stopping scale $k=k(m)$ of Section~\ref{ch13:sharp-section}. For the`

**10:381**

- was: `prove convergence at width $w$. For a Hilbert encoding instead, one`
- now: `prove convergence at width $w$. If the coefficients are instead bounded in the weighted $\ell^2$ norm $(\sum_\gamma e^{2\delta\ell(\gamma)}|c_N(\gamma)|^2)^{1/2}$ with $\delta>w$, one`

**10:382**

- was: `must verify summability of the encoding weights on that index set;`
- now: `must verify $\sum_\gamma e^{-2(\delta-w)\ell(\gamma)}<\infty$ on that index set;`

**10:626**

- was: `where the fixed fraction $\varepsilon$ can be made as`
- now: `where the fixed fraction $\varepsilon\le1/16$ of $C_{\rm st}x^{-11/10}$ allotted to the principal regular bound (and $2\varepsilon$ to the complementary one) can be made as`

**11:1237**

- was: `For normalized target columns with`
- now: `For the solutions $u=u_{j,N,p}$ of the lift equations \eqref{ch11:simultaneous-detector-lifts} below, which satisfy`

**11:1285**

- was: `Let $\mathcal E$ denote exposure in the fixed radial polynomial`
- now: `Let $\mathcal E$ send $v\in V_d$ to its polynomial, of weighted degree at most $d$, in the fixed radial jet variables.`

**11:1286**

- was: `basis, and choose $c_d$ with`
- now: `It is injective between finite-dimensional spaces, so one may choose $c_d\ge1$ with`

**11:1343**

- was: `At a fixed comparison scale the front-column bounds give`
- now: `At a fixed comparison scale $k$ the one-step coefficient bounds in the direction of the transfer, applied successively from the reference scale to $k$, give`

**11:1595**

- was: `Split the positive decay of the prescribed large-field set in`
- now: `Split the decay exponent $Kh(x)^2r$ of a selected component with $r$ selected cutoff conditions, given by`

**11:1596**

- was: `Chapter~\ref{ch06:large-fields} into fractions kept aside and choose`
- now: `Chapter~\ref{ch06:large-fields} (Section~\ref{ch11:restart-construction}), into fractions kept aside and choose`

**11:1597**

- was: `the reported bound $G(x)$ so that multiplication by $G(x)^{-2}$`
- now: `the reported bound $G(x)=\exp\{-a_*h(x)^2\}$ with $4a_*\le K/2$ so that multiplication by $G(x)^{-2}$`

**11:1934**

- was: `most $e^{-2u}$, with $u=a_*\,\mathrm{hot}(s)^2$.`
- now: `most $e^{-2u}$, with $u=a_*h(s)^2$.`

**12:131**

- was: `\begin{proposition}[Forgetting the terminal graph]`
- now: `\begin{proposition}[Independence of the graph at the ultraviolet cutoff]`

**14:186**

- was: `For example the construction below uses`
- now: `For example the construction below, with $M_k=H_k=\exp((\log\log\widehat\beta_k)^2)$, uses`

**14:903**

- was: `coordinate. This uses no integration of the infinitesimal rotation operators into a`
- now: `coordinate. This uses only exponentials of the individual infinitesimal rotation operators on the finite-dimensional field spaces, not an action of the full`

**17m:383**

- was: `Consequently, in the notation of the stability argument,`
- now: `Consequently, in the notation of the stability argument, with $v=(0,0,1)$ the kernel vector of the free quotient $s$,`

**17m:385**

- was: `j_i\to-v_{\rm eom},\quad |\rho(j_i)|\le CH_i^{-1/4},\qquad`
- now: `j_i\to-v,\quad |\rho(j_i)|\le CH_i^{-1/4},\qquad`

**17m:386**

- was: `v_i^{\rm eq}=\beta_i^{-1}\Sigma_{k_i}-j_i\to v_{\rm eom}.`
- now: `v_i^{\rm eq}=\beta_i^{-1}\Sigma_{k_i}-j_i\to v.`

**17:138**

- was: `scale in Figure~\ref{ch17:fig-radius-windows}. The first crossing places a`
- now: `scale in Figure~\ref{ch17:fig-radius-windows}. For a prescribed small radius, the first $n$ with $r(n,\alpha_0)$ at most that radius, together with continuity of $r(n,u)$ in $u$, places`

**17:139**

- was: `prescribed radius in one of them. Take a diagonal subsequence over finite degree, arity,`
- now: `that radius in one of them. Take a diagonal subsequence over finite degree, arity,`

**17:140**

- was: `compact-set and derivative requests, requiring`
- now: `compact-set and derivative requests, which gives $n_i$, $k_i=k(n_i)$ and the maps $U_{i,d}$, requiring`

**17w:31**

- was: `numbers, stop backwards from $n$ at the first crossing of`
- now: `numbers, stop backwards from $n$ at the first scale $n'<n$ with $\log(a_{n'}/a_n)\ge$`

**17w:32**

- was: `$(b+2)\log H_n$, and then at the first crossing of another`
- now: `$(b+2)\log H_n$, and then at the first scale $n''<n'$ with $\log(a_{n''}/a_{n'})\ge$`

**17w:87**

- was: `and corrected free-subset polynomial are common to all subsets;`
- now: `and the polynomial $\sum_IG_Iz_I$ of free moments are common to all subsets;`

**17w:122**

- was: `fixed derivatives and shell fluxes with these same comparison isomorphisms.`
- now: `fixed derivatives and shell fluxes with the same diagonal subsequence and the same comparison isomorphisms $U_{i,d}$.`

**18lp:27**

- was: `$x_l$ and a remainder of norm $r_l$ whose extracted coefficient vanishes. Its dimensionless`
- now: `$x_l$ and a remainder of norm at most $r_l$ whose extracted coefficient vanishes. Its dimensionless`

**18lp:36**

- was: `cutoff scale. In detail, a remainder of size $q$ with vanishing extracted coefficient has`
- now: `cutoff scale. In detail, a remainder of norm at most $q$ with vanishing extracted coefficient has`

**18:404**

- was: `If a contact projection extracts a degree-$q$ field from that cluster,`
- now: `If the contact projection of degree $q$, which reads a cluster of fields near a point through its correlations with finitely many fixed separated probe words, extracts a degree-$q$ field from that cluster,`
