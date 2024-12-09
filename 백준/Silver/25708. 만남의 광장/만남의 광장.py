import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
d = [g() for _ in range(N)]
row, col = [sum(l) for l in d], [sum(l) for l in zip(*d)]
ans = -1e6
for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(M - 1):
            for l in range(k + 1, M):
                ans = max(ans, row[i] + row[j] + col[k] + col[l] - d[i][k] - d[i][l] - d[j][k] - d[j][l] + (j - i - 1) * (l - k - 1))
print(ans)