import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = [*zip(*sorted([*map(int, input().split())] for _ in range(N)))][1]
dp = [-1000000001]
p = []

for num in nums:
    if num > dp[-1]:
        dp.append(num)
        p.append(len(dp) - 1)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num
        p.append(idx)

len_dp = len(dp) - 1
print(N - len_dp)