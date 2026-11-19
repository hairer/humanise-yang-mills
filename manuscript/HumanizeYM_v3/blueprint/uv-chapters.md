# Ultraviolet chapters: author instructions

Status: source-grounded design, not a verification certificate. Final UV Chapters 4–12 have a combined budget of **220 pages**: 18 + 26 + 24 + 26 + 18 + 30 + 24 + 30 + 24. The stable legacy IDs below are retained for dependencies: U1 is now part of foundation Chapter 2; U2–U5 are Chapters 4–7; U6 is split into Chapters 8–9; U7–U9 are Chapters 10–12. Free Maxwell comparison C1 is Chapter 3. All paths below are relative to the project root. Source labels are authoritative locators; line numbers refer to the supplied snapshot.

## Instructions common to every UV author

Read this file's conventions, your chapter specification, its stated inputs, and only the indicated source passages first. Read `uv-audit.md` before turning any conditional estimate into a theorem. The notation glossary and master blueprint prevail over provisional symbols below. Do not inherit a source's assertion that a previous package “supplies” a hypothesis without checking that the same coupling, path, masks, Gaussian law, normalization, support norm, and finite family occur on both sides.

Use nine independent writing units, but do not pretend their mathematical dependencies are independent. In particular, first prove **conditional one-step analytic estimates for an arbitrary admissible adjacent pair**; choose a simultaneous infinite schedule only once the finite-stage requirements have been collected. Existence of a schedule never proves an analytic estimate. Similarly, retain finite-cutoff Maxwell comparison in U8, and move limit rank and stress assertions of Outline III.11 to the continuum chapters.

The local section chapter U1 and free Maxwell chapter C1 may be written early. U2–U6 produce the unmarked transformation; U7 produces a common trajectory. U8 uses U1–U7 and C1. U9 uses U8. Individual subordinate propositions may be stated conditionally before their hypotheses are discharged, with that conditional status explicit in their titles. No global existence theorem may be stated as proved until those hypotheses have been discharged on the chosen family.

Cite existing arguments rather than reprove them. A citation to a method is not a theorem with the exact required hypotheses. Write the short normalization/admissibility check when applying a known theorem. New work here is often the uniformity, large-field complement, and compatibility with the chosen density, not the elementary analytic argument. The author's working notes should distinguish a checked application, a proposed adaptation, and an unverified source claim.

At every first appearance define a technical symbol in prose and an equation. When an unusual symbol has not appeared for roughly three pages, add a one-clause reminder or a definition reference. Avoid “paid,” “funded,” “receipt,” “coin,” “readout,” “healthy,” “warning,” “compiler,” “port,” “course,” and “horizon” as monograph terminology. Their source meanings are: quantified bound, admissibility estimate, coefficient vector, Taylor projection, small-field support, Gaussian tail event, connected expansion, input/output condition, auxiliary coupling sequence, and collection of Gaussian kernels. Some substitutions depend on context; do not perform a global search-and-replace.

## Shared conventions for these chapters

