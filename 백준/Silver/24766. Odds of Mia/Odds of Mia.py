from itertools import product
from math import gcd

def solve(p):
    s0, s1 = sorted(p[:2])
    r0, r1 = sorted(p[2:])
    if (r0, r1) == (1, 2):    return 0
    if (s0, s1) == (1, 2):    return 1
    if s0 == s1 and r0 == r1: return +(s0 > r0)
    if s0 == s1:              return 1
    if r0 == r1:              return 0
    return +(s1 * 10 + s0 > r1 * 10 + r0)

while (l:=input()) != "0 0 0 0":
    p = [int(x) if x != '*' else '*' for x in l.split()]
    cnt = p.count('*')
    if cnt == 0:
        print(solve(p))
    else:
        win = 0
        idx = [i for i, x in enumerate(p) if x == '*']
        for s in product(range(1, 7), repeat=cnt):
            for i, x in zip(idx, s):
                p[i] = x
            win += solve(p)
        r = 6**cnt
        if win == r:
            print(1)
        elif win == 0:
            print(0)
        else:
            g = gcd(win, (r:=6**cnt))
            print(f"{win//g}/{r//g}")