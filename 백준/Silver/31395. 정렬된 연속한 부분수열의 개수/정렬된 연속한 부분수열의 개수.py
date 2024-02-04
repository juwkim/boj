import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import pairwise

input()
ans, cnt = 0, 1
for a, b in pairwise(map(int, input().split())):
    if a < b:
        cnt += 1
    else:
        ans += cnt * (cnt + 1)
        cnt = 1
ans += cnt * (cnt + 1)
print(ans >> 1)