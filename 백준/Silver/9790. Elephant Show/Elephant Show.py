import sys
input = sys.stdin.readline

while (l:=[*map(int, input().split())]) != [0, 0]:
    W, H = l
    a = [input() for _ in range(H)]
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if a[i][j] == 'A':
                x, y = i, j
                break
        else:
            continue
        break
    visited = [bytearray(W) for _ in range(H)]
    visited[x][y] = 1
    ans, st = 0, [(x, y)]
    while st:
        ans += 1
        x, y = st.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and a[nx][ny] != '#':
                visited[nx][ny] = 1
                st.append((nx, ny))
    print(ans)