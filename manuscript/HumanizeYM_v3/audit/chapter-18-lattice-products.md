# Grouped lattice products and raw replacement

Files: `chapters/18-lattice-products.tex` and `chapters/18-raw-replacement.tex`. Parent owns their placement and changes to the main chapter.

## Placement and dependency

The first fragment has no phase, stress or Ward premise. Place it after the graded quotient and sharp bounds at the end of Chapter 13. It proves lattice signed replacement and mixed finite-spectator replacement. Thus Chapter 14 may use its annular consequence without referring forward to the operator-product chapter. Its finite correlation readouts use only the already defined physical quotient and all-spectator separation. The second fragment belongs in Chapter 18 after its raw readout and precise replacement statement; it uses the established phase/compression moment identity to prove that statement, with constants chosen before moment number.

## Independent graded review

The current `18-graded-quotient.tex` matches Scott's cone proof. Checked triangular low/high scaling, invariance of the high plane, repeated subtraction, subpower column products, and the all-spectator lower-field identification using normalized-null representatives. No correction found. This step is needed in Chapter 13 before the mixed local replacement, if the dependency is to run forward.

## Source packet and literature check

Scott `part2/J-section.tex`: signed local transport roughly 30–103; graded quotient 104–150; marked algebra and weights 211–272; extraction 273–304; grouping/replacement 334–414; continuum/probe/derivative passage 415–455. These source-specific estimates were checked against the actual Chapter 11 signed cone, termwise marked integration, cover transfer, higher modes and normalized replicated integral; Chapter 13 supplies sparse stopping and sharp source weights.

External check: the original arXiv record for Bauerschmidt–Brydges–Slade, *Critical two-point function of the 4-dimensional weakly self-avoiding walk*, arXiv:1403.7268, confirms incorporation of observable fields in the RG. The source bibliography entry `BauerschmidtBrydgesSlade2015` has CMP338 (2015),169–193, DOI10.1007/s00220-015-2353-5. Cite it only for that general method, not as a replacement proof of the present gauge-theory grouped bounds. Its existing entry is in Scott/references.bib for the bibliography collector. No new claim that an original literature theorem directly proves this manuscript-specific supplier is made.

## Quantitative checks

- Signed residual has physical degree-t factor and cone gain (a_m/a_l)^(1/8); exact column recentering retains the original inventory and zero readout.
- Marker grouping retains all original square-zero variables/partial modes until full coefficient extraction; no invalid algebra homomorphism or probabilistic independence of separated supports is asserted.
- Support enlargement pays both exp(sigma h) and rooted incidence reassignment. At most n−1 fusions occur per local cluster. Between fusions the *unsubtracted* incoming regular term uses its cover-conversion cost T_l<=L_l; it is not assigned a zero-jet contraction. The resulting 6L_l<=L_l^4 cost gives Z=W theta_plus+4n(theta_plus−theta).
- The two exact residual weight inequalities are stated. The chosen weight has strict exponent margins −15(theta−theta_minus)/16 in the extraction condition and −(theta−theta_minus)/16 in the transport condition. The intermediate-level ratio is (a_l/a_kstar)^(7/8), so the endpoint check suffices.
- Sparse kstar normalization uses the actual q_site and the sharp schedule. Both log N_k and all extraction/support costs are subpower; no volume-dependent scalar survives.
- Coefficient extraction for one residual per reflected cell costs varpi^-1 per cell, with all higher modes retained. Incidence estimates depend on fixed marks per cell, not total cells. This is the all-copy input needed later.
- Graded quotient recovers degree-i coordinate exponent Z−i theta. Auxiliary t is chosen strictly larger when necessary. Mixed derivative descent acts on fixed correlation readouts, never on a potentially nonsmooth selection of auxiliary output labels.
- The finite readout construction explicitly preserves old correlation functionals across higher degrees and kills them on newly lifted bases. Hence the raw low-degree readout is the intended truncation of the auxiliary field; arbitrary unrelated projections would not suffice.

## Remaining review focus

The supplied proof makes explicit the source-specific grouped-coefficient extraction and the transfer of all modes. It uses the existing termwise Chapter 11 compiler at arbitrary fixed arity per cell, not only its two-mark detector specialization. During independent integration review check precisely that the old large-field normalized source and the full-group density coefficient are in that format; no division by a gas/activity is allowed. No unproved estimate is intentionally introduced as a new scheduling request. The only new requests are finite degree/stage support constants, Taylor orders and numerical weight margins.

Static environment counts balance and all internal references currently resolve. No global compilation performed.

## Parent review

Parent independently checked the residual-weight arithmetic, order of quantifiers and fixed-probe derivative descent. Added explicit degree-independent exponents: crude c0=1, grid c1=4n(theta_plus−theta)−(D+1)theta for residuals, or with −i theta for a fixed coordinate. Clarified that the auxiliary horizon pays only raw coordinates through D, not every coordinate through t (which would fail when theta_minus>0). The earlier independent review of the graded quotient passed, with no mathematical correction requested.
