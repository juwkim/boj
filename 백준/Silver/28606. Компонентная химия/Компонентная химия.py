import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
ans, d = 0, defaultdict(int)
for _ in range(n):
    t, x = map(int, input().split())
    x, y = x % m, (m - x) % m
    if t == 1:
        ans += d[y]
        d[x] += 1
    else:
        d[x] -= 1
        ans -= d[y]
    print(ans)