dp = [0, 1, 1, 1, 2]
for i in range(5, 101):
    dp.append(dp[i-1] + dp[i-5])
for _ in range(int(input())):
    print(dp[int(input())])