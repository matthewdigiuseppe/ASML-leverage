# Prop 1 on random draws: collect ALL SPE outcomes (US indifference broken either way) and check that,
# when Q < min{V, B_U} strictly (margin > 2*eps), every SPE has A and tU within [Q^+ - lam*eps, Q^+ + eps];
# when Q > min{V,B_U} (margin > 2 eps), every SPE has exit.
import random
ns = {}; exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "coh_static.py")).read().split('print("=== Prop 1 at the tie')[0], ns)
spe = ns['spe_outcomes']; pos = ns['pos']
random.seed(9); eps = 0.02; bad = 0; n = 0
for _ in range(400):
    lam = random.uniform(0.2, 1); w = random.uniform(0, 4); BC = round(random.uniform(0, 4) / eps) * eps
    c = random.uniform(-1, 3); rr = random.uniform(0, 1.5); V = random.uniform(0.1, 4); BU = round(random.uniform(0, 4) / eps) * eps
    Q = lam * min(w, BC) - c + rr; M = min(V, BU)
    if abs(Q - M) < 2 * eps or abs(Q) < 2 * eps: continue
    n += 1
    outs = spe(V, w, BC, BU, lam, c, rr, eps)
    if Q < M:
        ok = all(o[1] == 'A' and pos(Q) - lam * eps - 1e-9 <= o[0] <= pos(Q) + eps + 1e-9 for o in outs)
    else:
        ok = all(o[1] == 'X' for o in outs)
    bad += (not ok)
print("draws", n, "mismatches", bad)
