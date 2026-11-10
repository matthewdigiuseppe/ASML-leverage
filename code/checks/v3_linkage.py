"""Proposition (linkage). Demand k costs Europe t_k, is worth w_k to Washington, and carries an issue-specific
penalty p_k in [0, inf] that Washington imposes if Europe reverses k, whatever Europe's alignment. Washington
links a set L of demands: reversing a linked concession while aligned gives Europe no more than exiting.
At the end of the period Europe chooses its alignment and the set D of concessions to reverse, by enumeration;
the settlement Phi (bidding, rupture bargaining or price driving) then pays a + Phi(x - a), where a and x are
Europe's best aligned and exit payoffs. Checks:
 (a) an aligned Europe delivers k iff k is linked or t_k <= p_k, and its loss equals
     sum_k min{t_k, p_k} + rho(sum_{k in L} [t_k - p_k]^+), rho(T) = T - [Phi(Q+T) - Phi(Q)];
 (b) with every t_k <= p_k, Washington's best single ultimatum pays no extra settlement and needs no linkage;
 (c) raising one p_k weakly raises Europe's loss and, when B(J^c) >= sum_k t_k, weakly raises Washington's
     optimal payoff; linking a demand with t_k <= p_k never changes anything.
Run: python3 -I v3_linkage.py
"""
import itertools
import numpy as np


def phis(rng):
    V = rng.uniform(2, 6); beta = rng.uniform(0, .9); psi = rng.uniform(0, .95); g = rng.uniform(0, 1.5)
    return [("bidding", lambda q: max(q, 0.0)),
            ("rupture", lambda q: max(q, psi * (q + beta * (V - q)))),
            ("price driving", lambda q: max(q + g, 0.0))]


def outcome(S, L, t, p, Q, Phi):
    """Enumerate Europe's end-of-period choice. Returns (loss, delivered set, extra settlement)."""
    S = list(S)
    best_a, best_D = -1e18, None
    unl = [k for k in S if k not in L]
    for r in range(len(unl) + 1):
        for D in itertools.combinations(unl, r):
            a = -sum(t[k] for k in S if k not in D) - sum(p[k] for k in D)
            if a > best_a + 1e-12:
                best_a, best_D = a, set(D)
    best_x = -1e18
    for r in range(len(S) + 1):
        for D in itertools.combinations(S, r):
            x = Q - sum(t[k] for k in S if k not in D) - sum(p[k] for k in D)
            best_x = max(best_x, x)
    E = best_a + Phi(best_x - best_a)
    delivered = set(S) - best_D
    return Phi(Q) - E, delivered, Phi(best_x - best_a) - Phi(Q)


def best_ultimatum(t, w, p, Q, Phi, B):
    n = len(t)
    best = (0.0, frozenset(), frozenset())
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            for rl in range(len(S) + 1):
                for L in itertools.combinations(S, rl):
                    loss, deliv, extra = outcome(S, set(L), t, p, Q, Phi)
                    if loss <= B + 1e-12:
                        val = sum(w[k] for k in deliv) - extra
                        if val > best[0] + 1e-12:
                            best = (val, frozenset(S), frozenset(L))
    return best


def main():
    rng = np.random.default_rng(5)
    va = vb = vc = vd = ve = 0
    n_b = n_c = 0
    for it in range(1500):
        n = 3
        Q = rng.uniform(-3, 1)
        t = list(rng.uniform(.1, 2, n))
        p = [float(x) if rng.random() < .8 else np.inf for x in rng.uniform(0, 2.5, n)]
        p = [0.0 if rng.random() < .2 else x for x in p]
        w = list(rng.uniform(.1, 2, n))
        for name, Phi in phis(rng):
            rho = lambda T: T - (Phi(Q + T) - Phi(Q))
            for r in range(1, n + 1):
                for S in itertools.combinations(range(n), r):
                    for rl in range(len(S) + 1):
                        for L in itertools.combinations(S, rl):
                            loss, deliv, extra = outcome(S, set(L), t, p, Q, Phi)
                            want = {k for k in S if k in L or t[k] <= p[k]}
                            f = sum(min(t[k], p[k]) for k in S) + rho(sum(max(t[k] - p[k], 0) for k in L))
                            if deliv != want or abs(loss - f) > 1e-9:
                                va += 1
                            # (c) Europe's loss nondecreasing in p_k
                            for k in S:
                                p2 = list(p); p2[k] = p[k] + 0.3
                                if outcome(S, set(L), t, p2, Q, Phi)[0] < loss - 1e-9:
                                    vd += 1
            B = rng.uniform(0, 1) * sum(t) if rng.random() < .5 else sum(t) + 1
            val, S, L = best_ultimatum(t, w, p, Q, Phi, B)
            if all(t[k] <= p[k] for k in range(n)):
                n_b += 1
                if any(max(t[k] - p[k], 0) > 0 for k in L):
                    vb += 1
                _, _, extra = outcome(S, set(L), t, p, Q, Phi)
                if extra > 1e-9:
                    vb += 1
            if B >= sum(t):
                n_c += 1
                k = int(rng.integers(n))
                p2 = list(p); p2[k] = p[k] + rng.uniform(0, 1)
                if best_ultimatum(t, w, p2, Q, Phi, B)[0] < val - 1e-9:
                    vc += 1
            # linking a demand with t <= p changes nothing
            for k in range(n):
                if t[k] <= p[k]:
                    S2 = tuple(range(n))
                    a = outcome(S2, set(), t, p, Q, Phi); b = outcome(S2, {k}, t, p, Q, Phi)
                    if abs(a[0] - b[0]) > 1e-9 or a[1] != b[1]:
                        ve += 1
    print(f"(a) delivered set and loss formula: violations {va}")
    print(f"(b) all t_k <= p_k ({n_b} draws): optimal ultimatum with linked excess or extra settlement: {vb}")
    print(f"(c) Europe's loss falling in p_k: {vd}; Washington's optimum falling in p_k when B >= sum t "
          f"({n_c} draws): {vc}; linking an enforced demand changing the outcome: {ve}")


if __name__ == "__main__":
    main()
