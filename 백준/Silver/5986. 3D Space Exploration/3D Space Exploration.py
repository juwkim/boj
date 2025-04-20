N = int(input())
grid = [[input() for _ in range(N)] for _ in range(N)]
visited = [[bytearray(N) for _ in range(N)] for _ in range(N)]
cnt = 0
for x in range(N):
    for y in range(N):
        for z in range(N):
            if grid[x][y][z] == '*' and not visited[x][y][z]:
                cnt += 1
                st = [(x, y, z)]
                visited[x][y][z] = True
                while st:
                    cx, cy, cz = st.pop()
                    for nx, ny, nz in (cx+1, cy, cz), (cx-1, cy, cz), (cx, cy+1, cz), (cx, cy-1, cz), (cx, cy, cz+1), (cx, cy, cz-1):
                        if 0 <= nx < N and 0 <= ny < N and 0 <= nz < N and grid[nx][ny][nz] == '*' and not visited[nx][ny][nz]:
                            visited[nx][ny][nz] = True
                            st.append((nx, ny, nz))
print(cnt)