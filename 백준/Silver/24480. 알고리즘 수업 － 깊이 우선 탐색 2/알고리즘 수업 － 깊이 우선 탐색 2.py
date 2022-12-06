g = lambda: [*map(int, input().split())]

import sys
sys.setrecursionlimit(10**5)
N, M, R = g()
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = g()
    E[a].append(b)
    E[b].append(a)

visited = [0] * (N + 1)
ans = [0] * (N + 1)
cnt = 1
def dfs(R):
    global cnt
    visited[R] = 1
    ans[R] = cnt
    cnt += 1
    for x in sorted(E[R], reverse=True):
        if visited[x] == 0:
            dfs(x)
dfs(R)    
print(*ans[1:])