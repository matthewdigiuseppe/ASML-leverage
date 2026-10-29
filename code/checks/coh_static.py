# Coherence checks on the static model (Prop 1, Prop 3 b/e, Prop 2 (d)/(f) text claims).
# Grid game: U offers tU, C offers tC (sees tU), E chooses A iff tU - chi_r r >= lam*tC - c (tie -> A).
# C payoffs: (1-theta)W - tC if exit; C "does not bid at zero profit" means C only wins with strictly positive profit.
# U tie-breaking is NOT fixed: we collect every SPE outcome (U may break its own indifference either way).
import itertools
pos = lambda x: max(0.0, x)

def spe_outcomes(V, w, BC, BU, lam, c, rr, eps):
    n_U = int(round(BU / eps)); n_C = int(round(BC / eps))
    GU = [i * eps for i in range(n_U + 1)]
    GC = [i * eps for i in range(n_C + 1)]
    res = {}
    for tU in GU:
        # C's best response: smallest winning offer with strictly positive profit, else lose
        win = [tC for tC in GC if lam * tC - c > tU - rr + 1e-12 and w - tC > 1e-12]
        if win:
            tC = min(win); res[tU] = ('X', -V, lam * tC - c)
        else:
            res[tU] = ('A', -tU, tU - rr)
    best = max(v[1] for v in res.values())
    return sorted({(round(tU, 6), v[0], round(v[2], 6)) for tU, v in res.items() if abs(v[1] - best) < 1e-12},
                  key=lambda x: x[0])

print("=== Prop 1 at the tie Q = V ===")
# lam=1, B_C=1 < (1-theta)W=2, c=0, chi_r r=0 => omega=1, Q=1; V=1, B_U=2
outs = spe_outcomes(V=1.0, w=2.0, BC=1.0, BU=2.0, lam=1.0, c=0.0, rr=0.0, eps=0.01)
print("SPE outcomes (tU, alignment, E payoff):", outs[:3], '...', outs[-2:])
print("exit SPE exists:", any(o[1] == 'X' for o in outs), "| aligned SPE exists:", any(o[1] == 'A' for o in outs))

print("\n=== Prop 3(e): B_U < Q <= V but China values exit MORE than the US values alignment ===")
W, theta, BC, lam, c, rr = 100.0, 0.0, 100.0, 1.0, 95.0, 0.0
w = (1 - theta) * W; omega = lam * min(w, BC); Q = omega - c + rr
V, BU = 10.0, 3.0
outs = spe_outcomes(V=V, w=w, BC=BC, BU=BU, lam=lam, c=c, rr=rr, eps=0.5)
print(f"Q={Q}, V={V}, B_U={BU}, China's value of exit (1-theta)W={w}")
print("outcomes:", set(o[1] for o in outs), "-> Europe exits, yet (1-theta)W =", w, "> V =", V,
      ": the US does NOT value alignment more than China values exit")

print("\n=== Prop 3(b): 'leverage is non-monotone in compute scarcity' ===")
def L_of_nu(nu, base, alpha, mai, kX, kA):
    chi = 1 if (nu + mai >= kX and nu < kA) else 0
    return pos(base - chi * alpha)   # base = Q without the AI term
for base in [0.5, -3.0]:
    Ls = [L_of_nu(nu / 10, base, alpha=1.0, mai=0.0, kX=1.0, kA=2.0) for nu in range(0, 31)]
    print(f"Q without AI term = {base}: L over nu grid takes values {sorted(set(Ls))}"
          f" -> {'non-monotone' if len(set(Ls))>1 else 'CONSTANT (monotone)'}")

print("\n=== Prop 2(f) text: 'the US must pay ... even when Q<0' ===")
for (Q, V, beta) in [(-1.0, 4.0, 0.5), (-9.0, 4.0, 0.5), (-3.0, 1.0, 0.2)]:
    print(f"Q={Q}, V={V}, beta={beta}: L = [Q + beta(V-Q)]^+ = {pos(Q + beta * (V - Q)):.3f}")
