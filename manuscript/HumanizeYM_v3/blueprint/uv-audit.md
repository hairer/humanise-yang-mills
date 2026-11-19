# Ultraviolet source audit and reading routes

This is an **audit of exposition and interfaces**, not a referee report certifying the construction. The outline's “What remains unexplained” paragraphs describe the scope of the outline's review. They do not establish that the underlying mathematics is missing. Likewise, a conditional intermediate lemma is not a global gap when a later theorem supplies its conditions. Conversely, the final assembly's assertion that all conditions hold does not replace checking those conditions in a readable proof.

The most valuable comparison found so far is that **Martin contains detailed candidate repairs for specific conditional passages in Trish**. Those repairs should be used to write the missing mathematical argument, with an explicit hypothesis correspondence. They have not all been independently checked down to primitive analytic estimates. Do not describe the source collection as either fully verified or globally incomplete on the basis of this audit.

## 1. Coverage of every ultraviolet outline unit

| Outline unit | Final chapter home | Exact source lead and audit issue |
|---|---|---|
| II.1 | 2 for labels/sections; 11 for transfers; 13 for limit quotient | Scott A `lem:A1`, `lem:A-R4`; E `lem:E2.1`. Split elementary label construction from actual RG transfer and continuum null-space identification. |
| II.2 | 4, 8 | Density/activity definitions are not the same as Gaussian or cluster estimates. Use Scott Part I definitions D05a/b,D06 and D definitions D24–25a. |
| III.1 | 4 | Scott B `lem:B1`; exact probability kernel and every branch. Energy estimates used in branch bounds need an explicit local conditional formulation, not a forward invocation of the completed construction. |
| III.2 | 10, with finite requirements recorded in 5–9 and 11 | Scott constants table, E `lem:E1.1`; Martin `common-scale-selection.tex`, `public-run-binding.tex`. Schedule selection uses analytic estimates already proved conditionally. Numerical maxima do not prove those estimates. |
| III.3 | 5; cutoff rate in 10 | Scott B `lem:B2`; Martin `flat-step.tex`, `flat-estimate.tex`. Zero/harmonic modes and gauge slice must be stated. No position-space continuum comparison follows from a Fourier coefficient statement alone. |
| III.4 | 6 | Scott B `lem:B-windows`, `lem:B-D2`; Martin `actual-local-compiler-handoff.tex`. Match the actual sector, frozen variables, precision, affine mean and chart. Flat-sector comparisons are insufficient for arbitrary interacting sectors. |
| III.5 | 8 abstract; 9 concrete | Scott D `lem:D-rooted`, `lem:D-connected`; Martin `cluster-expansion.tex`. Standard abstract convergence can be cited; the actual gauge activities and exact cover still require proof. |
| III.6 | 5 branch/inverse; 7 fresh matching; 10 stability | Scott B `lem:B3`–`lem:B7`; Martin `uniform-stationary-chart.tex`, `stationary-output-construction.tex`. Do not hide fresh classical/quantum matching in the hypotheses of an alleged complete induction. |
| III.7 | 7 | Scott C `lem:C3`–`lem:C7`; Martin `stationary-output-construction.tex`. Separate known perturbative coefficient from the nonperturbative exact-block comparison and bounded errors. |
| III.8 | 8 coefficient algebra; 11 support/factorization | Its Gaussian connected series is formal in the perturbative parameter unless convergence is separately proved. Locality of the block kernel is a different assertion from polymer convergence. Scalar terms need their own convergence. |
| III.9 | 9 reset/start; 10 shooting/running | Scott D `lem:C8`, `lem:D3`; Martin `coupling-reset-selection.tex`. The exact masked density identity and continuous scalar reset must match, not merely their quadratic approximations. |
| III.10 | 6 energy and Gaussian tails; 9 complete step; 11 marks | Scott B energy/sector; D complete recursion; Martin `seed-energy.tex`, `gaussian-reassembly.tex`. Preserve the distinction between local energy, rooted-integral bounds, outgoing norms, and reset. |
| III.11 | 11 finite-cutoff comparison; 13+ continuum rank/stress | Scott E free tests/rank; Martin actual-reader files and `actual-rank-purchases.tex`. Free Maxwell detector algebra is already in Chapter 3. Limit rank must not be used circularly to obtain pre-limit difference bounds. |
| III.12 | 11 uniform differences; 12 full mesh limit | Scott E `lem:E2.4`, `lem:E3.1/2`; Martin `fullmesh-fixedbounds-producer.tex`, `fullmesh-correlation-cauchy.tex`. Distinguish uniform-in-volume thresholds from fixed-volume convergence. |
| III.13 | Optional comparison note only, not a proof input without identification | An alternative coordinated family. The outline explicitly does not establish its equality with III.14's main family. Copying III.13's results into the main theorem would require new hypothesis checking. |
| III.14 | 10 quadratic convergence and retained family | Martin `rg-construction.tex`, `public-run-binding.tex`; outline's selected-run construction. Do not discard an attached datum and later infer it from a reduced record. |
| III.15 | 8 norm calculus; 9 concrete bounds; 11 marked comparison | Comparison-function existence does not supply the actual coefficient-matching hypothesis. Preserve full supports and positive reserves. |
| III.16 | 2 labels; 3 Maxwell; 5 Fourier/matrix tools; 13+ trace-gap tools | Distribute standard tools at their first use and cite them. Avoid a late toolkit that makes all prior arguments depend on definitions not yet given. |

