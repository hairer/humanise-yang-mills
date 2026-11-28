# Verification pass over the dictionary (26 November 2026)

Issue 1 of the fork, item 15a. `../terminology.md` at commit `54590227` was split into six parts of about 236 entries. One agent per part, three at a time, checked every entry against the current text and the cited sources, following one brief: the *Now* / *Formerly* / *In the text* lines, quotations of v3, references, counts below 30, meaning against the cited defining lines, *Adopted* / *Proposed*, *Source* citations, cross-references, format. Agents corrected only what they had verified to be wrong; headwords were not added, removed or reordered.

| Part | Entries | Corrected |
|---|---|---|
| 1 absorb … contraction derivative | 236 | 53 |
| 2 contraction estimate … floor | 236 | 54 (16 format only) |
| 3 fluctuation … local inverse columns | 236 | 28 |
| 4 local means … pre-L factor | 237 | 22 |
| 5 pre-ratio constants … small-field | 236 | 34 |
| 6 small-field at the new threshold … zero-mean | 236 | 48 |
| | 1,417 | 239 |

The corrections are in the git diff of `terminology.md` for this commit. Each `partN.md` records the corrections of substance, what was found doubtful and left, statements of the manuscript text noticed to be inconsistent or undefined, and what was not checked.

One consequence for the text: decision 52 of 25 November had not been applied at 10:446, 651, 772, 842–843, 902 and 13sb:26 (found by part 5); applied in commit `7d10536a`.

Limits. Not checked: *Literature* lines (the papers were not available to the agents); the mathematics of Lean declarations (only file and declaration name); long quotations of the sources word for word; *Where* lists of 30 or more items beyond spot checks. Each entry had one verifier, and the corrections were not themselves reviewed. The agent for part 1 delegated its part to four copies of itself.
