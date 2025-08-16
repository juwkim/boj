import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from fractions import Fraction

while n := int(input()):
    a, b = g()
    ys = g()
    p = Fraction(max(ys), 3)
    cands = {p}
    for y in ys:
        f = Fraction(y, 2)
        if f >= p:
            cands.add(f)
        f = Fraction(y)
        if f >= p:
            cands.add(f)
    ans = 1e9
    for f in cands:
        left, cnt = 0, 0
        for y in ys:
            while y > 0:
                y -= f
                cnt += 1
            left -= y
        ans = min(ans, a * left + b * cnt)
    if ans.denominator == 1:
        print(ans.numerator)
    else:
        print(f"{ans.numerator} / {ans.denominator}")