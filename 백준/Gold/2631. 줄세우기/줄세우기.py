from bisect import bisect_left

N = int(input())
dp = []
for _ in range(N):
    num = int(input())
    idx = bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num
print(N - len(dp))