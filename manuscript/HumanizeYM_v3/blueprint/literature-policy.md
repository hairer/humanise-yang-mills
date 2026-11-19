# Literature verification ledger

This ledger distinguishes checking a reference from checking that its hypotheses apply. Chapter audit files supply the theorem-specific entries. The bibliography in the source manuscripts is a starting list, not a list of verified dependencies.

## Verified mathematical input for the polymer chapter

**Ueltschi (2004), “Cluster expansions and correlation functions,” Moscow Mathematical Journal 4, 511–522.** Full statement inspected in the [author's arXiv text, version 3](https://arxiv.org/html/math-ph/0304003v3), §2, Theorem 1, equations (3)–(4). It supplies the exponential cluster identity and absolute rooted bound for a complex activity measure, under the weighted incompatibility criterion. The hard-core case uses the interaction −1 on incompatible pairs and 0 otherwise. The extra integrability condition is automatic for a finite volume under a finite site sum and nonempty supports. This is an appropriate citation in place of reproving tree combinatorics. Theorem 3 concerns decay of correlations; its applicability to the source's marked observables must be checked separately.

**Kotecký–Preiss (1986), “Cluster expansion for abstract polymer models,” Communications in Mathematical Physics 103, 491–498.** Original attribution, [DOI 10.1007/BF01211762](https://doi.org/10.1007/BF01211762). Publication metadata verified; use Ueltschi's explicitly inspected statement for the exact rooted estimate in the present conventions. Martin cites the original theorem on pp. 492–493. Do not claim to have inspected those pages in this pass.

The weighted geometric tail used in Martin `existence/cluster-expansion.tex`, `eq:cluster-local-tail`, can be obtained by applying the rooted bound after multiplying activities by a support weight and an activity-count parameter greater than one. This is a standard adaptation, not a new cluster-expansion proof. Its application still requires a site sum for the **actual** activities; no abstract convergence theorem supplies that input.

## Source attribution not independently verified online

The supplied outlines identify a Lean development at commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`. An attempt to open the repository URL through the browser search tool returned a cache miss. This neither disproves the reference nor verifies its contents. Attribute the formal-verification claims to the supplied manuscripts; do not claim this project has independently run the kernel or checked the formal-to-informal correspondence.

## Required ledger entry for each future proof

Record: intended proposition; search terms and original sources inspected; exact theorem/section; matching hypotheses; whether the result is imported, immediately adapted, or proved here; and any mismatch still requiring an argument. Full-text access failure is recorded explicitly. A bibliographic abstract or a title alone cannot validate the precise hypothesis needed in the book.
