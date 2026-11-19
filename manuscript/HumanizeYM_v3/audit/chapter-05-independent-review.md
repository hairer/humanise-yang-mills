# Independent review of Chapter 5 (19 November 2026)

Reviewed current `chapters/05-gaussian.tex` for algebra, counting normalizations, zero modes and conditional quantifiers. No direct edits made to the author's chapter.

- Finite Gaussian problem: A=K_f+bQ*Q, W=A⁻¹bQ*, K_c=bI−b²QA⁻¹Q*; completion of squares and determinant scalar are correct in counting inner products. For K_f>0 the Woodbury covariance identity is correct. Semidefinite extension is appropriately limited to A invertible, with no invalid massless prior probability interpretation. Conditional mean/covariance follows for proper joint Gaussian.
- Fourier: forward transform unnormalized, inverse s⁻⁴, Plancherel s⁻⁴. Downsampling and length-L line sum give Mhat=L⁻⁴Σ_z L what r_L ahat. Covariance then has L⁻⁸ L² L⁴=L⁻². Plus-sign averaging convention matches kernel a(Ly+z+r e_mu). Real w yields paired what(theta)what(−theta). No missing volume factor found.
- Gauge reduction: weighted projection gives numerator Σ_{mu<nu} w_mu w_nu |q_mu a_nu−q_nu a_mu|² divided by Σ w_mu |q_mu|². H0 formula matches. Harmonic zero modes are distinguished from periodic gradients; no 1/lambda(0) is used as a covariance.
- Pole cancellation: with c_mu=B_mu/lambda_M, identity Σq²/B=lambda_M h gives H0=(h B_mu B_nu)⁻¹. The geometric-sum identity used to establish h is correct. Holomorphic extension remains conditional on nonvanishing F,A,B,h; a uniform strip is not claimed from the algebra.
- Metric modification: H⁻¹=H0⁻¹+zeta(d2H0⁻¹)*(d2H0⁻¹) implies H⁻¹H0 d1=d1 by d2d1=0; hence H d1=H0d1, correct.
- Stationary graph: contraction constant≤1/4 and displacement≤r_y/4 imply mapping into r_y/2 ball and unique fixed point. Inverse derivative bound 4J/3 is correct. Holomorphic hypotheses are explicitly complex and uniform in number of coordinates; real finite differentiability is not promoted to uniform holomorphy.
- Uniform weighted inverse claim is a standard sufficient framework, not a proof of the actual gauge Hessian hypotheses. Draft appropriately makes this distinction.

Two clarification requests sent to author and parent: explain the beta-free Gaussian normalization relative to Chapter4 penalty b beta (rescale link logs by sqrt(beta), or label the displayed Gaussian model standalone), and explicitly retain bounded coordinate multiplicity per lattice site in the stationary-section shell-sum example. Otherwise the displayed anchored derivative bound alone does not make S_eta uniform if arbitrarily many coordinates share an anchor.

This review checks the written finite algebra and logical limits of conditional statements. It does not discharge the model-specific uniform alias estimates, positivity of the interscale defect, or actual nonlinear Hessian bounds listed at the chapter end.
