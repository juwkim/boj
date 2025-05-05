import sys
g = lambda: map(int, sys.stdin.readline().split())

def solve():
    h, w = g()
    grid = [[-1]*w for _ in range(h)]
    for i, r in enumerate(g()):
        for j in range(r):
            grid[i][j] = 1
        if r < w:
            grid[i][r] = 0
    for j, c in enumerate(g()):
        for i in range(c):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 1
        if c < h:
            if grid[c][j] == 1:
                return 0
            grid[c][j] = 0
    return pow(2, sum(row.count(-1) for row in grid), 10**9 + 7)
print(solve())