n, m = map(int, input().split())
grid = [input() for _ in range(n)]
ans, target = 0, "YOKOHAMA"
for i in range(n):
    for j in range(m):
        if grid[i][j] != 'Y':
            continue
        st = [(i, j, 0)]
        while st:
            x, y, d = st.pop()
            if d == 7:
                ans += 1
                continue
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == target[d + 1]:
                    st.append((nx, ny, d + 1))
print(ans)