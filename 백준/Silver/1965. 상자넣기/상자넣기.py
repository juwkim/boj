import sys
import bisect
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
dp = [-1000000001]

for num in g():
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num

print(len(dp) - 1)