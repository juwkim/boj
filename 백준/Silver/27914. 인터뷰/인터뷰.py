import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K, Q = g()
px, cnt = [0] * (N + 1), 0
for i, A in enumerate(g()):
    if A == K: cnt = 0
    else: cnt += 1
    px[i + 1] = px[i] + cnt
for X in g(): print(px[X])