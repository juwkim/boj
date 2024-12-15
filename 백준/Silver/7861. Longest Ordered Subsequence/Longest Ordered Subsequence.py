from bisect import bisect_left

N, *a = map(int, open(0).read().split())
dp = [-1]
for num in a:
    if num > dp[-1]:
        dp.append(num)
    else:
        dp[bisect_left(dp, num)] = num
print(len(dp) - 1)