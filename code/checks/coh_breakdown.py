# Prop 5 (breakdown): brute force over the US payment T, sigma ~ U[0, sbar].
# E accepts iff sigma <= s = T + a - R (a = b1 - r^c). US gain vs no ultimatum: R - T if accept, -e if refuse.
# US issues only if its best expected gain is STRICTLY positive (no tie-break toward issuing).
import random
import numpy as np
pos = lambda x: max(0.0, x)

def brute(a, e, R, sbar, n=200001):
    T = np.linspace(0, R + sbar + abs(a) + 1, n)
    s = T + a - R
    F = np.clip(s / sbar, 0, 1)
    G = F * (R - T) + (1 - F) * (-e)
    i = int(np.argmax(G))
    issued = G[i] > 1e-9
    Pb = 1 - F[i]
    return issued, (Pb if issued else 0.0), Pb, T[i]

def formula(a, e, R, sbar):
    s = max(a - R, min(sbar, (a + e) / 2))
    return pos(1 - s / sbar)

random.seed(2)
bad = 0
for _ in range(2000):
    a, e, R, sbar = random.uniform(0.05, 6), random.uniform(0, 6), random.uniform(0.05, 6), random.uniform(0.2, 6)
    iss, Pu, Pc, T = brute(a, e, R, sbar, 40001)
    if abs(Pc - formula(a, e, R, sbar)) > 2e-3: bad += 1
print("conditional P_b formula mismatches (2000 draws):", bad)

print("\n=== 'P_b is increasing in R' in the corner a - R > min{sbar,(a+e)/2} ===")
for R in [1.0, 1.5]:
    a, e, sbar = 5.0, 0.0, 2.0
    iss, Pu, Pc, T = brute(a, e, R, sbar)
    print(f"a={a}, e={e}, sbar={sbar}, R={R}: corner holds={a - R > min(sbar, (a + e) / 2)}, issued={iss}, T*={T:.3f}, P_b={Pc:.3f}")

print("\n=== Unconditional breakdown probability (issue AND refuse) vs execution cost e ===")
a, R, sbar = 2.0, 3.0, 4.0
for e in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]:
    iss, Pu, Pc, T = brute(a, e, R, sbar)
    print(f"a={a}, R={R}, sbar={sbar}, e={e}: issued={iss}, P_b|issued={Pc:.3f}, unconditional={Pu:.3f}")

print("\n=== Unconditional breakdown vs r^c (a = b1 - r^c) ===")
b1, e, R, sbar = 3.0, 1.0, 3.0, 4.0
for rc in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]:
    a = b1 - rc
    iss, Pu, Pc, T = brute(a, e, R, sbar)
    print(f"b1={b1}, r^c={rc}, e={e}, R={R}, sbar={sbar}: issued={iss}, P_b|issued={Pc:.3f}, unconditional={Pu:.3f}")

print("\n=== 'uncertainty' vs level: sigma ~ U[lo, lo + w] with fixed mean, P_b as spread w rises ===")
def brute_lohi(a, e, R, lo, hi, n=200001):
    T = np.linspace(0, R + hi + abs(a) + 1, n)
    s = T + a - R
    F = np.clip((s - lo) / (hi - lo), 0, 1)
    G = F * (R - T) + (1 - F) * (-e)
    i = int(np.argmax(G)); return G[i] > 1e-9, 1 - F[i]
for w in [0.5, 1.0, 2.0, 3.0]:
    mean = 1.6
    iss, Pc = brute_lohi(3.0, 0.5, 3.0, mean - w / 2, mean + w / 2)
    print(f"mean sigma={mean}, spread={w}: issued={iss}, P_b|issued={Pc:.3f}")
