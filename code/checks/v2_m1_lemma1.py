"""v2 Lemma 1 (bidding benchmark): brute-force check.

Model (memo v2, Section 2).  U and C bid for E's alignment with staked promises.
U's promise tau_U is credible iff tau_U <= mbar_U (larger promises are worthless, so U
bids on {0,...,mbar_U}).  C's promise tau_C is credible iff tau_C <= mbar_C and is worth
lambda_C * tau_C to E; C's cost of a winning promise is tau_C and its value of exit is W_C.
E's payoff (relative to the aligned baseline): A -> tau_U ; X -> lambda_C tau_C - c.
U: A -> -tau_U ; X -> -V.   C: A -> 0 ; X -> W_C - tau_C.
Claim: Q = lambda_C min{W_C, mbar_C} - c.  If Q < V and Q <= mbar_U, E aligns and U pays [Q]^+;
if Q > min{V, mbar_U}, E exits.

Three formalizations, none of which uses the claimed formula:
 1. Clock auction in E-utility units: check by enumeration that dropping out at one's maximal
    credible E-value is weakly dominant, and compute the dominant-strategy outcome.
 2. Alternating-raise English auction on an integer grid (jump bids allowed; two consecutive
    passes end the auction; then E chooses).  The FULL set of pure SPE outcomes is computed by
    set-valued backward induction (no tie-breaking at all).
 3. The same game solved by single-valued backward induction under four tie-breaking rules
    on larger grids.
Run: python3 -I v2_m1_lemma1.py   (about one minute)
"""
import random
import sys
from fractions import Fraction as Fr
from functools import lru_cache

sys.setrecursionlimit(100000)


def Qval(p):
    return p['lam'] * min(p['W'], p['mC']) - p['c']


def zbarU(p):
    return min(p['V'], p['mU'])


def target_E(p):
    """E's payoff claimed in the corrected statement: [min{Q, V, mbar_U}]^+."""
    return max(Fr(0), min(Qval(p), Fr(p['V']), Fr(p['mU'])))


def outcome_payoffs(p, bU, bC, a):
    if a == 'A':
        return (Fr(bU), Fr(-bU), Fr(0))           # (E, U, C)
    return (p['lam'] * bC - p['c'], Fr(-p['V']), Fr(p['W'] - bC))


# --------------------------------------------------------------------------------------------
# 1. Clock auction (E-utility units).  A strategy is a drop level d on the grid of E-values;
#    the bidder stays while z <= d.  Grid of E-values: multiples of h.  The clock starts at
#    z = 0 (baseline).  U wins if it stays at least as long as C (ties -> alignment).
# --------------------------------------------------------------------------------------------
def clock_check(p, h=Fr(1, 12)):
    # h = 1/12 puts every Q and zbarU on the grid (lambda_C has denominator 1,2,3,4 or 6)
    lam, c, V, mU, mC, W = p['lam'], p['c'], p['V'], p['mU'], p['mC'], p['W']
    top = max(V, mU, abs(Qval(p))) + 2
    grid = [h * i for i in range(int(top / h) + 1)]
    dropsU = [Fr(-1)] + grid          # -1: never enter
    dropsC = [Fr(-1)] + grid

    def pay(dU, dC):
        # price = the level at which the loser drops; winner U iff dU >= dC
        if dU >= dC:
            z = max(dC, Fr(0))
            if dU < 0:   # both out: baseline, E aligned with no transfer
                z = Fr(0)
            tauU = z
            return ('A', z, -tauU, Fr(0))
        z = max(dU, Fr(0))
        tauC = (z + c) / lam
        return ('X', z, Fr(-V), W - tauC if tauC <= mC else Fr(-10**9))

    # U's credible/valuable maximum: zbarU; C's: Q
    dU_star = max([d for d in dropsU if d <= zbarU(p)])
    dC_star = max([d for d in dropsC if d <= Qval(p)], default=Fr(-1))
    # weak dominance of the 'drop at own maximum' strategy (U drops only at levels <= mbar_U)
    okU = all(pay(dU_star, dC)[2] >= pay(dU, dC)[2] for dU in dropsU if dU <= mU for dC in dropsC)
    okC = all(pay(dU, dC_star)[3] >= pay(dU, dC)[3] for dC in dropsC
              if (dC < 0 or (dC + c) / lam <= mC) for dU in dropsU if dU <= mU)
    a, z, _, _ = pay(dU_star, dC_star)
    return okU and okC, a, z


