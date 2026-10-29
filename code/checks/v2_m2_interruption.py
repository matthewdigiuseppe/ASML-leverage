# v2 verifier m2: interruption corollary of Proposition 6 (Europe interrupts ASML servicing).
#
# Discrete game as in v2_m2_prop6_holdup.py with constant baseline disagreement costs cE0, cU0.
# Interruption costs E a flow l while interrupted; it costs U a flow (1-h) cS while interrupted
# AND the US buffer is exhausted. Four timing / buffer models are solved by backward induction
# over the buffer state (no closed form is used inside the solvers):
#   M  (memo)      : buffer is a STOCK b in [0, tU], depleted only in rounds with interruption;
#                    interruption chosen at the start of the round, before the proposer is drawn.
#   CAL (calendar) : buffer runs out at calendar date tU whatever E does; same within-round timing.
#   POST           : stock buffer; interruption chosen after an offer is rejected (by E, ex post).
#   PROP           : stock buffer; interruption chosen after the proposer is drawn, before offers.
# Closed forms compared (frequent-offer limit; rho = r + lam, w_b = lam/rho, K = beta(1-h)cS-(1-beta)l):
#   xF0  = w_b[Q+beta(V-Q)] + (1-w_b)[beta cU0 - (1-beta) cE0]
#   M  : P* = max{Q, xF0, xF0 + (1-w_b)[beta(1-h)cS e^{-rho tU} - (1-beta) l]}
#   CAL: P* = max{Q, xF0 + (1-w_b) e^{-rho tU} [K]^+}
#   POST (l>0): P* = max{Q, xF0} (interruption never used)
import numpy as np

rng = np.random.default_rng(7)


def fp(A, B, C, Dc, beta, Q):
    # unique fixed point of x = A + B x + (1-beta) max(Q, C + Dc x)   (B + (1-beta) Dc < 1)
    x1 = (A + (1 - beta) * C) / (1 - B - (1 - beta) * Dc)
    x2 = (A + (1 - beta) * Q) / (1 - B)
    return np.where(C + Dc * x1 >= Q, x1, x2)


def draw(N, D):
    p = {}
    p["r"] = rng.uniform(0.05, 1.0, N)
    p["lam"] = np.where(rng.random(N) < 0.25, 0.0, rng.uniform(0, 2, N))
    p["beta"] = np.where(rng.random(N) < 0.1, 0.0, rng.uniform(0, 0.95, N))
    p["V"] = rng.uniform(0.5, 3, N)
    p["cE0"] = rng.uniform(0, 1, N) * (rng.random(N) < 0.7)
    p["cU0"] = rng.uniform(0, 1, N) * (rng.random(N) < 0.7)
    p["l"] = np.where(rng.random(N) < 0.05, 0.0, rng.uniform(0, 1, N))
    p["cS"] = rng.uniform(0, 3, N)
    p["h"] = np.where(rng.random(N) < 0.2, 0.0, rng.uniform(0, 1, N))
    p["tU"] = np.round(rng.uniform(0, 3, N) / 0.01) * 0.01
    rho = p["r"] + p["lam"]; wb = p["lam"] / rho
    # Q chosen relative to the no-interruption value so that exit binds in about 1/3 of draws
    p["Q"] = np.zeros(N)
    xF0_noQ = lambda Q: wb * (Q + p["beta"] * (p["V"] - Q)) + (1 - wb) * (p["beta"] * p["cU0"] - (1 - p["beta"]) * p["cE0"])
    # Q* solving Q = xF0(Q):  Q(1 - wb(1-beta)) = wb beta V + (1-wb)(beta cU0 - (1-beta) cE0)
    Qstar = (wb * p["beta"] * p["V"] + (1 - wb) * (p["beta"] * p["cU0"] - (1 - p["beta"]) * p["cE0"])) / (1 - wb * (1 - p["beta"]))
    p["Q"] = np.minimum(Qstar + rng.uniform(-1.5, 0.7, N), p["V"] - 1e-3)
    return p