- Fix the compact matrix group $G\subset U(n_G)$, probability Haar measure, and Lie algebra metric $\langle X,Y\rangle=-n_G^{-1}\operatorname{Re}\operatorname{tr}(XY)$. The adjoint Casimir in this metric is $C_{\mathfrak g}$; $\kappa_G=11C_{\mathfrak g}/(24\pi^2)$. Reserve (b>0) for the block-kernel penalty, never for a norm record.
- The physical torus side is $R_p$, replacing Scott/Trish's $L_p$. Set $D_0=1$, $D_{m+1}=L_mD_m$, $a_m=D_m^{-1}$, $\tau_m=\log D_m$. $L_m$ is an odd **level-dependent** block ratio. The original files usually write $\ell_m$ for this ratio. Blocking is $m+1\to m$; $N$ is the ultraviolet cutoff. The lattice has $R_pD_m$ sites in each direction. Do not assume constant block ratios.
- $J_m$ is the nondecreasing stage index, tending to infinity, with steps at most one. The stage and level indices must never be silently interchanged.
- $\widehat\beta_m=\bar\beta+\kappa_G\tau_m$ is the reference inverse coupling. $\beta_{N,p,m}$ is the actual one. Their band is $\mathfrak B_m=[\widehat\beta_m/2,2\widehat\beta_m]$. $\bar\beta$ is the common level-zero value.
- For the Scott formulation, $M_m^{\rm cut}=\exp((\log\log\widehat\beta_m)^2)$, $t_m=\widehat\beta_m^{-1/2}M_m^{\rm cut}$, $B_m=\lceil(\log\widehat\beta_m)^2\rceil$, $\epsilon_m^{\rm reg}=\widehat\beta_m^{-11/10}$, $\epsilon_m^{\rm lf}=\exp(-(M_m^{\rm cut})^{1/5})$. These are definitions of that formulation, not automatically the numerical functions in every Martin argument. A translation check is required before importing estimates involving `hot`, `fineCut`, or `fieldCut` from Martin.
- $V_d$ is the space of invariant radial-gauge jet polynomials of scaling dimension at most $d$. A nested real basis $p_i$ has weight $w_i$ and factor number $f_i$. The diagonal map $S_t$ multiplies coordinate $i$ by $t^{f_i}$; it is distinct from spatial scaling, which multiplies a weight-$w$ polynomial by $h^w$. $c^\circ=c-c_0e_0$.
- $\Sigma_d$ denotes the fixed finite lattice stencil; $P_d^{\rm loc}[c]$ is its local polynomial representative. (r(d)) is the reference level. $\mathsf Z_{N,p,d}$ is the coefficient transfer map to that level, not the partition function $Z_{N,p}$.
- $E_i$ are small-field local activities anchored at $o_i\in X_i$; $K_i$ are large-field polymer activities on $Y_i$ with nonempty flagged inventory $I_i$. Activities need not be positive. Their sum gives the actual positive density on a constructed trajectory.
- $\mathcal B_m^\beta$ is the integral block map. $H_{N,p,m}^{(d)}(c)$ is an inserted, unnormalized density, and $O_{N,p}(v,x)$ is the normalized physical insertion. Do not divide by $K_i$ when defining marked activities; they can vanish.
- All geometric distances in lattice estimates are periodic maximum-coordinate distances, unless explicitly converted to Euclidean distance. Physical distance includes a factor $a_m$.

## Foundation Chapter 2 (U1): local gauge-invariant observables — integrated with foundations

**Purpose and input.** Starting only from the lattice/Wilson chapter and elementary differential geometry of $G$, define the finite-dimensional label spaces and realize them by finite-stencil observables. The construction does not presuppose continuum fields or their null spaces.

**Sections, in order.** (1) Radial gauge and curvature jets, including the relation between homogeneous potential and curvature jets. (2) Engineering weight, polynomial degree/factor number, invariant spaces $V_d$, conjugation and orthogonal action. (3) Holonomies of truncated potentials and the scaled Taylor map. (4) A finite plaquette sampler, equivariant polynomial inverse to the necessary jet order, and finite stencils. (5) Small-field derivative bounds. (6) Equation observables as a separate exact integration-by-parts construction; distinguish the free equation ideal from the as-yet-unconstructed continuum null space. End with the curvature-square example.

**Required output.** For every $d$, construct a real, symmetry-equivariant linear map $P_d^{\rm loc}:V_d\to C(G^{E(\Sigma_d)})$, gauge invariant and with $P_d^{\rm loc}[1]=1$, whose evaluation on scaled radial holonomies has the prescribed Taylor polynomial through order $d$. Each pure-factor column admits a local derivative bound $C_{d,k,P}t^{f_i}$, uniformly over periods admitting the stencil, for each fixed derivative order and spatial weight. State separately the dressed equation-section assertion: for each fixed degree there is an equivariant invertible change of label coordinates such that an equation insertion has zero Wilson expectation against every bounded measurable spectator depending only on links outside a fixed neighborhood, for every sufficiently large lattice period and every nonzero inverse coupling. Its application to limiting null spaces is deferred.

**Source packet.** Scott Outline II.1, propositions II.1.1–II.1.5, and III.16.8–III.16.10 for the algebra. Scott `part2/A-section.tex`: `sec:A-labels` (9), `lem:A1` (85), `lem:A-bounds` (142), `lem:A-R4` (181), `sec:A-example` (255). Martin `existence/local-sections.tex`, `sec:local-sections`, especially finite sampler (8), polynomial recovery (71), averaging (117), bounds (157); `local-splitting.tex` and `actual-equation-kernel-relay.tex` are follow-up sources for the dressed equation construction. Trish's A file is nearly identical, so compare only changed statements.

