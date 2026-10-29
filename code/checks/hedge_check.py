# Proposition 8 (marginal deterrence). After a hedge the US decides whether to withhold instrument k.
# Withholding: ex post gain g, removes D from Europe's exit costs. Not withholding: audience cost m.
# Then the static contest of Prop 1 is played (brute force: US offers on a grid, China best-responds on a grid,
# Europe picks A iff tau_U >= lam*tau_C - c; China bids only if strictly profitable; US may let Europe exit).
import random, math
import numpy as np

def contest_US_payoff(c, omega_cap, W, V, BU, eps=0.01):
    """US equilibrium payoff in the static contest with lam=1, chi_r r=0, China cap omega_cap (B_C), China value W."""
    grid_U = np.arange(0, BU + 1e-9, eps)
    grid_C = np.arange(0, omega_cap + 1e-9, eps)
    best = -math.inf
    for tU in grid_U:
        # China's cheapest winning offer: smallest grid tC with tC - c > tU
        win = grid_C[grid_C - c > tU + 1e-12]
        china_wins = len(win) > 0 and (W - win[0]) > 1e-12
        pay = -V if china_wins else -tU
        if pay > best:
            best = pay
    return best

random.seed(2)
mism_formula = 0; mism_cond = 0; n = 0; cex = []
for trial in range(400):
    W = 5.0; omega_cap = 3.0           # China's credible offer omega = 3
    Q = round(random.uniform(-3, 2.5), 2)
    c = omega_cap - Q                  # so that Q = omega - c
    D = round(random.uniform(0, 3), 2)
    V = round(random.uniform(0.2, 6), 2); BU = round(random.uniform(0.2, 6), 2)
    m = round(random.uniform(0, 1.5), 2); g = round(random.uniform(-1.5, 2.0), 2)
    u_no = -m + contest_US_payoff(c, omega_cap, W, V, BU)
    u_wh = g + contest_US_payoff(c - D, omega_cap, W, V, BU)
    actual = u_wh >= u_no - 1e-9
    lhs = m + g; rhs = max(Q + D, 0) - max(Q, 0)
    pred = lhs >= rhs
    n += 1
    close = abs(lhs - rhs) < 0.03
    in_region = (Q + D <= min(V, BU)) and (Q <= min(V, BU))
    if pred != actual and not close:
        if in_region:
            mism_formula += 1
        else:
            mism_cond += 1
            if len(cex) < 3:
                cex.append(dict(Q=Q, D=D, V=V, BU=BU, m=m, g=g, lhs=lhs, rhs=rhs, pred=pred, actual=actual))
print(f"{n} draws; mismatches inside Q+D_k <= min(V,B_U): {mism_formula}; mismatches outside that region: {mism_cond}")
for e in cex:
    print("  counterexample:", e)

# Third sentence: 'If Q + D_k > 0 and audience costs are small, the US cannot use security or AI linkage'
Q, D, m, g = 0.5, 1.0, 0.0, 1.2      # AI inside the scarcity window with nu - k_H = 1.2
V = BU = 10.0; c = 3.0 - Q
u_no = -m + contest_US_payoff(c, 3.0, 5.0, V, BU); u_wh = g + contest_US_payoff(c - D, 3.0, 5.0, V, BU)
print("g_k(H)>0 example: Q=0.5, D_k=1, m_k=0, g_k(H)=1.2 -> withholding credible?", u_wh >= u_no, "(US payoffs", round(u_wh, 3), "vs", round(u_no, 3), ")")
