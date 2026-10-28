"""Lemma 3: period-2 extension of the cut. In period 2 (Europe in control after refusal), the US
decides whether to continue the cut, with period-2 audience cost m2 and direct gain gN2 = nu2 - kA.
Continue iff gN2 - [Q2+a2]^+ >= -m2 - [Q2]^+.  Europe's loss from continuation b2 = a2 - ([Q2+a2]^+-[Q2]^+)."""
import random
def pos(x): return x if x > 0 else 0.0
rng = random.Random(4); bad = 0; n = 0; bite_pos_when_Q2pos = 0
for i in range(200000):
    Q2 = rng.uniform(-5, 5); a2 = rng.uniform(0, 5); gN2 = -rng.uniform(0, 3); m2 = rng.uniform(0, 8)
    extra = pos(Q2 + a2) - pos(Q2)
    if Q2 >= 0 and abs(extra - a2) > 1e-12: bad += 1
    cont = (gN2 - pos(Q2 + a2)) >= (-m2 - pos(Q2))
    if cont != (m2 >= extra - gN2): bad += 1
    b2 = a2 - extra
    if Q2 >= 0 and b2 > 1e-12: bite_pos_when_Q2pos += 1
    n += 1
print('draws', n, 'violations', bad, 'positive period-2 bite with Q2>=0:', bite_pos_when_Q2pos)
