# Chapter 17: marked trace rates and variable windows

New fragments: `chapters/17-marked-trace-rates.tex` and `chapters/17-variable-windows.tex`. Together compile standalone to five pages, no undefined control sequences or overfull boxes. No master/preamble changes. UV is independently reviewing the substantive score-to-coefficient argument before root integration.

## Sources and actual inputs

- Scott `part2/I-section.tex`, lines 331–425: current transfer, finite coefficient decomposition, equation direction, stability and forward-difference trace rate. Lines 75–115: prescribed-radius windows crossing stage boundaries.
- Actual block kernel: Chapter 4 equation `ch04:kernel`, q_gamma=Z_gamma^-1 exp(-gamma w), **not** a heat semigroup kernel.
- Chapter 6 `ch06:actual-jet-integral`: bounded pointwise derivative integrals, original fine Borel tests fixed by the protected-coordinate change. Do not invoke `ch06:common-majorant` as an automatic extra supplier; its aggregate quadratic exponential hypothesis is stronger than needed here.
- Chapter 9 differentiated ordinary regular action cap beta_hat^-11/10.
- Chapter 11 `ch11:descent-error`, `ch11:replicated-bound`, full density-valued squarefree marked expansion and `ch11:n-mark-comparison`.
- `11-restarted-history.tex`, proposition `ch11:restart-family`: finite windows up to (loglog beta)^4 steps, explicitly allowing adjacent-stage changes.
- Newly checked repeated-current contraction and exact contact/regulator fragments supply the current bounds, free jets, vanishing defect and scalar coefficient; no perturbative universal coefficient is substituted for the actual calculation.

## Measurable-factor issue and the proposed resolution

Differentiating forced factors is invalid. Distributionally moving their derivatives does not by itself produce bounded marked activities. Instead differentiate the original outgoing kernel, whose fine-field/frame tests are independent of the coarse field. For every fixed left derivative order, |D^r q_gamma| <= C_r (1+gamma)^r q_gamma pointwise. This bounds the inserted kernel score without a lower bound on q or division by the output density.

For the full incoming density f and outgoing F=integral k f, div(FY)=integral[(div Y)k+D_Vk[Y]]f exactly. The source is density-valued and remains in the same joint marked expansion. Against a disjoint spectator it vanishes; actual spectator tails are retained and bounded using the two spare support units. The Taylor polynomial alone is not said to vanish.

A generic score bound cannot preserve the ordinary beta^-1/10 gain. The fragment therefore gives a separate cancellation: in the healthy ordinary sector, the SAME normalized conditional Gaussian integral is Zord=C exp(-beta S-loop-Ereg), with all V-dependent determinants/normalizations included. Its exact differentiated logarithm yields -beta DS-Dloop-DEreg. The existing differentiated regular norm bounds DEreg; Y=O(t) cancels the inverse t from one derivative. An extra coarse derivative reserve is explicit. Absolute polynomial-beta score bounds are used only for complementary terms with failed tests, where exp(-H^1/5/2) absorbs them. Smooth guard boundaries are assigned to enlarged read supports and nested-cutoff failure estimates; no hard-mask derivative is used.

Current extension is first done at finite support and finite period; strict exponential width reserve absorbs derivative support-length powers. Pass to the weighted tail limit afterwards.

The full zero-moment coefficient is Sigma-beta j, not Sigma. This distinction is now explicit. Stationary/current defect is first made arbitrarily small at fixed reading level; finite coefficient and all remainders then follow the same joint limit.

## Rates checked algebraically

With H=exp((loglog beta_hat)^2), t=beta_hat^-1/2 H:
- t^-2 epsilon_reg = beta_hat^-1/10 H^-2.
- beta_hat^-1/10 H^C and beta_hat^C H^C exp(-H^1/5/2) are o(H^-1) at each stage; entry thresholds absorb finite constants.
- Wrapping error retains exp[-period/(5(2B+1))+2] and disappears first at fixed reading level.
- Twelve-plane scalar factor: l(C1,C2,C3)=(-24,-96,0), rho=(-2,-8,0), so l=12rho. Actual loop kills constant and affine links and therefore contributes zero rho.
- ||Sigma|| <= C H^1/6 and rho(Sigma)->-kappa; equation-vector rho error O(H^-1/4)+O(beta^-1), smaller than H^-1/5.
- Backward length T=(log beta)^48 gives e^-T/8; original-history replication costs O((log beta)^22), threshold/allowance costs O(log beta), and column costs o(T). The original history here has B=O(log² beta), not restarted B=O(log⁴ beta). Final residual <=e^-T/100.
- Radius rescaling exp[5(loglog beta)^3] and any fixed beta power are negligible versus that residual.
- Primitive endpoint O(a_k^eta), eta<1/8; averaging floor(a_k^-1+eta/2) forward differences gives O(a_k^eta/2), with shrinking physical window. Finite separating matrix remains invertible.

## Variable-stage windows

No assumption that only two stages can be crossed. For a fixed request the linear marked/response constants C_j are fixed BEFORE L_j. Require log(2+C_j)/log L_j ->0 (j^-2 is optional convenient strengthening). Then product C along any O(logH) window is H^o(1). Fixed-L nonlinear stationary constants are NOT placed in this product; they enter delayed local error allowances.

Single-step overshoot log L <= loglog beta =o(logH). Number of steps O(logH) is less than restart allowance (loglog beta)^4. Covariance telescoping uses unequal actual responses; their derivative product is S^-r-2 product R_j, still H^o(1) after normalization. Top extraction T depends on actual insertion/self covariance, not selected stopping levels; longest-window restart serves the entire compact exponent interval. Weakening final root exponent to 1/(32 arity) leaves margin for H^o(1) losses.

## Literature policy

