import sys
input = sys.stdin.readline

n = int(input())
a = [input() for _ in range(n)]
visited = [bytearray(n) for _ in range(n)]
st = [(0, 0)]
ans = "No"
while st:
    x, y = st.pop()
    if x == n - 1 and y == n - 1:
        ans = "Yes"
        break
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or a[x][y] == 'x':
        continue
    visited[x][y] = 1
    for dx, dy in (1, 0), (0, 1):
        st.append((x + dx, y + dy))
print(ans)