# Shared notation and terminology

## Status and use

This is the notation contract for the proposed monograph, drawn from Scott and Trish `part1/notation-index.tex`, their definitions and macros, and Martin `existence/symbolic-index.tex`. It fixes common names; a row does not assert existence of its object. Define each object in its owning chapter before using it. When a nonstandard symbol returns after three to four pages, write a short reminder or definition reference. Add a notation paragraph at every chapter entry listing only symbols that chapter actually uses. Local auxiliary symbols may be introduced if their scope ends with the subsection and they do not shadow reserved global symbols.

Source locators below use Scott labels unless marked M for Martin. A chapter writer need only open the named source file and search the label. The registry is intentionally not copied wholesale into the opening chapter. The printed book should have a short notation index at the back and local definition reminders in the text.

## Global conventions and collision repairs

- Coordinates are `x=(x₁,x₂,x₃,x₄)=(bold x,t)`; time is coordinate 4. Translate Martin's axes 0,1,2,3. Euclidean inner products are positive; Minkowski square is t²−|bold x|². Complex Hilbert inner products are antilinear in the first variable.
- `R_p` is the physical period (Scott L_p, Martin P_p). `L_m` is the odd blocking ratio (Scott ℓ_m). `s` or `s_{m,p}=R_pD_m` is an integer number of sites per side; `s_m` is **not** used for logarithmic scale in the monograph. Use `τ_m=log D_m`. A generic fixed ratio may be L.
- `b>0` is the block-kernel penalty, not the coupling, the one-loop coefficient or a basis vector. Use `b_{d,i}` only with both indices for label basis vectors. `β` is inverse bare/effective coupling; `b₀` is the one-loop coefficient; `κ_G=2b₀` is the inverse-coupling logarithmic slope.
- `μ_{N,p}` means the Wilson probability only. Use `δ^{F²}_{N,p}` for the additive unit counterterm of F² (Trish's repair of Scott's μ collision). Phase measure is ν and trace spectral measure is μ_Θ.
- `S` and `S_n` denote continuum correlations, never a lattice action. Use `E_s^W` for the Wilson energy and `V_ρ` for the effective action.
- `a_m` is always a spacing. Rename Martin's local quadratic/cubic/quartic coefficient arrays as `A_m^{(2)},A_m^{(3)},A_m^{(4)}`. `A_μ` is a connection component; in Gaussian sections use `K` for the kinetic operator, `Q` for linear block averaging and `C` or `Γ` for covariance, after giving their spaces. A localized approximate covariance is not necessarily the inverse of the original precision.
- `N_fac` is factor-count operator (Scott mathsf N); N without subscript is a cutoff index. `d` is scaling-dimension cutoff; `d_g` is dimension of the Lie algebra. A filtration index d bounds the scaling dimension and fixes the insertion normalization.
- Reserve `mathcal H` for Hilbert spaces, `H₄` for signed coordinate permutations and `mathcal D` for the common operator domain. `Ξ` is phase space, ξ a character and ξ_* selected phase. Do not use X for phase space because X is polymer support.
- Reserve `mathsf Z_{N,p,d}` for terminal coefficient maps and `Z_{s,β}` for partition functions. Reserve `mathscr U_{k,d}` for scaling maps and `U(g)` for relativistic unitaries; `U_e` remains a lattice link variable.

## Lattice geometry and gauge theory

