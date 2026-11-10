"""Proposition (bargaining with an outside option and rupture risk), v3: rupture is repaired at rate phi.
After a rejection without voluntary exit, rupture occurs with probability mu = 1 - exp(-lambda Delta);
the ruptured state pays flows (Q, -V) until a repair shock (rate phi), after which bargaining restarts
from the aligned status quo with no agreement. Voluntary exit is permanent.
Checks: (1) for finite Delta, backward induction on the extensive form (no formula used) gives Europe
x*(Delta) = max{x_A, x_B} with mu~ = mu(1-delta)/(1-delta(1-rho)), upsilon~ = mu delta rho/(1-delta(1-rho))
+ (1-mu) delta, x_A = mu~(Q + beta(V-Q))/(1-upsilon~), x_B = ((1-beta)Q + beta mu~ V)/(1-beta upsilon~),
and Washington -x*; (2) as Delta -> 0, x* -> P* = max{Q, lambda/(lambda+r+phi) (Q + beta(V-Q))};
(3) phi = 0 reproduces the v2 closed forms.
Run: python3 -I v3_temporary_rupture.py
"""
import math
import numpy as np


def backward_induction(Q, V, beta, lam, r, phi, dt, tol=1e-13):
    """Stationary SPE values by iterating the one-round game (Europe exits only after rejecting a US offer)."""
    mu = 1 - math.exp(-lam * dt)
    dl = math.exp(-r * dt)
    rho = 1 - math.exp(-phi * dt)
    vE, vU = 0.0, 0.0
    for _ in range(10**7):
        # ruptured-state values (normalized flows), restart continuation (vE, vU)
        RE = ((1 - dl) * Q + dl * rho * vE) / (1 - dl * (1 - rho))
        RU = ((1 - dl) * (-V) + dl * rho * vU) / (1 - dl * (1 - rho))
        cE = mu * RE + (1 - mu) * dl * vE      # Europe after a rejection, no exit
        cU = mu * RU + (1 - mu) * dl * vU
        # Washington proposes: Europe's best reply to an offer P is accept iff P >= max{Q, cE}
        rej_E = max(Q, cE)
        rej_U = -V if Q > cE else cU
        aE, aU = (rej_E, -rej_E) if -rej_E >= rej_U else (rej_E, rej_U)
        # Europe proposes: Washington accepts P iff -P >= cU
        P = -cU
        bE, bU = (P, -P) if P >= cE else (cE, cU)
        nE, nU = beta * bE + (1 - beta) * aE, beta * bU + (1 - beta) * aU
        if abs(nE - vE) + abs(nU - vU) < tol:
            return nE, nU
        vE, vU = nE, nU
    raise RuntimeError("no convergence")


def closed_form(Q, V, beta, lam, r, phi, dt):
    mu = 1 - math.exp(-lam * dt)
    dl = math.exp(-r * dt)
    rho = 1 - math.exp(-phi * dt)
    if phi == 0:
        mut, upt = mu, (1 - mu) * dl
    else:
        D = 1 - dl * (1 - rho)
        mut = mu * (1 - dl) / D
        upt = mu * dl * rho / D + (1 - mu) * dl
    xA = mut * (Q + beta * (V - Q)) / (1 - upt)
    xB = ((1 - beta) * Q + beta * mut * V) / (1 - beta * upt)
    return max(xA, xB)


def main():
    rng = np.random.default_rng(3)
    err_fin = 0.0
    n = 0
    for _ in range(3000):
        V = rng.uniform(0.3, 5)
        Q = rng.uniform(-6, V - 1e-3)
        beta = rng.uniform(0, 0.95)
        lam = 0.0 if rng.random() < 0.2 else rng.uniform(0, 3)
        r = rng.uniform(0.05, 2)
        phi = 0.0 if rng.random() < 0.2 else rng.uniform(0, 5)
        dt = rng.uniform(0.05, 1.0)
        vE, vU = backward_induction(Q, V, beta, lam, r, phi, dt)
        err_fin = max(err_fin, abs(vE - closed_form(Q, V, beta, lam, r, phi, dt)), abs(vE + vU))
        n += 1
    print(f"(1) finite Delta: {n} draws, max |BI - closed form| and |x_E + x_U| = {err_fin:.2e}")

    pts = [(rng.uniform(.5, 5), None, rng.uniform(0, .8), rng.uniform(.1, 3), rng.uniform(.2, 2), rng.uniform(0, 5))
           for _ in range(60)]
    pts = [(V, rng.uniform(-5, V - .05), b, l, r, p) for V, _, b, l, r, p in pts]
    for dt in (8e-3, 2e-3, 5e-4):
        e = 0.0
        for V, Q, b, l, r, p in pts:
            Pst = max(Q, l / (l + r + p) * (Q + b * (V - Q)))
            e = max(e, abs(closed_form(Q, V, b, l, r, p, dt) - Pst))
        print(f"(2) Delta = {dt:.0e}: max |x*(Delta) - P*| over 60 draws = {e:.2e}")

    e3 = 0.0
    for _ in range(500):
        V = rng.uniform(.3, 5); Q = rng.uniform(-5, V - .01); b = rng.uniform(0, .9)
        l = rng.uniform(0, 3); r = rng.uniform(.05, 2); dt = rng.uniform(.05, 1)
        mu = 1 - math.exp(-l * dt); ups = math.exp(-(r + l) * dt)
        v2 = max(mu / (1 - ups) * (Q + b * (V - Q)), ((1 - b) * Q + b * mu * V) / (1 - b * ups))
        e3 = max(e3, abs(v2 - closed_form(Q, V, b, l, r, 0.0, dt)))
    print(f"(3) phi = 0 against the v2 closed forms: max diff = {e3:.2e}")


if __name__ == "__main__":
    main()
