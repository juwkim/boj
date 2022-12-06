N, M = map(int, input().split())
sack = [*map(int, input().split())]
cost = [*map(int, input().split())]
dp = [0 for _ in range(10001)]

def solve():
    size = sum(cost)
    for i in range(N):
        for j in range(size, cost[i]-1, -1):
            dp[j] = max(dp[j], dp[j - cost[i]] + sack[i])
    
    ans, i = -1, 0
    while ans == -1:
        if dp[i] < M:
            i += 1
            continue
        ans = i
    return ans
print(solve())