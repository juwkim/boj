import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

def solve(r, c, cnt):
    if cnt == K or c == N:
        return 0
    if dp[r][c][cnt] != -1:
        return dp[r][c][cnt]
    dp[r][c][cnt] = a[r][c] + solve(r, c + 1, cnt + 1)
    if cnt + 2 <= K:
        dp[r][c][cnt] = max(dp[r][c][cnt], a[r][c] + a[r ^ 1][c] + solve(r ^ 1, c + 1, cnt + 2)) 
    return dp[r][c][cnt]

N, K = g()
a = g(), g()
dp = [[[-1] * (K + 1) for _ in range(N)] for _ in range(2)]
print(solve(1, 0, 0))