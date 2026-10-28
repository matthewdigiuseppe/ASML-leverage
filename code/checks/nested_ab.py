# Prop 6(a),(b) and K(0) brute-force checks
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random, itertools, math
import numpy as np
from hedge_check import contest_US_payoff
from nested_check import make_game, K0

random.seed(8)
bad_a = 0; n_a = 0
for trial in range(300):
    omega = 3.0; Q = round(random.uniform(-2, 2.5), 2); ks = round(random.uniform(0, 2), 2)
    y = round(random.uniform(0, 2), 2); fF = round(random.uniform(0, 2), 2)
    V = BU = 10.0
    c_eff = omega - Q + ks * (y < fF)       # compulsion cost adds to the cost of exit
    pay = -contest_US_payoff(c_eff, omega, 5.0, V, BU)
    pred = max(Q - ks * (y < fF), 0)
    n_a += 1
    if abs(pay - pred) > 0.011: bad_a += 1
print(f"6(a): {n_a} draws, |US payment - [Q - k_s 1(y<f^F)]^+| > mesh in {bad_a}")
# 6(b): payment change from a conditional benefit Delta to h
for Qh, Dl in ((1.0, 0.4), (0.3, 1.0), (-0.5, 1.0)):
    p0 = -contest_US_payoff(3.0 - Qh, 3.0, 5.0, 10, 10); p1 = -contest_US_payoff(3.0 - Qh + Dl, 3.0, 5.0, 10, 10)
    print(f"6(b): Q_h={Qh}, Delta={Dl}: payment {p0:.2f} -> {p1:.2f} (drop {p0-p1:.2f}; min(Delta,[Q_h]^+) = {min(Dl, max(Qh,0)):.2f})")
# 6(b) without Q_h <= min(V,B_U): US does not pay [Q_h]^+
print("6(b): Q_h=2, V=1: US payoff", contest_US_payoff(1.0, 3.0, 5.0, 1.0, 10.0), "(Europe exits; [Q_h]^+ = 2 is not paid)")
# K(0) brute force: min sum tau on grid s.t. {i: q_i > tau_i} is not winning
mm = 0
for trial in range(300):
    n = random.randint(3, 5)
    wt = np.random.dirichlet(np.ones(n)); W = set(make_game(n, "weighted", (wt, random.uniform(0.5, 0.8))))
    if not W: continue
    q = [random.choice([-1, -0.5, 0, 0.5, 1, 1.5]) for _ in range(n)]
    grid = [0, 0.5, 1, 1.5]
    best = min(sum(t) for t in itertools.product(grid, repeat=n)
               if not any(S <= frozenset(i for i in range(n) if q[i] > t[i]) for S in W))
    if abs(best - K0(n, list(W), q)) > 1e-9: mm += 1
print("K(0) brute-force mismatches:", mm)