**Checks and compression.** Cite matrix ODE existence, finite-group/Reynolds averaging and finite-dimensional inverse-function arguments; give the actual sampler and why its differential is injective. Do not identify “on-shell polynomial” with a physical null field yet. The stencil is finite but need not be explicit in coordinates. Export $V_d,\Sigma_d,P_d^{\rm loc},S_t$, the equation ideal $\mathcal E_d$, and the full quantified local derivative estimates to U8 and C1.

## Chapter 4 (U2). Exact blocking and effective densities — 18 pages

**Input.** Wilson measure and lattice geometry; U1 only for notation used in examples.

**Sections.** (1) Center-normalized local gauges and axial gauges. (2) Averaged parallel transports and the nearest-group-point predictor. (3) Extension to every configuration by a finite random choice of frames/connectors; normalized probability kernel. (4) Small/large plaquette fields and admissible local activities. (5) Exact covering sum, local derivative seminorm and weighted polymer norms. (6) A provisional admissibility class for one adjacent pair, with all constants treated as inputs.

**Required output.** Define $k_m^\beta(U,V)\ge0$, prove $\int k_m^\beta(U,V)\,dV=1$, gauge covariance and lattice symmetry, and exact preservation of partition integrals. The density representation is
\[
\rho(U)=\exp[-A_m(\beta,U)-\sum_i1_{X_i\text{ small}}E_i(U)+v_m|\Lambda_m|]
\sum_{\mathcal A}\prod_{i\in\mathcal A}K_i(U),
\]
where selected supports are disjoint and their inventories cover all flagged sites exactly. Define locality on the **full read support**, including flags and extra eligibility tests. Distinguish anchored regular sums from sums over all polymers containing a site. Define Borel masks and derivatives with masks fixed; the clipped action is not globally smooth. Leave actual path coefficients as parameters until U5.

**Source packet.** Outline II.2 and III.1; Scott `part1/05-renormalization.tex`, `def:D04` (41), `def:D06` (105), `def:D05a` (136), `def:D05b` (148), and equations `eq:I12-clipping`, `eq:I12-path-action`; `part2/B-section.tex`, `subsec:B-kernel` (19) through `lem:B1` (119); `part2/D-section.tex`, definitions D24–D25a (21–67). Martin `lattice.tex`, `haar-chart.tex`, `local-mean.tex`, `predictor-branch.tex` supply expanded local geometry; read their named subsections before importing a branch argument.

**Checks.** The density has every branch and the empty covering convention; it is not merely its small-field approximation. Standard Haar/Fubini arguments receive a short citation/application, not lengthy proofs. Do not call all density representations positive without proving that they represent an actual transformed Wilson density.

## Chapter 5 (U3). Gaussian kernels and stationary backgrounds — 26 pages

**Input.** U2 block map, local gauge slices, norms and conditional adjacent-level parameters. Ordinary finite-dimensional Gaussian integration and Fourier theory are background knowledge.

**Sections.** (1) Lattice differential forms, zero modes and the gauge slice. (2) Linearized block averaging, Fourier aliases and the Schur complement. (3) Exponentially weighted kernels, strip analyticity and positive row factorizations. (4) A volume-independent vertical Hessian gap. (5) Analytic stationary background and a uniform coordinate ball. (6) Gauge-tree changes, Haar Jacobian and determinant compatibility. (7) Localized inverse and vertex derivatives.

**Required output.** For admissible incoming/outgoing Gaussian data and each allowed period, prove the exact quadratic minimization and covariance identities on the specified gauge slice; retain harmonic/zero-momentum contributions explicitly. Obtain a positive lower Hessian bound and exponentially weighted inverse bounds uniform in the period, hence a stationary branch with a common analytic radius. State precisely which estimates are pre-$L$, post-$L$, or large-coupling estimates. The curvature covariance identity is $C_{m+1}-W_mC_mW_m^{*}=d_f\Gamma_m d_f^{*}$, with $\Gamma_m\succeq0$, under the full compatible-quadratic-data assumptions. Prove tree independence only for the combined stationary value/Haar/determinant quantity, with the Jacobian factors shown.

**Source packet.** Outline III.3, III.6, III.16.5–III.16.7; Scott B `lem:B2` (242), `lem:B3` (409), `lem:B4` (501), `lem:B7` (584), `lem:B5` (665). Martin `free-kernel-components.tex`, `free-kernel-estimates.tex`, `weighted-stationary-inverses.tex`, and `uniform-stationary-chart.tex`: local derivative/Hessian data (8), common-ball contraction (73), derivatives (138). For cutoff kernel convergence later, retain `flat-step.tex`, `prop:ex-lattice-flat-step` (375), and `flat-estimate.tex`, `prop:ex-lattice-flat-rate` (12), but do not prove that separate recursion here.

