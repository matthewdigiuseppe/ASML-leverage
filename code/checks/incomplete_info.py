# Prop 5 check: sigma ~ U[0, sb]; E accepts iff sigma <= T + a1 - rc - R; U payoff: accept -T, reject -R.
import random
def F(s, sb): return min(1.0, max(0.0, s/sb))
def best(R, a1, rc, sb):
    bestv, bestT = -R, None   # no demand
    for i in range(0, 20001):
        T = i*0.001
        s = T + a1 - rc - R
        v = F(s, sb)*(-T) + (1-F(s, sb))*(-R)
        if v > bestv + 1e-12: bestv, bestT = v, T
    if bestT is None: return None, 1.0
    s = bestT + a1 - rc - R
    return bestT, 1 - F(s, sb)
random.seed(3); bad = 0
for _ in range(200):
    R = random.uniform(0.01, 5); a1 = random.uniform(0, 6); rc = random.uniform(0, 3); sb = random.uniform(0.5, 6)
    a = a1 - rc
    T, brk = best(R, a1, rc, sb)
    if a <= 0:
        pred_demand = False
    else:
        pred_demand = True
    if a > 0:
        if a/2 <= R: s = min(a/2, sb)
        else: s = min(a - R, sb)
        pred_brk = 1 - min(1, s/sb)
    if (T is not None) != pred_demand:
        if abs(a) > 0.01: bad += 1; print('demand mismatch', R, a1, rc, sb, T)
    elif pred_demand and abs(brk - pred_brk) > 0.01:
        # corner where everyone accepts: s* = sb if a - x >= sb
        bad += 1; print('brk mismatch', dict(R=R, a1=a1, rc=rc, sb=sb), 'T', T, 'brk', brk, 'pred', pred_brk)
print('mismatches', bad)
