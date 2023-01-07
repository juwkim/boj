dp = [1, 1]
for i in range(39):
    dp.append(dp[-1] + dp[-2])
while N:= int(input()):
    print(dp[N])