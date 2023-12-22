import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product, permutations
from math import gcd

def solve():
    P, Q = g()
    GCD1 = gcd(P, Q)
    P //= GCD1
    Q //= GCD1
    for a, b in product(p, t):
        for e1, e2 in permutations(e, 2):
            x, y = a * e2, b * e1
            GCD2 = gcd(x, y)
            x //= GCD2
            y //= GCD2
            if x == P and y == Q:
                return "Yes"
    return "No"
            
for tc in range(1, 1 + int(input())):
    l = []
    while len(l) != 3:
        l.extend(g())
    assert len(l) == 3
    Np, Ne, Nt = l
    p = g()
    assert len(p) == Np
    e = g()
    assert len(e) == Ne
    t = g()
    assert len(t) == Nt
    print(f'Case #{tc}:')
    for _ in range(int(input())):
        print(solve())