## 2. The finite-cutoff comparison: precise candidate repair chain

### The caveat in Trish

`Trish/part2/E-Gaussian-sources.tex`, after `lem:E-source-polynomial` (the lemma begins around line 106 in this snapshot), says the application to the actual pushed source still requires a joint-law estimate. The physical reads, forecast, guard, determinant, residual loading and empty mode must all use the same sector law. The resulting estimates must control regular and normalized large-field terms with the original tests. If the comparison uses a restarted coupling sequence below the reading level, it additionally needs an exact density and coupling identification for that sequence. The paragraph explicitly makes the lemma and applications conditional until a supplier is established.

This is more than the elementary fact that a Gaussian polynomial moment is close to a Maxwell polynomial moment. The latter does not identify the integrand or measure used in the actual RG density.

`Trish/part2/E-Gaussian-sources.tex`, `lem:E-course-mass` (14), proves the useful exact statement that pushing the **whole** integrable marked polynomial through normalized block kernels preserves every coefficient integral and the empty coefficient's normalization. Changing the lower coupling sequence does **not** identify the two lower densities or their conditional laws. This elementary distinction must survive in the monograph.

### Martin's local estimates and their application

1. `Martin/existence/all-arity-reader-gaussian-model.tex`, `sec:ex-lattice-all-arity-reader-gaussian-model`, defines one sample space (12), joint transverse law (81), and simultaneous comparison (138). This is a definition/probability-law route, not by itself the bound for the actual sector.
2. `actual-reader-local-gaussian-prices.tex`, `sec:actual-reader-local-gaussian-prices`, controls removal of bare cut/window (65) and every cross-entry after reading curvature (128). `actual-reader-small-window-bridge.tex`, `prop:ex-lattice-actual-reader-panel` (56), is the concrete local comparison lead. `actual-reader-guarded-curvature.tex`, `actual-reader-tree-covariance.tex`, and `actual-reader-short-covariance.tex` supply further specialized bounds.
3. `actual-corrected-body-compiler.tex` explicitly lists local hypotheses at 11–62: actual path and clip, covariance floors, two determinant series, inverse correction, chart coordinate and residual bounds, radius inequalities, inherited activity reserve, and coupling/threshold relations. Its two distinguished remaining inputs are an energy bound on the actual large-field components and a Gaussian tail estimate uniform over compatible field/store pairs. The fact that they are assumptions here is **not** evidence that no later section supplies them.
4. `actual-local-compiler-handoff.tex`: matrix and both support inventories at 52; first derivatives of both long determinant series at 112; interval-uniform estimates at 225. Lines 234–236 explicitly use `eq:owner-actual-heft` from `actual-harvested-owner-energy.tex` for the actual energy input. `lem:actual-neutral-warning` (257) proves transfer of the simultaneous tail bound to the corrected alphabet, with the same Gaussian law and distinct event addresses. It does not replace the interacting density by its neutral version: neutralization is used for estimates while the corrected expansion reconstructs the genuine density.
5. The handoff's last section (327–404) distinguishes genuine and neutral representations, retains the positive original loading, and requires same-history path/clip/tube and remainder bounds on the comparison interval. Its final paragraph explicitly names `prop:restart-endpoint` and `prop:restart-actual-closure` as the history-level suppliers. Therefore stopping at its earlier conditional paragraph would give an incomplete account of Martin's argument.

### The explicit restarted-history closure

`Martin/existence/restarted-rank-history.tex`, `prop:restart-endpoint` (243), constructs the exact endpoint presentation. `prop:restart-actual-closure` (564), with proof at 581–742, is the main candidate response to Trish's same-course caveat.

**Its inputs, as stated:** the already selected chart/tube data, original path bounds and identification, adjacent metric floors, room/chart parameters, the local reserve choices of the handoff, the larger raw support exponent of `prop:allarity-compiler-reserve`, and the endpoint bounds of `prop:restart-endpoint`. The finite set of requests at each adjacent stage pair is met before its entry time. These are more than bounds on nominal couplings.

