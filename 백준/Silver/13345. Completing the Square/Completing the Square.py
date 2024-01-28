import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
dist2 = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

a, b, c = g(), g(), g()
if dist2(a, b) == dist2(a, c):
    p, q, r = b, c, a
elif dist2(b, c) == dist2(b, a):
    p, q, r = c, a, b
else:
    p, q, r = a, b, c
x = p[0] + q[0] - r[0]
y = p[1] + q[1] - r[1]
print(x, y)