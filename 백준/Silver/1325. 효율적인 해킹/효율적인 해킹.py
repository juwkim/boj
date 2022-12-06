from collections import deque, defaultdict
import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = g()
    graph[B].append(A)

ans = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    cnt = 0
    dq = deque([i])
    visited = bytearray(N + 1)
    visited[i] = 1
    while dq:
        cnt += 1
        num = dq.popleft()
        visited[num] = 1
        for j in graph[num]:
            if visited[j] == 0:
                visited[j] = 1
                dq.append(j)
    ans[i] = cnt

Max = max(ans)
for i in range(1, N + 1):
    if Max == ans[i]:
        print(i, end=' ')