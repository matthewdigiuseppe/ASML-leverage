# Brute-force check of the minimal model in notes/minimal/design.md (report: notes/minimal/verify.md).
# Run: python3 -I minimal_model_check.py   (numpy only; about 75 seconds)
#
# Every solver below works by backward induction from the primitives (payoffs at terminal nodes,
# each player's choice at each node). No solver uses the formula it is checked against.
#
#   Part 1  Core model: R1 (commitment), R1' (no commitment), R2 (u, and u threatened),
#           R3 (single bundle; demands issued one at a time).
#   Part 2  Add-on A: random-proposer bargaining with per-round standoff costs and short rounds;
#           four timings of the stoppage decision; exit option; rupture risk.
#   Part 3  Add-on B: two-period control demand; variants in which the period-1 threat could
#           instead extract concessions worth alpha per unit of Europe's cost.
#
# Tie handling: the core and add-on B solvers enumerate every pure-strategy SPE outcome that
# differs only in how an indifferent player breaks a tie (except Europe's acceptance of an offer
# that exactly meets its reservation value, which must be "accept" in any SPE with a continuum of
# offers). Claims are checked against the full outcome set.
import itertools
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(20261029)
TOL = 1e-12
FAIL = []


def report(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


# ======================================================================================
# Part 1. Core model
# ======================================================================================
def core_spe(c, k, V, u=0.0, commit=True, e=0.0, u_threat=False):
    """All pure SPE outcomes of the one-round game.
    Returns a set of (accepted, t, Europe payoff, US payoff, switched).
    Europe's payoffs: stay keeps u (unless u is withdrawn) and loses k if k is withdrawn;
    switching gives c and loses k (k is lost on switching by definition). US: -t if Europe stays
    after accepting, -V if Europe switches, -e per withdrawal executed against a Europe that stays.
    commit=True: the threat (withdraw k, and u too if u_threat) is executed after a rejection.
    commit=False: after a rejection Washington chooses whether to withdraw k (never u)."""
    outcomes = set()
    # --- post-rejection subgame: list of (Europe payoff, US payoff, switched) over SPE tie choices
    post = []
    w_options = [1] if commit else [0, 1]
    w_res = []  # for each w: list of (E, U, switched) over Europe's tie choices
    for w in w_options:
        uw = 0.0 if (commit and u_threat) else u
        stay = uw - k * w
        sw = uw + c - k
        res = []
        if stay >= sw - TOL:
            res.append((stay, -e * w, False))
        if sw >= stay - TOL:
            res.append((sw, -V, True))
        w_res.append(res)
    if commit:
        post = w_res[0]
    else:
        # Washington chooses w to maximize its payoff given Europe's (tie) response; enumerate
        # Europe's tie choice per w, then Washington's tie choice.
        for r0 in w_res[0]:
            for r1 in w_res[1]:
                best = max(r0[1], r1[1])
                if r0[1] >= best - TOL:
                    post.append(r0)
                if r1[1] >= best - TOL:
                    post.append(r1)
    for (RE, RU, sw) in post:
        tmin = RE - u  # Europe accepts t iff u + t >= RE (accept when indifferent)
        acc_U = -tmin
        if acc_U >= RU - TOL:
            outcomes.add((True, tmin, u + tmin, acc_U, False))
        if RU >= acc_U - TOL:
            outcomes.add((False, None, RE, RU, sw))
    return outcomes


def core_grid(c, k, V, commit=True, step=0.125, tmax=40.0):
    """Grid brute force (offers on a lattice); Europe accepts iff weakly better; Washington takes
    the best offer, breaking ties toward acceptance. Commitment case and the no-commitment case
    with e>0 or c>0 (unique continuation)."""
    # rejection continuation (unique when c > 0 or commit): computed by comparing branches
    if commit:
        stay, sw = -k, c - k
        RE, RU = (stay, 0.0) if stay >= sw else (sw, -V)
    else:
        # w = 0: stay 0 vs switch c-k; w = 1: stay -k vs switch c-k; Washington picks w
        cands = []
        for w in (0, 1):
            stay, sw = -k * w, c - k
            cands.append((stay, 0.0) if stay >= sw else (sw, -V))
        RE, RU = cands[0] if cands[0][1] >= cands[1][1] else cands[1]
    grid = np.arange(-tmax, tmax + step / 2, step)
    accepted = grid >= RE
    Upay = np.where(accepted, -grid, RU)
    j = int(np.argmax(Upay + 1e-9 * accepted))
    return bool(accepted[j]), float(grid[j]), float(np.where(accepted, grid, RE)[j])


print("Part 1: core model")

# ---- R1, R1', R2 on random continuous draws and on a dyadic lattice (exact ties)
n_cont, n_lat = 20000, 20000
mism = {"R1": 0, "R1p": 0, "R2": 0, "R2u": 0, "grid": 0}
multi = {"R1_qV": 0, "R1p_c0e0": 0, "other": 0}
counts = {"squeeze": 0, "pay": 0, "switch": 0}


def R(x):
    return round(float(x) + 0.0, 9)


def summarize(outs, u=0.0):
    """Payoff-relevant outcome: (Europe stays?, Europe payoff net of u, US payoff).
    A rejection after which Europe stays is payoff-equivalent to an accepted transfer."""
    s = set()
    for (acc, t, E, U, sw) in outs:
        s.add((not sw, R(E - u), R(U)))
    return s


def claim_R1(c, k, V):
    q = c - k
    out = set()
    if q <= V:
        out.add((True, R(q), R(-q)))
    if q >= V:
        out.add((False, R(q), R(-V)))
    return out


def claim_R1p(c, k, V):
    q = c - k
    t = max(0.0, q)
    out = set()
    if q <= V:
        out.add((True, R(t), R(-t)))
    if q >= V:
        out.add((False, R(q), R(-V)))
    return out


for it in range(n_cont + n_lat):
    if it < n_cont:
        c = rng.uniform(0, 5) if rng.random() > 0.05 else 0.0
        k = rng.uniform(0, 5) if rng.random() > 0.05 else 0.0
        V = rng.uniform(0.01, 5)
        if rng.random() < 0.05 and c - k > 0:
            V = c - k  # c - k = V tie
        u = rng.uniform(0, 5)
        e = 0.0 if rng.random() < 0.3 else rng.uniform(0, 1)
    else:
        c = rng.integers(0, 9) / 2
        k = rng.integers(0, 9) / 2
        V = rng.integers(1, 9) / 2
        u = rng.integers(0, 9) / 2
        e = 0.0 if rng.random() < 0.5 else rng.integers(1, 4) / 4
    q = c - k
    # R1 (commitment): accepted transfers must equal q
    o1 = core_spe(c, k, V, u=0.0, commit=True)
    s1 = summarize(o1)
    if s1 != claim_R1(c, k, V):
        mism["R1"] += 1
    for (acc, t, E, U, sw) in o1:
        if acc and abs(t - q) > 1e-9:
            mism["R1"] += 1
    if len(s1) > 1:
        if q == V:
            multi["R1_qV"] += 1
        else:
            multi["other"] += 1
    if q < V:
        counts["squeeze" if q < 0 else "pay"] += 1
    else:
        counts["switch"] += 1
    # R1' (no commitment)
    o1p = core_spe(c, k, V, u=0.0, commit=False, e=e)
    s1p = summarize(o1p)
    if c == 0 and e == 0 and k > 0 and q < V:
        # knife edge: Washington indifferent about withdrawing; Europe's payoff in {-k, 0}
        if s1p == {(True, R(0.0), R(0.0)), (True, R(-k), R(k))}:
            multi["R1p_c0e0"] += 1
        else:
            mism["R1p"] += 1
    elif s1p != claim_R1p(c, k, V):
        mism["R1p"] += 1
    # R2: u in payoffs, not threatened: outcomes unchanged (Europe's payoff net of u)
    o2 = core_spe(c, k, V, u=u, commit=True)
    if summarize(o2, u=u) != s1:
        mism["R2"] += 1
    # R2 scope: if Washington can also commit to withdrawing u, t* = q - u
    o2u = core_spe(c, k, V, u=u, commit=True, u_threat=True)
    s2u = summarize(o2u)  # Europe's gross payoff
    exp = set()
    if q - u <= V:
        exp.add((True, R(q), R(u - q)))
    if q - u >= V:
        exp.add((False, R(q), R(-V)))
    if s2u != exp:
        mism["R2u"] += 1
    for (acc, t, E, U, sw) in o2u:
        if acc and abs(t - (q - u)) > 1e-9:
            mism["R2u"] += 1
    # Grid brute force on the lattice draws (ties exact)
    if it >= n_cont and (q != V):
        acc, t, _ = core_grid(c, k, V, commit=True)
        if q < V and (not acc or abs(t - q) > 1e-12):
            mism["grid"] += 1
        if (c > 0 or e > 0) and q < V:
            acc, t, _ = core_grid(c, k, V, commit=False)
            if not acc or abs(t - max(0.0, q)) > 1e-12:
                mism["grid"] += 1

report("R1: accepted t* = c-k if c-k<V; switch if c-k>V; Europe's payoff c-k in every SPE",
       mism["R1"] == 0,
       f"({n_cont + n_lat} draws: squeeze {counts['squeeze']}, pay {counts['pay']}, "
       f"switch or tie {counts['switch']}; payoff-distinct SPE outcomes only at c-k=V: {multi['R1_qV']}, "
       f"elsewhere: {multi['other']})")
report("R1': t* = max{0,c-k} without commitment", mism["R1p"] == 0,
       f"(knife edge c=0, e=0, k>0, where SPE give Europe 0 or -k: {multi['R1p_c0e0']} draws)")
report("R2: t* independent of u when u is not threatened", mism["R2"] == 0)
report("R2 scope: if Washington can commit to withdrawing u too, t* = c-k-u", mism["R2u"] == 0)
report("R1/R1' grid brute force on lattice draws", mism["grid"] == 0)

# Hand-picked edge cases for the core
edge = [
    # (c, k, V, label)
    (0.0, 2.0, 1.0, "c=0"),
    (0.0, 0.0, 1.0, "c=k=0"),
    (3.0, 1.0, 2.0, "c-k=V"),
    (2.0, 2.0, 1.0, "c-k=0"),
    (4.0, 1.0, 1.0, "c-k>V"),
    (1.0, 3.0, 0.5, "squeeze with V small"),
]
print("  edge cases (c, k, V): SPE outcomes (stays, E, U) with commitment | without (e=0)")
for c, k, V, lab in edge:
    s1 = sorted(summarize(core_spe(c, k, V, commit=True)))
    s1p = sorted(summarize(core_spe(c, k, V, commit=False, e=0.0)))
    print(f"    {lab:22s} {s1} | {s1p}")

# ---- R3: single bundle (acceptance rule; Washington's optimal bundle)
mis3 = 0
mis3t = 0
n3 = 4000
for it in range(n3):
    n = rng.integers(1, 7)
    if it % 2 == 0:
        c, k = rng.uniform(0, 3), rng.uniform(0, 6)
        d = rng.uniform(0, 2, n)
    else:
        c, k = rng.integers(0, 7) / 2, rng.integers(0, 13) / 2
        d = rng.integers(0, 5, n) / 2
    V = 10.0
    q = c - k
    # rejection continuation from primitives (commitment): stay -k vs switch c-k
    RE = max(-k, c - k)
    for S in itertools.product([0, 1], repeat=n):
        S = np.array(S, bool)
        D = float(d[S].sum())
        acc = (-D) >= RE - TOL  # t = 0
        claim = D <= k - c + TOL
        if acc != claim:
            mis3 += 1
        # with a transfer t attached: Europe accepts iff t - D >= rejection payoff
        t = rng.uniform(-2, 2)
        if ((t - D) >= RE - TOL) != (t - D >= q - TOL):
            mis3t += 1
report("R3: Europe accepts bundle S (no transfer) iff sum d_i <= k-c", mis3 == 0,
       f"({n3} draws, all subsets)")
report("R3 with a transfer t: accept iff t - sum d_i >= c-k", mis3t == 0)


# ---- R3 robustness: demands issued one at a time, each backed by the same (unspent) threat
def seq_demands(d, c, k, V, tieE_accept=True, tieU_issue=False):
    """Sequential ultimatums, sunk demands valued equally by both; after a refusal the threat
    is executed and Europe switches (or stays at c=0), game ends. Washington may stop any time.
    Returns (Europe payoff, US payoff)."""
    n = len(d)
    memo = {}

    def val(mask):
        if mask in memo:
            return memo[mask]
        T = sum(d[i] for i in range(n) if mask >> i & 1)
        stopE, stopU = -T, T
        bestE, bestU = stopE, stopU
        for i in range(n):
            if mask >> i & 1:
                continue
            aE, aU = val(mask | 1 << i)
            # refusal: k withdrawn, concessions sunk; Europe chooses stay (-k-T) or switch (c-k-T)
            rE = max(-k - T, c - k - T)
            rU = (T if -k - T >= c - k - T else T - V)
            acc = aE > rE + TOL or (abs(aE - rE) <= TOL and tieE_accept)
            oE, oU = (aE, aU) if acc else (rE, rU)
            if oU > bestU + TOL or (abs(oU - bestU) <= TOL and tieU_issue):
                bestE, bestU = oE, oU
        memo[mask] = (bestE, bestU)
        return memo[mask]

    return val(0)


viol_seq = 0
ratchet_ok = 0
strictly_less = 0
nseq = 1500
for it in range(nseq):
    n = int(rng.integers(1, 6))
    if it % 2 == 0:
        c, k = rng.uniform(0, 2), rng.uniform(0, 6)
        d = list(rng.uniform(0, 2, n))
    else:
        c, k = rng.integers(0, 5) / 2, rng.integers(0, 13) / 2
        d = list(rng.integers(0, 5, n) / 2)
    V = 20.0
    single = max(sum(dd for dd, s in zip(d, S) if s)
                 for S in itertools.product([0, 1], repeat=n)
                 if sum(dd for dd, s in zip(d, S) if s) <= k - c + TOL) if k - c >= 0 else 0.0
    for tE in (True, False):
        for tU in (True, False):
            E, U = seq_demands(d, c, k, V, tE, tU)
            if -E > max(k - c, 0) + 1e-9:
                viol_seq += 1
            if U > single + 1e-9:
                viol_seq += 1
    E, U = seq_demands(d, c, k, V)
    if U < single - 1e-9:
        strictly_less += 1
# identical demands: Washington obtains n mod (b+1) of them, b = floor((k-c)/tau)
for n in range(1, 8):
    for gap in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.5]:
        E, U = seq_demands([1.0] * n, 0.0, gap, 20.0)
        b = int(np.floor(gap))
        if abs(U - (n % (b + 1))) < 1e-9:
            ratchet_ok += 1
