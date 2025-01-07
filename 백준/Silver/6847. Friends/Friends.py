import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import deque

graph = [[] for _ in range(10000)]
for _ in range(int(input())):
    x, y = g()
    graph[x].append(y)
while (l:=g())[0]:
    x, y = l
    dist = 1e9
    dq = deque([(x, 0)])
    visited = set()
    while dq:
        cur, d = dq.popleft()
        for nxt in graph[cur]:
            if nxt == y:
                dist = d
                break
            if nxt in visited:
                continue
            visited.add(nxt)
            dq.append((nxt, d + 1))
        else:
            continue
        break
    if dist == 1e9:
        print("No")
    else:
        print("Yes", dist)