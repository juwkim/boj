import sys
input = sys.stdin.readline

for _ in range(int(input())):
    L, W, A, B, C, D = map(int, input().split())
    grid = [input() for _ in range(W)]
    ax, ay = W - B, A - 1
    bx, by = W - D, C - 1
    visited = [bytearray(L) for _ in range(W)]
    visited[ax][ay] = True
    st = [(ax, ay)]
    ans = "NO"
    while st:
        x, y = st.pop()
        if (x, y) == (bx, by):
            ans = "YES"
            break
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < L and not visited[nx][ny] and grid[nx][ny] == grid[ax][ay]:
                visited[nx][ny] = True
                st.append((nx, ny))
    print(ans)