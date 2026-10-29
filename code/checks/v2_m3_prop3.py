"""v2 verifier m3: Proposition 3 (endogenous conditionality).

U chooses kappa in [kappa_0, kappa_bar] to maximize
    Pi(kappa) = -[Q(kappa)]^+ + w * [-Q(kappa)]^+ - H(kappa),
    Q(kappa) = Q_0 - (kappa - kappa_0) S_k,  H convex, increasing, H(kappa_0) = 0.
Brute force: dense grid (200001 points) plus golden-section polishing around the best
grid point, for several convex H.  Compared with
  memo (a)  w = 0:            kappa* = kappa_0 if Q_0 <= 0, else min{kappa_z, kappa_1, kappa_bar}
  memo (b)  w > 0, H'(kz) < w S_k, kz < kbar:  kappa* = min{kappa_w, kappa_bar} > kappa_z
  general   kappa* = min{kbar, max{kw, min{kz, k1}}},  kw = inf{k >= k0: H'(k) >= w S_k},
            k1 = inf{k >= k0: H'(k) >= S_k}   (inf of empty set = +infinity)
and the comparative statics in (c).  Part (d): kappa_bar = G(s_X+s_L) - G(s_X - mbar_U)
as a function of s_X for several distributions G.

Run: python3 -I v2_m3_prop3.py   (under a minute)
"""
import math
import random
import time

import numpy as np

NG = 200001


def make_H(rng):
    kind = rng.choice(['quad', 'exp', 'power', 'kink', 'linear', 'quad0'])
    a = rng.uniform(0.2, 6.0)
    if kind == 'quad':
        b = rng.uniform(0.0, 3.0)
        H = lambda x: a * x * x + b * x
        Hp = lambda x: 2 * a * x + b
    elif kind == 'quad0':
        H = lambda x: a * x * x
        Hp = lambda x: 2 * a * x
    elif kind == 'exp':
        c = rng.uniform(0.5, 6.0)
        H = lambda x: a * (np.exp(c * x) - 1)
        Hp = lambda x: a * c * math.exp(c * x)
    elif kind == 'power':
        p = rng.choice([1.5, 2.0, 3.0, 4.0])
        H = lambda x: a * x ** p
        Hp = lambda x: a * p * x ** (p - 1)
    elif kind == 'kink':
        a2 = rng.uniform(0.5, 8.0)
        x1 = rng.uniform(0.02, 0.4)
        H = lambda x: a * x + a2 * np.maximum(x - x1, 0.0)
        Hp = lambda x: a + (a2 if x >= x1 else 0.0)   # right derivative
    else:
        H = lambda x: a * x
        Hp = lambda x: a
    return kind, H, Hp


def thresh(Hp, level, k0, kbar):
    """inf{k in [k0, kbar]: H'(k) >= level}; +inf if none (H' nondecreasing)."""
    if Hp(0.0) >= level:
        return k0
    if Hp(kbar - k0) < level:
        return math.inf
    lo, hi = 0.0, kbar - k0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if Hp(mid) >= level:
            hi = mid
        else:
            lo = mid
    return k0 + hi


def solve(params):
    k0, kbar, Q0, S, w, H = params
    xs = np.linspace(k0, kbar, NG)
    Q = Q0 - (xs - k0) * S
    Hv = H(xs - k0) * np.ones_like(xs)
    Pi = -np.maximum(Q, 0) + w * np.maximum(-Q, 0) - Hv
    i = int(np.argmax(Pi))
    # polish by golden section on neighbouring cell
    lo = xs[max(i - 1, 0)]
    hi = xs[min(i + 1, NG - 1)]
    f = lambda x: float(-max(Q0 - (x - k0) * S, 0) + w * max(-(Q0 - (x - k0) * S), 0)
                        - H(x - k0))
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(80):
        if f(c) >= f(d):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    xstar = 0.5 * (a + b)
    cands = [(f(x), x) for x in (xstar, xs[i], k0, kbar)]
    best = max(cands)
    return best[1], best[0], f


def formula(params, Hp):
    k0, kbar, Q0, S, w, H = params
    kz = k0 + Q0 / S
    k1 = thresh(Hp, S, k0, kbar)
    kw = thresh(Hp, w * S, k0, kbar)
    return min(kbar, max(kw, min(kz, k1))), kz, k1, kw


