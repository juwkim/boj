import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
ans = 1e9
for _ in range(m):
    u, d = g()
    i = d * n // (u + d) + 1
    ans = min(ans, u * i - d * (n - i))
print(ans)