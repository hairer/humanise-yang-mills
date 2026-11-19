# Chapter 8 audit

## Scope

Draft of abstract polymer tools, not a proof of the actual gauge-theory step. Does not assume or assert the selected Wilson family has the required activity estimates. The completed chapter may need a concise norm-translation subsection once Chapter 4 is written.

## Sources inspected

- Scott Outline III.5, especially III.5.1–6: finite logarithm, rooted estimates, deletion, forced attachments.
- Martin `existence/cluster-expansion.tex`, `eq:cluster-vertex-input`, `eq:cluster-local-tail`, `eq:cluster-marked-size`: exact support hypotheses and factorial conventions.
- UV specification U6: connected activities and forced coverage.
- Ueltschi, arXiv math-ph/0304003v3, full HTML §2 Theorem 1, equations (3)–(4), inspected. This is the theorem used instead of reproving rooted tree combinatorics. Kotecký–Preiss original bibliographic metadata checked; original theorem pages not inspected in this pass.

## Checked application

Write w=|z|, inflate each activity to w exp(alpha c)/q, and use KP exponent delta c. The incompatibility sum is at most q^(-1)|X| gamma <= delta c(X), using h gamma <= q delta. Finite volume plus nonempty supports ensures total weighted activity summability. The rooted bound then controls the sum of all clusters hitting x with weights q^(-n) by gamma/q: choose an occurrence containing x, replace 1/n! by 1/(n-1)!, and sum the root. For n>=k restore q^n<=q^k to get gamma q^(k-1). Union support weights are bounded by product support weights because a nonzero connected coefficient has an overlap spanning tree. This proves the stronger tail displayed in the draft as an immediate application of the existing theorem; no new cluster theorem is claimed.

Martin uses q0=4h gamma/delta and obtains gamma q^m/(1-q). That sufficient condition implies the draft's criterion, so the cited abstract theorem can replace this repetitive combinatorial proof. This observation does not remove any source-specific activity hypothesis. Rooted tuples permit repeated labels; gas families do not.

## Additional checks

Independent review by the continuum writer confirmed the inflated-activity criterion, all factorials, union-weight inequality and the stronger tail on 19 November 2026.

The deletion identity follows by subtracting absolutely convergent series. Real positivity is a conclusion, not a premise. Cauchy differentiation requires uniform bounds on complex parameter neighbourhoods; the text says so. The large-field reassembly formula is stated for overlap incompatibility and fixed large-field configuration; it does not assert product factorization of clusters meeting multiple supports or convergence of an uncontrolled forced sum. The final support discussion was corrected after inspecting Scott D25: exact covering supports can be smaller than full link-dependence supports because boundary flags inspect adjacent plaquettes. The abstract overlap criterion does not assert independence of activity random variables.

## Still to integrate

Map Chapter 4's precise anchored and unanchored norms to the site norm, including any support enlargement for eligibility tests. Specify exactly which scalar and forced activity bounds Chapter 9 supplies. Confirm the final book's symbol registry reserves alpha, delta and gamma_0 only locally here. No source-specific missing estimate is declared solved by this chapter.