| Symbol | Definition/type | First definition; source |
|---|---|---|
| G, n_G, g | Fixed closed subgroup of U(n_G), matrix dimension, real Lie algebra | Ch. 1; `part1/02-definitions.tex`, def:D01 |
| \(\lVert A\rVert_G\) | Normalized matrix norm, \(\lVert A\rVert_G^2=n_G^{-1}\sum_{i,j}\lvert A_{ij}\rvert^2\). All unitary matrices have norm one. | Ch. 1, `ch01:matrix-norm` |
| `<X,Y>_g` | `−Re tr(XY)/n_G` on g | same |
| d_g, C_g | `dim_R g`; adjoint Casimir in that metric | same; C_g=2n² for defining SU(n) |
| b₀, κ_G | `11C_g/(48π²)`, `11C_g/(24π²)` | same; coefficient's RG role later |
| H₄, h | Group of signed coordinate permutation matrices, an element | Ch. 1; Scott conventions / Outline I.1.2 |
| e_μ | Coordinate unit vector, μ=1,…,4 | Ch. 1 |
| Λ_s, E_s | `(Z/sZ)^4`, positively oriented links | Ch. 1; M lattice.tex ex-lattice |
| r_s(y), hat y | Centered representative; physical point a_N r_s(y) | Ch. 1; eq:I12-physical-placement |
| dist_s(x,y) | Periodic sup distance in lattice units | Ch. 1; Outline I.1.1 |
| U_e, U_{y;μν}, U_γ | Link variable, plaquette product, ordered path transport | Ch. 1; def:D02 |
| \(\lVert u-v\rVert_G\) | Distance between group elements, invariant under left and right translations. A plaquette of holonomy \(u\) has Wilson energy \(\tfrac12\lVert u-1\rVert_G^2=1-n_G^{-1}\operatorname{Re}\operatorname{tr}u\). | Ch. 1, `ch01:matrix-norm` and `ch01:wilson-energy`; source `eq:I12-price-chord` |
| E_s^W, Z_{s,β}, μ_{s,β} | Wilson energy, partition function, law | Ch. 1; def:D02 |
| D_m, a_m, τ_m | Cumulative denominator, D_m⁻¹, log D_m | Ch. 1; eq:I12-levels |
| L_m, R_p, s_{m,p} | Odd ratio; physical period; R_pD_m sites per side | Ch. 1; eq:I12-levels; Outline I.1.3 |
| N, m, p, j | Fine cutoff; RG level; volume index; regularity stage | Ch. 1 / RG; always identify which varies |
| Θ_μ, θ_μ | Reflection of configurations; antilinear pullback on observables | Ch. 1; M eq:ex-lattice-reflection-pullback |
| `||F||_{cb,T}` | Chessboard seminorm for specified tiling T | Ch. 1; exact reflected/conjugated product convention required |
| B_R(x), cov_B(X) | Periodic sup ball; minimum number of radius-B balls with connected union covering X | Polymer chapter; def:D05b / Outline I.1.4 |
| Σ_d, Σ_v | Fixed finite stencil of a local section or insertion | Ch. 2; def:D19, def:Q1 |
| X_i,Y_i,o_i | Regular support, large-field exclusion/coverage support, anchor | Polymer chapter; eq:I12-representation; D24–D25 |
| Y_i^read | Full link-dependence region: internal links plus links queried by flags and extra tests | Chapter 4; Scott D25; can extend distance one beyond Y_i |

## Labels, representatives and normalized insertions

