# Second review, job r4: chapters 7, 8 and 9s

Files (worktree `/Users/mgubi/ym-terminology`, `manuscript/HumanizeYM_v3/`): `chapters/07-matching.tex` (289 changed lines 4f462ac5→HEAD), `chapters/08-polymers.tex` (34), `chapters/09-stationary-remainder.tex` (54). Every changed line was compared old against new (line-paired diff), with the surrounding text of HEAD, before the first-round reports (`audit/chapter-conversion/ch07-*.md`, `ch08-9s-*.md`) were read. 12 lines edited in place; line counts unchanged.

## Findings

| file:line | class | text at 4f462ac5 | text at HEAD | what is wrong | corrected text |
|---|---|---|---|---|---|
| 9s:127 | ERROR (symbol inserted, letter taken) | "all live tag actions coincide" | "the actions for all values of the auxiliary index $\alpha$ with positive probability weight coincide" | `$\alpha$` added; in chapter 9 (into which 9s is input) `\alpha` is the coefficient of `\mathcal Q` (9:403–409, 553–579) | "…values of the auxiliary index with positive probability weight coincide" |
| 9s:134 | ERROR (same) | "Tag probabilities sum to one, so there is no additional tag-count / factor." | "The probability weights of the auxiliary index $\alpha$ sum to one, so there is no additional factor counting the values of $\alpha$." | same | "The probability weights of the auxiliary index sum to one, so there is no additional factor counting its values." |
| 9s:221 | ERROR (same) | "tag-coincidence radius" | "the ball on which the actions for all values of the auxiliary index $\alpha$ coincide" | same | "…of the auxiliary index coincide" |
| 9s:242 | ERROR (same) | "at a fixed fine field and tag as" | "…and a fixed value of the auxiliary index $\alpha$ as" | same | "…a fixed value of the auxiliary index as" |
| 8:28 | MISMATCH | "about an integration sector, / derivative or local Taylor coefficient" | "about a term of the decomposition of the integral, a / derivative or a local Taylor coefficient" | Chapter 6 keeps and defines *sector* ("A \emph{sector} is a term of this decomposition with fixed discrete data", 6:85), and chapters 9, 10, 11 use "sector" (9:50, 75, 81, 105, 305, 436; 10:676; 11:244, 293). Chapters 8 and 9s alone renamed it; "term of the decomposition" is moreover wider than a sector (no fixed discrete data) | "about an integration sector, a / derivative or a local Taylor coefficient" |
| 8:359 | MISMATCH | "scalar factor and every large-field sector;" | "normalization constant and every large-field term of the decomposition;" | as above | "normalization constant and every large-field sector;" |
| 9s:16 | MISMATCH | "The other fine sectors have already been assigned" | "The other terms of the decomposition at the fine scale have already been attributed" | as above | "The other sectors at the fine scale have already been attributed" |
| 9s:170–171 | MISMATCH | "without a lower bound from a sector / expansion." | "without a lower bound from an / expansion over the terms of the decomposition." | as above | committed wording restored: "from a sector / expansion." |
| 7:1190, 1196 | MISMATCH | "then the coupling entry threshold so that"; "block ratio, then coupling threshold." | "then the lower bound on the inverse coupling so that"; "…then the lower bound on the inverse coupling." | The threshold bounds the reference coupling `β̂` (entry *coupling threshold*, basis R, 7:1189–1190). Every other chapter (6, 9, 10, 11, 11E, 11R, 13, 13sb, 13ba, 14lc, 17, 17w, 17c, 17m, 18lp, 19) writes "lower bound on the reference coupling"; in chapter 7 "the inverse coupling" is `β` itself (7:574) | "the lower bound on the reference coupling" (both lines) |
| 7:764 | MINOR (symbol inserted) | "identifies the actual stationary / thermal coefficient." | "identifies the coefficient $\alpha$ of / the Gaussian contribution \eqref{ch07:thermal}." | `$\alpha$` is a symbol the old line did not have (the first reviewer judged it correct; `\alpha` has the same meaning here as at 7:182, so it is not false). Removed under the no-new-symbol rule; the equation reference already names the object | "identifies the coefficient of / the Gaussian contribution \eqref{ch07:thermal}." |
| 7:22 | MINOR | "fixed stage bounds," | "…(a stage is defined in Section~\ref{ch10:choices})…" | true, but duplicates the definition already given at 4:651 (`\emph{stage}`, with the same reference) and 5:689 | left for the author |
| 7:1202 | MINOR | "an entire selected history" | "…history (a \emph{history} is defined in Chapter~\ref{ch11:insertions})" | true, but the same gloss is at 2e:253, which comes first in book order; the `\emph` suggests a definition here | left for the author |
| 7:216 | MINOR | "Subtracting the actual / kinetic symbol" | "Subtracting the / kinetic symbol $b_H$ itself" | symbol added; correct (the full `b_H` against its quadratic part, 7:184–188) | left |
| 7:613 | — | "The factor count is" | "The number of small factors is" | dictionary *factor count*, basis R; correct | — |
| 9s:127 | MINOR (formula) | "pass / the cutoff" | "satisfy / the regularity condition $\chi(U_p)\le t_f$" | formula added; it is the indicator of 9s:14 | left (first round listed it) |
| 9s:165–166 | MINOR (math changed) | "the exterior integrand, in stationary units, is / bounded by $e^{-\Delta+o(M^2)}$." | "…is bounded by / $\Omega e^{-\Phi(x)}e^{-\Delta+o(M^2)}$." | math-mode change (Appendix D repair); consistent with (ch09:exterior-bound) | left for the author |
| 9s:219–220 | MINOR (formula) | "raise the threshold for the microscopic / term." | "raise the lower bound on $z$ for the term / $C_{j,L}z^{-1}$." | formula for a word; correct (9s:217) | left |
| 9s:295 | DICTIONARY | "Actual small-field…" | "Original small-field…" | proposal *original* of *actual* has basis I (terminology.md:139); supported by the contrast with "reflected" in the same sentence | left for the author |
| 9s:139–141 | — | "The actual tree comparison recognizes … a fixed safe chart … gauge-covariant block average mismatches" | "By the estimate \eqref{ch05:nonlinear-tree} … a fixed closed coordinate ball of the chart, the \emph{safe chart}, … the deviations of the coarse links from the values of the averaging operation" | added content is the dictionary's basis-S repair (*safe chart*, *tree comparison* 1); *deviation* agrees with 6:49 | — |
| 7:742 | DICTIONARY | "Trace norms and recording." | "Trace norms and finite-volume coefficients." | entry *recording estimate* proposes *Fourier mesh estimate*; the title chosen is defensible (the paragraph ends with the finite-volume error) | left for the author (title) |
| 7:1074–1075, 1206 | MISMATCH (see below) | "a later scale / schedule"; "an infinite scale schedule." | "a later sequence / of scales"; "an infinite sequence of scales." | chapter 10 defines *schedule* (10:121); chapters 4, 6, 11, 17w, 18lp say "sequence of scales" | not fixed, listed |

