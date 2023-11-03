import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, m, k = g()
nums = sorted(g(), reverse=True)
print(sum(nums[:m + k]) * 100 / sum(nums))