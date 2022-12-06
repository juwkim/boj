g = lambda: [*map(int, input().split())]
N = int(input())
nums = [g() for _ in range(N)]
check = set(tuple(g()) for _ in range(int(input())))

d = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])
                
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        if (i, j) not in check:
            d[i][j] = 0

for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        if d[i-1][j] or d[i][j-1]:
            d[i][j] = max(d[i][j], nums[i-1][j-1] + max(d[i-1][j], d[i][j-1]))
        
print(d[N][N])