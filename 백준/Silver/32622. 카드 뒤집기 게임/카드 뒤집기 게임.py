from itertools import pairwise

N = int(input())
ans, prev, cur = 0, 0, 1
for a, b in pairwise(input().split()):
    if a == b:
        cur += 1
    else:
        ans = max(ans, prev + cur)
        prev, cur = cur, 1
print(max(ans, prev + cur))