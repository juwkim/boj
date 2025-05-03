from collections import deque

n, m = map(int, input().split())
maze = [[*input()] for _ in range(n)]
entrance = 0
for i in range(n):
    for j in range(m):
        if i and j and i < n - 1 and j < m - 1 or maze[i][j] == 'X':
            continue
        maze[i][j] = 'X'
        dq = deque([(i, j)])
        dot = False
        while dq:
            x, y = dq.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] in '. ':
                    dot |= maze[nx][ny] == '.'
                    maze[nx][ny] = 'X'
                    dq.append((nx, ny))
        entrance += dot
unrechable = sum(l.count('.') for l in maze)
print(entrance, unrechable)