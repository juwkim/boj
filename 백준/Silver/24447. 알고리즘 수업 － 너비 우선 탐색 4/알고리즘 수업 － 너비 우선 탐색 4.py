g = lambda: [*map(int, input().split())]

from collections import deque
N, M, R = g()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = g()
    E[a].append(b)
    E[b].append(a)

visited = [0] * (N + 1)
ans = 0
def bfs(R):
    global ans
    cnt = 1
    visited[R] = 1
    dq = deque([(R, 1)])
    while dq:
        u, d = dq.popleft()
        for v in sorted(E[u]):
            if visited[v] == 0:
                cnt += 1
                ans += d * cnt
                visited[v] = 1
                dq.append((v, d + 1))

bfs(R)
print(ans)