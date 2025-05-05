import sys
from functools import lru_cache
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    @lru_cache(maxsize=None)
    def dfs(r, c):
        if not (0 <= r < h and 0 <= c < w):
            return 0
        cell = grid[r][c]
        if cell == '.':
            return dfs(r + 1, c)
        elif cell == '*':
            return (dfs(r + 1, c - 1) + dfs(r + 1, c + 1)) / 2
        return int(cell)
    print(max(dfs(0, j) for j in range(w)))