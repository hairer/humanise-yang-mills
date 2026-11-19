# Independent review: comparison across stage boundaries

Reviewed `17-variable-windows.tex` against Chapter11's finite-arity and restart comparison interfaces.

- The accumulated pre-ratio linear cost is bounded by sup_j(log(2+C_j)/log L_j) times total logarithmic block length. This gives H^{o(1)} on the O(log H) window without restricting it to one or two stages.
- Both stopping overshoots are o(log H) under L_i<=log β_i. The number of steps is O(log H), within the restarted-history allowed window.
- Unequal actual response products telescope their conditional covariances; replacing them by a common stage covariance is neither required nor done.
- Requested and author added a quantitative actual coupling ratio bound H^{o(1)}(1+log H)/β, which is smaller than every fixed inverse H power. Mere qualitative o(1) would have been insufficient.
- Requested and author added the distinction that nonlinear propagation is the pre-ratio linear map plus an entry-controlled error. Fixed-L constants enter the latter additively and are not multiplied along the window.
- The full squarefree source, common corrected subset polynomial, marker-weight restoration, and bottom partition bound are preserved. Longest-window restart and top extraction give the same T for the finite/compact dilation requests; the parameter enters only bounded stopping ranges and explicit engineering dilations.

The revised statement is consistent with these supplied interfaces. Cross-reference check passes; no global compile performed by this agent.
