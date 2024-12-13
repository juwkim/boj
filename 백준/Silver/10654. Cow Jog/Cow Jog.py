import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
N, T = g()
a = [g() for _ in range(N)]
ans = 1
px, pv = a.pop()
while a:
    x, v = a.pop()
    if v <= pv or (v - pv) * T < px - x:
        px, pv = x, v
        ans += 1
print(ans)