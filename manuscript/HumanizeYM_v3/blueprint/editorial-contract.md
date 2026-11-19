# Editorial and mathematical contract

This file applies to every chapter. Read it together with the chapter specification and `notation.md`; no other chapter need be read in full. Source paths are relative to the workspace root, not to this directory.

## Audience and length

Write for a mathematical researcher familiar with probability, analysis, and the aims of constructive QFT. Explain the mathematical role of each construction before its technical definition. Cite standard arguments rather than reproducing textbook proofs. Target approximately 440 pages including references and notation, with a hard editorial ceiling of 500. A chapter's allocation is a ceiling for its completed exposition, not a request to pad a draft.

## Status of assertions

Distinguish (1) definitions, (2) standard results imported with an accurate citation and checked hypotheses, (3) source-specific results whose argument has been checked, and (4) conditional statements whose source-specific input still requires verification. An outline saying “theorem” is not itself a proof. Conversely, a local lemma being conditional does not show that its hypotheses are unavailable elsewhere. Trace suppliers through the final assembly and record the exact matching problem.

Do not call an argument verified merely because its formal counterpart is reported to compile. This project has the supplied informal manuscripts and outline; it has not independently checked the Lean development. Keep provenance claims attributed. Do not silently import a result from the alternative coordinated Wilson family into the selected family.

For each source-specific theorem, record in a chapter audit: source labels; hypotheses and quantifiers; constants and their dependence; the common lattice family and refinement used; proof status; literature search; and any remaining obligation. A failure to find an older proof is not a priority claim.

## Terminology

Use familiar mathematical language: local observable, polynomial jet, polymer activity, connected correlation, weighted norm, large-field region, small-field domain, stationary background, coupling adjustment, renormalization trajectory, reference scale, coefficient transfer, phase, spectral measure, Ward identity. Avoid the sources' financial and organizational metaphors. A translation is valid only after stating the exact mathematical object; “uniform estimate” cannot replace an unspecified inequality.

Do not use code names in the running exposition. Keep Lean names, source-specific jargon and supplier chains in the blueprint/audit only. Nonstandard but essential mathematical constructions require an explicit definition and a plain-language explanation.

## Definitions and reminders

Introduce every nonstandard symbol before first use, including symbols in theorem statements. Avoid a global catalogue of technical definitions before motivation. Reserve global names according to `notation.md`; use chapter-local symbols for disposable auxiliary objects.

After a symbol has been unused for more than three or four typeset pages, add a short reminder or definition reference at its next use. Check this against the compiled PDF, not source-line distance. Repeat the meaning of the scale indices at the start of every multiscale chapter. Remind readers which state (mixed or a phase) a correlation belongs to.

## Dependency discipline

Prove local analytic statements under explicit finite-scale assumptions before choosing a global trajectory. Put the simultaneous choice of constants and scales after the inequalities it must satisfy. Distinguish a definition of a global construction from its existence.

The ultraviolet limit is the full spacing limit at fixed volume; volume extraction comes afterwards. Compactness supplies subsequences and does not prove convergence along all ultraviolet cutoffs. Every final conclusion must concern the same selected Wilson family. Refining a sequence preserves proved limits, but changing a family, normalization, or trajectory requires a separate comparison theorem.

Place the free Maxwell calculations before their use in rank and stress-tensor arguments. Coordinate reflection spaces may precede continuous rotations. Full rotational covariance, phase disintegration, and relativistic reconstruction must follow the actual hypothesis dependencies, not the source's part numbering.

## Proof and literature policy

Before adding a proof, search original literature for the statement and its needed variant. Record an exact theorem/section where possible. If the argument is standard or an immediate adaptation, give the statement, cite it, and explain how the hypotheses match; do not reprove it. A related historical paper is not a substitute for the needed estimate. In particular, a perturbative beta-function calculation does not establish a uniform nonperturbative block-step error bound, and reflection positivity alone does not give the complete reconstruction theorem.

Use original publications for attribution, with an accessible author/institutional copy when available. Preserve a distinction between bibliographic metadata checked online, full statement inspected, and applicability established. Do not copy the full source bibliography into the book indiscriminately.

## Scope of the final theorem

Keep explicit: no mass gap is established; no uniqueness of the infinite-volume limit or independence of block penalty is asserted; the lattice limit is the mixed state; reconstruction concerns phases; the trace asymptotic is in a selected phase. The operator product expansion is a remainder estimate at each finite degree, not convergence of an infinite series. Contact extensions are constructed after separated limits, and do not automatically inherit positivity or contact Ward identities. Excluding finite Wick profiles does not exclude all generalized free fields.

## Chapter delivery

Deliver a LaTeX chapter, an audit note, and any new bibliography entries. Use ordinary `definition`, `lemma`, `proposition`, `theorem`, and `remark` environments; prefix labels by chapter number. Do not edit another writer's chapter or global macros without coordination. Give the editor concrete unresolved questions with source references rather than a generic request for verification.

Before accepting a chapter: verify definitions, common conventions, citation applicability, cross-references, quantifier order, page budget, and the long-gap notation reminders. A clean LaTeX build checks typesetting, not mathematics.
