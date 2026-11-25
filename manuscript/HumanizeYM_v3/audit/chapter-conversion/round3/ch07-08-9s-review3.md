# Third review: chapters 7, 8 and 9s

Files (worktree `/Users/mgubi/ym-terminology`, `manuscript/HumanizeYM_v3/`): `chapters/07-matching.tex` (288 changed lines 4f462ac5→HEAD), `chapters/08-polymers.tex` (31), `chapters/09-stationary-remainder.tex` (54). All 373 changed lines were compared old against new from a line-paired word diff, with the current file around each line. I formed my own reading first and only then read the earlier reports (`ch07-review.md`, `ch08-9s-review.md`, `round2/ch07-08-9s-review2.md`, `round2/harmonise.md`) and the leads. 9 lines edited, all within their lines. Line counts are unchanged.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text (or "left for the author") |
|---|---|---|---|---|---|
| 9s:221 | ERROR | "The common chart and tag-coincidence radius" | "The common chart and the ball on which the actions for all values of the auxiliary index coincide" | The condition "with positive probability weight" is dropped. The tag-coincidence radius concerns the live tags only (9s:127 keeps the condition, and so do the dictionary entries *tag-coincidence radius* and *live tag actions*). As written, the claim also covers indices of weight zero. | "…the ball on which the actions for all values of the auxiliary index with positive probability weight coincide" |
| 7:637 | ERROR (lead) | "a fixed-position read is a coordinatewise splice of its endpoints." | "the link read at a fixed position is a translate of a point having some coordinates of each endpoint." | The sentence says that a link *is* a translate of a point. The source (Martin `weighted-frame-penalty.tex:78–83`, quoted in the dictionary) and the dictionary's adopted wording say that the link is read *at* a translate of the splice point. | "the link read at a fixed position sits at a translate of a point having some coordinates of each endpoint." The name "coordinatewise splice" is not restored: see For the author. |
| 9s:189 | MISMATCH (lead e) | "Its tangent is the forest-coordinate lift $W_F$ of" | "Its linearization is the representative $W_F$ in the block axial chart of" | The defining place, 5:1143–1151 ("the unique minimizer in the block axial gauge"; "the representative $W_F$ in the block axial gauge"), and 5:1311, 7:574 and 11:642 all say "in the block axial gauge". Only 5:1234 and 9s:189 say "chart". | "…the representative $W_F$ in the block axial gauge of". 5:1234 (not my file) still says "chart". |
| 7:1083 | TERM | (gloss added by the conversion) | "in which ``pulled back'' means composed with the critical configuration" | The object composed with is the map $v\mapsto$ critical configuration, which 7:1150 and 7:1152 call the "critical-configuration map". The lead notes that "pull-back" also names `rep V` in chapters 5 and 6. | "…means composed with the critical-configuration map," |
| 7:505–506 | LANGUAGE | "Let $\zeta(x)$ be its stationary representative in centered coordinates," | "…in centered coordinates (the local gauge transformation normalized in the mean, Section~\ref{ch07:weighted})" | The parenthesis presents the coordinates as if they were a gauge transformation. | "(in which the local gauge transformation is normalized in the mean, Section~\ref{ch07:weighted})" |
| 7:521 | LANGUAGE | "Use rooted coordinates for the following exact calculation." | "Use rooted coordinates (the local gauge transformation normalized at the root of each block) for…" | Same fault. | "(in which the local gauge transformation is normalized at the root of each block)" |
| 7:745–746 | LANGUAGE | "the trace-class cube / argument preceding this subsection applies." | "the argument with the / trace-class factor $P_\mu^3$ preceding this subsection applies." | "preceding this subsection" now attaches to the factor rather than to the argument. | "the argument given before this / subsection for the trace-class factor $P_\mu^3$ applies." |
| 8:329 | LANGUAGE | "requires suppression of large-field activities by the action" | "requires a decay factor for the large-field activities coming from the action" | It is ambiguous whether the activities or the decay factor come from the action. | "requires a decay factor for the large-field activities from the action" |
| 8:288 | — (lead d) | "The set $I_\eta$ records the large-field sites assigned to that activity." | "The set $I_\eta$, the \emph{prescribed large-field set} of that activity, consists of the large-field sites attributed to it." | Verified: the term names $I_\eta$, the set attached to one activity. That is the object chapters 9–11 and the rest of the book mean: "a prescribed large-field set remain in the exact-cover sum" (9:151); "every selected incoming prescribed large-field set is covered" (11:247–248); "prescribed large-field set $I_M\subset X_M$" (09-forest-average:231); also 10:577, 12:162 and 11R:302. $D$ is the union of these sets (8:292). The dictionary's proposal ($D$) is wrong. The term already stood undefined at 4:657 before the conversion, so 8:288 is now its first definition. | right as it stands |
| 9s:295–296 | TERM (lead c) | "Actual small-field logarithmic coordinates and the reflected / normalized directions" | "Original … and the reflected / seminorm directions" | "Seminorm directions" is defined nowhere, though 10:495 already had "seminorm direction" before the conversion. The object is a direction with $|A_e|\le t(1+\mathrm{dist})^{\varpi}$. Chapter 2 defines this as a *permitted direction at threshold $t$* (2:326, (ch02:direction)), and chapter 4 uses it in (ch04:local-seminorm). "Reflected" is also undefined here, because the reflection map is introduced only at 9:322–330, after the input of 9s at 9:307. | left for the author (suggest "the reflected permitted directions", the chapter 2 term) |
| 9s:169, 171, 233 | TERM | "folded" | "reflected periodic extension(s)", "reflection map" (175) | The coined term is not defined anywhere. 9s is input at 9:307, while the map $\pi_v$ and the fields $U_{i,z}$ are introduced at 9:322–330, after that point and without a name. The consolidated list says "(chapters 8, 9s)", but chapter 8 does not contain the phrase. | left for the author (name the map at 9:326–330, or move the definition before 9:307) |
| 9s:165–166 | MINOR (formula) | "the exterior integrand, in stationary units, is / bounded by $e^{-\Delta+o(M^2)}$." | "…is bounded by / $\Omega e^{-\Phi(x)}e^{-\Delta+o(M^2)}$." | A formula replaces "in stationary units". It agrees with the source (Martin `stationary-exterior-receipt.tex:156–165`: $U_x\le\Omega e^{-\Phi(x)}e^{Y_*}$) and with (ch09:exterior-bound). | left (as in round 2) |
| 9s:139–141 | MINOR (content) | "The actual tree comparison recognizes … in a fixed safe chart … gauge-covariant block average mismatches" | "By the estimate \eqref{ch05:nonlinear-tree} … a fixed closed coordinate ball of the chart, the \emph{safe chart}, … the deviations of the coarse links from the values of the averaging operation" | "Closed coordinate ball" sharpens the old text. It is supported by the source, and the reference is correct: (ch05:nonlinear-tree) bounds $\chi(U_e(\mathrm{rep}V)_e^{-1})$ by the plaquettes and by $\chi(VQ(U)^{-1})$. The norm of the ball is not stated. | left |
| 7:554–555 | MINOR (qualifier) | "This uses the actual / block average, rather than an independently chosen linear average." | "This uses the nonlinear / averaging operation, rather than an independently chosen linear averaging operator." | "nonlinear" was added. It is true (the table of word choices says "averaging operation (nonlinear …)", and 5:986–993 says the same). | left |
| 7:1199–1200 | MINOR | "actual stationary block average." | "averaging operation at the critical configuration." | This reads as the operation evaluated at the critical configuration. The parallel at 7:765–766 ("the same density, averaging operation and critical configuration") suggests that "and" was meant. Round 1 already listed this. | left for the author |
| 8:268–269 | MINOR | "on an / actual complex neighbourhood of zero" | "on a / complex neighborhood of zero" | The emphasis of "actual" (a genuinely complex neighbourhood rather than a real one) is lost. "Complex" still says it. | left |
| 7:599 | LEFTOVER (lead) | "its number of residue blocks" | unchanged | "Residue" was converted to "positions within the block" at 7:585, 595 and 910, but it stays here. Whether "residue blocks" means the blocks of the padded patch is not settled by the text. | left for the author |
| 7:636 | MINOR | "For coordinate connector paths" | "For the coordinate contours of the transporters" | Round 1 (item 8) noted that in the source these coordinate paths join pairs of points of the patch (the construction of the local gauge transformation), and that the transporters come only at 7:640. "Of the transporters" may therefore name the wrong object. The dictionary (*connector*, basis D) maps every "connector" to "transporter". | left for the author |

