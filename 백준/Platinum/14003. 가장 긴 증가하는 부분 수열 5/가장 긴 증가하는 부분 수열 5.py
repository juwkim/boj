import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
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
print(len_dp)

LIS, idx = [], -1
while len_dp:
    if p[idx] == len_dp:
        LIS.append(nums[idx])
        len_dp -= 1
    idx -= 1
print(*LIS[::-1])