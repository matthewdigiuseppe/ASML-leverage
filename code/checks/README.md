# Numerical checks

Brute-force checks of the results in the paper. Run any script with `python3 -I <script>.py`
(numpy and scipy required for a few). Scripts were written by independent adversarial verifiers
and test the published statements, including tie cases. Mapping to the paper (proposition numbers
as in the current draft):

| Script(s) | Result |
|---|---|
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
| `holdup_a.py`, `holdup_b.py`, `holdup_abs.py`, `holdup_buffer.py`, `coh_holdup_dir.py` | Proposition 6 (time to pain) |
| `hedge_check.py` | Corollary 4 (marginal deterrence) |
| `misc_cex.py` | Counterexamples to earlier draft statements |

Note: the scripts use the earlier numbering in their comments (e.g. "Prop 4" for preventive
control, "Prop 5" for breakdown, "Prop 8" for marginal deterrence).
