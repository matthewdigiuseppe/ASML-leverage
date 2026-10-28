import random, sys
sys.path.insert(0, '.')
from v_lemma2_prop4 import spe_outcomes, predicted, draw, pos
rng = random.Random(3)
from collections import Counter
C = Counter(); ex = {}
for i in range(200000):
    mode = 'cont' if i % 2 == 0 else 'grid'
    p = draw(rng, mode); Q1,Q2,a1,gN,mbar,sig,rc,d = p
    ok,Tstar,Epay,b1,cs = predicted(*p)
    outs = spe_outcomes(*p)
    acc = any(o[0]=='issue_accept' for o in outs)
    oth = any(o[0]!='issue_accept' for o in outs)
    if ok and oth:
        k = 'pred YES, other SPE exists'
    elif (not ok) and acc:
        if Q2 <= 0 and b1 > 0 and b1 > sig+rc and cs[1]: k = 'pred NO, accepted-ultimatum SPE: Q2<=0, b1>sig+rc (open set)'
        elif Q2 <= 0 and b1 > 0 and b1 == sig+rc: k = 'pred NO: Q2<=0, b1==sig+rc'
        elif sig+rc == 0: k = 'pred NO: sig+rc==0 (zero-parameter tie)'
        elif Q2 > 0 and b1 == sig+rc: k = 'pred NO: Q2>0, b1==sig+rc (knife edge)'
        else: k = 'pred NO: other'
    else:
        continue
    C[k] += 1; ex.setdefault(k, (mode, p, outs))
for k,v in C.items():
    print(v, k); print('    e.g.', ex[k][0], ex[k][1])
