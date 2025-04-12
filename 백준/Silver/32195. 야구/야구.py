import sys
input = sys.stdin.readline
from bisect import bisect

nums, foul = [], 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if y >= x and y >= -x:
        nums.append(x * x + y * y)
    else:
        foul += 1
nums.sort()
for _ in range(int(input())):
    infield = bisect(nums, int(input())**2)
    homerun = len(nums) - infield
    print(foul, infield, homerun)