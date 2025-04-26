N = int(input())
dp = [1] * (N + 1)
for i in range(1, N):
    num = i + sum(int(digit) for digit in str(i))
    if num <= N:
        dp[num] += dp[i]
print(dp[N])