g = lambda: [*map(int, input().split())]
from bisect import bisect_left

N = int(input())

switch = g()
switch_dic = {num: idx for idx, num in enumerate(switch)}
bulbs = g()


dp = [-1]
p = []
for bulb in bulbs:
    num = switch_dic[bulb]
    if num > dp[-1]:
        dp.append(num)
        p.append(len(dp) - 1)
    else:
        idx = bisect_left(dp, num)
        dp[idx] = num
        p.append(idx)
    
len_dp = len(dp) - 1
print(len_dp)

LIS, idx = [], -1
while len_dp:
    if p[idx] == len_dp:
        LIS.append(bulbs[idx])
        len_dp -= 1
    idx -= 1
print(*sorted(LIS))