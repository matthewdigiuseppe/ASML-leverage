"""Brute force of Proposition 2, cases (b) simultaneous, (c) China first, (d) Europe TIOLI.

Integer units, lambda_C = a/b, mesh e.  Europe: A iff b*(tU - rr + c) >= a*tC (tie -> A).
No tie-breaking for the US or China beyond what the model states; we enumerate all
equilibria and compare the set of supported transfers L with the stated sets.
"""
import random
import numpy as np
from fractions import Fraction as F

def Q_of(W1, BC, c, rr, a, b):
    return F(a, b) * min(W1, BC) - c + rr

def Lbar_of(V, BC, c, rr, a, b):
    return min(F(V), max(F(0), F(a, b) * BC - c + rr))

def L0_of(c, rr):
    return max(F(0), F(rr - c))

def payoff_mats(W1, BC, BU, V, c, rr, a, b, e):
    tU = np.arange(0, BU + 1, e)
    tC = np.arange(0, BC + 1, e)
    ex = b * (tU[:, None] - rr + c) < a * tC[None, :]
    uU = np.where(ex, -V, -tU[:, None])
    uC = np.where(ex, W1 - tC[None, :], 0)
    return tU, tC, ex, uU, uC

def case_b(W1, BC, BU, V, c, rr, a, b, e, undominated=False):
    tU, tC, ex, uU, uC = payoff_mats(W1, BC, BU, V, c, rr, a, b, e)
    cols = np.arange(len(tC))
    if undominated:
        keep = []
        for j in cols:
            dom = False
            for k in cols:
                if k == j:
                    continue
                if np.all(uC[:, k] >= uC[:, j]) and np.any(uC[:, k] > uC[:, j]):
                    dom = True
                    break
            if not dom:
                keep.append(j)
        cols = np.array(keep)
    brU = uU[:, cols] == uU[:, cols].max(axis=0)[None, :]
    brC = uC[:, cols] == uC[:, cols].max(axis=1)[:, None]
    ne = np.argwhere(brU & brC)
    res = []
    for i, jj in ne:
        j = cols[jj]
        res.append((int(tU[i]), int(tC[j]), bool(ex[i, j])))
    return res

def case_c(W1, BC, BU, V, c, rr, a, b, e, undominated=False):
    """China moves first. For each tC, US best-response set (all maximisers).
    SPE: tC* with some selection s(tC*) such that China's payoff >= worst-case payoff
    (minimised over US BR selections) of every other tC."""
    tU, tC, ex, uU, uC = payoff_mats(W1, BC, BU, V, c, rr, a, b, e)
    cols = list(range(len(tC)))
    if undominated:
        # extensive-form weak dominance: US response at each tC arbitrary
        keep = []
        for j in cols:
            dom = False
            for k in cols:
                if k == j:
                    continue
                if uC[:, k].min() >= uC[:, j].max() and not (
                        uC[:, k].min() == uC[:, k].max() == uC[:, j].min() == uC[:, j].max()):
                    dom = True
                    break
            if not dom:
                keep.append(j)
        cols = keep
    br = {}
    for j in cols:
        col = uU[:, j]
        br[j] = np.where(col == col.max())[0]
    worst = {j: min(uC[i, j] for i in br[j]) for j in cols}
    thresh = max(worst.values())
    res = []
    for j in cols:
        for i in br[j]:
            if uC[i, j] >= thresh:
                res.append((int(tU[i]), int(tC[j]), bool(ex[i, j])))
    return res

def case_d(W1, BC, BU, V, c, rr, a, b, e):
    """Europe demands d (grid); US accepts/rejects; after rejection China offers
    (no bid at zero profit) and Europe chooses. All US-optimal responses kept."""
    tC = np.arange(0, BC + 1, e)
    exr = b * (0 - rr + c) < a * tC          # exit after rejection with tU = 0
    pC = np.where(exr, W1 - tC, 0)
    if pC.max() <= 0:
        rej_exit = bool(exr[0])
    else:
        rej_exit = True
    uU_rej = -V if rej_exit else 0
    outs = set()
    best_E = None
    for d in range(0, BU + 1, e):
        acc_vals = []
        if -d >= uU_rej:
            acc_vals.append(('acc', d))
        if -d <= uU_rej:
            acc_vals.append(('rej', 0 if not rej_exit else None))
        for kind, val in acc_vals:
            outs.add((d, kind))
    # Europe's payoff from demand d (in units of utility, ignoring -rr common): accepted -> d
    # rejected and exit -> approx lowest winning China offer value; rejected and A -> 0
    return rej_exit, uU_rej