| Symbol | Definition/type | First definition; source |
|---|---|---|
| J, J_{≤d} | Formal radial jets, finite truncation through scaling dimension d | Ch. 2; def:D07 |
| A_{k,μ} | Homogeneous radial potential of polynomial degree k+1 | Ch. 2; coordinates have scaling dimension k+2 |
| V_d | Ad(G)-invariant jet polynomials of scaling dimension ≤d | Ch. 2; def:D07 |
| b_{d,i}, (w_i,f_i) | Nested real bihomogeneous basis, scaling dimension (also called weight) and factor count | Ch. 2; Outline II.1.1 |
| N_fac, t^{N_fac} | Count operator; b_{d,i}↦t^{f_i}b_{d,i} | Ch. 2; sec:local-fields |
| sc_h J | Jet scaling with h^{k+2} on A_k | Ch. 2; eq:I12-test-holonomy |
| U(h,J) | Exact link holonomies of truncated smooth test connection | Ch. 2; eq:I12-test-holonomy |
| Tay_d | Taylor expansion in jet variables, weight truncated at d | Ch. 2; sec:A-labels |
| P_d^loc[c] | Polynomial finite-stencil right inverse of Tay_d | Ch. 2; lem:A1; M local-sections.tex |
| c_{F²}, P^cl | `¼Σ_{μν}<F_{μν},F_{μν}>`; clover representative | Ch. 2; sec:A-example |
| T=⊔_d V_d, v=(d,c) | Insertion labels with filtration index d | Ch. 2, then transfer chapter; sec:local-fields |
| r(d) | Chosen reference RG level of degree-d fields | Transfer chapter; Scott m_ref(d) |
| mathsf Z_{N,p,d} | Invertible map: fine coefficient → reference-level coefficient | Transfer chapter; def:D08, lem:E2.1a |
| I_{N,p}(v,y;U) | `a_N^{-d} P_d^loc[t_N^{-N_fac} mathsf Z_{N,p,d}^{-1} c](y;U)` | Transfer chapter; def:D08 |
| u_d | `a_{r(d)}^d 1`; produces unit insertion for N≥r(d) | Transfer chapter; def:D08 |
| λ^{F²}_{N,p}, δ^{F²}_{N,p} | Multiplicative and additive coefficients of Z⁻¹ c_{F²} | Transfer chapter; Trish sec:A-example |
| x_m, R^{reg}_{m,i}, Q^{lf}_{m,i} | Transferred coefficient and regular/large-field inserted remainders | Transfer chapter; eq:I12-marked-representation |
| I_d^eq, R_d^eq | Free equation ideal and triangular label change for exact lattice equations | Comparison chapter; Scott mathcal I_d, mathsf R_d; lem:A-R4 |

## Renormalization group

| Symbol | Definition/type | Source |
|---|---|---|
| b, bar β | Fixed soft-block penalty; common endpoint inverse coupling | sec:block-map, sec:trajectories |
| J_m, q_j, varpi_j, σ_j | Stage, derivative order, spatial power, support exponent | sec:constants; not interchangeable with scale m |
| hat β_m | `bar β+κ_G τ_m` reference coupling | eq:I12-scales |
| M_m^cut | `exp[(log log hat β_m)²]` | eq:I12-scales |
| t_m | `hat β_m^{-1/2} M_m^cut` plaquette threshold | eq:I12-scales |
| B_m | `ceil[(log hat β_m)²]` support-weight radius | eq:I12-scales-b |
| ε_m^reg, ε_m^lf | `hat β_m^{-11/10}`, `exp[-(M_m^cut)^{1/5}]` | eq:I12-scales-b; lf replaces for |
| mathfrak B_m | `[hat β_m/2,2hat β_m]` coupling band | sec:block-map |
| β_{N,p,m}, β_{N,p} | Trajectory coupling at m; bare value at N | prop:MT |
| Y_{e,z}, Q_e^pred, w_z^av | Framed connector; gauge-covariant block average; normalized averaging weights | eq:I12-framed-connector, eq:I12-predictor |
| α_tag, λ^tag(U,α_tag) | Auxiliary discrete branch choice and probability | eq:I12-tag-mass |
| q_γ(u) | Haar-normalized density proportional to \(\exp[-\tfrac{\gamma}{2}\lVert u-1\rVert_G^2]\) | def:D04 |
| k^{(m)}_β, B^{(m)}_β | Normalized block kernel, exact density integration map m+1→m | def:D04 |
| Bad_m(U) | Sites incident to a plaquette with \(\lVert U_\square-1\rVert_G>t_m\) | sec:density; Scott Flag |
| E_i^reg, K_i^lf | Small-field local correction; large-field polymer activity | eq:I12-forced-eligibility |
| I_i^bad | Exactly prescribed nonempty set Bad_m(U)∩Y_i | same; not a field insertion |
| mathfrak F_m(U) | Disjoint polymer families exactly covering Bad_m(U) | def:D06 |
| ρ, v_sc, V_ρ, dens(ρ) | Density coordinate tuple, scalar normalization, effective action, density | def:D06 |
| P^{path}_{N,m} | Gauge-invariant action in transported curvature variables | eq:I12-path-action |
| χ^{rel}_{m,x}, clip_t | Relaxed small-field test; piecewise action bound | eq:I12-clipping; clip has a jump, not a smooth cutoff |
| D^L_A, `||F||_{m,o,X}` | Left link derivative and local seminorm with specified derivative list | def:D05a |
| E_m(ρ), K_m(ρ) | Weighted regular and large-field activity sums | def:D05b |
| A_{N,m,p}, R_{N,m,p} | Admissible coordinate class; admissible adjacent-cutoff pairs | sec:density |
| Q_m, C_m | Precision/Hessian and covariance on an explicitly specified slice | Gaussian chapter; do not conflate with positive localized C |
| W_0, W_ax | Free interpolation and axial tangent map | subsec:B-free, subsec:B-stationary |
| mathsf C_μ, mathsf G_μ | Source's gauge-completed Hessian and ghost operator | subsec:B-inverse; may rename to Q_μ,Q_μ^gh locally |

