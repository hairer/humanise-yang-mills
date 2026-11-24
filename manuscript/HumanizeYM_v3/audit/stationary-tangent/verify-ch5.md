# Verification of the W_s / W_a / W_F table against chapter 5 (v3)

Files read (read-only). v3 = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/.
"05:" = 05-gaussian.tex, "04:" = 04-blocking.tex, "17cc:" = 17-current-contraction.tex,
"17mt:" = 17-marked-trace-rates.tex. Scott = /Users/mgubi/ym-terminology/manuscript/HumanizeYM_v2/part2/{B,D}-section.tex.
Labels: [v3 states] / [v3 proves] / [mine] = computation redone here.

## Verdicts in one table

| property | W_s | W_a | W_F |
|---|---|---|---|
| K_f W = M^*K_c = Q^*K_c (Q = calligraphic Q) | TRUE | TRUE | TRUE |
| M W = 1 - K_c/b | TRUE | fails by a coarse gradient | fails by a coarse gradient |
| Q W = 1 - K_c/b (rooted identity) | fails by d_{0,c} R W_s | TRUE | TRUE |
| stationary for the actual quadratic energy | no (unless Q^* d_{0,c} R W_s = 0) | yes (full space) | yes (full space and forest slice) |
| is D of nonlinear stationary map in forest chart | no | no (gauge-equivalent representative) | YES (05:1148) |
| covariant under coarse translations | yes, by construction | yes (R and E are, from their definitions) | only if the forest is translation invariant; v3 does not require this |
| exponential coarse decay | proved (05:586-601, not re-verified) | proved (05:1128-1132) | not stated in v3; follows in two lines (below), constants C_{j,L} |
| fine-difference bounds L^{-1-r} | proved, r <= j-2 | proved, r <= j-2 | false (not smooth; O(1) on crossing edges, 0 on tree edges) |
| exact polynomial preservation | proved (17mt:237-249) | not proved as such; only via gauge invariance | no |

## A. Definitions

- K (generic): `S_0(a)=1/2<d_1a,Hd_1a>, K=d_1^*Hd_1` (05:45-47). Abstract Schur data: `A=K_f+bQ^*Q, W=A^{-1}bQ^*, K_c=bI-b^2QA^{-1}Q^*` (05:90-94), consequences `K_fW=Q^*K_c, QW=I-b^{-1}K_c` (05:141-143).
- K_f: `K_f=d_{1,f}^*H_fd_{1,f}` with `H_f>=eps I>0`, introduced as an ASSUMPTION on the actual quadratic Taylor coefficient of the fine action (05:1052-1058).
- K_c: never displayed as a definition in the nonlinear section; it is `d_{1,c}^*H_cd_{1,c}` read off from `QW=I-b^{-1}d_{1,c}^*H_cd_{1,c}` (05:532) with H_c the coarse metric from (ch05:H0)/(metric-modification) (05:456).
- M: `(Ma)_mu(y)=sum_z w(z) sum_{r=0}^{L-1} a_mu(Ly+z+re_mu)` (05:155-158), a sum along the length-L link, not an average; `w` = j-fold convolution of the uniform probability on the centred box (05:196-201; = `w^av` of 04:186-188). 05:993-994 says M in (actual-Q) "is exactly the straight length-L average with the convolution weights used in (alias-recursion)".
- R: 05:975-983: `tau_y(r)=-av_{r',o} I_a(Ly+r->Ly+r';o)`, `H_{y,r}(a)=tau_y(r)-tau_y(0)`, `Ra(y)=-sum_r w_r^av H_{y,r}(a)`, where I_a is the signed sum of a along the coordinate path with order o in the frame patch at Ly, and av is the uniform average over r' in B_R and o in S_4 (04:118, 04:60-63, patch translated to Ly: 04:172-173).
- Q (calligraphic): `Qa=Ma+d_{0,c}Ra`, `Q d_{0,f}phi=d_{0,c}(phi|_{L Lambda_s})` (05:988-992).
- E: `(Eh)(x)=sum_{y in Lambda_s} sum_{k in Z^4} phi(x/L-y-sk)h(y)` with phi a smooth compactly supported cardinal partition of unity, `phi(n)=1_{n=0}`, `sum_n phi(x-n)=1` (05:1094-1103); `||nabla_f^r E||<=C_rL^{-r}` (05:1104-1106).
- W_s: "the straight-average transport already constructed in Section ch05:transports" (05:1084-1085). There: alias symbols `A_l=D_lF_{1,l}^*R+e_lx_l pi` (05:499-500; here R is the coarse kinetic symbol, a notational clash with the frame operator R), physical kernel `L^{-1}sum_l e^{i theta_l.r}A_l(p)` followed by coarse Fourier inversion (05:520-528), identities (05:529-534), "Q is the straight averaging operator in this construction" (05:535).
- W_a: `W_a=W_s-d_{0,f}ERW_s` (05:1107-1109).
- W_F: "adjust W_a v by the unique gradient d_{0,f}phi whose site potential is zero at every block root and makes all tree edges vanish ... Write the resulting representative as W_F v" (05:1139-1143). The forest: "in each centered block Ly+B_{(L-1)/2} a spanning tree rooted at Ly. Trees contain only internal block edges" (05:916-918).

