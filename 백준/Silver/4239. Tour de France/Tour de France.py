import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product

while input() != "0":
    buf = sorted(a / b for a, b in product(g(), g()))
    ans = max(t / s for s, t in zip(buf, buf[1:]))
    print("%.2f" % ans)