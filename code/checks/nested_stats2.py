# Breakdown: how often must optimal US payments go outside every minimal blocking coalition? (QMV-like games, n=3..6)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random, math
import numpy as np
from nested_check import make_game, blocking_family, K0, KB
def minimal_blocking(n, W):
    Bf = blocking_family(n, W); Bs = set(Bf)
    return [S for S in Bf if all((S - {i}) not in Bs for i in S)]
random.seed(4); np.random.seed(4)
for qmode in ("random q", "q = 0"):
    tot = out = exc = 0
    for trial in range(400):
        n = random.randint(3, 6)
        wt = np.random.dirichlet(np.ones(n)); W = make_game(n, "qmv", (wt, random.choice([1, 2])))
        if not W or frozenset() in W: continue
        q = [0.0] * n if qmode == "q = 0" else [round(random.uniform(-1, 1.5), 2) for _ in range(n)]
        B = 1.0
        k0 = K0(n, W, q); kb, tau = KB(n, W, q, B)
        tot += 1; exc += kb > k0 + B + 1e-9
        best_in = min(KB(n, W, q, B, support=set(M))[0] for M in minimal_blocking(n, W))
        out += best_in > kb + 1e-7
    print(f"{qmode}: {tot} QMV-like games; K(B)>K(0)+B in {exc}; payments outside every minimal blocking coalition required in {out}")
