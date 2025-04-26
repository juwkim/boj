R, S = map(int, input().split())
grid = [[*input()] for _ in range(R)]
fields = []
for i in range(R):
    for j in range(S):
        if grid[i][j] == '0':
            continue
        st = [(i, j)]
        log = [(i, j)]
        grid[i][j] = '0'
        while st:
            x, y = st.pop()
            for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= nx < R and 0 <= ny < S and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    st.append((nx, ny))
                    log.append((nx, ny))
        fields.append((len(log), log))

for day, (_, cells) in enumerate(sorted(fields), 1):
    for i, j in cells:
        grid[i][j] = day
for row in grid:
    print(*row, sep='')