## Correlations, continuum fields and comparison

| Symbol | Definition/type | Source |
|---|---|---|
| M^{lat}_{N,p}, C^{lat}_{N,p} | Unsmeared product moment; joint-test Riemann sum | def:D03 |
| Conf_n, sep_∞ | Pairwise-distinct configurations; minimum sup separation | sec:families |
| Gen_n, NoHit_{R,n} | Coordinatewise generic/separated domains | sec:uv-limit; never replace by Conf_n without proof |
| Δ_h^α, ∂^α | Finite differences with denominators; continuum derivatives | sec:uv-limit |
| M^{UV}_{p,v}, C_p^{UV}(v;f) | Fixed-volume kernel; its smeared value | prop:UV, def:D09 |
| P=p_seq∘q_seq | Retained volume-index map; no field polynomial meaning | prop:IV |
| S_n, S, S^ξ | Mixed correlations, family thereof, phase correlations | def:E1-E3, prop:PH |
| N_d(S), F_d | All-spectator null subspace of V_d; V_d/N_d(S) | def:D10 |
| iota_d, L_fields | Correlation-response embedding; span of images | def:D10; mathcal L in Scott |
| j_{d,e}, ∂_μ | Field inclusion and field derivative, proved from correlations | prop:FC; not naïve polynomial inclusion |
| 1_d, F_tag | Class [u_d]; disjoint union of degree-tagged quotient spaces | sec:field-spaces |
| M_d^Max, S^Max, Γ | Free Maxwell quotient fields, correlations, covariance | def:D11 |
| \(\mathcal S_j,\langle P,Q\rangle_j\) | Homogeneous degree-\(j\) Maxwell solution jets. Sum the Lie algebra inner products of corresponding coefficients over all ordered indices, including both orders of the antisymmetric index pair. | Ch. 3, `ch03:shell` and `ch03:strict` |
| mathscr U_{k,d}, r_k | Short-distance comparison maps and scale sequence | def:D12 |
| T^Max_{μν}, T_{μν} | Free Maxwell stress tensor; Ward-normalized interacting tensor | prop:ST |
| P_ν^J, Y_K^J, χ_shell | Translation flux, angular flux, smooth annular cutoff | def:D13; J here tensor, not jet space |
| R_d(O), L_d(K) | O(4) action and infinitesimal rotation action on fields | prop:ST |

## Phases, reconstruction and operator products

