import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
p = [True] * (N + 1)
for i in range(2, int(N**.5) + 1):
    if p[i]:
        for j in range(i * i, N + 1, i):
            p[j] = False
px = [0] * (N + 1)
for i in range(1, N + 1):
    px[i] = px[i - 1] + p[i]
for _ in range(M):
    a, b = g()
    print(px[b] - px[a - 1])