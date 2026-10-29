"""Remark 1 (self-binding). Europe binds before period 1 at cost sc (+ China punishes with rb);
binding sets the period-2 exit premium to -infinity. Then the two-period game of Prop 4 is played.
We compute SPE outcome sets of the post-binding and no-binding subgames (all tie-breaks) using
spe_outcomes from v_lemma2_prop4, and Europe's strict preference to bind."""
import random, sys
sys.path.insert(0, '.')
from v_lemma2_prop4 import spe_outcomes, pos
rng = random.Random(21)
n = 0; bad_paper = 0; bad_adv = 0; ex = None
for i in range(100000):
    Q1 = rng.uniform(-8, 0); a1 = rng.uniform(0, 6); Q2 = rng.uniform(0.01, 6)
    gN = -rng.uniform(0.01, 3); mbar = rng.uniform(0, 10)
    sig = rng.uniform(0, 3); rc = rng.uniform(0, 3); d = rng.uniform(0.05, 1)
    sc = rng.uniform(0, 3); rb = rng.uniform(0, 3)
    b1 = min(a1, pos(-Q1))
    if not (Q2 > 0 and mbar + gN >= pos(Q1 + a1) and b1 > sig + rc):
        continue
    n += 1
    claim = (sc + rb < sig + rc) and (sc + rb < b1 - d * Q2)
    # no-binding: unique SPE (strict conditions) -> Europe gets max{dQ2-b1, -sig-rc}
    Enb = {round(o[2], 9) for o in spe_outcomes(Q1, Q2, a1, gN, mbar, sig, rc, d)}
    # binding: Q2 -> -inf (use a very negative number)
    Eb = {round(o[2] - sc - rb, 9) for o in spe_outcomes(Q1, -1e6, a1, gN, mbar, sig, rc, d)}
    # paper convention: no ultimatum when US indifferent -> binding payoff -sc-rb
    paper = (-sc - rb) > max(Enb) + 1e-12
    if paper != claim: bad_paper += 1
    # adversarial: does there exist an SPE after binding in which binding is NOT strictly better?
    adv_bind_strict = min(Eb) > max(Enb) + 1e-12
    if claim and not adv_bind_strict:
        bad_adv += 1
        if ex is None: ex = (Q1, Q2, a1, gN, mbar, sig, rc, d, sc, rb, sorted(Eb), sorted(Enb))
print('draws satisfying Prop 4 conditions:', n)
print('mismatches under paper tie-break (US does not issue when indifferent):', bad_paper)
print('cases where Remark claims strict preference but some post-binding SPE has Europe coerced for T=0:', bad_adv)
print('example (Q1,Q2,a1,gN,mbar,sig,rc,d,sc,rb, E-payoffs after binding, E-payoffs without):', ex)