report("R3 sequential: Europe's total loss <= k-c in every SPE (all tie rules)", viol_seq == 0,
       f"({nseq} draws; Washington strictly below the single-bundle value in {strictly_less})")
report("R3 sequential, identical sunk demands of cost 1: Washington gets n mod (b+1)",
       ratchet_ok == 49, f"({ratchet_ok}/49 cases)")


# ======================================================================================
# Part 2. Add-on A: standoff in random-proposer bargaining
# ======================================================================================
def solve_A(p, timing, dt, scale="flow", yt_tie_stop=False, horizon=40.0):
    """Finite-horizon backward induction (unique SPE given tie rules), vectorized over draws.
    p: dict of arrays beta, x, y, q, V, r, lam. Agreement on a permanent transfer P gives (P, -P).
    Round costs during a stoppage: (1-delta)*x for the US and (1-delta)*y for Europe if
    scale == "flow" (x, y are flow rates in payoff units); x and y per round if scale == "round".
    After a rejection: if the US proposed, Europe may exit (q, -V); otherwise rupture with prob.
    mu gives (q, -V); otherwise the round's disagreement flows accrue and play continues.
    timing: 'none' (no stoppage), 'commit' (stoppage in every round until agreement),
    'before' (chosen each round before the proposer is drawn), 'proposer' (after the proposer is
    drawn, before offers), 'after' (chosen by Europe after an offer is rejected)."""
    beta, x, y, q, V, r, lam = (p[s] for s in ("beta", "x", "y", "q", "V", "r", "lam"))
    delta = np.exp(-r * dt)
    mu = 1 - np.exp(-lam * dt)
    cx = (1 - delta) * x if scale == "flow" else x
    cy = (1 - delta) * y if scale == "flow" else y
    N = int(np.ceil(horizon / (np.min(r + lam) * dt)))
    e1 = np.zeros_like(beta)
    u1 = np.zeros_like(beta)

    def branches(s, e1, u1):
        # Europe proposes; US rejects -> disagreement
        dU = mu * (-V) + (1 - mu) * (-cx * s + delta * u1)
        dEE = mu * q + (1 - mu) * (-cy * s + delta * e1)
        agreeE = -dU >= dEE
        eE = np.where(agreeE, -dU, dEE)
        uE = dU
        # US proposes; Europe rejects -> exit or disagreement
        dE = mu * q + (1 - mu) * (-cy * s + delta * e1)
        rE = np.maximum(q, dE)
        dUU = np.where(q > dE, -V, mu * (-V) + (1 - mu) * (-cx * s + delta * u1))
        agreeU = -rE >= dUU
        eU = rE
        uU = np.where(agreeU, -rE, dUU)
        return eE, uE, eU, uU, dEE, dE

    zero = np.zeros_like(beta)
    one = np.ones_like(beta)
    for _ in range(N):
        if timing in ("none", "commit", "before", "proposer"):
            b0 = branches(zero, e1, u1)
            b1 = branches(one, e1, u1)
            if timing == "none":
                eE, uE, eU, uU = b0[:4]
            elif timing == "commit":
                eE, uE, eU, uU = b1[:4]
            elif timing == "before":
                v0 = beta * b0[0] + (1 - beta) * b0[2]
                v1 = beta * b1[0] + (1 - beta) * b1[2]
                pick = v1 > v0
                eE, uE, eU, uU = (np.where(pick, b1[i], b0[i]) for i in range(4))
            else:  # proposer known
                pE = b1[0] > b0[0]
                pU = b1[2] > b0[2]
                eE, uE = np.where(pE, b1[0], b0[0]), np.where(pE, b1[1], b0[1])
                eU, uU = np.where(pU, b1[2], b0[2]), np.where(pU, b1[3], b0[3])
        else:  # 'after': Europe sets the stoppage after a rejection, for that round only
            # Europe's disagreement value with s = 0 or 1; it picks the larger (tie rule param)
            dEE0 = mu * q + (1 - mu) * (delta * e1)
            dEE1 = mu * q + (1 - mu) * (-cy + delta * e1)
            sE = (dEE1 > dEE0) | (yt_tie_stop & (dEE1 == dEE0))
            sE = sE.astype(float)
            dU = mu * (-V) + (1 - mu) * (-cx * sE + delta * u1)
            dEE = np.where(sE > 0, dEE1, dEE0)
            agreeE = -dU >= dEE
            eE = np.where(agreeE, -dU, dEE)
            uE = dU
            dE = dEE  # same continuation after the US's offer is rejected
            sU = sE
            rE = np.maximum(q, dE)
            dUU = np.where(q > dE, -V, mu * (-V) + (1 - mu) * (-cx * sU + delta * u1))
            agreeU = -rE >= dUU
            eU = rE
            uU = np.where(agreeU, -rE, dUU)
        e1 = beta * eE + (1 - beta) * eU
        u1 = beta * uE + (1 - beta) * uU
    return e1, u1


