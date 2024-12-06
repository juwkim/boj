import sys
input = sys.stdin.readline

dp = [1] * 191230
for i in range(2, 191230):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
for _ in range(int(input())):
    print(dp[int(input())])