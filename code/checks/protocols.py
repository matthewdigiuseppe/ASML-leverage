"""Brute-force checks of the static alignment contest under alternative protocols.
Single exit option a (plus A). Grid of mesh eps. E breaks ties toward A.
Payoffs: E: tU - r if A; tC - c if a.  U: -tU if A; -V if a.  C: 0 if A; w - tC if a, w=(1-theta)W.
Q = w - c + r.  rho0 = max(0, r - c) (unaided exit premium).
"""
import itertools, random
import numpy as np

def grid(mx, eps):
    return np.round(np.arange(0, mx + 1e-9, eps), 10)

def E_choice(tU, tC, r, c):
    return 'A' if tU - r >= tC - c - 1e-12 else 'a'

def payoffs(ch, tU, tC, r, c, V, w):
    if ch == 'A':
        return (tU - r, -tU, 0.0)
    return (tC - c, -V, w - tC)

def U_first(r, c, V, w, eps, mx):
    """Return set of SPE outcomes (E payoff, U payment if A else None, winner), over all C tie-breaks."""
    G = grid(mx, eps)
    outcomes = set()
    # C best-response sets
    def C_BR(tU):
        vals = []
        for tC in G:
            ch = E_choice(tU, tC, r, c)
            vals.append((payoffs(ch, tU, tC, r, c, V, w)[2], tC))
        best = max(v for v, _ in vals)
        return [tC for v, tC in vals if abs(v - best) < 1e-12]
    # For SPE set: C may use any BR. U's value at tU depends on C's selection. Collect U's best value range.
    # Approach: compute for each tU the set of U payoffs achievable; an SPE exists with tU* if there is a
    # selection such that U's payoff at tU* >= U's payoff at every other tU under the WORST selection for U there.
    Uvals = {}
    for tU in G:
        res = []
        for tC in C_BR(tU):
            ch = E_choice(tU, tC, r, c)
            pe, pu, pc = payoffs(ch, tU, tC, r, c, V, w)
            res.append((pu, pe, ch))
        Uvals[tU] = res
    worst = {tU: min(x[0] for x in res) for tU, res in Uvals.items()}
    for tU, res in Uvals.items():
        for pu, pe, ch in res:
            if all(pu >= worst[t2] - 1e-12 for t2 in G):
                outcomes.add((round(pe, 6), round(tU, 6), ch))
    return outcomes

def C_first(r, c, V, w, eps, mx, undominated=False):
    G = grid(mx, eps)
    GC = [t for t in G if (not undominated) or t <= w + 1e-12]
    outcomes = set()
    def U_BR(tC):
        vals = []
        for tU in G:
            ch = E_choice(tU, tC, r, c)
            vals.append((payoffs(ch, tU, tC, r, c, V, w)[1], tU))
        best = max(v for v, _ in vals)
        return [tU for v, tU in vals if abs(v - best) < 1e-12]
    Cvals = {}
    for tC in GC:
        res = []
        for tU in U_BR(tC):
            ch = E_choice(tU, tC, r, c)
            pe, pu, pc = payoffs(ch, tU, tC, r, c, V, w)
            res.append((pc, pe, tU, ch))
        Cvals[tC] = res
    worst = {t: min(x[0] for x in res) for t, res in Cvals.items()}
    for tC, res in Cvals.items():
        for pc, pe, tU, ch in res:
            if all(pc >= worst[t2] - 1e-12 for t2 in GC):
                outcomes.add((round(pe, 6), round(tU, 6), ch))
    return outcomes

def E_tiol(r, c, V, w, eps, mx):
    """E proposes T to U. If U rejects, C makes a TIOLI offer to E (C has all bargaining power vs E)."""
    G = grid(mx, eps)
    # continuation after rejection: C picks tC maximizing its payoff given E's choice rule with tU=0
    best = None
    for tC in G:
        ch = E_choice(0.0, tC, r, c)
        pe, pu, pc = payoffs(ch, 0.0, tC, r, c, V, w)
        if best is None or pc > best[2] + 1e-12:
            best = (pe, pu, pc, ch)
    peR, puR, _, chR = best
    # E chooses T: U accepts iff -T >= puR (tie: accept)
    bestE = None
    for T in G:
        if -T >= puR - 1e-12:
            pe = T - r
        else:
            pe = peR
        if bestE is None or pe > bestE[0] + 1e-12:
            bestE = (pe, T)
    return bestE, chR

random.seed(1)
eps, mx = 0.05, 6.0
print("=== U first: US wins case (V >= Q) and US loses case (V < Q) ===")
for trial in range(6):
    r = round(random.uniform(0, 1), 2); c = round(random.uniform(0, 2), 2); w = round(random.uniform(0, 3), 2)
    Q = w - c + r
    V = round(Q + random.uniform(-1.5, 1.5), 2)
    if V < 0: V = 0.3
    out = U_first(r, c, V, w, eps, mx)
    pes = sorted(o[0] for o in out); winners = set(o[2] for o in out)
    print(f"r={r} c={c} w={w} Q={Q:.2f} V={V} rho0={max(0,r-c):.2f} | winners={winners} E payoff range [{pes[0]:.2f},{pes[-1]:.2f}]  (-r+[Q]+={-r+max(0,Q):.2f}, V-r={V-r:.2f})")

print("\n=== C first (V >= Q): SPE set of US payments, all vs undominated C bids ===")
for trial in range(5):
    r = round(random.uniform(0, 1), 2); c = round(random.uniform(0, 2), 2); w = round(random.uniform(0.5, 3), 2)
    Q = w - c + r
    V = round(max(Q, 0) + random.uniform(0.5, 2), 2)
    out = C_first(r, c, V, w, eps, mx)
    outu = C_first(r, c, V, w, eps, mx, undominated=True)
    pay = sorted(o[1] for o in out if o[2] == 'A'); payu = sorted(o[1] for o in outu if o[2] == 'A')
    print(f"r={r} c={c} w={w} Q={Q:.2f} V={V} rho0={max(0,r-c):.2f} | all SPE: tU in [{pay[0]:.2f},{pay[-1]:.2f}] ; undominated: [{payu[0]:.2f},{payu[-1]:.2f}]")

print("\n=== E makes TIOLI to U; C makes TIOLI to E after rejection ===")
for trial in range(6):
    r = round(random.uniform(0, 1), 2); c = round(random.uniform(0, 2), 2); w = round(random.uniform(0, 3), 2)
    Q = w - c + r
    V = round(max(Q, 0) + random.uniform(0.2, 2), 2)
    (pe, T), chR = E_tiol(r, c, V, w, eps, mx)
    print(f"Q={Q:.2f} V={V} | E demands T={T:.2f} (prediction V*1{{Q>0}}={V if Q>0 else 0:.2f}), E payoff {pe:.2f}")