All other changed lines say what the old ones said, using the dictionary's word for the sense at that line. Checked in particular:
- *common* → infinite-lattice (7:36 defined, 46, 64–65, 558, 758, 778, 900, 962, 964, 992, 1029, 1112, 1130, 1170, 1182, 1201)
- *denominator* → inverse propagator, and *insertion* → background derivative (7:331–333 defined, 380–391, 415–443, 493–499, 603–612, 740, 752, 755, 770–777, 785)
- *weight* → scaling dimension (7:350–357, 365, 390, 610, 913, 1026; consistent with 7:1079 and ch02)
- *floor* → lower bound; *frame* → local gauge transformation; *internal/external* → fluctuation/background (7:886 keeps "internal" in math text, glossed at 7:873)
- *principal/nonprincipal* → zero/nonzero alias; *anchor* → base point (7:154, 619, 733, 912, 1119); *connector* → transporter; *path* → contour
- *straight* → linear averaging operator $M$ (7:693; 5:993 confirms) and $W_s$ (7:1112; 5:1084)
- *stationary identification* → \eqref{ch05:stationary-tangent} (7:578, 829; checked against 5:1143–1150)
- *inherited loop action* (7:237, = 4:525); *contact term* $Z$ / *contact correction* (7:529, consistent with 501, 504, 568, 773, 807); *width* (7:360); *leg* (7:61)
- "the step from scale $m+1$ to scale $m$" (7:855, as 7:13); "lower bound on the reference coupling" (7:1190, 1196)
- chapter 8: *source-dependent activities*, *anchored* (8:76), *margin in the support exponent* (8:150, 331, 362), *factorization identity* (8:279, 355; the label `ch08:deletion-identity` exists and is the deletion formula used at 8:310)
- 9s: *pure* (9s:12), *regularity condition* (only for the plaquette condition $\chi(U_p)\le t_f$: 9s:127, 168, 220, 224, 232), *lower bound on $z$* (9s:207, 219; $z=\widehat\beta_{m+1}$ at 9s:19)

