import sys
sys.setrecursionlimit(10**5)
g = lambda: [*map(int, input().split())]


N = int(input())
buf = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = g()
    buf[a].append(b)
    buf[b].append(a)

ans = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
def dfs(idx):
    visited[idx] = 1
    for num in buf[idx]:
        if visited[num] == 0:
            ans[num] = idx
            dfs(num)

dfs(1)
print(*ans[2:])