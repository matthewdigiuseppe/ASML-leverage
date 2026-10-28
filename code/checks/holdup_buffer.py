# Hold-up with a European buffer: Europe more vulnerable post-buffer but tau_E > tau_U still yields a positive share.
def run(psi, a, l, u, tauE, tauU, dt, T, wT):
    n = int(round(T / dt)); w = wT
    for k in range(n - 1, -1, -1):
        t = k * dt
        ce = (l + (a if t >= tauE else 0.0)) * dt
        cu = (u if t >= tauU else 0.0) * dt
        w = psi * max(w - ce, 0.0) + (1 - psi) * min(w + cu, 1.0)
    return w
psi, a, l, u, tauE, tauU = 0.5, 3.0, 0.1, 1.0, 2.0, 0.5   # post-buffer: psi*(a+l)=1.55 > (1-psi)*u=0.5 (Europe more vulnerable)
for wT in (0.0, 1.0):
    print("share with interruption:", round(run(psi, a, l, u, tauE, tauU, 0.001, 40, wT), 4), " without (u=0):", round(run(psi, a, 0.0, 0.0, tauE, tauU, 0.001, 40, wT), 4))
