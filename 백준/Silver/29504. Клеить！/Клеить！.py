def solve(n, m, k, grid):
    visited = [bytearray(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            cnt, id = 1, grid[i][j]
            visited[i][j] = True
            st = [(i, j)]
            while st:
                x, y = st.pop()
                for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == id:
                        visited[nx][ny] = True
                        st.append((nx, ny))
                        cnt += 1
            if cnt != k:
                return "Wrong answer"
    return "OK"

g = lambda: [*map(int, input().split())]
n, m = g()
k = int(input())
grid = [g() for _ in range(n)]
print(solve(n, m, k, grid))