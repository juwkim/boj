import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, Q = g()
row = [0] * N
col = [0] * M
for _ in range(Q):
    op, a, v = g()
    if op == 1:
        row[a - 1] += v
    else:
        col[a - 1] += v
for i in range(N):
    print(*[row[i] + col[j] for j in range(M)])