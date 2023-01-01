import sys
sys.setrecursionlimit(10 ** 5)
input = __import__('sys').stdin.readline

def g(): return tuple(map(int, input().split()))

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    node, *l, _ = g()
    for i in range(0, len(l), 2):
        graph[node].append((l[i], l[i + 1]))

def dfs(node, dist):
    global max_dist, endnode
    if dist > max_dist:
        max_dist = dist
        endnode = node
    visited[node] = 1
    for neighbor, weight in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, dist + weight)

endnode, max_dist, visited = 1, 0, bytearray(n + 1)
dfs(endnode, 0)

max_dist, visited = 0, bytearray(n + 1)
dfs(endnode, 0)
print(max_dist)