All other changed lines of the three files were found to say what the old ones said, with the dictionary's word for the sense at that line (examples checked against entries: *common* 1 → infinite-lattice; *insertion* 2–4 → background derivative / transported curvature / infinitesimal gauge action; *denominator* 1 → inverse propagator; *floor* 2 → lower bound; *internal/external* → fluctuation/background; *principal* 1 → zero/nonzero alias; *frame* 1 → local gauge transformation; *weight* 1 → scaling dimension, 6 → coefficients; *anchor* 1, 3 → base point; *stationary identification* → the identity (ch05:stationary-tangent); *adjacent pair* → two consecutive scales; *one-loop drift* → one-loop shift of the coupling; *connector* → transporter; *split-field* → derivatives in left increments; *mismatch* → deviation; *pure*; *trajectory* 1 → renormalization-group trajectory). Glosses added by the conversion checked against the chapter: 7:237 (inherited loop action = `β`-independent quadratic term, as 4:525 and 9:26), 7:313, 7:332, 7:360, 7:506, 7:521, 7:529, 7:1083 (pulled back = composed with the critical configuration, as 7:1150–1152), 8:76, 8:268, 8:288, 9s:12. All true. No sentence about Bałaban's or Dimock's papers and no citation key was added in these files.

## Corrections applied

ERROR 4 (9s:127, 134, 221, 242); MISMATCH 6 lines (8:28, 359; 9s:16, 170, 171; 7:1190 and 7:1196 counted as one finding); MINOR 1 (7:764). Total 12 lines edited (7: 3; 8: 2; 9s: 7).

## Cross-chapter mismatches not fixed

- *schedule* (10:121 defines it; 10, 13, 13ba, 18gq, RG:32 "one scale schedule") against *sequence of scales* (4:421, 6:1557, 7:1074–1075, 7:1206, 11:1059, 17w:35, 18lp:20). Same object, two names; the author should pick one.
- *leg*: 7:61 defines it as an argument of a multilinear symbol (chapter 17 agrees), while 3:827, 839 use "leg" for a linear factor of a Wick monomial (dictionary *leg* 1, proposal *linear factor*, basis I).
- *contact term* / *contact correction* (7:529) against the coincident-point "contact terms" of chapters 18–19 (already so before the conversion).
- *block kernel* (4, 7:574, 9s) against *blocking kernel* (5, 9-forest-average, 11, 13ba, 17m, 18lp): not a dictionary item; noted only.
- *prescribed large-field set* and *anchored*: defined at 4:440 and 4:603 and defined again (for the abstract gas) at 8:288 and 8:76; consistent, but two definitions.

