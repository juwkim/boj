import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import pairwise

while (l:=[*map(int, input().split())]) != [0, 0]:
    T, P = l
    d = [[0, 0, 0] for _ in range(T)] # solved, time, cnt
    for i in range(T):
        for s in input().split():
            a, b = s.split('/')
            if b == '-':
                continue
            d[i][0] += 1
            d[i][1] += int(b)
            d[i][2] += int(a) - 1
    nums = [[] for _ in range(P)]
    for solved, time, cnt in d:
        nums[solved - 1].append((time, cnt))
    lo, hi = 1, float('inf')
    for l in nums:
        if len(l) <= 1:
            continue
        l.sort(key=lambda x: x[0] + 20 * x[1])
        for (t1, c1), (t2, c2) in pairwise(l):
            if t1 == t2:
                pass
            elif t1 < t2:
                if c1 > c2:
                    time1 = t1 + 20 * c1
                    time2 = t2 + 20 * c2
                    if time1 == time2:
                        lo, hi = 20, 20
                    else:
                        hi = min(hi, 20 + (time2 - time1 - 1) // (c1 - c2))
            else:
                time1 = t1 + 20 * c1
                time2 = t2 + 20 * c2
                if time1 == time2:
                    lo, hi = 20, 20
                else:
                    lo = max(lo, 20 - (time2 - time1 - 1) // (c2 - c1))
    if hi == float('inf'):
        hi = '*'
    print(lo, hi)