def common(p, D):
    r, lam, beta, V, Q = p["r"], p["lam"], p["beta"], p["V"], p["Q"]
    mu = 1 - np.exp(-lam * D); delta = np.exp(-r * D); k = (1 - mu) * delta
    pain = (1 - p["h"]) * p["cS"]
    a = lambda cU: beta * (mu * V + (1 - mu) * (1 - delta) * cU)
    e = lambda cE: mu * Q - (1 - mu) * (1 - delta) * cE
    return mu, delta, k, pain, a, e


def solve_M(p, D):
    beta, Q = p["beta"], p["Q"]
    mu, delta, k, pain, a, e = common(p, D)
    N = len(beta); K = np.round(p["tU"] / D).astype(int); Kmax = K.max()
    y0 = fp(a(p["cU0"]), 0 * beta + beta * k, e(p["cE0"]), k + 0 * beta, beta, Q)       # never interrupt
    y1_0 = fp(a(p["cU0"] + pain), beta * k, e(p["cE0"] + p["l"]), k + 0 * beta, beta, Q)  # interrupt at b=0
    x = np.maximum(y0, y1_0)
    pol = y1_0 > y0
    allpol = pol.copy()
    xK = np.where(K == 0, x, np.nan); polK = np.where(K == 0, pol, False); allK = np.where(K == 0, allpol, False)
    for j in range(1, Kmax + 1):
        y1 = a(p["cU0"]) + beta * k * x + (1 - beta) * np.maximum(Q, e(p["cE0"] + p["l"]) + k * x)
        xn = np.maximum(y0, y1)
        pj = y1 > y0
        allpol = allpol & pj
        x = xn
        hit = K == j
        xK = np.where(hit, x, xK); polK = np.where(hit, pj, polK); allK = np.where(hit, allpol, allK)
    return xK, y0, polK, allK


def solve_CAL(p, D):
    beta, Q = p["beta"], p["Q"]
    mu, delta, k, pain, a, e = common(p, D)
    K = np.round(p["tU"] / D).astype(int); Kmax = K.max()
    y0 = fp(a(p["cU0"]), beta * k, e(p["cE0"]), k + 0 * beta, beta, Q)
    y1 = fp(a(p["cU0"] + pain), beta * k, e(p["cE0"] + p["l"]), k + 0 * beta, beta, Q)
    tail = np.maximum(y0, y1)
    # backward from tU: at calendar index j (steps before tU), the draw's own clock
    x = tail.copy(); early_int = np.zeros(len(beta), bool)
    out = np.where(K == 0, tail, np.nan)
    for j in range(1, Kmax + 1):
        active = j <= K
        c0 = a(p["cU0"]) + beta * k * x + (1 - beta) * np.maximum(Q, e(p["cE0"]) + k * x)
        c1 = a(p["cU0"]) + beta * k * x + (1 - beta) * np.maximum(Q, e(p["cE0"] + p["l"]) + k * x)
        early_int |= active & (c1 > c0 + 1e-15)
        x = np.where(active, np.maximum(c0, c1), x)
        out = np.where(K == j, x, out)
    return out, y0, early_int


def solve_POST(p, D, tie_interrupt=True):
    # E chooses interruption after a rejection, to maximize its own continuation (ties -> interrupt)
    beta, Q = p["beta"], p["Q"]
    mu, delta, k, pain, a, e = common(p, D)
    K = np.round(p["tU"] / D).astype(int); Kmax = K.max()
    l = p["l"]
    # b = 0: d_E^1 - d_E^0 = -(1-mu)(1-delta) l
    i0 = (l <= 0) if tie_interrupt else np.zeros(len(l), bool)
    cU_b0 = p["cU0"] + np.where(i0, pain, 0); cE_b0 = p["cE0"] + np.where(i0, l, 0)
    x = fp(a(cU_b0), beta * k, e(cE_b0), k + 0 * beta, beta, Q)
    y0 = fp(a(p["cU0"]), beta * k, e(p["cE0"]), k + 0 * beta, beta, Q)
    out = np.where(K == 0, x, np.nan); multi = np.zeros(len(l), bool)
    for j in range(1, Kmax + 1):
        # candidate i*=0 (stay): x = y0
        d0_c0 = e(p["cE0"]) + k * y0
        d1_c0 = e(p["cE0"] + l) + k * x
        ok0 = d0_c0 > d1_c0 if tie_interrupt else d0_c0 >= d1_c0
        # candidate i*=1 (deplete): x1 = F(x(b-D)), no US pain while b > 0
        x1 = a(p["cU0"]) + beta * k * x + (1 - beta) * np.maximum(Q, e(p["cE0"] + l) + k * x)
        d0_c1 = e(p["cE0"]) + k * x1
        d1_c1 = e(p["cE0"] + l) + k * x
        ok1 = d1_c1 >= d0_c1 if tie_interrupt else d1_c1 > d0_c1
        multi |= (j <= K) & ok0 & ok1
        xn = np.where(ok0 & ok1, np.maximum(y0, x1), np.where(ok1, x1, y0))
        x = np.where(j <= K, xn, x)
        out = np.where(K == j, x, out)
    return out, y0, multi