| Symbol | Definition/type | Source |
|---|---|---|
| H_μ^OS, mathcal H_μ^OS, Ω_μ^OS, P_μ^0 | Coordinate energy, reflection Hilbert space, vacuum, zero-energy projection | def:D14 |
| B_h(w), M^0(w), A₀ | Slab insertion operator, vacuum compression, commutative compression C*-algebra | def:compression |
| Ξ, ν, ξ_* | Spectrum of compression algebra, full-support probability, chosen character | prop:PH |
| mathcal H_ξ, mathcal D_ξ, Ω_ξ, Φ_ξ | Reconstructed space, common invariant dense domain, vacuum, operator fields | def:D14a, prop:RC |
| T_ξ(z), E_ξ, U_ξ(g), ρ_lab(g) | Unitary translations, joint spectral measure, Poincaré representation, label action | def:D14a |
| H_ξ, J_ξ^OS | Energy and isometric Euclidean/relativistic comparison | prop:RC |
| V_+, overline V_+, Poinc | Open/closed future cones; proper orthochronous Poincaré group | sec:wightman-defs |
| W_n^ξ, F_n^ξ | Boundary Wightman distribution; ordered-time analytic continuation | def:D15 and reconstruction chapter |
| Θ, G_Θ(r), A_G | Selected-phase centered trace; radial two-point function; `3d_g/π⁴` | def:D16, prop:TR |
| μ_Θ, hat f_+ | Trace spectral measure; Fourier transform with declared sign | after prop:TR |
| O_{F²}, d₂ | Curvature-square field; trace comparison coefficient | after prop:TR |
| W_Wick | Finite sum of finite products of free mass-shell Laplace kernels | def:D17; narrow comparison class |
| ζ | State index in Ξ disjoint-union {mix} | def:D18 |
| A,B (bold) | Cluster and spectator lists of fields with specified filtration indices | def:D18 |
| `|A|_deg` | Sum of normalization indices of clustered fields | def:D18 |
| Ch_j, O_{j,λ}, c_{j,λ} | Finite channel index, basis field, OPE coefficient | defs:D31–D33; Part II J |
| R_D^ζ | Correlation remainder at finite truncation D | def:D18, prop:OP |
| δ_sp, η, M_geo | Spectator clearance, internal scaled separation, cluster size parameter | def:D18; restate quantifiers |
| mathfrak D_A^ζ | Distributional contact extension of separated correlations | prop:CT; not a lattice limit at collisions |

## Terminology translation and restrictions

| Source wording | Monograph wording or precise definition |
|---|---|
| token, label | polynomial label with specified filtration index; distinguish from quotient field |
| table | family of Schwinger functions / correlation kernels |
| healthy/unhealthy | small-field / large-field configuration on the stated support |
| flag / inventory | large-field site / prescribed set of large-field sites |
| forced activity | large-field polymer activity constrained to cover specified sites |
| test | Test function for smearing a distribution. For a cutoff inequality, finite parameter evaluation, or correlation pairing, specify the condition or pairing. |
| higher modes (in the source variables) | Terms involving two or more insertions, indexed by the source monomial. |
| replicated root norm | Chessboard seminorm for a reflected tiling. State the product moment directly for other arrangements of copies. |
| primary source | Normalized local insertion, with its local polynomial coefficient when expressed in the chosen basis. |
| receipt, payment, price, budget | explicit estimate, bound, allowed norm bound, or constant; print the inequality |
| readout | coefficient-extraction map (or terminal coefficient map, if that is the actual map) |
| mark / marked density | observable insertion / density with specified insertions |
| rank purchase | rank or nondegeneracy estimate, with its matrix and norm specified |
| frame | local gauge choice, basis, or scaling map, according to type; never leave ambiguous |
| horizon / calendar / course / history | finite range or reference scale / scale schedule / RG trajectory; inspect actual definition |
| shell flux | integral of a conserved-current correlation against an annular cutoff derivative |
| all-shot, all-arity | uniform over every finite number of insertions, with dependence stated |
| contact extension | distribution extending a kernel from the complement of collision diagonals |

Do not translate a source metaphor by guessing: its domain, codomain, quantifiers and estimates determine its meaning. Distinguish support roles: large-field activities depend on internal links of Y_i **and flags in Y_i**; evaluating flags reads plaquettes within distance one beyond Y_i. Exact covers and the stated large-field norm use Y_i, while connected-expansion overlap graphs use full dependence regions Y_i^read. Disjoint exclusion supports may have overlapping dependence regions. Any conversion between these support conventions requires its own geometry and norm estimate. 'Phase' here means a character in the constructed compression algebra; do not assume uniqueness, lattice realizability, or equivalence to an extremal DLR state. 'Non-free' must specify the excluded finite Wick-profile class; the two-point trace law alone does not exclude generalized free fields.

