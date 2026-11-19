# Chapter 14 audit

Draft `chapters/14-reflection-ward.tex`, 12 standalone pages. This chapter constructs coordinate OS spaces/slab operators, then the stress/Ward/rotation mechanism. Its final rotation and normalized-stress theorems explicitly retain the actual marked comparison and annular estimates; it does not silently certify unfinished Chapter11 marked suppliers. No phase decomposition, Lorentz Hilbert-space action, vacuum uniqueness, mass gap or positive contact extension is claimed.

## Source trace

- Martin `reflection.tex` entire, Scott G `lem:H1.1`: OS quotient, orbit-bound contraction, transverse translations, strong continuity, positive heat generator. Standard quotient attributed to Osterwalder–Schrader1973; only the needed contraction estimate is adapted. Coordinate spectra are [0,infinity)×R3, not a forward cone.
- Martin `phases.tex:33–109`, `slab-regularity.tex`: formal insertion adjoint, repeated-word power bound, null descent, exact concatenation/width laws, norm smoothness by operator mean-value remainder. Actual all-repetition input is Ch13:word-bound, including its chosen width s<=h, then heat extension to h. Arity-fixed bounds are not substituted.
- Scott G223–310 `lem:G-lattice`, G390ff smooth comparison; Martin `actual-stress-normalization.tex:1–145`: size/variation/grid estimates on SAME lifts, coordinate-strip volume and grid error costs, exact inclusion correction, finite detectors, derivative-transport lower singular-value bound, Fourier L1-to-Cj upgrade. Draft spells out quantitative interface rather than asserting grid comparison from field-space dimension alone.
- Scott G78–96, G `lem:G2.2`; Martin `actual-stress-normalization.tex:145–230`: divergence rank and centered physical line, sign and scale sequence. Ch3 gives rank2 matrix and 3D tensor basis; Ch14 additionally identifies the full degree5 hypercubic vector target as the two F∂F contractions via Maxwell/Bianchi, needed for onto divergence. Centering maps require preserved unit and do not presume matching one-point functions.
- Scott G310–389 `lem:G-annular`; Martin `actual-stress-annulus.tex`, `actual-stress-shell-nodes.tex`: same-spectator two-mark correction, physical collar rho=128 B²a, t=1+1/[64(d+12)], cost1/32+1/64−1/8=−5/64, residual root e^-tau/32. Draft gives implication from actual marked inputs and finite-stencil interpolation across coordinate ties; no common tail over an entire growing collar is assumed. Need Ch11 exact two-mark backward inverse gain, coefficient correction and derivative growth C independent of q to discharge it.
- Scott G `lem:G2.3`; Martin `actual-stress-annulus.tex` conclusion and `physical-ward-propagation.tex:492–590`: annihilator finite-dimensional duality gives local charge fields; derivatives of moving shells give p/Y commutators. Conservation and tensor symmetry justify shell independence before normalization.
- Scott G coordinate section `lem:H-coordinate-signs`, `lem:H-G3`; Martin `physical-ward-packet-prices.tex`, `physical-ward-stress-cone.tex:1–280`: coordinate positive measures, undamping, finite damped moments, Lagrange annular corrections and positive residual rational kernel, mixed-sign transfer walk, separate diagonal estimate. Draft retains minimum symmetric product-test extension and normalization of contact divergence to degree>=3, then Q0/Q1/Q2 conservation chain and signs +,-,+. It does not call this extension positive.
- Scott G `lem:G-collinear-flux`, Martin `physical-ward-propagation.tex:145–445`: anisotropic lengths powers100/150/300, exact two-column cancellation, low energy split at lambda^-3000, W=lambda^-99 and explicit worst exponent table. E=0 kept in shallow region; diagonal positive weight itself vanishes at0. No rotational spectrum assumption.
- Martin `physical-ward-analytic-continuation.tex` entire, `physical-ward-propagation.tex:1–143`; Scott G `lem:G-analytic`: radial heat analyticity, finite-dimensional analytic comparator, transverse jet induction, stationary positive Gram factorial bound, extreme-point segment continuation. Equality of smooth jets alone is never used as an identity theorem.
- Scott G735–834, Martin `physical-ward-propagation.tex` finite tests/brackets and `physical-angular-actions.tex`: translation charge p=c*∂ using actual Ch3 vector tests, c_k→c*>0 via shell readouts, internal bracket defect removal using Ch3 finite tests, exact finite-dimensional relative-Casimir intertwiner, genuine O4 action instead of only its cover, Haar-averaged normalized stress. Draft uses ordinary finite-dimensional spectral projection instead of source polynomial projection iteration; these are equivalent standard spectral-calculus operations near an isolated eigenvalue.

