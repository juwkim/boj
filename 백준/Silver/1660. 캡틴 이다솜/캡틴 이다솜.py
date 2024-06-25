import sys
input = sys.stdin.readline

n = int(input())
a = [i * (i + 1) * (i + 2) // 6 for i in range(121)]
dp = [1e9] * (n + 1)
for i in range(1, n + 1):
    for num in a:
        if num == i:
            dp[i] = 1
            break
        elif num > i:
            break
        dp[i] = min(dp[i], dp[i - num] + 1)
print(dp[n])