def draw_A(D, exit_binding_frac=0.25, lam_pos_frac=0.0):
    p = {}
    p["beta"] = rng.uniform(0, 1, D)
    m = rng.random(D)
    p["beta"][m < 0.08] = 0.0
    p["beta"][(m >= 0.08) & (m < 0.16)] = 1.0
    p["x"] = rng.uniform(0, 3, D)
    p["x"][rng.random(D) < 0.05] = 0.0
    p["y"] = rng.uniform(0, 3, D)
    p["y"][rng.random(D) < 0.05] = 0.0
    p["V"] = rng.uniform(0.5, 5, D)
    p["q"] = -rng.uniform(0, 3, D)
    p["q"][rng.random(D) < 0.1] = 0.0
    sel = rng.random(D) < exit_binding_frac
    p["q"][sel] = rng.uniform(0, 1.5, sel.sum())
    p["q"] = np.minimum(p["q"], p["V"] - 0.1)
    p["r"] = rng.uniform(0.5, 2, D)
    p["lam"] = np.where(rng.random(D) < lam_pos_frac, rng.uniform(0.1, 2, D), 0.0)
    # exact ties beta x = (1-beta) y in a few draws
    t = (rng.random(D) < 0.05) & (p["beta"] > 0) & (p["beta"] < 1)
    b = p["beta"]
    hi = t & (b >= 0.5)
    lo = t & (b < 0.5)
    p["x"][hi] = (1 - b[hi]) * p["y"][hi] / b[hi]
    p["y"][lo] = b[lo] * p["x"][lo] / (1 - b[lo])
    return p


