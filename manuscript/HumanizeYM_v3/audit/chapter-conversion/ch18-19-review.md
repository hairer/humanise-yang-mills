# Review of the vocabulary conversion: 18-operator-products, 18-raw-replacement, 19-assembly

Worktree `/Users/mgubi/ym-terminology`, files under `manuscript/HumanizeYM_v3/chapters/`. I read the word diff first and the editor's report (`c9-apply.md`) afterwards. Every changed line was checked against the committed text (HEAD), the dictionary entry for its sense, and the committed chapters 1–16, 18gq and 18lp. Chapter 17 files were read only. Line numbers are those of the files, which have the same number of lines as before.

## Review findings

| file:line | class | committed | edited | problem | corrected |
|---|---|---|---|---|---|
| 19:63–64 | ERROR (language that changes the claim) | "The fields have units, injective inclusions and commuting positional derivatives." | "The fields include the identity field, injective inclusions and commuting derivatives in the positions." | With "include", the sentence now says that the fields *include* injective inclusions and derivatives. In the committed text "have" governs all three items. | "The field spaces contain the identity field and have injective inclusions and commuting derivatives in the positions." |
| 18:281 | ERROR | "We specify which normal jet is subtracted near simultaneous collisions." | "… is subtracted where several pairs of points coincide." | "near" was lost. The subtraction acts on configurations close to the diagonals (`ρ ≤ 2s`), not at points of `Δ`, where the kernel is not defined. | "… is subtracted near configurations in which several pairs of points coincide." |
| 18:412 | ERROR | "For several collisions the shell estimate …" | "For several coincident pairs the …" | These collisions are the collision subsets `h` of 18:399, which may contain more than two points and may be nested. "Pairs" narrows the claim. | "For several subsets of coincident points the …" (as 18:399) |
| 18:140, 141, 205, 222; 18r:61–62, 64 | DICTIONARY | "Cluster labels", "Spectator labels", "bounded label sets", "rotating labels", "Compact label sets", "rotated labels" | "Cluster fields", "Spectator fields", "bounded sets of fields", "rotating the fields", "Compact sets of fields", "rotated fields" | The entry *label* gives sense 2 (field) at exactly these lines with basis I ("probably also … basis I there"), and the brief forbids basis-I replacements. "Spectator labels have bounded degrees and coefficients" can also be read as polynomial labels (sense 1). The committed 18lp:17 and 18lp:295 keep "bounded label sets". | committed wording restored at all six places |
| 18:175 | DICTIONARY | "and the graded quotient comparison." | "and the estimate \eqref{ch18:graded-distance}." | The entry *graded quotient comparison* is basis I for identifying the nickname with (18.graded-distance) ("18:175 gives no reference"). | committed wording restored |
| 18:183 | MISMATCH / TERM | "using the normalized-null lemma of Chapter~\ref{ch13:continuum}." | "using the normalized null condition \eqref{ch13:normalized-null}." | The committed text points to the lemma (the observation of 13:189–212, which has no number). The edit points to its hypothesis, the display (13.normalized-null), so the referent changes. The entry says "cite the lemma by number", which cannot be done because the lemma has no number. 18gq:9 says "normalized-null statement". | committed wording restored; listed for the author |
| 19:22–23 | MISMATCH | "with prescribed coarse endpoint $\bar\beta$." | "… gives the prescribed value $\bar\beta$ of the inverse coupling at unit scale." | Chapter 10 (committed, 10:153) defines the short term once: "a prescribed value $\bar\beta>0$ of the coupling at unit scale, the \emph{coarse endpoint}". It uses that term at 10:209, 268, 813 and 850. Chapter 19 should use the defined term, not a longer description. | "… is tuned so that it gives the prescribed coarse endpoint $\bar\beta$." The "tuned" wording, also used in chapter 10, is kept. |
| 18:40–41 | TERM | "by the definition of correlation-null fields." | "because $F_d$ is the quotient by the fields all of whose separated correlations vanish." | `F_d = V_d/N_d(S)` (13:126–127): the quotient is taken by elements of `V_d`, which are polynomial labels in the sense of chapter 2, not fields (elements of `F_d`). | "… is the quotient by the polynomial labels all of whose separated correlations vanish." |
| 18r:5–6 | LANGUAGE | "We use its uniformity in replica number to obtain …" | "We use that its constants are independent of the number of reflected copies to obtain …" | "use that … to obtain" is a garden-path construction. | "We use the independence of its constants from the number of reflected copies to obtain …" |
| 19:98–99 | MINOR (TERM) | "to the mixed ground space." | "to the zero-energy subspace of the undecomposed family." | A family has no zero-energy subspace; its reflection Hilbert space does (15:7). The dictionary proposal (*mixed ground space*, R) includes the words. | "… zero-energy subspace of the reflection Hilbert space of the undecomposed family." |
| 18:430 | MINOR (LANGUAGE) | "uniqueness, unit removal and identification with …" | "uniqueness, compatibility with removal of an identity field and identification with …" | Without a comma, "compatibility with" can be read as also governing "identification". | comma added before "and identification" |