## Mandatory consistency checks

1. Same G representation and trace normalization throughout; every β or Casimir formula matches them.
2. At level m the integer period is R_pD_m and physical spacing a_m; blocking decreases m.
3. Unit label in V_d is 1, but normalized degree-d unit coefficient is a_{r(d)}^d1.
4. Distinguish scaling dimension, factor count and filtration index whenever transferring a label.
5. Record all constant dependencies: group, b, fixed degree/arity, derivative order, separation, but never silently N or p in a uniform estimate.
6. Do not turn pointwise-in-degree estimates into uniform-in-degree OPE convergence.
7. A common family and common volume refinement must be maintained through later constructions.
8. Separate Hilbert-space field-null relations from equality of formal polynomials and from Maxwell equation ideals.
9. Give the actual Fourier convention when introducing it; no global convention is guessed from a symbol.
10. In the final page audit search each chapter for unused-for-four-pages notation and add brief definition pointers; a back index alone does not satisfy the reminder rule.


## Implemented late-chapter notation (19 November revision)

These names supersede shorthand in the planning tables where they differ. Definitions occur in the indicated book labels.

| Symbol | Type and scope | Book definition |
|---|---|---|
| I_d (calligraphic) | Degree-d invariant polynomial ideal vanishing on Maxwell solution jets | ch02:equation-section |
| V_d (calligraphic) | Equation-adapted finite-stencil section, distinct from polynomial space V_d | ch02:equation-adapted |
| R_d (bare) | Triangular automorphism of polynomial labels for exact microscopic equations; distinguished from rotation R_d(K) by its domain and lack of group argument | ch02:equation-adapted |
| P_{N,p,d} | Near-identity comparison of the two microscopic sections on one actual history | ch11:equation-comparison |
| E_{N,p,d} (mathsf) | Actual moving equation subspace in reference coordinates, including factor scaling | ch11:actual-equation-subspace |
| M(w), mathfrak A | Whole-word compression and its commutative C*-algebra; replaces M^0/A_0 shorthand | ch15:compression |
| B_h(w), B_epsilon(A) | Width-h word insertion; in Chapter16 only, centered singleton in width 2epsilon | ch14:slab-bound; ch16:slabs |
| mathsf F_n^xi, mathcal W_n^xi | Ordered complex-time function and full spacetime tube function | ch16:heat-function; ch16:full-tube |
| rho_Theta | Positive trace spectral measure (mu_Theta in early planning table) | ch17:spectral-pairing |
| U_{i,d}, beta_i, b_i | Prescribed-radius comparison map, actual insertion-level coupling, reference coupling | ch17:radii |
| e_i, q_i | Trace stability amplification and coefficient growth bounds, M_i^(1/5), M_i^(1/6); local to Chapter17 | ch17:stability |
| rho(x,y,z) | Finite-dimensional trace functional -2x-8y; not a probability density | ch17:rho |
| E_j, Q_j, O_{j,a} | Fixed invariant degree summand, its projection, and basis for OPE/contact prescriptions | ch18:graded |
| rho(x), a_h(x), T_{h,k}, mathcal W | Smooth minimum-distance scale, nearest-pair weights, normal Taylor operator, contact subtraction | ch18:pair-weights--ch18:subtraction |

The Chapter18 contact prescription now uses the invariant summands E_j for one consistent multilinear family across degree inclusions. Its conservative Taylor order is k+1 with k+1>P for the established separated-kernel exponent P. It is distinct from the unverified sharper source forest prescription. The selected phase remains xi_* and the mixed family S is never silently replaced by S^xi_*.


## Additional local notation in the integrated proof

