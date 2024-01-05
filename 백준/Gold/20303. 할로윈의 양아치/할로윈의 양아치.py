import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
candy = [0] + g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
nums = []
for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = True
    stack = [i]
    collected, cried = candy[i], 1
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            collected += candy[nxt]
            cried += 1
            visited[nxt] = True
            stack.append(nxt)
    if cried < K:
        nums.append((cried, collected))

dp = [[0] * K for _ in range(len(nums) + 1)]

for idx, (w, v) in enumerate(nums, 1):
    for i in range(w):
        dp[idx][i] = dp[idx - 1][i]
    for i in range(w, K):
        dp[idx][i] = max(dp[idx - 1][i], dp[idx - 1][i - w] + v)
print(dp[-1][-1])