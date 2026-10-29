# Unconditional breakdown probability (ultimatum issued AND refused) as China's transfer punishment r^c rises.
ns = {}; exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "coh_breakdown.py")).read().split("random.seed(2)")[0], ns)
brute = ns['brute']
b1, e, R, sbar = 3.0, 1.0, 3.0, 3.0
for rc in [0.0, 0.25, 0.5, 0.75, 1.0]:
    iss, Pu, Pc, T = brute(b1 - rc, e, R, sbar)
    print(f"b1={b1}, r^c={rc}, e={e}, R={R}, sbar={sbar}: issued={iss}, P_b|issued={Pc:.3f}, unconditional={Pu:.3f}")