Comparison with Scott: Scott's `W_s` (B-section 363-366, "smooth centred") is the same operator as v3's W_s (same gradient part: Scott `d_fL eta`, `L=s_fA^*(As_fA^*)^{-1}`, v3 `e_l x_l pi`, `e_l=conj(m_l) tr D_l/alpha`). Scott's `W_r=W_s-d_fI_l(F_mW_s)` (B:388) is v3's W_a, with `F_m a(y)=tau_y(0)-sum_r w_r tau_y(r)` (B:502) = v3's R. Scott's "tree representative of W_0" (B:483) is v3's W_F. WARNING: Scott also uses the symbol `W_F` (B:364) for `C_fM^*C_c^{-1}`, a different operator.

## B. Stationarity identities [mine, from the definitions]

Preliminaries.
1. Linearised frame equation. Quadratic part of (04:60-63): av_{x,y,o}|H_x+I(x->y;o)-H_y|^2. Variation in H_x gives 2H_x-2av_yH_y+av_{y,o}[I(x->y;o)-I(y->x;o)]=0; route reversal permutes the orders (04:109), so av_oI(y->x;o)=-av_oI(x->y;o), hence H_x-av H=-av_{y,o}I(x->y;o), as stated at 05:984-985. tau(r)=-av I(r->r') has zero mean by the same antisymmetry, so H_r=tau(r)-tau(0). OK.
2. Q=M+d_{0,c}R. Linearising (04:176-179): log Y_{e,z} ~ H_{y,z}+sum_r a_mu(Ly+z+re_mu)-H_{y+e_mu,z}; the w^av-average and the projection to G (first order = average) give Ma-d_{0,c}(sum_z w_zH_{.,z})=Ma+d_{0,c}Ra. OK.
3. On gradients: I_{d phi}(x->x')=phi(x')-phi(x), so tau_y(r)=phi(Ly+r)-av phi, H_{y,r}=phi(Ly+r)-phi(Ly), and (sum w=1)
   `R d_{0,f}phi = phi|_roots - M_0 phi`, where `(M_0phi)(y)=sum_z w(z)phi(Ly+z)`.
   Telescoping: `M d_{0,f}phi = d_{0,c}M_0phi`. Sum: `Q d_{0,f}phi=d_{0,c}(phi|_roots)`. This confirms the second identity of (05:989-991); it needs w = w^av and total mass one, both stated.
4. `K_f d_{0,f}=0` since d_1d_0=0 (05:39). `K_c d_{0,c}=0` and, K_c being symmetric, `d_{0,c}^*K_c=0`, so `Q^*K_c=M^*K_c+R^*d_{0,c}^*K_c=M^*K_c`.

W_s. From (05:529-534): K_fW=d_{1,f}^*H_fd_{1,f}W=d_{1,f}^*TH_cd_{1,c}=(T^*d_{1,f})^*H_cd_{1,c}=(d_{1,c}M)^*H_cd_{1,c}=M^*K_c. I also rechecked the symbol identities (05:506-511): with DR=I-x pi, R_lD_lF_{1,l}^*R=F_{1,l}^*R-pi_l^*conj(m_l)x^*R=F_{1,l}^*R (x^*R=0, R_lx_l=0); and sum_lF_{1,l}A_l=(D-b^{-1})R+x pi sum_l m_le_l=I-x pi-b^{-1}R+x pi=I-b^{-1}R, using sum_l m_le_l=1. So
- `K_fW_s=M^*K_c=Q^*K_c` TRUE; `MW_s=1-K_c/b` TRUE;
- `QW_s=1-K_c/b+d_{0,c}RW_s`: the rooted identity FAILS for W_s unless d_{0,c}RW_s=0. v3 only says "The second identity does require a gradient correction" (05:1092); non-vanishing of d_{0,c}RW_s is not proved (NOT DETERMINED, generically nonzero, immaterial).
- Normal equation of the actual energy (05:1066-1068) is K_fa=bQ^*(v-Qa). For W_s the right side is Q^*K_c-bQ^*d_{0,c}RW_s, so W_s is a minimiser of the M-energy, not of the actual Q-energy.

W_a. W_a-W_s=-d_{0,f}(ERW_s) is a fine gradient with root values (ERW_s)(Ly)=RW_s(y) by cardinality of phi. Hence
- `QW_a=MW_s+d_{0,c}RW_s-d_{0,c}RW_s=1-K_c/b` TRUE;
- `K_fW_a=K_fW_s=M^*K_c=Q^*K_c` TRUE; `d_{1,f}W_a=d_{1,f}W_s` TRUE;
- `MW_a=1-K_c/b-d_{0,c}M_0ERW_s`: the straight identity fails by a coarse gradient;
- normal equation: K_fW_a=Q^*K_c=bQ^*(1-QW_a). TRUE. (05:1112-1118) is correct as stated; the "by (ch05:actual-Q)" proof is complete once item 4 is supplied.

W_F. W_F-W_a=-d_{0,f}phi with phi=0 at roots, so `QW_F=QW_a`, `K_fW_F=K_fW_a`, curl unchanged; `MW_F=MW_a-d_{0,c}M_0phi`. Both rooted identities TRUE for W_F.

## C. W_F as derivative of the stationary map

Verdict: TRUE; the proof in v3 is a two-line sketch (05:1143-1150) which I completed:
- Existence/uniqueness of the gradient: each block has a spanning tree rooted at Ly with internal edges only (05:916-918), so phi(root)=0 and (W_av-d phi)=0 on tree edges determine phi at each site by summing W_av along the tree path from the root. Unique for a GIVEN forest. W_F depends on the forest.
- rep v vanishes on tree edges (05:929-930), so W_Fv-rep v is zero on tree edges, i.e. W_Fv=rep v+iota_F z.
- Differentiating D_psi f(v,rho(v))=0 at 0 and using (05:1066-1068): for all z', with a=rep v+iota_F D rho(0)v, <iota_F z', K_fa-bQ^*(v-Qa)>=0. W_Fv satisfies the unprojected equation K_fa=bQ^*(v-Qa) (part B), lies in the same affine slice, and the slice Hessian is >= c>0 (05:1073-1076), so a=W_Fv.
Hypotheses actually used: (i) the ASSUMED coefficient condition K_f=d^*H_fd, H_f>=eps (05:1052-1058), with the same metric and penalty as in the construction of W_s ("These hold for the same incoming metric and penalty", 05:1089 - asserted); (ii) the tree comparison (05:1035-1040), whose derivation from (05:1009-1014) and chapter 4 I did not re-verify; (iii) existence and differentiability of rho: Proposition ch05:stationary-prop (05:1166-1187) and ch05:actual-stationary (05:1321-1342), under the path bound (05:1245-1248); rho is holomorphic. At 05:1145 this is a forward reference ("Once a stationary graph ... has been constructed").
Scott B:529 gives the same argument in the same words ("exactly one such modification of W_0v has zero tree links. By coercivity it is the unique minimizer over the slice").

## D. Translation covariance (coarse translations, i.e. fine shifts by L a)

- M: covariant, evident from (05:155-158).
- R: COVARIANT, from the definition, not by plausibility. (05:979-981) uses only: the patch Ly+B_R ("Translate the preceding frame construction to every patch Ly+B_R", 04:172-173), the uniform average over r' in B_R and over all 24 orders o, coordinate-order paths, and the fixed weights w^av (04:186-188). None depends on y except by translation and none depends on the trees. So (R tau_{La}a)(y)=(Ra)(y-a). Supporting: "every such equation reads a translate of one fixed finite patch" (05:961-962); kernel covariance under "corresponding fine/coarse translations" (04:263-264).
- E: COVARIANT. (E tau_a h)(x)=sum_y phi(x/L-y-sk)h(y-a)=sum_{y'}phi((x-La)/L-y'-sk)h(y')=(Eh)(x-La). Range: phi supported in (-1,1)^4, so one coarse block.
- W_s: covariant by construction: kernel = coarse Fourier inversion of L^{-1}sum_l e^{i theta_l.r}A_l(p) (05:520-528), a function of (y-y',r). Its alias amplitudes are L^{-1}A_l.
- W_a: covariant as a composition; alias amplitudes exist.
- W_F: covariant IF the forest is invariant under coarse translations (then the tree-straightening map P_F commutes with them). v3 does NOT require this: 05:916-917 only says "in each centered block ... a spanning tree rooted at Ly"; v3 treats trees as variable: "finitely many ... local tree shapes" (05:964), "uniform in the period and in the allowed trees" (05:1041), "independent of the allowed period and block trees" (05:1327-1328), and 06-large-fields.tex:85-87 puts "a rooted spanning tree in every block" into the allocation sector. For a non-periodic forest W_F is not covariant and has no alias amplitudes. Chapter 4 does not fix any forest (no occurrence of trees there besides 04:296).
  Scott DOES fix it where needed: "Choose one reference tree and translate it over the cells. The map P_tree taking a fine field to that representative adds the gradient of its signed tree-path sums; at fixed ratio it is a finite-range map" (D-section:1197); B:437 "fix an axial spanning tree rooted at l y" (with "Section B-energy allows every rooted block-tree gauge"). This stipulation is absent from v3 chapter 5.

## E. Decay and locality

- W_s: 05:586-601 asserts exponentially weighted coarse coefficient bounds of order L^{-1-r} for nabla_f^rW, r<=j-2. [v3 states with a proof sketch relying on Proposition ch05:history-prop; not re-verified.]
- W_a: (05:1128-1132) `|nabla_f^rW_a(Ly+x,y')|<=C_{j,r}L^{-1-r}e^{-c_jd(y,y')}, r<=j-2`. Checked given the W_s bound: R has finite coarse range and row sum <=C_jL (05:995-997; average of routes of length O_j(L)); W_s kernel <=C_jL^{-1}e^{-cd}; RW_s is O_j(1) exponentially decaying; nabla^r d_{0,f}E costs C_rL^{-r-1} and one block of range. TRUE.
- W_F: v3 proves nothing; it says explicitly "Estimate (ch05:actual-bridge) is asserted for W_a, not for tree coordinates" (05:1151-1153) and "the fine-difference bounds apply to W_a" (05:1234). [mine] W_F=P_FW_a, where (P_Fa)_e=a_e-(phi(e_+)-phi(e_-)) and phi(x) is a signed sum of a over the tree path (<=L^4-1 edges) inside the block of x. So W_F(e,y') is a combination of at most 1+2L^4 entries W_a(e',y') with e' in the one or two blocks meeting e, whence |W_F(Ly+x,y')|<=C_{j,L}e^{-c_jd(y,y')}. Exponential locality ACROSS blocks is therefore provable in two lines for any forest, with an L-dependent constant; it is not in the text. Fine-difference bounds are false for W_F: it is 0 on tree edges and equals v+O(...) (size O(1), not L^{-1}) on crossing edges (rep v, 05:921-926). Compare 07-matching.tex:1117-1118 "even if the tree-gauge representative itself has poor difference bounds".

## F. Polynomial preservation

Proved only for W_s: 17mt:237-249, eq. (ch17:polynomial-response) `(W_sp)(x)_a=sum_{b,z}A_0^{ab}(z)p_b(x/L+z)`, `sum_zA_0^{ab}(z)=L^{-1}delta_{ab}`, for vector polynomials of degree < j, from vanishing to order j of the nonprincipal alias columns (17mt:221-232; factor conj(m_l), m_l=w_L(theta_l)^j). Chapter 5 contains no polynomial statement: 05:527-535 only defines W, T and the three identities, and 05:599-601 gives the degree-zero case ("At zero momentum the principal columns are I and the other columns vanish"). For W_a the text does not prove polynomial preservation; 17mt:263-274 transfers the result by fine gauge invariance of the source ("Its difference from W_s is a fine gradient"), with a BCH error. Not proved, and false in general, for W_F. I did not re-derive the order-j vanishing.

## G. 17-current-contraction.tex 46-68 and 110-114

Sentences:
 S1 (48-50) "Let W be the actual stationary tangent ... The first derivative of the nonlinear stationary substitution is this W".
 S2 (52-53) "Fine gauge changes of W have no effect on this quadratic calculation".
 S3 (55-62) K_f(k_l)N_l=A_lK_c with N_l "the alias amplitude of W", A_l the amplitude of the adjoint of the gauge-covariant block average.
 S4 (62-66) projected nonprincipal amplitude analytic and O(|p|^2); removed gradient killed.
 S5 (66-67) "The principal amplitude is analytic by the exponential locality of W."
 S6 (112-113) "The actual tangent may be replaced by the smooth representative W_a because the quadratic Ward identities kill its gradient correction."

- W=W_F: S1 literally TRUE (05:1148). S3 identity TRUE, but "alias amplitude of W_F" exists only for a translation-invariant forest, which v3 does not stipulate (Scott does). S5: exponential locality of W_F is not proved in chapter 5 (disclaimed at 05:1151-1153); it is easily supplied (part E). S6 TRUE and meaningful.
- W=W_a: S1 FAILS literally: by (05:1148) the derivative of the stationary substitution in the forest chart is W_F; W_a is "the smooth representative of the actual stationary tangent" (05:1234) and equals the derivative only up to a fine gradient (S2 then repairs this at the quadratic level; Scott B:781 says the stationary curve can be gauge-transformed to have the smooth tangent, v3 chapter 5 does not). S3, S4, S5 TRUE on the basis of chapter 5. S6 becomes a tautology.
- W=W_s: S1 FAILS (W_s is not stationary for the actual energy, QW_s != 1-K_c/b). S3 TRUE (K_fW_s=M^*K_c=Q^*K_c), S4, S5 TRUE. S6: W_s is not "the actual tangent"; the replacement itself is legitimate since W_s-W_a is a gradient.
No single choice makes every sentence literally correct from chapter 5 as written. Minimal repair: W=W_F with one reference tree translated over the blocks, plus the two-line locality remark; or define W up to fine gradients and use amplitudes of W_a (or W_s) throughout.

Naming inconsistency inside v3: 05:1234 and 05:1310-1311 call W_a the smooth representative and W_F the forest representative of the tangent; 07-matching.tex:574 and 17mt:263 say "The actual (stationary) tangent is W_a"; 09-stationary-remainder.tex:188-191 says the tangent of the physical stationary field is W_F.

## Not checked

- The analytic construction and decay bounds of W_s (05:540-601) and Proposition ch05:history-prop; the pole cancellations.
- The nonlinear tree inequality (05:1009-1014), its chapter-4 inputs, and hence the constants in (05:1035-1040); I only used the resulting gap.
- That the Hessian of the nonlinear action really is (05:1066-1068) (v3 assumes the coefficient condition).
- Propositions ch05:stationary-prop / ch05:actual-stationary beyond their statements.
- The order-j vanishing behind (ch17:polynomial-response); the Ward identities of E_b invoked in 17cc.
- Whether d_{0,c}RW_s is actually nonzero.
- Martin's texts (manuscript/existence) were not consulted; the comparison is with Scott only.
- No numerical check was run; all computations are by hand.
