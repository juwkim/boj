def dfs(x, y, dir_idx):
    if dir_idx == len(directions):
        return 1
    dx, dy = DIRS[directions[dir_idx]]
    path = []
    nx, ny = x + dx, y + dy
    ret = 0
    while 0 <= nx < 3 and 0 <= ny < 3 and not grid[nx][ny]:
        grid[nx][ny] = True
        path.append((nx, ny))
        ret += dfs(nx, ny, dir_idx + 1)
        nx += dx
        ny += dy
    for px, py in path:
        grid[px][py] = False
    return ret
ans = 0
grid = [bytearray(3) for _ in range(3)]
DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
directions = input()
for i in range(3):
    for j in range(3):
        grid[i][j] = True
        ans += dfs(i, j, 0)
        grid[i][j] = False
print(ans)