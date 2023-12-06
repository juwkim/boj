import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

*nums, l = sorted(g())
ans = sum(num + 1000 >= l for num in nums)
print(ans)