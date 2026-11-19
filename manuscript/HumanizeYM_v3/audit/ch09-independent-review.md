# Independent review of Chapter 9

Snapshot reviewed: `chapters/09-renormalization.tex`, 2026-11-19, while author was doing terminology integration. No chapter edits were made. Scope: exact subtraction/replacement/fusion, scalar normalization, continuity, Wilson initialization, and hidden interface assumptions.

## Actionable findings

### 1. State spatial-weight and derivative-order hypotheses

At the local subtraction estimate (around line429), the assertion `t²|q_f(q,r)|<=3a_f` uses the affine directions A_b(y)=xi_o(y)^a T. Chapter4's seminorm allows directions only of size t(1+dist)^varpi, and its stated range is arbitrary varpi>=0. A support-independent affine test bound requires at least varpi>=1. With varpi<1 it incurs a support-diameter factor; it cannot be bounded by the displayed fixed constant.

Moreover the inherited L^-5 argument uses more than q>=2. Scott `part2/D-section.tex`, inherited discussion around lines260–279, explicitly requires incoming varpi>=outgoing varpi>=2 and q>=6. Add these chosen-stage conditions at Chapter9's start and one-step statement (or explicitly retain the appropriate support and derivative hypotheses). Since Chapter4 deliberately permits a general class, these requirements should not be left implicit in “choose the stage constants.”

### 2. Reflected localization needs the shifted evaluations

Around lines277–305, the claim that reflected local summands have the same value within an interior class is not true for a generic nonconstant configuration reflected once about x. The source uses two different evaluation arrangements:

- the bounded auxiliary sum defining G_x evaluates on V_(i,x);
- the pointwise discrepancy L_x evaluates its y summand on V_(i,x−ytilde), so auxiliary site y corresponds to the same physical site x.

Only the second arrangement has the class-constant property needed for the fourth finite difference. Summing over x and translation reindexing relates it to the first. See Scott `eq:D-five-weights`, `eq:D-mask-localization` and proof of `lem:D-localization` (around lines350–395).

Add those definitions and the reindexing step. Alternatively identify the localization result as another explicit input. Merely saying “extend by reflection” does not prove the claimed local reconstruction. The binomial weights themselves are correct: sum(-1)^i binom(4,i)i^4=4!, with leading multiplicity2^4.

### 3. Specify the finest direct coefficient

Wilson initialization chooses sqrt(1−c_dir), so requires 0<c_dir<=1 (usually strictly below1). Chapter4 only states16c_lin<c_dir. The matched metric identity elsewhere forces this bound for a selected metric, but initialization should explicitly choose it rather than use an undefined real square root for the general Chapter4 parameter range.

A useful accompanying sentence: F(e^X) is odd under X→−X, its local inverse is odd, and W(u^-1)=W(u). Hence W(e^{psi(Y)}) is even, so its missing cubic Taylor term really is zero. This is a short justification, not an additional substantive assumption.

## Exact algebra checked

- `ch09:subtract-identity` is correct on both h_Z=1 and h_Z=0. Enlargement includes X and the clover neighborhood; on h_Z=1 the smaller masks are1. The regular remainder has the intended flat value/affine-Hessian normalization on nonwrapping supports.
- `ch09:channel` is correct separately on the two health domains. On h_Y=1 it reduces to alpha aP+Delta aQ; on h_Y=0 its correction J supplies the difference exactly.
- The signs in `ch09:path-identity` and `ch09:before-fusion` are consistent: replacing alpha Q+Delta C by (alpha+Delta)K+F−J produces the positive exponent of J and zeta, and E=masked R+F. The cubic/quartic regular terms must have sign −(alpha+Delta), as written.
- No division by a possibly signed or zero exact-cover gas occurs.

## Fusion checks