# --------------------------------------------------------------------------------------------
# 2./3. Alternating-raise auction on the integer grid.
# state: (bU, bC, mover, lastpass); mover 0 = C, 1 = U.
# --------------------------------------------------------------------------------------------
def make_game(p):
    lam, c, V, mU, mC, W = p['lam'], p['c'], p['V'], p['mU'], p['mC'], p['W']

    def E_choice_set(bU, bC):
        zU, zC = Fr(bU), lam * bC - c
        if zU > zC:
            return ['A']
        if zC > zU:
            return ['X']
        return ['A', 'X']

    def children(state):
        bU, bC, mv, lp = state
        out = []
        out.append(('pass', ('END', bU, bC) if lp else (bU, bC, 1 - mv, 1)))
        # bids above one's own value are weakly dominated and excluded (U: <= min(V, mbar_U);
        # C: <= min(W_C, mbar_C)); bids above the cap are worthless promises and also excluded
        if mv == 0:
            for nb in range(bC + 1, min(W, mC) + 1):
                out.append((('raise', nb), (bU, nb, 1, 0)))
        else:
            for nb in range(bU + 1, min(V, mU) + 1):
                out.append((('raise', nb), (nb, bC, 0, 0)))
        return out

    return E_choice_set, children


def spe_outcome_set(p, first_mover=0):
    """Exact set of pure-SPE terminal outcomes (bU, bC, a) of the finite perfect-info game."""
    E_choice_set, children = make_game(p)
    memo = {}

    def S(state):
        if state in memo:
            return memo[state]
        if state[0] == 'END':
            _, bU, bC = state
            res = frozenset((bU, bC, a) for a in E_choice_set(bU, bC))
            memo[state] = res
            return res
        bU, bC, mv, lp = state
        who = 2 if mv == 0 else 1          # index into (E, U, C) payoffs
        ch = [S(s) for _, s in children(state)]
        # punishment value of each action: worst SPE continuation for the mover
        worst = [min(outcome_payoffs(p, *o)[who] for o in s) for s in ch]
        thr = max(worst)
        res = frozenset(o for s in ch for o in s if outcome_payoffs(p, *o)[who] >= thr)
        memo[state] = res
        return res

    return S((0, 0, first_mover, 0))


def spe_tiebreak(p, first_mover=0, rule='eager', e_tie='A'):
    """Single SPE by backward induction with a fixed tie-breaking rule.
    eager: when indifferent prefer the smallest raise, pass last;  lazy: prefer pass."""
    E_choice_set, children = make_game(p)

    @lru_cache(maxsize=None)
    def val(state):
        if state[0] == 'END':
            _, bU, bC = state
            cs = E_choice_set(bU, bC)
            a = e_tie if len(cs) == 2 else cs[0]
            return (bU, bC, a)
        bU, bC, mv, lp = state
        who = 2 if mv == 0 else 1
        ch = children(state)
        if rule == 'eager':
            ch = ch[1:] + ch[:1]
        best, bestv = None, None
        for _, s in ch:
            o = val(s)
            v = outcome_payoffs(p, *o)[who]
            if bestv is None or v > bestv:
                best, bestv = o, v
        return best

    return val((0, 0, first_mover, 0))


def rand_params(rng, small):
    if small:
        mU = rng.randint(0, 6)
        mC = rng.randint(0, 8)
        W = rng.randint(0, 8)
        V = rng.randint(1, 8)
        c = rng.randint(0, 5)
    else:
        mU = rng.randint(0, 20)
        mC = rng.randint(0, 22)
        W = rng.randint(0, 22)
        V = rng.randint(1, 22)
        c = rng.randint(0, 12)
    lam = rng.choice([Fr(1), Fr(1, 2), Fr(2, 3), Fr(3, 4), Fr(1, 3), Fr(5, 6)])
    return dict(mU=mU, mC=mC, W=W, V=V, c=c, lam=lam)


