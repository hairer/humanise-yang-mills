# Chapters 12–13 (12, 13, 13sb, 13ba): vocabulary applied

Files (worktree `/Users/mgubi/ym-terminology`, branch `claude/v3-terminology-dictionary`, uncommitted, unstaged): `manuscript/HumanizeYM_v3/chapters/12-ultraviolet-limit.tex` (108 lines changed), `13-continuum-fields.tex` (35), `13-sharp-bounds.tex` (37), `13-bounded-approximations.tex` (81). Edits within lines only; every file keeps its line count. Edits made by script (`scratchpad/c5/apply.py` with `e12*.py`, `e13*.py`; logs `log*.json`), each replacement checked to occur exactly once in its line.

## Changes

### `12`

| line | before | after | decision / entry |
|---|---|---|---|
| 12:5 | `We keep the physical period $R_p$ fixed` | `We keep the period $R_p$ in continuum units fixed` | physical 1 (R) |
| 12:6 | `The level $m$ has spacing` | `The scale $m$ has spacing` | table: scale (level) |
| 12:10 | `stopping the marked evolution at an intermediate level,` | `stopping the evolution with insertions at an intermediate scale,` | mark 1 (R); table: scale |
| 12:11 | `independent of that level.` | `independent of that scale.` | table: scale |
| 12:13 | `The common trajectory of Chapter~\ref{ch10:trajectory} and the` | `The construction of Chapter~\ref{ch10:trajectory} and the` | trajectory 2 (R) |
| 12:14 | `marked estimates of Chapter~\ref{ch11:insertions} supply the stability` | `estimates with insertions of Chapter~\ref{ch11:insertions} give the stability` | mark 1 (R); supplies (R) |
| 12:19 | `Fixed-level convergence data` | `Fixed-scale convergence data` | table: scale (title) |
| 12:22 | `and distinct physical origins.` | `and distinct insertion points in continuum units.` | origins / insertion origins (R); physical 1 (R) |
| 12:23 | `At a fixed level $m$ above their reference levels, use one dictionary` | `At a fixed scale $m$ above their reference scales, use one common index set` | table: scale; reference label (D); dictionary (R/I), as ch. 10 |
| 12:24 | `large-field inventories for all` | `prescribed large-field sets for all` | inventory (R) |
| 12:25 | `All small-field event indicators and eligibility criteria in this dictionary are` | `All indicators of small-field events and eligibility conditions in this index set are` | event indicator (R); eligible 2 (D), ch. 4 wording; dictionary |
| 12:26 | `fixed at level $m$. A large-field profile is the sum of activities` | `fixed at scale $m$. A \emph{total large-field activity} is the sum of activities` | table: scale; large-field profile (D), short term |
| 12:27 | `prescribed set of large-field sites; the original activity` | `prescribed large-field set; the original activity` | prescribed set of large-field sites (D) |
| 12:28 | `list can be infinite even though the number of such profiles on a` | `list can be infinite even though the number of such sums on a` | large-field profile (D) |
| 12:31 | `The required background convergence consists of` | `The required convergence of the action data consists of` | background convergence (R) |
| 12:33 | `the regular and large-field activity arrays in` | `the arrays of localized terms and large-field activities in` | table: localized term (regular activity) |
| 12:35 | `For the marked transformation we need` | `For the step with insertions we need` | mark 1 (R); table: step |
| 12:36 | `at each fixed level, applying` | `at each fixed scale, applying` | table: scale |
| 12:37 | `the cutoff-dependent marked map to any fixed admissible remainder` | `the cutoff-dependent step with insertions to any fixed admissible remainder` | mark 1 (R); table: step |
| 12:38 | `graph gives Cauchy output graphs` | `graph (Section~\ref{ch12:graphs}) gives Cauchy output graphs` | admissible 2 (D): define before first use (forward reference) |
| 12:40 | `For the common construction, Theorem~\ref{ch10:convergence} supplies` | `For the cutoff-independent construction, Theorem~\ref{ch10:convergence} gives` | common 3 (R); supplies (R) |
| 12:41 | `the background limits. The marked estimates and fixed-input comparison` | `the limits of the action data. The estimates with insertions and fixed-input comparison` | background convergence (R); mark 1 (R) |
| 12:42 | `supply the corresponding single-insertion` | `give the corresponding single-insertion` | supplies (R) |
| 12:48 | `obey a common bound at width` | `obey a common bound at decay rate` | width 1 (D) |
| 12:54 | `rather than all walks of a given length` | `rather than all paths of a given length` | walk (R at 12:53-54) |
| 12:62 | `convergence in the smaller width $v$. A strict width reserve makes` | `convergence in the smaller decay rate $v$. A strict margin in the decay rate makes` | width 1 (D); reserve (R) |
| 12:63 | `sufficient for the actual` | `sufficient for the` | actual 1 |
| 12:67 | `Contraction of the complete marked remainder` | `Contraction of the full remainder with insertions` | complete (R); mark 1 (R) (title) |
| 12:71 | `arrays at level $m$.` | `arrays at scale $m$.` | table: scale |
| 12:75 | `actual level-$m$ large-field bound` | `scale-$m$ large-field bound` | actual 1; table: scale |
| 12:78 | `of each large-field profile is a` | `of each total large-field activity is a` | large-field profile (D) |
| 12:80 | `admissible majorant and then by taking its infimum.` | `majorant admitted in the infimum and then by taking the infimum.` | admissible 6 (R) |
| 12:90 | `coefficient map of one marked step` | `coefficient map of one step with insertions` | mark 1 (R) |
| 12:96 | `Suppose the marked step maps` | `Suppose the step with insertions maps` | mark 1 (R) |
| 12:97 | `and the common-support marked difference estimates give, for` | `and the difference estimates with insertions on common supports give, for` | mark 1 (R) |
| 12:115 | `for the complete regular and large-field` | `for the full regular and large-field` | complete (R) |
| 12:118 | `for the actual inserted density.` | `for the inserted density.` | actual 1 |
| 12:119 | `For the actual transformation,` | `For the step with insertions,` | actual 1 |
| 12:123 | `thresholds for the starting scales impose` | `lower bounds on the starting scales impose` | threshold for the starting scale (R), as ch. 10-11 |
| 12:126 | `at a strict width reserve and` | `at a strict margin in the decay rate and` | width 1 (D); reserve (R) |
| 12:131 | `Forgetting the terminal graph` | `Independence of the graph at the cutoff` | App. D (12:131); forgetting (R) |
| 12:133 | `For the selected trajectory, the graph contraction` | `For the construction of Chapter~\ref{ch10:trajectory}, the graph contraction` | trajectory 2 (R) |
| 12:135 | `normalized at one reference level are Cauchy` | `normalized at one reference scale are Cauchy` | reference label (D): reference scale |
| 12:136 | `at every fixed level.` | `at every fixed scale.` | table: scale |
| 12:147 | `The coefficient at its reference level` | `The coefficient at its reference scale` | reference label (D) |
| 12:148 | `For each subsequent fixed level solve` | `For each subsequent fixed scale solve` | table: scale |
| 12:150 | `at this fixed level.` | `at this fixed scale.` | table: scale |
| 12:160 | `Consequently the complete functions multiplying a single source $f_{i,N,m}(U)$ and` | `Consequently the full functions multiplying a single source variable $f_{i,N,m}(U)$ and` | complete (R); source 1 (D) |
| 12:161 | `large-field profiles linear in the sources $k_{i,N,m,Q}(U)$` | `total large-field activities of source degree one $k_{i,N,m,Q}(U)$` | large-field profile (D); terms linear in the sources (R) |
| 12:162 | `its exact prescribed set of large-field sites.` | `its exact prescribed large-field set.` | prescribed set of large-field sites (D) |
| 12:163 | `Multiplication by a fixed Borel event indicator preserves` | `Multiplication by the indicator of a fixed Borel event preserves` | event indicator (R) |
| 12:164 | `no continuity of the event indicator as` | `no continuity of this indicator as` | event indicator (R) |
| 12:166 | `The scalar normalization cancels` | `The normalization constant cancels` | scalar 1 (D) (title) |
| 12:169 | `for the actual positive density` | `for the positive density` | actual 1 |
| 12:170 | `its extensive scalar term` | `its extensive constant term` | scalar 1 (D) |
| 12:175 | `Haar measure. Background` | `Haar measure. Convergence` | background convergence (R) |
| 12:176 | `convergence makes` | `of the action data makes` | background convergence (R) |
| 12:178 | `Summing a rooted` | `Summing the norms of` | App. D (12:177-179); rooted (R) |
| 12:179 | `activity norm over the finitely many sites` | `\eqref{ch04:weighted-sums} over the finitely many sites` | App. D (12:177-179) |
| 12:180 | `of the regular sum and every large-field profile.` | `of the regular sum and every total large-field activity.` | large-field profile (D) |
| 12:181 | `in the latter profiles and fixed eligibility` | `in the latter activities and the fixed indicators of the` | large-field profile (D); eligible 2 (D), ch. 10 wording |
| 12:182 | `indicators. Its product` | `eligibility conditions. Its product` | eligible 2 (D) |
| 12:187 | `satisfies the level-$m$ cutoff.` | `satisfies the regularity condition at scale $m$.` | cutoff 3 (R); table: regularity condition |
| 12:189 | `uniformly on` | `uniformly for` | tail 1 (R) |
| 12:190 | `the cutoff tail. Since` | `all sufficiently large $N$. Since` | tail 1 (R) |
| 12:201 | `The exact marked density at level $m$ has` | `The exact density with insertions at scale $m$ has` | mark 1 (R); table: scale |
| 12:202 | `regular terms linear in the sources $\sum_i z_i f_i$, higher regular entries` | `regular terms of source degree one $\sum_i z_i f_i$, regular terms of source degree at least two` | terms linear in the sources (R); entry 2 (R) |
| 12:208 | `All insertion origins belong to its support. Keep the complete` | `All insertion points belong to its support. Keep the full` | insertion origins (R); complete (R) |
| 12:209 | `terms linear in the sources and set only these higher entries to zero.` | `terms of source degree one and set only these terms of higher source degree to zero.` | terms linear in the sources (R); entry 2 (R) |
| 12:219 | `grouped profiles and functions multiplying a single source,` | `grouped total large-field activities and functions multiplying a single source variable,` | large-field profile (D); source 1 (D) |
| 12:221 | `The same scalar` | `The same constant term` | scalar 1 (D) |
| 12:222 | `deleting terms involving at least two insertions does` | `deleting terms of source degree at least two does` | terms involving at least two insertions (R) |
| 12:223 | `the large-field profiles linear in the sources.` | `the total large-field activities of source degree one.` | large-field profile (D); terms linear in the sources (R) |
| 12:225 | `uniform in the stopping level` | `uniform in the stopping scale` | table: scale (title) |
| 12:229 | `counts a connected cover of` | `counts a connected covering of` | connected covering number (D) |
| 12:230 | `Suppose the physical origins belong to one common` | `Suppose the insertion points, in continuum units, belong to one common` | origins (R); physical 1 (R) |
| 12:231 | `Their separation at level $m$` | `Their separation at scale $m$` | table: scale |
| 12:233 | `choose a fixed base level $r$` | `choose a fixed base scale $r$` | table: scale |
| 12:234 | `to include all reference levels.` | `to include all reference scales.` | reference label (D) |
| 12:236 | `We use the following marked norm conclusion. Terms involving at least two insertions have rooted` | `We use the following conclusion for the norms with insertions. Terms of source degree at least two have incidence` | mark 1 (R); terms involving at least two insertions (R); rooted (R at 12:236) |
| 12:237 | `majorant sums at most one` | `bounds at most one` | rooted (R at 12:236) |
| 12:239 | `It retains all inventories and insertion origins.` | `It retains all prescribed large-field sets and insertion points.` | inventory (R); insertion origins (R) |
| 12:240 | `to the fixed base level,` | `to the fixed base scale,` | table: scale |
| 12:247 | `is the vacuum normalization bound;` | `is the per-site normalization exponent of \eqref{ch11:replicated-bound} at scale $r$;` | App. D (12:247), words only; vacuum normalization bound (R) |
| 12:247 | `the terms linear in the sources;` | `the terms of source degree one;` | terms linear in the sources (R) |
| 12:248 | `bounds their weighted large-field profile sums.` | `bounds their weighted sums of total large-field activities.` | large-field profile (D) |
| 12:249 | `chosen uniformly on the cutoff tail: the fixed-level coefficients linear in the sources are bounded` | `chosen uniformly for all sufficiently large $N$: the fixed-scale coefficients of source degree one are bounded` | tail 1 (R); table: scale; terms linear in the sources (R) |
| 12:251 | `the later stopping level $m$.` | `the later stopping scale $m$.` | table: scale |
| 12:252 | `concern the complete actual marked transfer.` | `concern the full transfer with insertions.` | complete (R); actual 1; mark 1 (R) |
| 12:253 | `the estimate for terms involving at least two insertions` | `the estimate for terms of source degree at least two` | terms involving at least two insertions (R) |
| 12:257 | `Removal of terms involving at least two insertions` | `Removal of terms of source degree at least two` | terms involving at least two insertions (R) (title) |
| 12:259 | `Under these marked norm and transfer bounds,` | `Under these norm and transfer bounds with insertions,` | mark 1 (R) |
| 12:265 | `the cutoff threshold can` | `the lower bound on $N$ can` | threshold 3 (R), as ch. 11 |
| 12:269 | `containing two origins separated by $B_m^2$ has cover` | `containing two insertion points separated by $B_m^2$ has covering` | origins (R); connected covering number (D) |
| 12:277 | `Transport the entire modified marked density to $r$.` | `Transfer the entire modified density with insertions to $r$.` | transport 3 (R); mark 1 (R) |
| 12:277 | `The support` | `The margin in the support` | reserve (R) |
| 12:278 | `reserve allows its first` | `exponent allows its first` | reserve (R) |
| 12:279 | `coefficients linear in the sources are unchanged. If a source monomial contains $q$ origins,` | `coefficients of source degree one are unchanged. If a source monomial contains $q$ insertions,` | terms linear in the sources (R); origins (R) |
| 12:282 | `This is the weight reserve needed when using the marked transfer.` | `This is the margin in the source weights needed for the transfer with insertions.` | reserve (R); mark 1 (R) |
| 12:288 | `after grouping the finitely many support and prescribed-site profiles,` | `after grouping into the finitely many total large-field activities,` | large-field profile (D) |
| 12:293 | `actual cutoff moment and` | `actual lattice correlation at the cutoff and` | moment 1 (D) |
| 12:298 | `For the selected trajectory, the correlations` | `For the construction of Chapter~\ref{ch10:trajectory}, the correlations` | trajectory 2 (R) |
| 12:352 | `The union of the nested physical lattices is dense here.` | `The union of the nested lattices, in continuum units, is dense here.` | physical 1 (R) |
| 12:353 | `supply Proposition~\ref{ch12:dense-cauchy}; the all-order separated` | `are covered by Proposition~\ref{ch12:dense-cauchy}; the all-order separated` | supplies (R) |
| 12:354 | `finite-difference bounds supply the other hypothesis.` | `finite-difference bounds give the other hypothesis.` | supplies (R) |
| 12:359 | `The difference hypothesis is supplied by` | `The difference hypothesis is given by` | supplies (R) |
| 12:363 | `compact set on the cutoff tail.` | `compact set for all sufficiently large $N$.` | tail 1 (R) |
| 12:370 | `For the common selected trajectory with the strengthened stage` | `For the cutoff-independent construction with the strengthened stage` | trajectory 2 (R); common 3 (R) |
| 12:374 | `at every fixed physical period.` | `at every fixed period.` | physical 1 (R); period (keep) |
| 12:382 | `divided by their physical step` | `divided by their step` | physical 1 (R) |
| 12:383 | `lengths. Their` | `lengths in continuum units. Their` | physical 1 (R) |
| 12:384 | `which holds on a cutoff tail.` | `which holds for all sufficiently large $N$.` | tail 1 (R) |
| 12:395 | `The convergence threshold in this theorem` | `The lower bound on $N$ in this theorem` | threshold 3 (R) |
| 12:400 | `infinite-volume extraction.` | `infinite-volume limit along a subsequence.` | extraction 3 (R) |
| 12:402 | `supported away from collisions.` | `supported away from coincident points.` | collision (R); lesson 11d |

