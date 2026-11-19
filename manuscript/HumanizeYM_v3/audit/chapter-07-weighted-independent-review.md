# Independent review: Chapter7 weighted and vertex bounds

Reviewed current `07-matching.tex`, especially `ch07:integrand-input`, `ch07:weighted`, centered quotient, and inherited loop argument. No Chapter7 edits by this reviewer.

## Checks that passed

- Actual centered change `r=r_root-Ru` matches Chapter5's exact `Q=M+d_cR`. The centered scalar gauge insertion is the smoothed mean, with unitary Bloch coefficient mu² m_l. The principal m_l is bounded below at fixed smoothing order on the real coarse cube. The triangular internal linear change has determinant one.
- A weighted unit internal fine direction has normalized residue L² norm O(mu) and normalized first-difference norm O(mu²): Euclidean norms are respectively ≤mu^-1 and O(1), and normalized counting contributes L^-2=mu². External smooth legs have the corresponding supremum powers by `ch05:actual-bridge`.
- The local weight-four argument supplies the necessary leading Wilson response for the specified action class (direct curvature energy, path-row squares, and curvature-degree≥3 atoms). Kinetic normalization H(0)=I fixes the weight-four coefficient. Each extra transported-field factor/derivative increases weight. Thus after two internal and n background derivatives the difference from Wilson has combined momentum order≥3−n, n≤2. Exponential true-path-length bounds control the differentiated remainder uniformly; no period factor is needed.
- First kinetic insertion has at least one coordinate difference, obtained from the zero constant coefficient by coordinate division; second insertion needs none. The count `(n+2)+number of differences=4` gives normalized factor mu⁴ with two internal L² legs and external supremum legs, canceled by the L⁴ anchor sum. This checks the stated power, provided division is applied to the actual left-coordinate response, as the chapter specifies.
- Radial integrand bounds are dimensionally consistent. Denominator error is O(T³)+O(mu²), first insertion error is O(T²)+O(mu²/T), inverse factors are O(T^-2). Two external momentum derivatives of the telescoped bubble therefore give O(T^-3+mu² T^-6). Local seagull contributes O(T^-2); regulator seagull contributes O(mu² T^-6). Both fit the asserted annular remainder, without invoking a seagull cancellation. The ball T≈mu costs O(mu^-4), compensated by its four-dimensional volume.
- Regulator denominator floor `x+mu²(mu²/(x+mu²))^9 >= 2^-10(x+mu²)` is valid by splitting x≤mu² and x≥mu². First/second background regulator responses have sizes mu²/T and mu²/T². Differentiating in external momentum in the scaled norm retains these powers.
- The centered frame equation is algebraically correct: writing F=Pi J0+S and imposing the weighted centering gives `F=Pi1−sum omega Pi S+S`. At flat background E−1=0 and D(P−Pi)(1)=0, so the next derivative depends on lower frame derivatives. With at most two internal slots, products require only L∞,L²,L¹; averaged coordinate reads have bounded multiplicity on endpoint-pair space. The domination omega≤C_j nu follows from w≤L^-4 and O_j(L⁴) patch size.
- Quotient coercivity is correct at the linear algebra level: gauge away nonprincipal longitudinal aliases, remove the centered scalar by the principal scalar alias, control nonprincipal transverse modes by curvature, then control the remaining principal vector with the least singular value c_j mu of M's principal coefficient. The same argument includes zero coarse momentum. Uniform bounds for the smoothed scalar mean require its alias row norm, supplied by the centered-box decay, not just an individual alias estimate.
- Freezing the weights at a real coarse momentum while retaining the analytic block transform is a valid way to use holomorphic perturbation. A coarse displacement of fixed size changes q((p+2pi l)/L) by O(mu), and h_l≥mu. This avoids differentiating nonholomorphic weights.
- Inherited-loop gain is checked: four vanishing link-momentum orders can be divided into two differences per leg on a smaller strip; each leg is O(L^-3), and the fine anchor sum L⁴ leaves L^-2. The actual transport's gradient correction is annihilated by the insertion's Ward identities. Nonprincipal alias contributions retain order four because their transverse transport is O(p²); no ratio-uniform inverse of an individual alias is needed for this order statement.