print("Part 2: add-on A (standoff)")
NOEXIT = -1e12  # "exit not attractive" in its strongest form: Europe has no usable exit option

# (A1) No usable exit option, no rupture: exact for every round length
D = 3000
pA = draw_A(D, exit_binding_frac=0.0, lam_pos_frac=0.0)
pA["q"] = np.full(D, NOEXIT)
G = pA["beta"] * pA["x"] - (1 - pA["beta"]) * pA["y"]
tie = np.abs(G) < 1e-12
for dt in (0.1, 0.01):
    vN, _ = solve_A(pA, "none", dt)
    vC, _ = solve_A(pA, "commit", dt)
    gain = vC - vN
    errC = np.max(np.abs(vC - G))
    sign_ok = np.all((gain > 1e-12) == (G > 1e-12)) and np.all(np.abs(gain[tie]) < 1e-12)
    report(f"A1 (no exit, dt={dt}): take with standoff = beta x-(1-beta) y exactly; "
           "standoff raises take iff beta x > (1-beta) y", bool(sign_ok) and errC < 1e-9
           and np.max(np.abs(vN)) < 1e-12,
           f"({D} draws, {int((gain > 1e-12).sum())} with a gain, {int(tie.sum())} exact ties with "
           f"gain 0, {int((pA['beta'] == 0).sum())} with beta=0, {int((pA['beta'] == 1).sum())} with "
           f"beta=1; max error {errC:.1e})")