**Literature and checks.** Bałaban's propagator/background-field papers are the original method, but neither the precise soft kernel nor the period-uniform hypotheses can be inferred from a citation alone. Replace routine inverse differentiation by its formula and reference. Do not use the one-loop matching to prove existence of the stationary branch whose determinant defines that matching. Split fresh matching assumptions from the analytic branch theorem.

## Chapter 6 (U4). Large fields and local Gaussian integration — 24 pages

**Input.** U2 exact sectors and U3 positive quadratic data/stationary branch. Work on one arbitrary admissible adjacent pair.

**Sections.** (1) Defect sets, connected neighborhoods and bounded overlap. (2) Completing squares and allocating positive energy. (3) Fine plaquette, predictor mismatch and coarse plaquette bounds. (4) Exact changes from Haar variables to Gaussian coordinates. (5) Localized covariance, relative determinants and scalar normalization. (6) Simultaneous Gaussian tail events and uniform derivative bounds.

**Required output.** Establish a deterministic lower bound with a strictly positive energy per independent defect, sufficient to dominate entropy and all later polynomial losses. Prove the exact local integral formula with its chart indicators, tags, Jacobians, frozen links, affine shifts, Gaussian density and positive scalar. State a simultaneous tail estimate indexed by **distinct tail-event addresses**; marginal tail estimates multiplied as if independent are not sufficient. Prove determinant/inverse estimates on full read supports and on the actual covariance used in the integral, not on an unrelated flat Gaussian model. The output is a common integrable majorant for each fixed derivative order, uniform in periods, fields, allowed sector data and coupling interval.

**Source packet.** Outline III.4 and III.10 steps 1–10; Scott B `subsec:B-energy` (761), `lem:B-D1` (842), `subsec:B-sector` (964), `lem:B-windows` (1009), `lem:B-D2` (1157). Martin `seed-energy.tex` (especially 189–301), `seed-hit-comparison.tex`, `seed-unhit-comparison.tex`, `gaussian-moment-prices.tex`, `gaussian-warnings.tex`, `warning-safety.tex`, `actual-palette-warning.tex`, `actual-harvested-owner-energy.tex`, and `actual-local-compiler-handoff.tex`: matrix/support estimates (52), determinant derivatives (112), interval uniformity (225), `lem:actual-neutral-warning` (257).

**Checks.** Keep energy loss, determinant normalization and Gaussian tail costs distinct until their common bound is proved. Martin's last two actual-data files are candidate missing compatibility suppliers, not interchangeable estimates. Mark their assumptions explicitly. Cite Combes–Thomas decay and standard Gaussian moment formulas; derive only their required uniform application. See audit A4/A10.

## Chapter 7 (U5). Local matching and the running coupling coefficient — 26 pages

**Input.** U3 stationary action/determinants, U4 local bounds, U1 invariant jets. No all-scale trajectory yet.

**Sections.** (1) Translation kernels and gauge Ward identities for Taylor coefficients. (2) Quantitative division through lattice curl. (3) Cubic/quartic classical matching and the fixed path action. (4) Gauge completion of the one-loop determinant, including Haar and ghost contributions. (5) One-loop annulus calculation and normalization. (6) Extraction of the unique invariant quadratic coefficient and estimates for the remaining quadratic kernel. (7) Stability under one downward step and stronger exponential-weight reserve.

**Required output.** Construct path coefficients with the stated symmetry, weighted bounds and no residual curvature-square coefficient in the loop correction. Prove the quantum quadratic coefficient is $-\kappa_G\log L+O_j(1)$, the error uniform in periods and admissible inputs, with $\kappa_G=11C_{\mathfrak g}/(24\pi^2)$ in the fixed trace metric. Distinguish this coefficient theorem from the exact nonlinear coupling-reset theorem of U6. Record the derivative/parameter dependence required later, not only a value bound.

