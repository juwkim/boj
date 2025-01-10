import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
nums = [[*map(int, input().split())] for _ in range(int(input()))]
print(sum(all(l.index(x) < l.index(y) for x, y in nums) for l in permutations(range(1, n + 1))))