class DisjointSet:
    def __init__(self, nodes):
        self.parent = nodes
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root

def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda x: x[2])
    mst = []
    ds = DisjointSet(graph['nodes'])
    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            mst.append(edge)
            ds.union(u, v)
    return mst

input = __import__('sys').stdin.readline
from math import dist
g = lambda: [*map(float, input().split())]
graph = {'nodes': [], 'edges': []}
V = int(input())
graph['nodes'] = [*range(V)]
points = [g() for _ in range(V)]
for i in range(V - 1):
    for j in range(i + 1, V):
        graph['edges'].append((i, j, dist(points[i], points[j])))

mst = kruskal(graph)
weight = [edge[2] for edge in mst]
print(sum(weight))