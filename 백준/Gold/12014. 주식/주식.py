import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]
from bisect import bisect_left

for cnt in range(1, 1 + int(input())):
    N, K = g()
    dp = [-1]
    for num in g():
        if num > dp[-1]:
            dp.append(num)
        else:
            idx = bisect_left(dp, num)
            dp[idx] = num
    print(f'Case #{cnt}')
    len_dp = len(dp) - 1
    print(+(len_dp >= K))