def solve_PROP(p, D):
    # interruption chosen after the proposer is drawn, before offers; ties -> interrupt
    beta, Q, l = p["beta"], p["Q"], p["l"]
    mu, delta, k, pain, a, e = common(p, D)
    K = np.round(p["tU"] / D).astype(int); Kmax = K.max()
    # b = 0: E-proposer interrupts (raises U's disagreement cost, no state change); U-proposer: not if l>0
    iU0 = l <= 0
    x = fp(a(p["cU0"] + pain), beta * k, e(p["cE0"] + np.where(iU0, l, 0)), k + 0 * beta, beta, Q)
    y0 = fp(a(p["cU0"]), beta * k, e(p["cE0"]), k + 0 * beta, beta, Q)
    out = np.where(K == 0, x, np.nan); nsol_min = np.full(len(l), 9)
    for j in range(1, Kmax + 1):
        best = np.full(len(l), -np.inf); nsol = np.zeros(len(l), int)
        for iE in (0, 1):
            for iU in (0, 1):
                A = beta * (mu * p["V"] + (1 - mu) * (1 - delta) * p["cU0"]) + (beta * k * x if iE else 0)
                B = 0 if iE else beta * k
                C = e(p["cE0"] + (l if iU else 0)) + (k * x if iU else 0)
                Dc = 0 if iU else k
                xc = fp(A, B + 0 * beta, C, Dc + 0 * beta, beta, Q)
                okE = (x >= xc) if iE else (x < xc)
                d1 = e(p["cE0"] + l) + k * x
                d0 = e(p["cE0"]) + k * xc
                okU = (d1 >= d0) if iU else (d0 > d1)
                ok = okE & okU
                nsol += ok
                best = np.where(ok, np.maximum(best, xc), best)
        act = j <= K
        nsol_min = np.where(act, np.minimum(nsol_min, nsol), nsol_min)
        x = np.where(act, best, x)
        out = np.where(K == j, x, out)
    return out, y0, nsol_min


def closed(p):
    r, lam, beta, V, Q = p["r"], p["lam"], p["beta"], p["V"], p["Q"]
    rho = r + lam; wb = lam / rho
    xF0 = wb * (Q + beta * (V - Q)) + (1 - wb) * (beta * p["cU0"] - (1 - beta) * p["cE0"])
    pain = (1 - p["h"]) * p["cS"]
    Dm = beta * pain * np.exp(-rho * p["tU"]) - (1 - beta) * p["l"]
    Kp = np.maximum(beta * pain - (1 - beta) * p["l"], 0)
    P0 = np.maximum(Q, xF0)
    PM = np.maximum(P0, xF0 + (1 - wb) * Dm)
    PC = np.maximum(Q, xF0 + (1 - wb) * np.exp(-rho * p["tU"]) * Kp)
    return xF0, P0, PM, PC, Dm, wb


N = 3000
D = 0.002
p = draw(N, D)
xF0, P0, PM, PC, Dm, wb = closed(p)

