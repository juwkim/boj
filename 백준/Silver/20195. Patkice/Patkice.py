import sys
input = sys.stdin.readline

r, s = map(int, input().split())
grid = [input() for _ in range(r)]
currents = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def find():
    for i in range(r):
        for j in range(s):
            if grid[i][j] == 'o':
                return i, j
sx, sy = find()
ans = 1e9, ''
for d, dx, dy in zip("ENSW", (0, -1, 1, 0), (1, 0, 0, -1)):
    x, y = sx + dx, sy + dy
    steps = 1
    while 0 <= x < r and 0 <= y < s and grid[x][y] != '.':
        cell = grid[x][y]
        if cell == 'x':
            ans = min(ans, (steps, d))
            break
        if cell not in currents:
            break
        dx, dy = currents[cell]
        x += dx
        y += dy
        steps += 1

dist, direction = ans
if dist == 1e9:
    print(':(')
else:
    print(':)')
    print(direction)