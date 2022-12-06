N = int(input())
dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    minn = dp[i-1]
    for j in range(1, int(i**.5)+1):
        minn = min(minn, dp[i-j**2])
    dp[i] = minn + 1
    
print(dp[N])