Lines checked and found correct (no change made):
- **18:5, 8, 9.** "insertions approaching coincident points", "the diagonals", "renormalization group with insertions".
- **18:15, 72, 185, 207, 221, 277, 340.** "undecomposed", which agrees with 14:12 and 15sp:5. At 18:72, "The undecomposed correlations are always used for this measurement" is the object `S`.
- **18:43, 130.** "inclusions of the interacting field spaces" and "interacting quotient", which agree with 18gq:2 and 18gq:8.
- **18:59, 225.** "annihilated".
- **18:109, 382.** "identity field".
- **18:123–130.** "coefficient in the nilpotent source variables", "Insertions may merge", "source degree at least two" (the term of 12:202–236 and 13sb:11–71), "prescribed large-field set", "factor lost", "attributed".
- **18:144.** "prescribed".
- **18:158–159.** "with constants independent of the number of reflected copies" (15:276), and deletion of "actual". The constant `C` is independent of `k`, as before.
- **18:165, 18r:19–20, 70.** Thresholds as upper and lower bounds. The order of quantifiers is unchanged.
- **18:172.** "same family of measures" (*common family*, R).
- **18:174.** \eqref{ch18:signed-transport}: R; the label is the display at 18lp:50–53.
- **18:175.** "cutoff-dependent field" (*moving* 1, R).
- **18:182.** "its correlations with all other fields" (*spectator responses*, R).
- **18:215, 248; 18r:36–37.** "paired with" and "Pairing".
- **18:230, 256, 18r:33.** "contributes … factor" and "bound".
- **18:257.** "arbitrary small losses in the exponents": same claim.
- **18:297, 352, 358.** "positive weight". `φ = 0` on `[4√m, ∞)`, so a pair with `a_h > 0` has distance below `4√m ρ`. The direction of "Only … have positive weight" is the direction of the committed "Only … are selected".
- **18:299.** "arguments".
- **18:359, 399, 421.** "pattern / subset of coincident points".
- **18:404.** Appendix D repair (second round), copied exactly; no symbol was inserted.
- **18r:11, 21.** "full", "source degree at least two".
- **18r:48–53.** "downward induction", "constants of the crude estimate and of the estimate on the grid", "derivative in the positions" (18lp:296).
- **19:17, 143.** "penalty parameter".
- **19:18–19, 31.** "cutoff-independent choices" (*common* 3, *schedule* 2, R). "select" was kept, which is right: *selected* is basis I at 19:19.
- **19:20.** "lower bounds on the reference coupling", which agrees with 11:278, 443 and 10:157.
- **19:30.** \eqref{ch11:calibration-floor}: R; the label is the display at 11E:24–28.
- **19:33–38, 60, 112, 141.** "in continuum units", "these volumes", "subsequence", "chosen", "along the chosen subsequence".
- **19:45–48.** "given", "same family of measures", deletion of "actual", "comparisons with insertions".
- **19:50.** Proposition (13.bounded-singleton) and Corollary (13.bounded-word) are a proposition and a corollary (13ba:197, 301).
- **19:66.** "space of phases".
- **19:68.** "null spaces of the correlations".
- **19:73.** "multiples of the identity".
- **19:84.** "the diagonals".
- **19:107.** "extend uniqueness of the vacuum to every phase". It does not say that uniqueness fails anywhere (entry *exceptional phases*).
- **19:122.** "zero-mean trace", which agrees with the chapter 17 files as they now stand (17:23, 351, 390).
- **19:131.** Title "Conclusions that are not obtained". The title contained "supplied", and the new title claims nothing more.
- **19:152.** "Positivity at coincident points".
- **19:159–160.** "linearization of the critical configuration" (no representative named) and "gives".