**Source packet.** Outline III.7 and the fresh-data portion of III.6; Scott C `lem:C1` (44), `lem:C2` (62), `lem:C3` (87), `lem:C4` (147), `lem:C5` (185), `lem:C6` (211), `lem:C7` (266). Martin `stationary-output-construction.tex`: Ward data (10), leading coefficient (68), cubic/quartic matching (109), quadratic extraction (190), loop remainder (277), `prop:stationary-output-path` (359); `multileg-curvature-lift.tex`, `quadratic-lattice-symmetry.tex`, `thermal-contact-cancellation.tex`, `free-collision-pole-separation.tex`, and `free-maxwell-radial-flux.tex` give supplementary detailed routes.

**Literature and checks.** Cite Gross–Wilczek and Politzer for the one-loop coefficient and Abbott for background-field calculation; prove the bounded difference between that calculation and this exact lattice block map. A perturbative coefficient citation alone does not establish that comparison. Do not discard contact terms before explaining why they cannot change the extracted coefficient. If a quantitative curl-division lemma is already available in the needed weighted norm, cite it; otherwise prove that adaptation concisely.

## Chapter 8 (U6a). Abstract polymer and connected expansions — 18 pages

**Input.** Chapter 4's supports, anchored regular activities, containing-site large-field norms and exact-cover conventions. The abstract result needs only a countable incompatibility relation and complex activities, so it can be written independently of the nonlinear gauge estimates.

**Sections.** (1) Compatible gas and connected coefficients, including repeated labels and factorials. (2) The Kotecký–Preiss convergence criterion, stated with a precise rooted bound and cited rather than reproved. (3) Weighted supports and conversion from anchored to containing-site sums. (4) Several squarefree sources and bounds for connected marked coefficients. (5) Exact-cover large-field sums: distinguish the algebraic reorganization needed here from the unconstrained gas theorem. (6) Locality, parameter continuity under common domination, and the interface to Chapter 9.

**Required output.** State a standard absolute-convergence theorem with its actual incompatibility-sum hypothesis, and prove only the short reductions needed to apply it to the chosen support weights and finite source algebra. Show explicitly which source-specific bounds remain inputs: energy suppression, integrated Gaussian derivative bounds, eligibility events and exact cover reconstruction. No abstract polymer theorem establishes these estimates. A rooted estimate must charge all supports containing the root, not just activities anchored there. Count a repeated activity label correctly in the connected series even though compatible configurations contain each selected polymer once.

