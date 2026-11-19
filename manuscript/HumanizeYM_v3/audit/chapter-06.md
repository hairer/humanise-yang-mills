# Chapter 6 audit: large fields and one common Gaussian law

File: `chapters/06-large-fields.tex`. Status: substantive partial chapter, with explicit conditional implications. It does **not** certify Scott D1/D2 for the full chosen trajectory. No global files or compilation changed by this agent.

## Proven/exact content in this draft

- Exact six-term identity (`ch06:global-energy`) with **actual truncated transported adjoints**, not flat adjoints. It is a global identity; the local sum near a selection is treated separately.
- Fine/mismatch/coarse energy bounds, including counting witnesses for dropped relaxed-test path rows. These assume the stated path row/column norms and compatible clip coefficients.
- `ch06:energy`: complete scalar absorption proof from the now-verified quantitative signed comparison, in the order fixed stage/path data → L → W → reference-coupling threshold. The threshold is uniform in the torus and sector. No small fields are deleted.
- `ch06:predictor-comparison`: first-power synchronization bound for minimizing frames, eligible axial frames, and both exact predictor branches of Chapter4. Supplies the pre-L macro comparison and period multiplicity. The rooted predictor derivative is explicitly the straight average plus a gradient. `ch06:signed-input` is now a proposition proved for compatible aligned flat/path rows, rather than an additional nonlinear assumption.
- Actual coercivity transfer: the precise local tree inequality and finite-patch derivative comparison imply the actual selected-row gap, with a proof by squared local sums and bounded stencil multiplicity. This makes clear which geometric input still needs matching.
- `ch06:windows`: uniform local inverse-column construction from an actual matrix gap and exponential Schur bounds; proof covers every principal compression, finite-range covariance positivity, and fixed-order derivatives with fixed windows.
- `ch06:gaussian-identity`: exact affine normalization for arbitrary positive reference covariance, arbitrary mean, beta scaling, and the retained linear/quadratic density corrections. Haar and scalar normalization are not discarded.
- `ch06:protected-change`: exact physical-link-preserving change in a protected log chart; no claim that this formula alone constructs its global extension.
- `ch06:joint-tails`: elementary Gaussian exponential Markov + witness-counting argument, with distinct addresses and correlated coordinates. This is not a new Gaussian tail theorem; the source-specific content is the address/witness multiplicity and application scale.
- `ch06:common-majorant`: precise consequence of a common-product quadratic-exponential bound and same-mask local vanishing. Assumptions explicitly include polynomial moment control under the tilted Gaussian. Products of marginal norms are never used.

## Exact source map

Scott `part2/B-section.tex`:

- `subsec:B-energy` lines760ff: six rows, selected tests, very-large tests, affected anchors.
- `lem:B-D1`842ff: direct bounds; source proof Step2 gives the signed affected comparison and pre-L excess constant, Step3 common gauge and subtraction of the flat identities, Step4 scalar absorption.
- `subsec:B-sector`964ff: actual retained affine rows and distinct sector/local inverse windows; `eq:B-window` defines P,Gamma,m.
- `lem:B-windows`1009ff: claimed gap/derivative/mean estimates; the chapter isolates actual-data inputs instead of inferring them from a flat Hessian.
- `lem:B-D2`1157ff: local integration target. We have not imported its whole conclusion as a theorem.

Martin `existence/`:

- `seed-energy.tex`, especially189–325: explicit scalar assembly from signed/local geometric inputs. It does not by itself prove every signed input.
- `seed-hit-comparison.tex`: actual route multiplicity, constant part vs excess part; the excess constant is fixed before L,W.
- `seed-unhit-comparison.tex`: subtract the four exact flat identities before bounding nonlinear errors; actual rooted predictor differs from straight average by an exact gradient.
- `seed-tree-patch.tex`: `eq:tree-shell`, `eq:tree-common-gauge`; tree comparison and common gauge on the same field/tree/tags. The stated source trees have root path length≤4L; any extension to other trees requires tracking the route constant. The monograph requires the local inequality explicitly, rather than claiming it for arbitrary unverified trees.
- `sector-gram.tex`: `eq:sector-local-linear`66ff is the local tree inequality. Its main matrix is **transported flat** and selected by anchor, so cannot substitute for the actual matrix.
- `actual-global-row-prices.tex`: `prop:actual-global-row-prices`~106ff; actual stencil-selected derivative matrix. Lines139–248 give impulse/Schur bounds and a separate actual coercivity proof by fixed-patch continuity + local tree inequality. Lines260–306 principal inverse columns; lines308ff affine sources. This is a serious candidate supplier, not absent mathematics: the remaining work is matching all of its construction data and hypotheses to the chapter's Scott pair and differentiated family.
- `actual-local-compiler-handoff.tex`: matrix/support hypothesis handoff52ff, determinants112ff, interval uniformity225ff, `lem:actual-neutral-warning`257ff. Its final statement is not permission to drop the underlying same-field response/mask assumptions.
- `gaussian-moment-prices.tex`: fixed-degree moments and derivative-density ratios; the source key `IsserlisProof` is a **2025 proof**, not the original paper.
- `gaussian-warnings.tex`1–90: correlated Chernoff/crowding argument; later local mask vanishing is a separate assertion.
- `warning-safety.tex`: selected affine rows and mean25ff, minimizing branches92ff, three comparison errors140ff, threshold choice200ff.
- `actual-palette-warning.tex`: actual-response53ff, all-matched family149ff, local mask170ff, `prop:actual-palette-condition`229ff, combined matrix/mask257ff. Proposition229 explicitly assumes disjoint-region branch geometry, local branch estimates, chart/interface bounds, and response bounds on the **same** field/forest/tags/store. The combined section begins a comparison between auxiliary and actual means; they must not be identified.
- `actual-harvested-owner-energy.tex`: same-path/clip energy and normalized integration handoff; its final envelope needs the preceding same-data bounds.

