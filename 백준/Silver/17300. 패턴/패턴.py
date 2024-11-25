input()
c, *a = map(int, input().split())
px, py = divmod(c - 1, 3)
visited = [bytearray(3) for _ in range(3)]
visited[px][py] = 1
ans = "YES"
for c in a:
    x, y = divmod(c - 1, 3)
    if visited[x][y] or ((px == x) + (py == y) + (abs(px - x) >= 2) + (abs(py - y) >= 2) >= 2) and not visited[px + x >> 1][py + y >> 1]:
        ans = "NO"
        break
    visited[x][y] = 1
    px, py = x, y
print(ans)