### `13`

| line | before | after | decision / entry |
|---|---|---|---|
| 13:5 | `on each fixed physical torus.` | `on each fixed torus.` | physical 1 (R); period (keep) |
| 13:15 | `Compactness gives the volume extraction;` | `Compactness gives the subsequence of volumes;` | extraction 3 (R) |
| 13:27 | `The cutoff threshold used to prove` | `The lower bound on $N$ used to prove` | threshold 3 (R), as ch. 11 |
| 13:31 | `Arzel\`a--Ascoli and diagonal extraction` | `Arzel\`a--Ascoli and a diagonal argument` | extraction 3 (R) |
| 13:32 | `give one refinement $P(k)=p(q(k))$` | `give one subsequence $P(k)=p(q(k))$` | refinement (R) |
| 13:52 | `Every further volume` | `Every further subsequence of volumes` | refinement (R) |
| 13:53 | `refinement preserves` | `preserves` | refinement (R) |
| 13:58 | `the distinguished unit and` | `the distinguished identity field and` | unit 1 (R); table: identity field |
| 13:81 | `For a tiling of physical` | `For a tiling of` | physical 1 (R) |
| 13:82 | `side $a$, the translations` | `side $a$ in continuum units, the translations` | physical 1 (R) |
| 13:83 | `anchors within distance $w$` | `insertion points within distance $w$` | anchor 4 (R) |
| 13:86 | `Anchors with pairwise` | `Insertion points with pairwise` | anchor 4 (R) |
| 13:89 | `anchors separated by more than` | `insertion points separated by more than` | anchor 4 (R) |
| 13:132 | `in every slot.` | `in every argument.` | slot 2 (R) |
| 13:138 | `after a coefficient refinement. More` | `after a further subsequence for the coefficients. More` | refinement (R) |
| 13:139 | `precisely, diagonal extraction over` | `precisely, a diagonal argument over` | extraction 3 (R) |
| 13:141 | `A further volume` | `A further subsequence of volumes` | refinement (R) |
| 13:142 | `refinement makes those limits` | `makes those limits` | refinement (R) |
| 13:143 | `below use these refined ordered tails.` | `below use the ordered tails of these subsequences.` | refinement (R) |
| 13:159 | `bounded rows have uniformly subpower inverse terminal` | `bounded vectors have uniformly subpower cutoff-scale` | row 7 (R); inverse terminal coordinates (R), ch. 11 short term |
| 13:160 | `supplies every spectator` | `gives every spectator` | supplies (R) |
| 13:162 | `gives the actual finite-cutoff matrices` | `gives the finite-cutoff matrices` | actual 1 |
| 13:165 | `in the same coefficient refinement.` | `in the same subsequence for the coefficients.` | refinement (R) |
| 13:206 | `A common cluster point` | `A common limit point` | cluster 1 (R) |
| 13:211 | `at the same cluster point` | `at the same limit point` | cluster 1 (R) |
| 13:217 | `has subpower inverse terminal coordinates` | `has subpower cutoff-scale coordinates` | inverse terminal coordinates (R) |
| 13:236 | `and the fixed translated-stencil` | `and the factor contributed by the fixed translated stencil` | cost 1 (R) |
| 13:237 | `cost is bounded by the coupling-threshold requirements used in` | `is bounded by the lower bounds on the reference coupling used in` | cost 1 (R); coupling threshold (R) |
| 13:239 | `Trial descent yields` | `The backward comparison yields` | trial descent (R); backward comparison (R) |
| 13:272 | `Each identity follows by testing against every spectator and using` | `Each identity follows by pairing with every spectator and using` | test 2 (R) |
| 13:295 | `the moving test functions` | `the cutoff-dependent test functions` | moving 1 (R) |
| 13:303 | `every sufficiently fine fixed level $k$.` | `every sufficiently fine fixed scale $k$.` | table: scale |
| 13:367 | `have at most $2n$ residue patterns modulo the side-$a_m$ tiling,` | `lie in at most $2n$ classes modulo the side-$a_m$ tiling,` | App. D (13:366-367), words only; residue patterns (I/S) |
| 13:388 | `A cutoff threshold uniform in` | `A lower bound on $N$ uniform in` | threshold 3 (R) |
| 13:391 | `This estimate is the input for bounded slab insertions in the` | `This estimate is the hypothesis needed for bounded slab insertions in the` | inputs 2 (R) |
| 13:394 | `admissible trial encoding,` | `the reference labels of admissible trials,` | trial encoding (R), without the symbol (lesson 11a) |
| 13:396 | `family. Full` | `family of measures. Full` | App. D (13:395-396), 'selected' kept per assignment |

