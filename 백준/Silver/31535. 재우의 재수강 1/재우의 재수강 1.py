import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

w, h = g()
n, d = g()
a = [0] + g()
p = g()
ans = 1e9
l, r = 0, 0
for i in range(n):
    if d > a[i + 1]:
        r += (a[i + 1] - a[i]) * p[i]
    else:
        r += (d - a[i]) * p[i]
        break
for i in range(n - 1):
    ans = min(ans, p[i] * w + l + abs(r))
    l += (a[i + 1] - a[i]) * p[i]
    r -= (a[i + 1] - a[i]) * p[i]
ans = min(ans, p[n - 1] * w + l + abs(r))
print(ans)