- In a nonzero logarithmic selection each log support contains a bad site. Exact coverage places that site in a preliminary inventory whose exclusion support intersects the log support. Thus every connected component has a large-field vertex.
- Taking connected components and flattening are inverse operations when preliminary supports are disjoint, new supports are their unions with log supports, inventories are unions, and all inherited tests are retained. Extra flag-read overlap does not affect this combinatorial bijection.
- The sum bound is compatible with the stated spare exponent. A support has at most h c(Z) sites with h=(2B+1)^4. The positive rooted-tree recursion uses attachment sum<=h gamma c(Z); if h gamma<=1, the input weight exp((sigma+1)c) absorbs it. Rooting through a fixed site gives a bound<=gamma, hence<=exp(gamma)−1. Retaining exp(−kappa) from one large-field label per component is valid.
- The proposition's opening exact identity for countably many labels also uses absolute summability of the preliminary gas. This is supplied by the preceding early bounds; it would be helpful to include that hypothesis if the proposition is meant to stand alone. It is not a missing assumption in its present application.

## Scalar reset and continuity checks

- The reset beta=beta'+alpha+Delta and scalar tau−|Lambda|^-1 sum f_i(1) follow directly. At the flat field all path terms, regular remainders and logarithmic discrepancies vanish, and the only cover is empty. Thus the intrinsic flat logarithm agrees.
- Delta bound is H_pre/t² = O(beta_ref^-1/10 (M_cut)^-2); its exponent is correct.
- The intrinsic test has f(d)=(d−Delta)K(U_*), with the displayed sign of log(H(1)/H(U_*)). It is valid because the full identity has already been proved and U_* is small-field. It cannot serve as a substitute for that identity; the text explicitly says so.
- Gaussian Radon–Nikodym ratio and score signs are correct. Holding physical coordinates fixed avoids differentiating merely measurable link activities. Domination must include the actual means/matrices, which is acknowledged as common-law input.
- Fixed-curve compactness gives uniform weighted truncation; it does not give a common truncation over arbitrary same-label families. The draft correctly restricts this statement.
- The summable-subsequence argument for weighted output continuity is sound: continuity in weighted input norms gives a subsequence with summable discrepancies, the strict margin admits the envelope, and domination yields a convergent further subsequence of every allegedly bad sequence.
- At fixed volume, the exact-cover telescoping bound follows by dropping eligibility restrictions and summing the positive product envelope. It does not require positivity of individual activities.

## Wilson initialization checks

Conditional on 0<c_dir<=1, the residual-energy formula is algebraically correct in all cases:

- chord>t: health and relaxed masks vanish and W−c_lin t chord is the residual;
- chord<=t with h_p=0: L plus residual equals W because the row term cancels;
- chord<=t with h_p=1: T4+R=W−|F|²/2, so again the displayed equality holds, even if the relaxed test fails due to a nearby bad plaquette.

The residual is nonnegative using |F|<=chord and W=chord²/2. For chord>t, c_lin<=1/16 gives at least t²/4. The bound d_I>=c t²|I| follows from a bad plaquette per bad site and at most four vertices per plaquette. Components formed by overlapping radius2B neighborhoods give unique compatible exact cover; every positive row-test failure has a witness in that component. The connected-inventory count can be paid by beta t²~(M_cut)². The regular exponent beta t5 / epsilon_reg=beta_ref^-2/5(M_cut)^5 is correct.

## Hidden forward assumptions

The chapter properly leaves these model-specific estimates conditional: common sector product bounds, inherited interpolation comparison, low-order same-integral remainder, selected determinant comparison, and the output coupling-band margin. None follows merely from the standard one-loop coefficient or from selecting a scale schedule. The preparation-to-localization step needs the correction in finding2 before it can be counted as proved rather than an extra input.
# Integration follow-up

The chapter author incorporated the three review corrections before the integrated build of 19 November 2026: monotone derivative/spatial-weight requirements, the recentered reflected-evaluation formulas and translation reindexing, and the top-scale bound `0<c_dir<=1`. The review below records the earlier snapshot and should not be read as a list of still-open editorial fixes. The analytic assumptions recorded in the chapter remain open where explicitly stated.

