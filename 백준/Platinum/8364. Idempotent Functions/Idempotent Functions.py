mod = 1_000_000_007
import sys
input = sys.stdin.readline

from collections import Counter
from functools import reduce
g = lambda: [*map(int, input().split())]
N = int(input())
nums = Counter(g())
a = reduce(lambda x, y: x * y % mod, nums.values())
k = N - len(nums)
for i in range(1, 1 + k):
    a = a * i % mod
print(a)