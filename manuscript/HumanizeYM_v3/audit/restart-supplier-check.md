# Check of the restarted comparison and the uniform difference supplier

Checked against the supplied Martin sources, 2026-11-18. This note follows a particular implication chain. It independently checks the displayed algebra, quantifier changes and object identifications described below; it does **not** certify the primitive covariance, stationary-background or nonlinear RG estimates.

**Conclusion.** Martin contains a detailed route addressing Trish's conditional Gaussian-comparison caveat, including later replacement arguments that are easy to miss: a joint guarded Gaussian lemma, a stronger support-exponent construction, the complete opening polynomial, and an application to the selected chart. The final detector/absorption argument uses finite-cutoff ranks and estimates, so it does not require continuum rank to prove uniform difference bounds. The remaining verification boundary is the actual local Gaussian/energy/room hypotheses and their simultaneous supply by the selected schedule. No contradiction or definitive global gap has been established by this check.

All filenames abbreviate Martin/existence/. Labels are stable locators; line numbers refer to the supplied snapshot.

## 1. Objects that must remain identical

Fix the selected history, cutoff \(N\), volume \(p\), and comparison level \(k\). The original insertion family is fixed before comparison. Its complete unnormalized marked density at cutoff \(N\) is \(q_N\); its actual push to level \(k\) is \(q_k\). In general \(q_k\) contains higher connected modes and is not the unmarked density multiplied by singleton insertions.

The comparison restarts **below \(k\)** with constant actual coupling \(\beta_{N,p,k}\). The clock parameters \(x_i=\widehat\beta_i\) still vary with \(i\). The paths, clips, adjacent quadratic data and installed block geometry are retained. The restarted activities are newly constructed and need not equal the original lower-level activities.

At each step, the exact identity pushes the genuine incoming density. The neutral representation deletes only its additive remainder and is used in estimates. That deletion leaves unchanged the Gaussian precision and affine mean built from path, clip, coupling, field, forest, tag and store. It does change the interacting density. This distinction is explicit in actual-local-compiler-handoff.tex, proof of lem:actual-neutral-warning (257–321).

The invariant across normalized block-kernel sequences is every coefficient integral, including the empty coefficient, not equality of lower-level densities. The common denominator remains the original Wilson partition function.

## 2. Endpoint re-expression: stronger suppression

Source: restarted-rank-history.tex, endpoint construction (211), prop:restart-endpoint (243).

There are **two different slow functions**:
\[
H_s=e^{(\log\log s)^2},\qquad h_s=e^{(\log\log s)^{3/2}}.
\]
The original threshold/radius are \(t=s^{-1/2}H_s\), \(M=\lceil(\log s)^2\rceil\); the restarted ones are \(\tau=s^{-1/2}h_s\), \(B=M^2\). Thus \(2\tau\le t\) eventually. This is not a notational variant of one threshold.

For the piecewise clipped term \(d_t\), the source uses
\[
\Delta(r)=d_t(r)-d_\tau(r)\ge0,\qquad
\Delta(r)\ge c_{\rm lin}\tau^2\quad(r>\tau).
\]
The ranges check directly. For \(\tau<r\le t\),
\(\Delta(r)=c_{\rm dir}r^2/2-c_{\rm lin}\tau r\ge(c_{\rm dir}/2-c_{\rm lin})r^2\ge c_{\rm lin}\tau^2\), under \(c_{\rm lin}<c_{\rm dir}/16\). For \(r>t\), \(\Delta(r)=c_{\rm lin}(t-\tau)r\ge c_{\rm lin}\tau^2\). Allocating among at most five touched sites gives a positive charge per newly flagged site.

The theorem assumes original path coefficient bounds, \(s/2\le\beta\le2s\), loop bound \(2H_s\), additive allowance \(s^{-11/10}\), and original large-field allowance \(e^{-H_s^{1/5}}\). It preserves the coupling/scalar/path data and obtains allowance \(G(s)=e^{-a_0h_s^2}\), with \(0<a_0\le c_{\rm lin}/20\). The changed masks and exact new inventories must be kept; this is not monotonicity of the old polymer norm.