## Exports and limits

- `ch14:heat`, `ch14:coordinate-spectrum`: coordinate semigroup and joint measure, no cone.
- `ch14:slab-bound`, `ch14:slab-laws`, `ch14:slab-smooth`: bounded norm-smooth slabs, usable by phase chapter.
- `ch14:smooth-comparison`, `ch14:conserved-line`, `ch14:balanced-stress`: from marked grid comparison and Ch13 quotient calculus.
- `ch14:charges`: from actual annular remainder estimates.
- `ch14:rotations`: O4 action/correlation covariance, inclusion and vector laws, from actual comparison+annular estimates.
- `ch14:normalized-stress`: exact shell normalization and scaled stress comparison.

## Review priorities

1. Mixed-sign annular transfer and diagonal conservation estimates are compressed from the detailed source proof. Check correction normalization, spectral Fourier signs, and the order of choosing width exponents/moment orders. Diagonal Q0,Q1,Q2 normalization was expanded to explicit c_r(t),d_r relations to expose 4d0=5d1−d2.
2. Actual marked grid estimate and annular two-mark supplier are still quantitative interfaces to Chapter11. This is a source-specific dependency, not an appeal to OS reconstruction or to the existence of free Wick correlations.
3. Finite vector and internal-defect tests use Ch3 theorems at all finite required degrees and Ch13 faithful quotient/inclusions. Same comparison maps must preserve inclusions exactly; draft constructs this before transporting finite test matrices.
4. Normalized undamped point-field measures can have infinite total mass. Only finite energy windows and adequately damped moments are used. Finite translated words need damping beyond their offsets.
5. No local Taylor/contact extension from this chapter may be cited as an OS-positive distribution hierarchy.

## Original literature

OS1973 original Project Euclid PDF checked: https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/Axioms-for-Euclidean-Greens-functions/cmp/1103858969.pdf . OS1975 corrected theorem original PDF checked: https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf . Existing bibliography entries used; no new sidecar needed. Neither reconstruction theorem is invoked without its growth hypotheses.

Fröhlich–Osterwalder–Seiler1983 primary publisher page checked: https://annals.math.princeton.edu/1983/118-3/p04 . Its virtual-representation continuation is related, but does not directly supply this chapter's pre-rotation stress spectral estimate or its fixed-configuration Gram argument. It is therefore not cited as proving those source-specific assertions.

## Validation

Standalone pdflatex twice succeeds,12pages; last log contains no overfull/underfull boxes. No global build performed. Root handles global references and rendering.

## Expansion after root review

The opposite-sign proof now defines every response, scaled profile and omitted-axis limit. Equation ch14:sign-transfer follows by expanding the exact equality for TWO residual profiles; discarded term has nonnegative spectral response. Equation ch14:sign-induction gives its precise exponent ranges and visited-axis bookkeeping. Choices alpha(nextstep),r,D,a_s,m are ordered; the error exponent is p_*-2ralpha+max(K,a_sD). Added explicit tensor subtraction q_ab,cd=Σ_iR_ib,cd(∂_i(x_aχ0)) and parity-pattern justification of its pair symmetries. Standalone now13pages with no overfull/underfull boxes. Root handles global rendering.

## Integrated lattice suppliers

The earlier comparison/annular caveat is superseded in the working chapter by two explicit forward dependencies. `14-lattice-comparison.tex` uses Chapter11's finite-arity complete source estimate and exact common extraction at a finite menu of scales; its independent review is `chapter-14-lattice-comparison-review.md`. The shrinking-shell estimate now follows from the mixed local replacement proved at the end of Chapter13: for W=d+4 and D=d+1−kappa, multiplying its residual by r^(3+kappa) yields r^(1−epsilon). The replacement field is fixed before spectators, so the finite annihilator sum cancels it. This avoids a phase/OPE dependency and removes the former separate two-mark annular hypothesis. The coordinate spectral argument is undergoing an additional independent review.