**Its outputs, as stated:** on every level of the comparison interval, a restarted representation with the original level's path and clip, constant coupling equal to the original reading-level coupling, additive value cost at most (q_{k-i}), and large-field allowance (G(x_i)=\exp[-a_{\rm coast}\operatorname{hot}(x_i)^2]). The neutral versions satisfy the inherited-law hypotheses. Every adjacent step satisfies (V1)–(V3) on one corrected alphabet, the exact density identity `eq:restart-push`, and upper/lower connected-integral estimates with the same normalization. Bounds are uniform in cutoff, period, fields and finite marked families with fixed arity cap, allowing fixed-profile dependence.

**Proof structure inspected:** (a) clock and threshold estimates place the actual fixed coupling in each adjacent band; (b) the original paths/clips/tubes are unchanged by replacing activities; (c) deleting only the additive family gives the neutral incoming representation, while the genuine value cost is controlled separately; (d) large-field energy pays forced inflations, the **single joint Gaussian tail event** controls all tail factors, and full-support rooted sums control additive contributions; (e) the positive original scalar loading and connected expansion reconstruct the exact genuine density; (f) the renewed additive/large-field bounds allow induction, including adjacent stage transitions. This is a substantial mathematical candidate repair, not just an existential assembly assertion.

**Remaining audit task:** verify each cited actual energy/tail/support-reserve estimate on precisely these inputs, then check that the finite-reader theorem used by `actual-rank-purchases.tex` has the same source normalization, all-mark support conventions and Gaussian parameters. In particular, translate Martin's numerical functions into the monograph's chosen scale convention, rather than assuming that `hot` equals Scott's (H_m). This audit has not independently completed that final match. The correct current classification is **detailed supplier located and partially read; full hypothesis match pending**, not “unresolved global gap.”

### Route to the public family

`actual-rank-purchases.tex` builds common test lifts and a single auxiliary history for all rows (88), solves normalization equations (174), then obtains the point-comparison bound `eq:rank-purchased-point-comparison` (293). `fullmesh-fixedbounds-producer.tex` uses actual finite-cutoff detectors, projection absorption, equation errors and centered bounds, culminating in `prop:fullmesh-selected-supplier` (496). The full-mesh difference theorem at 144 has the exact quantifiers required in Chapter 11: one threshold for every volume and all separated periodic tuples, not a threshold for each fixed volume.

`public-run-binding.tex` retains the actual family, selected histories and transition witnesses; its opening explicitly says it supplies no replacement for an outstanding local estimate. `assembly.tex`, `thm:ex-construction-assembly` (267), cites the selected supplier and common-history Cauchy argument on that same family. The final assembly is therefore an intended closure of the conditional interface, not a proof that each intermediate matching step can be omitted in the monograph.

## 3. Fixed-level convergence: another compatibility-sensitive route

`Martin/existence/fixed-rung-convergence.tex` proves a useful graph-contraction argument, but at line 92 explicitly retains a fixed-input stability hypothesis: for every fixed admissible graph, the adjacent-step map and coefficient map are Cauchy as the terminal cutoff changes. The bound comparing two graphs under one fixed map does not imply this.

The candidate supplier is not an abstract compactness argument. `selected-history-limits.tex`, activity/coupling limits at 317, identifies the common dictionaries, actual paths and scalar corrections. It then explains the auxiliary zero-array input required by the common-variable comparison. `lem:selected-auxiliary-service` (147) supplies the same stationary branch, and `lem:selected-chartlet-matching` (378) checks activity budgets, sector access, Gaussian tails, chart, and corresponding comparison hypotheses for that auxiliary input. Scott's shorter route is D `lem:D-cutoff-continuity` (1069): stronger-weight tails, finite-coordinate convergence, Gaussian dominated convergence and exact affine coefficient recursion.

**Author task:** use one complete route, not half of each. Specify the fixed norm/dictionary, the allowed auxiliary inputs, their common chart, and the stability conclusion. Avoid claiming compactness of a ball in an infinite-dimensional activity space. Once this input is proved, the graph truncation and Cauchy argument are standard and can be presented briefly.

## 4. Prioritized verification list

