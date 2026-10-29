"""Remark (slack under rupture risk). With Europe's alignment payoff given by the frequent-offer
limit P*(Q) = max{Q, psi(Q + beta(V - Q))} of Proposition 1, withdrawing a threat set J with
Delta^A = u + d and Delta^X = u costs Europe B = u + d - [P*(Q + d) - P*(Q)].
Checks: (1) B <= u + min{d, Lambda_psi}, Lambda_psi = P*(Q) - Q >= Lambda = [-Q]^+;
(2) B = u + min{d, [-Q]^+} when lambda = 0; (3) an example where the bite exceeds Lambda.
Run: python3 -I v2_rupture_bite.py
"""
import numpy as np


def p_star(Q, V, beta, lam, r):
    psi = lam / (lam + r)
    return max(Q, psi * (Q + beta * (V - Q)))


def main():
    rng = np.random.default_rng(7)
    n = viol = 0
    gap0 = 0.0
    for _ in range(20000):
        V = rng.uniform(0.5, 5)
        Q = rng.uniform(-6, V - 0.05)
        beta = rng.uniform(0, 0.9)
        lam = 0.0 if rng.random() < 0.5 else rng.uniform(0, 3)
        r = rng.uniform(0.05, 2)
        u = rng.uniform(0, 2) * (rng.random() < 0.5)
        d = rng.uniform(0, 6)
        if Q + d >= V:
            continue
        n += 1
        p0, p1 = p_star(Q, V, beta, lam, r), p_star(Q + d, V, beta, lam, r)
        bite = u + d - (p1 - p0)
        if bite > u + min(d, p0 - Q) + 1e-12:
            viol += 1
        if lam == 0:
            gap0 = max(gap0, abs(bite - (u + min(d, max(-Q, 0.0)))))
    print(f"draws {n}; violations of B <= u + min(d, Lambda_psi): {viol}; "
          f"max |B - (u + min(d, Lambda))| at lambda = 0: {gap0:.2e}")
    Q, V, beta, lam, r, d = -1.0, 4.0, 0.5, 1.0, 0.25, 3.0
    p0, p1 = p_star(Q, V, beta, lam, r), p_star(Q + d, V, beta, lam, r)
    print(f"example: Lambda = {max(-Q, 0):.2f}, Lambda_psi = {p0 - Q:.2f}, bite of d = 3: {d - (p1 - p0):.2f}")


if __name__ == "__main__":
    main()