print("=== Model M (memo): stock buffer, interruption chosen before the proposer is drawn ===")
xa, y0a, polK, allK = solve_M(p, D)
xb, y0b, polKb, allKb = solve_M(p, D / 2)
xR, y0R = 2 * xb - xa, 2 * y0b - y0a
bind0 = p["Q"] > xF0
print("draws", N, " exit binds without interruption in", int(bind0.sum()))
print("max |P*_noint(D->0) - max(Q,xF0)|      =", f"{np.max(np.abs(y0R - P0)):.2e}")
print("max |P*_int(D->0) - closed form M|      =", f"{np.max(np.abs(xR - PM)):.2e}")
gain = xR - y0R            # D -> 0 (Richardson) gain from allowing interruption
margin = (1 - wb) * Dm - np.maximum(p["Q"] - xF0, 0)      # exact condition with exit
clear = np.abs(margin) > 5e-3
pred = margin > 0
dis = clear & ((gain > 1e-6) != pred)
for i in np.flatnonzero(dis)[:8]:
    print("   disagreement:", {kk: round(float(v[i]), 3) for kk, v in p.items()}, "margin", round(float(margin[i]), 4),
          "gain(D/2)", f"{(xb - y0b)[i]:.2e}", "gain(D)", f"{(xa - y0a)[i]:.2e}", "Richardson gain", f"{gain[i]:.2e}")
print("decision at t=0 (D->0 gain > 1e-6) vs exact condition (1-w_b)Dm > [Q-xF0]^+:",
      f"agree {np.mean((gain > 1e-6)[clear] == pred[clear]):.4f} on {clear.sum()} non-tie draws")
memo = Dm > 0
nb = ~bind0
print("memo condition beta(1-h)cS e^{-rho tU} > (1-beta) l vs decision, exit not binding:",
      f"agree {np.mean((gain > 1e-6)[clear & nb] == memo[clear & nb]):.4f} on {(clear & nb).sum()} draws")
cex = clear & bind0 & memo & ~pred
print("draws where exit binds, memo condition holds, but interruption does NOT raise P*:", int(cex.sum()))
if cex.any():
    i = np.flatnonzero(cex)[0]
    print("  example:", {kk: round(float(v[i]), 4) for kk, v in p.items()}, " xF0=", round(float(xF0[i]), 4),
          " gain D->0:", round(float(xR[i] - y0R[i]), 5))
viol = polKb & ~allKb
print("time consistency: draws interrupting at b=tU but not at some later stock level:", int(viol.sum()),
      "| draws interrupting at tU:", int(polKb.sum()))

print("\n=== Model CAL: buffer runs out at calendar date tU regardless of interruption ===")
ca, y0c, early_a = solve_CAL(p, D)
cb, y0cb, early_b = solve_CAL(p, D / 2)
cR = 2 * cb - ca
print("max |P*(D->0) - max{Q, xF0 + (1-w_b) e^{-rho tU}[K]^+}| =", f"{np.max(np.abs(cR - PC)):.2e}")
print("draws where E interrupts at some date before tU (l>0):", int((early_b & (p["l"] > 0)).sum()))
Kpos = p["beta"] * (1 - p["h"]) * p["cS"] - (1 - p["beta"]) * p["l"]
cex2 = nb & (Kpos > 1e-3) & (Dm < -1e-3) & ((1 - wb) * np.exp(-(p["r"] + p["lam"]) * p["tU"]) * Kpos > 1e-4)
print("draws where memo condition FAILS but interruption raises P* in CAL:", int(cex2.sum()),
      "; of these, D->0 gain > 0 in", int(((cR - y0R) > 1e-6)[cex2].sum()))

print("\n=== Model POST: interruption chosen after a rejection (ex post) ===")
pa, y0p, multi_a = solve_POST(p, D)
pb, y0pb, multi_b = solve_POST(p, D / 2)
lpos = p["l"] > 0
print("l>0 draws:", int(lpos.sum()), " max (P*_POST - P*_noint) =", f"{np.max((pb - y0pb)[lpos]):.2e}",
      " draws with multiple Markov equilibria at some stock:", int(multi_b[lpos].sum()))
l0 = ~lpos
if l0.any():
    print("l=0 draws (ties broken toward interruption):", int(l0.sum()), " max|P*_POST - P*_M| =",
          f"{np.max(np.abs(pb - xb)[l0]):.2e}")

print("\n=== Model PROP: interruption chosen after the proposer is drawn, before offers ===")
qa, y0q, nsa = solve_PROP(p, 0.004)
qb, y0qb, nsb = solve_PROP(p, 0.002)
gq = qb - y0qb
xM2, _, _, _ = solve_M(p, 0.002)
sel = nb & (p["beta"] > 0.05) & ((1 - p["h"]) * p["cS"] > 0.05) & (p["tU"] < 2)
print("draws (exit not binding, beta>0.05, (1-h)cS>0.05, tU<2):", int(sel.sum()),
      " min gain:", f"{gq[sel].min():.3e}", " draws where memo condition fails yet gain>0:",
      int(((gq > 1e-6) & (Dm < 0) & sel).sum()))
