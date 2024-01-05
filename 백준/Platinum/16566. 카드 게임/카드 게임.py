import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect_left

N, M, K = g()
nums = sorted(g())
parent = [*range(N)]
rank = [0] * N

def find(x):
    p = x
    while p != parent[p]:
        p = parent[p]
    parent[x] = p
    return p

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for num in g():
    idx = find(bisect_left(nums, num + 1))
    print(nums[idx])
    parent[idx] = find(idx + 1)