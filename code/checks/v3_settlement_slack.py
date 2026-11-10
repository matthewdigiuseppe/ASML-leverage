"""Proposition (slack principle), v3: any settlement Phi with Phi(q) >= q, Phi nondecreasing, slope <= 1.
Europe's net loss with conceded set S and withdrawn set J_w is
  L = T_s + Delta^A(J_w) + T_r - [Phi(Q + d(J_w) + T_r) - Phi(Q)],  Washington pays Phi(.) as settlement.
Brute force: subgame-perfect play of adaptive ultimatums (3 demands, 2 non-additive instruments),
solved from the game tree with no use of the bounds. Checks, for four settlements (bidding [q]^+,
rupture bargaining P*, hold-up with constant costs, price driving [q + g]^+):
 (a) bite B(J) = L(empty, J) <= u + min{d, Lambda_Phi}, with equality when Phi(Q+d) = Q+d or = Phi(Q),
     and B = u + min{d, [-Q]^+} for bidding;
 (b) loss from reversible T equals rho(T) <= min{T, Lambda_Phi};
 (c)(i) equilibrium loss <= B(J^c); (c)(ii) Washington's payoff <= V_1;
 (d) Washington obtains V_1 when all demands are reversible and B(J^c) >= Lambda_Phi (positive execution costs).
Run: python3 -I v3_settlement_slack.py
"""
import itertools
from functools import lru_cache
import numpy as np


def make_phi(kind, rng):
    if kind == "bidding":
        return lambda q: max(q, 0.0), "bidding"
    V = rng.uniform(2, 6); beta = rng.uniform(0, .9); lam = rng.uniform(0, 3); r = rng.uniform(.1, 2)
    phi_rep = rng.uniform(0, 3)
    psi = lam / (lam + r + phi_rep)
    if kind == "rupture":
        return lambda q: max(q, psi * (q + beta * (V - q))), "rupture"
    if kind == "holdup":
        N = beta * rng.uniform(0, 2) - (1 - beta) * rng.uniform(0, 2)
        return lambda q: max(q, psi * (q + beta * (V - q)) + (1 - psi) * N), "holdup"
    g = rng.uniform(0, 2)
    return lambda q: max(q + g, 0.0), "price driving"


def subsets(s):
    s = list(s)
    for k in range(1, len(s) + 1):
        for c in itertools.combinations(s, k):
            yield frozenset(c)


def solve(Q, dem, DA, DX, e, Phi, ni):
    nd = len(dem)

    def term(S, Jw):
        Tr = sum(dem[k][0] for k in S if dem[k][2]); Ts = sum(dem[k][0] for k in S if not dem[k][2])
        d = DA[Jw] - DX[Jw]
        E = -DA[Jw] - Tr - Ts + Phi(Q + d + Tr)
        U = sum(dem[k][1] for k in S) - Phi(Q + d + Tr) - e[Jw]
        return E, U

    @lru_cache(None)
    def val(S, Jw):
        best = term(S, Jw)
        rem = [k for k in range(nd) if k not in S]; ins = [j for j in range(ni) if j not in Jw]
        if rem and ins:
            for D in subsets(rem):
                for J in subsets(ins):
                    a = val(S | D, Jw); b = val(S, Jw | J)
                    out = a if a[0] >= b[0] - 1e-12 else b
                    if out[1] > best[1] + 1e-12:
                        best = out
        return best
    return val(frozenset(), frozenset())


def main():
    rng = np.random.default_rng(11)
    f = frozenset
    stats = {}
    for it in range(4000):
        kind = ["bidding", "rupture", "holdup", "price driving"][it % 4]
        Phi, name = make_phi(kind, rng)
        Q = rng.uniform(-3, 1.5)
        allrev = rng.random() < 0.3
        dem = [(rng.uniform(.1, 2), rng.uniform(.1, 2), True if allrev else bool(rng.integers(2))) for _ in range(3)]
        x1, x2 = rng.uniform(0, 1.5, 2); x12 = max(x1, x2) + rng.uniform(0, 1.5)
        a1 = x1 + rng.uniform(0, 2); a2 = x2 + rng.uniform(0, 2); a12 = max(a1, a2, x12) + rng.uniform(0, 2)
        DX = {f(): 0, f([0]): x1, f([1]): x2, f([0, 1]): x12}
        DA = {f(): 0, f([0]): a1, f([1]): a2, f([0, 1]): a12}
        e1, e2 = rng.uniform(.01, .5, 2); e = {f(): 0, f([0]): e1, f([1]): e2, f([0, 1]): e1 + e2}
        Lam = Phi(Q) - Q
        st = stats.setdefault(name, [0, 0, 0, 0, 0, 0, 0])
        st[0] += 1
        # (a) bite of every J
        for J in [f([0]), f([1]), f([0, 1])]:
            u = DX[J]; d = DA[J] - DX[J]
            B = DA[J] - (Phi(Q + d) - Phi(Q))
            if B > u + min(d, Lam) + 1e-9:
                st[1] += 1
            eq = abs(Phi(Q + d) - (Q + d)) < 1e-12 or abs(Phi(Q + d) - Phi(Q)) < 1e-12
            if eq and abs(B - (u + min(d, Lam))) > 1e-9:
                st[1] += 1
            if name == "bidding" and abs(B - (u + min(d, max(-Q, 0)))) > 1e-9:
                st[1] += 1
        # (b)
        for T in rng.uniform(0, 4, 5):
            if T - (Phi(Q + T) - Phi(Q)) > min(T, Lam) + 1e-9:
                st[2] += 1
        # (c), (d)
        E, U = solve(Q, dem, DA, DX, e, Phi, 2)
        loss = Phi(Q) - E
        Jc = f([0, 1]); dc = DA[Jc] - DX[Jc]
        BJc = DA[Jc] - (Phi(Q + dc) - Phi(Q))
        if loss > BJc + 1e-9:
            st[3] += 1
        V1 = -1e18
        for S in [f()] + list(subsets(range(3))):
            Tr = sum(dem[k][0] for k in S if dem[k][2]); Ts = sum(dem[k][0] for k in S if not dem[k][2])
            if Tr - (Phi(Q + Tr) - Phi(Q)) + Ts <= BJc + 1e-12:
                V1 = max(V1, sum(dem[k][1] for k in S) - Phi(Q + Tr))
        if U > V1 + 1e-9:
            st[4] += 1
        if allrev and BJc >= Lam - 1e-12:
            st[5] += 1
            if abs(U - V1) > 1e-9:
                st[6] += 1
    for name, s in stats.items():
        print(f"{name:14s}: {s[0]} draws; violations (a) {s[1]}, (b) {s[2]}, (c)(i) {s[3]}, (c)(ii) {s[4]}; "
              f"(d) applicable {s[5]}, failures {s[6]}")


if __name__ == "__main__":
    main()
