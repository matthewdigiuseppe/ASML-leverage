import random, sys
sys.path.insert(0, '.')
from v_cor2 import solve_P, solve_set, eligible_dates, pos, bite
from collections import Counter

def generic_tie_dates(par):
    Q, A, G, mbar, sig, rc, d = par
    T = len(Q)
    out = []
    for t in range(T):
        Delta = pos(Q[t]+A[t]) - pos(Q[t])
        cred = mbar + G[t] > Delta
        if cred and bite(Q[t], A[t]) > sig + rc and not any(Q[s] > 0 for s in range(t+1, T)):
            out.append(t)
    return out

rng = random.Random(5); random.seed(6)
C = Counter(); ex = {}
for i in range(60000):
    T = rng.randint(2, 6)
    q = rng.uniform(-6, 1); Q = []
    for t in range(T):
        Q.append(q); q += rng.uniform(-3, 3.5)
    A = [rng.uniform(0, 5) for _ in range(T)]
    G = [-rng.uniform(0.01, 3) for _ in range(T)]
    mbar = rng.uniform(0, 8); sig = rng.uniform(0.01, 3); rc = rng.uniform(0, 3)
    d = rng.choice([1.0, rng.uniform(0.05, 1)])
    par = (Q, A, G, mbar, sig, rc, d)
    pred = len(eligible_dates(par)) > 0
    S = solve_set(par, markov=True)
    issued = [s for s in S if s[2] is not None]
    C['n'] += 1
    if not pred and issued:
        C['pred NO, Markov SPE with ultimatum'] += 1
        gt = generic_tie_dates(par)
        if gt: C['  ...and a generic tie date (b_t>sig+rc, credible, no later Q>0) exists'] += 1
        # is any issuance strict at a non-tie date? i.e. issue date not in generic tie dates
        strict_early = [s for s in issued if s[2] not in gt]
        if strict_early:
            C['  ...with an SPE issuing at a date that is NOT itself a tie date (tie propagates)'] += 1
            ex.setdefault('propagated', (par, sorted(S, key=str)))
        else:
            ex.setdefault('direct', (par, sorted(S, key=str)))
    if pred and any(s[2] is None for s in S):
        C['pred YES, Markov SPE without ultimatum'] += 1
print(dict(C))
for k, v in ex.items():
    print('\n==', k); print('  par', v[0]); print('  SPE set', v[1])

print('\n--- Explicit example A (no eligible date; tie at date 3 propagates to strict issuance at date 1)')
par = ([-0.5, 2.0, -3.0], [1.0, 0.0, 3.0], [-0.5, -0.5, -0.5], 10.0, 1.0, 0.0, 0.9)
print('eligible dates:', eligible_dates(par), ' paper-convention issue date:', solve_P(par))
for s in sorted(solve_set(par, markov=True), key=str): print('  Markov SPE (U,E,issue date idx0):', s)

print('\n--- Explicit example B (paper convention issues outside the US window)')
par = ([-0.5, -3.0, 5.0], [2.0, 3.0, 0.0], [-0.5, -0.5, -0.5], 10.0, 1.0, 0.0, 0.9)
print('eligible dates (idx0):', eligible_dates(par), ' paper-convention issue date idx0, VU, VE:', solve_P(par))
print('bite at date1 =', bite(-0.5, 2.0), ' sig+rc =', 1.0)
par2 = ([-0.5, -3.0, 5.0], [2.0, 3.0, 0.0], [-0.5, -0.5, -0.5], 10.0, 1.0, 0.0, 1.0)
print('same with delta=1:', solve_P(par2))
