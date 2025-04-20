import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, m = g()
ans = N + 1
s, e = 0, 0
for c, d in sorted(g() for _ in range(m)):
    if c <= e:
        e = max(e, d)
    else:
        ans += 2 * (e - s)
        s, e = c, d
ans += 2 * (e - s)
print(ans)