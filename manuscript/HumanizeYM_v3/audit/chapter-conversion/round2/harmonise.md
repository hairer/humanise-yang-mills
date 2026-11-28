# Harmonisation pass: one name per object

Worktree /Users/mgubi/ym-terminology, manuscript/HumanizeYM_v3. 71 lines changed in 18 files, all edits within lines. Nothing committed or staged. No chapters/17-*.tex touched. The full before/after line log is in `harm-log.txt` next to this file, and the script with every replacement is in `harm-apply.py` / `harm-extra1.json`. Abbreviations: RG = reading-guide.tex, 9f = 09-forest-average, 9 = 09-renormalization, 11R = 11-restarted-history, 11 = 11-marked-insertions, 13ba = 13-bounded-approximations, 17m = 17-marked-trace-rates, 17w = 17-variable-windows, 18lp = 18-lattice-products.

## 1. "full dependence set" against "dependence set"
**Definition:** 4:458–460: "the \emph{dependence set} includes those links as well as the internal links and any links read by other conditions. Two disjoint exclusion supports can have overlapping dependence sets."
**Decision:** "full" is kept. In every use it stresses the contrast with the smaller exclusion support `Y_i`: 6:1179 "These are full dependence sets, not only exclusion supports"; 6:1324; 9:93 "disjoint exclusion supports `Y_i` … disjoint full dependence sets". In chapters 6 and 9 the set is also stated explicitly to include Haar coordinates, auxiliary indices and covariance neighbourhoods (9:82–84; 6:776). The adjective names the same object, so I removed the second adjective, "complete", to leave a single wording:
- 6:1074 "with their complete dependence sets" → "with their full dependence sets"
- 9:82 "A complete dependence set contains" → "A full dependence set contains"
- 9f:230 "containing its complete dependence set" → "containing its full dependence set"
**Left unchanged:** 6:1117, 1179, 1324; 9:93, 107; RG:28 ("the full dependence of an activity", which is not the term); 10:127 ("full dependence radius").
**Chapter 17:** 17m:87 "Fix the full dependence set" is consistent. No change needed.
**Author:** you may instead drop "full" everywhere, since the defined dependence set already contains everything read. Nothing else in the book is called a "dependence set" that is smaller.

## 2. "quadratic coefficient condition" against "quadratic hypothesis"
**Definition:** 5:1056–1058: "Identifying their sum with a chosen metric `H_f` is an exact coefficient condition on the incoming path action; with `H_f ≥ εI` it is called the \emph{quadratic hypothesis} below."
**Decision: no change.** 6:140 ("`C_ν^*C_ν = H_ν` … This is the quadratic coefficient condition of (ch05:actual-hessian)") and 6:380 ("the exact quadratic coefficient condition") refer only to the identity, which chapter 5 calls "an exact coefficient condition". The quadratic hypothesis is that identity plus `H_f ≥ εI`. Writing "quadratic hypothesis" at these lines would add the positivity bound, so the object is different.
**Author:** if you want a single phrase, use "the exact coefficient condition" at 6:140 and 6:380, matching 5:1057.

## 3. "density coordinate tuple" against "representation data"
**Definition:** 4:550: "\emph{Representation data} `ρ` consist of `β`, a real constant `v_sc` per site, the localized terms and the large-field activities". This is the same object; the 4f462ac5 text of 4:550 read "A density coordinate tuple `ρ` consists of …".
- 9f:86–87 "A density coordinate tuple / is equivariant if both its families are." → "Representation data / are equivariant if both their families are."
- 9f:224–225 "with an equivariant incoming density coordinate / tuple," → "with an equivariant incoming representation / data,"
No uses remain.

