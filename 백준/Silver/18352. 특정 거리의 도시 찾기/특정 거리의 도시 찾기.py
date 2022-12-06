import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

from collections import deque
N, M, K, X = g()
graph = [[] for _ in range(1 + N)]
for _ in range(M):
    A, B = g()
    graph[A].append(B)

visited = [0 for _ in range(1 + N)]
dq = deque([(X, 1)])
visited[X] = 1
ans = []
while dq:
    
    num, d = dq.popleft()
    for val in graph[num]:
        if visited[val] == 0:
            visited[val] = 1
            if d == K:
                ans.append(val)
            else:
                dq.append((val, d + 1))
if ans:
    print(*sorted(ans), sep='\n')
else:
    print(-1)