b0 = pA["beta"] == 0
report("A1: beta = 0 gives no gain (gain = -y <= 0 if committed)",
       bool(np.all(gain[b0] <= 1e-12)), f"({b0.sum()} draws)")
pV = dict(pA)
pV["V"] = pA["V"] + 3.0
vC2, _ = solve_A(pV, "commit", 0.01)
report("A1: V does not affect the take (no rupture)", bool(np.max(np.abs(vC2 - vC)) < 1e-12))
vNr, _ = solve_A(pA, "none", 0.01, scale="round")
vCr, _ = solve_A(pA, "commit", 0.01, scale="round")
d0 = 1 - np.exp(-pA["r"] * 0.01)
report("A1: costs fixed per round (not per unit time): take = (beta x-(1-beta)y)/(1-delta), "
       "same sign condition",
       bool(np.all(((vCr - vNr) > 1e-9) == (G > 1e-9)) and
            np.max(np.abs(vCr - G / d0) / (1 + np.abs(G / d0))) < 1e-9))

# Timings of the stoppage decision (no exit, no rupture)
dt = 0.01
vB, _ = solve_A(pA, "before", dt)
vP, _ = solve_A(pA, "proposer", dt)
vAf, _ = solve_A(pA, "after", dt)
vAf1, _ = solve_A(pA, "after", dt, yt_tie_stop=True)
eB = np.max(np.abs(vB - np.maximum(0, G)))
report("A timing: chosen each round before the proposer is drawn: take max{0, beta x-(1-beta)y}",
       bool(eB < 1e-9), f"(max err {eB:.1e}; same as a once-and-for-all commitment, "
                        "so no long-run commitment is needed)")
ypos = pA["y"] > 0
report("A timing: Europe can lift the stoppage after a rejection (y>0): never used, no gain",
       bool(np.max(np.abs(vAf[ypos] - vN[ypos])) < 1e-12),
       f"({ypos.sum()} draws, max |gain| {np.max(np.abs(vAf[ypos] - vN[ypos])):.1e})")
y0 = ~ypos
report("A timing: lift after a rejection with y = 0 and ties broken toward stopping: take beta x",
       bool(np.max(np.abs(vAf1[y0] - pA["beta"][y0] * pA["x"][y0])) < 1e-9) if y0.any() else True,
       f"({y0.sum()} draws)")
