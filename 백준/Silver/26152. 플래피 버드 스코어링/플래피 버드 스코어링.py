import sys
from bisect import bisect
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
nums = []
dist = 1e9
for A, B in zip(g(), g()):
    dist = min(dist, A - B)
    nums.append(-dist)
input()
for w in g():
    print(bisect(nums, -w))