# Review of the vocabulary conversion of chapter 10 (10-common-trajectory.tex)

File: `/Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/chapters/10-common-trajectory.tex` (uncommitted). I read the word diff before the editor's report (`c2-apply.md`) and checked every changed line against the dictionary entries (adjacent pair, admissible 5, coupling band, coupling threshold, block floor / floor, threshold for the starting scale, delay, terminal, occupancy, column, ordinary, schedule, plateau / stage plateau, coarse target / endpoint, frame, source, anchor, window, label, actual, scalar, reset, path coefficient, compensation, logarithmic, logarithmic correction, hard, soft correction, fusion, sector, eligible, connected covering number, response bound, reserve, derivative reserve, dictionary, row, direct, history, auxiliary history, stationary graph, branch, block bridge, moving, request, selected, shooting, test, inflation factors, pad absent labels by zero), against Appendix D (10:98, 314–315, 327, 626, 727, 921), and against the committed chapters 1–9s.

## Review findings

| file:line | class | old text (HEAD) | edited text | what was wrong | corrected text |
|---|---|---|---|---|---|
| 10:107 | ERROR | "The delays require their product" | "The lower bounds on the cutoff scale require their product" | *delay* (R) and *threshold for the starting scale* (R) say these are lower bounds on the **starting scale of a stage**, imposed so that conditions hold at `m = N` (11E:29–30: "the adjacent stage conditions on the starting scale"). "Lower bounds on the cutoff scale" names a different integer (`N`). | "The lower bounds on the starting scales require their product" |
| 10:111 | ERROR | "Those delays also impose" | "Those lower bounds also impose" | After the edit of 110 the nearest antecedent of "Those lower bounds" is "lower bounds on the reference coupling", so the sentence now said that the coupling bounds impose `β̂_N ≥ a_{d,J(N)}`; in the committed text the delays do. | "Those lower bounds on the starting scales also impose" |
| 10:123 | TERM | "a requested length for a stage plateau." | "a prescribed length for a \emph{plateau}, a maximal interval of scales on which the stage is constant." | Defining the bare word *plateau* collides with its other sense (region where a cutoff equals one) used in the committed chapters 5:973 and 6:917, 1011–1012, 1023, 1380; the dictionary separates the two (*plateau* 1 / 2, *stage plateau*). The committed "stage plateau" disambiguated. | "a prescribed length for a \emph{stage plateau}, a maximal interval of scales on which the stage is constant." (later bare "plateau" in 139–206, 749 is as committed and now refers back to this definition) |
| 10:356 | DICTIONARY, MISMATCH | "the direct row coefficient strictly below" | "the plaquette coefficient strictly below" | *direct* has basis I. The report's justification ("as ch. 6 did") does not hold: no committed chapter says "plaquette coefficient". The proposition cited in the same sentence ("as required there"), ch05:horizon-limit, says "the fixed direct coefficient $c$" (5:749). | "the direct coefficient strictly below" (drops only "row", as in 5:749) |
| 10:656 | DICTIONARY | "A raw hard bound $a_h\le C e^{-cP(y)^2}$," | "A raw bound … on the preliminary large-field activities," | *hard*: basis R / I (identification by matching 10:656–666 with 9:651–666); the edit adds an assertion about what `a_h` bounds. | restored committed wording |
| 10:658 | DICTIONARY | "The soft correction has" | "The large-field correction factors have" | *soft correction `a_s`*: basis R / I, same matching. | restored committed wording |
| 10:666 | DICTIONARY | "with the hard factor" | "with the preliminary large-field factor" | as 656. ("fusion estimate" → "estimate of the exact regrouping" in the same line is correct, basis S, and kept.) | "…the estimate of the exact regrouping, with the hard factor" |
| 10:676 | MISMATCH | "protected local sectors on the reserved" | "protected local terms of the decomposition on the reserved" | *sector* is defined in chapter 6 (6:85, "A \emph{sector} is a term of this decomposition with fixed discrete data") and used throughout chapter 6; this sentence applies "the real estimates of Chapter 6" and must use its word (brief §11c). "The decomposition" also has no antecedent in chapter 10. | "protected local sectors on the reserved" (committed wording) |
| 10:570 | MINOR | "Small logarithmic factors require" | "Small large-field correction terms in the exponent require" | Dictionary wording (*logarithmic* 2, R); "Small large-field" reads awkwardly but parses. | left |
| 10:185 | MINOR | "requiring a window $w_j(s)=o(s)$" | "requiring an interval of scales $w_j(s)=o(s)$" | `w_j(s)` is a length, compared with `⌊k/2⌋`; the committed "window" had the same looseness. | left |
| 10:153, 808 | MINOR | "coarse target"; "tuned actual inverse coupling $\beta_m$" | "prescribed value $\bar\beta$ of the coupling at unit scale"; "tuned coupling $\beta_m$" | The chapter otherwise says "inverse coupling" for `β` (about 40 times). "The coupling β" is chapter 4's word (4:406, 418) and the dictionary's proposal (*coarse target*, *actual* 4), so not wrong; unit scale = scale index 0, `a_0 = 1` (1:198; 10:145–146), correct. | left; noted for the author |
| 10:273, 818 | MINOR | "shooting parameter"; "shooting" | "bare coupling"; "tuning the bare coupling" | 243 says "bare inverse coupling"; the book uses both (1:338 "bare couplings", 1:402 "bare inverse coupling", MT:63). | left |
| 10:666 | MINOR | "exactly" | "precisely" | not a vocabulary change; harmless. | left |
| 10:889 | MINOR | "Replacing a terminal Wilson normalization" | "Replacing the Wilson normalization at the ultraviolet cutoff" | article changed; meaning unchanged. | left |
| 10:626 | MINOR | "fixed response bound $\varepsilon$" | "fixed fraction $\varepsilon$" | The fraction is not said to be of what; the full Appendix D repair would insert `\le1/16` and `C_{\rm st}x^{-11/10}` and is excluded by rule 11a. | left |
| 10:655, 666, 774, 914 | MINOR | "fusion" | "the exact regrouping" | The table says *exact regrouping*, "cited by number"; no `\ref` was added. | left for the author |

