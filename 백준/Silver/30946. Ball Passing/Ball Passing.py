import sys
input = sys.stdin.readline
from math import atan2, dist

N = int(input())
S = input()
nums = [[], []]
for i in range(N):
    nums[S[i] == 'B'].append([*map(int, input().split())])
ans = 0
for i in range(2):
    l = nums[i]
    if not l:
        continue
    p0 = min(l, key=lambda p: (p[1], p[0]))
    l.sort(key=lambda p: atan2(p[1] - p0[1], p[0] - p0[0]))
    for i in range(len(l)//2):
        ans += dist(l[i], l[i + len(l)//2])
print(ans)