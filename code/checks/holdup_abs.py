# Absorbing-stop variant with state-dependent terminal values: shows two Markov equilibria (interrupt / never interrupt).
def ABS2(psi, a, l, u, tauU, dt, T, wI_T, wS_T):
    n = int(round(T / dt)); w = wI_T; ws = wS_T
    for k in range(n - 1, -1, -1):
        t = k * dt
        cu = u * dt if t >= tauU - 1e-12 else 0.0
        ws_new = psi * max(ws - a * dt, 0.0) + (1 - psi) * min(ws, 1.0)
        cont = w - (a + l) * dt; stop = ws - a * dt
        if cont >= stop:
            eu, nxt = cont, w + cu
        else:
            eu, nxt = stop, ws
        w = psi * max(eu, 0.0) + (1 - psi) * min(nxt, 1.0)
        ws = ws_new
    return w
p = (0.5, 0.2, 0.1, 2.0, 1.0)
print("ABS, terminal (wI,wS)=(1,0):", round(ABS2(*p, 0.002, 30, 1.0, 0.0), 4))
print("ABS, terminal (wI,wS)=(0,0):", round(ABS2(*p, 0.002, 30, 0.0, 0.0), 4))
print("ABS, terminal (wI,wS)=(1,1):", round(ABS2(*p, 0.002, 30, 1.0, 1.0), 4))
