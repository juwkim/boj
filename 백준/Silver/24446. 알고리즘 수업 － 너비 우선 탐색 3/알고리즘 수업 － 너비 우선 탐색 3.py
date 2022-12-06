g = lambda: [*map(int, input().split())]

from collections import deque
N, M, R = g()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = g()
    E[a].append(b)
    E[b].append(a)

visited = [0] * (N + 1)
ans = [-1] * (N + 1)

def bfs(R):
    ans[R] = 0
    
    visited[R] = 1
    dq = deque([(R, 1)])
    while dq:
        u, d = dq.popleft()
        for v in sorted(E[u]):
            if visited[v] == 0:
                ans[v] = d                
                visited[v] = 1
                dq.append((v, d + 1))
bfs(R)
print(*ans[1:])