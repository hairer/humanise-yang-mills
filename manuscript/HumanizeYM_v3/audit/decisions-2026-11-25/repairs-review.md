# Review of the sentence repairs

Independent agent, 25 November 2026, as handed back (condensed). All 51 changed lines of commit `c5bd232d` listed in `repairs-apply.md` were read in context, each against the cited source passage, which the reviewer opened. Result: 44 correct, 1 error and 1 minor defect corrected, 5 left for the author. No house word reintroduced; every added formula matches its source and v3's conventions.

## Corrected

- **9:950 (error).** The applying agent's clause attributed the band property of the output inverse coupling to (ch10:drift-floor) alone. Chapter 10 obtains it from Theorem ch10:finite-history (10:232–239), which keeps the couplings between `ℓ_m` and `u_m` (10:212–218) by the barrier inequalities, resting on (ch10:step-drift) and (ch10:drift-floor) (10:218–222). Now: "along the tuned histories of Theorem ch10:finite-history it does, by the barrier inequalities of Section ch10:shooting, which rest on (ch10:step-drift) and the condition (ch10:drift-floor) on the choice of". This wording is the reviewer's reading of 10:212–254, not a source sentence.
- **11:1285 (minor).** Removing "radial polynomial basis" had left "this basis" (11:1288) without antecedent; "expanded in the fixed radial polynomial basis" added.

## Left for the author

1. **12:131.** The new title "Independence of the graph at the ultraviolet cutoff" claims more than the proposition, which proves decay like `2^{1−h}` of the effect of the replaced graph. Suggested: "Forgetting the graph at the ultraviolet cutoff". The source title is "Forgetting the terminal graph".
2. **9s:259.** "Renormalization terms" stands for the source's "reset contribution" (Martin `pure-action-small-field.tex:104–107`); whether it is the coupling constant renormalization, the vacuum energy renormalization or both was not confirmed.
3. **10:626.** Agrees with Martin `background-test-prices.tex:83–97`, but `C_st` and the "principal" and "complementary regular bound" are defined nowhere in v3 (`C_st` already at 10:622).
4. **11:1343.** Whether "in the direction of the transfer" renders the source's "front-column bound" (Martin `actual-rank-purchases.tex:176–187`) was not confirmed.
5. **10:99.** "The value of the trial outside that chart": Scott `E-bounded-real.tex:10–17` does not state how the value off the chart is controlled.
6. **6:1544, 9:283–284.** Consistent with the dictionary's reading; the source's "seeds" also include coarse sites, and its reference law is formed at the identity coarse field.

## Verified points worth recording

7:195 index convention as at 7:182, 187; 7:427 `m_μ` (7:270), `M_μ` (7:276); 7:599 Martin `weighted-frame-penalty.tex:168–170`; 7:628 `R=(j+3)L` (4:17), `𝔹_R` (4:34); 9:77 equals the factor at 9:68; 9:147 `s_M`, `d_j` (9:100, 107); 10:169–172 (ch11:replicated-bound) is the Haar-ball lower bound, `o(τ_k)` at 13sb:104–110; 11:1595–1597 `2a ≤ K/4` is `4a_* ≤ K/2`, symbols at 11R:14, 76–78, 288–290; 14:186 Scott `G-section.tex:240`; 17:138–140 first-crossing argument checked; 17m:383–386 `v`, `s` defined at 17:172; 18:404 a fair condensation of Scott `J-section.tex:591–612`.

## Not checked

Rendered pages; the Lean source; where `R_*` (6:460) is defined. Checks run: line counts equal; `python3 tools/check_draft.py` passes.
