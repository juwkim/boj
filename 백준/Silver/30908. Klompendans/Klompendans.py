from collections import deque

n, a, b, c, d = map(int, open(0).read().split())
l = ((a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)), ((c, d), (c, -d), (-c, d), (-c, -d), (d, c), (d, -c), (-d, c), (-d, -c))
visited = [[[0, 0] for _ in range(n)] for _ in range(n)]
visited[0][0] = [1, 1]
dq = deque([(0, 0, 0), (0, 0, 1)])
while dq:
    x, y, mod = dq.popleft()
    for dx, dy in l[mod & 1]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny][mod]:
            visited[nx][ny][mod] = 1
            dq.append((nx, ny, mod ^ 1))
print(sum(any(visited[i][j]) for i in range(n) for j in range(n)))