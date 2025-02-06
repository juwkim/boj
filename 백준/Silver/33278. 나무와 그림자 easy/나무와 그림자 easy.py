import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, t = g()
X, H = -1e9, 0
ans = 0
for x, h in sorted(g() for _ in range(N)):
    p = H - t * (x - X)
    if p > h:
        ans += h
    else:
        ans += max(0, p)
        X, H = x, h
print(ans)