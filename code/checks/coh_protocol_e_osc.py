# Horizon dependence of the 'exit after any rejection' version of Prop 2(e): L as a function of horizon N.
ns = {}
exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "coh_protocol_e.py")).read().split("for version in")[0], ns)
solve = ns['solve']
for delta in [0.99]:
    vals_any = [round(solve(1.0, 5.0, 0.0, delta, 'any', 'U', N=N)[1], 3) for N in range(2000, 2400, 20)]
    vals_own = [round(solve(1.0, 5.0, 0.0, delta, 'own', 'U', N=N)[1], 3) for N in range(2000, 2400, 20)]
    print("delta", delta, "any-rejection, L by horizon:", vals_any)
    print("delta", delta, "own-rejection, L by horizon:", vals_own)
    print("min/max any:", min(vals_any), max(vals_any), " (Q=1, V=5)")
