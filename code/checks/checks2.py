import numpy as np, itertools, random
from scipy.optimize import linprog

pos = lambda x: max(0.0, x)

# ---------- 1. Simultaneous offers: pure NE on a grid, with and without undominated C bids ----------
def simultaneous(r, c, V, w, eps, mx, undominated):
    G = np.round(np.arange(0, mx + 1e-9, eps), 10)
    GC = [t for t in G if (not undominated) or t <= w + 1e-12]
    GU = [t for t in G if (not undominated) or t <= V + 1e-12]
    def pay(tU, tC):
        if tU - r >= tC - c - 1e-12:
            return (tU - r, -tU, 0.0, 'A')
        return (tC - c, -V, w - tC, 'a')
    ne = []
    for tU in GU:
        for tC in GC:
            pe, pu, pc, ch = pay(tU, tC)
            if any(pay(t, tC)[1] > pu + 1e-12 for t in GU):
                continue
            if any(pay(tU, t)[2] > pc + 1e-12 for t in GC):
                continue
            ne.append((tU, tC, ch, pe))
    return ne

print("=== Simultaneous offers ===")
for (r, c, w, V) in [(0.3, 0.5, 1.2, 2.0), (0.3, 0.5, 1.2, 0.6)]:
    Q = w - c + r
    for und in (False, True):
        ne = simultaneous(r, c, V, w, 0.05, 3.0, und)
        pes = [x[3] for x in ne]; wins = set(x[2] for x in ne)
        print(f"Q={Q:.2f} V={V} undominated={und}: winner {wins}, E payoff in [{min(pes):.2f},{max(pes):.2f}]  (-r+Q={Q-r:.2f}, V-r={V-r:.2f})")

# ---------- 2. Prop 5: incomplete information, check the draft's cutoff formula ----------
def prop5_numeric(a, R, sbar, n=200001):
    Ts = np.linspace(0, a + R + sbar, n)
    s = Ts + a - R
    F = np.clip(s / sbar, 0, 1)
    U = F * (-Ts) + (1 - F) * (-R)
    i = np.argmax(U)
    return Ts[i], s[i], 1 - F[i]

def prop5_draft(a, R, sbar):
    if a / 2 <= R:
        s = min(a / 2, sbar)
    else:
        s = a - R
    T = s - a + R
    return T, s, max(0.0, 1 - s / sbar)

def prop5_corrected(a, R, sbar):
    s = max(a - R, min(a / 2, sbar))
    T = pos(min(a / 2, sbar) - a + R) if s <= sbar else 0.0
    T = s - a + R if s <= sbar else 0.0
    return T, s, pos(1 - s / sbar)

print("\n=== Prop 5 ===")
for (a, R, sbar) in [(10, 6, 3), (4, 5, 10), (4, 1, 10), (10, 2, 5)]:
    print(f"a={a} R={R} sbar={sbar}: numeric T,s,breakdown={tuple(round(x,3) for x in prop5_numeric(a,R,sbar))} "
          f"draft={tuple(round(x,3) for x in prop5_draft(a,R,sbar))} corrected={tuple(round(x,3) for x in prop5_corrected(a,R,sbar))}")
random.seed(3); bad = 0
for _ in range(3000):
    a, R, sbar = random.uniform(0.1, 10), random.uniform(0.1, 10), random.uniform(0.1, 10)
    tn, sn, bn = prop5_numeric(a, R, sbar, 40001)
    tc, sc, bc = prop5_corrected(a, R, sbar)
    if abs(bn - bc) > 1e-3 or abs(tn - tc) > 2e-3 * (a + R + sbar):
        bad += 1
print("corrected formula mismatches over 3000 random draws:", bad)

# ---------- 3. Lemma 2 / Prop 4: tie-break dependence; add ex post net gain g from cutting ----------
def control_game(Q1, a1, Q2, delta, sigma, rc, g=0.0, U_cuts_when_indiff=True):
    # after refusal, U compares cut vs no cut
    cutU = -pos(Q1 + a1) - delta * pos(Q2) + g
    nocutU = -pos(Q1) - delta * pos(Q2)
    cut = cutU > nocutU + 1e-12 or (abs(cutU - nocutU) <= 1e-12 and U_cuts_when_indiff)
    Eref = (-a1 + pos(Q1 + a1) if cut else pos(Q1)) + delta * pos(Q2)
    Uref = cutU if cut else nocutU
    T = pos(Eref + sigma + rc)  # E accepts iff T - sigma - rc >= Eref
    demand = -T > Uref + 1e-12
    return dict(cut_after_refusal=cut, demand=demand, T=T if demand else None)

