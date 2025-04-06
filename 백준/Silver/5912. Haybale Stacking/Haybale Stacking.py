import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K = g()
px = [0] * (N + 1)
for _ in range(K):
    A, B = g()
    px[A - 1] += 1
    px[B] -= 1
for i in range(N):
    px[i + 1] += px[i]
print(sorted(px[:-1])[N >> 1])