import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect_left

N, M, K = g()
nums = sorted(g())
parent = [*range(N)]

def find(x):
    p = x
    while p != parent[p]:
        p = parent[p]
    parent[x] = p
    return p

for num in g():
    idx = find(bisect_left(nums, num + 1))
    print(nums[idx])
    parent[idx] = find(idx + 1)