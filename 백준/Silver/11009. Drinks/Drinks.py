import sys
input = sys.stdin.readline
from math import perm
from fractions import Fraction

for _ in range(int(input())):
    n, m = map(int, input().split())
    f = sum(Fraction(n * perm(m, i), (n + m) * perm(n + m - 1, i)) for i in range(0, m + 1, 2))
    print(f)