### `13sb`

| line | before | after | decision / entry |
|---|---|---|---|
| 13sb:9 | `Gaussian comparison used for rank detection.` | `Gaussian comparison used for the separating families.` | detection (I; table: separating family) |
| 13sb:10 | `all incoming joint marked components;` | `all incoming joint components with insertions;` | mark 1 (R) |
| 13sb:11 | `terms linear in the sources would` | `terms of source degree one would` | terms linear in the sources (R) |
| 13sb:16 | `The stage ratio and coupling threshold may be chosen` | `The stage ratio and the lower bound on the reference coupling may be chosen` | coupling threshold (R) |
| 13sb:25 | `the per-site normalization cost of` | `the per-site normalization exponent of` | vacuum normalization bound (R); cost 3 (R) |
| 13sb:26 | `it is not a marked density or the scalar coupling correction.` | `it is not a density with insertions or the coupling constant renormalization.` | mark 1 (R); scalar 3 (D); table: coupling constant renormalization |
| 13sb:27 | `For the admissible path-action representation one can use` | `For the path-action representation of the density one can use` | App. D (13sb:27), without the symbol (lesson 11a) |
| 13sb:29 | `Indeed the scalar-free exponent` | `Indeed the exponent without its constant term` | scalar 1 (D) |
| 13sb:36 | `activity site sum have their admissible bounds.` | `activity site sum satisfy the bounds \eqref{ch04:activity-bounds}.` | App. D (13sb:36) |
| 13sb:36 | `The Haar-ball argument` | `The lower bound for the partition function` | Haar-ball normalization argument (R) |
| 13sb:37 | `therefore costs only` | `therefore adds only` | cost 2 (R) |
| 13sb:38 | `$C_{J(i)}V+2D_GV\log\widehat\beta_i$, where` | `$C_{J(i)}V+2D_GV\log\widehat\beta_i$ to the exponent, where` | cost 2 (R) |
| 13sb:41 | `compatible with sufficiently large coupling thresholds.` | `compatible with sufficiently large lower bounds on the reference coupling.` | coupling threshold (R) |
| 13sb:45 | `then increase the coupling threshold until` | `then increase the lower bound on the reference coupling until` | coupling threshold (R) |
| 13sb:46 | `The same threshold choice gives` | `The same choice gives` | coupling threshold (R) |
| 13sb:63 | `its counterpart constrained to cover the prescribed large-field sites,` | `its counterpart with a prescribed large-field set,` | prescribed set of large-field sites (D), ch. 10 wording |
| 13sb:65 | `multiplication of the \emph{complete} source by` | `multiplication of the \emph{full} insertion by` | complete (R); source 4 (R) |
| 13sb:66 | `for its regular term linear in the sources` | `for its regular term of source degree one` | terms linear in the sources (R) |
| 13sb:67 | `for its large-field term linear in the sources` | `for its large-field term of source degree one` | terms linear in the sources (R) |
| 13sb:71 | `for terms involving at least two insertions retain every` | `for terms of source degree at least two retain every` | terms involving at least two insertions (R) |
| 13sb:72 | `Decreasing all mark` | `Decreasing all source` | mark 4 (R/I): source weight |
| 13sb:73 | `weights only decreases their absolute mode sums.` | `weights only decreases their sums of absolute coefficients.` | mode (R) |
| 13sb:74 | `at the intervening levels` | `at the intervening scales` | table: scale |
| 13sb:84 | `It holds on a full cutoff tail uniformly` | `It holds for all sufficiently large $N$ uniformly` | tail 1 (R) |
| 13sb:85 | `whenever the reflected anchors at the stopping level have spacing` | `whenever the reflected insertion points at the stopping scale have spacing` | anchor 4 (R); table: scale |
| 13sb:86 | `stays adequate at finer levels because` | `stays adequate at finer scales because` | table: scale |
| 13sb:104 | `as the first level $k\ge m$` | `as the first scale $k\ge m$` | first-below scale (R); table: scale |
| 13sb:111 | `If the first level already qualifies` | `If the first scale already qualifies` | table: scale |
| 13sb:112 | `the fixed-stage cost bound.` | `the fixed-stage bound.` | cost 3 (R) |
| 13sb:136 | `use its selected` | `use its chosen` | selected 9 (R) |
| 13sb:137 | `fixed stopping level and` | `fixed stopping scale and` | table: scale |
| 13sb:138 | `The fixed lattice stencil becomes interior at every fixed physical cell` | `The fixed link support becomes interior at every fixed cell` | stencil (R), ch. 11 link support; physical 1 (R) |
| 13sb:139 | `scale as $N\to\infty$. Translation covariance makes the threshold` | `scale in continuum units as $N\to\infty$. Translation covariance makes the lower bound on $N$` | physical 1 (R); threshold 3 (R) |
| 13sb:145 | `gives a sharper first-below-scale estimate` | `gives a sharper estimate of the first scale below a length` | first-below scale (R) |
| 13sb:147 | `be the first level with` | `be the first scale with` | first-below scale (R) |
| 13sb:155 | `iteration of first-below choices` | `iteration of such choices of a first scale` | first-below scale (R) |
| 13sb:157 | `mutually separated anchors,` | `mutually separated insertion points,` | anchor 4 (R) |
| 13sb:159 | `away from all anchors.` | `away from all insertion points.` | anchor 4 (R) |

