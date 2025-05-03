n, m = map(int, input().split())
maze = [[*input()] for _ in range(n)]
entrance = 0
for i in range(n):
    for j in range(m):
        if i and j and i < n - 1 and j < m - 1 or maze[i][j] == 'X':
            continue
        maze[i][j] = 'X'
        st = [(i, j)]
        dot = False
        while st:
            x, y = st.pop()
            for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] in '. ':
                    dot |= maze[nx][ny] == '.'
                    maze[nx][ny] = 'X'
                    st.append((nx, ny))
        entrance += dot
unrechable = sum(l.count('.') for l in maze)
print(entrance, unrechable)