No sentence about Bałaban's or Dimock's papers and no citation key was added in these files.

## Corrections applied

ERROR 2 (9s:221; 7:637). MISMATCH 1 (9s:189). TERM 1 (7:1083). LANGUAGE 4 findings on 5 lines (7:506, 521, 745–746; 8:329). Total 9 lines: 07-matching 6, 08-polymers 1, 09-stationary-remainder 2.

## Cross-chapter mismatches not fixed

- `W_F`: "in the block axial chart" at 5:1234, against "in the block axial gauge" at 5:1151, 5:1311, 7:574, 9s:189 (now) and 11:642. 17c:49 has "forest representative" and 6:953 has "linearized critical configuration".
- "pull-back": `rep V` (5:920; 6:180, 445, 489) against composition with the critical-configuration map (7:1083–1152; chapter 17).
- "seminorm direction" (10:495; 9s:296) against "permitted direction at threshold $t$" (2:326).
- "reflected periodic extension" (9s) is used before the reflection is introduced (9:322–330), and is never named there.
- "coarse-frame projection / directions" (7:477, 892): the "frame" leftover, basis I. Round 2 and the harmonisation left it on purpose.
- "contact term" in chapter 7 (matrix $Z$) against the coincident-point "contact terms" of chapters 18–19 (pre-existing).
- "inherited loop action" (7:237; 9:26) against "$\beta$-independent quadratic term" (4:525; 6:170). These are consistent, because 7:237 defines the one by the other.

## Leftover house words

