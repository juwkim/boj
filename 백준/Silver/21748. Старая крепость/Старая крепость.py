import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import sin, radians

n, r = g()
nums = sorted(g() for _ in range(n))
ans = 0
for i in range(n):
    a1, b1 = nums[i - 1]
    a2, b2 = nums[i]
    ans += radians((b1 - a1) % 360) + 2 * sin(radians((a2 - b1) % 360) / 2)
ans *= r
print(ans)