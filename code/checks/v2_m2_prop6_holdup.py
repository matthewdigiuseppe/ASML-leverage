# v2 verifier m2: Proposition 6 (pain and breakdown) with time-varying disagreement costs.
#
# Discrete game (offers every D): proposer E w.p. beta, U otherwise. Responder accepts or rejects.
# After rejecting a U offer, E may exit (normalized value Q to E). Otherwise breakdown into exit
# w.p. mu = 1-exp(-lam D); else status quo with normalized flows -c_E(t), -c_U(t) for the period
# (weight 1-delta, delta = exp(-r D)), next round at t+D. Markov (state = calendar time t).
# Backward induction on a grid, exact stationary tail after T0 (costs constant after T0).
# Compared with:
#   formula   x_F(0) = w_b[Q+beta(V-Q)] + (1-w_b)[beta Chat_U - (1-beta) Chat_E]
#   exact     P*     = x_F(0) + max(0, sup_t e^{-rho t}(Q - x_F(t)))  (= sup over exit times)
#   condition exit never binds  <=>  Q <= inf_t x_F(t)
#            <=> Q <= inf_t [lam beta V + r G(t)]/(r + lam beta),  G = beta Chat_U(t) - (1-beta) Chat_E(t)
# The recursion does NOT use any of these formulas.
import numpy as np

rng = np.random.default_rng(20261029)


def stationary_fp(beta, mu, delta, V, Q, cE, cU):
    # unique fixed point of x = beta[mu V + (1-mu)((1-delta)cU + delta x)]
    #                         + (1-beta) max(Q, mu Q + (1-mu)(-(1-delta)cE + delta x))
    a = beta * (mu * V + (1 - mu) * (1 - delta) * cU)
    e = mu * Q - (1 - mu) * (1 - delta) * cE
    k = (1 - mu) * delta
    x1 = (a + (1 - beta) * e) / (1 - k)                 # exit not used
    x2 = (a + (1 - beta) * Q) / (1 - beta * k)          # exit floor used
    return np.where(e + k * x1 >= Q, x1, x2)


def backward(par, D):
    r, lam, beta, V, Q = par["r"], par["lam"], par["beta"], par["V"], par["Q"]
    mu = 1 - np.exp(-lam * D)
    delta = np.exp(-r * D)
    T0 = float(np.max(par["T0"]))   # costs are constant after each draw's T0 <= T0
    n = int(round(T0 / D))
    cEf, cUf = par["cE"], par["cU"]   # functions of t -> arrays over draws
    x = stationary_fp(beta, mu, delta, V, Q, cEf(T0 + 1e-9), cUf(T0 + 1e-9))
    for k in range(n - 1, -1, -1):
        t = k * D
        cE, cU = cEf(t + 1e-12), cUf(t + 1e-12)
        PE = mu * V + (1 - mu) * ((1 - delta) * cU + delta * x)
        dE = mu * Q + (1 - mu) * (-(1 - delta) * cE + delta * x)
        x = beta * PE + (1 - beta) * np.maximum(Q, dE)
    return x


def pc_fun(breaks, vals):
    # breaks: (N, m) increasing; vals: (N, m+1); value vals[:, j] on [breaks[j-1], breaks[j])
    def f(t):
        idx = (breaks <= t).sum(axis=1)
        return vals[np.arange(vals.shape[0]), idx]
    return f


def chat(breaks, vals, rho, t):
    # rho * int_0^inf e^{-rho s} c(t+s) ds for piecewise-constant c (exact)
    N, m = breaks.shape
    tot = np.zeros(N)
    # segments: [-inf,b0),[b0,b1),...,[b_{m-1},inf)
    lo = np.concatenate([np.full((N, 1), -np.inf), breaks], axis=1)
    hi = np.concatenate([breaks, np.full((N, 1), np.inf)], axis=1)
    for j in range(m + 1):
        a = np.maximum(lo[:, j], t) - t
        b = np.maximum(hi[:, j], t) - t
        w = np.exp(-rho * a) - np.where(np.isinf(b), 0.0, np.exp(-rho * np.where(np.isinf(b), 0, b)))
        tot += vals[:, j] * w
    return tot


