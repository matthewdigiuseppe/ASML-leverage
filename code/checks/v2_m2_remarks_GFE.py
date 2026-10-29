# v2 verifier m2: Section 6 remarks.
#   Remark G (gatekeeper, targeted benefit x_h): brute-force rent and slack vs the identities
#   Remark F (firm between jurisdictions): brute-force firm and holder choices
#   Remark E (two-stage ACI, delegated act): Council arithmetic with Council Decision 2025/2427 shares
#            (read from pop_check.py in this directory) and Groseclose-Snyder Phi(0)
import ast
import os
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(11)

# ---------------------------------------------------------------- Remark G
print("=== Remark G: targeted benefit x_h to the gatekeeper ===")
N = 20000
Q = rng.uniform(-3, 3, N)
xh = rng.uniform(0, 3, N)
# edge cases: x_h = 0, Q = 0, x_h = Q
Q[:200] = 0.0; xh[200:400] = 0.0; xh[400:600] = np.abs(Q[400:600]); Q[600:800] = np.round(Q[600:800], 1); xh[600:800] = np.round(xh[600:800], 1)
Q = np.round(Q, 3); xh = np.round(xh, 3)          # on the 1e-3 grid, so the brute force is exact
grid = np.round(np.arange(0, 6.0001, 0.001), 3)
err_rent = err_slack = 0.0
err_transfer = -np.inf
for i in range(N):
    A0, omega = 0.0, 1.0
    cNL = omega - Q[i]                          # so that Q_NL = omega - c_NL
    exit_pay = A0 - cNL + omega                 # x_h withdrawn on exit
    # rent: least staked promise tau >= 0 that makes E align (ties -> align)
    ok = A0 + xh[i] + grid >= exit_pay - 1e-12
    rent_after = grid[np.argmax(ok)]
    ok0 = A0 + grid >= A0 - cNL + omega - 1e-12
    rent_before = grid[np.argmax(ok0)]
    # slack: largest reversible concession T E accepts with tau = 0
    okT = A0 + xh[i] - grid >= exit_pay - 1e-12
    sl_after = grid[okT].max() if okT.any() else 0.0
    okT0 = A0 - grid >= A0 - cNL + omega - 1e-12
    sl_before = grid[okT0].max() if okT0.any() else 0.0
    Qp = max(Q[i], 0.0)
    err_rent = max(err_rent, abs((rent_before - rent_after) - min(xh[i], Qp)))
    err_slack = max(err_slack, abs((sl_after - sl_before) - max(xh[i] - Qp, 0.0)))
    # if x_h is instead a promised increment ABOVE baseline (paid on path), U's outlay is x_h + rent_after
    err_transfer = max(err_transfer, (rent_before) - (xh[i] + rent_after))
print(f"draws {N}: max|rent drop - min(x_h,[Q]^+)| = {err_rent:.1e}; "
      f"max|slack rise - [x_h-[Q]^+]^+| = {err_slack:.1e}")
print(f"if x_h is a transfer above baseline: max saving in U outlay = {err_transfer:.1e} (never positive)")

# ---------------------------------------------------------------- Remark F
print("\n=== Remark F: firm between jurisdictions ===")
M = 200000
y, pC, pB, fF, zeta, Qh = (rng.integers(0, 6, M).astype(float) for _ in range(6))
Qh = Qh - 2.5
ship = (y - fF) >= (-pC - pB)                       # firm's own choice under a licence (tie -> ship)
formula = (y + pC + pB) >= fF
Qeff = Qh - zeta * (~formula)
# holder: exit only if worthwhile; if firm will not ship, compel at cost zeta
exit_val = np.where(ship, Qh, Qh - zeta)
print("firm-choice formula matches enumeration:", bool(np.all(ship == formula)), "| draws", M)
print("effective premium matches holder's exit value:", bool(np.all(exit_val == Qeff)))

# ---------------------------------------------------------------- Remark E
print("\n=== Remark E: Council arithmetic (Council Decision 2025/2427 shares, from pop_check.py) ===")
src = open(os.path.join(HERE, "pop_check.py")).read()
P = None
for node in ast.walk(ast.parse(src)):
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "P":
        P = {kw.arg: kw.value.value for kw in node.value.keywords}
names = list(P)
tot = sum(P.values())
print("members", len(P), " sum of shares", round(tot, 4))


def pop(S):
    return sum(P[k] for k in S)


def qmv_pass(Y):          # Art 16(4) TEU: >=55% of members (15/27) and >=65% pop; blocking minority needs >=4 members
    N_ = [k for k in names if k not in Y]
    if len(Y) < 15:
        return False
    if pop(Y) >= 65 - 1e-9:
        return True
    return len(N_) <= 3   # QMV deemed attained


def blocks(Nset):         # memo rule for the non-yes set
    return len(Nset) >= 13 or (len(Nset) >= 4 and pop(Nset) > 35 + 1e-9)


