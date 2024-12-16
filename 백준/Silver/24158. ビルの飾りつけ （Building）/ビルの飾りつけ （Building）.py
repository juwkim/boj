import sys
input = sys.stdin.readline
from bisect import bisect_left

dp = [0]
for _ in range(int(input())):
    a = int(input())
    if a > dp[-1]:
        dp.append(a)
    else:
        dp[bisect_left(dp, a)] = a
print(len(dp) - 1)