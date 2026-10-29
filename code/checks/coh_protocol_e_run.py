# Same game as coh_protocol_e.py but with horizon long enough (N = 60/(1-delta)) that terminal effects vanish,
# and with two different terminal conditions to confirm convergence to the stationary equilibrium.
import importlib.util, sys
spec = importlib.util.spec_from_file_location("m", __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "coh_protocol_e.py"))
src = open(spec.origin).read().split("for version in")[0]
ns = {}; exec(src, ns)
solve = ns['solve']
for version in ['own', 'any']:
    for first in ['U', 'E']:
        for delta in [0.9, 0.99, 0.999]:
            N = int(60 / (1 - delta)) // 2 * 2
            L1 = solve(Q=1.0, V=5.0, rr=0.0, delta=delta, version=version, first=first, N=N)[1]
            L2 = solve(Q=1.0, V=5.0, rr=0.0, delta=delta, version=version, first=first, N=N + 1)[1]
            print(f"exit after {version:3s} rejection, first {first}, delta={delta}: L = {L1:.4f} / {L2:.4f} (N even/odd)  Q=1, V=5")
