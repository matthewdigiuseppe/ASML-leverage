# Corollary 2 (windows) and Figure 2 caption: WHEN does the US issue the ultimatum on the equilibrium path?
# N-period model as in the paper / code/checks/tperiod.py: state = Europe holds control at t.
# U may issue a public ultimatum at t; accept -> control transfers for all remaining periods, E pays c0 = sigma + r^c
# once and gets T; refuse -> U cuts AI in period t only (if credible), rent in t becomes [Q_t + a_t]^+.
# No tie-breaking in favour of the result: U issues only if STRICTLY better; we also report the date under the
# opposite tie-break (issue when indifferent). Credibility of the cut is assumed (mbar large) so b_t = min(a_t, [-Q_t]^+).
import random
pos = lambda x: max(0.0, x)

def solve(Q, a, d, c0, issue_if_indiff=False):
    N = len(Q)
    VE, VU = 0.0, 0.0
    plan = [False] * N
    for t in range(N - 1, -1, -1):
        nE = pos(Q[t]) + d * VE; nU = -pos(Q[t]) + d * VU          # no ultimatum at t
        rE = pos(Q[t] + a[t]) - a[t] + d * VE                      # refuse, cut (continuation = no-ultimatum-at-t path)
        T = pos(rE + c0)
        better = (-T > nU + 1e-12) or (issue_if_indiff and -T >= nU - 1e-12 and T < nU * -1 + 1e-12 and pos(Q[t]) + d*VE != None)
        if issue_if_indiff:
            better = -T >= nU - 1e-12 and any(pos(-Q[t]) > 0 for _ in [0]) and (-T > nU + 1e-12 or abs(-T - nU) <= 1e-12)
            # only count indifference as issuing when the ultimatum is actually used against future rents
            better = better and any(Q[s] > 1e-12 for s in range(t + 1, N))
        if better:
            VE, VU = T - c0, -T; plan[t] = True
        else:
            VE, VU = nE, nU
    path = next((t for t in range(N) if plan[t]), None)
    return path

def eligible(Q, a, c0):
    N = len(Q)
    return [t for t in range(N) if min(a[t], pos(-Q[t])) > c0 + 1e-12 and any(Q[s] > 1e-12 for s in range(t + 1, N))]

print("=== Figure 2 panel (a) parameters: Q_t = -3.4 + 0.42 t, alpha = 2, sigma + r^c = 1 ===")
Q = [-3.4 + 0.42 * t for t in range(11)]; a = [2.0] * 11; c0 = 1.0
el = eligible(Q, a, c0)
print("eligible dates (US window with later rents):", el, "| caption says demand at last date:", el[-1])
for d in [0.9, 0.95, 1.0]:
    print(f"  delta={d}: on-path ultimatum date (strict) = {solve(Q, a, d, c0)}, "
          f"(issue-when-indifferent) = {solve(Q, a, d, c0, True)}")

print("\n=== Ultimatum OUTSIDE the US window (b_t <= sigma + r^c) ===")
Q = [-1.5, -3.0, 5.0]; a = [0.5, 3.0, 0.0]; c0 = 1.0
print("Q =", Q, "a =", a, "c0 =", c0, "bites =", [min(x, pos(-q)) for q, x in zip(Q, a)], "eligible =", eligible(Q, a, c0))
for d in [1.0, 0.9]:
    print(f"  delta={d}: on-path ultimatum date = {solve(Q, a, d, c0)}")

print("\n=== Random draws: how often is the on-path date the LAST eligible date? ===")
random.seed(5)
n = 50000; stats = dict(last=0, earlier_in_window=0, outside_window=0, none=0)
for _ in range(n):
    N = random.randint(3, 7)
    x = random.uniform(-6, 0); Q = []
    for _ in range(N): Q.append(x); x += random.uniform(-0.5, 2.5)
    a = [random.uniform(0, 4) for _ in range(N)]
    d = random.uniform(0.6, 1.0); c0 = random.uniform(0, 1.5)
    el = eligible(Q, a, c0); p = solve(Q, a, d, c0)
    assert (p is not None) == (len(el) > 0)          # existence part of Corollary 2
    if p is None: stats['none'] += 1
    elif p == el[-1]: stats['last'] += 1
    elif p in el or min(a[p], pos(-Q[p])) > c0: stats['earlier_in_window'] += 1
    else: stats['outside_window'] += 1
print(stats, "of", n)
