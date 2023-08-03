from collections import deque
g = lambda: [*map(int, input().split())]

n, m = g()
Map = [g() for _ in range(n)]

a1, a2 = None, None
for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            a1, a2 = i, j
            break
    else:
        continue
    break

dist = [[-(Map[i][j] != 0) for j in range(m)] for i in range(n)]
visited = [bytearray(m) for _ in range(n)]

dist[a1][a2] = 0
visited[a1][a2] = True
dq = deque([(a1, a2, 1)])
while dq:
    p, q, step = dq.popleft()
    for s, t in ((p + 1, q), (p - 1, q), (p, q + 1), (p, q - 1)):
        if s < 0 or s >= n or t < 0 or t >= m:
            continue
        if Map[s][t] == 0:
            continue
        if visited[s][t]:
            continue
        dist[s][t] = step
        visited[s][t] = True
        dq.append((s, t, step + 1))
for line in dist:
    print(*line)