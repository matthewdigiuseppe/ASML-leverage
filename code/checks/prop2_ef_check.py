"""Proposition 2(e) and 2(f): alternating offers between Europe and the US.

All values are per-period, relative to the status quo (SQ): Europe gets tau (transfer),
exit gives Europe Q and the US -V; SQ gives both 0.  Discount factor delta.

(e) Two readings of "Europe may exit after any rejection":
   R  = responder-only: Europe may exit only after rejecting a US offer (Shaked-Sutton).
   AR = any rejection: Europe may also exit right after the US rejects Europe's demand.
"""
from fractions import Fraction as F

def finite_horizon(Q, V, delta, T, rule, terminal=0):
    """Backward induction over T rounds, US proposes in odd rounds (round 1 first).
    y[t] = transfer agreed at round t (immediate agreement, responder accepts ties).
    After round T: SQ forever (terminal=0)."""
    y_next = F(terminal)
    for t in range(T, 0, -1):
        us_proposes = (t % 2 == 1)
        if us_proposes:
            res = max(Q, delta * y_next)          # Europe can reject+exit or reject+continue
            alt = -V if Q > delta * y_next else -delta * y_next
            y = res if -res >= alt else None      # US prefers to pay res
            if y is None:
                return ('exit at round', t)
        else:
            exit_after_rej = (rule == 'AR') and (Q > delta * y_next)
            y = V if exit_after_rej else delta * y_next
        y_next = y
    return y_next

def paper_profile_deviation(Q, V, delta, rule):
    """Paper's stationary profile: US offers Q, Europe demands delta*Q.
    Check Europe's one-shot deviation to demanding V when it proposes."""
    xU = Q
    # after US rejects Europe's demand: continue -> delta*xU ; exit (AR only) -> Q
    exits = (rule == 'AR') and (Q > delta * xU)
    us_reject_value = -V if exits else -delta * xU
    accept_V = (-V >= us_reject_value)
    max_acceptable = V if exits else delta * xU
    return dict(exit_after_rejection=exits, max_acceptable_demand=max_acceptable,
                paper_demand=delta * Q, profitable_deviation=max_acceptable > delta * Q)

def mixed_stationary_AR(Q, V, delta):
    """Stationary eq. under AR when delta^2 V > Q: Europe exits after a US rejection w.p. p."""
    xU = Q / delta
    xE = Q / delta ** 2
    p = (xE - Q) / (V - Q)
    checks = dict(
        europe_indifferent_after_rejection=(delta * xU == Q),
        us_indifferent_on_xE=(xE == p * V + (1 - p) * delta * xU),
        europe_accepts_xU=(xU >= max(Q, delta * xE)),
        p_in_unit=(0 <= p <= 1))
    return xU, xE, p, checks

def breakdown(Q, V, delta, p, beta=None, voluntary_exit=False):
    """(f) Stationary values with exogenous breakdown prob p after each rejection.
    beta=None: alternating offers, returns US-proposer offer xU.
    beta given: random proposer (Europe w.p. beta), returns expected transfer w."""
    if beta is None:
        a = delta * (1 - p)
        xU = delta * p * (Q + a * V) / (1 - a * a)
        if voluntary_exit:
            xU = max(xU, Q)
        return xU
    w = delta * p * (Q + beta * (V - Q)) / (1 - delta * (1 - p))
    return w

if __name__ == '__main__':
    Q, V = F(1), F(10)
    print('=== 2(e) paper profile, one-shot deviation check (Q=1, V=10) ===')
    for d in [F(9, 10), F(99, 100)]:
        for rule in ['R', 'AR']:
            print(f' delta={d}, rule={rule}:', paper_profile_deviation(Q, V, d, rule))
    print('=== 2(e) finite-horizon backward induction, round-1 transfer, delta=0.95 ===')
    d = F(95, 100)
    for rule in ['R', 'AR']:
        vals = [finite_horizon(Q, V, d, T, rule) for T in range(60, 81)]
        print(f' rule={rule}:', [round(float(v), 3) if not isinstance(v, tuple) else v for v in vals])
    print('=== 2(e) AR rule, delta=0.999, T=1000..1100 range of round-1 transfers ===')
    d = F(999, 1000)
    vals = [float(finite_horizon(Q, V, d, T, 'AR')) for T in range(1000, 1101)]
    print('  min', round(min(vals), 3), 'max', round(max(vals), 3))
    print('=== 2(e) mixed stationary equilibrium under AR ===')
    for d in [F(9, 10), F(99, 100), F(999, 1000)]:
        xU, xE, p, ch = mixed_stationary_AR(Q, V, d)
        print(f' delta={d}: xU={float(xU):.4f} xE={float(xE):.4f} p={float(p):.5f}', ch)
    print('=== 2(e) Q<=0 under both rules (Q=-1) ===')
    for rule in ['R', 'AR']:
        print(' ', rule, [float(finite_horizon(F(-1), V, F(95, 100), T, rule)) for T in (50, 51)])

    print('=== 2(f) breakdown, Q=1, V=10, NBS(beta=1/2) predicts 5.5 ===')
    for p in [F(1, 10), F(1, 100), F(1, 1000), F(1, 10000)]:
        r1 = breakdown(Q, V, F(1), p)
        r2 = breakdown(Q, V, F(99, 100), p)
        r3 = breakdown(Q, V, F(99, 100), p, voluntary_exit=True)
        r4 = breakdown(Q, V, 1 - p, p)          # delta = 1 - p (kappa = 1)
        print(f' p={float(p)}: delta=1 -> {float(r1):.4f};  delta=.99 -> {float(r2):.4f};'
              f' delta=.99 w/ exit option -> {float(r3):.4f};  delta=1-p -> {float(r4):.4f}')
    print('=== 2(f) random proposer, beta=0.3: predicts Q+beta(V-Q)=', float(Q + F(3, 10) * (V - Q)))
    for p in [F(1, 100), F(1, 10000)]:
        print(f' p={float(p)}: delta=1 -> {float(breakdown(Q, V, F(1), p, beta=F(3,10))):.4f};'
              f' delta=.99 -> {float(breakdown(Q, V, F(99,100), p, beta=F(3,10))):.4f}')
    print('=== 2(f) Q<0 example: Q=-2, V=10, beta=1/2: [Q+beta(V-Q)]^+ =', max(0, float(F(-2) + F(1,2)*12)))
    print('   delta=1, p=1e-4 alternating ->', float(breakdown(F(-2), V, F(1), F(1, 10000))))
