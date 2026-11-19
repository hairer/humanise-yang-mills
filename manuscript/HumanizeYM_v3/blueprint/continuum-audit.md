# Continuum source audit and unresolved verification tasks

Date: 18 November 2026. This is a targeted editorial/dependency audit, not a full independent verification of the proof or the linked Lean development. Read alongside `continuum-chapters.md`. Source paths below are workspace-relative; chapter IDs C1–C8 are stable even if numbered differently in the final book.

## Findings that change the exposition

1. The Outline's eight parts are not a logical order. Free strict reflected Gram positivity is used for ultraviolet/interacting ranks; move independent free theory C1 before those uses. Coordinate OS spaces and slab operators precede rotations; rotations precede spatial invariance of the ground space and phase decomposition. Reconstruction/locality precedes upgrading a.e. vacuum uniqueness to every phase.
2. The repeated reflected-word bound is listed with OPE (Outline VII.4), but depends on lattice reflection/chessboard estimates and is needed long before the OPE. Put its proof in C2, then slabs in C3. This avoids an apparent circular dependence.
3. Ward/spectral analysis uses an elementary two-point contact extension before the final contact theorem. `Martin/existence/physical-ward-stress-cone.tex:19–87` constructs it by Taylor subtraction, arranges tensor symmetries and cancels low divergence jets. It does not assume collision positivity. State this local auxiliary construction in C3; do not forward-reference the final OPE contact prescription.
4. The kernels have full mesh convergence at fixed volume, then only subsequential volume convergence. Coefficient projections may be extracted along additional cutoff subsequences without changing the full-mesh kernel theorem. Keep these two sorts of extraction distinct.
5. The main observable limit is the mixture. The trace law is in a selected phase. Every phase is reconstructed with a unique vacuum, but the mixture need not have one. Polynomial heat decay does not imply a mass gap.

## Audit register

| ID | Evidence and status | Required action before unconditional prose |
|---|---|---|
| C-A1 | Trish `part2/F-infinite-volume.tex:7–9` explicitly retains upstream inputs: higher-marker support propagation/restart exponent 98; same-sample guarded Gaussian comparison including scalar/forced terms and exact density/coupling identification for restarts; actual marked graph-operator continuity. Scott F lacks that paragraph. | Do not assume Scott's shorter version closes these. Trace hypotheses into Martin's candidate closure results, in particular `restarted-rank-history.tex`, `prop:restart-actual-closure` at 564 (proof 581–742), and `actual-local-compiler-handoff.tex:399–404`. The UV audit must decide whether the exact selected family, density, coupling, supports, and all required norms agree. This is a verification task, not an established global mathematical gap. |
| C-A2 | Trish `part2/G-section.tex` opening explicitly retains actual equation/projection/inclusion/difference/rank estimates. Outline IV.1's derivative theorem is conditional on an additional dimension comparison. | Cite precise UV outputs for both rank inequalities; no dimension equality follows just from an approximate derivative formula. `Scott/part2/F-infinite-volume.tex:102–148` gives the assembly argument. |
| C-A3 | Outline IV.1 raw extraction is subsequential in both indices; its limitation points to III.13, an alternative coordinated family. Scott F instead starts from full fixed-volume kernels. | Use the full fixed-volume supplier for the chosen family, not an unidentified alternative-family theorem. Compare Martin `assembly.tex`, `ex-full-mesh` and `thm:ex-construction-assembly`, with `prop:fullmesh-selected-supplier`. Full mesh convergence is an extra premise in the elementary identification lemma. |
| C-A4 | Outline VI.1 warns that supporting flux/contact analysis was not fully checked. Martin provides a substantial conservation argument. | Check diagonal conservation estimates separately from reflection-parity estimates, and check their use before rotation invariance or spectral cone support. Verify the early Taylor correction preserves all claimed tensor symmetries. |
| C-A5 | Outline VI.2 imports invariant spanning, bounded-order detection, Lorentz/Casimir facts; VII.1 imports Fourier uniformity. | C1 should prove or cite each free input once. In C3 verify that the actual comparison is uniform for bounded tests and not only pointwise; narrow coordinate strips and moving insertion maps need stronger estimates. |
| C-A6 | Phase reflection and null-space equality do not follow from abstract character decomposition. Trish H expands the relevant operator/moment argument. | Preserve positivity of the compressed whole-word Gram operator and all-copy moment bounds. Do not replace it by a rank-one product of individual compressed words. Verify same-table corrected detectors in every phase. |
| C-A7 | C5's no-exceptional-phase argument uses locality and positive cone spectrum to prove `O(u^2)` low-energy mass, then phase continuity/full support. | Keep the full zero-energy projection Q until the final argument identifies it with the vacuum line. Do not assume the result while deriving the heat estimate. |
| C-A8 | Outline VII.6 provides prescribed-radii weak comparisons but explicitly does not assert compatibility across degrees/stress normalization by itself. | Match its estimates to the stronger moving-stress trace inputs and amplification rates. `Martin/existence/trace-asymptotic.tex`, `input:trace-scales`, `prop:trace-scale-supplier` and `lem:trace-moving-correlation` separate these obligations. |
| C-A9 | Trish `part2/J-section.tex:20–24` explicitly makes OPE/contact conclusions conditional on stronger anchored/restart, guarded comparison and graph continuity inputs. | Resolve C-A1 for exactly the marked cluster replacement theorem. Verify the lower-degree subtraction, support exponents and all phase norm bounds rather than citing generic cluster convergence. Martin's detailed closure candidates may address these; that matching has not been performed here. |
| C-A10 | Outline VII.4 does not identify contact-device projections with OPE coefficient projections, and disclaims positivity/uniqueness/contact Ward identities. | Define the two prescriptions separately unless an explicit equivalence is proved. Prove partial-collision sector integrability, not merely integrability on the total radial diagonal. |
| C-A11 | Martin `assembly.tex:209ff` states a conditional joint input and later a retained-construction assembly theorem. | Read the later supplier chain before alleging a missing proof. Conversely, the conditional assembly alone cannot certify the preceding analytic assumptions. Track selected-family identity through every cited supplier. |

