# Two-period control game (complete information), brute force over a grid of T.
# Period-1: U may demand control with transfer T and threat of Tier-3 (cost a1 to E) if refused.
# If refused, U chooses execute or not; execution raises period-1 pivot premium to Q1+a1.
# Payoffs relative to baseline (E Atlantic, zero transfers). U always wins contests (V large).
# E accept: T - sig - rc.  E refuse&exec: -a1 + max(0,Q1+a1) + d*max(0,Q2). E refuse&noexec: max(0,Q1)+d*max(0,Q2)
# U accept: -T. U refuse&exec: -max(0,Q1+a1) - d*max(0,Q2). U refuse&noexec: -max(0,Q1) - d*max(0,Q2). No demand: -max(0,Q1)-d*max(0,Q2)
import random
pos = lambda x: max(0.0, x)
def solve(Q1, Q2, a1, sig, rc, d, grid):
    nodemand = -pos(Q1) - d*pos(Q2)
    best = ('none', None, nodemand)
    for T in grid:
        # U's execution decision after refusal (ties -> execute)
        ex_U = -pos(Q1+a1) - d*pos(Q2)
        nx_U = -pos(Q1) - d*pos(Q2)
        execute = ex_U >= nx_U - 1e-12
        refuse_E = (-a1 + pos(Q1+a1) + d*pos(Q2)) if execute else (pos(Q1) + d*pos(Q2))
        accept_E = T - sig - rc
        if accept_E >= refuse_E - 1e-12:
            uU = -T
        else:
            uU = ex_U if execute else nx_U
        if uU > best[2] + 1e-9:
            best = ('demand', T, uU)
    return best
grid = [i*0.01 for i in range(0, 1001)]
random.seed(7)
bad = 0
for _ in range(300):
    Q1 = random.uniform(-6, 2); Q2 = random.uniform(-3, 4)
    a1 = random.uniform(0, 4); sig = random.uniform(0, 2); rc = random.uniform(0, 2); d = random.uniform(0.5, 1)
    res = solve(Q1, Q2, a1, sig, rc, d, grid)
    pred = (Q2 > 0) and (Q1 + a1 <= 0) and (a1 > sig + rc)
    got = res[0] == 'demand' and res[2] > -pos(Q1) - d*pos(Q2) + 0.011
    if pred != got:
        # allow grid-edge cases
        margin = min(abs(a1 - sig - rc), abs(Q1 + a1), abs(Q2))
        if margin > 0.03:
            bad += 1
            print('MISMATCH', dict(Q1=round(Q1,2), Q2=round(Q2,2), a1=round(a1,2), sig=round(sig,2), rc=round(rc,2), d=round(d,2)), 'pred', pred, 'got', res)
print('mismatches', bad)