## 4. "sequence of scales" against "schedule"
**Definition:** 10:121: "We construct explicitly the \emph{schedule}: the stage and the block ratio at every scale, including the initial scales."
- 4:421 "compatibility with the sequence of scales is a later choice" → "compatibility with the schedule of Chapter~\ref{ch10:trajectory} is a later choice"
- 6:1557 "estimates that can be created by choosing a sequence of scales." → "… by choosing the schedule of Chapter~\ref{ch10:trajectory}."
- 7:1074–1075 "without invoking a later sequence / of scales or a nonlinear …" → "without invoking the schedule of Chapter~\ref{ch10:trajectory} / or a nonlinear …". "Later" is dropped because the forward reference now carries it.
- 10:5–6 "used with a single sequence of / scales and a consistent choice" → "used with a single schedule (Section~\ref{ch10:schedule}) / and a consistent choice"
- 13:307 "and the selected schedule." → "and the schedule."
**Left unchanged:**
- 7:1205–1206 "or prove the existence of an infinite sequence of scales." The object here is the whole multiscale construction (the histories), not only the numerical schedule. The author should choose.
- RG:32 "one scale schedule (the choices of Chapter~\ref{ch10:trajectory})" names the same object, has a gloss, and is acceptable. It could become "one schedule".
**Chapter 17:** 17w:35 no longer contains "sequence of scales" in the working tree; the other reviewer has evidently changed it. If it still does at merge, change it to "The bound `L_i ≤ log β̂_i` of the schedule".

## 5. Support reserve, decay rate of the support weight, support exponent
**Definition:** 4:571–572 "a support-weight exponent `σ>0`", used in `e^{σ cov_{B_m}(X_i)}` (ch04:weighted-sums). 4:651 calls the stage data "support exponents". Chapters 10, 11, 11R, 11E and 12 use "support exponent" (10:84 "support exponent `σ_j`"; 11:218, 225 "margin in the support exponent"). Chapters 6, 8 and 9 used "decay rate of the support weight", which read literally is wrong, because the weight grows. Chapter 10 used "support reserve".
**Name chosen:** *support exponent*, the defining chapter's name. A strictly larger exponent kept for later use is a *margin in the support exponent*, the phrase chapter 11 already uses (11:225, 474, 1044).
- 4:572 "a support-weight exponent `σ>0`," → "a support exponent `σ>0` (the exponent of the support weight),"
- 6:1170 "a decay rate `α>0` of the support weight," → "a support exponent `α>0`,"
- 6:1475 "a small further decrease of the decay rate `α`." → "… of the support exponent `α`."
- 6:1556 "a strictly larger decay rate of the support weight than" → "a strictly larger support exponent than"
- 8:150, 331, 362: "margin (`δ`) in the decay rate of the support weight" → "margin (`δ`) in the support exponent". In chapter 8, `α` is the exponent in `e^{α c(X_γ)}` (8:69–72), so this is the same role.
- 9:148, 267, 438, 919: "margin(s) in the decay rate of the support weight" → "margin(s) in the support exponent"
- 9:230 "the incoming decay rate of the support weight" → "the incoming support exponent"
- 9:282–283 "from the margin in the decay rate of the incoming support / weight." → "from the margin in the incoming support / exponent."
- 9:516 "An additional exponent in the support weight" → "An additional margin in the support exponent"
- 9:687 "One additional unit of the decay rate of the support weight" → "One additional unit of the support exponent"
- 9f:615, 960: "the margin in the decay rate of the support weight" → "the margin in the support exponent"
- 10:37 "and the support reserves in the local integral." → "and the margins in the support exponent for the local integral."
- 10:507 "derivative order and support reserves." → "derivative order and margins in the support exponent."
- 10:594 "absorbed by a support-exponent reserve," → "absorbed by a margin in the support exponent,"
- 10:603–604 "another fixed support / reserve." → "another fixed margin in the / support exponent."
- 10:760 "by the support and attachment reserves of the polymer estimates." → "by the margins in the support exponent and the attachment reserves of the polymer estimates."
- 10:913 "require the stronger support reserve" → "require the larger margin in the support exponent"
- 11:198 "retain an additional exponent in the support weight / `σ>0`" → "retain an additional margin in the support exponent / `σ>0`"
- 11:1446 "retain one additional unit in the exponent of the support weight" → "retain one additional unit of the support exponent"
- 18lp:78 "and `σ` is its exponential support weight." → "and `σ` is the support exponent." This was already in 4f462ac5 and named the exponent as the weight.
- 19:20 (the choices of Chapter 10 select) "support weights" → "support exponents". The stage specifies exponents (10:25, 4:651).
**Left unchanged, different objects:**
- "support weight(s)" where the weight itself is meant: RG:28; 6:1308; 8:16, 177; 11:204; 11R:188; 13ba:133.
- Other "reserve"s: 9:34 "derivative reserves"; 10:112 "reserve inequalities"; 10:426 "numerical reserves"; 10:491 and 529 coupling reserve and "reserved band"; 10:813 "comparison reserves". The dictionary records these as basis I.
**Chapter 17:**
- 17m:316 "using the spare exponential support weight" should read "using a margin in the support exponent".
- 17m:332 and 17m:413 "Retaining two units of the exponential support exponent" should drop "exponential": "Retaining two units of the support exponent".

