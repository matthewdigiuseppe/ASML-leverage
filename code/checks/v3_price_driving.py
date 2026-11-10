"""Remark (price driving). Alternating-raise auction in which China's payoff when Europe aligns at price p
is rho*p (rho > 0) and China may bid up to its credibility bound bbar_C = lambda_C*mbar_C - c, even where a
winning bid would be unprofitable. Integer grid (lambda_C = 1, epsilon = 1) in units of value to Europe.
Claim: if Q <= bbar_C < zbar_U - epsilon, every SPE has Europe aligned and a price in
[bbar_C - lambda_C*epsilon, bbar_C + epsilon]. Without spite (rho = 0) the price can be anywhere in [0, Q].
Solved by backward induction over all pure-strategy tie-breaking rules (the extremes are reported).
Run: python3 -I v3_price_driving.py
"""
from functools import lru_cache
import itertools


def solve(Qg, bC, zU, V, rho, WC_units, pick):
    """Qg: China's profitable maximum; bC: credibility bound (>= Qg); zU: Washington's maximum (< V or = V).
    China's payoff from winning at value b is (Qg - b) (scaled so lambda_C = 1, W_C binding: W_C - (b+c) = Qg - b).
    pick: +1 breaks every tie toward a higher final price, -1 toward a lower one."""
    @lru_cache(None)
    def val(bU, bCh, turn, passed):
        # returns (U payoff, China payoff, price, Europe aligns?)
        def end():
            if bU >= bCh:
                return (-max(bU, 0), rho * max(bU, 0), max(bU, 0), True)
            return (-V, Qg - bCh, bCh, False)
        opts = [end() if passed else val(bU, bCh, 1 - turn, True)]
        if turn == 0:
            for b in range(max(bU, -1) + 1, zU + 1):
                opts.append(val(b, bCh, 1, False))
            key = lambda o: (round(o[0], 9), pick * o[2])
        else:
            for b in range(max(bCh, -1) + 1, bC + 1):
                opts.append(val(bU, b, 0, False))
            key = lambda o: (round(o[1], 9), pick * o[2])
        return max(opts, key=key)
    return val(-1, -1, 1, False)


def main():
    bad = 0
    cases = 0
    for Qg, extra, zU in itertools.product(range(0, 7), range(0, 5), range(3, 13)):
        bC = Qg + extra
        if not (bC < zU - 1):
            continue
        V = zU + 0.5
        for rho in (0.1, 0.5):
            for pick in (1, -1):
                U, C, price, aligned = solve(Qg, bC, zU, V, rho, None, pick)
                cases += 1
                if not aligned or price < bC - 1 or price > bC + 1:
                    bad += 1
                    print("violation", Qg, bC, zU, rho, pick, price, aligned)
    print(f"spite rho > 0: {cases} cases, violations of 'aligned, price within one step of bbar_C': {bad}")
    lo = solve(6, 6, 10, 10.5, 0.0, None, -1)[2]
    hi = solve(6, 6, 10, 10.5, 0.0, None, 1)[2]
    print(f"no spite (rho = 0), Q = bbar_C = 6, zbar_U = 10: price ranges over [{lo}, {hi}] across tie-breaking")
    p = solve(6, 9, 12, 12.5, 0.2, None, -1)[2], solve(6, 9, 12, 12.5, 0.2, None, 1)[2]
    print(f"spite, Q = 6 < bbar_C = 9 < zbar_U = 12: price {p} (Washington pays China's credibility bound)")


if __name__ == "__main__":
    main()