errP = np.max(np.abs(vP - pA["beta"] * pA["x"]))
report("A timing: chosen after the proposer is drawn, before offers: take = beta x whatever y",
       bool(errP < 1e-9),
       f"(max err {errP:.1e}; gain in {int((vP - vN > 1e-9).sum())} draws, of which "
       f"{int(((vP - vN > 1e-9) & (G <= 0)).sum())} have beta x <= (1-beta) y)")

# (A2) Exit option q present (no rupture). Frequent-offer limit: no standoff max{q,0},
# standoff max{q, G}. Finite-dt values converge at rate O(dt/(1-beta)).
pE = draw_A(3000, exit_binding_frac=0.3, lam_pos_frac=0.0)
pE["beta"] = np.minimum(pE["beta"], 0.9)
GE = pE["beta"] * pE["x"] - (1 - pE["beta"]) * pE["y"]
limN = np.maximum(pE["q"], 0)
limC = np.maximum(pE["q"], GE)
res = {}
for dt in (0.02, 0.005, 0.00125):
    vN, _ = solve_A(pE, "none", dt)
    vC, _ = solve_A(pE, "commit", dt)
    res[dt] = (vN, vC)
    print(f"  A2 dt={dt}: max |value - limit| no standoff {np.max(np.abs(vN - limN)):.4f}, "
          f"standoff {np.max(np.abs(vC - limC)):.4f}")
# Richardson extrapolation (first-order error): L ~ (4 v(h/4) - v(h)) / 3
vN = (4 * res[0.00125][0] - res[0.005][0]) / 3
vC = (4 * res[0.00125][1] - res[0.005][1]) / 3
print(f"  A2 extrapolated: max |value - limit| no standoff {np.max(np.abs(vN - limN)):.4f}, "
      f"standoff {np.max(np.abs(vC - limC)):.4f}")
nb = pE["q"] <= 0
m = np.abs(GE) > 0.05
ok_nb = np.all(((vC - vN)[nb & m] > 0.01) == (GE[nb & m] > 0))
report("A2 (exit not attractive, q <= 0): limit gain iff beta x > (1-beta) y",
       bool(ok_nb) and np.max(np.abs(vC - limC)) < np.max(np.abs(res[0.02][1] - limC)),
       f"({int((nb & m).sum())} draws with |beta x-(1-beta)y| > 0.05, classified on extrapolated values)")
eb = ~nb
m2 = np.abs(GE - pE["q"]) > 0.05
ok_eb = np.all(((vC - vN)[eb & m2] > 0.01) == (GE[eb & m2] > pE["q"][eb & m2]))
cnt = int((eb & m2 & (GE > 0) & (GE < pE["q"])).sum())
report("A2 (exit attractive, q > 0): gain iff beta x-(1-beta)y > q; the sign condition is "
       "necessary, not sufficient", bool(ok_eb),
       f"({int((eb & m2).sum())} draws; condition holds but no gain in {cnt})")

# (A3) Rupture risk lambda > 0 (paper's Corollary 5 with t_U = 0, h = 0)
pR = draw_A(1500, exit_binding_frac=0.25, lam_pos_frac=1.0)
pR["beta"] = np.minimum(pR["beta"], 0.9)
GR = pR["beta"] * pR["x"] - (1 - pR["beta"]) * pR["y"]
psi = pR["lam"] / (pR["lam"] + pR["r"])
M = pR["q"] + pR["beta"] * (pR["V"] - pR["q"])
xF0 = psi * M
limN = np.maximum(pR["q"], xF0)
limC = np.maximum(pR["q"], xF0 + (1 - psi) * GR)
errs = []
for dt in (0.02, 0.005, 0.00125):
    vN, _ = solve_A(pR, "none", dt)
    vC, _ = solve_A(pR, "commit", dt)
    errs.append(np.max(np.abs(vC - limC)))
nbR = pR["q"] <= xF0
mR = np.abs((1 - psi) * GR) > 0.05
ok = np.all(((vC - vN)[nbR & mR] > 0.005) == (GR[nbR & mR] > 0))
report("A3 rupture risk: limit gain (1-psi)[beta x-(1-beta)y]^+ when exit not attractive; "
       "same sign condition", bool(ok) and errs[2] < errs[0],
       f"(max |disc - limit| {errs[0]:.3f}, {errs[1]:.3f}, {errs[2]:.3f} at dt=0.02, 0.005, "
       f"0.00125; {int((nbR & mR).sum())} draws classified)")


# ======================================================================================
# Part 3. Add-on B: control
# ======================================================================================
def stage(alt_stay, alt_switch, V):
    """One period without control and without threats: Washington offers p >= 0, Europe stays
    (alt_stay + p) or switches (alt_switch, costs Washington V). Returns all SPE (E, U) pairs."""
    need = alt_switch - alt_stay  # payment that makes Europe indifferent
    pmin = max(0.0, need)
    res = []
    if -pmin > -V + TOL:
        res.append((alt_stay + pmin, -pmin))
    elif -pmin < -V - TOL:
        res.append((alt_switch if alt_switch >= alt_stay + 0 else alt_stay, -V))
    else:
        res.append((alt_stay + pmin, -pmin))
        res.append((max(alt_switch, alt_stay), -V))
    return res


