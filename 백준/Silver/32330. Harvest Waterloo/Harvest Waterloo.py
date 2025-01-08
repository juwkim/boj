import sys
input = sys.stdin.readline

R, C = int(input()), int(input())
a = [input() for _ in range(R)]
A, B = int(input()), int(input())
visited = [bytearray(C) for _ in range(R)]
visited[A][B] = 1
ans, st = 0, [(A, B)]
d = {'S': 1, 'M': 5, 'L': 10}
while st:
    x, y = st.pop()
    ans += d[a[x][y]]
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and a[nx][ny] != '*':
            visited[nx][ny] = 1
            st.append((nx, ny))
print(ans)