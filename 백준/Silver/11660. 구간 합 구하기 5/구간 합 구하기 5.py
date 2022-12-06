import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [[0 for _ in range(N+1)]] + [[0] + [*map(int, input().split())] for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, N):
        nums[i][j+1] += nums[i][j]
for i in range(1, N):
    for j in range(1, N+1):
        nums[i+1][j] += nums[i][j]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = nums[x2][y2] + nums[x1-1][y1-1] - nums[x2][y1-1] - nums[x1-1][y2]
    print(ans)