### Points the caller asked about

- **19, every theorem statement and scope sentence, word by word.**
  - Theorem `ch19:conditional`: its label and title ("Assembly of the common Wilson family") are unchanged. The only differences from HEAD are the following word replacements:
    - refinement → subsequence (60);
    - units → identity field, with the repair of line 63 above;
    - positional derivatives → derivatives in the positions;
    - phase space → space of phases;
    - field-null spaces → null spaces of the correlations;
    - is scalar → consists of multiples of the identity;
    - collision diagonals → the diagonals.
  - Corollary `ch19:conditional-trace`: only centered → zero-mean.
  - 19:139–144: refinement → subsequence; block penalty → penalty parameter.
  - 19:146–154: contacts → coincident points; "the fact that inserting the identity leaves correlations unchanged" → "compatibility with removal of an identity field". No other difference. "Contact Ward identities", "uniqueness of contact terms", "additional normalization conditions", "may have larger local order than an optimized prescription" and "no infinite series convergence has been asserted" are unchanged.
  - 19:134–137 (mass gap) is unchanged.
  - The proof (19:88–112) differs only in replaced words. At 19:107 "remove exceptional vacua" became "extend uniqueness of the vacuum to every phase", which is the entry's sense; it is not a statement that non-uniqueness occurs.
- **19:152–154 and 18:430.** "compatibility with removal of an identity field" parses in both places. In context it is a property of the extension (the subject of the preceding sentence at 19:150 and of the paragraph at 18:423–431). It matches the source "compatibility with unit deletion". The longer Appendix D B7 wording ("compatibility of the extension with deletion of an identity-field insertion") was not used; the shorter wording is what the assignment prescribes.
- **18:398–421 (forest prescription).** Unchanged in claim. The text still reports "the source prescription and its proposed sharper local-order bound" (18:411). It still says that "A one-shell estimate alone does not verify that stronger forest prescription" and that "We have therefore used the fully specified pair-weighted subtraction \eqref{ch18:subtraction}", with absolute convergence "proved directly". The edits there are collision → coincident points (399, 412, with the fix above, and 421), complete → full (413), and the Appendix D repair at 404.
- **"contact".** The chapter 7 / 17 "contact identity" and "contact term" are not cited in these files. The "contact extension", "contact terms", "contact Ward identities" and "Contact reflection positivity" of 18–19 are kept. Only "contacts" (19:152) was changed. "probe" is kept everywhere. "field reconstruction" `H_d` is kept (18:67). "cluster", "clearance" (basis I) and "replacement" are kept. "signed" is kept.
- **"marked replacement" → "with insertions".** The object is `Z_D` (18:154–157): the error of replacing the cluster in the density with insertions (nilpotent source variables). "Lattice replacement with insertions" describes it correctly. The dictionary is in conflict here: *marked replacement* (D) proposes keeping the term, while *mark* 1 (R) lists 18:119. The author decides (see below).
- **Chapter 19 nicknames.**
  - Replaced by citations: "bounded approximations" (R, 19:50) and "equation calibration floor" (R, 19:30).
  - Replaced in words: "exceptional vacua" (R) and "mixed ground space" (R).
  - Kept: "annular estimates" (I, 19:51, 95), "fixed-input convergence" (I, 19:47), "prescribed-radius squeeze" (I, 19:126–127) and "real approximation" (I, 19:99). This is correct.
- **"admissible physical periods" (19:20–21).** "Admissible" and `R_p` are untouched. "physical" became "in continuum units", placed after `R_p` ("admissible periods $R_p$ in continuum units"), on the authority of *physical* 1 (R), which lists 19:20. The entry *admissible periods* itself was not applied (its proposal prints a formula). Neither of its two notions is altered by this wording. Listed for the author.