### `13ba`

| line | before | after | decision / entry |
|---|---|---|---|
| 13ba:7 | `the physical normalization of a local field` | `the dimensionful normalization of a local field` | physical 2 (R) |
| 13ba:8 | `at one fixed coarse level and` | `at one fixed coarse scale and` | table: scale |
| 13ba:11 | `the precise marked estimate` | `the precise estimate with insertions` | mark 1 (R) |
| 13ba:12 | `with every term involving at least two insertions` | `with every term of source degree at least two` | terms involving at least two insertions (R) |
| 13ba:14 | `level $h$, write` | `scale $h$, write` | table: scale |
| 13ba:15 | `for the ordinary norm bound` | `for the small-field norm bound` | ordinary 1 (R) |
| 13ba:16 | `for its complete bound, including the complementary large-field` | `for its full bound, including the large-field` | complete (R); complementary 1 (R/I) |
| 13ba:17 | `For the selected trajectory these bounds` | `For the construction of Chapter~\ref{ch10:trajectory} these bounds` | trajectory 2 (R), as ch. 12 |
| 13ba:29 | `cell tiling at level $k$` | `cell tiling at scale $k$` | table: scale |
| 13ba:30 | `selected level-$h$ polynomial` | `selected scale-$h$ polynomial` | table: scale ('selected' kept per assignment; App. D 13ba:30 not applied) |
| 13ba:32 | `and the physical period.` | `and the period.` | physical 1 (R); period (keep) |
| 13ba:36 | `the local smooth cutoff` | `the small-field indicator` | App. D second round (13ba:36) |
| 13ba:37 | `is identically one on the ordinary chart, so its ordinary derivative` | `is identically one on the small-field chart, so its small-field derivative` | ordinary 1 (R) |
| 13ba:39 | `by a larger coupling threshold as in` | `by a larger lower bound on the reference coupling as in` | coupling threshold (R) |
| 13ba:43 | `a small coefficient linear in the sources.` | `a small coefficient of source degree one.` | terms linear in the sources (R) |
| 13ba:44 | `We prove its complete marked version next.` | `We prove its full version with insertions next.` | complete (R); mark 1 (R) |
| 13ba:50 | `after the finite coupling-threshold requirements` | `after the finite lower bounds on the reference coupling` | coupling threshold (R) |
| 13ba:52 | `terms involving at least two insertions retained.` | `terms of source degree at least two retained.` | terms involving at least two insertions (R) |
| 13ba:56 | `At level $i$, choose` | `At scale $i$, choose` | table: scale |
| 13ba:57 | `a term linear in the sources with complete normalized` | `a term of source degree one with full normalized` | terms linear in the sources (R); complete (R) |
| 13ba:61 | `the complete adjacent comparison constant` | `the full adjacent comparison constant` | complete (R) |
| 13ba:67 | `the global section and its complementary` | `the global section and its large-field` | complementary 1 (R/I) |
| 13ba:68 | `cutoff part; this symbol` | `part; this symbol` | complementary 1 (R/I) |
| 13ba:69 | `the incidence sum for terms linear in the sources below` | `the incidence sum for terms of source degree one below` | terms linear in the sources (R) |
| 13ba:71 | `before the physical factor` | `before the dimensionful factor` | physical 2 (R) |
| 13ba:77 | `the original large-field suppression` | `the original large-field decay factor` | suppression (R) |
| 13ba:78 | `is reserved separately in` | `is kept aside separately in` | reserve (R), as ch. 11 |
| 13ba:83 | `the coupling thresholds, since` | `the lower bounds on the reference coupling, since` | coupling threshold (R) |
| 13ba:101 | `the single schedule of coupling thresholds.` | `the single schedule of lower bounds on the reference coupling.` | coupling threshold (R) |
| 13ba:111 | `at successive levels is` | `at successive scales is` | table: scale |
| 13ba:120 | `normalized cost at most` | `normalized size at most` | cost 3 (R) |
| 13ba:122 | `and the physical factor $L_i^d$.` | `and the dimensionful factor $L_i^d$.` | physical 2 (R) |
| 13ba:123 | `Thus its terminal source satisfies` | `Thus its terminal insertion satisfies` | source 4 (R) |
| 13ba:124 | `and its complete push to $h$ is available` | `and its full image under the block maps down to $h$ is available` | complete (R); push (R) |
| 13ba:126 | `for its terms involving at least two insertions, including those` | `for its terms of source degree at least two, including those` | terms involving at least two insertions (R) |
| 13ba:131 | `$r\ge2$ distinct marked ancestors, then` | `$r\ge2$ distinct ancestors of insertion points, then` | mark 2 (R) |
| 13ba:140 | `for terms involving at least two insertions at level $i$, and impose` | `for terms of source degree at least two at scale $i$, and impose` | terms involving at least two insertions (R); table: scale |
| 13ba:144 | `Reserve four units of the incoming $A_{i+1}$ norm` | `Keep aside four units of the incoming $A_{i+1}$ norm` | reserve (R) |
| 13ba:148 | `reserves. Thus` | `margins. Thus` | reserve (R) |
| 13ba:149 | `the bounds for terms linear in the sources small enough` | `the bounds for terms of source degree one small enough` | terms linear in the sources (R) |
| 13ba:151 | `for both arrays of terms involving at least two insertions.` | `for both arrays of terms of source degree at least two.` | terms involving at least two insertions (R) |
| 13ba:153 | `its complete original prescribed set of large-field sites, not as a product of its coefficients linear in the sources. The terminal joint construction reserves the original` | `its full original prescribed large-field set, not as a product of its coefficients of source degree one. The terminal joint construction keeps aside the original` | complete (R); prescribed set of large-field sites (D); terms linear in the sources (R); reserve (R) |
| 13ba:154 | `decay for the complementary factors.` | `decay for the large-field parts of the insertions.` | complementary 1 (R/I) |
| 13ba:155 | `at the intermediate level $h$.` | `at the intermediate scale $h$.` | table: scale |
| 13ba:157 | `At that level insert` | `At that scale insert` | table: scale |
| 13ba:158 | `is the complete pushed negative source,` | `is the full transferred negative insertion,` | complete (R); push (R); source 4 (R) |
| 13ba:163 | `entry linear in the sources. All regular terms involving at least two insertions and all original large-field` | `term of source degree one. All regular terms of source degree at least two and all original large-field` | entry 2 (R); terms linear in the sources / involving at least two insertions (R) |
| 13ba:164 | `The scalar part is exactly` | `The constant term is exactly` | scalar 1 (D) |
| 13ba:165 | `The nonconstant part multiplied by the smooth cutoff has zero complementary profile because` | `The nonconstant part multiplied by the small-field indicator has no large-field part, because` | App. D (13ba:165, both repairs); profile 1 (D) |
| 13ba:167 | `the new term linear in the sources precisely` | `the new term of source degree one precisely` | terms linear in the sources (R) |
| 13ba:170 | `Descend this whole polynomial to $m$. Its regular terms linear in the sources have` | `Transfer this whole polynomial down to $m$. Its regular terms of source degree one have` | descent 1 (R); terms linear in the sources (R) |
| 13ba:171 | `large-field terms linear in the sources have bound at most one, and its two incidence bounds for terms involving at least two insertions` | `large-field terms of source degree one have bound at most one, and its two incidence bounds for terms of source degree at least two` | terms linear in the sources / involving at least two insertions (R) |
| 13ba:173 | `is the cell census and` | `is the set of cells and` | cell census (R) |
| 13ba:185 | `separately pushed densities` | `separately transferred densities` | push (R) |
| 13ba:194 | `once the cones have the room verified` | `provided the cones lie inside the cells, as verified` | room (R) |
| 13ba:212 | `At a finer level $h$` | `At a finer scale $h$` | table: scale |
| 13ba:219 | `The scalar part is retained` | `The constant term is retained` | scalar 1 (D) |
| 13ba:220 | `the relaxed small-field condition.` | `the relaxed regularity condition.` | relaxed (D); ch. 4 wording |
| 13ba:226 | `fine links to level $h$` | `fine links to scale $h$` | table: scale |
| 13ba:229 | `to choose a gauge-covariant block average or gauge` | `to choose a gauge-covariant averaging operation or local gauge` | table: averaging operation; frame 1 (R) |
| 13ba:230 | `frame. Conditional` | `transformation. Conditional` | frame 1 (R) |
| 13ba:230 | `independent primitive` | `independent auxiliary` | primitive 4 (R) |
| 13ba:233 | `at every intermediate level.` | `at every intermediate scale.` | table: scale |
| 13ba:241 | `after a shared frame choice has been` | `after a shared choice of local gauge transformation has been` | frame 1 (R) |
| 13ba:244 | `each endpoint frame reads a box of` | `the local gauge transformation at each endpoint reads a box of` | frame 1 (R) |
| 13ba:246 | `the connector paths stay` | `the paths of the transporters stay` | connector (D), ch. 4 short term |
| 13ba:247 | `every shared frame seed for an output` | `every auxiliary random variable for an output` | shared frame seed (R) |
| 13ba:248 | `lies within physical distance $(j_i+7)a_i$ of` | `lies within distance $(j_i+7)a_i$, in continuum units, of` | physical 1 (R) |
| 13ba:251 | `$r_d$ in level-$h$ units,` | `$r_d$ in lattice units of scale $h$,` | table: scale |
| 13ba:258 | `late levels.` | `late scales.` | table: scale |
| 13ba:260 | `permitted adjacent pairs, require` | `permitted stage pairs, require` | adjacent pair 2 (S), ch. 10 short term |
| 13ba:264 | `The finitely many initial levels` | `The finitely many initial scales` | table: scale |
| 13ba:270 | `each reflected level-$k$ cell. The cones, including their shared seeds,` | `each reflected scale-$k$ cell. The cones, including their auxiliary random variables,` | table: scale; shared frame seed (R) |
| 13ba:271 | `sufficiently large physical` | `sufficiently large` | physical 1 (R) |
| 13ba:272 | `periods prevent` | `periods in continuum units prevent` | physical 1 (R) |
| 13ba:283 | `Replicate the discrepancies before applying the kernel. At level $h$` | `Place a copy of the discrepancy in each reflected cell before applying the kernel. At scale $h$` | replicate (R); table: scale |
| 13ba:284 | `multiply the complete source density, including its` | `multiply the full density with insertions, including its` | complete (R); source 4 (R), as ch. 11 |
| 13ba:285 | `terms involving at least two insertions. Equation` | `terms of source degree at least two. Equation` | terms involving at least two insertions (R) |
| 13ba:305 | `holds on a cofinal set of` | `holds for arbitrarily fine` | cofinal grids (R) |
| 13ba:307 | `approximation thresholds may depend` | `the lower bounds on $N$ for the approximation may depend` | threshold 3 (R) |
| 13ba:310 | `Choose the grid level after` | `Choose the grid scale after` | table: scale |
| 13ba:311 | `level, then fix a generic` | `scale, then fix a generic` | table: scale |
| 13ba:336 | `initial lower-level request gives the required cofinal grids.` | `initial lower-scale request gives the required arbitrarily fine grids.` | table: scale; cofinal grids (R); 'request' kept per assignment |
## First-use sentences added

