import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
p = [0] + [*g()]
for _ in range(Q):
    cmd, a, b = g()
    if cmd == 1: p[a] = b
    else: print(abs(p[a] - p[b]))