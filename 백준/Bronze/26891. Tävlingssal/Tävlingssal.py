from math import isqrt
ans = 1e12
N = int(input())
for r in range(1, isqrt(N) + 1):
    c = (N + r - 1) // r
    ans = min(ans, (r + 1) * (c + 1))
print(ans)