None. No term of the table has its first use in the book in these files with a difference from Bałaban still to be stated (step, scale, averaging operation, regularity condition, localized term, critical configuration, history, stage, Taylor localization are all covered in chapters 4–11). A forward reference "(Section~\ref{ch12:graphs})" was added at 12:38, because "admissible remainder graph" is used there 45 lines before its definition at 12:82 (entry *admissible* 2, D: "define before first use"). The graph-transform sentence stands at 11:380 and was not repeated; "graph" is used as is.

## Short terms introduced

| term | defining sentence | line |
|---|---|---|
| *total large-field activity* (for "large-field profile"; entry *large-field profile* / *profile* 1, D, proposal "total large-field activity with given support and large-field set") | "A \emph{total large-field activity} is the sum of activities having one particular support and prescribed large-field set; …" | 12:26–27; used at 12:78, 161, 180–181, 219, 223, 248, 288 |

Used as defined elsewhere (no new definition): *source degree* (11:134: "of source degree one / at least two" throughout, 42 places); *with insertions* (marked); *insertion point(s)* (anchors, origins); *cutoff-scale coordinates* (11:885; at 13:159, 217); *reference scale*; *lower bound on the reference coupling* (11, 10); *lower bound on the starting scale(s)* (12:123); *lower bound on $N$* (11:1119; for cutoff/convergence/approximation thresholds); *prescribed large-field set*; *link support* (13sb:138); *large-field part*; *margin* / *keep aside* (reserve); *transfer* (transport, push, descend); *transporter* (ch. 4, for connector); *local gauge transformation* (frame); *averaging operation* (block average); *stage pairs* (ch. 10, for adjacent pairs); *relaxed regularity condition* (ch. 4); *backward comparison* (ch. 11 section title, for "trial descent"); *coupling constant renormalization* (scalar coupling correction); *in continuum units*, *dimensionful* (physical 1, 2); *identity field* (unit).

