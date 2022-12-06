g = lambda: [*map(int, input().split())]

N = int(input())
dp = [1e10]
for num in g():
    if num < dp[-1]:
        dp.append(num)
    else:
        idx = 0
        for idx in range(len(dp)):
            if dp[idx] <= num:
                break
        dp[idx] = num

ans = N - (len(dp) - 1)
print(ans)