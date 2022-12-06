import sys
input = sys.stdin.readline

g = lambda: map(int, input().split())
N = int(input())
nums = [list(g()) for _ in range(N)]
check = set(tuple(g()) for _ in range(int(input())))

d0 = [[0] * (N + 1) for _ in range(N + 1)]
d1 = [[0] * (N + 1) for _ in range(N + 1)]
d2 = [[0] * (N + 1) for _ in range(N + 1)]
d3 = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        if (i, j) in check:
            if d0[i-1][j] or d0[i][j-1]:
                d1[i][j] = nums[i-1][j-1] + max(d0[i-1][j], d0[i][j-1])
            if d1[i-1][j] or d1[i][j-1]:
                d2[i][j] = nums[i-1][j-1] + max(d1[i-1][j], d1[i][j-1])
            if d2[i-1][j] or d2[i][j-1]:
                d3[i][j] = nums[i-1][j-1] + max(d2[i-1][j], d2[i][j-1])
        else:
            d0[i][j] = nums[i-1][j-1] + max(d0[i-1][j], d0[i][j-1])
            if d1[i-1][j] or d1[i][j-1]:
                d1[i][j] = nums[i-1][j-1] + max(d1[i-1][j], d1[i][j-1])
            if d2[i-1][j] or d2[i][j-1]:
                d2[i][j] = nums[i-1][j-1] + max(d2[i-1][j], d2[i][j-1])
            if d3[i-1][j] or d3[i][j-1]:
                d3[i][j] = nums[i-1][j-1] + max(d3[i-1][j], d3[i][j-1])
print(d3[N][N] if d3[N][N] else -1)