## Coverage of every assigned Outline unit

| Outline unit | Book location | Main retained content and intentional omissions |
|---|---|---|
| IV.1 | C2 | Full-volume compactness, weak derivative labels, quotient ranks, hierarchy; present full mesh upgrade using the chosen-family theorem rather than alternate-family labels. |
| V.1 | C3 §§1–2; C4 | Split OS/slab preliminaries from compression, phases and a.e. uniqueness. Move the repeated-word prerequisite from VII.4 to C2. |
| V.2 | C5 §§1–4 | Continuation, tempered boundary, boosts, cone support, locality, positive word realization and faithful labels. Cite standard reconstruction machinery after hypotheses are checked. |
| V.3 | C5 §§4–6 | Surjectivity onto OS space, phasewise uniform bounds, every vacuum, scalar weak commutant, stress charge continuation and joint-test barycenter. |
| VI.1 | C3 §§3–6 | Flux estimates, translation proportionality, analytic propagation, brackets, integration, physical normalization. Do not import completed field algebra as an unexplained hypothesis of itself. |
| VI.2 | C1 §§3–5; C3 §§3–6 | Separate free positivity/classification/Ward flux from interacting comparison/rank transfer and normalized stress. |
| VII.1 | C1 §§1–3 and UV free lattice comparison; C3 §3 | Free Gaussian/Wick reference and detector theory; lattice-to-free Fourier estimates belong with UV covariance estimates. Formal itinerary-specific variants need not be separate book sections. |
| VII.2 | C6 | Spectral trace, controlled stress normalization, arbitrary radii, all-radius asymptotic and precise finite-profile exclusion. Optional Fock nonembedding can be omitted if not part of the target theorem. |
| VII.3 | C1 §§2–4; C6 §§2,5 | Reflected Gram positivity, degree-four finite-dimensional rigidity, lattice Wick prescription, finite power-log obstruction; avoid duplicate positivity proof. |
| VII.4 | C2 §5; C7 | Repeated words early; nonperturbative OPE and contacts late. Nested/integrated refinements condensed; no convergence as truncation degree grows. |
| VII.5 | UV running-coupling chapter; C3 §6 | Leading lattice logarithm is upstream. Auxiliary normalization-ratio and exact filtration correction belongs with stress/frame identification. No independently defined continuum running coupling is silently inferred. |
| VII.6 | C6 §2; C3 §3 as needed | Prescribed-radius schedules and fixed-field estimates; distinguish approaching correlations from stable, exactly compatible maps. Low degrees below four reduce to the unit. |
| VIII.1 | C8, with its upstream premises in earlier chapters | One-family assembly and quantifier order. Public theorem and stronger internal conclusions are not conflated. Formal bookkeeping variants are compressed to a dependency table. |

