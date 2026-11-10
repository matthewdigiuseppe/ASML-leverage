"""Proposition (hold-up: the range of equilibria). Constant baseline disagreement costs, no buffer (t_U = 0).
Variant (b): Europe chooses whether to interrupt after a rejection. Two-state profile: H (Europe interrupts
after Washington rejects a demand, otherwise as in the Markov game with Washington's cost raised by (1-h)c_S
in Europe's proposing rounds) and L (the Markov equilibrium, no interruption); a failure to interrupt in H
moves play to L. Checks for small Delta: (1) every one-shot deviation from H and L is unprofitable;
(2) x_L and x_H converge to max{Q, x0} and max{Q, x0 + (1 - psi) beta (1-h) c_S}, x0 = psi M + (1-psi)
(beta c_U0 - (1-beta) c_E0); (3) main timing (choice before the proposer is drawn): value iteration on the
operator with a maximum over the interruption choice gives max{Q, x0, x0 + (1-psi)D}, D = beta(1-h)c_S -
(1-beta) ell, the single value that the proposition says every SPE attains.
Run: python3 -I v3_holdup_range.py
"""
import math
import numpy as np


def params(dt, lam, r):
    mu = 1 - math.exp(-lam * dt); dl = math.exp(-r * dt)
    return mu, dl


def fixed_point(f, x0=0.0):
    x = x0
    for _ in range(10**7):
        y = f(x)
        if abs(y - x) < 1e-13:
            return y
        x = y
    raise RuntimeError


def main():
    rng = np.random.default_rng(21)
    worst_ic = float("inf")
    lim_err = [0.0, 0.0, 0.0]
    n = 0
    for _ in range(400):
        V = rng.uniform(1, 5); Q = rng.uniform(-4, V - .1); beta = rng.uniform(.05, .9)
        lam = rng.uniform(0, 2); r = rng.uniform(.2, 2)
        cE0, cU0 = rng.uniform(0, 1, 2); ell = rng.uniform(0, 2); cS = rng.uniform(0, 3); h = rng.uniform(0, 1)
        cI = (1 - h) * cS
        dt = 1e-3
        mu, dl = params(dt, lam, r)
        psi = lam / (lam + r)
        M = Q + beta * (V - Q)

        def T(x, cU):
            rejE = max(Q, mu * Q + (1 - mu) * (-(1 - dl) * cE0 + dl * x))
            dem = mu * V + (1 - mu) * ((1 - dl) * cU + dl * x)
            return beta * dem + (1 - beta) * rejE
        # exact fixed points of the two piecewise-affine contractions (largest branch, as in Step 2 of the
        # proof of the bargaining proposition); checked against iteration in a subsample below
        def fp(cU):
            a = (beta * mu * V + (1 - beta) * mu * Q + (1 - mu) * (1 - dl) * (beta * cU - (1 - beta) * cE0)) / (1 - (1 - mu) * dl)
            b = (beta * (mu * V + (1 - mu) * (1 - dl) * cU) + (1 - beta) * Q) / (1 - beta * (1 - mu) * dl)
            return max(a, b)
        xL = fp(cU0); xH = fp(cU0 + cI)
        if _ < 5:
            assert abs(xL - fixed_point(lambda x: T(x, cU0))) < 1e-8 and abs(xH - fixed_point(lambda x: T(x, cU0 + cI))) < 1e-8
        # one-shot deviations
        # (i) in H, interrupting after Washington rejects a demand
        ic1 = (mu * Q + (1 - mu) * (-(1 - dl) * (cE0 + ell) + dl * xH)) - (mu * Q + (1 - mu) * (-(1 - dl) * cE0 + dl * xL))
        # (ii) Washington's rejection of Europe's demand in H yields exactly -P_E (indifferent): accept is a best reply
        PE = mu * V + (1 - mu) * ((1 - dl) * (cU0 + cI) + dl * xH)
        # (iii) Europe demanding more than P_E: rejected, Europe interrupts
        ic3 = PE - (mu * Q + (1 - mu) * (-(1 - dl) * (cE0 + ell) + dl * xH))
        # (iv) Washington offering less than O_H: rejected
        cE = mu * Q + (1 - mu) * (-(1 - dl) * cE0 + dl * xH)
        OH = max(Q, cE)
        wrej = -V if Q > cE else -mu * V + (1 - mu) * (-(1 - dl) * cU0 - dl * xH)
        ic4 = -OH - wrej
        # (v) in L, interrupting after any rejection only costs Europe
        ic5 = (1 - mu) * (1 - dl) * ell
        x0_ = psi * M + (1 - psi) * (beta * cU0 - (1 - beta) * cE0)
        gap_lim = max(Q, x0_ + (1 - psi) * beta * cI) - max(Q, x0_)
        if gap_lim > 1e-2:   # H differs from L in the limit
            n += 1
            worst_ic = min(worst_ic, ic1, ic3, ic4, ic5)
        x0 = psi * M + (1 - psi) * (beta * cU0 - (1 - beta) * cE0)
        lim_err[0] = max(lim_err[0], abs(xL - max(Q, x0)))
        lim_err[1] = max(lim_err[1], abs(xH - max(Q, x0 + (1 - psi) * beta * cI)))
        # main timing
        def Tm(x):
            best = -1e18
            for i in (0, 1):
                rejE = max(Q, mu * Q + (1 - mu) * (-(1 - dl) * (cE0 + i * ell) + dl * x))
                dem = mu * V + (1 - mu) * ((1 - dl) * (cU0 + i * cI) + dl * x)
                best = max(best, beta * dem + (1 - beta) * rejE)
            return best
        xm = fixed_point(Tm, x0=max(Q, x0))
        D = beta * cI - (1 - beta) * ell
        lim_err[2] = max(lim_err[2], abs(xm - max(Q, x0, x0 + (1 - psi) * D)))
    print(f"(1) {n} draws with x_H above x_L in the limit, Delta = 1e-3: smallest one-shot-deviation margin "
          f"{worst_ic:.2e} (nonnegative = no profitable deviation)")
    print(f"(2) |x_L - limit| <= {lim_err[0]:.2e}, |x_H - limit| <= {lim_err[1]:.2e}")
    print(f"(3) main timing: |value - max{{Q, x0, x0 + (1-psi)D}}| <= {lim_err[2]:.2e}")


if __name__ == "__main__":
    main()
