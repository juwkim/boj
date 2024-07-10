import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
X, Y = zip(*[g() for _ in range(M)])
X, Y = sorted(X), sorted(Y)
dx = sum(X[i] - X[0] for i in range(1, M))
dy = sum(Y[i] - Y[0] for i in range(1, M))
dxmin, dymin = dx, dy
for i in range(1, M):
    dx += (2 * i - M) * (X[i] - X[i - 1])
    dy += (2 * i - M) * (Y[i] - Y[i - 1])
    dxmin, dymin = min(dxmin, dx), min(dymin, dy)
print(dxmin + dymin)