## Leftover house words

Kept on purpose:
- "stationary" at 9s:2 (title), 43, 74, 254, 299 and 8:372 ("stationary integration"): ordinary sense (Laplace's method about a stationary point; "stationary estimates" as in 9:293, 305); 9s:112 is a label.
- "actual-sector inputs" (9s:299): entry *actual* sense 1 (basis I, 9s:299 listed there); not applied.
- "physical" (9s:188, 213): entry *physical* sense 9, basis I.
- "coarse-frame projection / directions" (7:477, 892): *frame* sense 1 lists 7:892, but whether "coarse frame" is the coarse scalar component `r` or the coarse gauge directions is not settled by the text; left, as in the first round.
- "unit" at 7:351 ("counts as one unit"), 7:14, 184, 197, 295, 595, 713, 837, 850, 907: ordinary.
- "weight(ed)" in chapter 7 (Fourier weights `h_l`, weighted norms; *weight* 3, keep) and chapter 8 (support / exponential weight; *weight* 2, keep; "probability weights" 8:54).
- "label(s)" in chapter 8: *polymer label*, defined at 8:24 (standard).
- "mixed derivative(s)" (7:562, 671, 914; 8:258): ordinary.
- "common strip / width / bound / output path action" (7:136, 456, 806, 820, 958, 1013, 1159, 1169), "principal real cube" (7:704), "residue blocks" (7:599), "amplitudes" (7:1173, 1196): not in the table; left (7:1013 "common bound" is sense 1 of *common*; author may write "infinite-lattice bound").
Replaced: none beyond the corrections above (no missed table word found).

## Assessment of the first review's corrections

Chapter 7 (25 lines) and chapters 8/9s (8 lines): all read; none wrong in meaning. Two gaps: (i) the chapter 8/9s reviewer accepted "term of the decomposition" and listed only that chapter 6 "must define it", without checking that chapter 6 (and 9–11) keep the word *sector*; (ii) the chapter 7 reviewer did not compare 7:1190, 1196 with the book-wide "lower bound on the reference coupling", and accepted the inserted `$\alpha$` at 7:764. The chapter 8/9s reviewer also accepted "auxiliary index `$\alpha$`" at four lines in a chapter where `\alpha` is the coefficient of `\mathcal Q`.

## For the author

1. 7:22 and 7:1202: forward glosses for *stage* and *history* duplicate 4:651 and 2e:253; remove or keep.
2. 7:742 title "Trace norms and finite-volume coefficients" (dictionary: "Fourier mesh estimate"); other changed titles 7:229, 501, 572, 603, 626, 825/827, 863; 8:279; 9s:111.
3. 9s:165–166 (math changed to `\Omega e^{-\Phi(x)}e^{-\Delta+o(M^2)}`), 9s:127 and 9s:219–220 (formulas for words), 7:216 (`$b_H$ itself`).
4. 9s:295 "Original" (basis-I proposal applied).
5. *schedule* against *sequence of scales* (above); "coarse-frame" (7:477, 892).
6. 7:578–579 (pre-existing): `\ref{ch05:transports}` should probably be `\ref{ch05:actual-tangent}` (first round's item 7).
7. 7:636–637 "a translate of a point having some coordinates of each endpoint": follows the source, not provable from the chapter alone.

## Checks

- Line counts: 07-matching 1206 = HEAD 1206; 08-polymers 374 = 374; 09-stationary-remainder 301 = 301. `git diff --stat` on the three files: 3, 2, 7 lines changed (12 insertions, 12 deletions).
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1249 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=…/scratchpad/v3build-r4 monograph.tex`: exit 0 (then `latexmk -g`, exit 0). In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build included other reviewers' uncommitted edits present at the time (01-lattice, 02-observables, …).
- Nothing staged, committed, pushed or reverted.

## Not checked

- Rendered pages not inspected (no `pdftotext` available).
- Source manuscripts (Scott, Martin) and Bałaban/Dimock papers not opened; Appendix D repairs judged against the chapter text and dictionary only.
- Mathematics not re-derived (e.g. the glosses of centered/rooted coordinates rest on the dictionary's basis R).