def solve_B(c1, k1, c2, k2, s, delta, V1, V2, squeeze=False):
    """Returns set of SPE outcomes (demand issued & accepted?, T or None, E, U).
    squeeze=True: without a control demand Washington uses its committed threat in period 1 for
    an ordinary transfer demand (R1), instead of paying max{0, q1}."""
    out = set()
    p2 = stage(0.0, c2 - k2, V2)
    for (E2, U2) in p2:
        # no demand
        if squeeze:
            # R1 with commitment in period 1: Europe's rejection value from primitives
            RE = max(-k1, c1 - k1)
            RU = 0.0 if -k1 >= c1 - k1 else -V1
            nd = []
            if -RE >= RU - TOL:
                nd.append((RE, -RE))
            if RU >= -RE - TOL:
                nd.append((RE, RU))
        else:
            nd = stage(0.0, c1 - k1, V1)
        for (E1, U1) in nd:
            NE, NU = E1 + delta * E2, U1 + delta * U2
            # demand: refusal -> k1 withdrawn in period 1, then the period-1 stage game with
            # Europe's stay payoff -k1 and switch payoff c1 - k1; period 2 unchanged
            for (rE1, rU1) in stage(-k1, c1 - k1, V1):
                RE, RU = rE1 + delta * E2, rU1 + delta * U2
                Tmin = max(0.0, RE + s)  # accept iff T - s >= RE
                acc = -Tmin
                dem = max(acc, RU)
                outs_dem = []
                if acc >= RU - TOL:
                    outs_dem.append((True, round(Tmin, 12), Tmin - s, -Tmin))
                if RU >= acc - TOL:
                    outs_dem.append((False, None, RE, RU))
                for od in outs_dem:
                    if od[3] > NU + TOL:
                        out.add(od)
                    elif od[3] < NU - TOL:
                        out.add(("none", None, round(NE, 12), round(NU, 12)))
                    else:
                        out.add(od)
                        out.add(("none", None, round(NE, 12), round(NU, 12)))
    return out


def solve_B_grid(c1, k1, c2, k2, s, delta, step=1 / 16, Tmax=30.0):
    """Grid brute force for lattice draws (V large): Washington picks T on a grid."""
    q1, q2 = c1 - k1, c2 - k2
    E2 = max(0.0, q2)
    NU = -max(0.0, q1) - delta * E2
    RE = q1 + delta * E2  # refusal value from the stage game (k1 withdrawn, rent c1)
    grid = np.arange(0, Tmax + step / 2, step)
    acc = grid - s >= RE
    U = np.where(acc, -grid, -c1 - delta * E2)
    j = int(np.argmax(U + 1e-9 * acc))
    if U[j] > NU + 1e-12:
        return bool(acc[j]), float(grid[j])
    return "none", None


print("Part 3: add-on B (control)")
misB = 0
tieB = 0
misBgrid = 0
cntB = {"demand": 0, "none": 0}
squeeze_viol = 0
nB = 20000
for it in range(nB):
    lattice = it % 2 == 1
    if lattice:
        c1, k1, c2, k2 = (rng.integers(0, 9) / 2 for _ in range(4))
        s = rng.integers(0, 5) / 2
        delta = [0.0, 0.25, 0.5, 1.0][rng.integers(0, 4)]
    else:
        c1, k1, c2, k2 = rng.uniform(0, 4, 4)
        s = rng.uniform(0, 2) if rng.random() > 0.1 else 0.0
        delta = rng.uniform(0.05, 1)
    V1 = max(c1, c1 - k1) + 1 + rng.uniform(0, 3)
    V2 = max(c2 - k2, 0) + 1 + rng.uniform(0, 3)
    q1, q2 = c1 - k1, c2 - k2
    outs = solve_B(c1, k1, c2, k2, s, delta, V1, V2)
    claim_dem = (q2 > 0) and (k1 - c1 > s)
    Tclaim = max(0.0, delta * q2 + s - (k1 - c1))
    NU = -max(0.0, q1) - delta * max(0.0, q2)  # Washington's payoff without a demand
    if claim_dem and delta > 0:
        cntB["demand"] += 1
        o = next(iter(outs))
        if len(outs) != 1 or o[0] is not True or abs(o[1] - Tclaim) > 1e-9:
            misB += 1
        # joint payoff: control destroys s; without it the payments are pure transfers (sum 0)
        if abs((o[2] + o[3]) - (-s)) > 1e-9:
            misB += 1
    else:
        # no strict gain: "no demand" is an SPE outcome and every SPE outcome gives Washington
        # its no-demand payoff (other outcomes are zero-gain ties)
        cntB["none"] += 1
        if not any(o[0] == "none" for o in outs) or any(abs(o[3] - NU) > 1e-9 for o in outs):
            misB += 1
        if len(outs) > 1:
            tieB += 1
    if lattice:
        g = solve_B_grid(c1, k1, c2, k2, s, delta)
        if claim_dem and delta > 0 and (g[0] is not True or abs(g[1] - Tclaim) > 1e-12):
            misBgrid += 1
        if not (claim_dem and delta > 0) and g[0] != "none":
            misBgrid += 1
    # (control strictly better <=> some demand outcome and no "none" outcome in the SPE set)
    outsq = solve_B(c1, k1, c2, k2, s, delta, V1, V2, squeeze=True)
    if any(o[0] is True for o in outsq) and not any(o[0] == "none" for o in outsq):
        squeeze_viol += 1
