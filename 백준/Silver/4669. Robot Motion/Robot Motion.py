import sys
input = sys.stdin.readline

dx = {'N': -1, 'S': 1, 'E': 0, 'W': 0}
dy = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
while (l:=[*map(int, input().split())])[0]:
    R, C, E = l
    grid = [input() for _ in range(R)]
    visited = [[-1] * C for _ in range(R)]
    x, y, step = 0, E - 1, 0
    while 0 <= x < R and 0 <= y < C:
        if visited[x][y] != -1:
            s = visited[x][y]
            print(f"{s} step(s) before a loop of {step - s} step(s)")
            break
        visited[x][y] = step
        c = grid[x][y]
        x, y = x + dx[c], y + dy[c]
        step += 1
    else:
        print(f"{step} step(s) to exit")