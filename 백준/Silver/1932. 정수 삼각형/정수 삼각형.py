N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * N for _ in range(N)]
def solve(i, j):
    if dp[i][j]:   return dp[i][j]
    if i == N - 1: return nums[i][j]
    dp[i][j] = nums[i][j] + max(solve(i + 1, j), solve(i + 1, j + 1))
    return dp[i][j]
print(solve(0, 0))