print("stock levels with no Markov equilibrium in pure choices:", int((nsb == 0).sum()))
print("PROP value >= memo-timing value (same D) in all draws:", bool(np.all(qb >= xM2 - 1e-12)),
      "; max shortfall:", f"{np.max(xM2 - qb):.2e}")

print("\n=== Hand-picked cases (memo timing M) ===")
cases = [
    dict(r=0.2, lam=0.3, beta=0.5, V=2.0, Q=-1.0, cE0=0.2, cU0=0.1, l=0.5, cS=2.0, h=0.0, tU=0.5),
    dict(r=0.2, lam=0.3, beta=0.5, V=2.0, Q=-1.0, cE0=0.2, cU0=0.1, l=0.5, cS=2.0, h=0.0, tU=2.0),
    dict(r=0.2, lam=0.3, beta=0.5, V=2.0, Q=-1.0, cE0=0.2, cU0=0.1, l=0.5, cS=2.0, h=0.75, tU=0.1),
    dict(r=0.2, lam=0.0, beta=0.5, V=2.0, Q=-1.0, cE0=0.2, cU0=0.1, l=0.0, cS=2.0, h=0.0, tU=3.0),
    dict(r=0.2, lam=0.3, beta=0.0, V=2.0, Q=-1.0, cE0=0.2, cU0=0.1, l=0.1, cS=2.0, h=0.0, tU=0.0),
    dict(r=0.2, lam=0.3, beta=0.5, V=2.0, Q=0.6, cE0=0.2, cU0=0.1, l=0.2, cS=2.0, h=0.0, tU=0.5),
]
for c in cases:
    pc = {kk: np.array([float(v)]) for kk, v in c.items()}
    xF0c, P0c, PMc, PCc, Dmc, wbc = closed(pc)
    xa_, y0a_, _, _ = solve_M(pc, 0.002); xb_, y0b_, _, _ = solve_M(pc, 0.001)
    rho = c["r"] + c["lam"]
    tbar = np.log(c["beta"] * (1 - c["h"]) * c["cS"] / ((1 - c["beta"]) * c["l"])) / rho if c["beta"] * c["l"] * (1 - c["h"]) > 0 else np.inf
    print(c, f"\n   P*_noint={2*y0b_[0]-y0a_[0]:.5f} P*_int={2*xb_[0]-xa_[0]:.5f} closed form={PMc[0]:.5f} "
          f"memo condition={bool(Dmc[0] > 0)} tbar={tbar:.4f}")

# PROP: lower bounds from the two constant policies (frequent-offer limit, exit not binding):
#   u=0 (deplete only in E-proposer rounds): gain0 = (1-w_b) beta (1-h) cS e^{-rho tU / beta}
#   u=1 (deplete in every round)          : gain1 = (1-w_b)[beta(1-h)cS e^{-rho tU} - (1-beta) l (1 - e^{-rho tU})]
rho = p["r"] + p["lam"]
with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
    g0 = np.where(p["beta"] > 0, (1 - wb) * p["beta"] * (1 - p["h"]) * p["cS"] * np.exp(-rho * p["tU"] / np.maximum(p["beta"], 1e-300)), 0.0)
g1 = (1 - wb) * (p["beta"] * (1 - p["h"]) * p["cS"] * np.exp(-rho * p["tU"]) - (1 - p["beta"]) * p["l"] * (1 - np.exp(-rho * p["tU"])))
qa2, y0qa2, _ = solve_PROP(p, 0.004)
gR = 2 * (qb - y0qb) - (qa2 - y0qa2)
print("PROP, exit not binding: min over draws of [gain(D->0) - max(gain0, gain1, 0)] =",
      f"{np.min((gR - np.maximum(np.maximum(g0, g1), 0))[nb]):.2e}",
      "; max excess over the better constant policy:", f"{np.max((gR - np.maximum(np.maximum(g0, g1), 0))[nb]):.2e}")