Checked and found correct (no finding): the stage definition 10:25–31 (still "finitely many derivative orders, support exponents, path widths and coefficient bounds"; no "regularity class"; *stage pairs* glossed as "the stages of the two scales of one step", *adjacent pair* 2, basis S); every "level" → "scale" (186, 212, 238, 243, 250, 271, 354, 389, 394, 726, 783, 824 twice, 833, 878): each names the same integer, and "level set" (229) is untouched; "reference coupling" is used only for `β̂` (38, 104–105, 110, 153, 157, 627, 643, 686, 726, 808), consistent with 6:238–1161 and 9:145–929, while 524 ("reference inverse coupling $\beta_0$", a local value) is correctly left; *coupling constant renormalization*: at 421–422, 446, 772, 816, 842–843, 902 it is `q_m` / `Q_{m,N}` (*scalar* sense, basis D), at 651 the reset `Δ` (*reset*, table); these are one object, since `β_m − β_{m+1} − α_{N,m} = q_m` is the reset formula `β = β′ + α + Δ`, and chapter 9 (being converted) now writes "the coupling constant renormalization $\Delta$" (9:717, 748); "vacuum normalization" (422) is kept and is not the coupling constant renormalization; *explicit coupling increment* for `α` (423, 855; *path coefficient*, R); "history", "finite history", "auxiliary history" (826, 918) and "zero-terminal-array history" kept; "blocking sequence" only for the nested quadratic data (373, 933), as in 5:303–305, 5:757; *critical configuration* (329, 716–717, 789, 920) and *critical-configuration map* (922, 924) match 5:1145–1373, 7:517–1152, 9s:39; Appendix D 98 ("indicator of the relaxed regularity condition"), 314–315 ("linear curl division and the choice of coordinate contours", 7:146), 327 ("unenlarged"), 727, and the partial 626 and 921 (no `W_a` named, rule 11b) are words only; 336 "implicit-differentiation formula" matches 7:937; lines 233, 257, 431 are byte-identical to HEAD.

## Corrections applied

Within lines only; line count unchanged (935).