**Source packet.** Outline II.2, III.5, III.8 connected coefficients, III.15. Scott D `lem:D-rooted` (111), `lem:D-connected` (128), `lem:D-fusion` (546). Martin `cluster-expansion.tex`: cancellation (41), tree bound (56), root anywhere (132), exact logarithm (187). `high-degree-cluster-prices.tex`, `soft-log-fusion.tex`, and `forced-exclusion.tex` are follow-up sources for marked and exact-cover applications. The parent editor verified Ueltschi 2004, [full text](https://arxiv.org/html/math-ph/0304003v3), Theorem 1 and equations (3)–(4), as a convenient precise formulation of the standard criterion and rooted bound; Theorems 2–3 cover correlations. Cite Kotecký–Preiss for origin and Ueltschi for the form used.

**Boundary.** This chapter exports the abstract tool and norm conversions. The exact Gaussian integral, the concrete activities, and the proof that they obey its hypotheses belong to Chapter 9 and preceding analytic chapters. Do not reproduce Chapter 9's nonlinear construction here.

## Chapter 9 (U6b). The nonlinear RG step — 30 pages

**Input.** U2 density class, U3–U5 conditional estimates. Use Chapter 8 for the abstract polymer criterion and prove its model-specific hypotheses here.

**Sections.** (1) Apply Chapter 8 to the concrete local Gaussian expansion. (2) Integrated activity derivatives and spatial support weights. (3) Inherited terms, auxiliary-period localization and local quadratic subtraction. (4) Large-field polymer regrouping and exact coverage. (5) Reassembly of the genuine block integral. (6) Scalar coupling reset and parameter continuity. (7) Wilson initialization. (8) The complete one-step theorem, with its finite list of stage requirements.

**Required output (RG).** For every $N,p,m<N$, every compact real parameter interval, and every continuous admissible fine family $\rho'_u$ with couplings $\beta'_u\in\mathfrak B_{m+1}$, construct a continuous admissible coarse family $\rho_u$ such that pointwise
\[
\rho_u=\mathcal B_m^{\beta'_u}\rho'_u,
\qquad \beta(\rho_u)=\beta'_u-\kappa_G\log L_m+e_u,
\quad |e_u|\le\omega_{J_{m+1}}.
\]
The error bound is independent of $N,p,u$ and the chosen curve. The output regular and large-field norms obey the next-scale allowances. The construction must be fixed on entire curves with restriction compatibility; selecting unrelated output representations point by point is insufficient for U7 shooting and convergence. Record the stronger weighted analytic/continuity outputs needed for U7 separately.

**Source packet.** Outline III.5, III.8 (connected coefficients only), III.9, III.10 steps 8–12, III.15; Scott D: `lem:D-rooted` (111), `lem:D-connected` (128), `lem:D-inherited` (254), `lem:D-localization` (366), `lem:D-local-subtraction` (490), `lem:D-fusion` (546), `lem:D1` (574), `lem:D5` (603), `lem:C8` (663), `lem:D6` (732), `lem:D3` (772), `lem:D2` (843). Martin `cluster-expansion.tex`: repeated labels, weighted tree estimate (56), exact logarithm (187); `gaussian-reassembly.tex`: exact coordinate factors (13), restoring masks (87), absolute expansion (201), connected factorization (256); `coupling-reset-selection.tex`: separating field (10), scalar equation (53), identification with local coefficient (126); `actual-corrected-body-compiler.tex`, especially genuine density (270) and corrected forced output (416), for compatibility-sensitive applications.

**Literature and checks.** State and cite Kotecký–Preiss rather than reproduce an abstract cluster-expansion proof; show the activities satisfy its criterion and how source norms are incorporated. If using the repeated-label connected series, spell out the factorial convention and choose a matching formulation. No division by a vanishing polymer. Pointwise equality of the full integral, continuity, locality and both outgoing norms are separate conclusions. The one-loop approximation is not an approximation to this identity.

## Chapter 10 (U7). A common trajectory and fixed-scale stability — 24 pages

**Input.** U6 one-step theorem including continuation/continuity and stronger norm reserves, U5 path stability. U8's future finite-degree requests may be listed as explicit numerical requirements, but their analytic validity must already be established in conditional form before closing the simultaneous construction.

**Sections.** (1) Order of constants and finite-stage requests. (2) Increasing block ratios, stage plateaux, periods and reference scales. (3) Wilson shooting to the common endpoint. (4) Uniform logarithmic running. (5) Cutoff comparison of quadratic kernels, then cubic/quartic and loop coefficients. (6) Common activity dictionaries and fixed-scale convergence. (7) Retaining one family and all its transition witnesses.

**Required output (MT).** One schedule and one collection of trajectories for all $N,p$, before a requested volume subsequence, with Wilson start, endpoint $\beta_{N,p,0}=\bar\beta$, exact block identities and all admissible bands. For every $\varepsilon>0$, some $m_0$, independent of $N,p$, satisfies
\[
|\beta_{N,p,m}-\kappa_G\tau_m|\le\varepsilon \tau_m\quad(N\ge m\ge m_0).
\]
For fixed $m,p$, couplings and activities converge in one specified weighted space as $N\to\infty$; **no convergence of accumulated scalar normalizations is asserted**. Use normalized density ratios later. Provide a source-backed adjacent-step stability theorem on a fixed input; graph contraction alone cannot give stability of maps that themselves vary with the cutoff.

**Source packet.** Outline III.2, III.9 shooting, III.14; Scott `part1/09-constants.tex`, all rows 1–11; E `lem:E1.1` (112), `lem:E1.2` (160), `lem:E1.3` (199); D `lem:D-cutoff-continuity` (1069), `lem:D-E1` (1122), `lem:D-fixed-level` (1164). Martin `common-funded-history.tex`, `common-scale-selection.tex`, `surviving-interval-shooting.tex`, `running-coupling.tex` (`prop:running-asymptotic`, 105); `flat-step.tex` and `flat-estimate.tex`; `selected-history-limits.tex`, especially auxiliary service (147), activity/coupling limits (317), `lem:selected-chartlet-matching` (378); `public-run-binding.tex` and `original-history-portfolio-attachment.tex` for common-family identity.

**Checks.** The Outline III.13 coordinated construction is an alternative, not a replacement for this family. Its convergence results may be used only after proving equality of families or reproducing its hypotheses for this one. An infinite-dimensional norm ball is not compact. Use finite truncation plus uniform contraction/tails. The scalar drift must be divided by $\log L_m$ before summing; a stage error $O_j(1)$ alone is not summable. Include the finitely many initial indices rather than hiding them in “eventually.”

## Chapter 11 (U8). Insertions, Gaussian comparison and uniform difference bounds — 30 pages

**Input.** U1 sections/equation observables; U2–U7; C1 free Maxwell quotient, strict reflected Gram positivity and finite separating detectors. Treat C1 as a mathematical predecessor, not a forward reference to the final continuum comparison theorem.

**Sections.** (1) One inserted density, primary coefficient, vanishing-jet regular remainder and large-field remainder. (2) Reference-level normalization and the physical unit. (3) Several insertions using squarefree source variables, including joint large-field terminal modes. (4) Replicated sources and centered chessboard bounds. (5) Exact auxiliary restart for comparison and its full Gaussian law. (6) Corrected finite-cutoff free comparison, projections and finite detectors. (7) Equation errors, local matching and normalized lattice differences. (8) Separated correlation bounds uniform in the volume.

**Required outputs.** Construct an invertible $\mathsf Z_{N,p,d}$, respecting reality/symmetry, and
\[
O_{N,p}(d,c;x)=a_N^{-d}P_d^{\rm loc}[S_{1/t_N}\mathsf Z_{N,p,d}^{-1}c](x).
\]
The unit coefficient is $a_{r(d)}^de_0$, because the RG rescaling uses degree $d$ of the whole space, not the individual basis weight. The exact inserted recursion is $H_m=L_m^d\mathcal B_m^{\beta_{m+1}}H_{m+1}$. State coefficient/remainder estimates on this same density. For every finite tuple $v$, finite slot-difference list $l$, and (r>0), there are $C,N_0$, independent of $p$, such that $ |\Delta_l M_{N,p}(v;y)|\le C$ for all $N\ge N_0$ and all tuples with periodic physical separation at least $r$. Every normalized difference carries $a_N^{-1}$; a bound for undifferenced fields does not imply this one.

**Source packet.** Outline II.1.6–II.1.10, III.8 locality, III.11 finite-cutoff estimates only, III.12.1–III.12.5, III.15. Scott E `def:D26` (230), `lem:E2.1` (255), `def:D27` (314), `lem:E2.3` (354), `lem:E2.6` (417), `lem:E2.7` (438), `lem:E2.8` (456), `lem:E2.9` (474), `lem:E2-free-tests` (498), `lem:E2.10` (544), `lem:E2.4` (618); companions `E-one-mark.tex`, `E-several-mark.tex`, `E-Gaussian-sources.tex`, `E-local-comparison.tex`, `E-bounded-real.tex`. Read **Trish** `E-several-mark.tex`, `lem:E-joint-terminal` (52), for joint terminal modes and `E-Gaussian-sources.tex`, `lem:E-course-mass` (14), for exact mass preservation under a different comparison sequence. Its conditional paragraph after `lem:E-source-polynomial` must be explicitly addressed.

**Detailed candidate repair packet.** Martin `actual-marked-portfolio-calibration.tex`, `original-history-portfolio-attachment.tex`; `actual-local-compiler-handoff.tex` (327–404); `restarted-rank-history.tex`, `prop:restart-endpoint` (243), `prop:restart-actual-closure` (564, proof 581–742); `actual-mixed-marked-compiler.tex`; `allarity-planted-compiler.tex`, `all-arity-reader-gaussian-model.tex`, `actual-reader-local-gaussian-prices.tex`, `actual-reader-guarded-curvature.tex`, `actual-reader-tree-covariance.tex`, `actual-reader-short-covariance.tex`, `actual-reader-small-window-bridge.tex`; `fullmesh-fixedbounds-producer.tex`, `lem:ex-fullmesh-cap` (31), `prop:ex-fullmesh-cap-source` (68), full difference theorem (144), `prop:fullmesh-selected-supplier` (496). These detailed sections require a hypothesis-by-hypothesis comparison; no blanket claim that all Trish caveats are resolved is authorized by this blueprint.

**Checks and compression.** Squarefree source algebra is standard; show only the exact density correspondence and new large-field joint modes. The centered moment bound is a volume-uniform estimate of a replicated integral. In the finite-detector argument bound the projected coefficient and absorb half its norm; do not assume bounded raw differenced coefficients. Comparisons on an auxiliary restart preserve original normalized integrals, not equality of the two lower-level densities. Do not deduce continuum rank here.

## Chapter 12 (U9). The full ultraviolet limit at fixed volume — 24 pages

**Input.** U7 fixed-scale stability on the selected family and U8 actual inserted densities, replicated-source error bounds and all finite differences. No infinite-volume extraction is required to prove the principal theorem.

**Sections.** (1) Common intermediate level and scalar-normalized densities. (2) Contraction of the complete marked remainder graph and convergence of coefficient maps. (3) Joint marked expression, removal of higher modes and stopping error. (4) Cauchy convergence on common lattice points. (5) Equicontinuity, all position derivatives and interpolation. (6) Separated smearing and statement of the exact ultraviolet interface. Optional short final section: analytic endpoint dependence, only if needed downstream.

**Required output (UV).** For every fixed (p,n,v), obtain a smooth periodic $M^{\rm UV}_{p,v}$ on $\{x:x_i-x_j\notin R_p\mathbb Z^4,\ i\ne j\}$. For every finite difference list $l$ and smooth test compactly supported away from periodic collisions inside an admissible period cell,
\[
\lim_{N\to\infty}a_N^{4n}\sum_y f(a_Ny)\Delta_lM_{N,p}(v;y)
=\int f(x)\partial_lM^{\rm UV}_{p,v}(x)\,dx.
\]
The inner limit is the whole cutoff sequence. Explain separately that thresholds for fixed-volume convergence can depend on $p$, whereas U8's compact separated bounds are uniform in $p$. Coincident coordinate projections are allowed when points themselves are distinct. Export finite reflection positivity and the volume-uniform derivative bounds to C2.

**Source packet.** Outline III.12.6–III.12.8; Scott E `sec:partII-E.3` (663), `lem:E3.1` (703), `lem:E3.2` (732); `E-fixed-level.tex`, `lem:E-fixed-level` (21), `lem:E-stopping` (63); `E-bounded-real.tex`, `lem:E-coarse-bounded` (4), `lem:E2-bounded-real` (64). Martin `fixed-rung-convergence.tex`: graph contraction (10), fixed-input stability explicitly required (92), inserted functions (158), background density (183), positive normalized partition limit (287); `fullmesh-correlation-cauchy.tex`: fixed-level data (31), higher modes (86), their omission (164), Cauchy argument (237), all distinct points (279); `smooth-limits.tex`; `selected-history-limits.tex` for the required actual stability input. Compare Trish `E-fixed-level.tex` for warnings and stronger support bookkeeping.

**Checks.** The stopping estimate must have a prefactor uniform in the stopping level, or a demonstrated growth bound dominated by its decaying error. A subsequence obtained from Arzelà–Ascoli does not establish the full-sequence limit: prove Cauchy convergence first. A contraction bound for two graphs using the same map does not compare graphs using different cutoffs. Reflection positivity is passed only for admissible tests and finite identities; do not claim an unsubtracted distributional limit at collisions.

## Original-literature checks for these chapters

The following are checked bibliographic starting points, not a completed theorem-equivalence audit. The author must read the cited theorem before substituting it for a source proof.

- Kotecký–Preiss, *Cluster expansion for abstract polymer models*, CMP **103** (1986), 491–498, [DOI](https://doi.org/10.1007/BF01211762). Publisher and original paper accessed through search on 2026-11-18. Use its abstract criterion after matching conventions; do not claim it proves this gauge model's activity bounds.
- Bałaban, *Propagators and renormalization transformations for lattice gauge theories. I*, CMP **95** (1984), 17–40, [DOI](https://doi.org/10.1007/BF01215753). Publisher page identified. Relevant to U3's linear mechanism, not a replacement for the actual nonlinear/marked estimates.
- Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP **102** (1985), 277–309, DOI 10.1007/BF01229381. Metadata located; precise theorem application remains to be checked against the original paper.
- Brydges–Yau, *Grad φ perturbations of massless Gaussian fields*, CMP **129** (1990), 351–392, DOI 10.1007/BF02096987. Source bibliography and search metadata agree; inspect the original before invoking a norm or localization theorem.
- The supplied Scott introduction gives useful original-work pointers: Bałaban 1987 §§4–5 and pp. 252–254; Bałaban 1989 large fields, Theorem 1; Gawędzki–Kupiainen 1985 pp. 212, 218–221; Brydges–Yau §§1–2; Osterwalder–Seiler 1978; Fröhlich–Israel–Lieb–Simon 1978 §4. These exact-location claims are source leads, not independently verified citations in this blueprint.
