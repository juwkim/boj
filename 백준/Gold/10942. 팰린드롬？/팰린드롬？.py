import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
M = int(input())
dp = [[1, 1] + [0 for _ in range(N-1)] for _ in range(N+1)]

for size in range(2, N+1):
    for start in range(1, N - size + 2):
        if dp[start+1][size-2] and nums[start-1] == nums[start+size-2]:
            dp[start][size] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E-S+1])