## 6. Coupling band, reference coupling
**Definitions:** 10:212 "The coupling band at scale `m` is `[β̂_m/2, 2β̂_m]`" (the same interval as 4:418 `𝔅_m`). `β̂` is "the reference coupling" throughout (for example 10:808).
- 9:386 "on the compact inverse coupling band" → "on the compact coupling band"
- 9:429 "the permitted neighboring reference-inverse-coupling bands." → "… reference-coupling bands."
- 11:693 "on the inverse coupling band." → "on the coupling band." In 4f462ac5 this read "actual inverse coupling band", which is dictionary *actual* sense 4, the running-coupling band.
- 11:743 "For a large reference inverse coupling parameter `s`" → "For a large reference coupling parameter `s`"
**Left unchanged:**
- 10:524 "a slightly smaller reference inverse coupling `β_0`": a local value, a different object.
- 10:676 "on the reserved inverse coupling band" and 10:529 "the reserved band": from 10:491 this is the band reserved around the line parameter (`33/40 ≤ χ_mλ ≤ 47/40`). It is not shown to be the coupling band of 10:212, so I did not rename it.
- Every "inverse coupling" for `β` (chapters 7, 9, 10, 11, MT, chapter 1). This is the book-wide choice still open for the author.
**Chapter 17:** 17m:312 "The inverse coupling band gives" → "The coupling band gives". The 4f462ac5 text was "The actual coupling band".

## 7. "coarse-frame" (7:477, 892)
**Dictionary:** *coarse scalar component*, variants "coarse-frame directions" and "coarse-frame projection": the zero-form (gauge-parameter) variable `r` at coarse sites. The basis is I and the proposal is "coarse frame variable `r`".
**Decision: left unchanged and listed.** The basis is I, and "local gauge transformation" would not name the variable `r` correctly.

## 8. "auxiliary index `α`" at 5:968
`α` is a scalar at 5:495 and 5:815 ("`α = Σ_l |m_l|^2 tr D_l`"). Chapter 4 introduces the symbol (4:217).
- 5:968 "Every local value of the auxiliary index `$\alpha$` of Chapter~\ref{ch04:blocking}" → "Every local value of the auxiliary index of Chapter~\ref{ch04:blocking}"

## 9. "index triple"
**Definition:** 6:49, the large-field index triple. No "empty index triple" or "nonempty index triple" remains anywhere. "Seeded / unseeded" stands at 6:1544 and 9:283–284, as restored. **No change.** As round 2 noted, "seeded" itself is still undefined.

