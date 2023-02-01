def g(): return [*map(int, input().split())]

from fractions import Fraction

n, p, q = g()
Min, Max = Fraction(1, p), Fraction(1, q)
ans = []
for i in range(1, n):
    for j in range(1, n + 1):
        s = Fraction(i, j)
        if Min < s < Max:
            ans.append(s)

print(*sorted(set(ans)))