import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

class SegmentTree:
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.dummy = 0
        if key == min:   self.dummy = float('inf')
        elif key == max: self.dummy = float('-inf')
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        self.build(l, start, mid)
        self.build(r, mid + 1, end)
        self.tree[node] = self.key(self.tree[l], self.tree[r])
    
    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return self.dummy
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        query_left = self.query(l, start, mid, left, right)
        query_right = self.query(r, mid + 1, end, left, right)
        return self.key(query_left, query_right)

    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        l = 2 * node
        r = 2 * node + 1
        self.update(l, start, mid, index, value)
        self.update(r, mid + 1, end, index, value)
        self.tree[node] = self.key(self.tree[l], self.tree[r])

N = int(input())
minTree = SegmentTree(g(), min)
for _ in range(int(input())):
    op, a, b = g()
    if op == 1:
        minTree.update(1, 1, N, a, b)
    else:
        print(minTree.query(1, 1, N, a, b))