def rqmv_pass(Y):         # Art 238(2) TFEU (Council not acting on a Commission proposal): >=72% (20/27) and >=65%
    return len(Y) >= 20 and pop(Y) >= 65 - 1e-9


# exhaustive check of the blocking rule on all non-yes sets of size <= 5 and >= 22, random sets in between
cnt = 0; bad = 0
for m in list(range(0, 6)) + list(range(22, 28)):
    for Nset in combinations(names, m):
        Y = [k for k in names if k not in Nset]
        cnt += 1; bad += (qmv_pass(Y) == blocks(Nset))
for _ in range(200000):
    m = rng.integers(6, 22)
    Nset = list(rng.choice(names, m, replace=False))
    Y = [k for k in names if k not in Nset]
    cnt += 1; bad += (qmv_pass(Y) == blocks(Nset))
print(f"stage-1 rule: 'blocked iff |N|>=13 or (|N|>=4 and pop(N)>35)' checked on {cnt} non-yes sets, mismatches {bad}")
print("  15 = ceil(0.55*27) =", int(np.ceil(0.55 * 27)), "; count-blocking size 27-15+1 =", 27 - 15 + 1)
big3 = ["DE", "FR", "IT"]
print("  DE+FR+IT:", round(pop(big3), 2), "% but only 3 members -> QMV deemed attained:", qmv_pass([k for k in names if k not in big3]))
# smallest blocking coalitions
small13 = sorted(names, key=lambda k: P[k])[:13]
print("  smallest-population blocking coalition: 13 smallest members", small13, round(pop(small13), 2), "%")
min4 = min((pop(c), c) for c in combinations(names, 4) if pop(c) > 35)
print("  smallest-population 4-member population-blocking coalition:", min4[1], round(min4[0], 2), "%")
nobig = [k for k in sorted(names, key=lambda k: -P[k]) if k not in ("DE", "FR", "IT", "ES")]
c = 0
for i, k in enumerate(nobig, 1):
    c += P[k]
    if c > 35:
        print("  without DE, FR, IT, ES a population block needs at least", i, "members (largest remaining:", round(c, 2), "%)")
        break

core = ["PL", "LT", "LV", "EE", "FI", "RO"]
ext = ["SE", "DK", "CZ", "SK", "HU", "BG", "HR"]
groups = {
    "frontline core (PL,LT,LV,EE,FI,RO)": core,
    "core + SE,DK": core + ["SE", "DK"],
    "Bucharest Nine EU members + FI,SE,DK": ["PL", "RO", "HU", "CZ", "SK", "BG", "LT", "LV", "EE", "FI", "SE", "DK"],
    "core + SE,DK,CZ,SK,HU,BG,HR (13)": core + ext,
    "13 without HU, with SI": [k for k in core + ext if k != "HU"] + ["SI"],
    "13 without HU, HR, with SI, GR": [k for k in core + ext if k not in ("HU", "HR")] + ["SI", "GR"],
}
print("\n  coalition                                   members  pop%   blocks stage 1   keeps delegated act (blocks objection)")
for nm, g in groups.items():
    Y = [k for k in names if k not in g]
    print(f"  {nm:42s} {len(g):5d}  {pop(g):6.2f}   {str(not qmv_pass(Y)):5s}            {str(not rqmv_pass(Y)):5s}")
g13 = core + ext
print("  13-member group minimal (members whose removal still leaves a blocking set):",
      [k for k in g13 if not qmv_pass([x for x in names if x not in g13 or x == k])])
# additions the core needs
others = [k for k in names if k not in core]
for m in range(1, 9):
    ok = [cmb for cmb in combinations(others, m) if blocks(core + list(cmb))]
    popok = [cmb for cmb in ok if pop(core + list(cmb)) > 35]
    if popok:
        print(f"  core needs {m} more member(s) to block by POPULATION; {len(popok)} ways, e.g.", popok[:6])
        nobig_ok = [cmb for cmb in popok if not set(cmb) & {"DE", "FR", "IT", "ES"}]
        break
for m in range(1, 12):
    ok = [cmb for cmb in combinations([k for k in others if k not in ("DE", "FR", "IT", "ES")], m) if pop(core + list(cmb)) > 35]
    if ok:
        print(f"  without DE/FR/IT/ES the core needs {m} more members for a population block (count route needs 7)")
        break

print("\n  Delegated act (removal of the US from EU001): Council objection needs >=20 members and >=65% pop")
print("  20 = ceil(0.72*27) =", int(np.ceil(0.72 * 27)), "; act stays if non-objectors have >= 8 members or > 35% pop")
three = sorted([(pop(cmb), cmb) for cmb in combinations(names, 3) if pop(cmb) > 35])
two = [cmb for cmb in combinations(names, 2) if pop(cmb) > 35]
print("  2-member sets with >35%:", two, "; 3-member sets with >35%:", len(three),
      "; smallest:", three[0][1], round(three[0][0], 2), "%")
