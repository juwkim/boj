import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque([(1, 0)])
visited = bytearray(N + 1)
visited[1] = 1
ans = [0] * (N + 1)
while dq:
    node, cnt = dq.popleft()
    flag = True
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dq.append((next_node, cnt + 1))
            flag = False
    if flag:
        ans[node] = cnt
print(("No", "Yes")[sum(ans) & 1])