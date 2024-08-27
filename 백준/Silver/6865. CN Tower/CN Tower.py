import sys
input = sys.stdin.readline
from itertools import pairwise

nums = sorted(float(input().split()[1]) for _ in range(int(input())))
d = min(nums[-1] - nums[0], *[360 - (b - a) for a, b in pairwise(nums)])
print(int((4320 * d + 359)// 360))