print("  3-member sets with >35% excluding DE:", [(c_, round(p_, 2)) for p_, c_ in three if "DE" not in c_][:5])
small8 = sorted(names, key=lambda k: P[k])[:8]
print("  smallest-population coalition keeping the act in force: 8 smallest", small8, round(pop(small8), 2), "%")
# exhaustive check of the reinforced rule on sizes <=4 and >=23 + random sets
bad = 0; cnt = 0
for m in list(range(0, 5)) + list(range(23, 28)):
    for Nset in combinations(names, m):
        Y = [k for k in names if k not in Nset]
        cnt += 1; bad += (rqmv_pass(Y) == (len(Nset) >= 8 or pop(Nset) > 35 + 1e-9))
for _ in range(200000):
    m = rng.integers(5, 23); Nset = list(rng.choice(names, m, replace=False)); Y = [k for k in names if k not in Nset]
    cnt += 1; bad += (rqmv_pass(Y) == (len(Nset) >= 8 or pop(Nset) > 35 + 1e-9))
print(f"  reinforced rule 'act stays iff |N|>=8 or pop(N)>35' checked on {cnt} sets, mismatches {bad}")
need = 65 - pop(g13)
print(f"  for the 13-member frontline group to OBJECT it needs 7 more members with >= {need:.2f}% more population")
best = None
for m in range(7, 15):
    ok = [cmb for cmb in combinations([k for k in names if k not in g13], m) if len(g13) + m >= 20 and pop(g13) + pop(cmb) >= 65]
    if ok:
        best = min(ok, key=pop)
        print(f"   minimal additions: {m} members, e.g. smallest-pop completion {best} ({pop(best):.2f}%)")
        break
print("  ACI stage 2 (appeal committee): Commission may adopt unless a QMV (15 members, 65%) votes against;")
print("    the 13-member group cannot stop it alone:", not (len(g13) >= 15 and pop(g13) >= 65))

# ---------------------------------------------------------------- Phi(0)
print("\n=== Groseclose-Snyder Phi(0) = min over blocking J of sum [q_i]^+ ===")
W = {k: int(round(P[k] * 100)) for k in names}


def phi0(q):
    cost = {k: max(q[k], 0.0) for k in names}
    # route 1: any 13 members
    r1 = sum(sorted(cost.values())[:13])
    # route 2: >=4 members with pop > 35% : exact DP over (members capped at 4, pop in hundredths)
    INF = 1e18
    S = sum(W.values())
    dp = np.full((5, S + 1), INF); dp[0, 0] = 0.0
    for k in names:
        w, cst = W[k], cost[k]
        new = dp.copy()
        for c_ in range(5):
            tgt = min(c_ + 1, 4)
            cand = dp[c_, :S + 1 - w] + cst
            new[tgt, w:] = np.minimum(new[tgt, w:], cand)
        dp = new
    r2 = dp[4, 3501:].min()
    return r1, r2, min(r1, r2)


# illustrative profiles
profiles = {}
profiles["q_i = 1 for all (no exposure differences)"] = {k: 1.0 for k in names}
profiles["q_i = -1 frontline core, +1 others"] = {k: (-1.0 if k in core else 1.0) for k in names}
profiles["q_i = -1 frontline 13, +1 others"] = {k: (-1.0 if k in g13 else 1.0) for k in names}
profiles["q_i = pop share, frontline core negative"] = {k: (-P[k] if k in core else P[k]) for k in names}
profiles["q_i = 1 - 2*exposure, exposure high in the east"] = {k: 1 - 2 * (0.9 if k in core else 0.6 if k in ext else 0.2) for k in names}
for nm, q in profiles.items():
    r1, r2, ph = phi0(q)
    free = [k for k in names if q[k] <= 0]
    print(f"  {nm:50s} Phi(0)={ph:7.3f}  (13-member route {r1:.3f}, population route {r2:.3f}); free members {len(free)}, "
          f"free set blocks: {blocks(free)}")

# verify the DP-based Phi(0) by brute force on random small instances (scale rule: count >= 13 still, but force
# most members to be prohibitively expensive so only a 14-member sub-council matters)
mx = 0.0
for trial in range(30):
    sub = list(rng.choice(names, 14, replace=False))
    q = {k: (rng.uniform(-1, 3) if k in sub else 1e6) for k in names}
    _, r2, _ = phi0(q)
    best = np.inf
    for m in range(4, 15):
        for cmb in combinations(sub, m):
            if pop(cmb) > 35 + 1e-9:
                best = min(best, sum(max(q[k], 0) for k in cmb))
    if np.isfinite(best):
        mx = max(mx, abs(best - r2))
    else:
        assert r2 >= 1e5   # no cheap population-blocking set exists; DP must use an expensive member
print(f"  DP population route vs brute force on 30 random 14-member sub-councils: max abs diff {mx:.2e}")
