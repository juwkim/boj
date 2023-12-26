import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import comb

M = int(input())
nums = g()
K = int(input())
cnt = 0
for num in nums:
    cnt += comb(num, K)
total = comb(sum(nums), K)
print(cnt / total)