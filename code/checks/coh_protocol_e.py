# Prop 2(e): Europe and US alternate offers of a permanent per-period transfer tau.
# Status quo during bargaining: E gets -rr per period, U gets 0. Exit (absorbing): E gets e=omega-c per period, U gets -V.
# Agreement on tau: E gets tau - rr, U gets -tau per period. Discount delta. Values are in per-period units
# (i.e. multiplied by (1-delta)).
# Version "any": Europe may exit after ANY rejection (its own or the US's), as the proposition is worded.
# Version "own": Europe may exit only after it rejects a US offer (Shaked-Sutton timing used in the proof).
# Finite horizon N with backward induction on a fine grid of offers; after round N the status quo or exit forever,
# Europe choosing. U breaks its own indifference against Europe (accepts only if strictly better or equal? -> we
# report both), Europe accepts when indifferent. Grid mesh is small.
import numpy as np
pos = lambda x: max(0.0, x)

def solve(Q, V, rr, delta, version, first, N=400, mesh=1e-4):
    e = Q - rr                      # exit flow for E, since Q = omega - c + rr
    sqE, sqU = -rr, 0.0
    # terminal: E chooses exit vs status quo forever
    if e > sqE: vE, vU = e, -V
    else: vE, vU = sqE, sqU
    proposer = first if N % 2 == 1 else ('E' if first == 'U' else 'U')
    # we iterate backwards over rounds; round k proposer alternates; compute proposer of last round
    props = []
    p = first
    for k in range(N):
        props.append(p); p = 'E' if p == 'U' else 'U'
    for k in reversed(range(N)):
        P = props[k]
        # continuation if rejected and no exit: one status-quo period then (vE, vU)
        contE = (1 - delta) * sqE + delta * vE
        contU = (1 - delta) * sqU + delta * vU
        if P == 'U':
            # E rejects -> E may exit (both versions)
            if e > contE: rejE, rejU = e, -V
            else: rejE, rejU = contE, contU
            # U offers the least tau with tau - rr >= rejE, if that beats rejection for U
            tau = pos(rejE + rr)
            if -tau >= rejU: vE, vU = tau - rr, -tau
            else: vE, vU = rejE, rejU
        else:
            # E demands tau; if U rejects:
            if version == 'any' and e > contE: rejE, rejU = e, -V
            else: rejE, rejU = contE, contU
            # U accepts iff -tau >= rejU ; E demands the most U accepts if better than rejection
            tau = -rejU
            if tau >= 0 and tau - rr >= rejE: vE, vU = tau - rr, -tau
            else: vE, vU = rejE, rejU
    return vE + rr, -vU   # transfer to E in per-period units (if agreement) = -vU

for version in ['own', 'any']:
    for first in ['U', 'E']:
        for delta in [0.9, 0.99, 0.999]:
            Lr = solve(Q=1.0, V=5.0, rr=0.0, delta=delta, version=version, first=first)
            print(f"exit after {version:3s} rejection, first proposer {first}, delta={delta}: L = {Lr[1]:.4f}  (Q=1, V=5)")
