"""Remark (control under a general settlement). Preventive control (two periods) solved from primitives with
the bidding payment [q]^+ replaced by a settlement Phi (rupture bargaining P*), for finite enforceability
Delta_c. Brute force: Europe's accept/refuse and investment choices and Washington's minimal acceptable payment
are found by search, not by the Gamma formula. Checks: (1) issuance and Washington's gain match
Gamma = v_c - iota + min{dR_U, dR_U - dR_H + B_1 - sigma - r^c} with Phi in place of [.]^+ and
B_1 = u_1 + d_1 - [Phi(Q_1 + d_1) - Phi(Q_1)] when credible; (2) the text's example (premium negative at both
dates, yet Washington demands control): Gamma = 0.2, T* = 1.4.
Run: python3 -I v3_control_settlement.py
"""
import numpy as np


def mk_phi(V, beta, psi):
    return lambda q: max(q, psi * (q + beta * (V - q)))


def brute(Phi, Q1, Q2, dl, Dc, Ibar, K, u1, d1, g1, mU, sig, rc, vc, iota):
    def p2(q):
        inv = dl * (Phi(q + Ibar) - Phi(q)) > K
        rent = dl * Phi(q + (Ibar if inv else 0.0))
        return rent, rent - (K if inv else 0.0)
    r2, v2 = p2(Q2)
    U0 = -Phi(Q1) - r2
    e = g1 + Phi(Q1 + d1) - Phi(Q1)
    if e <= mU:
        Eref = -(u1 + d1) + Phi(Q1 + d1) + v2
    else:
        Eref = Phi(Q1) + v2
    r2c, v2c = p2(Q2 - Dc)
    lo, hi = 0.0, 100.0
    if 0 - sig - rc + Phi(Q1 - Dc) + v2c >= Eref:
        T = 0.0
    else:
        for _ in range(200):
            mid = (lo + hi) / 2
            if mid - sig - rc + Phi(Q1 - Dc) + v2c >= Eref:
                hi = mid
            else:
                lo = mid
        T = hi
    Uacc = vc - iota - T - Phi(Q1 - Dc) - r2c
    return Uacc - U0 > 1e-9, Uacc - U0, T


def formula(Phi, Q1, Q2, dl, Dc, Ibar, K, u1, d1, g1, mU, sig, rc, vc, iota):
    I = lambda q: dl * (Phi(q + Ibar) - Phi(q)) > K
    R = lambda q: dl * Phi(q + Ibar * I(q))
    Vh = lambda q: R(q) - K * I(q)
    dRU = Phi(Q1) - Phi(Q1 - Dc) + R(Q2) - R(Q2 - Dc)
    dRH = Phi(Q1) - Phi(Q1 - Dc) + Vh(Q2) - Vh(Q2 - Dc)
    e = g1 + Phi(Q1 + d1) - Phi(Q1)
    B1 = u1 + d1 - (Phi(Q1 + d1) - Phi(Q1)) if e <= mU else 0.0
    return vc - iota + min(dRU, dRU - dRH + B1 - sig - rc), max(dRH - B1 + sig + rc, 0.0)


def main():
    rng = np.random.default_rng(9)
    bad = 0
    for _ in range(5000):
        V = rng.uniform(3, 8); beta = rng.uniform(0, .9); psi = rng.uniform(0, .95)
        Phi = mk_phi(V, beta, psi)
        a = dict(Q1=rng.uniform(-3, 1.5), Q2=rng.uniform(-3, 2), dl=rng.uniform(.3, 1), Dc=rng.uniform(.1, 4),
                 Ibar=0.0 if rng.random() < .4 else rng.uniform(0, 2), K=rng.uniform(0, 2), u1=rng.uniform(0, 1),
                 d1=rng.uniform(0, 2.5), g1=rng.uniform(0, 1), mU=rng.uniform(0, 4), sig=rng.uniform(0, 2),
                 rc=rng.uniform(0, 1), vc=0.0 if rng.random() < .5 else rng.uniform(0, 2), iota=rng.uniform(0, .3))
        iss, gain, T = brute(Phi, **a)
        G, Tf = formula(Phi, **a)
        if abs(G) < 1e-6:
            continue
        if (G > 0) != iss or (iss and (abs(gain - G) > 1e-6 or abs(T - Tf) > 1e-6)):
            bad += 1
    print(f"(1) 5000 draws with Phi = P*: mismatches between brute force and the Gamma formula: {bad}")
    Phi = mk_phi(4.0, 0.5, 0.8)
    ex = dict(Q1=-1.0, Q2=-1.0, dl=1.0, Dc=2.0, Ibar=0.0, K=0.0, u1=0.0, d1=2.0, g1=0.0, mU=1.0, sig=1.0, rc=0.0,
              vc=0.0, iota=0.0)
    iss, gain, T = brute(Phi, **ex)
    print(f"(2) example: issued {iss}, Gamma = {gain:.4f}, T* = {T:.4f}; bidding benchmark would give "
          f"dR_U = {max(-1,0)-max(-3,0) + max(-1,0)-max(-3,0)} (no motive)")


if __name__ == "__main__":
    main()
