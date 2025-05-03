import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
for _ in range(int(input())):
    input()
    x, y = 0, 0
    graph = defaultdict(set)
    for _ in range(int(input())):
        dx, dy = dirs[input()]
        nx, ny = x + dx, y + dy
        graph[(x, y)].add((nx, ny))
        graph[(nx, ny)].add((x, y))
        x, y = nx, ny
    dq = deque([((x, y), 0)])
    visited = {(x, y)}
    while dq:
        cur, dist = dq.popleft()
        if cur == (0, 0):
            print(dist)
            break
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                dq.append((nxt, dist + 1))