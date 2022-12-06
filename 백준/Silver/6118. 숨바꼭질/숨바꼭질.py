g = lambda: [*map(int, input().split())]

from collections import deque
N, M = g()
graph = [[] for _ in range(1 + N)]
for _ in range(M):
    A, B = g()
    graph[A].append(B)
    graph[B].append(A)




dist = [0 for _ in range(1 + N)]
visited = [0 for _ in range(1 + N)]
visited[1] = 1
dq = deque([(1, 1)])
Max = 0
while dq:
    num, d = dq.popleft()
    for val in graph[num]:
        if visited[val] == 0:
            visited[val] = 1
            dist[val] = d
            dq.append((val, d + 1))
            Max = max(Max, d)

ans = []
for i in range(1, 1 + N):
    if dist[i] == Max:
        ans.append(i)
print(ans[0], Max, len(ans))