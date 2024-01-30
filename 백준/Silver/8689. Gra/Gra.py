import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = [0] * 5 + g()
dp = [0] * (n + 5)
for i in range(6):
    dp[i] = nums[5]
for i in range(6, n + 5):
    dp[i] = max(dp[j] for j in range(i - 6, i)) + nums[i]
print(dp[-1])