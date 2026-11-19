# Independent review: actual finite detector comparison

Reviewed the updated `chapters/11-marked-insertions.tex`, common-extraction, window-covariance, opening higher modes, forced fusion and denominator normalization (2026-11-19). Author UV edited during review; review findings below refer to its final changes communicated to parent.

## Corrections found and addressed

1. Solved lift norm is H^(bd+c_d), not H^c_d. The high engineering-weight remainder still gains rho^−(d+1)=H^−b(d+1), leaving H^(c_d−b) (and the coefficient prefactorH if present), so b>c_d+3 is adequate. Author corrected the actual lift bound. Opening near remainder must use H^(f+bd+c_d−D) and distant term H^(f+bd+c_d)e^−thetaC; author corrected both, choosingU afterbd+c_d andD afterU.
2. Replacing actual coarse conditional background outside a patch by0 is NOT an exact equality. Author added the protected response-path tail CB^a e^−cB g^−1, assigned as a regular remainder. This is smaller than every fixed H^−v because B~(log s)^4 while log(g^−1)=O(log s). The closed zero extension then supplies the local comparison mean, with the tail explicitly accounted for.
3. Denominator comparison originally only asserted3V−3 integrations. Author supplied an explicit axial tree and lexicographic elimination order. I checked it below.

## Checks that passed

Common extraction T:
- Near-support cutoff diameter is O(M²), fits8M²patch. Taylor/axial polynomial construction is linear in the actual inserted function; it need not select linear representatives of individual activities.
- Rescaled p_u(y)=W_u(zy) removes the g/theta axial coefficient, leaving rowO(b). The diagonal Wick covariance becomesz^-2K=O(H^-1); coefficient-l1 norm makes the finite Wick bound independent of ambient coordinate count.
- Positive Wick sign is correct: exp(+Delta_K/2) on polynomial paired against covarianceSigma−K gives originalSigma expectation. Negative diagonal covariance is only a formal polynomial Wick functional, never presented as a probability law.
- Relative half-error T−A yields same-map invertibility and simultaneous real detector lifts; fixed-depth boundedness inN,p suffices. No closeness of interacting projection planes tofreeplanes assumed.

Window covariance:
- Completed inverse curvature multiplier has P−P0=O(|p|), differentiatedjtimesO(|p|^(1−j)); local Fourier remainder therefore decays|x|^−5, with higher differences addingorders. The finite mesh derivative singularity1/|p| is integrable in4D, allowing O((1+|x|)/Nper). Smallestperiod exponentialinscale makes this negligible on fixedpowerH windows.
- Response difference factorization uses boxfilters BEFORE dividing by coarse difference; aliashyperplanes are not crossed by a naked division. Enough smoothingorders and strictwidthreserve are required and stated.
- Row transport bounds imply mean andcoarsecovariance budgets; covariance uses bounded entries ofkappa and rowl1bounds, so no false integrability assumption on the borderline|x|^-4 covariance kernel is needed.
- Exact conditionalcovariance telescoping gives diag−B0 after originalselfcovariance subtraction, correctly retained.
- Common retained jet/residual coordinate system is exact reconstruction; Wick coefficient-l1 recursion controls errors independentofcoordinatecount. It applies to every subset withsamebackground/covariance, so correctedpair coefficients are controlled jointly.

Opening higher modes:
- Weight inequality checks directly: aftercover conversion logratio<=m u0+C0−theta c_C/2, and c_C>=Cm/64 plus64(u0+Gamma+C0)<=Ctheta/2 make it<=−Gamma. It does NOT assume newradius<=oldradius. Thus complete incominghigherfamily survives withsmallbound.
- Forced regrouping retains original/new inventories and jointmodeproducts. This needs actualrestart failedcutoff/site suppression and commonproductbounds; those are now explicitly referenced to restart-family, not inferred from singleton estimates.
- Choose amplificationkappa beforeD-dependentL; q thenD thenL avoids a parametercycle. The lowerwindow lengthlogC=o(logH) supplies its small amplification.

Full denominator:
- Tree edges (x−e_p(x),p(x)),p(x)=highestnonzero coordinate, numberV−1. Remaining3V+1free links.
- For free (x,i), t=max(i,p(x)). Ifi<t, plaquetteatx−e_t in(i,t) has otherfreeedges with lower(t,1_i=t,sumx). Thetwo t-edges aretreeedges. Ifi=t andlinkfree, itwraps; nonretained meansw=x+e_i!=0, j=p(w)<i. Plaquetteatx−e_j in(j,i) has otherfreeedges lowerbyindicator orsum. Fourretained links are exactly(−e_i,i).
- Eachchosenplaquette has unique maximalfreeedge, so chosenplaquettesdistinct and descendingintegration uses a fresh Haar variable exactlyonce. Count3V−3is valid. Remaining4wrappinglinks contribute harmonicloss g^(−4dimG), not an extensive extra gpower.
- Denominator3V+1small-link restriction and numerator3V−3integrations yield logloss2dimGlogbeta dividedby outputcellcount. WithV=q0 andsmallestperiodgrowth this is<=1. Genuine additivevalueerrors cost2Vdelta andmustbeincluded inCstage, as stated.

## Interface boundary

The review verifies deductions conditional on the ACTUAL restarted representation having its stated small additive value error, common joint product bounds, positive coercive action envelope, and protected response-tail bound. Those are supplied by the separate restart-family proposition, being checked by foundations. An arbitrary one-step Gaussian reader with bounded covariance alone would not suffice. No additional internal mathematical error found after the three corrections above. Root should keep the restart-family reference explicit in the final finite-detector theorem and its proof.

No chapter edits by reviewer, no global build.
