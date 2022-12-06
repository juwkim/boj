import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]
from bisect import bisect_left

N = int(input())

dp = [-1]
for num in g():
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = bisect_left(dp, num)
        dp[idx] = num
len_dp = N - len(dp) + 1
print(len_dp)