# Complete coarse-trial residual and bounded approximations

Implemented in `13-bounded-approximations.tex`, label `ch13:coarse-residual-supplier`.

## Exact source match

- Martin/existence/actual-phase-grid-approximants.tex, marked discrepancy subsection: source weight w=ζ_m a_m^d exp((τ_h−τ_m)/8)/(2E_h), intermediate weights t_i=w product φ, backward cone bound, adjacent upper/lower comparison, original-law coefficient expansion, final root exp(site cost+5)/w.
- Martin/existence/actual-phase-detector-moments.tex, lemma c14-selected-phase-reflection: the positive intermediate insertion modifies only the regular singleton in the whole nilpotent exponential; all ordinary/flagged higher arrays are retained. This supplies the exact two-stage density representation, not merely a singleton response.
- Martin/existence/selected-centered-service.tex 117–123 gives u_i=βhat_i^(-1/2)/4 and δ_i=βhat_(i+1)^(-2); 1893–1911 gives ζ, φ, δ and δφ exp(B/128)>=1; 2645–2670 identifies the actual comparison constant with a fixed local-section derivative bound, distinguishing it from the exponentially small forced allowance.

## Additional explicit payment written in the book

A single jump by exp(τ_h/8) at h is unnecessary and was not justified by the previous paragraph. Choose heights satisfying all finite local and adjacent costs, then t_i/t_(i+1)=φ_i^-1 <= exp(B_i/128). For any existing higher mode with r distinct ancestors, B_i r<=64c_B(X), so the change of marker weights costs at most half one spare support unit:

    φ_i^(-r) exp(-c_B(X)) <= exp(-c_B(X)/2).

The second reserve unit and the exact original component inventories are retained in Chapter11's higher-mode induction. This estimate is uniform in cardinality/period and applies above as well as below the intermediate insertion. Heights have inverse polynomial coupling cost at fixed stage; adjacent-stage entry delays bound their ratios and the incidence allowance, so φ exists before the history is used. There is no need for a uniform-in-h fixed source weight.

The original-law coefficient after insertion is the subset sum of pushed negative products times positive coarse factors. Disjoint full ancestor cones give the product of pullback discrepancies, including shared frame random variables in each cone. The normalized integral has singleton costs 2+1 and higher costs 2, hence +5 per cell. This proves the exact residual estimate used by the bounded approximation proposition.

Removed the explicit unproved-residual qualification and proposition's assumption of it. Kept the specified schedule requests, room requirement, ordered limits, and dependence of approximation thresholds on each fixed pair. No claim of cutoff thresholds uniform over all copy numbers.

Validation: check_draft.py resolves all explicit labels; no global compilation performed by this agent.

Independent-review refinement: reweight on the incoming fine support, using B_i<=B_(i+1) and B_(i+1)r<=64c_(B_(i+1))(X). Explicit full exponents A_i satisfy 10·15^4(A_i+9)<=L_i(A_(i+1)−4); four reserved incoming units absorb weight/site/attachment costs and cover contraction restores the full outgoing exponent. There is no accumulated reserve loss. The scalar trial part is an exact global exponential unit entry; only the guarded nonconstant part is described as having zero complementary profile.