## Corrections applied

1. 19:63–64: "The field spaces contain the identity field and have injective inclusions and commuting derivatives in the positions."
2. 18:281: "near configurations in which several pairs of points coincide".
3. 18:412: "For several subsets of coincident points".
4. 18:140, 141, 205, 222 and 18r:61–62, 64: "labels" restored (basis I).
5. 18:175: "the graded quotient comparison" restored (basis I).
6. 18:183: "normalized-null lemma of Chapter~\ref{ch13:continuum}" restored.
7. 19:22–23: "the prescribed coarse endpoint $\bar\beta$" (the term defined at 10:153).
8. 18:41: "the quotient by the polynomial labels all of whose separated correlations vanish".
9. 18r:5–6: "We use the independence of its constants from the number of reflected copies".
10. 19:99: "zero-energy subspace of the reflection Hilbert space of the undecomposed family".
11. 18:430: comma before "and identification".

After these corrections the files differ from HEAD on 58 / 14 / 37 lines; the editor's edit changed 63 / 17 / 38.

## Left for the author

- **Titles.** 18:119 "The replacement estimate with insertions" and 18:146 "[Replacement with insertions on the same history]" (formerly "The marked replacement estimate" and "[Same-history marked replacement]"). The entry *marked replacement* (D) says keep; *mark* 1 (R) lists 18:119. The wording is not wrong, so it was left. The same choice applies to the running text at 18:158 and 18:240.
- **19:20–21.** "admissible periods $R_p$ in continuum units" (formerly "admissible physical periods $R_p$"). Confirm the word order, or keep "physical" here as part of the *admissible periods* compound.
- **18:183.** Neither "normalized-null lemma" (committed; the observation has no number) nor "normalized-null statement" (18gq:9) is cited by number. The author may wish to number the observation in chapter 13 or to unify the two names.
- **18:174.** "the stronger anchored marked support bound" is kept (basis ?). Since "marked" → "with insertions" was applied elsewhere in the chapter, this phrase now stands alone.
- **19:56.** The theorem title "Assembly of the common Wilson family" keeps "common" (*common family* lists 19:56). It was not changed because label and title changes are the author's choice.
- **19:18–19.** "The cutoff-independent choices of Chapter 10 select all block lengths …". Here "choices … select" is slightly odd; "select" is basis I and was left.

## Words this file introduces that other chapters may also define

- *coincident points* / *subset of coincident points* / *pattern of coincident points*. This agrees with 1:424–426 and 14:18, 207, 253.
- *undecomposed* (correlations, family, vacuum functional). This agrees with chapters 14 and 15sp.
- *interacting quotient* and *inclusions of the interacting field spaces*, as in 18gq.
- *with insertions* for "marked". Chapter 17m, under another agent's review, uses the same word.
- *source degree at least two* (chapters 12–13).
- *constants independent of the number of reflected copies* (15:276).
- *lower bounds on the reference coupling* (chapter 11).
- *cutoff-independent choices* (chapter 19 only; the reading guide's "schedule" at RG:32 may need the same word).
- *zero-energy subspace* (chapter 15).
- *zero-mean trace* (17-trace-law, as currently edited).
- *compatibility with removal of an identity field* (also 18:430). 14:990 and 17:33 may phrase the same property differently.

## Checks

- Line counts: 18-operator-products 432 = 432 (HEAD); 18-raw-replacement 73 = 73; 19-assembly 162 = 162. `git diff --numstat`: 58/58, 14/14, 37/37. No line was joined, split, added or removed.
- `python3 tools/check_draft.py` (from manuscript/HumanizeYM_v3): "51 files; 679 labels; 1248 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-c89b monograph.tex`: exit 0. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build includes the chapter 17 files in whatever state the other reviewer had left them.
- No other file was edited. references.bib was not touched.

## Not checked

- The rendered pages were not inspected visually (pdftotext is not installed; only the log was checked).
- Senses were taken from the dictionary entries and the committed text; no Bałaban or Dimock paper and no source manuscript was opened.
- The parallel chapter 17 conversions were read only for the words "zero-mean" and "with insertions"; they were not reviewed.
