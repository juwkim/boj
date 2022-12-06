g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
dp = [1e7 for _ in range(1 + N)]
dp[1] = 0
for i in range(1, N):
    for step in range(1, 1 + min(N - i, nums[i-1])):
        dp[i+step] = min(dp[i+step], dp[i] + 1)

print(-1 if dp[N] == 1e7 else dp[N])