report("B: demand issued and accepted iff q2 > 0 and k1 - c1 > s (delta > 0); "
       "T* = max{0, delta q2 + s - (k1-c1)}; joint payoff -s",
       misB == 0, f"({nB} draws: demand {cntB['demand']}, none {cntB['none']}; in {tieB} of the latter "
                  f"Washington is indifferent (zero gain) and other SPE outcomes exist)")
report("B: grid brute force on lattice draws", misBgrid == 0)
report("B variant: if Washington can squeeze in period 1 anyway (R1), control is never strictly "
       "better", squeeze_viol == 0)



# Variant with an opportunity cost of the bite: Washington can instead (or also) demand ordinary
# sunk concessions D from the same threat, worth alpha*D to it (alpha = 1: pure transfers).
# Grid brute force over (control?, T, D); Europe accepts iff its payoff >= refusal payoff
# (k1 withdrawn, period-1 rent c1, period 2 unchanged). Candidate condition derived in the report:
#   control iff (1-alpha) delta q2 > alpha s  and  (1-alpha)(k1-c1) > s.
def B_alpha_grid(c1, k1, c2, k2, s, delta, alpha, step=1 / 8):
    q1, q2 = c1 - k1, c2 - k2
    E2 = max(0.0, q2)
    base_U = -max(0.0, q1) - delta * E2
    refE = q1 + delta * E2
    Dg = np.arange(0, 8 + step / 2, step)
    Tg = np.arange(0, 10 + step / 2, step)
    # no control, concessions D (Washington still pays the period-1 and period-2 rents if any)
    accS = (max(0.0, q1) - Dg) + delta * E2 >= refE  # Europe: pays rent [q1]^+ minus D
    US = np.where(accS, alpha * Dg - max(0.0, q1) - delta * E2, -c1 - delta * E2)
    bestS = US.max()
    TT, DD = np.meshgrid(Tg, Dg)
    accC = TT - s - DD >= refE
    UC = np.where(accC, -TT + alpha * DD, -c1 - delta * E2)
    bestC = UC.max()
    return bestC - max(bestS, base_U)


mis_alpha = 0
n_alpha = 0
for it in range(3000):
    c1, k1, c2, k2 = (rng.integers(0, 9) / 2 for _ in range(4))
    s = rng.integers(0, 5) / 2
    delta = [0.25, 0.5, 1.0][rng.integers(0, 3)]
    alpha = [0.0, 0.25, 0.5, 0.75, 1.0][rng.integers(0, 5)]
    q2 = c2 - k2
    m1 = (1 - alpha) * delta * q2 - alpha * s
    m2 = (1 - alpha) * (k1 - c1) - s
    if abs(m1) < 1e-12 or abs(m2) < 1e-12:
        continue  # boundary: Washington indifferent
    n_alpha += 1
    gain = B_alpha_grid(c1, k1, c2, k2, s, delta, alpha)
    if (gain > 1e-12) != (m1 > 0 and m2 > 0):
        mis_alpha += 1
report("B with opportunity cost alpha: control iff (1-alpha) delta q2 > alpha s and "
       "(1-alpha)(k1-c1) > s", mis_alpha == 0, f"({n_alpha} non-boundary lattice draws)")

# delta = 0 edge case: claim's condition can hold but Washington gains nothing
o = solve_B(0.0, 3.0, 2.0, 0.0, 1.0, 0.0, 10.0, 10.0)
print(f"  edge delta=0, q1=-3, q2=2, s=1: SPE outcomes {sorted(o, key=str)} (claim needs delta>0)")
o = solve_B(0.0, 3.0, 2.0, 0.0, 3.0, 0.5, 10.0, 10.0)
print(f"  edge k1-c1 = s: SPE outcomes {sorted(o, key=str)} (Washington indifferent)")
o = solve_B(0.0, 3.0, 0.0, 0.0, 1.0, 0.5, 10.0, 10.0)
print(f"  edge q2 = 0: SPE outcomes {sorted(o, key=str)}")
o = solve_B(0.0, 3.0, 2.0, 0.0, 0.0, 0.5, 10.0, 10.0)
print(f"  edge s = 0, c1 = 0: SPE outcomes {sorted(o, key=str)} (T* = max(0, 1 - 3) = 0)")

print(f"\nTotal time {time.time() - T0:.1f} s. Failures: {len(FAIL)}")
for f in FAIL:
    print("  ", f)
