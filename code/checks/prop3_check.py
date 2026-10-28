"""Proposition 3 (determinants) and Corollary 1: brute-force spot checks using the
grid SPE of the static game (same solver as prop1_check.py, copied because -I mode)."""
import random
import numpy as np
from fractions import Fraction as F

def spe(W1, BC, BU, V, c, rr, a, b, e):
    tU = np.arange(0, BU + 1, e)
    tC = np.arange(0, BC + 1, e)
    exit_ = b * (tU[:, None] - rr + c) < a * tC[None, :]
    pay_C = np.where(exit_, W1 - tC[None, :], 0)
    mx = pay_C.max(axis=1)
    out_exit = np.array([exit_[i, 0] if mx[i] <= 0 else True for i in range(len(tU))])
    pay_U = np.where(out_exit, -V, -tU)
    idx = np.where(pay_U == pay_U.max())[0]
    return [(int(tU[i]), bool(out_exit[i])) for i in idx]

def primitives_to_c(kS, alpha, chi_ai, f, chi_f, eta):
    return kS + alpha * chi_ai + f * chi_f + eta

rng = random.Random(7)
e = 1

# (a) monotonicity in pi_A holding pi_X fixed (S scaled so kappa*S integer)
viol_a = 0
for _ in range(300):
    S = rng.randint(1, 40); piX = rng.randint(0, 10)
    W1 = rng.randint(0, 200); BC = rng.randint(0, 200); a, b = rng.choice([(1, 1), (1, 2), (2, 3)])
    rest = rng.randint(0, 60); rr = rng.randint(0, 60)
    V = 400; BU = 400
    prevL = None
    for piA in range(piX, 11):
        c = S * (piA - piX) // 1 + rest            # kappa*S with pi in tenths -> scale S
        out = spe(W1, BC, BU, V, c, rr, a, b, e)
        L = max(tu for tu, ex in out if not ex) if all(not ex for _, ex in out) else None
        if L is None:
            continue
        if prevL is not None and L > prevL + e:
            viol_a += 1
        prevL = L
print('(a) violations of "L nonincreasing in pi_A":', viol_a)

# (b) counterexample: leverage NOT non-monotone in nu when Q without the AI lever is <= 0
kX, kA, m_ai, alpha = 5, 10, 0, 30
W1, BC, a, b, rr = 50, 50, 1, 1, 0
base_c = 70                                       # Q without AI lever = 50 - 70 = -20
Ls = []
for nu in range(0, 15):
    chi_ai = int(nu + m_ai >= kX) * int(nu < kA)
    c = base_c + alpha * chi_ai
    out = spe(W1, BC, 400, 400, c, rr, a, b, e)
    Ls.append(out[0][0] if len(out) == 1 and not out[0][1] else out)
print('(b) L as nu runs 0..14 with Q(no AI lever) = -20, alpha=30:', Ls)
# and with m_ai >= k_X (lever conditional already at nu=0): Q monotone in nu
m_ai = 6; base_c = 20                             # Q(no lever)=30 > 0
Ls = []
for nu in range(0, 15):
    chi_ai = int(nu + m_ai >= kX) * int(nu < kA)
    out = spe(W1, BC, 400, 400, base_c + alpha * chi_ai, rr, a, b, e)
    Ls.append(out[0][0])
print('(b) L as nu runs 0..14 with m_ai=6 >= k_X=5, Q(no lever)=30:', Ls)

# (c) nondecreasing in V (via chi_f), maintaining Q <= min{V, B_U}
viol_c = 0
for _ in range(300):
    gamma, m_f, f = rng.randint(0, 20), rng.randint(0, 10), rng.randint(0, 40)
    phi_num = rng.randint(1, 5)                    # phi = phi_num/10
    W1 = rng.randint(0, 150); BC = rng.randint(0, 150); rr = rng.randint(0, 40); base = rng.randint(0, 60)
    prevL = None
    for V in range(150, 400, 5):
        chi_f = int(phi_num * V <= 10 * (gamma + m_f))
        c = base + f * chi_f
        out = spe(W1, BC, 400, V, c, rr, 1, 1, e)
        if any(ex for _, ex in out):
            continue
        L = out[0][0]
        if prevL is not None and L < prevL:
            viol_c += 1
        prevL = L
print('(c) violations of "L nondecreasing in V":', viol_c)

# (d) Europe payoff = max{omega - c, -chi_r r}
viol_d = 0
for _ in range(500):
    W1 = rng.randint(0, 150); BC = rng.randint(0, 150); a, b = rng.choice([(1, 1), (1, 2), (3, 4)])
    c = rng.randint(0, 100); rr = rng.randint(0, 100)
    out = spe(W1, BC, 600, 600, c, rr, a, b, e)
    omega = F(a, b) * min(W1, BC)
    pred = max(omega - c, F(-rr))
    for tu, ex in out:
        if ex or abs((tu - rr) - pred) > 1:
            viol_d += 1
            break
print('(d) violations of Europe payoff formula (tolerance one grid step):', viol_d)

# (e) counterexample: B_U < Q <= V but V < (1-theta)W
W1, BC, a, b, c, rr = 10_000, 10_000, 1, 2, 0, 0   # lambda=1/2, units 1/1000
Q = F(a, b) * min(W1, BC) - c + rr                 # 5000
V, BU = 6000, 4000
out = spe(W1, BC, BU, V, c, rr, a, b, 100)
print('(e) Q =', Q, 'V =', V, 'B_U =', BU, '(1-theta)W =', W1, '-> all SPE exit:', all(ex for _, ex in out))
print('    US value of A (V) =', V, '< China value of exit (1-theta)W =', W1)
# welfare in the SPE where US offers 0: China bids one grid step
tauC = 100
print('    3-player welfare X minus A at tau_U=0 SPE:', (-V) + (W1 - tauC) + F(a, b) * tauC - (-rr), '(>0: exit efficient)')
