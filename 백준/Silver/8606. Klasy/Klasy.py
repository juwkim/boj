def get_dic(direction, turn):
    if direction == "POLNOC":
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    elif direction == "POLUDNIE":
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    elif direction == "ZACHOD":
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    else:  # WSCHOD
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    if turn == "PRAWO":
        return dirs
    else:
        return [dirs[0], dirs[3], dirs[2], dirs[1]]

n, start_dir, turn = input().split()
n = int(n)
x1, x2, y1, y2 = map(int, input().split())

grid = [[0] * n for _ in range(n)]
if turn == "PRAWO":
    x, y = {"POLNOC": (0, 0), "POLUDNIE": (n - 1, n - 1), "ZACHOD": (0, n - 1), "WSCHOD": (n - 1, 0)}[start_dir]
else:
    x, y = {"POLNOC": (0, n - 1), "POLUDNIE": (n - 1, 0), "ZACHOD": (n - 1, n - 1), "WSCHOD": (0, 0)}[start_dir]
dic = get_dic(start_dir, turn)

idx, num = 0, 1
for _ in range(n * n):
    grid[x][y] = num
    num += 1
    nx, ny = x + dic[idx][0], y + dic[idx][1]
    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
        x, y = nx, ny
    else:
        idx = (idx + 1) % 4
        x, y = x + dic[idx][0], y + dic[idx][1]
for y in range(y2 - 1, y1 - 2, -1):
    print(*grid[y][x1 - 1:x2])