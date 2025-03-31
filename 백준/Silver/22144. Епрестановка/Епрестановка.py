import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
p = [0] + [*map(int, input().split())]
group = [-1] * (n + 1)
id = 1
for i in range(1, n + 1):
    if group[i] != -1:
        continue
    nums, cur = [i], p[i]
    while cur != i:
        nums.append(cur)
        cur = p[cur]
    for num in nums:
        group[num] = id
    id += 1
if group[2] == 2:
    for i in range(1, n + 1):
        if group[i] == 2:
            group[i] = 1
for _ in range(m):
    a, b = map(int, input().split())
    print(("No", "Yes")[group[a] == group[b]])