# Misc. checks: Lemma 3 (period-2 bite), Lemma 2 tie, Prop 6(b) slope, Prop 7 condition, Remark 1.
pos = lambda x: max(0.0, x)

print("=== Lemma 3: extra loss to Europe from extending the cut into period 2 ===")
for Q2, a2 in [(0.5, 2.0), (0.0, 1.0), (3.0, 1.0), (-0.5, 2.0), (-3.0, 1.0)]:
    extra_bite = a2 - (pos(Q2 + a2) - pos(Q2))
    extra_rent = pos(Q2 + a2) - pos(Q2)
    print(f"Q2={Q2}, alpha2={a2}: extra loss to Europe = {extra_bite:.2f}, extra rent paid by US = {extra_rent:.2f}")

print("\n=== Lemma 2 at the tie m + g_N = [Q1+a1]^+ - [Q1]^+ ===")
Q1, a1, gN, m = -2.0, 1.5, -0.3, 0.3
cut = gN - pos(Q1 + a1); nocut = -m - pos(Q1)
print(f"U payoff cut={cut:.2f}, no cut={nocut:.2f}: indifferent -> SPE with and without the cut both exist")

print("\n=== Prop 6(b): marginal cost of a unit of US buffer to Europe (in utility) ===")
def share(psi, cE, ell, sE, cU, sU, tauU, dt=1e-3, tail=20.0):
    # discrete-time recursion of the proof, tau_E = 0, interruption: E bears cE+ell from 0, U bears cU after tauU
    n = int((tauU + tail) / dt); w = 0.5
    for k in range(n - 1, -1, -1):
        t = k * dt
        hE = (cE + ell) / sE * dt; hU = (cU / sU * dt) if t >= tauU else 0.0
        w = psi * max(w - hE, 0.0) + (1 - psi) * min(1.0, w + hU)
    return w
psi, cE, ell, sE, cU, sU = 0.5, 0.2, 0.3, 4.0, 2.0, 1.0
w1, w2 = share(psi, cE, ell, sE, cU, sU, 1.0), share(psi, cE, ell, sE, cU, sU, 2.0)
print(f"share at tau_U=1: {w1:.4f}, at 2: {w2:.4f}; Europe's utility loss per unit buffer = {(w1 - w2) * sE:.4f}")
print(f"   psi*c_E = {psi * cE:.4f}   vs   psi*(c_E+ell) = {psi * (cE + ell):.4f}")

print("\n=== Prop 7: 'If Q + D_k > 0 and audience costs are small, the US cannot use linkage' ===")
Q, Dk, mk, gkH = 0.5, 1.0, 0.0, 2.0
print(f"Q={Q}, D_k={Dk}, m_k={mk} (zero audience cost), g_k(H)={gkH}: credible = {mk + gkH >= pos(Q + Dk) - pos(Q)}")

print("\n=== Remark 1 brute force ===")
import random
random.seed(4); bad = 0
for _ in range(100000):
    dQ2 = random.uniform(0.01, 5); b1 = random.uniform(0, 5); c0 = random.uniform(0, b1)  # (iii): b1 > c0
    cb = random.uniform(0, 5)   # sigma_c + r^b
    nobind = max(dQ2 - b1, -c0); bind = -cb
    pred = cb < c0 and cb < b1 - dQ2
    if (bind > nobind + 1e-12) != pred: bad += 1
print("Remark 1 mismatches:", bad)
