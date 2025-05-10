import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(grid):
    while True:
        changed = False
        for i in range(9):
            if grid[i].count(0) == 1:
                idx = grid[i].index(0)
                grid[i][idx] = 45 - sum(grid[i])
                changed = True
        for j in range(9):
            col = [grid[i][j] for i in range(9)]
            if col.count(0) == 1:
                idx = col.index(0)
                grid[idx][j] = 45 - sum(col)
                changed = True
        for bi in range(3):
            for bj in range(3):
                cells = []
                for i in range(3):
                    for j in range(3):
                        cells.append(grid[bi * 3 + i][bj * 3 + j])
                if cells.count(0) == 1:
                    idx = cells.index(0)
                    r = bi * 3 + idx // 3
                    c = bj * 3 + idx % 3
                    grid[r][c] = 45 - sum(cells)
                    changed = True
        if not changed:
            break
for tc in range(1, int(input()) + 1):
    grid = [[*map(int, input())] for _ in range(9)]
    input()
    solve(grid)
    print(f"Scenario #{tc}:")
    for row in grid:
        print(*row, sep='')
    print()