| Symbol | Meaning and scope | Book definition |
|---|---|---|
| H(x), h(x), r(x) | Original and reduced cutoff amplitudes, and recording-scale change; r is not a physical radius in this subsection | ch11:restart-construction |
| D_k (mathscr), sigma_k | Actual restarted density and its scalar normalization; its integral is the original partition function | ch11:restart-density |
| T, S_t, W_rho | Common polynomial extraction, factor-count dilation, scaling-dimension dilation; in comparison sections T is not the stress tensor | ch11:common-extraction; ch11:simultaneous-detector-lifts |
| R_I, G_I, omega | Corrected subset source, free subset moment, and source amplitude in the fixed-arity squarefree algebra | ch11:n-mark-comparison |
| zeta_i, phi_i, omega_i^res | Small singleton allowance, adjacent source-weight ratio, and residual source weight | ch13:coarse-residual-supplier |
| A_i, mathscr A_h | Full support exponent in the residual induction; separately, the complete pushed source polynomial at h | ch13:coarse-residual-supplier |
| J_h, E_h, Q_h | Coarse trial coefficient matrix, complete trial bound, ordinary small-field trial bound | ch13:coarse-matrix |
| P_{N,h} (calligraphic) | Pullback of a bounded coarse observable by the forward probability kernel, retaining all frame/randomness dependencies | ch13:cone-factorization |
| mathcal P_D | Fixed-probe reconstruction of a local cluster into F_D, before phase or rotation averaging | ch18:mixed-replacement (placed in Chapter13) |
| varpi, phi_l, Xi_l, y_{t,l} | Residual weight, its adjacent ratio, subpower extraction allowance and degree-t attachment allowance; local to the cluster proof | ch18:residual-weights (placed in Chapter13) |
| K_0,K_a,K_a^t | Mass-one current anchor average, component average and difference primitive | ch17:block-identities |
| mathcal E_b, e_r, bar e_{m,r} | Current conservation defect, weighted field-order norm, and logarithmically normalized norm | ch17:defect-four; ch17:unnormalized-defect |
| R_f,R_0,d_V | Actual predictor differential, coarse-vertex gauge correction, and coarse infinitesimal gauge action | ch17:actual-current-map |

The residual marker weight is written omega_i^res, never t_i: t_i is already reserved for the small-field threshold used in local sections. Likewise the complete polynomial mathscr A_h is not the numerical support exponent A_h. Remind the reader of these types when reusing them in later subsections.


## Trace comparison and marked-current additions

| Symbol | Meaning and scope | Book definition |
|---|---|---|
| mathscr L_j, J_i | Stage-j block ratio and the stage J(i+1) used in the i-to-i+1 step | ch17:variable-windows; ch10:schedule |
| epsilon_j | log(2+C_j)/log(mathscr L_j), where C_j is fixed before the ratio is selected | ch17:window-product |
| H_n, M_n | exp((log log beta-hat_n)^2), the same large small-field multiplier in the trace comparison | ch17:radii; ch17:variable-windows |
| D_Y k (calligraphic) | Haar divergence of the outgoing block kernel times the smooth current displacement; a density-valued insertion | ch17:kernel-divergence |
| P_5, P_(5,t) (calligraphic) | Scaling-dimension-five extraction and its factor-count threshold normalization | ch17:marked-rates |
| Sigma_k, j_k | Nonclassical marked current coefficient and coefficient of current divergence; the complete zero-moment coefficient is Sigma_k−beta j_k | ch17:finite-sigma |
| v_i^eq | beta_i^(-1) Sigma_(k_i)−j_i, the approximate equation direction in the finite-dimensional vector space | ch17:marked-rates |

In this chapter the scale index n is never the arity; fixed arity is N_*. The smooth gauge-fixed response W_s and the actual forest-coordinate response W_a must be distinguished. Polynomial transport is proved for W_s; using it for W_a requires the gauge-coordinate comparison. A remainder of high scaling dimension may still have field degree two; never infer an extra threshold factor from scaling dimension alone.