**Checked:** clipping arithmetic and threshold hierarchy. **Not independently checked:** all path-tail and connected-component estimates in the endpoint proof; the explicit construction is present.

## 3. Closure on the actual restarted history

Source: restarted-rank-history.tex, prop:restart-actual-closure (564), proof 581–742; actual-local-compiler-handoff.tex (399–404).

The coupling match is quantitative. The clock gives \(3s/4\le x_i\le s\), while \(|\beta_{N,p,k}-s|\le s/8\). Consequently
\[
x_i/2\le\beta_{N,p,k}\le2x_i.
\]
Indeed \(x_i/2\le s/2<7s/8\), and \(2x_i\ge3s/2>9s/8\). A constant actual coupling meets the adjacent-coupling drift condition with difference zero.

The original paths/clips/tubes and their diagonal identities, metric floors and row bounds do not involve the additive/forced coefficients. Neutralization therefore preserves them. The genuine additive cost is only a **value** cost; it need not meet the smaller derivative allowance of the original calendar.

For \(y=\log\log s\), put
\[
A_s=e^{y^3},\quad q_n=s^{-1/200}A_s^{4n},\quad
\omega_n=q_nA_s,\quad\delta_n=q_nA_s^3.
\]
The window length satisfies \(n\le h\le y^4\) eventually. For fixed \(r\),
\[
\log(q_nA_s^r)\le-\tfrac1{200}\log s+(4y^4+r)y^3
\le-\tfrac1{400}\log s
\]
eventually, since \(\log s=e^y\). Also
\[
s^{-1/200}+16\delta_n\le17\delta_n\le A_s\delta_n=q_{n+1}
\]
when \(A_s\ge17\). These inequalities close the displayed short-interval value recurrence.

The loop/cubic/quartic path correction has weighted value bound
\[
\beta e^{7a}C_c\tau_x^3+\beta e^{9a}C_c\tau_x^4+e^{5a}\Gamma_c\tau_x^2.
\]
With \(\beta\le4x\), \(\tau_x=x^{-1/2}e^{(\log\log x)^{3/2}}\), and \(\Gamma_c\le2e^{(\log\log x)^2}\), this is \(x^{-1/2+o(1)}\), hence eventually at most \(s^{-1/200}\) uniformly for \(x\in[s/2,s]\). The additional requirement \(a/B_c\le\sigma_c\) is eventual for a fixed positive path rate.

The large-field inflation is paid by actual energy. The proof takes the larger forced multiplier \(\max(G(x_i)^{-2},G(x_{i+1})^{-1})\). Its bound \(\log m\le4a_{\rm coast}\operatorname{hot}(x_{i+1})^2\), together with \(2a_{\rm coast}\le K/4\), leaves at least half the energy exponent \(K\operatorname{hot}^2\). The analytic inputs remain the actual energy bound and a **single joint Gaussian tail event**, not multiplied marginal probabilities.

**Checked:** bands, value recurrence, path-correction scaling and inflation arithmetic. **Retained hypotheses:** positive compatible tubes, full support inventories, actual energy/tail estimates, exact all-hole identities and fixed raw-exponent purchases.

## 4. Support reserve at construction time

Source: allarity-marked-propagation.tex, prop:allarity-compiler-reserve (2062).

The upper comparison needs \(e_*=e+1+\sigma\), \(0<\sigma\le1\), before returning to exponent \(e\). The source fixes
\[
E=e+2,\qquad \widehat E=E+8,\qquad\alpha\ge8T_E.
\]
The raw connected expansion uses \(E\); local support estimates use \(\widehat E\). The mixed expansion requires cover charge \(E+7\), leaving one reserve. The fine-to-coarse inequality
\[
10\cdot15^4(E+7)\le L\sigma_f
\]
must be imposed **before \(L\) is fixed**. Increasing the coupling cannot fix an insufficient block ratio.

