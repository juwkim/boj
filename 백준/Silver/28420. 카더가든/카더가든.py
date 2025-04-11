import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
a, b, c = g()
A = [g() for _ in range(N)]
px = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    cur = 0
    for j in range(M):
        cur += A[i][j]
        px[i + 1][j + 1] = cur + px[i][j + 1]
def get_sum(i, j, h, w):
    return px[i + h][j + w] - px[i][j + w] - px[i + h][j] + px[i][j]
ans = 1e9
for i in range(N + 1 - a):
    for j in range(M + 1 - b - c):
        ans = min(ans, get_sum(i, j, a, b + c))
for i in range(N + 1 - a - b):
    for j in range(M + 1 - a - c):
        ans = min(ans, get_sum(i, j, a, c) + get_sum(i + a, j + c, b, a))
for i in range(N + 1 - a - c):
    for j in range(M + 1 - a - b):
        ans = min(ans, get_sum(i, j, a, b) + get_sum(i + a, j + b, c, a))
print(ans)