# Chapter 4 audit: exact blocking and effective densities

Draft `chapters/04-blocking.tex`; reviewed source passages Scott B 19–190, Part I 05 6–190, D 21–67; Martin `predictor-branch.tex` 9–200. No one-step stability or global trajectory is asserted. The output is an exact normalized kernel and a conditional density coordinate system.

## Sources and local proof status

- Frames: Scott `def:D20a`, `def:D20b`, `lem:B1`; Martin `predictor-branch.tex`, uniform uniqueness subsection. Detailed averaging contraction checked: gauge loop test makes all route matrices ε-close to identity; global minimizers satisfy the average squared-distance estimate; center by nearest centroid; inclusive diagonal self term preserves nearest-point optimality; centroid normality kills projection of their difference; derivative bound produces contraction ε+1/4 uniformly over number of sites. The group acts by a common left multiplier, so h_0=1 is a legitimate global gauge normalization and does not remove coordinatewise optimality. Constants depend only on the specified matrix group, not patch radius.
- Axial eligibility: Scott `lem:B1`, axial branch proof; each fixed coordinate order gets a root by successive low-average-layer selection. Internal link differences telescope through internal plaquettes; the induction factor at r varying axes can be 4r(2R+1), giving16 in dimension4. This is a finite-root variant of the standard axial gauge estimate. The short argument is retained because it supplies this exact eligible-root rule; no original exact published theorem was located in the targeted search. No novel-method claim.
- Nearest predictor: Scott `def:D21`, `lem:B1`; completion of squares gives nearest projection of weighted ambient matrix mean. Uniform tubular radius supplies threshold independent of weight count. Predictor tag is uniform over B_R on minimizing branch; otherwise weights w_z^av. Frame tags sampled first; predictor probabilities conditional on frame tags. Boundary equality goes to fallback branch.
- Exact kernel: Scott `def:D04` and B covariance paragraph. All finite alternative branches retained, all q factors Haar normalized. Haar/Fubini normalization given as immediate application, not a separate long proof. Gauge transformations at coarse endpoints are g(Ly); lattice translations are matched fine Ly/coarse y. Kernel Borel, positive and bounded at fixed β, not asserted globally continuous through branch changes. Analytic frame dependence and its derivative are intentionally deferred to Chapter5.

## Literature

Foote1984: parent downloaded original /tmp/ym-foote.pdf and inspected p153 lemma: compact C^k submanifold, k≥2, has unique nearest point in a neighborhood and projection C^{k−1}. Since compact matrix group is smooth, this supplies smooth projection. Derivative at identity is the tangent projection by the standard normal chart. Draft uses no unproved analytic enhancement. Citation key already in Scott bibliography.

Searches before proof: “Balaban averaging operations lattice gauge fields minimizing gauge group average 1985” and “synchronization compact Lie group all pair transports unique minimizer near identity gauge fixing”. Original Bałaban averaging paper identified through Rutgers metadata (CMP98(1985)17–51, DOI10.1007/BF01211042), but exact finite-rule matching not verified. Draft cites existing Balaban1987RG only for historical methodology, not as proof of this kernel or its uniform branches.

## Essential support distinction

Source D25 makes K_i a function of internal links of Y_i AND flags in Y_i. Actual flag decisions read plaquettes meeting those sites, extending distance1 beyond Y_i. Draft calls Y_i exclusion support, I_i^bad prescribed large-field set, and separately defines full dependence region. Covers and K_m weights use Y_i. Connected factor overlap must use full dependence. No independence or disjoint read support is inferred from disjoint Y_i. This correction is also recorded in notation registry and UV audit.

## Effective action and norm conditions

The path action is defined with its coefficient data treated as given and absolutely summable at the fixed volume. Invariant transported curvature rows and masked quadratic/cubic/quartic expressions retain both β-dependent and β-independent parts. Their later matching and uniform kernel bounds are not claimed here. `clip` is discontinuous at threshold, with c_dir/2>c_lin; thresholds are based on reference beta, fixed when actual beta changes. Relaxed tests written over all sites are finite-range in effect because chord≤2; actual local dependence includes every nonautomatic queried plaquette.

Regular norm: ordered left derivatives through fixed q, fields small on X_i (all plaquettes meeting X_i), directions t_m(1+dist(e−,o_i))^varpi. Majorants anchored at o_i. Large-field norm: supremum value, containing-site sum over exclusion support. Both weighted with connected ball-cover number. Draft explicitly requires a conversion estimate for anchors or dependence-support enlargement; no hidden equality of these norms. Countable sums converge at fixed volume by elementary product estimate, without volume-uniform full partition-function claim.

Regular normalization: zero at flat field; first derivative vanishes by Ad(G)-invariance and absence of invariant linear functionals on simple g; affine Hessian vanishes on nonwrapping supports. Wrapping support treatment intentionally follows source condition rather than guessing a coordinate lift. Parameter curves keep addresses/tests/masks fixed, all-address weighted difference sums vanish at fixed volume. Reference coupling differs from actual coupling. The complete reachable admissibility class is deferred until the nonlinear step is proved.

## Remaining work

1. Later chapter must supply path coefficient data and prove both summability and the stated normalization, not merely cite this definition.
2. Later overlap estimates must retain both exclusion and dependence supports under each conversion.
3. Later trajectory construction must check t_m≤1, period/patch geometry and stage-dependent q,varpi,σ. Those are finite-step inputs here.
4. Original exact axial finite-root variant has not been found; a verified applicable published formulation would permit compressing its local proof further.
5. Parent handles full build, visual layout and page-distance reminder check. Chapter4 uses only existing macros plus Foote1984 and Balaban1987RG citation keys.
