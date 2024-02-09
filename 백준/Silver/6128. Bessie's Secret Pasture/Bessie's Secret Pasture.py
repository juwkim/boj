N = int(input())
dp = [0] * 10001
for i in range(int(N ** 0.5) + 1):
    for j in range(int((N - i * i)**.5) + 1):
        dp[i * i + j * j] += 1
ans = sum(dp[i] * dp[N - i] for i in range(N + 1))
print(ans)