## Dictionary words applied that are not in the table of word choices

| word replaced | word used | occurrences |
|---|---|---|
| terms linear in the sources / higher entries / entry linear in the sources (R) | (terms) of source degree one | 19 (plus 2 "higher entries" → "terms of source degree at least two") |
| terms involving at least two insertions (R) | (terms) of source degree at least two | 13 |
| marked (*mark* 1, R) | with insertions | 18 lines (20 occurrences of "marked" removed, incl. mark 2) |
| marked ancestors (*mark* 2, R) | ancestors of insertion points | 1 (13ba:131) |
| mark weights (*mark* 4) | source weights | 1 (13sb:72) |
| mode sums (R) | sums of absolute coefficients | 1 (13sb:73) |
| physical origins, insertion origins, origins (R) | insertion points | 6 (12:22, 208, 230, 239, 269, 279 "insertions") |
| anchors (*anchor* 4, R) | insertion points | 6 (13:83, 86, 89; 13sb:85, 157, 159) |
| physical (1, R) | in continuum units; dropped before "period" | 13 (12:5, 22, 230, 352, 374, 382–383; 13:5, 81–82; 13sb:138–139; 13ba:32, 248, 271–272) |
| physical (2, R) | dimensionful | 3 (13ba:7, 71, 122) |
| complete (R) | full | 15 |
| actual (sense 1) | deleted, or "the step with insertions" | 8 (12:63, 75, 118, 119, 169, 252; 13:162) |
| dictionary (R/I) | common index set (ch. 10 word) | 2 (12:23, 25) |
| inventory (R) | prescribed large-field set | 2 (12:24, 239) |
| prescribed set of large-field sites / constrained to cover the prescribed large-field sites (D) | prescribed large-field set; with a prescribed large-field set | 4 (12:27, 162; 13sb:63; 13ba:153) |
| event indicator (R) | indicator of (small-field / Borel) events | 3 (12:25, 163, 164) |
| eligibility criteria / indicators (*eligible* 2, D) | eligibility conditions; indicators of the eligibility conditions (ch. 4, 10) | 2 (12:25, 181–182) |
| background convergence / background limits (R) | convergence of (limits of) the action data | 3 (12:31, 41, 175–176) |
| regular activity arrays (table: localized term) | arrays of localized terms | 1 (12:33) |
| common construction, common selected trajectory (*common* 3, R) | cutoff-independent construction | 2 (12:40, 370) |
| common / selected trajectory (*trajectory* 2, R) | the construction of Chapter~\ref{ch10:trajectory} | 4 (12:13, 133, 298; 13ba:17) |
| supply, supplies, supplied (R) | give(s), given, are covered by | 7 (12:14, 40, 42, 353, 354, 359; 13:160) |
| width (1, D) | decay rate | 3 (12:48, 62, 126) |
| width reserve, support reserve, weight reserve, reserve(s), reserved (R) | margin (in the decay rate / support exponent / source weights); keep aside | 8 (12:62, 126, 277–278, 282; 13ba:78, 144, 148, 153) |
| walks (R at 12:53–54) | paths | 1 |
| admissible majorant (*admissible* 6, R) | majorant admitted in the infimum | 1 (12:80) |
| Forgetting the terminal graph (App. D; *forgetting*, R) | Independence of the graph at the cutoff | 1 (title 12:131) |
| scalar (1, D) | normalization constant; constant term; exponent without its constant term | 6 (12:166 title, 170, 221; 13sb:29; 13ba:164, 219) |
| scalar coupling correction (*scalar* 3, D; table: reset) | coupling constant renormalization | 1 (13sb:26) |
| rooted activity norm (App. D 12:177–179) | the norms of \eqref{ch04:weighted-sums} | 1 |
| rooted majorant sums (*rooted*, R at 12:236) | incidence bounds | 1 |
| level-$m$ cutoff (*cutoff* 3, R) | regularity condition at scale $m$ | 1 (12:187) |
| cutoff tail, full cutoff tail (*tail* 1, R) | for all sufficiently large $N$ | 6 (12:189–190, 249, 363, 384; 13sb:84) |
| cutoff / convergence / approximation threshold, the threshold (*threshold* 3, R) | lower bound on $N$ | 6 (12:265, 395; 13:27, 388; 13sb:139; 13ba:307) |
| coupling threshold(s), coupling-threshold requirements (R) | lower bound(s) on the reference coupling | 9 (13:237; 13sb:16, 41, 45, 46; 13ba:39, 50, 83, 101) |
| thresholds for the starting scales (R) | lower bounds on the starting scales | 1 (12:123) |
| cover, cover number (*connected covering number*, D) | covering, covering number | 2 (12:229, 269) |
| transport (3, R); push, pushed (R); descend (*descent* 1, R) | transfer; image under the block maps; transferred | 6 (12:277; 13ba:124, 158, 170, 185) |
| vacuum normalization bound (R; App. D 12:247 without the symbol $q$) | per-site normalization exponent of \eqref{ch11:replicated-bound} | 2 (12:247; 13sb:25 "normalization cost") |
| moment (1, D) | lattice correlation | 1 (12:293) |
| extraction (3, R) | subsequence; diagonal argument; limit along a subsequence | 4 (12:400; 13:15, 31, 139) |
| refinement (R) | subsequence | 7 (13:32, 52–53, 138, 141–143, 165) |
| unit (1, R) | identity field | 1 (13:58) |
| slot (2, R) | argument | 1 (13:132) |
| row (7, R) | vectors | 1 (13:159) |
| inverse terminal coordinates (R) | cutoff-scale coordinates (11:885) | 2 (13:159, 217) |
| cluster point (*cluster* 1, R) | limit point | 2 (13:206, 211) |
| cost (1, 2, 3; R) | factor contributed by; adds … to the exponent; size; bound; exponent | 6 (13:236–237; 13sb:25, 37–38, 112; 13ba:120) |
| trial descent (R) | the backward comparison | 1 (13:239) |
| testing against (*test* 2, R) | pairing with | 1 (13:272) |
| moving (1, R) | cutoff-dependent | 1 (13:295) |
| residue patterns (I/S; App. D 13:367, words only) | classes modulo the side-$a_m$ tiling | 1 |
| input (*inputs* 2, R) | hypothesis | 1 (13:391) |
| trial encoding (R; without the symbol $v_{N,p}$) | reference labels of admissible trials | 1 (13:394) |
| rank detection (*detection*; table: separating family) | the separating families | 1 (13sb:9) |
| admissible path-action representation (App. D 13sb:27, without "at level $i$") | path-action representation of the density | 1 |
| have their admissible bounds (App. D 13sb:36) | satisfy the bounds \eqref{ch04:activity-bounds} | 1 |
| Haar-ball argument (R) | the lower bound for the partition function | 1 (13sb:36) |
| first-below-scale, first level (R) | first scale (below a length) | 5 (13sb:104, 111, 145, 147, 155) |
| selected (9, R: ordinary "chosen") | chosen | 1 (13sb:136) |
| lattice stencil (*stencil*, R; ch. 11 short term) | link support | 1 (13sb:138) |
| source (4, R) | insertion; density with insertions | 4 (13sb:65; 13ba:123, 158, 284) |
| ordinary (1, R) | small-field | 3 (13ba:15, 37 twice) |
| complementary (1, R/I) | large-field part (of the insertions) | 4 (13ba:16, 67–68, 154, 165) |
| local smooth cutoff / smooth cutoff (App. D second round, 13ba:36, 165) | small-field indicator | 2 |
| zero complementary profile (App. D 13ba:165–166) | no large-field part | 1 |
| suppression (R) | decay factor | 1 (13ba:77) |
| cell census (R) | set of cells | 1 (13ba:173) |
| room (R) | provided the cones lie inside the cells, as verified below | 1 (13ba:194) |
| relaxed small-field condition (*relaxed*, D; ch. 4) | relaxed regularity condition | 1 (13ba:220) |
| block average (table) / frame (1, R) | averaging operation / local gauge transformation | 4 (13ba:229–230, 241, 244) |
| primitive random variables (4, R) | auxiliary random variables | 1 (13ba:230) |
| connector (D; ch. 4 short term) | transporters | 1 (13ba:246) |
| shared frame seed(s) (R) | auxiliary random variable(s) | 2 (13ba:247, 270) |
| adjacent pairs (*adjacent pair* 2, S; ch. 10) | stage pairs | 1 (13ba:260) |
| replicate (R) | place a copy … in each reflected cell | 1 (13ba:283) |
| cofinal set of grids (R) | arbitrarily fine grids | 2 (13ba:305, 336) |

