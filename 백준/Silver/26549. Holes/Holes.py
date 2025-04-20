import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]
    visited = [bytearray(c) for _ in range(r)]
    total_spaces = sum(grid[i].count('.') for i in range(r))
    sections = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.' and not visited[i][j]:
                sections += 1
                st = [(i, j)]
                visited[i][j] = True
                while st:
                    cx, cy = st.pop()
                    for nx, ny in (cx + 1, cy),(cx - 1, cy), (cx, cy + 1), (cx, cy - 1):
                        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            st.append((nx, ny))
    print(f"{sections} section{'s' * (sections != 1)}, {total_spaces} space{'s' * (total_spaces != 1)}")