The additional arguments are exact finite-dimensional differentiation, finite polynomial algebra, and explicit use of already documented constructive estimates. No new external theorem or unverified bibliographic claim is introduced. Scott is used as a source locator, not as authority for the missing measurable-factor step. Martin's trace-asymptotic/scribe chain contains conditional transfer interfaces and does not replace this check.

## Revisions from independent review

UV required and the fragment now includes the following joins:

1. The ordinary score cancellation is the derivative of the SAME normalized Gaussian conditional integral, not a generic polynomial-beta estimate. The full rooted connected component is its dependence region; distant failures connected to the score remain in the complementary sum.
2. Choose a finite covariant completion of the controlled displacement jets through order four. This controls the extra derivatives without assuming that arbitrary higher jets of a deep transferred current are bounded. Cancel the entire classical current divergence through order four: its remaining error costs t^-2 beta t^5=beta^-1/2 H^3, fitting the asserted ordinary beta^-1/10 H^C budget. Loop/Jacobian higher remainders have no leading beta.
3. Pointwise in U, integral over V of D_Y k is zero. Thus multiplying by any original incoming marked coefficient f_A(U), measurable or smooth, preserves exact zero; the same source is used for all A and retains all pushed cross-modes. For coarse smooth spectators the separate integration-by-parts identity is valid; approximating them by local sections leaves a cover tail at distance R>=c exp(T_n), negligible compared with exp(-T_n/100).

Standalone recheck after these additions gives six pages for both fragments together, no overfull boxes or undefined controls. Root handles cross-reference resolution/global build.

## Open point found in final review: screened spatial moments

Do NOT integrate the rate fragment as an unconditional proof of all five transfer estimates yet. The differentiated-kernel identity and ordinary cancellation are checked, as is the high-field-order error beta*t^5/t². However, a vanishing engineering jet need not gain an extra field amplitude: a bilinear term with high spatial differences is still O(t²). Its leading linear screened transport must be analyzed separately. The fragment now explicitly retains this condition and marks subsequent rate deductions conditional.

Potential weaker sufficient condition: include the full linear screened spatial contribution in Sigma (only ||Sigma||<=H^1/6 needed), prove its rho contribution vanishes, and prove the transported divergence coefficient rho error=o(H^-1/5). Simple finite-step O(1/L) suppression alone does not imply H^-1/5 at a fixed stage. An exact K0 double-zero alias argument may apply to actual anchored current transfer, but cannot be applied to the marked extraction without matching its anchor and response maps. This matching is being investigated; it is not yet asserted.

## Final resolution of the spatial-moment point

The preceding open-point entry is superseded by Proposition `ch17:spatial-moments`, now proved in the fragment and independently checked by UV and foundations.

Actual supplier: Martin `heading-history-handoff.tex`10–90, `kernel-transport-identities.tex`155–193, `trace-regular-atom.tex`274–379, `trace-row-jet-estimates.tex`161–278, and `trace-local-rate-selection.tex`173–207. These match the installed straight transport W_s of Chapter5, not an unrelated response. The pole-cancelled nonprincipal formula is A_l=D_l F1,l* D^-1+diag(g_l)x_l sigma, g_l=bar(m_l)[trD_l/(s alpha)−D_l,aa |r_L|²/B_a], sigma=chi^-1 x*diag(B^-1), chi=(x*diag(B^-1)x)/s. All remaining denominators are nonzero analytic at zero. Thus both terms carry bar(m_l)=boxfilter^j, giving exact nonprincipal order j. Principal row mass is L^-1. Fourier differentiation proves global polynomial preservation through degree<j.

Apply this only to polarized coefficient probes of summed engineering weight≤5: W_s lowers or preserves each polynomial degree, so the prescribed vanishing moment is exact. It does not say the function vanishes on arbitrary polynomial input fields.

Actual W_a differs from W_s by a fine gradient. The regular coefficient is a color scalar and spacetime vector, invariant under fine gauge transformations: Haar divergence of equivariantY is invariant because the gauge action preserves Haar volume; action/loop variations are invariant as well. Matching the gauge representatives by BCH costs poly(B)t² in fields, or poly(B)t after normalizing by t. The ordinary source has already had its classical β contribution cancelled. It starts at field order2, so its t^-2-normalized regular norm is N_k<=H^(theta_j+o(1)), with theta_j→0. No extra t^-2 is applied to the following estimate.

Subtract the deterministic coefficient inside the same normalized conditional expectation. Its selected jet is zero. Use the actual joint polynomial moments and differentiated conditional density scores for the evaluation difference; no small total-variation comparison of nonlinear and Gaussian laws is asserted. The normalized Gaussian displacement costs g/t=H^-1. Nonlinear response and gauge-coordinate errors cost poly(B)t, and cropped tails exp(-c log² beta). Fixed powers of log beta are H^o(1), so the total spatial coefficient error is H^(-1+theta_j+o(1))<=CH^-1/2.

This weaker rate is enough. Sigma's rho error merely needs o(1), and j's error can still be bounded by CH^-1/4, giving H^1/5 times that error→0. The unsupported stronger beta^-1/10 spatial bound has been removed; equation `ch17:sigma-error` explicitly includes CH^-1/2. All five transfer estimates are now derived, rather than assumed.

Both reviewers also passed variable-window comparison after these clarifications: distinct stage ratio mathscr L_j versus scale L_i; pre-L linear constants only in per-step products; post-L nonlinear errors summed after propagation; actual coupling change bounded quantitatively by H^o(1)(1+logH)/beta_hat, smaller than every fixed inverse power of H. Source-specific 'reading/screened/same-guide' wording was replaced in the new mathematical prose.

Final standalone verification: both fragments together seven pages, no undefined controls or overfull boxes. Root owns global integration. No further edits pending from this agent.
