import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, R = g()
buf = [g() for _ in range(N)]
for _ in range(R):
    for i in range(min(N, M) // 2):
        tmp = buf[i][i]
        for j in range(i + 1, M - i):
            buf[i][j - 1] = buf[i][j]
        for j in range(i + 1, N - i):
            buf[j - 1][M - i - 1] = buf[j][M - i - 1]
        for j in range(M - i - 1, i, -1):
            buf[N - i - 1][j] = buf[N - i - 1][j - 1]
        for j in range(N - i - 1, i, -1):
            buf[j][i] = buf[j - 1][i]
        buf[i + 1][i] = tmp
for i in range(N):
    print(*buf[i])