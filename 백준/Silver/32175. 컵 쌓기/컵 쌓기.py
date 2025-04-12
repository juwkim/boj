N, H, *A = map(int, open(0).read().split())
dp = [0] * (H + 1)
dp[0] = 1
for i in range(H):
    for num in A:
        if i + num <= H:
            dp[i + num] = (dp[i + num] + dp[i]) % 1000000007
print(dp[H])