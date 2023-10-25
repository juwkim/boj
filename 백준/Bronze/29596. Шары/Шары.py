import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

x1, v1 = g()
x2, v2 = g()
T = int(input())
x1f, x2f = x1 + v1 * T, x2 + v2 * T
if (x1f - x2f) * (x1 - x2) > 0:
    print(x1f, v1)
    print(x2f, v2)
else:
    t = (x2 - x1) / (v1 - v2)
    p = x1 + v1 * t
    v1, v2 = v2, v1
    x1f = p + v1 * (T - t)
    x2f = p + v2 * (T - t)
    print(round(x1f), v1)
    print(round(x2f), v2)