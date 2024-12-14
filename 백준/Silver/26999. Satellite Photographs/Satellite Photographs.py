import sys
input = sys.stdin.readline

W, H = map(int, input().split())
a = [input() for _ in range(H)]
visited = [bytearray(W) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if a[i][j] == '.' or visited[i][j]:
            continue
        cur = 0
        stack = [(i, j)]
        visited[i][j] = 1
        while stack:
            x, y = stack.pop()
            cur += 1
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and a[nx][ny] == '*' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
        ans = max(ans, cur)
print(ans)