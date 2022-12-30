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

import sys
sys.setrecursionlimit(10 ** 5)
input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

n, m = g()
ds = DisjointSet(list(range(n + 1)))
for _ in range(m):
    cmd, a, b = g()
    if cmd:
        print(['NO', 'YES'][ds.find(a) == ds.find(b)])
    else:
        ds.union(a, b)