After construction, \(e_*\le E\) makes every nonnegative weighted majorant at \(e_*\) bounded by its value at \(E\). Likewise \(\max(1,H^{q-3})\) bounds every needed multiplier \(l(z)\), \(z\in[H^{-q},H^{-4}]\). Thus one alphabet and its original identities serve both uses. Constructing separate alphabets would not establish the claimed compatibility.

**Checked:** exponent and multiplier matching. The proposition retains the local handoff's analytic hypotheses; restarted closure supplies history-specific inherited-law and small-remainder conditions. These can be read as a conditional local theorem followed by its application, rather than an automatic circularity. The upstream local estimates remain separate.

## 5. Joint Gaussian comparison: the later guarded route

An earlier sufficient criterion (M), around line 1030 of allarity-marked-propagation.tex, demands a common cutoff-weighted chart measure and jet identities. Ordinary Gaussian marginal equality is insufficient. But (M) is **not an undischarged necessity for the entire argument**: a later route expressly bypasses it.

The replacement is lem:allarity-guarded-gaussian (1266), applied through lem:allarity-pair-reader (1415) and the following attachment. For each sector/tag \(t\), all polynomial factors use one probability space, one centered joint Gaussian array \(\eta_t\), and the same mean \(a\). Individual guards obey
\[
|C_t-C_*|\le\epsilon,\quad
\int(1-\Gamma_{t,I})\,d\mu_t\le\epsilon^2,\quad
|\xi_{t,I}-a-\eta_t|\le\epsilon\ \text{on }\Gamma_{t,I}>0.
\]
Every polynomial is invariant under the allowed patch gauge. The same mixture weights, nonnegative and summing to one, apply to every partition and the empty product. The empty expectation is one.

The proof checks without independence of guards. For a partition with \(\ell\) factors,
\[
1-\prod_I\Gamma_{t,I}\le\sum_I(1-\Gamma_{t,I}),\qquad
\mathbb E(1-\prod_I\Gamma_{t,I})\le\ell\epsilon^2.
\]
Telescoping monomials bounds the physical-coordinate replacement by \(\epsilon\) times a Gaussian moment polynomial. Cauchy–Schwarz removes the product guard at cost \(\sqrt\ell\,\epsilon\). Wick pairing compares covariance entries. At fixed polynomial degree and coefficient \(\ell^1\) norm, constants do not grow with unused coordinates. The finite marker logarithm is a polynomial in these moments with unit constant coefficient. This proves the finite-arity discrepancy conditional on the joint-law input.

The proposed actual supplier in actual-reader-dawn-selection.tex uses actual-to-flat covariance error \(x^{-1/8}\), short-row tail \(p_x=x^{-1/8}\), physical error \(x^{-1/32}\), and guard loss \(x^{-1}\). For fixed \(f\), these are bounded by \(H^{-f}\) or \(H^{-2f}\) as required, uniformly for \(x\in[s/2,s]\), since \((\log\log s)^2=o(\log s)\). At a stage boundary, the pair-reader lemma uses the minimum strip width, maximum bounds and **fine metric floor**, while retaining distinct metrics in
\[
(DI_F)A_F^{-1}(DI_F)^{\mathsf T}=P_f-JP_cJ^{\mathsf T}.
\]

The same reference-forest/tag scalar is extracted before choosing marks: actual-corrected-body-compiler.tex, eq:actual-body-loading (278). Its eq:actual-body-density (327) identifies the genuine integrand. A wholly leading component contains no body letter and no compatible background packet; it is a product of guarded principal values on the common Gaussian/Haar probability space. This identifies the component, not the entire interacting density as a Gaussian.

