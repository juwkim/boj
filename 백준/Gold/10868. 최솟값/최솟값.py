import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

class SegmentTree:
    def __init__(self, arr: list[int], key, dummy) -> None:
        self.arr = arr
        self.key = key
        self.dummy = dummy
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)
    
    def build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        l = 2 * node + 1
        r = 2 * node + 2
        self.build(l, start, mid)
        self.build(r, mid + 1, end)
        self.tree[node] = self.key(self.tree[l], self.tree[r])
    
    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or left > end:
            return self.dummy
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        l = 2 * node + 1
        r = 2 * node + 2
        query_left = self.query(l, start, mid, left, right)
        query_right = self.query(r, mid + 1, end, left, right)
        return self.key(query_left, query_right)

N, M = g()
nums = [int(input()) for _ in range(N)]
minTree = SegmentTree(nums, min, float('inf'))
for _ in range(M):
    a, b = g()
    print(minTree.query(0, 0, N - 1, a - 1, b - 1))