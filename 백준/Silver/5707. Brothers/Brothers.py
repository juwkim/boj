import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

while True:
    N, R, C, K = g()
    if N == 0: break
    grid = [g() for _ in range(R)]
    for _ in range(K):
        next_grid = [row[:] for row in grid]
        for r in range(R):
            for c in range(C):
                for nr, nc in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == (grid[r][c] + 1) % N:
                            next_grid[nr][nc] = grid[r][c]
        grid = next_grid
    for row in grid:
        print(*row)