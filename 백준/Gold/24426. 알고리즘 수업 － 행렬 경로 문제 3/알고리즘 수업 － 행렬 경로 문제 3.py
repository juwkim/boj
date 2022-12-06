g = lambda: [*map(int, input().split())]
N = int(input())
nums = [g() for _ in range(N)]
r, c = g()

d = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, 1 + r):
    for j in range(1, 1 + c):
        d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])

for i in range(r, 1 + N):
    for j in range(c, 1 + N):
        d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])
print(d[N][N], end=' ')

if r == 1:
    for i in range(c-1, N):
        nums[0][i] = -1e10
elif c == 1:
    for i in range(r-1, N):
        nums[i][0] = -1e10
else:
    nums[r-1][c-1] = -1e10

d = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])
print(d[N][N])