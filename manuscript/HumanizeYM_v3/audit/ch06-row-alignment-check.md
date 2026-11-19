# Final dependency check: compatible quadratic rows

The former Chapter6 statement that the compatible row identities 'remain assumptions' was too broad for the selected construction. It has been replaced by their explicit realization from the proved Chapter5 identities, while retaining the exact coefficient condition for arbitrary alternative path actions.

Let C_nu be the actual direct/path curvature row, H_nu=C_nu* C_nu the selected modified metric, B_nu=H_nu^-1, and P_c=C_c B_c C_c*. Chapter5 positive-defect gives a local row K with K*K=B_c−T*B_fT−b^-1 d_c d_c*. Choose

    M_f=C_f B_f T C_c*, M_n=b^-1/2 d_c* C_c*,
    N=(I−P_c, K C_c*)^T.

Multiplication gives M_f*M_f+M_n*M_n+N*N=I. The actual predictor curl identity T*d_f=d_c Q gives the second flat identity on X_f=C_f d_f a and Z=sqrt(b)(v−Qa). The coarse-gradient correction in actual Q has zero curl. The modified metric agrees with the unmodified metric on curls.

Actual selected action match:

- Chapter7 classical matching explicitly writes H=c_dir I+rho*rho and constructs its direct Wilson plus transported rho-square action J with that exact Hessian. Its added cubic/quartic curvature terms cannot change that coefficient. The loop action is a separate non-beta contribution.
- Chapter9 one-step theorem explicitly uses this outgoing construction, so alignment is preserved under induction.
- Chapter9 Wilson initialization chooses direct sqrt(c_dir) and extra sqrt(1−c_dir) rows, with Gram I. At the terminal fine level take the allowed unmodified metric (zeta_f=0); the first coarse metric uses the positive-defect construction. Later rows are the constructed modified ones. This choice is now stated in Chapter6 and is compatible with the fixed-scale horizon limit, since a fixed scale is eventually nonterminal.

No assertion was made that normalization H(0)=I alone implies full symbol alignment, or that an arbitrary path family matches the chosen quadratic history.

check_draft.py passes after the edit. Global compilation left to parent.
