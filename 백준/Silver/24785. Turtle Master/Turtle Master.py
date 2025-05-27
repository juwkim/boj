dx = 0, 1, 0, -1
dy = 1, 0, -1, 0
def solve():
    grid = [list(input()) for _ in range(8)]
    x, y, d = 7, 0, 0
    for cmd in input():
        match cmd:
            case 'F':
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < 8 and 0 <= ny < 8) or grid[nx][ny] not in '.D':
                    return "Bug!"
                x, y = nx, ny
            case 'R':
                d = (d + 1) % 4
            case 'L':
                d = (d - 1) % 4
            case 'X':
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < 8 and 0 <= ny < 8) or grid[nx][ny] != 'I':
                    return "Bug!"
                grid[nx][ny] = '.'
    if grid[x][y] == 'D':
        return "Diamond!"
    return "Bug!"
print(solve())