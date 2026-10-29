# Prop 6(a) proof wording: does w(t) fall or rise moving FORWARD in time between the buffer dates?
def path(psi, cE, cU, tauE, tauU, dt=1e-3, tail=30.0):
    n = int((max(tauE, tauU) + tail) / dt); w = 0.5; ws = {}
    for k in range(n - 1, -1, -1):
        t = k * dt
        hE = cE * dt if t >= tauE else 0.0; hU = cU * dt if t >= tauU else 0.0
        w = psi * max(w - hE, 0.0) + (1 - psi) * min(1.0, w + hU)
        ws[k] = w
    return ws
psi, dt = 0.5, 1e-3
ws = path(psi, cE=0.2, cU=2.0, tauE=1.0, tauU=3.0)   # D>0, Europe less vulnerable post-buffer
print("D>0: w(tauE=1) =", round(ws[int(1.0/dt)], 3), " w(2) =", round(ws[int(2.0/dt)], 3), " w(tauU=3) =", round(ws[int(3.0/dt)], 3), "-> rises moving forward")
ws = path(psi, cE=2.0, cU=0.2, tauE=3.0, tauU=1.0)   # D<0, Europe more vulnerable post-buffer
print("D<0: w(tauU=1) =", round(ws[int(1.0/dt)], 3), " w(2) =", round(ws[int(2.0/dt)], 3), " w(tauE=3) =", round(ws[int(3.0/dt)], 3), "-> falls moving forward")
