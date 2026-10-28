# Proposition 7(b): credibility of servicing interruption.
# Normalized units (divide by s_E, s_U): a = c_E/s_E, l = ell/s_E, u = c_U/s_U. tau_E = 0.
# Without interruption: Europe bears a from 0, US bears nothing  -> p* = 0.
# Paper: interruption (Europe a+l from 0, US u after tau_U) is played iff (1-psi)u > psi(a+l) and tau_U < H_E = 1/(psi(a+l)),
# with share 1 - tau_U/H_E.
# We compare four timings of the interruption decision:
#  T0: once-and-for-all commitment at date 0 (what the proof uses)
#  ABS: Europe may stop after any rejection, stopping is irreversible (absorbing); buffer runs in calendar time from 0
#  A:  after each rejection Europe chooses whether to interrupt during the coming interval (reversible);
#      US buffer depletes only while servicing is interrupted (state b = remaining buffer steps)
#  B:  same as A but the interval's interruption decision is taken at the start of the period, before offers
import random, math
import numpy as np

def T0(psi, a, l, u, tauU, dt, T, wT):
    n = int(round(T / dt)); w = wT
    for k in range(n - 1, -1, -1):
        t = k * dt
        cu = u * dt if t >= tauU - 1e-12 else 0.0
        w = psi * max(w - (a + l) * dt, 0.0) + (1 - psi) * min(w + cu, 1.0)
    return w

def ABS(psi, a, l, u, tauU, dt, T, wT, tie_interrupt=True):
    # value if Europe has stopped: no US cost -> w_stop solves the no-interruption game (= 0 for a > 0)
    n = int(round(T / dt)); w = wT; ws = wT
    for k in range(n - 1, -1, -1):
        t = k * dt
        cu = u * dt if t >= tauU - 1e-12 else 0.0
        ws_new = psi * max(ws - a * dt, 0.0) + (1 - psi) * min(ws, 1.0)
        # after a rejection Europe chooses continue (w, cost a+l, US cost cu) or stop (ws, cost a, no US cost)
        cont = w - (a + l) * dt; stop = ws - a * dt
        if cont > stop or (tie_interrupt and cont == stop):
            eu, us_extra, nxt = cont, cu, w
        else:
            eu, us_extra, nxt = stop, 0.0, ws
        w = psi * max(eu, 0.0) + (1 - psi) * min(nxt + us_extra, 1.0)
        ws = ws_new
    return w

def A_or_B(psi, a, l, u, tauU, dt, T, wT, timing, tie_interrupt=True):
    nb = int(round(tauU / dt)); n = int(round(T / dt))
    W = np.full(nb + 1, wT, dtype=float)       # W[b], b = remaining buffer steps
    b = np.arange(nb + 1)
    for k in range(n):
        Wd0 = W                                   # next state if no interruption
        Wd1 = np.concatenate(([W[0]], W[:-1]))    # next state if interruption: b -> max(b-1, 0)
        usc = np.where(b == 0, u * dt, 0.0)       # US bears cost only once buffer exhausted
        if timing == "A":
            e0 = Wd0 - a * dt; e1 = Wd1 - (a + l) * dt
            d = (e1 > e0) | (tie_interrupt & (e1 == e0))
            eu = np.where(d, e1, e0); nxt = np.where(d, Wd1 + usc, Wd0)
            W = psi * np.maximum(eu, 0.0) + (1 - psi) * np.minimum(nxt, 1.0)
        else:
            v0 = psi * np.maximum(Wd0 - a * dt, 0.0) + (1 - psi) * np.minimum(Wd0, 1.0)
            v1 = psi * np.maximum(Wd1 - (a + l) * dt, 0.0) + (1 - psi) * np.minimum(Wd1 + usc, 1.0)
            W = np.maximum(v0, v1) if tie_interrupt else np.where(v1 > v0, v1, v0)
    return W[nb]

def paper(psi, a, l, u, tauU):
    HE = 1.0 / (psi * (a + l)) if psi * (a + l) > 0 else math.inf
    if (1 - psi) * u > psi * (a + l) and tauU < HE:
        return True, 1 - tauU / HE
    return False, 0.0

random.seed(9)
dt = 0.005
res = {k: [0, 0] for k in ("T0", "ABS", "A", "B")}
examplesA = []
for trial in range(120):
    psi = random.uniform(0.15, 0.85); a = random.uniform(0.05, 1.5); l = random.uniform(0.0, 1.0); u = random.uniform(0.05, 4)
    tauU = random.uniform(0, 4)
    gap = abs((1 - psi) * u - psi * (a + l))
    if gap < 0.03:
        continue
    HE = 1.0 / (psi * (a + l))
    if abs(tauU - HE) < 0.05:
        continue
    T = tauU + 1.0 / min(gap, psi * a) + 2.0
    if T > 60:
        continue
    pred, share = paper(psi, a, l, u, tauU)
    vals = {}
    for wT in (0.0, 1.0):
        vals.setdefault("T0", []).append(T0(psi, a, l, u, tauU, dt, T, wT))
        vals.setdefault("ABS", []).append(ABS(psi, a, l, u, tauU, dt, T, wT))
        vals.setdefault("A", []).append(A_or_B(psi, a, l, u, tauU, dt, T, wT, "A"))
        vals.setdefault("B", []).append(A_or_B(psi, a, l, u, tauU, dt, T, wT, "B"))
    for k, v in vals.items():
        played = min(v) > 0.02          # interruption raises Europe's share above the no-interruption value 0
        res[k][0] += 1
        if played != pred or (pred and abs(min(v) - share) > 0.03) or abs(v[0] - v[1]) > 0.03:
            res[k][1] += 1
            if k == "A" and len(examplesA) < 3:
                examplesA.append((round(psi, 3), round(a, 3), round(l, 3), round(u, 3), round(tauU, 3), "paper share", round(share, 3), "A-timing", [round(x, 3) for x in v]))
for k, (n, m) in res.items():
    print(f"timing {k}: {n} draws, mismatches with Prop 7(b) (incl. share and terminal-condition dependence): {m}")
print("examples under timing A:", examplesA)

# Exact illustration: psi=0.5, a=0.2, l=0.1, u=2, tauU=1 -> paper: share 1 - 0.5*0.3*1 = 0.85
p = (0.5, 0.2, 0.1, 2.0, 1.0)
for name, f in (("T0", lambda wT: T0(*p, 0.002, 12, wT)), ("ABS", lambda wT: ABS(*p, 0.002, 12, wT)),
                ("A", lambda wT: A_or_B(*p, 0.002, 12, wT, "A")), ("B", lambda wT: A_or_B(*p, 0.002, 12, wT, "B"))):
    print(name, [round(f(wT), 4) for wT in (0.0, 1.0)], "paper:", paper(*p))
# timing A with l = 0 (no private cost of interrupting): indifference, ties broken toward interruption
p0 = (0.5, 0.2, 0.0, 2.0, 1.0)
print("A, l=0, ties->interrupt:", [round(A_or_B(*p0, 0.002, 12, wT, "A"), 4) for wT in (0.0, 1.0)],
      " ties->no interrupt:", [round(A_or_B(*p0, 0.002, 12, wT, "A", tie_interrupt=False), 4) for wT in (0.0, 1.0)], "paper:", paper(*p0))
