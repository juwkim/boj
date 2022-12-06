import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]
from bisect import bisect_left
for cnt in range(1, 1 + int(input())):
    N = int(input())
    dp = [-1e10]
    
    for num in g():
        if num > dp[-1]:
            dp.append(num)
        else:
            idx = bisect_left(dp, num)
            dp[idx] = num

    ans = N - (len(dp) - 1)
    print(f'Case #{cnt}: {ans}')