# Brute-force check of the alignment contest on a discrete grid.
# U offers t_U (paid if A); C then offers t_C (paid if P); E chooses A iff t_U - r >= t_C - L (ties -> A).
# Prediction: if V >= Q: A with t_U = max(0, Q) (up to grid); else P with E payoff V - r.
import itertools, random
def solve(V, W, L, r, grid):
    best_U = None
    for tU in grid:
        # C's best response
        best_c = (0.0, None)  # payoff, tC ; None = lose
        for tC in grid:
            if tC - L > tU - r and tC <= W:  # C wins strictly
                pay = W - tC
                if pay > best_c[0] or best_c[1] is None and pay >= 0:
                    if best_c[1] is None or pay > best_c[0]:
                        best_c = (pay, tC)
        if best_c[1] is None:
            uU, uE, a = V - tU, tU - r, 'A'
        else:
            uU, uE, a = 0.0, best_c[1] - L, 'P'
        if best_U is None or uU > best_U[0] + 1e-12:
            best_U = (uU, tU, uE, a)
    return best_U
step = 0.01
grid = [round(i*step, 4) for i in range(0, 801)]
random.seed(1)
bad = 0
for _ in range(40):
    V, W, L, r = [round(random.uniform(0, 5), 2) for _ in range(4)]
    Q = W - L + r
    uU, tU, uE, a = solve(V, W, L, r, grid)
    predE = -r + min(V, max(0, Q))
    if abs(uE - predE) > 0.03:
        bad += 1
        print('MISMATCH', V, W, L, r, 'Q', Q, 'got', a, tU, uE, 'pred', predE)
print('mismatches', bad)