- 107: "lower bounds on the cutoff scale" → "lower bounds on the starting scales".
- 111: "Those lower bounds also impose" → "Those lower bounds on the starting scales also impose".
- 123: "\emph{plateau}" → "\emph{stage plateau}".
- 356: "the plaquette coefficient" → "the direct coefficient".
- 656: restored "A raw hard bound $a_h\le C e^{-cP(y)^2}$,".
- 658: restored "The soft correction has".
- 666: "the preliminary large-field factor" → "the hard factor" (rest of the edit kept).
- 676: restored "sectors on the reserved".

## Left for the author

- *hard* / *soft correction* (656, 658, 666): the dictionary's proposals (*preliminary large-field activity*; *bound on the logarithmic correction factors `e^{ℓ_a} − 1`*) are plausible but rest on an identification of basis R / I; confirm, then apply.
- *direct* (356, and "Direct path terms" 746): basis I; chapter 5:749 says "direct coefficient", kept here.
- Whether the "exact regrouping" (655, 666, 774, 914) should cite Proposition~\ref{ch09:fusion-prop} by number, as the table says.
- "inverse coupling" (about 40 uses for `β`) against chapter 4's "the coupling β" (now also at 153, 808): one word should be chosen book-wide.
- The editor's own list (title with "trajectory"; Appendix D repairs 10:169–172, 381–382, the full 626 and 921; basis-I words; "scalar" compounds at 645, 684, 826, 849, 868, 870; "zero terminal arrays" 432, 447) stands as reported in `c2-apply.md`.

## Words this file introduces that other chapters may also define

- *stage pair* (30; used 125). Chapter 5:689 has "adjacent pair of stages"; chapter 17 "adjacent-stage cases".
- *schedule* (121, defined: "the stage and the block ratio at every scale"); used earlier without definition at 4:421, 5:703–707, 6:1557, 7:1075, 1206 and RG:32 ("scale schedule").
- *stage plateau* / *plateau* (123); chapters 11 (11:1965) and 17w:7 use it; chapters 5–6 use *plateau* for a cutoff.
- *coarse endpoint* (153), also 19:21–23.
- *explicit coupling increment* `α` (423, 855): chapter 9 (9:409–411, 739, being converted) may name `α`.
- *coupling constant renormalization* for `q_m`; chapter 9 defines it for `Δ` (9:717, 748).
- *lower bound on the block ratio / on the reference coupling / on the starting scale (of a stage)*: chapters 11, 11E, 13, 17–19 have "floor", "threshold", "delay".
- *index set* (for "dictionary"; 316, 376, 379, 382, 393, 727, 905), chapters 11:472, 12:23–25.
- *width margin* (375, 442, 703, 712, 758); chapters 11 (471, 474, 1748) and 12 (62, 126) still say "width reserve".
- *large-field correction terms in the exponent* (570), the proposal also for chapter 9's "logarithmic correction" (9:368, 630–698).
- *finite parameter evaluation* (457, glossed).

## Checks

- `wc -l chapters/10-common-trajectory.tex`: 935; `git show HEAD:manuscript/HumanizeYM_v3/chapters/10-common-trajectory.tex | wc -l`: 935.
- Lines 233, 257, 431 compared with HEAD: identical.
- `git status --short`: ` M chapters/09-forest-average.tex`, ` M chapters/09-renormalization.tex` (other agent), ` M chapters/10-common-trajectory.tex`. I edited only chapter 10.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1218 references. All explicit cross-references resolve; no duplicate labels." exit 0.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-c2 monograph.tex`: exit 0 (log written after the last edit); in `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0.
- Rendered text: with `pypdf`, the corrected phrases were found on PDF pages 148 ("stage pairs"), 149 ("stage plateau", "starting scales also"), 152 ("direct coefficient strictly"), 157 ("sectors on the reserved"). The pages were not inspected visually.

## Not checked

- The pages were not looked at as images.
- The literature lines of the dictionary entries were not compared with the papers (no first-use sentence was added by the edit, so none needed checking).
- Chapter 9's ongoing conversion was read only for "coupling constant renormalization"; its final wording for `α`, the exact regrouping and the logarithmic corrections may differ from chapter 10's.
- The meaning of `C_j` at 83 ("coefficient-map bound"): whether it bounds the coefficient map or its inverse is not settled in chapter 10; the neutral wording was accepted.
