import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from math import isqrt
N = int(input())
dp = [0] * (N + 1)
def solve(num):
    if dp[num]:
        return dp[num]
    
    tmp = isqrt(num)
    if num == tmp ** 2:
        dp[num] = 1
        return 1
    
    if num == tmp ** 2 + 1:
        dp[num] = 2
        return 2
    
    val = 1e9
    for i in range(1, int(num ** .5) + 1):
        val = min(val, 1 + solve(num - i * i))
    dp[num] = val
    return dp[num]
    

solve(N)
print(dp[N])