# Numerical checks

Brute-force checks of the results in the paper. Run any script with `python3 -I <script>.py`
(numpy and scipy required for a few). Scripts were written by independent adversarial verifiers
and test the published statements, including tie cases. No solver uses the formula it checks.
Appendix B of the paper (`paper/sections/B_numerics.tex`) describes each check.

## Current draft (v2)

Labels as in `notes/v2/resolutions.md` and the current paper. Results are named rather than numbered,
because LaTeX numbers them by order of appearance and several statements now sit in the paper's
supplementary appendix. Each script finishes in under 30 seconds.

| Script | Result(s) in the current draft | Label(s) |
|:--|:--|:--|
| `v2_m1_lemma1.py` | Bidding benchmark lemma, including the alternating-raise claim in Appendix A | `lem:bidding` |
| `v2_m1_prop1.py` | Bargaining with an outside option and rupture risk, and its corollary (threshold and channels); also the alternative exit timing (footnote), convergence near beta = 1, and the sign of P* | `prop:master`, `cor:master` |
| `v2_m3_prop2.py` | Slack principle, rationing corollary, policing a hedge (part (b) of the counter-threats proposition); also the burning example, a newly credible instrument (excess up to 4.91 over the initial credible set) and bundle-capped credibility | `prop:slack`, `cor:rationing`, `prop:counter` |
| `v2_rupture_bite.py` | Remark on slack under rupture risk: 13,079 draws, 0 violations of B_psi <= u + min{d, Lambda_psi}; agreement with the slack principle's bite at lambda = 0 to rounding (8.9e-16); the text's example (Lambda = 1, Lambda_psi = 2.2, bite 1.8) | `rem:rupture` |
| `v2_m3_prop2e.py` | Counter-threats (part (a) of the counter-threats proposition); loads the solver from `v2_m3_prop2.py` | `prop:counter` |
| `v2_m3_prop3.py` | Conditionality is the price of concessions, including part (d) | `prop:conditionality` |
| `v2_m4_prop4.py` | Preventive control, parts (a)-(c) of its corollary, and the special case stated after the proposition | `prop:control`, `cor:control` |
| `v2_m4_prop4_china.py` | Part (d) of the preventive-control corollary (counter-threats against a transfer); imports `v2_m4_prop4.py` | `cor:control` |
| `v2_m4_cuts_windows.py` | Spent and self-limiting cuts (part A) and windows (part B) | `lem:selflimit`, `cor:windows` |
| `v2_m4_selfbind.py` | Self-binding and dual key; imports `v2_m4_prop4.py` | `rem:bind` |
| `v2_m4_prop5.py` | Breakdown | `prop:breakdown` |
| `v2_m2_remarks_GFE.py` | Gatekeeper, firm between jurisdictions, blocking minorities, and the arithmetic in Table `tab:council`; reads population shares from `pop_check.py` (keep it in this folder) | `rem:gatekeeper`, `rem:firm`, `rem:council` |
| `council_revealed_blocking.py` | Blocking minorities and the Council arithmetic in `sec:council` and `app:scenario`: scenario coalition and its completions, revealed-position orderings, supermajority norms, exact Shapley-Shubik and Banzhaf indices, 2026 Council weights and EUROPOP2023 projections for 2029-2031 | `rem:council` |
| `v2_m2_prop6_holdup.py` | Pain and rupture (hold-up) | `prop:pain` |
| `v2_m2_interruption.py` | Interruption, including the timing variants (a)-(c) proved in Appendix A | `cor:interrupt` |

The v2 scripts' comments use the numbering of the verification reports
(`notes/v2/verify_m1.md` to `verify_m4.md`), which differs from the paper:

| Name in script comments | Result in the current draft |
|:--|:--|
| Proposition 2 (a)-(d), (f) in `v2_m3_*` | Slack principle (a)-(c), rationing corollary, counter-threats proposition (b); old (c)(iv) is slack principle (d) |
| Proposition 2(e) | Counter-threats proposition (a) |
| Proposition 3 in `v2_m3_prop3.py` | Conditionality proposition (`prop:conditionality`) |
| Proposition 4 and corollaries (i)-(iv), (v) in `v2_m4_*` | Preventive control (`prop:control`); its corollary's parts (a)-(c) are (i)-(iii), (iv) is the special case, part (d) is (v) |
| Lemma on multi-period cuts; windows corollary | `lem:selflimit`; `cor:windows` |
| Remark on self-binding vs dual key | `rem:bind` |
| Proposition 5 in `v2_m4_prop5.py` | Breakdown (`prop:breakdown`) |
| Remarks G, F, E | `rem:gatekeeper`, `rem:firm`, `rem:council` |
| Proposition 6 in `v2_m2_prop6_holdup.py` | Pain and rupture (`prop:pain`) |
| Interruption corollary | `cor:interrupt` |

In the scripts, `k` or `K_I` denotes the issuing cost and the investment cost (`iota` and `K` in the
paper), `w` the value per unit of slack (`nu`), and `w_b` or `omega_b` the rupture weight (`psi`).
In `v2_m4_prop4_china.py`, `r`, `gam*r` and `H_C` are China's punishment `r^c`, its execution cost
`e^C(r^c)` and its gain `z_C` when Europe keeps control; in `v2_m4_prop5.py`, `s0` is the purchase
cutoff `s_P`.

## Earlier draft (v1): superseded

The scripts below check the results of an earlier draft of the paper. Those results were revised or
replaced in the current draft, so the numbering in this table does not match the paper. They are
kept for the record.

| Script(s) | Result in the earlier draft |
|:--|:--|
| `lemma1_check.py` | Lemma 1 (credible conditionality) |
| `prop1_check.py`, `coh_prop1_random.py`, `coh_static.py` | Proposition 1 (exit premium) |
| `prop2_abcd_check.py` | Proposition 2 (a)-(d) (protocol bounds) |
| `prop2_ef_check.py`, `coh_protocol_e*.py` | Proposition 2 (e)-(f) |
| `prop3_check.py` | Corollary 2 (determinants of leverage) |
| `v_lemma2_prop4.py`, `v_prop4_classify.py`, `v_lemma3.py` | Lemmas 2-3, Proposition 3 (preventive control) |
| `v_cor2.py`, `v_cor2_classify.py`, `coh_windows.py`, `tperiod_quick.py` | Corollary 3 (windows) |
| `v_prop5.py`, `v_prop5_examples.py`, `coh_breakdown*.py` | Proposition 4 (breakdown) |
| `v_remark1.py`, `coh_dynamic_misc.py` | Remark 1 (self-binding) and misc. |
| `nested_ab.py`, `nested_check.py`, `nested_stats*.py`, `pop_check.py` | Proposition 5 (nested chokepoints, Council arithmetic) |
| `council_revealed_blocking.py` | Proposition 5(c): blocking minorities under revealed-position orderings, 2026 Council and EUROPOP2023 2029-2031 weights, supermajority-norm variants, exact Shapley-Shubik and Banzhaf indices (also used for the current draft; see above) |
| `holdup_a.py`, `holdup_b.py`, `holdup_abs.py`, `holdup_buffer.py`, `coh_holdup_dir.py` | Proposition 6 (time to pain) |
| `hedge_check.py` | Corollary 4 (marginal deterrence) |
| `misc_cex.py` | Counterexamples to earlier draft statements |

Note: these scripts use the earlier numbering in their comments (e.g. "Prop 4" for preventive
control, "Prop 5" for breakdown, "Prop 8" for marginal deterrence). `pop_check.py` is still needed
by `v2_m2_remarks_GFE.py`.
