import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
graph = defaultdict(list)
for _ in range(N):
    u, *neighbors = input().split()
    graph[u] = neighbors
    for v in neighbors:
        graph[v].append(u)
s, e = input().split()
visited = {s}
def dfs(node, path):
    if node == e:
        print(*path)
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            if dfs(neighbor, path + [neighbor]):
                return True
            visited.remove(neighbor)
    return False
if not dfs(s, [s]):
    print("no route found")