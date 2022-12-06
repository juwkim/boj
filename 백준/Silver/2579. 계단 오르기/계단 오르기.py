N = int(input())
dp = [0] * (N+1)
steps = [int(input()) for _ in range(N)]

dp[1] = steps[0]
if N > 1:
    dp[2] = steps[0] + steps[1]
    for i in range(3, N+1):
        dp[i] = steps[i-1] + max(dp[i-3] + steps[i-2], dp[i-2])
print(dp[N])