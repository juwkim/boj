from math import inf, isqrt
def g(): return [*map(int, input().split())]

def solve(num):
    
    if dp[num] != inf:
        return dp[num]

    if all(dp[int(digit)] == 1 for digit in str(num)):
        dp[num] = len(str(num))
        return dp[num]

    for i in range(2, 1 + isqrt(num)):
        q, r = divmod(num, i)
        if r:
            continue
        dp[num] = min(dp[num], solve(i) + solve(q) + 1)
    
    return dp[num]
    
for t in range(1, 1 + int(input())):
    nums = g()
    X = int(input())
    dp = [inf] * (max(10, X) + 1)
    for i in range(10):
        if nums[i]:
            dp[i] = 1

    ret = solve(X)
    if ret == inf:
        ans = 'Impossible'
    else:
        ans = ret + 1        
    print(f'Case #{t}: {ans}')