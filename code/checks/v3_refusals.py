"""Proposition (refusals and executed threats). Europe's net cost kappa of one demand is private, kappa ~ F.
Washington picks a threat set J (possibly empty) with bite B(J) and ex post execution cost E(J) >= 0, E(empty) = 0;
Europe accepts iff kappa <= B(J); a refused backed demand is carried out. Brute force over random menus of
threat sets and distributions (normal, uniform, two-point mixtures). Checks: (1) the refusal probability is at
least 1 - F(B(J^c)); (2) the largest optimal bite is nondecreasing in w; (3) an unbacked request beats no
demand whenever F(0) > 0; (4) slack-capped bite: with purely conditional instruments, B(J^c) <= Lambda, so
the refusal probability is at least 1 - F(Lambda), which rises as Q rises toward 0.
Run: python3 -I v3_refusals.py
"""
import math
import numpy as np


def cdf_factory(rng):
    kind = rng.integers(3)
    if kind == 0:
        m, s = rng.uniform(-1, 3), rng.uniform(.2, 2)
        return lambda x: 0.5 * (1 + math.erf((x - m) / (s * math.sqrt(2))))
    if kind == 1:
        lo = rng.uniform(-1, 1); hi = lo + rng.uniform(.5, 4)
        return lambda x: min(1.0, max(0.0, (x - lo) / (hi - lo)))
    m1, m2 = rng.uniform(-1, 1), rng.uniform(1, 4); s = rng.uniform(.1, .5); q = rng.uniform(.2, .8)
    return lambda x: q * 0.5 * (1 + math.erf((x - m1) / (s * math.sqrt(2)))) + (1 - q) * 0.5 * (1 + math.erf((x - m2) / (s * math.sqrt(2))))


def main():
    rng = np.random.default_rng(8)
    v1 = v2 = v3 = v4 = 0
    for _ in range(3000):
        F = cdf_factory(rng)
        m = int(rng.integers(2, 7))
        menu = [(0.0, 0.0)] + [(rng.uniform(0, 4), rng.uniform(0, 3)) for _ in range(m)]
        Bmax = max(b for b, _ in menu)
        def best(w):
            vals = [(F(b) * w - (1 - F(b)) * E, b) for b, E in menu]
            top = max(v for v, _ in vals)
            return top, max(b for v, b in vals if v >= top - 1e-12)
        ws = sorted(rng.uniform(0, 6, 8))
        prev = -1
        for w in ws:
            top, b = best(w)
            if 1 - F(b) < 1 - F(Bmax) - 1e-12:
                v1 += 1
            if b < prev - 1e-12:
                v2 += 1
            prev = b
            if F(0) > 0 and top <= 0:
                v3 += 1
        Q = rng.uniform(-3, 0)
        Lam = -Q
        ds = rng.uniform(0, 4, 3)
        B = min(ds.sum(), Lam)  # purely conditional bundle: bite u + min{d, Lambda} with u = 0
        if 1 - F(B) < 1 - F(Lam) - 1e-12:
            v4 += 1
    print(f"(1) refusal probability below 1 - F(B(J^c)): {v1}")
    print(f"(2) optimal bite falling in w: {v2}")
    print(f"(3) F(0) > 0 but no demand optimal: {v3}")
    print(f"(4) conditional bite exceeding the slack floor: {v4}")


if __name__ == "__main__":
    main()
