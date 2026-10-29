# Proposition 7(a): discrete-time backward induction, random proposer (US w.p. psi), flow costs, no discounting.
# Normalized units: Europe share p in [0,1]; per-period costs cE*dt (t >= tauE), cU*dt (t >= tauU).
# w(t) = psi*max(w(t+dt) - cE(t)dt, 0) + (1-psi)*min(w(t+dt) + cU(t)dt, 1); terminal w(T) in {0, 1}.
import random, math
import numpy as np

def solve(psi, cE, cU, tauE, tauU, dt, T, wT):
    n = int(round(T / dt))
    w = wT
    for k in range(n - 1, -1, -1):
        t = k * dt
        ce = cE * dt if t >= tauE - 1e-12 else 0.0
        cu = cU * dt if t >= tauU - 1e-12 else 0.0
        w = psi * max(w - ce, 0.0) + (1 - psi) * min(w + cu, 1.0)
    return w

def formula(psi, cE, cU, tauE, tauU):
    D = tauU - tauE
    if psi * cE < (1 - psi) * cU:
        return 1.0 if D <= 0 else max(0.0, 1 - psi * cE * D)
    else:
        return 0.0 if D >= 0 else min(1.0, (1 - psi) * cU * (-D))

def horizon(psi, cE, cU, tauE, tauU):
    gap = abs((1 - psi) * cU - psi * cE)
    return max(tauE, tauU) + 1.0 / gap + 1.0

random.seed(5)
for dt in (0.01, 0.002):
    worst = 0; worst_par = None; n = 0; big = 0
    for trial in range(400 if dt == 0.01 else 150):
        psi = random.choice([0.0, 1.0, random.random(), random.random(), random.random()])
        cE = random.choice([0.0, random.uniform(0, 3)]); cU = random.choice([0.0, random.uniform(0, 3)])
        if abs(psi * cE - (1 - psi) * cU) < 0.02:   # tie excluded by the proposition; keep near-ties
            continue
        tauE = random.choice([0.0, random.uniform(0, 3)])
        tauU = random.choice([tauE, random.uniform(0, 3)])
        T = horizon(psi, cE, cU, tauE, tauU)
        if T > 80:
            continue
        f = formula(psi, cE, cU, tauE, tauU)
        w0 = solve(psi, cE, cU, tauE, tauU, dt, T, 0.0)
        w1 = solve(psi, cE, cU, tauE, tauU, dt, T, 1.0)
        err = max(abs(w0 - f), abs(w1 - f))
        n += 1
        # O(dt) bound: one step of each cost plus the stationary offset psi*cE*dt/(1-psi) or (1-psi)*cU*dt/psi
        bound = 5 * dt * (cE + cU) / max(min(psi, 1 - psi), 0.05) + 1e-9
        if err > bound:
            big += 1
        if err > worst:
            worst, worst_par = err, (round(psi, 3), round(cE, 3), round(cU, 3), round(tauE, 3), round(tauU, 3), round(w0, 4), round(w1, 4), round(f, 4))
    print(f"dt={dt}: {n} draws, max |error| = {worst:.4f} at {worst_par}; draws exceeding O(dt) bound: {big}")

# Error scaling at a fixed interior point
for dt in (0.02, 0.01, 0.005, 0.0025):
    p = (0.4, 1.0, 1.5, 0.5, 1.2)
    f = formula(*p)
    T = horizon(*p)
    print("dt", dt, "error", round(max(abs(solve(*p, dt, T, 0.0) - f), abs(solve(*p, dt, T, 1.0) - f)), 5))

# Tie case psi*cE == (1-psi)*cU (excluded): show dependence on terminal condition / horizon
p = (0.5, 1.0, 1.0, 0.0, 0.5)
for T in (5, 10, 20):
    print("tie case, T =", T, "w0 =", round(solve(*p, 0.01, T, 0.0), 4), "w1 =", round(solve(*p, 0.01, T, 1.0), 4))