## 10. The object of Chapter 10
**Chapter 10's own name:** the title is "A common trajectory and fixed-scale stability". The first paragraph describes the object ("a single schedule … and a consistent choice of coefficient arrays") without naming it. RG:59 says "One common trajectory". Chapter 1 (1:465–489) uses "trajectory" for the same thing.
**Name chosen:** *common trajectory*. References now read "the common trajectory of Chapter~\ref{ch10:trajectory}" or "the common trajectory".
- RG:35 "The resulting construction, the same for all ultraviolet cutoffs," → "The resulting common trajectory, the same for all ultraviolet cutoffs,"
- 12:13 "The construction of Chapter~…" → "The common trajectory of Chapter~…"
- 12:40 "For the cutoff-independent construction, Theorem…" → "For the common trajectory, Theorem…"
- 12:133 and 12:298 "For the construction of Chapter~…" → "For the common trajectory of Chapter~…"
- 12:370 "For the cutoff-independent construction with the strengthened stage" → "For the common trajectory with …"
- 13ba:17 "For the construction of Chapter~…" → "For the common trajectory of Chapter~…"
- 11R:89 "at the comparison scale of the construction of Chapter~…" → "… of the common trajectory of Chapter~…"
- 11:2176 "On the selected trajectory" → "On the common trajectory"
- 11:2294 "For the selected trajectory" → "For the common trajectory"
- 10:812 "Use the common construction above" → "Use the common trajectory above"
- 10:817 "the fixed common construction," → "the fixed common trajectory,"
**Left unchanged:** 13ba:50, 195, 200, 304 "selected histories". These are the tuned histories, one per cutoff, which are a different object (a history, 11:18).
**Note for the author:** the dictionary entry *trajectory* sense 2 proposed "the construction of Chapter 10". That reverses the title, so I followed the title as instructed. If you prefer the dictionary's phrase, change the title instead and revert these lines.

## 11. "spatial exponents" against "spatial weights"
**Definitions:** 4:571 "a nonnegative spatial exponent `ϖ`"; 2:325 "a nonnegative spatial exponent `p_0`". 2:333 "the later polymer norms will specify which orders and spatial exponents they retain". 9:30 "spatial exponents" refers to `ϖ_m`. 10:79 is about the derivative constants of the equation-adapted sections "at the orders and spatial weights of stage `j`", which is the same parameter. The definition of a stage at 10:25 lists "derivative orders, support exponents, path widths and coefficient bounds" and does not list spatial exponents.
- 10:79 "orders and spatial weights of stage `j`" → "orders and spatial exponents of stage `j`"
- 11:351 "fine spatial weight at least `d`" → "fine spatial exponent at least `d`"
**Left unchanged:** 6:576 "Polynomial spatial weights are moved along a kernel" refers to the weights `(1+d)^ϖ` themselves.
**Author:** the stage definition (10:25; 4:651) omits spatial exponents, but 4:651 says `ϖ` depends on the stage. You may want "derivative orders, spatial and support exponents, …" there. That adds an item, so I did not do it.

## 12. "link support" against "support of the expression"
**Definitions:** 4:504–506: the multilinear expressions `A_i^{(q)}` of the path action, each "multiplied by the indicator of the regularity condition on its declared support. The support of the expression contains the contours, plaquettes and base point". 6:453 defines the "link support" of a retained component, "the fixed set of links from which its expression is built". 6:459 adds: "The link support contains the links on which the averaging operation depends and every endpoint of a retained path." In 4f462ac5 the two were different words ("stencil" in chapter 6, "footprint" in chapter 4).
**Finding:** the tie added at 6:453, "(the support of the expression, in the words of Chapter~\ref{ch04:blocking})", is not correct. The chapter-6 link support consists of fine links read through the averaging operation, so it is larger than the chapter-4 support of a path-action expression.
- 6:453 removed " (the support of the expression, in the words of Chapter~\ref{ch04:blocking})". This restores the 4f462ac5 content.
"Link support" stays as chapter 6's defined term, used in chapters 6, 11, 11E, 13, 18.

## 13. Forward glosses repeating earlier definitions
- 7:22 "depend on fixed stage bounds (a stage is defined in Section~\ref{ch10:choices}), but" → "depend on fixed stage bounds, but". 4:651 already glosses stage with the same reference.
- 7:1202 "an entire selected history (a \emph{history} is defined in Chapter~\ref{ch11:insertions})" → "an entire selected history". 2e:253 already has the forward reference. The `\emph` also wrongly marked a second definition.
**Still open (r6):** chapter 10 uses "history" (10:209–256) without a reference. 2e:253 covers this in book order.

