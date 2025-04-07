N, *a = map(int, open(0).read().split())
dp = []
for num in a:
    for i in range(len(dp)):
        if dp[i][0] >= num:
            dp[i][0] += num
            dp[i][1] += 1
    dp.append([num, 1])
print(max(v for _, v in dp))