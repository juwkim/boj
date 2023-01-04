def g(): return [*map(int, input().split())]

from math import comb
while sum(l:= g()):
    n, m = l
    print(comb(n + m, m))