**Checked:** the guarded comparison proof, the scale conversion, and the explicit distinction between scalar loading and probability law. **Remaining:** the actual mean/covariance/guard estimates, their room assumptions, and all cross-entry identities have not been independently rederived.

## 6. Higher modes and the original denominator

Source: allarity-marked-propagation.tex, lem:allarity-selected-opening (2615), prop:allarity-selected-application (2704).

The opening lemma starts from the complete \(q_k\). It invokes the earlier mixed-grade finite-menu expansion, then a stronger support norm to suppress higher modes at small marker weight. The joint endpoint expansion retains original eligibility tests, old/new inventories and full modes. Every forced component contains a newly flagged-site factor \(X_z\); after reserving one factor \(G(s)\), the stated remainder sum satisfies
\(G(s)(e^{r_s}-1)\le G(s)\)
when \(r_s\le H^{-1}\), \(Z(B)r_s\le1\), and \(H\) is large. A small singleton error alone would not prove this.

The last paragraph of the selected application contains an important exact identity. For prescribed reference cumulants \(D_c^{\rm ref}\), set
\[
J=\exp_*(-\sum_cD_c^{\rm ref}).
\]
The corrected density is \(Jq_N\), whose push to \(k\) is \(Jq_k\): \(J\) is field independent and each block map is linear on the finite coefficient algebra. Multiplying by the *whole invoice* would double-count the insertions. Since \(J\)'s empty coefficient is one, the unmarked density and original partition denominator remain unchanged.

**Checked:** coefficientwise push identity and the distinction between \(q_k\) and a singleton product. **Not rederived:** the upstream weighted mixed-grade bounds making \(r_s\) small. Their source is the proof preceding eq:trace-original-marked-payment and eq:trace-endpoint-marked-budget in trace-firesky-gallery.tex, not the final marked-output estimate itself.

## 7. Root normalization and finite detectors

rank-root-normalization.tex retains the finite-volume correction. Tree gauge leaves \(3V+1\) links; plaquette elimination integrates \(3V-3\) factors. Division leaves four powers of \(g^{-\dim G}\):
\[
\frac{z|\int f|}{Z_R}\le e^{VP_R(X)-4(\dim G)\log g}.
\]
With \(q\) replica cells and coefficient weight \(a^{q|I|}\), the root is at most
\[
a^{-|I|}\exp\{P_R(X)-4(\dim G)\log g/q\}.
\]
For \(a=e^{2I_k}\), this is \(\le e^{-I_k}\) if the entire exponent is at most \(I_k\). The harmonic correction is not discarded.

prop:rank-root-output-ticket (308) buys this at the **output** stage, possibly different from the reading stage. The request
\(1+\sqrt{16M\max(T_M(\pi_i),0)}\le1+\log\log\widehat\beta_k\)
gives \(T_M(\pi_{J(w(k))})\le I_k\) after squaring. Output lawfulness is separate: actual-rank-purchases.tex, prop:rank-trace-output-lawful (1323) and cor:rank-trace-all-levels (1440).

The lift calculation is finite dimensional. Common maps satisfy
\[
|Av-Tv|\le\tfrac12|Av|,\qquad |v|\le D_k|Av|.
\]
Hence \(T\) is invertible and \(|T^{-1}|\le2D_k\). The **same** \(T\) solves all columns' equations \(S_tTu_i=W_\rho v_i\). The resulting bound \(B_k\) depends on \(k\) but not \(N,p\), as needed.

fullmesh-fixedbounds-producer.tex, lem:fullmesh-uniform-detector (367), uses a finite-cutoff estimate. Although eq:rank-purchased-point-comparison is displayed after extraction in actual-rank-purchases.tex, its preceding paragraphs expressly give the root bound for all sufficiently large \(N\) and every \(p\), before extraction. The detector therefore does not strengthen a merely ordered-limit claim.

