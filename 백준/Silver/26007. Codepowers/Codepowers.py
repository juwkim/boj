import sys

g = lambda: map(int, sys.stdin.readline().split())
N, M, K, score = g()
px = [0]
for A in g():
    score += A
    px.append(px[-1] + (score < K))
for _ in range(M):
    l, r = g()
    print(px[r - 1] - px[l - 1])