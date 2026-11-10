"""Remark (a source of assurance cost). Washington chooses the conditionality kappa of Europe's guarantee.
A second ally's premium rises with kappa, Q_2(kappa) = Q_2^0 + a (kappa - kappa_0) with Q_2^0 <= 0, and
Washington converts that ally's slack at the same rate nu. Then H(kappa) = Pi_2(kappa_0) - Pi_2(kappa),
Pi_2 = -[Q_2]^+ + nu [-Q_2]^+. Checks by grid search over kappa (no formula used in the search):
(1) H is nondecreasing and convex with H(kappa_0) = 0; (2) with Q_0 < 0 the optimal kappa is kappa_0 if
a >= S_k (or nu = 0), the point where the second ally's premium reaches zero, min{kappa_tilde, kappa_bar},
if nu S_k <= a < S_k, and kappa_bar if a < nu S_k.
Run: python3 -I v3_assurance.py
"""
import numpy as np


def main():
    rng = np.random.default_rng(4)
    bad1 = bad2 = 0
    for _ in range(3000):
        k0 = 0.0; kbar = rng.uniform(.2, 1.0); Sk = rng.uniform(.5, 4); nu = 0.0 if rng.random() < .15 else rng.uniform(0, 1)
        Q0 = rng.uniform(-3, -0.01); Q20 = rng.uniform(-2, 0); a = rng.uniform(0, 6)
        grid = np.linspace(k0, kbar, 20001)
        Q2 = Q20 + a * (grid - k0)
        Pi2 = -np.maximum(Q2, 0) + nu * np.maximum(-Q2, 0)
        H = Pi2[0] - Pi2
        dH = np.diff(H)
        if H[0] != 0 or (dH < -1e-12).any() or (np.diff(dH) < -1e-9).any():
            bad1 += 1
        Q = Q0 - (grid - k0) * Sk
        Pi = -np.maximum(Q, 0) + nu * np.maximum(-Q, 0) - H
        mx = Pi.max()
        cands = grid[Pi >= mx - 1e-9]
        kt = k0 - Q20 / a if a > 0 else np.inf
        if nu == 0 or a >= Sk:
            pred = k0
        elif a >= nu * Sk:
            pred = min(kt, kbar)
        else:
            pred = kbar
        # the predicted point must be among the maximizers (ties allowed when slopes coincide)
        if not np.any(np.abs(cands - pred) < 2 * (kbar - k0) / 20000):
            bad2 += 1
    print(f"(1) H nondecreasing, convex, H(kappa_0) = 0: violations {bad1}")
    print(f"(2) optimal conditionality against the closed form: violations {bad2} of 3000")


if __name__ == "__main__":
    main()