def analytic(par):
    r, lam, beta, V, Q = par["r"], par["lam"], par["beta"], par["V"], par["Q"]
    rho = r + lam
    wb = lam / rho
    M = Q + beta * (V - Q)
    bE, vE, bU, vU = par["bE"], par["vE"], par["bU"], par["vU"]
    pts = np.concatenate([np.zeros((len(r), 1)), bE, bU, par["T0"][:, None] * np.ones((len(r), 1))], axis=1)

    def xF(t):
        G = beta * chat(bU, vU, rho, t) - (1 - beta) * chat(bE, vE, rho, t)
        return wb * M + (1 - wb) * G, G

    x0, _ = xF(np.zeros(len(r)))
    sup = np.zeros(len(r))           # tau = infinity gives 0
    infx = np.full(len(r), np.inf)
    # x_F is monotone between breakpoints, constant after the last one: check breakpoints (both sides)
    for j in range(pts.shape[1]):
        for eps in (0.0, 1e-9):
            t = pts[:, j] + eps
            xt, G = xF(t)
            sup = np.maximum(sup, np.exp(-rho * t) * (Q - xt))
            infx = np.minimum(infx, xt)
    # tail value (after all breakpoints)
    xt, _ = xF(np.full(len(r), 1e3))
    infx = np.minimum(infx, xt)
    return x0, x0 + sup, infx


def draw(N, T0max=4.0, grid=0.05):
    r = rng.uniform(0.05, 1.5, N)
    lam = np.where(rng.random(N) < 0.2, 0.0, rng.uniform(0.0, 2.0, N))
    beta = np.where(rng.random(N) < 0.15, 0.0, rng.uniform(0.0, 0.95, N))
    V = rng.uniform(0.2, 3.0, N)
    T0 = np.round(rng.uniform(0.5, T0max, N) / grid) * grid
    m = 3
    def pcs():
        br = np.sort(np.round(rng.uniform(0, 1, (N, m)) * T0[:, None] / grid) * grid, axis=1)
        vals = rng.uniform(0, 3, (N, m + 1)) * (rng.random((N, m + 1)) < 0.75)
        return br, vals
    bE, vE = pcs()
    bU, vU = pcs()
    # breakpoints <= T0, so costs are constant after T0
    par = dict(r=r, lam=lam, beta=beta, V=V, T0=T0, bE=bE, vE=vE, bU=bU, vU=vU)
    # Q: centre draws near the exact no-exit threshold so both regimes are well represented
    par["Q"] = np.zeros(N)
    return par


def set_Q(par, mode):
    N = len(par["r"])
    r, lam, beta, V = par["r"], par["lam"], par["beta"], par["V"]
    # Qbar = inf_t [lam beta V + r G(t)] / (r + lam beta): compute with Q-free G
    rho = r + lam
    pts = np.concatenate([np.zeros((N, 1)), par["bE"], par["bU"]], axis=1)
    infG = np.full(N, np.inf)
    for j in range(pts.shape[1]):
        for eps in (0.0, 1e-9):
            t = pts[:, j] + eps
            G = beta * chat(par["bU"], par["vU"], rho, t) - (1 - beta) * chat(par["bE"], par["vE"], rho, t)
            infG = np.minimum(infG, G)
    G = beta * chat(par["bU"], par["vU"], rho, np.full(N, 1e3)) - (1 - beta) * chat(par["bE"], par["vE"], rho, np.full(N, 1e3))
    infG = np.minimum(infG, G)
    Qbar = (lam * beta * V + r * infG) / (r + lam * beta)
    if mode == "below":
        Q = Qbar - rng.uniform(0.0, 2.0, N)
    elif mode == "above":
        Q = Qbar + rng.uniform(0.0, 2.0, N)
    elif mode == "at":
        Q = Qbar.copy()
    else:
        Q = Qbar + rng.uniform(-1.5, 1.5, N)
    Q = np.minimum(Q, V - 1e-3)   # memo assumes Q < V
    par["Q"] = Q
    par["cE"] = pc_fun(par["bE"], par["vE"])
    par["cU"] = pc_fun(par["bU"], par["vU"])
    return Qbar


def run_block(N, mode, D=0.002):
    par = draw(N)
    Qbar = set_Q(par, mode)
    xa = backward(par, D)
    xb = backward(par, D / 2)
    xR = 2 * xb - xa            # Richardson extrapolation to D -> 0
    form, exact, infx = analytic(par)
    nobind = par["Q"] <= infx + 1e-12
    return dict(par=par, Qbar=Qbar, xR=xR, xb=xb, form=form, exact=exact, nobind=nobind, infx=infx)