Kept on purpose:
- "stationary": 9s:2 (title), 43, 74, 254, 299 and 8:372. This is the ordinary sense (Laplace's method; "stationary estimates").
- "physical": 9s:188, 213 (basis I).
- "actual-sector inputs": 9s:299. The dictionary *actual* lists it as remaining. The sense would be "sector at a non-flat background" (6:439), but this is not settled.
- "coarse-frame": 7:477, 892 (basis I; the variable is $r$).
- "mark": 7:378 (*mark* sense 5, basis I).
- "internal": 7:886, in math text.
- "unit": 7:351 and elsewhere, ordinary.
- "weight(ed)": the Fourier weights $h_l$ and weighted norms in chapter 7, and the support weights in chapter 8.
- "label": the polymer label of chapter 8, defined at 8:24.
- "cutoff": 9s:2, 10, 108, the indicator retained.

Replaced: none beyond the corrections above. "Residue blocks" (7:599) is listed above.

## Leads

- (a) 7:636–637: verified as garbled. Corrected to "sits at a translate of a point …". The term "coordinatewise splice" was not restored (see For the author).
- (b) 9s:221: verified. "with positive probability weight" restored.
- (c) 9s:295–296: verified as undefined. Left for the author, with the chapter 2 term proposed.
- (d) 8:288: the term names $I_\eta$, which is also what chapters 9–12 and 11R mean by it. Right as it stands. The dictionary's $D$ is wrong.
- (e) `W_F` gauge/chart: 9s:189 harmonised to "in the block axial gauge"; 5:1234 remains.
- 7:599 "residue blocks": left, as explained above.
- Pull-back (7:1083): the gloss is made precise ("critical-configuration map"). The two senses across chapters are listed above.
- 7:1154 (checked right by a dictionary agent): confirmed.

## Assessment of earlier corrections

- Round 1 judged the conversion's 7:637 ("is a translate of a point") to say "what the source says". It does not: the source says the link is read *at* a translate. Round 2 also passed it.
- Round 2's corrections in these files are right: 9s:127, 134, 221 and 242 (the inserted `$\alpha$` removed); 8:28, 359 and 9s:16, 170 ("sector" restored); 7:1190, 1196 (reference coupling); 7:764.
- The harmonisation edits are right. At 7:1074 it puts "the schedule of Chapter~\ref{ch10:trajectory}" for the old "a later scale schedule", which agrees with the 4f462ac5 word. 7:22 and 7:1202 had duplicate glosses, which it removed. At 8:150, 331 and 362 it puts "margin in the support exponent".
- However, when round 2 removed `$\alpha$` from 9s:221 it did not notice that "with positive probability weight" was missing from the same phrase (now fixed).
- The round 1 glosses at 7:506 and 7:521 had a faulty construction (now fixed).

## For the author

1. 9s:296: whether to write "the reflected permitted directions" (2:326) or keep "seminorm directions" (10:495). Also restore the bound $2t(1+\bar w)^\varpi$, as the dictionary suggests.
2. 9s:169–175 and 233: name the reflection map and the reflected periodic extension where they are defined (9:322–330), or define them before 9s is input at 9:307.
3. 7:637: whether to name the "coordinatewise splice" (the source's term) and add the missing sentence "a coordinate path has four straight pieces". The present sentence is correct but does not explain why the point has some coordinates of each endpoint.
4. 7:636 "coordinate contours of the transporters": possibly the wrong object (round 1, item 8).
5. 7:1199–1200 "averaging operation at the critical configuration" or "… and the critical configuration".
6. 7:599 "residue blocks".
7. 5:1234 (not my file): "block axial chart" should become "block axial gauge" to agree with 5:1151 and 9s:189.
8. Still open from earlier rounds: 9s:165–166 (displayed bound), 7:578–579 `\ref{ch05:transports}` (probably `ch05:actual-tangent`), changed titles (7:229, 501, 572, 603, 626, 742, 825/827, 863; 8:279; 9s:111), and "coarse-frame" (7:477, 892).

## Checks

- Line counts: 07-matching 1206 = HEAD 1206; 08-polymers 374 = 374; 09-stationary-remainder 301 = 301. `git diff --numstat`: 6/6, 1/1, 2/2.
- `python3 tools/check_draft.py`: "51 files; 679 labels; 1250 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-t4 monograph.tex`: exit 0, PDF written at 11:11. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build included the uncommitted edits of other reviewers present at that time.
- Nothing staged, committed, pushed or reverted.

## Not checked

- Rendered pages were not inspected: neither `pdftotext` nor `pypdf` is available.
- Source manuscripts and Bałaban's and Dimock's papers were not opened. Source statements were taken from the dictionary's quotations.
- The mathematics was not re-derived. For example, the claim that centering normalizes the local gauge transformation "in the mean" rests on 7:655–656.
