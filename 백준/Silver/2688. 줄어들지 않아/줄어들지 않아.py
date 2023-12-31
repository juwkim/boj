dp = [[0], [1] * 10]
for i in range(2, 65):
    dp.append([sum(dp[i-1][:j+1]) for j in range(10)])
ans = [sum(l) for l in dp]
for _ in range(int(input())):
    print(ans[int(input())])