Bounded projections with the finite equation kernel already exist before extraction: finite-rank-kernel-transport.tex (9–45) constructs a projection using a fixed Euclidean inner product and averages over finite symmetries. Each average still kills the same subspace and differs from the identity by a map into it; these two properties imply idempotence. Its norm is uniform in the varying subspace. The rank is the finite free-quotient rank by an exact calibrated isomorphism, not a continuum rank theorem.

For a fixed injective free matrix \(G\), if \(|c|\le K|Gc|\) and each entry of \(Q-G\) is less than \(1/(2Kr)\), then \(|c|\le2K|Qc|\). Bounded lifted columns/projections give \(|\Pi_i v|\le Z|L_i\Pi_i v|\). Constants are independent of \(N,p\) once one comparison level is fixed.

Averaged differences satisfy the exact identity
\[
\frac1h\sum_{j=0}^{h-1}
\frac{H(x+(j+1)e)-H(x+je)}{a_N}
=\frac{H(x+he)-H(x)}{ha_N}.
\]
With \(h=\lceil b/a_N\rceil\), each averaged derivative costs at most \(2/b\), using undifferentiated bounds. The positional modulus used to average detector positions is attributed to the earlier transfer/Schatten argument, not the derivative estimate being proved.

**Checked:** normalizer factors, inversion/detector algebra, special projection averaging and telescoping. **Remaining:** primitive centered-root and positional-modulus estimates with their support assumptions.

## 8. Final absorption and its independent inputs

Source: fullmesh-fixedbounds-producer.tex, prop:fullmesh-selected-supplier (496).

Encoding gives \(x_i\) and vanishing root error \(E_i=O(x_i)-D_lF_i\). The assay satisfies \(|L_ix_i|\le c\). Set \(y_i=\Pi_ix_i\) and
\[
z_i=(1+|y_i|)^{-1}(x_i-y_i).
\]
The source checks \(z_i\) is uniformly subpower in calibrated coordinates: its first term is a bounded scalar times a subpower row; the second is bounded by one. Its projected kernel is zero. Microscopic equation comparison gives \(|L_iz_i|\to0\) uniformly in \(p\). Eventually it is at most \(1/(2Z)\), so
\[
|y_i|\le Zc+\tfrac12(1+|y_i|),\qquad |y_i|\le2Zc+1.
\]
Thus \(y_i\) has a primary root budget. The exact identity
\(D_lF_i=O(y_i)+O(x_i-y_i)-E_i\)
gives the difference bound. Finitely many orientations can be included before taking maxima. No limit of \(\Pi_i\) is needed.

The microscopic equation insertion vanishes **before limits** against the product of distant reflected copies. A fixed physical cell and sufficiently small \(a_N\) give the required distance outside a fixed finite microscopic stencil uniformly in \(p\), since the smallest physical period is positive. An ordered spectator limit would not justify this uniform sweep.

This checks the last implication conditional on the actual encoding, equation-column discrepancy, primary root budget and positional-modulus inputs. Their separate suppliers are actual-equation-kernel-relay.tex, actual-insertion-derivative-relay.tex, cor:ex-c02-uniform-census, and the directional part of ex-centered-producers. **The restart theorem alone does not supply all of these.**

## 9. Concrete writing consequences

1. Present three inputs before the finite detector: common restarted Gaussian comparison; exact microscopic equation comparison; primary centered bounds and positional modulus. Then give absorption.
2. Use the later guarded-value proof for finite rank. Do not impose the earlier common-cutoff jet criterion (M) unless a later derivative argument needs it.
3. Define the two thresholds, two radii and stronger support exponent before use; these are real representation changes.
4. Keep the genuine density identity beside the neutral estimates, explaining why neutralization leaves the Gaussian law unchanged.
5. Include \(Jq_N\mapsto Jq_k\) and the unit coefficient of \(J\). This makes the denominator claim explicit.
6. Do not advertise the numerical and finite-dimensional checks here as verification of the full construction. The local analytic supplier audit remains unfinished.
