# Chapters 8 and 9s: review of the vocabulary conversion, and corrections (job b1f)

Files: `chapters/08-polymers.tex` (`8`) and `chapters/09-stationary-remainder.tex` (`9s`) in `/Users/mgubi/ym-terminology/manuscript/HumanizeYM_v3/`. Every changed line of both diffs was read against the committed text, the dictionary entry of the word, and chapters 4 and 5 as committed. Nothing committed or staged; corrections are within lines.

Counts: ERROR 0, LANGUAGE 4, DICTIONARY 1 (three lines), TERM 0, MISMATCH 0 (the DICTIONARY point is also a mismatch with chapter 4), MINOR 1. Six further points are not wrong and are left for the author.

## Review findings

| place | class | committed text | edited text | what was wrong | corrected text |
|---|---|---|---|---|---|
| 8:337–339 | DICTIONARY (and disagreement with chapter 4) | "need not contain every link read / by an activity. For example, … can / inspect a plaquette" | "need not contain every link on which an activity depends. / For example, … can / depend on a plaquette" | The entry *read* has basis I, so its proposal was not to be applied; converted chapter 4 keeps "reads" and "links read by other conditions" (4:450, 457, 460, 490). The meaning of the edit was right, but the rule and the agreement with chapter 4 both say to leave the word. | committed wording restored on the three lines |
| 8:228–229 | LANGUAGE | "their logarithmic / cluster terms cancel" | "the terms of the cluster / expansions of their logarithms cancel" | "their" refers to the two families of activities, which have no logarithm; the logarithm is that of the partition function (entry *logarithmic* 8: "of the logarithm of the partition function"). | "the terms of the cluster / expansions of the logarithms of their partition functions cancel" |
| 8:329 | LANGUAGE | "requires suppression of large-field activities by the / action" | "requires a decay factor of the large-field activities supplied by the / action" | Attachment unclear ("activities supplied by the action"). | "requires a decay factor for the large-field activities coming from the / action" |
| 9s:16 | LANGUAGE | "The other fine sectors have already been assigned" | "The other fine terms of the decomposition have already been attributed" | "fine terms" does not read as "terms at the fine scale". | "The other terms of the decomposition at the fine scale have already been attributed" |
| 9s:233 | LANGUAGE | "applies to the / folded auxiliary fields and their microscopic neighborhoods, which" | "auxiliary fields that are reflected periodic extensions, and their microscopic neighborhoods, which" | The comma detaches "their microscopic neighborhoods" from "applies to". | "auxiliary fields that are reflected periodic extensions and to their microscopic neighborhoods, which" |
| 8:269 | MINOR | "Boundedness of the undeformed gas" (unchanged by the editor) | same | With "source-deformed" replaced at 8:268, "undeformed" has no antecedent. | "Boundedness of the gas without sources" |

Points flagged by the editor, examined and found correct:

- **9s:219–220, "the term `C_{j,L}z^{-1}`" for "the microscopic term".** It is what the text says. The bound two lines above has exactly two terms, `C_{j,L}z^{-1}+L_0gD`; the second is made small by the choice of `d_0` in the same sentence; the first comes from the variation of `x` by `z^{-1}`, the radius the chapter calls microscopic (9s:93, 223). The basis-I proposal of *microscopic* ("neighborhood of radius `β̂^{-1}`") was not applied. A formula was introduced where a word stood; not wrong, left, listed below.
- **9s:230, "the linearization of the critical configuration (through its smooth representative `W_a`)".** Consistent with chapter 5: the derivative of the critical-configuration map is `W_F` (5:1145–1149), `W_a` is "the smooth representative of the linearization `W` of the critical configuration" (5:1234), the two have the same curl (5:1141–1143, 1153–1154), and the property used in the deduction, `d_{1,f}W_a = H_f^{-1}TH_c d_{1,c}` (9s:194), is stated for `W_a` (in chapter 5 for `W_s`, (ch05:physical-transports), which has the same curl). "its second derivatives" can only be those of the critical configuration (9s:199–200), since `W_a` is linear. Left.
- **8:355, two equations cited by number.** `ch08:deletion-identity` is the "removal" formula (8:208–217) and `ch08:reassembly` the "exact factorization" (8:310–316); both labels exist and both are identities. Correct; not a vocabulary change, listed below.
- **"polymer activities `z_γ`" for "regular activities" (8:285, 318, 322, 331, 333).** The chapter 8 object is the abstract polymer activity: `z_γ` is the complex number of 8:24–27 ("called its activity"), a factor in the gas (ch08:gas). Chapter 4's localized term `E_i^reg` is an additive term of the exponent and is a different object; the entry *regular activity* separates the two senses (sense 2, basis R, "polymer activity `z_γ`; not regular activity"). The edit is right, and "localized term" would have been wrong here.
- **"margin `δ` in the decay rate of the support weight" (8:150, 331, 362).** The entry proposes "margin `δ` in the decay rate". The added words "of the support weight" agree with the parallel conversion of chapter 6 as it stands in the worktree ("a decay rate `α>0` of the support weight", 6:1170; 6:1556) and with the entry *support exponent* ("decay rate (in the support weight)"). Read literally the weight `e^{αc(X)}` grows and it is the activities that decay; left as it is for agreement with chapter 6, listed below.