def main():
    rng = random.Random(20261029)
    # ---------------- 1. clock auction --------------------------------------------------------
    n_clock, bad_clock, max_err_clock = 0, 0, Fr(0)
    for _ in range(300):
        p = rand_params(rng, small=True)
        if p['lam'] == 0:
            continue
        ok, a, z = clock_check(p)
        n_clock += 1
        Q, zb = Qval(p), zbarU(p)
        err = abs(z - target_E(p))
        # outcome prediction (strict cases; at Q == zbarU alignment by the tie rule unless Q == V)
        pred = 'A' if Q <= zb else 'X'
        if not ok or (a != pred and Q != p['V']) or (err > 0 and Q != p['V']):
            bad_clock += 1
        max_err_clock = max(max_err_clock, err)
    print(f"[clock] draws={n_clock}  dominance or outcome failures={bad_clock}  "
          f"max |E payoff - [min(Q,V,mU)]^+| = {float(max_err_clock):.3f} (grid 1/12)")

    # ---------------- 2. full SPE outcome sets (small grids) ----------------------------------
    stats = dict(draws=0, A_region=0, X_region=0, winner_fail=0, price_indeterminate=0,
                 upper_fail=0)
    max_upper_gap = Fr(0)
    example = None
    for _ in range(400):
        p = rand_params(rng, small=True)
        for fm in (0, 1):
            outs = spe_outcome_set(p, fm)
            stats['draws'] += 1
            Q, zb = Qval(p), zbarU(p)
            Epays = [outcome_payoffs(p, *o)[0] for o in outs]
            winners = {o[2] for o in outs}
            gstep = max(Fr(1), p['lam'])
            if Q < zb - gstep:
                stats['A_region'] += 1
                if winners != {'A'}:
                    stats['winner_fail'] += 1
            elif Q > zb + gstep:
                stats['X_region'] += 1
                if winners != {'X'}:
                    stats['winner_fail'] += 1
            # maximum E payoff over all SPE equals [min(Q, V, mU)]^+ up to the grid
            gap = max(Epays) - target_E(p)
            if abs(gap) > gstep:
                stats['upper_fail'] += 1
            max_upper_gap = max(max_upper_gap, abs(gap))
            if min(Epays) < target_E(p) - gstep:
                stats['price_indeterminate'] += 1
                if example is None and Q > 1 and Q < zb - 1:
                    example = (p, fm, sorted({float(e) for e in Epays}))
    print("[alternating raise, all pure SPE] ", stats,
          f" max |max_SPE E payoff - [min(Q,V,mU)]^+| = {float(max_upper_gap):.3f}")
    if example:
        p, fm, E = example
        print("   example of price indeterminacy: params", {k: str(v) for k, v in p.items()},
              "Q =", str(Qval(p)), " E payoffs across SPE:", E)

    # ---------------- 3. tie-breaking selections on larger grids -----------------------------
    res = {}
    for rule in ('eager', 'lazy'):
        for e_tie in ('A', 'X'):
            n, wfail, perr, maxerr = 0, 0, 0, Fr(0)
            for _ in range(70):
                p = rand_params(rng, small=False)
                fm = rng.randint(0, 1)
                bU, bC, a = spe_tiebreak(p, fm, rule, e_tie)
                n += 1
                Q, zb = Qval(p), zbarU(p)
                gstep = max(Fr(1), p['lam'])
                if (Q < zb - gstep and a != 'A') or (Q > zb + gstep and a != 'X'):
                    wfail += 1
                Epay = outcome_payoffs(p, bU, bC, a)[0]
                err = abs(Epay - target_E(p))
                if rule == 'eager':
                    maxerr = max(maxerr, err)
                    if err > gstep:
                        perr += 1
            res[(rule, e_tie)] = (n, wfail, perr, float(maxerr))
    for k, v in res.items():
        print(f"[tie rule {k}] draws={v[0]} winner failures={v[1]}"
              + (f" price failures={v[2]} max |E payoff - [min(Q,V,mU)]^+|={v[3]:.3f}"
                 if k[0] == 'eager' else " (price not checked: lazy loser)"))

    # ---------------- edge cases ---------------------------------------------------------------
    print("[edge cases] (E payoff, outcome sets over all SPE, first mover C)")
    cases = {
        'Q<0 (c large)': dict(mU=5, mC=6, W=6, V=8, c=7, lam=Fr(1)),
        'Q = mbar_U < V': dict(mU=4, mC=6, W=6, V=8, c=2, lam=Fr(1)),
        'Q = V < mbar_U': dict(mU=8, mC=8, W=7, V=5, c=2, lam=Fr(1)),
        'mbar_U < Q < V (inefficient exit)': dict(mU=2, mC=8, W=8, V=8, c=2, lam=Fr(1)),
        'Q > V': dict(mU=8, mC=8, W=8, V=3, c=1, lam=Fr(1)),
        'cap binds (mbar_C < W_C)': dict(mU=8, mC=4, W=8, V=8, c=1, lam=Fr(1)),
        'lambda_C = 1/2': dict(mU=8, mC=8, W=8, V=8, c=1, lam=Fr(1, 2)),
        'Q = 0': dict(mU=3, mC=4, W=4, V=6, c=4, lam=Fr(1)),
    }
    for name, p in cases.items():
        outs = spe_outcome_set(p, 0)
        E = sorted({float(outcome_payoffs(p, *o)[0]) for o in outs})
        W = sorted({o[2] for o in outs})
        sel = spe_tiebreak(p, 0, 'eager', 'A')
        selX = spe_tiebreak(p, 0, 'eager', 'X')
        print(f"   {name:36s} Q={str(Qval(p)):>5s} zbarU={zbarU(p)}  winners={W}  "
              f"E payoff range=[{E[0]}, {E[-1]}]  eager/A-tie: {sel[2]} E={float(outcome_payoffs(p, *sel)[0])}"
              f"  eager/X-tie: {selX[2]}")
        if name.startswith('mbar_U < Q'):
            Ue = outcome_payoffs(p, *sel)
            Q = Qval(p)
            # any binding transfer in [Q, V) is strictly better for both E and U
            better = all(Fr(t) > Ue[0] and -Fr(t) > Ue[1] for t in range(int(Q), p['V']))
            print(f"      inefficient exit: equilibrium (E,U)=({float(Ue[0])},{float(Ue[1])}); "
                  f"every tau in [Q,V) Pareto-improves E and U: {better}")


if __name__ == '__main__':
    main()
