import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n, e, *l, vx = input().split()
    n, e = map(int, (n, e))
    graph = [[] for _ in range(n + 1)]
    for i in range(0, 2 * e, 2):
        a, b = int(l[i][1:]), int(l[i + 1][1:])
        graph[a].append(b)
        graph[b].append(a)
    x = int(vx[1:])
    visited = bytearray(n + 1)
    visited[x] = 1
    dq, cnt = deque([(x, 0)]), -1
    while dq:
        cnt += 1
        cur, dist = dq.popleft()
        if dist == 2:
            continue
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = 1
                dq.append((i, dist + 1))
    print(f"The number of supervillains in 2-hop neighborhood of {vx} is {cnt}")