print("=== Prop 6: random draws (piecewise-constant c_E(t), c_U(t), lambda=0 and beta=0 included) ===")
tot = 0
for mode in ("below", "above", "mixed", "at"):
    res = run_block(1500, mode)
    p = res["par"]
    nb = res["nobind"]
    tot += len(nb)
    e_exact = np.max(np.abs(res["xR"] - res["exact"]))
    e_form_nb = np.max(np.abs(res["xR"][nb] - res["form"][nb])) if nb.any() else np.nan
    # condition check: Q <= Qbar  <=> Q <= inf x_F
    agree = np.mean((p["Q"] <= res["Qbar"] + 1e-9) == (p["Q"] <= res["infx"] + 1e-9))
    gap_bind = res["exact"][~nb] - res["form"][~nb]
    print(f"mode={mode:6s} draws={len(nb)} no-bind={nb.sum():4d}  max|x_D - exact P*|={e_exact:.2e}  "
          f"max|x_D - formula| (no-bind)={e_form_nb:.2e}  Qbar-test agrees with inf x_F: {agree:.3f}  "
          f"min(P* - formula | binds)={gap_bind.min() if gap_bind.size else np.nan:.3e}")
print("total draws", tot)

# Naive condition (exit does not bind at t=0 only: Q <= x_F(0)) is NOT sufficient
print("\n=== Counterexample: exit binds later although Q <= x_F(0) ===")
N = 1
par = dict(r=np.array([0.5]), lam=np.array([0.0]), beta=np.array([0.0]), V=np.array([1.0]), T0=np.array([2.0]),
           bE=np.array([[2.0]]), vE=np.array([[0.0, 2.0]]), bU=np.array([[2.0]]), vU=np.array([[0.0, 0.0]]))
par["Q"] = np.array([-1.0])
par["cE"] = pc_fun(par["bE"], par["vE"]); par["cU"] = pc_fun(par["bU"], par["vU"])
form, exact, infx = analytic(par)
xa = backward(par, 0.001); xb = backward(par, 0.0005)
print("beta=0, lam=0, r=0.5, c_E=0 on [0,2), c_E=2 after, c_U=0, Q=-1:")
print(f"  x_F(0)={form[0]:.4f} (>= Q, naive test passes), inf_t x_F(t)={infx[0]:.4f} (< Q)")
print(f"  formula={form[0]:.4f}  exact sup-stopping={exact[0]:.4f}  backward induction (Richardson)={2*xb[0]-xa[0]:.4f}")

# Edge cases: lambda=0 & c=0 (Prop 1 nesting), r small, beta near 1
print("\n=== Edge cases ===")
for (r, lam, beta, V, Q, cE, cU) in [(0.3, 0.0, 0.5, 1.0, -0.4, 0.0, 0.0), (0.3, 0.0, 0.5, 1.0, 0.4, 0.0, 0.0),
                                     (0.3, 1.0, 0.5, 1.0, 0.2, 0.0, 0.0), (0.3, 1.0, 0.5, 1.0, 0.9, 0.0, 0.0),
                                     (0.05, 2.0, 0.9, 2.0, -1.0, 1.0, 0.5), (1.0, 0.5, 0.0, 1.0, -0.5, 0.5, 2.0),
                                     (1.0, 0.5, 0.0, 1.0, -0.6, 0.5, 2.0)]:
    par = dict(r=np.array([r]), lam=np.array([lam]), beta=np.array([beta]), V=np.array([V]), T0=np.array([1.0]),
               bE=np.array([[1.0]]), vE=np.array([[cE, cE]]), bU=np.array([[1.0]]), vU=np.array([[cU, cU]]))
    par["Q"] = np.array([Q]); par["cE"] = pc_fun(par["bE"], par["vE"]); par["cU"] = pc_fun(par["bU"], par["vU"])
    form, exact, infx = analytic(par)
    xa = backward(par, 0.002); xb = backward(par, 0.001)
    wb = lam / (r + lam)
    prop1 = max(Q, wb * (Q + beta * (V - Q)) + (1 - wb) * (beta * cU - (1 - beta) * cE))
    print(f"r={r} lam={lam} beta={beta} V={V} Q={Q} cE={cE} cU={cU}: BI={2*xb[0]-xa[0]:.5f} "
          f"exact={exact[0]:.5f} max(Q,formula)={prop1:.5f} formula={form[0]:.5f}")

# Convergence where exit binds: error vs D (no extrapolation), same draws
print("\n=== Convergence in D when the exit floor binds somewhere (mode=above, 600 draws) ===")
par = draw(600)
set_Q(par, "above")
form, exact, infx = analytic(par)
for D in (0.004, 0.002, 0.001, 0.0005, 0.00025):
    x = backward(par, D)
    err = np.abs(x - exact)
    print(f"D={D:.5f}: max|x_D - exact P*|={err.max():.3e}  mean={err.mean():.3e}  "
          f"max over beta<0.8: {err[par['beta'] < 0.8].max():.3e}")