print("\n=== Prop 4 knife-edge: Q1=-2, a1=1.5, Q2=1, delta=.9, sigma=.2, rc=.1 ===")
for g in [0.0, -0.01, 0.01]:
    print(f"g={g:+.2f}:", control_game(-2, 1.5, 1, .9, .2, .1, g=g))
print("g=0, U breaks indifference against cutting:", control_game(-2, 1.5, 1, .9, .2, .1, g=0.0, U_cuts_when_indiff=False))

# ---------- 4. Permanent Tier 3: is it credible? ----------
# permanent cut removes alpha from E's exit cost in both periods; U's ex post comparison after refusal
def permanent_cut(Q1, a1, Q2, a2, delta):
    cutU = -pos(Q1 + a1) - delta * pos(Q2 + a2)
    oneU = -pos(Q1 + a1) - delta * pos(Q2)
    nocutU = -pos(Q1) - delta * pos(Q2)
    return cutU, oneU, nocutU
print("\n=== permanent vs one-period cut (Q1=-2,a1=1.5,Q2=1,a2=1.5,delta=.9): U payoffs (perm, one-period, none) =",
      permanent_cut(-2, 1.5, 1, 1.5, .9))

# ---------- 5. T-period preemption with gradual shifts ----------
def T_period(Q, alpha, delta, sigma, rc):
    """Backward induction. State: E retains control. Each period: U may demand (one-shot control transfer, permanent);
    E accepts/refuses; after refusal U may cut alpha_t this period; period rent [Q_t + alpha_t*cut]^+.
    Ties: U cuts when indifferent, U does not demand when indifferent, E accepts when indifferent.
    Returns (E value, U value, list of periods where U demands on the equilibrium path)."""
    Tn = len(Q)
    VE, VU = 0.0, 0.0
    plan = [None] * Tn
    for t in reversed(range(Tn)):
        cutU = -pos(Q[t] + alpha[t]) + delta * VU
        nocutU = -pos(Q[t]) + delta * VU
        cut = cutU >= nocutU - 1e-12
        Eref = (-alpha[t] + pos(Q[t] + alpha[t]) if cut else pos(Q[t])) + delta * VE
        Uref = cutU if cut else nocutU
        Tpay = pos(Eref + sigma + rc)
        if -Tpay > Uref + 1e-12:
            VE, VU = Tpay - sigma - rc, -Tpay
            plan[t] = ('demand', round(Tpay, 3))
        else:
            # no demand: contest without cut
            VE, VU = pos(Q[t]) + delta * VE, -pos(Q[t]) + delta * VU
            plan[t] = ('none',)
    return VE, VU, plan

print("\n=== 4-period gradual shift: Q=(-2,-1.2,-0.4,0.4), alpha=1 each, steps 0.8<alpha ===")
print(T_period([-2, -1.2, -0.4, 0.4], [1, 1, 1, 1], 0.9, 0.2, 0.1))

# ---------- 6. Prop 3(c): Groseclose-Snyder counterexample ----------
# 3 members, passage needs 2 of 3; second mover P values passage at B; members' own premium for 'yes' q_i = 0.
# U (first mover) pays tau_i for 'no'. P can buy member i at [tau_i - q_i]^+ (+eps).
# U must make every winning coalition cost >= B.  LP: min sum tau s.t. tau_i + tau_j >= B for all pairs.
B = 1.0
res = linprog(c=[1, 1, 1], A_ub=[[-1, -1, 0], [-1, 0, -1], [0, -1, -1]], b_ub=[-B, -B, -B], bounds=[(0, None)] * 3)
print("\n=== G-S counterexample: U's minimal cost =", round(res.fun, 3), "tau =", np.round(res.x, 3),
      "| draft's 'cheapest blocking minority premium' = 0 (q_i=0) or B=1 if pricing only a minimal blocking pair")

# ---------- 7. Prop 2 remark: preventive incentive non-monotone in Z ----------
print("\n=== preventive gain vs Z (complete info): alpha1 = Z, Q2 = 5 - Z, Q1 + alpha1 = -3 + 0.5 Z, sigma+rc = 0.5, delta=1")
for Z in [0.5, 1, 2, 3, 4, 5, 6, 7]:
    a1, Q2, Q1pa = Z, 5 - Z, -3 + 0.5 * Z
    credible = Q1pa <= 0
    gain = min(a1 - 0.5, pos(Q2)) if (credible and Q2 > 0 and a1 > 0.5) else 0.0
    print(f"Z={Z}: credible={credible}, Q2={Q2}, U's gain from demanding control={pos(gain):.2f}")