Table words applied: *scale* / *scale index* for "level" (about 50 places, including the titles of 12.1 "Fixed-scale convergence data" and 12.3 "… uniform in the stopping scale", "reference scale", "base scale", "stopping scale"; "comparison depth" at 13:163–165 kept, as c3a kept it); *step* ("step with insertions" for "marked transformation/map/step"); *localized term*; *averaging operation*; *local gauge transformation*; *regularity condition*, *relaxed regularity condition*; *coupling constant renormalization*; *transfer*; *identity field*; *separating family*; *coincident points* (12:402, lesson 11d).

Appendix D repairs applied: 12:131 (title), 12:177–179 (rooted activity norm → norms of \eqref{ch04:weighted-sums}), 12:247 (words only: "per-site normalization exponent of \eqref{ch11:replicated-bound} at scale $r$", without the new symbol $q$), 13:367 (words only: "lie in at most $2n$ classes modulo the side-$a_m$ tiling,"; the formula "$a_m\mathbb Z^4$, those of $w$ and $\theta w$" not inserted, lesson 11a), 13:395–396 ("family of measures"; "selected" kept, see below), 13sb:27 (without "at level $i$": the line has no $i$), 13sb:36, 13ba:36, 13ba:165–166 (both repairs combined: "multiplied by the small-field indicator has no large-field part, because").