def memo_formula(params, Hp):
    """Memo (a)/(b); returns None when neither applies."""
    k0, kbar, Q0, S, w, H = params
    kz = k0 + Q0 / S
    k1 = thresh(Hp, S, k0, kbar)
    if w == 0:
        if Q0 <= 0:
            return k0, 'a'
        return min(kz, k1, kbar), 'a'
    if kz >= k0 and kz < kbar and Hp(kz - k0) < w * S:
        kw = thresh(Hp, w * S, k0, kbar)
        return min(kw, kbar), 'b'
    return None, None


def main():
    t0 = time.time()
    rng = random.Random(3)
    N = 1500
    maxdpi = 0.0
    maxdk = 0.0
    memo_a_err = 0.0
    memo_b_err = 0.0
    na = nb = 0
    regimes = {}
    slack_err = 0.0
    rent_err = 0.0
    for it in range(N):
        kind, H, Hp = make_H(rng)
        k0 = rng.uniform(0, 0.3)
        kbar = k0 + rng.uniform(0.05, 0.7)
        S = rng.uniform(0.5, 10.0)
        Q0 = rng.choice([rng.uniform(-3, 4), 0.0, rng.uniform(0, 1)])
        w = rng.choice([0.0, 1.0, rng.uniform(0, 1), rng.uniform(0, 1)])
        params = (k0, kbar, Q0, S, w, H)
        kb, pib, f = solve(params)
        kf, kz, k1, kw = formula(params, Hp)
        pif = f(kf)
        maxdpi = max(maxdpi, pib - pif)  # formula must be (weakly) optimal
        if kind not in ('linear', 'kink') or True:
            # argmax distance only meaningful when the maximiser is unique; check by
            # comparing payoffs at a 1e-3 perturbation
            uniq = (f(kf) - max(f(min(kbar, kf + 1e-3)), f(max(k0, kf - 1e-3)))) > 1e-12
            if uniq:
                maxdk = max(maxdk, abs(kb - kf))
        km, which = memo_formula(params, Hp)
        if which == 'a':
            na += 1
            memo_a_err = max(memo_a_err, pib - f(km))
        elif which == 'b':
            nb += 1
            memo_b_err = max(memo_b_err, pib - f(km))
            slack_err = max(slack_err, abs(max(-(Q0 - (km - k0) * S), 0) - (km - kz) * S))
        # regime classification
        if kf >= kbar - 1e-12:
            reg = 'capped'
        elif kf <= k0 + 1e-12 and kz <= k0:
            reg = 'corner k0 (Q0<=0, kw=k0)'
        elif abs(kf - kz) < 1e-12:
            reg = 'kz (zero premium)'
        elif kf < kz:
            reg = 'k1 < kz (interior, pays rent)'
        else:
            reg = 'kw > kz (interior slack)'
        regimes[reg] = regimes.get(reg, 0) + 1
    print("Prop 3 random draws: %d (H kinds: quad, quad0, exp, power, kink, linear)" % N)
    print("  general formula: max Pi(grid optimum) - Pi(formula) = %.2e; max |argmax diff| "
          "(unique maximiser) = %.2e" % (maxdpi, maxdk))
    print("  memo (a) applicable %d draws: max payoff shortfall %.2e" % (na, memo_a_err))
    print("  memo (b) applicable %d draws: max payoff shortfall %.2e; slack formula err %.2e"
          % (nb, memo_b_err, slack_err))
    print("  regimes:", regimes)

    # (c) comparative statics in Q0 by finite differences, per regime
    print("\n(c) finite differences in Q_0 (h=1e-4), strictly convex H:")
    rng = random.Random(9)
    agg = {}
    for it in range(2000):
        kind, H, Hp = make_H(rng)
        if kind in ('linear', 'kink'):
            continue
        k0 = rng.uniform(0, 0.3)
        kbar = k0 + rng.uniform(0.05, 0.7)
        S = rng.uniform(0.5, 10.0)
        Q0 = rng.uniform(-3, 4)
        w = rng.uniform(0, 1)
        h = 1e-4
        p1 = (k0, kbar, Q0, S, w, H)
        p2 = (k0, kbar, Q0 + h, S, w, H)
        kf1, kz, k1, kw = formula(p1, Hp)
        kf2 = formula(p2, Hp)[0]
        # verify formula against brute force at both points (payoff)
        _, pib1, f1 = solve(p1)
        if pib1 - f1(kf1) > 1e-7:
            agg['FORMULA FAIL'] = agg.get('FORMULA FAIL', 0) + 1
        Qs1 = Q0 - (kf1 - k0) * S
        Qs2 = Q0 + h - (kf2 - k0) * S
        dk = (kf2 - kf1) / h
        drent = (max(Qs2, 0) - max(Qs1, 0)) / h
        dslack = (max(-Qs2, 0) - max(-Qs1, 0)) / h
        if kf1 >= kbar - 1e-9 or kf2 >= kbar - 1e-9:
            reg = 'capped' + (' Q>0' if Qs1 > 0 else ' Q<=0')
            if abs(kf1 - kbar) > 1e-9 or abs(kf2 - kbar) > 1e-9:
                continue
        elif abs(kf1 - kz) < 1e-12:
            reg = 'kz'
        elif kf1 < kz:
            reg = 'k1<kz'
        elif kf1 <= k0 + 1e-12:
            reg = 'k0 corner'
        else:
            reg = 'kw>kz'
        a = agg.setdefault(reg, [0, set()])
        a[0] += 1
        a[1].add((round(dk * S, 3), round(drent, 3), round(dslack, 3)))
    for k, v in agg.items():
        if k == 'FORMULA FAIL':
            print("  FORMULA FAIL count", v)
            continue
        print("  %-14s n=%4d  observed (S_k dk*/dQ0, d rent/dQ0, d slack/dQ0): %s"
              % (k, v[0], sorted(v[1])[:6]))

    # (d) kappa_bar in s_X
    print("\n(d) kappa_bar = G(s_X + s_L) - G(s_X - mbar_U) as s_X rises:")
    def Gnorm(x):
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))
    def gnorm(x):
        return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    dists = {
        'normal(0,1)': (Gnorm, gnorm),
        'logistic': (lambda x: 1 / (1 + math.exp(-x)), lambda x: math.exp(-x) / (1 + math.exp(-x)) ** 2),
        'exponential(1)': (lambda x: 1 - math.exp(-x) if x > 0 else 0.0,
                           lambda x: math.exp(-x) if x > 0 else 0.0),
        'uniform[0,4]': (lambda x: min(max(x / 4, 0), 1), lambda x: 0.25 if 0 < x < 4 else 0.0),
    }
    rng = random.Random(4)
    for name, (G, g) in dists.items():
        inc = 0
        dec = 0
        flat = 0
        derr = 0.0
        tot = 0
        ex = None
        for _ in range(3000):
            sX = rng.uniform(-3, 5)
            sL = rng.uniform(0.05, 2)
            mb = rng.uniform(0.05, 3)
            h = 1e-5
            kb = lambda s: G(s + sL) - G(s - mb)
            dnum = (kb(sX + h) - kb(sX - h)) / (2 * h)
            dform = g(sX + sL) - g(sX - mb)
            # skip draws that straddle a kink of G
            if name != 'normal(0,1)' and name != 'logistic':
                kinks = [0.0] + ([4.0] if name.startswith('uniform') else [])
                if any(abs(sX + sL - kk) < 1e-3 or abs(sX - mb - kk) < 1e-3 for kk in kinks):
                    continue
            tot += 1
            derr = max(derr, abs(dnum - dform))
            if dnum > 1e-9:
                inc += 1
                if ex is None:
                    ex = (round(sX, 3), round(sL, 3), round(mb, 3), round(kb(sX), 4),
                          round(kb(sX + 0.1), 4))
            elif dnum < -1e-9:
                dec += 1
            else:
                flat += 1
        print("  %-15s draws %d: kappa_bar increasing in s_X in %d, decreasing in %d, flat in %d;"
              " max |numerical - (g(s_A)-g(s_X-mbar))| = %.1e" % (name, tot, inc, dec, flat, derr))
        if ex:
            print("      example (s_X, s_L, mbar_U, kbar(s_X), kbar(s_X+0.1)) =", ex)
    # explicit counterexample
    sX, sL, mb = 0.0, 1.0, 2.0
    print("  normal: s_X=0, s_L=1, mbar_U=2: kbar=%.4f; at s_X=0.5: %.4f (rises)"
          % (Gnorm(sX + sL) - Gnorm(sX - mb), Gnorm(0.5 + sL) - Gnorm(0.5 - mb)))
    print("\nTotal time %.1fs" % (time.time() - t0))


if __name__ == '__main__':
    main()
