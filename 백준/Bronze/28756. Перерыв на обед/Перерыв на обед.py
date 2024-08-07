import sys
g = lambda: map(int, sys.stdin.readline().split())
from math import dist

ans = 1e6
xs, ys, xt, yt = g()
a, c = (xs, ys), (xt, yt)
for _ in range(int(input())):
    *b, t = g()
    ans = min(ans, dist(a, b) + dist(b, c) + t)
print(ans)