## Not changed, for the author

- **Kept per assignment:** graph, column (13sb:15, 49, 75, 92; 13ba:13, 14, 109, 276, 278; 13:164), stopping (12:10, 225, 251, 302; 13sb:85, 102, 137; 13ba:8, 193), exact-cover gas (12:180), label, ordered tail(s) (13:143, 213, 293; 13ba:207, 298, 334), one-slot response / responses (13:9–10, 120, 151–152, 161, 177, 183, 210, 265), buffer (13:335, 348), protected trial (13:229), selected (12:123, 134, 139; 13:6–7, 143 "selection", 172, 307, 395; 13sb:50; 13ba:30, 50, 195, 200, 304), terminal (13sb:92; 13ba:61, 77, 123, 153, 174), principal, request (13:96; 13ba:100, 336), opening (13ba:127 "Open"), trial, lift (12:347), fixed-input continuity (12:36, 41, 128, 133, 141; kept by ch. 11 at 11:1038; proposal "continuity in the cutoff at fixed argument" is six words).
- **App. D 13ba:30** ("drop selected") not applied, because the assignment keeps "selected"; only "level-$h$" → "scale-$h$". At 13:395–396 the repair was applied as "the same selected / family of measures", keeping "selected". At 12:131 the App. D title repair removed "terminal" (the assignment keeps "terminal"); check that the repair should win there.
- **13ba:258, 261 "coupling-threshold requirement/conditions"**: the dictionary lists these lines under *coupling threshold* (lower bound on β̂), but the condition there is `b_q log3 ≥ 2 log(ȷ_q+7)` on `b_q`, which ch. 10 (10:122) calls the minimum starting scale. "Lower bound on the reference coupling" would misname it; "lower bound on the starting scale" is my inference. Left.
- **actual**, sense 6 (I): 12:143 ("the actual graphs"), 12:293 ("the actual lattice correlation at the cutoff": *moment* applied, "actual" kept), 13ba:32 ("the actual cutoff $N$").
- **physical** at 13:231 ("a physical lattice difference": sense 2, the difference divided by $a_N$; not listed for 13; left).
- **excess** (13sb:7, 164): proposal "loss ε in the exponent" introduces the symbol ε on lines without it (lesson 11a). Left.
- **stencil** as a finite-difference stencil (12:345, 362, 389, 390; 13:236) kept, as c3b did; in 13ba (216 math `\text{small-field stencil}`, 219, 232, 250, 297) kept, since the displayed formula at 216 carries the word in math mode, which may not be changed.
- **cone / ancestor cone** (13ba:131, 181, 194, 232, 234, 241, 251, 270): proposal "domain of dependence" is marked "proposal only" in *cone* and collides with chapter 4's *dependence set*; left.
- **Basis I / ? or no definite proposal:** absorb (13sb:61, 92; 12:281); amplitude/atom/degree 4 (12:60); row 2 at 12:55 (I); incoming / outgoing (13sb:10, 72); inspected (12:186; 13ba:219, 250); read(s) (13ba:232, 244); endpoint 4 (13ba:18, 34); degree ceiling (13ba:56); transitions (13sb:49; 13ba:81); vacuum denominator, denominator 2 (12:286); target 2 (13:252, 260); raw (13sb:173); signed 2 (13sb:35 "Signed regular costs" — the subject of the App. D 13sb:36 repair, left as it is); centered 4 (13:87, 98, 301, …; proposal is a description); arity (13:39, 93, 330); comparison depth (13:163–165, entry *comparison level* basis I); unreparametrized remainder map (12:91; I for the word); source 8 "source constants/attachment" (13sb:15, 63, 73; R/I); spectator, exterior word (13:336, 349; S, "define once" needs a sentence about clusters that the text does not have).
- **Long proposals not applied** (rule 7): equation space (13:14, 157, 220); normalized null condition (kept); site conversion (13ba:145); attachment (13sb:63, 69, 73; 13ba:58, 62, 77, 78, 99, 123, 145; c3a also kept it); incidence (kept); source weight / available weight (12:247, 281; kept "source weight" as ch. 11); generic (13ba:306, 311; defined at 15:178); sparse stopping scale (13sb: the word "sparse" is not in the file).
- "large-field activities", "regular sum" kept (12:78, 180, 189).

## Inconsistencies noticed

- The assignment keeps "terminal" and "selected", while App. D repairs 12:131 and 13ba:30 / 13:395 remove them; resolved as stated above (12:131 applied, 13ba:30 not, 13:395 partly).
- 13ba:258, 261: *coupling threshold* entry lists lines whose condition is on the starting scale `b_q` (10:122). The entry should be corrected.
- *large-field profile*: the dictionary's proposal "total large-field activity with given support and large-field set" was shortened to the defined term *total large-field activity*; 13ba:165 "complementary profile" is the same object and is now "no large-field part" (App. D).
- *ancestor cone* → "domain of dependence" against chapter 4's "dependence set": two names for related sets.
- *stencil* in 13ba is fixed by the math-mode text `\mathbf1_{\text{small-field stencil}}` at 13ba:216, so the prose word cannot be changed consistently without touching math.
- *rooted* at 12:236: "rooted majorant sums" → "incidence bounds" follows the entry (R), but the incidence sum of 11:258 is a sum over terms containing a given insertion, while 11:266–272 converts between rooted and containing-site bounds; a reviewer should confirm the identification.
- 12:22: "labels" kept; entry *label* 1 proposes "polynomial label", already defined in chapter 2.

## Checks

- `wc -l`: 12-ultraviolet-limit.tex 405 = HEAD 405; 13-continuum-fields.tex 403 = 403; 13-sharp-bounds.tex 177 = 177; 13-bounded-approximations.tex 337 = 337.
- `git diff --numstat`: 108/108, 35/35, 37/37, 81/81 (pure in-line changes). `git diff --stat` also shows 11-equation-calibration.tex, 11-marked-insertions.tex, 11-restarted-history.tex (other agents); I did not touch them.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1232 references. All explicit cross-references resolve; no duplicate labels." exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<scratchpad>/v3build-c5 monograph.tex`: exit 0; `grep -c undefined monograph.log` → 0; no "Rerun" or "multiply defined" warnings. Labels referenced by new text exist: `ch04:weighted-sums` (04:601), `ch04:activity-bounds` (04:648), `ch11:replicated-bound` (11:812), `ch12:graphs`, `ch10:trajectory`.
- Rendered text (pypdf extraction, pp. 200–222): no "??"; chapter 12 opening, the new definition (p. 201), the titles "Independence of the graph at the cutoff" (p. 203) and "Removal of terms of source degree at least two" (p. 204) read correctly. Page images not viewed (no pdftoppm installed).
- Whole word diff of the four files reread for sentences that no longer parse.