## 14. "step" emphasised twice
- 4:5 "called a \emph{step}," → "called a step,". The emphasis stays at RG:22, the first place in book order.

## 15. RG:18 "correlations with all other fields"
**Definition:** 13:119–122: "define the correlation functional `L_{v,f}(c)=…`". 13:9 says fields are defined "by their responses in all separated correlations".
- RG:18 "by equality of all their separated correlations with all other fields." → "by equality of all their responses, the values of the correlation functionals."
- 18:182 "The lower field must be identified by its correlations with all other fields," → "… identified by all its spectator responses,". This matches 18gq:130 "requires all spectator responses" and 13:217 "every spectator response" (r9's pair).
**Dictionary:** the entry *spectator responses* still proposes "correlations with all other fields", which contradicts *correlation responses*. The dictionary should be corrected.

## 16. Other cases from the reports
- **Prescribed large-field set** (definition 4:440):
  - 9f:231 "prescribed set `I_M⊂X_M` of large-field sites, possibly empty," → "prescribed large-field set `I_M⊂X_M`, possibly empty,"
  - 9:893 "A connected prescribed set of `r` large-field sites" → "A connected prescribed large-field set of `r` sites"
- **Regularity condition** (book-wide row "small-field condition → regularity condition"):
  - 9:510 "under their own small-field conditions." → "under their own regularity conditions."
- **Checked and already consistent in the working tree:**
  - "comparison level / depth": all are now "comparison scale".
  - "inverse terminal coordinates": now "cutoff-scale coordinates".
  - Contour is no longer defined twice; 4:36 is a use.
  - "blocking kernel" no longer occurs.
- **Left for the author:** see the list at the end.

## Chapter 17 (report only; files not touched)
- 17m:312 "The inverse coupling band gives" → "The coupling band gives".
- 17m:316 "using the spare exponential support weight" → "using a margin in the support exponent".
- 17m:332 and 17m:413 "two units of the exponential support exponent" → "two units of the support exponent".
- 17m:330 "large-field event" against the book's "large fluctuation-field event" (6, 9, 10, 11, 11R). Check which is meant: large-field set or cutoff failure.
- 17t:12 title "Difference-preserving block averages" ("block average" is a house word). Use "averaging operation" if the object is the nonlinear operation, or "linear averaging operator" if it is `M` (r2: also 17c:75 "block average `M_a`", now apparently changed).
- 17m:87 "full dependence set": consistent with the choice in case 1.
- 17w:35 "sequence of scales" → "schedule", if it is still present.
- 17c:396 "as the trajectory with insertions": check whether this means the common trajectory with insertions (Chapter 11) or a history.

## Systematic check
For every row of "Book-wide word choices" and every coined term in the round-2 list, I grepped MT, RG and all chapters for the house word, older synonyms, singular and plural, and hyphenation variants.

**Clean (no competing variant left):**
- house words with no remaining occurrence: "block transformation", "one-step transformation", "stationary field / configuration / map / tangent", "actual tangent", "cutoff failure", "tree gauge / slice", "small-field condition", "regular activity", "gauge completion", "first expansion", "regularity class", "averaging order", "unit field", "anchor average", "source order", "density coordinate", "decay rate of the support weight", "support reserve", "complete dependence set", "cutoff-independent construction", "selected trajectory";
- coined terms with a single name in use: block axial chart (always in full), transporter, loop condition, relaxed regularity condition, containing-site, exact cover, eligible pair, link multipliers, periodization criterion, blocking sequence, stage pairs, stage plateau, coarse endpoint, activity array, finite parameter evaluation, source degree, cutoff-scale coordinates, Taylor localization, common / one-step localization map, normalized local insertion, upper interval, larger source weight, reduced density, auxiliary reference parameter, total large-field activity, jet functional, base-point average, exterior moments, current defect, ratio-(in)dependent constants, coupling constant / vacuum energy renormalization, exact regrouping, compression algebra, separating family, identity field, filtration index, penalty parameter / penalty term.

**Benign hits:**
- "route" (6:514, the 6:1025 title "bounded-jet route") is ordinary English.
- "reset" occurs only in labels and in `C_reset`.
- "cluster expansion" occurs in chapter 8 (standard) and in "exponentiated cluster expansion" (9:192).
- "second cluster" at 18:249 is ordinary use.
- "minimal configuration" at 5:20 is a quotation of Bałaban.

**Objects that still have two names (not changed):**
1. `β`: "inverse coupling" (about 69 uses: MT, 1, 7, 9, 9f, 9s, 10, 11, 11R, 17m, 17) against "the coupling `β`" (4:418; 10:153, 808). This is the author's pending book-wide choice.
2. Smoothing order `j` (4:16, the number of convolution factors) against 11:351–352 "fine kernel order … coarse kernel order". These are probably the same parameter of the block kernel, but that is not verified (dictionary *coarse kernel level*, basis S).
3. "coefficient arrays" (10:6, 10:321) against "activity array" (10:421 defines `x_m`). 10:6 very probably means the activity arrays. 10:321 may mean Taylor coefficient arrays. Not changed.
4. "large-field event" (17m:330) against "large fluctuation-field event".
5. "scale schedule" (RG:32) against "schedule" (chapter 10). The gloss makes it harmless.
6. "coarse-frame projection / directions" (7:477, 892) against the variable `r`. Basis I.
7. The inequality ch05:tree-comparison has four names in chapter 5: 945 "tree inequality", 1290 and 1375 "Poincaré-type inequality", 1306 "deterministic comparison", 1319 "Euclidean tree gap" (r2).
8. "normalization index" (11:2307, unchanged since 4f462ac5). Whether this is the filtration index `e` or a power of `a_N` is not clear from the line.
9. The coefficient `α_{N,m}`: "the determinant coefficient fixed by the matching" (9:410, 723, 738) against "explicit coupling increment" (10:423, 855) (r5).
10. Plaquette corner: "plaquette based at `z`" (2:167, 222) against "initial point `z` of the plaquette" (2e:88, 135). Both are ordinary geometric language.
11. Admissible periods: MT:14 "admissible physical periods" against 19:20–21 "admissible periods `R_p` in continuum units". MT was outside my files.

## Left for the author
- Case 2: whether to write "exact coefficient condition" at 6:140, 380.
- Case 4: 7:1206 "existence of an infinite sequence of scales": schedule or the whole multiscale history.
- Case 5: whether to add "spatial exponents" to the definition of a stage (10:25, 4:651).
- Case 6: the "reserved (inverse coupling) band" of 10:491–529, 676: name it, or state that it lies inside the coupling band. Also the book-wide "inverse coupling" against "coupling" for `β`.
- Case 10: the dictionary's "construction of Chapter 10" against the title's "common trajectory". I applied the title's name.
- Case 15: correct the dictionary entry *spectator responses* (its *Proposed* contradicts *correlation responses*).
- Items 2, 3, 7, 8, 9, 10, 11 of the systematic list. Also MT:50 against 1:416, the duplicate gloss of "phase" (MT not in my files), and 2e:254 "spectators" used before its definition at 3:705.

## Checks
- Line counts: every modified file equals `git show HEAD:<path> | wc -l`, checked with a loop over `git diff --name-only`; no mismatch.
- `git diff --name-only | grep /17-`: empty.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1250 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-harm monograph.tex`: rc 0, PDF written. The first call reported "up-to-date", so I forced the rebuild with `-g`.
- Log counts: "undefined" 0, "Citation" 0, "Overfull" 0.
- Rendered pages not inspected visually: `pdftotext` is not installed, so only the log was checked.