## Exact remaining assertions, with quantifiers

Fix the group and trace metric, one stage j, incoming/outgoing path families and coefficients, penalty b, predictor patches/branch rules, tree family, orientation normalization, log chart and cutoff profile. Fix L and W in the order prescribed by the energy argument. The following statements must hold for all sufficiently large reference coupling x, **uniformly over** every coarse period n≥100(B(x)+1), every admissible actual coupling beta in [hatbeta_f/2,2hatbeta_f], every consistent selection/sector, every allowed tree and positive-mass tag, every allowed coarse configuration, and every frozen field Y. Cutoff tests, selected rows, windows and coordinate sets remain fixed when differentiating. Constants can depend on fixed j,L,W,k,q, but not the subsequent choices. The exceptions where a constant must be fixed before L,W are stated below.

### 1. Signed comparison: nonlinear branch obligation discharged

The actual route comparison is now proved as `ch06:predictor-comparison`, matching Chapter4 exactly: normalized minimizing frames on the loop-test branch; eligible axial frames otherwise; weighted nearest-group-point predictor below its minimum-cost cutoff; an actual connector otherwise. The lower probability of a fallback connector never enters the chord estimate. The normalization is chi²/2=w, matching Martin's squared-chord cost.

The proof gives `r_c(p) <= sum_boundary(p)n_e + C_j L^-2 sum_q m_y(q)r_f(q)`, with the excess C_j and `sup_q sum_y m_y(q)<=K_j` fixed before L. It uses a uniform first-power frame synchronization lemma, not a square-root Jensen bound. The affected estimate follows by absolute row/column summation exactly as in `seed-hit-comparison.tex`.

The common gauge is now constructed with the actual tree slice. Rooted tree path lengths need only a fixed-L bound≤L⁴−1 here; this constant is NOT used in the pre-L excess estimate. The actual predictor derivative is obtained by differentiating Chapter4 connectors: `Q a = A a + Hbar_y(a)-Hbar_(y+mu)(a)`, hence differs from the straight average by a coarse gradient. The gradient vanishes under curl. Fixed-patch smoothness follows from the nondegenerate minimizing-frame equation, and only second derivatives are needed for this Taylor estimate.

`ch06:signed-input` is now a proposition, conditional on the explicit **remaining path-data input**: for the same fine/coarse stages and actual selected path coefficients, the uncut curvature row maps and flat square-completion maps satisfy `Mf* Mf+Mn* Mn+N* N=I` and `Mf*Xf_lin+Mn*Z_lin=Xc_lin`; their path coefficients are aligned under displacement/orientation grouping, absolutely exponentially summable with a common positive rate, and their transported row/column sums have the stated pre-L bounds `(CL^-2,CL²)` for Phi and `(C,C)` for the other maps. A stationary kernel with unrelated coefficients does not supply this. Production of these aligned path data remains Chapter5/7 work. Given them, the chapter now proves both signed inequalities and the large coarse-plaquette count; no extra nonlinear signed comparison is assumed.

### 2. Actual local tree and matrix/forcing estimates

The geometric proof now supplies `ch06:tree-control` by differentiation for the exact permitted trees and actual predictor derivative, and the finite-patch branch is smooth near identity. Verify that the selected row coordinates of the intended sector are precisely these zero-extended forest directions and same actual plaquette/predictor derivatives; then the common-gauge comparison and absorption in the chapter give the actual gap. The remaining work is this coordinate identification and the higher-order/source estimates below, not a missing deterministic branch comparison. In addition, for A=D*D, f=D*b_Y of **stencil-selected actual retained affine rows**, need constants c,C,tau>0 such that

- `c I <= A <= C I`, and weighted absolute row AND column sums of A bounded by C at rate tau;
- for any prescribed k,q, coarse derivative directions of size≤t_c(1+dist(o,e))^q obey `|D^r A_{ii'}| <= C_k exp(-tau dist(i,i')) (1+dist(o,i))^(qr)` for 0≤r≤k (or the equivalent ordered multilinear weighted norm);
- the affine source/forcing satisfies `|D^r f_Y(i)| <= C_k t_f (1+dist(o,i))^(qr)` on the same family.

