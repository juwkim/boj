dp = [1]
for i in range(1, 1 + int(input())):
    num = 0
    for j in range(i):
        num += dp[j] * dp[i-j-1]
    dp.append(num)
print(dp[-1])