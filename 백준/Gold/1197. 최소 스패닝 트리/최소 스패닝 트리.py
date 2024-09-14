class DisjointSet:
    def __init__(self, nodes):
        self.parent = nodes
        self.rank = [0] * len(nodes)  # Initialize rank array
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            # Union by rank
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1  # Increase rank if both have the same rank

def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda x: x[2])  # Sort edges by weight
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