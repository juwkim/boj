import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[*input()] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'H':
            grid[i][j] = '#'
            x, y = i, j
            break
    else:
        continue
    break
ans = "NEJ"
st = [(x, y)]
while st:
    x, y = st.pop()
    if grid[x][y] == 'H':
        ans = "JA"
        break
    for dx, dy in (-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
            if grid[nx][ny] == '.':
                grid[nx][ny] = '#'
            st.append((nx, ny))
print(ans)