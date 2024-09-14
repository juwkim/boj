import sys
sys.setrecursionlimit(10**6)

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

g = lambda: [*map(int, input().split())]
graph = {}
V, E = g()
graph['nodes'] = [*range(V + 1)]
graph['edges'] = [g() for _ in range(E)]

mst = kruskal(graph)
weight_sum = sum(edge[2] for edge in mst)
print(weight_sum)