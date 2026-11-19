# Foundations: literature checks (18 November 2026)

## Checked sources

- **Wilson1974**: APS publisher page, https://journals.aps.org/prd/abstract/10.1103/PhysRevD.10.2445. Verified title, author, journal/volume/page/year and abstract describing gauge-invariant lattice quantization. Full article not inspected (publisher access restriction). Suitable attribution for Wilson action and formulation, not for any continuum-existence statement.
- **OsterwalderSeiler1978**: publisher search record, https://www.sciencedirect.com/science/article/pii/0003491678900398. Verified title, authors, Annals of Physics 110 (1978), pp. 440–471 and abstract's assertion of physical positivity of lattice approximations. Direct page access returned 403 and DOI route failed. No exact theorem number or full finite-torus hypothesis verification is claimed. The source manuscript's restricted gauge-invariant/interior-support theorem is at Martin `existence/lattice.tex`, `prop:ex-lattice-finite-reflection`, lines 182–191; both site and link cuts are specified at lines 98–105. Before final acceptance compare these domains to the original statement or Seiler's book.
- **FrohlichIsraelLiebSimon1978**: original author-hosted paper identified at https://www.math.caltech.edu/SimonPapers/93.pdf; search record verifies CMP 62 (1978), pp. 1–34. Direct PDF fetch returned 502. An institutional original preprint is https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1978-1980/P_78_224/P_78_224.pdf. Manuscript citation points to §4, Theorems 4.1–4.2. Exact multi-reflection and complex-conjugation conventions remain to check; do not use a metadata check as proof of a chessboard variant.
- **Seiler1982**: bibliographic entry supplied by Scott, LNP 159 chapter pp. 3–98, DOI 10.1007/3-540-11559-5_2. Manuscript locators §2a, Theorems 2.1–2.2. Not independently inspected in this pass.

## Proof decisions

Gauge invariance is a standard consequence of endpoint covariance and Haar invariance, covered by the lattice literature; state the transformation formula and cite instead of reproducing cancellation algebra. Compactness/positivity of the partition integral requires only a sentence, not a formal lemma proof. Reflection positivity and chessboard estimates are standard imports, but match cut and support restrictions before final theorem use.

The specific finite-stencil, weighted-Taylor right inverse with a lower bound on curvature factor count is provided by Scott `lem:A1` and Martin `existence/local-sections.tex`. Its analytic inverse-function step is standard; that does not make the entire gauge-covariant sampler construction a cited theorem. A dedicated search for a prior exact local-section statement is still required before drafting its proof. Scott cites **Rudin1976**, Theorem 9.24 for the inverse function theorem and **Teschl2012** for analytic ODE dependence; those general analytic results should be invoked, not reproved.

None of these checks independently verifies the claimed four-dimensional continuum construction or the linked Lean repository.

## Local-section search

Searched “lattice gauge local observables radial gauge jets polynomial sections curvature plaquette invariant polynomials” and “lattice gauge theory local polynomial curvature observables Taylor jets inverse function theorem plaquette”. Results found recent expositions of this same construction and general lattice-observable literature, but no prior original publication establishing the exact finite-stencil right inverse with factor-count control. These negative search results are not a novelty claim. For a first draft, retain the short source-specific sampler argument, invoking standard analytic ODE and inverse-function theorems without reproving them; mark its applicability as locally checked against the supplied sources. Do not cite secondary webpages as original sources for the construction.


## Update 19 November: FILS full statement inspected

The parent fetched the original institutional preprint (/tmp/ym-fils.pdf; extracted /tmp/ym-fils.txt). Read abstract Theorem4.1 and proof, then4.2–4.3. Arbitrary2n slots are allowed. The Chapter1 macro-strip adaptation matches cyclicity, involutive local reflection and reflection Schwarz using its finite-torus RP input; repeat across four axes. See chapters-01-02.md update. This supersedes the earlier failed-fetch status for FILS, but does not supersede the still-pending original Osterwalder–Seiler finite-torus applicability check.

Follow-up access check during Chapters12–13: Springer chapter PDF route for Seiler1982 redirects to subscription page; Elsevier original PDF is still403. The original OS lattice theorem applicability check remains a recorded literature-access limitation. No claim of full-text inspection added. FILS original preprint inspection remains valid as above.
