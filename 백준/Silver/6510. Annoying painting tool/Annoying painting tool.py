import sys
input = lambda: sys.stdin.readline().rstrip()

while (l:=[*map(int, input().split())])[0]:
    n, m, r, c = l
    grid = [list(map(int, input())) for _ in range(n)]
    def flip(x, y):
        for i in range(x, x + r):
            for j in range(y, y + c):
                grid[i][j] ^= 1
    cnt = 0
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            if grid[i][j]:
                flip(i, j)
                cnt += 1
    if any(grid[i][j] for i in range(n) for j in range(m)):
        print(-1)
    else:
        print(cnt)