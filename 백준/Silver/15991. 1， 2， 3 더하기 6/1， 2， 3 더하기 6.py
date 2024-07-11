dp = [1, 2, 3]
for i in range(3, 50001):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
for _ in range(int(input())):
    print(dp[int(input()) >> 1])