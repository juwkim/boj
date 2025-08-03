import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

def weighted_median(weights):
    total = sum(weights)
    cum = 0
    for i, w in enumerate(weights):
        cum += w
        if 2 * cum >= total:
            return i

for _ in range(int(input())):
    x, y = map(int, input().split())
    row_weights = [0] * y
    col_weights = [0] * x
    grid = [g() for _ in range(y)]
    for r in range(y):
        for c, d in enumerate(grid[r]):
            row_weights[r] += d
            col_weights[c] += d
    best_r = weighted_median(row_weights)
    best_c = weighted_median(col_weights)
    cost = 0
    for r in range(y):
        dr = abs(r - best_r)
        for c in range(x):
            dc = abs(c - best_c)
            cost += grid[r][c] * (dr + dc)
    print(f"{cost} blocks")