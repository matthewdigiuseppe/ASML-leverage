# Check EU Council population claims in 06_extensions.tex against Council Decision 2025/2427 shares (1 Jan 2026)
from itertools import combinations
P = dict(DE=18.47, FR=15.18, IT=13.19, ES=10.86, PL=8.29, RO=4.21, NL=4.02, BE=2.63, CZ=2.42, PT=2.38,
         SE=2.34, GR=2.30, HU=2.11, AT=2.03, BG=1.42, DK=1.32, FI=1.24, SK=1.21, IE=1.20, HR=0.86,
         LT=0.64, SI=0.47, LV=0.41, EE=0.30, CY=0.22, LU=0.15, MT=0.13)
print("n members", len(P), "sum of shares", round(sum(P.values()), 4))
opp = ["NL", "IE", "PL", "LT", "LV", "EE", "IT"]
s = sum(P[k] for k in opp)
print("scenario opponents share", round(s, 4), "n =", len(opp))
# Treaty rule (Art 16(4) TEU, 27 members): a measure fails iff the non-yes set N is blocking:
# |N| >= 13 (yes < 15 = 55% of 27 rounded up) or (|N| >= 4 and pop(N) > 35)
import math
print("55% of 27 =", 0.55*27, "-> yes needed", math.ceil(0.55*27), "-> number-blocking needs", 27-math.ceil(0.55*27)+1)
def blocks_treaty(N):
    return len(N) >= 13 or (len(N) >= 4 and sum(P[k] for k in N) > 35 + 1e-12)
def blocks_paper(N):
    return len(N) >= 4 and sum(P[k] for k in N) > 35 + 1e-12
rest = sorted([k for k in P if k not in ("DE", "FR", "IT", "ES")], key=lambda k: -P[k])
cum = 0
for i, k in enumerate(rest, 1):
    cum += P[k]
    if cum > 35:
        print("min #members of pop-blocking coalition excluding DE,FR,IT,ES:", i, "cum share", round(cum, 2)); break
prev = sum(P[k] for k in rest[:i-1]); print("  with", i-1, "largest remaining:", round(prev, 2))
small13 = sorted(P, key=lambda k: P[k])[:13]
print("13 smallest members:", small13, "share", round(sum(P[k] for k in small13), 2),
      "treaty-blocking:", blocks_treaty(small13), "paper-blocking:", blocks_paper(small13))
# scenario opponents plus additional eastern-flank states
add = ["RO", "CZ", "HU"]
c = opp + add
print("opponents + RO,CZ,HU:", round(sum(P[k] for k in c), 2), "members", len(c), "blocks:", blocks_treaty(c))
# minimal number of additional states (any) that make the opponents a blocking minority
others = sorted([k for k in P if k not in opp], key=lambda k: -P[k])
for m in range(1, 7):
    ok = [cmb for cmb in combinations(others, m) if blocks_treaty(opp + list(cmb))]
    if ok:
        noLarge = [cmb for cmb in ok if not set(cmb) & {"DE", "FR", "ES"}]
        print("additions needed:", m, "count", len(ok), "without DE/FR/ES:", len(noLarge), noLarge[:5]); break
# Example where the 13-member route changes K(0): q_i = population share
q = P
# paper's K(0): min over pop-blocking coalitions of sum q_i: greedy is not exact; enumerate via knapsack-like DP over subsets? Use simple reasoning:
# minimize sum q_i s.t. sum q_i > 35 -> about 35.x; treaty also allows 13 smallest
best_paper = None
names = list(P)
# exact via DP on integer hundredths
w = {k: int(round(P[k]*100)) for k in P}
INF = 10**9
# dp[c][s] = min cost with c members and pop s (cost = pop here), just check feasibility of sums
reach = {(0, 0)}
for k in names:
    new = set(reach)
    for (c_, s_) in reach:
        new.add((min(c_+1, 27), s_ + w[k]))
    reach = new
best_paper = min(s_ for (c_, s_) in reach if c_ >= 4 and s_ > 3500)
print("K(0) with q_i = pop share: paper's B family ->", best_paper/100, "; treaty family ->", min(best_paper/100, round(sum(P[k] for k in small13), 2)))
