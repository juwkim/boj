import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
X = [1] * (N + 1)
for _ in range(M):
    a, b, c = g()
    X[a] = max(X[a], c)
    X[b] = max(X[b], c)
print(*X[1:])