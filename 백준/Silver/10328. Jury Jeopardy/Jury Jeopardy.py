dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
change = {'F': 0, 'L': 1, 'B': 2, 'R': 3}
hmax, wmax = 100, 100
N = int(input())
print(N)
for _ in range(N):
    maze = [['#'] * wmax for _ in range(2 * hmax - 1)]
    x, y, d = hmax - 1, 0, 0
    Min_x, Max_x, Max_y = x, x, y
    maze[x][y] = '.'
    for move in input():
        d = (d + change[move]) % 4
        x += dx[d]
        y += dy[d]
        maze[x][y] = '.'

        Min_x = min(Min_x, x)
        Max_x = max(Max_x, x)
        Max_y = max(Max_y, y)

    print(Max_x - Min_x + 3, Max_y + 2)
    for i in range(Min_x - 1, Max_x + 2):
        print(*maze[i][:Max_y + 2], sep='')