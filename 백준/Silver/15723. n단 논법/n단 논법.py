import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

graph = defaultdict(list)
for _ in range(int(input())):
    a, _, b = input().split()
    graph[a].append(b)
for _ in range(int(input())):
    s, _, e = input().split()
    ans = 'F'
    dq = deque([s])
    visited = set()
    visited.add(s)
    while dq:
        cur = dq.popleft()
        if cur == e:
            ans = 'T'
            break
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                dq.append(nxt)
    print(ans)