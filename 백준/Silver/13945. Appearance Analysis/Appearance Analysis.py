r, c = map(int, input().split())
grid = [input() for _ in range(r)]

Rf = [i for i in range(r) if grid[i] == '#' * c]
Cf = [j for j in range(c) if all(grid[i][j] == '#' for i in range(r))]
H = Rf[1] - Rf[0] - 1
W = Cf[1] - Cf[0] - 1

designs = set()
for i in range(1, r, H + 1):
    for j in range(1, c, W + 1):
        mat = [grid[k][j:j+W] for k in range(i, i+H)]
        normalized = None
        for _ in range(4):
            mat = [l[::-1] for l in zip(*mat)]
            if normalized is None or mat < normalized:
                normalized = mat
        designs.add(tuple(normalized))
print(len(designs))