def L_set(res):
    return sorted({tu for tu, tc, ex in res if not ex}), any(ex for _, _, ex in res)

def run(n=400, seed=3):
    rng = random.Random(seed)
    stats = dict(b=0, b_und=0, c=0, c_und=0, d=0)
    bad = dict(b=[], b_und=[], c=[], c_und=[], d=[])
    for _ in range(n):
        e = rng.choice([2, 5])
        a, b = rng.choice([(1, 1), (1, 2), (2, 3), (3, 4)])
        W1 = rng.randint(1, 120)
        BC = e * rng.randint(0, 120 // e)
        c = rng.randint(0, 80)
        rr = rng.randint(0, 80) * rng.randint(0, 1)
        Q = Q_of(W1, BC, c, rr, a, b)
        V = rng.randint(max(1, int(Q) + 3 * e), 160) if Q + 3 * e < 160 else None
        if V is None:
            continue
        BU = e * (V // e + 2)                      # B_U >= V
        Qp = max(Q, F(0)); Lb = Lbar_of(V, BC, c, rr, a, b); L0 = L0_of(c, rr)
        lam = F(a, b)
        tol = e
        # (b)
        res = case_b(W1, BC, BU, V, c, rr, a, b, e)
        Ls, anyexit = L_set(res)
        stats['b'] += 1
        if anyexit or not Ls or min(Ls) < Qp - tol or max(Ls) > Lb + tol or min(Ls) > Qp + tol or max(Ls) < Lb - tol:
            bad['b'].append((W1, BC, BU, V, c, rr, (a, b), e, float(Q), float(Lb), Ls[:3], Ls[-3:], anyexit))
        res = case_b(W1, BC, BU, V, c, rr, a, b, e, undominated=True)
        Ls, anyexit = L_set(res)
        stats['b_und'] += 1
        if anyexit or not Ls or min(Ls) < Qp - tol or max(Ls) > Qp + tol:
            bad['b_und'].append((W1, BC, BU, V, c, rr, (a, b), e, float(Q), Ls, anyexit))
        # (c)
        res = case_c(W1, BC, BU, V, c, rr, a, b, e)
        Ls, anyexit = L_set(res)
        stats['c'] += 1
        if anyexit or not Ls or min(Ls) > L0 + tol or min(Ls) < L0 - tol or max(Ls) > Lb + tol or max(Ls) < Lb - tol:
            bad['c'].append((W1, BC, BU, V, c, rr, (a, b), e, float(Q), float(L0), float(Lb), Ls[:3], Ls[-3:], anyexit))
        res = case_c(W1, BC, BU, V, c, rr, a, b, e, undominated=True)
        Ls, anyexit = L_set(res)
        stats['c_und'] += 1
        if anyexit or not Ls or min(Ls) > L0 + tol or min(Ls) < L0 - tol or max(Ls) > Qp + tol or max(Ls) < Qp - tol:
            bad['c_und'].append((W1, BC, BU, V, c, rr, (a, b), e, float(Q), float(L0), Ls[:3], Ls[-3:], anyexit))
        # (d)
        rej_exit, uU_rej = case_d(W1, BC, BU, V, c, rr, a, b, e)
        # US accepts d iff -d >= uU_rej; Europe's best accepted demand:
        maxd = max(d for d in range(0, BU + 1, e) if -d >= uU_rej)
        stats['d'] += 1
        pred = V if Q > 0 else 0
        if abs(maxd - pred) > tol:
            bad['d'].append((W1, BC, BU, V, c, rr, (a, b), e, float(Q), maxd, pred))
    print('draws per case:', stats)
    for k, v in bad.items():
        print(f'case {k}: mismatches {len(v)}')
        for x in v[:4]:
            print('    ', x)

def b_boundary():
    """(b) and (c) at Q = V with China's cap binding: exit equilibria exist."""
    W1, BC, c, rr, a, b, e = 200, 100, 30, 0, 1, 1, 5
    Q = Q_of(W1, BC, c, rr, a, b); V = int(Q); BU = 100
    r1 = case_b(W1, BC, BU, V, c, rr, a, b, e)
    r2 = case_c(W1, BC, BU, V, c, rr, a, b, e)
    print('Q=V=', Q, ' (b) NE with exit exist:', any(x[2] for x in r1), ' (c) SPE with exit exist:', any(x[2] for x in r2))

if __name__ == '__main__':
    run()
    b_boundary()