Other checks on every changed line: no hypothesis, quantifier or claim changed; no symbol, label or macro argument changed; no sentence about Bałaban's or Dimock's papers and no citation was added in either file; the words agree with chapters 4 and 5 (*base point*, *anchored*, *prescribed large-field set*, *dependence set*, *normalization constant*, *renormalization-group trajectory*, *regularity condition*, *auxiliary index `α`* with *probability weights*, *averaging operation*, *block axial gauge / chart*, *critical configuration*, *critical-configuration map*, *penalty term of the block kernel*, *induced map on curvatures*, *representative `W_F` in the block axial chart*, *smooth representative `W_a`*).

## Corrections applied

1. 8:229 — "of the logarithms of their partition functions".
2. 8:269 — "the gas without sources".
3. 8:329 — "a decay factor for the large-field activities coming from the".
4. 8:337, 338, 339 — committed wording restored ("read / by an activity", "inspect").
5. 9s:16 — "The other terms of the decomposition at the fine scale".
6. 9s:233 — "reflected periodic extensions and to their microscopic neighborhoods".

## Left for the author

- **Formulas and equation numbers introduced where words stood** (correct, but more than a change of words): 9s:79 `z^{o(1)}` for "subpower"; 9s:127 `χ(U_p) ≤ t_f` after "regularity condition"; 9s:139 and 9s:232 `\eqref{ch05:nonlinear-tree}`; 9s:165–166 the factor `Ω e^{-Φ(x)}` for "in stationary units" (the repair of Appendix D, consistent with (ch09:exterior-bound)); 9s:219–220 `C_{j,L}z^{-1}` for "the microscopic term"; 9s:283–284 "the left side of (ch09:pure-decomposition) minus its value at zero" (Appendix D); 8:355 the two equation numbers.
- **Titles**: 8:279 "Large-field constraints and the factorization identity" (was "exact reassembly"); 9s:111 "… in the pure block integral" (was "actual integral"; the entry *actual* 1 says only "delete").
- **9s:295 "Original"** for "Actual": sense 9 of *actual* has basis I; applied under the editors' instruction to follow that entry. The contrast with "reflected" in the same sentence supports it.
- **"decay rate of the support weight"** (8:150, 331, 362): see above; one wording should be fixed for chapters 6, 8 and 9.
- **"term of the decomposition"** (8:28, 359; 9s:16, 171) has no definition in these files; it relies on chapter 6 (6:85–87), which must define it. 8:359 "every large-field term of the decomposition" may read better as "every term of the large-field decomposition" (the phrase of 8:373).
- **9s:230 "its second derivatives"**: the antecedent is the critical configuration; the author may prefer to say so.
- **`D` and `I_η`**: "prescribed large-field set" names `I_η` (8:288, as chapter 4), while `D` is "the set of sites prescribed as lying in the large-field region" (8:284); the dictionary gives the one name to both.
- The editor's own list "Not changed, for the author" stands; nothing in it was found to need a change.

## Words this file introduces that other chapters may also define

- *term of the decomposition* (chapter 6 owns the definition; chapters 9–11 use "sector").
- *polymer activities `z_γ`* / *polymers `γ`* against *large-field activities* (chapter 9 says "ordinary"; `09-forest-average.tex` and `09-renormalization.tex` already say "polymer activities").
- *margin (`δ`) in the decay rate of the support weight* (chapter 9: 9:267, 438, 687, 919; chapter 6 has "decay rate of the support weight").
- *rescaled activities* (also 9:180).
- *source-dependent activities* (chapter 8 only at present).
- *anchored* norm (chapter 4 has "anchored sum").
- *factorization identity*; *deletion identity* (11R:238–239 cites `ch08:deletion-identity`).
- *pure* block integral (9:969).
- *safe chart*; *deviation* of the coarse links from the values of the averaging operation (chapter 6: "mismatch", "block average discrepancy"; 4:397).
- *reflected periodic extension*, *reflection map* (the map is at 9:326–330).
- *lower bound on `z`* for "coupling threshold" (chapters 6, 7, 9–11: "lower bound on `β̂`").

## Checks

Run after the corrections:

- Line counts: `08-polymers.tex` 374 = 374 at HEAD; `09-stationary-remainder.tex` 301 = 301 at HEAD.
- `git diff --stat` for the two files: 31 and 54 changed lines (three lines of chapter 8 are back to the committed text).
- `python3 tools/check_draft.py` (from `manuscript/HumanizeYM_v3`): "51 files; 679 labels; 1214 references. All explicit cross-references resolve; no duplicate labels."
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/private/tmp/claude-501/-Users-mgubi-humanise-yang-mills/d57c97db-1eb7-4140-8a5d-1c6dc4dec0db/scratchpad/v3build-b1f monograph.tex`: exit 0, three runs. In `monograph.log`: "undefined" 0, "Citation" 0, "Overfull" 0. The build included the other chapters as they stood in the worktree at that moment (1, 2, 2e, 3, 6, 7, main-theorem, reading-guide modified by others).

## Not checked

- The rendered PDF pages were not looked at.
- Bałaban's and Dimock's papers were not opened (no sentence about them was added in these files).
- The Appendix D repairs were checked against the chapter text and its formulas, not against the source manuscripts they quote.
- `figures/exact-cover.tex` (input at 8:300) was not opened.
- Chapters 6 and 7 were read only by search, in their uncommitted state, for the words shared with these files.
