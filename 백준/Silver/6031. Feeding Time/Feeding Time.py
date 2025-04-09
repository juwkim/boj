W, H = map(int, input().split())
grid = [[*input()] for _ in range(H)]

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            grid[i][j] = '*'
            st, cnt = [(i, j)], 1
            while st:
                x, y = st.pop()
                for d in range(8):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
                        grid[nx][ny] = '*'
                        st.append((nx, ny))
                        cnt += 1
            ans = max(ans, cnt)
print(ans)