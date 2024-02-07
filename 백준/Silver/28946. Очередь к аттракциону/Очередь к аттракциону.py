import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, m, t = g()
a = g()
if n & 1:
    x = sum(i <= t for i in g())
    print(sum(a[1:]), x)
else:
    print(sum(a), 0)