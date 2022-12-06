from itertools import combinations
g = lambda: [*map(int, input().split())]
dist = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2

n = int(input())
nums = [g() for _ in range(n)]
x, y = min(combinations(range(n), 2), key=lambda x: dist(nums[x[0]], nums[x[1]]))
print(x + 1, y + 1)