import sys
sys.path.insert(0, '.')
from v_prop5 import formula, optimize, pos
def show(tag, b1, rc, R, e, sbar):
    a = b1 - rc
    s, Pb = formula(a, R, e, sbar); T, G = optimize(a, R, e, sbar)
    print('%-28s b1=%.2f rc=%.2f R=%.2f e=%.2f sbar=%.2f | s*=%.3f Pb(cond)=%.3f T*=%.3f maxgain=%.4f issue=%s uncondPb=%.3f'
          % (tag, b1, rc, R, e, sbar, s, Pb, T, G, G > 1e-9, Pb if G > 1e-9 else 0.0))
print('Unconditional breakdown vs b1 (rc=0,R=5,e=1,sbar=10):')
for b1 in (5.0, 6.0): show('', b1, 0, 5, 1, 10)
print('Unconditional breakdown vs sbar (b1=7,rc=0,R=5,e=1):')
for sb in (15.0, 17.0): show('', 7, 0, 5, 1, sb)
print('Unconditional breakdown vs rc (b1=7,R=5,e=1,sbar=10):')
for rc in (1.0, 1.7): show('', 7, rc, 5, 1, 10)
print('Corner a-R>=sbar: P_b flat in R (b1=5,rc=0,e=1,sbar=2):')
for R in (1.0, 1.5): show('', 5, 0, R, 1, 2)
print('\nPrimitive Q1 with -alpha1<Q1<0: b1=-Q1, e=-gN+Q1+alpha1 (alpha1=4,gN=-1,rc=0.5,R=3,sbar=6):')
for Q1 in (-1.0, -2.0, -3.0):
    a1, gN = 4.0, -1.0
    b1 = min(a1, pos(-Q1)); e = -gN + pos(Q1 + a1)
    show('Q1=%.1f' % Q1, b1, 0.5, 3, e, 6)
