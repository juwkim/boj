from bisect import bisect_left

dp = [0]
for num in map(int, open(0).read().split()[1:]):
    if num > dp[-1]:
        dp.append(num)
    else:
        dp[bisect_left(dp, num)] = num
print(len(dp) - 1)