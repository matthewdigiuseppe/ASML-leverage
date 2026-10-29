"""Brute-force SPE of the static game (Proposition 1) on an offer grid.

Integer units.  lambda_C = a/b.  Europe: A iff b*(tU - rr + c) >= a*tC  (tie -> A, model rule).
China: picks payoff-maximising tC; if its max payoff is <= 0 it offers 0 ("does not bid").
US: we keep ALL payoff-maximising tU (no tie-breaking toward the stated result).
"""
import random
import numpy as np
from fractions import Fraction as F

def spe(W1, BC, BU, V, c, rr, a, b, e):
    tU = np.arange(0, BU + 1, e)
    tC = np.arange(0, BC + 1, e)
    exit_ = b * (tU[:, None] - rr + c) < a * tC[None, :]
    pay_C = np.where(exit_, W1 - tC[None, :], 0)
    mx = pay_C.max(axis=1)
    outcome_exit = np.empty(len(tU), dtype=bool)
    for i in range(len(tU)):
        if mx[i] <= 0:
            outcome_exit[i] = exit_[i, 0]          # China offers 0
        else:
            outcome_exit[i] = True                 # every maximiser wins (payoff>0)
    pay_U = np.where(outcome_exit, -V, -tU)
    best = pay_U.max()
    idx = np.where(pay_U == best)[0]
    return [(int(tU[i]), bool(outcome_exit[i])) for i in idx]

def Qval(W1, BC, c, rr, a, b):
    return F(a, b) * min(W1, BC) - c + rr

def run_random(n=3000, seed=2):
    rng = random.Random(seed)
    bad = []
    counts = dict(interior=0, exit_region=0)
    for _ in range(n):
        e = rng.choice([1, 2, 5])
        a, b = rng.choice([(1, 1), (1, 2), (2, 3), (3, 4), (3, 7)])
        W1 = rng.randint(0, 300)            # (1-theta)W, includes theta=1
        BC = e * rng.randint(0, 300 // e)
        BU = e * rng.randint(0, 300 // e)
        V = rng.randint(1, 300)
        c = rng.randint(0, 200)
        rr = rng.randint(0, 200) * rng.randint(0, 1)
        Q = Qval(W1, BC, c, rr, a, b)
        out = spe(W1, BC, BU, V, c, rr, a, b, e)
        lam = F(a, b)
        if Q < min(V, BU) - e:              # comfortably inside
            counts['interior'] += 1
            Qp = max(Q, 0)
            for tu, ex in out:
                if ex or not (Qp - lam * e <= tu <= Qp + e):
                    bad.append(('interior', W1, BC, BU, V, c, rr, (a, b), e, Q, out))
                    break
        elif Q > min(V, BU) + e:
            counts['exit_region'] += 1
            for tu, ex in out:
                if not ex:
                    bad.append(('exit', W1, BC, BU, V, c, rr, (a, b), e, Q, out))
                    break
    print('random draws:', counts, 'mismatches:', len(bad))
    for x in bad[:5]:
        print('  ', x)

def boundary_Q_equals_V():
    """Q = V with China's cap binding and Q off the grid: Prop 1 says A in every SPE."""
    # lambda=1, (1-theta)W = 2000, B_C = 1000, c = 293 (units of 1/1000)  -> Q = 707
    W1, BC, c, rr, a, b = 2000, 1000, 293, 0, 1, 1
    Q = Qval(W1, BC, c, rr, a, b)
    V = int(Q); BU = 1000
    print('Q =', Q, 'V =', V, 'B_U =', BU)
    for e in [100, 50, 20, 10, 5]:
        if BC % e or BU % e:
            continue
        out = spe(W1, BC, BU, V, c, rr, a, b, e)
        print(f'  mesh {e}: SPE (tau_U, exit?) ->', out[:3], '... n =', len(out),
              ' all exit' if all(x[1] for x in out) else '')
    # same with Q on the grid: indifference, both outcomes
    for e in [1]:
        out = spe(W1, BC, BU, V, c, rr, a, b, e)
        print(f'  mesh {e}: alignments in SPE set ->', sorted({x[1] for x in out}))

def theta_one():
    """theta=1 ((1-theta)W=0), chi_r r > c: Europe exits even at tau_C = 0."""
    out = spe(0, 100, 300, 500, 20, 70, 1, 1, 1)
    print('theta=1, rr=70>c=20: Q =', Qval(0, 100, 20, 70, 1, 1), 'SPE', out)

if __name__ == '__main__':
    run_random()
    boundary_Q_equals_V()
    theta_one()
