import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a1, b1, c1 = g()
a2, b2, c2 = g()
h, m, s = g()
t = h * (b1 * c1) + m * c1 + s

t, s = divmod(t, c2)
h, m = divmod(t, b2)
print(h, m, s)