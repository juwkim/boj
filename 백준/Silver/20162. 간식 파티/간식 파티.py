import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
snack = [0] * (n + 1)
for i in range(1, n + 1):
    snack[i] = int(input())
    dp[i] = snack[i]
    for j in range(1, i):
        if snack[i] > snack[j]:
            dp[i] = max(dp[i], dp[j] + snack[i])
print(max(dp))