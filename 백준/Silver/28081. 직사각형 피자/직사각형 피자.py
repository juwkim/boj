import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from bisect import bisect

W, H, K = g()
N = int(input())
y = [0] + g() + [H]
nums = sorted(y[i+1] - y[i] for i in range(N + 1))
M = int(input())
x = [0] + g() + [W]
print(sum(bisect(nums, K // (x[i+1] - x[i])) for i in range(M + 1)))