N = int(input())
dp = [*range(-1, N)]
x = [0 for _ in range(N+1)]

for i in range(2, N+1):
    if i % 3 == 0 and dp[i] > dp[i//3]:
        dp[i] = 1 + dp[i//3]
        x[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i//2]:
        dp[i] = 1 + dp[i//2]
        x[i] = i // 2
    if dp[i] > dp[i-1]:
        dp[i] = 1 + dp[i-1]
        x[i] = i-1

print(dp[N])
while N:
    print(N, end=" ")
    N = x[N]