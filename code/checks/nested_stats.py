# Statistics on K(B)-K(0) and on whether optimal US payments must go outside every minimal blocking coalition.
import random, math, itertools
import numpy as np
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nested_check import make_game, blocking_family, K0, KB, subsets

def minimal_blocking(n, W):
    Bf = blocking_family(n, W)
    Bs = set(Bf)
    return [S for S in Bf if all((S - {i}) not in Bs for i in S)]

random.seed(3); np.random.seed(3)
stats = dict(games=0, exceed=0, below0=0, outside=0, exceed_qmv=0, qmv=0)
example = None; ex_out = None
for trial in range(1500):
    n = random.randint(3, 6)
    kind = random.choice(["qmv", "qmv", "weighted", "maj"])
    if kind == "maj":
        W = make_game(n, "maj", random.randint(n // 2 + 1, n))
    elif kind == "qmv":
        wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "qmv", (wt, random.choice([1, 2])))
    else:
        wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "weighted", (wt, random.uniform(0.5, 0.8)))
    if not W or frozenset() in W:
        continue
    q = [round(random.uniform(-1, 1.5), 2) for _ in range(n)]
    B = round(random.uniform(0.2, 2), 2)
    k0 = K0(n, W, q); kb, tau = KB(n, W, q, B)
    stats["games"] += 1
    if kind == "qmv": stats["qmv"] += 1
    if kb < k0 - 1e-9: stats["below0"] += 1
    if kb > k0 + B + 1e-9:
        stats["exceed"] += 1
        if kind == "qmv":
            stats["exceed_qmv"] += 1
            if example is None or n < example[0]:
                example = (n, kind, [round(x, 3) for x in wt], q, B, k0, kb, [round(t, 3) for t in tau])
    # is there an optimal solution supported inside some minimal blocking coalition?
    mins = minimal_blocking(n, W)
    best_in = min(KB(n, W, q, B, support=set(M))[0] for M in mins)
    if best_in > kb + 1e-7:
        stats["outside"] += 1
        if ex_out is None and kind == "qmv": ex_out = (n, [round(x, 3) for x in wt], q, B, kb, best_in)
print(stats)
print("smallest QMV-like example with K(B) > K(0) + B:", example)
print("QMV-like example needing payments outside every minimal blocking coalition:", ex_out)
