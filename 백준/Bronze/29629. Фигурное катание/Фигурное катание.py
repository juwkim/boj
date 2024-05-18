import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from math import inf

n, m, x, y = g()
dp = [0, *[inf] * m]
for _ in range(n):
    tmp = [inf] * (m + 1)
    b, a = g()
    for w in range(b, a + 1):
        add = 0 if w == 0 else (x if w < 10 else y)
        for t in range(m + 1 - w):
            tmp[t + w] = min(tmp[t + w], dp[t] + add)
    dp = tmp
print(-1 if dp[m] == inf else dp[m])