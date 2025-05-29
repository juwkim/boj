import sys
input = sys.stdin.readline
mod = 10**9 + 7

N, M, K = map(int, input().split())
maze = [input() for _ in range(M)]
cnt1 = [[0] * (N + 1) for _ in range(M + 1)] # cnt1[i][j] = number of ways to reach (i - 1, j - 1) from (0, 0)
cnt1[0][1] = 1
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if maze[i - 1][j - 1] != '1':
            cnt1[i][j] = (cnt1[i - 1][j] + cnt1[i][j - 1]) % mod
cnt2 = [[0] * (N + 2) for _ in range(M + 2)] # cnt2[i][j] = number of ways to reach (M - 1, N - 1) from (i - 1, j - 1)
cnt2[M][N+1] = 1
for i in range(M, 0, -1):
    for j in range(N, 0, -1):
        if maze[i - 1][j - 1] != '1':
            cnt2[i][j] = (cnt2[i + 1][j] + cnt2[i][j + 1]) % mod
ans = cnt1[M][N]
for _ in range(K):
    x1, y1, x2, y2 = map(lambda x: int(x) + 1, input().split())
    if (x2, y2) not in ((x1, y1 + 1), (x1 + 1, y1)):
        ans += cnt1[y1][x1] * cnt2[y2][x2]
    if (x1, y1) not in ((x2, y2 + 1), (x2 + 1, y2)):
        ans += cnt1[y2][x2] * cnt2[y1][x1]
    ans %= mod
print(ans)