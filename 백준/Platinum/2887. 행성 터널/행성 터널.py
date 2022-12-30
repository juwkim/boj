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

dist = lambda a, b: abs(a - b)
g = lambda: [*map(int, input().split())]
graph = {'nodes': [], 'edges': []}
V = int(input())
points = [[idx] + g() for idx in range(V)]
graph['nodes'] = [*range(V)]

for k in range(1, 4):
    points.sort(key=lambda x: x[k])
    for i in range(V - 1):
        graph['edges'].append((points[i][0], points[i + 1][0], dist(points[i][k], points[i + 1][k])))

mst = kruskal(graph)
weight = [edge[2] for edge in mst]
print(sum(weight))