| ID | Obligation | Candidate source | Classification |
|---|---|---|---|
| A1 | Parameter-independent exact local section and dressed equation identity | Scott A; Martin local-sections/local-splitting/actual-equation-kernel-relay | Section construction inspected; full equation compatibility not yet audited |
| A2 | Every branch of normalized block map, measurability and symmetry | Scott B kernel; Outline III.1 | Read at statement/proof-summary level |
| A3 | Gauge/zero modes, compatible Gaussian kernel and uniform stationary radius | Scott B2–B7; Martin uniform-stationary-chart | Concrete routes located, not fully verified |
| A4 | Same actual sector for coordinate, determinant, inverse, energy and joint-tail estimates | Martin actual-local-compiler-handoff and its named inputs | Handoff and joint-tail transfer read; primitive estimates pending |
| A5 | One-loop coefficient normalization and bounded exact-block difference | Scott C5–C7; Martin stationary-output-construction | Precise obligations identified; full calculation pending |
| A6 | Exact full-density reassembly with both outgoing norms and reset | Scott D5/C8; Martin gaussian-reassembly/coupling-reset-selection | Routes located; must be checked as one application |
| A7 | A single schedule and original-family identity | Martin public-run-binding/common-funded-history; Scott constants | Order and witness retention inspected |
| A8 | Cross-cutoff adjacent-map stability on the actual/auxiliary inputs | Martin selected-history-limits and fixed-rung-convergence; Scott D cutoff continuity | Explicit missing premise and candidate supplier both located |
| A9 | Joint large-field terminal modes, no division by activity | Trish E-joint-terminal; Martin actual-marked-portfolio-calibration | Trish algebra/construction read; norm translation pending |
| A10 | Restarted exact density and full marked joint law | Martin restart-endpoint/restart-actual-closure plus reader files | Detailed closure proof read; downstream hypothesis match pending |
| A11 | Projection absorption and volume-uniform normalized differences | Martin fullmesh-fixedbounds-producer | Theorem quantifiers and absorption structure read; all inputs pending |
| A12 | Stopping error uniform enough in intermediate level and full-sequence convergence | Martin fullmesh-correlation-cauchy; Scott E-fixed-level | Route located; all prefactor dependencies require audit |

These are work instructions, not claims of mathematical errors.

## 5. How to use the three versions economically

A line-sequence comparison of matching Part II files shows that Scott/Trish overlap strongly: A ≈97.9%, E main ≈97.9%, D ≈93.4%, B ≈91.2%, C ≈86.3%. The most useful UV differences are `E-several-mark.tex` (≈56.4% matching lines), `E-Gaussian-sources.tex` (≈75.4%), and `E-fixed-level.tex` (≈77.7%). These figures are textual, not measures of correctness. Read Scott for the concise architecture, Trish for these compatibility warnings/additions, and Martin only along the explicit supplier routes above. Martin's dense naming is best translated by writing the exact mathematical input/output before shortening the prose.

Every unit's full `Scott/Outline/units/III-k.md` contains pinned formal-source references and a separate limitations paragraph. When a supplied manuscript remains ambiguous, use those exact links to identify the relevant declaration; do not substitute a broad repository search for reading its hypotheses. The outline status “edited” is editorial review, not independent mathematical verification of every dependency.

## 6. Follow-up check of the candidate repair

See [restart-supplier-check.md](../audit/restart-supplier-check.md) for a deeper check. It follows the later replacement route in Martin's long allarity-marked-propagation.tex: lem:allarity-guarded-gaussian (1266), lem:allarity-pair-reader (1415), prop:allarity-compiler-reserve (2062), lem:allarity-selected-opening (2615), and prop:allarity-selected-application (2704). In particular, the earlier common-cutoff measure criterion (M) is a sufficient route, not a necessary missing premise of the later guarded route.

The follow-up checks the clipping inequality, restarted value-cost recursion, support-exponent monotonicity, guarded Gaussian finite-polynomial estimate, exact identity \(Jq_N\mapsto Jq_k\), common denominator, lift inversion, finite-detector stability, and final coefficient absorption. It also distinguishes the independent microscopic-equation/centered-budget branches needed by the full-mesh supplier. Primitive local covariance, energy and room estimates remain outside that independent verification.


## Support clarification for Chapters 4 and 8 (19 November 2026)

Scott `part2/D-section.tex`, `def:D25` and the immediately following paragraph distinguish three objects: Y_i is the large-field polymer exclusion/coverage support, I_i is its exact set of flagged sites, and the complete read support is its actual dependence region. K_i depends on links internal to Y_i and flags in Y_i. Deciding these flags reads plaquettes within distance one of Y_i. Thus disjoint Y_i can have overlapping full read supports. Exact covers require disjoint Y_i; their weighted containing-site norm uses cov_B(Y_i). Connected elementary-factor expansions use overlap of full read supports. Neither independence nor disjoint dependence follows from disjoint Y_i. Enlarge supports only with an explicit conversion estimate, not by silent renaming.

The Chapter 4 source packet's `Martin/existence/local-mean.tex` concerns Gaussian means away from seeds; it is not the gauge-average construction. Use `Martin/existence/predictor-branch.tex`, especially `lem:branch-nearest-projection` and the uniform-minimizing-frame subsection, for that argument.
