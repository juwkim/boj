import sys
input = sys.stdin.readline
from math import inf

n = int(input())
a = [-1] + [*map(int, input().split())]
right_min = [0] * (n + 1) + [inf]
left_max = [-1] + [0] * n
for i in range(1, n + 1):
    right_min[n - i + 1] = min(a[n - i + 1], right_min[n - i + 2])
    left_max[i] = max(a[i], left_max[i - 1])

ans = [i for i in range(1, n) if right_min[i + 1] > left_max[i]]
print(len(ans))
print(*ans)