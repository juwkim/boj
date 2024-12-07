import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, K, score = g()
px = [0] * (N + 1)
for i, num in enumerate(g()):
    score += num
    px[i + 1] = px[i] + (score < K)
for _ in range(M):
    l, r = g()
    print(px[r - 1] - px[l - 1])