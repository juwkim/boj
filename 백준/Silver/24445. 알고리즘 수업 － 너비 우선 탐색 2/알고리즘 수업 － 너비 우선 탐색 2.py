g = lambda: [*map(int, input().split())]

from collections import deque
N, M, R = g()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = g()
    E[a].append(b)
    E[b].append(a)

visited = [0] * (N + 1)
ans = [0] * (N + 1)

def bfs(R):
    cnt = 1
    ans[R] = cnt
    
    visited[R] = 1
    dq = deque([R])
    while dq:
        u = dq.popleft()
        for v in sorted(E[u], reverse=True):
            if visited[v] == 0:
                cnt += 1
                ans[v] = cnt
                
                visited[v] = 1
                dq.append(v)

bfs(R)
print(*ans[1:])