## Clarification sent to author

The trace paragraph says the regulator mu² factor pays “both the L² frame derivative and the two weighted-to-Euclidean conversions.” These are **different terms**, not three simultaneous losses:

- `m_mu X`: the Euclidean output norm of X is O(mu^-2), absorbed by the trace norm O(mu²) of m_mu.
- `P_f* M_mu P_f`: the two conversions cost mu^-1 each, absorbed by that same power mu² in this separate term.

An interpretation that multiplies all three losses would leave mu^-2 and would be false. The author was asked to make the termwise allocation explicit. The available estimates support the separate allocations.

## Precise remaining classical stationary-jet issue

Chapter5's actual stationary graph plus the path budget gives period-uniform fixed-L local jets, actual tangent identification, and a smooth representative with pre-L difference bounds. It does **not by itself** give ratio-uniform stationary Taylor coefficients of orders3/4: its tree gap and supremum inverse may deteriorate with L.

To derive those stronger coefficients, use the stationary chain identities

- `E'''(0)=f'''(0)[W,W,W]`;
- `E''''(0)=f''''(0)[W,W,W,W] − sum_(3 pairings) B_ij H_vert^-1 B_kl`, where `B_ij=f'''(0)[W_i,W_j,·]` on the vertical space.

The exchange terms require (a) ratio-uniform compatible dual weighted bounds for B, (b) a ratio-uniform inverse on those gauge-annihilating functionals, and (c) translation/exponential kernel estimates for the complete contractions. The new completed quotient/inverse and vertex estimates in Chapter7 are plausible suppliers for (a)/(b), but they must actually be applied to these contractions; they cannot be replaced by citing the fixed-L Chapter5 implicit-function theorem. Common infinite-lattice coefficients are also required to turn finite-volume local jets into the exact periodized strip kernels used by classical matching. Parent and Chapter7 author were notified.

No incorrect radial exponent or centering sign was found. This review checks the displayed power/norm mechanisms; it does not certify the full infinite RG trajectory or eliminate the incoming path-budget/coefficient compatibility conditions.

## Follow-up: the classical-jet gap was closed in the revised chapter

The author added `ch07:classical-uniform` and `ch07:uniform-stationary-jets` with the missing stationary contractions. The gauge-annihilation argument checks: differentiate `D_z S[R(v,z)a]=0` twice along full stationary tangents. The terms involving derivatives of R vanish by tangent orthogonality `D²S[T,(0,z)]=0`, and DS(0)=0 removes the last term. Thus B annihilates gauge directions. For C=H+F*F and Cw=B, pairing with R a gives `<FR a,Fw>=0`; surjectivity of FR implies Fw=0 and hence Hw=B. The completed inverse therefore gives the same exchange pairing as the forest inverse. The weighted vertex and inverse bounds now give the pre-L cubic/quartic contractions; the common complex strip and exact periodized Fourier matrices give the required common kernels. This addresses the earlier issue, rather than merely citing Chapter5.

The added classical-budget gain also checks. It compares actual fine vertices with Wilson vertices on the **same** actual tangents and inverse, so no estimate for an inverse difference is required. Higher incoming coefficients do not alter that inverse once the quadratic metric/predictor data are fixed. Weight≥5 of the fine-action difference gives two differences in its cubic vertex and one in its quartic vertex. For the dual cubic remainder, differences on the one internal leg can be transferred to the two external legs by exact momentum conservation; at most two differences are required on an external leg. Their actual smooth bounds give P(A)/L. Expanding the exchange pairing into its baseline and delta-B terms yields the stated fixed-stage constant plus P_stage(A)/L, with the squared remainder absorbed into the polynomial. The baseline includes the block penalty and depends only on fixed Gaussian/predictor data. This conclusion requires A to denote the remaining nonlinear incoming budget, excluding changes to those fixed quadratic data, as the revised text states.
