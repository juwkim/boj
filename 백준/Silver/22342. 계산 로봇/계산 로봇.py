M, N = map(int, input().split())
a = [[0] * N] + [[int(c) for c in input()] for _ in range(M)] + [[0] * N]
dp = [0] * (M + 2)
for j in range(N - 1):
    new = [0] * (M + 2)
    for i in range(1, M + 1):
        new[i] = max(dp[k] + a[k][j] for k in range(i - 1, i + 2))
    dp = new
print(max(dp))