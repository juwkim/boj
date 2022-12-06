g = lambda: [*map(int, input().split())]

from math import gcd
N, S = g()
num, *A = g()
ans = abs(S - num)
for num in A:
    ans = gcd(ans, abs(S - num))
print(ans)