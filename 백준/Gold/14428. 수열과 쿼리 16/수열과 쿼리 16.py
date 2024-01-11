import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [(0, 0)] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)
    
    def cmp(self, a, b):
        return min(a, b)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = (self.arr[start], start + 1)
            return
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        self.build(l, start, mid)
        self.build(r, mid + 1, end)
        self.tree[node] = self.cmp(self.tree[l], self.tree[r])
    
    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return (float('inf'), 0)
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        query_left = self.query(l, start, mid, left, right)
        query_right = self.query(r, mid + 1, end, left, right)
        return self.cmp(query_left, query_right)

    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        if start == end:
            self.tree[node] = (value, index)
            return
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        self.update(l, start, mid, index, value)
        self.update(r, mid + 1, end, index, value)
        self.tree[node] = self.cmp(self.tree[l], self.tree[r])

N = int(input())
minIndexTree = SegmentTree(g())
for _ in range(int(input())):
    op, a, b = g()
    if op == 1:
        minIndexTree.update(1, 1, N, a, b)
    else:
        k, v = minIndexTree.query(1, 1, N, a, b)
        print(v)