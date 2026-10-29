"""Blocking minorities and a priori power in the Council for an anti-US countermeasure
(ACI Art. 5 determination stage: Council implementing act by positive QMV; abstention = not yes).

Data
- 2026 Council population figures: Council Decision (EU, Euratom) 2025/2427, Annex III
  (OJ L 2025/2427, 27.11.2025), http://data.europa.eu/eli/dec/2025/2427/oj
- EUROPOP2023 baseline projections, Eurostat dataset proj_23np (projection=BSL, sex=T,
  age=TOTAL, unit=PER), retrieved 2026-10-29 from
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/proj_23np
  (dataset 'updated' stamp 2026-05-12).

Decision rule (Art. 16(4) TEU, Art. 238(3) TFEU, 27 members): a set Y of 'yes' votes wins iff
  (|Y| >= 15 and pop(Y) >= 65% of EU population) or |Y| >= 24
(the second clause encodes 'a blocking minority must include at least four members').
A set N of non-yes votes (against + abstain + absent) blocks iff Y = complement(N) loses.

Power indices are computed exactly (integer populations, no rounding) by meet-in-the-middle
counting of swing coalitions, and cross-checked against a Monte Carlo estimate.
Run: python3 council_revealed_blocking.py
"""
from bisect import bisect_left
from itertools import combinations
from math import factorial
import random

POP2026 = dict(DE=83502300, FR=68635943, IT=59635202, ES=49093546, PL=37475594, RO=19036031,
               NL=18191086, BE=11900123, CZ=10921096, PT=10749635, SE=10583000, GR=10409547,
               HU=9539502, AT=9180000, BG=6437360, DK=5985790, FI=5626971, SK=5456246,
               IE=5440278, HR=3874350, LT=2890664, SI=2130850, LV=1860565, EE=1369995,
               CY=982966, LU=680084, MT=574250)
assert sum(POP2026.values()) == 452162974  # EU-27 total printed in the Decision

# EUROPOP2023 baseline (Eurostat geo code EL = Greece, mapped to GR here)
EUROPOP = {
    2029: dict(BE=11974068, BG=6629192, CZ=10882453, DK=6045664, DE=85304262, EE=1362440,
               IE=5384987, GR=10090457, ES=49167929, FR=69251760, HR=3713774, IT=58797473,
               CY=955378, LV=1777599, LT=2767640, LU=730190, HU=9550024, MT=594914,
               NL=18291923, AT=9192199, PL=37614410, PT=10274413, RO=18341717, SI=2119727,
               SK=5465314, FI=5636361, SE=10960521),
    2030: dict(BE=12009045, BG=6574153, CZ=10851301, DK=6059699, DE=85284256, EE=1358611,
               IE=5416927, GR=10032545, ES=49266930, FR=69386211, HR=3693206, IT=58773783,
               CY=957744, LV=1756334, LT=2741927, LU=740420, HU=9526758, MT=604727,
               NL=18341701, AT=9214690, PL=37420524, PT=10249138, RO=18218553, SI=2118806,
               SK=5450183, FI=5631487, SE=11020442),
    2031: dict(BE=12043620, BG=6520799, CZ=10820816, DK=6072787, DE=85263378, EE=1354919,
               IE=5448839, GR=9975534, ES=49363835, FR=69519142, HR=3673118, IT=58748917,
               CY=959918, LV=1735494, LT=2716418, LU=750434, HU=9503984, MT=614208,
               NL=18389941, AT=9236319, PL=37228439, PT=10223387, RO=18097342, SI=2117905,
               SK=5434204, FI=5626065, SE=11078730),
}
EUROPOP_TOTAL = {2029: 452876789, 2030: 452700101, 2031: 452518492}
for y in EUROPOP:
    assert sum(EUROPOP[y].values()) == EUROPOP_TOTAL[y], y

N_MEMBERS = 27


def wins(count, pop, total):
    # pop >= 65% of total, in exact integer arithmetic
    return count >= 24 or (count >= 15 and 100 * pop >= 65 * total)


def blocks(nonyes, P):
    total = sum(P.values())
    ycount = N_MEMBERS - len(nonyes)
    ypop = total - sum(P[k] for k in nonyes)
    return not wins(ycount, ypop, total)


def share(S, P):
    return 100.0 * sum(P[k] for k in S) / sum(P.values())


# ---------- exact power indices by meet-in-the-middle ----------
def half_table(players, P):
    """dict count -> sorted list of subset populations"""
    tab = {}
    m = len(players)
    pops = [P[p] for p in players]
    for mask in range(1 << m):
        c = 0
        s = 0
        for j in range(m):
            if mask >> j & 1:
                c += 1
                s += pops[j]
        tab.setdefault(c, []).append(s)
    for c in tab:
        tab[c].sort()
    return tab