Fixed coordinate multiplicity per anchor includes L⁴ residues/colors/orientations. A precision bound for an anchor-selected transported-flat matrix is insufficient. The actual source can involve frozen coordinates: 'arbitrary Y' is only meaningful on the sector constraints supporting those affine rows, and must retain those constraints.

The chapter derives the inverse/window bounds and `D^r m=O(t_f weight)`, `D^r[g^-1(Am+f)]=O(exp(-cB)weight)` from these inputs. Principal inverse and Gaussian marginal inverse are distinguished.

### 3. Same-law coordinate change and common majorant

For every finite union I of factor dependence regions, construct a smooth invertible extension of `ch06:protected-change` agreeing with it on the nested protected chart. Prove all required ordered derivatives of its Jacobian, the marginal covariance Gamma_I, affine shift, Haar densities, tags and smooth factors are bounded under the **one** law `dY dgamma_{Gamma(Y)}`. The product's fixed-order derivative must have `ch06:majorant-form`, with

`||Gamma^1/2 K Gamma^1/2|| <=1/8` and `tr(Gamma^1/2 K Gamma^1/2)+|Gamma^1/2 eta|² <= C sum lambda_i`,

where K and eta are the sums for the whole product, not individual unrelated local estimates. Polynomial moments under the corresponding doubled-exponent tilted Gaussian must be controlled by a fixed polynomial in (1+s), with declared coupling factor. For a power beta^-tau per address one may use polynomial/subpower coupling factors; stronger requested large-field norms need their exact advertised functions verified, not inferred from a power estimate.

### 4. Same-mask local vanishing

Each distinct actual cutoff remainder/address w in that product must vanish whenever all relevant coordinates within2B of w satisfy `|z_i|<xi t_f/(2g)`, with xi>0 uniform over the same configurations/branches/Y/beta interval. Include fine-plaquette and predictor cutoffs, frame/predictor likelihoods, inventory/interface and chart factors. A small-field bound for an auxiliary centered background does not establish this for the actual mean m_Y without a comparison. Address and coordinate multiplicities per coarse anchor must be bounded and include all tag types. This is the exact missing input to apply the proved joint-tail lemma.

### 5. Normalization and dependence needed downstream

Keep `(2 pi g²)^(n/2) det(Gamma)^(1/2) exp(-beta Q_Y(m))`, all chart indicators/Haar Jacobians, and both residual exponents. A claimed per-test suppression must exhibit the assignment of its logarithmic normalization losses to tests; an extensive vacuum scalar cannot be discarded or silently absorbed.

An activity's exclusion support controls the cover sum only. All statistical factorization and connected graphs must use full dependence regions. Conditional Gaussian factorization requires cross covariance zero; after Haar mixing it additionally requires the relevant frozen variables/law to factor. Neither fact follows from disjoint exclusion supports.

## Literature check

- Original Gaussian moments: Leon Isserlis, *On a formula for the product-moment coefficient of any order of a normal frequency distribution in any number of variables*, Biometrika12(1–2),134–139(1918), DOI10.1093/biomet/12.1-2.134. Primary OUP metadata verified at https://academic.oup.com/biomet/article-abstract/12/1-2/134/193428 . Chapter cites key `Isserlis1918`; parent added bibliography entry. Formula is cited, not reproved. A search result purporting to be an original-paper mirror at University of Cincinnati was actually a lecture-note compilation; it was not relied upon as the original.
- Window decay uses the weighted-conjugation argument already exposed in Chapter5. Historically this is the Combes–Thomas method; no unsupported citation is used as a theorem about these exact selected matrices. Standard inverse differentiation, logdet differentiation and elementary finite Gaussian completion are not presented as original results.
- No original literature located for the exact six-term nonlinear row/mask bookkeeping. Its retained short proofs and hypotheses are source-specific; no novelty claim made.

## Independent review already completed

`chapter-05-independent-review.md` records the Schur/Fourier/zero-mode review. UV agent confirmed the two requested corrections were made: beta-rescaled fluctuation variables/covariance and bounded total coordinate multiplicity. Chessboard original-source match was completed in `chapters-01-02.md` and `foundations-literature.md` using FILS Theorem4.1; no power-of-two cell-count restriction remains.

## Stationary Hessian implication checked after the branch proof

`path-attachment-producer.tex`130–235 uses the identical tree/macro/predictor comparison. Its squared sum gives `||v||² <= C_L(||d_f v||²+||Q v||²)` in physical counting coordinates. Together with an actual fine-action Hessian floor a>0 and penalty b>0 this supplies a period-uniform vertical Hessian gap. For Chapter5 one must identify `e(0,v)` (the forest-lift derivative) with the zero-extended forest direction and use the same predictor Q. The statement does not prove a period-uniform analytic radius or all higher derivative row/column bounds merely from finite-volume IFT. Parent notified; relocation of the deterministic tree argument earlier in the final exposition is an integration decision.
