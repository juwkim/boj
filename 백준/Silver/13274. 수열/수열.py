import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, K = g()
A = sorted(g())
for _ in range(K):
    L, R, X = g()
    for i in range(L - 1, R):
        A[i] += X
    A.sort()
print(*A)