def count_in_range(lst, lo, hi):
    """number of x in sorted lst with lo <= x < hi"""
    return bisect_left(lst, hi) - bisect_left(lst, lo)


def power_indices(P):
    names = list(P)
    total = sum(P.values())
    # smallest integer pop T with 100*T >= 65*total
    T = -(-65 * total // 100)
    BIG = total + 1
    n = len(names)
    ss, bz = {}, {}
    for i in names:
        others = [x for x in names if x != i]
        A, B = others[:13], others[13:]
        ta, tb = half_table(A, P), half_table(B, P)
        pi = P[i]
        swings_by_k = [0] * n
        for k in range(n):  # size of S (coalition of others)
            if k + 1 < 15 or k >= 24:
                continue
            if k == 14:
                lo, hi = T - pi, BIG
            elif k <= 22:
                lo, hi = T - pi, T
            else:  # k == 23
                lo, hi = 0, T
            cnt = 0
            for ca, la in ta.items():
                cb = k - ca
                if cb not in tb:
                    continue
                lb = tb[cb]
                for sa in la:
                    cnt += count_in_range(lb, lo - sa, hi - sa)
            swings_by_k[k] = cnt
        ss[i] = sum(swings_by_k[k] * factorial(k) * factorial(n - k - 1) for k in range(n)) / factorial(n)
        bz[i] = sum(swings_by_k)
    tot_bz = sum(bz.values())
    return ss, {k: v / tot_bz for k, v in bz.items()}, {k: v / 2 ** (n - 1) for k, v in bz.items()}


def mc_ss(P, draws=200000, seed=1):
    rng = random.Random(seed)
    names = list(P)
    total = sum(P.values())
    hits = dict.fromkeys(names, 0)
    for _ in range(draws):
        rng.shuffle(names)
        c = s = 0
        for x in names:
            c += 1
            s += P[x]
            if wins(c, s, total):
                hits[x] += 1
                break
    return {k: v / draws for k, v in hits.items()}


# ---------- revealed-position orderings ----------
SCENARIO = ["NL", "IE", "PL", "LT", "LV", "EE", "IT"]  # Europe 2031, 2029: 6 oppose + IT abstains
CEE_TRIO = ["HU", "SK", "CZ"]  # Greenland Jan 2026: HU blocked a joint EU statement; SK, CZ declined to back statements

# Ordering A ('revealed 2025-26'): most to least likely to withhold 'yes' on an anti-US measure.
# Coding (see memo): Greenland behaviour Jan 2026, reactions to the July 2025 Turnberry deal,
# security dependence on the US, and the scenario's named opponents.
ORDER_A = ["HU", "SK", "IT", "CZ", "PL", "LT", "LV", "EE", "IE", "NL",
           "RO", "FI", "DE", "BG", "HR", "GR", "PT", "MT", "CY", "SI", "LU", "AT", "BE",
           "ES", "SE", "DK", "FR"]
# Ordering B ('structural'): scenario states first, then security-dependent or US-exposed states,
# with the 2025-26 CEE governments placed after them (government turnover by 2029).
ORDER_B = ["NL", "IE", "PL", "LT", "LV", "EE", "IT", "RO", "DE", "HU", "SK", "CZ",
           "FI", "BG", "HR", "GR", "PT", "MT", "CY", "SI", "LU", "AT", "BE", "ES", "SE", "DK", "FR"]
assert sorted(ORDER_A) == sorted(POP2026) and sorted(ORDER_B) == sorted(POP2026)


def first_blocking_prefix(order, P):
    for j in range(1, len(order) + 1):
        if blocks(order[:j], P):
            return j, order[j - 1], share(order[:j], P), share(order[:j - 1], P)
    return None


def single_additions(base, P):
    return sorted([k for k in P if k not in base and blocks(base + [k], P)], key=lambda k: -P[k])


def minimal_completions(base, P, max_add=3, exclude=()):
    pool = [k for k in P if k not in base and k not in exclude]
    out = {}
    for m in range(1, max_add + 1):
        sols = [c for c in combinations(pool, m) if blocks(base + list(c), P)]
        if sols:
            out[m] = sols
            break
    return out


def report(label, P):
    print("=" * 78)
    print(label, "| EU total", sum(P.values()))
    sc = SCENARIO
    print("Scenario coalition", sc, "share %.2f%%, n=%d, blocks=%s" % (share(sc, P), len(sc), blocks(sc, P)))
    print("  single additions that block:", single_additions(sc, P))
    mc = minimal_completions(sc, P, exclude=("DE", "FR", "ES", "RO"))
    print("  smallest completions excluding DE, FR, ES, RO:",
          {m: [(c, round(share(sc + list(c), P), 2)) for c in v[:6]] + (["... %d total" % len(v)] if len(v) > 6 else [])
           for m, v in mc.items()})
    sc2 = sc + CEE_TRIO
    print("Scenario + HU, SK, CZ: share %.2f%%, n=%d, blocks=%s" % (share(sc2, P), len(sc2), blocks(sc2, P)))
    print("  single additions that block:", single_additions(sc2, P))
    sc3 = sc + ["SK", "CZ"]
    print("Scenario + SK, CZ (no HU): share %.2f%%, n=%d, blocks=%s" % (share(sc3, P), len(sc3), blocks(sc3, P)))
    print("  single additions that block:", single_additions(sc3, P))
    small13 = sorted(P, key=lambda k: P[k])[:13]
    print("13 smallest:", small13, "share %.2f%%, blocks=%s" % (share(small13, P), blocks(small13, P)))
    for nm, order in (("Ordering A (revealed 2025-26)", ORDER_A), ("Ordering B (structural)", ORDER_B)):
        j, piv, sh, shprev = first_blocking_prefix(order, P)
        print("%s: first blocking prefix has %d members, pivot=%s, share %.2f%% (before pivot %.2f%%)"
              % (nm, j, piv, sh, shprev))


if __name__ == "__main__":
    report("2026 Council weights (Decision 2025/2427)", POP2026)
    for y in (2029, 2030, 2031):
        report("EUROPOP2023 baseline %d" % y, EUROPOP[y])

    # EV duties vote, 4 Oct 2024 (Zhang 2025, Table 6.2), re-weighted with 2026 figures
    ev_for = ["BG", "DK", "EE", "FR", "IE", "IT", "LV", "LT", "NL", "PL"]
    ev_against = ["DE", "HU", "MT", "SK", "SI"]
    ev_abst = [k for k in POP2026 if k not in ev_for + ev_against]
    print("=" * 78)
    print("EV CVD vote (2026 weights): for %.2f%% (%d), against %.2f%% (%d), abstain %.2f%% (%d)" % (
        share(ev_for, POP2026), len(ev_for), share(ev_against, POP2026), len(ev_against),
        share(ev_abst, POP2026), len(ev_abst)))
    print("  QMV in favour?", wins(len(ev_for), sum(POP2026[k] for k in ev_for), sum(POP2026.values())),
          "| QMV against?", wins(len(ev_against), sum(POP2026[k] for k in ev_against), sum(POP2026.values())))

    # Supermajority / consensus norms: tabling (or adoption) requires yes-share >= tau of population
    # and at least m yes-states. Which coalitions then suffice to stop a measure?
    print("=" * 78)
    for label, P in (("2026", POP2026), ("2031", EUROPOP[2031])):
        sc = SCENARIO
        print("[%s] scenario yes-share %.2f%% with %d yes-states -> fails under any norm tau > that share"
              % (label, 100 - share(sc, P), 27 - len(sc)))
        print("[%s] scenario+HU,SK,CZ yes-share %.2f%% (%d yes-states)" % (label, 100 - share(sc + CEE_TRIO, P), 17))
        for tau in (65, 70, 75, 80, 90):
            need = 100 - tau  # non-yes share strictly above this blocks
            j = None
            for jj in range(1, 28):
                if share(ORDER_A[:jj], P) > need + 1e-12 and jj >= 1:
                    j = jj
                    break
            print("   tau=%d%%: first blocking prefix of ordering A (pop rule only): %s (%.2f%%)"
                  % (tau, ORDER_A[:j], share(ORDER_A[:j], P)))

    print("=" * 78)
    for label, P in (("2026", POP2026), ("2031", EUROPOP[2031])):
        ss, bzn, bza = power_indices(P)
        print("Power indices (%s): state  SS%%  Banzhaf-normalised%%  Banzhaf-absolute  pop%%" % label)
        for k in sorted(P, key=lambda k: -P[k]):
            print("   %s  %6.3f  %6.3f  %.4f  %6.2f" % (k, 100 * ss[k], 100 * bzn[k], bza[k], share([k], P)))
        print("   sum SS = %.6f" % sum(ss.values()))
        if label == "2026":
            mc = mc_ss(P)
            print("   Monte Carlo SS check (200k orderings): DE %.3f, FR %.3f, NL %.3f, MT %.3f" % (
                100 * mc["DE"], 100 * mc["FR"], 100 * mc["NL"], 100 * mc["MT"]))
