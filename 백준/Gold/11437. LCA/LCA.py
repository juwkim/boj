import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
g = lambda: map(int, input().split())
from functools import lru_cache

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
lca = [[0, 0] for _ in range(N + 1)] # parent, depth
visited = bytearray(N + 1)
visited[1] = 1
st = [(1, 0)]
while st:
    node, depth = st.pop()
    for child in graph[node]:
        if not visited[child]:
            visited[child] = 1
            lca[child][0] = node
            lca[child][1] = depth + 1
            st.append((child, depth + 1))

@lru_cache(None)
def solve(a, b):
    if lca[a][1] < lca[b][1]:
        return solve(b, a)
    if lca[a][1] > lca[b][1]:
        return solve(lca[a][0], b)
    if a != b:
        return solve(lca[a][0], lca[b][0])
    return a

for _ in range(int(input())):
    a, b = g()
    print(solve(a, b))