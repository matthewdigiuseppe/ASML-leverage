"""Check corrected Prop 4: public ultimatum with audience cost m, U's ex post gain from cutting an
aligned E that retains control g_N <= 0, and from cutting after control transfer g_C < 0.
Backward induction with ties: U cuts iff strictly better (no tie-break toward the threat),
E accepts when indifferent, U demands only if strictly better."""
import random
pos = lambda x: max(0.0, x)

def solve(Q1, a1, Q2, d, sig, rc, m, gN, gC):
    # no demand branch: U may cut (no audience cost)
    cutU = -pos(Q1 + a1) + gN - d * pos(Q2); nocutU = -pos(Q1) - d * pos(Q2)
    if cutU > nocutU + 1e-12:
        ndE, ndU = -a1 + pos(Q1 + a1) + d * pos(Q2), cutU
    else:
        ndE, ndU = pos(Q1) + d * pos(Q2), nocutU
    # refusal of public ultimatum: not cutting costs m
    cutU = -pos(Q1 + a1) + gN - d * pos(Q2); nocutU = -pos(Q1) - d * pos(Q2) - m
    if cutU > nocutU + 1e-12:
        rE, rU = -a1 + pos(Q1 + a1) + d * pos(Q2), cutU
    else:
        rE, rU = pos(Q1) + d * pos(Q2), nocutU
    # acceptance: U controls ASML; U cuts iff gC > 0
    accCut = gC > 1e-12
    accE_noT = -sig - rc - (a1 if accCut else 0.0)
    accU_noT = (gC if accCut else 0.0)
    T = pos(rE - accE_noT)
    demand = accU_noT - T > ndU + 1e-12
    return demand, (T if demand else None)

def formula(Q1, a1, Q2, d, sig, rc, m, gN, gC):
    # valid for gN <= 0, gC <= 0
    drent = pos(Q1 + a1) - pos(Q1)
    credible = m + gN > drent + 1e-12 or (drent == 0 and m + gN > 1e-12)
    credible = (m + gN - drent) > 1e-12
    bite = min(a1, pos(-Q1))
    demand = Q2 > 1e-12 and credible and bite > sig + rc + 1e-12
    T = pos(d * Q2 + sig + rc - bite) if demand else None
    return demand, T

random.seed(7); mism = 0; n = 200000; ndem = 0
for _ in range(n):
    Q1, Q2 = random.uniform(-4, 2), random.uniform(-2, 4)
    a1 = random.uniform(0, 4); d = random.uniform(0.5, 1)
    sig, rc = random.uniform(0, 1.5), random.uniform(0, 1)
    m = random.choice([0.0, random.uniform(0, 4)]); gN = random.choice([0.0, -random.uniform(0, 1)])
    gC = random.choice([0.0, -random.uniform(0, 1)])
    s = solve(Q1, a1, Q2, d, sig, rc, m, gN, gC); f = formula(Q1, a1, Q2, d, sig, rc, m, gN, gC)
    ndem += s[0]
    if s[0] != f[0] or (s[0] and abs(s[1] - f[1]) > 1e-9):
        mism += 1
        if mism < 5: print("mismatch", (Q1, a1, Q2, d, sig, rc, m, gN, gC), s, f)
print(f"draws={n}, demands={ndem}, mismatches={mism}")