## Terminology replacement dictionary

These translations are contextual, not equations identifying packages of different hypotheses.

| Source expression | Book expression |
|---|---|
| table / hierarchy | correlation family / listed Euclidean properties |
| token / label | polynomial insertion label (then field class in the quotient) |
| chamber | coordinate reflection Hilbert space with translations |
| bench / train | bound on repeated reflected insertions |
| spread / slab family | bounded slab insertion operators |
| respects S | every S-null label is also null in the second correlation family |
| station / panel / vane | finite-degree, finite-window comparison data (define exact estimates) |
| reader / decoder | finite-dimensional correlation projection / its left inverse |
| cap | polynomial bound on separated correlations or their derivatives |
| quota / price / budget | coefficient norm / quantitative estimate / allowed bound |
| quiet charge / row erasure | charge invisible to the specified test functionals / vanishing of the detected internal action |
| lighthouse stress | normalized free Maxwell stress tensor |
| funded run / campaign | one RG trajectory with the complete enumerated estimates |
| contact device | chosen compatible Taylor-subtraction projections |
| footprint / generic configuration | specify the actual support or coordinatewise separation condition |

Do not replace “phase” by “pure state” without explaining exactly which commutative algebra's characters are involved. Do not call a “finite Wick profile” simply a “free theory”: define the restricted comparison class.

## Literature check record

Checked primary-source landing pages on 18 November 2026. These checks establish provenance/scope; they do not yet establish that every technical lemma is a direct adaptation.

- Osterwalder–Schrader, *Axioms for Euclidean Green's functions II*, CMP 42 (1975), 281–305, DOI `10.1007/BF01608978`. Primary full text located at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf . C5 author must match the actual growth and boundary assumptions, rather than just cite reconstruction abstractly. Also cite the 1973 first paper, DOI `10.1007/BF01645738`.
- Brunetti–Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, CMP 208 (2000), 623–661, https://arxiv.org/abs/math-ph/9903028 , DOI `10.1007/s002200050004`. General extension machinery belongs in citations; the multi-diagonal quantitative prescription still needs its own hypothesis check.
- Fröb–Holland, *All-order existence of and recursion relations for the operator product expansion in Yang–Mills theory*, https://arxiv.org/abs/1603.08012 (2016, revised 2021). Its stated result is perturbative, including gauge-invariant closure; do not use it as an unconditional nonperturbative OPE theorem.
- Collins–Duncan–Joglekar, *Trace and dilatation anomalies in gauge theories*, Phys. Rev. D 16 (1977), 438, https://doi.org/10.1103/PhysRevD.16.438 . Primary publisher page confirms scope and authors. The all-radius nonperturbative limit is additional work.
- Still to verify at proof-writing stage: original precise sources for strict Maxwell jet positivity/Kelvin detectors, bounded-degree Ward classification, uniform all-phase low-energy estimate, and the exact finite power-log profile obstruction. Existing manuscript citations to Wick theory, harmonic analysis and C*-algebras cover standard mechanisms but do not by themselves identify these specialized statements as previously proved.

No claims about the contemporary acceptance or correctness of the linked formal construction have been inferred from web search. The audit concerns the supplied manuscripts and their dependencies.
