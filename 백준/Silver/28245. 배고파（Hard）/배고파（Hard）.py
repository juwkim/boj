import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect_left
dic = {}
for i in range(60):
    p = 1 << i
    for j in range(i, 61):
        q = 1 << j
        m = p + q
        dic[m] = (i, j)

nums = sorted(dic.keys())
for _ in range(int(input())):
    m = int(input())
    idx = bisect_left(nums, m)
    if idx == 0:
        num = 2
    else:
        num = min(nums[idx], nums[idx - 1], key=lambda x: (abs(x - m), x))
    print(*dic[num])