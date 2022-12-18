g = lambda: [*map(int, input().split())]

from math import dist
N = int(input())
P = g()
Q = min([g() for _ in range(N - 1)], key=lambda X: dist(P, X))
print(*P)
print(*Q)
print("%.2f" % dist(P, Q))